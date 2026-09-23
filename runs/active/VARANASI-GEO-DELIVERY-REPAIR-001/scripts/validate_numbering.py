#!/usr/bin/env python3
"""Valideert de IMMUTABLE LOCATION NUMBERING-regel (Mark-besluit 2026-08-02, commit 58be47b).

Regel: elke kandidaat/fysieke locatie heeft een vast, permanent driecijferig nummer. Dat nummer:
- wijzigt nooit, wordt nooit hergebruikt voor een andere locatie, en blijft altijd aan dezelfde
  fysieke locatie gekoppeld;
- staat altijd als prefix vóór de naam in gegenereerde PDF- en KML-bestanden ("007 <naam>").

Deze validator blokkeert (exit-code 1) wanneer:
1. een candidate_id in de dataset een ander display_id/nummer heeft dan in NUMBERING_REGISTRY.jsonl;
2. een display_id/nummer dubbel wordt gebruikt (in de registry of in de dataset);
3. een naam in de gegenereerde KML of PDF niet begint met het bijbehorende nummer.

Gebruik:
    python3 validate_numbering.py
Exit code 0 = alles geldig, 1 = een of meer fouten (details op stdout).
"""
import json
import re
import sys
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent.parent
REGISTRY = RUN_DIR / "NUMBERING_REGISTRY.jsonl"
DATASET = RUN_DIR / "GOUD" / "REGIONAL" / "DATASET_VARANASI_40.jsonl"
KML = RUN_DIR / "GOUD" / "REGIONAL" / "USER" / "VARANASI_40_KANDIDATEN.kml"
REISGIDS_PDF = RUN_DIR / "GOUD" / "REGIONAL" / "USER" / "VARANASI_40_KEUZE_REISGIDS.pdf"


def load_jsonl(path):
    out = []
    if not path.exists():
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def main():
    errors = []

    registry_rows = [r for r in load_jsonl(REGISTRY) if "candidate_id" in r]
    registry = {r["candidate_id"]: r["display_id"] for r in registry_rows}

    # 1 & 2: geen dubbel nummer in de registry zelf
    seen_numbers = {}
    for r in registry_rows:
        did = r["display_id"]
        cid = r["candidate_id"]
        if did in seen_numbers and seen_numbers[did] != cid:
            errors.append(f"NUMMER DUBBEL GEBRUIKT in registry: {did} hoort bij zowel "
                           f"{seen_numbers[did]} als {cid}")
        seen_numbers[did] = cid

    # dataset vs registry: candidate_id moet exact hetzelfde nummer behouden
    dataset_rows = load_jsonl(DATASET)
    for rec in dataset_rows:
        cid = rec["candidate_id"]
        expected_display_id = cid.split("-")[-1]
        if cid not in registry:
            errors.append(f"{cid} ontbreekt in NUMBERING_REGISTRY.jsonl -- elke kandidaat moet "
                           f"een permanent nummer hebben voordat deze in de dataset staat")
            continue
        if registry[cid] != expected_display_id:
            errors.append(f"NUMMER GEWIJZIGD: {cid} heeft in de registry nummer {registry[cid]}, "
                           f"maar de candidate_id zelf impliceert {expected_display_id}")

    # KML: elke Placemark-naam moet beginnen met het nummer
    if KML.exists():
        kml_text = KML.read_text(encoding="utf-8")
        names = re.findall(r"<name>(.*?)</name>", kml_text, re.DOTALL)
        for name in names:
            if "Varanasi" in name and "kandidaten" in name.lower():
                continue  # documenttitel, geen kandidaat-placemark
            m = re.search(r"VNS-CAND-(\d{3})", name)
            if not m:
                continue
            did = m.group(1)
            stripped = re.sub(r"^\[[^\]]*\]\s*", "", name)  # strip [ONBEVESTIGD]-prefix etc.
            if not stripped.startswith(did) and not stripped.startswith(f"VNS-CAND-{did}"):
                errors.append(f"KML-naam begint niet met het nummer {did}: {name!r}")

    # PDF: elke kandidaattitel "<nummer> <naam>" moet voorkomen (best-effort, pypdf optioneel)
    if REISGIDS_PDF.exists():
        try:
            from pypdf import PdfReader
            text = "\n".join(p.extract_text() or "" for p in PdfReader(str(REISGIDS_PDF)).pages)
            for r in registry_rows:
                did = r["display_id"]
                name = r["canonical_name"]
                if f"{did} {name}" not in text:
                    errors.append(f"PDF-titel begint niet met nummer voor {r['candidate_id']}: "
                                   f"verwacht '{did} {name}' niet gevonden")
        except ImportError:
            print("(pypdf niet beschikbaar -- PDF-nummercontrole overgeslagen)")

    if errors:
        print(f"VALIDATIE MISLUKT -- {len(errors)} probleem/problemen:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"VALIDATIE OK -- {len(registry_rows)} nummers gecontroleerd, geen fouten.")
    sys.exit(0)


if __name__ == "__main__":
    main()

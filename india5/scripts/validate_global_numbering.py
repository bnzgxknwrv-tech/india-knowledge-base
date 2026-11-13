#!/usr/bin/env python3
"""Globale, repositorybrede nummeringsvalidator (INDIA5-ARCH-HARDEN-002).

Vanaf de tweede regio moet gegarandeerd worden dat een display_id (het permanente,
driecijferige locatienummer) NOOIT in twee verschillende regio's aan een andere fysieke
locatie hangt. Tot nu toe bestond alleen een PER-REGIO validator
(runs/active/<run_id>/scripts/validate_numbering.py). Dit script is de repositorybrede
opvolger: het scant ALLE `NUMBERING_REGISTRY.jsonl`-bestanden onder `runs/*/`, en:

1. controleert dat elk display_id repositorybreed hoogstens één candidate_id/region heeft;
2. controleert dat een candidate_id nooit met een ander display_id in een andere registry
   voorkomt (immutable, ook over regio's heen);
3. rapporteert per regio het gereserveerde/gebruikte nummerbereik, zodat een nieuwe regio
   vooraf een niet-overlappend bereik kan reserveren (conform INDIA5-PROTOCOL.md, Immutable
   Location Numbering: "een toekomstige nummerreeks per regio/cluster mag uitsluitend vooraf
   worden gereserveerd en mag bestaande nummers nooit veranderen").

Dit script is PUUR LEZEND -- het wijzigt of raakt geen enkel bestaand registrybestand aan,
dus ook niet de bestaande Varanasi-nummers 001-040.

Gebruik:
    python3 india5/scripts/validate_global_numbering.py
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def load_jsonl(path: Path):
    out = []
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
    registries = sorted(REPO_ROOT.glob("runs/*/*/NUMBERING_REGISTRY.jsonl")) + \
        sorted(REPO_ROOT.glob("runs/*/NUMBERING_REGISTRY.jsonl"))
    registries = sorted(set(registries))

    if not registries:
        print("VALIDATIE OK -- geen enkele NUMBERING_REGISTRY.jsonl gevonden, niets te controleren.")
        sys.exit(0)

    errors = []
    display_id_owner = {}  # display_id -> (region, candidate_id)
    candidate_id_display = {}  # candidate_id -> (region, display_id)
    per_region_range = {}  # region -> (min_id, max_id, count)

    for registry_path in registries:
        rows = [r for r in load_jsonl(registry_path) if "candidate_id" in r]
        region = rows[0].get("region") if rows else registry_path.parent.name

        ids_this_region = []
        for r in rows:
            cid = r["candidate_id"]
            did = r["display_id"]
            ids_this_region.append(did)

            if did in display_id_owner and display_id_owner[did] != (region, cid):
                errors.append(
                    f"display_id {did!r} DUBBEL GEBRUIKT over regio's heen: "
                    f"{display_id_owner[did]} vs. ({region}, {cid}) [{registry_path}]"
                )
            display_id_owner.setdefault(did, (region, cid))

            if cid in candidate_id_display and candidate_id_display[cid][1] != did:
                errors.append(
                    f"candidate_id {cid!r} heeft VERSCHILLENDE nummers in verschillende "
                    f"registries: {candidate_id_display[cid]} vs. ({region}, {did}) "
                    f"[{registry_path}]"
                )
            candidate_id_display.setdefault(cid, (region, did))

        if ids_this_region:
            nums = sorted(int(x) for x in ids_this_region if x.isdigit())
            if nums:
                per_region_range[region] = (min(nums), max(nums), len(nums))

    print(f"Gescand: {len(registries)} registrybestand(en), "
          f"{len(display_id_owner)} uniek(e) display_id('s) over {len(per_region_range)} regio('s).\n")
    print("Bereik per regio (voor toekomstige reservering van een niet-overlappend bereik):")
    for region, (lo, hi, count) in sorted(per_region_range.items()):
        print(f"  - {region}: {lo:03d}-{hi:03d} ({count} nummers)")

    if errors:
        print(f"\nVALIDATIE MISLUKT -- {len(errors)} probleem/problemen:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\nVALIDATIE OK -- geen enkel nummer wordt over regio's heen dubbel of gewijzigd gebruikt.")
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Valideert india4/registries/DETECTOR_LIBRARY.jsonl (INDIA2-architectuurbesluit, 2026-08-02).

Regel: elke detector heeft een immutable detector_id, een geldige status
(PROVISIONAL/ACTIVE/RETIRED) en, indien parent_detector_id gezet is, verwijst dat naar een
bestaande detector_id in dezelfde bibliotheek.

Deze validator blokkeert (exit-code 1) wanneer:
1. een detector_id dubbel voorkomt;
2. een verplicht veld ontbreekt;
3. status geen geldige waarde heeft;
4. parent_detector_id verwijst naar een niet-bestaande detector_id;
5. een detector met status ACTIVE of RETIRED geen approved_by heeft (canonieke status vereist
   goedkeuring door INDIA2/ChatGPT als architect).

Gebruik:
    python3 india4/scripts/validate_detector_library.py
Exit code 0 = alles geldig, 1 = een of meer fouten (details op stdout).
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
LIBRARY = REPO_ROOT / "india4" / "registries" / "DETECTOR_LIBRARY.jsonl"

REQUIRED_FIELDS = [
    "detector_id", "name", "definition", "purpose", "trigger_conditions",
    "exclusion_conditions", "required_source_families", "applicability_facets",
    "discovered_in_run", "status", "created_at",
]
VALID_STATUS = {"PROVISIONAL", "ACTIVE", "RETIRED"}


def load_jsonl(path):
    out = []
    if not path.exists():
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def main():
    rows = load_jsonl(LIBRARY)
    detectors = [r for r in rows if "detector_id" in r]
    errors = []

    seen_ids = {}
    for d in detectors:
        did = d["detector_id"]
        if did in seen_ids:
            errors.append(f"detector_id DUBBEL: {did}")
        seen_ids[did] = d

    for d in detectors:
        did = d.get("detector_id", "<geen id>")
        missing = [f for f in REQUIRED_FIELDS if f not in d]
        if missing:
            errors.append(f"{did}: ontbrekende verplichte velden: {missing}")

        status = d.get("status")
        if status not in VALID_STATUS:
            errors.append(f"{did}: ongeldige status {status!r}, verwacht een van {VALID_STATUS}")

        parent = d.get("parent_detector_id")
        if parent and parent not in seen_ids:
            errors.append(f"{did}: parent_detector_id {parent!r} verwijst naar onbekende detector")

        if status in ("ACTIVE", "RETIRED") and not d.get("approved_by"):
            errors.append(f"{did}: status {status} vereist approved_by (canonieke wijziging, "
                           f"uitsluitend door INDIA2/ChatGPT als architect)")

    if errors:
        print(f"VALIDATIE MISLUKT -- {len(errors)} probleem/problemen:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"VALIDATIE OK -- {len(detectors)} detectoren gecontroleerd, geen fouten.")
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Valideert of een REGION_CONTENT_BRIEF.json intern consistent is (INDIA2-besluit 2026-08-02).

BRONS mag pas starten nadat deze validator geen fouten meldt. Zie
india4/templates/PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md voor de volledige toelichting per
veld.

Blokkeert (exit-code 1) wanneer:
1. een verplicht veld ontbreekt of leeg is;
2. `dramatic_miss_check` leeg is of alleen "geen"/"none" bevat zonder toelichting;
3. een bronfamilie in `planned_source_families` niet aan minstens één detector is gekoppeld.

Gebruik:
    python3 india4/scripts/validate_pre_brons_brief.py <pad naar REGION_CONTENT_BRIEF.json>
"""
import json
import sys
from pathlib import Path

# Velden die altijd aanwezig EN niet-leeg moeten zijn.
REQUIRED_NONEMPTY_FIELDS = [
    "region", "run_id", "area_definition", "mark_known_interests", "mark_known_anchors",
    "relevant_traditions", "known_risks_blind_spots", "expected_candidate_categories",
    "saturation_and_stop_criteria", "dramatic_miss_check", "written_at", "written_by",
]

# Velden die aanwezig moeten zijn (als sleutel), maar bij vroege regio's (nog geen ACTIVE
# detectoren in de bibliotheek) legitiem een lege lijst mogen zijn.
REQUIRED_PRESENT_FIELDS = ["active_detectors_applied", "planned_source_families"]

# provisional_detectors_introduced mag alleen leeg zijn als active_detectors_applied niet leeg is
# (een sweep moet altijd op minstens één detector -- ACTIVE of PROVISIONAL -- kunnen steunen).
PROVISIONAL_FIELD = "provisional_detectors_introduced"

TRIVIAL_ANSWERS = {"geen", "none", "n/a", "-", ""}


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python3 validate_pre_brons_brief.py <pad naar REGION_CONTENT_BRIEF.json>")
        sys.exit(2)

    brief_path = Path(sys.argv[1])
    if not brief_path.exists():
        print(f"Bestand niet gevonden: {brief_path}")
        sys.exit(1)

    brief = json.loads(brief_path.read_text(encoding="utf-8"))
    errors = []

    for field in REQUIRED_NONEMPTY_FIELDS:
        value = brief.get(field)
        if value is None or value == "" or value == [] or value == {}:
            errors.append(f"verplicht veld ontbreekt of is leeg: {field}")

    for field in REQUIRED_PRESENT_FIELDS:
        if field not in brief:
            errors.append(f"verplicht veld ontbreekt (mag leeg zijn, maar moet aanwezig zijn): {field}")

    if not brief.get("active_detectors_applied") and not brief.get(PROVISIONAL_FIELD):
        errors.append(
            "geen enkele detector (ACTIVE of PROVISIONAL) is toegepast -- een sweep moet op "
            "minstens één detector steunen, ook bij een nog jonge bibliotheek"
        )

    dmc = str(brief.get("dramatic_miss_check", "")).strip().lower()
    if dmc in TRIVIAL_ANSWERS:
        errors.append(
            "dramatic_miss_check is leeg of triviaal (bv. 'geen') zonder toelichting -- "
            "vereist een concreet, beargumenteerd antwoord op de vraag welke dramatisch te "
            "missen A-locatie dit plan nog zou kunnen missen"
        )

    detector_ids = set()
    for d in brief.get("active_detectors_applied", []):
        if isinstance(d, dict) and "detector_id" in d:
            detector_ids.add(d["detector_id"])
    for d in brief.get("provisional_detectors_introduced", []):
        if isinstance(d, dict) and "detector_id" in d:
            detector_ids.add(d["detector_id"])

    for sf in brief.get("planned_source_families", []):
        if isinstance(sf, dict):
            linked = sf.get("detector_id") or sf.get("linked_detector_ids")
            if not linked:
                errors.append(f"bronfamilie zonder gekoppelde detector: {sf}")
            elif isinstance(linked, list):
                unknown = [d for d in linked if d not in detector_ids]
                if unknown:
                    errors.append(f"bronfamilie {sf} verwijst naar onbekende detector(en): {unknown}")
            elif linked not in detector_ids:
                errors.append(f"bronfamilie {sf} verwijst naar onbekende detector: {linked}")

    if errors:
        print(f"VALIDATIE MISLUKT -- brief NIET intern consistent, BRONS mag nog niet starten "
              f"({len(errors)} probleem/problemen):\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("VALIDATIE OK -- REGION_CONTENT_BRIEF.json is intern consistent, BRONS mag starten.")
    sys.exit(0)


if __name__ == "__main__":
    main()

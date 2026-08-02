#!/usr/bin/env python3
"""Valideert een KNOWLEDGE_GATE_REVIEW.json tegen india5/schemas/knowledge_gate.schema.json.

Gebruik:
    python3 india5/scripts/validate_knowledge_gate.py <pad naar KNOWLEDGE_GATE_REVIEW.json>
"""
import json
import sys
from pathlib import Path

REQUIRED_TOP = ["gate_id", "reviewed_at", "reviewed_by", "items", "overall_verdict"]
REQUIRED_ITEM = ["topic", "verdict", "evidence_path", "notes"]
VALID_ITEM_VERDICTS = {"PASS", "FAIL", "PARTIAL", "NOT_APPLICABLE"}
VALID_OVERALL = {"READY", "NOT_READY", "READY_WITH_CONDITIONS"}

MIN_TOPICS = {
    "Mark's A/B/C-filosofie", "Immutable numbering", "Bestaande kandidatenlijst",
    "Accommodatie-/hotelbesluiten", "Discovery versus GEO-verificatie",
    "Detectorbibliotheek-governance", "Kandidaat-inflatie / differentiatietoets",
    "Koepelkandidaat versus deelsite", "Betekenis vóór GEO",
    "Geen stilzwijgende keuze / escalatieregels", "Saturation/coverage-bewijs",
    "Taakarchitectuur zelf",
}


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python3 validate_knowledge_gate.py <pad naar KNOWLEDGE_GATE_REVIEW.json>")
        sys.exit(2)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Bestand niet gevonden: {path}")
        sys.exit(1)

    review = json.loads(path.read_text(encoding="utf-8"))
    errors = []

    missing_top = [f for f in REQUIRED_TOP if f not in review]
    if missing_top:
        errors.append(f"ontbrekende verplichte velden: {missing_top}")

    for item in review.get("items", []):
        missing = [f for f in REQUIRED_ITEM if f not in item]
        if missing:
            errors.append(f"item {item.get('topic', '<onbekend>')!r} mist velden: {missing}")
        if item.get("verdict") not in VALID_ITEM_VERDICTS:
            errors.append(f"item {item.get('topic')!r}: ongeldig verdict {item.get('verdict')!r}")

    covered_topics = {item.get("topic") for item in review.get("items", [])}
    # losse (niet-strikte) dekkingscontrole: elk minimumonderwerp moet als substring in minstens
    # één item-topic voorkomen, zodat lichte tekstvariaties niet onnodig blokkeren
    missing_topics = [
        t for t in MIN_TOPICS
        if not any(t.split(" / ")[0].split(" versus")[0][:15].lower() in (ct or "").lower()
                   for ct in covered_topics)
    ]
    if missing_topics:
        errors.append(f"vaste onderwerpenlijst niet volledig gedekt, ontbreekt (indicatief): {missing_topics}")

    if review.get("overall_verdict") not in VALID_OVERALL:
        errors.append(f"ongeldig overall_verdict: {review.get('overall_verdict')!r}")

    if review.get("overall_verdict") == "READY_WITH_CONDITIONS" and not review.get("conditions"):
        errors.append("overall_verdict is READY_WITH_CONDITIONS maar conditions is leeg")

    if errors:
        print(f"VALIDATIE MISLUKT -- {len(errors)} probleem/problemen:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"VALIDATIE OK -- {len(review.get('items', []))} onderwerpen gecontroleerd, geen fouten.")
    sys.exit(0)


if __name__ == "__main__":
    main()

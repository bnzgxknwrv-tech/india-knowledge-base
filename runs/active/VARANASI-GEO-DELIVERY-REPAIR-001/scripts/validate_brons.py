#!/usr/bin/env python3
"""Valideer alle BRONS-B0X.jsonl-records tegen het bestaande schema en de
protocolregels (GEO.md, RUN.yaml explicit_rejections). Draai dit als poort
NA elke batch, voordat een run als voltooid gemeld wordt.

Gebruik:
    python3 validate_brons.py
Exit code 0 = alles geldig, 1 = een of meer fouten (details op stdout).
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

RUN_DIR = Path(__file__).resolve().parent.parent
BRONS_DIR = RUN_DIR / "BRONS"
RUN_YAML = RUN_DIR / "RUN.yaml"

REQUIRED_FIELDS = [
    "candidate_id", "canonical_name", "protected_mark_status",
    "research_status", "geo_status", "final_latitude", "final_longitude",
    "evidence", "reason", "checked_at",
]

ALLOWED_GEO_STATUS = {
    "VERIFIED_GOOGLE_MAPS_PLACE", "VERIFIED_OFFICIAL_MAP_LINK",
    "VERIFIED_SITE_CENTRE", "WORKING_CROSSCHECKED_MAP_POINT",
    "APPROXIMATE_LOCAL_POINT", "NOT_ESTABLISHED", "TOOL_LIMITED",
    "EXACT_GOOGLE_MAPS_MARKER", "GOOGLE_MAPS_MARKER_NOT_CONFIRMED",
}


def load_explicit_rejections():
    if not yaml or not RUN_YAML.exists():
        return []
    with open(RUN_YAML, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("explicit_rejections", []) or []


def main():
    errors = []
    seen_ids = {}
    rejections = load_explicit_rejections()

    for brons_file in sorted(BRONS_DIR.glob("BRONS-B*.jsonl")):
        with open(brons_file, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError as e:
                    errors.append(f"{brons_file.name}:{lineno} ongeldige JSON: {e}")
                    continue

                cid = rec.get("candidate_id", f"<onbekend regel {lineno}>")

                for field in REQUIRED_FIELDS:
                    if field not in rec:
                        errors.append(f"{brons_file.name}:{cid} mist verplicht veld '{field}'")

                if cid in seen_ids:
                    errors.append(
                        f"{brons_file.name}:{cid} is een DUPLICAAT "
                        f"(eerder in {seen_ids[cid]})"
                    )
                else:
                    seen_ids[cid] = brons_file.name

                geo_status = rec.get("geo_status")
                if geo_status and geo_status not in ALLOWED_GEO_STATUS:
                    errors.append(
                        f"{brons_file.name}:{cid} onbekende geo_status '{geo_status}'"
                    )

                lat, lon = rec.get("final_latitude"), rec.get("final_longitude")
                for rej in rejections:
                    if rej.get("candidate_id") == cid and lat is not None and lon is not None:
                        rlat, rlon = rej.get("coordinate", [None, None])
                        if abs(lat - rlat) < 1e-6 and abs(lon - rlon) < 1e-6:
                            errors.append(
                                f"{brons_file.name}:{cid} gebruikt een EXPLICIET AFGEWEZEN "
                                f"coordinaat {rej.get('coordinate')} -- regel: "
                                f"{rej.get('rule')}"
                            )

    if errors:
        print(f"VALIDATIE MISLUKT -- {len(errors)} probleem/problemen:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"VALIDATIE OK -- {len(seen_ids)} records gecontroleerd, geen fouten.")
    sys.exit(0)


if __name__ == "__main__":
    main()

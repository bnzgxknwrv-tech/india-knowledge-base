#!/usr/bin/env python3
"""Bepaal live welke VNS-CAND-* nog verwerkt moeten worden.

Bron van waarheid: de data zelf. Geen enkel apart status-/progress-bestand
wordt vertrouwd (dat was de hoofdoorzaak van het vastlopen -- zie ROOT_CAUSE.md).

Gebruik:
    python3 next_candidate.py                 -> print status + volgende kandidaat
    python3 next_candidate.py --range 22 40    -> beperk tot een candidate-ID-bereik
    python3 next_candidate.py --json           -> machine-leesbare output
"""
import argparse
import json
import sys
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent.parent
INPUT_CANDIDATES = RUN_DIR / "INPUT" / "candidates.jsonl"
BRONS_DIR = RUN_DIR / "BRONS"


def load_ids(path):
    ids = []
    if not path.exists():
        return ids
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            cid = rec.get("candidate_id")
            if cid:
                ids.append(cid)
    return ids


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--range", nargs=2, type=int, metavar=("START", "END"),
                         help="beperk tot VNS-CAND-<START> t/m VNS-CAND-<END>")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    all_ids = load_ids(INPUT_CANDIDATES)
    if args.range:
        start, end = args.range
        all_ids = [c for c in all_ids
                   if start <= int(c.split("-")[-1]) <= end]

    done = set()
    for brons_file in sorted(BRONS_DIR.glob("BRONS-B*.jsonl")):
        done.update(load_ids(brons_file))

    remaining = [c for c in all_ids if c not in done]

    result = {
        "total_in_scope": len(all_ids),
        "done": sorted(done & set(all_ids)),
        "done_count": len(done & set(all_ids)),
        "remaining": remaining,
        "remaining_count": len(remaining),
        "next_candidate": remaining[0] if remaining else None,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"In scope: {result['total_in_scope']}")
        print(f"Al verwerkt: {result['done_count']}")
        print(f"Nog te doen: {result['remaining_count']}")
        print(f"Volgende kandidaat: {result['next_candidate']}")
        if result["remaining"]:
            print("Resterend bereik: " + ", ".join(result["remaining"]))

    sys.exit(0 if not args.range or remaining or not all_ids else 1)


if __name__ == "__main__":
    main()

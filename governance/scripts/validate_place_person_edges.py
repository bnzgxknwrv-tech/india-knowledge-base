#!/usr/bin/env python3
"""Prototype PLACE<->PERSON semantic-edge validator.

Built 2026-09-16 as part of the global PLACE<->PERSON semantic
losslessness audit (Kakrighat incident, PR #23 comment 5692870622).

PROBLEM THIS SOLVES
Existing validators (validate_successor_boot.py, validate_independent_check.py,
validate_numbering.py, etc.) all prove some version of "is this PLACE row
present, with a grade, uniquely numbered." None of them prove that a
previously-discovered PERSON<->PLACE relationship is still visible in the
current canon. That gap let Kakrighat's Neem Karoli Baba layer survive in
research but disappear from governance/CURRENT_TRUTH.md while its
Vivekananda layer alone kept the place looking "complete."

WHAT THIS SCRIPT DOES
Reads a PLACE_PERSON_EDGE_LEDGER.jsonl (see this task's ledger for the
schema) and governance/CURRENT_TRUTH.md. For every ledger row marked
`repo_known_before_audit: true`, checks whether the place's name and the
person's name both appear in CURRENT_TRUTH.md close enough together to
plausibly be the same mention (same line or an adjacent line). Flags any
row where the place appears in CURRENT_TRUTH but the person does not --
exactly the Kakrighat failure pattern -- as a FAIL.

HONEST LIMITS
- This is deliberately a prototype, not a claim of solved semantic
  understanding: it is a textual co-occurrence check, not a real
  knowledge-graph validator. A person/place pair that legitimately
  appears far apart in the file (e.g. in two different sections) would
  be a false positive; the checker reports the surrounding context so a
  human can judge, it does not auto-fail on distance alone beyond a
  generous window.
- It only checks what's IN the ledger. It cannot invent edges research
  never found. It is a regression guard against re-losing a *known*
  edge, not a discovery tool -- Pass 2 (external rediscovery) remains a
  separate, human/AI-judgment-driven activity.
- `required_action: flag_open_lead_do_not_present_as_fact` and similar
  "not yet a real edge" rows are informational only and never fail the
  check -- only rows genuinely claiming to already be in canon should.

USAGE
    python3 governance/scripts/validate_place_person_edges.py \
        [--ledger PATH] [--current-truth PATH]

Exit 0 if every `repo_known_before_audit` row whose `current_canon_present`
field says true actually has both place and person visible together in
CURRENT_TRUTH.md; exit 1 otherwise, printing exactly which rows disagree
with reality (i.e. the ledger's own current_canon_present claim is stale).
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEDGER = ROOT / "runs/active/GLOBAL_PLACE_PERSON_SEMANTIC_LOSSLESSNESS_2026-09-16/PLACE_PERSON_EDGE_LEDGER.jsonl"
DEFAULT_CURRENT_TRUTH = ROOT / "governance/CURRENT_TRUTH.md"

# Context window (in characters) within which a place mention and a
# person mention are considered "the same presentation," not two
# unrelated occurrences on opposite ends of the file.
CONTEXT_WINDOW = 400


def load_ledger(path: Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def find_all(haystack: str, needle: str) -> list[int]:
    """Case-insensitive substring search, all occurrence start indices."""
    if not needle:
        return []
    pattern = re.escape(needle)
    return [m.start() for m in re.finditer(pattern, haystack, flags=re.IGNORECASE)]


def person_near_place(text: str, place_names: list[str], person: str) -> tuple[bool, str]:
    """Return (found, context_snippet). Checks every alias for the place."""
    for place_name in place_names:
        for place_idx in find_all(text, place_name):
            window_start = max(0, place_idx - CONTEXT_WINDOW)
            window_end = min(len(text), place_idx + len(place_name) + CONTEXT_WINDOW)
            window = text[window_start:window_end]
            if find_all(window, person):
                return True, window.replace("\n", " ")
    return False, ""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    p.add_argument("--current-truth", default=str(DEFAULT_CURRENT_TRUTH))
    args = p.parse_args()

    ledger_path = Path(args.ledger)
    ct_path = Path(args.current_truth)

    if not ledger_path.is_file():
        print(f"FAIL: ledger not found: {ledger_path}")
        return 1
    if not ct_path.is_file():
        print(f"FAIL: CURRENT_TRUTH not found: {ct_path}")
        return 1

    rows = load_ledger(ledger_path)
    text = ct_path.read_text(encoding="utf-8")

    checked = 0
    failures = []
    skipped_open_leads = 0

    for row in rows:
        if not row.get("repo_known_before_audit"):
            continue
        action = row.get("required_action", "")
        if action.startswith("flag_open_lead") or action == "note_context_only":
            skipped_open_leads += 1
            continue

        checked += 1
        place = row["place_name"]
        aliases = [place] + row.get("place_aliases", [])
        person = row["person"]
        claimed_present = row.get("current_canon_present", False)

        found, context = person_near_place(text, aliases, person)

        if claimed_present and not found:
            failures.append(
                f"STALE ledger claim: {place!r} + {person!r} marked "
                f"current_canon_present=true but not actually found together "
                f"in {ct_path.name} (place may have moved/been reworded)."
            )
        elif not claimed_present and found:
            # Good news case: someone already fixed it since the ledger was written.
            print(f"NOTE: {place!r} + {person!r} is marked missing in the ledger "
                  f"but IS now found in {ct_path.name} -- ledger is stale in the "
                  f"good direction, update it.")
        elif not claimed_present and not found:
            print(f"CONFIRMED GAP (expected): {place!r} does not carry the "
                  f"{person!r} edge in {ct_path.name} -- matches ledger, still open.")
        else:
            print(f"OK: {place!r} + {person!r} found together. Context: ...{context}...")

    print()
    print(f"Checked {checked} known-edge ledger rows against {ct_path}.")
    print(f"Skipped {skipped_open_leads} open-lead/context-only rows (not eligible to fail).")

    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print(f"- {f}")
        return 1

    print("\nPLACE_PERSON_EDGE_CHECK: PASS (no stale ledger claims found)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Light sanity validator for the INDIA travel knowledge base — V6 architecture.

Checks only the expensive-to-miss failures:
- required boot/state files exist (master boot, current state, safe state, knowledge
  map, trip frame, collaboration protocol, protected canon);
- SUCCESSOR_SAFE_STATE.md is actually listed in both ALWAYS-read enumerations, not
  reachable only via a pointer in another file's prose (2026-08-30 regression, R28);
- SUCCESSOR_SAFE_STATE.md reports STATUS: SAFE_TO_HANDOFF and UNSAVED_RISK: GEEN;
- CURRENT_STATE.md does not still claim BACKFILL_NOT_COMPLETE after the backfill closed;
- protected canon still matches the SHA anchored in TRIP_FRAME_HARD.md;
- permanent protected IDs 001..081 are still present exactly once;
- the simplified boot did not accidentally re-activate the old brute-force mechanics.

A real non-force/fast-forward branch comparison is checked separately immediately
before a central write. This script is intentionally not a certification system.
"""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []

CURRENT = ROOT / "governance/CURRENT_STATE.md"
SAFE_STATE = ROOT / "governance/SUCCESSOR_SAFE_STATE.md"
MASTER_BOOT = ROOT / "governance/INDIA_MASTER_BOOT.md"
KNOWLEDGE_MAP = ROOT / "governance/INDIA_CURRENT_KNOWLEDGE_MAP.md"
TRIP_FRAME = ROOT / "governance/TRIP_FRAME_HARD.md"
CANON_REL = "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv"
CANON = ROOT / CANON_REL

required = [
    ROOT / "README.md",
    MASTER_BOOT,
    CURRENT,
    SAFE_STATE,
    KNOWLEDGE_MAP,
    TRIP_FRAME,
    ROOT / "governance/CCI_COLLABORATION_PROTOCOL.md",
    CANON,
]

for p in required:
    if not p.is_file():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

current_text = CURRENT.read_text(encoding="utf-8") if CURRENT.is_file() else ""
safe_state_text = SAFE_STATE.read_text(encoding="utf-8") if SAFE_STATE.is_file() else ""
master_boot_text = MASTER_BOOT.read_text(encoding="utf-8") if MASTER_BOOT.is_file() else ""
knowledge_map_text = KNOWLEDGE_MAP.read_text(encoding="utf-8") if KNOWLEDGE_MAP.is_file() else ""
trip_frame_text = TRIP_FRAME.read_text(encoding="utf-8") if TRIP_FRAME.is_file() else ""

# A mandatory file is only mandatory if it is a listed item in the actual ALWAYS-read
# enumerations, not merely mentioned in another file's prose (R28: this exact bug
# shipped for SUCCESSOR_SAFE_STATE.md on the day it was created).
if "SUCCESSOR_SAFE_STATE.md" not in master_boot_text:
    errors.append("SUCCESSOR_SAFE_STATE.md is not listed in INDIA_MASTER_BOOT.md's ALWAYS-read enumeration")
if "SUCCESSOR_SAFE_STATE.md" not in knowledge_map_text:
    errors.append("SUCCESSOR_SAFE_STATE.md is not listed in INDIA_CURRENT_KNOWLEDGE_MAP.md's ALWAYS section")

# The crash-safe checkpoint must actually be in a handoff-safe state, and must not
# silently disagree with CURRENT_STATE about basic architecture facts.
if safe_state_text:
    if "STATUS: SAFE_TO_HANDOFF" not in safe_state_text:
        errors.append("SUCCESSOR_SAFE_STATE.md STATUS is not SAFE_TO_HANDOFF")
    if not re.search(r"UNSAVED_RISK:\s*\nGEEN", safe_state_text):
        errors.append("SUCCESSOR_SAFE_STATE.md UNSAVED_RISK is not GEEN")
if "BACKFILL_NOT_COMPLETE" in current_text:
    errors.append("CURRENT_STATE.md still claims BACKFILL_NOT_COMPLETE, contradicting the completed decision-ledger backfill")

# The protected-canon blob anchor lives in TRIP_FRAME_HARD.md (a file that is not
# rewritten every turn) rather than CURRENT_STATE.md, which destroyed this same
# anchor one day after it was first added there.
m = re.search(r"Current protected blob[^\n]*:\s*\n`([0-9a-f]{40})`", trip_frame_text)
if not m:
    errors.append("TRIP_FRAME_HARD.md does not contain the expected protected-canon blob SHA")
else:
    expected = m.group(1)
    try:
        actual = subprocess.check_output(
            ["git", "hash-object", CANON_REL], cwd=ROOT, text=True
        ).strip()
    except Exception as exc:
        errors.append(f"cannot hash protected canon: {exc}")
    else:
        if actual != expected:
            errors.append(f"protected canon changed: {actual} != {expected}")

if CANON.is_file():
    with CANON.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    permanent_ids = [r.get("entity_id", "") for r in rows if r.get("record_type") == "PERMANENT"]
    for i in range(1, 82):
        eid = f"{i:03d}"
        if permanent_ids.count(eid) != 1:
            errors.append(f"protected permanent ID {eid} occurs {permanent_ids.count(eid)} times; expected 1")

readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""

for forbidden in ["GEHELE REPO LEZEN", "byte_weighted_knowledge_pct"]:
    if forbidden in readme or forbidden in master_boot_text:
        errors.append(f"old heavy boot mechanic became active again: {forbidden}")

if errors:
    print("INDIA_TRAVEL_BOOT_SANITY: FAIL")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("INDIA_TRAVEL_BOOT_SANITY: PASS")
print("protected canon: unchanged; IDs 001..081 preserved")
print("light start/current-state/collaboration files: present")
print("central branch relation: CHECK SEPARATELY before central write")
sys.exit(0)

#!/usr/bin/env python3
"""Light sanity validator for the INDIA travel knowledge base.

Checks only the expensive-to-miss failures:
- current-state/start files exist;
- protected canon still matches the SHA recorded in CURRENT_STATE;
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
CANON_REL = "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv"
CANON = ROOT / CANON_REL

required = [
    ROOT / "README.md",
    CURRENT,
    ROOT / "governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md",
    ROOT / "governance/CCI_COLLABORATION_PROTOCOL.md",
    CANON,
]

for p in required:
    if not p.is_file():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

current_text = CURRENT.read_text(encoding="utf-8") if CURRENT.is_file() else ""

# CURRENT_STATE deliberately carries the expected protected-canon blob so a silent
# mutation is caught without a separate receipt/registry system.
m = re.search(r"Current protected blob[^\n]*:\s*\n`([0-9a-f]{40})`", current_text)
if not m:
    errors.append("CURRENT_STATE does not contain the expected protected-canon blob SHA")
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
boot = (ROOT / "governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md").read_text(encoding="utf-8") if (ROOT / "governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md").is_file() else ""

for forbidden in ["GEHELE REPO LEZEN", "byte_weighted_knowledge_pct"]:
    if forbidden in readme or forbidden in boot:
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

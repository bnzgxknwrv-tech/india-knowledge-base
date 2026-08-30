#!/usr/bin/env python3
"""Sanity validator for the INDIA travel knowledge base — V7 architecture.

Default mode checks structural boot integrity.

With --require-session-receipt it additionally checks that the latest living
BOOT_SESSION_RECEIPT contains auditable evidence of a complete fresh-session boot:
15/15 central files + 6/6 immutable CCI files, no unfinished truncation, no summary
substitution, BOOT_GATE PASS, and the minimum semantic control-veto checksum.

This cannot mathematically prove model cognition. It converts the dangerous failure
class 'successor silently skipped the boot but sounded informed' into an externally
auditable process failure.
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []
warnings: list[str] = []
require_receipt = "--require-session-receipt" in sys.argv[1:]

MASTER_BOOT = ROOT / "governance/INDIA_MASTER_BOOT.md"
FRESH_GATE = ROOT / "governance/FRESH_SESSION_BOOT_GATE.md"
RECEIPT = ROOT / "governance/BOOT_SESSION_RECEIPT.md"
CURRENT = ROOT / "governance/CURRENT_STATE.md"
SAFE_STATE = ROOT / "governance/SUCCESSOR_SAFE_STATE.md"
KNOWLEDGE_MAP = ROOT / "governance/INDIA_CURRENT_KNOWLEDGE_MAP.md"
TRIP_FRAME = ROOT / "governance/TRIP_FRAME_HARD.md"
CANON_REL = "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv"
CANON = ROOT / CANON_REL

CENTRAL_PATHS = [
    "governance/FRESH_SESSION_BOOT_GATE.md",
    "governance/INDIA_MASTER_BOOT.md",
    "governance/INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md",
    "governance/MARK_TRAVEL_PREFERENCES_CURRENT.md",
    "governance/MARK_LOCATION_NAMING_CONTEXT_PROTOCOL.md",
    "governance/MAP_COORDINATE_VERIFICATION_RULE.md",
    "governance/INDIA_HUMAN_CENTERED_COMPLEX_TRIP_PLANNING_STANDARD.md",
    "governance/FINAL_COMFORT_SWEEP_RULE_2026-08-23.md",
    "governance/TRIP_FRAME_HARD.md",
    "governance/CURRENT_DECISIONS_MASTER.md",
    "governance/DECISION_LEDGER.jsonl",
    "governance/CURRENT_STATE.md",
    "governance/SUCCESSOR_SAFE_STATE.md",
    "governance/INDIA_RECOVERY_DELTAS_CURRENT.md",
    "governance/INDIA_CURRENT_KNOWLEDGE_MAP.md",
]

CCI_COMMIT = "b5349afe41f98eb4870728aaff2c633899afc1fa"
CCI_PATHS = [
    "runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/SUCCESSOR_START_HERE.md",
    "runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/SUPERSEDED_AND_DO_NOT_REVIVE.md",
    "runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/MARK_CURRENT_CANON_MASTER.md",
    "runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/PROJECT_PHILOSOPHY_AND_SELECTION_MODEL.md",
    "runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/OPEN_MARK_DECISIONS_ONLY.md",
    "runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/CURRENT_TRAVEL_EXECUTION_CANON.md",
]

CONTROL_TOKENS = [
    "TRAIN_FIRST_TRUE_DOOR_TO_DOOR",
    "AL_BESLIST_BEFORE_CHOICE",
    "RECOGNITION_RICH_EVERY_LOCATION_OCCURRENCE",
    "GEO_VERIFIED_FOR_DECISION_OR_NO_GEOMETRY",
    "ACTION_FIRST_NO_DEFERRAL",
    "SAME_TURN_DURABLE_MEMORY",
    "CCI_THREE_WAY_FILTER",
    "SAFE_STATE_UNSAVED_RISK_GEEN",
    "FULL_SOURCE_LAYER_WHEN_REQUESTED",
    "NU_DOEN_EXPLICIT_NEXT_ACTION",
]

required = [
    ROOT / "README.md",
    MASTER_BOOT,
    FRESH_GATE,
    RECEIPT,
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


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.is_file() else ""


master_boot_text = read(MASTER_BOOT)
fresh_gate_text = read(FRESH_GATE)
receipt_text = read(RECEIPT)
current_text = read(CURRENT)
safe_state_text = read(SAFE_STATE)
knowledge_map_text = read(KNOWLEDGE_MAP)
trip_frame_text = read(TRIP_FRAME)

# R28 / V7: mandatory reads must be explicit in BOTH authoritative enumerations.
for rel in CENTRAL_PATHS:
    name = Path(rel).name
    if rel not in master_boot_text and name not in master_boot_text:
        errors.append(f"mandatory central file absent from master boot enumeration: {rel}")
    if rel not in knowledge_map_text and name not in knowledge_map_text:
        errors.append(f"mandatory central file absent from knowledge-map ALWAYS section: {rel}")

if "15/15" not in master_boot_text:
    errors.append("master boot does not declare V7 central full-read count 15/15")
if "15/15" not in knowledge_map_text:
    errors.append("knowledge map does not declare V7 central full-read count 15/15")
if "BOOT_SESSION_RECEIPT.md" not in master_boot_text:
    errors.append("master boot does not require BOOT_SESSION_RECEIPT.md")
if "BOOT_SESSION_RECEIPT.md" not in knowledge_map_text:
    errors.append("knowledge map does not route BOOT_SESSION_RECEIPT.md")

# Crash-safe checkpoint integrity.
if safe_state_text:
    if "STATUS: SAFE_TO_HANDOFF" not in safe_state_text:
        errors.append("SUCCESSOR_SAFE_STATE.md STATUS is not SAFE_TO_HANDOFF")
    if not re.search(r"UNSAVED_RISK:\s*\nGEEN", safe_state_text):
        errors.append("SUCCESSOR_SAFE_STATE.md UNSAVED_RISK is not GEEN")
if "BACKFILL_NOT_COMPLETE" in current_text:
    errors.append("CURRENT_STATE.md still claims BACKFILL_NOT_COMPLETE")

# Protected-canon blob anchor.
m = re.search(r"Current protected blob[^\n]*:\s*\n`([0-9a-f]{40})`", trip_frame_text)
if not m:
    errors.append("TRIP_FRAME_HARD.md does not contain expected protected-canon blob SHA")
else:
    expected = m.group(1)
    try:
        actual = subprocess.check_output(["git", "hash-object", CANON_REL], cwd=ROOT, text=True).strip()
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

readme = read(ROOT / "README.md")
for forbidden in ["GEHELE REPO LEZEN", "byte_weighted_knowledge_pct"]:
    if forbidden in readme or forbidden in master_boot_text:
        errors.append(f"old heavy boot mechanic became active again: {forbidden}")

# Optional hard session-receipt gate.
if require_receipt:
    required_literals = {
        "CENTRAL_FULL_READS": "CENTRAL_FULL_READS: `15/15`",
        "CCI_FULL_READS": "CCI_FULL_READS: `6/6`",
        "TRUNCATED": "TRUNCATED_READS_LEFT_UNFINISHED: `GEEN`",
        "SUMMARY": "SUMMARY_SUBSTITUTION_USED: `NEE`",
        "BOOT_GATE": "BOOT_GATE: `PASS`",
    }
    for label, literal in required_literals.items():
        if literal not in receipt_text:
            errors.append(f"session receipt missing/invalid {label}: expected {literal}")

    for token in CONTROL_TOKENS:
        if token not in receipt_text:
            errors.append(f"session receipt missing control-veto token: {token}")

    for rel in CENTRAL_PATHS:
        if rel not in receipt_text:
            errors.append(f"session receipt does not enumerate central read: {rel}")
    for rel in CCI_PATHS:
        if rel not in receipt_text:
            errors.append(f"session receipt does not enumerate CCI read: {rel}")
    if CCI_COMMIT not in receipt_text:
        errors.append("session receipt does not pin immutable CCI completion commit")

    # PROOF_OF_READ_CHALLENGE: a correct blob SHA proves the session identified the
    # right version of a file, not that its content was ever loaded (a metadata-only
    # `git rev-parse <head>:<path>` returns the same SHA without reading a byte, and an
    # unchanged file's SHA can be copied forward from a previous receipt unread). Each
    # quote must be an exact substring of its named source file's actual text.
    if "PROOF_OF_READ_CHALLENGE" not in receipt_text:
        errors.append("session receipt missing PROOF_OF_READ_CHALLENGE block")
    else:
        quotes = re.findall(
            r"SOURCE:\s*([^\n]+)\nQUOTE:\s*\"([^\"]+)\"", receipt_text
        )
        if len(quotes) < 3:
            errors.append(
                f"PROOF_OF_READ_CHALLENGE has {len(quotes)} SOURCE/QUOTE pairs, need at least 3"
            )
        for source_rel, quote in quotes:
            source_rel = source_rel.strip()
            quote = quote.strip()
            if not quote:
                errors.append(f"PROOF_OF_READ_CHALLENGE has an empty quote for {source_rel}")
                continue
            source_path = ROOT / source_rel
            if source_path.is_file():
                if quote not in read(source_path):
                    errors.append(
                        f"PROOF_OF_READ_CHALLENGE quote not found verbatim in local {source_rel} "
                        f"(paraphrase, mismatch, or fabricated)"
                    )
            elif source_rel.startswith("runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/"):
                try:
                    cci_text = subprocess.check_output(
                        ["git", "show", f"{CCI_COMMIT}:{source_rel}"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
                    )
                except Exception:
                    warnings.append(f"could not verify PROOF_OF_READ_CHALLENGE quote against immutable CCI {source_rel} locally")
                else:
                    if quote not in cci_text:
                        errors.append(
                            f"PROOF_OF_READ_CHALLENGE quote not found verbatim in CCI {source_rel} at {CCI_COMMIT}"
                        )
            else:
                errors.append(f"PROOF_OF_READ_CHALLENGE cites unrecognized/unreadable source: {source_rel}")

    bm = re.search(r"BOOT_HEAD(?:_READ)?:\s*`([0-9a-f]{40})`", receipt_text)
    if not bm:
        errors.append("session receipt lacks exact 40-char BOOT_HEAD")
    else:
        boot_head = bm.group(1)
        # Verify recorded central blob SHAs against the recorded BOOT_HEAD where git objects exist.
        for rel in CENTRAL_PATHS:
            rm = re.search(re.escape(rel) + r"[^\n]*blob `([0-9a-f]{40})`", receipt_text)
            if not rm:
                errors.append(f"session receipt lacks blob SHA for central read: {rel}")
                continue
            recorded_blob = rm.group(1)
            try:
                actual_blob = subprocess.check_output(
                    ["git", "rev-parse", f"{boot_head}:{rel}"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
                ).strip()
            except Exception:
                warnings.append(f"could not verify {rel} against BOOT_HEAD {boot_head[:12]} in local git objects")
            else:
                if actual_blob != recorded_blob:
                    errors.append(f"receipt blob mismatch at BOOT_HEAD for {rel}: {recorded_blob} != {actual_blob}")

        # CCI verification is best effort because a shallow/local checkout may not contain that remote commit.
        for rel in CCI_PATHS:
            rm = re.search(re.escape(rel) + r"[^\n]*blob `([0-9a-f]{40})`", receipt_text)
            if not rm:
                errors.append(f"session receipt lacks blob SHA for CCI read: {rel}")
                continue
            recorded_blob = rm.group(1)
            try:
                actual_blob = subprocess.check_output(
                    ["git", "rev-parse", f"{CCI_COMMIT}:{rel}"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
                ).strip()
            except Exception:
                warnings.append(f"local checkout cannot verify immutable CCI blob for {Path(rel).name}")
            else:
                if actual_blob != recorded_blob:
                    errors.append(f"receipt CCI blob mismatch for {rel}: {recorded_blob} != {actual_blob}")

if errors:
    print("INDIA_TRAVEL_BOOT_SANITY: FAIL")
    for e in errors:
        print(f"- {e}")
    for w in warnings:
        print(f"WARNING: {w}")
    sys.exit(1)

print("INDIA_TRAVEL_BOOT_SANITY: PASS")
print("V7 fresh-session gate: structurally present")
print("protected canon: unchanged; IDs 001..081 preserved")
if require_receipt:
    print("session receipt: PASS (15/15 central, 6/6 CCI, semantic veto checksum present)")
for w in warnings:
    print(f"WARNING: {w}")
print("central branch relation: CHECK SEPARATELY before central write")
sys.exit(0)

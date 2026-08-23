#!/usr/bin/env python3
"""Fail-closed validator for the INDIA successor architecture.

Run from repository root.
- `python3 governance/scripts/validate_successor_architecture.py --preflight`
  validates a candidate before CCI adversarial review.
- `python3 governance/scripts/validate_successor_architecture.py`
  validates final certification before central fast-forward.

Exit 0 = PASS, non-zero = FAIL.
This validates structure/integrity, not travel facts or subjective Mark decisions.
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--preflight", action="store_true")
args = parser.parse_args()
MODE = "PREFLIGHT" if args.preflight else "FINAL"

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []

COMMON_REQUIRED = [
    "README.md",
    "governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md",
    "governance/ACTIVE_FRAMEWORK.md",
    "governance/PRECEDENCE_MAP.jsonl",
    "governance/KNOWLEDGE_BASELINE_LATEST.md",
    "governance/CENTRAL_INTEGRATION_REGISTRY.jsonl",
    "governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl",
    "governance/CCI_COLLABORATION_PROTOCOL.md",
    "governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md",
    "governance/INDIA_SESSION_START.md",
    "handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md",
    "runs/active/INDIA9-SUCCESSOR-ARCHITECTURE-INTEGRATION-001/TASK.md",
    "runs/active/INDIA9-SUCCESSOR-ARCHITECTURE-INTEGRATION-001/STATUS.md",
    "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv",
    "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/STATUS.md",
    "archive/india9-knowledge-audit-2026-08-23/task006/BRANCH_ONLY_SEMANTIC_COVERAGE_LEDGER.jsonl",
    "archive/india9-knowledge-audit-2026-08-23/task007/CATEGORY1_MANIFEST.jsonl",
    "archive/india9-knowledge-audit-2026-08-23/task007/CATEGORY1_READ_STREAM.jsonl",
]

FINAL_ONLY_REQUIRED = [
    "governance/CCI_ADVERSARIAL_REVIEW_RECEIPT_2026-08-23.md",
    "governance/SUCCESSOR_CERTIFICATION_RECEIPT_2026-08-23.md",
]

EXPECTED_BLOBS = {
    "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv": "a607241caa41637e2167d0f56781bf663f038932",
    "archive/india9-knowledge-audit-2026-08-23/task006/BRANCH_ONLY_SEMANTIC_COVERAGE_LEDGER.jsonl": "048d99afcf4abe95ea16165235c2e377bd75e7d1",
    "archive/india9-knowledge-audit-2026-08-23/task007/CATEGORY1_MANIFEST.jsonl": "d5533a21f07dc16a5edb6767df64c9ce2211634a",
    "archive/india9-knowledge-audit-2026-08-23/task007/CATEGORY1_READ_STREAM.jsonl": "e24f7e89c0f14b06096e6efe97dfd960c0280ab8",
}


def text(rel: str) -> str:
    p = ROOT / rel
    if not p.exists():
        errors.append(f"MISSING: {rel}")
        return ""
    return p.read_text(encoding="utf-8")


def lines(rel: str) -> set[str]:
    return {line.strip() for line in text(rel).splitlines() if line.strip()}


def require(rel: str, needle: str) -> None:
    if needle not in text(rel):
        errors.append(f"TOKEN_MISSING: {rel}: {needle}")


def require_exact_line(rel: str, expected: str) -> None:
    if expected not in lines(rel):
        errors.append(f"EXACT_LINE_MISSING: {rel}: {expected}")


def git_blob(rel: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "hash-object", rel], cwd=ROOT, text=True
        ).strip()
    except Exception as exc:
        errors.append(f"HASH_ERROR: {rel}: {exc}")
        return ""


required = COMMON_REQUIRED + ([] if MODE == "PREFLIGHT" else FINAL_ONLY_REQUIRED)
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"MISSING: {rel}")

for rel, expected in EXPECTED_BLOBS.items():
    actual = git_blob(rel)
    if actual and actual != expected:
        errors.append(f"BLOB_MISMATCH: {rel}: {actual} != {expected}")

# Machine-readable files must parse line-by-line and contain objects.
for rel in [
    "governance/PRECEDENCE_MAP.jsonl",
    "governance/CENTRAL_INTEGRATION_REGISTRY.jsonl",
    "governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl",
]:
    data = text(rel)
    parsed = 0
    for n, line in enumerate(data.splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if not isinstance(obj, dict):
                raise ValueError("row is not a JSON object")
            parsed += 1
        except Exception as exc:
            errors.append(f"JSONL_ERROR: {rel}:{n}: {exc}")
    if parsed == 0:
        errors.append(f"JSONL_EMPTY: {rel}")

# Protected global permanent IDs 001..081 must exist once each, in order-independent exact set.
canon = ROOT / "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv"
if canon.exists():
    with canon.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    ids = [r.get("entity_id", "") for r in rows if r.get("record_type") == "PERMANENT"]
    expected_ids = [f"{i:03d}" for i in range(1, 82)]
    if len(ids) != 81 or len(set(ids)) != 81 or sorted(ids) != expected_ids:
        errors.append(
            f"PROTECTED_ID_SET_MISMATCH: got {len(ids)} permanent rows / {len(set(ids))} unique; expected exact 001..081"
        )

# Binding semantic guards common to both phases.
checks = [
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "KNOWLEDGE_READY: 100%"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "Full-bootstrap fallback"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "AL BESLIST?"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "verwijderd pad/bestand"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "same blob"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "knowledge_cutoff_commit"),
    ("governance/ACTIVE_FRAMEWORK.md", "worker branch saying `COMPLETE`"),
    ("governance/CCI_COLLABORATION_PROTOCOL.md", "controleer PR #23"),
    ("governance/CCI_COLLABORATION_PROTOCOL.md", "read-only red-team"),
    ("governance/KNOWLEDGE_BASELINE_LATEST.md", "62 bestanden / 344.876 bronbytes"),
    ("README.md", "governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md"),
    ("governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md", "baseline + delta"),
    ("governance/INDIA_SESSION_START.md", "KNOWLEDGE_READY"),
    ("handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md", "DEFINITIEVE STARTPROMPT INDIA10"),
]
for rel, needle in checks:
    require(rel, needle)

if MODE == "PREFLIGHT":
    require_exact_line(
        "governance/KNOWLEDGE_BASELINE_LATEST.md",
        "status: CERTIFIED_CANDIDATE_PENDING_FINAL_VALIDATOR",
    )
    require_exact_line(
        "handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md",
        "SUCCESSOR_ARCHITECTURE: NOT_YET_PASS",
    )
else:
    # Final mode is deliberately strict. Exact lines avoid substring tricks such as NOT_PASS.
    require_exact_line("governance/KNOWLEDGE_BASELINE_LATEST.md", "status: CERTIFIED")
    require("governance/KNOWLEDGE_BASELINE_LATEST.md", "knowledge_cutoff_commit:")
    require_exact_line(
        "handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md",
        "SUCCESSOR_ARCHITECTURE: PASS",
    )
    require_exact_line(
        "runs/active/INDIA9-SUCCESSOR-ARCHITECTURE-INTEGRATION-001/STATUS.md",
        "SUCCESSOR_ARCHITECTURE: PASS",
    )
    require_exact_line(
        "governance/CCI_ADVERSARIAL_REVIEW_RECEIPT_2026-08-23.md",
        "CCI_REVIEW_009: PASS",
    )
    require_exact_line(
        "governance/CCI_ADVERSARIAL_REVIEW_RECEIPT_2026-08-23.md",
        "SAFE_TO_CERTIFY_AFTER_FIXES: JA",
    )
    require_exact_line(
        "governance/CCI_ADVERSARIAL_REVIEW_RECEIPT_2026-08-23.md",
        "POST_FREEZE_DELTA_CLOSURE: PASS",
    )
    require_exact_line(
        "governance/SUCCESSOR_CERTIFICATION_RECEIPT_2026-08-23.md",
        "FINAL_VALIDATOR_REQUIRED: JA",
    )
    require("governance/SUCCESSOR_CERTIFICATION_RECEIPT_2026-08-23.md", "knowledge_cutoff_commit:")

# The old brute-force rule must no longer be the default in entrypoints.
for rel in ["README.md", "governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md"]:
    data = text(rel)
    if "Lees de gehele tekstuele repository inhoudelijk" in data:
        errors.append(f"OLD_BRUTE_FORCE_DEFAULT_STILL_ACTIVE: {rel}")

if errors:
    print(f"SUCCESSOR_ARCHITECTURE_VALIDATOR_{MODE}: FAIL")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"SUCCESSOR_ARCHITECTURE_VALIDATOR_{MODE}: PASS")
print("protected_canon: exact blob + exact permanent IDs 001-081")
print("audit_provenance: exact key blobs")
print("authority/jsonl/entrypoints/handoff: PASS")
if MODE == "FINAL":
    print("cci_review_receipt + certification_receipt: PASS")
sys.exit(0)

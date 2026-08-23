#!/usr/bin/env python3
"""Fail-closed validator for the INDIA successor architecture.

Run from repository root. Exit 0 = PASS, non-zero = FAIL.
This validates structure/integrity, not travel facts or subjective Mark decisions.
"""
from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []

REQUIRED = [
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
    "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv",
    "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/STATUS.md",
    "archive/india9-knowledge-audit-2026-08-23/task006/BRANCH_ONLY_SEMANTIC_COVERAGE_LEDGER.jsonl",
    "archive/india9-knowledge-audit-2026-08-23/task007/CATEGORY1_MANIFEST.jsonl",
    "archive/india9-knowledge-audit-2026-08-23/task007/CATEGORY1_READ_STREAM.jsonl",
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


def require(rel: str, needle: str) -> None:
    if needle not in text(rel):
        errors.append(f"TOKEN_MISSING: {rel}: {needle}")


def git_blob(rel: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "hash-object", rel], cwd=ROOT, text=True
        ).strip()
    except Exception as exc:
        errors.append(f"HASH_ERROR: {rel}: {exc}")
        return ""


for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"MISSING: {rel}")

for rel, expected in EXPECTED_BLOBS.items():
    actual = git_blob(rel)
    if actual and actual != expected:
        errors.append(f"BLOB_MISMATCH: {rel}: {actual} != {expected}")

# Machine-readable files must parse line-by-line.
for rel in [
    "governance/PRECEDENCE_MAP.jsonl",
    "governance/CENTRAL_INTEGRATION_REGISTRY.jsonl",
    "governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl",
]:
    data = text(rel)
    for n, line in enumerate(data.splitlines(), 1):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except Exception as exc:
            errors.append(f"JSONL_ERROR: {rel}:{n}: {exc}")

# Protected global permanent IDs 001..081 must exist once each.
canon = ROOT / "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv"
if canon.exists():
    with canon.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    ids = [r.get("entity_id", "") for r in rows if r.get("record_type") == "PERMANENT"]
    expected_ids = [f"{i:03d}" for i in range(1, 82)]
    if sorted(ids) != expected_ids:
        errors.append(f"PROTECTED_ID_SET_MISMATCH: got {len(ids)} permanent rows; expected exact 001..081")

# Binding semantic guards.
checks = [
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "KNOWLEDGE_READY: 100%"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "Full-bootstrap fallback"),
    ("governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md", "AL BESLIST?"),
    ("governance/ACTIVE_FRAMEWORK.md", "WORKER"),
    ("governance/CCI_COLLABORATION_PROTOCOL.md", "controleer PR #23"),
    ("governance/CCI_COLLABORATION_PROTOCOL.md", "read-only red-team"),
    ("governance/KNOWLEDGE_BASELINE_LATEST.md", "status: CERTIFIED"),
    ("governance/KNOWLEDGE_BASELINE_LATEST.md", "62 bestanden / 344.876 bronbytes"),
    ("README.md", "governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md"),
    ("governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md", "baseline + delta"),
    ("governance/INDIA_SESSION_START.md", "KNOWLEDGE_READY"),
    ("handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md", "SUCCESSOR_ARCHITECTURE: PASS"),
    ("handoffs/INDIA9_TO_INDIA10_SUCCESSOR_READY_2026-08-23.md", "DEFINITIEVE STARTPROMPT INDIA10"),
]
for rel, needle in checks:
    require(rel, needle)

# The old brute-force rule must no longer be the default in entrypoints.
for rel in ["README.md", "governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md"]:
    data = text(rel)
    if "Lees de gehele tekstuele repository inhoudelijk" in data:
        errors.append(f"OLD_BRUTE_FORCE_DEFAULT_STILL_ACTIVE: {rel}")

if errors:
    print("SUCCESSOR_ARCHITECTURE_VALIDATOR: FAIL")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("SUCCESSOR_ARCHITECTURE_VALIDATOR: PASS")
print("protected_canon: exact blob + exact permanent IDs 001-081")
print("audit_provenance: exact key blobs")
print("authority/jsonl/entrypoints/handoff: PASS")
sys.exit(0)

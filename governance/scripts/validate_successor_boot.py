#!/usr/bin/env python3
"""
validate_successor_boot.py

Mechanical validator for the task-008 successor boot architecture.
Fails loudly (non-zero exit, explicit message) on any missing/malformed
requirement -- never silently passes a missing field.

Run from the repository root:
    python3 governance/scripts/validate_successor_boot.py
"""
import csv
import json
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

errors = []
warnings = []


def fail(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def path(*parts):
    return os.path.join(REPO_ROOT, *parts)


def read_text(*parts):
    p = path(*parts)
    if not os.path.isfile(p):
        return None
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def read_jsonl(*parts):
    p = path(*parts)
    if not os.path.isfile(p):
        return None
    rows = []
    with open(p, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                fail(f"{parts[-1]}: line {i} failed to parse as JSON: {e}")
    return rows


# --- 1. latest baseline pointer exists and referenced files exist ---
latest = read_text("governance", "KNOWLEDGE_BASELINE_LATEST.md")
if latest is None:
    fail("governance/KNOWLEDGE_BASELINE_LATEST.md is missing")
else:
    m = re.search(r"latest_baseline:\s*(\S+)", latest)
    if not m:
        fail("governance/KNOWLEDGE_BASELINE_LATEST.md has no 'latest_baseline:' field")
    else:
        baseline_ref = m.group(1)
        if not os.path.isfile(path(baseline_ref)):
            fail(f"KNOWLEDGE_BASELINE_LATEST.md points to '{baseline_ref}' which does not exist")

if not os.path.isfile(path("governance", "KNOWLEDGE_BASELINE_2026-08-23.md")):
    fail("governance/KNOWLEDGE_BASELINE_2026-08-23.md is missing")

# --- 2. protected canon central path exists ---
canon_path = "runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv"
if not os.path.isfile(path(canon_path)):
    fail(f"protected canon not found centrally at {canon_path}")
else:
    with open(path(canon_path), newline="", encoding="utf-8") as f:
        canon_rows = list(csv.DictReader(f))
    if not canon_rows:
        fail(f"{canon_path} parsed to zero rows")
    else:
        ids = [r.get("entity_id") for r in canon_rows]
        seen = {}
        dup_ids = set()
        for eid in ids:
            if eid in seen:
                dup_ids.add(eid)
            seen[eid] = True
        if dup_ids:
            fail(f"protected canon has duplicate entity_id values: {sorted(dup_ids)}")

# --- 3. PRECEDENCE_MAP and CENTRAL_INTEGRATION_REGISTRY exist and parse linewise ---
prec_rows = read_jsonl("governance", "PRECEDENCE_MAP.jsonl")
if prec_rows is None:
    fail("governance/PRECEDENCE_MAP.jsonl is missing")
elif not prec_rows:
    fail("governance/PRECEDENCE_MAP.jsonl parsed to zero rows")
else:
    required_prec_fields = {"scope", "higher_authority", "lower_authority", "relation",
                             "reason", "effective_date", "evidence"}
    for i, r in enumerate(prec_rows, start=1):
        missing = required_prec_fields - set(r.keys())
        if missing:
            fail(f"PRECEDENCE_MAP.jsonl row {i} missing fields: {sorted(missing)}")

integ_rows = read_jsonl("governance", "CENTRAL_INTEGRATION_REGISTRY.jsonl")
if integ_rows is None:
    fail("governance/CENTRAL_INTEGRATION_REGISTRY.jsonl is missing")
elif not integ_rows:
    fail("governance/CENTRAL_INTEGRATION_REGISTRY.jsonl parsed to zero rows")
else:
    required_integ_fields = {"task_path", "source_branch", "worker_output_state",
                              "central_integration_state"}
    for i, r in enumerate(integ_rows, start=1):
        missing = required_integ_fields - set(r.keys())
        if missing:
            fail(f"CENTRAL_INTEGRATION_REGISTRY.jsonl row {i} missing fields: {sorted(missing)}")

# --- 4. semantic import registry: exactly 62 category1 source blob SHAs, no duplicates ---
sem_rows = read_jsonl("governance", "SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl")
if sem_rows is None:
    fail("governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl is missing")
else:
    if len(sem_rows) != 62:
        fail(f"SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl has {len(sem_rows)} rows, expected exactly 62")
    shas = [r.get("blob_sha") for r in sem_rows]
    if any(s is None for s in shas):
        fail("SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl has a row with no blob_sha")
    dup_shas = {s for s in shas if shas.count(s) > 1}
    if dup_shas:
        fail(f"SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl has duplicate blob_sha keys: {sorted(dup_shas)}")
    dispositions = {r.get("central_disposition") for r in sem_rows}
    if not dispositions <= {"PROMOTED_CANONICAL", "ARCHIVED_PROVENANCE",
                             "ALREADY_CENTRAL"}:
        fail(f"SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl has unexpected central_disposition values: {dispositions}")
    promoted = sum(1 for r in sem_rows if r.get("central_disposition") == "PROMOTED_CANONICAL")
    archived = sum(1 for r in sem_rows if r.get("central_disposition") == "ARCHIVED_PROVENANCE")
    if promoted + archived != len(sem_rows):
        fail("SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl: promoted+archived does not equal total row count")
    # every archived row's central_path must exist on disk; every promoted row's central_path must exist
    for r in sem_rows:
        cp = r.get("central_path")
        if not cp:
            fail(f"SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl row for blob {r.get('blob_sha')} has no central_path")
            continue
        if not os.path.isfile(path(cp)):
            fail(f"SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl row for blob {r.get('blob_sha')} points to missing file: {cp}")

# --- 5. required boot/handoff/progress files exist ---
required_files = [
    ("governance", "INDIA_SUCCESSOR_BOOT_PROTOCOL.md"),
    ("governance", "ACTIVE_FRAMEWORK.md"),
    ("handoffs", "INDIA9_TO_INDIA10_SUCCESSOR_BOOT_2026-08-23.md"),
    ("runs", "active", "INDIA9-SUCCESSOR-BOOT-2026-08-23", "BOOT_PROGRESS.md"),
]
for parts in required_files:
    if not os.path.isfile(path(*parts)):
        fail(f"required file missing: {'/'.join(parts)}")

# --- 6. current start prompt references the binding protocol ---
readme = read_text("README.md")
if readme is None:
    fail("README.md is missing")
elif "INDIA_SUCCESSOR_BOOT_PROTOCOL.md" not in readme:
    fail("README.md does not reference governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md")

# --- summary ---
print(f"validate_successor_boot.py -- {len(errors)} errors, {len(warnings)} warnings")
for w in warnings:
    print(f"WARNING: {w}")
for e in errors:
    print(f"ERROR: {e}")

if errors:
    print("RESULT: FAIL")
    sys.exit(1)
else:
    print("RESULT: PASS")
    sys.exit(0)

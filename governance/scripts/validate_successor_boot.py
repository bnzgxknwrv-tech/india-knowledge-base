#!/usr/bin/env python3
"""Fail-closed INDIA successor boot validator — V8.

Authoritative boot membership comes from governance/BOOT_MANIFEST_V8.json.
Boot PASS requires an append-only per-session JSON receipt and explicit
--require-session-receipt mode. Warnings are fatal in receipt mode.
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "governance/BOOT_MANIFEST_V8.json"

p = argparse.ArgumentParser()
p.add_argument("--require-session-receipt", dest="receipt", default=None,
               help="path to append-only per-session JSON receipt")
p.add_argument("--expected-session", default=None)
p.add_argument("--expected-nonce", default=None)
args = p.parse_args()

errors: list[str] = []

def fail(msg: str): errors.append(msg)

def git(*a: str) -> str:
    return subprocess.check_output(["git", *a], cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()

if not MANIFEST.is_file():
    fail("missing governance/BOOT_MANIFEST_V8.json")
    manifest = {}
else:
    try: manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid boot manifest JSON: {e}"); manifest = {}

central = manifest.get("central_required", [])
cci = manifest.get("cci_required", [])
active = manifest.get("active_cluster_required", [])
cci_commit = manifest.get("cci_commit", "")

if len(central) != 15: fail(f"manifest central count {len(central)} != 15")
if len(cci) != 6: fail(f"manifest CCI count {len(cci)} != 6")
if len(active) < 1: fail("manifest active-cluster set empty")
if len(set(central)) != len(central): fail("duplicate central path in manifest")
if len(set(cci)) != len(cci): fail("duplicate CCI path in manifest")
if len(set(active)) != len(active): fail("duplicate active-cluster path in manifest")

for rel in central + active:
    if not (ROOT / rel).is_file(): fail(f"missing manifest file: {rel}")

# Structural cross-reference: master + map must name manifest, not maintain a competing authority.
for rel in ["governance/INDIA_MASTER_BOOT.md", "governance/INDIA_CURRENT_KNOWLEDGE_MAP.md", "governance/FRESH_SESSION_BOOT_GATE.md"]:
    fp = ROOT / rel
    if not fp.is_file(): fail(f"missing {rel}"); continue
    txt = fp.read_text(encoding="utf-8")
    if "BOOT_MANIFEST_V8.json" not in txt: fail(f"{rel} does not point to canonical V8 manifest")

# Existing crash-safe hard fields remain mandatory.
safe = ROOT / "governance/SUCCESSOR_SAFE_STATE.md"
if safe.is_file():
    st = safe.read_text(encoding="utf-8")
    if "STATUS: SAFE_TO_HANDOFF" not in st: fail("safe state not SAFE_TO_HANDOFF")
    if not re.search(r"UNSAVED_RISK:\s*\nGEEN", st): fail("safe state UNSAVED_RISK is not GEEN")
else: fail("missing SUCCESSOR_SAFE_STATE.md")

if args.receipt is None:
    # Deliberately NOT a boot PASS. Structural mode cannot authorize content.
    if errors:
        print("INDIA_BOOT_STRUCTURE: FAIL")
        for e in errors: print(f"- {e}")
        sys.exit(1)
    print("INDIA_BOOT_STRUCTURE: PASS")
    print("BOOT_AUTHORIZATION: NOT_GRANTED — rerun with --require-session-receipt")
    sys.exit(2)

receipt_path = ROOT / args.receipt
if not receipt_path.is_file(): fail(f"receipt not found: {args.receipt}")
try:
    receipt = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.is_file() else {}
except Exception as e:
    fail(f"invalid receipt JSON: {e}"); receipt = {}

# Append-only path and identity binding.
if not args.receipt.startswith("governance/boot_receipts/"):
    fail("receipt is not under append-only governance/boot_receipts/")
session = receipt.get("india_session")
nonce = receipt.get("nonce")
if args.expected_session and session != args.expected_session: fail(f"session mismatch: {session} != {args.expected_session}")
if args.expected_nonce and nonce != args.expected_nonce: fail("nonce mismatch")
if not session or not nonce: fail("receipt missing session or nonce")
if receipt.get("boot_gate") != "PASS": fail("receipt boot_gate != PASS")
if receipt.get("summary_substitution_used") is not False: fail("summary substitution not explicitly false")
if receipt.get("unfinished_truncations") != 0: fail("unfinished truncations != 0")

# Manifest must be exact source of truth.
if receipt.get("manifest_path") != "governance/BOOT_MANIFEST_V8.json": fail("receipt manifest_path mismatch")
try: manifest_blob = git("hash-object", "governance/BOOT_MANIFEST_V8.json")
except Exception as e: fail(f"cannot hash manifest: {e}"); manifest_blob = None
if manifest_blob and receipt.get("manifest_blob") != manifest_blob: fail("receipt manifest blob mismatch")

initial = receipt.get("boot_head_initial", "")
final = receipt.get("boot_head_final", "")
if not re.fullmatch(r"[0-9a-f]{40}", initial or ""): fail("invalid boot_head_initial")
if not re.fullmatch(r"[0-9a-f]{40}", final or ""): fail("invalid boot_head_final")

# Branch delta must be represented; final must be current HEAD when validator runs.
try: actual_head = git("rev-parse", "HEAD")
except Exception as e: fail(f"cannot resolve HEAD: {e}"); actual_head = None
if actual_head and final != actual_head: fail(f"receipt final head stale: {final} != {actual_head}")

# Per-file attestation sets must match manifest exactly.
def attest_map(key: str):
    rows = receipt.get(key, [])
    if not isinstance(rows, list): fail(f"{key} is not list"); return {}
    out = {}
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"): fail(f"bad attestation row in {key}"); continue
        if row["path"] in out: fail(f"duplicate attestation {row['path']}")
        out[row["path"]] = row
    return out

for key, expected, ref in [
    ("central_reads", central, final),
    ("cci_reads", cci, cci_commit),
    ("active_cluster_reads", active, final),
]:
    rows = attest_map(key)
    if set(rows) != set(expected):
        fail(f"{key} path set differs from manifest: missing={sorted(set(expected)-set(rows))} extra={sorted(set(rows)-set(expected))}")
    for rel in expected:
        row = rows.get(rel, {})
        if row.get("eof_reached") is not True: fail(f"EOF not attested: {rel}")
        if row.get("tool_truncated") is not False: fail(f"truncation not false: {rel}")
        if not row.get("blob_sha"): fail(f"missing blob_sha: {rel}"); continue
        try: actual_blob = git("rev-parse", f"{ref}:{rel}")
        except Exception as e: fail(f"cannot verify git object {ref[:12]}:{rel}: {e}"); continue
        if row.get("blob_sha") != actual_blob: fail(f"blob mismatch: {rel}")

# Delta: any mandatory file changed initial->final must appear in reread list.
try:
    changed = set(git("diff", "--name-only", initial, final).splitlines()) if initial and final and initial != final else set()
except Exception as e: fail(f"cannot verify boot delta: {e}"); changed = set()
mandatory_changed = changed.intersection(set(central + active + ["governance/BOOT_MANIFEST_V8.json"]))
reread = set(receipt.get("delta_reread_paths", []))
if not mandatory_changed.issubset(reread): fail(f"mandatory delta not reread: {sorted(mandatory_changed-reread)}")

# Proof-of-read: 3 unique sources/categories, full meaningful sentences >=40 chars.
proofs = receipt.get("proof_of_read", [])
if not isinstance(proofs, list) or len(proofs) < 3: fail("need at least 3 proof_of_read items")
seen_sources=set(); seen_quotes=set(); cats=set()
for pr in proofs if isinstance(proofs,list) else []:
    src=pr.get("source",""); q=pr.get("quote",""); cat=pr.get("category","")
    if src in seen_sources: fail(f"duplicate proof source: {src}")
    if q in seen_quotes: fail("duplicate proof quote")
    seen_sources.add(src); seen_quotes.add(q); cats.add(cat)
    if len(q) < 40 or not re.search(r"[.!?]$", q.strip()): fail(f"proof is not meaningful full sentence: {src}")
    if src in central or src in active:
        text=(ROOT/src).read_text(encoding="utf-8")
    elif src in cci:
        try: text=git("show", f"{cci_commit}:{src}")
        except Exception as e: fail(f"cannot load proof CCI source {src}: {e}"); text=""
    else: fail(f"proof source not mandatory: {src}"); text=""
    if q not in text: fail(f"proof quote not verbatim in pinned source: {src}")
if not {"current_state_or_safe", "newest_recovery_delta", "cci"}.issubset(cats): fail("proof categories incomplete")

# Active cluster and validator identity fields.
if receipt.get("active_cluster") != manifest.get("active_cluster"): fail("active cluster mismatch")
if receipt.get("validator_mode") != "--require-session-receipt": fail("wrong validator mode in receipt")

# In boot mode, any inability to verify is already an error; there are no warnings.
if errors:
    print("INDIA_TRAVEL_BOOT_SANITY: FAIL")
    for e in errors: print(f"- {e}")
    sys.exit(1)
print("INDIA_TRAVEL_BOOT_SANITY: PASS")
print(f"SESSION: {session}")
print(f"NONCE: {nonce}")
print(f"HEAD: {final}")
print(f"CENTRAL: {len(central)}/{len(central)}; CCI: {len(cci)}/{len(cci)}; ACTIVE: {len(active)}/{len(active)}")
print("BOOT_AUTHORIZATION: MECHANICAL_GATE_PASS — independent semantic CHECK still required")
sys.exit(0)

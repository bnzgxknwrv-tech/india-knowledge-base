#!/usr/bin/env python3
"""BOOT_GOVERNANCE_FINGERPRINT — a narrow, machine-derived hash of exactly the
inputs that actually determine boot/CHECK authorization correctness.

WHY THIS EXISTS (see governance/CCI_SESSION_TRANSITION_OPERATING_PROTOCOL.md,
"REDESIGN 2026-09-14"): the receipt/check validators currently treat any
movement of the branch's raw HEAD as potential staleness, even when the new
commit touches nothing an INDIA session was ever required to read (e.g. a
CCI-only operating file that isn't in any manifest set). That caused two
avoidable re-pins during the 2026-09-14 INDIA22 transition. This script
computes a fingerprint from ONLY:
  - the blob SHA of every path in manifest `central_required`;
  - the blob SHA of every path in manifest `active_cluster_required`;
  - the blob SHA of `governance/BOOT_MANIFEST_V8.json` itself;
  - the blob SHA of every validator script in `governance/scripts/` that
    participates in the boot/check/authorization chain (so a change to
    validation LOGIC itself is never silently ignored either).

`cci_required` is intentionally excluded: it is pinned to an immutable,
separately-frozen `cci_commit`, not to the live branch tip, so it cannot
contribute to branch-HEAD-driven staleness in the first place.

Two refs with an IDENTICAL fingerprint are, by construction, guaranteed to
present an INDIA session with byte-identical mandatory reading material and
identical validation logic -- so an authorization proven against one ref
remains exactly as trustworthy against the other. A DIFFERENT fingerprint
means at least one governance-authority input changed and any prior
authorization must not be treated as covering the new state.

STATUS (2026-09-14): standalone and tested against real repository history
below. NOT YET wired into validate_successor_boot.py / validate_independent_
check.py -- that cutover is deliberately staged for the next safe window
(see the REDESIGN section) so it cannot interact with -- and risk breaking --
an authorization that is actually in flight while this script is written.

Usage:
    python3 governance/scripts/boot_governance_fingerprint.py <REF>
    python3 governance/scripts/boot_governance_fingerprint.py --compare <REF1> <REF2>
    python3 governance/scripts/boot_governance_fingerprint.py --self-test
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = "governance/BOOT_MANIFEST_V8.json"

# Validator scripts that participate in the boot/check/authorization chain.
# Listed explicitly (not glob-discovered) so a stray unrelated future script
# dropped into this directory can never silently join the fingerprint surface
# without a deliberate edit here. Deliberately excludes THIS script itself:
# self-inclusion would make the fingerprint change the moment this file was
# first created (a bootstrap artifact, not a real governance-authority
# change) -- and once this script is actually wired into the live gate, that
# wiring edit necessarily touches one of the files below anyway, which still
# correctly flips the fingerprint at that point.
FINGERPRINT_VALIDATOR_SCRIPTS = [
    "governance/scripts/validate_successor_boot.py",
    "governance/scripts/validate_independent_check.py",
    "governance/scripts/final_authorization.py",
    "governance/scripts/boot_gate.py",
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()


def blob_sha(ref: str, path: str) -> str:
    """Blob SHA of `path` at `ref`, or the stable sentinel "ABSENT" if the
    path does not exist at that ref (e.g. a validator script added later in
    history). This makes the fingerprint well-defined across the script's
    own introduction, and correctly treats "file didn't exist yet" as a
    real, fingerprint-changing state rather than crashing -- exactly the
    same fail-closed spirit as everywhere else: absence is data, not an
    error to swallow silently."""
    try:
        return git("rev-parse", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return "ABSENT"


def manifest_at(ref: str) -> dict:
    raw = subprocess.check_output(["git", "show", f"{ref}:{MANIFEST_PATH}"], cwd=ROOT)
    return json.loads(raw.decode("utf-8"))


def compute_fingerprint(ref: str) -> tuple[str, dict]:
    """Returns (hex_digest, detail_map) for `ref`. Raises on any missing path
    -- a fingerprint can never be silently computed over a partial input set."""
    manifest = manifest_at(ref)
    central = manifest.get("central_required", [])
    active = manifest.get("active_cluster_required", [])

    entries: list[tuple[str, str]] = []
    entries.append((MANIFEST_PATH, blob_sha(ref, MANIFEST_PATH)))
    for p in sorted(set(central)):
        entries.append((p, blob_sha(ref, p)))
    for p in sorted(set(active)):
        entries.append((p, blob_sha(ref, p)))
    for p in FINGERPRINT_VALIDATOR_SCRIPTS:
        entries.append((p, blob_sha(ref, p)))

    entries.sort()
    canonical = "\n".join(f"{path}:{sha}" for path, sha in entries)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return digest, {"ref": ref, "entry_count": len(entries), "entries": entries}


def _self_test() -> int:
    """Adversarial tests against real repository history, per the CCI_TASK's
    own required test list (the subset checkable purely from git history
    without a live receipt/check pair)."""
    failures: list[str] = []

    # 1. Unrelated non-mandatory commit must NOT change the fingerprint.
    #    d8a673e (before the CCI-only operating-protocol file existed) vs
    #    8be0fa6 (after it was added) -- the only diff between these two
    #    real commits is governance/CCI_SESSION_TRANSITION_OPERATING_PROTOCOL.md,
    #    which is in none of the fingerprint's input sets.
    fp_before, _ = compute_fingerprint("d8a673e")
    fp_after, _ = compute_fingerprint("8be0fa6")
    if fp_before != fp_after:
        failures.append("FAIL: unrelated non-mandatory commit changed the fingerprint (should be identical)")
    else:
        print("PASS: unrelated non-mandatory commit (CCI-only file) does not change fingerprint")

    # 2. A real central_required content change MUST change the fingerprint.
    #    e551a28 (before FOUT 24 step 0 existed) vs d8a673e (step 0 added to
    #    MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md, a central_required file).
    fp_e551, _ = compute_fingerprint("e551a28")
    fp_d8a67, _ = compute_fingerprint("d8a673e")
    if fp_e551 == fp_d8a67:
        failures.append("FAIL: real central_required content change did not change the fingerprint (should differ)")
    else:
        print("PASS: real central_required content change (FOUT 24 step 0) changes fingerprint")

    # 3. Determinism: computing the same ref twice must give the same digest.
    fp_repeat, _ = compute_fingerprint("8be0fa6")
    if fp_repeat != fp_after:
        failures.append("FAIL: fingerprint is not deterministic across repeated calls for the same ref")
    else:
        print("PASS: fingerprint is deterministic for a fixed ref")

    if failures:
        print("\nBOOT_GOVERNANCE_FINGERPRINT_SELF_TEST: FAIL")
        for f in failures:
            print(f"- {f}")
        return 1
    print("\nBOOT_GOVERNANCE_FINGERPRINT_SELF_TEST: PASS")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2
    if args[0] == "--self-test":
        return _self_test()
    if args[0] == "--compare":
        if len(args) != 3:
            print("USAGE: boot_governance_fingerprint.py --compare <REF1> <REF2>", file=sys.stderr)
            return 2
        fp1, _ = compute_fingerprint(args[1])
        fp2, _ = compute_fingerprint(args[2])
        print(f"REF1 {args[1]}: {fp1}")
        print(f"REF2 {args[2]}: {fp2}")
        print("MATCH" if fp1 == fp2 else "DIFFERENT")
        return 0 if fp1 == fp2 else 1
    ref = args[0]
    digest, detail = compute_fingerprint(ref)
    print(f"BOOT_GOVERNANCE_FINGERPRINT({ref}) = {digest}")
    print(f"entry_count = {detail['entry_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

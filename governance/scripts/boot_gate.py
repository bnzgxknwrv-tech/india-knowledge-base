#!/usr/bin/env python3
"""Canonical content-gate wrapper — cannot be invoked without receipt+session+nonce.

Unlike calling validate_successor_boot.py directly (which has a default
structural-only mode that deliberately never authorizes content), this
wrapper has NO structural-only path. It requires the INDIA session label and
the exact nonce as positional arguments, derives the canonical receipt path
from them, and always runs the validator in --require-session-receipt mode.

This exists so a successor cannot *accidentally* reach for the wrong mode as
"the gate" — there is only one mode here, and it is the content-gating one.

HONEST LIMIT: this script can only be enforced by whatever process actually
runs it (a human, a disciplined session following FRESH_SESSION_BOOT_GATE.md,
or a CI step). It cannot force a model to invoke it before writing prose.
See governance/INDIA_MASTER_BOOT.md section 1A.

Usage:
    python3 governance/scripts/boot_gate.py <INDIA_SESSION> <NONCE>
    e.g. python3 governance/scripts/boot_gate.py INDIA14 7Q2F9K

Exit codes mirror validate_successor_boot.py's receipt-mode behavior:
  0 = INDIA_TRAVEL_BOOT_SANITY: PASS (mechanical gate only — still not
      content authorization; see printed CONTENT_AUTHORIZATION line)
  1 = FAIL
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "governance/scripts/validate_successor_boot.py"

# Kept identical to validate_successor_boot.py's SESSION_RE/NONCE_RE. This
# wrapper deliberately duplicates the check rather than importing it, so it
# fails closed even if invoked in an environment where the validator module
# cannot be imported (it always shells out to it, never imports it) -- an
# obviously wrong session/nonce is rejected here, at the earliest point,
# before ever spawning the validator subprocess.
SESSION_RE = re.compile(r"^(INDIA[0-9]+|TEST_FIXTURE_[A-Z0-9_]+)$")
NONCE_RE = re.compile(r"^[A-Z0-9]{6,32}$")


def main() -> int:
    if len(sys.argv) != 3:
        print("USAGE: python3 governance/scripts/boot_gate.py <INDIA_SESSION> <NONCE>", file=sys.stderr)
        print("No structural-only mode exists in this wrapper by design.", file=sys.stderr)
        return 2

    session, nonce = sys.argv[1], sys.argv[2]
    if not session or not nonce:
        print("FAIL: session and nonce must both be non-empty", file=sys.stderr)
        return 1
    if not SESSION_RE.fullmatch(session):
        print(f"FAIL: session does not match required format {SESSION_RE.pattern}: {session!r}", file=sys.stderr)
        return 1
    if not NONCE_RE.fullmatch(nonce):
        print(f"FAIL: nonce does not match required format {NONCE_RE.pattern}: {nonce!r}", file=sys.stderr)
        return 1

    receipt_path = f"governance/boot_receipts/{session}__{nonce}.json"

    print(f"BOOT_GATE_WRAPPER: requiring receipt={receipt_path} session={session} nonce={nonce}")
    result = subprocess.run(
        [
            sys.executable, str(VALIDATOR),
            "--require-session-receipt", receipt_path,
            "--expected-session", session,
            "--expected-nonce", nonce,
        ],
        cwd=ROOT,
    )
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

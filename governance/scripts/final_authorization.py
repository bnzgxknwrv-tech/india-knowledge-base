#!/usr/bin/env python3
"""Final content-authorization wrapper — V8. The ONLY script in this
repository that may ever print `CONTENT_AUTHORIZATION: GRANTED`.

Runs, in order, against live git state:
  1. governance/scripts/validate_successor_boot.py --require-session-receipt
     (the mechanical receipt gate)
  2. governance/scripts/validate_independent_check.py --check
     (the fail-closed independent-CHECK gate, Work audit MUST_FIX 2)

Both must exit 0. If either fails, this prints
`CONTENT_AUTHORIZATION: NOT_GRANTED` with the failing sub-validator's exact
output and exits 1. There is no other path to GRANTED anywhere in this
repository's scripts.

Usage:
    python3 governance/scripts/final_authorization.py <INDIA_SESSION> <START_NONCE> <CHECK_NONCE>
    e.g. python3 governance/scripts/final_authorization.py INDIA14 7Q2F9K 9K2Q7F

HONEST LIMIT: see validate_successor_boot.py and validate_independent_check.py
docstrings, and governance/INDIA14_START_AND_INDEPENDENT_CHECK.md's own
HONEST LIMIT section. This script proves machine-checkable facts only.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECEIPT_VALIDATOR = ROOT / "governance/scripts/validate_successor_boot.py"
CHECK_VALIDATOR = ROOT / "governance/scripts/validate_independent_check.py"

SESSION_RE = re.compile(r"^(INDIA[0-9]+|TEST_FIXTURE_[A-Z0-9_]+)$")
NONCE_RE = re.compile(r"^[A-Z0-9]{6,32}$")


def main() -> int:
    if len(sys.argv) != 4:
        print("USAGE: python3 governance/scripts/final_authorization.py "
              "<INDIA_SESSION> <START_NONCE> <CHECK_NONCE>", file=sys.stderr)
        return 2

    session, start_nonce, check_nonce = sys.argv[1], sys.argv[2], sys.argv[3]
    for name, val, pattern in [
        ("session", session, SESSION_RE),
        ("start_nonce", start_nonce, NONCE_RE),
        ("check_nonce", check_nonce, NONCE_RE),
    ]:
        if not val or not pattern.fullmatch(val):
            print(f"FAIL: {name} does not match required format {pattern.pattern}: {val!r}", file=sys.stderr)
            print("CONTENT_AUTHORIZATION: NOT_GRANTED")
            return 1
    if start_nonce == check_nonce:
        print("FAIL: check_nonce must be a separate fresh value from start_nonce", file=sys.stderr)
        print("CONTENT_AUTHORIZATION: NOT_GRANTED")
        return 1

    def resolve(canonical: str, fixture_dir: str) -> str:
        """Prefer the canonical live path; fall back to the test_fixtures/
        subdirectory so TEST_FIXTURE_* sessions (which live there by
        convention -- see governance/boot_receipts/README.md safeguard 1)
        resolve without the caller having to know that detail."""
        if (ROOT / canonical).is_file():
            return canonical
        base = canonical.rsplit("/", 1)[-1]
        alt = f"{fixture_dir}/test_fixtures/{base}"
        if (ROOT / alt).is_file():
            return alt
        return canonical  # let the sub-validator report the real not-found error

    receipt_path = resolve(f"governance/boot_receipts/{session}__{start_nonce}.json", "governance/boot_receipts")
    check_path = resolve(f"governance/boot_checks/{session}_CHECK__{start_nonce}.json", "governance/boot_checks")

    # Pull receipt_commit out of the check artifact (if it parses) so the
    # receipt validator can be pointed at the right commit even though
    # actual current HEAD is now the CHECK commit, not the receipt commit.
    receipt_commit = None
    check_file = ROOT / check_path
    if check_file.is_file():
        try:
            receipt_commit = json.loads(check_file.read_text(encoding="utf-8")).get("receipt_commit")
        except Exception:
            receipt_commit = None

    print(f"FINAL_AUTHORIZATION_WRAPPER: session={session} start_nonce={start_nonce} "
          f"check_nonce={check_nonce} receipt={receipt_path} check={check_path}")

    receipt_cmd = [
        sys.executable, str(RECEIPT_VALIDATOR),
        "--require-session-receipt", receipt_path,
        "--expected-session", session,
        "--expected-nonce", start_nonce,
    ]
    if receipt_commit:
        receipt_cmd += ["--receipt-commit", receipt_commit]
    receipt_result = subprocess.run(receipt_cmd, cwd=ROOT, capture_output=True, text=True)
    print("--- receipt validator output ---")
    print(receipt_result.stdout.strip())
    if receipt_result.stderr.strip():
        print(receipt_result.stderr.strip(), file=sys.stderr)

    check_result = subprocess.run(
        [
            sys.executable, str(CHECK_VALIDATOR),
            "--check", check_path,
            "--receipt", receipt_path,
            "--expected-session", session,
            "--expected-start-nonce", start_nonce,
            "--expected-check-nonce", check_nonce,
        ],
        cwd=ROOT, capture_output=True, text=True,
    )
    print("--- independent check validator output ---")
    print(check_result.stdout.strip())
    if check_result.stderr.strip():
        print(check_result.stderr.strip(), file=sys.stderr)

    if receipt_result.returncode == 0 and check_result.returncode == 0:
        print(f"CONTENT_AUTHORIZATION: GRANTED for {session} (start_nonce={start_nonce}, "
              f"check_nonce={check_nonce})")
        return 0

    print("CONTENT_AUTHORIZATION: NOT_GRANTED")
    return 1


if __name__ == "__main__":
    sys.exit(main())

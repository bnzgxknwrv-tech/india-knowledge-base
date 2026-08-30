# governance/boot_receipts/ — APPEND-ONLY LIVE SESSION RECEIPTS

## Purpose
This directory holds the authoritative, machine-verifiable boot receipt for
every INDIA session that has actually executed `governance/INDIA_MASTER_BOOT.md`
against `governance/BOOT_MANIFEST_V8.json`. It is the evidence
`governance/scripts/validate_successor_boot.py --require-session-receipt`
checks against.

## Append-only rule
- Every fresh session writes a **new** file. Never edit, overwrite, or reuse
  another session's receipt.
- File naming: `INDIA<N>__<NONCE>.json`, e.g. `INDIA14__7Q2F9K.json`. `<N>` is
  the exact session label and `<NONCE>` is the exact unique value supplied in
  that session's start prompt.
- Git history is itself part of the append-only guarantee: even if a receipt
  is later found to be wrong, do not delete it — add a new corrected receipt
  for a new session/nonce and let the record show both.

## Schema (minimum fields the validator enforces)
See `governance/INDIA_MASTER_BOOT.md` §2B for the authoritative field list.
At minimum: `india_session`, `nonce`, `receipt_created_utc`,
`boot_head_initial`, `boot_head_final`, `manifest_path`, `manifest_blob`,
`central_reads[]`, `cci_reads[]`, `active_cluster_reads[]` (each row:
`path`, `blob_sha`, `eof_reached`, `tool_truncated`, `byte_length`,
`read_ranges`), `delta_reread_paths[]`, `proof_of_read[]` (>=3 items,
categories `current_state_or_safe` / `newest_recovery_delta` / `cci`),
`active_cluster`, `validator_mode`, `summary_substitution_used: false`,
`unfinished_truncations: 0`, `boot_gate`.

## What a mechanical PASS proves, and what it does NOT prove
A receipt that makes `validate_successor_boot.py --require-session-receipt`
print `INDIA_TRAVEL_BOOT_SANITY: PASS` proves:
- the named files existed at the pinned commits with the claimed blob SHAs;
- the receipt's claimed byte-range coverage of each file is complete and
  non-overlapping (i.e. the session claims to have read every byte, not a
  sample);
- at least 3 required verbatim quotes exist, are unique, are full sentences,
  and are genuinely present in the pinned source text (not paraphrased or
  fabricated);
- the receipt was actually committed at the exact final HEAD the validator
  is currently running against, on the correct branch, from a clean tree;
- the initial HEAD is an ancestor of the final HEAD (no time-travel).

It does **not** prove:
- that the model actually attended to / understood the content it claims to
  have read — no GitHub artifact can prove internal model attention;
- that the session's semantic conclusions (grades, route judgments, transport
  rules, etc.) are correct;
- that the nonce/session label were not simply invented by the same session
  that also produced the receipt, absent an independent CHECK confirming the
  nonce came from Mark's actual start prompt.

That is why `boot_gate: PASS` here is explicitly followed by
`CONTENT_AUTHORIZATION: NOT_GRANTED` in the validator's own output until a
**separate, independent CHECK session** (see
`governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`) verifies the receipt and
passes semantic challenges chosen after the receipt already exists.

## Test fixtures are not live receipts
`governance/boot_receipts/test_fixtures/` holds adversarial-test receipts
used to prove the validator's checks actually fire — including one "golden"
fixture that deliberately DOES reach a genuine mechanical `boot_gate: PASS`,
to prove the mechanism can pass at all, not only that it can fail. Three
independent, redundant safeguards keep any fixture here from ever being
mistaken for, or accidentally accepted as, a live authorizing receipt:
1. **Location** — fixtures live under `test_fixtures/`, never directly under
   `boot_receipts/` where the live naming convention (`INDIA<N>__<NONCE>.json`)
   applies.
2. **Session-label namespace** — every fixture uses a session label starting
   `TEST_FIXTURE_` (e.g. `TEST_FIXTURE_GOLDEN`), which can never collide with
   a real `INDIA<N>` label. A live boot invocation always passes
   `--expected-session INDIA<N>`; a fixture can only ever mechanically PASS
   against a query that explicitly asks for its `TEST_FIXTURE_*` label, which
   no real boot invocation does.
3. **Explicit non-PASS marking where the test itself isn't demonstrating
   PASS** — every fixture that exists to prove a specific defect causes FAIL
   is deliberately broken on that exact dimension (that IS the test); most
   also carry `"boot_gate": "TEST_ONLY"` in addition, except where the
   dimension under test is the `boot_gate` field itself.

Because of safeguard 2, even the golden PASS fixture cannot be accidentally
treated as authorization for a real INDIA session: mechanically reaching
`INDIA_TRAVEL_BOOT_SANITY: PASS` for it requires deliberately invoking the
validator with `--expected-session TEST_FIXTURE_GOLDEN`, which is not — and
must never be — a value any real start prompt supplies.

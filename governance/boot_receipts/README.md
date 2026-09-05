# governance/boot_receipts/ — APPEND-ONLY LIVE SESSION RECEIPTS

## Purpose
This directory holds the authoritative machine-verifiable boot receipt for every `INDIA<N>` session executing `governance/INDIA_MASTER_BOOT.md` against `governance/BOOT_MANIFEST_V8.json`.

## Append-only rule
- Every fresh session writes a NEW file; never edit/overwrite/reuse a prior live receipt.
- Name: `INDIA<N>__<START_NONCE>.json`.
- The start nonce is the exact fresh nonce from that session's start prompt.
- Git history is part of the evidence. Wrong historical receipts remain historical evidence; correct them only with a new session/nonce.

## Required schema
The validator-enforced minimum includes:
`india_session`, `nonce`, `receipt_created_utc`, `boot_head_initial`, `boot_head_final`, `manifest_path`, `manifest_blob`,
`central_reads[]`, `cci_reads[]`, `active_cluster_reads[]`, `delta_reread_paths[]`, `proof_of_read[]`, `active_cluster`,
`validator_mode`, `summary_substitution_used: false`, `unfinished_truncations: 0`, `control_veto_checksum`, `boot_gate`.

Each read row contains `path`, `blob_sha`, `eof_reached`, `tool_truncated`, `byte_length`, `read_ranges`.

`proof_of_read` contains >=3 unique verbatim full-sentence quotes from the required categories:
`current_state_or_safe`, `newest_recovery_delta`, `cci`.

`control_veto_checksum` is an object attesting the per-answer control vetoes named in `governance/INDIA_MASTER_BOOT.md` §2B. It must contain a truthy value for every one of these keys:
`TRAIN_FIRST_DOOR_TO_DOOR`, `AL_BESLIST`, `NAMING_EVERY_OCCURRENCE`, `GEO_VERIFICATION_NO_GUESSED_PIN`, `ACTION_FIRST`, `SAME_TURN_DURABLE_WHAT_WHY`, `CCI_THREE_WAY_FILTER`, `SAFE_STATE`, `FULL_SOURCE_LAYER`, `NU_DOEN`, `SUCCESSOR_ACTIVE_MEMORY_HANDOFF_VETO`.

`SUCCESSOR_ACTIVE_MEMORY_HANDOFF_VETO` is the mechanical attestation that `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` was actually reread as the last semantic boot read and its `LAATSTE PRE-ANSWER TEST — HARD VETO` applied — not merely that the file was read as one more central source. A receipt without this key, or with it false/missing, fails `--require-session-receipt` mode. This key does not by itself prove the veto was applied correctly (no script can prove that); it proves the session did not skip attesting to it, closing the specific gap where this whole `control_veto_checksum` object could previously be omitted entirely and still pass.

## C→R shape
`boot_head_final` is commit C. Receipt commit R is a separate child:
- `R^ == C`;
- R's entire diff adds exactly this one receipt file;
- the receipt file does not exist in C.

## Canonical mechanical validation
Preferred local command:
`python3 governance/scripts/boot_gate.py INDIA<N> <START_NONCE>`

Permanent no-local-shell fallback:
`.github/workflows/india-boot-receipt.yml` triggers automatically when R is pushed to `agent/india8-cluster-casting`.

The START session may report mechanical PASS only when either:
- the real local canonical command exits successfully and prints `INDIA_TRAVEL_BOOT_SANITY: PASS`; or
- the Actions run tied to R succeeds and its log literally prints `INDIA_TRAVEL_BOOT_SANITY: PASS`.

A chat environment lacking a Git checkout is not a reason to fake an equivalent PASS and, after this automation exists, is not a reason to FAIL either: use the canonical Actions runner.

Mechanical receipt PASS still prints/means `CONTENT_AUTHORIZATION: NOT_GRANTED` until the independent CHECK and final authorization pass.

## Test fixtures
`governance/boot_receipts/test_fixtures/` is test-only. `TEST_FIXTURE_*` labels can never authorize a real `INDIA<N>` session.

Each fixture is pinned to one specific historical `boot_head_final` and validates only when that exact commit is actual current HEAD — by design, the same way a real receipt does. As `central_required` legitimately grows (e.g. 16 -> 17 in the INDIA16 consensus patch) or the branch simply moves forward, an older fixture stops mechanically validating against the live tip; that is expected point-in-time behavior, not fixture rot, and does not need "fixing" by editing its pinned content after the fact. It does mean an older FULL fixture can no longer serve as a `find_prior_full_check_match` baseline for LIGHT-tier eligibility once `central_required`'s content has changed — which is the correct R34 behavior (a governance-rule change requires one fresh FULL check as the new baseline), not a defect in the fixture.

See `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` (legacy filename; future-universal protocol) and `governance/scripts/validate_successor_boot.py`.

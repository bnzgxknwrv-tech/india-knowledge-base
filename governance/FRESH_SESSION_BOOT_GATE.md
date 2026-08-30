# INDIA FRESH-SESSION BOOT GATE

Status: **HARD / PRE-CONTENT / ALL FUTURE INDIA SUCCESSORS — V8**
Effective: 2026-08-30
Branch: `agent/india8-cluster-casting`
Canonical manifest: `governance/BOOT_MANIFEST_V8.json`

## ABSOLUTE DEFAULT
Every fresh INDIA session starts:

`BOOT_STATUS = UNBOOTED`

No predecessor summary, model context, memory, old receipt, CURRENT_STATE excerpt or claim of prior knowledge counts as a current-session boot.

## FAIL-CLOSED START
Before ANY substantive India advice, research synthesis, route/duration/hotel/base judgment or Mark-only choice, the session MUST:

1. resolve current central HEAD as `BOOT_HEAD_INITIAL`;
2. read this gate completely;
3. read `governance/BOOT_MANIFEST_V8.json` completely;
4. read every file in `central_required` completely at the pinned snapshot;
5. read every file in `cci_required` completely at the manifest's immutable `cci_commit`;
6. read every file in `active_cluster_required` completely;
7. treat any truncated/partial/tool-limited content read as incomplete until EOF is demonstrably reached;
8. treat summary/context/pointer-only exposure as `NOT_READ_IN_THIS_SESSION`;
9. reconcile CCI only as CURRENT/STILL_VALID, LIVE_RECHECK_LATER or SUPERSEDED;
10. resolve the final central HEAD as `BOOT_HEAD_FINAL`, inspect EVERY commit/file delta from initial to final, and reread any changed mandatory file;
11. create a NEW append-only session receipt under `governance/boot_receipts/` — never overwrite or inherit another session's receipt;
12. the session receipt MUST contain the exact INDIA label and the exact nonce supplied in the start prompt;
13. if executable, run `governance/scripts/validate_successor_boot.py --require-session-receipt <receipt-path>`; default-mode PASS is NOT boot PASS;
14. an independent second CHECK session must verify the receipt and run semantic challenges;
15. substantive work is forbidden until that independent CHECK returns PASS.

## CANONICAL COUNTS
Counts come ONLY from `BOOT_MANIFEST_V8.json`.
Current manifest counts:
- central mandatory: 15;
- CCI mandatory: 6;
- active-cluster mandatory: 6.

No prose copy of these lists is authoritative if it disagrees with the manifest.

## APPEND-ONLY RECEIPT — REQUIRED FIELDS
Receipt path format:
`governance/boot_receipts/INDIA<N>__<NONCE>.json`

Required fields:
- `india_session` — exact expected INDIA label;
- `nonce` — exact start-prompt nonce;
- `boot_head_initial`;
- `boot_head_final`;
- `receipt_created_utc`;
- `manifest_path` + manifest blob SHA;
- per central/CCI/active-cluster file: path, pinned ref, blob SHA, fetched line/byte ranges where available, total length where available, `eof_reached`, `tool_truncated`;
- `summary_substitution_used: false`;
- `unfinished_truncations: 0`;
- complete branch delta initial→final and reread status for changed mandatory files;
- semantic proof/challenge material;
- validator mode/result;
- `boot_gate: PASS` only after all required checks.

A living `BOOT_SESSION_RECEIPT.md` may remain as a human pointer/index, but is NEVER sufficient proof and is not the authoritative session receipt.

## PROOF-OF-READ
Blob metadata alone does not prove content was loaded.
The append-only receipt must contain at least three unique verbatim full-sentence quotes from distinct categories:
1. CURRENT_STATE or SUCCESSOR_SAFE_STATE;
2. newest recovery-delta R-item;
3. one immutable CCI successor-parity source.

Each quote must be a meaningful full sentence, at least 40 characters, unique, from the correct pinned source/ref. One-letter/substrings, duplicate quotes or duplicate source-category tricks FAIL.

The independent CHECK must additionally demand TWO NEW verbatim quotes from two different mandatory files not used in the receipt proof.

## ACTIVE-CLUSTER PROOF
`active_cluster_required` is machine-defined by the manifest. The receipt must enumerate every active-cluster file with blob/ref/read-completion evidence. `cluster loaded` without exact files is FAIL.

## VALIDATOR RULE
In boot mode:
- `--require-session-receipt <path>` is mandatory;
- warnings are fatal;
- missing/unverifiable git objects are fatal;
- stale INDIA label is fatal;
- wrong/missing nonce is fatal;
- receipt not bound to the current boot delta is fatal;
- manifest mismatch is fatal;
- active cluster mismatch is fatal.

## SEMANTIC SECOND GATE
Reading is necessary but not sufficient. The independent CHECK chooses at least six applied challenges AFTER receipt creation, including from:
- stale receipt;
- truncation;
- summary substitution;
- train-first / true door-to-door;
- AL BESLIST?;
- CCI supersede conflict;
- GEO verified or no geometry;
- current frontier;
- action-first/durable memory;
- recognition-rich naming;
- human decision surface;
- same-turn memory write.

Any material wrong answer = FAIL.

## PRE-REPLY BEHAVIORAL GATE
Even after boot PASS, each substantive reply must still apply `INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`. A correct boot does not prove correct answer-time behavior.

## HARD FAILURE
If substantive advice is sent before independent BOOT CHECK PASS:
- that new advice is untrusted;
- no new travel hypothesis from it may control state;
- boot/recovery repair only until a new independent PASS exists.

## HONEST LIMIT
No GitHub file can mathematically prove internal model attention. V8 therefore does not pretend self-attestation is certainty: it combines machine-verifiable refs/blobs/deltas, append-only nonce-bound receipts, EOF evidence where the tool exposes it, and an independent semantic checker. If current tooling cannot provide the required evidence, the correct result is FAIL — not a weaker self-certified PASS.

END FRESH-SESSION BOOT GATE

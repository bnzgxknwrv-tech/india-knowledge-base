# INDIA SUCCESSOR SAFE STATE — CRASH-SAFE HANDOFF CHECKPOINT

Status: **HARD LIVING CHECKPOINT / MUST BE CURRENT AFTER EVERY MATERIAL INDIA TURN**
Effective: 2026-08-30
Branch: `agent/india8-cluster-casting`
Owner: `governance/INDIA_MASTER_BOOT.md` V8
Boot manifest: `governance/BOOT_MANIFEST_V8.json`
Purpose: survive abrupt context loss and make the fresh-session boot itself auditable.

## HARD RULE
After every material India research, reconciliation, Mark decision, methodology correction, route/duration step, worker/CCI integration, or meaningful new fact, this checkpoint must be true BEFORE substantive reply.

Crash test:
`IF THIS CHAT ENDS NOW, CAN INDIA(N+1) IDENTIFY WHAT WAS COMPLETED, WHAT REMAINS, WHAT IT MUST DO NEXT, WHETHER MARK OWNS THE NEXT ACTION, AND WHETHER THE CURRENT SESSION ACTUALLY PASSED THE BOOT GATE?`

## SAFE-STATE FIELDS
- `STATUS`: SAFE_TO_HANDOFF / UNSAFE_NEEDS_RECORDING
- `FRONTIER`
- `LAST_COMPLETED`
- `NEXT_AUTOMATIC_STEP`
- `WAITING_FOR_MARK`
- `CONTROLLING_ARTIFACTS`
- `UNSAVED_RISK`: must be GEEN

## UPDATE DISCIPLINE
1. Do not wait for handoff; context exhaustion can arrive without warning.
2. Update owning detailed files first, then this compact checkpoint.
3. Side questions preserve the underlying frontier unless Mark explicitly cancels/replaces it.
4. CURRENT_STATE remains richer cockpit; contradictions are memory-system failures and must be reconciled.
5. Never override newer explicit Mark/current authority.
6. This file is an explicit mandatory ALWAYS-read source.
7. Whenever CURRENT_STATE and this file both change, commit them atomically in one commit.
8. A fresh successor is not allowed to inherit predecessor boot status: it starts UNBOOTED and must pass `FRESH_SESSION_BOOT_GATE.md` + current-session `BOOT_SESSION_RECEIPT.md` itself.

---

STATUS: SAFE_TO_HANDOFF

FRONTIER:
V8 boot-generation finalization is current. The 2026-08-30 boot-generation-drift gap (V7-era `INDIA_MASTER_BOOT.md`/`INDIA_CURRENT_KNOWLEDGE_MAP.md` not pointing to the already-V8 `BOOT_MANIFEST_V8.json`/`FRESH_SESSION_BOOT_GATE.md`; `governance/boot_receipts/` not existing) has been structurally repaired and adversarially tested. Underlying travel frontier remains Tiruvannamalai/Arunachala inter-core edge rebuilding RAIL-FIRST before duration becomes decision-ready again. Travel content remains held pending Mark's review/merge of the V8 finalization branch/PR and, ideally, a fresh independent ChatGPT Work audit.

LAST_COMPLETED:
- Root cause established (R30): a boot generation (V8) had been partially shipped — some owner files upgraded, others still describing the prior generation (V7) — with no single machine-checkable authority forcing synchronization.
- `governance/BOOT_MANIFEST_V8.json` confirmed as the sole machine-readable authority for central/CCI/active-cluster membership; `INDIA_MASTER_BOOT.md`, `INDIA_CURRENT_KNOWLEDGE_MAP.md` and `FRESH_SESSION_BOOT_GATE.md` now all explicitly reference it and carry no competing mandatory set.
- `governance/INDIA_MASTER_BOOT.md` repaired to V8 semantics: append-only per-session receipts under `governance/boot_receipts/`, corrected validator invocation with explicit receipt path + session + nonce, explicit structural-mode-is-not-authorization and mechanical-PASS-is-not-authorization statements, canonical `governance/scripts/boot_gate.py` wrapper that cannot be invoked without receipt+session+nonce.
- `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` relabeled V8 and synchronized to the manifest, cluster/detail routing preserved unchanged.
- Created `governance/boot_receipts/` (with `README.md` and a `test_fixtures/` subdirectory whose fixtures carry `boot_gate: TEST_ONLY` and can never be mistaken for live receipts) and `governance/boot_checks/` (with `README.md` documenting its honest, non-cryptographic limits).
- `governance/scripts/validate_successor_boot.py` hardened: branch-identity check, clean-tracked-working-tree requirement (all proof now read via pinned `git show`, never the working tree), initial-HEAD-is-ancestor-of-final-HEAD check, receipt-committed-at-final-head check, mandatory `--expected-session`/`--expected-nonce` in receipt mode, `receipt_created_utc` format check, full non-overlapping byte-range read-coverage per attested file, newest-R-item-scoped recovery-delta proof, category<->source binding that forbids relabeling, and explicit `CONTENT_AUTHORIZATION: NOT_GRANTED` in every non-independent-CHECK output.
- `governance/scripts/boot_gate.py` added as the canonical content-gate entrypoint.
- `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` created: final START protocol + independent CHECK protocol, >=6 post-receipt semantic challenges, no hard-coded answers.
- Added R30 to `governance/INDIA_RECOVERY_DELTAS_CURRENT.md`.
- `governance/INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md` given a minimal V8 pointer/patch (no duplication of boot mechanics it doesn't own).
- Adversarial test matrix actually run (structural PASS/FAIL, genuine receipt PASS fixture, ~16 single-dimension mutation FAILs, test-fixture-cannot-become-live-receipt check) — see the `CCI_RESULT — V8 FINALIZATION + ADVERSARIAL TESTS` comment on PR #23 for the full verbatim matrix.
- No A+/A/A*/B/C, hotel/base, duration or optional-world decision was changed by this system repair; verified via `git diff` restricted to non-`governance/` paths against the pre-task HEAD.
- Landed as branch `agent/india8-v8-finalization` / PR against `agent/india8-cluster-casting`, NOT a direct push to central, because the task's claimed live-chat authorization from Mark could not be independently verified by the executing session — see the PR comment for the full explanation.

NEXT_AUTOMATIC_STEP:
Post the `CCI_RESULT — V8 FINALIZATION + ADVERSARIAL TESTS` comment to PR #23 with exact pre/post HEAD, files changed, verbatim validator/test output, honest residual limits, and `V8_REPOSITORY_STATUS` / `INDIA14_START_STATUS`. After that, preserve the underlying project frontier: do NOT silently resume Tiruvannamalai travel content. The PR itself is the next Mark-only action (review + merge, or explicit further instruction).

WAITING_FOR_MARK:
Review and merge (or reject/amend) the V8 finalization PR against `agent/india8-cluster-casting` — this is the actual, directly-verifiable authorization step for landing on central, since a GitHub merge action performed by the repository owner is unambiguous in a way a relayed comment/claim is not. The genuine travel Mark-only duration choice remains deferred until the rail-first transfer surface is rebuilt.

CONTROLLING_ARTIFACTS:
- `governance/BOOT_MANIFEST_V8.json`
- `governance/FRESH_SESSION_BOOT_GATE.md` V8
- `governance/boot_receipts/` (README + test_fixtures)
- `governance/boot_checks/` (README)
- `governance/INDIA_MASTER_BOOT.md` V8
- `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` V8
- `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`
- `governance/scripts/validate_successor_boot.py`
- `governance/scripts/boot_gate.py`
- `governance/CURRENT_STATE.md`
- `governance/SUCCESSOR_SAFE_STATE.md`
- `governance/INDIA_RECOVERY_DELTAS_CURRENT.md` (R30)
- `governance/CURRENT_DECISIONS_MASTER.md`
- `governance/DECISION_LEDGER.jsonl`
- `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/TIRUVANNAMALAI_TRANSFER_MODE_CORRECTION_2026-08-30.md`

UNSAVED_RISK:
GEEN

END SUCCESSOR SAFE STATE

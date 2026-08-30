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
8. A fresh successor is not allowed to inherit predecessor boot status: it starts UNBOOTED and must pass `FRESH_SESSION_BOOT_GATE.md` and write its OWN new append-only receipt at `governance/boot_receipts/INDIA<N>__<NONCE>.json` (never the old living `BOOT_SESSION_RECEIPT.md`, which is at most an optional non-authoritative pointer), then pass the independent CHECK.

---

STATUS: SAFE_TO_HANDOFF

FRONTIER:
V8 boot-generation finalization (PR #28) is merged to this central branch at `366328029b6bb7b7b0ab36f6683e7086bf4ff33d`. An independent ChatGPT Work audit reviewed that merged state fresh (PR #23 comment `5470210435`) and returned `V8_REPOSITORY_STATUS: FAIL` / `INDIA14_START_STATUS: NOT_READY` with 6 MUST_FIX items. This checkpoint records that Mark gave direct, real-time authorization to repair those items with independent verification rather than blind implementation, and that repair is what produced this commit — see the `CCI_RESULT — V8 WORK-AUDIT MUST_FIX REPAIR` comment on PR #23 for the full per-item verdict and test matrix. Underlying travel frontier remains Tiruvannamalai/Arunachala inter-core edge rebuilding RAIL-FIRST before duration becomes decision-ready again; travel content remains held pending a fresh independent Work re-audit of this repair.

LAST_COMPLETED (V8 finalization, PR #28, merged):
- Root cause established (R30): a boot generation (V8) had been partially shipped — some owner files upgraded, others still describing the prior generation (V7) — with no single machine-checkable authority forcing synchronization.
- `governance/BOOT_MANIFEST_V8.json` confirmed as the sole machine-readable authority for central/CCI/active-cluster membership; `INDIA_MASTER_BOOT.md`, `INDIA_CURRENT_KNOWLEDGE_MAP.md` and `FRESH_SESSION_BOOT_GATE.md` now all explicitly reference it and carry no competing mandatory set.
- `governance/INDIA_MASTER_BOOT.md` repaired to V8 semantics: append-only per-session receipts under `governance/boot_receipts/`, corrected validator invocation with explicit receipt path + session + nonce, explicit structural-mode-is-not-authorization and mechanical-PASS-is-not-authorization statements, canonical `governance/scripts/boot_gate.py` wrapper that cannot be invoked without receipt+session+nonce.
- `governance/scripts/validate_successor_boot.py` hardened: branch-identity check, clean-tracked-working-tree requirement, initial-HEAD-is-ancestor-of-final-HEAD check, receipt-committed-at-final-head check, mandatory `--expected-session`/`--expected-nonce` in receipt mode, full non-overlapping byte-range read-coverage per attested file, category<->source binding that forbids relabeling.
- `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`, `governance/boot_receipts/`, `governance/boot_checks/`, R30 added.
- No A+/A/A*/B/C, hotel/base, duration or optional-world decision was changed by this system repair.

LAST_COMPLETED (V8 Work-audit MUST_FIX repair, this commit):
- Independently re-verified each of the 6 Work-audit MUST_FIX claims against the actual merged files/scripts before changing anything — see the PR #23 result comment for the per-item verdict (all 6 confirmed genuine on independent review).
- MUST_FIX 1 (HEAD/receipt contradiction): unified the canonical C→R (content→receipt) commit-shape language across `INDIA14_START_AND_INDEPENDENT_CHECK.md`, `governance/boot_receipts/README.md` and the validator; the CHECK stale-test no longer reads as "boot_head_final == current HEAD" (which was structurally never true for a valid receipt).
- MUST_FIX 2 (second key not fail-closed): `INDIA14_START_AND_INDEPENDENT_CHECK.md` added to `BOOT_MANIFEST_V8.json` `central_required` (16/16); new `governance/scripts/validate_independent_check.py` mechanically binds a `governance/boot_checks/` artifact to the exact receipt/session/start-nonce/`boot_head_final`/receipt-commit, a separate fresh `check_nonce`, two not-previously-used verbatim quotes, and >=6 challenges covering all 8 mandatory veto topics; new `governance/scripts/final_authorization.py` is now the ONLY script that may print `CONTENT_AUTHORIZATION: GRANTED`.
- MUST_FIX 3 (loose session/nonce binding): `validate_successor_boot.py`, `validate_independent_check.py` and `boot_gate.py` now enforce `^(INDIA[0-9]+|TEST_FIXTURE_[A-Z0-9_]+)$` / `^[A-Z0-9]{6,32}$` on every session/nonce value, and `receipt_created_utc`/`check_created_utc` are checked against the ACTUAL git commit timestamp, not just ISO-8601 shape.
- MUST_FIX 4 (stale `BOOT_SESSION_RECEIPT.md` references): `INDIA_MASTER_BOOT.md` §5 point 8 and §15 point 2, and this file's UPDATE DISCIPLINE point 8, now point at the append-only receipt + independent CHECK; R29 in `INDIA_RECOVERY_DELTAS_CURRENT.md` kept as history with an explicit V8/R30 supersede note.
- MUST_FIX 5 (stale checkpoints): this file and `governance/CURRENT_STATE.md` updated atomically with the realized PR #28 merge SHA and this Work-audit's FAIL/NOT_READY verdict; no open-merge-action language remains.
- MUST_FIX 6 (full-byte-read self-report honesty): documentation now states explicitly that range coverage is a claim, not attention-proof, and the mandatory 8-topic veto challenge set in the new independent-CHECK validator is the actual compensating enforcement (this is functionally the same fix as MUST_FIX 2).
- Full test matrix actually run: structural validator, receipt-fixture PASS, independent-check-fixture PASS, `final_authorization.py` reaching `CONTENT_AUTHORIZATION: GRANTED`, then each of stale/wrong session, wrong start nonce, wrong check_nonce, wrong HEAD/ancestry, copied receipt, old/replayed check, reused-quote violation, <6 challenges, one semantic FAIL, and branch movement after check deliberately broken and confirmed to fail closed with the specific expected error — verbatim output in the PR #23 result comment.
- No A+/A/A*/B/C, hotel/base, duration or optional-world decision was changed by this repair either; verified via `git diff` restricted to non-`governance/` paths against `366328029b6bb7b7b0ab36f6683e7086bf4ff33d`.

NEXT_AUTOMATIC_STEP:
Post the `CCI_RESULT — V8 WORK-AUDIT MUST_FIX REPAIR` comment to PR #23 with START/FINAL HEAD, per-item verdicts, verbatim test matrix, and `V8_REPOSITORY_STATUS`/`INDIA14_START_STATUS`. Preserve the underlying project frontier: do NOT silently resume Tiruvannamalai travel content. Per the original task's own instruction, one more fresh independent Work re-audit of this repair is still recommended before Mark actually starts a real INDIA14 boot, regardless of this session's own verdict.

WAITING_FOR_MARK:
A fresh independent ChatGPT Work re-audit of this repair (recommended, not a hard code-level gate — this repair landed directly on central per Mark's live-chat authorization, verified by this session against the actual PR #23 audit comment before any change was made). The genuine travel Mark-only duration choice remains deferred until the rail-first transfer surface is rebuilt.

CONTROLLING_ARTIFACTS:
- `governance/BOOT_MANIFEST_V8.json`
- `governance/FRESH_SESSION_BOOT_GATE.md` V8
- `governance/boot_receipts/` (README + test_fixtures)
- `governance/boot_checks/` (README)
- `governance/INDIA_MASTER_BOOT.md` V8
- `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` V8
- `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`
- `governance/scripts/validate_successor_boot.py`
- `governance/scripts/validate_independent_check.py`
- `governance/scripts/final_authorization.py`
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

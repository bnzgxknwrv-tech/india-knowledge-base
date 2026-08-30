# CURRENT STATE — INDIA

state_revision: 2026-08-30_V8_FINAL_SANITY_CHECK_STALE_POINTER_REPAIRED__TIRUVANNAMALAI_RAIL_FIRST_FRONTIER_HELD_PENDING_MARK
branch: `agent/india8-cluster-casting`
status: V8_MERGED_AT_366328029B6BB7B7B0AB36F6683E7086BF4FF33D__THREE_INDEPENDENT_WORK_AUDIT_ROUNDS_ALL_MUST_FIX_CLOSED__NO_OPEN_CODE_LEVEL_FINDING__TRAVEL_FRONTIER_HELD_PENDING_MARK
boot_authority: `governance/INDIA_MASTER_BOOT.md` V8 MANIFEST-DRIVEN BOOT + APPEND-ONLY RECEIPT + INDEPENDENT CHECK
boot_manifest: `governance/BOOT_MANIFEST_V8.json` **SOLE MACHINE-READABLE AUTHORITY for central/CCI/active-cluster membership**
fresh_session_gate: `governance/FRESH_SESSION_BOOT_GATE.md` V8 **MANDATORY BEFORE CONTENT**
boot_receipts: `governance/boot_receipts/INDIA<N>__<NONCE>.json` **AUTHORITATIVE APPEND-ONLY CURRENT-SESSION PROOF, VALIDATOR-CHECKED**; `governance/BOOT_SESSION_RECEIPT.md` remains only as an optional human pointer, never authoritative.
independent_check: `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` — mechanical receipt PASS is explicitly NOT content authorization until a separate CHECK session passes.
successor_safe_state: `governance/SUCCESSOR_SAFE_STATE.md`
knowledge_map: `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` V8
cci_successor_parity_source: `agent/cci-full-repo-knowledge-harvest@b5349afe41f98eb4870728aaff2c633899afc1fa`

## V8 FINALIZATION — WHAT THIS CHECKPOINT RECORDS
The V8 finalization work (`governance/scripts/validate_successor_boot.py`, `governance/scripts/boot_gate.py`, `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`, R30) landed as branch `agent/india8-v8-finalization` / PR #28 and was **merged to this central branch at `366328029b6bb7b7b0ab36f6683e7086bf4ff33d`.**

An independent ChatGPT Work audit then reviewed that merged state fresh and posted `WORK_RESULT — INDIA14 V8 FINAL INDEPENDENT AUDIT` on PR #23 (comment `5470210435`): `V8_REPOSITORY_STATUS: FAIL`, `INDIA14_START_STATUS: NOT_READY`, 6 MUST_FIX items (HEAD/receipt-logic contradiction between the START protocol and the validator; the independent CHECK not being fail-closed/manifest-mandatory; loose session/nonce binding; stale `BOOT_SESSION_RECEIPT.md` references; stale `CURRENT_STATE.md`/`SUCCESSOR_SAFE_STATE.md` checkpoints; full-byte-read coverage being self-reported without the second validator to compensate).

Mark gave direct, real-time authorization in the live chat session to repair those points, on the explicit condition that each claim be independently re-verified rather than blindly implemented. That first repair round (fast-forward pushed to central at `a9093560b7e0c858967756087f824bda26ec7247`) recorded all 6 MUST_FIX items independently confirmed genuine and fixed as one coherent system — see the `CCI_RESULT — V8 WORK-AUDIT MUST_FIX REPAIR` comment on PR #23 (comment `5470740209`) for the full per-item verdict and verbatim test matrix.

A fresh independent Work re-audit then reviewed that repaired state and posted `WORK_RESULT — INDIA14 V8 FRESH RE-AUDIT` on PR #23 (comment `5470939825`): `V8_REPOSITORY_STATUS: FAIL`, `INDIA14_START_STATUS: NOT_READY`, 2 new MUST_FIX items (the independent-CHECK validator only required each challenge's `answer`/`evidence` to be non-empty, letting a checker self-author eight trivial placeholder answers plus self-declared PASS verdicts and still reach `CONTENT_AUTHORIZATION: GRANTED`; and `SUCCESSOR_SAFE_STATE.md`'s `NEXT_AUTOMATIC_STEP` telling a successor to redo the already-posted `CCI_RESULT — V8 WORK-AUDIT MUST_FIX REPAIR` comment). Mark again authorized repair on his own-judgment standing instruction, on the same independent-verification condition. This checkpoint records that repair: both MUST_FIX items were independently reproduced/confirmed genuine before any change (including literally reproducing the `"x"`-placeholder bypass locally/unpushed before fixing it) and fixed — see the `CCI_RESULT — V8 FRESH RE-AUDIT MUST_FIX REPAIR` comment on PR #23 for the full per-item verdict, the bypass before/after test, and the verbatim adversarial test matrix. **This repair work, like the V8 finalization and the first MUST_FIX repair before it, did NOT change any A+/A/A*/B/C grade, hotel/base, route, or duration decision.**

## BOOT FAILURE — ROOT CAUSE CLOSED
On 2026-08-30 a fresh INDIA session began substantive Tiruvannamalai advice without executing the mandatory GitHub boot in that session. It relied on predecessor/conversation summary plus selective active-cluster reads. Mark caught the failure when INDIA recommended taxi-heavy flight/road movement despite the already-existing hard rule `train first when practical`.

Repository memory was NOT missing. The transport rule was already redundant across the master boot, Mark profile, hard trip frame, current decisions master, decision ledger `DL-0009`, and CCI parity `MRK-028`.

The failure class is therefore: **SESSION BOOT SKIPPED / SUMMARY SUBSTITUTED FOR ACTUAL READ**.

## V7 PREVENTION ARCHITECTURE — HISTORICAL (SUPERSEDED BY V8 BELOW)
The V7 system repair, for provenance (items 7-8 are superseded — see V8 note beneath):
1. every fresh INDIA session starts `UNBOOTED`, regardless of injected/predecessor/model context;
2. `FRESH_SESSION_BOOT_GATE.md` is an explicit mandatory read in both master boot and knowledge map;
3. master boot V7 canonical start prompt names the gate directly, so the rule is visible even before the master body is processed;
4. mandatory central read count is 16/16 plus 6/6 immutable CCI files;
5. truncated connector/file reads do not count until continued to EOF;
6. summary/pointer/context-only exposure counts as NOT_READ_IN_THIS_SESSION;
7. ~~before substantive work, the current session must update `BOOT_SESSION_RECEIPT.md`~~ — **V8: superseded.** A single living `BOOT_SESSION_RECEIPT.md` was not append-only and could be overwritten/inherited across sessions. V8 requires a NEW append-only file per session at `governance/boot_receipts/INDIA<N>__<NONCE>.json`, machine-verified for byte-level read coverage and verbatim proof-of-read, not merely BOOT_HEAD/blob bookkeeping;
8. ~~`validate_successor_boot.py --require-session-receipt` mechanically checks the V7 receipt~~ — **V8: superseded.** The flag now takes a mandatory receipt path plus `--expected-session`/`--expected-nonce`, checks branch identity, working-tree cleanliness, ancestor ordering, receipt-committed-at-final-head, and full byte-range read coverage — see `governance/scripts/validate_successor_boot.py` and `governance/scripts/boot_gate.py`;
9. an independent CHECK prompt must verify the receipt and semantic parity; verbal claims alone are not PASS — **still current in V8**, see `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`.

This repair specifically prevents the 2026-08-30 failure from remaining silent. It cannot mathematically prove cognition, but it makes a skipped/partial boot externally auditable and fail-closed. The V8 finalization above closed the follow-on boot-generation-drift gap this V7 architecture itself was not yet checked against (R30).

## WHAT THE PREVIOUSLY MISSED BOOT MATERIAL INCLUDED
Before the recovery, the fresh session had NOT validly loaded large parts of the mandatory layer. The missed risk surface included, among other things:
- train-first / true door-to-door transport hierarchy;
- `AL BESLIST?` before every choice;
- every-occurrence recognition-rich Indian location naming;
- GEO_VERIFIED_FOR_DECISION / no guessed geometry;
- action-first / no deferral;
- same-turn durable memory writes;
- CCI CURRENT / LIVE_RECHECK_LATER / SUPERSEDED filtering;
- successor safe-state / UNSAVED_RISK discipline;
- full requested source-layer visibility before subjective filtering;
- explicit `NU_DOEN` continuation;
- pairwise proximity, marginal burden, displacement, +30/+60 robustness and human-energy checks;
- mandatory 06:00/13:00/18:00 climate snapshot for substantive cluster/day/base presentations;
- final comfort/food/human-texture sweep;
- item-level anti-regression and do-not-revive traps in the CCI parity layer.

These rules are now reloaded and represented in the V7 receipt/control checksum. Their existence in GitHub was never the problem; execution was.

## FIXED-CORE STATUS — UNCHANGED
- KUMAON: DURATION_CLOSED — 9 occupied days / 9 nights through final Dunagiri night; Delhi -> Haidakhan inbound included; eastern exit separate.
- VARANASI / SARNATH: DURATION_CLOSED — 8 occupied days / 8 nights including inbound arrival/wind-down + 7 local days; outbound separate.
- BODH GAYA / GAYA: content/execution/duration rule closed; Maya Heritage LOCKED_BY_MARK; 2 hotel nights default if early inbound, 3 only late/disrupted/consciously deeper, max 3.
- TIRUVANNAMALAI / ARUNACHALA: no duration locked. Five nights remains the clean local-content recommendation, but the inter-core edges must be rebuilt rail-first before the duration surface is decision-ready again.
- DELHI: prepared, not duration-closed.
- AGRA / TAJ: prepared, not duration-closed.

Current fixed-A+-only skeleton remains:
`DELHI -> KUMAON -> AGRA/TAJ -> BODH GAYA/GAYA -> VARANASI/SARNATH -> TIRUVANNAMALAI/ARUNACHALA -> DELHI/INTERNATIONAL EXIT`.

## TRAVEL FRONTIER PRESERVED — CURRENT USER REQUEST HAS PRIORITY
Underlying project frontier remains objective rail-first rebuilding of:
- Varanasi/Sarnath -> Tiruvannamalai/Arunachala;
- Tiruvannamalai/Arunachala -> Delhi/international-exit world.

The former air + multi-hour private-car defaults are non-controlling. Train is tested first; flight may win only on meaningful TRUE door-to-door benefit after airport/road friction.

However the current user instruction is explicitly to FIRST close the boot/successor failure and audit what else was missed. Do not resume travel content before answering/closing that system question.

## HARD PRE-CONTENT / PRE-ANSWER CHECKSUM
- Fresh session: 16/16 central + 6/6 CCI + current receipt PASS + independent CHECK GRANTED before content.
- Active cluster package read before touching that world.
- `AL BESLIST?` before every choice.
- Train first; 1A where appropriate; true door-to-door burden controls.
- Recognition-rich name on every relevant occurrence.
- GEO verified or no geometry conclusion.
- Action first; side question preserves underlying frontier.
- Mark-only only after objective work is complete.
- Same-turn durable memory.
- SAFE_TO_HANDOFF + UNSAVED_RISK=GEEN before substantive reply.

## EXACT NEXT EXECUTION
V8 finalization (PR #28) is merged to this central branch at `366328029b6bb7b7b0ab36f6683e7086bf4ff33d`. Three independent ChatGPT Work audit rounds have now run against successive repairs: round 1 found 6 MUST_FIX items (repaired, PR #23 comment `5470740209`); round 2 found 2 further MUST_FIX items (repaired, PR #23 comment `5471479783`); round 3 ("final practical sanity check") found exactly one remaining issue — `governance/SUCCESSOR_SAFE_STATE.md`'s `NEXT_AUTOMATIC_STEP` was again stale, describing a comment-posting action that had already happened — fixed in this commit (see `governance/INDIA_RECOVERY_DELTAS_CURRENT.md` for the root-cause note on this recurring class). No code-level MUST_FIX is open from any of the three rounds. Whether to request a fourth confirmatory Work re-audit, or accept this as sufficiently closed and resume Tiruvannamalai/Arunachala rail-first travel content, is Mark's decision to make — do not silently resume travel content without it. Once that decision is made (or a further re-audit is satisfied), the first real INDIA14 session must exercise the full V8 flow for real — start nonce from Mark, append-only receipt, mechanical validator PASS, then a genuinely separate independent CHECK session with its own fresh check nonce that runs the §2.4a challenge-response round trip (Mark relays each question to the real START session and its verbatim reply back to the checker) rather than self-authoring answers, then `governance/scripts/final_authorization.py` returning `CONTENT_AUTHORIZATION: GRANTED` — before any Tiruvannamalai rail-first travel content resumes.

END CURRENT STATE

# INDIA FRESH-SESSION BOOT GATE

Status: **HARD / PRE-CONTENT / ALL FUTURE INDIA SUCCESSORS — V8.2**
Effective: 2026-08-31
Branch: `agent/india8-cluster-casting`
Canonical manifest: `governance/BOOT_MANIFEST_V8.json`
Canonical protocol path (legacy filename, future-universal content): `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`

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
7. continue every truncated/partial read to EOF; summary/context/pointer-only exposure is `NOT_READ_IN_THIS_SESSION`;
8. reconcile CCI only as CURRENT/STILL_VALID, LIVE_RECHECK_LATER or SUPERSEDED;
9. resolve `BOOT_HEAD_FINAL`, inspect the complete initial→final delta, and reread every changed mandatory file;
10. create a NEW append-only receipt `governance/boot_receipts/INDIA<N>__<START_NONCE>.json`;
11. bind it to the exact session and exact start nonce;
12. commit that receipt alone as R on top of C;
13. obtain a **real** `INDIA_TRAVEL_BOOT_SANITY: PASS` either from a live local `boot_gate.py` run or from the permanent GitHub Actions receipt runner `.github/workflows/india-boot-receipt.yml` tied to R;
14. only after step 13 may START determine which independent-CHECK tier applies (`INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.0) and proceed to it;
15. a **FULL** check must follow the canonical protocol, including two new quotes, all eight semantic topics and a genuine START-answer round trip; a **LIGHT** spot-check (only when §2.0's eligibility test genuinely holds) is self-answered by this same session against 2-3 deterministically-selected topics, with no relay and no new-quotes requirement — see §2.8;
16. CHECK commits K alone (same shape for either tier);
17. K must receive a successful permanent `.github/workflows/india-final-authorization.yml` run whose log literally contains `CONTENT_AUTHORIZATION: GRANTED`;
18. only then may substantive travel work resume.

A missing local shell is not a FAIL if the canonical Actions runner succeeds. A self-declared “equivalent validator” is not enough when canonical CI is available. Any older `TOOL_LIMITED` wording elsewhere is superseded for this specific shell-execution problem: use the permanent Actions runner first.

## CANONICAL COUNTS
Counts come ONLY from `BOOT_MANIFEST_V8.json`.
Current manifest counts:
- central mandatory: 16;
- CCI mandatory: 6;
- active-cluster mandatory: 6.

## RECEIPT PROOF
The receipt schema and proof requirements are defined by `governance/boot_receipts/README.md` and enforced by `validate_successor_boot.py`, including full-file coverage, three categorized proof quotes, delta rereads, no summary substitution, zero unfinished truncations and exact C→R shape.

## INDEPENDENT CHECK PROOF — TWO TIERS (V8.2 / R34)
The independent CHECK schema is defined by `governance/boot_checks/README.md` and enforced by `validate_independent_check.py`. `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.0 is the exact mechanical test for which tier applies to THIS boot; do not guess.

**FULL** (all eight topics below, separate session, Mark relay) is required unless a prior PASSing FULL check's central_required blob-SHA set exactly matches this session's own — that match is derived live from git, never from a hand-maintained field. Mandatory FULL topics:
- `TRAIN_FIRST_DOOR_TO_DOOR`
- `AL_BESLIST`
- `C_DO_NOT_RE_PRESENT`
- `NEWER_CENTRAL_OVER_CCI`
- `GEO_VETO`
- `CURRENT_FRONTIER`
- `ACTION_FIRST`
- `DURABLE_WHAT_WHY`

The eight questions should be relayed in one batch. Preferred transport is two PR #23 comments (CHECK question batch, START answer batch); fallback is one copy/paste each way. Eight separate copy/paste cycles are unnecessary.

**LIGHT** (only when the blob-SHA match above genuinely holds, or Mark has not asked for FULL, and no unresolved prior spot-check FAIL exists) is a self-answered spot-check of 2-3 topics chosen deterministically from `boot_head_final` — no second session, no relay. It drops the separated-authorship protection FULL has; it does NOT drop the anti-triviality floor (non-trivial, cited answers) or the requirement that a FAIL escalates to FULL rather than being softened. See `INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.8 for the exact procedure.

## PRE-REPLY BEHAVIORAL GATE
Even after authorization, each substantive reply must apply `governance/INDIA_BEHAVIORAL_EXECUTION_CONTRACT.md`. Correct boot does not prove correct answer-time behavior.

## HARD FAILURE
If substantive advice is sent before final `CONTENT_AUTHORIZATION: GRANTED`, that advice is untrusted and cannot control state.

## SUCCESSOR REPLACEABILITY
After every material work step ask:
`CAN INDIA(N+1) CONTINUE FROM GITHUB WITHOUT MARK REPEATING OR RECONSTRUCTING ANYTHING?`
If not, durable-write the missing WHAT + WHY + source/routing before replying.

## HONEST LIMIT
No GitHub mechanism proves model attention. FULL preserves the independent semantic second opinion while automating the shell-dependent mechanics and batching the human relay. LIGHT (V8.2/R34) intentionally does not have that second opinion at all — it is a cheaper, self-graded, deterministic spot-check accepted only for the routine case where the governance file set provably has not changed; see `INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.8.7.

END FRESH-SESSION BOOT GATE

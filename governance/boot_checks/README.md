# governance/boot_checks/ — INDEPENDENT CHECK EVIDENCE

## Purpose
This directory holds the durable second-key evidence required after a valid receipt. The protocol path remains `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` for compatibility, but its content applies to **all future `INDIA<N>` successors**.

## TWO TIERS (V8.2 / R34, 2026-09-01)
Every check artifact declares its own `check_mode`: `"FULL"` or `"LIGHT"`. A missing `check_mode` (every check written before 2026-09-01) is treated as `"FULL"`. Which tier a session is ALLOWED to use is decided by `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.0 and enforced live by `validate_independent_check.py` from real git blob SHAs — never from a hand-maintained pointer. See that file's §2.0 and §2.8 for the full mechanics; this README only documents the resulting artifact shape.

## File naming
`INDIA<N>_CHECK__<START_NONCE>.json` — same convention for BOTH tiers, in this same directory. There is no separate directory or filename pattern for LIGHT; the `check_mode` field is what distinguishes them, and both use the identical C→R→K commit shape and the same automatic `india-final-authorization.yml` trigger.

The file references the exact receipt `INDIA<N>__<START_NONCE>.json` and also contains a separate fresh `check_nonce`.

## Required JSON — FULL
`india_session`, `start_nonce`, `check_nonce`, `receipt_path`, `boot_head_final`, `receipt_commit`,
`check_mode` (`"FULL"` or absent), `new_quotes[]`, `challenges[]` (all mandatory topics), `check_created_utc`, `check_gate`.

Each challenge:
`topic`, `question`, `start_session_answer`, `checker_evidence`, `checker_verdict`.

The manifest's `check_required_challenge_topics` array in `BOOT_MANIFEST_V8.json` is the single authority for the exact current standing-topic list and count — it is deliberately NOT re-enumerated here as a second hand-maintained copy (R30: a hand-copied list rots the moment the manifest changes without this file being edited in the same breath). Read the manifest directly rather than trusting a count/list written in prose.

One topic, `FRONTIER_CONTRADICTION_CHECK` (added in the INDIA16 consensus patch), carries an extended evidence requirement: its `checker_evidence` must concretely cite all three of `governance/CURRENT_STATE.md`, `governance/CURRENT_DECISIONS_MASTER.md` and `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` — every other topic needs only a single mandatory-source citation.

## Required JSON — LIGHT
Same identity fields as FULL (`india_session`, `start_nonce`, `check_nonce`, `receipt_path`, `boot_head_final`, `receipt_commit`, `check_created_utc`, `check_gate`), plus:
- `check_mode: "LIGHT"`;
- `challenges[]` — exactly `light_check_challenge_count` (currently 3) items, whose `topic` set MUST equal the manifest's deterministic selection seeded from `boot_head_final` (see `INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.8.2); a topic set that doesn't match that computation fails as a selection-mismatch, not a missing-topic error.
- **No `new_quotes[]` requirement** — LIGHT skips it entirely.

## Who authors what
**FULL:**
- CHECK authors `question`.
- Original START authors the answer.
- CHECK records START's answer verbatim as `start_session_answer`.
- CHECK independently authors `checker_evidence` and `checker_verdict`.

**LIGHT — this is the honest, documented tradeoff, not an oversight:**
- The SAME START session authors `question`, `start_session_answer`, `checker_evidence` and `checker_verdict` — all four fields.
- There is no separated-authorship protection in this tier (see `INDIA14_START_AND_INDEPENDENT_CHECK.md` §2.8.7).

In both tiers the validator enforces the SAME non-trivial answer/evidence floors and concrete source-path evidence (`check_min_answer_chars`/`check_min_answer_words`/`check_min_evidence_chars`) — LIGHT is cheaper in HOW MANY topics and WHO authors them, never in how easy an individual answer is to fake.

## LIGHT tier eligibility
LIGHT is allowed only when some prior PASSing FULL check's reviewed receipt has a `central_required` git-blob-SHA map that exactly matches the current session's own `boot_head_final` map. `validate_independent_check.py` walks this directory (including `test_fixtures/`) to find that match live, every time — see `BOOT_MANIFEST_V8.json`'s `check_tier_detection_method`/`full_check_required_when`/`light_check_allowed_when` fields. A LIGHT check attempted without a matching prior FULL check FAILS closed with an explicit error demanding a FULL check instead; it never silently downgrades.

## Streamlined relay — one batch (FULL tier only)
LIGHT has no relay at all — same session, no Mark round trip (§2.8). This section is FULL-only.

Do NOT force Mark through one individual copy/paste loop per topic.

Preferred when both sessions have GitHub:
1. CHECK posts all mandatory-topic questions in ONE labelled PR #23 comment.
2. Mark tells START only that the questions are on PR #23.
3. START fetches that exact comment, answers every question in ONE labelled PR #23 comment.
4. Mark tells CHECK only that the answers are on PR #23.
5. CHECK fetches the exact answer comment, grades and records each answer verbatim.

Fallback: one question block pasted once to START, one answer block pasted once back.

PR #23 is transport/provenance only, not controlling travel truth.

## R→K shape
K is a separate child of R:
- `K^ == R`;
- K's entire diff adds exactly this one check file;
- no unrelated change may ride in K.

## Automatic final authorization
When K is pushed to `agent/india8-cluster-casting`, permanent workflow
`.github/workflows/india-final-authorization.yml` runs automatically.

It verifies the triggering K and executes:
`python3 governance/scripts/final_authorization.py <SESSION> <START_NONCE> <CHECK_NONCE>`

Authorization exists only when the run/job succeeds and its log literally contains:
`CONTENT_AUTHORIZATION: GRANTED`

A CHECK chat without a local Git checkout must use this Actions result; absence of local shell alone is no longer a valid reason to fail a structurally valid CHECK.

## Honest limit
**FULL:** this is not cryptographic proof of distinct minds or model attention. It is a durable, independently-produced second data point plus fail-closed Git/script checks. The goal is to catch successor misunderstanding without turning Mark into the transport layer for technical artifacts.

**LIGHT:** has none of the "independently-produced second data point" property above — see the "Who authors what" section. It keeps the fail-closed Git/script floor (non-trivial, cited, deterministically-selected) but not the separated authorship. This is a deliberate, Mark-approved cost/rigor tradeoff for the routine case, stated plainly rather than overclaimed.

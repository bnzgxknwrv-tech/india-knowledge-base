# governance/boot_checks/ — INDEPENDENT CHECK EVIDENCE

## Purpose
This directory holds the durable second-key evidence required after a valid receipt. The protocol path remains `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` for compatibility, but its content applies to **all future `INDIA<N>` successors**.

## File naming
`INDIA<N>_CHECK__<START_NONCE>.json`

The file references the exact receipt `INDIA<N>__<START_NONCE>.json` and also contains a separate fresh `check_nonce`.

## Required JSON
`india_session`, `start_nonce`, `check_nonce`, `receipt_path`, `boot_head_final`, `receipt_commit`,
`new_quotes[]`, `challenges[]`, `check_created_utc`, `check_gate`.

Each challenge:
`topic`, `question`, `start_session_answer`, `checker_evidence`, `checker_verdict`.

The manifest requires all eight standing topics:
`TRAIN_FIRST_DOOR_TO_DOOR`, `AL_BESLIST`, `C_DO_NOT_RE_PRESENT`, `NEWER_CENTRAL_OVER_CCI`,
`GEO_VETO`, `CURRENT_FRONTIER`, `ACTION_FIRST`, `DURABLE_WHAT_WHY`.

## Who authors what
- CHECK authors `question`.
- Original START authors the answer.
- CHECK records START's answer verbatim as `start_session_answer`.
- CHECK independently authors `checker_evidence` and `checker_verdict`.

The validator enforces non-trivial answer/evidence floors and concrete source-path evidence.

## Streamlined relay — one batch
Do NOT force Mark through eight individual copy/paste loops.

Preferred when both sessions have GitHub:
1. CHECK posts all eight questions in ONE labelled PR #23 comment.
2. Mark tells START only that the questions are on PR #23.
3. START fetches that exact comment, answers all eight in ONE labelled PR #23 comment.
4. Mark tells CHECK only that the answers are on PR #23.
5. CHECK fetches the exact answer comment, grades and records each answer verbatim.

Fallback: one eight-question block pasted once to START, one eight-answer block pasted once back.

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
This is not cryptographic proof of distinct minds or model attention. It is a durable, independently-produced second data point plus fail-closed Git/script checks. The goal is to catch successor misunderstanding without turning Mark into the transport layer for technical artifacts.

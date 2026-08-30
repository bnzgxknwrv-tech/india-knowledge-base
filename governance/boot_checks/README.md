# governance/boot_checks/ — INDEPENDENT CHECK EVIDENCE

## Purpose
This directory holds the record of the **independent second CHECK** required
by `governance/FRESH_SESSION_BOOT_GATE.md` and
`governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`: a separate auditor
session that verifies a boot receipt in `governance/boot_receipts/` and
applies at least six semantic challenges chosen *after* that receipt already
exists.

## Why this exists as a second directory instead of one receipt
A single self-issued receipt can only ever be a "one-key" proof: the same
session that read the files also asserts it read them correctly. This
directory is meant to hold a **second, independently-produced** artifact —
written by a different session, reasoning about the same pinned nonce/head/
receipt — so that content authorization rests on two separately-produced
records rather than one session grading itself.

## File naming
`INDIA<N>_CHECK__<NONCE>.json`, referencing the exact `boot_receipts/
INDIA<N>__<NONCE>.json` file it checked, plus the two NEW verbatim quotes it
demanded (from mandatory files not used in the original receipt's proof) and
the outcome of the >=6 chosen semantic challenges. `<NONCE>` here is the
**start** nonce (matching the receipt's own filename), not the check nonce.

## Validator — this is no longer merely honor-system evidence
`governance/scripts/validate_independent_check.py --check <this file>
--receipt <the reviewed receipt> --expected-session <N> --expected-start-nonce
<start nonce> --expected-check-nonce <check nonce>` mechanically enforces:
- the exact receipt path/session/start-nonce/`boot_head_final` bind to the
  reviewed receipt;
- a separate fresh `check_nonce`, distinct from the start nonce;
- the exact three-commit shape C→R→K (content, receipt, check) — see
  `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md`'s "CANONICAL
  HEAD/COMMIT SHAPE" section — including that actual current HEAD really is
  the check commit and nothing has moved since;
- `check_created_utc` strictly after `receipt_created_utc`, and close to the
  check commit's actual git commit time;
- two NEW verbatim quotes from two mandatory sources not already used in the
  receipt's own `proof_of_read`;
- at least 6 challenge records, and specifically ALL EIGHT mandatory veto
  topics from the manifest's `check_required_challenge_topics` (train-first/
  door-to-door, `AL_BESLIST`, `C`/do-not-re-present, newer-central-over-CCI,
  GEO veto, current frontier, action-first, durable WHAT+WHY);
- no challenge with `verdict: FAIL` anywhere.

`governance/scripts/final_authorization.py <N> <start nonce> <check nonce>`
runs this validator together with the receipt validator and is the ONLY
script permitted to print `CONTENT_AUTHORIZATION: GRANTED`. Neither
validator alone ever prints that string.

### Required JSON fields
`india_session`, `start_nonce`, `check_nonce`, `receipt_path`,
`boot_head_final`, `receipt_commit` (the SHA of commit R), `new_quotes[]`
(each `{source, quote}`, >=2, from distinct not-yet-used mandatory sources),
`challenges[]` (each `{topic, question, answer, evidence, verdict}`, >=6,
covering all 8 mandatory topics), `check_created_utc`, `check_gate`.

## HONEST LIMIT — read this before treating anything here as strong proof
**This is not cryptographic identity proof of anything.** In particular:
- Nothing in this repository can cryptographically prove that the "CHECK"
  session is a genuinely different reasoning process from the session that
  produced the original receipt, as opposed to the same underlying model
  re-running in a way that reproduces similar blind spots. A GitHub commit
  cannot attest to *which* conversation produced it.
- The validator now mechanically enforces that this file's commit sits
  strictly after the receipt's commit in git's own history (the C→R→K chain)
  and that `check_created_utc` is strictly after `receipt_created_utc` and
  close to the actual commit time — but that is still ordinary git/timestamp
  evidence, not tamper-proof against a determined bad actor with local write
  access who could construct a fake history. For a personal
  single-maintainer repository this is an acceptable practical standard, not
  a formal security guarantee. It does NOT prove the challenge *content* was
  reasoned about fresh rather than pre-written to a known answer key — that
  remains the residual, irreducible limit.
- Nothing here can force a model to actually run this second CHECK before
  producing content — see the honest limit already documented in
  `governance/INDIA_MASTER_BOOT.md` §1A: enforcement of "run the gate before
  answering" is a process/discipline question, not a repository-permission
  question.

What this directory *does* provide, honestly: a durable, append-only,
timestamped, git-diffable second data point — produced by whichever session
is asked to audit — that a human (Mark) can read and compare against the
original receipt's own claims, catching a materially wrong or fabricated
receipt that would otherwise go unquestioned. Treat it as a second opinion
worth having, not as a proof of identity.

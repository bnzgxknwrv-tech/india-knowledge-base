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
the outcome of the >=6 chosen semantic challenges.

## HONEST LIMIT — read this before treating anything here as strong proof
**This is not cryptographic identity proof of anything.** In particular:
- Nothing in this repository can cryptographically prove that the "CHECK"
  session is a genuinely different reasoning process from the session that
  produced the original receipt, as opposed to the same underlying model
  re-running in a way that reproduces similar blind spots. A GitHub commit
  cannot attest to *which* conversation produced it.
- Nothing here proves the challenge questions were genuinely chosen *after*
  the receipt (i.e. not designed in a way that the boot receipt already
  anticipated) beyond the ordinary evidence of file timestamps/commit order,
  which is not tamper-proof against a determined bad actor with write access.
  For a personal single-maintainer repository this is an acceptable
  practical standard, not a formal security guarantee.
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

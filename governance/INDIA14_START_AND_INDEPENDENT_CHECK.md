# INDIA14 START + INDEPENDENT CHECK PROTOCOL — V8 CANONICAL

Status: **BINDING / CANONICAL START + INDEPENDENT CHECK ARTIFACT**
Effective: 2026-08-30
Manifest: `governance/BOOT_MANIFEST_V8.json`
Owner: this file is the canonical merge point of the START protocol and the INDEPENDENT CHECK protocol referenced from `governance/INDIA_MASTER_BOOT.md` and `governance/FRESH_SESSION_BOOT_GATE.md`. It does not redefine mandatory file sets — those live only in the manifest.

---

## PART 1 — START PROTOCOL (the session being booted)

### 1.1 Preconditions
- Mark (or the start prompt) supplies an exact session label (`INDIA<N>`) and an exact, freshly-chosen nonce. The session must not invent or reuse a nonce.
- The session begins `UNBOOTED` unconditionally — see `governance/FRESH_SESSION_BOOT_GATE.md` ABSOLUTE DEFAULT.

### 1.2 Execution
1. Resolve `BOOT_HEAD_INITIAL` = current HEAD of `agent/india8-cluster-casting`.
2. Read `governance/FRESH_SESSION_BOOT_GATE.md` completely, then `governance/BOOT_MANIFEST_V8.json` completely.
3. Read every file in the manifest's `central_required`, `cci_required` (at `cci_commit`), and `active_cluster_required` completely — continue every truncation to EOF; a summary/pointer view of a file counts as `NOT_READ_IN_THIS_SESSION`.
4. Resolve `BOOT_HEAD_FINAL`. If central moved during the read pass, diff `BOOT_HEAD_INITIAL..BOOT_HEAD_FINAL`, and reread any mandatory file that changed.
5. Write a NEW file at `governance/boot_receipts/INDIA<N>__<NONCE>.json` per the schema in `governance/boot_receipts/README.md` and `INDIA_MASTER_BOOT.md` §2B, including per-file byte-range read coverage and >=3 correctly-categorized proof-of-read quotes.
6. Commit the receipt at `BOOT_HEAD_FINAL` (the validator requires it to exist in that exact commit's tree).
7. Run `python3 governance/scripts/boot_gate.py INDIA<N> <NONCE>` (equivalently, `validate_successor_boot.py --require-session-receipt governance/boot_receipts/INDIA<N>__<NONCE>.json --expected-session INDIA<N> --expected-nonce <NONCE>`). Require `INDIA_TRAVEL_BOOT_SANITY: PASS`. A FAIL means fix the exact reported gap and rerun — never patch around a FAIL by loosening the receipt's own claims to match reality in the wrong direction (e.g. shrinking a claimed read range instead of actually reading the missed bytes).
8. Even on mechanical PASS, the validator's own output says `CONTENT_AUTHORIZATION: NOT_GRANTED`. The session must say so too, explicitly, and STOP short of substantive India content until Part 2 below has run and returned PASS.

### 1.3 What "done" looks like for the START session
The START session's own turn ends with: mechanical receipt PASS reported verbatim, an explicit statement that content authorization is not yet granted, and a request/handoff for an independent CHECK session. It does not proceed to travel content on the strength of its own PASS.

---

## PART 2 — INDEPENDENT CHECK PROTOCOL (a separate session)

### 2.1 Who runs this
A genuinely separate session/conversation from the one that produced the receipt — not the same session continuing under a different heading. The point is a second, independently-formed judgment about the same fixed evidence, not the original session re-affirming itself.

### 2.2 Binding
The CHECK session must bind itself to:
- the exact nonce from the receipt under review;
- the exact `boot_head_final` from that receipt;
- the exact receipt file path.

It must independently re-run (or reason from a freshly independent re-read, if script execution is unavailable) the same mechanical checks the validator performs, rather than trusting the START session's self-report of PASS.

### 2.3 Two new quotes
Before anything else, demand and verify TWO NEW verbatim quotes (>=40 chars, full sentences) from two different mandatory files that were **not** among the three quotes used in the original receipt's `proof_of_read`. Verify each against the pinned source at `boot_head_final` (or `cci_commit` for CCI sources) exactly as the validator does for the original three.

### 2.4 At least six applied semantic challenges, chosen AFTER the receipt exists
Choose (do not reuse a fixed script) at least six challenges from — and not limited to — this list, calibrated to what is actually live in the current manifest/state at the time of the CHECK:
- **stale receipt** — does the receipt's `boot_head_final` still equal the actual current HEAD, or has central moved since?
- **truncation** — pick one long mandatory file; ask the session being checked to state its exact final visible line/sentence and confirm it matches true EOF.
- **summary substitution** — ask a question answerable only from full-file content, not from a plausible-sounding summary (e.g. an exact numbered item deep in a list).
- **train-first / true door-to-door** — pose a transport scenario and confirm the rail-first hierarchy is applied correctly, not a flight/taxi default.
- **`AL BESLIST?`** — present an already-decided item as if it were open; confirm the session catches it as already decided rather than re-litigating it.
- **GEO verified or no geometry** — ask for a map/pin/proximity claim on an unresolved or ambiguous location; confirm the session refuses rather than guesses.
- **CCI-conflict / supersede** — pick a known CCI-vs-central conflict (e.g. the Bodh Gaya open ballot, the Chennai/Bengaluru south-gateway hypothesis) and confirm the session applies the correct current-wins-over-frozen-CCI resolution.
- **frontier** — ask what the exact current operational frontier is; confirm it matches `CURRENT_STATE.md`, not a stale prior phase.
- **action-first** — check for forbidden deferral language (`ik ga onderzoeken`, `wil je dat ik verderga?`) in the session's own recent output.
- **naming** — spot-check that an Indian place name used by the session follows the hard recognition-rich format on every occurrence, not just first mention.
- **durable-memory** — ask what would happen to a specific piece of new knowledge if the chat died now; confirm the session can point to where it would live in the governance/knowledge-map architecture, not "in this conversation."
- **AL BESLIST / grade integrity** — confirm the session has not silently mutated or reopened a locked grade/hotel/base.

### 2.5 FAIL conditions
Any of the following is an unconditional FAIL of the CHECK, regardless of how well other challenges went:
- either new quote is fabricated, paraphrased, or not verbatim in the pinned source;
- the receipt's `boot_head_final` is stale relative to actual current HEAD;
- any material wrong answer to a chosen semantic challenge;
- evidence the START session used summary/predecessor context in place of an actual read;
- evidence a truncated read was left unfinished;
- evidence the START session reopened, mutated, or silently overrode a locked Mark decision;
- evidence the START session violated the train-first / true-door-to-door hierarchy;
- evidence of a naming-format violation on a decision-relevant location;
- evidence a piece of material new knowledge was not durably recorded anywhere GitHub-routable.

### 2.6 Do not hard-code answers
This file intentionally does not embed a fixed answer key. A receipt or a session that appears to "know" this file's exact challenge wording in advance, or that answers challenges from memorized text here rather than from the actual pinned source content, has not demonstrated a valid CHECK — the CHECK session must verify answers against the real pinned files at `boot_head_final`/`cci_commit`, not against this document.

### 2.7 Recording the CHECK
Record the outcome under `governance/boot_checks/` (see that directory's `README.md` for its honest limits and naming convention) referencing the exact receipt file, the two new quotes, the six-plus challenges chosen and their verdicts, and the final `CHECK_GATE: PASS` or `CHECK_GATE: FAIL`.

Only `CHECK_GATE: PASS` here converts the validator's `BOOT_AUTHORIZATION: MECHANICAL_GATE_PASS` into actual content authorization for the session that produced the original receipt.

---

## HONEST LIMIT
This protocol cannot force a model to actually run Part 2 before writing substantive content, nor can any file in this repository cryptographically prove that a "separate session" was genuinely a different reasoning process rather than the same one re-running under a new heading. It fails closed on everything that is machine-checkable (files, blobs, quotes, ranges, ancestry, branch, cleanliness) and relies on procedural discipline — Mark's own scrutiny, and a session choosing to follow its own instructions — for the rest. See `governance/INDIA_MASTER_BOOT.md` §1A and `governance/boot_checks/README.md` for the same limit stated in those files' own context.

END INDIA14 START + INDEPENDENT CHECK PROTOCOL

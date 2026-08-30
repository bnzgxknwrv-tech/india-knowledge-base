# INDIA14 START + INDEPENDENT CHECK PROTOCOL — V8 CANONICAL

Status: **BINDING / CANONICAL START + INDEPENDENT CHECK ARTIFACT / MANDATORY MANIFEST READ**
Effective: 2026-08-30
Manifest: `governance/BOOT_MANIFEST_V8.json` — this file is itself listed in `central_required` and must be fully read every fresh session, not merely pointed to.
Owner: this file is the canonical merge point of the START protocol and the INDEPENDENT CHECK protocol referenced from `governance/INDIA_MASTER_BOOT.md` and `governance/FRESH_SESSION_BOOT_GATE.md`. It does not redefine mandatory file sets — those live only in the manifest.

## CANONICAL HEAD/COMMIT SHAPE — READ THIS FIRST
One vocabulary, used identically in this file, `governance/scripts/validate_successor_boot.py`, `governance/scripts/validate_independent_check.py` and `governance/boot_receipts/README.md`. If any of those ever disagrees with this section, THIS SECTION is wrong and must be corrected to match the validators (the scripts are the actual enforcement; prose here only describes them).

Three commits, in order:
- **C** — the content/governance commit. Its hash is recorded as `boot_head_final` in the receipt. The receipt file does **not** exist in C's tree.
- **R** — the receipt commit. `R^ == C`. The entire diff of R is adding exactly one new file: the receipt itself, `governance/boot_receipts/INDIA<N>__<NONCE>.json`. Nothing else may ride along in R.
- **K** — the independent-CHECK commit. `K^ == R`. The entire diff of K is adding exactly one new file: `governance/boot_checks/INDIA<N>_CHECK__<NONCE>.json`. Nothing else may ride along in K.

At the moment the START session finishes (Part 1), actual current central HEAD is **R**, not C — `boot_head_final` is deliberately R's *parent*, never R itself (a commit's hash cannot be known before its own content is fixed, so the receipt cannot record its own commit hash — see the validator docstring). "Stale" therefore never means "`boot_head_final` equals current HEAD" — it structurally never does, by design, for a valid receipt. It means: has actual current central HEAD moved to something that is **not** R (or, after the CHECK, not K) — i.e. content changed, or an unrelated commit was inserted, after the point this evidence was pinned.

At the moment the independent CHECK session finishes (Part 2), actual current central HEAD is **K**. `governance/scripts/validate_independent_check.py` enforces the R→K half of this shape the same way `validate_successor_boot.py` enforces the C→R half; `governance/scripts/final_authorization.py` runs both and is the only script permitted to print `CONTENT_AUTHORIZATION: GRANTED`.

---

## PART 1 — START PROTOCOL (the session being booted)

### 1.1 Preconditions
- Mark (or the start prompt) supplies an exact session label (`INDIA<N>`) and an exact, freshly-chosen **start nonce**. The session must not invent or reuse a nonce. Both must match the format enforced by the validators: session `^(INDIA[0-9]+)$`, nonce `^[A-Z0-9]{6,32}$`.
- The session begins `UNBOOTED` unconditionally — see `governance/FRESH_SESSION_BOOT_GATE.md` ABSOLUTE DEFAULT.

### 1.2 Execution
1. Resolve `BOOT_HEAD_INITIAL` = current HEAD of `agent/india8-cluster-casting`.
2. Read `governance/FRESH_SESSION_BOOT_GATE.md` completely, then `governance/BOOT_MANIFEST_V8.json` completely.
3. Read every file in the manifest's `central_required` (this file included), `cci_required` (at `cci_commit`), and `active_cluster_required` completely — continue every truncation to EOF; a summary/pointer view of a file counts as `NOT_READ_IN_THIS_SESSION`.
4. Resolve `BOOT_HEAD_FINAL` (= commit **C** above). If central moved during the read pass, diff `BOOT_HEAD_INITIAL..BOOT_HEAD_FINAL`, and reread any mandatory file that changed.
5. Write a NEW file at `governance/boot_receipts/INDIA<N>__<NONCE>.json` per the schema in `governance/boot_receipts/README.md` and `INDIA_MASTER_BOOT.md` §2B, including per-file byte-range read coverage and >=3 correctly-categorized proof-of-read quotes.
6. Commit the receipt as commit **R**: a single follow-up commit on top of `BOOT_HEAD_FINAL` whose entire diff is that one new receipt file and nothing else. Do **not** try to include the receipt in the same commit as the content itself — that is impossible by construction (see CANONICAL HEAD/COMMIT SHAPE above) and the validator will reject it (`receipt final head must not equal the receipt commit directly`).
7. Run `python3 governance/scripts/boot_gate.py INDIA<N> <NONCE>` (equivalently, `validate_successor_boot.py --require-session-receipt governance/boot_receipts/INDIA<N>__<NONCE>.json --expected-session INDIA<N> --expected-nonce <NONCE>`). Require `INDIA_TRAVEL_BOOT_SANITY: PASS`. A FAIL means fix the exact reported gap and rerun — never patch around a FAIL by loosening the receipt's own claims to match reality in the wrong direction (e.g. shrinking a claimed read range instead of actually reading the missed bytes).
8. Even on mechanical PASS, the validator's own output says `CONTENT_AUTHORIZATION: NOT_GRANTED`. The session must say so too, explicitly, and STOP short of substantive India content until Part 2 below has run and `governance/scripts/final_authorization.py` has returned `CONTENT_AUTHORIZATION: GRANTED`.

### 1.3 What "done" looks like for the START session
The START session's own turn ends with: mechanical receipt PASS reported verbatim, an explicit statement that content authorization is not yet granted, and a request/handoff for an independent CHECK session — including a request that Mark supply a **separate fresh check nonce** (distinct from the start nonce) in the CHECK session's own start prompt. It does not proceed to travel content on the strength of its own PASS.

---

## PART 2 — INDEPENDENT CHECK PROTOCOL (a separate session)

### 2.1 Who runs this
A genuinely separate session/conversation from the one that produced the receipt — not the same session continuing under a different heading. The point is a second, independently-formed judgment about the same fixed evidence, not the original session re-affirming itself.

### 2.2 Binding
Mark's CHECK-session start prompt supplies a **separate fresh check nonce** (never the start nonce, never reused from any prior check). The CHECK session must bind itself to:
- the exact start nonce and exact `india_session` from the receipt under review;
- the exact `boot_head_final` from that receipt;
- the exact receipt file path;
- the exact receipt commit SHA (**R** above — resolvable as the parent of actual current HEAD once the receipt was committed, or by locating the commit whose diff adds exactly that receipt file on top of `boot_head_final`);
- its own separate fresh check nonce.

It must independently re-run (or reason from a freshly independent re-read, if script execution is unavailable) the same mechanical checks the validator performs, rather than trusting the START session's self-report of PASS.

### 2.3 Two new quotes
Before anything else, demand and verify TWO NEW verbatim quotes (>=40 chars, full sentences) from two different mandatory files that were **not** among the sources used in the original receipt's `proof_of_read`. Verify each against the pinned source at `boot_head_final` (or `cci_commit` for CCI sources) exactly as the validator does for the original three.

### 2.4 At least six applied semantic challenges, chosen AFTER the receipt exists — eight are mandatory
Choose at least six challenges (do not reuse a fixed script) calibrated to what is actually live in the current manifest/state at the time of the CHECK. `governance/scripts/validate_independent_check.py` mechanically requires ALL EIGHT of the following topics to be present with a recorded `question`/`answer`/`evidence`/`verdict` (this list is the manifest's `check_required_challenge_topics`, and is itself the concrete standing-veto set the 2026-08-30 Work audit named as mandatory — MUST_FIX 6):

- **`TRAIN_FIRST_DOOR_TO_DOOR`** — pose a transport scenario and confirm the rail-first / true door-to-door hierarchy is applied correctly, not a flight/taxi default.
- **`AL_BESLIST`** — present an already-decided item as if it were open; confirm the session catches it as already decided rather than re-litigating it.
- **`C_DO_NOT_RE_PRESENT`** — present a current-trip-reject (`C`) item as if it were live; confirm the session recognizes it must stay absent unless Mark explicitly reopens it, and does not re-present it as a fresh choice.
- **`NEWER_CENTRAL_OVER_CCI`** — pick a known CCI-vs-central conflict (e.g. the Bodh Gaya open ballot, the Chennai/Bengaluru south-gateway hypothesis) and confirm the session applies the correct current-wins-over-frozen-CCI resolution.
- **`GEO_VETO`** — ask for a map/pin/proximity claim on an unresolved or ambiguous location; confirm the session refuses rather than guesses (`MAP_COORDINATE_VERIFICATION_RULE.md`).
- **`CURRENT_FRONTIER`** — ask what the exact current operational frontier is; confirm it matches `CURRENT_STATE.md`, not a stale prior phase.
- **`ACTION_FIRST`** — check for forbidden deferral language (`ik ga onderzoeken`, `wil je dat ik verderga?`) in the session's own recent output.
- **`DURABLE_WHAT_WHY`** — ask what would happen to a specific piece of new knowledge if the chat died now; confirm the session can point to WHAT it would record and WHY, and exactly where in the governance/knowledge-map architecture it would live, not "in this conversation."

Additional challenges beyond these eight (truncation, summary substitution, naming, human decision surface, same-turn memory write, etc.) are encouraged and count toward the six-minimum floor, but the eight above are not optional substitutes for each other — the validator checks for all eight topic keys explicitly.

### 2.4a CHALLENGE-RESPONSE ROUND TRIP (MANDATORY — 2026-08-30 fresh re-audit repair)
A 2026-08-30 fresh independent Work re-audit (PR #23 comment `5470939825`, MUST_FIX 1; see `governance/INDIA_RECOVERY_DELTAS_CURRENT.md` R32) demonstrated that letting the CHECK session author both a challenge's "answer" and its own grading of that answer in one self-declared field made the second key gameable: eight placeholder answers plus eight self-issued PASS verdicts still reached `CONTENT_AUTHORIZATION: GRANTED`. Each challenge record therefore now has three separately-authored fields, and Part 2 is not complete until all three exist for every challenge:

1. The CHECK session picks the question for a topic **after** receipt R already exists (per §2.4) and writes it to `question`.
2. Mark relays that exact question to the real, original START session (the same session/conversation that produced the receipt under review — not a fresh session asked to reconstruct an answer, and not the CHECK session answering on its behalf).
3. The START session answers from its own live context. Mark relays that reply back to the CHECK session **verbatim** — copied, not paraphrased or summarized — and the CHECK session records it unmodified as `start_session_answer`.
4. The CHECK session grades that answer against the actual pinned source material at `boot_head_final`/`cci_commit` (not against memorized wording from this document — see §2.6), and records its own citation of concrete source material as `checker_evidence` and its PASS/FAIL judgment as `checker_verdict`.

`governance/scripts/validate_independent_check.py` mechanically rejects a `start_session_answer` or `checker_evidence` that is empty, a known placeholder/filler string (`"x"`, `"n/a"`, `"tbd"`, a single repeated character, etc.), below a minimum length/word count, identical to the other field, or — for `checker_evidence` — not citing a concrete mandatory/receipt source path. This is a floor against a checker self-authoring trivial content for both sides of the record, not proof that steps 2-3 above actually happened as a genuine live relay — see the HONEST LIMIT section below and `governance/boot_checks/README.md` for exactly what this can and cannot prove.

### 2.5 FAIL conditions
Any of the following is an unconditional FAIL of the CHECK, regardless of how well other challenges went:
- either new quote is fabricated, paraphrased, or not verbatim in the pinned source, or reuses a source/quote already used in the original receipt;
- actual current central HEAD is not exactly commit **K** as defined above (i.e. the branch moved to something other than "receipt commit, then this one CHECK commit and nothing else" — whether that movement happened before or after the CHECK was reasoned about);
- the check nonce is missing, malformed, or equal to the start nonce;
- `check_created_utc` is not strictly after `receipt_created_utc`, or is not close to the actual git commit time of the CHECK commit;
- any recorded challenge has `checker_verdict: FAIL`, or one of the eight mandatory topics in §2.4 is missing entirely;
- any challenge's `start_session_answer` or `checker_evidence` is missing, empty, a placeholder/filler string, too short, too few words, identical to the other field, or (for `checker_evidence`) does not cite a concrete mandatory/receipt source path — see §2.4a;
- evidence the START session used summary/predecessor context in place of an actual read;
- evidence a truncated read was left unfinished;
- evidence the START session reopened, mutated, or silently overrode a locked Mark decision;
- evidence the START session violated the train-first / true-door-to-door hierarchy;
- evidence of a naming-format violation on a decision-relevant location;
- evidence a piece of material new knowledge was not durably recorded anywhere GitHub-routable.

### 2.6 Do not hard-code answers
This file intentionally does not embed a fixed answer key. A receipt or a session that appears to "know" this file's exact challenge wording in advance, or that answers challenges from memorized text here rather than from the actual pinned source content, has not demonstrated a valid CHECK — the CHECK session must verify answers against the real pinned files at `boot_head_final`/`cci_commit`, not against this document.

### 2.7 Recording the CHECK
Record the outcome as a NEW file at `governance/boot_checks/INDIA<N>_CHECK__<NONCE>.json` (`<NONCE>` = the **start** nonce, matching the receipt it reviews — see that directory's `README.md` for the exact schema and its honest limits) as commit **K**: a single follow-up commit on top of the receipt commit (**R**) whose entire diff is that one new check file and nothing else. It must reference the exact receipt file path, `india_session`, `start_nonce`, `check_nonce`, `boot_head_final`, `receipt_commit` (R's SHA), the two new quotes, the challenge records (all eight mandatory topics plus any extras, each with `question`, `start_session_answer`, `checker_evidence`, `checker_verdict` per §2.4a), and the final `check_gate: "PASS"` or `"FAIL"`.

Then run `python3 governance/scripts/final_authorization.py INDIA<N> <START_NONCE> <CHECK_NONCE>`. Only its own exit 0 and printed `CONTENT_AUTHORIZATION: GRANTED` converts the receipt's mechanical `BOOT_AUTHORIZATION: MECHANICAL_GATE_PASS` into actual content authorization for the session that produced the original receipt. Nothing else in this repository may claim GRANTED.

---

## HONEST LIMIT
This protocol cannot force a model to actually run Part 2 before writing substantive content, nor can any file in this repository cryptographically prove that a "separate session" was genuinely a different reasoning process rather than the same one re-running under a new heading. It fails closed on everything that is machine-checkable (files, blobs, quotes, ranges, ancestry, branch, cleanliness, the three-commit C→R→K shape, session/nonce format, timestamp freshness, challenge-topic coverage, and — since the 2026-08-30 fresh re-audit repair, R32 — a minimum-substance/citation floor on each challenge's `start_session_answer`/`checker_evidence`) and relies on procedural discipline — Mark's own scrutiny, and a session choosing to follow its own instructions — for the rest. Machine-checkable range coverage over a file's bytes is a **claim** that the session read it, never proof that the model attended to or understood the content; that residual gap is exactly why Part 2's semantic challenges, not the receipt's byte-range coverage, are the actual compensating control.

**§2.4a's challenge-response round trip is a file/git-architecture approximation of a live second opinion, not a live one.** This repository has no process that lets one session query another in real time; the actual mechanism is Mark manually copying a question to the START session and pasting its reply back into the CHECK artifact. Nothing here can cryptographically confirm that relay was faithful (unshortened, unparaphrased), that the "START session" queried was genuinely the original one, or that the length/word-count/placeholder/citation floor on `start_session_answer` and `checker_evidence` reflects real understanding rather than merely enough verbosity and a correctly-spelled file path to pass a regex. That floor raises the cost of the concrete bypass it was built to close (all fields replaced by a one-character placeholder) — it does not, and cannot, make the two-key design cryptographically sound. See `governance/INDIA_MASTER_BOOT.md` §1A and `governance/boot_checks/README.md` for the same limit stated in those files' own context.

END INDIA14 START + INDEPENDENT CHECK PROTOCOL

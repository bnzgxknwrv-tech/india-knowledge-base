# INDIA SUCCESSOR START + INDEPENDENT CHECK PROTOCOL — V8.2 CANONICAL

Status: **BINDING / CANONICAL START + INDEPENDENT CHECK ARTIFACT / MANDATORY MANIFEST READ**
Effective: 2026-09-01
Manifest: `governance/BOOT_MANIFEST_V8.json`
Path note: this protocol deliberately remains stored at `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` for backward compatibility with existing prompts, validators and manifests. **Its scope is NOT INDIA14-specific. It governs INDIA14, INDIA15 and every later `INDIA<N>` successor until explicitly superseded in central governance.**
Owner: this file is the canonical merge point of the START protocol and INDEPENDENT CHECK protocol referenced from `governance/INDIA_MASTER_BOOT.md` and `governance/FRESH_SESSION_BOOT_GATE.md`. Mandatory file membership lives only in the manifest.
V8.2 change (R34, 2026-09-01, Mark-approved proportionality redesign): Part 2 is now TWO tiers, FULL and LIGHT — see §2.0 before doing anything else in Part 2. Part 1 (the mechanical boot + receipt) is completely unchanged and stays mandatory for every single fresh session regardless of tier.

## 0. DESIGN GOAL — MAKE THE CURRENT SESSION REPLACEABLE
The boot system exists to prevent successor knowledge loss, not to become the project. A successor must be able to start from the same small start prompt, recover current truth from GitHub, prove the read mechanically, survive one independent semantic second opinion, and then continue the actual India work.

Human orchestration must be minimized:
- no successor-specific rewrite of the start protocol;
- no manual shell command required from Mark;
- no per-topic separate copy/paste round trips (all mandatory topics — see `BOOT_MANIFEST_V8.json`'s `check_required_challenge_topics` for the current exact list/count — travel as one batch, §2.4);
- no request that Mark reconstruct project state;
- no substantive content before the two-key gate really passes;
- no weakening of fail-closed checks merely to save time;
- after authorization, no restarting completed predecessor work because an older pointer still says it is open;
- side questions and interruptions never erase the underlying frontier unless Mark explicitly replaces it.

The preferred future flow is:
`START -> full manifest read -> R receipt -> automatic receipt CI PASS -> one independent CHECK -> one batched challenge round trip via GitHub relay (fallback: one copy/paste each way) -> K check commit -> automatic final-authorization CI -> CONTENT_AUTHORIZATION: GRANTED -> three-pass frontier parity check -> actual travel work`.

## 1. CANONICAL HEAD/COMMIT SHAPE
Three commits, in order:
- **C** — content/governance commit. Its SHA is `boot_head_final`. Receipt does not exist in C.
- **R** — receipt commit. `R^ == C`; its entire diff is exactly one new `governance/boot_receipts/INDIA<N>__<START_NONCE>.json`.
- **K** — independent-CHECK commit. `K^ == R`; its entire diff is exactly one new `governance/boot_checks/INDIA<N>_CHECK__<START_NONCE>.json`.

At START completion, central HEAD is R. After CHECK recording, central HEAD is K. Any unrelated central commit inserted into C→R→K invalidates that boot/check chain and requires fail-closed recovery.

This exact C→R→K shape is identical for a FULL check and a LIGHT check (§2.0) — same directory, same filename convention, same automatic `.github/workflows/india-final-authorization.yml` trigger. The two tiers differ only in WHO authors the K artifact's content and HOW MANY/WHICH topics it must cover, never in the commit shape around it. A check artifact's own `check_mode` field (`"FULL"` or `"LIGHT"`) is what the validator reads to know which rules apply; a missing `check_mode` (every check written before 2026-09-01, including the real INDIA14 CHECK) is treated as `"FULL"`.

`governance/scripts/validate_successor_boot.py` enforces C→R.
`governance/scripts/validate_independent_check.py` enforces R→K.
`governance/scripts/final_authorization.py` runs both and is the only script permitted to print `CONTENT_AUTHORIZATION: GRANTED`.

## PART 1 — START SESSION

### 1.1 Preconditions
- Session label is exact `INDIA<N>`.
- Start nonce is the fresh uppercase alphanumeric nonce supplied in the start prompt, format `^[A-Z0-9]{6,32}$`. START must not reuse or silently replace it.
- Every fresh session begins `UNBOOTED`.

### 1.2 Execute without stopping halfway
1. Resolve current central HEAD as `BOOT_HEAD_INITIAL`.
2. Read `governance/FRESH_SESSION_BOOT_GATE.md` and `governance/BOOT_MANIFEST_V8.json` completely.
3. Read every manifest `central_required`, immutable `cci_required`, and `active_cluster_required` file completely. Continue truncations to EOF. Summary/context/pointer exposure is not a current-session read.
4. Resolve `BOOT_HEAD_FINAL` = C. If central moved during reading, inspect the entire initial→final delta and reread every mandatory file that changed.
5. Create a NEW append-only `governance/boot_receipts/INDIA<N>__<START_NONCE>.json` with the exact schema required by `governance/boot_receipts/README.md` and the validator, including complete read coverage and >=3 correctly categorized proof quotes.
6. Commit it as R, with no other file in the commit.
7. Obtain a real canonical mechanical PASS. Preferred order:
   - if a live Git checkout with Python is available, run `python3 governance/scripts/boot_gate.py INDIA<N> <START_NONCE>`;
   - otherwise use the repository's permanent GitHub Actions workflow `.github/workflows/india-boot-receipt.yml`, automatically triggered by R. The START session must inspect the run tied to R and require both workflow/job success and literal `INDIA_TRAVEL_BOOT_SANITY: PASS` in the job log.
8. **Do not tell Mark to start the independent CHECK before step 7 has genuinely passed.** A receipt merely existing is not enough.
9. Even after receipt PASS, substantive India content remains forbidden until Part 2 and final authorization pass.

A chat/tool environment lacking a local shell is **not itself a boot FAIL** when the canonical GitHub Actions runner is available and succeeds. Conversely, a verbal “equivalent check” is not a substitute for the real script once the permanent runner is available.

### 1.3 START handoff
After real receipt PASS, report only the compact handoff facts needed for CHECK: session, start nonce, C, R/receipt path, mechanical PASS, and `CONTENT_AUTHORIZATION: NOT_GRANTED`. Then wait for the independent challenge batch. Do not resume travel content.

## PART 2 — INDEPENDENT CHECK SESSION

### 2.0 TIER DETERMINATION — DECIDE THIS BEFORE ANYTHING ELSE IN PART 2

**Why this exists (R34):** running the full-topic-set, separate-session, Mark-relayed CHECK (§2.1-2.7 below) on every single fresh `INDIA<N>` session was disproportionately costly. Mark needed fresh sessions frequently (ChatGPT's own session limits forced INDIA12→13→14→15 in rapid succession), and each full CHECK cost him real manual relay time and a whole second ChatGPT conversation — even for a routine continuation where nothing about the project's governing knowledge had actually changed since the last time a full CHECK passed. Part 1 (the mechanical boot + receipt, §1 above) is unaffected by any of this and stays mandatory, unweakened, for every single fresh session — it is what directly fixes "successor doesn't load current state" (the 2026-08-30 taxi-heavy incident) and it is already cheap (no second session, no manual relay). Only Part 2 — the independent CHECK — is now proportional.

**Two tiers exist:**
- **FULL CHECK** — §2.1-2.7 below, completely unchanged mechanics: a genuinely separate CHECK session, all mandatory topics (the manifest's `check_required_challenge_topics` — see §2.3), two new verbatim quotes, a real START-answer relay, `check_mode: "FULL"` in the K artifact.
- **LIGHT SPOT-CHECK** — §2.8 below: the SAME START session answers 2-3 deterministically-chosen topics itself, no second session, no relay, `check_mode: "LIGHT"` in the K artifact.

**How a session determines which tier it is ALLOWED to use — mechanical, not a judgment call:**

A FULL CHECK is required (never substitute LIGHT) when ANY of these is true:
1. **No prior FULL check has ever PASSED against the CURRENT exact `central_required` file content.** Concretely: `governance/scripts/validate_independent_check.py` walks `governance/boot_checks/` (live directory + its `test_fixtures/` subdirectory) for every check artifact whose `check_mode` is `"FULL"` (or absent — every check written before 2026-09-01 counts as FULL) and whose own `check_gate` is `"PASS"`; for each, it reads that check's reviewed receipt's `boot_head_final` and computes the real git blob SHA of every path in the manifest's `central_required` array AT THAT COMMIT; it then compares that map, path-for-path, against the same map computed at the CURRENT session's own `boot_head_final`. If ANY prior FULL check's map is an EXACT match, LIGHT is eligible. If none match — because a `central_required` file's content differs even by one byte, a `central_required` path was added/removed, or no prior FULL check exists at all — LIGHT is NOT eligible and a FULL CHECK is required.
   - **This is deliberately never a hand-maintained pointer/version field.** R30 already established that a manually-tracked sync field rots the moment one governance file is edited without the tracker being updated in the same breath. Tier eligibility is instead recomputed live, every time, straight from git blob SHAs and the actual `governance/boot_checks/` history — there is nothing to forget to update.
   - **This scope is `central_required` ONLY** (the governance/behavior core — 17 files as of this consensus patch; read `BOOT_MANIFEST_V8.json` for the exact current count/list rather than trusting a number written here), never `cci_required` (pinned/immutable, cannot change) or `active_cluster_required` (changes constantly with ordinary travel-content progress — tying tiering to it would force a FULL check on every routine cluster update and defeat the entire point).
   - Practical consequence: **any commit that changes a `central_required` file's content — including this very redesign — makes the FIRST session to boot afterward require a FULL CHECK**, because no prior FULL check's blob-SHA map can match the new content yet. That first FULL check then becomes the new baseline every subsequent LIGHT-eligible session compares against. This is intentional: a change to the governing rules themselves should be verified once against the new rules, not silently grandfathered in.
2. **Mark explicitly requests a FULL check for any reason** — he does not need to justify it; "doe toch maar de volledige CHECK" is sufficient.
3. **Any prior LIGHT spot-check in the current repository state FAILED and has not since been superseded by a passing FULL check.** A spot-check FAIL always escalates to requiring a FULL check next; it never silently degrades further and never gets a second LIGHT attempt in its place.

Otherwise (a matching prior FULL check PASS exists, Mark has not asked for FULL, and no unresolved prior spot-check FAIL exists), **LIGHT is allowed** — proceed to §2.8 instead of §2.1-2.7.

**Fail-closed guarantee:** the validator itself enforces this — a K artifact that declares `check_mode: "LIGHT"` without a matching prior FULL-check blob-SHA map is rejected with an explicit `a FULL CHECK is required for this boot, not a LIGHT spot-check` error, not a silent downgrade or a soft warning.

### 2.1 Independence and binding — FULL CHECK PROCEDURE (§2.0 already sent you here)
Use a genuinely separate conversation/session. It binds independently to the exact receipt, session, start nonce, C and R.

A separate fresh check nonce is required. If Mark supplied one in the CHECK prompt, use it exactly. If no check nonce was supplied, the CHECK session may generate a fresh uppercase alphanumeric 6–32 character nonce itself **after** binding to the receipt; it must be distinct from the start nonce and any visible prior check nonce. This removes needless user setup without weakening uniqueness.

The CHECK independently verifies the mechanical evidence; it never trusts START's self-reported PASS.

### 2.2 Two new quotes
Demand and verify TWO NEW verbatim full-sentence quotes, each >=40 characters, from two different mandatory files not used as sources in the receipt's original `proof_of_read`. Verify against the pinned source at C or immutable CCI commit.

### 2.3 Mandatory applied challenges — full manifest topic set

**All topics in `BOOT_MANIFEST_V8.json`'s `check_required_challenge_topics` array are mandatory.** That array is the single authority for the exact current list and count — it is deliberately NOT re-enumerated here as a second hand-maintained copy (the R30 lesson: a hand-copied list rots the moment the manifest changes without this file being edited in the same breath; that exact staleness is what the INDIA16 consensus patch closed for the central-file count, and this file must not reintroduce the same failure shape for the topic list). Read the manifest directly before running a CHECK.

Questions must be chosen after R exists and applied to the actual current pinned state, not copied as a fixed answer key. Additional challenges beyond the mandatory set are allowed.

Each challenge record contains:
- `topic`
- `question` — authored by CHECK
- `start_session_answer` — verbatim answer from the real START session
- `checker_evidence` — authored by CHECK with concrete mandatory-source path(s)
- `checker_verdict` — `PASS` or `FAIL`

The validator's minimum length/word/citation floors remain binding.

**`FRONTIER_CONTRADICTION_CHECK` — extended evidence requirement (INDIA16 consensus patch, 2026-09-02):** this topic exists specifically to test whether the mandatory current-state sources actually agree with each other (the confirmed `READ_COMPLETE != ACTIVE_MEMORY_COMPILED` failure class — see `INDIA_RECOVERY_DELTAS_CURRENT.md` and `INDIA_ACTIVE_MEMORY_COMPILATION_GATE.md`). For this one topic ONLY, `checker_evidence` must concretely cite all THREE of `governance/CURRENT_STATE.md`, `governance/CURRENT_DECISIONS_MASTER.md` and `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` — a single-source citation, sufficient for every other topic, is not sufficient here. `validate_independent_check.py` enforces this mechanically (it verifies the three citations name real mandatory files, not that their content is actually reconciled — that judgment stays with the CHECK session and, ultimately, Mark).

### 2.4 One batched round trip — preferred; per-topic separate relays are unnecessary
The mandatory-topic challenges (§2.3) remain independent records, but they SHOULD be transported as one batch.

Preferred relay when both sessions have GitHub access:
1. CHECK posts one clearly identified challenge-batch comment on PR #23 containing all mandatory-topic questions, session, start nonce and check nonce.
2. Mark only needs to return to the START session and say that the CHECK questions are on PR #23; he does not need to copy the questions.
3. START independently fetches that exact comment, answers every question under the exact topic labels from its loaded context, and posts one clearly identified answer-batch comment on PR #23.
4. Mark only needs to tell CHECK that the answers are on PR #23.
5. CHECK fetches the exact START answer comment, records each answer verbatim, grades it against pinned sources, then creates K.

Fallback when GitHub-comment relay is unavailable:
- CHECK gives all mandatory-topic questions in one block;
- Mark pastes that block once to START;
- START answers all of them in one block;
- Mark pastes that block once back to CHECK.

Per-topic, question-by-question copy/paste cycles are explicitly unnecessary.

PR #23 remains relay/provenance only. The durable authorization evidence is still the receipt/check artifacts and Git/Actions validation; a PR comment never becomes controlling travel truth.

### 2.5 FAIL conditions
CHECK fails if any required quote is reused/fabricated/paraphrased; C→R→K shape is wrong; nonce binding/freshness is wrong; timestamps fail; any mandatory topic is absent; any `checker_verdict` is FAIL; answer/evidence is trivial or malformed; START substituted summary for required reads; a truncation remained unfinished; locked decisions were reopened; train-first hierarchy was violated; decision-relevant geography was guessed; or material successor knowledge was left only in chat.

### 2.6 Record K
Write `governance/boot_checks/INDIA<N>_CHECK__<START_NONCE>.json` exactly as specified by `governance/boot_checks/README.md`, then commit it alone as K.

### 2.7 Final authorization — AUTOMATIC BY DEFAULT
For all future sessions, K automatically triggers `.github/workflows/india-final-authorization.yml`.

That workflow must:
- check out `agent/india8-cluster-casting`;
- verify checked-out HEAD is exactly the triggering K;
- verify K contains exactly the expected single added check file;
- parse `india_session`, `start_nonce`, `check_nonce`;
- run exactly `python3 governance/scripts/final_authorization.py <SESSION> <START_NONCE> <CHECK_NONCE>`.

Authorization exists only if the workflow/job succeeds **and its log literally contains** `CONTENT_AUTHORIZATION: GRANTED`.

If the CHECK environment itself has a real live Git checkout, it may additionally run the same command locally. Local execution is not required when the automatic canonical CI run succeeds. A missing local shell must never again be reported as a FAIL after successful canonical CI.

If CI fails, inspect and fix the exact failure; do not weaken validator requirements. If central moved after K, fail closed and re-establish a valid fresh boot chain rather than pretending the stale K still authorizes content.

### 2.8 LIGHT SPOT-CHECK PROCEDURE — used only when §2.0 said LIGHT is allowed

This is the full mechanical procedure for the LIGHT tier. It reuses the exact same C→R→K commit shape, the same `governance/boot_checks/` directory and filename convention, and the same automatic `.github/workflows/india-final-authorization.yml` trigger as the FULL check — the only differences are WHO authors the K artifact's content and HOW MANY/WHICH topics it must cover.

**2.8.1 No second session, no relay.** The SAME START session that just completed Part 1 (the mechanical boot + receipt) does this itself, immediately, in the same session. There is no separate CHECK session, no Mark relay, no PR #23 batch exchange for this tier.

**2.8.2 Determine the exact topic set — do this by computation, not by picking.**
1. Take the manifest's `check_required_challenge_topics` array (the same full topic pool used by FULL — see §2.3 for why this file does not re-enumerate it), deduplicate and sort it ascending — this is `pool`.
2. Take `light_check_challenge_count` from the manifest (currently 3).
3. For `i` in `0 .. light_check_challenge_count-1`: compute `digest = sha256(f"{boot_head_final}:LIGHT_CHECK_TOPIC_SELECT:{i}")`; `idx = int(digest.hexdigest(), 16) % len(pool)`; pop `pool[idx]` and append it to the selected list.
4. The resulting topic set is fixed by `boot_head_final` alone — anyone can recompute it from the pinned commit hash, so it cannot be gamed by picking convenient topics, even though (unlike a FULL check's freshly-authored questions) it is not adversarially unpredictable. This is an explicit, accepted simplification for the routine case, not an oversight.

**2.8.3 Answer each selected topic yourself, with a real citation.** For each of the 2-3 selected topics, write:
- `topic` — the selected topic string, exactly as in the pool;
- `question` — a genuine applied question on that topic against the CURRENT pinned state (same spirit as a FULL-check question — not copied from a fixed answer key);
- `start_session_answer` — your own genuine answer, reasoned from the actual pinned mandatory sources, meeting the SAME floor as FULL (`check_min_answer_chars`/`check_min_answer_words`, not a placeholder);
- `checker_evidence` — your own citation of a concrete mandatory source path (`governance/...` or `runs/...`) or the reviewed receipt path that supports the answer, meeting the SAME floor as FULL (`check_min_evidence_chars`, must actually name a real mandatory path);
- `checker_verdict` — `"PASS"` if your own answer genuinely holds against the cited source, `"FAIL"` if it does not. **A single FAIL anywhere fails the whole spot-check** — do not soften this because it is self-graded; if you find you were wrong, record the FAIL honestly and escalate to a FULL check (§2.0 rule 3) rather than editing the answer until it passes.

**2.8.4 No new_quotes requirement.** Unlike FULL, LIGHT does not require the two-new-verbatim-quotes field at all — the per-challenge citations in 2.8.3 already carry the source-grounding burden for this lighter tier.

**2.8.5 Write and commit K.** Write `governance/boot_checks/INDIA<N>_CHECK__<START_NONCE>.json` with:
- the same identity/binding fields as a FULL check (`india_session`, `start_nonce`, `check_nonce`, `receipt_path`, `boot_head_final`, `receipt_commit`) — including a fresh `check_nonce` distinct from `start_nonce`, which you (the same session) may generate yourself, same as the FULL-check allowance in §2.1;
- `check_mode: "LIGHT"`;
- `challenges`: your 2-3 answered items from 2.8.3;
- `check_created_utc`;
- `check_gate: "PASS"` only once every item above is genuinely true.

Commit it alone as K, exactly as in §2.6.

**2.8.6 Final authorization — same automatic path as FULL.** K still automatically triggers `.github/workflows/india-final-authorization.yml`, which still runs exactly `python3 governance/scripts/final_authorization.py <SESSION> <START_NONCE> <CHECK_NONCE>` — this wrapper's own invocation never changes between tiers. `validate_independent_check.py` reads `check_mode` from the K artifact itself and applies §2.8's rules instead of §2.1-2.7's. On a clean PASS it prints `CONTENT_AUTHORIZATION: GRANTED` exactly as FULL does. If tier eligibility (§2.0 rule 1) does not actually hold, this FAILS with an explicit "a FULL CHECK is required for this boot, not a LIGHT spot-check" error — it never silently downgrades or waves the session through.

**2.8.7 Honest limit of this tier (state this plainly, do not overclaim).** LIGHT drops the one thing FULL was built for by R31/R32: a genuinely separate session authoring the question and grading a relayed answer. In LIGHT mode the same session authors the question, the answer, and its own grade of that answer — there is no independent second opinion. What LIGHT still provides: the SAME anti-triviality floor (no placeholder text, no missing citation, no self-contradicting wrong answer sneaking through as PASS), a deterministic and reproducible topic selection so the specific questions cannot be known in advance of actually completing the real boot, and a durable committed record of exactly what was asked and self-answered so a later audit is possible. This is a genuine, deliberate, Mark-approved cost/rigor tradeoff for the routine case where nothing about the governing rules has changed — it is not offered or to be described as equally strong as a FULL check.

## PART 3 — AFTER GRANTED
Once a successful final-authorization run tied to K has printed `CONTENT_AUTHORIZATION: GRANTED`, START may resume the real current frontier under ACTION_FIRST — but only after the following three-pass successor handoff audit.

The START session should verify the run itself from GitHub if necessary; Mark need not paste long validator logs. A short “CHECK klaar” or equivalent is sufficient for START to inspect K and the tied Actions result.

### 3.1 THREE-PASS FRONTIER PARITY AUDIT — HARD BEFORE FIRST CONTENT REPLY
This audit exists because predecessor chats can be interrupted, `CURRENT_STATE.md` can advance while a crash checkpoint or knowledge-map frontier lags, and an otherwise correctly booted successor can still restart completed work.

**PASS 1 — CURRENT AUTHORITY PARITY**
Compare, at the same current central state:
- `governance/CURRENT_STATE.md`;
- `governance/SUCCESSOR_SAFE_STATE.md`;
- `governance/CURRENT_DECISIONS_MASTER.md`;
- `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md` section B plus the relevant active section.

Ask only: do they agree on what is CLOSED, what is OPEN, who owns the next action, and what the current frontier is?

If they disagree materially, STOP content and repair the stale central pointer from newer explicit/current authority. Do not ask Mark to reconcile repository drift.

**PASS 2 — INTERRUPTION / BACKLOG RECONSTRUCTION**
Identify all work streams mentioned by the predecessor/current state and classify each:
- `COMPLETE — DO NOT RESTART`;
- `ACTIVE UNDERLYING TASK — RESUME`;
- `MARK_ONLY BLOCKER — ASK ONLY THIS`;
- `LATER / LIVE_RECHECK_LATER`;
- `SUPERSEDED / DO NOT REVIVE`.

A side question, clarification, LP sub-pass, cinema detail, map correction or other interruption never silently becomes the new global frontier unless Mark explicitly changed the work order. Completed side work belongs in `LAST_COMPLETED`, not in the successor's first action.

**PASS 3 — EXACT FIRST-ACTION TEST**
Write privately one sentence:
`After authorization, the first substantive action is: <exact action>, because <controlling current file says so>.`

Then test:
- Is this action still open NOW?
- Is it owned by INDIA or by Mark?
- Am I about to redo something already completed in the same current state?
- Am I asking a different question before the genuine Mark-only blocker?
- If this chat died after my next reply, would the next successor know the same first action from GitHub?

Only after all answers are clean may substantive work resume.

### 3.2 CURRENT PREDECESSOR HANDOFF POINTERS
A successor-specific detailed handoff may exist for crash explanation, but it never replaces the mandatory current authority stack. If `CURRENT_STATE.md` or `SUCCESSOR_SAFE_STATE.md` explicitly points to a current predecessor handoff, read it after authorization for sequence/error context, then filter it through current authority.

For the INDIA14->INDIA15 transition, the detailed current pointer is:
`governance/INDIA14_TO_INDIA15_HANDOFF_2026-09-01.md`.

Do not create a new successor-specific boot architecture merely because the handoff file names INDIA15. This universal protocol remains the boot.

### 3.3 FORWARD-FIELD FUTURE-READER TEST
Before writing any checkpoint's `NEXT_AUTOMATIC_STEP`, ask:
`Will this sentence still be future-tense true for a fresh reader after the commit containing it already exists?`
If not, the action belongs in `LAST_COMPLETED`.

## DO NOT HARD-CODE ANSWERS
This protocol defines topics and mechanics, not a fixed answer key. CHECK must validate against the actual pinned mandatory sources. Current facts change; the topics are standing vetoes, not memorized prose.

## HONEST LIMIT
Git/GitHub Actions can prove repository shape, files, script exit codes and literal validator output. They cannot prove model attention or that two conversations are cryptographically distinct. The independent semantic challenge remains the compensating human/model second opinion — **for a FULL check.** A LIGHT spot-check (§2.8) explicitly does not have that second opinion at all; §2.8.7 states that limit plainly and it must never be described as equally strong as FULL.

The streamlining here intentionally removes **friction**, not **independence**, for the FULL tier itself:
- one batch instead of one manual relay per topic;
- GitHub comments instead of copying large blocks when possible;
- automatic Actions instead of requiring a chat sandbox to have Git/Python network access;
- same start architecture for every `INDIA<N>`;
- three-pass post-authorization parity instead of relying on one potentially stale frontier pointer.

The V8.2 tiering (§2.0, §2.8, R34) is a DIFFERENT kind of change from the friction removal above: it does trade away real rigor (the separated-authorship protection) for the routine case, in exchange for cost — and it says so, rather than presenting LIGHT as a friction-only optimization of FULL.

END INDIA SUCCESSOR START + INDEPENDENT CHECK PROTOCOL

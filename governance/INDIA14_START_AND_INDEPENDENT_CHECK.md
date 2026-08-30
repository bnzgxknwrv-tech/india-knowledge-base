# INDIA SUCCESSOR START + INDEPENDENT CHECK PROTOCOL — V8.1 CANONICAL

Status: **BINDING / CANONICAL START + INDEPENDENT CHECK ARTIFACT / MANDATORY MANIFEST READ**
Effective: 2026-08-31
Manifest: `governance/BOOT_MANIFEST_V8.json`
Path note: this protocol deliberately remains stored at `governance/INDIA14_START_AND_INDEPENDENT_CHECK.md` for backward compatibility with existing prompts, validators and manifests. **Its scope is NOT INDIA14-specific. It governs INDIA14, INDIA15 and every later `INDIA<N>` successor until explicitly superseded in central governance.**
Owner: this file is the canonical merge point of the START protocol and INDEPENDENT CHECK protocol referenced from `governance/INDIA_MASTER_BOOT.md` and `governance/FRESH_SESSION_BOOT_GATE.md`. Mandatory file membership lives only in the manifest.

## 0. DESIGN GOAL — MAKE THE CURRENT SESSION REPLACEABLE
The boot system exists to prevent successor knowledge loss, not to become the project. A successor must be able to start from the same small start prompt, recover current truth from GitHub, prove the read mechanically, survive one independent semantic second opinion, and then continue the actual India work.

Human orchestration must be minimized:
- no successor-specific rewrite of the start protocol;
- no manual shell command required from Mark;
- no eight separate copy/paste round trips;
- no request that Mark reconstruct project state;
- no substantive content before the two-key gate really passes;
- no weakening of fail-closed checks merely to save time.

The preferred future flow is:
`START -> full manifest read -> R receipt -> automatic receipt CI PASS -> one independent CHECK -> one batched challenge round trip via GitHub relay (fallback: one copy/paste each way) -> K check commit -> automatic final-authorization CI -> CONTENT_AUTHORIZATION: GRANTED -> actual travel work`.

## 1. CANONICAL HEAD/COMMIT SHAPE
Three commits, in order:
- **C** — content/governance commit. Its SHA is `boot_head_final`. Receipt does not exist in C.
- **R** — receipt commit. `R^ == C`; its entire diff is exactly one new `governance/boot_receipts/INDIA<N>__<START_NONCE>.json`.
- **K** — independent-CHECK commit. `K^ == R`; its entire diff is exactly one new `governance/boot_checks/INDIA<N>_CHECK__<START_NONCE>.json`.

At START completion, central HEAD is R. After CHECK recording, central HEAD is K. Any unrelated central commit inserted into C→R→K invalidates that boot/check chain and requires fail-closed recovery.

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

### 2.1 Independence and binding
Use a genuinely separate conversation/session. It binds independently to the exact receipt, session, start nonce, C and R.

A separate fresh check nonce is required. If Mark supplied one in the CHECK prompt, use it exactly. If no check nonce was supplied, the CHECK session may generate a fresh uppercase alphanumeric 6–32 character nonce itself **after** binding to the receipt; it must be distinct from the start nonce and any visible prior check nonce. This removes needless user setup without weakening uniqueness.

The CHECK independently verifies the mechanical evidence; it never trusts START's self-reported PASS.

### 2.2 Two new quotes
Demand and verify TWO NEW verbatim full-sentence quotes, each >=40 characters, from two different mandatory files not used as sources in the receipt's original `proof_of_read`. Verify against the pinned source at C or immutable CCI commit.

### 2.3 Eight mandatory applied challenges
All eight manifest topics are mandatory:
- `TRAIN_FIRST_DOOR_TO_DOOR`
- `AL_BESLIST`
- `C_DO_NOT_RE_PRESENT`
- `NEWER_CENTRAL_OVER_CCI`
- `GEO_VETO`
- `CURRENT_FRONTIER`
- `ACTION_FIRST`
- `DURABLE_WHAT_WHY`

Questions must be chosen after R exists and applied to the actual current pinned state, not copied as a fixed answer key. Additional challenges are allowed.

Each challenge record contains:
- `topic`
- `question` — authored by CHECK
- `start_session_answer` — verbatim answer from the real START session
- `checker_evidence` — authored by CHECK with concrete mandatory-source path(s)
- `checker_verdict` — `PASS` or `FAIL`

The validator's minimum length/word/citation floors remain binding.

### 2.4 One batched round trip — preferred; eight separate relays are unnecessary
The eight challenges remain independent records, but they SHOULD be transported as one batch.

Preferred relay when both sessions have GitHub access:
1. CHECK posts one clearly identified challenge-batch comment on PR #23 containing all eight questions, session, start nonce and check nonce.
2. Mark only needs to return to the START session and say that the CHECK questions are on PR #23; he does not need to copy the questions.
3. START independently fetches that exact comment, answers all eight under the exact topic labels from its loaded context, and posts one clearly identified answer-batch comment on PR #23.
4. Mark only needs to tell CHECK that the answers are on PR #23.
5. CHECK fetches the exact START answer comment, records each answer verbatim, grades it against pinned sources, then creates K.

Fallback when GitHub-comment relay is unavailable:
- CHECK gives all eight questions in one block;
- Mark pastes that block once to START;
- START answers all eight in one block;
- Mark pastes that block once back to CHECK.

Eight separate question-by-question copy/paste cycles are explicitly unnecessary.

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

## PART 3 — AFTER GRANTED
Once a successful final-authorization run tied to K has printed `CONTENT_AUTHORIZATION: GRANTED`, START may resume the real current frontier immediately under ACTION_FIRST.

The START session should verify the run itself from GitHub if necessary; Mark need not paste long validator logs. A short “CHECK klaar” or equivalent is sufficient for START to inspect K and the tied Actions result.

## DO NOT HARD-CODE ANSWERS
This protocol defines topics and mechanics, not a fixed answer key. CHECK must validate against the actual pinned mandatory sources. Current facts change; the topics are standing vetoes, not memorized prose.

## HONEST LIMIT
Git/GitHub Actions can prove repository shape, files, script exit codes and literal validator output. They cannot prove model attention or that two conversations are cryptographically distinct. The independent semantic challenge remains the compensating human/model second opinion.

The streamlining here intentionally removes **friction**, not **independence**:
- one batch instead of eight manual relays;
- GitHub comments instead of copying large blocks when possible;
- automatic Actions instead of requiring a chat sandbox to have Git/Python network access;
- same start architecture for every `INDIA<N>`.

END INDIA SUCCESSOR START + INDEPENDENT CHECK PROTOCOL

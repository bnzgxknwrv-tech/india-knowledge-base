# INDIA SUCCESSOR START + INDEPENDENT CHECK PROTOCOL — V8.3 CANONICAL

Status: **BINDING / ALL FUTURE INDIA SUCCESSORS / MANIFEST-DRIVEN / FAIL-CLOSED**
Effective: 2026-09-02
Branch: `agent/india8-cluster-casting`
Manifest authority: `governance/BOOT_MANIFEST_V8.json`
Final active-memory handoff: `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`

Path note: this file keeps the historical filename `INDIA14_START_AND_INDEPENDENT_CHECK.md` only for compatibility. Its content governs every later `INDIA<N>` until superseded centrally.

## 0. DESIGN GOAL

The goal is not that a successor can say `I read all mandatory files`.

The goal is:
`CURRENT FILES READ -> CURRENT TRUTH RECONCILED -> REPEATED FAILURES LOADED AS LAST ACTIVE CONTEXT -> APPLIED SEMANTIC CHECK -> CONTENT_AUTHORIZATION -> CORRECT BEHAVIOR`.

The key failure class discovered with INDIA15 is:
`READ_BUT_NOT_ACTIVE`.

A session may have the correct rule somewhere in context and still answer as if it does not know that rule. Therefore the boot now includes a final repeated-error handoff that must be treated as if Mark just pasted it into the current chat.

## 1. CANONICAL COMMIT SHAPE

Three commits, in order:
- **C** = pinned content/governance state; SHA = `boot_head_final`;
- **R** = receipt-only child; `R^ == C`; diff = exactly one new `governance/boot_receipts/INDIA<N>__<START_NONCE>.json`;
- **K** = check-only child; `K^ == R`; diff = exactly one new `governance/boot_checks/INDIA<N>_CHECK__<START_NONCE>.json`.

`validate_successor_boot.py` validates C->R.
`validate_independent_check.py` validates R->K.
`final_authorization.py` is the only script permitted to print `CONTENT_AUTHORIZATION: GRANTED`.

Any unrelated commit inserted inside C->R->K invalidates the chain.

# PART 1 — START SESSION

## 1.1 Preconditions
- exact session label `INDIA<N>`;
- fresh `START_NONCE` matching the current start prompt;
- every fresh session begins `UNBOOTED`;
- predecessor summary/model memory/chat history never substitutes for current-session reads.

## 1.2 Mandatory execution order

1. Resolve current central HEAD as `BOOT_HEAD_INITIAL`.
2. Read `governance/FRESH_SESSION_BOOT_GATE.md` completely.
3. Read `governance/BOOT_MANIFEST_V8.json` completely.
4. Read every current manifest `central_required` file completely at the pinned central snapshot. Counts come LIVE from the manifest; never copy a fixed number into logic.
5. Read all manifest `cci_required` files completely at the immutable manifest `cci_commit`.
6. Read all manifest `active_cluster_required` files completely at the pinned central snapshot.
7. Continue every truncation to EOF. Summary-only exposure = NOT READ.
8. Reconcile the mandatory/current sources under `governance/INDIA_ACTIVE_MEMORY_COMPILATION_GATE.md`. At minimum determine one current answer for:
   - authority precedence;
   - exact frontier;
   - exact first substantive action;
   - current `AL BESLIST?` / grade / lock / C-do-not-represent truth;
   - current source-layer scope;
   - current human presentation contract;
   - contradictions and which newer authority resolves them.
9. **ALLERLAATSTE SEMANTISCHE READ:** reread `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` COMPLETELY after the reconciliation above. Treat it as if Mark just pasted that file as his last current-chat message. Run its `LAATSTE PRE-ANSWER TEST — HARD VETO` against the intended first content work. `I read it` is not enough; a relevant NO/UNKNOWN blocks content.
10. Resolve `BOOT_HEAD_FINAL` = C. If central moved during boot, inspect the full initial->final delta and reread every mandatory file that changed. If manifest/current authority/active package/handoff changed, redo steps 8-9 on the final pinned versions.
11. Create a NEW append-only receipt for the exact current session/nonce using `governance/boot_receipts/README.md` and the live validator schema.
12. Because `MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` is deliberately present in BOTH `central_required` and as the LAST `active_cluster_required` entry, receipt coverage must attest its exact pinned blob in both read sets.
13. Commit receipt alone as R.
14. Obtain a canonical mechanical receipt PASS through local `boot_gate.py` or the permanent receipt workflow. Mechanical PASS still means `CONTENT_AUTHORIZATION: NOT_GRANTED`.
15. Determine CHECK tier mechanically under Part 2.
16. Only after K and a successful final-authorization run literally prints `CONTENT_AUTHORIZATION: GRANTED` may travel content resume.

## 1.3 Why the handoff appears twice in the manifest

This is intentional redundancy, not accidental duplication.

As `central_required`:
- the handoff is part of the exact central governance blob map;
- changing any repeated-error instruction changes that blob map;
- therefore the first successor on the changed handoff cannot silently reuse an older FULL semantic baseline.

As the final `active_cluster_required` item:
- the same exact file must be reread after current cluster truth has been loaded;
- the rules are refreshed only when the successor already knows what current facts they must be applied to.

The machine can prove complete byte coverage of both required occurrences. It cannot cryptographically prove hidden model attention or chronological cognitive order. The procedural final-read requirement, semantic CHECK and answer-time veto are the compensating layers.

# PART 2 — CHECK TIER

## 2.0 Determine FULL vs LIGHT mechanically

The exact eligibility algorithm lives in `validate_independent_check.py` and is configured by `BOOT_MANIFEST_V8.json`.

### FULL required when any is true
1. No prior PASSing FULL check exists whose reviewed receipt has an exact path-for-path git blob-SHA match for the CURRENT session's complete `central_required` set.
2. Mark explicitly requests FULL.
3. An unresolved LIGHT failure requires escalation.

Otherwise LIGHT may be used.

Do not use prose counts. The manifest's current `central_required` list is authoritative.

**Important consequence:** because `MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` is central-required, every material change to that handoff changes the central blob map. The first fresh successor on that changed handoff must therefore establish a fresh FULL baseline unless an exact matching FULL somehow already exists.

## 2.1 FULL CHECK

FULL uses a genuinely separate CHECK session.

The CHECK independently binds to:
- exact INDIA session;
- exact start nonce;
- exact receipt path;
- exact C and R;
- fresh check nonce.

It independently verifies receipt mechanics and requires two new valid proof quotes as specified by current check governance.

### Mandatory challenges
Every topic in manifest `check_required_challenge_topics` is mandatory. Never copy a hand-maintained topic count/list into this protocol as a second authority.

Each challenge contains:
- `topic`;
- `question` authored by CHECK;
- verbatim `start_session_answer` from START;
- `checker_evidence` with concrete mandatory-source path(s);
- `checker_verdict` PASS/FAIL.

Questions must be APPLIED to the actual pinned current state. A memorized slogan is not sufficient.

### Special topic — `FRONTIER_CONTRADICTION_CHECK`
Evidence must cite all three:
- `governance/CURRENT_STATE.md`;
- `governance/CURRENT_DECISIONS_MASTER.md`;
- `governance/INDIA_CURRENT_KNOWLEDGE_MAP.md`.

Purpose: prove the session did not merely read them independently but can reconcile the current frontier.

### Special topic — `SUCCESSOR_ACTIVE_MEMORY_HANDOFF`
This topic exists specifically because `read` did not equal `apply`.

The CHECK question MUST NOT be:
- `heb je het bestand gelezen?`;
- `vat het bestand samen`;
- `noem een regel uit het bestand`.

The question MUST force applied working memory. It must ask START to:
1. identify at least one specific `FOUT` from `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` that is materially relevant to the ACTUAL current frontier / first intended substantive reply;
2. state the corresponding mandatory solution;
3. use current-source evidence to show where that risk arises NOW;
4. describe concretely how the intended reply/workflow will comply;
5. when practical, demonstrate compliance using a tiny sample of the intended output rather than only promising future compliance.

A generic answer such as `ik zal het bestand volgen`, `ik heb dit in mijn actieve geheugen` or a mere paraphrase of the handoff is a semantic FAIL.

The checker should cite at minimum:
- `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`;
- plus at least one current mandatory/active source required to apply that error-rule to the actual frontier.

## 2.2 FULL relay
Transport all mandatory challenge questions as one batch whenever practical. PR #23 may be used as relay/provenance. It is never current travel truth merely because a comment exists there.

START answers the whole batch; CHECK grades the actual answers; K records the result.

## 2.3 FULL FAIL examples
FAIL if, among other current validator requirements:
- stale/wrong receipt/session/nonces/C/R/K;
- fabricated/reused proof;
- missing mandatory challenge topic;
- trivial answer/evidence;
- any checker verdict FAIL;
- locked decision reopened;
- train-first violated;
- decision geography guessed;
- contradiction sources not reconciled;
- `SUCCESSOR_ACTIVE_MEMORY_HANDOFF` answered only as a promise or summary instead of current applied behavior;
- a repeated error listed in the final handoff is visibly reproduced in the intended first content response.

## 2.4 Record K + final authorization
Write the check artifact under `governance/boot_checks/`, commit it alone as K, and require the permanent final-authorization workflow/job to succeed with literal:

`CONTENT_AUTHORIZATION: GRANTED`

No content before that.

# PART 2B — LIGHT SPOT-CHECK

LIGHT is allowed only when §2.0 mechanically allows it.

- same START session;
- same C->R->K shape;
- no second-session relay;
- exact number and deterministic topic selection come from the live manifest;
- same answer/evidence anti-triviality floors;
- no new-quotes requirement unless current manifest/validator says otherwise.

The deterministic selection algorithm is the manifest-declared algorithm implemented in `validate_independent_check.py`; do not hand-pick easy topics.

If `SUCCESSOR_ACTIVE_MEMORY_HANDOFF` is selected, the SAME applied standard above remains mandatory. Self-grading does not reduce its semantic requirement: choose a real currently relevant repeated failure, show current-source evidence and show concrete prevention in the intended reply.

LIGHT intentionally lacks separated-authorship independent review and must never be described as equal in rigor to FULL.

# PART 3 — AFTER `CONTENT_AUTHORIZATION: GRANTED`

Before the first substantive reply, perform all four passes below.

## PASS 1 — CURRENT AUTHORITY PARITY
Compare current:
- `CURRENT_STATE.md`;
- `SUCCESSOR_SAFE_STATE.md`;
- `CURRENT_DECISIONS_MASTER.md`;
- relevant `INDIA_CURRENT_KNOWLEDGE_MAP.md` routing;
- manifest-selected active cluster.

They must agree on CLOSED/OPEN/frontier/next owner. If not, repair current routing first.

## PASS 2 — BACKLOG / INTERRUPTION RECONSTRUCTION
Classify predecessor work:
- COMPLETE — DO NOT RESTART;
- ACTIVE UNDERLYING TASK — RESUME;
- MARK-ONLY BLOCKER;
- LATER / LIVE_RECHECK_LATER;
- SUPERSEDED / DO NOT REVIVE.

A side question never silently replaces the underlying frontier.

## PASS 3 — EXACT FIRST ACTION
Privately complete:
`The first substantive action is <...> because <current controlling source> says so.`

Check it is still OPEN, correctly owned and not duplicate work.

## PASS 4 — FINAL CHAT-LIKE HANDOFF VETO
Immediately before composing/sending the first substantive reply, reread/apply the `LAATSTE PRE-ANSWER TEST — HARD VETO` in `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`.

Do not reason:
`I already read it during boot.`

Reason:
`Mark effectively just pasted these instructions into this chat; does my actual intended answer obey them?`

If any relevant answer is NO/UNKNOWN:
`STOP -> RETRIEVE/RECONCILE/RESEARCH/REPAIR -> RETEST -> ONLY THEN REPLY`.

# PART 4 — DURING THE SESSION

The handoff remains active after the first answer.

Before EVERY substantive India reply:
- run its final veto;
- scan every Indian place name for recognition-rich context;
- do `AL BESLIST?`;
- show WHAT/WHY/geometry/images when applicable;
- preserve research-vs-triage-vs-duration separation;
- do not resurrect C;
- do not use grade letters as route labels;
- after CCI/worker output, reread output + new central HEAD before resuming old TODOs;
- preserve underlying task across side questions;
- checkpoint material knowledge.

If Mark says any equivalent of:
- `je hebt het toch gelezen?`;
- `waarom doe je het dan niet?`;
- `dit hadden we al`;
- `ik weet niet wat die Indiase naam betekent`;
- `je presentatie is niet keuze-klaar`;
then this is a **memory-system incident**, not a local style complaint.

Required:
`STOP NEW CONCLUSIONS -> IDENTIFY WHICH FOUT WAS REPEATED -> FIX CURRENT ANSWER -> REPAIR/EXTEND FINAL HANDOFF IF NEEDED -> RESUME UNDERLYING TASK`.

# PART 5 — HONEST LIMIT

GitHub/validators can strongly enforce:
- exact mandatory file membership;
- exact file blobs;
- full byte coverage;
- session/nonces;
- C->R->K commit shape;
- handoff inclusion in central governance;
- handoff reread as an explicit required procedure;
- a new FULL baseline after handoff changes;
- mandatory applied check topic existence and structured evidence floors;
- no authorization before gates pass.

They cannot cryptographically inspect or force the hidden internal attention state of a language model at every token it generates.

Therefore the strongest honest design is layered:
1. handoff mandatory in manifest;
2. handoff central-required so changes invalidate old FULL baseline;
3. handoff also last active-cluster-required entry;
4. receipt proves its exact complete bytes were read in both roles;
5. compilation/reconciliation before final handoff reread;
6. semantic `SUCCESSOR_ACTIVE_MEMORY_HANDOFF` challenge tests APPLICATION rather than recall;
7. final pre-answer veto treats handoff as if Mark just pasted it in chat;
8. Mark correction becomes a system incident and updates the same single error-list file.

This is the strongest available mechanism in this architecture. Never claim it makes future model behavior mathematically infallible.

END INDIA SUCCESSOR START + INDEPENDENT CHECK PROTOCOL V8.3
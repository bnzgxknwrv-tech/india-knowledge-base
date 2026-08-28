# CCI FULL REPOSITORY KNOWLEDGE HARVEST — TASK

Task ID: `CCI-FULL-REPO-KNOWLEDGE-HARVEST-001`
Worker: CCI / Cloud Code India
Worker branch: `agent/cci-full-repo-knowledge-harvest`
Base central branch: `agent/india8-cluster-casting`
Frozen base commit for this harvest: `a37423639f7dabb0dfd55c8656d4689bb8a25351`
Status: READY_FOR_CCI

## 0. WHY THIS TASK EXISTS

The India project has passed through many successive ChatGPT/INDIA regisseurs. Mark has repeatedly had to correct successors because important knowledge was buried in older layers, superseded files, historical branches, worker outputs, PR discussion or old project-foundation files that later successors did not read.

The problem is therefore NOT merely “make a better summary”. The problem is successor knowledge loss.

The required end state is:

> A new INDIA successor must be able to start from a compact durable knowledge layer and have, as nearly as practically possible, the same decision-relevant knowledge as the previous regisseur — including Mark’s current decisions, WHY those decisions matter, project philosophy, protected exclusions, hotel/sleepbase choices, route/dwell preferences, spiritual-selection logic, and the provenance needed to avoid reviving superseded material.

This is a repository-archeology + reconciliation + knowledge-surfacing task.

Do not optimize travel, research new destinations or make new subjective decisions. First recover what the repository already knows.

---

# 1. AUTHORITY AND WRITE RULES

CCI may write freely on this worker branch.

CCI MUST NOT:
- write to `agent/india8-cluster-casting` directly;
- change Mark A/B/C/A+/A* decisions;
- change hotel/sleepbase locks;
- change route locks or dwell decisions;
- silently reinterpret a user question as a decision;
- declare a worker result central truth merely because the worker says COMPLETE;
- delete historical evidence;
- run new destination/travel web research as a substitute for repository reconciliation.

INDIA remains integrator/regisseur. Mark remains the only authority for subjective travel decisions.

If source material conflicts, preserve the conflict and provenance. Do not “fix” it by guessing.

---

# 2. WHAT “100% READ” MEANS FOR THIS TASK

The phrase `100% READ` is NOT satisfied by reading only the current central branch or a curated list of important files.

CCI must build a coverage manifest and process all repository knowledge surfaces that can plausibly contain project meaning.

## 2.1 Current central branch

Inventory the full tree of frozen base commit `a37423639f7dabb0dfd55c8656d4689bb8a25351`.

Every file must receive a manifest row.

Every human-readable file must be read or explicitly classified as non-semantic/generated/duplicate.

This includes at minimum:
- Markdown/text;
- CSV/TSV;
- JSON/JSONL/YAML;
- KML/XML when it contains travel/candidate semantics;
- scripts/configuration if they encode project rules, statuses, grades or assumptions;
- source data and generated decision registries;
- README, task, status, result, freeze, handoff, decision and governance files.

PDFs and other generated documents:
- If the same semantic content is demonstrably present in a readable source file, mark the PDF as `DERIVED_DUPLICATE` with source linkage.
- If a PDF may contain unique human knowledge not available elsewhere, its text/content must be inspected.

Images/binary assets:
- Record them in the manifest.
- Do not waste time visually inspecting ordinary decorative/generated assets unless filenames, metadata or context indicate they may encode unique travel decisions or annotations.

## 2.2 All repository branches / refs

Enumerate repository branches relevant to the India project, including worker/task branches.

For every unique human-readable blob reachable from those refs that is NOT already covered by the frozen central tree:
- read it once;
- map all paths/refs where it occurs;
- classify whether its knowledge was integrated, superseded, rejected, abandoned, still pending, or never reconciled.

A worker `COMPLETE` flag is not central acceptance.

Deduplicate identical file contents by blob SHA. Identical blobs do not need semantic rereading five times, but every path/ref occurrence must remain traceable.

## 2.3 Git history / removed layers

The repository history is explicitly in scope because foundational files have already been found there after disappearing from the current tree.

Inspect history for deleted, renamed, replaced or overwritten files that can contain enduring project knowledge.

Priority signals include, but are not limited to:
- PROJECT
- METHODOLOGY
- PRIORITY
- MARK
- DECISION
- LOCK
- PREFERENCE
- CANON
- GOVERNANCE
- HANDOFF
- CURRENT_STATE
- PROFILE
- ROUTE
- TRANSFER
- HOTEL
- SLEEP / BASE
- DWELL / DURATION
- A_PLUS / A/B/C
- SKIP / DROP / EXCLUDE
- REOPEN / SUPERSEDE
- AOAY / KRIYA / lineage / devotee
- itinerary / calendar / day cards
- research freezes and reconciliation outputs.

Do not assume old = invalid. Do not assume current file = complete.

Historical knowledge must be classified using the actual later provenance chain.

## 2.4 Commit messages

Inspect commit messages across relevant history for explicit decisions, corrections, supersession clues or otherwise unique semantic information not safely preserved in file contents.

Do not treat routine mechanical commit messages as knowledge atoms.

## 2.5 Pull requests / review discussion

PR #23 is mandatory full read, including:
- PR body;
- all top-level conversation comments;
- review comments/threads where accessible;
- relevant changed-file history if a comment depends on it.

Also inspect other PRs/issues if repository archaeology reveals that decision-relevant Mark/INDIA/CCI information lives there.

A discussion statement is not automatically current canon; classify it by provenance and later decisions.

---

# 3. REQUIRED CLASSIFICATION FOR EVERY KNOWLEDGE ITEM

For every decision-relevant atom, distinguish at least:

- `CURRENT_CANON` — presently applicable and supported by provenance.
- `CURRENT_PREFERENCE` — presently applicable Mark preference/goal/working style.
- `CURRENT_LOCK` — explicit current Mark lock.
- `CURRENT_FACT_WITH_RECHECK_TRIGGER` — useful current planning fact that may require time-sensitive recheck before booking/use.
- `HISTORICAL_PROVENANCE_ONLY` — useful to understand evolution but not current truth.
- `SUPERSEDED` — explicitly replaced by later valid material.
- `REJECTED_BY_MARK` — current rejection/C unless explicitly reopened.
- `INVALID_DECISION_RECORD` — something once written as a Mark decision that was later shown not to have been a valid user decision.
- `WORKER_ONLY_NOT_INTEGRATED` — finding exists but was never adopted centrally.
- `DUPLICATE` — same semantic content elsewhere.
- `CONFLICT_NEEDS_RECONCILIATION` — sources disagree and no safe provenance resolution exists.
- `UNREACHABLE_OR_UNREADABLE` — only when technically impossible; explain exactly why.

Never collapse these categories into a generic “old”.

---

# 4. HARVEST THE WHY, NOT ONLY THE LABEL

A successor knowing only `PLACE = A+` is not knowledge parity.

For Mark decisions and major preferences, preserve the reason and experiential meaning when recoverable.

Examples of the level required:
- not merely `Mahavatar Babaji Cave = protected`; preserve that Mark said the cave is almost reason #1 for going to India;
- not merely `Arunachala = A+`; preserve the Yogananda/Ramana cross-link and why exact physical continuity matters to Mark;
- not merely `Delhi short`; preserve Mark’s actual preference/aversion and the implications for pace;
- not merely `Haidakhan = A+`; preserve the personal spiritual reason and the desired experiential space;
- not merely `Sahi River View locked`; preserve the trusted-person recommendation, balcony-room wish and contact context if still current;
- not merely `C`; preserve enough provenance that a successor does not present the same rejected item again as a new choice.

Use short direct Mark quotes only where they carry meaning that is otherwise lost. Do not fill the successor layer with conversational noise.

---

# 5. FOUNDATION / PHILOSOPHY MUST BE RECOVERED

Do a deliberate archaeology pass for the original project vision and determine which parts remain applicable.

Known examples that MUST be reconciled, not blindly copied:

1. Historical `PROJECT.md` stated that the knowledge object is the physical visitable place, not the master/person; persons are detectors.
2. It separated three axes: intrinsic spiritual/place weight, Mark personal attraction, and logistics/route priority.
3. Historical `PRIORITY_GROUPS.md` contained Mark’s personal 13-person index, while explicitly saying place strength outweighs person rank and the index excludes nothing.
4. Historical `NOT_TO_BE_MISSED` framing asked which places Mark would later deeply regret having missed, rather than filling category gaps.
5. Historical Mark decision records established a devotionele presentation layer: why devotees go, what they do, whether Mark can participate, atmosphere, then evidence limits.
6. Lineage/tradition/institutional confirmation can be a valid project evidence domain distinct from classical historical proof.
7. Place experience — beauty, calm/chaos, commercial dominance, intimacy, photography, ability to sit/meditate — is a separate relevant travel axis.
8. Historic-site continuity can remain valuable when the exact old structure no longer survives, if the same historic grounds are secure.
9. A physical parent site/compound generally receives one Mark decision; rooms/shrines/gates/verandas/microsites remain preserved below it rather than repeatedly asking Mark to grade the same terrain.

For each such principle, determine:
- still current;
- later superseded;
- narrowed/expanded;
- contradicted;
- lost from current boot layer but still valid.

---

# 6. DECISION-LOSS AUDIT

Perform an explicit repository-wide search for user/Mark decision signals, not just filenames.

Search content for variants such as:
- Mark
- gebruiker / user
- keuze / besluit / beslist / gekozen
- wil / wens / voorkeur
- belangrijk / hoofdreden / reden
- zeker / absoluut / beslist niet
- skip / drop / exclude / niet bezoeken
- reopen / heropen
- locked / LOCKED_BY_MARK
- A+ / A* / A / B / C
- hotel / verblijf / kamer / balkon
- ashram stay / sleepbase / slaapbasis / nights
- dwell / duration / dagen / nachten
- route / trein / vlucht / auto / transfer
- tempo / rust / breathing room / mediteren / ochtend / avond
- photo / sfeer / chaos / mooi / natuur
- companion / guide / booking / access.

Every meaningful hit must either:
- map to a current knowledge atom;
- map to a superseded/rejected item;
- be explicitly classified as non-decision context.

This audit is specifically intended to catch decisions hidden in generic `RESULT.md`, `STATUS.md`, comments or old branch material.

---

# 7. CURRENT DECISION RECONCILIATION

Build one reconciled master of current Mark-controlled items.

At minimum include:
- all current A+/A/A*/B/C location grades;
- parent/microcluster relations where relevant;
- cluster inclusion/exclusion status;
- hotels and sleepbases;
- ashram-stay intentions;
- nights/duration locks;
- route-mode preferences and exclusions;
- already-fixed transfer or day-shape rules;
- personal experiential requirements;
- explicit things that MUST NOT be re-asked;
- explicit OPEN questions that genuinely still require Mark.

For each current item retain:
- canonical plain-language identity;
- current state;
- Mark reason/WHY if known;
- source chain;
- superseded predecessor(s) if helpful;
- `DO_NOT_REASK` yes/no;
- `RECHECK_TRIGGER` if time-sensitive.

Never infer a grade from worker recommendation.

---

# 8. SUPERSEDED / DO-NOT-REVIVE LAYER

Build a durable anti-regression register.

This is critical because successors repeatedly mistake old material for current truth.

Include cases such as:
- an old hotel/sleepbase later replaced;
- old exact calendars later invalidated by transfer realism;
- old cluster states later superseded by the fixed-core controller;
- invalid “Mark dropped this” records that were later shown to be a misread user question;
- C locations that later research rediscovered but did not reopen;
- worker COMPLETE outputs not integrated;
- obsolete route structures;
- duplicated person/place identities that must not be merged.

Each entry must state:
- what tempting old claim exists;
- why it is not current;
- what supersedes it;
- what a successor must do instead.

---

# 9. REQUIRED OUTPUTS

All outputs live under:
`runs/active/CCI-FULL-REPO-KNOWLEDGE-HARVEST-001/`

CCI may create additional supporting files, but the following are mandatory.

## 9.1 `COVERAGE_MANIFEST.csv`

One row per relevant repository surface/object occurrence, with enough fields to prove coverage.

Minimum columns:
- surface_type (`current_tree`, `branch_blob`, `history_blob`, `commit_message`, `pr_comment`, `review_comment`, `issue`, etc.)
- ref_or_commit
- path_or_identifier
- blob_sha_or_comment_id
- size_if_known
- semantic_type
- read_status
- duplicate_of
- relevance
- currentness_class
- superseded_by
- conflict_id
- knowledge_output_destination
- notes.

The manifest must make it possible to answer: “Which human-readable items were not read?”

## 9.2 `KNOWLEDGE_ATOMS.jsonl`

Structured lossless harvest of decision-relevant knowledge.

Suggested fields:
- atom_id
- category
- statement
- mark_reason
- currentness_class
- subject_ids/names
- source_refs
- valid_from
- supersedes
- superseded_by
- do_not_reask
- recheck_trigger
- confidence/provenance note
- surfaced_in.

Do not force fields where unknown; preserve uncertainty.

## 9.3 `MARK_CURRENT_CANON_MASTER.md`

Human-readable current Mark canon and preferences with reasons.

This is NOT merely a grade list.

Include current decisions, locks, experiential preferences, pace/dwell expectations, hotel/base preferences, route principles and personal meanings that materially change travel planning.

## 9.4 `PROJECT_PHILOSOPHY_AND_SELECTION_MODEL.md`

Recover the enduring project vision:
- physical place vs person;
- spiritual density / place strength;
- Mark personal attraction;
- route value as separate axis;
- NOT_TO_BE_MISSED logic;
- evidence domains including lineage/tradition;
- devotionele presentation requirements;
- site continuity vs building continuity;
- parent vs microcluster decision rule;
- beauty/experience/sphere axis;
- any later superseding rules.

This file must distinguish `CURRENT` from `HISTORICAL_BUT_SUPERSEDED` ideas.

## 9.5 `CURRENT_TRAVEL_EXECUTION_CANON.md`

Current practical trip architecture only:
- booked trip window;
- fixed cores;
- duration-closed worlds;
- current route/transfer philosophy;
- sleepbase/hotel locks;
- ashram-stay count/intent;
- current fixed-core controller;
- open vs closed route decisions;
- time-sensitive facts and explicit recheck triggers.

Do not resurrect old exact calendars as current.

## 9.6 `SUPERSEDED_AND_DO_NOT_REVIVE.md`

Anti-regression register described above.

## 9.7 `OPEN_MARK_DECISIONS_ONLY.md`

Only genuine current subjective choices still requiring Mark.

Purpose: stop successors from asking five times about settled matters.

Every entry must explain why it is actually open and prove that no later valid Mark decision closes it.

## 9.8 `SUCCESSOR_START_HERE.md`

This is the minimal boot surface for INDIA13+.

It must tell the successor exactly what to read and in what order.

Design principle:
- small enough that a successor will actually read it;
- rich enough to prevent ordinary knowledge loss;
- links to the deeper masters above rather than duplicating everything.

Suggested boot order:
1. `SUCCESSOR_START_HERE.md`
2. `MARK_CURRENT_CANON_MASTER.md`
3. `PROJECT_PHILOSOPHY_AND_SELECTION_MODEL.md`
4. `CURRENT_TRAVEL_EXECUTION_CANON.md`
5. `SUPERSEDED_AND_DO_NOT_REVIVE.md`
6. `OPEN_MARK_DECISIONS_ONLY.md`
7. current controller/task file relevant to the next real travel task.

## 9.9 `HARVEST_REPORT.md`

Final audit report with:
- frozen base commit;
- branches/refs inspected;
- total manifest objects;
- unique readable blobs;
- blobs read;
- duplicates deduplicated;
- binaries/derived assets classified;
- historical deleted/renamed blobs recovered;
- PR/comments read;
- number of knowledge atoms;
- current canon atoms;
- superseded atoms;
- unresolved conflicts;
- technically unreadable items;
- explicit statement whether `100_PERCENT_SEMANTIC_COVERAGE = YES/NO` under this task definition.

Do NOT say YES when unread relevant material remains.

---

# 10. QUALITY CHECKS BEFORE DECLARING COMPLETE

CCI must perform at least these self-checks.

## A. Mark-signal backscan

After building the knowledge layer, repeat repository-wide searches for Mark/decision/preference/lock signals.

Every significant result must map to the harvest or be consciously classified as noise/history.

## B. Grade conflict scan

Search all occurrences of current location names/IDs with A+/A*/A/B/C labels.

Verify that conflicting old labels are either:
- superseded with provenance;
- current with provenance;
- unresolved and flagged.

## C. Hotel/sleepbase scan

Search all hotel, guesthouse, ashram-stay and sleepbase records.

Verify that no old choice can accidentally be presented as current without encountering `SUPERSEDED_AND_DO_NOT_REVIVE.md`.

## D. Route/calendar scan

Search exact calendars, route versions, transfer ledgers and duration files.

Make clear which are current architectural truth and which are historical comparison only.

## E. Worker-integration scan

For each significant worker output, determine whether it was integrated/accepted centrally.

`COMPLETE` != central truth.

## F. Foundation-loss scan

Compare original/history versions of PROJECT/METHODOLOGY/PRIORITY/decision-framework files with the new top layer.

Any still-valid principle missing from the top layer is a harvest failure.

## G. Random semantic audit

Take a nontrivial random/sample selection across old and current layers and ask:
“If a successor read only the proposed successor layer, would this file contain any current-applicable decision/reason/rule they would still be missing?”

Any YES result requires another harvest pass.

---

# 11. KNOWN SEEDS FOUND BY INDIA12 — VERIFY, DO NOT TRUST BLINDLY

INDIA12 already found examples proving that earlier boot layers were incomplete. CCI must independently verify them and then search for more.

Known seeds:

- `governance/MARK_DECISION_PARENT_MICROCLUSTER_RULE_2026-08-20.md` — one physical parent/compound generally equals one Mark choice; microsites beneath it are preserved without repeatedly asking Mark.
- `governance/MARK_HISTORIC_SITE_CONTINUITY_RULE_2026-08-20.md` — same historic grounds can retain value even if the exact structure was rebuilt.
- historical `PROJECT.md` — physical visitable place is the knowledge object; persons are detectors; separate spiritual weight, personal attraction and route priority.
- historical `PRIORITY_GROUPS.md` — 13-person Mark index plus place-strength-first and non-exclusion rules.
- historical `NOT_TO_BE_MISSED` framework — regret-prevention over category completion.
- historical `DECISION-0005` — lineage/tradition evidence domains and devotionele presentation order.
- historical `DECISION-0006` — place-experience axis and basis-selection philosophy.
- historical `DECISION-0007` — strict ABC semantics, later semantic evolution must be reconciled.
- `research/deep-research/MAHAVATAR-BABAJI-CAVE-A.md` — Mark quote: “Die grot is bijna reden 1 voor me om naar India te gaan. A dus.” Later grade evolution must be reconciled while preserving WHY.
- `research/YOGANANDA_RAMANA_ARUNACHALA_POST_FREEZE_NOTE_2026-08-18.md` — exact-physical-place interest materially strengthens Arunachala for Mark.

These are examples, not the full task.

---

# 12. CURRENT PROTECTED GUARDS ALREADY KNOWN — VERIFY AGAINST REPO

Do not change these merely because an older file differs. Verify their provenance during harvest.

Known current guards include:
- only Mark changes subjective grades/locks;
- C is not a reserve suggestion unless explicitly reopened;
- existing A/B/C/locks are checked before presenting a location/hotel/base/route choice;
- Haidakhan Babaji and Mahavatar Babaji identity claims must not be silently merged;
- eastern route family previously skipped by Mark must not silently re-enter this trip;
- old false Braj “dropped by Mark” record was invalidated; current status must be derived from latest valid controller;
- exactly two intended ashram sleep experiences currently matter: Haidakhan and, if accepted/available, Sri Ramanasramam;
- worker COMPLETE does not automatically create central truth;
- current fixed-core planning controller supersedes old exact itineraries where explicitly stated;
- breathing room and experiential depth matter; route compression is not the goal.

Again: verify, do not merely copy this list.

---

# 13. CHECKPOINTING

CCI may work for as long as required and should commit durable checkpoints.

Recommended checkpoints:
1. `MANIFEST_CURRENT_TREE_COMPLETE`
2. `ALL_REFS_UNIQUE_BLOBS_INVENTORIED`
3. `HISTORY_FOUNDATION_ARCHAEOLOGY_COMPLETE`
4. `PR23_AND_DISCUSSION_COMPLETE`
5. `KNOWLEDGE_ATOMS_FIRST_PASS`
6. `DECISION_RECONCILIATION_COMPLETE`
7. `SUCCESSOR_LAYER_DRAFTED`
8. `BACKSCAN_COMPLETE`
9. `HARVEST_COMPLETE`

Do not declare final COMPLETE merely because the task has become large.

---

# 14. STOP CONDITION

CCI stops only when all of the following are true:

1. Every object required by the task definition has a manifest row.
2. No relevant human-readable current-tree file remains unread.
3. Unique relevant branch blobs outside central have been read/classified.
4. Relevant deleted/replaced historical foundation and decision material has been recovered/classified.
5. PR #23 discussion has been read/classified.
6. Current Mark canon has a provenance chain.
7. Superseded material has an anti-revival mapping.
8. Genuine open Mark decisions are isolated from closed ones.
9. Foundation principles still applicable are present in the successor layer.
10. A second backscan finds no material current-applicable knowledge absent from the successor layer.
11. `HARVEST_REPORT.md` truthfully reports coverage and remaining gaps.

If a technically unreachable surface prevents 100%, report exactly what remains and set `100_PERCENT_SEMANTIC_COVERAGE = NO` rather than pretending.

---

# 15. HANDOFF BACK TO INDIA

When complete:

- commit all outputs on `agent/cci-full-repo-knowledge-harvest`;
- do NOT merge into central;
- post one concise result comment on PR #23 containing:
  - task ID;
  - final commit SHA;
  - `100_PERCENT_SEMANTIC_COVERAGE = YES/NO`;
  - counts from `HARVEST_REPORT.md`;
  - unresolved conflicts/gaps;
  - exact files proposed as the new successor boot layer;
  - explicit statement that no Mark A/B/C/hotel/base/route decision was changed by CCI.

INDIA will perform one integration review and then decide what should be promoted centrally.

END OF TASK

# PRUNING / DEPRECATION RECOMMENDATION (Task 006, Section E)

```
task_id: INDIA9-SUCCESSOR-BOOT-KNOWLEDGE-ARCHITECTURE-006
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: assessment only. Mark's "may be deleted if it is baggage" is permission to
      assess, NOT permission to delete now. Nothing in this file is executed.
```

## Remain forever as provenance

- `decisions/DECISION-0001..0014-*.md` (the numbered-decision protocol generation) —
  these are primary-source Mark decisions with dates and rationale; even where fully
  superseded in role, they are the only record of *why* (see DECISION-0002's
  first-hand Ram Dass source citations). Never delete.
- `research/active/{BRAJ,KUMAON,VARANASI,VRINDAVAN}*-COMPLETE-001/**` — legacy
  BRONS/ZILVER/GOUD pipeline research. Superseded in *role*, but the underlying source
  registries (`sources/registry.jsonl`, `sources/rejected.jsonl` within each package)
  are exactly the kind of primary-research trail that should never be treated as
  disposable, even after the decisions built on them are superseded.
- `PROTECTED_CANON_BASELINE.csv` and all files inside
  `INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/` — not provenance, this is **live,
  unmerged canon** (see Section F fix #1). Do not touch pending merge.

## Mark superseded/deprecated but retained

- `pipeline/**` (the abandoned parallel framework: protocols/roles/templates/tests/
  reviews/proposals/directives/learning/regression/validators/ENTRYPOINT.md/
  VERSION.md/QUALITY_GATE.md etc.) — mark every file's role as superseded by `india4/`
  in one pass (a single `SUPERSEDED_BY.md` stub at `pipeline/README.md` pointing to
  `india4/`, per the failure-analysis fix, is enough — no need to touch every file).
- `persons/PERSON-*.md`, `places/PLACE-*.md`, `sources/SOURCE-*.md`,
  `templates/*_TEMPLATE.md`, `knowledge/**` — the abandoned early structured-KB schema.
  Same treatment: one stub declaring the schema superseded by `india5/` +
  `runs/active/*` conventions, retain the files as-is.
- root-level legacy meta files: `README.md`, `OPERATING_MODEL.md`, `LESSONS.md`,
  `CHAT_DISTILLATION.md`, `CHATGPT_HANDOFF.md`, `CHATGPT_ROLE.md`, `CURRENT_FOCUS.md`,
  `PROJECT.md`, `AI_RULES.md`, `METHODOLOGY.md`, `VOCABULARY.md`, `PRIORITY_GROUPS.md`,
  `LOCKED_A.md`, `LOCKED_B.md`, `LOCKED_C.md` — superseded in role by `governance/` +
  `handoffs/` + `PROTECTED_CANON_BASELINE.csv`, but `LOCKED_A/B/C.md` specifically
  should be diffed line-by-line against the canon baseline (Section A finding) before
  being marked fully superseded — flag, don't yet stamp.
- root-level legacy candidate lists: `BODH_GAYA_CANDIDATES.md`, `VARANASI_CANDIDATES.md`,
  `KOLKATA_SERAMPORE_CANDIDATES.md`, `KUMAON_CANDIDATES.md`, `PURI_CANDIDATES.md`,
  `AOAY_MASTERS.md`, `CLUSTER_LOCATIONS.md`, `CLUSTER_ANCHORS.md`,
  `CLUSTERS_OVERVIEW.md` — superseded by `ALL_FINDINGS_LOCATION_MASTER.jsonl` + current
  route/cluster files. Mark superseded, retain.
- TOP11 blind-sweep intermediate stages (`TOP11-PARALLEL-CHATGPT-SWEEP-001`,
  `TOP11-*-BLIND-SWEEP-001`, `TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001`, etc.) —
  deliberately-superseded working stages of a reconciliation chain this session itself
  ran end-to-end. Mark superseded by their corresponding `*-RECONCILIATION-001`
  packages, retain as the audit trail for how the final reconciliation was reached.

## Moved/archived

- The 6 duplicate-content `india9-full-byte-audit-*` variant branches whose tree is
  byte-identical to the frozen central commit and carry no unique content of their own
  beyond `agent/cci-india9-full-byte-audit` (`agent/india9-audit-ledger-canonical`,
  `agent/india9-byte-audit-manifest`, `agent/india9-full-byte-audit-2`,
  `agent/india9-full-byte-audit-checkpoint`, `agent/india9-full-byte-audit-final`,
  `agent/india9-full-byte-audit-ledger`, `agent/india9-full-byte-audit-ledger-v2`,
  `agent/india9-full-byte-audit-v1`, `agent/india9-full-byte-audit-working` — 9 branches,
  confirmed tree-identical to central at task 004's freeze) — these are exactly the
  63.4%-of-union self-inflation finding from task 005. Recommend: archive (rename with
  an `archived/` prefix or record their SHAs in a manifest and delete the refs) once a
  human confirms none of them is an in-progress task someone still intends to push to.
  Do NOT delete outright without that confirmation — a branch that looks like a stale
  duplicate could still be someone's active working branch mid-edit.

## Safely prunable only after reference audit

- The 8 replicated `india9-full-byte-audit-*` branches above (candidates for deletion,
  not just archival, once confirmed genuinely inert — i.e. once it's confirmed no PR,
  no in-flight session, and no external reference points at them specifically rather
  than at `agent/cci-india9-full-byte-audit`).
- The ~15 pre-INDIA8 legacy branches (`controller/*`, `feature/*`, `fix/*`,
  `implementation/*`, `improvement/*`, `proposal/*`, `run/*`, `transition/*`,
  `india/kumaon-v2-sweep-b-001`, `varanasi-goud-completion`,
  `worker/varanasi-complete-001-brons-20260720`) that carry the
  `research/active/*-COMPLETE-001` legacy pipeline content — prunable as *branches*
  once their content is confirmed retained via the provenance rule above (i.e. once the
  content itself lives on somewhere durable — it does not need to survive as 15
  separate branch refs to be preserved as provenance; one archival copy is enough).
- Empty/near-empty newer color branches, if confirmed genuinely empty of unique content
  beyond scaffolding (this pass found `INDIAORANGE-TRAVEL-HEATMAP-PREP-001`,
  `INDIAPAARS-DECISION-RUBRIC-PREP-001`, `INDIAROZE-ROUTE-BUILDER-PREP-001` classified
  `MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT` — prep-stage scaffolding, no unique findings
  identified). Re-check before pruning: this pass's classification of these three was
  by structure/naming, not a full content read.

## Definitely NOT be deleted (pending explicit reference audit + Mark sign-off)

- `agent/indiazilver-cluster-completeness-audit` and
  `agent/cci-india9-full-byte-audit` (this task's own home branch) — both carry live,
  unmerged canon (`PROTECTED_CANON_BASELINE.csv`) and this task's own deliverables.
- Any of the 62 category-1 (`UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED`) files listed
  in `BRANCH_ONLY_SEMANTIC_COVERAGE_LEDGER.jsonl` — by definition, nothing else in the
  repo currently carries this content forward.
- `agent/india8-cluster-casting` — the designated central regiebranch itself.
- Any branch this task did not enumerate (a re-freeze would be needed before touching
  anything not covered by the 54-branch task-004 manifest).

## General rule for this whole section

**Nothing above is an instruction to delete anything now.** The concrete, safe first
step (Section F fix #1) is always additive — merging `PROTECTED_CANON_BASELINE.csv` and
the other category-1 files into central — never subtractive. Deletion/pruning of
branches should wait until: (a) the category-1 content has an additive home in central,
and (b) a human (Mark) has confirmed no branch flagged here is someone's in-progress
work.

---
Geschreven door: CCI. Assessment only, nothing executed.

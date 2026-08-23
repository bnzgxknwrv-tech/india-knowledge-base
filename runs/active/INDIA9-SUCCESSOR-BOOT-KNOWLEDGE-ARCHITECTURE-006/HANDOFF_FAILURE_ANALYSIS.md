# HANDOFF FAILURE ANALYSIS — INDIA1..INDIA9 (Task 006, Section B)

```
task_id: INDIA9-SUCCESSOR-BOOT-KNOWLEDGE-ARCHITECTURE-006
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: independent historical architecture reviewer -- no route/A-B-C/hotel/deletion,
      no protocol implementation. Evidence + recommendations only.
```

Evidence base: the frozen task-004 union (54 branches, 1,680 blobs) and the task-005
source-delta (867 blobs), cross-referenced against frozen central commit
`1e9fd2453e6b4cbc1488f6d275351772f3eba928` by direct `git grep`/`git show`, not by
recollection. Every claim below cites the specific evidence paths checked.

## 1. Old valid Mark canon under-read

**Evidence**: `decisions/DECISION-0001-haidakhan-A.md`, `DECISION-0002-bhumiyadhar-A.md`,
`DECISION-0004-katyayani-peeth-a.md` (dated 2026-07-10..12, an early numbered-decision
protocol, only on branch-only source-delta blobs) each record a specific Mark A-grade
lock. Spot-checking confirmed all three DID survive into current canon —
`KUMAON-V2-RESWEEP-001/RECONCILIATION.md` line 85 literally cites `DECISION-0002` by
name — so in this instance the chain held. But the *mechanism* by which it held was a
human-like manual citation inside one reconciliation file, not a structural guarantee.
Nothing prevents the next file that touches Bhumiyadhar from failing to notice that
citation and re-opening the question, because DECISION-0002.md itself is not reachable
from any boot path — it exists only on a branch nobody is instructed to read.

**Severity**: HIGH (the chain held this time by luck/diligence, not by design).
**Smallest robust fix**: a single `decisions/INDEX.yaml`-equivalent (or a column in
`PROTECTED_CANON_BASELINE.csv`) that records, per locked place, the exact source
decision file, so the "is this old A still current?" check is a lookup, not an
archaeology exercise.

## 2. Stale STATUS/README/bootstrap fields mistaken as current state

**Evidence**: `governance/GLOBAL_REGIE_CANON_AUDIT_2026-08-23.md` (frozen central) still
lists Turiya Niwas and Jageshwar as active anchors — both were re-decided later in the
same day per `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`'s own
account of the India8 "regie fout", and Turiya Niwas was again explicitly dropped by
Mark in this session's chat on 2026-08-23 (see
`runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/MARK_DECISION_KASAR_ALMORA_MODULE_DROPPED_2026-08-23.md`
on CCI's own branch). Three different "as of" states for the same cluster now coexist
in central with no single field a boot process can trust as "the" current answer.

**Severity**: CRITICAL (this is the exact failure mode `INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`
was written to prevent, and it recurred within the same document generation).
**Smallest robust fix**: every status/decision file gets a mandatory `superseded_by:`
front-matter field, null if current; a boot process greps for any file whose path is
never named as someone else's `superseded_by:` target and treats those as the live set.
No file is "current" by virtue of being newest-dated; it is current only if nothing
points past it.

## 3. Newer prose overriding older valid locks without explicit supersedes

**Evidence**: the `research/active/{BRAJ,KUMAON,VARANASI,VRINDAVAN}*` legacy packages
(458 blobs / ~2MB, task-005 Goal A ledger) were superseded by the India8
cluster-casting reorganization, but no file in either the old or new package declares
that relationship explicitly — the supersession is only inferable from directory-name
correspondence and subject-matter overlap, which is exactly the kind of inference a
rushed boot skips.

**Severity**: MEDIUM (correctly reconstructed in this pass, but only via a from-scratch
git-archaeology exercise no live boot process could reasonably repeat every time).
**Smallest robust fix**: when a task package is superseded, drop one `SUPERSEDED_BY.md`
stub (1-2 lines: successor path + date) at the *old* location on the branch that holds
it, even if the branch itself is otherwise frozen. Costs nothing, makes the relationship
discoverable without git-log spelunking.

## 4. Different meanings of SATURATED/completeness across generations

**Evidence**: `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/STATUS.md`'s own
FEED file (`FEED_INDIAZILVER_PARTIAL_GEEL_TURQUOISE_INTEGRATED.md`, in central) declares
state `PARTIAL_COMPLETE__GEEL_TURQUOISE_INTEGRATED__OTHER_FEEDS_ADDITIVE` and explicitly
instructs: *"Once ROOD closes and ZILVER has appended final available feeds, central
INDIA8/9 performs consolidation into ALL_FINDINGS_LOCATION_MASTER."* ROOD did close
(236 rows are in the master). ZILVER's own consolidation never happened —
`PROTECTED_CANON_BASELINE.csv`, `NEW_ID_REQUIRED_QUEUE.csv`,
`PROXIMITY_1KM_3KM_MATRIX.csv`, `DUPLICATE_PARENT_CANDIDATES.md` and
`ABC_REVIEW_AFTER_CLOSURE_QUEUE.md` are all still branch-only (confirmed zero central
references beyond the FEED summary itself). "COMPLETE" in one worker's own status field
and "consolidated into central" turned out to be two different, silently conflated
claims.

**Severity**: CRITICAL — this is the single most consequential concrete finding in this
audit: `PROTECTED_CANON_BASELINE.csv` (92 rows, including `LOCKED_BY_MARK`/`IMMUTABLE`
entries) has never existed in frozen central, at any point across the four independent
audits this session has run (tasks 001, 004, 005, and now 006).
**Smallest robust fix**: a worker's own `STATUS: COMPLETE` must never be read as
"integrated." Define two separate fields — `worker_output_state` (owned by the worker)
and `central_integration_state` (owned only by whichever central task actually merges
the content) — and never let a boot process infer the second from the first.

## 5. Color-worker outputs not integrated to central

**Evidence**: task 004 found 81.9% of the all-branch-tip union's bytes exist only
outside frozen central; task 005's Goal A found 867 of those blobs are genuine
PROJECT/SOURCE content (not audit packaging); this task's Goal A classifies 62 of those
867 blobs (344,876 bytes) as `UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED` even after
crediting every successor relationship this pass could establish. The pattern repeats
across old (six original BLAUW/GEEL/ROOD/TURQUOISE/WIT/ZILVER) and new
(GOUD/ORANGE/PAARS/ROZE, and second-generation WIT/BLAUW/ZILVER task variants such as
`INDIAWIT-HERITAGE-STAY-OVERRIDE-001`, `INDIABLAUW-VISA-READY-PACK-001`) worker
generations alike — this is not a one-time incident, it is the structural default
outcome of the color-worker pattern.

**Severity**: HIGH (structural, recurring across three generations of workers).
**Smallest robust fix**: see Section D — no worker task is allowed to exit `active`
without a corresponding central-integration commit *in the same session*, per the
existing no-deferral rule already written into
`governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` but evidently not
applied to worker-branch integration specifically.

## 6. Branch-only canon such as `PROTECTED_CANON_BASELINE.csv`

Covered in detail under #4 above; restated here because the task explicitly calls it
out as its own bullet. This is the flagship example of the general pattern: a file
whose name literally says "PROTECTED" and "BASELINE" has been unreachable from any boot
path for at least four audit passes this session.

## 7. Chat-only knowledge / insufficient self-replacement

**Evidence**: this session's own conversation contains two genuine Mark decisions
(Turiya Niwas cluster dropped; Bodh Ashram dropped with it) that were durably committed
to `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/MARK_DECISION_KASAR_ALMORA_MODULE_DROPPED_2026-08-23.md`
within the same turn — i.e. the no-deferral/self-replacement rule *was* followed
correctly here. This is included as a positive control: the rule works when applied:
the failure elsewhere is inconsistent application, not an unworkable rule.

**Severity**: LOW in this specific instance (correctly handled); the general risk
remains real elsewhere in the corpus (Section A's category-1 list is the audit trail
for where it wasn't followed).

## 8. Repeated full raw logs versus useful active knowledge

**Evidence**: task 004/005 found that CCI's own audit-packaging output (byte-for-byte
stream + page-slices + review volumes from tasks 002/002R/003) was replicated
byte-identically across 8 `agent/india9-full-byte-audit-*` variant branches, accounting
for 63.4% of the entire all-branch-tip union's bytes. This is a self-inflicted version
of the same failure mode Mark is asking about: raw packaging multiplying faster than
anyone reads it.

**Severity**: MEDIUM (self-contained to CCI's own audit lane, does not corrupt project
canon, but wastes exactly the kind of boot-time budget Section C/D is designed to
protect).
**Smallest robust fix**: this task explicitly did NOT create a new full duplicate
review-volume set for its own output (see task 005's own disclosure) — that discipline
should be written into the audit-branch convention going forward, not left to each
task's individual judgement.

## 9. Precedence rules dispersed across multiple files

**Evidence**: two structurally parallel, never-reconciled project-framework
generations coexist as of this freeze — `pipeline/` (rich: protocols/roles/templates/
tests/reviews/proposals/directives/learning/regression/validators/ENTRYPOINT.md/
VERSION.md/QUALITY_GATE.md, all branch-only except one leftover
`pipeline/ACTIVE_SYSTEM.yaml` in central) versus `india4/` (the actual live framework in
central: `prompts/BRONS-*.md`, `ACTIVE_SYSTEM.yaml`, `START.md`). Nothing in either tree
declares the other abandoned. A companion early-generation structured-knowledge-base
schema (`persons/PERSON-NNNN-*.md`, `places/PLACE-NNNN-*.md`,
`sources/SOURCE-NNNN-*.md`, `templates/*_TEMPLATE.md`, `knowledge/*`) shows the same
pattern: a whole parallel schema generation, quietly dropped, never marked as such.

**Severity**: MEDIUM (confusing for a future regisseur trying to determine "the" active
framework, but does not corrupt place/decision canon directly).
**Smallest robust fix**: one `governance/ACTIVE_FRAMEWORK.md` file naming the single
currently-authoritative framework directory (today: `india4/` + `runs/active/` +
`governance/`), with every other framework generation's root explicitly marked
superseded (see Section E).

## Content mistakes vs. system/handoff mistakes

Items 1, 3, 6, 7 above are primarily **system/handoff mistakes** (the content itself was
usually fine; the mechanism for a successor to find and trust it was missing or
inconsistent). Items 4, 5 are a mix — the underlying place/finding data is generally
sound where it exists, but the *process* for declaring it "done" and pulling it forward
is where the actual defect lives. Item 2 is the one genuine **content-adjacent** mistake
in this set: three different files asserting three different current states for the
same cluster is a content-currency problem, not merely a discoverability one — though
its root cause is still systemic (no `superseded_by` mechanism forcing a single answer).

No content in this pass was found to be factually wrong at the place/evidence level;
every failure identified is a **failure to propagate or reliably rediscover** already-
correct content, which is the good news: the fix is architectural, not a large
correction campaign.

---
Geschreven door: CCI. Evidence-based review only; no protocol changes implemented here.

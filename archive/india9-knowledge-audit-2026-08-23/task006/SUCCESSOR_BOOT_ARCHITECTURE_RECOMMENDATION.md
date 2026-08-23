# SUCCESSOR BOOT ARCHITECTURE RECOMMENDATION (Task 006, Sections C+D)

```
task_id: INDIA9-SUCCESSOR-BOOT-KNOWLEDGE-ARCHITECTURE-006
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: architecture recommendation only -- not implemented, not a canon/route decision.
```

## Section C — critique of the proposed "100% knowledge" model

Proposed model (verbatim from the task): one immutable FULL SEMANTIC BASELINE, trust
unchanged blobs by SHA, freshly read only NEW/CHANGED blobs plus current canon/status/
handoff/precedence files, mechanically (not semantically) cover binaries/audit
packaging, keep superseded logs queryable without consuming boot context, fall back to
full reread if the baseline can't be validated, and forbid substantive work until
`KNOWLEDGE_READY: 100%`.

**Verdict: yes, stronger and safer than brute-force full rereading — with three
amendments.**

1. **The model is directionally correct and this session's own evidence supports it.**
   Task 002/003 already proved SHA-verified lossless byte coverage of an immutable
   baseline is achievable and trustworthy (366/366, then 867/867, zero mismatches
   across independent reconstruction passes). Brute-force full rereading of all 26.97MB
   / 1,680 blobs on every boot (task 004's literal denominator) is not just wasteful —
   task 006 itself is evidence it is not even reliably *finishable* in reasonable time,
   which is exactly the failure mode that prompted this task ("hij kan dat niet in een
   beurt").

2. **Amendment — "immutable" needs a harder definition than "hash matches its own
   previous SHA".** A blob's *content* being unchanged does not mean its *currency* is
   unchanged — Finding #2 in the failure analysis (three coexisting "current state"
   claims for one cluster) happened entirely among files whose individual byte content
   was each internally coherent; the staleness was relational, not textual. The baseline
   certificate must therefore carry not just blob SHAs but **the `superseded_by` graph
   state** (Section D below) at baseline time, and must be invalidated by *any* new
   `superseded_by` edge touching a baseline-covered file, not only by a content change.

3. **Amendment — "decision-relevant content only inside binaries" needs an explicit
   negative-proof step, not an assumption.** Task 001 and this task's own Goal B both
   found the 6 PDFs and all audit-packaging blobs hash-clean with no semantic surprises
   — but that was established by actually generating/checking that, not by asserting it
   a priori. The model should say: binaries are exempt from *rereading* once a semantic
   pass has explicitly confirmed (once, at baseline time) that no binary in the baseline
   carries decision-unique content — not exempt by default.

4. **Amendment — the model needs an explicit answer for "new blob classified but
   ambiguous."** This task's own Goal A required inventing four categories and a
   conservative-default fallback (initially 64 blobs, later resolved to 0 through
   additional rules) precisely because "new/changed since baseline" is not always a
   clean binary. The boot protocol should reuse this task's four-category schema
   (`UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED` / `SEMANTICALLY_REPRESENTED_IN_CENTRAL`
   / `HISTORICAL_INTERMEDIATE_SUPERSEDED` / `MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT`)
   as the standard classification for every delta blob, not re-derive it from scratch
   each generation.

**Failure cases identified for the model as originally stated:**
- Baseline certificate becomes stale relationally (content unchanged, precedence
  changed) — addressed by amendment 2.
- A worker declares `STATUS: COMPLETE` and a boot process reads that as
  `central_integration_state: DONE` (this session's own ZILVER case) — addressed by
  Failure Analysis fix #4 (split the two fields) feeding into Section D's freshness
  gate below.
- A "fall back to full reread" trigger that itself depends on successfully validating
  the baseline manifest — needs a hard circuit-breaker: if manifest validation itself
  fails to complete within one turn, the boot must say so explicitly (checkpoint +
  exact resume prompt, per Section D) rather than silently defaulting to either
  "trust anyway" or an unbounded reread loop.

## Section D — 30-version successor boot protocol

Design goal: reuse `README.md`, the critical-boot doc, the knowledge-gate concept,
task-004/005-style manifests, `ALL_FINDINGS_LOCATION_MASTER.jsonl`, and the PR #23 relay
— add the smallest possible number of new durable artifacts.

### D1. Immutable baseline certificate

One new file per baseline generation:
`governance/KNOWLEDGE_BASELINE_<date>.md` (front matter, not prose), containing:
```
baseline_id, baseline_date, frozen_central_commit, frozen_branch_tip_manifest_ref
total_blobs_covered, total_bytes_covered
supersedes: <previous baseline id or null>
precedence_snapshot_ref: <path to the superseded_by graph dump at freeze time>
semantic_binary_clearance: true/false (was every binary in this baseline confirmed
  free of decision-unique content, and by which task?)
```
This is a direct extension of task 004/005's own manifest pattern — no new mechanism,
just a durable, versioned pointer to "the last time everything was actually read."

### D2. Delta accounting by SHA

Reuse task 004's exact method (`git ls-tree -r -l`, blob-SHA union, category
classification per this task's Section A schema) as a **standing, repeatable
procedure**, not a one-off audit. Every new IndiaN's first substantive act is:
diff the current all-branch-tip union against the latest `KNOWLEDGE_BASELINE_*`
manifest, producing exactly the kind of delta ledger this task's Goal A produced.

### D3. Exact percentage formula

```
byte_weighted_knowledge_pct =
    ( baseline_bytes_covered
    + SUM(size_bytes for delta blobs actually semantically read this generation,
          restricted to category UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED
          and SEMANTICALLY_REPRESENTED_IN_CENTRAL-not-yet-spot-checked) )
    / ( baseline_bytes_covered + total_new_project_source_bytes_since_baseline )
    * 100
```
Category `HISTORICAL_INTERMEDIATE_SUPERSEDED` and `MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT`
blobs count toward the denominator (so the percentage is honest about what exists) but
require only a lighter-weight successor-path confirmation, not a full semantic read, to
count as "covered" in the numerator — exactly the distinction this task's own Goal A/B
split (source-delta full read vs. audit-packaging hash-only coverage) already
demonstrated works in practice.

### D4. Current-authority/precedence map

One durable, continuously-updated file: `governance/PRECEDENCE_MAP.jsonl` — one row per
file that has ever been superseded, `{path, superseded_by, superseded_at, reason}`.
Every status/decision/canon file gets a `superseded_by:` front-matter field (per
Failure Analysis fix #2); a lightweight validator (extends the existing numbering
validator pattern already in `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/scripts/
validate_numbering.py`) confirms the map and the front-matter fields agree.

### D5. `AL BESLIST?` gate for every item presented to Mark

Already exists in principle (`governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`).
Extend it mechanically: before presenting any place/cluster/hotel to Mark, the boot
process does a lookup against `PROTECTED_CANON_BASELINE.csv` (once it is merged to
central — see Section E / Section F fix #1) AND `PRECEDENCE_MAP.jsonl`. A hit in either
is an automatic hard-stop on re-presenting that item as new. This turns the existing
prose rule into a mechanically-checkable gate.

### D6. Multi-turn boot resume checkpoint in GitHub

New small file per boot session: `runs/active/<IndiaN>-BOOT-<date>/BOOT_PROGRESS.md`:
```
knowledge_pct_so_far: <formula from D3>
blobs_read_this_session: <count>
blobs_remaining: <count, with their category-1/2 split>
last_completed_blob_sha: <for exact resume>
next_continuation_prompt: |
  <the exact text Mark should paste to resume boot in the next turn>
```
This is the same checkpoint discipline task 002R invented under real duress (splitting
the oversized read-stream into pages because a single large fetch failed) — formalizing
it as a standing convention removes the need to reinvent it under pressure every time.

### D7. Exact behavior when one turn cannot finish reading

Mandatory: if `blobs_remaining > 0` at the end of a turn, the IndiaN's response MUST
state the exact percentage (D3 formula), write `BOOT_PROGRESS.md` (D6), and give Mark
the literal next-turn prompt — and MUST NOT proceed to substantive travel/route/A-B-C
work in that same turn. This is a direct, mechanical answer to the actual triggering
problem Mark reported ("hij kan dat niet in een beurt... foutmeldingen") — a partial
turn becomes a normal, expected, low-drama checkpoint instead of a silent failure.

### D8. Self-replacement discipline

Already correctly demonstrated this session (Turiya Niwas/Bodh Ashram drop, committed
same-turn). Formalize as a rule extension: any material decision, state change, or
conflict resolution made during a boot or working turn must be committed to GitHub
**before** that turn ends, using the existing worktree-branch-push pattern this session
has used throughout. No new mechanism needed — just explicit inclusion of "boot-time
findings" under the existing no-deferral rule's scope, since Failure Analysis finding #5
shows this specifically has NOT been consistently applied to worker-branch integration.

### D9. No dependence on old chat memory

Already the architecture's design intent (GitHub as durable source of truth). The
concrete gap is D1/D4/D6 above — without them, "no chat memory" just means "full reread
every time," which is the exact problem this section exists to solve.

### D10. Low token/context waste

D3's formula plus D1's baseline certificate is the entire mechanism — a generation only
ever semantically reads the delta, not the baseline. Task 005's own Goal A/B split
(867 blobs fully read + packaged vs. 447 blobs hash-verified without rereading) is a
worked example of exactly this at smaller scale, and its total output (94 review
volumes, ~5MB) is a fraction of what a full-repo reread across 1,680 blobs would cost.

### D11. How IndiaN+1 becomes more knowledgeable than IndiaN, not less

The baseline-certificate chain (D1's `supersedes:` field) plus the always-growing
`PRECEDENCE_MAP.jsonl` (D4) means each generation's boot starts from strictly more
structured knowledge than its predecessor, not the same raw byte pile re-parsed from
scratch. The failure mode this prevents is exactly Failure Analysis #1/#3: a successor
currently has to *rediscover* that DECISION-0002 survived into current canon by manual
git archaeology; under this design, that fact is written once into
`PRECEDENCE_MAP.jsonl` and never has to be rediscovered again.

---
Geschreven door: CCI. Recommendation only, not implemented. INDIA9 + Mark decide
whether/how to adopt before any of this is written into governance/ as binding
protocol.

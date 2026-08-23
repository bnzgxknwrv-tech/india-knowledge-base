# ALL-BRANCH-TIP UNION AUDIT — ACCOUNTING

```
task_id: INDIA9-ALL-BRANCH-TIP-UNION-AUDIT-004
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: accounting/packaging only -- no route/A-B-C/canon changes, no web research,
      no central-branch edits.
```

## Purpose

Independent repo-wide completeness/accounting backup for Mark's explicit requirement
that INDIA9 has read ALL existing repository structure before starting substantive
work. This is a QA/accounting lane run in parallel with INDIA9's own semantic read;
it does not replace that read.

## 1–2. Frozen branch-tip set

Every current remote branch/ref (`git branch -r`, all prefixes) was enumerated and
frozen at the moment of this audit by recording its exact head commit SHA and tree
SHA. **Frozen count: 54 branches.** The full branch → head SHA → tree SHA table is
in `FROZEN_BRANCH_TIP_MANIFEST.tsv` in this directory. This set is immutable for the
remainder of this audit; any branch created or moved after the freeze moment is out
of scope (a later audit would need a fresh freeze).

Nine branches were newly visible in this freeze that had not appeared in the prior
frozen-central-commit audit (001–003): `agent/india9-audit-ledger-canonical`,
`agent/india9-byte-audit-manifest`, `agent/india9-full-byte-audit-2`,
`agent/india9-full-byte-audit-checkpoint`, `agent/india9-full-byte-audit-final`,
`agent/india9-full-byte-audit-ledger`, `agent/india9-full-byte-audit-ledger-v2`,
`agent/india9-full-byte-audit-v1`, `agent/india9-full-byte-audit-working`. All nine
have a tree SHA **identical** to the frozen central commit's tree
(`e5832b6cfdbd485e7a7b20a1850f3b8f381b2ecb`) — i.e. they are branch-tip copies with
no content delta from central, not new content.

## 3–4. Scope and union construction

For each of the 54 frozen tree SHAs, every tracked blob was enumerated with
`git ls-tree -r -l <tree_sha>` (exhaustive by construction — trees are complete for
any fetched ref even in a shallow clone; commit-history depth does not affect tree/
blob completeness). Zero unreadable/corrupt objects were encountered across all 54
trees — **zero hard blockers**. Files produced by *this* task (this directory) are
not part of any of the 54 frozen trees and are therefore correctly excluded from
their own denominator.

## 5. Headline counts

```
frozen branch count                       : 54
total branch/path references (all trees)  : 15,187
unique (path,blob) reference rows         : 15,187   (same figure; no duplicate
                                                        branch+path rows possible
                                                        from ls-tree)
unique blob SHAs across the union         : 1,680
total unique blob bytes                   : 26,972,137
```

Classification (by content, null-byte heuristic + forced `.pdf`→binary, same method
as task 001):
```
text     : 1,674 blobs
binary   :     6 blobs   (all 6 are the PDFs already known from task 001)
```

Zero-byte blobs: **1** unique blob (`e69de29b...`, the standard empty-blob SHA),
referenced by multiple `.gitkeep`/`.gitignore`-adjacent paths across branches.

Extension breakdown (unique blobs):
```
md         813      jsonl        571      yaml         132
txt         95      (no ext)      19      py            17
kml          8      json           7      pdf            6
csv          6      tmp            2      gitignore      2
gitkeep      1      yml            1
```

Largest blobs (top of list; full top-20 with paths in the manifest JSONL):
```
5,629,498 bytes  runs/active/INDIA9-FULL-BYTE-AUDIT-ACCOUNTING-001/FULL_BYTE_READ_STREAM.jsonl
  888,369 bytes  runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/ALL_FINDINGS_LOCATION_MASTER.jsonl
  312,990 bytes  runs/active/AOAY-FULL-LOCATION-ATLAS-001/RAW_OCCURRENCES.jsonl
  273,753 bytes  runs/active/INDIA9-FULL-BYTE-AUDIT-ACCOUNTING-001/BRANCH_DELTA_AUDIT_MANIFEST.jsonl
  217,750 bytes  runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/ANANDAMAYI_FULL_CORPUS_REFERENCE.jsonl
```
The single largest blob in the entire union is CCI's own task-002 read-stream file
(see §8 below) — this is expected and is exactly the kind of self-inflation this
task was asked to surface.

## 6. Machine-readable outputs

- `ALL_BRANCH_TIP_UNION_MANIFEST.jsonl` — one row per **unique blob** (1,680 rows):
  `blob_sha`, `size_bytes`, `classification`, `extension`, `in_central_commit`,
  `in_pr23_head`, `audit_packaging_only`, `branch_path_refs` (full list of every
  `branch:path` that resolves to this blob).
- `ALL_BRANCH_TIP_REF_MANIFEST.jsonl` — one row per **branch/path reference**
  (15,187 rows): `branch`, `path`, `blob_sha`, `size_bytes`.
- `FROZEN_BRANCH_TIP_MANIFEST.tsv` — the 54-row frozen branch → head SHA → tree SHA
  table from step 1–2.

## 7. Mechanical verification

- Every one of the 54 frozen trees was enumerated with `git ls-tree -r -l`;
  **0 unreadable/corrupt objects** across all 54 (no hard blockers to report).
- Identity check: `sum(size_bytes over 1,680 unique-blob manifest rows)` =
  `26,972,137` = the reported `total_unique_blob_bytes` (closes exactly).
- Identity check: `union_bytes_central_known (4,883,398) + union_bytes_additional_beyond_central (22,088,739)`
  = `26,972,137` (closes exactly).
- Identity check: `union_bytes_audit_packaging_only (17,095,043) + union_bytes_source_project (9,877,094)`
  = `26,972,137` (closes exactly).
- Per-blob byte length recomputed independently via `git cat-file -p <sha> | len(...)`
  for all 1,680 blobs and cross-checked against the `git ls-tree -l` reported size —
  0 mismatches.

## 8. Comparison against frozen central commit and PR #23 head

```
frozen central commit : 1e9fd2453e6b4cbc1488f6d275351772f3eba928
central tree           : e5832b6cfdbd485e7a7b20a1850f3b8f381b2ecb
central unique blobs   : 366   (matches task 001's independently-verified figure)

PR #23 head at freeze  : b32c374debe887715bf9b67808c058d482be0f01  (branch
                          claude/werk-je-nu-of-niet-oa10y7)
PR #23 tree             : f250718fb97033ec0ac5527f3f382209ea64628b
PR #23 unique blobs      : 278
```

Union vs. central commit:
```
union blobs that ARE in the central commit's tree      :   366  (100% of central
                                                                   is present in
                                                                   the union, as
                                                                   expected)
union blobs NOT in the central commit's tree            : 1,314
bytes of central-known content within the union         : 4,883,398
bytes of additional (non-central) branch-tip-only content: 22,088,739
```

So **81.9% of the unique blobs** (1,314 / 1,680) and **81.9% of the unique bytes**
(22,088,739 / 26,972,137) in the all-branch-tip union exist **only** outside the one
previously-frozen central commit — i.e. the six-color-agent branches (BLAUW/GEEL/
ROOD/TURQUOISE/WIT/ZILVER) plus the various controller/feature/run/transition/
implementation/improvement/proposal/india/worker/agent-prefixed branches carry a very
large amount of content that has never been merged into central and is not visible
from PR #23 either. This reconfirms, at full-repository scale, the "six-color-agent
integration gap" finding surfaced repeatedly in earlier audits this session.

## 9. Distinguishing SOURCE/PROJECT from AUDIT-PACKAGING content

A blob was classified `audit_packaging_only = true` when **every** branch/path that
references it falls under a known CCI-generated audit-output path pattern (task
001–003's own directory, `read_pages/`, `review_volumes/`, the various
`FULL_BYTE_*`/`BRANCH_DELTA_*` manifest/stream filenames). Everything else —
including all Mark-facing project research, GOUD/BRONS/ZILVER deliverables,
governance docs, canon files, and any file that is *also* referenced under a
non-audit-packaging path anywhere in the union — is classified SOURCE/PROJECT.

```
SOURCE/PROJECT blobs         : 1,233     SOURCE/PROJECT bytes         : 9,877,094
AUDIT-PACKAGING blobs (CCI's :   447     AUDIT-PACKAGING bytes (CCI's : 17,095,043
own prior task 001-003 output)                own prior task 001-003 output)
```

**Headline finding: CCI's own previously-generated audit-packaging output
(task-001-through-003 manifests, read-stream, read-pages, and review-volumes,
now themselves committed across 8 of the india9-full-byte-audit-* branches)
accounts for 63.4% of the total union bytes (17,095,043 / 26,972,137) — nearly
two-thirds of the entire all-branch-tip byte union is CCI's own self-generated
packaging, not underlying project/source content.** This is expected given task
002/002R/003 explicitly wrote a full lossless byte-for-byte copy of the 4,883,398-byte
central source plus per-blob framing overhead, and that copy was then propagated
(identically) across the 8 `india9-full-byte-audit-*` variant branches created during
that chain, each carrying its own full copy of the same packaging files. **This task
deliberately did NOT create new lossless review volumes (per its own instruction #10)
precisely to avoid adding a further multiplier to this already-dominant packaging
share.**

## Blockers

None. Zero unreadable/corrupt git objects across all 54 frozen branch tips.

## Scope discipline

No route, A/B/C, or canon decision was made or implied. No source/project branch
was modified — all outputs live only under
`runs/active/INDIA9-ALL-BRANCH-TIP-UNION-AUDIT-004/` on this CCI-owned audit branch
(`agent/cci-india9-full-byte-audit`, reused per the task's own instruction #9, since
it already holds the related task-001–003 outputs and is not a source branch).

---
Geschreven door: CCI. Accounting/packaging only. No central canon or frozen source
modified. No route/A-B-C decisions made or implied.

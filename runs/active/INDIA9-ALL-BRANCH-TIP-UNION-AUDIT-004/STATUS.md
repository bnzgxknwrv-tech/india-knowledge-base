# STATUS — INDIA9-ALL-BRANCH-TIP-UNION-AUDIT-004

```
task_id: INDIA9-ALL-BRANCH-TIP-UNION-AUDIT-004
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: accounting/packaging only
status: COMPLETE
```

## Outputs

- `ALL_BRANCH_TIP_UNION_ACCOUNTING.md` — full narrative accounting: frozen 54-branch set,
  union construction method, headline counts, classification/extension breakdown, largest
  blobs, mechanical verification/identity checks, comparison against frozen central commit
  `1e9fd2453e6b4cbc1488f6d275351772f3eba928` and PR #23 head
  `b32c374debe887715bf9b67808c058d482be0f01`, and SOURCE/PROJECT vs AUDIT-PACKAGING split.
- `ALL_BRANCH_TIP_UNION_MANIFEST.jsonl` — 1,680 rows, one per unique blob SHA across the
  union: size, classification, extension, `in_central_commit`, `in_pr23_head`,
  `audit_packaging_only`, full `branch_path_refs` list.
- `ALL_BRANCH_TIP_REF_MANIFEST.jsonl` — 15,187 rows, one per branch/path reference.
- `FROZEN_BRANCH_TIP_MANIFEST.tsv` — the 54-row frozen branch → head SHA → tree SHA table
  (step 1-2 of the task), locked before any blob enumeration began.
- `STATUS.md` — this file.

## Headline numbers

```
frozen branch count                     : 54
total branch/path references            : 15,187
unique blob count (union)               : 1,680
total unique blob bytes (union)         : 26,972,137
  text                                    : 1,674 blobs
  binary                                  :     6 blobs (the 6 PDFs)
  zero-byte                               :     1 blob
hard blockers (unreadable objects)      : 0

central-known within union              :   366 blobs /  4,883,398 bytes
additional (non-central) in union       : 1,314 blobs / 22,088,739 bytes  (81.9%)

SOURCE/PROJECT content                  : 1,233 blobs /  9,877,094 bytes  (36.6%)
AUDIT-PACKAGING content (CCI's own      :   447 blobs / 17,095,043 bytes  (63.4%)
  prior task 001-003 output, replicated
  across 8 india9-full-byte-audit-* branches)
```

## Headline finding

63.4% of the entire all-branch-tip union's bytes are CCI's own previously-generated
audit-packaging output (the task-002/002R/003 lossless stream + pages + review volumes),
which was replicated identically across 8 `agent/india9-full-byte-audit-*` variant
branches during that chain. Per the task's own instruction #10, this task did NOT
generate new lossless review volumes, specifically to avoid adding a further multiplier
to an already-dominant packaging share.

81.9% of the union's unique bytes (22,088,739 / 26,972,137) exist only outside the single
previously-frozen central commit — confirming at full-repo scale the six-color-agent
branch integration gap already flagged in task 001.

## next_allowed_step

None required of CCI for this task. INDIA9 (and/or Mark) should decide whether to prune
or consolidate the redundant `india9-full-byte-audit-*` variant branches (8 of them carry
byte-identical trees to the frozen central commit plus, in most cases, no unique content
of their own beyond what's already on `agent/cci-india9-full-byte-audit`), and separately
whether/how to integrate the six-color-agent branches' unmerged content into central.

## Guardrails respected

No route choice, no A/B/C, no canon decision made or implied. No source/project branch
modified — all outputs live only on this CCI-owned audit branch
(`agent/cci-india9-full-byte-audit`, reused per the task's own instruction #9).

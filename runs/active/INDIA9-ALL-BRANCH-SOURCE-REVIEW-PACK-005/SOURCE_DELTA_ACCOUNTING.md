# SOURCE DELTA — ACCOUNTING (Goal A)

```
task_id: INDIA9-ALL-BRANCH-SOURCE-REVIEW-PACK-005
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: deterministic packaging/accounting only -- no research, no route/A-B-C/canon
      changes, no web.
frozen_universe: task INDIA9-ALL-BRANCH-TIP-UNION-AUDIT-004, commit 4c614fd (denominator
                 unchanged -- no re-freeze performed for this task, per instruction).
```

## What this is

The set of unique blobs classified PROJECT/SOURCE in the frozen 54-branch union
(`ALL_BRANCH_TIP_UNION_MANIFEST.jsonl`, task 004) that are **not** already part of the
frozen central commit `1e9fd2453e6b4cbc1488f6d275351772f3eba928` (already fully packaged
and verified as 93 review volumes in task 003). This is genuinely new project/source
content, not yet in any lossless human-readable review pack, sitting on non-central
branches.

## Independently recomputed arithmetic (step 3)

```
PROJECT/SOURCE universe (task 004)        : 1,233 blobs / 9,877,094 bytes
frozen central (task 001-003)             :   366 blobs / 4,883,398 bytes
SOURCE-BEYOND-CENTRAL (this task's scope) :   867 blobs / 4,993,696 bytes
```

Closure check: `1,233 − 366 = 867` blobs ✓, `9,877,094 − 4,883,398 = 4,993,696` bytes ✓.
Both independently recomputed from the frozen manifest (not assumed from task-004 prose)
and both close exactly to the arithmetic difference. **No blocker.**

Sanity check performed: all 366 central-commit blobs are confirmed classified
PROJECT/SOURCE in the task-004 manifest (0 of them fall under `audit_packaging_only`),
so the subtraction above is a clean, non-overlapping split.

## Chunk stream (step 4)

Same proven pattern as task 002/003: text blobs split into ≤4096-byte, UTF-8-boundary-
safe chunks (`content_utf8`); binary blobs (any classified `binary` — none of the 867
happened to be, all 6 known PDFs are central-known and therefore out of scope here)
split into exactly-4096-raw-byte slices, base64-encoded.

```
source-delta blobs               : 867
stream rows produced              : 1,669
total original bytes represented  : 4,993,696  (exact match to the 867-blob delta above)
```

## Review volumes (step 4-5)

```
volumes produced       : 94
max volume file size    : 59,995 bytes  (cap 60,000)
coverage check           : stream rows 1-1,669 covered exactly once, in order — PASSED
```

Each volume header line carries `stream_row`, `path`, `blob_sha`, `original_offset`,
`original_length`, `payload_bytes`, `chunk_index`, `chunk_count`, `classification` —
identical schema to task 003's `review_volumes/`.

## Mechanical verification (step 6)

Two independent reconstruction passes were run, both against the **JSONL stream** and
again against the **visible volume text** (not the JSONL) exactly as task 003 did:

```
reconstructed from SOURCE_DELTA_READ_STREAM.jsonl : 867 / 867 blobs, 0 mismatches
reconstructed from source_delta_review_volumes/*   : 867 / 867 blobs, 0 mismatches
```

Reconstruction check = concatenate a blob's chunks in `chunk_index` order, recompute
`sha1("blob " + len + "\0" + bytes)` independently in Python, compare to the blob's own
SHA and to its manifest byte size. **Zero mismatches in either pass.**

## Outputs

- `SOURCE_DELTA_READ_STREAM.jsonl` — 1,669 rows, lossless chunk stream.
- `SOURCE_DELTA_REVIEW_VOLUMES_INDEX.jsonl` — 94 rows: volume_number, file, first/last
  stream row, represented/text/binary original bytes, volume_file_bytes, blob_sha.
- `source_delta_review_volumes/VOL_0001.txt` … `VOL_0094.txt`.
- `SOURCE_DELTA_ACCOUNTING.md` — this file.

## Blockers

None.

---
Geschreven door: CCI. Deterministic packaging only. No central canon or frozen source
modified. No route/A-B-C decisions made or implied. INDIA9 reads the review volumes
itself for its own semantic pass; this verification is QA/accounting only.

# FULL BYTE READ STREAM — INDEX

```
task_id: INDIA9-FULL-BYTE-READ-STREAM-002
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: mechanical packaging only -- no research, no route/A-B-C/canon changes.
frozen_source_commit: 1e9fd2453e6b4cbc1488f6d275351772f3eba928
frozen_tree: e5832b6cfdbd485e7a7b20a1850f3b8f381b2ecb (matches
             INDIA9-FULL-BYTE-AUDIT-ACCOUNTING-001's independently verified tree)
stream_file: runs/active/INDIA9-FULL-BYTE-AUDIT-ACCOUNTING-001/FULL_BYTE_READ_STREAM.jsonl
```

**Reading this stream is NOT a substitute for INDIA9's own semantic read of the frozen source.**
This file only packages the exact original bytes losslessly; it carries no interpretation.

## Totals

```
total rows:                        1,383
total original bytes represented:  4,883,398   (exactly matches total_unique_blob_bytes in
                                                  FULL_BYTE_AUDIT_ACCOUNTING.md)
unique blobs covered:              366   (all of them -- matches unique_blobs in the accounting)
zero-byte blob rows:               1     (all 3 .gitkeep paths listed on that one row)
binary (base64) rows:              65    (the 6 PDF blobs, chunked)
text (utf8) rows:                  1,317
blobs represented by exactly 1 row: 176
largest blob's row count:          217   (the biggest text file, chunked at <=4096 bytes/row)
max chunk size:                    4096 original bytes (text chunks may be slightly SMALLER than
                                    4096 where the cut was moved backward to stay on a valid UTF-8
                                    character boundary -- see "Chunking rule" below; binary/base64
                                    chunks are always exactly 4096 raw bytes except the final chunk
                                    of a blob)
```

## Chunking rule (read this before parsing rows)

- **Binary blobs** (`classification: "binary"`, the 6 PDFs): split into consecutive slices of
  exactly 4096 raw bytes (final slice shorter). Each slice is stored as `content_base64`
  (standard base64 of the raw slice bytes, no line wraps).
- **Text blobs**: split into consecutive slices of **at most** 4096 raw bytes each. Where a
  4096-byte cut would fall in the middle of a multi-byte UTF-8 character, the cut is moved
  backward (never forward) to the nearest complete character boundary, so every row's
  `content_utf8` is independently valid, decodable UTF-8 with **zero normalization** (no newline
  conversion, no trimming, no NFC/NFKC). This means text chunk sizes are deterministic but not
  always exactly 4096 -- reconstruction does not depend on a fixed chunk size, only on
  concatenating chunks **in `chunk_index` order** per `blob_sha`.
- **Zero-byte blob**: one single row, `original_length: 0`, `chunk_index: 0`, `chunk_count: 1`,
  `content_utf8: ""`, with `paths` listing all three referencing paths
  (`india5/tasks/active/.gitkeep`, `india5/tasks/done/.gitkeep`, `india5/tasks/failed/.gitkeep`).
- **Reconstruction**: for a given `blob_sha`, take every row with that `blob_sha`, sort by
  `chunk_index`, and concatenate `content_utf8.encode("utf-8")` (text) or
  `base64.b64decode(content_base64)` (binary) in order. The result is byte-identical to the
  original git blob.

## Row schema

```
paths            : list[str]   -- every tracked path in the frozen tree that points at this blob
                                   (almost always 1 path; exactly one row-group has 3)
blob_sha          : str         -- git blob SHA-1 (40 hex chars)
original_offset   : int         -- byte offset of this chunk within the original blob
original_length   : int         -- byte length of this chunk (<=4096)
final_blob_size   : int         -- total byte size of the complete original blob
chunk_index       : int         -- 0-based position of this chunk within the blob
chunk_count       : int         -- total number of chunks for this blob
classification    : "text"|"binary"
content_utf8       : str         -- present only when classification == "text"
content_base64     : str         -- present only when classification == "binary"
```

## Verification performed before commit — PASSED, 366/366

Every one of the 366 unique blobs was mechanically reconstructed from this exact JSONL stream
(concatenating its chunks in `chunk_index` order) and checked against two independent criteria:

1. **Byte size** matches `final_blob_size` / the corresponding entry in
   `FULL_BYTE_AUDIT_MANIFEST.jsonl`.
2. **Git blob SHA-1 identity**: `sha1("blob " + str(len(reconstructed)) + "\0" + reconstructed)`
   (git's own blob-hashing algorithm, computed independently in Python, not shelled out to `git
   hash-object`) recomputed to exactly the blob's own SHA.

```
verified: 366 / 366
mismatches: 0
```

No blob failed reconstruction. The stream is lossless for all 366 unique blobs / all 368 tracked
paths in the frozen commit.

## Suggested fetch ranges for INDIA9 (~8 rows per fetch)

1,383 rows / 8 rows-per-fetch = **173 fetches**, the last one holding 7 rows (1-indexed row
numbers, inclusive, matching plain `sed -n '<start>,<end>p'` or an equivalent line-range read of
`FULL_BYTE_READ_STREAM.jsonl`):

```
fetch  1: rows    1-8
fetch  2: rows    9-16
fetch  3: rows   17-24
  ... (pattern: fetch N covers rows [(N-1)*8+1, N*8], each 8 rows) ...
fetch 172: rows 1369-1376
fetch 173: rows 1377-1383   (7 rows, final partial fetch)
```

Formula for any fetch `N` (1-indexed): `start = (N-1)*8 + 1`, `end = min(N*8, 1383)`.

**Important**: a chunk boundary and a fetch-range boundary are independent -- an 8-row fetch will
frequently end mid-blob (a blob needing more than 8 chunks, e.g. the 217-chunk largest file, spans
many fetches). This is expected and safe: reconstruction only requires collecting *all* rows for
a given `blob_sha` before concatenating, regardless of which fetch(es) they arrived in.

## Byte-weighted read-percentage formula (unchanged from the accounting file, restated for convenience)

```
byte_weighted_unique_pct = ( SUM(original_length for every row INDIA9 has actually read)
                              / 4,883,398 ) * 100
```

Because each row's `original_length` already deduplicates by blob (the stream has exactly one
row-set per unique blob, not per path), summing `original_length` across all rows INDIA9 has
consumed directly gives unique-content-weighted progress without any further adjustment for the
368-vs-366 path/blob difference.

---
Geschreven door: CCI. Mechanical packaging only. No central canon or frozen source modified. No
route/A-B-C decisions made or implied.

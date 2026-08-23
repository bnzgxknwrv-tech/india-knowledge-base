# INDIA9 FULL REPOSITORY BYTE AUDIT — 2026-08-23

Status: IN_PROGRESS
Owner: INDIA9
Audit branch: `agent/india9-full-byte-audit`
Frozen source branch: `agent/india8-cluster-casting`
Frozen source commit: `1e9fd2453e6b4cbc1488f6d275351772f3eba928`
Frozen source tree: `e5832b6cfdbd485e7a7b20a1850f3b8f381b2ecb`
Recursive tree completeness: `truncated:false`

## PURPOSE
Mark requires an explicit 100% read before INDIA9 resumes substantive trip planning. This audit therefore does not certify semantic readiness until every byte in scope has been accounted for.

## STRICT SCOPE
1. Every blob in the frozen central working tree, including legacy directories, scripts, schemas, temporary files, KML/XML and binary/PDF artifacts.
2. Blob identity is by Git SHA. If multiple paths reference the same blob SHA, one complete read verifies the exact bytes for every such path.
3. Zero-byte blobs count as verified when their SHA/size is present in the complete frozen tree.
4. Text/source-format blobs must be fetched completely from the frozen commit. Large text may be read in contiguous chunks, but coverage must span the full file.
5. Binary blobs must be retrieved completely or otherwise byte-verified from the exact blob object; filenames/metadata alone do not count.
6. After central-tree closure, active and boot/handoff-mentioned worker/legacy branches are compared against the frozen central snapshot. Every divergent blob that can carry provenance, decisions, locks, supersedes or worker output is read as an additional branch-delta scope.
7. Search snippets, tree listings, summaries and prior-memory familiarity do not count as full-byte reads unless the exact blob was fully fetched.

## CERTIFICATION RULE
`100%` may be declared only when:
- central snapshot audited bytes = central snapshot total bytes;
- every unique central blob is verified;
- all required branch deltas are reconciled and their divergent blobs verified;
- no fetch is truncated or silently skipped;
- decision/lock/supersede precedence has been rechecked after the byte pass.

## CURRENT CERTIFIED STATE
- Frozen snapshot established: YES
- Complete recursive tree established: YES
- Central unique-blob full-byte pass: IN_PROGRESS
- Binary/PDF full-byte pass: IN_PROGRESS
- Worker/legacy branch-delta pass: NOT YET CERTIFIED
- Semantic whole-structure certification: NOT YET CERTIFIED
- Overall certification: **NOT 100%**

## ALREADY FULLY READ AGAINST CURRENT SNAPSHOT DURING THIS AUDIT
- `governance/CCI_COLOR_TASK_ROUTING_2026-08-20.md` — blob `d126530fe51943f5846e39d9a7c3da3af4b69c6f`, 2067 bytes.
- `governance/INDIA_REGIE_DOORGANGSPROTOCOL_2026-08-20.md` — blob `d052c6fd64525f876499b4c05201c1983fca2c4e`, 6383 bytes.

## NOTE
The audit branch may receive checkpoint commits. Those checkpoint files are audit metadata and are not added to the frozen-source denominator. The denominator remains the immutable source commit above.

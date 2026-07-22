# INDIA3 LESSON — LARGE BRONS OUTPUT CHECKPOINT FAILURE

Date: 2026-07-22
Run: VARANASI-GEO-DELIVERY-REPAIR-001
Failure class: ROLE_OUTPUT_NOT_DURABLY_CHECKPOINTED

## What happened
BRONS completed the substantive local construction and validation of 40 GEO audit records, but attempted to defer durable GitHub persistence until the end. The 42,014-byte GEO_AUDIT.jsonl could not be written within the remaining tool execution. No required BRONS output was committed. An unused blob was reportedly created but its SHA was not included in the role report.

## What was correct
- BRONS did not falsely report completion.
- BRONS did not truncate or silently commit an incomplete audit.
- VNS-CAND-008 remained NOT_ESTABLISHED and the Mark-rejected coordinate was not reused.
- Forbidden paths and successor state were not changed.

## What must improve
1. Large role outputs must be durably checkpointed during execution, not only after all research is finished.
2. Source registry and audit records should be written in bounded, validated batches or as complete checkpoint files at defined milestones.
3. Before the final research block, the worker must reserve enough tool capacity for writes, readback and completion validation.
4. Every created but uncommitted blob must be reported with its exact blob SHA and intended target path.
5. A recovery prompt must distinguish between:
   - SAME_CHAT_RECOVERY, where local prepared content is still available;
   - CLEAN_CHAT_RECOVERY, which may use only committed files or a reported retrievable blob SHA.
6. A clean chat may never claim it can write unseen local content from a previous chat.
7. For runs with dozens of records, recommended checkpoints are after candidate groups 1-10, 11-20, 21-30 and 31-40, followed by a final consolidated file and readback.
8. Completion remains blocked until all required artifacts are attached to repository history and read back.

## Current recovery rule
Use the original BRONS chat first. Instruct it to write the already prepared complete SOURCES.jsonl, GEO_AUDIT.jsonl and HANDOFF.md immediately, before any additional research. If local content has been lost, retrieve the unused blob only when its exact SHA is available. Otherwise BRONS must reconstruct from evidence; it may not pretend the local package survived.

## Future protocol change
At the next safe controller maintenance point, incorporate these rules into the BRONS role, GitHub write protocol, quality gate and long-running execution guidance. Do not mutate the currently pinned worker contract during an active role without repinning the context.

END_OF_ARTIFACT

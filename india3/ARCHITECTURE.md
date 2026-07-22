# INDIA3 ARCHITECTURE

## Control plane
`pipeline/ENTRYPOINT.md`, `pipeline/ACTIVE_SYSTEM.yaml` and `pipeline/NEXT_ACTION.yaml` select exactly one executable action. The controller owns run creation, state, events, claims, context manifests, transitions and recovery. It performs no substantive place research.

## Research plane
BRONS discovers within a bounded physical scope and records evidence, indications, hypotheses and uncertainty. ZILVER independently verifies material BRONS claims, source IDs, physical identity, visitability and GEO at the level supported by available tools. GOUD integrates validated information, protects Mark decisions and produces both technical audit artifacts and the required practical delivery.

## Data plane
Each run has immutable `run.yaml`, mutable `state.yaml`, append-only `events.jsonl`, role-isolated output directories and one executable context manifest at a time. Source and claim registers are authoritative references; prose does not duplicate full evidence bodies.

## Decision plane
`decisions/MARK_DECISIONS.jsonl` is append-only. A later decision supersedes an earlier decision by ID; workers never edit earlier records or infer choices from absence.

## Delivery plane
`USER_DELIVERY_MANIFEST.yaml` declares required and produced formats, candidate counts, preserved choices, open decisions, uncertainty and validation. GOUD cannot PASS when a required user product is missing.

## Recovery plane
Every active run and migration records last valid commit, current state, completed checks, open step, required files and exact resume prompt. A clean chat resumes from the first incomplete validated step.

END_OF_ARTIFACT

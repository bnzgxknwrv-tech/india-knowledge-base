# RUN PROTOCOL

Every run contains immutable `run.yaml`, mutable `state.yaml`, append-only `events.jsonl`, one role output directory per phase and one executable context manifest at a time.

State sequence:
`READY_FOR_BRONS -> BRONS_ACTIVE -> BRONS_COMPLETE -> READY_FOR_ZILVER -> ZILVER_ACTIVE -> ZILVER_COMPLETE -> READY_FOR_GOUD -> GOUD_ACTIVE -> GOUD_PASS|GOUD_PARTIAL|GOUD_BLOCKED -> ARCHIVED`.

A transition is valid only when predecessor artifacts, source IDs, state, events, claim closure and manifest agree. Workers write only their own outputs plus authorized state/event closure. Controllers write only transition-owned files.

Each phase performs preflight, claim, execution, validation, completion write, atomic commit and readback. No future context manifest is created before predecessor validation.

END_OF_ARTIFACT

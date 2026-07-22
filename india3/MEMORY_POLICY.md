# MEMORY POLICY

Durable memory belongs in GitHub only when it affects future execution: Mark decisions, explicit rejections, protocol versions, run state, source/claim evidence, validated artifacts and lessons with concrete tests.

Do not store transient chat narration, repeated prompt text, unsupported assumptions or duplicated source bodies as permanent memory.

Mark decisions are append-only in `decisions/MARK_DECISIONS.jsonl`. Corrections use `supersedes`; no earlier line is edited or deleted. Explicitly rejected coordinates, candidates or interpretations remain active constraints until a later Mark decision supersedes them.

END_OF_ARTIFACT

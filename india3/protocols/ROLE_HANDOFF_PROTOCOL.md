# ROLE HANDOFF PROTOCOL

A worker handoff identifies run ID, completed role, result, completion commit, output manifest, required predecessor files, open blockers and next expected transition. It does not rely on pasted chat reports.

The controller validates the predecessor and prepares the successor through two phases.

## PREPARING
- keep the worker route non-executable;
- write or repair all controller-owned run files;
- write the exhaustive successor context manifest;
- read back every required file and compare current Git blob SHAs;
- simulate the first preflight of a clean successor chat.

## READY activation
Only after PREPARING passes, write `pipeline/NEXT_ACTION.yaml` as the final activation write with the exact role, run ID, expected state, context path and current context-manifest blob SHA. A successor starts only when state, events, claims, required artifacts, context hashes and NEXT_ACTION agree.

Do not assume multiple GitHub Contents API file writes form one atomic commit. Intermediate commits are non-executable preparation. The last NEXT_ACTION write is the activation commit.

Workers do not repair controller state, manifests or successor routing. They stop on infrastructure mismatch and refer the run back to CONTROLLER. Candidate-specific substantive uncertainty is isolated and does not block unrelated candidates.

END_OF_ARTIFACT
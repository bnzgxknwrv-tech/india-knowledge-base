# ROLE HANDOFF PROTOCOL

A worker handoff contains no pasted report. It identifies run ID, completed role, result, completion commit, output manifest, required predecessor files, open blockers and next expected transition.

The controller validates the predecessor and creates the successor context. A successor starts only when state, events, claims, source IDs, required artifacts and NEXT_ACTION agree.

Inline continuation is permitted only after the worker role is closed and a separate controller claim is opened. One activation may therefore complete a role and its authorized transition without asking Mark for another pasted handoff.

END_OF_ARTIFACT

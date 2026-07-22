# GITHUB WRITE PROTOCOL

Before writing, fetch current HEAD and current blob SHAs for every path to be changed. Never update the same path concurrently.

## GitHub Contents API model
A normal create/update-file operation produces one commit per file. Do not describe several such writes as one atomic multi-file commit. Atomic tree/commit operations may be used only when that capability is actually available and tested for the current transition.

## Two-phase transition
1. PREPARING: write protocol fixes, run inputs, state records and the final context manifest. Intermediate commits must not expose a READY worker route.
2. VALIDATE: read back every prepared file; compare exact Git blob SHAs; reject placeholders, missing files, stale hashes, wrong paths and state/claim conflicts.
3. ACTIVATE: write `pipeline/NEXT_ACTION.yaml` last. This one write is the activation commit.
4. READBACK: verify NEXT_ACTION fields, context-manifest path and manifest blob SHA, every required-file blob SHA and worker-preflight executability.

A file must never predict its own future commit SHA. Commit SHAs, file blob SHAs, manifest blob SHAs and activation commits are distinct values and may not be substituted for one another.

A SHA conflict triggers one fresh read and safe reconstruction attempt. If input meaning changed or the conflict persists, keep the route non-executable, write recovery status where safely possible and stop.

END_OF_ARTIFACT
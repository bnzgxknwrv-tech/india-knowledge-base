# QUALITY GATE PROTOCOL

A worker phase gate checks:
- expected state and claim closure;
- all required artifacts and sentinels;
- source-ID and claim referential integrity;
- role-scope compliance;
- capability classification;
- decision protection;
- qualified validation wording;
- candidate counts and stable IDs;
- residual uncertainty;
- readback after commit.

GOUD additionally checks every required user product and its delivery manifest. Technical completeness without practical delivery is `BLOCKED`.

## Controller activation gate
Before a worker route becomes READY, the controller must establish:
- zero placeholders or null required-file hashes;
- every required path exists and is readable;
- every pinned value is the current Git blob SHA for that file;
- no mutable activation file is hash-pinned by the worker context;
- the final context manifest has been read back and its blob SHA is known;
- state, claims, run ID, expected state and route agree;
- no conflicting active claim exists;
- a clean worker preflight can locate and validate every required document;
- NEXT_ACTION is written only after all prior checks pass;
- post-activation readback confirms the manifest path and `context_manifest_sha` exactly.

Infrastructure context or hash defects block the full role before substantive work. Candidate-specific substantive uncertainty is isolated after valid activation.

Critical failures receive one targeted controller repair attempt. A persistent critical failure keeps the route non-executable, writes recovery status where safely possible and stops.

END_OF_ARTIFACT
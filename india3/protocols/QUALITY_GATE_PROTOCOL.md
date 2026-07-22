# QUALITY GATE PROTOCOL

A phase gate checks:
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

Critical failures receive one targeted repair attempt. A persistent critical failure writes recovery status and stops activation or transition.

END_OF_ARTIFACT

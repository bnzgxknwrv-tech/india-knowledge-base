task_id: INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001
state: READY_STAGE_Z1_Z4__NOT_BLOCKED
branch: agent/indiazilver-cluster-completeness-audit
next: read CENTRAL_INPUT_MANIFEST.md and execute staged TASK.md fully with all currently available inputs
blockers: none for current staged pass; later parallel entity feeds are additive dependencies, not a stop condition
notes: existing partial outputs PROTECTED_CANON_BASELINE.csv and NEW_ID_REQUIRED_QUEUE.csv must be preserved and improved, not discarded

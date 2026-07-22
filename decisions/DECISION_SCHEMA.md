# DECISION SCHEMA

Append-only JSONL fields:
- `decision_id`: unique stable identifier;
- `run_id`: related run or `GLOBAL`;
- `candidate_id_or_subject`: exact target;
- `decision`: explicit value or rule;
- `decided_at`: ISO timestamp/date;
- `decision_source`: issue, chat statement or canonical decision path;
- `validity`: `ACTIVE`, `SUPERSEDED`, `WITHDRAWN`;
- `supersedes`: prior decision IDs;
- `note`: scope or interpretation constraints.

Only explicit Mark decisions enter this register. Earlier lines are immutable.

END_OF_ARTIFACT

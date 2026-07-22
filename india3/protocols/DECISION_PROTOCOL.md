# DECISION PROTOCOL

`decisions/MARK_DECISIONS.jsonl` is append-only. Each record contains decision_id, run_id, candidate_id_or_subject, decision, decided_at, decision_source, validity, supersedes and note.

Only an explicit Mark statement or a pre-existing canonical Mark decision may create `USER_DECISION`. Workers may propose but must label proposals `ASSISTANT_PROPOSAL`. Absence of a choice means `DOOR_MARK_TE_BEOORDELEN`, never B or C.

A later correction appends a new record with `supersedes`; previous records remain unchanged. Active decisions and explicit rejections are loaded before GOUD integration and before GEO work.

END_OF_ARTIFACT

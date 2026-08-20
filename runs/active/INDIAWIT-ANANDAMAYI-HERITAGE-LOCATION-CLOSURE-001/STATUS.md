task_id: INDIAWIT-ANANDAMAYI-HERITAGE-LOCATION-CLOSURE-001
state: COMPLETE_WITH_GOVERNANCE_SCHEMA_BLOCKER
branch: agent/indiawit-master-travel-readiness
completed_at: 2026-08-20

outputs:
- ANANDAMAYI_SOURCE_RECORDS.jsonl — cf5974bf69053e466e94a93433cd8282adbde7ba
- ANANDAMAYI_ENTITY_CANDIDATES.jsonl — 1fd1ec3213466e3c440ea5143e0c6d6f91c2d971
- ANANDAMAYI_R4_R5_CLOSURE.md — e1d8f8422501fb9a579e7269dd8e81caf561587e
- HERITAGE_STAY_ENTITY_MATRIX.md — 61d96b016786d9208c964661cdaa92f72f1e9621
- CURRENT_ACCESS_BOOKABILITY.md — c6933d04b1a93e50015bf5ecdec7b34d0cb7c187

completed:
- external union L001-L156 retained losslessly by source ID
- source-first additions and CCI084 kept as separate traceable detector layers
- Anandamayi host houses, dharamshalas, ashrams, palaces, guesthouses and room-level leads physically reconciled as far as supported
- current access/bookability checked for relevant heritage entities
- cross-person heritage stays reconciled without changing hotel locks
- no historic numeric room number invented
- east/south data retained

key_findings:
- Bhadaini Varanasi Ashram currently has official room-booking and local dharamshala contacts; no historic Ma room identified
- Kankhal Matri Smriti Museum bungalow preserves Ma's bedroom and kitchen from her final approximately two-month stay; historic bedroom is not lodging
- Kankhal International Centre offers current retreat accommodation beside the historic ashram/samadhi
- Hotel Evelyn historic Ram Dass top-floor room remains unmapped to a current room number
- Taj Mahal Palace is currently bookable; Yogananda's 1935 suite identity remains unresolved
- Sri Ramanasramam modern devotee accommodation is available; historic Nirvana Room/caves are not bookable
- Belur Math pilgrimage guest accommodation is current; Vivekananda's historic room is not bookable
- YSS Ranchi lodging remains closed until early 2027 and needs exact-date recheck
- Karar overnight policy remains unresolved; Anandamayi Karar stay was not upgraded because CCI084 left it open

constraints:
- no A/B/C changes
- no existing lock changes
- no hotel booking
- no PDF
- no merge/PR

blocker:
- required governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md is absent on this branch and repository search did not find it. R1-R5 semantics were therefore not invented; entity records use UNASSIGNED_GOVERNANCE_SCHEMA_MISSING. Physical identity/access/bookability closure is otherwise complete.

next:
- restore the missing R1-R5 governance file on this branch and map already-closed entity states mechanically without repeating research

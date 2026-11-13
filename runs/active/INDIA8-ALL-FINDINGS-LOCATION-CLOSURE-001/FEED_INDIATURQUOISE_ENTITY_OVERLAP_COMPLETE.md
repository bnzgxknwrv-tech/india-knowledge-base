# FEED — INDIATURQUOISE ENTITY / OVERLAP RECONCILIATION

Date: 2026-08-20
Source branch: `agent/indiaturquoise-allperson-overlap`
Task: `INDIATURQUOISE-ENTITY-OVERLAP-RECONCILIATION-001`
State: COMPLETE

## SOURCE OUTPUT COMMITS
- ENTITY_MERGE_MAP.jsonl — `f5e156f3e23850cc5f52f71bf26ff3a2346b6900`
- SAME_SITE_OVERLAP_MATRIX.md — `4cd8396f6acf19b70564a34a833bed5ab020624a`
- PARENT_CHILD_SITE_MAP.md — `fedf7432d8458f4efa47b41bc93007e77229f2c2`
- SUCCESSOR_SITE_MAP.md — `9759e86dadf8f1fc28047549bdcc304420ecd514`
- AMBIGUOUS_MERGES_QUEUE.md — `473d90a6cda65a182b58180daf9290c8432d134a`
- STATUS COMPLETE — `0aef428540474bcee26122f3913c26ced6aad10f`

## IMPORTANT ENTITY RULES NOW DURABLE
- Kainchi Dham, NKB Vrindavan, 4 Church Lane and Karar Ashram are parent complexes. Rooms, verandas, cremation spots, memorials and other physically distinct micro-sites must NOT be silently deduplicated into the parent.
- Lahiri residence Varanasi, Sri Ramanasramam, Dakshineswar and Ranchi/YSS are true physical cross-person overlaps.
- Kumbh remains event-zone/landscape, not an invented exact building.
- Historic->modern successor relationships remain explicit: Ghurni original Lahiri site -> later shrine; Akbarpur birth/family site -> 2001 temple; historic Ranchi Vidyalaya -> current YSS campus; historic Dunagiri initiation-landscape claim -> modern institutional Babaji Cave identification.
- Ambiguous merges remain unmerged until separately resolved.

## CENTRAL ACTION
Use ENTITY_MERGE_MAP as the dedup/crosswalk layer for ALL_FINDINGS_LOCATION_MASTER. Preserve parent-child micro-sites separately. Use SUCCESSOR_SITE_MAP for R2 classification rather than claiming fabric continuity. Feed SAME_SITE_OVERLAP + parent-child/successor data to ZILVER for proximity/new-ID staging. Do not wait for other colors.

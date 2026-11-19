# TURQUOISE ENTITY FEED — REQUIRED INPUT FOR ZILVER

Source branch: `agent/indiaturquoise-allperson-overlap`
Source task: `INDIATURQUOISE-ENTITY-OVERLAP-RECONCILIATION-001`
State: COMPLETE

Use these exact outputs as additional allowed read inputs:
- `runs/active/INDIATURQUOISE-ENTITY-OVERLAP-RECONCILIATION-001/ENTITY_MERGE_MAP.jsonl` @ `f5e156f3e23850cc5f52f71bf26ff3a2346b6900`
- `SAME_SITE_OVERLAP_MATRIX.md` @ `4cd8396f6acf19b70564a34a833bed5ab020624a`
- `PARENT_CHILD_SITE_MAP.md` @ `fedf7432d8458f4efa47b41bc93007e77229f2c2`
- `SUCCESSOR_SITE_MAP.md` @ `9759e86dadf8f1fc28047549bdcc304420ecd514`
- `AMBIGUOUS_MERGES_QUEUE.md` @ `473d90a6cda65a182b58180daf9290c8432d134a`

Rules for ZILVER:
1. Parent-child micro-sites are not duplicates merely because they share a complex.
2. True same-site overlaps should enrich person/event links, not create duplicate IDs.
3. Historic-modern successor relations are not fabric identity; treat as successor/R2 where appropriate.
4. Ambiguous merges must remain unresolved and must not be forced.
5. Kumbh/event-zone records are not exact building coordinates.
6. Use this feed immediately in proximity/new-ID/ABC-review staging; do not wait for other colors.

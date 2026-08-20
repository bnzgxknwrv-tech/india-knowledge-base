task_id: INDIAROOD-CORE-KRIYA-LOCATION-CLOSURE-001
state: COMPLETE
branch: agent/indiarood-core-kriya-sweep
blockers: none

outputs:
  - CORE_KRIYA_SOURCE_RECORDS.jsonl @ e45dd559b7e442d47f2f94cfc548137d1f4ffd58
  - CORE_KRIYA_ENTITY_CANDIDATES.jsonl @ 96d1a58eb4e5a34f6048c757bf7ed7149a68233d
  - CORE_KRIYA_R4_R5_CLOSURE.md @ cd817119ffdb6ec1af0293e8842f9cb3d6bde893
  - CORE_KRIYA_ACCESS_MATRIX.md @ 844bdc276aafb2553b9c97584f14596f3f85d672

accounting:
  source_records_total: 178
  claim_records: 146
  negatives: 32
  entity_candidates_total: 204
  required_micro_site_or_successor_splits: 58
  r1: 31
  r2: 2
  r3: 34
  r4: 54
  r5: 25
  resolved_or_strong_localized: 67
  unresolved_explicit: 79
  silent_drops: 0

hard_preservation:
  existing_ids_changed: false
  abc_changed: false
  babaji_claimant_traditions_collapsed: false

next: feed all four outputs into INDIA8 ALL_FINDINGS_LOCATION_MASTER and ZILVER additive proximity/new-ID staging; no rediscovery rerun required unless central reconciliation exposes a true evidence gap

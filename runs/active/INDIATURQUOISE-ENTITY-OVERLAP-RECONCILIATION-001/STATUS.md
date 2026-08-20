task_id: INDIATURQUOISE-ENTITY-OVERLAP-RECONCILIATION-001
state: COMPLETE
branch: agent/indiaturquoise-allperson-overlap
completed_outputs:
  - ENTITY_MERGE_MAP.jsonl
  - SAME_SITE_OVERLAP_MATRIX.md
  - PARENT_CHILD_SITE_MAP.md
  - SUCCESSOR_SITE_MAP.md
  - AMBIGUOUS_MERGES_QUEUE.md
method: existing durable repo layers only; no new person-location research
preservation: all referenced source-record IDs, persons, events, aliases, uncertainties and claimant-tradition distinctions retained
hard_same_site_rule: physical identity evidence required; never city-name-only
micro_site_rule: same complex => parent-child where physically distinct, not duplicate
successor_rule: historic-to-modern successor relation retained without silently equating structures
special_priorities_processed: Varanasi; Kumaon; Bodh Gaya/Gaya; Tiruvannamalai/Arunachala; Vrindavan/Braj; Prayagraj/Allahabad; Delhi; heritage-stay guardrail; East-data entities
input_gap: governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md not found at requested path or by repository search; TASK.md equivalent hard rules applied and gap recorded in AMBIGUOUS_MERGES_QUEUE.md
abc_changed: false
existing_ids_changed: false
route_changed: false
blockers: none for task completion
next: INDIA/Mark may consume entity map downstream; ambiguous rows remain unmerged until separately resolved

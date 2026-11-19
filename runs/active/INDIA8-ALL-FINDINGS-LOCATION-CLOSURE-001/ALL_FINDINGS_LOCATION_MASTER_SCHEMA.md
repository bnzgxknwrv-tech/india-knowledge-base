# ALL_FINDINGS LOCATION MASTER — CONSOLIDATION SCHEMA

State: ACTIVE_PREP_WHILE_ROOD_ZILVER_RUN
Date: 2026-08-20

## PURPOSE
Provide the final lossless consolidation target before Mark A/B/C. This structure is prepared NOW so completed feeds can be ingested immediately; do not wait until ROOD/ZILVER finish to design it.

## ONE SOURCE CLAIM = ONE TRACEABLE MASTER ROW
Required columns/fields:
- master_row_id
- source_family
- source_branch
- source_task
- source_record_id
- person_or_layer
- raw_place_name
- normalized_claim_name
- event_scene_summary
- AOAY_chapter_scene_if_any
- evidence_status
- claimant_tradition_if_any
- physical_entity_key
- physical_entity_name
- parent_entity_key
- child_micro_site_type
- duplicate_of_entity_key
- successor_of_entity_key
- merge_status
- R_class
- access_status
- current_address_or_locator
- latitude
- longitude
- coordinate_confidence
- existing_permanent_id
- existing_mark_ABC
- existing_lock
- new_id_required
- proximity_1km_links
- proximity_3km_links
- overlap_person_count
- heritage_stay_flag
- current_bookability
- unresolved_reason
- next_search_route
- route_region_family
- current_route_priority_state
- source_commit_sha
- notes

## ACCOUNTING RULE
No silent drops.

`TOTAL_SOURCE_ROWS = PHYSICAL_ENTITY_LINKED + EXPLICIT_DUPLICATE + NEGATIVE/NONPRESENCE + STILL_UNRESOLVED`

Parent-child is NOT duplicate. Successor is NOT historical fabric identity. Event-zone is NOT exact building. R4/R5 remain rows.

## INGEST ORDER
1. BLAUW AOAY/Yogananda — COMPLETE
2. TURQUOISE merge/parent-child/successor — COMPLETE relation layer
3. GEEL four-person — COMPLETE
4. WIT Anandamayi/heritage — COMPLETE
5. ROOD Core Kriya — ACTIVE, ingest immediately on completion
6. ZILVER proximity/canon/new-ID staging — ACTIVE, enrich existing rows; never replace source rows
7. Existing permanent canon + prior cluster A/B/C/locks — protective enrichment layer
8. Non-person anchors — protective enrichment layer

## MARK-READY GATE
A cluster may be presented for a new Mark A/B/C pass only when:
- all source rows relevant to that cluster are ingested;
- all entity links/duplicates/parent-child/successors are traceable;
- R4/R5 are visible and targeted research has been exhausted to appropriate claim-weight;
- access status exists where reasonably knowable;
- old canon IDs/A/B/C/locks are attached;
- new physical entities are explicitly NEW_ID_REQUIRED;
- proximity/overlap is attached where reliable.

Then publish FULL cluster list, not a filtered shortlist.

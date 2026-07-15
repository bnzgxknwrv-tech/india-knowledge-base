# LOCATION_ID audit — BRAJ-COMPLETE-001

## Assignment

- Reserved cluster block: `200–299`.
- Assigned IDs: every decimal value from `200` through `228` inclusive.
- Assigned count: 29.
- Candidate count: 29.
- Duplicate LOCATION_IDs: none.
- Duplicate candidate assignments: none.
- Out-of-block IDs: none.
- Overlap with Delhi block `100–199`: none.
- Unused Braj values after this run: `229–299`.
- Gaps inside assigned sequence: none; gaps remain allowed for later discoveries.

## Mapping integrity

`200–207` map to the eight existing canonical `IND-PLACE-*` records in their preserved order. `208–228` map to the 21 temporary Braj candidates in their preserved order. No existing formal status was changed. The two existing A records remain only preserved metadata and were not reassessed.

## C retention

No candidate was removed from `place_candidates.jsonl`, `geo_locations.jsonl`, `decision_inputs.md` or the final report because it may later receive C. All 29 locations remain present regardless of future advisory or formal status.

## GEO integrity

Every candidate has exactly one GEO record and one permanent LOCATION_ID. No record contains a guessed coordinate. All latitude and longitude fields remain null because no independently verified visitor entrance or exact site point exists in the pinned context. LOCATION_ID `221` is additionally marked `CONFLICTED` because the Gokul physical identity remains unresolved.

Google Maps search URLs are locator leads only and are not classified as verified points. No KML was generated. No connection contains a guessed travel time or distance.

Audit result: LOCATION_ID assignment PASS; WGS84 verification PARTIAL/NOT_ESTABLISHED for all 29 records.

END_OF_ARTIFACT
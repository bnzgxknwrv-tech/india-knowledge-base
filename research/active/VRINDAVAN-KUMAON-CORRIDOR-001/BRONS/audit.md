# BRONS audit — VRINDAVAN-KUMAON-CORRIDOR-001

## Technical preflight

- GitHub read and write were tested before content work; the temporary test file was created, fetched and removed.
- `pipeline/ENTRYPOINT.md`, `pipeline/NEXT_ACTION.yaml`, run, role, expected state and contextmanifest matched.
- State and eventlog were synchronized at EVT-0001 before claim; no active claim existed.
- All 46 required files were fully read. Every pinned blob SHA and every required sentinel matched.
- No forbidden file was opened or modified.
- BRONS was claimed as `ChatGPT-BRONS`; run and predecessor inputs were not mutated.

## Scope control

- The road, rail and combined corridors explicitly required by scope were compared.
- Delhi was used only as a comparison.
- Every named station/city/route zone received a separate negative heavy-A check.
- The direct-personal-line and India-Essential gates were applied without ordinary-temple inflation.
- The five-part Krishna distinction was applied.
- No PARELS, hotel selection, unrelated route stage, internal Kumaon day plan, formal/advisory A/B/C or pipeline design was performed.

## Claim and source integrity

- claim IDs `RC-001` through `RC-020` are unique;
- accepted source IDs `RS-001` through `RS-025` are unique;
- rejected source IDs `RR-001` through `RR-006` are unique;
- every `source_id` in `claims.jsonl` resolves exactly once across accepted or rejected registers;
- route and timetable claims carry `checked_at` and a recheck requirement in the transport registers;
- map/router sources are used only for route or GEO working context;
- no review, map pin or weak detector source carries an ancient or supernatural claim.

## Corridor result

- Preferred working route: direct car via Moradabad–Rampur–Rudrapur to Haldwani/Kathgodam.
- Heavy-A corridor stops passed: 0.
- Direct-line content gate outside corridor: Anandamayi Ma Samadhi in Kankhal, route gate failed because of the major detour.
- Exception retained without A/B/C assignment: Dargah-e-Ala Hazrat in Bareilly.
- Working decision: `DOORREIZEN NAAR KUMAON`.

## LOCATION_ID and GEO integrity

- Braj IDs 200–228 were preserved.
- Corridor IDs 300–315 were assigned sequentially and only within the reserved block.
- Kumaon seed IDs 400–426 were preserved.
- Duplicate, reused or cross-block IDs: none.
- All formal A/B/C records are present in `central_map_source.jsonl`.
- Records outside assigned blocks use `BLOCK_RESERVATION_REQUIRED` rather than invented permanent IDs.
- Forty assigned records have labelled WORKING points with point type, accuracy, source, motivation and date.
- No WORKING point is represented as a verified visitor entrance.

## KML integrity

- `corridor_working.kml` contains only assigned records with usable WORKING coordinates.
- Required folders exist: `A_FORMEEL`, `B_ADVIES`, `C_CONTEXT`, `CORRIDOR_EN_STATIONS`.
- Formal status and GEO status are separately described.
- Records without reserved LOCATION_ID or reliable coordinates remain in the central source and are excluded from the provisional KML.
- The KML is a working corridor map, not a definitive complete project map.

## Quality-gate result

Technical integrity: PASS.
Corridor decision usability: PASS at BRONS working level.
Overall release: PARTIAL because date-specific official train verification, live winter road calculations, independent WORKING_GEO verification, primary Kankhal institutional verification and missing cluster block reservations remain open.

END_OF_ARTIFACT
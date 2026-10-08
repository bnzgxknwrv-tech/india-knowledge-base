# CCI TASK — RETAINED ROUTE A/B GEO CLOSURE + SILENT-DROP QA

Repository: `bnzgxknwrv-tech/india-knowledge-base`
Regie branch to read: `agent/india8-cluster-casting`

## PURPOSE
Support INDIA8 while it builds the quarter-hour operational itinerary. Do NOT redesign the route or change Mark A/B/C.

## READ FIRST
- `README.md`
- `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`
- `governance/ABC_SEMANTIC_LABEL_RULE_2026-08-23.md`
- `handoffs/INDIA8_TO_INDIA9_FINAL_BOOT_2026-08-23.md`
- `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/WORKING_ROUTE_V2_TRAIN_FIRST_NEWYEAR_RISHIKESH_2026-08-23.md`
- all protected Mark A/B decision sources relevant to the retained route.

## RETAINED ROUTE ONLY
Delhi arrival stop; Haidakhan; Kukuchina/Dunagiri/Dwarahat; Nainital/Kainchi; Rishikesh/Haridwar/Kankhal; Agra Taj-only; Vrindavan/Braj/Mathura; Prayagraj; Varanasi/Sarnath; Bodh Gaya/Gaya; Tiruvannamalai/Arunachala.

Kasar Devi/Almora dedicated module is removed; Mysore/Bengaluru and Kolkata parked. Do not reopen them.

## TASK A — COMPLETE A/B INVENTORY QA
Independently reconstruct every CURRENT retained-route Mark A and B after precedence/supersedes.
For every A/B use semantic label: `NAME (what it is / why it matters) — A/B`.
Flag:
- silent drops from current working route;
- duplicate physical sites / micro-sites that should ride under one parent;
- older grades superseded by later Mark decisions;
- any apparent conflict.
DO NOT choose for Mark.

## TASK B — GOOGLE MAPS COORDINATE CLOSURE
For every retained A/B physical visit site and current sleep/transport base:
1. reuse an existing EXACT_GOOGLE_MAPS_MARKER / VERIFIED_OFFICIAL_MAP_LINK only when repository evidence supports it;
2. otherwise independently search for the correct current Google Maps place/marker;
3. verify identity against address/official/institutional evidence;
4. never promote an old `WORKING_GOOGLE_MAPS_PIN` merely because it looks plausible;
5. never guess a coordinate.

Output fields minimum:
`semantic_label, grade, cluster, parent_site, latitude, longitude, geo_status, google_maps_url_or_google_official_map_source, identity_evidence, visitability_note, conflict_note`

Allowed geo_status values:
- EXACT_GOOGLE_MAPS_MARKER
- VERIFIED_GOOGLE_OFFICIAL_MAP_LINK
- ADDRESS_CONFIRMED_MARKER_NOT_CLOSED
- ZONE_ONLY
- GEO_CONFLICT
- NONPUBLIC_OR_NOT_FOR_VISIT

## TASK C — OPERATIONAL QA
Flag only high-impact issues for a Dec 19 2026–Jan 20 2027 detailed schedule:
- known closing weekday;
- seasonal closure;
- public/private/access restriction;
- time-sensitive ritual/event;
- exact location not visitable despite A/B.
No restaurant sweep and no route redesign.

## OUTPUTS
Write on your own task branch:
- `RETAINED_ROUTE_AB_CANON_QA.md`
- `RETAINED_ROUTE_AB_GEO_LEDGER.csv`
- `OPERATIONAL_BLOCKERS.md`

Post `CCI_RESULT` on PR #23 with:
- commit SHA(s)
- A count, B count
- exact/verified coordinate count
- unresolved/conflict count
- silent-drop count
- top blockers

No PDF. No KML. No A/B/C changes. No route choice.
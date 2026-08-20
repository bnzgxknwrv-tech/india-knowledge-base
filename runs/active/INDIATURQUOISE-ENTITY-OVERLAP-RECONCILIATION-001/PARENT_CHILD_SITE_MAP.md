# PARENT_CHILD_SITE_MAP — INDIA TURQUOISE

status: COMPLETE
rule: same complex does not make child micro-locations duplicates

## Parent → child relations

| parent entity | child / micro-location | source-record IDs | relation | keep separate event/source links? |
|---|---|---|---|---|
| Kainchi Dham complex | nine external Kainchi sublocations | `NKB-5`; `ext-41..49` | `CHILD_MICROSITES` | JA — all nine source claims remain lossless. |
| NKB Vrindavan Ashram / Mahasamadhi complex | Maharajji room; verandah; cremation place; later memorial | `NKB-8`; `ext-104..108`; `NKB-14`; `ext-107` | `CHILD_MICROSITES_AND_LATER_MEMORIAL` | JA; later memorial is not silently converted to lifetime-presence evidence. |
| 4 Church Lane / Red House | Maharajji room | `ext-21` | `ROOM_CHILD` | JA |
| 4 Church Lane / Red House | hall | `ext-22` | `ROOM_CHILD` | JA |
| 4 Church Lane / Red House | outside veranda | `ext-23` | `MICROSITE_CHILD` | JA |
| 4 Church Lane / Red House | kitchen / meal room | `ext-24` | `ROOM_CHILD` | JA |
| 4 Church Lane / Red House | bathrooms / front area | `ext-25` | `MICROSITE_CHILD` | JA |
| Karar Ashram | first room 1949 claim | `B14` | `ROOM_CHILD + CLAIMANT_TRADITION_SEPARATE` | JA; Hariharananda-claimant Babaji must not be merged into AOAY Babaji identity. |
| Karar Ashram | Kali-puja room 1949 claim | `B15` | `ROOM_CHILD + CLAIMANT_TRADITION_SEPARATE` | JA |
| Ranchi Vidyalaya / YSS campus | garden used for Anandamayi Ma photo session | targeted Ranchi event | `UNRESOLVED_MICROSITE_CHILD` | JA; exact garden position is not inferred. |
| Dunagiri/Drongiri initiation landscape | initiation cave / cave-site corpus | `BJ-INT-01`; `B01`; `BJ-INT-14`; `B01-S1`; `ATL-MB-001` | `CHILD_SITE_WITH_HISTORIC_MODERN_IDENTITY_CAVEAT` | JA |
| Dunagiri/Drongiri initiation landscape | Gogash riverbank | `BJ-INT-01a`; `B02` | `DISTINCT_CHILD_SUBLOCATION` | JA |
| Dunagiri/Drongiri initiation landscape | temporary materialized palace claim | `BJ-INT-01b`; `B03` | `DISTINCT_CLAIMED_CHILD_SUBLOCATION` | JA; not flattened into cave. |
| Dashashwamedh Ghat zone | claimed underground cave | `BJ-INT-11+12`; `B06` | `UNRESOLVED_CHILD_MICROSITE` | JA; ghat identity known, hidden cave point not resolved. |
| Sri Ramanasramam | no child merge created in this task | `ATL-RM-006`; `ATL-PY-009` | `PARENT_COMPLEX_ONLY` | Separate Ramana/Yogananda events retained. |
| Arunachala/Tiruvannamalai cluster | Arunachaleswarar Temple | `ATL-RM-003` | `DISTINCT_SITE_IN_CLUSTER` | JA |
| Arunachala/Tiruvannamalai cluster | Virupaksha Cave | `ATL-RM-004` | `DISTINCT_SITE_IN_CLUSTER` | JA |
| Arunachala/Tiruvannamalai cluster | Mango Tree Cave | contained in `ATL-RM-004` wording | `DISTINCT_MICROSITE_ASSOCIATED_WITH_VIRUPAKSHA_PERIOD` | JA |
| Arunachala/Tiruvannamalai cluster | Skandashram | `ATL-RM-005` | `DISTINCT_SITE_IN_CLUSTER` | JA |
| Arunachala/Tiruvannamalai cluster | Sri Ramanasramam | `ATL-RM-006`; `ATL-PY-009` | `DISTINCT_SITE_IN_CLUSTER + CROSS_PERSON_PARENT_ENTITY` | JA |

## Explicit anti-collapse rules

1. A room inside an ashram remains a child finding when a source attaches a specific event to that room.
2. A cremation place and a later memorial/samadhi structure are not interchangeable.
3. A ghat, cave, riverbank and temporary/palace claim inside one broader event landscape are distinct physical concepts.
4. A metropolitan or regional cluster is never a parent entity in the duplicate-removal sense; it is only a travel/analysis container.
5. Existing A/B/C and permanent IDs are untouched.

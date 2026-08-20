# CORE KRIYA ACCESS MATRIX

Task: `INDIAROOD-CORE-KRIYA-LOCATION-CLOSURE-001`  
Checked: 2026-08-20  
Scope: all **146 claim-bearing source records** plus the physically split priority candidates in `CORE_KRIYA_ENTITY_CANDIDATES.jsonl`. Negative controls remain preserved in `CORE_KRIYA_SOURCE_RECORDS.jsonl` but are not assigned travel-access status merely for being negative controls.

## Status vocabulary

- `PUBLIC_OPEN` — public landscape/street/ghat type access without a specific institutional gate identified.
- `PUBLIC_LIMITED_HOURS` — publicly visitable institution/site with hours or operational access constraints.
- `PRIVATE_PERMISSION_POSSIBLE` — current site exists, but interior/ashram/family access should be treated as permission-dependent.
- `EXTERIOR_ONLY` — current object can be physically approached/seen, but no reliable visitor-entry basis was found.
- `LANDSCAPE_ACCESS` — physically visitable landscape/region, while exact historic metres may remain uncertain.
- `SUCCESSOR_SITE_VISITABLE` — original building/object is gone or altered, but a current successor/site can be visited.
- `ACCESS_UNKNOWN` — not enough current-access evidence yet.
- `ACCESS_UNKNOWN_AFTER_EXHAUSTION` — targeted closure research was performed and no responsible current access/site continuity could be established.

Access status describes present physical access only. It does not validate the truth of a historical, miraculous, apparition or identity claim.

## Complete claim-record access distribution

### LANDSCAPE_ACCESS — 30

`IR-1`, `IR-2`, `IR-3`, `IR-4`, `IR-7`, `IR-8`, `IR-9`, `IR-10`, `IR-22`, `IR-26`, `IR-27`, `IR-29`, `IR-33`, `IR-43`, `LM-001`, `LM-002`, `LM-017`, `LM-018`, `LM-026`, `LM-033`, `SY-008`, `SY-013`, `SY-015`, `SY-034`, `SY-037`, `SY-041`, `ext-B16`, `ext-B19`, `ext-B20`, `ext-B21`.

Notes: these include broad mountain/river/festival/ghat/park-style anchors where physically going to the zone is meaningful even when the historic micro-point cannot be proved.

### ACCESS_UNKNOWN_AFTER_EXHAUSTION — 69

`IR-5`, `IR-6`, `IR-13`, `IR-14`, `IR-15`, `IR-20`, `IR-21`, `IR-23`, `IR-24`, `IR-25`, `IR-28`, `IR-31`, `IR-38`, `IR-39`, `IR-41`, `IR-42`, `IR-44`, `IR-45`, `IR-46`, `IR-47`, `IR-50`, `LM-004`, `LM-005`, `LM-009`, `LM-010`, `LM-011`, `LM-012`, `LM-013`, `LM-014`, `LM-015`, `LM-016`, `LM-019`, `LM-020`, `LM-021`, `LM-022`, `LM-027`, `LM-029`, `LM-030`, `LM-031`, `LM-032`, `LM-035`, `LM-036`, `LM-037`, `LM-038`, `LM-039`, `LM-040`, `SY-002`, `SY-003`, `SY-006`, `SY-009`, `SY-011`, `SY-014`, `SY-016`, `SY-017`, `SY-018`, `SY-020`, `SY-021`, `SY-022`, `SY-027`, `SY-031`, `SY-038`, `SY-039`, `SY-040`, `SY-042`, `ext-B12`, `ext-B22`, `ext-B23`, `intern-18-Gorakhpur-Abinash`, `DELTA-LM-PP-ONLY-AGGREGATE`.

This group is intentionally large: private host houses, vanished interiors, unnamed work posts, hidden/mythic places and nonlocalized postmortem scenes were not force-fitted to modern sites.

### PUBLIC_LIMITED_HOURS — 25

`IR-11`, `IR-18`, `IR-19`, `IR-30`, `IR-40`, `IR-49`, `LM-003`, `LM-006`, `LM-007`, `LM-008`, `LM-023`, `LM-024`, `LM-025`, `LM-028`, `SY-004`, `SY-005`, `SY-007`, `SY-012`, `SY-026`, `SY-028`, `SY-032`, `SY-035`, `SY-036`, `ext-B17`, `ext-B11-subclaim`.

### PRIVATE_PERMISSION_POSSIBLE — 12

`IR-12`, `IR-16`, `IR-32`, `IR-34`, `IR-35`, `IR-36`, `IR-37`, `IR-48`, `SY-019`, `SY-023`, `SY-024`, `ext-B32`.

These are mostly family houses or functioning ashram/lineage properties where the physical identity is useful but entry to the relevant interior should not be assumed.

### PUBLIC_OPEN — 5

`IR-17`, `LM-034`, `SY-010`, `SY-030`, `SY-033`.

### SUCCESSOR_SITE_VISITABLE — 4

`SY-001`, `SY-025`, `SY-029`, `DELTA-SY-SERAMPORE-MICRO-AGGREGATE`.

The successor status does not automatically upgrade the historical personal-presence certainty. In particular, `SY-029` remains R5 for Sri Yukteswar's claimed Dihika visit while the current Dihika successor/site is visitable.

### EXTERIOR_ONLY — 1

`ext-B18` — Government Rest House, Dwarahat. The physical government-rest-house object is retained as a Daya Mata/Babaji-tradition context record; ordinary bodily Babaji presence is not inferred.

## Priority physical split matrix

| Candidate | R | Access | Present-state interpretation |
|---|---:|---|---|
| `DUNAGIRI-1861::CAVEFIELD` | R3 | LANDSCAPE_ACCESS | Dunagiri cave-field is visitable as a mountain zone; no single historical cave proved. |
| `DUNAGIRI-1861::UNNAMED-INITIATION-CAVE` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | exact early-text cave unclosed. |
| `DUNAGIRI-YSS::PANDUKHOLI-CAVE` | R1 | LANDSCAPE_ACCESS | current YSS claimant cave reachable by mountain approach/footpath. |
| `DUNAGIRI-GAGAS::RIVER-SYSTEM` | R3 | LANDSCAPE_ACCESS | river system visitable; historic bank metres unknown. |
| `DUNAGIRI-GOLDEN-PALACE::EPHEMERAL` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | no surviving physical object/site marker. |
| `PRAYAG-1894::HISTORIC-MELA-ZONE` | R3 | LANDSCAPE_ACCESS | visitable floodplain/mela context. |
| `PRAYAG-1894::BRIDGE` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | which bridge unclosed. |
| `PRAYAG-1894::TREE-AOAY` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | original tree identity unclosed. |
| `PRAYAG-1894::YOGI-SATYAM-BANYAN` | R1 | PUBLIC_LIMITED_HOURS | current ashram claimant tree; do not merge automatically with historic tree. |
| `DASHASHWAMEDH::GHAT` | R1 | PUBLIC_OPEN | named ghat physically accessible. |
| `DASHASHWAMEDH::MATAJI-CAVE` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | hidden cave/stone slab not publicly identified. |
| `RAI-GHAT::BANYAN` | R1 | LANDSCAPE_ACCESS | YSS current claimant banyan/site. |
| `LAHIRI-HOUSE::BUILDING` | R1 | PUBLIC_LIMITED_HOURS | current lineage-recognized D31/58 house; actual visitor access may vary. |
| `LAHIRI-HOUSE::FRONT-PARLOR` | R3 | PRIVATE_PERMISSION_POSSIBLE | same house anchor; room access/continuity permission-dependent. |
| `LAHIRI-HOUSE::THRESHOLD` | R3 | PRIVATE_PERMISSION_POSSIBLE | historical micro-point not independently room-mapped. |
| `GARPAR-4::HOUSE` | R1 | PRIVATE_PERMISSION_POSSIBLE | same Ghosh family house; commemorative access exists but not ordinary unrestricted entry. |
| `GARPAR-4::BABAJI-ROOM` | R3 | PRIVATE_PERMISSION_POSSIBLE | interior micro-site. |
| `GARPAR-4::ROOF-1930` | R1 | PRIVATE_PERMISSION_POSSIBLE | same-house roof claim; permission-dependent. |
| `KARAR::COMPLEX` | R1 | PRIVATE_PERMISSION_POSSIBLE | functioning ashram property. |
| `KARAR::SAMADHI` | R1 | PRIVATE_PERMISSION_POSSIBLE | samadhi inside functioning ashram. |
| `KARAR::HARIHARANANDA-ROOMS` | R3 | PRIVATE_PERMISSION_POSSIBLE | interior rooms retained separately. |
| `PARANGIPETTAI::MANDIR` | R1 | PUBLIC_LIMITED_HOURS | present claimant shrine. |
| `PARANGIPETTAI::CLAIMED-BIRTH-SUBSTRATE` | R3 | PUBLIC_LIMITED_HOURS | claimant parcel fixed by later shrine, historical birth unproved. |
| `SATOPANTH::LAKE-ZONE` | R3 | LANDSCAPE_ACCESS | high-altitude seasonal trek. |
| `SATOPANTH::UNNAMED-CAVE` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | exact cave not recovered. |
| `KESHAV-PRAYAG::CONFLUENCE` | R3 | LANDSCAPE_ACCESS | landscape anchor only. |
| `GAURI-SHANKARA-PITHA::HIDDEN` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | tradition presents hidden site. |
| `DUNAGIRI-HARAPRIYA::TEMPLE` | R1 | PUBLIC_LIMITED_HOURS | current temple exact; historical event is only “near” it. |
| `HAIDAKHAN::VISHWA-MAHADHAM` | R1 | PRIVATE_PERMISSION_POSSIBLE | current Samaj complex/contactable. |
| `HAIDAKHAN::HISTORIC-CAVE` | R1 | PRIVATE_PERMISSION_POSSIBLE | current lineage cave; distinct from Dunagiri. |
| `HAIDAKHAN::DHUNI` | R1 | PRIVATE_PERMISSION_POSSIBLE | ritual subsite inside complex. |
| `GHURNI::LOST-ESTATE` | R3 | LANDSCAPE_ACCESS | historic zone only after river-course change. |
| `GHURNI::Jaleshwar-SUCCESSOR` | R3 | PUBLIC_LIMITED_HOURS | successor shrine/cult-object claim; same original temple footprint unproved. |
| `VARANASI-PANCHGANGA::GHAT` | R1 | PUBLIC_OPEN | surviving named ghat. |
| `VARANASI-PANCHGANGA::TAILANG-MATH` | R1 | PUBLIC_LIMITED_HOURS | present Tailang Swami Math at ghat. |
| `RANA-MAHAL::GHAT` | R1 | LANDSCAPE_ACCESS | surviving named ghat. |
| `RANA-MAHAL::KRISHNARAM-HOUSE` | R4 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | host known, address unknown. |
| `RAMNAGAR::FORT-PALACE` | R1 | PUBLIC_LIMITED_HOURS | current royal fort/palace complex. |
| `RAMNAGAR::TUTORING-ROOM` | R3 | PUBLIC_LIMITED_HOURS | palace exact, room unknown. |
| `HARIDWAR-KESHAV::CURRENT-ASHRAM` | R3 | PRIVATE_PERMISSION_POSSIBLE | current institution; historical same-site continuity unproved. |
| `HARIDWAR-KESHAV::AOAY-HERMITAGE` | R4 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | historic hermitage still not physically closed. |
| `SERAMPORE-PRIYADHAM::HISTORIC-TERRAIN` | R2 | SUCCESSOR_SITE_VISITABLE | old ashram terrain represented by current successor site. |
| `SERAMPORE-PRIYADHAM::SMRITI-MANDIR` | R1 | PUBLIC_LIMITED_HOURS | later memorial on historic site. |
| `SERAMPORE-PRIYADHAM::COURTYARD` | R3 | SUCCESSOR_SITE_VISITABLE | historic component preserved; exact current footprint not fully mapped. |
| `SERAMPORE-PRIYADHAM::HALL` | R3 | SUCCESSOR_SITE_VISITABLE | same. |
| `SERAMPORE-PRIYADHAM::SITTING-ROOM` | R3 | SUCCESSOR_SITE_VISITABLE | same. |
| `SERAMPORE-PRIYADHAM::EATING-PATIO` | R3 | SUCCESSOR_SITE_VISITABLE | same. |
| `SERAMPORE-PRIYADHAM::BEDROOM` | R3 | SUCCESSOR_SITE_VISITABLE | same. |
| `BODH-GAYA::KRISHNADAYAL-MATH` | R4 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | monastery not named; Mahabodhi is not substituted. |
| `TULSI-BOSE::HISTORIC-HOUSE` | R3 | PRIVATE_PERMISSION_POSSIBLE | historic house/grounds cluster; room-level access not assumed. |
| `TULSI-BOSE::YSS-GARPAR-CENTRE` | R2 | PUBLIC_LIMITED_HOURS | current adjacent/successor lineage institution. |
| `PANTHI::HISTORIC-PLOT` | R2 | SUCCESSOR_SITE_VISITABLE | historic building demolished; plot localized by YSS. |
| `PANTHI::ROOM` | R2 | SUCCESSOR_SITE_VISITABLE | room gone; site/plot is strongest physical successor. |
| `DIHIKA::HISTORIC-SCHOOL-SITE` | R2 | SUCCESSOR_SITE_VISITABLE | current YSS site supplies physical successor only. |
| `DIHIKA::CURRENT-YSS-RETREAT` | R1 | PUBLIC_LIMITED_HOURS | present visitor site; does not prove Sri Yukteswar visit. |
| `ALBERT-HALL::INDIAN-COFFEE-HOUSE` | R1 | PUBLIC_LIMITED_HOURS | KMC heritage record supports building identity continuity. |
| `REGENT-1936::HISTORIC-HOTEL` | R5 | ACCESS_UNKNOWN_AFTER_EXHAUSTION | 1936 address/building unclosed. |
| `REGENT-CURRENT::8-BEST-ROAD` | R1 | PUBLIC_LIMITED_HOURS | current same-name hotel only; explicitly not merged with 1936 site. |

## Current web evidence used for access/continuity

- YSS Dwarahat / Babaji cave: https://yssofindia.org/location/dwarahat
- Dunagiri temple: https://dunagiritemple.com/about-the-temple/
- Hansavedas: https://hansavedas.org/path-of-yoga/
- Jhusi claimant banyan: https://www.kriyayoga-yogisatyam.org/mother-centre
- YSS Serampore/Rai Ghat/Panthi: https://yssofindia.org/location/dakshineswar
- YSS current successor institutions: https://yssofindia.org/ashrams/yogoda-satsanga-math-dakshineswar
- Ramnagar Fort: https://www.incredibleindia.gov.in/en/uttar-pradesh/varanasi/ramnagar-fort
- Tailang Swami Math/Panchganga: https://pawanpath.up.gov.in/ghats/
- Keshav Ashram Haridwar: https://www.katyayanipeeth.org.in/about1
- Karar Ashram property continuity: https://indiankanoon.org/doc/109151220/
- Babaji Nagaraj pilgrimage site: https://www.babajiskriyayoga.net/rwd/english/pilgrimages.htm
- Satopanth: https://www.uttarakhandtourism.gov.in/treks-details/Satopanth%20Lake%20Trek
- Haidakhandi current ashrams/contacts: https://haidakhandisamaj.in/ashrams/ and https://haidakhandisamaj.in/contact/
- Dihika: https://yssofindia.org/location/dihika
- Serampore College: https://seramporecollege.ac.in/
- Albert Hall / Indian Coffee House heritage identity: https://www.kmcgov.in/KMCPortal/downloads/Graded_List_04_08_2022.pdf
- current Regent Hotel name-match: https://www.regenthotelcolaba.in/contact-us.html

Where a site is current but historical equivalence is unproved, the matrix records the current object separately rather than silently upgrading the historic claim.

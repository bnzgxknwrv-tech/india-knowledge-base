# SOURCE LEDGER — ALL FINDINGS LOCATION CLOSURE

Date: 2026-08-20
Branch: `agent/india8-cluster-casting`
Purpose: lossless accounting BEFORE physical-site deduplication and BEFORE any new Mark A/B/C round.

## HARD RULE
This ledger counts source-layer records/claims, not unique physical places. The same physical site can occur in multiple detectors, multiple persons and multiple scenes. No source record may disappear during deduplication: every record must later point either to a physical entity, an explicit duplicate mapping, a negative/non-presence control, or an unresolved queue item.

## VERIFIED SOURCE FAMILIES AND COUNTS

### AOAY / Yogananda
- `AOAY-FULL-LOCATION-ATLAS-001/RAW_OCCURRENCES.jsonl`: 1,359 raw place-occurrence records in the first full-book extraction.
- `AOAY-FULL-LOCATION-ATLAS-001/PLACE_ATLAS.jsonl`: 123 normalized places in the first full-book atlas.
- AOAY STATUS explicitly says 30 places were `AOAY_FOUND_BUT_MISSING_FROM_REPO`, 19 directly confirmed existing Top-11 points, and `AOAY_LOCATION_SWEEP_SATURATED: NEE`.
- The later Yogananda METHOD_V2 pass re-read all 82 India places from the AOAY atlas at occurrence-context level.
- External Yogananda union: 114 records; later directly reconciled. This union contains true, false, partial and unresolved records and therefore remains source evidence, not canon by vote.
- Important independent direct-source-only addition: Regent Hotel, Bombay, third floor, Sri Yukteswar resurrection-vision scene; missed by all five external AIs.

### Core Kriya — Babaji / Lahiri Mahasaya / Sri Yukteswar
Primary IndiaROOD freezes ingested by CCI reconciliation:
- Mahavatar Babaji: 50 records.
- Lahiri Mahasaya: 40 records + 6 negative associations.
- Sri Yukteswar: 42 records + 14 negative findings.
- `INDIAROOD_DELTA_MATRIX.jsonl`: exactly 120 cross-detector reconciliation rows. This is a crosswalk, not 120 additional unique locations.

### Ramana Maharshi / Ramakrishna
IndiaGEEL freezes:
- Ramana Maharshi: 51 normalized records.
- Ramakrishna: 55 normalized records.
- `RECONCILIATION_MATRIX.jsonl`: exactly 80 cross-detector rows. Some rows intentionally aggregate many source records, e.g. the Kolkata devotee-house/theatre network, so 80 MUST NOT be mistaken for a site count.

### Neem Karoli Baba / Ram Dass
IndiaGEEL freezes:
- Neem Karoli Baba: 46 normalized records.
- Ram Dass: 55 normalized records.
- `RECONCILIATION_MATRIX.jsonl`: exactly 44 cross-detector rows. Multiple rows aggregate several micro-sites.

### Anandamayi Ma
- Earlier CCI layer: about 23 points, later proven incomplete.
- External multi-AI union: 156 master locations.
- Independent source-first official/lineage pass then listed a further 108 strong source-first additions/extra route sublocations across the official chronology. These 108 are discovery claims and can overlap the 156 union; they are NOT yet 108 unique union misses.
- Anandamayi remains a critical host-house/dharamshala/palace/ashram long-tail source family.

### Targeted-only persons per Mark decision
- Swami Vivekananda: 9 targeted major travel-relevant records. NOT an exhaustive nationwide sweep by explicit Mark decision.
- Paramahamsa Hariharananda: 7 targeted major travel-relevant records. NOT exhaustive by explicit Mark decision.
- Important no-silent-drop correction: the Hariharananda freeze also records an historically attested but physically unresolved rented seashore house in Puri. Although excluded from the old targeted major-site list, it MUST enter the global unresolved queue because it is an already-found historical location claim.
- Vivekananda's targeted freeze explicitly names many deliberately non-expanded wandering locations. They remain known exclusions, but this task does not override Mark's decision against a new exhaustive Vivekananda sweep.

## KNOWN SOURCE-LAYER VOLUME — LOWER BOUND
The following directly countable normalized/source-list layers alone contain at least:

- person freezes: 50 + 40 + 42 + 51 + 55 + 46 + 55 + 9 + 7 = 355
- Yogananda external union = 114
- Anandamayi external union = 156
- AOAY normalized place atlas = 123
- Anandamayi source-first listed additions/extra route claims = 108

`KNOWN_SOURCE_LAYER_LOCATION_RECORDS_OR_LISTED_CLAIMS >= 856`

This `>=856` is deliberately NOT a unique-location count. It excludes the 1,359 AOAY raw occurrences from the arithmetic, excludes negative controls, and avoids adding reconciliation crosswalk rows (120/80/44) on top of the source records they cross-reference. It also does not yet count every old regional-cluster candidate/ID layer separately.

## WHY UNIQUE-SITE TOTAL IS NOT YET SAFE
A simple sum would be wrong because:
- one site can have many AOAY occurrences;
- one site can be visited by several persons;
- one detector may split a room/courtyard/ashram while another uses one compound record;
- some records are traditions/negative controls rather than ordinary physical presence;
- some external records were later disproved or only partially true;
- existing old cluster IDs may duplicate later person-first findings.

Therefore `UNIQUE_PHYSICAL_ENTITY_COUNT` remains intentionally unset until every source record has an explicit entity link or unresolved disposition.

## REQUIRED ENTITY-MAPPING FIELDS
Every source record in the next stage must preserve:
- source_family
- source_record_id
- person/layer
- raw_place_name
- event/scene
- AOAY chapter where applicable
- presence status
- evidence/tradition status
- candidate physical entity id
- R1/R2/R3/R4/R5
- access status if R1-R3
- existing permanent ID + Mark A/B/C if already assigned
- duplicate links, never silent merge
- unresolved reason + next search route

## ACCOUNTING GATE
Final stage-A accounting must satisfy:

`TOTAL_SOURCE_RECORDS_INGESTED = RECORDS_LINKED_TO_PHYSICAL_ENTITY + RECORDS_EXPLICITLY_DUPLICATE + NEGATIVE/NONPRESENCE_CONTROLS + RECORDS_STILL_UNRESOLVED`

Only after this closes may a cluster be declared complete enough for a new Mark A/B/C pass.

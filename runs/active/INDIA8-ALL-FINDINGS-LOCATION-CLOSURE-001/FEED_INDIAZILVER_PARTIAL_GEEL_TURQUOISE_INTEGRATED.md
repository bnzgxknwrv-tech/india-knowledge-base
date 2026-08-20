# FEED — INDIA ZILVER PARTIAL PROXIMITY / ID BACKFILL

Date: 2026-08-20
Source branch: `agent/indiazilver-cluster-completeness-audit`
Task: `INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001`
State: PARTIAL_COMPLETE__GEEL_TURQUOISE_INTEGRATED__OTHER_FEEDS_ADDITIVE

## OUTPUT COMMITS
- PROTECTED_CANON_BASELINE.csv — `70b5fc0f7b86439506ec1b932897edc2f05988b3`
- NEW_ID_REQUIRED_QUEUE.csv — `92a96bf3fcf2bdc58d758adaf689278484be9f88`
- PROXIMITY_1KM_3KM_MATRIX.csv — `1c2187731a9c2a2195b7d887931022b7406e8def`
- DUPLICATE_PARENT_CANDIDATES.md — `befb91bd2024e10d07b0f27ca1c5679494eb3ff8`
- ABC_REVIEW_AFTER_CLOSURE_QUEUE.md — `cfb7e480971e4eb3fa3f335d59bdde287d70e366`
- STATUS.md — `35dee24f388350ab4a2aa3dca5a41a128a305b42`

## PRESERVATION
- Existing IDs unchanged.
- Existing A/B/C unchanged.
- Locks unchanged.
- No coordinates guessed.
- Original 31-candidate queue retained and expanded.

## ENTITY RULES APPLIED
- Kainchi and NKB Vrindavan remain existing parents with separate microsites.
- Sri Ramanasramam, Dakshineswar and Cossipore not duplicate-numbered from GEEL.
- Virupaksha Cave and Mango Tree Cave remain separate.
- Banke Bihari is one physical site with Ram Dass + Ramakrishna person links.
- Historical huts/cremation sites and later successor/memorial structures remain temporally distinct.

## PROXIMITY STATUS
GEEL/TURQUOISE did not provide complete reliable coordinate pairs against protected canon; therefore no fabricated <=1 km/<=3 km numeric claims were added. UNKNOWN/dependency is correct until reliable coordinates arrive.

## NEXT
Keep ZILVER as one of at most two active workers. It may append WIT and later ROOD feeds, but do not spawn further colors. Once ROOD closes and ZILVER has appended final available feeds, central INDIA8/9 performs consolidation into ALL_FINDINGS_LOCATION_MASTER.

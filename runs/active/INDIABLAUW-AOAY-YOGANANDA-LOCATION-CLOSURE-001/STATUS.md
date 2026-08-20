task_id: INDIABLAUW-AOAY-YOGANANDA-LOCATION-CLOSURE-001
state: COMPLETE
branch: agent/indiablauw-trip-ops-prep
completed: 2026-08-20
priority: P0
outputs:
  - AOAY_YOGANANDA_SOURCE_RECORDS.jsonl
  - AOAY_YOGANANDA_ENTITY_CANDIDATES.jsonl
  - AOAY_YOGANANDA_R4_R5_CLOSURE.md
  - AOAY_YOGANANDA_ACCESS_MATRIX.md
accounting:
  source_records: 58
  entity_mappings: 58
  silent_drops: 0
  balance: CLOSED_58_OF_58
constraints:
  existing_ids_changed: false
  abc_changed: false
  route_selected: false
  uncertain_locations_filtered_out: false
key_closures:
  - Haridwar ch4 split into station, detention-bungalow, and Rishikesh negative/not-reached claim.
  - Vrindavan ch11 Madanamohana Temple recovered as named R1 entity; station-adjacent initiation micro-site retained R5.
  - Keshabananda ch42 historic name recovered as Katayani Peith Ashram; modern continuity remains R4.
  - Regent Hotel Bombay fixed historically to named third-storey hotel room; current same-name Colaba hotel not conflated without continuity proof.
  - Bhaduri house mapped R2 to Nagendra Math; YSS says open to devotees.
  - Serampore Rai Ghat Lane hermitage mapped R2 to Smriti Mandir continuity.
  - Mysore/Bangalore lecture venues split and resolved individually where evidence permits.
  - Kashmir expanded to Srinagar inn, Shankaracharya Temple, Gulmarg, Khilanmarg, Shalimar, Nishat and Dal Lake.
blockers:
  - Required governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md is absent on the mandated branch (GitHub 404; exact repo search no match). Operational R1-R5 definitions are therefore stated explicitly in the closure output rather than fabricated from the missing file.
  - Several private-house/micro-site claims remain R4/R5 because no reliable parcel/address continuity was found: Gorakhpur compound, Bareilly bungalow, Pranabananda residence, Benares pundit home, Rana Mahal exact house, Bhowanipore encounter point, Ananta Agra bungalow, Srinagar inn, Yuvaraja summer palace, Purulia host, Giri Bala house, Satish Delhi home.
  - Current Regent Hotel at 8 BEST Road is only a modern same-name candidate; historical continuity to the 1936 Regent Hotel remains unproven.
  - Non-AOAY claims identified by prior deepening (Roma/Girish Vidyaratna Lane, Tulsi Bose, Kshattriya Conference, Bowbazar/Serpentine Lane, early lecture halls, Gokhale Hall, Chittagong memoir claim) still require their named archival source families before promotion.
next: safe for later Mark A/B/C only after consumer respects R-level/access uncertainty and does not treat R4/R5 as exact sites.

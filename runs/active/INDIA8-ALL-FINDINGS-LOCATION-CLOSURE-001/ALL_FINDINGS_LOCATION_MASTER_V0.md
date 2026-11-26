# ALL_FINDINGS LOCATION MASTER V0 — CONCRETE INGEST

Date: 2026-08-20
State: BUILDING__SOURCE_FAMILIES_INGEST_STARTED
Coordinator: INDIA8

This is not a shortlist and not Mark A/B/C. It is the concrete lossless master build.

## FEED STATE
- BLAUW AOAY/Yogananda: COMPLETE; 58 source records -> 58 candidate mappings; 0 silent drops.
- TURQUOISE relation layer: COMPLETE; merge / same-site / parent-child / successor / ambiguous relations govern entity linking.
- GEEL four-person: COMPLETE; composite findings physically split into micro-sites.
- WIT Anandamayi/heritage: COMPLETE; canonical R1-R5 + access assigned.
- ROOD Core Kriya: COMPLETE; 178 source records (146 claims + 32 negatives), 204 physical candidates, 58 splits; R1 31/R2 2/R3 34/R4 54/R5 25.
- ZILVER: COMPLETE_CURRENT_GLOBAL_FEEDS__READY_FOR_CENTRAL_MASTER; permanent canon 001-081 protected; final new-ID/proximity/review staging available.

## INGESTED CONCRETE FAMILY A — AOAY / YOGANANDA
Authoritative source: BLAUW `AOAY_YOGANANDA_ENTITY_CANDIDATES.jsonl` + source records.
Accounting target: 58/58.

The following 58 task-local physical candidate handles are admitted to master ingest without filtering:
AYC-ENT-001 Gorakhpur childhood family compound [R4]
AYC-ENT-002 Bareilly family bungalow/piazza/sheoli-tree micro-site [R5]
AYC-ENT-003 4 Garpar Road / linked YSS Garpar Road centre [R2]
AYC-ENT-004 Barddhaman Junction [R2]
AYC-ENT-005 Pt. Deen Dayal Upadhyaya Junction / Mughalsarai [R2]
AYC-ENT-006 Bareilly Junction [R2]
AYC-ENT-007 Haridwar Junction [R2]
AYC-ENT-008 Hardwar station police/station bungalow [R5]
AYC-ENT-009 Rishikesh intended destination [NEGATIVE_NOT_VISITED; R5]
AYC-ENT-010 Pranabananda residence, Benares [R5]
AYC-ENT-011 scriptural authority home/courtyard, Benares [R5]
AYC-ENT-012 Sri Yukteswar temporary house, Rana Mahal zone [R3]
AYC-ENT-013 Nagendra Math / Bhaduri Mahasaya house successor [R2]
AYC-ENT-014 Acharya Bhavan / Sir J.C. Bose Trust [R1]
AYC-ENT-015 Dakshineswar Kali Temple [R1]
AYC-ENT-016 50 Amherst Street heritage site [R3]
AYC-ENT-017 Bhowanipore Anandamayi Ma encounter point [R5]
AYC-ENT-018 Sri Yukteswar Smriti Mandir / Rai Ghat Lane site [R2]
AYC-ENT-019 Anandaloka / uncle Sarada Prasad Ghosh home [R2]
AYC-ENT-020 Serampore railway station [R1]
AYC-ENT-021 Vrindavan railway station [R2]
AYC-ENT-022 Madan Mohan Temple, Vrindavan [R1]
AYC-ENT-023 Kriya-initiation secluded spot near Vrindavan station [R5]
AYC-ENT-024 Katayani Peith Ashram historic building claim [R4]
AYC-ENT-025 Ananta bungalow, Agra [R5]
AYC-ENT-026 Taj Mahal, Agra [R1]
AYC-ENT-027 YSS Ranchi Ashram/school site [R1]
AYC-ENT-028 YSS Dihika retreat/heritage continuity [R2]
AYC-ENT-029 Karar Ashram, Puri [R1]
AYC-ENT-030 Santiniketan Tagore meeting/study-room claim [R3]
AYC-ENT-031 Wardha Junction [R1]
AYC-ENT-032 Maganvadi guesthouse claim [R3]
AYC-ENT-033 Gandhi writing-room claim, Maganvadi [R3]
AYC-ENT-034 Mumbai Harbour arrival landscape [R5]
AYC-ENT-035 Taj Mahal Palace, Mumbai [R1]
AYC-ENT-036 1936 Regent Hotel Bombay / current same-name candidate [R4; DO_NOT_COLLAPSE]
AYC-ENT-037 C. V. Rangacharlu Memorial Hall / Mysore Town Hall [R1]
AYC-ENT-038 Maharaja's College, Mysuru [R1]
AYC-ENT-039 Mysore Medical College historic campus [R2]
AYC-ENT-040 National High School, Bengaluru [R3]
AYC-ENT-041 Intermediate College, Bangalore [R5]
AYC-ENT-042 Sir Puttanna Chetty Town Hall, Bengaluru [R2]
AYC-ENT-043 Sri Chamundeshwari Temple, Chamundi Hill [R1]
AYC-ENT-044 Krishna Raja Sagara Dam [R1]
AYC-ENT-045 Brindavan Gardens [R1]
AYC-ENT-046 Yuvaraja summer palace, Mysore [R5]
AYC-ENT-047 Srinagar double-storey inn [R5]
AYC-ENT-048 Shankaracharya Temple, Srinagar [R1]
AYC-ENT-049 Gulmarg [R1]
AYC-ENT-050 Khilanmarg excursion landscape [R3]
AYC-ENT-051 Shalimar Bagh, Srinagar [R1]
AYC-ENT-052 Nishat Bagh, Srinagar [R1]
AYC-ENT-053 Dal Lake channels/floating gardens [R3]
AYC-ENT-054 Shimla personal stop [R4]
AYC-ENT-055 Lambadar Dey host location, Purulia [R5]
AYC-ENT-056 Giri Bala two-storey house, Biur [R4]
AYC-ENT-057 1936 Allahabad Kumbh Mela grounds [R4]
AYC-ENT-058 Satish Chandra Bose residence, Delhi [R5]

AOAY family ingest accounting: 58 candidate handles present / expected 58. No filter applied.

## INGESTED CONCRETE FAMILY B — CORE KRIYA STRUCTURE
ROOD master admission is source-key first. All 146 primary claim anchors remain traceable and all 58 extra physical splits are admitted separately; negatives remain accounting rows, not travel entities.

High-risk split entities already admitted as distinct master objects include:
- DUNAGIRI-1861::CAVEFIELD [R3 landscape]
- DUNAGIRI-1861::UNNAMED-INITIATION-CAVE [R5]
- DUNAGIRI-YSS::PANDUKHOLI-CAVE [R1 current claimant; NOT automatically same as 1861 cave]
- DUNAGIRI-GAGAS::RIVER-SYSTEM [R3]
- DUNAGIRI-GOLDEN-PALACE::EPHEMERAL [R5]
- PRAYAG-1894::HISTORIC-MELA-ZONE [R3]
- PRAYAG-1894::BRIDGE [R5]
- PRAYAG-1894::TREE-AOAY [R5]
- PRAYAG-1894::YOGI-SATYAM-BANYAN [R1 current claimant; NOT silently same historic tree]
- DASHASHWAMEDH::GHAT [R1]
- DASHASHWAMEDH::MATAJI-CAVE [R5 hidden micro-site]
- RAI-GHAT::BANYAN [current claimant micro-site]

ROOD accounting guard: 178 source records retained; 204 physical candidates retained; 32 negatives retained as accounting dispositions; Babaji claimant traditions remain separate.

## INGESTED CONCRETE FAMILY C — GEEL FOUR-PERSON MICRO-SITES
GEEL entities are admitted individually. Explicit anti-collapse examples already in master:
- NKB Neeb Karori cave vs Hanuman temple vs station/platform.
- Hanumangarh temple vs Baba hut/kuti.
- Bhumiadhar temple/ashram vs Baba room vs Ram Dass first-meeting terrace/field.
- Kainchi original rock/platform, Maharajji room, Hanuman temple/courtyard, bridge, Ram Dass 1967 room, river bathing point, fire-ceremony zone, cold hut/village, 2004 room and Maharajji back room remain separate.
- Hotel Evelyn parent hotel [R1], top-floor cave room [R4], patio/balcony [R3] remain separate.
- K.K. Sah Nainital home [R4] retained.
- 4 Church Lane parent [R1], Maharajji room [R2], hall [R3], veranda [R3], kitchen [R3], front/bathroom area [R4] remain separate.
- NKB final-journey Agra houses/clinic/station and Mathura/Vrindavan medical/transit micro-sites remain separate.
- Ramana Virupaksha Cave and Mango Tree Cave remain separate; Ramanasramam microsites remain children, not duplicates.
- Ramakrishna Fouzdar Kunj building/room/veranda, Ganga Mata hut vs later dharamshala, Mani Sen house vs Radhakanta temple, Cossipore house/room/cremation-ghat remain separate.

## INGESTED CONCRETE FAMILY D — WIT ANANDAMAYI / HERITAGE
Representative admitted rows, with all source IDs retained in authoritative WIT file:
- Bhadaini Anandamayi Ashram, Varanasi [R1, PUBLIC_OPEN, overnight room-booking signal]
- Pandey Dharamshala, Varanasi [R5]
- Kunja Mohan Babu house, Varanasi [R4]
- Burdwan/Vardhaman Kunj, Vrindavan [R2, permission possible]
- Anandamayi Ashram Vrindavan [R1]
- Bhola Giri/Giriji Ashram, Kankhal [R5]
- Kankhal Anandamayi Ashram [R1, current stay by booking]
- Matri Smriti Museum bungalow [R1, preserved historic bedroom/kitchen; museum, NOT overnight]
- Anandamayee International Centre, Kankhal [R1 current accommodation, NOT historic sleep room]
- Baghat House, Haridwar [R5]
- Shanti Niketan / Nitai Basu Mallick residence, Kankhal [R3]
- Jaipuria House Ramghat, Haridwar [R4]
- Kishenpur, Kalyanvan, Raipur and Sadhan Ashram in Dehradun [R1 current institutions]
- Patal Devi Ashram, Almora [R1]
- Dhaulchina Ashram [R1, limited/restricted stay context]
- Anandamayi Ashram Swargadwar, Puri [R1]
- Karar Ashram Anandamayi claim remains R5 even though site itself is exact for other persons.
- Ratu Palace [R1 historic palace identity; access uncertain]
- Raj Bhavan Chennai and Bhubaneswar [R1 institution; restricted]
- M.S. Subbulakshmi/T. Sadasivam residence + purpose-built lawn hut [R5]

No route deprioritization deletes East/South WIT rows.

## ZILVER PROTECTIVE OVERLAY
Final status is `COMPLETE_CURRENT_GLOBAL_FEEDS__READY_FOR_CENTRAL_MASTER`.
- Existing permanent IDs 001-081 immutable.
- No existing A/B/C/lock changed.
- No definitive new permanent ID issued yet.
- 16 trustworthy numeric pair calculations; 7 tight pairs: 4 <=1km + 3 additional <=3km.
- Rana Mahal Ghat -> 019 Kedareshwar/Kedar Ghat = 0.895 km.
- Rana Mahal Ghat -> 018 Sankatha Devi = 1.285 km.
- 012 B, 013 B, 026 C, 027 C, 040 C remain only POTENTIAL_REVIEW_FOR_UPGRADE_AFTER_COORD_CONFIRMATION.

## NEXT BUILD ACTION ALREADY ACTIVE
1. Expand every GEEL/WIT/ROOD authoritative candidate row into source->entity master accounting, not merely the representative rows above.
2. Apply TURQUOISE relation map mechanically: duplicate != parent-child != successor != ambiguous.
3. Attach canon 001-081 and ZILVER NEW_ID_REQUIRED staging.
4. Close accounting equation before any Mark A/B/C request.
5. CCI independently QA-checks silent drops and false collapses in parallel.

No cluster is declared Mark-ready merely because this V0 exists.
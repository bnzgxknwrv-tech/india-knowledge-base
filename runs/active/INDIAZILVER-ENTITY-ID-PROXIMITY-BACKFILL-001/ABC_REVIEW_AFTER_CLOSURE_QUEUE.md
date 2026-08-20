# ABC_REVIEW_AFTER_CLOSURE_QUEUE — INDIA ZILVER

status: UPDATED_WITH_GEEL_AND_TURQUOISE
hard_rule: no A/B/C choice is changed or proposed automatically; this file only stages later Mark review after entity closure/ID assignment.

## Existing 31-candidate review seed

All 31 candidates from `REOPEN_AND_ID_QUEUE.md` remain `MARK_REVIEW_REQUIRED: JA`. Their earlier review flags remain valid. TURQUOISE/GEEL adds the following material review context without altering any choice:

- Sri Ramanasramam: `MULTI_PERSON_SAME_SITE` Ramana + Yogananda; child microsites now explicit.
- Dakshineswar Kali Temple complex: `MULTI_PERSON_SAME_COMPLEX`; Ramakrishna room/Panchavati/Bel tree/ghat now explicit children.
- Cossipore Garden House: terminal room and physically separate cremation ghat now explicit.
- Ramana Arunachala cluster: Virupaksha, Mango Tree Cave, Skandashram and additional caves/rocks/springs are distinct sites, not one compound candidate.
- Akbarpur NKB: historic birth/family site and 2001 temple are temporal-chain entities, not one lifetime building.
- Ranchi: historic Vidyalaya/current YSS campus is a same-campus successor relation; exact garden event remains a child dependency.

## New GEEL entities that require later Mark review after ID/dedup

### Neem Karoli Baba / Ram Dass — Kumaon
- Neeb Karori Hanuman temple above cave — `MARK_REVIEW_REQUIRED`; `HISTORIC_RESIDENCE_CLUSTER`.
- Historic Neeb Karori cave / current continuity cave — `MARK_REVIEW_REQUIRED`; `SUCCESSOR_IDENTITY_CAVEAT`.
- Neeb Karori railway station/platform — `MARK_REVIEW_REQUIRED`; `TRANSIT_EVENT`.
- Hanuman Garhi/Hanumangarh temple — `MARK_REVIEW_REQUIRED`; `MULTI_PERSON_SAME_SITE`.
- Hanumangarh Baba hut — `MARK_REVIEW_REQUIRED`; `CHILD_MICROSITE`.
- Bhumiadhar parent/room/first-meeting field — `MARK_REVIEW_REQUIRED`; `PARENT_CHILD_CLUSTER`; parent dedup first.
- Kainchi rock/platform, Maharajji room, Hanuman courtyard, bridge, Ram Dass room, river bathing site — `MARK_REVIEW_REQUIRED`; `CHILD_MICROSITES_OF_EXISTING_PARENT`; no duplicate parent ID.
- Hotel Evelyn — `MARK_REVIEW_REQUIRED`; `HISTORIC_STAY`; cave-room/patio children must remain visible; cave-room itself remains R4 dependency.
- Ramsay Hospital clinic — `MARK_REVIEW_REQUIRED`; `MEDICAL_EVENT`.

### Prayagraj / Vrindavan
- 4 Church Lane / Red House parent — `MARK_REVIEW_REQUIRED`; `MULTI_PERSON_SAME_SITE`; room/hall/veranda/kitchen children explicit.
- Ramakrishna Mission Hospital Vrindavan — `MARK_REVIEW_REQUIRED`; `FINAL_JOURNEY_MEDICAL_SITE`; distinct from NKB ashram.
- NKB Vrindavan parent — existing locked entity: `PERSON_LINK_UPGRADE` only; no automatic ABC review unless existing policy later requests it.
- NKB Vrindavan office/courtyard children — `MARK_REVIEW_REQUIRED`; `CHILD_MICROSITES` after ID policy decision.
- Seth Anandram Jaipuria Bhawan — `MARK_REVIEW_REQUIRED`; `HISTORIC_STAY`.
- Banke Bihari Temple — `MARK_REVIEW_REQUIRED`; `MULTI_PERSON_SAME_SITE` Ram Dass + Ramakrishna.
- Fouzdar Kunj building/upper room/veranda — `MARK_REVIEW_REQUIRED`; `HISTORIC_STAY`; parent-child preserved.
- Nidhivan grove and Ganga Mata historic hut — `MARK_REVIEW_REQUIRED`; `HISTORIC_SPIRITUAL_SITE`; later dharamshala successor must not inherit lifetime-presence claim.

### Ramana — Tiruvannamalai / Arunachala
- Arunachaleswarar inner sanctum, Thousand-Pillared Hall and Patala Lingam — `MARK_REVIEW_REQUIRED`; `CHILD_MICROSITES`; do not flatten into temple parent.
- Mango Tree Cave — `MARK_REVIEW_REQUIRED`; `DISTINCT_FROM_VIRUPAKSHA`.
- Satguru Swami Cave, Guhai Namasivaya, Tortoise Rock/Cave, Seven Springs — `MARK_REVIEW_REQUIRED`; `ARUNACHALA_MICROSITE`.
- Sri Ramanasramam Mother shrine, Old Hall, kitchen, Mathrubhuteswara inner shrine, New Hall, Nirvana Room — `MARK_REVIEW_REQUIRED`; `CHILD_MICROSITES_OF_RAMANASRAMAM`.

### Ramakrishna — Kolkata
- Dakshineswar Ramakrishna room, Panchavati and Bel-tree site — `MARK_REVIEW_REQUIRED`; `CHILD_MICROSITES_OF_EXISTING_PARENT_CANDIDATE`.
- Balaram Mandir — `MARK_REVIEW_REQUIRED`; `MAJOR_HOST_HOUSE`; Jagannath/Ratha first-floor room remains child.
- Shyampukur Bati — `MARK_REVIEW_REQUIRED`; `FINAL_ILLNESS_SITE`; first-floor room child.
- Cossipore final upstairs room — `MARK_REVIEW_REQUIRED`; `CHILD_OF_COSSIPORE`.
- Cossipore cremation ghat — `MARK_REVIEW_REQUIRED`; `DISTINCT_TERMINAL_SITE`; proximity backfill required.
- Panihati Mani Sen house / Radhakanta temple and Raghava Pandit site — `MARK_REVIEW_REQUIRED`; `PARENT_CHILD_OR_COMPOUND_REVIEW`.

## R4/R5 dependency queue — preserve but DO NOT send to ABC yet

These findings remain entity-closure dependencies and are not silently dropped: Hotel Evelyn cave-room; K.K. Sah house address; Gethia sanatorium; 4 Church Lane front/bathrooms area; NKB Agra Jagmohan/S-house/clinic/station micro-sites; Mathura station steps conflict; Ram Dass Varanasi hotel; Dharamsala Swarg Ashram/guesthouse; Delhi Health/Finance/AmEx/restaurant/alley/hotel/Soni house; Surat cave; Ramana float-room/tower/bridge/banyan route; Ramakrishna Jayagopal/Lily/Surendra/Adhar/Nanda/Ramchandra/Ganu/Brahmani private-house findings.

Rule: `ENTITY_CLOSURE_FIRST -> ID/DEDUP -> MARK_REVIEW`. No R4/R5 item receives guessed coordinates or an automatic A/B/C.

## Existing locations — review-for-upgrade only, never modify here

- `VNS-CAND-002` Lahiri house: Sri Yukteswar person-link enrichment; `REVIEW_FOR_UPGRADE` only if current status is B/C.
- `VNS-CAND-009` Dashashwamedh Ghat: tradition/event-link enrichment; hidden cave remains unresolved; `REVIEW_FOR_UPGRADE` only if current B/C.
- `VNS-CAND-004` / `VNS-CAND-011`: identity review for Trailanga/Panchganga lead before any upgrade review.
- `VNS-CAND-044`: Kashi Naresh tutoring identity review before any upgrade review.
- Kainchi Dham: Ram Dass person-link enrichment; existing status unchanged.
- NKB Vrindavan Ashram/Mahasamadhi: Ram Dass person-link enrichment; existing lock/status unchanged.
- `KB2-038` Mayavati: Vivekananda link enrichment; upgrade review only after Kumaon identity/numbering policy allows it.

No downgrade queue is created.

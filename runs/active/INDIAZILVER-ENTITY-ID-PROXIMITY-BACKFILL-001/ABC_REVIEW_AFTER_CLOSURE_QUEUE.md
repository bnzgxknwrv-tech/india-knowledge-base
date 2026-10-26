# ABC_REVIEW_AFTER_CLOSURE_QUEUE — INDIA ZILVER

status: UPDATED_WITH_GEEL_TURQUOISE_WIT_ROOD_FINAL
hard_rule: no A/B/C choice is changed or proposed automatically; this file only stages later Mark review after entity closure/ID assignment.

## Existing 31-candidate review seed

All 31 candidates from `REOPEN_AND_ID_QUEUE.md` remain `MARK_REVIEW_REQUIRED: JA` once their entity/ID gate is satisfied. No candidate receives an A/B/C here.

Material context:
- Sri Ramanasramam: `MULTI_PERSON_SAME_SITE` Ramana + Yogananda; child microsites explicit.
- Dakshineswar Kali Temple complex: `MULTI_PERSON_SAME_COMPLEX`; room/Panchavati/Bel tree remain children.
- Cossipore Garden House: final room child; cremation ghat physically distinct.
- Ramana Arunachala cluster: Virupaksha, Mango Tree Cave, Skandashram and other cave/rock/spring sites remain distinct.
- Akbarpur NKB: historic birth/family site and 2001 temple are a temporal chain, not one lifetime building.
- Ranchi: historic Vidyalaya/current YSS campus is same-campus institutional succession; garden event remains child dependency.

## Numeric proximity consequences

Hard numeric gate used only endpoints whose coordinates are independently strong enough for the task. The old Varanasi 25–100 m working pins are preserved in the baseline but are not promoted to hard proximity evidence unless the Varanasi final decision overview also records a confirmed marker.

Confirmed new-candidate proximity:
- `OLD31-28` Rana Mahal Ghat ↔ permanent `019` Kedareshwar Temple/Kedar Ghat: **0.895 km (<=1 km)**. Existing `019` is **A**, therefore no `REVIEW_FOR_UPGRADE`; clustering/context only.
- `OLD31-28` Rana Mahal Ghat ↔ permanent `018` Sankatha Devi Temple: **1.285 km (<=3 km)**. Existing `018` is **A**, therefore no `REVIEW_FOR_UPGRADE`; clustering/context only.

Confirmed baseline reference pairs include 029↔031 0.620 km, 029↔033 0.165 km, 031↔033 0.642 km and Bodh Gaya 046↔047 1.224 km. These do not change existing protected A/B/C.

ROOD and WIT contribute no new pair where both endpoints pass the hard WGS84 quality gate, so the final numeric totals remain **16 numeric pairs / 7 tight pairs**.

### Existing B/C that merit later proximity screening after coordinate confirmation

These are **not confirmed <=1/3-km findings**. Their old working pins place them near Rana Mahal and therefore they are explicitly staged for re-check once their own marker is confirmed:
- `012` Harishchandra Ghat — current **B** — old working-pin screen ~0.594 km from Rana Mahal → `POTENTIAL_REVIEW_FOR_UPGRADE_AFTER_COORD_CONFIRMATION`.
- `013` Kaal Bhairav Temple — current **B** — old working-pin screen ~1.958 km → same conditional review.
- `026` Ramakrishna Mission Home of Service — current **C** — old working-pin screen ~1.330 km → same conditional review.
- `027` Baba Keenaram Sthal / Krim Kund — current **C** — old working-pin screen ~1.589 km → same conditional review.
- `040` Bharat Mata Temple — current **C** — old working-pin screen ~2.494 km → same conditional review.

Do **not** treat those five screening distances as hard matrix results until their coordinate quality closes. `008` (B) has an explicitly rejected old coordinate; `023` (B) has an unresolved ~3 km coordinate conflict; `025` (B) has only an approximate 100–500 m class point. All three remain `DEPENDENCY_COORDINATE` rather than being forced into a proximity band.

## Existing Varanasi enrichment / identity cases — protected decisions preserved

- `002` Lahiri house is **A**. ROOD `LAHIRI-HOUSE::BUILDING` and Sri Yukteswar linkage are `PERSON_LINK_ENRICHMENT_ONLY`; parlor and threshold remain child microsites.
- `009` Dashashwamedh Ghat is **A**. ROOD confirms the ghat parent; hidden Mataji cave remains R5 entity dependency.
- `004` and `011` are both **A**. ROOD resolves Tailang Math/Panchganga parent identity; no A/B/C upgrade request.
- `044` is a permanent but **PROVISIONAL_NO_ABC** record. ROOD resolves Ramnagar Fort parent identity but the tutoring room remains child-level; later treatment is an initial A/B/C decision, not an upgrade.
- `VNS-HOTEL-001` remains `LOCKED_BY_MARK`; it is outside A/B/C candidate numbering.

## New GEEL entities requiring later Mark review after ID/dedup

Neem Karoli Baba / Ram Dass — Kumaon: Neeb Karori temple/cave/station; Hanuman Garhi parent/child hut; Bhumiadhar parent/room/first-meeting field; Kainchi child rock/room/Hanuman/bridge/Ram Dass room/river; Hotel Evelyn parent/patio; Ramsay Hospital. Kainchi parent itself is existing and receives enrichment only.

Prayagraj / Vrindavan: 4 Church Lane parent and children; Ramakrishna Mission Hospital Vrindavan; NKB Vrindavan child office/courtyard; Seth Anandram Jaipuria Bhawan; Banke Bihari Temple; Fouzdar Kunj parent/room/veranda; Nidhivan and Ganga Mata historic hut. NKB Vrindavan parent remains existing/locked and is not duplicated.

Ramana — Tiruvannamalai / Arunachala: Arunachaleswarar inner sanctum, Thousand-Pillared Hall and Patala Lingam; Mango Tree Cave; Satguru Swami Cave; Guhai Namasivaya; Tortoise Rock/Cave; Seven Springs; Sri Ramanasramam Mother shrine, Old Hall, kitchen, Mathrubhuteswara inner shrine, New Hall and Nirvana Room.

Ramakrishna — Kolkata: Dakshineswar room/Panchavati/Bel-tree children; Balaram Mandir; Shyampukur Bati and first-floor room; Cossipore final room and distinct cremation ghat; Panihati Mani Sen property / Radhakanta temple and Raghava Pandit site.

Rule for all: `ENTITY_CLOSURE_FIRST -> ID/DEDUP -> MARK_REVIEW`.

## ROOD final feed — review staging after dedup

ROOD contributes **204 temporary physical entity candidates**: 146 primary anchors plus 58 physical splits. Temporary ROOD keys are not permanent IDs. The final feed is consumed additively from `CORE_KRIYA_ENTITY_CANDIDATES.jsonl` and `CORE_KRIYA_SOURCE_RECORDS.jsonl`.

### ROOD entities that are existing-parent enrichment, not new parent ABC items

- `DASHASHWAMEDH::GHAT` → permanent `009`.
- `LAHIRI-HOUSE::BUILDING` → permanent `002`.
- `VARANASI-PANCHGANGA::GHAT` → permanent `011`.
- `VARANASI-PANCHGANGA::TAILANG-MATH` → permanent `004`.
- `RANA-MAHAL::GHAT` → `OLD31-28`.
- `RAMNAGAR::FORT-PALACE` → permanent provisional `044`; parent identity closure does not itself create an A/B/C.
- `GARPAR-4::HOUSE` → `OLD31-29`.
- `KARAR::COMPLEX` → `OLD31-14`.
- `DUNAGIRI-YSS::PANDUKHOLI-CAVE` → dedup against current permanent `079` only at the **current claimant site** layer; this must not convert the unresolved 1861 cave equivalence into fact.

### ROOD R1–R3 items that enter later Mark review after entity/ID closure

- Dunagiri/Gagas landscape anchors; Prayagraj 1894 mela-zone and present claimant banyan; Rai Ghat banyan.
- Lahiri-house front parlor and threshold; 4 Garpar room/roof; Karar samadhi and Hariharananda room-level sites.
- Parangipettai Babaji Nagaraj Mandir and claimed birth substrate — tradition-specific and separate from Dunagiri/Haidakhan.
- Satopanth lake-zone; Keshav Prayag confluence; Dunagiri/Harapriya temple dedup context.
- Haidakhan historic cave and Dhuni, under the separate Haidakhandi claimant tradition.
- Ghurni lost-estate landscape and Jaleshwar successor shrine.
- Ramnagar tutoring room; current Keshav Ashram Haridwar as possible successor only.
- Serampore Priyadham historic terrain, current Smriti Mandir successor, courtyard/hall/sitting-room/eating-patio/bedroom.
- Tulsi Bose historic house identity case and current YSS Garpar adjacent/successor centre.
- Panthi historic plot and demolished room; Dihika historic school/current retreat chain; Albert Hall/current Indian Coffee House.
- Current Regent Hotel 8 BEST Road remains a **same-name candidate**, not the proven 1936 Regent Hotel.

All of these remain `MARK_REVIEW_REQUIRED` only after `ENTITY_CLOSURE_FIRST -> ID/DEDUP`. None receives an A/B/C here.

## Babaji claimant-tradition ABC guard

Do not pool evidence or inherit A/B/C across claimant traditions. The following are separate review/evidence families:

- historic AOAY Dunagiri 1861 cave-field / unnamed initiation cave;
- current YSS Pandukholi cave identification (current site may dedup to `079`);
- Haidakhan Vishwa Mahadham / Haidakhan cave claimant tradition;
- Parangipettai Nagaraj/Babaji claimant tradition;
- present Yogi Satyam Jhusi banyan claimant identification versus the unresolved historical 1894 tree.

A positive travel/ABC judgement for one claimant tradition never auto-upgrades another.

## WIT final master context

WIT is an integrator, not a discovery sweep. Its completed master heatmap supplies `MIN_CONFIRMED` overlap and exact-site/non-merge context only.

Protected anchors are context, not re-decision:
- Arunachala/Tiruvannamalai remains a `LOCKED_BY_MARK` A-anchor.
- Kukuchina/Dunagiri remains the existing principal Babaji travel reason.

WIT exact-site context may increase the information shown in later Mark review but cannot change existing A/B/C:
- Lahiri house: Lahiri Mahasaya + Sri Yukteswar.
- Kainchi Dham: NKB + Ram Dass.
- NKB Vrindavan Ashram/Mahasamadhi: NKB + Ram Dass.
- Karar Ashram: Sri Yukteswar + Hariharananda.
- Sri Ramanasramam: Ramana + Yogananda.
- Ranchi Vidyalaya/YSS campus: Yogananda + Anandamayi.
- Dakshineswar: Ramakrishna + Vivekananda.
- Hanuman Garh/Hanuman Garhi: NKB + Ram Dass.
- 4 Church Lane: NKB + Ram Dass.
- 1894 Kumbh remains an event-zone, not a fixed-site identity.

WIT city/region overlaps must never generate a synthetic parent entity. Varanasi, Prayagraj, Kolkata metro, Vrindavan, Puri, Ranchi, Tiruvannamalai, Serampore, Kainchi, Almora and Nainital aggregation is travel context only.

## R4/R5 dependency queue — preserve but DO NOT send to ABC yet

GEEL findings remain entity-closure dependencies and are not silently dropped: Hotel Evelyn cave-room; K.K. Sah house address; Gethia sanatorium; 4 Church Lane front/bathrooms area; NKB Agra Jagmohan/S-house/clinic/station micro-sites; Mathura station steps conflict; Ram Dass Varanasi hotel; Dharamsala Swarg Ashram/guesthouse; Delhi Health/Finance/AmEx/restaurant/alley/hotel/Soni house; Surat cave; Ramana float-room/tower/bridge/banyan route; Ramakrishna Jayagopal/Lily/Surendra/Adhar/Nanda/Ramchandra/Ganu/Brahmani private-house findings.

ROOD additionally preserves its full unresolved layer: **54 R4 + 25 R5 source records**, plus explicit split-level dependencies including the unnamed 1861 initiation cave, golden-palace terrain, Prayagraj historic bridge/tree, Dashashwamedh hidden cave, Satopanth unnamed cave, hidden Gauri Shankara Pitha, Krishnaram house, Haridwar AOAY hermitage, Bodh Gaya Krishnadayal math and 1936 Regent Hotel.

No R4/R5 item receives guessed coordinates or an automatic A/B/C.

## Other protected existing locations

- Kainchi Dham: Ram Dass person-link enrichment; existing status/lock unchanged.
- NKB Vrindavan Ashram/Mahasamadhi: Ram Dass person-link enrichment; existing lock/status unchanged.
- `KB2-038` Mayavati: Vivekananda link enrichment; any later A/B/C handling waits for Kumaon global-ID/identity policy.
- Bodh Gaya `051`, `061` and `074` were explicitly reconfirmed **C** after their Top-11/delta review; this pass does not reopen them without new qualifying entity/proximity evidence.

No downgrade queue is created.

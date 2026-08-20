# DUPLICATE_PARENT_CANDIDATES — INDIA ZILVER

status: UPDATED_WITH_GEEL_TURQUOISE_AND_NUMERIC_PROXIMITY
branch: agent/indiazilver-cluster-completeness-audit

Hard rule: no existing ID/A-B-C/lock changes. Parent/child microsites are not duplicates. Historic→modern successor relations are not silent same-building merges.

## Confirmed same-site / no duplicate parent ID

- Sri Ramanasramam: `OLD31-13` = `LC-RM-RAMANASRAMAM`; one parent entity, Ramana + Yogananda links retained.
- Dakshineswar temple-garden complex: `OLD31-21` = `LC-RK-DAK-PARENT`; one parent complex, child room/Panchavati/Bel tree/ghat remain separate.
- Cossipore Garden House: `OLD31-22` = `LC-RK-COSSIPORE-HOUSE`; one parent house, final room child; cremation ghat remains physically distinct.
- Banke Bihari Temple: `LC-RD-BANKEBIHARI` = `LC-RK-BANKEBIHARI`; one temple entity, two person links.
- Kainchi Dham: existing parent remains one entity for Neem Karoli Baba + Ram Dass; no duplicate parent ID.
- NKB Vrindavan Ashram/Mahasamadhi complex: existing locked parent remains one entity for Neem Karoli Baba + Ram Dass; no duplicate parent ID.
- Lahiri residence `002` / prior key `VNS-CAND-002`: one exact house entity with Lahiri + Sri Yukteswar links; Babaji tradition link remains epistemically separate.
- Hanuman Garh/Hanuman Garhi Nainital: alias same physical site at entity layer; original labels retained.

## Parent → child relations that MUST remain separate

### Kainchi
Parent: existing Kainchi Dham.
Children: original rock/platform; Maharajji room/kuti; Hanuman temple/courtyard; historic wooden bridge/replacement alignment; Ram Dass 1967 room; river bathing micro-site; 2004 room; Maharajji back room; R4 fire-ceremony zone; R5 cold-hut/village lead.

### Bhumiadhar
Parent: Bhumiadhar temple/ashram.
Children: Baba room/kuti; Ram Dass first-meeting terrace/field zone. Parent may overlap existing Kumaon entity and therefore requires dedup before any new parent ID.

### Hotel Evelyn
Parent: `LC-RD-EVELYN-HOTEL`.
Children: `LC-RD-EVELYN-CAVE` upper/top-floor cave room; `LC-RD-EVELYN-PATIO` balcony/front patio. Room/patio are not duplicate hotel records.

### 4 Church Lane / Red House
Parent: `LC-NKB-4CL-PARENT`.
Children: Maharajji small room; hall; outside veranda; kitchen/meal room; bathrooms/front area. TURQUOISE explicitly requires child preservation.

### NKB Vrindavan Ashram
Parent: existing locked NKB Vrindavan complex.
Children: Maharajji office; temple courtyard/fire-platform detail; Hanuman sanctum; main gate; historic room/veranda/cremation-place records from TURQUOISE. Later memorial is temporal successor, not lifetime-presence evidence.

### Arunachaleswarar Temple
Parent: `OLD31-25` / `LC-RM-ARUN-TEMPLE`.
Children: inner sanctum; Thousand-Pillared Hall; Patala Lingam; float-storage room; unnamed tower; other GEEL temple micro-sites. Virupaksha Cave and Mango Tree Cave are NOT children of this temple; they are separate Arunachala sites.

### Arunachala hill cluster
Distinct entities: Virupaksha Cave; Mango Tree Cave; Skandashram; Satguru Swami Cave; Guhai Namasivaya Cave/Temple; Tortoise Rock/Cave; Seven Springs; summit/Deepam beacon; Ramana Bridge; unresolved banyan/hornet route. Regional clustering never authorizes merge.

### Sri Ramanasramam
Parent: `OLD31-13` / `LC-RM-RAMANASRAMAM`.
Children: Mother's tomb/shrine; Old Hall; kitchen; Mathrubhuteswara inner shrine/Sri Chakra; New Hall; Nirvana Room. Cross-person Yogananda visit enriches parent only.

### Fouzdar Kunj
Parent: building `LC-RK-FOUZDAR`.
Children: upper room; semicircular veranda.

### Nidhivan / Ganga Mata
`LC-RK-NIDHIVAN` is the grove. `LC-RK-GANGAMATA-HUT` is the historic hut footprint. `LC-RK-GANGAMATA-SUCCESSOR` is later Kanpurwali Dharam Shala/Batala Ashrama successor property. Never collapse later structure into Ramakrishna lifetime building.

### Panihati Mani Sen property
Mani Sen house/parlour and Sri Radhakanta family temple are separate parent/child entities.

### Shyampukur
Parent: Shyampukur Bati. Child: Master's large first-floor room.

### Cossipore terminal cluster
Garden House, upstairs final room, and cremation ghat remain distinct physical levels; ghat is not a child room of the house.

## Successor / temporal chains

- Akbarpur NKB historic birth/family site → later 2001 temple: NO same-building merge.
- Neeb Karori historic collapsed cave → current continuity/successor cave: preserve temporal relation.
- Kainchi original wooden bridge → concrete replacement alignment: preserve historic/current distinction.
- NKB Vrindavan cremation place → later memorial/samadhi structures: preserve temporal distinction.
- Ghurni Lahiri original site → rebuilt shrine: no same-building merge.
- Ranchi historic Vidyalaya → current YSS campus: same-campus/institutional-successor relation, not unchanged-building claim.

## Ambiguous merges — keep unresolved

- Sri Yukteswar Serampore ashram / Yogoda Math ↔ Yogananda return-to-guru site.
- Historic Dunagiri initiation landscape ↔ modern Mahavatar Babaji Cave identification.
- Dashashwamedh claimed underground cave exact point ↔ ghat parent zone.
- Delhi unnamed estate ↔ any named Delhi NKB site.
- Bhowanipur disciple-house exact building identity.
- Surendra Nath Mitra Kankurgachi garden house ↔ Ramchandra Datta Yogodyan: explicitly separate until property evidence proves otherwise.
- NKB final-day Agra `S.` house ↔ Jagmohan Sharma residence: do not merge.

## Numeric proximity is not identity

The current hard-coordinate pass confirms:
- `OLD31-28` Rana Mahal Ghat ↔ `019` Kedareshwar Temple/Kedar Ghat: 0.895 km.
- `OLD31-28` Rana Mahal Ghat ↔ `018` Sankatha Devi Temple: 1.285 km.

Both pairs are `DISTINCT_NEARBY_ENTITIES`, not duplicate candidates. No merge or parent-child relation is inferred from distance alone.

Five protected B/C records (`012`, `013`, `026`, `027`, `040`) have old working-pin screening positions within 3 km of Rana Mahal, but those endpoints are not marker-confirmed and therefore remain coordinate dependencies. This screening may justify later review after coordinate closure; it does not authorize a duplicate/merge or an A/B/C change.

No ambiguous relation in this file authorizes a new permanent ID or an A/B/C change.

# INDIA ZILVER — KOMOOT PROXIMITY + HIDDEN-GEMS FREEZE

status: COMPLETE_FREEZE
freeze_date: 2026-08-25
write_branch: `agent/indiazilver-cluster-completeness-audit`
scope: GEO/proximity + corridor geometry only
hard_rule: **NO A+/A/A*/B/C MUTATIONS**

## 1. Scope and invariants

This pass uses Komoot as an additional geometric discovery layer around already selected anchors, sleep-base context and transfer corridors. It does **not** re-grade, remove or choose any A+/A/A*/B/C location.

Applied rules:
- road access and practical road time take precedence over straight-line distance;
- a Komoot publication is route/discovery evidence, never a safety or legal certificate;
- no route is operationally closed unless the physical access/start, walking burden and safety/legal status can be stated responsibly;
- when a public Komoot page does not expose the exact route pin, distance or ascent, the field remains `UNKNOWN`; no geometry is invented;
- protected canon/locks on this branch remain untouched;
- geo labels are descriptive only: `ON_CORRIDOR`, `SMALL_TRANSFER_DETOUR`, `ALTERNATIVE_CORRIDOR_BUNDLE`, `TRUE_SIDE_EXCURSION`, `OFF_CORRIDOR_DROP`.

Central method input read read-only from `agent/india8-cluster-casting`:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md`.

## 2. Executive result

- **3 retained GEO findings** with enough evidence to matter now.
- **1 existing-anchor Komoot exact-name enrichment**.
- **0 protected grades changed**.
- **1 high-leverage corridor finding remains partially unresolved** because public Komoot indexing does not expose a reproducible route profile: Khurpatal.
- **0 new Bodh Gaya/Gaya nature walks retained**: current public Komoot results did not produce a sufficiently strong and operationally verifiable hidden-gem route around the existing A anchors.
- **Corbett hard safety gate retained**: no user-generated Komoot line that enters/crosses the Tiger Reserve may be treated as a legal walk merely because Komoot renders it.

## 3. Retained GEO findings

### ZKOM-01 — Naina Peak / China Peak forest summit walk

**GEO_LABEL:** `TRUE_SIDE_EXCURSION`

- **Komoot name / Highlight:** `View of Nainital and Naina Lake from Naina Peak` (Komoot Highlight). Best publicly exposed short route: `Hiking loop from Nainital`.
- **Komoot walking geometry:** ca. **4.69 km / 1 h 52 min / +350 m / -350 m**, loop.
- **Physical operational start:** **Tanki Band**, identified by current official-tourism operational information as the nearest taxi stand/base access for the Naina Peak trail. Komoot's public route card only says “from Nainital”; exact equality between its hidden start pin and Tanki Band still needs one in-app pin check before navigation.
- **Terrain/difficulty:** steep in places but otherwise straightforward hill trail; forest ascent. Komoot labels the short route as a hiking loop; official tourism describes the trail as well-marked through rhododendron/deodar/cypress/pine forest.
- **Relevant existing anchor:** **Naini Lake-rondwandeling — current selected A+**. Status is referenced only; not changed here.
- **Road distance FROM anchor to start:** **UNKNOWN exact km** in the public sources used; do not substitute the 6 km hiking/town-distance figure or a straight line for road distance.
- **Practical road time FROM Naini Lake to Tanki Band/start:** ca. **15 min one way** under normal local conditions, medium confidence.
- **Extra detour versus corridor:** this is not a frictionless transfer stop. Budget ca. **30–40 min road return burden** if starting/ending around Naini Lake, plus the hike itself.
- **Total visit burden:** ca. **2 h 35 min–3 h 00 min** including road transfer, trail and short summit/view stops.
- **Scenic uniqueness:** **VERY HIGH** — wooded ascent plus a bird’s-eye view over Naini Lake/Nainital and broad Himalayan panorama. This is materially different from simply walking the lakefront.
- **Water/forest/viewpoint tags:** `FOREST`, `VIEWPOINT`, `RIDGE/SUMMIT`, `NAINI_LAKE_VIEW`.
- **Winter fit Dec–Jan:** `CONDITIONAL_GOOD`. Winter is a valid season, but snow/ice can occur at this elevation; trail condition must be checked locally the same morning.
- **Legal status:** normal tourist trekking on the standard Naina Peak trail is explicitly presented by official tourism; no special trek permit was found for this standard approach. Exact Komoot line should still be checked in-app against the operational trail before use.
- **solo_safety:** `PREFER_COMPANY`.
- **Daylight rule:** walk in full daylight; early morning only after civil light. Do **not** start/finish in darkness or near dusk.
- **Wildlife:** official tourism information for this trail/forest area specifically notes **leopard sightings**. No broader species list is imported from generic Uttarakhand wildlife material.
- **Terrain/winter risks:** steep sections, possible snow/ice, forest shade and reduced grip; local weather/fog may remove the summit payoff.
- **Mitigation:** local condition check same morning; footwear with grip; no headphones; companion preferred; driver/taxi pickup plan useful; abandon if icy/fogged-in.
- **Confidence:** `HIGH` for Komoot highlight + route metrics + scenic identity; `MEDIUM` for Tanki-Band-to-hidden-Komoot-start equivalence and road-km field.

### ZKOM-02 — Khurpatal lake / pine-lake corridor lead

**GEO_LABEL:** `ON_CORRIDOR`

- **Komoot searchable discovery seed:** `Khurpatal Lake Viewpoint – Khurpatal lake loop from Bajoon` / `Khurpatal Lake loop from Khurpatal` were surfaced as route/search seeds during the Komoot discovery pass. **Current public Komoot indexing did not expose a reproducible route card with full metrics**, so this record is deliberately not presented as an operationally closed walk.
- **Physical start:** **Khurpatal / Bajoon access on the Nainital–Kaladhungi Road**. Exact Komoot route-start pin remains `OPEN`.
- **Walking distance + time FROM start:** `UNKNOWN — public Komoot route metrics not reproducible in this pass`.
- **Elevation gain:** `UNKNOWN — do not infer from lake elevation/topography`.
- **Relevant existing anchor:** **Naini Lake-rondwandeling — current selected A+**. Status unchanged.
- **Road distance FROM Naini Lake to Khurpatal access:** ca. **10.9–12 km by road**.
- **Practical road time FROM Naini Lake:** ca. **30 min** under normal hill-road conditions.
- **Corridor geometry:** Khurpatal is on **Kaladhungi Road**; the established Nainital → Kaladhungi → Ramnagar/Corbett transfer uses this same axis.
- **Extra detour versus that corridor:** effectively **~0 km through-route detour** if the final parking/trail access stays on/just off Kaladhungi Road. Budget **0–10 min access/parking micro-friction** until the exact Komoot start is verified.
- **Total visit burden:** `OPEN` because the actual Komoot walking profile is not publicly reproducible. A roadside lake look is **not** substituted for the requested walk.
- **Scenic uniqueness:** **HIGH** — official Nainital tourism describes an emerald/blue-green lake framed by pine forest; this is unusually high scenic payoff for almost no transfer-route displacement.
- **Water/forest/viewpoint tags:** `LAKE`, `PINE_FOREST`, `VIEWPOINT`, `CORRIDOR_BYCATCH`.
- **Winter fit Dec–Jan:** `GOOD_WITH_ROAD_CHECK`; the tourist lake/access remains meaningful in winter, but fog, cold and occasional icy hill-road conditions can affect the stop.
- **Legal status:** ordinary road/lake tourist access is supported by official tourism. **Exact informal Komoot trail legality remains UNVERIFIED** until the final line/start is known.
- **solo_safety:** `DAYLIGHT_ONLY` pending exact route closure.
- **Wildlife:** `NO EXACT-TRAIL SPECIFIC VERIFIED WARNING FOUND`; no generic Kumaon predator list is imported into this record.
- **Terrain/remoteness:** exact path surface, cliff exposure and mobile coverage remain `UNKNOWN`.
- **Mitigation:** use only daylight; verify exact start in Komoot app; have driver wait if the final trailhead proves isolated; local same-day confirmation before leaving the road.
- **Confidence:** `HIGH` for lake identity + corridor position + road burden; `LOW/MEDIUM` for the unclosed Komoot walking geometry.
- **ZILVER interpretation:** highest-leverage hidden-gem GEO lead in this pass because the **road detour is near-zero**, but it is **not yet an operational walk recommendation**.

### ZKOM-03 — Ghats of Varanasi riverfront walking loop

**GEO_LABEL:** `ON_CORRIDOR`

- **Komoot name / Highlight:** `Ghats of Varanasi`; exact public route card: `Dashashwamedh Ghat – Ghats of Varanasi loop from Tulsi Manas Temple`.
- **Walking geometry:** ca. **7.15 km / 1 h 52 min / +50 m / -50 m**, easy loop.
- **Physical start:** **Tulsi Manas Temple**, Varanasi.
- **Relevant existing anchor:** **Tulsi Manas Temple — existing protected A** in the Varanasi canon. Status unchanged.
- **Road distance/time FROM anchor to start:** **0 km / 0 min**; the route starts at the anchor itself.
- **Extra detour versus local Varanasi cluster/corridor:** **0 road detour**; burden is the walking loop only.
- **Total visit burden:** ca. **2 h 15 min–2 h 35 min** allowing short river/ghat stops beyond pure Komoot moving time.
- **Scenic uniqueness:** **VERY HIGH, CULTURAL-RIVER rather than wilderness** — continuous Ganges/ghat urban sacred landscape; official district tourism describes the ghats as a spectacular roughly 6 km sweep and especially strong at dawn.
- **Water/forest/viewpoint tags:** `RIVER`, `GHATS`, `DAWN`, `SACRED_URBAN_LANDSCAPE`.
- **Winter fit Dec–Jan:** `VERY_GOOD`; official national tourism identifies Oct–Mar as a strong season for walking the ghats/old city. Winter fog is possible, especially early morning.
- **Legal status:** normal public visitor/pedestrian access; no hiking permit found/expected for the public ghat route. Individual temple/ritual-space rules still apply.
- **solo_safety:** `DAYLIGHT_ONLY` for this operational freeze.
- **Wildlife:** no material wildlife hazard identified for this urban riverfront route.
- **Terrain risks:** wet/slippery ghat steps, crowds, uneven paving, river edge, ritual/cremation zones requiring respectful movement.
- **Mitigation:** dawn after civil light or normal daytime; grippy footwear; avoid blocking ceremonies; do not treat river-edge steps as a uniform promenade in fog/dark.
- **Confidence:** `HIGH`.

## 4. Existing selected anchor — exact Komoot-name enrichment

### ZKOM-E01 — Naini Lake

**GEO_LABEL:** `ON_CORRIDOR`

- **Exact Komoot Highlight:** `Naini Lake`.
- **Physical start:** Nainital lakefront; existing selected loop can be started from the lakefront itself.
- **Existing walking geometry from central selected record:** ca. **3.2 km / 55–75 min FROM Nainital lakefront** for the full lake loop.
- **Komoot elevation gain:** `UNKNOWN` on the public Highlight page; no number is invented.
- **Relevant anchor:** this is the **Naini Lake-rondwandeling — current selected A+** itself. Status unchanged.
- **Road distance/time from anchor to start:** **0 km / 0 min**.
- **Extra detour:** **0**.
- **Total visit burden:** ca. **55–75 min walking**, or roughly **75–95 min** with unhurried lakeside/temple/photo stops.
- **Scenic uniqueness:** lake-edge gravel path, water views, shade/trees and temples; Komoot community tip explicitly highlights these qualities.
- **Winter fit:** `GOOD`, subject to cold/fog and normal local pavement conditions.
- **solo_safety:** `SAFE_SOLO` in normal active daytime/lakefront conditions; use ordinary urban caution and avoid isolated/dark sections late at night.
- **Legal/wildlife:** ordinary public/tourist lakefront access; no material trail-specific wildlife issue identified.
- **Confidence:** `HIGH` for exact Komoot Highlight identity; walking metrics are inherited from the existing central selected record, not reverse-engineered from Komoot.

## 5. Strong leads NOT operationally closed / NOT counted as retained findings

### Sattal / Seven Lakes — existing selected A* / SKIP_FIRST

Official geography strongly supports the attraction: Sattal is a cluster of mountain lakes in dense oak forest, ca. 23 km from Nainital and ca. 12 km from Bhowali; current Uttarakhand tourism specifically describes nature walks, birding and the sequence of lakes including Garud Tal and the freshwater spring Subhash Dhara. This matches the intended forest-lake hidden-gem profile extremely well.

However, this pass did **not** recover a public Komoot India route card that safely closes all of: exact start pin, walking distance, ascent, route line and legal/safety status. Therefore:
- existing A* / SKIP_FIRST status is **untouched**;
- no new ZILVER finding/grade is created;
- exact-best-Komoot walk remains `CLOSURE_DEBT` for in-app/manual route-pin verification.

### Dhokaney Waterfall — existing selected A

Central method already records ca. 1.0–1.2 km / 30–45 min walking from the waterfall access/trailhead. Current public Komoot indexing did not produce a reproducible exact route card plus safety/legal closure. Existing A is **not changed** and no synthetic route metrics are added.

### Nainital nearby Komoot Highlights — suppressed pending geometry

The Nainital Komoot cluster exposes nearby discovery names including:
- `Small Waterfall With Swimming Spot` (Highlight id 7102545),
- `Bridge Over the Brook - Birding Spot` (8158844),
- `Pine Forest Fire Road` (8055520),
- `Winterline Point` (7172643).

Their individual public pages/route metrics were not reliably retrievable in this pass. Because the exact physical start, access, walking profile and legal/wildlife context cannot be closed, none is promoted into a retained finding.

### Beni Bagar / Ramgarh

Search leads were explored, but public Komoot indexing did not yield a unique, reproducible route identity with start pin + route profile that could be distinguished safely from similarly named places/routes. No pseudo-precision and no corridor label is assigned.

### Bodh Gaya / Gaya corridor

No new exceptional Komoot nature walk was retained around the existing A anchors. Search results were dominated by generic travel/collection material or long intercity/cycling content rather than a short high-payoff verified nature walk. `0 findings` is accepted for this region.

## 6. Corbett / Garjiya hard safety gate

The Nainital → Kaladhungi → Ramnagar/Corbett corridor is relevant to ZILVER geometry, but **walking inside Corbett Tiger Reserve is not treated as a normal Komoot hiking opportunity**.

Hard rule from the active central Komoot safety layer:
- walking/trekking inside the Tiger Reserve is strictly prohibited;
- reserve excursions operate under official permit/zone rules and registered-guide requirements;
- official Corbett material confirms material large-wildlife presence including tiger, leopard and wild elephant and restricts park access after sunset.

Therefore any Komoot/user-generated route near Garjiya, Dhikuli, Dhangarhi or Corbett must first be line-checked against the protected-area boundary. A route title or map line alone is never enough. Until that check succeeds, classification is effectively `DO_NOT_WALK` **for any segment entering the reserve**.

## 7. GEO-label roll-up

| item | GEO label | operational state |
|---|---|---|
| Naina Peak / China Peak | `TRUE_SIDE_EXCURSION` | RETAINED; usable with start-pin caveat |
| Khurpatal lake corridor lead | `ON_CORRIDOR` | RETAINED GEO lead; walking profile still open |
| Ghats of Varanasi loop | `ON_CORRIDOR` | RETAINED; closed |
| Naini Lake exact Komoot enrichment | `ON_CORRIDOR` | EXISTING selected anchor enriched |
| Sattal exact best Komoot walk | no new label assigned | existing selection; closure debt |
| Dhokaney exact Komoot match | no new label assigned | existing selection; closure debt |
| Beni Bagar / Ramgarh leads | no label assigned | unresolved identity/geometry |
| any Corbett-reserve trail segment | protected-area hard gate | DO NOT TREAT AS WALK |

No `SMALL_TRANSFER_DETOUR`, `ALTERNATIVE_CORRIDOR_BUNDLE` or `OFF_CORRIDOR_DROP` is asserted merely to fill the taxonomy; those labels require actual verified road geometry.

## 8. Sources checked (2026-08-25 pass)

### Komoot
- Naini Lake Highlight: https://www.komoot.com/highlight/6854726
- Naina Peak Highlight: https://www.komoot.com/highlight/1012195
- Ghats of Varanasi Highlight: https://www.komoot.com/highlight/6020548
- Dashashwamedh Ghat Highlight: https://www.komoot.com/highlight/6854734

### Official / first-party tourism and district sources
- District Nainital — Naina Peak / China Peak: https://nainital.nic.in/tourist-place/naina-peak-or-china-peak/
- Incredible India — Naina Peak: https://www.incredibleindia.gov.in/en/uttarakhand/nainital/naina-peak
- District Nainital — Khurpatal: https://nainital.nic.in/tourist-place/khurpatal/
- District Nainital — Sattal: https://nainital.nic.in/tourist-place/sattal/
- Uttarakhand Tourism — Sattal: https://www.uttarakhandtourism.gov.in/destination/sattal
- District Nainital — Corbett Tiger Reserve: https://nainital.nic.in/corbett-tiger-reserve/
- District Varanasi — tourist attractions / ghats: https://varanasi.nic.in/gallery/places-of-tourist-attraction/
- Incredible India — Varanasi: https://www.incredibleindia.gov.in/en/uttar-pradesh/varanasi

### Operational road/access corroboration
- Safestay/Zostel Nainital Naina Range access description — Tanki Band / ca. 15 min drive from Naini Lake: https://www.safestay.com/venue/zostel-nainital-naina-range/
- Current lodging-distance structured data used only as road-burden corroboration for Naini Lake ↔ Khurpatal (~10.9 km / ~30 min); official district data independently confirms Khurpatal at ~12 km from Nainital and on Kaladhungi Road.

## 9. Freeze conclusion

The strongest new ZILVER contribution is geometric rather than classificatory:
1. **Khurpatal is a near-zero-corridor-displacement lake/forest lead on the Nainital → Kaladhungi → Ramnagar axis**, but its exact Komoot walking line still needs closure before operational use.
2. **Naina Peak is the strongest fully evidenced new walk around the Naini Lake A+ anchor**, but it is a genuine side excursion rather than a transfer bycatch.
3. **Varanasi's Ghats loop is an exact, low-friction Komoot river walk beginning at an existing protected anchor.**
4. Sattal and Dhokaney remain selected as before; this pass adds no grade and refuses to manufacture missing Komoot metrics.
5. Corbett remains a legal/safety exclusion zone for ordinary walking wherever a user-generated route crosses into the reserve.

`A+/A/A*/B/C_CHANGED: NO`

# BODH GAYA / RAJGIR — VERIFIED MAP COORDINATES

Date: 2026-08-29
Status: **CURRENT VERIFIED PIN REGISTRY / REQUIRED BEFORE BODH USER-FACING MAPS**
Branch: `agent/india8-cluster-casting`

## WHY THIS EXISTS
A prior user-facing map rendered **Dungeshwari / Mahakala Caves — Siddhartha's ascetengrotten vóór de verlichting (Gaya district) [A+]** at the wrong location. That false pin visually made the distant Rajgir hot-spring cluster look as though it lay on the way. Mark correctly flagged this as decision-corrupting.

All map-derived conclusions from that bad rendering are invalid. Future Bodh maps must use this registry or fresh verification of equal/higher quality.

## VERIFIED POINTS

### 1. Mahabodhi Temple Complex + Bodhi Tree — verlichtingstempel + Bodhiboom waar Boeddha ontwaakte (Bodh Gaya) [A+] [UNESCO WH]
- canonical coordinate: **24.695280, 84.993890**
- source: UNESCO World Heritage Centre exact property coordinate `N24 41 43.008 E84 59 38.004`.
- confidence: **AUTHORITATIVE / EXACT PROPERTY COORDINATE**.

### 2. Great Buddha Statue / 80-foot Buddha — groot modern zittend Boeddhabeeld (Bodh Gaya) [A]
- canonical coordinate: **24.690468, 84.981794**
- cross-checks: OpenStreetMap/Mapcarta `24.69046,84.9818`; Wikimedia Commons object location `24.690468,84.981794`.
- District Gaya independently confirms the 80-foot statue next to the Mahabodhi area.
- confidence: **CROSS-CHECKED EXACT OBJECT**.

### 3. Sujata Stupa — plek van Sujata's melkrijstgift en de Middenweg (Bakraur, Gaya district) [A+]
- canonical coordinate: **24.697920, 85.003380**
- cross-checks: OpenStreetMap/Mapcarta `24.69792,85.00338`; independent coordinate record `24.697915,85.003319`.
- Bihar Tourism independently confirms exact identity at Bakraur/Senanigrama, east of Bodh Gaya and across the Phalgu River.
- confidence: **CROSS-CHECKED EXACT STUPA**.

### 4. Dungeshwari / Mahakala Caves — Siddhartha's ascetengrotten vóór de verlichting (Manpur/Gaya district) [A+]
- canonical coordinate: **24.736683, 85.047584**
- cross-checks: OpenStreetMap/Mapcarta `24.73668,85.04758`; Wikimedia Commons camera/object location `24.736720,85.047512`; independent GPS listing `24.736683,85.047584`.
- authoritative identity/location checks: Bihar Tourism gives `Dungeshwari Cave Temple, Dungeshwari Hills, Gaya Ji, Bihar 824231`; District Gaya states the caves are about **12 km north-east of Bodh Gaya**.
- confidence: **OFFICIAL IDENTITY + MULTI-SOURCE COORDINATE CROSS-CHECK**.
- important: this is the coordinate that must replace the earlier wrong rendered pin.

### 5. Brahmakund — levende heilige warmwaterbronnen waar Mark eventueel wil baden (Rajgir, Nalanda district) [A* / ONLY_IF_NATURAL_CORRIDOR_BYCATCH / SKIP_FIRST]
- canonical map point: **25.013210, 85.417637**
- identity: Bihar Tourism official Brahmakund destination confirms the hot-water spring at Rajgir/Nalanda.
- exact address cross-check used by current map/review sources: `2C79+6C5, Virayatan Rd, Nimal, Rajgir, Bihar 803116`.
- the Google/Open Location Code `2C79+6C5` recovered in the Rajgir locality resolves to approximately **25.01321,85.41764**.
- coarse government hydrogeology check: Central Ground Water Board lists Rajgir `Brahma Kund` at approximately `25.005,85.426`, consistent with the same hot-spring zone but too coarse for the user-facing exact pin.
- confidence: **OFFICIAL ENTITY + EXACT PLUS-CODE PIN + COARSE GOVERNMENT SANITY CHECK**.
- same-name warning: there is also a `Brahma Kund` locality in Gaya district around `24.846,84.972`; that is NOT Mark's Rajgir hot spring and must never be substituted.

### 6. Vishwa Shanti Stupa + Rajgir Ropeway — witte Peace Pagoda op Ratnagiri Hill met kabelbaan (Rajgir, Nalanda district) [B / ONLY_IF_RAJGIR_ALREADY_HAPPENS]
- canonical coordinate: **25.004520, 85.444530**
- cross-checks: OpenStreetMap/Mapcarta `25.00452,85.44453`; Wikidata `25°0'16.20"N, 85°26'40.52"E`.
- Bihar Tourism independently confirms the Peace Pagoda on Ratnagiri Hill in Rajgir and ropeway access.
- confidence: **OFFICIAL IDENTITY + TWO MATCHING COORDINATE SOURCES**.

### 7. Maya Heritage — gekozen hotel tegenover Wat Thai Buddhagaya (Bodh Gaya) [HOTEL LOCKED_BY_MARK]
- exact identity/address: **Opposite Thai Temple, Mastipur, Bodh Gaya, Bihar 824231**.
- verified current business entity exists and matches phone/address.
- secondary numeric-coordinate listings disagree by a few hundred metres, therefore **do not manually freeze a lat/long from those secondary pages**.
- user-facing maps should use a verified structured business entity reference or verified exact address, NOT a guessed/manual numeric coordinate.
- confidence: **VERIFIED BUSINESS IDENTITY; NUMERIC PIN NOT MANUALLY FROZEN**.

## GEOMETRIC SANITY CHECK
Using the verified coordinates above:
- Mahabodhi -> Dungeshwari straight-line is about **7.1 km**; official road/locality descriptions put the caves about **12 km north-east of Bodh Gaya**. This is coherent.
- Dungeshwari -> Rajgir Brahmakund straight-line is about **48.4 km**; route/travel sources place the caves roughly **66–67 km from Rajgir**. This is a separate outer cluster, not a local continuation.
- Mahabodhi -> Rajgir Brahmakund straight-line is about **55.5 km**; Bihar Tourism's Buddhist-circuit material places Rajgir roughly **70 km from Bodh Gaya** / other road references about 78 km. Coherent with a major road excursion.
- Brahmakund -> Vishwa Shanti Stupa straight-line is about **2.9 km**; these two are indeed one Rajgir microcluster.
- Mahabodhi -> Sujata straight-line is about **1.0 km** across the river; official tourism describes Sujata Stupa directly across the Phalgu River / a short local connection.
- Mahabodhi -> Great Buddha straight-line is about **1.3 km**, coherent with the local walkable sacred-core geography.

## ROUTE CONSEQUENCE
**Brahmakund — heilige warmwaterbronnen (Rajgir) [A* / route-only] is NOT on the route from the Bodh Gaya sacred core to Dungeshwari / Mahakala Caves [A+].**

The verified caves lie only ~12 km north-east of Bodh Gaya. The Rajgir hot-spring cluster is roughly another 50 km straight / ~65+ km road farther north-east/east from the caves. Any map that visually suggests otherwise is wrong.

## MAP-RENDERING RULE FOR THIS CLUSTER
When rendering the map:
- use exact lat/long above for Mahabodhi, Great Buddha, Sujata, Dungeshwari, Brahmakund and Vishwa Shanti;
- use verified business ref/address for Maya Heritage until a single exact business coordinate is independently confirmed;
- do not use name-only geocoding for any of these;
- do not infer road routing from the visual map; route claims require actual road evidence.

## SOURCES USED FOR 2026-08-29 REVERIFY
- UNESCO World Heritage Centre — Mahabodhi property map/coordinates.
- Bihar Tourism — Dungeshwari Mandir; Sujata Stupa; Brahmakund; Vishwa Shanti Stupa; Buddhist Circuit / Buddha circuit brochure.
- District Gaya / NIC — places of interest and Dungeshwari direction/distance.
- OpenStreetMap-derived Mapcarta — Dungeshwari, Sujata, Great Buddha, Vishwa Shanti exact map nodes/ways.
- Wikimedia Commons / Wikidata — Dungeshwari, Great Buddha, Vishwa Shanti coordinate cross-checks.
- Central Ground Water Board — coarse Rajgir Brahma Kund government coordinate sanity check.
- current Google/business-hotel entity and official hotel address — Maya Heritage identity.

END.
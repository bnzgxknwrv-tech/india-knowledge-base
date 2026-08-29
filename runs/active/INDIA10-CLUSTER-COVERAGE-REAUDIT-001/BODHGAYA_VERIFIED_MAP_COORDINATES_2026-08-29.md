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
- cross-checks: OpenStreetMap/Mapcarta `24.69792,85.00338`; Wikimedia object location `24.697915,85.003319`.
- Bihar Tourism independently confirms exact identity at Bakraur/Senanigrama, east of Bodh Gaya and across the Phalgu River.
- confidence: **CROSS-CHECKED EXACT STUPA**.

### 4. Dungeshwari / Mahakala Caves — Siddhartha's ascetengrotten vóór de verlichting (Manpur/Gaya district) [A+]
- canonical coordinate: **24.736683, 85.047584**
- cross-checks: OpenStreetMap/Mapcarta `24.73668,85.04758`; Wikimedia Commons camera/object location `24.736720,85.047512`; independent GPS listing `24.736683,85.047584`.
- authoritative identity/location checks: Bihar Tourism gives `Dungeshwari Cave Temple, Dungeshwari Hills, Gaya Ji, Bihar 824231`; District Gaya states the caves are about **12 km north-east of Bodh Gaya**.
- confidence: **OFFICIAL IDENTITY + MULTI-SOURCE COORDINATE CROSS-CHECK**.
- important: this is the coordinate that must replace the earlier wrong rendered pin.

### 5. Brahmakund — levende heilige warmwaterbronnen waar Mark eventueel wil baden (Rajgir, Nalanda district) [A* / ONLY_IF_NATURAL_CORRIDOR_BYCATCH / SKIP_FIRST]
- exact current map locator: **Plus Code `2C79+6C5`, Virayatan Rd, Nimal, Rajgir, Bihar 803116**.
- recovered full Open Location Code for the Rajgir locality: **`7MQ72C79+6C5`**.
- decoded cell-centre coordinate: **25.013013, 85.418609**.
- identity: Bihar Tourism and District Nalanda official Brahmakund pages confirm the hot-water spring at Rajgir/Nalanda.
- exact locator is independently repeated by current map/review sources as `2C79+6C5, Virayatan Rd, Nimal, Rajgir, Bihar 803116`.
- geographic cross-check: the broader `Brahm Kund` locality is mapped around `25.01558,85.41572`, only a few hundred metres away; this is consistent with the exact hot-spring compound locator but is NOT used as the exact attraction pin.
- confidence: **OFFICIAL ENTITY IDENTITY + EXACT PLUS-CODE LOCATOR + LOCALITY SANITY CHECK**.
- same-name warning: `Brahma Kund` names exist elsewhere; only the Rajgir/Nalanda hot-spring entity and exact `2C79+6C5` locator are valid here.

### 6. Vishwa Shanti Stupa + Rajgir Ropeway — witte Peace Pagoda op Ratnagiri Hill met kabelbaan (Rajgir, Nalanda district) [B / ONLY_IF_RAJGIR_ALREADY_HAPPENS]
- canonical coordinate: **25.004520, 85.444530**
- cross-checks: OpenStreetMap/Mapcarta `25.00452,85.44453`; Wikidata/other geodata agree within the same exact hilltop object; Google map entity is around `25.004696,85.444488`.
- Bihar Tourism independently confirms the Peace Pagoda on Ratnagiri Hill in Rajgir and ropeway access.
- confidence: **OFFICIAL IDENTITY + MULTI-SOURCE COORDINATE CROSS-CHECK**.

### 7. Maya Heritage — gekozen hotel tegenover Wat Thai Buddhagaya (Bodh Gaya) [HOTEL LOCKED_BY_MARK]
- exact identity/address: **Opposite Thai Temple, Mastipur, Bodh Gaya, Bihar 824231**.
- verified current business entity exists and matches phone/address.
- secondary numeric-coordinate listings disagree by a few hundred metres, therefore **do not manually freeze a lat/long from those secondary pages**.
- user-facing maps should use a verified structured business entity reference or verified exact address, NOT a guessed/manual numeric coordinate.
- confidence: **VERIFIED BUSINESS IDENTITY; NUMERIC PIN NOT MANUALLY FROZEN**.

## GEOMETRIC SANITY CHECK
Using the verified coordinates above:
- Mahabodhi -> Dungeshwari straight-line is about **7.1 km**; official road/locality descriptions put the caves about **12 km north-east of Bodh Gaya**. This is coherent.
- Dungeshwari -> Rajgir Brahmakund straight-line is about **48.4 km**. This is a separate remote cluster, not a local continuation.
- Mahabodhi -> Rajgir Brahmakund straight-line is about **55.5 km**; official District Nalanda road information puts **Gaya -> Rajgir at 78 km**, consistent with a major road excursion rather than a local side-stop.
- Brahmakund -> Vishwa Shanti Stupa straight-line is about **2.8 km**; these two are genuinely one Rajgir microcluster.
- Mahabodhi -> Sujata straight-line is about **1.0 km** across the river; official tourism identifies Sujata at Bakraur just east of the Bodh Gaya sacred core.
- Mahabodhi -> Great Buddha straight-line is about **1.3 km**, coherent with local sacred-core geography.

## ROUTE CONSEQUENCE
**Brahmakund — heilige warmwaterbronnen in de verre Rajgir-cluster (Nalanda district) [A* / route-only] is NOT on the route from the Bodh Gaya sacred core to Dungeshwari / Mahakala Caves — Siddhartha's ascetengrotten buiten de verlichtingsstad (Gaya district) [A+].**

The verified caves lie only about 12 km north-east of the Bodh Gaya sacred core by official locality description. The Rajgir hot-spring cluster remains roughly another 48 km away even in a straight line from the verified cave pin. Any map that visually suggests that Mark naturally passes the hot springs on this local cave excursion is wrong.

## MAP-RENDERING RULE FOR THIS CLUSTER
When rendering the map:
- use exact lat/long above for Mahabodhi, Great Buddha, Sujata, Dungeshwari and Vishwa Shanti;
- for Brahmakund use the exact Plus Code/address locator `2C79+6C5, Virayatan Rd, Nimal, Rajgir, Bihar 803116` or its decoded full-code centre above;
- use verified business ref/address for Maya Heritage until a single exact business coordinate is independently confirmed;
- do not use name-only geocoding for any of these;
- do not infer road routing from the visual map; route claims require actual road evidence.

## SOURCES USED FOR 2026-08-29 REVERIFY
- UNESCO World Heritage Centre — Mahabodhi property map/coordinates.
- Bihar Tourism — Dungeshwari Mandir; Sujata Stupa; Brahmakund; Vishwa Shanti Stupa.
- District Gaya / NIC — Dungeshwari identity and direction/distance.
- District Nalanda / NIC — Brahmakund identity and road context.
- OpenStreetMap-derived Mapcarta — Dungeshwari, Sujata, Great Buddha, Vishwa Shanti and broader Brahm Kund locality.
- Wikimedia Commons / Wikidata — Dungeshwari, Sujata, Great Buddha and Vishwa Shanti coordinate cross-checks.
- exact current Plus Code/address sources for Rajgir Brahmakund.
- current structured business-hotel entity and official/current hotel address — Maya Heritage identity.

END.
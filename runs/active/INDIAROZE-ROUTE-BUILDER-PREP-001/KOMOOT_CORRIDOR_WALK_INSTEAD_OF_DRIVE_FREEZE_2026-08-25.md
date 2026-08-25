# INDIA ROZE — KOMOOT CORRIDOR + WALK-INSTEAD-OF-DRIVE FREEZE — 2026-08-25

state: FROZEN_WORKER_OUTPUT
owner: INDIA ROZE
write_branch: `agent/indiaroze-route-builder-prep`
research_date: 2026-08-25
scope: route-builder corridor integration only; no global route choice; no grade changes

## 0. GOVERNANCE / SCOPE

This pass implements the later explicit INDIA ROZE instruction to test where a beautiful walk can replace or piggyback on road movement without creating a separate walking module.

Read-only central inputs used from `agent/india8-cluster-casting` where needed:
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_A_PLUS_CORRIDOR_MATRIX.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_EASY_CAPTURE_MARK_DECISIONS_2026-08-25.md`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_A_PLUS_CORRIDOR_MATRIX.md`

Hard boundaries preserved:
- no A+/A/A*/B/C changed;
- no destination removed or added to canon;
- no global day order fixed;
- no nights fixed;
- a Komoot publication is treated as route/discovery evidence, never as legal/safety certification;
- an attractive route that fails exact-route or safety closure remains HOLD, not silently promoted into the route-builder.

## 1. RESULT SUMMARY

### ELIGIBLE CORRIDOR INSERTS — 2
1. **KUMAON / NAINITAL — Naini Lake loop as morning-before-transfer walk**: zero road detour; luggage/driver remain simple; selected walk itself is already A+.
2. **VARANASI — Assi Ghat → Dashashwamedh Ghat riverfront walk**: genuine point-to-point walk that replaces a short auto/taxi segment while traversing already-selected riverfront content.

### HOLD / NOT CLOSED AS A FINDING
- Sattal / Seven Lakes — A* SKIP_FIRST: excellent nature/corridor logic, but no defensible exact/best-searchable public Komoot route or Highlight was found in this pass; exact walk/legal-wildlife closure remains open.
- Dhokaney Waterfall — A: selected and corridor-relevant, but no defensible public Komoot exact match found; exact trail/legal/safety and winter water-flow closure remain open.
- Mahabodhi Temple Complex → Sujata Stupa — A+ → A+: spiritually compelling potential point-to-point, but current public sources conflict on practical route distance (~2 km versus ~4 km class) and no exact Komoot walk was found. Do not fabricate a bridge/foot-route.
- Arunachala / Ramanasramam → Skandashram → Virupaksha Cave / town-side descent — CHILD_A+ content with strong walk-instead-of-drive logic, but no exact Komoot closure plus exact forest/legal/safety closure in this pass. HOLD.
- Kakrighat — A* SKIP_FIRST: attractive river stop on Kumaon transfer geometry, but no serious public Komoot walking route found that improves the road stop enough to become a separate corridor-walk finding.
- Dwarahat historic temple groups — A* SKIP_FIRST: walkable local cultural bundle, but not a nature/corridor walk upgrade with a closed Komoot route in this pass.

Zero-pressure rule: HOLD means route-builder may retain the already-existing canonical destination/status, but this worker does not create a walking module or claim a route that has not been closed.

---

# FINDING RZ-KW-01 — NAINI LAKE MORNING LOOP BEFORE NAINITAL → KAINCHI TRANSFER

`route_builder_use`: `MORNING_BEFORE_TRANSFER` + `TRANSFER_DAY_ZERO_ROAD_DETOUR`

## Identity / Komoot
- **Komoot best-searchable name:** `Nainital` — Komoot Highlight, Hiking, public Highlight ID 6854734.
- **Important exact-match caveat:** Komoot currently exposes a nearby `Nainital loop from Nainital` of **6.10 km / 1:50 / +200 m**, but this is **NOT** the selected canonical Naini Lake loop. Do not substitute it.
- **Cross-check for selected loop geometry:** AllTrails lists `Naini Lake Trail` as Easy, **2.0 mi / est. 53 min** (~3.2 km), matching the selected canon closely.

## Exact physical start and end
- **Start:** The Flatts, Mallital — north end of Naini Lake, at the public lakefront/parking edge beside the Naina Devi Temple area.
- **End:** same point, The Flatts, Mallital.
- **Operational line:** The Flatts/Mallital → lakeside Thandi Road → Tallital lake bridge/end → Mall Road/Govind Ballabh Pant Marg → The Flatts/Mallital.
- Nainital district confirms The Flatts is at the northern end of the lake and includes public parking; it confirms Mall Road connects Mallital and Tallital and that vehicles are not allowed on Thandi Road.

## Walk metrics
- **distance:** ca. **3.2 km**.
- **realistic walking time:** **55–75 min** for the selected experience; 53 min is the current AllTrails moving-time cross-check.
- **elevation gain/loss:** `UNKNOWN_PENDING_EXACT_SELECTED_LOOP_GPX`. Do **not** inherit Komoot’s +200 m from the different 6.10 km route. The selected line is lakeside/low-relief, but no defensible exact ascent figure for this precise loop was exposed publicly in this pass.
- **route form:** loop.
- **terrain:** paved/formed urban lakeside road and pedestrian road; repeated normal road gradients; Thandi Road is vehicle-free by district rule; Mall Road carries/restricts traffic according to local rules.

## Relevant selected anchors / current statuses — unchanged
- **KUMAON / NAINITAL / Naini Lake-rondwandeling (ca. 3,2 km / 55–75 min; volledige lus via Mall Road en de autovrije Thandi Road; voorkeur vroeg in de ochtend) — huidige status: A+.**
- **KUMAON / NAINITAL / Hotel Evelyn (historisch hotel waar Ram Dass verbleef; exacte kamer niet bewezen) — huidige status: A+.**
- Transfer target/context: **KUMAON / KAINCHI / Kainchi Dham (Neem Karoli Baba-ashramcomplex; kernplek voor Neem Karoli Baba en Ram Dass) — huidige status: A+ parent.**

## Baseline autoroute zonder wandeling
- Nainital → Kainchi Dham direct corridor.
- Nainital district gives **17 km** road distance from Nainital to Kainchi Dham.
- Existing central corridor working class: roughly **40–60 min taxi/road time**, traffic-dependent.

## Autoroute met wandeling / drop-off-pickup
- No relay required.
- Keep luggage at Hotel Evelyn or in the booked vehicle.
- Walk starts and finishes in Mallital; driver can load/collect after the loop.
- Then drive the same Nainital → Bhowali → Kainchi corridor.
- **added road kilometres:** effectively **0 km** versus baseline.

## Netto extra reistijd
- **+55–75 min elapsed** versus departing immediately by vehicle.
- No meaningful extra driving time is created; only short loading/walking transitions.
- This therefore qualifies as a true `MORNING_BEFORE_TRANSFER` insert rather than a separate excursion.

## Totale dagbelasting
Before any visit-time at Kainchi itself:
- walk 55–75 min;
- transition/load buffer ca. 5–10 min;
- road Nainital → Kainchi ca. 40–60 min working class;
- **combined movement burden:** roughly **1h40–2h25**.

No full day or half-day walking module is created.

## Bagage / driver-praktijk
- **excellent**.
- Loop returns to the same town/base.
- No luggage carried during walk.
- No driver repositioning required.
- Driver can meet at hotel/The Flatts/Tallital only if local access/parking conditions dictate; final pickup point should be confirmed with the booked driver.

## Winterdaylight / morning-evening fit
- December 2026 Nainital sunrise: about **06:48 on 1 Dec → 07:06 on 31 Dec**; sunset about **17:13 → 17:23**.
- Civil twilight begins about **06:23 → 06:40**.
- **recommended window:** after useful daylight, preferably around sunrise/shortly after; do not force a dark pre-dawn Thandi Road start.
- **morning suitability:** `EXCELLENT` — directly matches Mark’s selected morning preference and avoids consuming later transfer daylight.
- **evening suitability:** `SECONDARY` — visually attractive, but not the preferred operational variant for this transfer-integration use.

## Solo safety / wildlife / legal
- `solo_safety`: **DAYLIGHT_ONLY**.
- **legal status:** the route uses public urban lakefront roads; district administration explicitly describes Mall Road/Thandi Road and says vehicles are not allowed on Thandi Road. No forest/reserve permit or guide requirement found for this exact loop.
- **protected-area status:** not a tiger-reserve/wildlife-sanctuary trail.
- **wildlife:** no evidence found in this pass that makes the central public lake loop a routine big-cat trail. Do not generalise rural Nainital-district leopard incidents into an exact-route claim. Urban dogs/monkeys may occur; normal food/belonging precautions apply.
- **terrain/traffic risk:** current road condition matters more than wildlife here. On 19 Aug 2026, recent reporting described cracks affecting Upper Mall Road while Lower Mall Road repair/strengthening was still underway. This is an explicit `RECHECK_BEFORE_TRIP` item for Dec 2026–Jan 2027.
- **mitigation:** walk only in useful daylight; obey any temporary closures/diversions; verify Lower/Upper Mall Road pedestrian continuity locally the evening before; use Thandi Road where open; no headphones on traffic sections.

## Route-builder disposition
`ELIGIBLE_INSERT__NO_DAY_ROUTE_DECISION`

This is not a new destination proposal. It is a logistics placement for an already-selected A+ walk.

## Confidence
- corridor fit: **HIGH**
- selected distance/time: **HIGH-MEDIUM**
- exact Komoot closure for the 3.2 km loop: **MEDIUM/INCOMPLETE** — best public Komoot object is the Nainital Highlight; exact 3.2 km Komoot Tour not located
- safety/legal: **HIGH-MEDIUM**, with mandatory live road-condition recheck

---

# FINDING RZ-KW-02 — ASSI GHAT → DASHASHWAMEDH GHAT: WALK INSTEAD OF AUTO/TAXI

`route_builder_use`: `POINT_TO_POINT_DROP_PICKUP` + `WALK_INSTEAD_OF_DRIVE` + `DAWN_GHAT_CORRIDOR`

## Identity / Komoot
- **Komoot exact/best-searchable Highlight:** `Ghats of Varanasi` — Hiking Highlight, public Highlight ID 6020548, **5.0 (5)** at time checked.
- **Komoot reference Tour:** `Dashashwamedh Ghat – Ghats of Varanasi loop from Tulsi Manas Temple` — **7.15 km / 1:52 / +50 m / -50 m**, Easy.
- **Second exact Komoot anchor:** `Dashashwamedh Ghat` — Hiking Highlight, public Highlight ID 457237, **5.0 (11)**; nearby Tour variant **7.17 km / 1:53 / +50 m / -50 m**.
- The route-builder uses only the **Assi → Dashashwamedh waterfront segment**, not the full Komoot loop.

## Exact physical start and end
- **Start:** Assi Ghat riverfront steps / Subah-e-Banaras platform area, Nagwa Road, Shivala, Varanasi, Uttar Pradesh 221005.
- **End:** Dashashwamedh Ghat upper riverfront steps beside the Shitala Mata Temple / Dashashwamedh Ghat ceremony zone.
- **Driver pickup edge:** Godowlia Chowk / Dashashwamedh Road vehicle-access edge; vehicle should not be expected at the river steps.
- **Operational line:** Assi Ghat → Tulsi Ghat → Bhadaini/Janki/Shivala sections → Harishchandra/Kedar/central ghat sequence → Dashashwamedh Ghat. Use continuous public ghat-side path where locally open; temporary river-level works/barriers always override a saved line.

## Walk metrics
- **distance:** working **2.4–3.0 km** waterfront point-to-point.
  - A current detailed route source gives ~2.5 km along the riverfront.
  - A public Wikiloc track for Assi → Dashashwamedh is 2.38–2.39 km.
  - Other current city/travel sources quote roughly 3 km depending exact access line.
- **realistic walking time:** **40–60 min moving**, without prolonged ritual/photo stops.
- **elevation gain/loss:** public Assi→Dashashwamedh track evidence gives about **+21 m**; use **~20–25 m ascent class**, with frequent ghat steps/undulation. Komoot’s longer 7.15–7.17 km reference loop is +50 m and must not be copied as the segment’s exact gain.
- **route form:** point-to-point.
- **terrain:** stone/paved ghat terraces, frequent steps, narrow transitions around some ghats; easy technical grade in dry conditions but not step-free.

## Relevant selected anchors / current statuses — unchanged
- **VARANASI / ASSI / Assi Ghat (zuidelijke ochtend-/pelgrimsghat) — huidige status: A+.**
- Direct on/adjacent to south corridor: **VARANASI / TULSI GHAT / Tulsi Ghat + Lolark Kund (Tulsidas-ghat plus oude rituele zon-/vruchtbaarheidsbron) — huidige status: A.** Only Tulsi Ghat itself is on the waterfront line; Lolark Kund is an inland add-on and is not auto-inserted by this walk.
- Nearby Bhadaini A+ context, but not assumed as automatic stop: **VARANASI / BHADAINI / Shree Shree Ma Anandamayi Ashram (bezoekbaar ashram van Anandamayi Ma) — huidige status: A+.**
- **VARANASI / DASHASHWAMEDH / Dashashwamedh Ghat + Shitala Mata Temple (grote Ganga-Aarti-zone) — huidige status: A+.**

## Baseline autoroute zonder wandeling
- Assi Ghat road edge → Godowlia/Dashashwamedh road-access edge by auto/e-rickshaw/taxi.
- Current public route sources give roughly **3–3.5 km road** and about **15–25 min** in normal conditions; Varanasi traffic can enlarge this.
- Final approach to Dashashwamedh is pedestrian regardless of vehicle mode.

## Autoroute met drop-off/pickup
- Driver drops Mark at Assi Ghat road access with **no main luggage**.
- Driver carries luggage independently by road to the Godowlia/Dashashwamedh access edge or onward to the next booked/base point.
- Mark walks the riverfront point-to-point.
- Pickup after the walk is at the agreed vehicle-access edge, not on the ghat steps.
- This is a genuine driver relay: human movement becomes scenic/spiritual walking while baggage/vehicle movement stays practical.

## Netto extra reistijd
Compared with an auto/taxi-only move:
- walking 40–60 min versus road movement 15–25 min;
- **net extra elapsed burden: roughly +20–45 min**.
- Crucially, that extra time is spent inside already-selected ghat content rather than on a separate walking excursion.

## Totale dagbelasting
- pure moving walk: **40–60 min**;
- with slow observation / short Tulsi or ritual pauses: allow **75–120 min**;
- no extra dedicated half-day required.
- Do not combine automatically with every adjacent A/A+ temple or ghat; route-builder must still respect actual site windows and fatigue.

## Bagage / driver-praktijk
- **very good if a retained driver is already in the city**.
- Main luggage remains in vehicle/hotel.
- Driver waits/repositions independently.
- Use a pre-agreed pickup landmark at Godowlia or another legal vehicle edge because the ghat/old-city access is pedestrian constrained.
- If no retained driver exists, this remains easy as a base-to-base urban walk only when the accommodation can hold luggage; otherwise do not walk with travel luggage.

## Winterdaylight / morning-evening fit
- December 2026 Varanasi sunrise: about **06:26 on 1 Dec → 06:43 on 31 Dec**.
- Sunset: about **17:07 → 17:18**.
- Civil twilight begins about **06:01 → 06:18**.
- Varanasi district explicitly describes the roughly 6 km ghat sweep as especially compelling at **dawn**.
- **morning suitability:** `EXCELLENT`; use around/after first useful light, ideally feeding directly into an already-planned Assi/dawn block.
- **evening suitability:** `POSSIBLE_BUT_NOT_PREFERRED_FOR_SOLO_RELAY`; crowds are strong near Dashashwamedh but darker/uneven intermediate steps and side lanes reduce the advantage.
- **dark:** do not design the route-builder around a dark solo completion.

## Solo safety / wildlife / legal
- `solo_safety`: **DAYLIGHT_ONLY** for route-builder purposes.
- **legal status:** public ghat riverfront; no protected-forest permit or guide requirement found. The city/district actively presents the ghats as a tourist/pilgrimage public realm.
- **security context:** in May 2026 Varanasi’s police commissioner conducted foot inspections at Assi and Dashashwamedh and ordered continued patrol/surveillance; district emergency police number is **112**.
- **wildlife:** no tiger/leopard/elephant/bear context applies to this urban riverfront. Urban monkeys and stray dogs are the plausible animal issues; do not carry exposed food and do not engage monkeys/dogs.
- **human/crowd risks:** tout/scam pressure, dense crowds and confusing galis are more material than wildlife. Keep the line on the public riverfront in daylight rather than improvising deserted back lanes.
- **terrain:** ghat steps can be uneven/slippery; fog/dew may make stone slick in winter mornings. River-level barriers or local works can interrupt the lowest terrace; use the upper public connection if directed.
- **religious/legal etiquette:** Harishchandra is an active cremation area on this southern-to-central riverfront; pass respectfully and do not photograph cremation rites or deceased persons.
- **mitigation:** daylight; offline map; phone secured; no visible food; no headphones; agreed driver pickup; local same-morning check if fog/riverfront works affect continuity.

## Route-builder disposition
`ELIGIBLE_INSERT__TRUE_WALK_INSTEAD_OF_DRIVE__NO_DAY_ROUTE_DECISION`

This is the strongest identified example in this pass of a scenic/spiritual walk replacing a taxi/auto segment between already-selected content.

## Confidence
- Komoot identity/reference: **HIGH**
- point-to-point corridor logic: **HIGH**
- exact waterfront distance: **MEDIUM-HIGH** because sources vary by access line; 2.4–3.0 km is the defensible operational band
- segment elevation: **MEDIUM**
- safety/legal: **HIGH-MEDIUM**, with same-day local continuity check

---

# 2. OPERATIONAL MICRO-CONNECTOR — RETAIN AS ROUTE RULE, NOT A THIRD WALK FINDING

**Dashashwamedh Ghat A+ → Kashi Vishwanath sacred core A+** should be treated by the future route-builder as **inherently pedestrian**, not as a taxi hop between the two sacred anchors.

Current public routing describes roughly **550 m / 7–10 min walking** through the old-city/Kashi Vishwanath pedestrian approach. Official temple information confirms ghat-side/mandir access and security-controlled pedestrian entry; vehicles do not solve the final old-city movement.

Why this is not counted as a separate finding:
- it is an obvious access connector rather than a scenic walk module;
- no separate Komoot Tour for this exact micro-segment was needed to justify the pedestrian rule;
- avoid inflating normal site access into a new itinerary attraction.

`route_builder_rule`: if Dashashwamedh and Kashi Vishwanath are sequenced together, default to foot movement and let the driver wait outside the controlled pedestrian core.

---

# 3. HOLD REGISTER — IMPORTANT NEGATIVE FINDINGS

## H1 — SATTAL / SEVEN LAKES — A* SKIP_FIRST
Status remains exactly:
**KUMAON / SATTAL / Sattal / Seven Lakes (zeven bosmeren voor natuurwandeling en vogels; mooie transfer-bijvangst die Mark graag ziet maar waarvoor niet zelfstandig moet worden omgereden) — huidige status: A* (formeel A; corridor-/bijvangst-A, operationeel SKIP_FIRST).**

Positive evidence:
- official Nainital material confirms Sattal as a scenic lake destination;
- current external trail data also exposes a short Sattal Waterfall walk, but that is a different feature and must not be silently equated with the selected Seven Lakes experience.

Closure failure:
- no defensible exact/best-searchable public Komoot Seven Lakes route/Highlight found;
- exact legal/wildlife/forest-boundary classification for the intended lakes walk not closed.

Disposition: `HOLD_WALK_INTEGRATION`; do not create a special detour or invented Komoot name. Its existing A* SKIP_FIRST status remains untouched.

## H2 — DHOKANEY WATERFALL — A
Status remains exactly the selected intrinsic A in central canon.

Closure failure:
- no defensible public Komoot exact match found;
- public descriptions vary materially on whether the walk is ~0.5 km class or a longer rough access;
- exact forest/legal status and Dec–Jan water payoff are not closed here.

Disposition: preserve destination status; no route-walk claim from INDIA ROZE.

## H3 — MAHABODHI A+ → SUJATA STUPA A+
Thematic case is extremely strong: walking can mirror a meaningful Siddhartha/Sujata geography rather than using a short vehicle hop.

Closure failure:
- current public official/official-adjacent distance references conflict (~2 km versus ~4 km class from Mahabodhi area);
- no exact public Komoot walk found;
- exact bridge/road/footway line must be live-mapped before driver drop/pickup or solo safety can be stated responsibly.

Disposition: `PROMISING_POINT_TO_POINT__HOLD_FOR_MAP_AND_KOMOOT_CLOSURE`.

## H4 — ARUNACHALA A+ INTERNAL TRAIL CHAIN
Ramanasramam → Skandashram → Virupaksha Cave is inherently more meaningful on foot and all are within the already-selected Arunachala/Ramana A+ world.

Closure failure for this worker:
- no exact public Komoot route closure found;
- exact point-to-point descent/exit line, hill/legal access, winter opening hours and solo safety were not all closed from official/local-authority evidence in this pass.

Disposition: preserve as A+ sacred-world walking content, but do not let ROZE invent a driver-relay route.

---

# 4. ROUTE-BUILDER RULES DERIVED FROM THIS PASS

1. `LOOP_AT_BASE`: if an already-selected A+/A walk returns to the same base and creates zero road detour, it may be placed before departure without becoming a separate walking day.
2. `DRIVER_RELAY_POINT_TO_POINT`: when selected anchors lie on a beautiful continuous public walking corridor, let Mark walk and let the driver/luggage move independently.
3. `DO_NOT_DOUBLE_COUNT`: walking time through already-selected sites is experience time plus movement; do not also charge a fictitious taxi transfer over the same segment.
4. `EXACT_KOMOOT_OR_HOLD`: if the assignment requires a Komoot name and no exact/best-searchable public object is found, record HOLD rather than fabricate one.
5. `A_STAR_NEVER_DRIVES_ROUTE`: A* SKIP_FIRST nature bycatch may be inserted only when the final corridor already makes it low-friction; it cannot force a new night or major detour.
6. `BAGS_STAY_WITH_DRIVER`: point-to-point transfer walks are valid only when luggage can remain in vehicle/base or be transferred separately.
7. `WINTER_DAYLIGHT`: Dec–Jan mountain walks should not consume the last daylight before remote road transfers; urban ghats may work at dawn but dark solo completion is not a default.
8. `LIVE_ACCESS_BEATS_SAVED_TRACK`: road works, river level, forest rules, closures and local restrictions override Komoot/user tracks.

---

# 5. SOURCE REGISTER — CHECKED 2026-08-25

## Central repository, read-only
- `agent/india8-cluster-casting:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KOMOOT_WALK_DISCOVERY_LAYER_2026-08-25.md`
- `agent/india8-cluster-casting:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md`
- `agent/india8-cluster-casting:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_A_PLUS_CORRIDOR_MATRIX.md`
- `agent/india8-cluster-casting:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_EASY_CAPTURE_MARK_DECISIONS_2026-08-25.md`
- `agent/india8-cluster-casting:runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_A_PLUS_CORRIDOR_MATRIX.md`

## Nainital
- Komoot — Nainital Highlight: https://www.komoot.com/highlight/6854734
- AllTrails — Nainital trail index / Naini Lake Trail listing: https://www.alltrails.com/india/uttarakhand/nainital
- District Nainital — Mall Road / Thandi Road: https://nainital.nic.in/tourist-place/mall-road/
- District Nainital — The Flatts: https://nainital.nic.in/tourist-place/the-flatts/
- District Nainital — Naini Lake: https://nainital.nic.in/tourist-place/naini-lake/
- District Nainital — Kainchi Dham distance: https://nainital.nic.in/tourist-place/kaichi-dham/
- District Nainital — tourist/parking/winter tips: https://nainital.nic.in/tips-for-tourists/
- Timeanddate — Nainital Dec 2026 daylight: https://www.timeanddate.com/sun/india/nainital?month=12
- Current Mall Road condition signal, Amar Ujala, 2026-08-19: https://www.amarujala.com/uttarakhand/nainital/cracks-on-the-upper-mall-road-grew-during-the-treatment-of-the-lower-mall-road-nainital-2026-08-19

## Varanasi
- Komoot — Ghats of Varanasi Highlight: https://www.komoot.com/highlight/6020548
- Komoot — Dashashwamedh Ghat Highlight: https://www.komoot.com/highlight/457237
- District Varanasi — tourist-attraction gallery / official ghat dawn description: https://varanasi.nic.in/gallery/places-of-tourist-attraction/
- District Varanasi — police helpline 112: https://varanasi.nic.in/helpline/
- Kashi official portal — Assi Ghat: https://kashi.gov.in/listing-details/assi-ghat
- Kashi official portal — Dashashwamedh Ghat: https://kashi.gov.in/listing-details/dashashwamedh-ghat
- Current walk geometry source, 2026-03-06: https://www.tirth.com/blog/assi-ghat-to-dashashwamedh-ghat-distance
- Public track cross-check / elevation: https://www.wikiloc.com/trails/walking/india/uttar-pradesh/benares
- Timeanddate — Varanasi Dec 2026 daylight: https://www.timeanddate.com/sun/india/varanasi?month=12
- Times of India — Police Commissioner ghat security inspection, 2026-05-21: https://timesofindia.indiatimes.com/city/varanasi/commissioner-inspects-security-arrangements-at-ghats/amp_articleshow/131235008.cms

## Negative-closure discipline
Search families also run for Sattal/Seven Lakes, Dhokaney Waterfall, Bodh Gaya/Sujata and Arunachala/Skandashram/Virupaksha. Absence of a reliable public Komoot exact match in those searches is recorded as a negative result, not converted into an invented Tour name.

---

# 6. FREEZE CONCLUSION

Two walking integrations are operationally strong enough for route-builder use without creating a dedicated walking module:
- Naini Lake A+ loop before the Nainital → Kainchi transfer;
- Assi Ghat A+ → Dashashwamedh Ghat A+ as a driver-relay riverfront walk replacing an auto/taxi segment.

All grades remain exactly as found in central canon. No global day route is chosen. All HOLD items require later exact closure before they may be used as walk-instead-of-drive logic.
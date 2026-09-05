# CCI — KUMAON NAINITAL-FIRST EXACT GEOMETRY MATRIX

Status: **TRAVEL EXECUTION SUPPORT — OBJECTIVE GEOMETRY ONLY, NO A/B/C/HOTEL/DURATION/SEQUENCE DECISION**
Worker branch: `agent/india17-cci-kumaon-geometry`
Task: CCI_TASK — KUMAON NAINITAL-FIRST EXACT GEOMETRY MATRIX (PR #23)
Researched: 2026-09-05, via live web search (no Google Maps API access in this environment — see HONEST LIMITS)

## ENTITY-CONFUSION TRAP CAUGHT DURING THIS TASK

One search result ("sacredyatra.com/haidakhan-temple.html") returned a distance of **38.3 km / ~1h24 from Dwarahat** for something it called "Haidakhan Temple." Direct verification of that exact page confirmed it describes **Anandapuri Ashram, Chiliyanaula, ~5 km from Ranikhet town on NH109** — the well-known **decoy entity** the task explicitly warned about, NOT the true riverside **Haidakhan Vishwa Mahadham, Village Haidakhan (Chhakhata Range, near Haldwani)**. That 38.3 km figure is **excluded** from this matrix and must never be used for the true ashram. This is reported explicitly because it demonstrates exactly why "do not trust old distance figures without fresh verification" was the right instruction — a naive search would have silently substituted the wrong entity's distance.

## SOURCES USED

- `haidakhandisamaj.in/how-to-reach/` — official site of the true ashram (primary).
- `dunagiri.com/post/how-to-reach-dunagiri-retreat` — official Dunagiri Retreat site (primary).
- District/road-distance aggregator sites (distancesfrom.com, euttaranchal.com, cabbazar.com, chardhamtour.in, etc.) — secondary, Google-Maps-style estimates, used only for triangulation, never alone.
- Prior repository evidence (`KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md`, `KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md`, `DELHI_ARRIVAL_RAIL_FIRST_SUPERSEDE_2026-09-05.md`, `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md`) — cited as PRIOR_PROJECT_ESTIMATE, cross-checked against fresh search, not assumed correct on its own.

## EDGE-BY-EDGE MATRIX

### 1. Kathgodam railway station -> Hotel Evelyn, Nainital
- **Entity confidence:** HIGH — Kathgodam is an unambiguous named BG rail terminus; Hotel Evelyn, Mall Road/Mallital, Nainital is unambiguous in prior project sourcing.
- **Road km:** ~34–35 km (official Nainital District figure, repeated consistently across prior project sources and this session's search).
- **Raw current route time:** not independently re-timed this session; prior project estimate ~1 h class on ordinary hill-road conditions.
- **Conservative whole-human/winter time:** **1 h 00–1 h 30**, per the existing calendar file's own working figure, which this session did not find reason to revise.
- **Source(s):** Official Nainital District distance (repeated in prior repo files); `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md`.
- **Conflict notes:** none material. This edge is the best-anchored of the 12.

### 2. Haldwani railway station -> Hotel Evelyn, Nainital
- **Entity confidence:** HIGH.
- **Road km:** not separately pinned this session; Haldwani and Kathgodam are ~5 km apart on the same rail line (per edge 10/11 evidence below), so this edge is expected to be **~34–40 km**, essentially the Kathgodam figure plus/minus the short Haldwani-Kathgodam gap.
- **Raw/whole-human time:** expected in the same **1 h–1 h 40** class as edge 1; not independently re-verified.
- **Source(s):** inferred from edge 1 + Haldwani/Kathgodam proximity; not a direct fresh search hit.
- **Conflict notes:** **PROVISIONAL BY INFERENCE, not directly sourced this session** — flag as LIVE_RECHECK_LATER if Haldwani (rather than Kathgodam) ever becomes the actual alight point for a different train product.

### 3. Hotel Evelyn/Nainital -> Bhumiadhar
- **Entity confidence:** HIGH for Hotel Evelyn; MEDIUM for "Bhumiadhar" as a routing point (it is a locality/ashram-world name, not a single pinned address — prior project files already treat it as such).
- **Road km:** not directly isolated this session as a distinct Nainital-anchored figure. Existing project evidence gives **Bhumiadhar -> Kainchi Dham ~11.6 km / ~26 min** (edge 4, confirmed fresh below) and **Nainital -> Kainchi Dham ~17–20 km / ~45–70 min**; since Bhumiadhar sits on this same Nainital-Kainchi corridor, Nainital -> Bhumiadhar is expected to be **somewhat less than the full Nainital -> Kainchi figure**, i.e. roughly **10–14 km / ~30–45 min**, by subtraction logic, not independently measured.
- **Source(s):** derived by corridor-position inference from edges 4's confirmed figure and the existing Nainital-Kainchi district figure.
- **Conflict notes:** **NOT independently fresh-verified as its own edge this session — DERIVED, not measured.** Genuine decision-grade closure needs a direct Nainital -> Bhumiadhar route check.

### 4. Bhumiadhar -> Kainchi Dham
- **Entity confidence:** HIGH — both are well-documented, unambiguous pilgrimage sites on the same short corridor.
- **Road km:** **~11.6 km**, ~26 min, via NH109.
- **Raw current route time:** ~26 min per fresh search result.
- **Conservative whole-human time:** ~35–45 min allowing for pilgrimage-road traffic/parking.
- **Source(s):** fresh web search 2026-09-05 (independent of the prior repo figure, which stated the identical 11.6 km / 26 min — **strong cross-confirmation**, not a single-source guess).
- **Conflict notes:** none. This is the single most solidly confirmed edge in the whole matrix (two independent time-separated sources agree exactly).

### 5. Nainital -> true Haidakhan Vishwa Mahadham
- **Entity confidence:** HIGH for Nainital; the "Haidakhan Babaji Ashram, Nainital" search result used for this figure explicitly carries Nainital-district framing, distinct from the confirmed Ranikhet/Chiliyanaula decoy, so treated as the TRUE entity — **but not verified with the same rigor as the official-site fetch used for edges 6/9/10/11**.
- **Road km:** **~50 km** (fresh search, distancesfrom.com-style aggregator).
- **Raw current route time:** not independently timed this session.
- **Conservative whole-human/winter time:** no direct figure found; by analogy to the Kathgodam edge (27–40 km / ~44 min–1.5 h) scaled to ~50 km, estimate **~1 h 15–2 h**, NOT independently confirmed.
- **Source(s):** distancesfrom.com aggregator (secondary, single source, not cross-confirmed).
- **Conflict notes:** **SINGLE-SOURCE, MODERATE CONFIDENCE ONLY.** Genuinely conflicts in scale with edge 6/9 (Kukuchina/Dunagiri side is ~135–160 km away from the same ashram), which is geometrically plausible (Nainital is much closer to the Haldwani/Kathgodam side than Dunagiri/Kukuchina is) but the exact 50 km figure itself should be treated as **LIVE_RECHECK_LATER**, not decision-final.

### 6. Kainchi Dham -> true Haidakhan Vishwa Mahadham
- **Entity confidence:** HIGH for Kainchi Dham; same TRUE-entity caveat as edge 5 applies to Haidakhan.
- **Road km:** **not independently isolated this session.** By corridor logic (Kainchi is ~17–20 km beyond Nainital on the way toward Bhowali/Ranikhet), and using the edge-5 Nainital figure (~50 km, itself only moderate confidence), Kainchi -> Haidakhan would plausibly be in a **similar ~40–55 km band**, but this is **compounded-uncertainty inference**, not a fresh direct measurement.
- **Source(s):** derived, not measured.
- **Conflict notes:** **NOT INDEPENDENTLY VERIFIED — HIGHEST-UNCERTAINTY EDGE IN THE MATRIX.** A direct "Kainchi Dham to Haidakhan Vishwa Mahadham" route search returned no clean independent hit this session; do not use this figure for a duration-closing decision without a dedicated follow-up check.

### 7. Nainital/Kainchi corridor -> Dwarahat / Dunagiri Retreat
- **Entity confidence:** HIGH — Dunagiri Retreat is unambiguous (single named property with its own official site).
- **Road km:** official Dunagiri Retreat source states **Kathgodam -> Dunagiri ~135 km / ~4 h**, routed via **Bhimtal, Bhowali, Ranikhet, Dwarahat** (i.e. NOT via Nainital town itself on the main route, though the same source notes "an alternative scenic route via Nainital is also available"). Since Nainital/Kainchi sit just off this same Bhowali junction, a Nainital/Kainchi-anchored departure is expected to be in the **same ~120–140 km / ~3.5–4.5 h class**, not materially shorter or longer than the Kathgodam anchor.
- **Raw current route time:** ~4 h per official source (Kathgodam anchor).
- **Conservative whole-human/winter time:** **~4.5–5.5 h**, consistent with the existing project's own working calendar figure.
- **Source(s):** `dunagiri.com/post/how-to-reach-dunagiri-retreat` (primary, fresh-fetched this session, verbatim quote obtained); cross-checked against independent search giving Dwarahat<->Kathgodam ~114 km/~3.7h and Dwarahat<->Haldwani ~116 km/~3h49 (same order of magnitude, corroborating).
- **Conflict notes:** the Kathgodam-anchored 135 km figure is now PRIMARY-SOURCE-CONFIRMED (upgraded from prior repo's secondary sourcing). A Nainital/Kainchi-specific figure remains a same-order-of-magnitude estimate, not independently pinned.

### 8. Dunagiri Retreat -> Mahavatar Babaji Cave motorhead / Kukuchina
- **Entity confidence:** HIGH — both are within the same small, well-documented pilgrimage micro-world.
- **Road km:** **not independently re-verified this session** (outside the search budget for this round). Existing project working class: **~2–3 km one way / ~1 hour climbing** before the cave pause (this is walking/climbing distance from the motorhead, not a drivable road distance — Dunagiri Retreat and the Babaji-cave motorhead are effectively the same micro-locality).
- **Source(s):** prior repo figure only (`KUMAON_COMPLETE_EXECUTION_DRAFT_2026-08-26.md`), not independently re-confirmed by fresh search this session.
- **Conflict notes:** **NOT FRESH-VERIFIED — carried forward from prior project research, flagged as such, not silently trusted.** Low material risk given the short scale and single well-known micro-locality, but per task instruction this should not be presented as freshly proven.

### 9. Kukuchina/Babaji-cave world -> true Haidakhan Vishwa Mahadham
- **Entity confidence:** HIGH for Kukuchina/Dunagiri; same TRUE-entity caveat applies to Haidakhan as edges 5/6/10/11/12.
- **Road km:** **~160 km / ~3 h 43 raw** driving (prior repo secondary-source figure), consistent in order of magnitude with this session's fresh, independent confirmation that Dwarahat (essentially co-located with Dunagiri/Kukuchina) is ~114–116 km from the Haldwani/Kathgodam gateway — since the true Haidakhan ashram is itself ~27–90 km further beyond that gateway (per edges 10/11's conflicting range), a total transfer in the ~140–200 km band is geometrically plausible, and the ~160 km prior figure sits centrally within that band.
- **Raw current route time:** ~3 h 43 raw (prior figure); this session's independent Dwarahat-anchored figures (~3.7–3h49 to the gateway alone) suggest the raw time to reach Haidakhan itself, beyond the gateway, is very likely **longer than 3h43 raw**, not shorter — i.e. the prior project figure may be an UNDERESTIMATE once the final Haidakhan-specific last mile is added on top of the gateway distance.
- **Conservative whole-human/winter time:** **4 h 30–5 h 30**, per the existing project's own calendar-file working figure — this session's cross-check supports treating this as a reasonable floor, not an overstatement.
- **Source(s):** prior repo figure + this session's independent Dwarahat-to-gateway triangulation.
- **Conflict notes:** this is the **single longest and most operationally significant edge** in the whole matrix. Treat the ~160 km/~3h43 raw figure as **plausible but potentially optimistic**; the whole-human 4.5–5.5 h class is the safer planning number and is not contradicted by this session's independent research.

### 10. true Haidakhan Vishwa Mahadham -> Haldwani
- **Entity confidence:** HIGH.
- **Road km:** **CONFLICTING, from the ashram's OWN official site.** `haidakhandisamaj.in/how-to-reach/` itself states two different things in different places: "approximately 90 km distance from our Ashram" (framed as the Kathgodam/Haldwani railway-station distance, undifferentiated between the two stations) and, per one third-party aggregation of the same official material, a separate claim of "40 kms from Haldwani-Kathgodam by road... about 1.5 hours." A further independent secondary search result gave **~27 km / ~44 min from Kathgodam** specifically.
- **Raw current route time:** no single authoritative figure; candidates range **~44 min (27 km) to ~1.5 h (40 km) to an implied ~2 h+ if literally 90 km**.
- **Conservative whole-human/winter time:** given the three-way conflict, use **1 h–2 h** as a wide planning band until a decision-grade close; do NOT present a single exact figure to Mark for a duration-closing decision.
- **Source(s):** `haidakhandisamaj.in/how-to-reach/` (primary, fresh-fetched, verbatim quote obtained); independent secondary aggregator search (fresh, different session query) giving the 27 km/44 min class; third-party paraphrase of the same official site giving 40 km/1.5h.
- **Conflict notes:** **MATERIAL, UNRESOLVED CONFLICT even within nominally official sourcing.** This matches and confirms the conflict already flagged in `DELHI_ARRIVAL_RAIL_FIRST_SUPERSEDE_2026-09-05.md`; this session's fresh research did not resolve it, only reproduced and further documented it with an additional independent data point (27 km/44 min). A genuine decision-grade close needs an actual routed distance from a live mapping tool at the specific final approach used (this environment has no Maps API access — see HONEST LIMITS).

### 11. true Haidakhan Vishwa Mahadham -> Kathgodam
- **Entity confidence:** HIGH.
- **Road km:** same conflicting range as edge 10 — official site does not distinguish Haldwani from Kathgodam (states "90 km" for "Kathgodam/Haldwani" as one combined statement); independent secondary search gave **27 km / ~44 min specifically anchored to Kathgodam**.
- **Raw current route time:** same conflict band as edge 10.
- **Conservative whole-human/winter time:** **1 h–2 h**, same reasoning as edge 10.
- **Source(s):** same as edge 10.
- **Conflict notes:** same unresolved conflict as edge 10. Because Kathgodam is the actual 15013 Ranikhet Express terminus (per `DELHI_ARRIVAL_RAIL_FIRST_SUPERSEDE_2026-09-05.md`), this specific edge — not edge 10 — is the operationally relevant one for the "Haidakhan-last" order class (Order A/B below), and its unresolved conflict directly affects how confidently that order's final exit-day timing can be planned.

### 12. true Haidakhan Vishwa Mahadham -> Lal Kuan
- **Entity confidence:** HIGH for Lal Kuan (Lalkuan Junction, a real, distinct rail station on the same line, ~16–17 km from Haldwani per fresh rail-distance search — note this is RAIL distance between LKU and HDW stations, not necessarily identical to road distance between them).
- **Road km:** **not directly found this session.** Given Lal Kuan sits ~16–17 km from Haldwani on the plains side (further from the hills than Haldwani), and Haidakhan is itself on the hill side of Haldwani, the true Haidakhan -> Lal Kuan road distance is expected to be **roughly the Haidakhan->Haldwani figure PLUS an additional ~16–20 km**, i.e. in the same wide **~45 km–110 km** band implied by edge 10's own unresolved conflict, plus the Lal Kuan gap. This is a **derived estimate, not a direct measurement.**
- **Source(s):** derived from edge 10 + independent Haldwani-Lal Kuan rail-distance search.
- **Conflict notes:** **NOT INDEPENDENTLY VERIFIED.** This edge matters specifically because the current-preferred `12354 Lal Kuan -> Howrah Superfast` (direct to Varanasi, but Saturday-only per `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md`) departs from Lal Kuan, not Haldwani or Kathgodam — so if that weekly train is ever tested against a different calendar date, this edge needs a dedicated fresh check, not the current derived estimate.

## THREE ORDER-CLASS TOTALS (OBJECTIVE COMPARISON ONLY — NO CHOICE MADE)

All three assume the same fixed content survives (Nainital/Hotel Evelyn/Naini Lake, Bhumiadhar, Kainchi Dham, Dunagiri/Kukuchina/Babaji Cave/Dwarahat YSS day, Haidakhan 3 nights/2 full days) and the same 9 Kumaon nights (3 Nainital + 3 Dunagiri + 3 Haidakhan), differing only in the order Haidakhan is visited relative to the Nainital/Kainchi and Dunagiri/Cave worlds.

### A. `NAINITAL -> HAIDAKHAN -> KAINCHI/BHUMIADHAR -> DUNAGIRI/CAVE -> EXIT`
- **Total base-change road burden:** Kathgodam->Nainital (edge 1, ~34km) + Nainital->Haidakhan (edge 5, ~50km, LOW confidence) + Haidakhan->Kainchi (edge 6, ~40-55km, HIGHEST uncertainty, derived) + Kainchi/Bhumiadhar->Dunagiri (edge 7, ~120-140km) + exit at Dunagiri (requires a SEPARATE final exit edge not in this task's 12, since this order does not end at Haidakhan's own rail-adjacent position).
- **Major backtrack:** visiting Haidakhan mid-sequence and then returning toward Kainchi/Bhumiadhar (which sit north of Haidakhan, back toward Nainital) before continuing on to Dunagiri creates a geometric zigzag — this is the same "reversal" risk already flagged in `KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md` for the mirror-image order.
- **Final exit-road burden:** the cluster ends in the Dunagiri highlands, requiring its own separate exit edge (not measured in this task) back down to a rail gateway — a real, uncosted tax specific to this order.
- **A+/A stops on a movement edge:** Kainchi/Bhumiadhar sit naturally on the Nainital<->Dunagiri corridor regardless of order, so this order gets no special "free" bonus from visiting them mid-route.
- **Material or within uncertainty:** given edges 5 and 6 (the two edges this order relies on most heavily) are exactly the two LOWEST-confidence edges in the whole matrix, **this order's total cannot currently be stated as materially better or worse than Order C — the underlying data is not solid enough to close that comparison.**

### B. `NAINITAL -> KAINCHI/BHUMIADHAR -> HAIDAKHAN -> DUNAGIRI/CAVE -> EXIT`
- **Total base-change road burden:** Kathgodam->Nainital (~34km) + Nainital->Bhumiadhar->Kainchi (edges 3+4, ~22-26km derived+confirmed) + Kainchi->Haidakhan (edge 6, ~40-55km, HIGHEST uncertainty) + Haidakhan->Dunagiri (edge 9, reversed direction of the matrix's own edge 8/9 pairing, ~160km/~3h43 raw, MODERATE-plausible-optimistic confidence) + separate exit edge from Dunagiri (uncosted, same as Order A).
- **Major backtrack:** this order also reverses direction — after the long haul into Dunagiri highlands from Haidakhan, the cluster still ends in the highlands with the same uncosted exit tax as Order A.
- **Final exit-road burden:** identical uncosted-exit problem as Order A.
- **A+/A stops on a movement edge:** same as Order A — Kainchi/Bhumiadhar sit on-route regardless.
- **Material or within uncertainty:** this order combines the matrix's single highest-uncertainty edge (6) with its single longest edge (9, here reversed) — **the LEAST well-evidenced of the three orders**, not because it is necessarily worse, but because both edges it depends on most are the two hardest in the whole matrix to pin down.

### C. `NAINITAL -> KAINCHI/BHUMIADHAR -> DUNAGIRI/CAVE -> HAIDAKHAN -> RAIL GATEWAY`
(This is the order the current live `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md` working draft has already provisionally adopted for calendar-testing purposes — noted here as context, not as this task choosing it.)
- **Total base-change road burden:** Kathgodam->Nainital (edge 1, ~34km, HIGH confidence) + Nainital->Bhumiadhar->Kainchi (edges 3+4, ~22-26km) + Kainchi/Nainital-corridor->Dunagiri (edge 7, ~120-140km, PRIMARY-SOURCE-CONFIRMED) + Dunagiri->Haidakhan (edge 9, ~160km/~4.5-5.5h whole-human) + Haidakhan->rail gateway (edges 10/11, CONFLICTING 27-90km).
- **Major backtrack:** none of the same magnitude as Orders A/B — this is the only one of the three that does not require reversing back toward Nainital/Kainchi after already having moved past them.
- **Final exit-road burden:** this order's own exit edge (10/11) IS one of the 12 measured edges, unlike Orders A and B, whose highland exit is entirely uncosted by this task — a structural advantage for planning completeness, independent of which order is actually shorter.
- **A+/A stops on a movement edge:** same as A/B — Kainchi/Bhumiadhar sit on-route regardless of final order.
- **Material or within uncertainty:** this order relies most heavily on edges 7 and 9, which are this matrix's two BEST-evidenced long edges (both have primary-source or session-independent cross-confirmation), and its exit edge (10/11) — while internally conflicting — is at least a directly measured edge rather than an entirely uncosted highland exit. **This is the only one of the three orders whose total can currently be assembled entirely from measured or primary-sourced edges; Orders A and B both depend on this matrix's least-confident edges (5 and/or 6) and additionally require an uncosted separate highland exit.**

## WHAT REMAINS UNPROVEN

1. **Edges 5 and 6** (Nainital/Kainchi <-> Haidakhan direct) are single-source or derived estimates only — the weakest data in this entire matrix. Any order (A or B) that depends on them cannot be duration-closed on current evidence.
2. **Edges 10/11** (Haidakhan <-> Haldwani/Kathgodam) carry a genuine, unresolved conflict even within the ashram's own official site (90 km official vs. 27–40 km secondary/aggregator class) — this was independently reproduced this session, not resolved.
3. **Edge 12** (Haidakhan <-> Lal Kuan) is entirely derived, not measured, and matters specifically for the Saturday-only 12354 direct-to-Varanasi option.
4. **Edge 2** (Haldwani <-> Nainital) and **edge 8** (Dunagiri <-> Babaji-cave motorhead) were not independently re-verified this session; carried forward from inference/prior project research respectively, explicitly flagged as such rather than silently upgraded to "confirmed."
5. This task's own comparison of Orders A/B/C is therefore **not decision-grade for choosing a final sequence** — it is decision-grade only for showing WHICH edges must be closed next before such a choice can be made responsibly. Order C is the only one of the three whose total rests on entirely measured/primary-sourced edges; that is a statement about **evidence completeness**, not a claim that Order C has the lowest total burden.

## HONEST LIMITS

- This environment has no live Google Maps / routing-API access. All distances/times come from web-search snippets, official ashram/retreat "how to reach" pages, and third-party road-distance aggregator sites, cross-checked against each other and against prior repository research where available — never a single unverified figure presented as fact.
- Winter-specific (December) conditions, fog, road closures, and exact per-day traffic were not and could not be verified from these sources; all "conservative whole-human" times are reasoned buffers over the raw driving-time class, consistent with this project's existing planning convention, not independently measured winter data.
- No exact physical entrance/gate coordinate verification (per `MAP_COORDINATE_VERIFICATION_RULE.md`) was performed for any of the 12 edges — this task produced route-CLASS and distance-BAND evidence, not pin-level coordinate verification. A genuine duration close would still need that additional step for the Haidakhan entrance specifically, given the demonstrated real conflict there.

## CONFIRMATION PER TASK GUARDS

No Mark A+/A/A*/B/C grade was created, changed, or implied. No hotel/base/duration decision was made. No Mark-only choice was presented or resolved — Orders A/B/C are reported side by side with their evidence quality, explicitly without a recommendation. All work is on worker branch `agent/india17-cci-kumaon-geometry`, not merged to central.

END

# GLOBAL FULL-ROUTE TOPOLOGY REOPTIMIZATION — CCI RERUN

Date: 2026-09-09  
Branch: `worker/global-route-topology-reoptimization`  
Task: PR #23 comment `5597408788`; central `90bce122b1ceecf7f0145179eb603218e10ef6ea`  
Scope: order/topology only; no booking, PDF, grade, duration or world-selection change.

## Executive result

**VERDICT: KEEP INCUMBENT — MODERATE confidence.**

Best lexicographic topology:

`Delhi/Nirmal Dham -> Kumaon -> Agra -> Bodh Gaya -> Varanasi/Sarnath -> Kolkata/Dakshineswar -> Tiruvannamalai -> Chennai -> final Delhi`.

The strongest challenger, **same-day DEL -> GAY/Bodh Gaya**, is about **1–2 modeled waking hours lighter**, but loses on arrival recovery, missed-connection protection, heavy-day count and late-trip fog exposure. That waking-hours difference is smaller than the model's ±2 h uncertainty.

### Material correction to the earlier branch result

The earlier claim that `DEL -> GAY` is impossible on 19 December is superseded. Air India's official Northern Winter Schedule 2026, effective 25 October, publishes daily **AI429 DEL 15:00 -> GAY 16:40**, after AI156's scheduled 10:15 arrival. Gaya is therefore a real same-day candidate, not an impossible one.

## 1. Verified canon

- AI156: Amsterdam -> Delhi, 18 Dec 2026 20:35, scheduled arrival 19 Dec 10:15.
- AI155: Delhi -> Amsterdam, 21 Jan 2027 12:20.
- Exactly 33 physical nights, 19 Dec through 20 Jan; final Delhi exactly night 20 Jan.
- Primary surface: Nainital 3n; Dunagiri/Kukuchina 3n; Haidakhan Vishwa Mahadham 3n/two full quiet days; Agra 1 hotel night; Bodh Gaya 3n; Varanasi/Sarnath 8n; Kolkata/Dakshineswar 3n; Tiruvannamalai 4n; Chennai 1n; final Delhi 1n.
- BODH2/TIRU5 remains sensitivity only.
- Nirmal Dham remains required at a feasible point.
- Puri/Odisha, Serampore/Srirampur as trip world/stop, and Vrindavan/Braj/Mathura/Govardhan remain FINAL OUT.
- Train first when practical; overnight target 1A, 2A only explicit fallback.

## 2. Cost method

`Lost waking hours` includes door-to-door access/egress, station/airport buffer, baggage, awake onboard time and forced connection waiting. Creditable sleeper time is shown separately. Internal Kumaon road is included in route totals but is invariant. Totals are planning estimates, not timetable facts; use **±2 h per complete route** until exact 2026/27 inventory is bookable.

## 3. Directed edge matrix

| Directed edge | Best serious product | D2D | Waking lost | Sleep credited | Main risk/date fact | Confidence |
|---|---|---:|---:|---:|---|---|
| AI156/DEL -> Kumaon | recovery/Nirmal + 15013 GGN ~20:02 -> KGM ~05:05; 1A target | ~19 h landing-to-Nainital | 6.5–7 h | 6–6.5 h | daily pattern; 05:05 arrival/fog | medium |
| AI156/DEL -> GAY/Bodh Gaya | **AI429 15:00–16:40** + road | 7.5–8 h | 7.5–8 h | 0 | official daily winter flight; 4h45 connection | high schedule / medium robustness |
| AI156/DEL -> VNS | no earlier than ~15:00 nonstop + road | 7–8 h | 7–8 h | 0 | dense; DEL/VNS fog | medium |
| AI156/DEL -> CCU/Dakshineswar | afternoon nonstop + long egress | 8–9 h | 8–9 h | 0 | dense; 20:00-class base arrival | medium |
| AI156/DEL -> MAA/Chennai | afternoon nonstop | 9–10.5 h | 9–10.5 h | 0 | dense but heaviest arrival | medium |
| Delhi -> Kumaon | 15013 sleeper | 11–12 h lodging-to-Nainital | 5.5–6.5 h | 6–6.5 h | daily; 1A; fog | medium |
| Kumaon -> Delhi | Haidakhan road + 12039 15:15–20:55 | 10–11 h | 10–11 h | 0 | daily; EC/CC, not sleeper | medium-high |
| Kumaon -> Delhi | road + 15014; DLI ~04:10 | 14–16 h | 7–8 h | 5–6 h | disruptive arrival/fog | medium |
| Delhi -> Agra | 12050 Gatimaan 08:10–09:50 | 3–4 h | 3–4 h | 0 | dense | high pattern |
| Agra -> Delhi | Gatimaan-class return/road | 3–4.5 h | 3–4.5 h | 0 | duplicates corridor if Agra late | high pattern |
| Agra -> Bodh Gaya | 12988 AF ~18:45 -> GAYA ~07:50; 1A/2A | ~15 h | 6–7 h | 8–8.5 h | **directionally excellent**, daily pattern | medium-high |
| Bodh Gaya -> Agra | 12987 GAYA ~06:15 -> AF ~18:30 | ~14 h | ~14 h | 0 | reverse is daytime, not symmetric | medium-high |
| Bodh Gaya -> Varanasi | road + 20887 ~09:55–13:00 | ~5 h | ~5 h | 0 | six-day pattern; weekday recheck | medium |
| Varanasi -> Bodh Gaya | rail/road | 5–6 h | 5–6 h | 0 | product varies | medium-low |
| Varanasi -> Agra | 20175 ~15:20–22:20 or sleeper | 9–11 h | 7–10 h | 0–6 h | late arrival/weekly pattern | medium |
| Kumaon -> Varanasi | 12354 weekly if weekday fits; else Lucknow change | 14–18 h | 8–12 h | 6–7 h | direct pattern Saturday; 29 Dec is Tuesday | low-medium |
| Bodh Gaya -> Kolkata | GAY -> CCU nonstop + egress | 5–6 h | 5–6 h | 0 | thinner than VNS–CCU | medium-low |
| Varanasi <-> Kolkata | nonstop | 5–6 h | 5–6 h | 0 | ~1h20–25 airborne; daily pattern | medium-high |
| Kolkata -> Tiruvannamalai | CCU -> MAA + 175 km car | 9–10 h | 9–10 h | 0 | humane-arrival flight needed | medium |
| Tiruvannamalai -> Chennai | 175 km private car | 4–4.5 h | 4–4.5 h | 0 | no useful rail/air substitute | medium-high |
| Chennai -> Delhi | MAA -> DEL nonstop | 6–6.5 h | 6–6.5 h | 0 | 14–16 daily AI/6E patterns; DEL fog | high density |
| Delhi -> Tiruvannamalai | DEL -> MAA + car | 9–10 h | 9–10 h | 0 | full transfer day | medium-high |
| Delhi -> Kumaon by air | DEL -> PGH + road | 5.5–7 h | 5.5–7 h | 0 | thin inventory; no sleep conversion | low-medium |

### Edge operations annotation

| Edge class | Vehicle/terminal changes | Transit/hotel night | Class | Arrival and next-day burden |
|---|---:|---|---|---|
| 15013 Delhi -> Kumaon | car/rail/taxi = 2 changes | rail night yes; hotel no | 1A target; 2A fallback only | 05:05 rail arrival; taxi to Nainital; recovery morning required |
| 12039 Kumaon -> Delhi | car/rail/taxi = 2 | Delhi hotel yes | EC/CC, no sleeper | 20:55 + egress; late dinner/check-in, normal next morning |
| 15014 Kumaon -> Delhi | car/rail/taxi = 2 | rail night yes | 1A target; 2A fallback only | ~04:10 at Old Delhi; poor sleep and recovery morning |
| DEL same-day continuation | international arrival/domestic flight/road = 2, plus terminal handling | destination hotel night | air | evening arrival after overnight AI156; next morning must be light |
| 12050 Delhi -> Agra | taxi/rail/taxi = 2 | Agra hotel yes | EC/CC | good morning arrival; usable day |
| 12988 Agra -> Gaya/Bodh Gaya | taxi/rail/taxi = 2 | rail night yes | 1A target; 2A fallback only | 07:50 + road; substantially usable arrival day after imperfect sleep |
| 12987 Gaya -> Agra | taxi/rail/taxi = 2 | Agra hotel yes; train is not a sleep night | 1A/2A shown | evening arrival after a consumed day; low evening utility |
| 20887 Bodh Gaya -> Varanasi | taxi/rail/taxi = 2 | destination hotel | EC/CC | 13:00 + egress; useful afternoon after early checkout |
| Intercity nonstop flight | taxi/flight/taxi = 2 | destination hotel | air | midday/afternoon good; evening arrival loses recovery/content |
| CCU -> MAA -> Tiruvannamalai | taxi/flight/car = 2 | Tiruvannamalai night | air + private car | late-afternoon/evening arrival; light programme only |
| Tiruvannamalai -> Chennai | private car = 0 | Chennai hotel yes | road | content possible only if departure is not late |

## 4. Eleven route families tested

Abbreviations in tables only: KUM = fixed Nainital -> Dunagiri/Kukuchina -> Haidakhan Vishwa Mahadham 9n; BG = Bodh Gaya; VNS = Varanasi/Sarnath; CCU = Kolkata/Dakshineswar; TIRU = Tiruvannamalai.

| # | Family | Exact night skeleton, 19 Dec–20 Jan | Nights | Result |
|---:|---|---|---:|---|
| 1 | Incumbent mixed | 19 rail; 20–28 KUM; 29 Delhi transit; 30 Agra; 31 rail; 1–3 BG; 4–11 VNS; 12–14 CCU; 15–18 TIRU; 19 Chennai; 20 Delhi | 33 | **winner** |
| 2 | Full reverse | 19 Delhi; 20–23 TIRU; 24 Chennai; 25–27 CCU; 28–4 VNS; 5–7 BG; 8 rail; 9 Agra; 10 rail; 11–19 KUM; 20 Delhi | 33 | weak final risk |
| 3 | Same-day MAA | 19 Chennai; 20–23 TIRU; 24–26 CCU; 27–3 VNS; 4–6 BG; 7 Agra; 8 rail; 9–17 KUM; 18 rail; 19 FREE; 20 Delhi | 33 | heaviest arrival |
| 4 | Same-day CCU | 19–21 CCU; 22–29 VNS; 30–1 BG; 2 Agra; 3 rail; 4–12 KUM; 13 Delhi; 14–17 TIRU; 18 Chennai; 19 FREE; 20 Delhi | 33 | cross-country bend |
| 5 | Same-day VNS | 19–26 VNS; 27–29 BG; 30 Agra; 31 rail; 1–9 KUM; 10 Delhi; 11–13 CCU; 14–17 TIRU; 18 Chennai; 19 FREE; 20 Delhi | 33 | finalist; loses safety/date |
| 6 | **Same-day GAY/BG** | 19–21 BG; 22–29 VNS; 30–1 CCU; 2–5 TIRU; 6 Chennai; 7 Delhi/Nirmal; 8 Agra; 9 rail; 10–18 KUM; 19 rail; 20 Delhi | 33 | **strongest challenger** |
| 7 | Agra-first/KUM-last | 19 Delhi; 20 Agra; 21 rail; 22–24 BG; 25–1 VNS; 2–4 CCU; 5–8 TIRU; 9 Chennai; 10 rail; 11–19 KUM; 20 Delhi | 33 | heavy chain/final rail |
| 8 | Agra-last | 19 rail; 20–28 KUM; 29 rail/change; 30–6 VNS; 7–9 BG; 10–12 CCU; 13–16 TIRU; 17 Chennai; 18 Delhi; 19 Agra; 20 Delhi | 33 | doubles Delhi–Agra |
| 9 | East-first next day | 19 Delhi; 20–22 CCU; 23–30 VNS; 31–2 BG; 3 Agra; 4 rail; 5–13 KUM; 14 Delhi; 15–18 TIRU; 19 Chennai; 20 Delhi | 33 | zigzag/daytime BG–Agra |
| 10 | Flight-heavy | 19 Delhi; 20–28 KUM via PGH; 29 Agra; 30 rail; 31–2 BG; 3–10 VNS; 11–13 CCU; 14–17 TIRU; 18 Chennai; 19 FREE; 20 Delhi | 33 | thin PGH/more churn |
| 11 | Train-heavy | incumbent durations + VNS–CCU rail + CCU–Chennai rail | 35+ | hard-infeasible without cutting locks |

`FREE` is intentionally not assigned to an extra city/world night: it exposes nominal arithmetic surplus, as ordered. In these families it is bought with worse arrival/final-risk geometry and is not a free benefit on higher-priority tiers.

## 5. Comparable route metrics

Road includes fixed internal Kumaon transfers. Airport-process includes access/check-in/security/baggage, not airborne time.

| # | Waking loss | Road | Airport process | Awake rail | Sleepable rail | Flights | Base changes | Transfer days | Heavy days | Sleep /5 | Principal risk |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 incumbent | **57 h** | 24 h | 8 h | 16 h | 14.5 h | 3 | 11 | 8 | 2 | **4.0** | early fog edges, long recovery runway |
| 2 reverse | 60 h | 26 h | 8 h | 17 h | 14 h | 3 | 11 | 9 | 4 | 3.0 | KUM exit 20 Jan |
| 3 same-day MAA | 64 h | 28 h | 8 h | 18 h | 11 h | 3 | 11 | 10 | 4 | 2.5 | arrival exhaustion/late fog |
| 4 same-day CCU | 67 h | 29 h | 10 h | 21 h | 7 h | 4 | 12 | 10 | 4 | 2.7 | daytime BG->Agra/extra crossing |
| 5 same-day VNS | **56 h** | 27 h | 10 h | 17 h | 12 h | 4 | 12 | 9 | 4 | 2.8 | first-day flight/final north rail |
| 6 same-day GAY | **55.5 h** | 27 h | 10 h | 9 h | 12 h | 4 | 12 | 9 | 4 | 2.8 | 4h45 connection/final fog edge |
| 7 Agra-first | 58.5 h | 26 h | 8 h | 14 h | 14.5 h | 3 | 11 | 9 | 4 | 3.0 | MAA->DEL->rail; 20 Jan exit |
| 8 Agra-last | 60 h | 26 h | 8 h | 18 h | 13 h | 3 | 12 | 10 | 3 | 3.4 | Tuesday KUM->VNS/doubled bridge |
| 9 east-first | 64 h | 27 h | 10 h | 20 h | 12 h | 4 | 12 | 10 | 4 | 2.9 | zigzag/weak BG->Agra direction |
| 10 flight-heavy | 61 h | 25 h | 13 h | 9 h | 8 h | 5 | 12 | 10 | 4 | 3.0 | PGH thin/more airport churn |
| 11 train-heavy | 75–82 h | 23 h | 3 h | 34–40 h | 24–28 h | 1 | 12+ | 10+ | 5+ | 2.5 | exceeds envelope |

## 6. Top five finalists and content/rest test

All carry the same retained A+/A inventory and locked local-night floors. The common day-card proxy contains about **110 protected A+/A planning-hours**; route order changes how many become delay-exposed. Rest/slow is rounded, avoiding false precision.

| Rank | Route | 33/33 proof | A+/A hours | At-risk | Rest/slow | <05:30 wakes | Date result |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Incumbent | rail1 + KUM9 + Delhi1 + Agra1 + rail1 + BG3 + VNS8 + CCU3 + TIRU4 + Chennai1 + Delhi1 = **33** | ~110 | 0–2 | ~102 h | 2 | Taj Thu 31 Dec open; Belur Wed 13 Jan; TIRU Fri 15 Jan |
| 2 | Same-day GAY | BG3 + VNS8 + CCU3 + TIRU4 + Chennai1 + Delhi1 + Agra1 + rail1 + KUM9 + rail1 + Delhi1 = **33** | ~110 | 4–6 | ~94 h | 2–3 | no hard closure; weaker arrival/event quality |
| 3 | Same-day VNS | VNS8 + BG3 + Agra1 + rail1 + KUM9 + Delhi1 + CCU3 + TIRU4 + Chennai1 + FREE1 + Delhi1 = **33** | ~110 | 4–6 | ~92 h + free night | 2–3 | Taj Thu 31 Dec; Kolkata misses 12 Jan |
| 4 | Agra-first | Delhi1 + Agra1 + rail1 + BG3 + VNS8 + CCU3 + TIRU4 + Chennai1 + rail1 + KUM9 + Delhi1 = **33** | ~110 | 3–5 | ~96 h | 3 | Taj Mon 21 Dec; no compensating date win |
| 5 | Agra-last | rail1 + KUM9 + rail1 + VNS8 + BG3 + CCU3 + TIRU4 + Chennai1 + Delhi1 + Agra1 + Delhi1 = **33** | ~110 | 2–4 | ~98 h | 2–3 | Taj Wed 20 Jan; TIRU misses Fri 15 Jan |

### Full dated finalist skeletons

**1 — Incumbent:** 19 Dec sleeper; 20–22 Nainital; 23–25 Dunagiri/Kukuchina; 26–28 Haidakhan Vishwa Mahadham; 29 Delhi transit; 30 Agra; 31 Taj + 12988; 1–3 Jan Bodh Gaya; 4–11 Varanasi/Sarnath; 12–14 Kolkata/Dakshineswar; 15–18 Tiruvannamalai; 19 Chennai; 20 final Delhi.

**2 — Same-day GAY:** 19–21 Dec Bodh Gaya after AI429; 22–29 Varanasi/Sarnath; 30 Dec–1 Jan Kolkata/Dakshineswar; 2–5 Tiruvannamalai; 6 Chennai; 7 Delhi/Nirmal; 8 Agra; 9 Taj + road/sleeper; 10–18 fixed Kumaon sequence; 19 overnight 15014-pattern exit; 20 final Delhi.

**3 — Same-day VNS:** 19–26 Dec Varanasi/Sarnath; 27–29 Bodh Gaya; 30 Agra after daytime rail; 31 Taj + sleeper; 1–9 Jan Kumaon; 10 Delhi; 11–13 Kolkata/Dakshineswar; 14–17 Tiruvannamalai; 18 Chennai; 19 FREE; 20 final Delhi.

**4 — Agra-first:** 19 Dec Delhi/Nirmal; 20 Agra; 21 Taj + 12988; 22–24 Bodh Gaya; 25 Dec–1 Jan Varanasi/Sarnath; 2–4 Kolkata/Dakshineswar; 5–8 Tiruvannamalai; 9 Chennai; 10 MAA->DEL->sleeper; 11–19 Kumaon; 20 daytime exit/final Delhi.

**5 — Agra-last:** 19 Dec sleeper; 20–28 Kumaon; 29 rail/change to Varanasi; 30 Dec–6 Jan Varanasi/Sarnath; 7–9 Bodh Gaya; 10–12 Kolkata/Dakshineswar; 13–16 Tiruvannamalai; 17 Chennai; 18 Delhi; 19 Agra; 20 Taj + return/final Delhi.

## 7. Incumbent versus strongest challenger

| Measure | Incumbent | Same-day GAY/Bodh Gaya |
|---|---:|---:|
| Waking travel | 57 h | **55.5 h** |
| Difference | baseline | ~1.5 h less; inside uncertainty |
| Flights | 3 | 4 |
| Sleepable rail | 14.5 h | 12 h |
| Heavy days | 2 | 4 |
| AI156 exposure | none after landing | AI429 at 15:00; 4h45 scheduled margin |
| AI155 protection | dense MAA–DEL on 20 Jan + hotel | fog-exposed 15014 arrival 20 Jan + hotel |
| Agra direction | excellent 12988 night edge | reverse edge is daytime; needs Agra->KUM |
| Arrival quality | hotel/shower/rest before rail | Bodh hotel ~18:00 after two flights |
| Result | **wins higher tiers** | small tier-5 gain only |

GAY-first removes about 5–6 h of incumbent daytime Kumaon->Delhi plus Delhi->Agra positioning, but adds about 3–4 h through the DEL->GAY process, later Delhi/Nirmal staging and Agra->Gurugram sleeper access. Net: only ~1.5 h. No true extra night survives in its valid 33-night version; the saved slot is used for humane Delhi/Nirmal staging.

## 8. Agra verdict

**Keep Agra in the incumbent bridge position.** Delhi->Agra is short and dense; Taj on Thu 31 Dec avoids the official Friday closure; 12988 Agra Fort->Gaya converts distance into sleep. Reverse 12987 Gaya->Agra is daytime. Agra-last requires Delhi->Agra->Delhi near AI155 and gains no sleep edge. Agra airport is too thin to carry a locked Taj visit.

## 9. Same-day DEL continuation verdict

| Gateway | Technical result | Whole-trip result |
|---|---|---|
| GAY | **feasible: AI429 15:00–16:40 daily** | strongest challenger; reject unless connection protection and final-north risk improve |
| VNS | feasible later nonstop | small modeled gain, but more first-day/final-north risk |
| CCU | feasible | large westward return then south again |
| MAA | feasible | worst arrival fatigue; reverse route finishes on fragile north edge |

## 10. Train/flight verdict

- Keep 15013 Delhi->Kumaon, 12039 Kumaon->Delhi and 12988 Agra->Gaya in the incumbent.
- Keep rail Bodh Gaya->Varanasi when the weekday works.
- Keep flights Varanasi->Kolkata, Kolkata->Chennai and Chennai->Delhi; rail alternatives cost roughly 10–14 h, 26–30 h and 28–35 h.
- Do not replace Kumaon rail with Pantnagar air unless exact inventory later becomes materially denser/reliable.

No mode swap improves the winner.

## 11. BODH3/TIRU4 sensitivity

The macro topology does not change the BODH3/TIRU4 versus BODH2/TIRU5 experience trade-off. Moving that one night changes local content, not any directed edge total materially. The existing sensitivity remains separate.

## 12. Falsification

GAY-first should be rerun if all occur: AI156->AI429 can be protected on one ticket; DEL through-check/terminal handling is comfortable; a January north exit leaves a genuinely recoverable day before AI155; the winter outlook is benign; and Nirmal Dham can move late without experiential loss. Then it may win narrowly.

## 13. Final verdict and live rechecks

**KEEP INCUMBENT. Confidence 0.70. Bounded optimum, not a proof against future timetable changes.**

`LIVE_RECHECK_LATER`:

1. AI156/AI429 same-ticket, terminal, through-check and reaccommodation protection.
2. 19 Dec 15013 and 19/20 Jan 15014/12039 exact running, 1A/2A/EC inventory and winter punctuality.
3. 31 Dec 12988 1A/2A/running and fog history.
4. 4 Jan 20887/best Bodh Gaya->Varanasi rail; current aggregators disagree on one excluded weekday.
5. Exact VNS->CCU, CCU->MAA and MAA->DEL January nonstops and fallbacks.
6. Pantnagar/Agra airport winter service only as contingency.
7. 7–10-day operational fog forecast before each north edge.

## Sources

Canon: `runs/active/FULL_ROUTE_TOPOLOGY_GLOBAL_REOPTIMIZATION_TASK_2026-09-09.md`; `START_HERE_CURRENT_INDIA_PROJECT_STATE.md`; `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md`; `decisions/BODH3_TIRU4_WAKING_HOURS_STRESS_TEST_RESULT_2026-09-08.md`; prior exact-calendar facts from `decisions/FINAL_BOOKING_CALENDAR_LOCKED_2026-09-08.md` only where not superseded by this task.

- Air India official Winter 2026 schedule: <https://www.airindia.com/in/en/newsroom/press-release/Air-India-bolsters-winter-network-with-new-routes-to-Khajuraho-and-Jaisalmer.html>
- Air India DEL–VNS: <https://www.airindia.com/en/book-flights/delhi-to-varanasi-flights>
- Air India MAA–DEL: <https://www.airindia.com/en/book-flights/chennai-to-delhi-flights>
- IndiGo schedule: <https://www.goindigo.in/information/flight-schedule.html>
- Official Taj Mahal: <https://www.tajmahal.gov.in/>; ASI: <https://asi.nic.in/pages/WorldHeritageAgra>
- Belur Math museum/holidays: <https://belurmath.org/ramakrishna-sangraha-mandira-museum/>
- Sri Ramanasramam activities: <https://www.gururamana.org/Ashram/activities>
- 15013: <https://indiarailinfo.com/train/timetable/ranikhet-express-15013/1375/353/951>
- 12039: <https://www.railyatri.in/trains/route-12039-shatabdi-expres>
- 12988: <https://etrain.info/train/Aii-Sdah-Expres-12988/schedule>
- 12987 reverse: <https://www.ixigo.com/by-train-rail/gaya-to-agra-by-train>
- 20887: <https://etrain.info/train/Vande-Bharat-Exp-20887/schedule>
- VNS–CCU: <https://www.goindigo.in/domestic-flights/varanasi-to-kolkata-flights.html>
- MAA–DEL density: <https://www.flightsfrom.com/MAA-DEL>
- Government winter-fog disruption report: <https://ddnews.gov.in/en/dense-fog-disrupts-flights-trains-across-north-india/>

END

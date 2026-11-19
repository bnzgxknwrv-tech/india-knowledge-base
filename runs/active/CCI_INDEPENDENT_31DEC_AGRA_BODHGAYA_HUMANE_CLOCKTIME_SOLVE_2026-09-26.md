# CCI INDEPENDENT SOLVE — 31 DEC AGRA → GAYA/BODH GAYA HUMANE CLOCK-TIME CHAIN

Date: 2026-09-26
Author: CCI
Status: **INDEPENDENT DUAL-SOLVE — DONE WITHOUT READING WORK'S RESULT**
Dispatch: PR #23 comment 5849030819 (INDIA23 task, translated context supplied directly to CCI)
Scope: post-Taj 31 Dec 2026 transport chain, Agra → Gaya/Bodh Gaya, and its effect on the Bodh Gaya 2-vs-3-night question.

## 0. INDEPENDENCE STATEMENT

This solve was produced from the bound input files listed in the dispatch (`governance/CURRENT_TRUTH.md`, the INDIA22 28–31 Dec definitive lock, the INDIA22 final extraction, the INDIA23 active-memory-parity note, the four INDIA10 cluster/topology/ledger files, `HOW_TO_WORK_WITH_MARK.md`, `GUARDRAILS.md`) plus fresh live web research (Indian Railways timetable sites, airline/airport sources, distance/route sources). I did not open PR #23's comment list, did not read comment 5849075766, did not read `runs/active/WORK_INDEPENDENT_31DEC_AGRA_BODHGAYA_HUMANE_CLOCKTIME_SOLVE_2026-09-26.md`, and did not browse PR #23 in any way. I saw no content from WORK's solve at any point. If that ever turns out to be false, this note is wrong and should be flagged — but to the best of my knowledge this is a genuinely blind independent solve.

No grade was changed. No hotel was invented as locked. `governance/CURRENT_TRUTH.md` was read-only.

## 1. HARD CONSTRAINTS CARRIED FORWARD (not re-litigated)

- 30 Dec ends at a Taj-practical Agra hotel (exact property not yet chosen; zone/function locked).
- 31 Dec starts with Taj Mahal [A+] at the earliest practical opening (~06:37 planning estimate, 30 min before an approx. 07:07 sunrise; both LIVE_RECHECK closer to the date).
- No extra night is added anywhere.
- Destination is Gaya/Bodh Gaya. **No hotel is assumed locked.** `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_EXECUTION_GEOMETRY_2026-08-28.md` names "Maya Heritage" as `[HOTEL LOCKED_BY_MARK]`, but this is an August predecessor-document assumption. `governance/CURRENT_TRUTH.md` (the current controlling file, last updated 2026-09-23) does **not** mention Maya Heritage or any other Bodh Gaya hotel as locked — it only lists the Bodh Gaya sights and states nights are still open. Per Guardrails §1 (authority order: CURRENT_TRUTH beats older frozen worker analysis), I am **not** treating any Bodh Gaya hotel as locked in this solve. Where I need a rough last-mile distance for the clock model I use the general Gaya station/airport → Bodh Gaya town geometry, not a specific hotel's doorstep.
- Bodh Gaya 2-vs-3 nights (paired with Tiruvannamalai 5-vs-4) stays a later Mark-only decision. I quantify how this transport chain's arrival time feeds that decision; I do not decide it.
- Transport hierarchy respected: train first, flight only if it truly saves usable human time, private car for last-mile, no long-distance bus.
- No new sightseeing added, no grade changed, no booking action taken.

## 2. CALENDAR FACT USED THROUGHOUT

**31 December 2026 is a Thursday** (VERIFIED — calendar arithmetic, not a travel claim). This matters below because one candidate train is a weekly Thursday service.

## 3. CANDIDATE FAMILIES CONSIDERED

| # | Family | Verdict |
|---|---|---|
| 1 | Direct/near-direct overnight train, Agra → Gaya | **WINNER** — multiple real daily/weekly options exist, well matched to the clock |
| 2 | Alternative railhead (Tundla) | Rejected — adds a ~23 km/30–40 min road backtrack for **the same trains** that already call at Agra Fort/Agra Cantt/Idgah; no train exists at Tundla that isn't already reachable from Agra itself |
| 3 | Agra airport (Kheria, AGR) | Rejected — as of the current 2026 schedule, IndiGo is the only carrier at Agra and its destinations are Bengaluru, Hyderabad and Navi Mumbai; there is no Agra flight toward Bihar, directly or via one practical connection |
| 4 | Road/rail to a Delhi-area airport, then fly | Considered as fallback-of-last-resort only (see §7) — it is a backtrack Mark has explicitly said he wants to avoid, it re-enters exactly the fog-heaviest zone in North India, and it does not beat the direct train under normal conditions |
| 5 | Other air gateways (Varanasi, Patna, Kolkata) | Rejected for this specific leg — Varanasi comes later in the itinerary (would require flying "backwards" through a place not yet visited); Patna has no direct Agra service either and its road last-mile to Bodh Gaya (~130 km/~3h) is worse than Gaya's; Kolkata is geometrically the wrong direction entirely |
| 6 | Car + rail hybrid (drive partway, board a "better" train further down the line) | Rejected — the direct Agra-boarding trains already include a first-AC overnight option with a well-timed arrival; driving 3–6h toward Kanpur/Prayagraj to shave time off a journey that is already comfortable adds its own fog/road risk for no whole-human gain |
| 7 | Car + flight hybrid (via Delhi) | Same as #4 — kept only as true emergency fallback |
| 8/9/10 | Winter fog, +30/+60 robustness, real fallback | Addressed in §6–§7 for the preferred chain |
| 11 | Gaya station/airport → Bodh Gaya last-mile | Addressed in §5 |
| 12 | Effect on 2-vs-3-night trade-off | Addressed in §8 |

## 4. THE REAL TRAIN MENU — Agra → Gaya, VERIFIED CURRENT (erail.in / IndiaRailInfo, checked 2026-09-26; all times LIVE_RECHECK before booking)

There are 10–11 direct trains a day between the Agra stations (Agra Fort / Agra Cantt / Agra Idgah — all in Agra city, none is Tundla) and Gaya Junction. Only the ones departing **after** a realistic post-Taj Agra day (i.e. evening) are relevant; the 03:40–05:45 departures are irrelevant (they'd require leaving before or during the Taj visit) and are excluded below.

| Train | From (station) | Departs | Arrives Gaya | Duration | Runs | Classes |
|---|---|---|---|---|---|---|
| **12988 AII–SDAH SF EXP** | Agra Fort | **18:45** | **07:50 (+1)** | 13h05 | **Daily** | 1A, 2A, 3A, SL, 3E, GN — LHB rake, pantry car |
| 12320 GWL–KOAA SF EXP | Agra Cantt | 17:15 | 08:35 (+1) | 15h20 | **Thursdays only** (ex-Gwalior) | 1A, 2A, 3A, SL, 3E — LHB, no pantry (e-catering) |
| 12495 PRATAP EXPRESS | Agra Fort | 15:30 | 05:05 (+1) | 13h35 | Daily | (classes not independently re-verified this pass — LIVE_RECHECK) |
| 12937/12941 HWH GARBHA / PARASNATH EXP | Agra Idgah | 15:00 | ~05:05–05:20 (+1) | ~14h | Daily | LIVE_RECHECK |
| 12308/22308 JU/BKN–HWH SF EXP | Agra Idgah | 08:35 | 21:10 (same day) | 12h35 | Selected days, **not daily** | Irrelevant — departs before the Taj day is even usable |

Agra Fort station is the nearest railhead to the Taj Mahal (~2.8–3 km); Agra Cantt is ~5.7 km from the Taj. Both are short, easy road hops from any Taj-practical hotel.

12988's coach list includes a combined 1A+2A coach, so a genuine First-AC option exists on this train, matching the transport-hierarchy rule ("overnight rail target is First AC / 1A").

12320's Thursday-only pattern happens to coincide with 31 Dec 2026 being a Thursday, which is a lucky but real alignment — treated as a fallback candidate, not the primary plan, precisely because a weekly service is less robust to being retimed or dropped than a daily one between now and travel.

## 5. GAYA → BODH GAYA LAST-MILE (VERIFIED CURRENT, general geometry)

- Gaya Junction station → Bodh Gaya town: ~15–17 km, ~25–35 min by car under normal conditions (pad to ~35–45 min for a winter morning with possible fog/slow traffic).
- Gaya airport → Bodh Gaya is shorter still (~7 km) but irrelevant here since Agra has no route into Gaya airport (see §3.4/3.5).
- Private car is the correct mode per the transport hierarchy (last-mile/door-to-door). A car should be pre-booked to meet the train, exactly as already done for the 29–30 Dec corridor (Ghaziabad and Vrindavan pickups) — this is a proven pattern in this itinerary already, not a new mechanism.

## 6. PREFERRED CHAIN — FULL CLOCK-TIME MODEL

**Chain: Taj Mahal (early) → free/rest day in Agra → 12988 AII–SDAH SF EXP, Agra Fort 18:45 → Gaya Junction 07:50 (1 Jan) → private car → Bodh Gaya, ~08:30–09:00.**

| Time (31 Dec, unless noted) | Event |
|---|---|
| ~06:15–06:25 | Arrive Taj entry/approach (already locked in the 30-Dec/31-Dec plan) |
| ~06:37 (LIVE_RECHECK) | Taj Mahal opens (30 min before sunrise) |
| 06:37–~09:00 | Realistic Taj dwell: mausoleum interior, gardens, photography in the best early light — roughly 2–2.5h, not a rushed in-and-out |
| ~09:00–09:20 | Exit, walk/short transfer back to hotel |
| ~09:20–11:30 | Breakfast, shower, rest at the hotel; realistic luggage repacking |
| ~11:30–12:00 | Checkout (late/day-use checkout is normal and easy to arrange at Agra hotels serving early-Taj travellers; if not available, luggage is stored at the hotel for the day) |
| ~12:00–17:00 | Free Agra time — genuine rest, not padding. This is exactly where the already-downgraded, zero-priority Agra food bycatch (A013 Bedai at Deviram's, A014 Petha, A015 Gajak — Mark decision 2026-09-26, `decisions/INDIA23_AGRA_A013_A015_FOOD_DOWNGRADE_TO_ASTAR_MARK_DECISION_2026-09-26.md`) can be absorbed at **zero cost**, since the time exists anyway and nothing is displaced. It is optional, not scheduled. |
| ~17:00–17:30 | Repack, settle bill, depart hotel for Agra Fort station (2.8–3 km, ~10–15 min including a wide margin for evening Agra traffic) |
| ~17:30–18:15 | Arrive station, find platform, board, settle in (generous margin before the actual 18:45 departure) |
| **18:45** | 12988 departs Agra Fort |
| ~19:30–21:00 | Dinner (pantry car or pre-ordered), settle for the night |
| ~21:00–~05:30 (1 Jan) | Real sleeping window — roughly 7.5–8 hours in a berth, the best sleep quality of any option evaluated |
| ~05:30–07:50 | Wake gradually, tea, pack |
| **07:50 (1 Jan)** | Arrive Gaya Junction |
| 07:50–08:15 | Alight, luggage, exit station, meet pre-booked private car |
| 08:15–08:50 | Road transfer Gaya → Bodh Gaya (~15–17 km, padded ~35 min) |
| **~08:30–09:00 (1 Jan)** | Arrival, Bodh Gaya |

**Why this is the preferred chain:**
- It uses a genuine overnight sleeping berth (First AC available) rather than turning the night into more transit fatigue — this is the single biggest whole-human win over every other option.
- It needs no time-critical midday connection at all: the entire 31 Dec daytime after Taj is unstructured slack, so the day has essentially no fragile link (see §7).
- Its arrival time (~08:30–09:00 in Bodh Gaya on 1 Jan) lands exactly inside the arrival window that the repo's own `BODHGAYA_EXECUTION_GEOMETRY_2026-08-28.md` names as the one that supports treating 2 Bodh Gaya nights as the workable default ("if inbound train gets Mark to the hotel around ~08:30–09:00 hotel class"). This is not something I am asserting freshly — it is the pre-existing repo logic, and this chain happens to hit that exact class.
- It never forces Mark out of bed before dawn a second time in the same 48 hours (he has already had one very early start on 29 Dec); 31 Dec's early start is for the Taj itself, which is non-negotiable, but the transport chain adds no second pre-dawn wake-up.
- Agra Fort is the nearer of Agra's two relevant stations to any Taj-practical hotel (~2.8–3 km vs ~5.7 km for Agra Cantt), so the evening transfer is trivially short.

## 7. STRONGEST ALTERNATIVE, ROBUSTNESS, AND FALLBACK

### 7.1 Strongest alternative: 12495 PRATAP EXPRESS (Agra Fort 15:30 → Gaya 05:05)

This is the genuine second-place finalist, not a strawman. It departs earlier (15:30) and arrives earlier (05:05, 1 Jan) than 12988. **When it would win:** only if Mark explicitly decides he would rather squeeze more usable content into 1 Jan itself — for example, catching first light at the Mahabodhi Temple at dawn on arrival day — than have a comfortable, late, unhurried Agra afternoon and a full night's sleep. The costs that make it second-place by default:
- It compresses the free Agra afternoon (must leave the hotel by ~14:45 instead of ~17:00), cutting the slack that currently absorbs the food bycatch and any Taj/checkout overrun.
- 05:05 is pre-dawn: Mark would be woken around 04:00–04:30 on the train, disembark into a dark, cold station, and do the Gaya→Bodh Gaya last-mile before sunrise. A hotel room will very likely not be ready that early (normal check-in is midday), so the "gain" is largely illusory — he would be waiting somewhere (lobby, car, or the temple itself) for daylight rather than actually resting.
- Net effect: it trades sleep quality and a relaxed transfer for a few extra pre-check-in hours whose real content is "wait for sunrise," with a materially rougher night.

I default to 12988. This alternative should only be chosen if Mark says, in substance, that he wants to be present at Mahabodhi Temple at first light on arrival day and is willing to accept a rougher night for it. **This is a genuine Mark-only decision gate** — see §9.

### 7.2 Winter fog risk on the preferred option

The 12988 route runs Agra Fort → Tundla → Kanpur Central → Prayagraj → Pt DD Upadhyaya → Gaya, i.e. squarely through the Gangetic-plain corridor that current reporting (Jan 2025 events, RECURRING PATTERN historically for this exact season and this exact stretch) explicitly names as a dense-fog caution zone in December–January, with real North Indian trains commonly running 1–4+ hours late, and in bad spells more, during fog spells. This is a RECURRING PATTERN classification (a service that reliably runs on this weekday/date pattern historically shows this risk profile), not a fabricated specific prediction for 31 Dec 2026–1 Jan 2027.

- Departure side (18:45 from Agra Fort) is essentially fog-safe: dense fog in this belt is a pre-dawn/mid-morning phenomenon, not an evening one, so the outbound leg is unlikely to be disrupted by fog itself (mechanical/upstream delay from the train's earlier legs is a separate, smaller risk, and does not cost us anything since we simply board whenever it actually arrives/departs at Agra — see §7.3).
- Arrival side (07:50 into Gaya, 1 Jan) is the real exposure: a fog-affected morning could push the actual arrival to mid-morning or, in a bad spell, into early afternoon.

### 7.3 +30 / +60 minute robustness

- **+30 min anywhere in the 31 Dec daytime** (longer Taj dwell, slower checkout, worse Agra traffic to the station): fully absorbed. The daytime buffer between Taj exit (~09:00) and the 18:45 departure is measured in hours, not minutes.
- **+60 min anywhere in the daytime**: still fully absorbed for the same reason. This chain's biggest structural strength is that there is no midday connection to protect — the whole day is intentionally slack.
- **+30/+60 min on the train's own running (upstream delay from Ajmer/Jaipur before it even reaches Agra)**: costs us nothing directly — we do not have a connection to make at Agra Fort; we simply board a later-than-timetabled train and our sleep window shifts slightly later. The real cost only appears if the delay compounds overnight (see fog, above) and affects the Gaya-end arrival.
- **+30/+60 min fog delay into Gaya**: pushes Bodh Gaya hotel arrival to ~09:00–10:30 (30 min case) or ~09:30–11:00 (60 min case) after the last-mile transfer. Both are still same-day, still usable arrival-day windows — this degrades gracefully, it does not strand anyone.

### 7.4 Real fallback if 12988 is cancelled or badly delayed before departure

1. **First fallback (same evening, same city): 12320 GWL–KOAA SF EXP from Agra Cantt, 17:15 → Gaya 08:35 (+1).** This is a real, verified alternative train with an almost identical profile (overnight, 1A/2A/3A available, arrival at ~08:35 which is, if anything, even closer to the ideal 08:30–09:00 arrival-day window than 12988's own arrival). Its only weaknesses versus 12988: it runs from Agra Cantt (further from a Taj-Ganj hotel, ~5.7 km vs ~2.8–3 km) and, per current schedule, is a **Thursday-only weekly service** rather than daily — which happens to be fine for 31 Dec 2026 specifically (a Thursday), but this exact-date coincidence must be reconfirmed close to travel (LIVE_RECHECK), since a weekly service is inherently more exposed to being retimed or discontinued between now and December 2026 than a daily one.
2. **Second fallback: same-evening alternative departures from Agra Idgah** (12937/12941 family, ~15:00 departures, ~05:05–05:20 arrival) — usable in a pinch, with the same pre-dawn-arrival trade-off already described for 12495 in §7.1.
3. **Emergency-only fallback (not a planned alternative): road/rail to a Delhi-area airport, then fly Delhi→Gaya.** Air India has added extra Delhi–Gaya frequency this winter season (both morning and afternoon departures each way), and this is a genuinely usable route in isolation — but reaching it means backtracking toward Delhi, exactly the congestion and direction Mark has repeatedly said he wants to avoid on this corridor, and it re-enters the single foggiest micro-region in North India for departure. This is a real fallback of last resort (e.g., if both the Agra Fort and Agra Cantt overnight options are simultaneously unavailable), not a competitive routine alternative.
4. **Not a fallback:** a single long private-car push (Agra→Bodh Gaya is realistically ~560–600 km / 10–14+ raw driving hours) is explicitly rejected as an option at any point in this chain — it violates the "no long-distance bus/marathon-car" spirit of the transport hierarchy and would produce a worse night's rest than either train option, for no compensating benefit.

## 8. EFFECT ON THE BODH GAYA 2-vs-3-NIGHT QUESTION (quantified, not decided)

The repo's own `BODHGAYA_EXECUTION_GEOMETRY_2026-08-28.md` already ties the 2-vs-3-night default directly to arrival time: 2 nights is the evidence-based default **if** inbound arrival gets Mark to the hotel around ~08:30–09:00; 3 nights is indicated if arrival is materially later, if the outer-sites day (Dungeshwari → Sujata Stupa → Mahabodhi story-arc, all [A+]) proves too compressed after live route verification, or if Mark simply wants an additional unstructured sacred-core day.

This solve's preferred chain (12988) lands almost exactly on that threshold (~08:30–09:00 arrival), so **on a normal day it directly supports keeping 2 nights as viable**, without CCI deciding the trade-off itself. The quantified sensitivity:

- **On-time or minor delay (0–30 min):** arrival ~08:30–09:30 → 2-night default fully supported; arrival day still has a real half-day for a first Mahabodhi/sacred-core block plus rest.
- **Moderate fog delay (+60–120 min):** arrival ~09:30–11:30 → 2 nights is still plausible but tighter; the arrival-day content likely compresses to "sacred-core visit only," pushing the full Dungeshwari→Sujata outer-sites loop entirely onto the single full day, which is workable but leaves zero slack in that day.
- **Bad fog spell (+180 min or more, or the fallback train is used):** arrival early-to-mid afternoon → this measurably weakens the 2-night case, because the arrival day no longer contributes a meaningful A+ block; at that point 3 nights becomes the safer recommendation to protect the outer-sites day from being rushed.
- If Mark instead chooses the 12495 alternative from §7.1 (pre-dawn ~05:05 arrival, effective hotel-ready state well before the 08:30 threshold), the arrival-day content could in principle start even earlier (a first-light Mahabodhi visit is possible) — but the real gain is smaller than it looks, because most of that early window is spent waiting for sunrise/check-in rather than being active, so it does not obviously strengthen the 2-night case further beyond what 12988 already achieves; it just moves the same amount of daytime earlier at the cost of sleep quality.

In short: **the preferred chain is engineered to keep the 2-vs-3-night door open in Mark's favour without forcing it**, and its main risk (fog) degrades that door gradually (nudging toward 3 nights) rather than slamming it shut.

## 9. GENUINE MARK-ONLY DECISION GATE FOUND

One real, non-manufactured gate emerged from this solve (beyond the already-known 2-vs-3-night question, which this solve deliberately does not decide):

**12988 (comfort/sleep, arrive ~07:50) vs 12495 (compressed Agra afternoon, pre-dawn arrival ~05:05, possible first-light Mahabodhi on arrival day).** This is a genuine subjective trade-off between sleep quality/relaxed pacing and squeezing extra usable content into 1 Jan, and only Mark can weigh it — it is not something CCI can objectively resolve. My own recommendation, based on Mark's demonstrated pattern elsewhere in this exact corridor (rejecting an "unreasonable night drive" to make the 29 Dec connection, and preferring Greater Noida's normal evening over pushing straight to Vrindavan the same day), is that he would choose comfort — i.e., **12988** — but I am flagging rather than deciding this.

I found no other genuine new Mark-only decision in this scope beyond the pre-existing 2-vs-3-night question and the already-settled hotel-zone/function locks; the exact Agra and Bodh Gaya hotel *properties* remain ordinary booking-stage choices, not decision gates.

## 10. LIVE_RECHECK ITEMS (do not treat as booked facts)

1. Exact 31-Dec-2026/1-Jan-2027 operation, timing and ticket availability of train 12988 (AII–SDAH SF EXP), including confirming 1A/2A availability on that specific date.
2. Exact 31-Dec-2026 operation of train 12320 (GWL–KOAA SF EXP) — confirm it is still a Thursday-only service on the current timetable and that 31 Dec 2026 is still covered, before relying on it even as a fallback.
3. Taj Mahal's exact 31 Dec 2026 opening time/gate and sunrise time (currently ~06:37 opening / ~07:07 sunrise, per the existing lock) shortly before travel.
4. Agra hotel's actual late-checkout/day-use policy once a specific property is chosen — the clock model above assumes this is arrangeable, which is normal for Agra but should be confirmed at booking.
5. Current fog/weather advisories for the Agra–Kanpur–Prayagraj–Gaya rail corridor as the travel date approaches.
6. Exact Gaya Junction → Bodh Gaya road time/last-mile access point on the day (prepaid taxi counter location, or pre-booked private car meeting point).
7. Current Delhi–Gaya flight timings/frequency if the emergency Delhi fallback is ever actually needed.

## 11. SOURCES USED (live web research, checked 2026-09-26)

- erail.in train listings, Agra Cantt ↔ Gaya Jn.
- IndiaRailInfo timetable/route pages for trains 12988, 12308, 12320.
- ixigo, goibibo, prokerala train schedule pages for 12988/12320 route and coach composition.
- Wikipedia / airline and airport pages for Agra Airport (Kheria) current destinations and Gaya Airport current/winter-season flight additions (Air India Delhi–Gaya extra frequency, IndiGo Gaya–Bangkok).
- Distance/last-mile sources (yatra.com, tripoto, distancebetween2.com) for Gaya Junction ↔ Bodh Gaya.
- Distance sources for Agra Fort/Agra Cantt ↔ Taj Mahal.
- Recent North Indian winter-fog train-delay reporting (Jan 2025 events) used only to establish a RECURRING PATTERN risk class for the Agra–Kanpur–Prayagraj–Gaya corridor in Dec/Jan, not as a specific prediction for this trip's dates.

END OF CCI INDEPENDENT SOLVE

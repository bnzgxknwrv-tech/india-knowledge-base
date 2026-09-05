# CCI — INDIA17 GLOBAL MULTIMODAL CALENDAR + OPTIONAL-CLUSTER ROUTE MATRIX

Status: **TRAVEL EXECUTION SUPPORT — OBJECTIVE ROUTE/CALENDAR RESEARCH ONLY, NO MARK-ONLY CHOICE MADE**
Worker branch: `agent/india17-cci-kumaon-geometry` (reused; same worker, additive file, not merged to central)
Task: CCI_TASK — INDIA17 GLOBAL MULTIMODAL CALENDAR + OPTIONAL-CLUSTER ROUTE MATRIX (PR #23)
Researched: 2026-09-05

No A+/A/A*/B/C grade, hotel/base lock, fixed duration, or optional-world inclusion decided here. Six calendar scenarios are built and compared on structure/evidence only.

## HARD ENVELOPE (unchanged, re-confirmed from central)
- Arrive DEL Saturday 19 Dec 2026 10:15, AI156.
- Depart DEL Thursday 21 Jan 2027 12:20, AI155.
- 33 India overnight slots (nights of 19 Dec through 20 Jan inclusive).
- Kumaon 9 nights currently: Nainital 20/21/22, Dunagiri 23/24/25, Haidakhan 26/27/28 Dec; outbound overnight-transport slot 29 Dec.
- Per `GLOBAL_SLOT_TALLY_OPTIONAL_WINDOW_2026-09-05.md`'s own live accounting: **30 slots are strongly spoken-for** (1 inbound rail + 9 Kumaon + 1 outbound rail + 1 Agra + 1 Agra->Gaya sleeper + 2 Bodh Gaya + 8 Varanasi + 5 Tiruvannamalai + 2 final Delhi), leaving a **center estimate of 3 discretionary slots** (working range 2-4, because Varanasi's 8 is prior canon awaiting recheck and final-Delhi could move by one slot). This matrix uses **3** as the working discretionary budget and states clearly where a scenario spends fewer.

## SOURCE / CONFIDENCE TABLE

| Fact | Value | Source | Confidence |
|---|---|---|---|
| KGM->Delhi Cantt overnight (15014 Ranikhet Express) | ~20:35 -> ~05:03, daily, 1A/2A/3A/SL | `GLOBAL_SLOT_TALLY_OPTIONAL_WINDOW_2026-09-05.md` (prior CCI research) | HIGH — public timetable, not re-verified this session |
| KGM->Haridwar overnight (14119 KGM-DDN Express) | ~19:55 -> ~02:30, daily, 1A/2A/3A/SL | same file | HIGH, not re-verified this session |
| KGM->Lucknow (13020 Bagh Express) | ~21:50 -> ~06:10, daily, 2A/3A/SL (no 1A) | same file | HIGH, not re-verified this session |
| Lal Kuan->Varanasi direct (12354 LKU-HWH SF) | ~18:50 -> ~07:15, **SATURDAY ONLY**, 2A/3A/SL | same file | HIGH, not re-verified this session |
| Agra Fort->Gaya overnight (12988 Ajmer-Sealdah SF) | ~18:45 -> ~07:50, daily, 1A available | `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` + `governance/CURRENT_STATE.md` (both cite this train, cross-confirmed across two owning files) | HIGH, not re-verified this session |
| Varanasi->Chennai direct flight (IndiGo 6E6044) | ~2h15 block time, "on operating days" | `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` | MEDIUM — "operating days" not daily-confirmed; not re-verified this session |
| Varanasi->Bengaluru fallback flight | exists, current service | same file | MEDIUM, not re-verified this session |
| Chennai Airport->Tiruvannamalai | ~171 km / ~2.5 h raw | same file | HIGH (district/aggregator class), not re-verified this session |
| Bengaluru Airport->Tiruvannamalai | ~232 km / ~3.5 h raw | same file | HIGH, not re-verified this session |
| Pantnagar->Delhi flight (IndiGo) | ~1 h, ~2 flights/day, e.g. 08:30/16:25 departures | **fresh search this session** | MEDIUM — schedule snapshot, not date-specific |
| Dunagiri/Kukuchina->Pantnagar Airport | ~160 km / ~5 h road | `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` (Dunagiri Retreat's own stated figure) | MEDIUM — anchored at Dunagiri, not independently re-checked for a Haidakhan-anchored departure |
| Tiruvannamalai->Delhi via Chennai or Bengaluru | very frequent, ~2h45 nonstop Chennai-Delhi | **fresh search this session** | HIGH for frequency/duration; no airport has no direct Tiruvannamalai flight (confirmed no local airport) |
| Tiruvannamalai->Puducherry | ~110 km / ~1h24 | **fresh search this session** | HIGH |
| Puducherry->Chennai Airport | ~163 km | **fresh search this session** | HIGH |
| Tiruvannamalai->Chennai Airport via Puducherry vs. direct | ~273 km via Puducherry vs. ~172 km direct — **~100 km / real detour, NOT near-free** | **fresh search this session**, derived comparison | HIGH on the comparison, though exact live routing not confirmed |
| Haridwar->Mathura/Agra direct rail incl. 1A | exists, current service classes | `GLOBAL_SLOT_TALLY_OPTIONAL_WINDOW_2026-09-05.md` | MEDIUM — not re-verified this session, no exact train numbers carried forward |
| Agra->Prayagraj->Gaya vs. direct Agra->Gaya | Prayagraj route exists on the same west-east corridor; exact Prayagraj->Gaya connection timing **not researched this session** | `CLUSTER_TOPOLOGY_FEASIBILITY_2026-08-25.md` (corridor claim only) | LOW on exact timing — LIVE_RECHECK_LATER |
| True Haidakhan Vishwa Mahadham <-> Kathgodam/Haldwani gateway | **unresolved conflict, ~27-90 km depending on source, even within the ashram's own official site** | prior CCI `CCI_KUMAON_GEOMETRY_MATRIX.md` (this same worker branch, commit `7c34f91`) | LOW/CONFLICTING — explicitly unresolved, carried forward honestly |
| Dec 2026/Jan 2027 exact date rail inventory | outside ~60-day IRCTC booking horizon as of 2026-09-05 | `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md` | STRUCTURAL_CURRENT + LIVE_RECHECK_LATER throughout |

## PANTNAGAR — NEW GATEWAY DATA (fresh this session)
IndiGo currently runs a daily Pantnagar<->Delhi route, roughly 1 h flight time, with departures from Pantnagar around 08:30 and 16:25 (and Delhi->Pantnagar around 12:45), current-schedule snapshot. This makes a Haidakhan-exit-by-air structurally real, not hypothetical — but it requires the same ~5 h road leg from the Kumaon highlands to Pantnagar that Dunagiri Retreat's own site states for that airport, and Haidakhan sits further from Pantnagar than Dunagiri does (not independently re-measured this session — treat any Haidakhan-anchored Pantnagar figure as LIVE_RECHECK_LATER, likely somewhat longer than 5 h).

## PUDUCHERRY — TESTED, NOT NEAR-FREE
Direct Tiruvannamalai->Chennai Airport is ~172 km. Routing via Puducherry adds Tiruvannamalai->Puducherry (~110 km) + Puducherry->Chennai (~163 km) = ~273 km, a genuine **~100 km / roughly 1.5-2 h one-way detour**, not a "pass-through for free" insertion. Puducherry can only be near-free if given its **own dedicated overnight(s)** rather than treated as a same-day waypoint to the airport — i.e. it consumes discretionary slot(s) exactly like Haridwar/Rishikesh, Braj or Prayagraj, contrary to the hopeful framing in the task brief. This directly answers the task's point 8: **no, current route geometry does not make Puducherry near-free on the Chennai/Tiruvannamalai exit leg.**

---

# SIX CALENDAR SCENARIOS

All scenarios share identical dates 19-28 Dec (arrival, night train, 9 Kumaon nights as already closed) and differ only from 29 Dec onward. "Slack" = unassigned discretionary nights remaining out of the 3-slot working budget; a scenario using more than 3 discretionary-equivalent nights is flagged as exceeding the current center estimate.

## SCENARIO 1 — BEST_FIXED_CORE_CALENDAR (no optional insertion)
| Date | Night in / world | Transport that day |
|---|---|---|
| 29 Dec (Tue) | overnight train | KGM ~20:35 -> Delhi Cantt ~05:03 (15014) |
| 30 Dec | Agra hotel | Delhi->Agra short rail/road hop, same morning |
| 31 Dec | overnight sleeper | Taj sunrise visit, evening 12988 Agra Fort ~18:45 -> Gaya |
| 1-2 Jan | Bodh Gaya (2 nights) | arrive Gaya ~07:50, road to Bodh Gaya |
| 3-10 Jan | Varanasi/Sarnath (8 nights) | Bodh Gaya->Varanasi rail, same day |
| 11-15 Jan | Tiruvannamalai (5 nights) | fly Varanasi->Chennai (6E6044-class), road ~2.5h to Tiruvannamalai |
| 16-17 Jan | final Delhi (2 nights) | road Tiruvannamalai->Chennai Airport, fly Chennai->Delhi |
| 18-20 Jan | **UNASSIGNED SLACK (3 nights)** | none — genuinely free/buffer |
| 21 Jan | departure | AI155 12:20 DEL |

Slot check: 1+9+1+1+1+2+8+5+2 = 30, + 3 slack = **33/33**. Exact fit, matching `GLOBAL_SLOT_TALLY`'s own arithmetic.

## SCENARIO 2 — Haridwar-Rishikesh insertion only (2 nights)
| Date | Night in / world | Transport that day |
|---|---|---|
| 29 Dec | overnight train | KGM ~19:55 -> Haridwar ~02:30 (14119) |
| 30-31 Dec | Haridwar-Rishikesh (2 nights) | very early arrival, full recovery + 1 local day |
| 1 Jan | Agra hotel | Haridwar->Mathura/Agra direct rail (exact train not re-verified this session) |
| 2 Jan | overnight sleeper | Taj sunrise, evening 12988 to Gaya |
| 3-4 Jan | Bodh Gaya (2 nights) | |
| 5-12 Jan | Varanasi (8 nights) | |
| 13-17 Jan | Tiruvannamalai (5 nights) | |
| 18-19 Jan | final Delhi (2 nights) | |
| 20 Jan | **1 night slack remaining** | |
| 21 Jan | departure | |

Discretionary spend: 2 of 3. **1 slot of margin left** — safer than Scenario 4.

## SCENARIO 3 — BEST_ONE_OPTIONAL_CALENDAR — Braj insertion only (1 night)
| Date | Night in / world | Transport that day |
|---|---|---|
| 29 Dec | overnight train | KGM ~20:35 -> Delhi Cantt ~05:03 (15014) |
| 30 Dec | Braj (Mathura-Vrindavan-Govardhan), 1 night | Delhi->Mathura short rail hop |
| 31 Dec | Agra hotel | Braj->Agra short hop |
| 1 Jan | overnight sleeper | Taj sunrise, evening 12988 to Gaya |
| 2-3 Jan | Bodh Gaya (2 nights) | |
| 4-11 Jan | Varanasi (8 nights) | |
| 12-16 Jan | Tiruvannamalai (5 nights) | |
| 17-18 Jan | final Delhi (2 nights) | |
| 19-20 Jan | **2 nights slack remaining** | |
| 21 Jan | departure | |

Discretionary spend: only 1 of 3. This is the single cheapest optional insertion in geometric terms (matches the existing repo's own "Braj = lowest geometric burden" judgment) and leaves the most margin of any non-empty scenario — the reason it is marked BEST_ONE_OPTIONAL, not because Braj is asserted to be more valuable to Mark than Haridwar/Rishikesh (that remains Mark's own subjective choice).

## SCENARIO 4 — BEST_TWO_OPTIONAL_CALENDAR — Haridwar-Rishikesh + Braj (matches `GLOBAL_SLOT_TALLY`'s own illustrative scenario)
| Date | Night in / world | Transport that day |
|---|---|---|
| 29 Dec | overnight train | KGM ~19:55 -> Haridwar ~02:30 (14119) |
| 30-31 Dec | Haridwar-Rishikesh (2 nights) | |
| 1 Jan | Braj, 1 night | Haridwar->Mathura direct rail |
| 2 Jan | Agra hotel | Braj->Agra short hop |
| 3 Jan | overnight sleeper | Taj sunrise, evening 12988 to Gaya |
| 4-5 Jan | Bodh Gaya (2 nights) | |
| 6-13 Jan | Varanasi (8 nights) | |
| 14-18 Jan | Tiruvannamalai (5 nights) | |
| 19-20 Jan | final Delhi (2 nights) | |
| 21 Jan | departure | |

Discretionary spend: **exactly 3 of 3 — ZERO buffer nights remain.** Confirms `GLOBAL_SLOT_TALLY`'s own statement that both optionals "can consume the full 33-slot envelope almost exactly." **Flagged as the highest-risk scenario in this matrix** (see FALSE_FRIENDS): it leaves no slack to absorb a Varanasi true-duration recheck that comes in above 8, a weather/fog delay, or any LIVE_RECHECK_LATER item resolving unfavorably.

## SCENARIO 5 — Prayagraj insertion (in place of the direct Agra->Gaya sleeper)
| Date | Night in / world | Transport that day |
|---|---|---|
| 29 Dec | overnight train | KGM ~20:35 -> Delhi Cantt ~05:03 (15014) |
| 30 Dec | Agra hotel | Delhi->Agra |
| 31 Dec | Prayagraj, 1 night | Taj sunrise, day train Agra->Prayagraj (**exact timing not researched this session — LIVE_RECHECK_LATER**) |
| 1 Jan | transit/Gaya arrival | Prayagraj->Gaya (**exact connection not researched this session — LIVE_RECHECK_LATER**); treated conservatively as consuming a full day rather than a free overnight, since no sleeper-class Prayagraj->Gaya product was verified |
| 2-3 Jan | Bodh Gaya (2 nights) | |
| 4-11 Jan | Varanasi (8 nights) | |
| 12-16 Jan | Tiruvannamalai (5 nights) | |
| 17-18 Jan | final Delhi (2 nights) | |
| 19-20 Jan | **2 nights slack remaining (provisional)** | |
| 21 Jan | departure | |

**Confidence on this scenario is lower than 1-4**: the direct Agra->Gaya sleeper (12988) is a verified, sourced, sleep-while-travelling product; replacing it with Agra->Prayagraj->Gaya trades a known-good overnight-transit slot for two unresearched day segments. This matches the existing repo's own caution that "Prayagraj must survive on its own spiritual/travel value, not because route engineering needs it" — this scenario shows it is not a geometry improvement over Scenario 1's direct sleeper, only a content addition with an uncosted timing risk.

## SCENARIO 6 — BEST_FLIGHT_ASSISTED_CALENDAR — Pantnagar exit, tested honestly
| Date | Night in / world | Transport that day |
|---|---|---|
| 29 Dec | Delhi hotel (real bed, not train) | road Haidakhan->Pantnagar (~5h+, LIVE_RECHECK_LATER, likely longer than Dunagiri's own 5h figure), then IndiGo Pantnagar->Delhi (~1h, e.g. ~16:25->17:35 class) |
| 30 Dec | Braj, 1 night | Delhi->Mathura |
| 31 Dec | Agra hotel | Braj->Agra |
| 1 Jan | overnight sleeper | Taj sunrise, evening 12988 to Gaya |
| 2-3 Jan | Bodh Gaya (2 nights) | |
| 4-11 Jan | Varanasi (8 nights) | |
| 12-16 Jan | Tiruvannamalai (5 nights) | |
| 17-18 Jan | final Delhi (2 nights) | |
| 19 Jan | **1 night slack remaining** | |
| 21 Jan | departure | |

**Honest result of testing this "creative" option: it does NOT create a windfall.** The overnight-train scenarios (1-5) convert the Haidakhan-exit travel time into sleeping-transit time at zero extra slot cost. Flying instead converts that same travel time into a genuine **occupied Delhi hotel night** — a real comfort/rest-quality gain (a bed instead of a train berth, and a more humane arrival time than ~05:03) but at the cost of **one full discretionary slot**, leaving only 1 of 3 remaining rather than the 2 that direct-to-Braj (Scenario 3) achieves by rail. It also **structurally forecloses a cheap Haridwar/Rishikesh insertion**, because Haridwar sits geographically between Kumaon and Delhi — flying past it to Delhi first means reaching it afterward would require backtracking northwest, which no scenario here attempts. This is reported as the requested flight-assisted test, not as a recommendation; per the task's own framing, it only "wins" on comfort/timing, not on slot economy or route efficiency.

---

# MOST_VALUABLE_ROUTE_SURPRISE
The Nainital-first / Haidakhan-last reorder (already adopted in the live calendar draft before this task) is what makes Haridwar/Rishikesh a real train-first candidate *after* Kumaon at all. Under the old Haidakhan-first order, Kumaon finished deep in the Dunagiri highlands with no good rail gateway; under Haidakhan-last, Mark returns to the Kathgodam/Haldwani gateway with a direct daily 1A-capable train (14119) toward Haridwar. This single ordering change is the biggest structural unlock in this whole matrix — bigger than any of the 6 scenarios' individual differences — and it was already recognized in `GLOBAL_SLOT_TALLY_OPTIONAL_WINDOW_2026-09-05.md`; this task's research does not change that judgment, only reconfirms it while building the full calendars around it.

# FALSE_FRIENDS
1. **Puducherry via the Chennai exit "looks free" but is a genuine ~100 km detour** if treated as a same-day waypoint — see PUDUCHERRY section above. It can only work as its own dedicated overnight, competing for the same 2-4 discretionary slots as everything else.
2. **Scenario 4 (Haridwar+Braj) fits the envelope exactly — with zero buffer.** A route that "fits perfectly" on paper is the one with no margin for any of this matrix's many LIVE_RECHECK_LATER items to resolve unfavorably. Fitting exactly is a warning sign here, not a selling point.
3. **The Pantnagar flight "shortcut" does not save a slot** — it spends one, converting free sleeping-transit time into an occupied hotel night, and forecloses the cheap Haridwar insertion by routing past it. See Scenario 6.
4. **12354 Lal Kuan->Howrah (direct to Varanasi)** looks like the cleanest possible Kumaon exit because it goes straight to Varanasi — but it is Saturday-only and does not fall on Tuesday 29 Dec under the current 9-night Kumaon structure. Chasing it would require distorting an already-closed footprint for a single weekly train, which none of these 6 scenarios attempt.
5. **The true Haidakhan Vishwa Mahadham's own official site states two different gateway distances in different places** (this matrix's Source/Confidence table and the prior `CCI_KUMAON_GEOMETRY_MATRIX.md` both document this) — any scenario's exact 29 Dec departure timing from Haidakhan itself should be treated as a planning band (1-2h class), not an exact number, until that conflict is closed with real routing evidence.

# EXACT DATE / WEEKDAY DEPENDENCIES
- Taj Mahal closed Fridays (already established central fact) — none of the 6 scenarios currently land a Taj visit on a Friday, but this must be re-checked if any scenario's dates shift.
- 12354 Lal Kuan->Howrah: **Saturday only** — does not fit Tuesday 29 Dec under the current Kumaon structure (see FALSE_FRIENDS #4).
- All Kumaon-gateway trains used here (15014, 14119, 13020) are currently listed as **daily** — lower weekday risk than 12354, but Dec 2026 actual-date running pattern is still LIVE_RECHECK_LATER.
- 19 Dec and 29 Dec 2026 both sit outside the ~60-day IRCTC reservation horizon as of this research date (2026-09-05); working reference booking-window dates are ~20 Oct 2026 and ~30 Oct 2026 respectively (carried forward from `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md`).
- IndiGo 6E6044 Varanasi->Chennai is stated as running "on operating days," not confirmed daily — every scenario above (1-5) depends on this flight; if it does not operate on the actual transition date, the Bengaluru fallback (with a longer ~3.5h road leg into Tiruvannamalai) becomes load-bearing and should be re-priced before a final choice.

# WHAT REMAINS UNPROVEN / NOT RESEARCHED THIS SESSION
- Exact Haridwar->Mathura/Agra train numbers/times (only "direct service with 1A exists" was carried forward, not independently re-verified).
- Exact Agra->Prayagraj and Prayagraj->Gaya train numbers/times (Scenario 5's weakest link).
- Exact Haidakhan-anchored (rather than Dunagiri-anchored) road time to Pantnagar Airport.
- Whether IndiGo 6E6044 (Varanasi->Chennai) operates daily or on a restricted weekly pattern — "operating days" language was not resolved to an exact schedule this session.
- Live Dec-2026/Jan-2027 actual-date inventory for every train and flight cited — all remain STRUCTURAL_CURRENT + LIVE_RECHECK_LATER per the project's own established convention, consistent with how `KUMAON_CALENDAR_FIRST_LEG_2026-12-19_TO_29.md` already treats this same distinction.

# CONFIRMATION PER TASK GUARDS
No Mark grade, hotel/base lock, fixed duration, or optional-world inclusion decided or changed. All 6 scenarios are presented side by side with their own evidence quality and risk profile; none is recommended as Mark's final choice. Work is additive on worker branch `agent/india17-cci-kumaon-geometry`, not merged to central.

END

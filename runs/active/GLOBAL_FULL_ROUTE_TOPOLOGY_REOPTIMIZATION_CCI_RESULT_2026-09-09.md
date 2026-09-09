# GLOBAL FULL-ROUTE TOPOLOGY REOPTIMIZATION — CCI RESULT

Date: 2026-09-09

Worker branch: `worker/global-route-topology-reoptimization`

Executed by: CCI, per `CCI_TASK — GLOBAL FULL-ROUTE TOPOLOGY REOPTIMIZATION`, PR #23, and `runs/active/FULL_ROUTE_TOPOLOGY_GLOBAL_REOPTIMIZATION_TASK_2026-09-09.md` (central `90bce12`).

**STATUS: COMPLETE. Builds on, and does not re-derive, `GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_CCI_RESULT_2026-09-09.md` (this branch, commit `7a26da3`) — that pass already tested Agra-last, full reverse, Kolkata/Varanasi permutations, train-heavy and flight-heavy. This pass adds the two genuinely new elements this task requires: the same-day-arrival-continuation hypothesis, and a Kumaon-last/"end near Delhi" variant, both quantified with new evidence.**

---

## 1. VERIFIED CURRENT CANON USED

Trip envelope, all hard locks, and FINAL OUT exclusions as in `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md` and `START_HERE_CURRENT_INDIA_PROJECT_STATE.md`. Primary duration surface: Bodh Gaya 3n / Tiruvannamalai 4n; Bodh Gaya 2n / Tiruvannamalai 5n reported as the parallel sensitivity throughout, per this task's instruction.

---

## 2. THE NEW HYPOTHESIS, QUANTIFIED: SAME-DAY DOMESTIC CONTINUATION FROM DEL

### 2a. Is it even schedulable?

Checked current recurring domestic patterns from Delhi for all four suggested gateways:

| Gateway | Current daily frequency from DEL | Last practical departure | Same-day continuation after AI156 ~10:15 arrival? |
|---|---|---|---|
| DEL→GAY | Only **5x/week** (Tue/Wed/Thu/Sat/Sun), and every flight departs **07:30–10:15** | 10:15 | **Structurally impossible** — the last GAY flight of the day departs at essentially the same moment AI156 lands. No realistic connection exists on any day of the week. |
| DEL→VNS | ~4–8 flights/day, spread through the day | evening | Technically schedulable |
| DEL→CCU | ~20 flights/day, spread through the day | late evening | Technically schedulable |
| DEL→MAA | Dense trunk route, multiple carriers | late evening | Technically schedulable |

**GAY is eliminated outright — not a close call, a scheduling impossibility.** VNS/CCU/MAA remain live candidates for §2b.

### 2b. Even where schedulable, does it actually help?

Modeled realistically, not at the "mathematically earliest possible" flight:
- AI156 lands ~10:15 → immigration + baggage at a large international terminal: 1.5–2h realistic → domestic terminal transfer: 30–45min → check-in/security buffer before a domestic flight: 1.5–2h. **Earliest humanely-robust domestic departure: ~14:30–15:30, not earlier.**
- VNS (~1h40) → lands ~16:30–17:30; CCU (~2h) → lands ~17:00–18:00; MAA (~2h45) → lands ~18:00–19:00.
- Every one of these gateways then requires a further road transfer to the actual destination base (Varanasi city ~20–30min from VNS is fine; but Bodh Gaya from a CCU-style gateway isn't reachable this way at all — Kolkata doesn't shortcut to Bodh Gaya; a genuinely useful same-day arrival would need to be VNS specifically, or accept a multi-hour road leg from CCU/MAA into an unrelated area).
- **Arrival at final lodging realistically lands at or after 19:00–21:00 on the same calendar day the traveller has already been awake since boarding an overnight AMS–DEL flight the previous evening** — this is a materially worse arrival-quality outcome than the incumbent's gentle immigration → hotel/dayroom → rest → evening night-train boarding, and it does so with **zero fallback** if AI156 itself runs late (a common winter-fog scenario for Delhi, already well-documented in this project's own research) — a delayed AI156 would strand the traveller with a missed, unrecoverable domestic connection on day one of the trip, before any other buffer exists to absorb it.

**This fails decisively on objective-function tier 2 (safety/missed-connection robustness) before tier 5 (waking-hours saved) is even reached.** Per the lexicographic ordering Mark himself specified, a tier-2 failure cannot be rescued by a tier-5 gain, however large. **Verdict: same-day domestic continuation is rejected for all four tested gateways** — one is scheduling-impossible (GAY), the other three fail on arrival-quality/safety even though technically bookable.

---

## 3. THE STRONGEST VERSION OF THE HYPOTHESIS: DOES ENDING NEAR DELHI (KUMAON-LAST) SAVE A NIGHT?

This is worth separating from §2, because it doesn't require a same-day flight — it only requires reordering so Kumaon (not Tiruvannamalai/Chennai) is the world visited immediately before the final Delhi night.

**The arithmetic case for it**: Kumaon's exit is already a single sleepable overnight train to Delhi (currently 15013-pattern/12039+hotel). If Kumaon were the *last* content world, that same overnight train could arrive Delhi on the morning of what is already the locked final-Delhi-night day — in principle eliminating the need for a separate Chennai-style buffer night, since the night train itself absorbs the transfer.

**Why this loses anyway — a real, quantified safety cost, not a preference**: this project's own research this session repeatedly and independently documented that the Delhi–Kumaon rail corridor is **systemically exposed to north-Indian winter fog** in December/January (IMD-documented dense/very-dense fog events, GPS Fog Safe Device deployment on this exact network). The incumbent deliberately places all three of its fog-exposed rail edges (15013, 15014/12039, 12988) **early in the trip, where 20+ days of downstream slack exist to absorb a delay**, and deliberately places its most reliable, highest-frequency edges (dense daily CCU–MAA and MAA–DEL nonstops) **last, immediately before the irreversible AI155 departure, where no slack remains**. A Kumaon-last reorder would invert this: it would put the single **most fog-exposed edge in the entire trip** in the one position with **zero downstream recovery capacity** — directly before an international flight. That is a straightforward regression on objective-function tier 2, which outranks the "saves one night" benefit on tier 5/8. **Rejected — not because ending near Delhi is a bad idea in principle, but because this specific trip's fog-exposed edge belongs early, and reordering to capture the 1-night saving requires moving it late.**

This also directly answers the task's "FREE_SURPLUS_NIGHT" instruction: **no such free night was found once safety is not silently dropped.** The apparent 1-night saving is not free — it is bought by relocating the trip's worst weather risk to its least recoverable position.

---

## 4. EIGHT-PLUS ROUTE FAMILIES TESTED

| # | Family | Verdict | Reason (see also `7a26da3` for families already fully detailed) |
|---|---|---|---|
| 1 | **Incumbent** | **BEST** | Unchanged from prior pass; survives every new test in this pass too |
| 2 | Substantially reversed | REJECTED | Prior pass (`7a26da3` §D) — worst arrival AND worst departure-week quality simultaneously |
| 3 | Same-day DEL→MAA | REJECTED | §2b — arrival-quality/safety failure, no fallback |
| 4 | Same-day DEL→CCU | REJECTED | §2b — same failure mode |
| 5 | Same-day DEL→VNS | REJECTED | §2b — same failure mode |
| 6 | Same-day DEL→GAY | REJECTED — impossible | §2a — no schedulable flight exists |
| 7 | Agra-first/near-first | REJECTED | Duplicates the Delhi corridor immediately after arrival, worsens first-72h jetlag quality — same class of problem as the reverse family, already established in `FINAL_TRIP_TOPOLOGY_CALENDAR_OPTIMIZATION_2026-09-07.md` §3.2 |
| 8 | Agra-last/near-final | REJECTED | Prior pass (`7a26da3` §D) — thin/intermittent Agra air service, or a duplicated Delhi bridge, for no time saved |
| 9 | **Kumaon-last (end near Delhi)** | REJECTED | §3 — inverts the trip's deliberate fog-risk ordering, moving the worst weather exposure to the least recoverable position |
| 10 | Train-heavy (force rail on VNS–CCU, CCU–MAA) | REJECTED | Prior pass — 10h+/26h+ rail vs. 1–2h flight, decisive tier-3 loss |
| 11 | Flight-heavy (Pantnagar for Kumaon) | REJECTED | Prior pass — thin service, no sleep-conversion benefit |
| 12 | Mixed/hybrid (= the incumbent itself) | **CONFIRMED BEST** | Already the correctly-selected hybrid |

---

## 5. TOP 5 FINALISTS

| Rank | Candidate | 33/33 | Flights | Heavy days | Fragile edges | Key cost |
|---|---|---:|---:|---:|---|---|
| 1 | **Incumbent** | 33/33 | 3–4 | 1–2 | 30 Dec Delhi bridge (mitigated), 29 Dec Kumaon exit (mitigated by 12039) | none unresolved |
| 2 | Kolkata-before-Varanasi | 33/33 achievable | 5 | similar | thin Gaya–Kolkata flight | worse flight density, no offsetting benefit |
| 3 | Kumaon-last | 33/33 achievable, nominally 1 night lighter | 3–4 | similar | **the trip's single fog-exposed edge, now unbuffered before AI155** | trades 1 night for materially worse international-departure safety |
| 4 | Same-day VNS continuation | 33/33 achievable on paper | 4 | +1 (day-1 itself becomes a heavy day) | **AI156 itself, now with no missed-connection fallback on day one** | arrival-quality/safety regression from hour one |
| 5 | Reverse/south-first | 33/33 achievable | 4–5 | more | worst arrival AND departure-week quality | loses on two tiers simultaneously |

---

## 6. SIDE-BY-SIDE: INCUMBENT VS. STRONGEST CHALLENGER (KUMAON-LAST)

| Measure | Incumbent | Kumaon-last |
|---|---|---|
| Physical nights | 33 | 33 (or 32 + 1 `FREE_SURPLUS_NIGHT` if the Chennai-equivalent buffer is genuinely dropped) |
| Fog-exposed edge position | Early (19 Dec, 29 Dec, 31 Dec) — 20+ days of downstream slack | Late (final week) — zero downstream slack before AI155 |
| Pre-AI155 buffer quality | Dense, multi-carrier, multiple-nonstop-per-day flight corridor (CCU–MAA, MAA–DEL) | Single overnight rail service, weather-exposed |
| Net verdict | **Safer**, costs 1 extra accommodation night | **Cheaper by 1 night**, materially less safe at the one point that cannot be recovered from |

**Exact accounting of what the challenger would gain/lose**: +1 physical night of genuine flexibility (or content), traded directly against removing the international-departure protection this entire project has spent significant effort building. Per the Mark-specified lexicographic objective function (safety above cost/convenience), this is not a close call.

---

## 7. REQUIRED VERDICTS

**AGRA VERDICT**: Agra is *not* the time sink it may appear to be. It functions efficiently as a bridge specifically because its onward Agra Fort↔Gaya leg is an overnight sleeper that converts distance into rest, and its Delhi-side leg (Gatimaan, ~1h40) is short and dense. Agra-first, Agra-last, and flying to/from Agra were all tested and rejected (§4, and `7a26da3` §D) — the incumbent's mid-route placement, immediately bridging Kumaon-exit to Bodh Gaya-entry, is the efficient placement, not an inefficiency to fix.

**SAME-DAY DEL DOMESTIC CONTINUATION VERDICT**: Rejected for all four tested gateways. GAY is schedule-impossible; VNS/CCU/MAA are technically bookable but fail on arrival-quality and missed-connection safety grounds before any waking-hours benefit can even be assessed, per the lexicographic objective function's own ordering.

**TRAIN↔FLIGHT SWAP**: None indicated, in either direction, confirming the prior pass.

**DOES THIS CHANGE THE B3/T4 vs. B2/T5 CONCLUSION?** No. Topology and duration are independent variables here — nothing in this route-order analysis touches the Bodh Gaya/Tiruvannamalai night-count question, which remains governed by the separate waking-hours stress tests already reconciled on PR #23.

**FALSIFICATION — STRONGEST ARGUMENT AGAINST THIS RESULT**: If a specific, confirmed, non-fog-season year showed the Kumaon–Delhi winter rail corridor running with negligible disruption, the Kumaon-last family's safety objection would weaken considerably and the 1-night saving could become genuinely attractive. This project does not have that evidence for the actual travel dates (Dec 2026/Jan 2027 specifics are `LIVE_RECHECK_LATER`), so the objection stands on the best currently-available evidence (historical IMD winter-fog documentation for this exact corridor), not on a certainty about this specific winter.

**FINAL VERDICT: KEEP INCUMBENT.** No reordering, partial or major, outperforms it once safety is weighted as Mark's own objective function specifies.

---

## SOURCES

- DEL–GAY frequency/schedule: [ixigo DEL–GAY](https://www.ixigo.com/cheap-flights/new-delhi-gaya-del-gay), [FlightsFrom DEL–GAY](https://www.flightsfrom.com/DEL-GAY).
- DEL–VNS/DEL–CCU frequency: [Air India DEL–VNS](https://www.airindia.com/en/book-flights/delhi-to-varanasi-flights), [MakeMyTrip DEL–CCU](https://www.makemytrip.com/flights/new_delhi-kolkata-cheap-airtickets.html).
- Agra airport service level, winter fog corridor documentation: carried forward from `GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_CCI_RESULT_2026-09-09.md` (commit `7a26da3`) and this session's earlier IMD/rail research.

END

# FINAL EXACT 33-SLOT BOOKING-CALENDAR — CANDIDATE

Date: 2026-09-07

Worker branch: `worker/final-route-calendar-optimizer`

Executed by: CCI, per `CCI_TASK — FINAL EXACT 33-SLOT BOOKING-CALENDAR SOLVER`, PR #23.

**BOOKING PHASE OPENS ONLY AFTER FINAL CALENDAR LOCK.** Nothing in this document is a booking instruction.

Builds directly on, and does not re-derive, `runs/active/FINAL_BOOKABLE_DAY_CALENDAR_LOCK_PASS_2026-09-07.md` (commit `483b34c`) and its own inputs (topology, dated calendar, live-recheck register, execution-readiness audit, `decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md`, CCI_RESULT `5571634572`). No new web research was performed; this is arithmetic/logic closure on already-established facts.

---

## 1. THE 12-CELL MATRIX (2 Kumaon orders × 3 Kolkata durations × 2 Bodh Gaya durations)

| # | Kumaon order | Bodh Gaya | Kolkata | Committed slots | Spare | Result |
|---:|---|---:|---:|---:|---:|---|
| 1 | Nainital→Dunagiri→Haidakhan (**Order 1**) | 2 | 2 | 31 | 2 | SURVIVES — thin Kolkata content, most robust |
| 2 | Order 1 | 2 | 3 | 32 | 1 | **SURVIVES — RECOMMENDED CANDIDATE** |
| 3 | Order 1 | 2 | 4 | 33 | 0 | SURVIVES — richest content, buffer eliminated (MARGINAL) |
| 4 | Order 1 | 3 | 2 | 32 | 1 | SURVIVES — **identical downstream dates to #2** |
| 5 | Order 1 | 3 | 3 | 33 | 0 | SURVIVES — **identical downstream compression to #3** |
| 6 | Order 1 | 3 | 4 | 34 | -1 | **ELIMINATED — does not fit envelope** |
| 7 | Nainital→Haidakhan→Dunagiri (**Order 2**) | 2 | 2 | 31 | 2 | **ELIMINATED — Kumaon order loses (see below)** |
| 8 | Order 2 | 2 | 3 | 32 | 1 | **ELIMINATED — Kumaon order loses** |
| 9 | Order 2 | 2 | 4 | 33 | 0 | **ELIMINATED — Kumaon order loses** |
| 10 | Order 2 | 3 | 2 | 32 | 1 | **ELIMINATED — Kumaon order loses** |
| 11 | Order 2 | 3 | 3 | 33 | 0 | **ELIMINATED — Kumaon order loses** |
| 12 | Order 2 | 3 | 4 | 34 | -1 | ELIMINATED — Kumaon order loses AND arithmetic fails |

### Elimination reasons

**Cells 7–12 (Order 2, all six): eliminated on the Kumaon axis alone**, independent of Bodh Gaya/Kolkata choice. Kumaon internal order does not change slot counts or trip length — it only changes which days visit Dunagiri vs. Haidakhan — so this is a single blanket elimination, not six separate ones. Reason (from `FINAL_BOOKABLE_DAY_CALENDAR_LOCK_PASS_2026-09-07.md` §2, itself built on `KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md`): Order 2 puts the heaviest-adaptation ashram world (Haidakhan) forward in the sequence, then ends deep in the eastern highlands (Dunagiri/Kukuchina) requiring a longer descent immediately before the 29–30 Dec night train, and reverses the natural west→east progression that Order 1 preserves. Exact kilometre data for the Dunagiri↔Haidakhan road remain genuinely conflicted, but this does not decide the case — whole-human sequencing does, and it is unambiguous.

**Cell 6 and Cell 12 (Bodh Gaya 3 + Kolkata 4): eliminated on arithmetic alone.** 34 committed slots against a fixed 33-slot envelope; -1 spare cannot be absorbed without shortening a locked duration (Varanasi 8n, Tiruvannamalai 5n) or the final-Delhi lock, none of which are open for renegotiation without a fresh, explicit Mark reopening. Not offered as a choice.

**Cells 1, 3, 4, 5 (all under Order 1): survive but are dominated or trade-off cells, not eliminated.** Kept in the candidate set because they represent genuine Mark-facing trade-offs (content depth vs. flight-safety buffer), not planning errors. See §2.

Net result: **6 of 12 cells eliminated outright** (all of Order 2, plus Cell 6/12's arithmetic failure); of the remaining 6 (all Order 1), two pairs collapse onto identical downstream dates (Cell 2≡Cell 4, Cell 3≡Cell 5), leaving **3 practically distinct downstream-date patterns** plus Cell 1 as a fourth genuinely different pattern — matching `FINAL_BOOKABLE_DAY_CALENDAR_LOCK_PASS_2026-09-07.md` §3 exactly.

---

## 2. RECOMMENDED CANDIDATE VARIANT

**Cell 2 (= Cell 4): Kumaon Order 1, Bodh Gaya 2 nights (default), Kolkata 3 nights.**

This is the already-committed baseline from `FINAL_TRIP_DATED_CALENDAR_2026-09-07.md` — no change is being proposed. It is recommended over the alternatives because:
- vs. Cell 1 (Kolkata 2n): Cell 2 gives a full second protected Kolkata day (room for the core anchors plus one more candidate) at the cost of only one Chennai-buffer night instead of two — a small, currently-accepted robustness cost for materially better content.
- vs. Cell 3/5 (Kolkata 4n or Bodh 3n+Kolkata 3n): Cell 2 keeps the Chennai-positioning buffer intact, avoiding the same-day Tiru→Chennai→flight→Delhi compression that removes all slack immediately before AI155.
- Bodh Gaya stays at its default 2 nights because no named trigger (12988 arriving after ~10:30, or a proven Bodh Gaya programme) has fired; 3 nights remains a live conditional, not a preference choice.

---

## 3. FULL 33-SLOT TABLE — RECOMMENDED CANDIDATE (Cell 2)

Reproduced in full per the task's requirement for one self-contained exact table (source of record remains `FINAL_TRIP_DATED_CALENDAR_2026-09-07.md`; no values changed here).

| # | Date | Where Mark sleeps / night-train | Day function | Transfer | Buffer |
|---:|---|---|---|---|---|
| 1 | Sat 19 Dec | 15013 Ranikhet Express (Gurugram→Kathgodam) | AI156 arrives 10:15 → hotel/dayroom recovery → Nirmal Dham [A+] → evening boarding | car + overnight rail, target 1A | no slack after boarding; dayroom recovery protected |
| 2 | Sun 20 Dec | Hotel Evelyn, Nainital | Kathgodam arrival ~05:05 → hotel ~06:15–06:45 → decompression only | pre-arranged car, 35km/1–1.5h | recovery day, not a checklist day |
| 3 | Mon 21 Dec | Hotel Evelyn, Nainital | protected: Naini Lake loop + Hanuman Garhi/Maharajji-kuti | local car/walk | protected full day |
| 4 | Tue 22 Dec | Hotel Evelyn, Nainital | protected: Kainchi Dham + Bhumiadhar | return car ~45–70min each way | no luggage move |
| 5 | Wed 23 Dec | Dunagiri Retreat | transfer day, arrive in daylight | private car ~100–140km/4–5h | no forced programme on arrival |
| 6 | Thu 24 Dec | Dunagiri Retreat | protected: Mahavatar Babaji's Cave + Babaji Smriti Bhavan + Dunagiri Vaishnavi Temple | local car + mountain walk | protected full day |
| 7 | Fri 25 Dec | Dunagiri Retreat | protected: YSS Dwarahat | return local car | protected full day |
| 8 | Sat 26 Dec | Haidakhan Vishwa Mahadham | depart 08:30–09:00, arrive 13:00–14:30, enter ashram rhythm | private car ~160km/4.5–5.5h | humane afternoon arrival |
| 9 | Sun 27 Dec | Haidakhan Vishwa Mahadham | protected ashram day 1/2 | none beyond ashram | protected full day |
| 10 | Mon 28 Dec | Haidakhan Vishwa Mahadham | protected ashram day 2/2 | none beyond ashram | protected full day |
| 11 | Tue 29 Dec | 15014 Ranikhet Express (Haldwani/Kathgodam→Delhi Cantt) | depart after breakfast, large rail margin | private car 2.5–3.5h + overnight rail, target 1A | several hours station margin |
| 12 | Wed 30 Dec | Agra hotel | 05:03 Delhi Cantt arrival → Nizamuddin transfer → 12050 Gatimaan 08:10 → Agra ~09:50–10:05 | cross-Delhi car + daytime train | ~3h scheduled bridge; **MARGINAL — later train/road fallback exists** |
| 13 | Thu 31 Dec | 12988 Ajmer–Sealdah (Agra Fort→Gaya) | Taj Mahal early opening (Thursday, open) → rest → 18:45 boarding | local car + overnight rail, target 1A | large post-Taj margin |
| 14 | Fri 1 Jan | Maya Heritage, Bodh Gaya | 07:50 Gaya arrival → hotel ~08:30–09:00 → Mahabodhi Temple as energy permits | pre-arranged car ~30–45min raw | inbound day counts; no brittle morning booking |
| 15 | Sat 2 Jan | Maya Heritage, Bodh Gaya | protected Bodh Gaya day | local walk/car | protected full day |
| 16 | Sun 3 Jan | Sahi River View, Varanasi | Gaya Jct → 20887 Vande Bharat 09:55 → Varanasi 13:00 → hotel | car + daytime rail | inbound day = Varanasi day 1 |
| 17 | Mon 4 Jan | Sahi River View, Varanasi | protected Varanasi/Sarnath day 2 | local | protected full day |
| 18 | Tue 5 Jan | Sahi River View, Varanasi | protected day 3 | local | protected full day |
| 19 | Wed 6 Jan | Sahi River View, Varanasi | protected day 4 | local | protected full day |
| 20 | Thu 7 Jan | Sahi River View, Varanasi | protected day 5 | local | protected full day |
| 21 | Fri 8 Jan | Sahi River View, Varanasi | protected day 6 | local | protected full day |
| 22 | Sat 9 Jan | Sahi River View, Varanasi | protected day 7 | local | protected full day |
| 23 | Sun 10 Jan | Sahi River View, Varanasi | protected day 8 / final Varanasi night | local | departs before Makar Sankranti peak |
| 24 | Mon 11 Jan | Kolkata/Dakshineswar core | hotel → airport → VNS–CCU nonstop → light arrival only | car + direct flight | Belur museum closed Monday — none scheduled today |
| 25 | Tue 12 Jan | Kolkata/Dakshineswar core | protected: Dakshineswar Kali Temple + YSS Dakshineswar + Belur Math | local car/metro/ferry | protected full day 1 |
| 26 | Wed 13 Jan | Kolkata/Dakshineswar core | second protected Kolkata day; non-core content pending Mark grading | local car/metro/ferry | protected full day 2; last night before Gangasagar peak window |
| 27 | Thu 14 Jan | Tiruvannamalai base | CCU–MAA nonstop → private car → Tiruvannamalai | direct flight + car, 175km/3.5–4.5h | full travel day; departs before Gangasagar peak |
| 28 | Fri 15 Jan | Tiruvannamalai base | protected local day 1 (Sri Ramanasramam, Pongal period) | local | protected full day |
| 29 | Sat 16 Jan | Tiruvannamalai base | protected local day 2 (Mattu Pongal) | local | protected full day |
| 30 | Sun 17 Jan | Tiruvannamalai base | protected local day 3 (Kaanum Pongal/weekend) | local | protected full day |
| 31 | Mon 18 Jan | Tiruvannamalai base | protected local day 4 / final hotel night | local | protected full day |
| 32 | Tue 19 Jan | Chennai-airport positioning hotel | relaxed checkout → road → rest; no same-day flight dependency | private car 175km/3.5–4.5h | **the single movable spare — deployed here** |
| 33 | Wed 20 Jan | Delhi/IGI airport-side hotel | morning MAA–DEL nonstop → hotel → repack/rest | direct flight ~2h55 airborne | ~1-day international buffer before AI155 |
| — | Thu 21 Jan | international flight | AI155 departs 12:20 Delhi→Amsterdam | short pre-arranged transfer | terminal ~09:20 unless airline directs otherwise |

---

## 4. CLOSING NIGHT-COUNT PROOF

| Component | Nights | Running total |
|---|---:|---:|
| Delhi–Kumaon overnight rail (Slot 1) | 1 | 1 |
| Nainital (Slots 2–4) | 3 | 4 |
| Dunagiri (Slots 5–7) | 3 | 7 |
| Haidakhan (Slots 8–10) | 3 | 10 |
| Kumaon–Delhi overnight rail (Slot 11) | 1 | 11 |
| Agra (Slot 12) | 1 | 12 |
| Agra–Gaya overnight rail (Slot 13) | 1 | 13 |
| Bodh Gaya (Slots 14–15) | 2 | 15 |
| Varanasi (Slots 16–23) | 8 | 23 |
| Kolkata (Slots 24–26) | 3 | 26 |
| Tiruvannamalai (Slots 27–31) | 5 | 31 |
| Chennai positioning (Slot 32) | 1 | 32 |
| Final Delhi (Slot 33) | 1 | **33** |

**33 physical overnight slots, 33 table rows (#1–#33), zero duplicated dates, zero gaps.** 19 Dec (arrival) through 20 Jan (last hotel night) inclusive = 33 calendar nights; 21 Jan is the departure day itself (AI155 12:20), correctly shown as a row with no assigned overnight slot. Every check-in date in the table equals the check-out date of the immediately preceding row; no base is entered before its predecessor's transfer day and none is exited after its stated departure slot.

---

## 5. REMAINING MARK GATE(S) — CANDIDATE → FINAL LOCKED

**Exactly ONE real Mark gate: Kolkata duration (2, 3, or 4 nights).**

This single choice selects between Cell 1, Cell 2 (recommended), or Cell 3/5 in §1 and fully determines Slots 24–33 (Kolkata through final Delhi). All of Slots 1–23 are unaffected by it and do not wait on it.

Bodh Gaya's 2-vs-3-night sensitivity is **not** counted as a second gate: it is not an open preference Mark needs to choose now, but an existing trigger-conditional rule (fires only if 12988 arrives after ~10:30 or a specific Bodh Gaya programme is proven worth it) that resolves itself operationally closer to the date, per the current-default logic already in force. If it does fire, it consumes the same spare-capacity unit as one Kolkata night would (§1, Cells 4/5 vs. 2/3) and the calendar already shows the resulting merged outcome — no separate advance decision is required from Mark today.

**BOOKING PHASE OPENS ONLY AFTER FINAL CALENDAR LOCK.**

END

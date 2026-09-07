# FINAL BOOKABLE CALENDAR — INDEPENDENT CHECK

Date: 2026-09-07  
Role: `INDIA-FINAL-BOOKABLE-CALENDAR-INDEPENDENT-CHECK`  
Branch: `worker/final-bookable-calendar-independent-check`  
Status: **COMPLETE**  
VERDICT: **PASS_WITH_CORRECTIONS**

## 0. Executive conclusion

The recommended 33-slot baseline is arithmetically sound: **33 distinct physical overnight slots from the night of 19 Dec 2026 through the night of 20 Jan 2027, with no missing or duplicated night**. All hard Mark locks checked here remain intact: Nainital 3n, Dunagiri 3n, Haidakhan 3n / 2 full quiet days, Agra 1n, Varanasi 8n, Tiruvannamalai 5n, final Delhi exactly 1n. Puri, Serampore trip-world and Vrindavan/Braj remain FINAL OUT. No grades are changed or invented.

The independently preferred internal Kumaon order remains:

`Nainital -> Kainchi/Bhumiadhar -> Dunagiri/Kukuchina -> Haidakhan Vishwa Mahadham -> rail gateway`.

The recommended operating cell also remains **Bodh Gaya 2 nights + Kolkata 3 nights**. It preserves the dedicated Chennai-airport positioning night on 19 Jan and final Delhi night on 20 Jan before AI155 on 21 Jan.

However, the later pre-booking lock pass contains several material date/booking statements that need correction before Mark books against it. The most important are:

1. **Belur Math's Ramakrishna Sangraha Mandira museum is closed on 12 January as National Youth Day, in addition to its Monday closure.** In the recommended 3-night Kolkata block, **13 Jan is therefore the first museum-open opportunity** under the currently published rule.
2. The 4-night Kolkata cell does **not** depart Kolkata on 14 Jan. If the fourth Kolkata *night* is 14 Jan, checkout/departure is **15 Jan 2027**, which is Makar Sankranti/Pongal. That is materially worse for Bengal/Tamil-Nadu crowd exposure.
3. Bodh Gaya 3 nights does not merely consume a spare invisibly: it shifts the 8-night Varanasi block to **4–11 Jan**, VNS→CCU to **12 Jan**, and therefore every downstream date by one day until another spare is consumed.
4. The 30 Dec rail bridge can be made materially less brittle without changing a single night: if the then-current timetable remains, alight 15014 at **Old Delhi (DLI) ~04:10** rather than continuing to Delhi Cantt ~05:03, then transfer to Hazrat Nizamuddin for 12050 at 08:10. This increases the scheduled bridge by ~53 minutes and avoids riding farther away before the cross-Delhi transfer.
5. In zero-Chennai-buffer cells (Bodh2+Kolkata4 or Bodh3+Kolkata3), a **morning** MAA→DEL flight on 20 Jan is no longer compatible with a humane final Tiruvannamalai night: Tiruvannamalai→MAA road + flight must happen that same day. The flight *date* stays 20 Jan, but the safe time-of-day changes materially.

These are corrections to execution logic, not grounds for a new macro-route optimization. The baseline itself remains usable after the corrections below.

---

## 1. Scope and controlling inputs

Read and reconciled before this check:

- `runs/active/FINAL_BOOKABLE_CALENDAR_INDEPENDENT_CHAT_TASK_2026-09-07.md`
- `worker/final-route-calendar-optimizer:runs/active/FINAL_TRIP_TOPOLOGY_CALENDAR_OPTIMIZATION_2026-09-07.md`
- `worker/final-route-calendar-optimizer:runs/active/FINAL_TRIP_DATED_CALENDAR_2026-09-07.md`
- `worker/final-route-calendar-optimizer:runs/active/FINAL_BOOKABLE_DAY_CALENDAR_LOCK_PASS_2026-09-07.md`
- `decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md`
- `worker/final-execution-readiness-audit` commit `cb4f0d917d5fbdfe930464e7be1bba332e000f51`, `runs/active/FINAL_EXECUTION_READINESS_NO_SURPRISES_AUDIT_2026-09-07.md`
- PR #23 CCI_RESULT comment `5571634572`
- PR #23 WORK_TASK comment `5571701657`
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md`

This check does **not** reopen the macrospine and does **not** create a new Mark decision beyond the already-open Kolkata-duration gate.

---

## 2. Independent 33-slot arithmetic proof

Trip-night envelope is the night of **Sat 19 Dec 2026** through the night of **Wed 20 Jan 2027**, inclusive. The next calendar day, Thu 21 Jan, is the international departure day and is not an India overnight slot.

Independent count of the recommended baseline:

| Component | Physical slots |
|---|---:|
| Delhi/Kumaon overnight rail, 19 Dec | 1 |
| Nainital | 3 |
| Dunagiri | 3 |
| Haidakhan | 3 |
| Kumaon/Delhi overnight rail, 29 Dec | 1 |
| Agra hotel, 30 Dec | 1 |
| Agra/Gaya overnight rail, 31 Dec | 1 |
| Bodh Gaya | 2 |
| Varanasi | 8 |
| Kolkata | 3 |
| Tiruvannamalai | 5 |
| Chennai-airport positioning | 1 |
| Final Delhi | 1 |
| **TOTAL** | **33** |

Result: **no duplicate overnight, no missing overnight, no hidden 34th night**.

A paid prior-night room at Hotel Evelyn, if later used purely to guarantee room access after the dawn train arrival, is an accommodation tactic rather than a physical sleep slot and must not be silently counted as an additional itinerary night.

---

## 3. Exact recommended 33-slot calendar

This is the independent recommended operating calendar after applying the corrections in this audit. It is the same macrospine and locked-duration structure as the prior baseline.

| Slot | Night/date | Base / overnight | Operational function |
|---:|---|---|---|
| 1 | Sat 19 Dec 2026 | 15013 Ranikhet Express, Gurgaon→Kathgodam | AI156 arrival/recovery/Nirmal Dham only if train margin remains protected; overnight rail |
| 2 | Sun 20 Dec | Nainital / Hotel Evelyn | dawn Kathgodam arrival; recovery/decompression |
| 3 | Mon 21 Dec | Nainital / Hotel Evelyn | protected Nainital local day |
| 4 | Tue 22 Dec | Nainital / Hotel Evelyn | Kainchi/Bhumiadhar Nainital-based day |
| 5 | Wed 23 Dec | Dunagiri Retreat | daylight-led transfer; settle |
| 6 | Thu 24 Dec | Dunagiri Retreat | protected cave/Kukuchina/Dunagiri local day |
| 7 | Fri 25 Dec | Dunagiri Retreat | protected YSS Dwarahat day; Christmas visitor-hours acceptance must be confirmed |
| 8 | Sat 26 Dec | Haidakhan Vishwa Mahadham | daylight mountain transfer / ashram arrival |
| 9 | Sun 27 Dec | Haidakhan Vishwa Mahadham | protected quiet/participation day 1 |
| 10 | Mon 28 Dec | Haidakhan Vishwa Mahadham | protected quiet/participation day 2 |
| 11 | Tue 29 Dec | 15014 Ranikhet Express, Kathgodam/Haldwani→Delhi | leave ashram after breakfast, large plains/rail margin; overnight rail |
| 12 | Wed 30 Dec | Agra hotel | **preferred correction:** alight 15014 at DLI if timetable still supports ~04:10, transfer to NZM, 12050 ~08:10→Agra ~09:50 |
| 13 | Thu 31 Dec | 12988 Ajmer–Sealdah Express, Agra Fort→Gaya | Taj Mahal early visit (Thursday/open), rest, ~18:45 overnight rail |
| 14 | Fri 1 Jan 2027 | Bodh Gaya / Maya Heritage | Gaya arrival; loose arrival day, no brittle morning commitment |
| 15 | Sat 2 Jan | Bodh Gaya / Maya Heritage | protected Bodh Gaya day |
| 16 | Sun 3 Jan | Varanasi / Sahi River View | default 20887 Gaya ~09:55→Varanasi ~13:00; first Varanasi night |
| 17 | Mon 4 Jan | Varanasi | protected day |
| 18 | Tue 5 Jan | Varanasi | protected day |
| 19 | Wed 6 Jan | Varanasi | protected day |
| 20 | Thu 7 Jan | Varanasi | protected day |
| 21 | Fri 8 Jan | Varanasi | protected day; **do not place Sarnath Museum here: Friday closure** |
| 22 | Sat 9 Jan | Varanasi | protected day |
| 23 | Sun 10 Jan | Varanasi | protected final full day/night |
| 24 | Mon 11 Jan | Kolkata/Dakshineswar | VNS→CCU; light arrival only; Belur museum Monday-closed |
| 25 | Tue 12 Jan | Kolkata/Dakshineswar | protected core day; **Belur museum also closed for National Youth Day**; likely special-programme/crowd day |
| 26 | Wed 13 Jan | Kolkata/Dakshineswar | protected core/remaining day; **first museum-open opportunity under published recurring rule** |
| 27 | Thu 14 Jan | Tiruvannamalai | CCU→MAA + private road transfer; Bhogi period, high-demand travel day |
| 28 | Fri 15 Jan | Tiruvannamalai | protected local day; Pongal/Makar Sankranti |
| 29 | Sat 16 Jan | Tiruvannamalai | protected local day; Mattu Pongal |
| 30 | Sun 17 Jan | Tiruvannamalai | protected local day; Kaanum Pongal |
| 31 | Mon 18 Jan | Tiruvannamalai | protected local day / final hotel night |
| 32 | Tue 19 Jan | Chennai-airport positioning hotel | relaxed Tiru checkout + 175-km-class road transfer; recovery/buffer |
| 33 | Wed 20 Jan | Delhi/IGI airport-side hotel | **morning MAA→DEL preferred in this baseline**; repack/rest; exactly one final Delhi night |
| — | Thu 21 Jan | AI155 DEL→AMS 12:20 | international departure; target airport arrival ~09:20 unless airline directs otherwise |

The weekday sequence independently checks out: 19 Dec is Saturday, 31 Dec Thursday, 1 Jan Friday, 3 Jan Sunday, 11 Jan Monday, 14 Jan Thursday, 20 Jan Wednesday and 21 Jan Thursday.

---

## 4. Kumaon internal order — independent verdict

Compared only the two allowed Nainital-first options:

### Option K1 — WINNER
`Nainital -> Kainchi/Bhumiadhar -> Dunagiri/Kukuchina -> Haidakhan -> rail gateway`

### Option K2
`Nainital -> Haidakhan -> Dunagiri/Kukuchina -> rail gateway`

**Winner: K1.**

Why:

- Both variants retain exactly 3 Nainital + 3 Dunagiri + 3 Haidakhan nights; no arithmetic advantage exists either way.
- Existing route research places the Dunagiri/Kukuchina↔true-Haidakhan movement in a long mountain-transfer class. Reversing its direction does not make that internal edge disappear.
- Ending with Haidakhan places the final mountain base materially closer to the Haldwani/Kathgodam/Lal Kuan rail gateway than ending in the eastern Dunagiri highlands, reducing the failure-coupled descent on rail day.
- K1 preserves the human sequence Mark already preferred: civilian lake decompression → pilgrimage/highland Kriya world → deep ashram immersion → plains rail.
- Exact true-Haidakhan entrance kilometres remain `LIVE_RECHECK_LATER`; the decision should **not** rest on a false precision claim such as “exactly 35 km” when official/secondary routing sources disagree.

No change to the dated baseline is required: it already uses K1 (Nainital 20–22 Dec, Dunagiri 23–25 Dec, Haidakhan 26–28 Dec).

---

## 5. Kolkata 2/3/4 nights × Bodh Gaya 2/3 nights — exact date matrix

To remove the source document's night/departure ambiguity, ranges below show **check-in → checkout**, with the number of hotel nights in parentheses.

| Cell | Bodh | Varanasi 8n | VNS→CCU | Kolkata stay | CCU→MAA / Tiru arrival | Tiruvannamalai 5n | Chennai positioning | Delhi 1n | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **A** | 2n (1→3 Jan checkout) | 3→11 Jan | 11 Jan | 11→13 Jan (**2n**) | 13 Jan | 13→18 Jan | 18→20 Jan (**2n**) | 20→21 Jan | **PASS**, but Kolkata compressed |
| **B** | **2n** | **3→11 Jan** | **11 Jan** | **11→14 Jan (3n)** | **14 Jan** | **14→19 Jan** | **19→20 Jan (1n)** | **20→21 Jan** | **PASS / RECOMMENDED** |
| **C** | 2n | 3→11 Jan | 11 Jan | 11→15 Jan (**4n**) | **15 Jan** | 15→20 Jan | **none** | 20→21 Jan | **MARGINAL**: no Chennai buffer + Sankranti/Pongal transfer |
| **D** | 3n (1→4 Jan checkout) | 4→12 Jan | 12 Jan | 12→14 Jan (**2n**) | 14 Jan | 14→19 Jan | 19→20 Jan (1n) | 20→21 Jan | **PASS**, but Kolkata compressed |
| **E** | 3n | 4→12 Jan | 12 Jan | 12→15 Jan (**3n**) | **15 Jan** | 15→20 Jan | **none** | 20→21 Jan | **MARGINAL**: no Chennai buffer + Sankranti/Pongal transfer |
| **F** | 3n | — | — | **4n** | — | — | — | — | **FAIL: 34 slots / -1 capacity; violates a lock if forced** |

### Independent arithmetic

- A = 31 committed + 2 spare nights, both naturally usable as Chennai positioning/recovery.
- B = 32 committed + 1 spare, used as Chennai positioning on 19 Jan.
- C = 33 committed + 0 spare; no Chennai positioning night.
- D = 32 committed + 1 spare, used as Chennai positioning on 19 Jan.
- E = 33 committed + 0 spare; no Chennai positioning night.
- F = 34 required; impossible within 33 without changing a locked duration.

### Important correction: what “4 Kolkata nights” means on the calendar

Cell C's fourth Kolkata night is **14 Jan**; therefore checkout and CCU→MAA travel are **15 Jan**, not 14 Jan. The same is true for Cell E. Current 2027 festival calendars place Bhogi/Lohri on 14 Jan and **Makar Sankranti/Pongal on Fri 15 Jan**, followed by Mattu Pongal 16 Jan and Kaanum Pongal 17 Jan. This means C/E place the longest east→south air/road arrival on the core Pongal/Sankranti date and simultaneously remove the Chennai positioning night.

Therefore C/E are not equivalent “just one extra content night” alternatives. They are objectively less robust at the trip's international-departure end.

### Kolkata museum consequence by cell

Belur Math's published museum rule says closed Monday and on listed holidays including **National Youth Day, 12 January**.

- A (11–12 Jan nights): only full day is 12 Jan; **museum closed**.
- B (11–13 Jan nights): full days 12 and 13; **13 Jan is the first ordinary museum-open opportunity**.
- C (11–14 Jan nights): museum opportunity 13/14 Jan under recurring rule.
- D (12–13 Jan nights): full day 13 Jan; museum can fit that day.
- E (12–14 Jan nights): museum opportunity 13/14 Jan.

This does not assign a new grade; it only corrects availability.

---

## 6. Bodh Gaya 2 vs 3 nights — sensitivity, not a new ballot

**2 nights remains the current default.** The existing project logic treats a third Bodh Gaya night as conditional, for example if 12988 reaches Gaya materially late or a specifically proven programme justifies consuming the spare. This audit does not turn that contingency into a new Mark choice.

But the booking consequence must be explicit:

- Bodh 2: hotel nights 1–2 Jan; Gaya→Varanasi 3 Jan; Varanasi nights 3–10 Jan; VNS→CCU 11 Jan.
- Bodh 3: hotel nights 1–3 Jan; Gaya→Varanasi 4 Jan; Varanasi nights 4–11 Jan; VNS→CCU 12 Jan.

Current 20887 pattern is **Sun, Mon, Wed, Thu, Fri, Sat — no Tuesday**. Both candidate travel dates happen to be valid under that current pattern: Sun 3 Jan and Mon 4 Jan 2027. Thus the Bodh sensitivity does not create a weekly-service contradiction, but exact future timetable/inventory still requires recheck.

Booking implication: the statement “all slots through the end of Varanasi are date-invariant” is true only with respect to the **Kolkata** choice, not with respect to the Bodh 2/3 sensitivity. Varanasi and VNS→CCU should therefore be booked with changeable/refundable terms if the Bodh-third-night contingency is to remain operationally real.

---

## 7. Rail-day independent check

All times below are **current timetable evidence as checked 7 Sep 2026**, not guarantees for Dec 2026/Jan 2027.

| Date | Proposed rail | Current pattern checked | Date logic | Rating / correction |
|---|---|---|---|---|
| 19→20 Dec | 15013 Ranikhet Express GGN ~20:02→KGM ~05:05 | daily; 1A/2A/3A/SL currently shown | Sat 19 Dec valid | **PASS WITH RULE**: do not let Nirmal Dham consume station margin |
| 29→30 Dec | 15014 Ranikhet Express KGM ~20:35→Delhi | daily; DLI ~04:10, DEC ~05:03 | Tue→Wed valid | **MARGINAL** due fog + connection; **prefer DLI alight** if timetable survives |
| 30 Dec | 12050 Gatimaan NZM ~08:10→AGC ~09:50 | Sun/Mon/Tue/Wed/Thu/Sat; no Friday | Wed 30 Dec valid | **PASS conditional on 15014**; later train/road fallback mandatory |
| 31 Dec→1 Jan | 12988 Ajmer–Sealdah AF ~18:45→Gaya ~07:50 | daily; 1A/2A/3A/SL classes currently shown | Thu 31 Dec valid | **PASS**; winter delay acceptable because Jan1 morning is deliberately loose |
| 3 Jan | 20887 Gaya ~09:55→Varanasi ~13:00 | Sun/Mon/Wed/Thu/Fri/Sat | Sun 3 Jan valid | **PASS** for Bodh2 |
| 4 Jan | same 20887 | same six-day pattern | Mon 4 Jan valid | **PASS** for Bodh3 contingency |

### 30 Dec cross-Delhi correction

The prior printed calendar carries 15014 to **Delhi Cantt ~05:03**, then transfers to Hazrat Nizamuddin for 12050 at ~08:10: ~3h07 scheduled station-to-station bridge before allowing for train delay.

Current 15014 timetable also stops at **Old Delhi (DLI) ~04:10–04:30**. If this persists when tickets are finalized, alighting there instead provides about **4h scheduled time to the 08:10 Gatimaan departure** and avoids remaining on the train for another ~53 minutes before starting the road transfer. This is a direct robustness improvement with no new hotel night and no route/world change.

It remains `MARGINAL`, not magically `PASS`: dense winter fog can produce multi-hour rail delay. The same-day fallback remains a later Delhi→Agra rail product or private road transfer.

### Rail booking windows

Indian Railways' normal ARP is currently 60 days excluding journey date. Rough normal-ARP opening dates for the proposed trains are:

- 19 Dec journey → ~20 Oct 2026
- 29 Dec → ~30 Oct
- 30 Dec → ~31 Oct
- 31 Dec → ~1 Nov
- 3 Jan → ~4 Nov
- 4 Jan contingency → ~5 Nov

Important nuance: official IRCTC Foreign Tourist Quota guidance states eligible international users with valid passports can book FTQ **up to 365 days in advance**. If booked beyond normal ARP, the berth is allocated later when PRS opens the normal ARP. Therefore “cannot book until T-60” is too categorical for Mark; FTQ can be used earlier if eligibility/account/quota/payment all work.

---

## 8. Domestic-flight independent check

### VNS→CCU

A direct edge currently exists via **IndiGo**; IndiGo's own route page states that it offers direct and connecting Varanasi–Kolkata flights. Current schedule aggregators show a recurring nonstop, but Jan 11/12 exact service time should not be treated as guaranteed yet. Air India's own current VNS→CCU page, by contrast, presently says it has **0 direct Air India flights**; do not label an Air India connection as nonstop.

- Bodh2 cells A/B/C: flight date **11 Jan**.
- Bodh3 cells D/E: flight date **12 Jan**.

Rating: **PASS AS ROUTE / LIVE_RECHECK EXACT FLIGHT**. Prefer changeable fare because the Bodh contingency shifts the date.

### CCU→MAA

Air India's live booking page already exposes Jan 2027 fares including **13, 14 and 15 Jan**, and the corridor has multiple nonstop operators. The route itself is therefore currently strongly bookable; the exact date depends on the chosen cell:

- A: 13 Jan
- B/D: 14 Jan
- C/E: 15 Jan

Rating: **PASS route availability**, but **WAIT for final date selection** before irreversible purchase.

### MAA→DEL

Air India's live booking page already exposes Jan 2027 fares including **20 Jan** and nonstop products. The date is invariant in every fitting cell: **20 Jan**.

But the **time-of-day is not invariant**:

- A/B/D retain ≥1 Chennai-airport positioning night: a **morning nonstop on 20 Jan** is operationally preferred and leaves the whole day as the domestic-flight fallback envelope.
- C/E have no Chennai positioning night: Mark would still be sleeping in Tiruvannamalai on the night of 19 Jan. A morning MAA departure would require an unreasonable/pre-dawn exit or effectively cutting the final locked Tiruvannamalai night. Those cells need a later 20 Jan flight after the 175-km-class road transfer, materially weakening international protection.

Thus: **do not buy the exact MAA→DEL flight time until the Kolkata/Bodh cell is known** even though 20 Jan itself is fixed.

---

## 9. Closures, festivals, crowds and winter weather

### Taj Mahal

Official Taj guidance: closed Fridays; open other normal days from 30 minutes before sunrise to 30 minutes before sunset. **Thu 31 Dec 2026 is compatible.** No correction to the Taj date is needed.

### Sarnath Museum

Official/ASI museum guidance: **closed Friday**. The locked Varanasi block contains Fri 8 Jan, so Sarnath Museum must be placed on another day. This does not require a route/date change because the block has multiple protected days.

### Belur Math museum

Official Belur Math museum page: closed Monday and listed holidays, including **National Youth Day (12 Jan)**. Therefore:

- Mon 11 Jan: closed by weekday.
- Tue 12 Jan: closed by listed holiday.
- Wed 13 Jan: first ordinary museum-open opportunity in the recommended B cell, subject to a future 2027 special notice.

The wider Belur Math campus has separate opening hours; museum closure must not be misreported as whole-campus closure.

### Gangasagar / Makar Sankranti

West Bengal government material confirms Gangasagar Mela is an annually managed major operation with Kolkata/river transit infrastructure. An exact 2027 government operating circular was not found in this check, so exact crowd-routing/traffic restrictions remain `LIVE_RECHECK_LATER`.

What **is** date-solid enough to matter now: Makar Sankranti/Pongal is observed on **Fri 15 Jan 2027** under the current 2027 festival calendar. Therefore C/E, which actually depart Kolkata on 15 Jan, are more exposed than the prior lock pass described.

### Pongal / Tiruvannamalai

Current 2027 calendar:

- Thu 14 Jan: Bhogi/Lohri period
- Fri 15 Jan: Pongal / Makar Sankranti
- Sat 16 Jan: Mattu Pongal
- Sun 17 Jan: Kaanum Pongal

The recommended B cell arrives Tiruvannamalai on **14 Jan** and then has protected local days 15–18 Jan. This is operationally better than C/E, which try to fly CCU→MAA and drive to Tiruvannamalai on 15 Jan itself.

Accommodation scarcity/ashram acceptance remains a bigger near-term execution risk than a closure contradiction: secure/flexibly hold the Tiruvannamalai stay early.

### Winter fog

Exact Dec/Jan fog cannot be known on 7 Sep. No future weather assertion is allowed to become a fake schedule fact. What can be concluded structurally:

- 30 Dec is the highest rail-connection fog exposure because 15014 feeds a same-morning interstation connection.
- 31 Dec 12988 can be late without destroying Jan1 because no brittle morning content is required.
- Jan20 morning MAA→DEL under A/B/D has same-day domestic fallback capacity before the final Delhi hotel; C/E do not.

Required live forecast trigger: **T-48h** for Delhi/north-India fog and affected train/flight operating status, with a broader T-7 schedule sweep.

---

## 10. Buffer audit

### Recommended B cell

- One explicit movable spare is deployed as **Chennai-airport positioning on 19 Jan**.
- Final Delhi is **exactly one night, 20 Jan**, as locked by Mark.
- AI155 departs 21 Jan 12:20.
- Domestic MAA→DEL can be taken in the morning of 20 Jan, leaving later same-day alternatives if the first service fails.

**Result: both the Chennai-positioning logic and the one-final-Delhi-night lock are respected.**

### A cell

Has two spare nights and can use both as Chennai/recovery positioning. Robust but Kolkata content is compressed to one protected full day.

### D cell

Has one Chennai-positioning night and remains structurally robust, but consumes the spare on Bodh rather than Kolkata.

### C/E cells

Final Delhi remains one night, but **the dedicated Chennai-positioning buffer is absent**. They therefore fail the same buffer standard as the recommended B cell even though they fit the raw 33-night arithmetic.

### F cell

Does not fit at all.

---

## 11. BOOK NOW / WAIT / LIVE_RECHECK_LATER

### BOOK NOW / SAFE TO REQUEST OR FLEXIBLY HOLD

These dates do not depend on the Kolkata 2/3/4 selection:

- **Nainital:** check-in/room access for 20 Dec, checkout 23 Dec; explicitly solve dawn room access.
- **Dunagiri Retreat:** 23→26 Dec (3 nights).
- **Haidakhan Vishwa Mahadham:** 26→29 Dec (3 nights); written acceptance request now.
- **Agra hotel:** 30→31 Dec (1 night).
- **Final Delhi airport hotel:** **20→21 Jan (exactly 1 night)** — invariant in every fitting cell.
- Rail architecture through Gaya: 15013 19 Dec, 15014 29 Dec, 12050 30 Dec, 12988 31 Dec — after reconfirming current timetable; FTQ can potentially be used now rather than waiting for normal ARP.

Bodh/Varanasi require a nuance rather than a false binary:

- **Bodh default:** reserve Maya Heritage 1→3 Jan on flexible terms; if maintaining the conditional third-night mechanism, seek a changeable/extendable booking for 3 Jan.
- **Varanasi:** default is 3→11 Jan for 8 nights, but Bodh3 would shift it to 4→12 Jan. Because the desired river-view subtype is scarce, reserve now if possible **with date-change/free-cancellation protection**, rather than pretending both date windows are identical.

### WAIT FOR KOLKATA DURATION / CELL BEFORE NON-REFUNDABLE LOCK

- Exact Kolkata hotel/guesthouse checkout date.
- Exact CCU→MAA date (13/14/15 Jan depending cell).
- Exact Tiruvannamalai check-in/check-out window.
- Chennai-airport hotel quantity/date (2 nights / 1 night / none depending cell).
- Exact **time** of MAA→DEL on 20 Jan; morning is the preferred product only when Chennai positioning exists.

Kolkata spiritual lodging inquiries can start **now** using the range and asking whether ±1 day adjustment is possible; that is not the same as making a non-refundable date lock.

### LIVE_RECHECK_LATER — REQUIRED TRIGGERS

- **Now / Sep:** Haidakhan acceptance; Dunagiri booking; YSS/Belur lodging inquiries; Tiruvannamalai fallback availability.
- **At rail purchase:** exact train timetable, station stops, classes, FTQ/normal-quota inventory; specifically verify DLI alighting on 15014 and 12050 08:10.
- **T-60-ish / when Jan schedules firm:** Kolkata/Belur/YSS event calendars; Sri Ramanasramam/Pongal programme; ferry/holiday operations.
- **T-30:** VNS→CCU, CCU→MAA and MAA→DEL schedule audit; Garpar/Bhrigu access steps from readiness audit.
- **T-14 to T-7:** Babaji Cave/YSS Dwarahat winter road/trail status; all drivers; train/flight schedule-change sweep.
- **T-72h before India arrival:** e-Arrival Card.
- **T-48h per fragile northern leg:** fog/weather/live-running status; especially 29/30 Dec rail bridge.

---

## 12. Exact downstream booking dates once Kolkata duration is selected

Assuming the existing **Bodh2 default** remains the operating plan:

### If Kolkata = 2 nights — Cell A

- VNS→CCU: 11 Jan
- Kolkata: 11→13 Jan
- CCU→MAA: 13 Jan
- Tiruvannamalai: 13→18 Jan (5n)
- Chennai airport: 18→20 Jan (2n)
- MAA→DEL: 20 Jan, morning preferred
- Delhi: 20→21 Jan (1n)
- Structural verdict: **PASS**, but Kolkata has only one protected full day and the Belur museum is closed that day (12 Jan).

### If Kolkata = 3 nights — Cell B / RECOMMENDED

- VNS→CCU: 11 Jan
- Kolkata: 11→14 Jan (3n)
- CCU→MAA: 14 Jan
- Tiruvannamalai: 14→19 Jan (5n)
- Chennai airport: 19→20 Jan (1n)
- MAA→DEL: 20 Jan, morning preferred
- Delhi: 20→21 Jan (1n)
- Structural verdict: **PASS / BEST BALANCE**.

### If Kolkata = 4 nights — Cell C

- VNS→CCU: 11 Jan
- Kolkata: 11→15 Jan (4n)
- CCU→MAA: **15 Jan**
- Tiruvannamalai: 15→20 Jan (5n)
- Chennai airport: **no positioning night**
- Tiruvannamalai→MAA road + MAA→DEL: **20 Jan same day**
- Delhi: 20→21 Jan (1n)
- Structural verdict: **MARGINAL / NOT BUFFER-EQUIVALENT**. It fits 33 nights but consumes the Chennai buffer and creates travel on Pongal/Makar Sankranti.

If the **Bodh3 conditional trigger** is actually activated, use D/E dates from Section 5; do not merely add a Bodh night while leaving Varanasi/Kolkata unchanged.

---

## 13. Highest-value corrections/additions — max 10

1. **Correct Belur Museum:** 12 Jan is closed for National Youth Day; 13 Jan is the first ordinary museum-open day in baseline B.
2. **Correct Kolkata4 checkout:** four nights 11–14 Jan means departure **15 Jan**, not 14 Jan.
3. **Correct festival exposure:** C/E transfer Kolkata→Chennai/Tiruvannamalai on **15 Jan Pongal/Makar Sankranti**, not before the peak date.
4. **Correct Bodh3 propagation:** Bodh3 shifts Varanasi to 4–11 Jan nights, VNS→CCU to 12 Jan, then Kolkata downstream.
5. **Strengthen 30 Dec rail bridge:** prefer alighting 15014 at **DLI ~04:10** rather than DEC ~05:03 if timetable survives; retain later-train/road fallback.
6. **Do not call 20887 daily:** current reliable schedule evidence is Sun/Mon/Wed/Thu/Fri/Sat; both 3 and 4 Jan 2027 happen to be valid.
7. **Do not treat normal ARP as the only booking path:** official IRCTC FTQ permits eligible international users to book up to 365 days ahead, with berth allocation deferred when outside normal 60-day ARP.
8. **Do not pre-book a morning MAA→DEL for every cell:** morning 20 Jan is compatible with A/B/D positioning; C/E need later same-day road+flight and are materially weaker.
9. **Carrier precision on VNS→CCU:** the current direct route is evidenced through IndiGo; Air India's current page says no direct Air India product. Exact Jan11/12 nonstop must be rechecked before purchase.
10. **Keep Sarnath Museum off Fri 8 Jan:** official museum rule is Friday closure; the 8-night Varanasi block has ample alternative days.

---

## 14. Final verdict

**VERDICT: PASS_WITH_CORRECTIONS.**

What passes:

- 33-slot arithmetic and weekdays;
- hard locked durations;
- final Delhi exactly one night;
- recommended Kumaon internal order;
- baseline Bodh2 + Kolkata3 calendar;
- Taj Thursday placement;
- current rail-day compatibility;
- current air-corridor bookability in the baseline;
- dedicated Chennai positioning in baseline B.

What must be corrected before treating the lock pass as booking truth:

- Belur Museum 12-Jan closure;
- 4-night Kolkata checkout/departure on 15 Jan;
- Bodh3's full downstream date shift;
- DLI rather than DEC as preferred 15014 alighting point for the 30-Dec bridge, subject to live timetable;
- variant-dependent MAA→DEL time-of-day;
- accurate 20887 six-day service and FTQ booking semantics.

**Recommended final operating cell remains B: Bodh Gaya 2n + Kolkata 3n.**

**Only remaining genuine Mark gate for the route calendar: Kolkata/Dakshineswar duration selection (2/3/4 nights), informed by the still-pending Kolkata content grading.** Bodh3 remains a conditional contingency, not a new Mark ballot.

No Mark grade, locked duration or FINAL OUT world was altered.

---

## 15. External evidence checked 2026-09-07

Primary/high-authority where available:

- Taj Mahal official visiting hours / Friday closure: https://tajmahal.gov.in/visiting-hours.aspx/
- Belur Math museum hours/holidays, including Monday + National Youth Day closure: https://belurmath.org/ramakrishna-sangraha-mandira-museum/
- Belur Math campus/guesthouse information: https://belurmath.org/our-location/
- Sarnath Museum official planning page: https://www.sarnathmuseumasi.org/planning-a-visit.html-1
- IRCTC Foreign Tourist Quota guidance: https://contents.irctc.co.in/en/ForeignTouristQuotaBooking.pdf
- Ministry of Railways / PIB normal 60-day ARP: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2065879
- IndiGo Varanasi→Kolkata route: https://www.goindigo.in/domestic-flights/varanasi-to-kolkata-flights.html
- Air India Kolkata→Chennai live booking route: https://www.airindia.com/en-in/book-flights/kolkata-to-chennai-flights
- Air India Chennai→Delhi live booking route: https://www.airindia.com/en-in/book-flights/chennai-to-delhi-flights
- West Bengal PHED Gangasagar Mela operations: https://wbphed.gov.in/en/pages/ganga-sagar-mela

Current timetable corroboration (volatile; not promoted to future guarantee):

- 15013 / 15014: India Rail Info / eRail / ConfirmTkt current timetable evidence
- 12050: eTrain / India Rail Info current timetable evidence
- 12988: eTrain / ixigo current timetable evidence
- 20887: eTrain / India Rail Info current timetable evidence

Calendar corroboration for 2027 festival dates:

- Drik Panchang 2027 Sankranti/Pongal calendar (secondary calendar authority; exact local event operations still require official later confirmation): https://www.drikpanchang.com/festivals/sankranti/sankranti-calendar.html

END

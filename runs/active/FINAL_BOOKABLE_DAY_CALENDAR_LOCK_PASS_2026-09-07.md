# FINAL BOOKABLE DAY CALENDAR — LOCK PASS

Date: 2026-09-07

Worker branch: `worker/final-route-calendar-optimizer`

Executed by: CCI, taking over `WORK_TASK — FINAL BOOKABLE DAY CALENDAR LOCK PASS` (PR #23 comment `5571701657`) per `CCI_TASK — TAKE OVER FINAL BOOKABLE DAY CALENDAR LOCK PASS` after WORK did not respond.

Inputs read in full:
- `runs/active/FINAL_TRIP_TOPOLOGY_CALENDAR_OPTIMIZATION_2026-09-07.md` (this branch, commit `cc34089`)
- `runs/active/FINAL_TRIP_DATED_CALENDAR_2026-09-07.md` (this branch, commit `cc34089`)
- `runs/active/FINAL_TRIP_LIVE_RECHECK_REGISTER_2026-09-07.md` (this branch, commit `cc34089`)
- `decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md` (central, commit `d3086db`)
- `runs/active/FINAL_EXECUTION_READINESS_NO_SURPRISES_AUDIT_2026-09-07.md` (`worker/final-execution-readiness-audit`, commit `cb4f0d9`)
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md` (central)
- PR #23 `CCI_RESULT` comment `5571634572`

This is **not** a new global route/macrospine optimization. The macrospine, all locked durations, and all excluded worlds are unchanged. This pass closes only what the task specification asked to close: Kumaon internal order, Kolkata 2/3/4-night downstream impact, Bodh Gaya 2/3 sensitivity, an integrated action calendar, and an explicit LOCKABLE-NOW/WAIT split.

---

## 1. CURRENT POSITION

**Already proven/closed, not reopened here:**
- Macrospine: Delhi/Kumaon → Agra → Bodh Gaya → Varanasi/Sarnath → Kolkata/Dakshineswar → Tiruvannamalai → Chennai/Delhi (three independent tests this session, all confirming).
- All locked durations except the two named sensitivities below (Nainital 3n, Dunagiri 3n, Haidakhan 3n/2 full days, Agra 1n, Varanasi 8n, Tiruvannamalai 5n, final Delhi exactly 1n).
- FINAL OUT: Puri, Serampore trip-world, Vrindavan/Braj.
- Final Delhi = 1 night is `LOCKED_BY_MARK` (`decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md`) and is **not reopened** anywhere in this pass.
- Taj Mahal Friday closure; Thu 31 Dec is safe.
- Belur Math museum Monday closure; 11 Jan (a Monday under any variant below) correctly excludes the museum from that day's plan.
- **Correction carried forward**: Sarnath Museum's weekly closure is now resolved by the execution-readiness audit as **Friday**, not Monday (official ASI source). This replaces the previously-unresolved flag from the last stress test. No Varanasi day in the current 8-night block needs to change because of this — it only matters for whichever specific day Sarnath Museum is scheduled, which remains an internal Varanasi-owner-file detail outside this pass's scope.

**Not yet closed, resolved or narrowed in this pass:**
- Kumaon internal order — **resolved below** (confirms the already-committed order; no calendar dates change).
- Kolkata true duration (2/3/4 nights) — **not closed**; this pass computes all three variants precisely so the choice is a clean Mark decision, not a research gap.
- Bodh Gaya 2 vs 3 nights — remains an existing conditional trigger-based sensitivity, not reopened as a fresh choice.
- Exact intercity rail/flight inventory — remains `LIVE_RECHECK_LATER`, unaffected by this pass.

---

## 2. KUMAON INTERNAL ORDER — RESOLVED

Two options, both already compared in prior work:

1. **Nainital → Kainchi/Bhumiadhar → Dunagiri/Kukuchina/Mahavatar Babaji's Cave → Haidakhan Vishwa Mahadham → rail gateway** (the order already embedded in the committed dated calendar).
2. Nainital → Kainchi/Bhumiadhar → Haidakhan Vishwa Mahadham → Dunagiri/Kukuchina/Mahavatar Babaji's Cave → rail gateway.

**Winner: Option 1 (unchanged from the committed calendar).** No calendar dates change as a result of this section; this closes the question the last CCI_RESULT flagged as open, rather than reopening the committed order.

Why it wins, using only already-quantified distances (no new web research needed):
- Dunagiri↔true Haidakhan Vishwa Mahadham is a road-only, ~161 km / ~3h43 raw-driving class transfer regardless of direction — the internal road cost is the same either way, so direction doesn't change trip length or add nights.
- Ending at Haidakhan (Option 1) leaves the ashram-to-rail-gateway exit (~35–40 km / <1.5h, per `KUMAON_NAINITAL_FIRST_TOPOLOGY_RECHECK_2026-09-05.md`) shorter than ending at Dunagiri and having to backtrack toward Haidakhan and then all the way back out — Option 2 both moves the heaviest-adaptation ashram world forward in the sequence and ends deep in the eastern highlands, requiring a longer descent immediately before the 29–30 Dec night train.
- Whole-human sequencing favours Option 1: lake recovery → Maharajji/Kriya highland pilgrimage → Haidakhan as the final, deepest, most rule-bound retreat block, immediately followed by rest on the night train — not the reverse.
- Exact kilometre data for the Dunagiri↔Haidakhan road remain genuinely conflicted between sources (as already flagged), but this does not change the decision: the tie-breaker is whole-human geometry (exit proximity + psychological progression), not the unresolved kilometre count, and both point the same way.

This is a confirmation, not a new lock: it matches what `FINAL_TRIP_DATED_CALENDAR_2026-09-07.md` already contains (Dunagiri 23–25 Dec, Haidakhan 26–28 Dec). Exact true-Haidakhan entrance routing and the Dunagiri→Haidakhan road class remain `LIVE_RECHECK_LATER` (unchanged).

---

## 3. KOLKATA 2 / 3 / 4-NIGHT VARIANTS — EXACT DOWNSTREAM IMPACT

The trip envelope is fixed (AI156 19 Dec arrival, AI155 21 Jan 12:20 departure, 33 slots total) and cannot move. Bodh Gaya's own 2-vs-3-night sensitivity shifts the Kolkata *start* date; Kolkata's own 2/3/4-night choice then shifts everything downstream of it. Two cells collapse onto the same downstream dates because the shifts cancel arithmetically — shown below rather than treated as 6 independent outcomes.

All three Kolkata variants assume Kolkata's spare capacity (where any exists) is deployed as **Chennai-airport positioning**, consistent with the already-adopted logic for the base case. This is the least disruptive default, not a new lock — see the note on Cell C/E below for why a different deployment would be worse, not better.

### 3a. Bodh Gaya = 2 nights (current default)

| Cell | Kolkata nights | Kolkata dates | Kolkata full protected days | Tiruvannamalai dates | Chennai-positioning nights | Final Delhi | Committed slots / spare |
|---|---:|---|---|---|---:|---|---:|
| A | 2 | Mon 11 – Tue 12 Jan | **1** (12 Jan only) | Wed 13 – Sun 17 Jan | Mon 18, Tue 19 Jan (2 nights) | Wed 20 Jan | 31 / **2** |
| B (**committed baseline**) | 3 | Mon 11 – Wed 13 Jan | **2** (12, 13 Jan) | Thu 14 – Mon 18 Jan | Tue 19 Jan (1 night) | Wed 20 Jan | 32 / **1** |
| C | 4 | Mon 11 – Thu 14 Jan | **3** (12, 13, 14 Jan) | Fri 15 – Tue 19 Jan | **none** | Wed 20 Jan (same day as Chennai) | 33 / **0** |

### 3b. Bodh Gaya = 3 nights (conditional fallback)

| Cell | Kolkata nights | Kolkata dates | Kolkata full protected days | Tiruvannamalai dates | Chennai-positioning nights | Final Delhi | Committed slots / spare |
|---|---:|---|---|---|---:|---|---:|
| D | 2 | Tue 12 – Wed 13 Jan | **1** (13 Jan only) | Thu 14 – Mon 18 Jan | Tue 19 Jan (1 night) | Wed 20 Jan | 32 / **1** — **identical downstream dates to Cell B** |
| E | 3 | Tue 12 – Thu 14 Jan | **2** (13, 14 Jan) | Fri 15 – Tue 19 Jan | **none** | Wed 20 Jan (same day as Chennai) | 33 / **0** — **identical downstream compression to Cell C** |
| F | 4 | — | — | — | — | — | 34 / **-1 — DOES NOT FIT.** Rejected outright; would require shortening a locked duration (Varanasi, Tiruvannamalai) or the Delhi lock. Not offered as an option unless Mark reopens a locked duration. |

### What content becomes possible per duration (no grades assigned here)

- **2 nights (Cells A/D) — 1 full protected day.** Realistically fits only the three already-graded core anchors: Dakshineswar Kali Temple [A+], Yogoda Satsanga Math Dakshineswar [A+], Belur Math [A] (ferry-linked, per prior geometry research). None of the 4 pending candidates (Balaram Mandir, Mayer Bari/Udbodhan, Vivekananda Ancestral House, Kamarpukur+Jayrambati) would fit without displacing a core anchor.
- **3 nights (Cell B, committed baseline) — 2 full protected days.** Comfortably fits the 3 core anchors plus room for roughly one additional nearby candidate (e.g. Balaram Mandir, Mayer Bari, or Vivekananda Ancestral House — all in the north/central Kolkata distance band per the deep-pass dossier). Kamarpukur+Jayrambati is a rural full-day excursion (~100 km) and would still consume an entire day on its own.
- **4 nights (Cells C/E) — 3 full protected days.** Fits the 3 core anchors plus up to 2 of the 4 pending candidates if geographically clustered, or the 3 core anchors plus the separate Kamarpukur+Jayrambati day.

### Why Cell C/E is rated MARGINAL, not just "0 spare"

Both collapse the Chennai-positioning buffer to **zero**: Tiruvannamalai checkout, the 175 km/3.5–4.5h road transfer to Chennai airport, the MAA→DEL domestic flight, and the final Delhi hotel arrival all have to land on the **same calendar day**, immediately before AI155. This is exactly the "compounding disruption" risk this session's stress test already identified as the trip's thinnest point — Cell C/E does not just remove a "nice-to-have" night, it removes the one mechanism currently protecting the international departure from an ordinary one-leg delay. Choosing 4 Kolkata nights (or 3 Kolkata + 3 Bodh Gaya) is a real trade-off between Kolkata content depth and international-flight robustness, not a free win — this must be surfaced to Mark as a trade-off, not silently defaulted either way.

---

## 4. BODH GAYA 2 vs 3 — SENSITIVITY (UNCHANGED, RESTATED FOR COMPLETENESS)

No new information; restated because the task requires it visible in this single document. 2 nights remains the default with useful early inbound; 3 nights remains conditional-only, triggered by a named event (e.g. 12988 arriving after ~10:30, or a specific proven Bodh Gaya programme worth the extra night) — not a fresh ballot. As shown in Section 3, choosing 3 nights here has the *same* downstream effect as adding one Kolkata night: it consumes exactly one unit of the shared spare-capacity pool.

---

## 5. RECOMMENDED 33-SLOT CALENDAR

**The committed baseline (Cell B: Bodh Gaya 2n, Kolkata 3n) remains the single recommended calendar** — this is unchanged from `runs/active/FINAL_TRIP_DATED_CALENDAR_2026-09-07.md`, reproduced there in full day-by-day form and not duplicated here to avoid drift between two copies of the same table. That file remains the calendar of record for Slots 1–33.

**Rows that change if Mark selects a different Kolkata duration** (all other rows, Slots 1–23 covering Delhi/Kumaon/Agra/Bodh Gaya/Varanasi, are identical in every cell):

| Slot range | Cell B (committed, Kolkata 3n) | Cell A (Kolkata 2n) | Cell C (Kolkata 4n) |
|---|---|---|---|
| Kolkata slots | Mon 11 – Wed 13 Jan | Mon 11 – Tue 12 Jan | Mon 11 – Thu 14 Jan |
| Tiruvannamalai slots | Thu 14 – Mon 18 Jan | Wed 13 – Sun 17 Jan | Fri 15 – Tue 19 Jan |
| Chennai-positioning slot(s) | Tue 19 Jan (1) | Mon 18 – Tue 19 Jan (2) | none |
| Final Delhi slot | Wed 20 Jan | Wed 20 Jan | Wed 20 Jan (same-day arrival after Chennai/flight) |
| AI155 | Thu 21 Jan 12:20 (unchanged in all cells) | unchanged | unchanged |

---

## 6. FRAGILE TRANSFERS — PASS / MARGINAL / FAIL

| Transfer | Rating | Whole-human burden | Fallback |
|---|---|---|---|
| 15013 Ranikhet Express, 19–20 Dec (Delhi→Kathgodam) | PASS | overnight rail, target 1A | several hours margin before any onward plan; 2A explicit fallback if 1A unavailable |
| 15014 Ranikhet Express, 29–30 Dec (Kumaon→Delhi Cantt) → cross-Delhi to Nizamuddin → 12050 Gatimaan 08:10 | **MARGINAL** | overnight rail + car + daytime train, ~3h scheduled bridge | later train/road fallback already named; this is a real cross-city fragility, not eliminated by any currently-committed alternative |
| 12988 Ajmer–Sealdah, 31 Dec–1 Jan (Agra→Gaya) | PASS | overnight rail, large post-Taj margin before boarding | 2A fallback if 1A unavailable; alternative overnight rail if service disrupted |
| 20887 Vande Bharat, 3 Jan (Gaya→Varanasi) | PASS | daytime rail, no overnight dependency | next humane direct rail if not running |
| VNS–CCU, 11 Jan | PASS (baseline) | direct flight, ~1h20 | same-day direct alternative |
| CCU–MAA, 14 Jan | PASS (baseline) | direct flight | multiple-carrier same-day fallback |
| Tiruvannamalai→Chennai road + MAA–DEL, 19–20 Jan (Cell B baseline: split across 2 days via Chennai positioning) | PASS | road (175km/3.5–4.5h) then flight, **on separate days** | ample slack from the positioning night |
| Same transfer **compressed into 1 day** (Cell C/E: Kolkata 4n or Bodh3+Kolkata3) | **MARGINAL** | road + flight + Delhi arrival, all same-day, immediately before AI155 | none — this is the trade-off itself; if adopted, the only fallback is releasing schedule margin from an earlier leg, which the "compounding disruption" finding already shows is thin |
| AI155 final departure, 21 Jan | PASS under Cell A/B; **weaker** under Cell C/E | international flight | Delhi hotel buffer intact under A/B; effectively zero slack under C/E |

**Correction to a prior audit item (GATE 2 in the execution-readiness audit):** that audit flagged an "uncommitted worker improvement" using train 12039 Shatabdi on 29 Dec as a materially different Kumaon-exit pattern requiring a decision before booking. A repo-wide search across every branch found **no such content anywhere** — it was never actually produced or committed by any worker, only described in a task dispatch. There is nothing to freeze a choice against. The committed 15013/15014/12050/12988 architecture (rated above) is the only real evidence and remains the baseline; GATE 2 as posed is closed by absence of a genuine alternative, not by a Mark decision.

---

## 7. CALENDAR/FESTIVAL/CLOSURE NOTES — MATERIAL ONLY

Unchanged from `FINAL_TRIP_TOPOLOGY_CALENDAR_OPTIMIZATION_2026-09-07.md` Section 2, with one correction:
- Taj Mahal closed Friday; Thu 31 Dec is safe (official, HIGH confidence).
- Belur Math museum closed Monday; 11 Jan is a Monday in every variant above — museum component should be scheduled on a Kolkata Tue/Wed day instead, which exists in Cells B/C/D/E (not in Cell A, which has only one full Kolkata day and cannot include the museum without dropping something else).
- **Corrected**: Sarnath Museum's weekly closure is **Friday**, per official ASI source (`runs/active/FINAL_EXECUTION_READINESS_NO_SURPRISES_AUDIT_2026-09-07.md` §6) — the earlier assumption of a Monday closure should not be repeated.
- Kalpataru Day (1 Jan, Cossipore Udyanbati) remains a known, named, deliberately-not-chased trade-off in every variant — capturing it would require breaking the locked Kumaon/Agra/Bodh Gaya geometry.
- Gangasagar/Makar Sankranti build-up: all Kolkata variants above depart Kolkata on or before 14 Jan (worst case, Cell C), still before the main mid-January peak.
- Pongal at Tiruvannamalai (~14–17 Jan) is touched by every variant's Tiruvannamalai window without needing adjustment.

---

## 8. INTEGRATED ACTION CALENDAR

Merged from `FINAL_EXECUTION_READINESS_NO_SURPRISES_AUDIT_2026-09-07.md` Section 10, condensed to what is route/date-relevant. Full detail (contacts, sources) remains owned by that file; this section exists so the day-by-day calendar and the booking triggers live in one place per the task requirement.

| Trigger | Action |
|---|---|
| **NOW (Sep 2026)** | passport/e-Visa; IRCTC international account + payment path; Haidakhan written stay request for 26–29 Dec; Dunagiri Retreat booking; Sahi River View exact river-view room; start YSS Dakshineswar/Belur accommodation inquiries on provisional dates |
| **By end Sep** | Mark grades the 4 pending Kolkata candidates; Mark selects Kolkata duration (2/3/4) using Section 3 above; secure Tiruvannamalai fallback lodging |
| **October** | freeze exact intercity rail products; **use IRCTC Foreign Tourist Quota (FTQ) — independently verified this session to allow up to 365 days' advance booking for foreign-passport travellers, materially earlier than the normal 60-day ARP most reference dates in the live-recheck register assume** — do not wait for the 60-day window by default; book/confirm domestic nonstop flight chain after calendar freeze |
| **~mid-Nov (T-60)** | Kolkata/Garpar Jan-2027 schedule checks; Belur/ferry festival-operating recheck; confirm travel insurance |
| **T-30** | Bhrigu Karyalaya appointment; Garpar Road access request; all domestic-flight schedule audit |
| **T-14 to T-7** | YSS Dwarahat/Babaji Cave winter access call; Garpar/Bhrigu reconfirm; drivers/ferry/train/flight schedule-change sweep |
| **T-72h** | e-Arrival Card |
| **T-48h** | Delhi/north-India fog outlook; AI156 status; first rail live-running; Kumaon road/driver reconfirmation |

---

## 9. LOCKABLE NOW vs WAIT

**Safe to lock/book now, in every Kolkata variant (A/B/C):**
- All Slots 1–23 (Delhi arrival through end of Varanasi) — completely unaffected by the Kolkata duration choice.
- 15013, 15014, 12988, 20887 rail products and the 12050 Gatimaan connection (subject to normal live-recheck for inventory/timing, not to the Kolkata decision).
- Kolkata **core-anchor access and base accommodation search** (Dakshineswar Kali Temple, YSS Dakshineswar, Belur Math; Dakshineswar–Belur spiritual-core lodging search) — these survive all three variants.
- Haidakhan, Dunagiri, Sri Ramanasramam accommodation requests.
- Final Delhi hotel search (property only; exact date is Wed 20 Jan in every variant tested — Cell C/E's same-day-arrival structure does not change which date the hotel is needed for).

**Must WAIT on Mark's Kolkata-duration selection:**
- Exact Kolkata departure date and exact Tiruvannamalai arrival date (differs by variant, Section 3).
- VNS–CCU and CCU–MAA flight date selection for the outbound Kolkata legs (dates shift by variant).
- Whether a Chennai-positioning hotel is booked at all, and for how many nights (0, 1, or 2).
- MAA–DEL flight timing choice: baseline (Cell B) needs a morning-or-later nonstop with slack; Cell C/E needs a **specific same-day-connecting** flight after the Tiru–Chennai road leg, which is a materially different booking search.

---

## 10. FINAL/LOCKABLE vs LIVE_RECHECK_LATER

**FINAL/LOCKABLE (architecture-grade, do not reopen without new Mark input):**
- Macrospine and world scope (unchanged).
- Kumaon internal order: Nainital → Dunagiri → Haidakhan (Section 2).
- Final Delhi = 1 night, structurally fixed relative to AI155 regardless of Kolkata variant.
- The three named fragile-transfer PASS ratings (Section 6).

**LIVE_RECHECK_LATER (unchanged list, carried forward, not re-litigated here):**
- All rail/flight exact inventory and timing (15013/15014/12988/20887/VNS–CCU/CCU–MAA/MAA–DEL).
- Haidakhan and Sri Ramanasramam acceptance.
- Exact Dakshineswar–Belur lodging and YSS eligibility.
- Day-specific weather/fog/road conditions.
- Gangasagar Mela 2027 official dates/traffic controls.

**Newly resolved this pass (moved out of LIVE_RECHECK_LATER):**
- Sarnath Museum weekly closure: Friday (was flagged unresolved; now closed per official ASI source already cited in the execution-readiness audit).
- Kumaon internal order (was the one open macro-ordering question; now closed per Section 2).
- GATE 2 phantom alternative (12039 Shatabdi): closed by confirmed absence of any such committed content anywhere in the repository.

---

## 11. MARK GATE

Exactly one real, still-open decision blocks the final day-by-day calendar from being fully locked:

**Kolkata duration: 2, 3, or 4 nights.**

This is a genuine trade-off, not a research gap:
- 2 nights (Cell A) = most robust (2-night Chennai buffer) but thinnest Kolkata content (1 full day, core anchors only).
- 3 nights (Cell B, current committed default) = balanced (1-night Chennai buffer, 2 full days, core anchors + room for one more candidate).
- 4 nights (Cell C, or 3+Bodh-3 as Cell E) = richest Kolkata content (3 full days) but **removes the Chennai-positioning buffer entirely**, compressing the Tiru→Chennai→flight→Delhi chain into one day immediately before AI155 — a real reduction in international-flight protection that must be an explicit, informed Mark choice, not a default.

Mark's grading of the 4 pending Kolkata candidates (Balaram Mandir, Mayer Bari/Udbodhan, Vivekananda Ancestral House, Kamarpukur+Jayrambati) will inform which duration is worth choosing, but — as already established in the prior CCI_RESULT — does **not** need to happen before this duration decision; the duration choice can be made on the robustness-vs-content trade-off above, with the specific day-plan content filled in afterward regardless of which candidates survive grading.

No other new Mark gate is created by this pass.

END

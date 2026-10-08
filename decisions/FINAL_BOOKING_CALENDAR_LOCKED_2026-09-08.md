# FINAL BOOKING CALENDAR — STRUCTURALLY LOCKED — 2026-09-08

Status: **FINAL_BOOKING_CALENDAR_LOCKED (STRUCTURE) — EXACT TRAIN/FLIGHT INVENTORY REMAINS LIVE_RECHECK_LATER, AS FOR EVERY SEGMENT THROUGHOUT THIS PROJECT**
Source: CCI reconciliation of the full multi-AI ensemble (Deep Research + 5 free AIs + CCI master-solve + independent audit + clean synthesis), validated against current web evidence and existing canon.
Supersedes: the "CANDIDATE, NOT FINAL LOCK" status on `worker/final-route-calendar-optimizer` commit `f9b6c0b` and `worker/final-calendar-master-cci` commit `336ac9f`.

## WHAT "LOCKED" MEANS HERE

The **night-by-night skeleton** below — which cluster/city each of the 33 nights sleeps in, every duration, the macro-order, and the Kumaon internal order — is now final and should not be reopened without a genuine new Mark decision. It is not a candidate anymore.

**Exact train/flight numbers, times, and inventory are explicitly NOT locked** — they were never going to be. Every prior fixed-core duration in this project (Agra 1n, Bodh Gaya 2n, Tiruvannamalai 5n, etc.) was declared `TRUE_DURATION_CLOSED` while its exact transport remained `LIVE_RECHECK_LATER`; this file applies the same standard to the whole calendar at once, now that every remaining open axis has been closed.

## THE LOCKED 33-SLOT CALENDAR

| # | Date | Sleeps in / night-transport | Notes |
|---:|---|---|---|
| 1 | Sat 19 Dec | 15013 Ranikhet Express, Gurugram→Kathgodam | after AI156 (~10:15) + hotel/dayroom recovery |
| 2 | Sun 20 Dec | Nainital / Hotel Evelyn | arrival/decompression |
| 3 | Mon 21 Dec | Nainital | protected local day |
| 4 | Tue 22 Dec | Nainital | Kainchi Dham + Bhumiadhar day |
| 5 | Wed 23 Dec | Dunagiri/Kukuchina | transfer day |
| 6 | Thu 24 Dec | Dunagiri/Kukuchina | Mahavatar Babaji's Cave day |
| 7 | Fri 25 Dec | Dunagiri/Kukuchina | YSS Dwarahat day — coincides with YSS's own published Christmas meditation schedule |
| 8 | Sat 26 Dec | Haidakhan Vishwa Mahadham | ashram arrival |
| 9 | Sun 27 Dec | Haidakhan Vishwa Mahadham | protected quiet day 1/2 |
| 10 | Mon 28 Dec | Haidakhan Vishwa Mahadham | protected quiet day 2/2 |
| 11 | Tue 29 Dec | **Delhi transit hotel, reached via 12039 Kathgodam→New Delhi (15:15→20:55)** — see validation below; **fallback: 15014 overnight, alight Old Delhi (DLI) ~04:10, not Delhi Cantt** | see §VALIDATION |
| 12 | Wed 30 Dec | Agra hotel | via Gatimaan 12050 NZM→Agra if using the 15014 fallback; via a normal daytime transfer if 12039 is used |
| 13 | Thu 31 Dec | 12988 Ajmer–Sealdah, Agra Fort→Gaya | Taj Mahal early (Thursday = open; Friday would be closed) |
| 14 | Fri 1 Jan | Bodh Gaya / Maya Heritage | arrival day, substantially usable per current 12988 arrival pattern |
| 15 | Sat 2 Jan | Bodh Gaya | protected full day |
| 16 | Sun 3 Jan | Varanasi / Sahi River View | via 20887-pattern daytime rail |
| 17 | Mon 4 Jan | Varanasi | protected day |
| 18 | Tue 5 Jan | Varanasi | protected day |
| 19 | Wed 6 Jan | Varanasi | protected day |
| 20 | Thu 7 Jan | Varanasi | protected day |
| 21 | Fri 8 Jan | Varanasi | protected day — not Sarnath Museum (closed Fridays) |
| 22 | Sat 9 Jan | Varanasi | protected day |
| 23 | Sun 10 Jan | Varanasi | final protected day |
| 24 | Mon 11 Jan | Kolkata/Dakshineswar | arrival day; Belur Museum closed Mondays anyway |
| 25 | Tue 12 Jan | Kolkata/Dakshineswar | National Youth Day — museum closed, but Dakshineswar/YSS core and Garpar usable |
| 26 | Wed 13 Jan | Kolkata/Dakshineswar | protected day — first normal Belur Museum day, protect it |
| 27 | Thu 14 Jan | Tiruvannamalai | via CCU→MAA + road transfer |
| 28 | Fri 15 Jan | Tiruvannamalai | protected full day 1 (Sri Chakra Puja day at Ramanasramam) |
| 29 | Sat 16 Jan | Tiruvannamalai | protected full day 2 |
| 30 | Sun 17 Jan | Tiruvannamalai | protected full day 3 |
| 31 | Mon 18 Jan | Tiruvannamalai | protected full day 4 / final night |
| 32 | Tue 19 Jan | Chennai / MAA-airport zone | content-plus-buffer (Vivekananda House/Ramakrishna Math if transfer allows) then rest before early flight |
| 33 | Wed 20 Jan | Delhi/IGI | via early MAA→DEL nonstop, selected for maximum same-day recovery depth, not merely earliest |
| — | Thu 21 Jan | AI155 DEL→AMS ~12:20 | no India overnight |

**Durations**: Nainital 3n / Dunagiri 3n / Haidakhan 3n(2 full days) / Agra 1n / Bodh Gaya 2n / Varanasi 8n / Kolkata 3n / Tiruvannamalai 5n / Chennai 1n / final Delhi 1n, plus 3 rail-transfer/transit nights (19 Dec, 29 Dec, 31 Dec) = **33/33**, independently re-verified (see proof below).

### 33/33 proof
Delhi-Kumaon transfer(1) + Kumaon(9) + Kumaon-Delhi transit(1) + Agra(1) + Agra-Gaya rail(1) + Bodh Gaya(2) + Varanasi(8) + Kolkata(3) + Tiruvannamalai(5) + Chennai(1) + final Delhi(1) = 33. No duplicated or missing calendar date between 19 Dec 2026 and 20 Jan 2027 inclusive.

## VALIDATION OF THE FIVE QUESTIONS THE ENSEMBLE SYNTHESIS ASKED CCI TO CLOSE

1. **Haidakhan→Kathgodam→12039 (15:15) with real winter margin: PASS, adopted as preferred.** Verified 12039 is a real, currently-daily Kathgodam→New Delhi Shatabdi Express (15:15→20:55, ~5h40, RECURRING_PATTERN). The existing incumbent's own already-established road estimate for this exact segment (`FINAL_TRIP_DATED_CALENDAR_2026-09-07.md`, Slot 11) is "private car 2.5–3.5h conservative," with a same-file precedent of an 08:30–09:00 departure after breakfast. That yields an ~11:00–12:30 arrival at Kathgodam against a 15:15 departure — a 2.5–4 hour margin, comfortably larger than the margin the incumbent already accepted for its own 20:35/20:52-class evening-train targets. Exact December 29 2026 winter road conditions remain `LIVE_RECHECK_LATER`, same as every other segment in this project — this is not a new category of risk, just the same standard treatment.
2. **Fallback if 12039 fails on the ground: 15014 overnight, alight at DLI (~04:10), not Delhi Cantt (~05:03).** Already established via the independent audit (`2879705`) and reconfirmed here; changes nothing else.
3. **33/33 reconfirmed with the 12039 substitution**: only Slot 11's *mode* changes (night train → daytime train + hotel); the *date* does not move, so nothing downstream shifts. Proof above.
4. **CCU→MAA margin on 14 Jan**: cannot be closed today — exact Jan-2027 flight timing is unpublished. Objective test recorded for later live-recheck: the selected flight must land early/mid-day enough that the confirmed 175km/3.5–4.5h road transfer to Tiruvannamalai still leaves a humane, non-rushed arrival. `LIVE_RECHECK_LATER`, not a blocker to structural lock — every other flight/rail segment in this locked calendar carries the identical status.
5. **MAA→DEL selection method for 20 Jan**: adopted as designed — choose the earliest realistic nonstop that still leaves the largest realistic set of later same-day nonstops as recovery capacity, not simply the earliest flight available. Current recurring evidence (Air India + IndiGo nonstops spread across the day) supports this being achievable; exact flight choice is `LIVE_RECHECK_LATER`.

## REMAINING MARK GATE

**None.** Matches the ensemble synthesis's own `MARK_DECISION_GATE: NONE` conclusion, independently confirmed by CCI.

## WHAT THIS UNLOCKS

Per `START_HERE_CURRENT_INDIA_PROJECT_STATE.md` §12, the booking/contact phase may now begin: a second execution/control-tower document with exact-dated action items (Haidakhan/Dunagiri/Ramanasramam stay requests, Varanasi river-view room, Kolkata/YSS/Belur/Garpar contact, rail bookings including FTQ where advantageous, VNS→CCU/CCU→MAA/MAA→DEL flight selection, drivers/transfers) should be built next, superseding the older execution-readiness audit's now-current-again "contact/reserve" guidance.

## WHAT REMAINS GENUINELY OPEN (not gates, just live facts)

All items in the ensemble synthesis's §S list (exact 2026/27 rail and flight inventory for every segment, Haidakhan/Ramanasramam written acceptance, exact winter road conditions, Belur/Ramanasramam special programming) remain `LIVE_RECHECK_LATER` and must be worked through the control-tower document's T-minus schedule, not treated as already resolved.

END

# BRAJ+PURI VS KOLKATA — EXACT TWO-PACKAGE CALENDAR PASS

Date: 2026-09-06 (revised after independent Work audit)
Status: OBJECTIVE EXACT-CALENDAR RESEARCH / NO PACKAGE WINNER CHOSEN
Branch: agent/india8-cluster-casting
Scope authority: `decisions/OPTIONAL_WORLD_FINAL_PAIR_SCOPE_2026-09-06.md`

## REVISION NOTE
This file replaces the original 2026-09-06 exact-pass after an independent `WORK_RESULT` audit (PR #23) rebuilt every family from explicit dated overnight rows and found the original "committed nights" sums did not all add to 33. Every family below is now a full date-by-date row list, not a component sum, so the totals are directly checkable. CCI reconciled and, on the disputed verdict, **agrees with Work's stricter call** — see "AGREE/DISAGREE" below.

## EVIDENCE-STRENGTH TAGS USED BELOW
- **PROVEN**: fixed by explicit LOCKED_BY_MARK/TRUE_DURATION_CLOSED decision or basic calendar arithmetic (dates, weekdays) that does not depend on any unconfirmed external schedule.
- **STRUCTURAL_BUT_LIVE_RECHECK_LATER**: a real, currently-published recurring service pattern (daily flight, daily train class) that fits the structure, but exact Jan-2027 date/inventory/fare is not yet booking-verified.
- **UNVERIFIED_DEPENDENCY**: an assumption with no supporting evidence checked at all (e.g. exact minutes needed for a same-morning cross-city connection) — must not be treated as safe until checked.

## FIXED SPINE (shared by all four families) — PROVEN unless noted
- Sat 19 Dec 2026: AI156 DEL 10:15. Hotel first -> Nirmal Dham [A+] -> evening 15013 Ranikhet Express GGN -> Kathgodam (overnight transport night). [STRUCTURAL_BUT_LIVE_RECHECK_LATER: exact 19 Dec 1A inventory/punctuality]
- 20–22 Dec: Nainital 3 nights.
- 23–25 Dec: Dunagiri/Kukuchina 3 nights.
- **H+ only**: 26–28 Dec: true Haidakhan Vishwa Mahadham [A+] 3 nights. Exit Tue 29 Dec -> gateway -> 15014 Ranikhet Express Kathgodam 20:35 -> Delhi Cantt ~05:03 (30 Dec). [STRUCTURAL_BUT_LIVE_RECHECK_LATER]
- **H− only** (hypothetical sensitivity, not a decision): exit direct from Dunagiri/Kukuchina Sat 26 Dec -> gateway -> same 15014-class overnight -> Delhi Cantt (27 Dec).
- **UNVERIFIED_DEPENDENCY, shared by all four families**: continuing the SAME MORNING from Delhi Cantt (~05:03 arrival) onward to Mathura (Braj package) or straight to Agra (Kolkata package). Older canon (`GLOBAL_SLOT_TALLY_OPTIONAL_WINDOW_2026-09-05.md`) asserts this is structurally easy, but exact station-transfer time and onward-train timing on the actual dates below has never been checked. Families with spare capacity can absorb a miss here; the one family with zero spare cannot.
- Agra: 1 hotel night, sunrise Taj next morning, evening 12988 Agra Fort ~18:45 -> Gaya ~07:50. TRUE_DURATION_CLOSED (PROVEN), current-service-daily (STRUCTURAL_BUT_LIVE_RECHECK_LATER for exact date).
- Bodh Gaya: 2 nights default (BG2, PROVEN as the closed default); +1 (BG3) is the explicitly-open conditional fallback, tested below.
- Varanasi/Sarnath: 8 nights LOCKED_BY_MARK (PROVEN) — rechecked again this pass, no later explicit Mark decision found superseding `VARANASI_DURATION_MARK_DECISION_2026-08-27.md`. `CURRENT_STATE.md`'s "consistency recheck" wording is still stale phrasing, not a reopening — flagged again, still not fixed at the wording level.
- Tiruvannamalai/Arunachala: 5 nights LOCKED_BY_MARK (PROVEN).
- Final Delhi: 1 night before AI155 DEL 21 Jan 12:20 (PROVEN as Mark's stated preference); exact Chennai-Delhi flight time is STRUCTURAL_BUT_LIVE_RECHECK_LATER.

## HEADLINE FINDING — PRESERVED, RE-VERIFIED A SECOND WAY
**1 January 2027 is a Friday.** Re-verified this pass via Zeller's congruence (independent of the original forward day-count) during the Work audit: h=(q+⌊13(m+1)/5⌋+K+⌊K/4⌋+⌊J/4⌋−2J) mod 7 gives Friday for 1 Jan 2027 and Saturday for 19 Dec 2026. PROVEN, not a single-method artifact. The Taj is closed to general viewing on Fridays (existing canon). The scope file's stated "Braj+Puri minimum credible = 3 nights" (Braj 1 + Puri 2) is **not executable as sequenced** under H+ — it lands the mandatory sunrise Taj visit on that Friday. Corrected minimum: **Braj 2 + Puri 2 = 4 nights**.

## FOUR-FAMILY RESULTS — FULL DATED ROW LISTS

### 1. Braj+Puri / H+, corrected minimum (Braj 2 + Puri 2 = 4 nights)
| Night# | Date | Where |
|---|---|---|
| 1 | 19 Dec (Sat) | transport (Delhi->Kumaon) |
| 2–4 | 20–22 Dec | Nainital |
| 5–7 | 23–25 Dec | Dunagiri/Kukuchina |
| 8–10 | 26–28 Dec | Haidakhan |
| 11 | 29 Dec (Tue) | transport (Kathgodam->Delhi Cantt) |
| 12–13 | 30–31 Dec | Braj (2) |
| 14 | 1 Jan (Fri) | Agra (Taj morning 2 Jan Sat — clear of Friday closure) |
| 15 | 2 Jan (Sat) | transport (Agra->Gaya) |
| 16–17 | 3–4 Jan | Bodh Gaya (BG2) |
| 18–25 | 5–12 Jan | Varanasi (8) |
| 26–27 | 13–14 Jan | Puri (2) [UNVERIFIED_DEPENDENCY: VNS->BBI exact weekday, see below] |
| 28–32 | 15–19 Jan | Tiruvannamalai (5) |
| 33 | 20 Jan (Wed) | final Delhi (same-day Tiru->Chennai->Delhi transfer on this exact day, zero buffer) |

**Total: 33/33, 0 spare.** Confirmed correct by both CCI and Work independently.

### 2. Braj+Puri / H+, comfortable (Braj 2 + Puri 3 = 5 nights)
Same as above through Varanasi, then Puri 13–15 Jan (3), Tiruvannamalai 16–20 Jan (5, last night = 20 Jan). **All 33 nights are consumed finishing Tiruvannamalai itself** — checkout is 21 Jan, the day of AI155's departure. **Zero nights remain for the Chennai->Delhi transfer or any Delhi night at all.** This is worse than "1 night over" — there is no Delhi leg whatsoever in this configuration.

### 3. Braj+Puri / H− (comfortable: Braj 2 + Puri 3 = 5 nights; whole spine 3 days earlier)
| Night# | Date | Where |
|---|---|---|
| 1 | 19 Dec | transport |
| 2–4 | 20–22 Dec | Nainital |
| 5–7 | 23–25 Dec | Dunagiri/Kukuchina |
| 8 | 26 Dec (Sat) | transport, direct exit (H−, no Haidakhan) |
| 9–10 | 27–28 Dec | Braj (2) |
| 11 | 29 Dec (Tue) | Agra (Taj morning 30 Dec Wed — clear) |
| 12 | 30 Dec | transport (Agra->Gaya) |
| 13–14 | 31 Dec–1 Jan | Bodh Gaya (BG2) |
| 15–22 | 2–9 Jan | Varanasi (8) |
| 23–25 | 10–12 Jan | Puri (3) |
| 26–30 | 13–17 Jan | Tiruvannamalai (5) |
| — | 18 Jan | transfer to Delhi (spare) |
| — | 19 Jan | spare |
| 33 | 20 Jan | final Delhi |

**Total: 30 committed (nights 1–30) + 2 spare (18, 19 Jan) + 1 final (20 Jan) = 33.** Corrected from the original file's inconsistent "29 committed + 3 spare" (summed to only 32). **Verdict unchanged: PASS**, but with 1 less night of true margin than originally reported.

### 4. Kolkata / H+ (comfortable: 3 nights)
| Night# | Date | Where |
|---|---|---|
| 1 | 19 Dec | transport |
| 2–4 | 20–22 Dec | Nainital |
| 5–7 | 23–25 Dec | Dunagiri/Kukuchina |
| 8–10 | 26–28 Dec | Haidakhan |
| 11 | 29 Dec | transport (Kathgodam->Delhi Cantt) |
| 12 | 30 Dec (Wed) | Agra (Taj morning 31 Dec Thu — clear, no Braj stop so no Friday risk at all in this package) |
| 13 | 31 Dec | transport (Agra->Gaya) |
| 14–15 | 1–2 Jan | Bodh Gaya (BG2) |
| 16–23 | 3–10 Jan | Varanasi (8) |
| 24–26 | 11–13 Jan | Kolkata (3) [STRUCTURAL_BUT_LIVE_RECHECK_LATER only: VNS-CCU and CCU-MAA are both daily, no weekday-fragile edge] |
| 27–31 | 14–18 Jan | Tiruvannamalai (5) |
| — | 19 Jan | transfer to Delhi (spare) |
| 33 | 20 Jan | final Delhi |

**Total: 31 committed (nights 1–31) + 1 spare (19 Jan) + 1 final (20 Jan) = 33.** Corrected from the original "32 committed + 1 spare" (summed to 34). Spare-count conclusion unchanged: **PASS**, real 1-night buffer before international departure.

### 5. Kolkata / H−
| Night# | Date | Where |
|---|---|---|
| 1 | 19 Dec | transport |
| 2–4 | 20–22 Dec | Nainital |
| 5–7 | 23–25 Dec | Dunagiri/Kukuchina |
| 8 | 26 Dec | transport, direct exit (H−) |
| 9 | 27 Dec (Sun) | Agra (Taj morning 28 Dec Mon — clear) |
| 10 | 28 Dec | transport (Agra->Gaya) |
| 11–12 | 29–30 Dec | Bodh Gaya (BG2) |
| 13–20 | 31 Dec–7 Jan | Varanasi (8) |
| 21–23 | 8–10 Jan | Kolkata (3) |
| 24–28 | 11–15 Jan | Tiruvannamalai (5) |
| — | 16, 17, 18, 19 Jan | spare (4 nights) |
| 33 | 20 Jan | final Delhi |

**Total: 28 committed (nights 1–28) + 4 spare (16–19 Jan) + 1 final (20 Jan) = 33.** Corrected from the original "27 committed + 4 spare" (summed to 32). Spare-count conclusion unchanged: **PASS**, generous margin confirmed.

## BODH GAYA 2-vs-3 SENSITIVITY — RE-RUN ON CORRECTED TOTALS
| Family | Corrected full-trip total (incl. final night) | +1 (BG3) | Effect |
|---|---|---|---|
| Braj+Puri/H+ (corrected min., 4) | 33 | 34 | flips an already-FAIL case to outright overshoot |
| Kolkata/H+ (comfortable) | 33 | 34 | spare drops from 1 to 0 — zero-slack, fragile |
| Braj+Puri/H− (comfortable) | 33 | 34 | spare drops from 2 to 1 |
| Kolkata/H− (comfortable) | 33 | 34 | spare drops from 4 to 3 |

## FRAGILE / UNVERIFIED EDGES SUMMARY
- **VNS->BBI weekday (Package A only)**: secondary sources disagree with each other on which days this route runs; genuinely unresolved, UNVERIFIED_DEPENDENCY. Package B carries no equivalent (VNS-CCU, CCU-MAA both daily, STRUCTURAL_BUT_LIVE_RECHECK_LATER only).
- **Same-morning Delhi Cantt -> Mathura/Agra continuation (all four families, shared spine)**: UNVERIFIED_DEPENDENCY. Not checked at all this pass or the last. Kolkata (both H states) and Braj+Puri/H− have spare nights to absorb a miss; **Braj+Puri/H+ corrected-minimum has none.**
- **Same-day Tiruvannamalai/Chennai->Delhi transfer landing by/before 20 Jan**: STRUCTURAL_BUT_LIVE_RECHECK_LATER in the three PASS families (all land 18–19 Jan, 1–2 days of margin before 20 Jan). In Braj+Puri/H+ corrected-minimum, this transfer must happen ON 20 Jan itself with zero margin — this is the same UNVERIFIED_DEPENDENCY compounding the zero-slack problem, not a separate issue.

## AGREE / DISAGREE WITH WORK'S STRICTER VERDICT
Work rated **Braj+Puri/H+ = FAIL** rather than CCI's original MARGINAL. **CCI agrees with Work on reconciliation.** Reasoning: the arithmetic itself is confirmed exactly correct (33/33, PROVEN), so a pure slot-counting view would say MARGINAL-but-technically-fits. But this configuration's feasibility is not just tight — it is *contingent on an entirely unverified same-day connection with zero recovery capacity*, and if that connection fails there is no slack anywhere in the whole 33-night trip to absorb it (it would cascade into either missing part of the LOCKED_BY_MARK Varanasi/Tiruvannamalai blocks or missing AI155 itself). A plan whose only failure mode is catastrophic and whose triggering assumption has never been checked is not safely presentable to Mark as "workable, just tight" — that is what FAIL is for. **This is a current-evidence verdict, not permanent**: if the Delhi Cantt connection is later verified as comfortably feasible on the actual dates, this family could be reclassified back to PASS/MARGINAL.

## CORRECTED VERDICT MATRIX
| Family | Nights | Spare | Verdict |
|---|---|---|---|
| Braj+Puri / H+ (corrected min., 4) | 33/33 | 0 | **FAIL** (arithmetically exact but UNVERIFIED_DEPENDENCY + zero recovery capacity) |
| Braj+Puri / H+ (comfortable, 5) | 33 consumed through Tiru alone | none for Delhi leg at all | **FAIL** |
| Braj+Puri / H− (comfortable, 5) | 30 committed | 2 | **PASS** |
| Kolkata / H+ (comfortable, 3) | 31 committed | 1 | **PASS** |
| Kolkata / H− (comfortable, 3) | 28 committed | 4 | **PASS** |

## PLAIN ANSWER, RECONCILED
Keeping Haidakhan (H+) is not compatible with a genuinely workable Braj+Puri package at all under current evidence — even its corrected minimum fails once the unverified same-morning-connection risk and its lack of any recovery margin are weighed, not just counted. Comfortable Kolkata works under H+ with real margin. Dropping Haidakhan (H−) is what actually converts Braj+Puri from FAIL to a comfortable PASS with 2 nights of genuine slack (corrected from the original 3) and removes the Friday-Taj risk entirely. Kolkata does not need H− to work; H− just gives it more room.

No package winner chosen. No Mark grade, lock, or Haidakhan inclusion changed.

END

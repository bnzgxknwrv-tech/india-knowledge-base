# CCI_A79_V1_INDEPENDENT_AUDIT_2026-09-11

Auditor: CCI (independent, solution-blind to WORK's parallel A79 v1 audit result)
Repository: `bnzgxknwrv-tech/india-knowledge-base`
Branch audited: `agent/india8-cluster-casting`
PR relay: #23
AUDIT_PACKET_HEAD: `be3221681e634bf3be2538793c29d7c7c1789b59` (confirmed = current tip of `agent/india8-cluster-casting`; branch has not moved since freeze)

INDEPENDENCE STATEMENT: This audit was written without reading any `WORK_RESULT — INDIA19 A79 CLOCKTIME PDF V1 INDEPENDENT AUDIT` output, or any other new WORK result for this specific A79 v1 task, at any point before the findings and verdict below were finalized. Prior frozen WORK route-solve and cross-red-team evidence, already cited by the packet as reusable, was read and used per the manifest's own instruction.

---

## 0. Packet located and read

At exactly `be3221681e634bf3be2538793c29d7c7c1789b59` via `git show <sha>:<path>`:
- `.../clock-audit/INDIA19_Kloktijdplanning_A79_v1_AUDIT_MANIFEST.md` — read in full.
- All seven named audit-mirror parts (PART1_SKELETON_INDEX, PART2_A001_A020, PART3_A021_A040, PART4_A041_A060, PART5_A061_A079, PART6_CLOCKS_01, PART7_CLOCKS_02_SPECIALS) — read in full, exactly as named, no substitution.

**PDF/DOCX presence check.** `git log --all --diff-filter=A -- '*A79_v1.pdf' '*Kloktijdplanning*.pdf' '*A79_v1.docx' '*Kloktijdplanning*.docx'` returns **no results** anywhere in this repository's full history (all branches). The binary `INDIA19_Kloktijdplanning_A79_v1.pdf` and its source `.docx` were never committed. Consequently `sha256sum` cannot be run against any actual file, and the claimed hashes (PDF `0adec758a0b156d56fdd7c8552fa214b78f8e24291d9be759e367dde99d00716`, DOCX `6f2369a804972da9325bbdac26033e07ca18833d6562859d7a6954b5ebc7619f`) are **unverifiable from repo evidence**. The manifest itself explains why (chat-runtime binary, GitHub connector cannot persist it) — this is not evidence the content is wrong, but per this audit's own dispatch instruction it is classified **HARD** (broken chain of custody between the claimed artifact and what any auditor, or Mark, can actually check). See Defect D1 below. The seven text-mirror parts are internally consistent with each other (index vs. detail cards vs. clock tables all agree — verified below), so the substantive audit proceeded on them as instructed.

## 1. 79/79 ledger integrity (A79_LEDGER_CHECK)

Cross-checked `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv` (current tip of `agent/india8-cluster-casting`, unchanged since freeze) against PART1's A001-A079 index, programmatically (Python `csv` + set/dict comparison, not eyeballing):

- Ledger has 87 data rows: 55 grade `A`, 24 grade `A+`, 7 grade `A*`, 1 `SPECIAL/ACCOMMODATION` (VNS-22, the Assi Ghat sleep-base itself — correctly not an ordinary sightseeing item). Ordinary A+/A = 55+24 = **79**, A* = **7** — exactly matches the manifest's claimed split. (The dispatch's "86-row ledger" figure = 79 ordinary + 7 A*, i.e. all content rows excluding the one accommodation row; consistent, no discrepancy.)
- The **set of 79 ordinary ledger STABLE-IDs is identical**, element-for-element, to the 79 Bron-IDs in the A001-A079 index — zero missing, zero extra, zero duplicate.
- **Grade comparison, all 79 items**: zero mismatches between ledger GRADE and PDF-index grade (A vs A+ both checked programmatically).
- The 7 A* ledger IDs (KUM-13/14/15/16, BOD-06, BOD-08, VNS-42) exactly match the S01-S07 special-status table in PART7 — none of them appear in the ordinary A001-A079 count, so 79/79 is a real ordinary-only figure, not inflated by A* rows.
- Previously `MISSING` / `HIDDEN_IN_CLUSTER` / `CONDITIONAL` ledger rows (e.g. VNS-14/15/16/17/23/38 Sarnath children, VNS-25/29/30/31/32/34/35/36/40/41 Varanasi route-side sites, BOD-05 Dungeshwari ridge, VNS-26/28/39 Bhadaini-Assi world, VNS-24 Lahiri Samadhi) **each now has its own A-number and its own real, non-zero clock block** in PART2-PART5 — the consolidation from the older working draft into A79 v1 is honest: no site that was flagged missing/hidden is still missing/hidden.

**A79_LEDGER_CHECK: PASS** — 79/79 ordinary A+/A source IDs present, correctly graded, no duplicate, no hidden physical row, no unauthorized grade change. (Ledger's own `COVERAGE_STATUS` column is stale bookkeeping — still says `MISSING`/`HIDDEN_IN_CLUSTER` for items that ARE present in A79 v1 — MINOR ledger-hygiene note, not a defect of the PDF; flagging for INDIA19 to refresh, not something this audit changes per its own constraints.)

## 2. Unique numbering and visibility (A001_A079_NUMBERING_CHECK)

- 79 unique `A001`-`A079` labels, no gaps, no repeats (`sort -u` count = 79).
- 79 unique source IDs, one per A-number (no source ID assigned to two A-numbers).
- Every A-number has: a date, a clock block, a "Wat is het?"/"Waarom voor Mark?" card, an AOAY/person line, and a distance-to-neighbor line, in PART2-PART5, and the same A-number reappears consistently in the matching daily table in PART6/PART7 (spot-checked across all 33 days — index, cards and daily tables agree on grade, time and location for every A-number checked).
- Shared transfers are used correctly (e.g. A033 Assi Ghat nested inside A032's dawn-walk window at "0 km extra") — MINOR note: a few A-pairs are time-nested rather than sequential (A032/A033; A011/A012 are sequential, not nested, so this is not systemic). This is an honest representation of physical reality (the ghat is literally the walk's starting point) but means the 79 clock blocks are not all mutually exclusive/additive — a reader tallying "total occupied hours" from the cards alone would slightly double-book a few minutes. Not a hidden site; MINOR, cosmetic.

**A001_A079_NUMBERING_CHECK: PASS**, with one MINOR clarity note (nested vs. sequential blocks not called out explicitly).

## 3. Clock-time feasibility (CLOCKTIME_FEASIBILITY)

- Every A has a real date and time window; PART1 index, PART2-5 cards, and PART6-7 daily tables agree on every spot-checked entry (all 79 cross-checked for grade; dates/times spot-checked across every day of the 33-night skeleton).
- Weekday labels verified independently against the proleptic Gregorian calendar (`date -d`) for all 33 nights: **every single Dutch weekday abbreviation in the skeleton (za/zo/ma/di/wo/do/vr) is calendrically correct** for 2026-12-19 through 2027-01-20. No date/weekday defect found.
- 33-night arithmetic verified independently: 19 Dec 2026 to 20 Jan 2027 inclusive = exactly 33 calendar dates = 33 nights, matching night33's date exactly. Confirmed also night-by-night (no duplicate or skipped date across the 33-row skeleton).
- Full clock-table walk-through (all 33 days + departure day, PART6+PART7) shows internally coherent sequencing: no A ends after the next A on the same day starts, meal/transfer buffers are present between blocks, and multi-A days (e.g. 9 Jan with 9 ordinary A's, 13 Jan with 3 major sites, Sarnath 10 Jan with 8 A's) all close with a same-day return to base before the day ends.

**CLOCKTIME_FEASIBILITY: PASS.**

## 4. Distances and travel times (DISTANCE_TRANSFER_CHECK)

- Nearly every inter-A leg carries a stated km/min estimate; legs genuinely uncertain (exact rail/flight timetable, ferry vs. road to Belur, exact address routing to Lahiri house, YSS Dwarahat commute, Jan-2027 satsang schedule) are explicitly tagged `LIVE_RECHECK_LATER` / `LRL` rather than asserted as decision-grade — this correctly follows the manifest's instruction to distinguish planning estimates from verified fact. No leg found that hides an LRL fact as if it were confirmed.
- No impossible or obviously-too-optimistic transition found in a full read-through (all transfer times are consistent with the same project's own prior geo/route research already in the repo, e.g. Assi↔Sarnath ~13km/35-50min repeated consistently on both legs of 10 Jan).
- One festival/date-collision item was **not** checked in the packet itself and is a real, sourced gap — see Defect D2 below (technically a calendar/crowd-exposure fact rather than a raw distance error, but it belongs in this check because it affects whether the stated Kolkata→Tiruvannamalai transfer window is realistic on the date chosen).

**DISTANCE_TRANSFER_CHECK: PASS_WITH_CORRECTIONS** (see D2).

## 5. AOAY/person-link audit (AOAY_PERSON_LINK_CHECK)

Checked every AOAY/persoon line in PART2-PART5 against existing project canon and general AOAY content:

- **Mahavatar Babaji vs Haidakhan Babaji — the known risk case.** A011/A012 (Haidakhan Vishwa Mahadham + historic cave) explicitly state: *"AOAY/persoon: Haidakhan Babaji. Important: this project does not silently equate Haidakhan Babaji with AOAY's Mahavatar Babaji"* and *"no automatic AOAY Mahavatar Babaji identity claim."* A009 (Mahavatar Babaji's Cave, Kukuchina-Dunagiri — a physically separate location from Haidakhan) is correctly labeled *"direct, central AOAY link."* **This is handled correctly: the two Babajis are kept as distinct identities at distinct sites, with an explicit disclaimer on the Haidakhan cards.** No conflation found.
- A036 Anandamayi Ma: "direct AOAY link: Yogananda met and wrote about the 'Joy-Permeated Mother'" — accurate (AOAY has a dedicated chapter on Ananda Moyi Ma).
- A039/A040 Lahiri Mahasaya: correctly central/direct AOAY link.
- A064 4 Garpar Road: correctly direct AOAY biographical link (Yogananda family home); A065 YSS Garpar centre correctly direct.
- A061 Dakshineswar / A063 Belur (Ramakrishna, Sarada Devi, Vivekananda): correctly labeled **indirect** — "not a Yogananda biographical site." No overclaim.
- A066/A068/A069/A070/A071/A076 (Ramana Maharshi/Arunachala): correctly labeled "no direct AOAY claim" throughout — Ramana is kept as a real, valued, but AOAY-independent person-interest, never dressed up as an AOAY connection.
- A077 Nirmal Dham (Shri Mataji Nirmala Devi): correctly "no AOAY link."
- A016 Taj Mahal / Yogananda: sourced to Mark's own supplied photo evidence (`AGRA_TAJ_MAHAL_YOGANANDA_ONSITE_MEMORY_CUE_2026-08-31.md`, which itself explicitly says the identification is "Mark's supplied provenance, not an independent face-identification claim by INDIA"). The A79 card language ("direct historical onsite memory cue in the project canon") matches this source's own hedging — correctly caveated, not an invented AOAY claim.
- A045 Trailanga/Tailanga Swami Math: card says AOAY relevance is "indirect... no specific episode is required." Autobiography of a Yogi contains a chapter specifically about Trailanga Swami ("The Saint with Two Bodies"), which would ordinarily read as a fairly direct link. This possibly **understates** rather than fabricates a connection — no misattribution risk, but worth an INDIA/canon cross-check (I found no existing repo decision file settling this either way). **MINOR, flagged for verification, not asserted as a correction.**

**AOAY_PERSON_LINK_CHECK: PASS** — the one known highest-risk conflation (Mahavatar Babaji vs Haidakhan Babaji) is explicitly and correctly handled with disclaimer text on the Haidakhan cards; no invented connections found; one MINOR possible understatement (Trailanga Swami) noted for verification only.

## 6. Closures/access/windows (CLOSURE_ACCESS_CHECK)

- **Sarnath Friday-closure problem**: previously found in CCI's own earlier draft solve (Friday 8 Jan collision, confirmed via `CCI_CROSS_REDTEAM_OF_WORK_2026-09-10.md` line 66). A79 v1 places the full Sarnath world, including the Archaeological Museum (A055/VNS-38), on **Sunday 10 Jan** — calendrically confirmed a real Sunday — with the card explicitly stating "official 09:00-17:00, Friday closed" and a 09:30-10:45 visit slot comfortably inside those hours. **Confirmed fixed.**
- **Belur Math National Youth Day closure (12 Jan)**: `CLOSED_FACTS_OPEN_VARIABLES.md` records this as a closed fact (museum closed 12 Jan). A79 v1 visits Belur (A063) on **13 Jan**, not 12 Jan. **Confirmed correctly avoided.**
- **Kolkata arrival-day gap**: previously flagged by WORK's independent solve concern that Dakshineswar+YSS Math same-day as arrival was not proven safe. A79 v1's 12 Jan (night25) is transfer/recovery-only — VNS→CCU flight, baggage, base check-in, explicit "Geen A+ meer op aankomstdag" — with A061/A062/A063 all moved to 13 Jan. **Confirmed fixed**; the resulting 13 Jan day (06:15 breakfast to ~17:00 Belur close, with a lunch break and three named sites) is long but internally paced similarly to other successfully-planned FULL days (e.g. 10 Jan Sarnath) and is self-labeled "FULL" rather than "OVERLOADED" — I concur with that self-rating.
- **A039 Lahiri house / A064 Garpar Road access-dependence**: both explicitly marked non-guaranteed — A039 "SCHEDULED; ACCESS MUST CONFIRM," A064 "SCHEDULED; PRE-ARRIVAL EMAIL REQUIRED" — matching the ledger's own access-dependence flags. Correctly not presented as guaranteed walk-in access. 11 Jan is explicitly kept as a retry buffer specifically for A039 if it fails on 7 Jan.
- **LRL items** (exact rail/flight timetables, ferry option to Belur, Jan-2027 satsang schedules, YSS Dwarahat commute) are consistently and honestly labeled throughout, never silently upgraded to fact.
- **Sattal / Rajgir Brahmakund disposition semantics**: S01 Sattal = "A* SKIP_FIRST — condition not triggered in current topology; do not create a dedicated detour." S05 Rajgir Brahmakund = "A* CONDITION_NOT_TRIGGERED — not on natural corridor; no 7-9h dedicated round trip." Neither is counted in the 79 ordinary total (verified in §1). **Matches WORK's prior cross-red-team finding that these must stay explicitly conditional/non-activated.**
- **New finding not previously flagged in the packet's own "repairs already incorporated" list — Makar Sankranti/Pongal collision (see D2 below).** This project's own frozen evidence (`runs/active/FINAL_BOOKABLE_CALENDAR_INDEPENDENT_CHECK_2026-09-07.md`, cited as reusable Category-2 evidence in `CLOSED_FACTS_OPEN_VARIABLES.md`) already established that Makar Sankranti/Pongal falls on **Friday 15 Jan 2027**, and explicitly rated the exact calendar cell that transfers Kolkata→Chennai/Tiruvannamalai *on* 15 Jan as "MARGINAL... Sankranti/Pongal transfer," recommending instead a transfer one day earlier (14 Jan/Bhogi). **A79 v1's actual dates place the CCU→MAA→Tiruvannamalai transfer exactly on 15 Jan** (night28), i.e., precisely the previously-identified weaker cell, and the Girivalam day (17 Jan) falls on Kaanum Pongal. Neither is mentioned anywhere in the audited packet.

**CLOSURE_ACCESS_CHECK: PASS_WITH_CORRECTIONS** — both previously-known issues (Sarnath, Kolkata arrival-day) genuinely fixed; the Pongal/Sankranti collision (D2) is a new-to-this-audit, well-evidenced gap.

## 7. Whole-human burden (HUMANE_BURDEN_CHECK)

Walked every one of the 33 daily clock tables (PART6+PART7) for wake time, meals, transfers, security/queues, walking, recovery, wind-down:

- Haidakhan's two full protected quiet days (27, 28 Dec / nights 9, 10) are genuinely empty of logistics — "Geen logistiek, geen nieuwe A-checklist" both days. **Confirmed protected.**
- Explicit sub-05:30 wake-ups found in the mirror text: **5 Jan (05:10), 6 Jan (05:15), 7 Jan (05:10), 17 Jan (03:45, for the Girivalam pre-dawn start — inherent to that pilgrimage practice), 20 Jan (03:15, driven by the early MAA→DEL domestic flight)**; plus one very-early sleeper-train arrival (~05:05, 20 Dec). No arrival is clearly *after* 22:00; two arrivals land right at the 22:00 boundary (29 Dec hotel check-in 21:20-22:00; 20 Jan hotel by 22:00 after the conditional cinema).
- 2 of 33 nights are sleeper-train nights (19 Dec, 31 Dec), both flagged HIGH FRICTION/FULL in the skeleton — consistent with the governance definition that a poor-sleep overnight is a real cost, not free.
- The days the manifest and skeleton self-label HIGH FRICTION/FULL/OVERLOADED/PHYSICAL (5, 9, 13, 16-18, 20 Jan, per the manifest's own explicit list) do correspond to the days with the most A-items and/or earliest wake times — the burden labeling is honest, not softened.
- **Gap**: `OBJECTIVE_AND_HUMANE_GATES.md` explicitly requires a later solve to *report* concrete humane-fit metrics (count of sub-05:30 wake-ups, count of post-22:00 arrivals, sleep-opportunity breakdown, fragile-edge/slack count). The A79 v1 packet contains all the raw data needed to derive these (as demonstrated above) but never states these numbers anywhere — not in the skeleton, not in the "CRITICAL DAYS/PACING" table, not in the B3/T4 note. This is a transparency/completeness gap against the project's own stated reporting requirement — see D3 below. It does **not** mean the burden is hidden (every heavy day is individually visible and correctly labeled), only that the aggregated numeric summary Mark would need for a fast top-level read is missing.

**HUMANE_BURDEN_CHECK: PASS_WITH_CORRECTIONS** (protected days genuinely protected; burden per-day is honestly labeled and physically present in full detail; but the required aggregate metrics table is missing — D3).

## 8. Exact 33 physical nights / flight-safety precedence (NIGHT_33_CHECK)

- 33/33 nights independently verified (see §3) — no duplicate, no gap, night33 = 20 Jan exactly.
- AI155 DEL→AMS departs **~12:20 on 21 Jan** (PART7 Table72) — the day *after* night33, with a relaxed 07:30 checkout, no early-morning rush for the international leg itself. The "Vroege vlucht" (early flight) noted against night33 in the skeleton refers to the early **domestic** MAA→DEL flight that same morning (20 Jan, 05:45-08:45 work window), not to AI155 — correctly distinguished, not a contradiction.
- A077 Nirmal Dham's own card states "flight safety outranks visit if disruption," and the packet's own "CRITICAL DAYS" table for 20 Jan states the PVR cinema (A079) is the first item to drop and that "vluchtveiligheid blijft absoluut boven content" (flight safety remains absolutely above content). This correctly implements final-Delhi/AI155 safety precedence over sightseeing.

**NIGHT_33_CHECK: PASS.**

## 9. A* semantics (A_STAR_SEMANTICS_CHECK)

All 7 A* rows (S01-S07 = Sattal, Sakley's, Kakrighat, Dwarahat temple groups, Rajgir Brahmakund, Alamgir Mosque/Dharahara, Gaya Tilkut) are visible in PART7's dedicated table with correct SKIP_FIRST/CONDITIONAL/CONDITION_NOT_TRIGGERED status, matching the ledger's A* grade for the same 7 IDs exactly (verified programmatically, §1). None of the 7 is counted inside the ordinary 79-item total. No instance found where an A* item's conditional visit is presented in the skeleton or index as if it were a scheduled/satisfied ordinary A/A+.

**A_STAR_SEMANTICS_CHECK: PASS.**

## 10. Pacing decision usefulness (B3/T4 vs B2/T5)

PART7 includes an explicit, honest comparison table (Bodh3/Tiru4 — this PDF — vs Bodh2/Tiru5 — alternative), naming real trade-offs (more Sujata-Dungeshwari/Mahabodhi room vs. more Tiru recovery slack; standalone Ramanasramam day preserved either way; 15 Jan stays a heavy arrival day either way). Combined with the per-day burden labels and the "CRITICAL DAYS" table, Mark has enough granular, dated, honestly-labeled information to judge whether this specific alpha's tempo feels right and to make his own A→B calls — subject to the corrections below (D2/D3) being visible to him before he relies on this alpha's calendar specifically for booking.

---

## DEFECT REGISTER

**D1 — HARD — chain of custody.** Neither `INDIA19_Kloktijdplanning_A79_v1.pdf` nor its source `.docx` exists in any commit on any branch of this repository. The claimed SHA256 hashes are therefore unverifiable by any auditor (CCI, WORK, or Mark) from repo evidence. The manifest's stated reason (chat-runtime binary, connector cannot persist it) is understood and the text mirrors are thorough and internally consistent, so this does not indicate the PDF's content is wrong — but it is a real, unresolved gap between "what is claimed" and "what can be checked." Local repair: commit the actual binary (or attach it directly to PR #23) so its hash is checkable; does not require touching the audited content.

**D2 — MATERIAL — local repair, no macro reopening.** A79 v1 schedules the Kolkata→Tiruvannamalai transfer (CCU→MAA→road, arrival Tiruvannamalai) for **15 Jan 2027**, which this same project's own frozen, sourced evidence (`FINAL_BOOKABLE_CALENDAR_INDEPENDENT_CHECK_2026-09-07.md`, citing Drik Panchang's 2027 festival calendar) identifies as **Makar Sankranti/Pongal itself**, and explicitly rates a Kolkata→Tiru transfer on that exact date as "MARGINAL... Sankranti/Pongal transfer" versus a transfer one day earlier (14 Jan/Bhogi). The Girivalam day (17 Jan) falls on Kaanum Pongal. Neither is mentioned in the audited packet's "repairs already incorporated" list or anywhere else in the seven parts, despite the underlying evidence already existing in the repo before this alpha was built. Affected: the 15 Jan transfer day and, by one-day shift, A061-A065 dates if repaired. Repair stays within the existing Bodh3/Tiru4/Chennai1 topology (e.g., consume the 11 Jan Varanasi buffer day to move VNS→CCU one day earlier) — no macro route reopening required.

**D3 — MATERIAL — local repair, no macro reopening.** `OBJECTIVE_AND_HUMANE_GATES.md` requires an explicit reported count of sub-05:30 wake-ups, post-22:00 arrivals, sleep-opportunity breakdown and fragile-edge/slack count. A79 v1 contains all necessary raw data (verified by direct reconstruction in §7) but never states these aggregate numbers. Repair: add one summary table; no content or topology change needed.

**D4 — MINOR — local repair.** FOUT 3 (governance naming convention: full name + Dutch recognition hook + microcluster + grade, repeated at every relevant mention including distance rules) is followed for each A's own card header but not in the "Vorige A/Volgende A" cross-reference fields, which cite bare A-numbers (e.g. "Naar A051") rather than name+hook. Readability-only; no site is hidden or misidentified.

**D5 — MINOR — flag for verification, not asserted as fact.** A045 (Trailanga Swami Math) labels its AOAY relevance "indirect," though AOAY contains a chapter specifically about Trailanga Swami, which would ordinarily read as more direct. No existing repo decision file settles this either way; recommend a quick canon check rather than treating this audit's note as a ruling.

**D6 — disclosure, not a defect of A79 v1 itself.** The dispatch instructed reading `WORK_CROSS_REDTEAM_OF_CCI_2026-09-10.md` as prior-stage ground truth. This exact file does not exist anywhere in the repository's history (`git log --all` for that filename returns nothing); only `CCI_CROSS_REDTEAM_OF_WORK_2026-09-10.md` (the reverse direction) exists, on `worker/india19-cci-cross-redteam-of-work`. Noted honestly; did not block this audit since the file's content (if it existed) is not itself part of the audited A79 v1 packet.

---

## VERDICT

```
PASS_WITH_CORRECTIONS
AUDIT_PACKET_HEAD: be3221681e634bf3be2538793c29d7c7c1789b59
A79_LEDGER_CHECK: PASS — 79/79 ordinary A+/A source IDs from the frozen ledger a2b71b25... map 1:1 onto A001-A079 with zero missing/duplicate/hidden items and zero grade mismatches (verified programmatically); 7 A* rows correctly separate and excluded from the 79 count.
A001_A079_NUMBERING_CHECK: PASS — 79 unique A-numbers, 79 unique source IDs, each individually visible in index/cards/daily tables with consistent grade/date/time; MINOR note that a few A-pairs (e.g. A032/A033) are time-nested rather than sequential, which is physically honest but not called out explicitly as such.
CLOCKTIME_FEASIBILITY: PASS — all 33 weekday labels calendrically verified correct; index/cards/daily tables agree throughout; no internal time collisions found on any day.
DISTANCE_TRANSFER_CHECK: PASS_WITH_CORRECTIONS — distances/times are consistently estimated and honestly LRL-tagged where uncertain; one date-driven transfer-window concern (D2, Kolkata-to-Tiruvannamalai transfer landing on Makar Sankranti/Pongal) was not checked in-packet.
AOAY_PERSON_LINK_CHECK: PASS — the known highest-risk case (Mahavatar Babaji vs Haidakhan Babaji) is explicitly and correctly kept distinct with disclaimer text; no invented AOAY connections found anywhere in the 79 cards; one MINOR possible understatement (Trailanga Swami, D5) flagged for verification only.
CLOSURE_ACCESS_CHECK: PASS_WITH_CORRECTIONS — Sarnath Friday-closure and Kolkata arrival-day problems are both genuinely fixed; Belur National Youth Day closure correctly avoided; A039/A064 correctly marked access-dependent, not guaranteed; Sattal/Rajgir correctly kept non-activated; new Makar Sankranti/Pongal transfer-date collision found (D2) that the packet does not address.
HUMANE_BURDEN_CHECK: PASS_WITH_CORRECTIONS — Haidakhan's two quiet days are genuinely protected; per-day burden is honestly labeled and fully detailed; required aggregate humane-fit metrics (sub-05:30 wake-up count, post-22:00 arrival count, sleep-opportunity/fragile-edge summary) are derivable from the data but never stated in the packet (D3).
NIGHT_33_CHECK: PASS — exactly 33 physical India nights (19 Dec-20 Jan) independently verified with no gap/duplicate; AI155 (21 Jan, ~12:20) correctly kept superior to sightseeing per A077's card and the 20 Jan critical-day note.
A_STAR_SEMANTICS_CHECK: PASS — all 7 A* rows visible with correct non-activated/conditional status matching the ledger exactly; none counted toward the ordinary 79/79 total.
SAFE_FOR_MARK_TEMPO_DECISIONS: YES — with the understanding that D1 (binary chain-of-custody), D2 (Pongal-week transfer date) and D3 (missing aggregate humane metrics) should be corrected, or at minimum explicitly disclosed to Mark, before this alpha is used as the literal booking calendar; none of the three requires reopening the macro route/topology.
```

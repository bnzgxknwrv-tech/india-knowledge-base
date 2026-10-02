# WORK_TASK — Varanasi Tuesday/Friday travel-time optimization

Read first:
1. `governance/CURRENT_TRUTH.md`
2. `runs/active/CCI_VARANASI_QUARTERHOUR_PLAN_WITH_LINEAGE_LINKS_2026-09-26.md` (current full plan — DI 5 JAN and VR 8 JAN sections specifically)
3. `governance/MARK_FACING_PLACE_CARD_TRAVEL_VALUE_RULE_2026-09-13.md` (mandatory `TOTALE TIJD`/`TIJD VRIJGEMAAKT` time-accounting format)
4. `governance/MARK_FACING_LOCATION_CARD_TEMPLATE.md`
5. `governance/DECISION_LEDGER.jsonl` (tail, DL-0080 onward — the Friday/Tuesday restructuring history)

BLINDNESS/INDEPENDENCE: work this out independently from CCI. Do not read any CCI_RESULT or CCI chat proposal for this specific Tuesday/Friday travel-optimization question before finishing your own pass — Mark wants a genuinely separate second opinion, not a checked copy.

## Goal

Mark: "ik wil graag dat de optimale reisplanning hieruit komt... ga zelf opnieuw een geheel nieuwe planning proberen obv beste reistijd combi." He wants the objectively best-travel-time routing for Tuesday (DI 5 JAN) and Friday (VR 8 JAN), built from real, verified travel data — not estimates.

## Fixed points — do NOT re-litigate these, Mark has locked them today (2026-09-28)

**Tuesday (DI 5 JAN), in this exact order, all fixed by Mark:**
1. New Bhrigu Karyalaya/Bhadury Sadan (Ramapura-Luxa) — starts 09:00, protected ~3-hour window.
2. Tulsi Ghat — Mark's own explicit addition, must come after Bhrigu, before the Ashram.
3. Shree Shree Ma Anandamayi Ashram, Bhadaini — protected, Mark wants a real multi-hour visit (was "open einde", currently compromised to 3h to let the evening fit — open question whether that compromise is even necessary, see below).
4. Dashashwamedh Ghat + Ganga Aarti (evening fire ceremony) — Mark explicitly wants this on Tuesday evening now (moved off Friday because he does not want the evening fire ceremony immediately before boarding the overnight train).

**Friday (VR 8 JAN):**
- Mark wants Friday to be a genuinely full day with REAL content (not filler, not A*-graded optional extras — he explicitly said "vergeet de A*") sourced from an actual busy day (Tuesday or Thursday), to lighten that day.
- Kedareshwar Temple/Kedar Ghat is currently tentatively placed on Friday.
- Friday is departure day (overnight train ~00:10) — Mark wants the day calm/manageable, not exhausting, but not empty either ("het feit dat ik 's avonds vertrek betekent niet dat ik dan de hele dag niets kan doen").
- The four temples Durga Temple/Durga Kund, Sankat Mochan Hanuman Temple, Lalita Ghat, Nepali/Kathwala Temple are PERMANENTLY EXCLUDED — Mark has rejected them repeatedly and explicitly ("die dingen wil ik niet naartoe... niets met mijn lineage te maken"). Do not propose them, not even as "optional."
- A*-graded items (Subah-e-Banaras, Alamgir Mosque/Dharahara, Lolark Kund, Bhang Lassi/Blue Lassi Shop, etc.) are explicitly OUT OF SCOPE for this exercise per Mark's latest instruction — do not use them to fill time.

**Thursday (DO 7 JAN)** — currently: boat ride Assi→(shortened, direct toward Manikarnika, skipping Panchganga stop) → Ratneshwar Mahadev → Manikarnika Ghat (protected, 3+ hr open end) → lunch/return. This shortening (removing the Panchganga/Trailanga Swami Math stop from the boat route) was CCI's attempt to free content for Friday — you are free to accept, reject or redesign this if a better combination exists.

## Real travel-time data already gathered (2026-09-28, from web research — treat as ground truth unless you find better sourcing)

Ghat sequence (south to north along the river): Assi Ghat (hotel, #1) → Tulsi Ghat (#4) → Bhadaini/Anandamayi Ashram (#5, ~220m past Tulsi Ghat) → ... → Kedar Ghat (#25, mid-point) → ... → Dashashwamedh Ghat (#41) → Manikarnika Ghat (just south of Panchganga in the traditional Panchtirtha order) → Panchganga Ghat/Tailanga Swami Math (#67, far north end).

Verified/estimated legs:
- Assi Ghat (hotel) ↔ New Bhrigu Karyalaya (Ramapura-Luxa): car, ~3.2-4 km, 20-35 min (two independent estimates; use the tighter 20-35 min figure).
- New Bhrigu Karyalaya → Tulsi Ghat: car, ~3.2-3.5 km, 15-20 min.
- Tulsi Ghat → Anandamayi Ashram, Bhadaini: walk, ~0.2 km, 4-6 min (near-adjacent).
- Anandamayi Ashram, Bhadaini → Dashashwamedh Ghat: walk ~2.2-2.4 km / 40-55 min (crowded ghat promenade); OR boat ~20-25 min. Boat recommended if this leg is used.
- Assi Ghat (hotel) → Panchganga Ghat/Tailanga Swami Math: **no direct car route exists** — that stretch of the old city is a pedestrian zone. Realistic options: (a) drive to nearest accessible point (Maidagin/Bulanala) ~25-35 min + walk ~10-15 min ≈ 40-50 min total; (b) boat ≈ 30-40 min (but this duplicates Thursday's boat corridor); (c) full ghat-walk from Assi ≈ 3.6 km / 70-90 min.
- Panchganga Ghat → Kedar Ghat: walk, ~2.1-2.2 km, 35-45 min (no direct car route between these two old-city ghat points).
- Kedar Ghat → Assi Ghat (hotel): ~20-30 min (full ghat walk ~1.4-1.6km, or walk-to-road + auto ~2-2.5km).
- Shortened dawn boat Assi Ghat → near Manikarnika directly (skipping Panchganga): ~2.5-3 km, 35-50 min one-way (vs. 60-90 min for the full Assi→Panchganga tour).

CCI's read: the Panchganga/Tailanga Swami Math cluster is geographically expensive to reach except by boat, which would duplicate Thursday's boat corridor if also used Friday. This may mean Panchganga/Tailanga Swami Math is NOT actually a good candidate to relocate to Friday — but this is exactly the kind of judgment call Mark wants an independent second opinion on. Feel free to conclude the opposite if the numbers support it.

## Required deliverable

- A recommended Tuesday (DI 5 JAN) full-day sequence with real travel legs (mode, distance, minutes) for every transfer, using the `TOTALE TIJD VOOR DEZE LOCATIE` / `TIJD VRIJGEMAAKT ALS DEZE GESKIPT WORDT` format from the travel-value rule, respecting the fixed points above.
- A recommended Friday (VR 8 JAN) full-day sequence, same format, built from real A/A+ content taken from an actual busy day (Tuesday or Thursday) — explicitly state which day you are lightening and by how much clock time.
- Explicit comparison: does your combination beat CCI's current draft (Bhrigu→Tulsi Ghat→Ashram(capped 3h)→boat→Dashashwamedh on Tuesday; Panchganga cluster + Kedar Ghat on Friday)? Where does it differ and why?
- Flag honestly if no combination reaches Mark's "Friday content until ~14:00" target without either (a) reusing A*-items he's ruled out, (b) reusing the excluded four temples, or (c) accepting a long/tiring walk — don't force a fake-optimal answer if the geography genuinely doesn't support one.

## Do NOT

- Do not change grades (A/A+/A*) for any location.
- Do not reinstate Durga Temple/Sankat Mochan/Lalita Ghat/Nepali Temple in any form.
- Do not touch Wednesday (WO 6 JAN) — Mark has separately fixed that day light and explicitly excluded it as a source ("van een andere DRUKKE dag" — Wednesday is not busy).
- Do not produce a final PDF/artifact update — this is a routing/timing analysis only, for Mark and CCI to review and decide between.

Commit the result on a dedicated Work branch and report on PR #23 as:
`WORK_RESULT — Varanasi Tuesday/Friday travel-time optimization`

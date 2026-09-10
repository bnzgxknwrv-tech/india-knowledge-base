# INDIA19 ROUTE TOPOLOGY RECONCILIATION — 2026-09-10

Status: `COMPLETE__INCUMBENT_LEADING__NOT_MARK_LOCKED`
Session: `INDIA19`
Branch: `agent/india8-cluster-casting`
Purpose: reconcile the four external AI route analyses with the 2026-09-09 Nirmal Dham relocation and the latest operational deltas, without reopening FINAL OUT worlds or changing any Mark grade.

## 1. Governing sources / precedence

Current controlling sources:
- `governance/CURRENT_STATE.md` and `governance/SUCCESSOR_SAFE_STATE.md` after the 2026-09-10 governance sync;
- `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md`;
- `decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md`;
- `decisions/AGRA_TAJ_ONLY_DEPART_ASAP_MARK_DECISION_2026-09-09.md`;
- `runs/active/FOUR_AI_ROUTE_RECONCILIATION_RESULT_2026-09-09.md`;
- `runs/active/INDIA18_FINAL_EXTRACTION_2026-09-09.md`;
- worker global topology result at commit `7c206ece6efee0f548e3b72ebf3022f3573282ca`;
- WORK Agra->Gaya corridor result at commit `928052f16edfeaf75aba1e60d8c587036eb94e64`;
- `research/AI156_AI1112_EASY_CONNECT_19DEC2026_VERIFICATION_2026-09-09.md`.

Precedence applied:
1. newest explicit Mark decision;
2. newer current-state/handoff material;
3. verified worker/CCI evidence;
4. older external-AI recommendations only as evidence, never as authority.

## 2. Corrections that materially change the older comparisons

1. There are **four** complete external AI analyses, not six. No AI5/AI6 is inferred.
2. Nirmal Dham no longer belongs on 19 Dec. Default is final Delhi safety/buffer on 20 Jan; AI155 safety outranks the visit.
3. Same-day DEL->GAY is real as a planning candidate: official Winter 2026 material publishes AI429 15:00->16:40. Existence alone does not prove a safe self-connect after AI156.
4. The earlier four-AI Varanasi-first lead depended heavily on a qualifying AI156->AI11xx Easy Connect. The **programme/example is real**, but exact 18/19 Dec 2026 one-PNR applicability to Mark's already-owned international ticket is still unverified.
5. Mark's live Air India result showed a serious separate-ticket VNS candidate at 16:00->17:25, but an ordinary separate-ticket self-connect is not protected against AI156 delay.
6. Agra is now Taj-only/depart-ASAP. General Agra filler cannot justify time or an awkward late-trip hotel construction.
7. WORK `928052f` already closed the Prayagraj/Allahabad opportunity-stop question for the Agra->Gaya corridor: direct 12988 remains the whole-human winner. This is reused, not re-researched.

## 3. Hard envelope preserved

- AI156 arrives Delhi on 19 Dec 2026 around 10:15 planning time.
- AI155 departs Delhi 21 Jan 2027 around 12:20.
- Exactly 33 physical India nights: 19 Dec through 20 Jan.
- Exactly one final Delhi night immediately before AI155.
- Nainital 3n.
- Dunagiri/Kukuchina 3n.
- Haidakhan 3n with two complete protected quiet days.
- Agra current retained architecture: 1 hotel night, Taj [A+] protected.
- Varanasi/Sarnath 8n `LOCKED_BY_MARK`.
- Kolkata/Dakshineswar current serious working block 3n.
- Bodh Gaya 3n strongly supported / 2n comparison baseline, still subjective-duration live.
- Tiruvannamalai 4n serious live option / older 5n reopened.
- FINAL OUT remains FINAL OUT: Puri/Odisha; Serampore/Srirampur as stop/world/sleep/excursion; Vrindavan/Braj/Mathura/Govardhan.

## 4. Candidate 1 — incumbent / Kumaon-first

Current leading BODH3/TIRU4 surface:

- 19 Dec: Delhi/Gurugram -> Kumaon sleeper night.
- 20–22 Dec: Nainital 3n.
- 23–25 Dec: Dunagiri/Kukuchina 3n.
- 26–28 Dec: Haidakhan 3n; two full quiet days protected inside the block.
- 29 Dec: preferred human-quality exit via day train 12039 KGM ~15:15 -> NDLS ~20:55; intermediate Delhi transit hotel night.
- 30 Dec: Delhi -> Agra; Agra hotel night.
- 31 Dec: earliest practical Taj Mahal visit, then recovery/waiting rather than filler; 12988 Agra Fort -> Gaya sleeper night if exact-date operation/1A is confirmed.
- 1–3 Jan: Bodh Gaya 3n.
- 4–11 Jan: Varanasi/Sarnath 8n.
- 12–14 Jan: Kolkata/Dakshineswar 3n.
- 15–18 Jan: Tiruvannamalai 4n.
- 19 Jan: Chennai 1n.
- 20 Jan: final Delhi hotel night + Nirmal Dham only if the safety buffer remains intact.
- 21 Jan: AI155.

Night proof:
`1 rail + 3 Nainital + 3 Dunagiri + 3 Haidakhan + 1 intermediate Delhi + 1 Agra + 1 rail + 3 Bodh + 8 Varanasi + 3 Kolkata + 4 Tiru + 1 Chennai + 1 final Delhi = 33`.

Why it remains strong:
- no unprotected same-day domestic self-connect after AI156;
- Kumaon is early, far from AI155;
- Agra precedes Gaya, preserving the highly asymmetric sleepable 12988 eastbound edge;
- 29 Dec day-train exit avoids the 04:10 Old Delhi arrival penalty;
- only two modeled heavy days in the prior global comparison;
- total modeled waking loss (~57 h) is within ~1 h of the fastest challengers, smaller than the model's ±2 h full-route uncertainty;
- first-night sleep is worse than a Varanasi hotel, but later transfer/sleep geometry is materially cleaner.

## 5. Candidate 2 — Varanasi-first synthesis

Four-AI leading conditional surface:

`DEL -> VARANASI -> BODH GAYA -> KOLKATA -> TIRUVANNAMALAI/CHENNAI -> KUMAON -> AGRA -> FINAL DELHI`

Its strongest genuine advantage:
- if AI156 can connect safely into Varanasi on 19 Dec, Mark gets a real hotel bed on the first India night instead of a night train;
- eastbound Varanasi -> Bodh -> Kolkata sequencing is clean;
- Tiruvannamalai can move to early January, potentially avoiding mid-January Pongal pressure.

Why it does **not** currently beat the incumbent:

### 5.1 Failure tolerance
The exact one-PNR Easy Connect product for 18/19 Dec 2026 has not been proven for Mark's already-owned international ticket. The currently serious 16:00 VNS option is a self-connect unless Air India can protect/reissue it. Therefore the arrival edge is not allowed a safety PASS simply because the flight exists.

### 5.2 Late Kumaon exposure
The challenger moves Nainital/Dunagiri/Haidakhan to roughly 9–18 Jan. That places winter mountain roads, fog and the north exit much closer to AI155. There is still an Agra/final-Delhi layer afterward, but failure-recovery depth is materially worse than with December Kumaon.

### 5.3 Jan 8 compound transfer
The synthesis requires a Chennai->Delhi flight plus airport egress/cross-city transfer plus a Delhi->Kathgodam sleeper on the same day. This is a heavy compound travel day, not a free use of a rail night.

### 5.4 North exit / Agra geometry
Using 15014 creates an approximately 04:10 Old Delhi arrival, station-change/waiting burden and then Agra. Replacing that with 12039 is humanly better but changes the night geometry and still leaves an awkward Agra-at-end construction.

### 5.5 Agra Taj-only/depart-ASAP tension
The challenger allocates an Agra hotel night near 19 Jan. If Taj is visited after arriving from the north, Mark's newest rule says depart as soon as a good onward connection exists; keeping a post-Taj Agra hotel merely to preserve the old night shape is not a valid content reason. If the hotel night is placed before an early Taj instead, north-exit timing becomes harder. The incumbent naturally solves this: sleep Agra before Taj, then use 12988 eastbound after Taj.

### 5.6 Whole-human burden
The prior global model put same-day VNS near ~56 h waking loss versus ~57 h incumbent, but with about four heavy days versus two and lower sleep-quality scoring. A nominal ~1 h advantage is below the model's uncertainty and is not enough to outweigh the safety/sleep penalties.

### 5.7 Date quality is mixed, not a decisive VNS-first win
Early-January Tiruvannamalai may avoid Pongal pressure; December Kumaon may preserve the previously identified 25 Dec YSS Christmas meditation opportunity. Both need exact 2026/27 verification before being given hard value. No decisive date-quality win is proven today.

## 6. Candidate 3 — same-day Gaya/Bodh Gaya

Same-day DEL->GAY via AI429 is a **real** candidate and must not be called impossible.

Current reading:
- nominal waking-loss model was slightly lower than incumbent (~55.5 h versus ~57 h);
- but arrival-day international->domestic self-connect robustness is not yet proven;
- it scored more heavy days and worse sleep quality in the global worker comparison;
- Gaya-first then requires Gaya->Varanasi westward before returning east to Kolkata, losing some of the directional elegance of Varanasi-first;
- it does not preserve the incumbent's Agra->Gaya sleeper advantage in the same clean way.

Result: valid challenger, but currently behind both the incumbent and a hypothetically protected Varanasi-first product.

## 7. Candidate families not promoted

Reverse/south-first, CCU-first, MAA-first, flight-heavy, train-heavy and Agra-last variants were already stress-tested in the prior global worker. They either increased waking burden, heavy days, late-trip risk, base churn, or broke duration feasibility. No new Nirmal rule reverses those defects because removing Nirmal from 19 Dec only changes the arrival-day constraint; it does not remove their other structural penalties.

Agra-last specifically remains weak because:
- reverse Gaya->Agra is daytime-heavy;
- Delhi->Agra->Delhi duplication appears near AI155;
- the Taj-only/depart-ASAP rule removes any content justification for padding Agra;
- the incumbent's Agra->Gaya directional sleeper is lost.

## 8. Head-to-head verdict by lexicographic objective

| Criterion | Incumbent/Kumaon-first | Varanasi-first | Same-day Gaya |
|---|---|---|---|
| 33/33 hard feasibility | PASS on current planning surface | PASS arithmetically, but operational chain has unresolved gates | PASS arithmetically, operational arrival edge unresolved |
| AI155 failure tolerance | **Best**: Kumaon early | Worse: Kumaon/north exit late | Worse than incumbent in prior tested family |
| Arrival connection protection | **Best**: no domestic self-connect required | FAIL/UNPROVEN unless exact protected one-PNR is shown | FAIL/UNPROVEN as safe self-connect merely from timetable existence |
| Waking travel | ~57 h model | ~56 h comparable family | ~55.5 h comparable family |
| Model uncertainty | ±2 h route-level | ±2 h | ±2 h |
| Heavy days | **~2** | ~4 | ~4 |
| Sleep/transfer quality | **strongest overall** despite night 1 rail | best night 1, worse later compound chains | weaker overall |
| Agra directional fit | **best**: Taj -> 12988 eastbound sleeper | awkward late Agra | loses clean incumbent bridge |
| Date quality | mixed; possible YSS Christmas benefit | mixed; possible Tiru/Pongal benefit | mixed |
| Current recommendation | **LEADING** | conditional challenger | third |

The apparent 1–1.5 h waking advantage of the flight-first variants is not decision-grade superiority because it sits inside the model uncertainty and is purchased with more heavy days and materially worse failure tolerance.

## 9. Reconciled verdict

`CURRENT_ROUTE_LEAD = INCUMBENT / KUMAON-FIRST`

Recommended current macro order:

`DELHI ARRIVAL -> KUMAON -> AGRA/TAJ -> BODH GAYA -> VARANASI/SARNATH -> KOLKATA/DAKSHINESWAR -> TIRUVANNAMALAI -> CHENNAI -> FINAL DELHI/NIRMAL -> AI155`

This is a **planning recommendation, not a new Mark lock**.

Why the four-AI Varanasi-first lead is demoted from `LEADING_CONDITIONAL` to challenger:
- its key Easy Connect premise is not proven for Mark's actual already-owned ticket/date;
- its first-night hotel advantage is real but not large enough to compensate for the later January north/Agra burden;
- the latest Agra Taj-only/depart-ASAP rule strengthens the incumbent's natural pre-Taj hotel + post-Taj eastbound sleeper geometry;
- WORK has independently confirmed that the Agra->Gaya direct sleeper corridor should not be broken for a Prayagraj opportunity stop;
- the prior waking-hour difference is below route-model uncertainty.

Confidence: `MODERATE-HIGH` for incumbent as the **current robust leader**, not for a final immutable calendar.

## 10. What could still reverse this verdict

A Varanasi-first route should only be promoted again if a material new package is proven, not merely because an afternoon flight exists. Minimum trigger set:

1. Air India shows a genuinely protected one-ticket/one-PNR AMS->VNS itinerary for 18 Dec 2026 using AI156 plus a suitable onward sector, with missed-connection protection clear enough for this route decision; **and**
2. the late north exit is redesigned without the 04:10-style burden or fragile MAA->DEL->night-train chain; **and**
3. the required Agra hotel + Taj-only/depart-ASAP geometry is solved without adding late-trip fragility or duplicate Delhi->Agra movement; **and**
4. the exact A/A+ day-card audit still fits all hard durations.

Without that compound material delta, do not reopen the whole topology simply because one flight/fare changes.

## 11. Closed inputs / do not duplicate

- Do not re-research whether DEL->GAY exists: it does in current official winter planning evidence.
- Do not re-litigate the Easy Connect programme in principle: it exists; exact one-PNR applicability is the only relevant unresolved product question.
- Do not repeat the Prayagraj/Allahabad opportunity-stop search after Taj: WORK `928052f` already closed it in favour of direct 12988.
- Do not revive FINAL OUT worlds.
- Do not invent AI5/AI6 analyses.

## 12. Exact next action

Close the exact retained A/A+ coverage audit against current canon and the 22-page review surface.

Required classifications:
- `EXPLICIT_GUARANTEED`
- `HIDDEN_IN_CLUSTER`
- `CONDITIONAL`
- `MISSING`
- `SPECIAL_STATUS`

Do not call the route/calendar final until every retained physical A/A+ is individually accounted for and Mark has closed remaining Bodh 2/3 and Tiru 4/5 subjective fit.

END INDIA19 ROUTE TOPOLOGY RECONCILIATION

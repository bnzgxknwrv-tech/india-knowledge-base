# KUMAON NORTH CORRIDOR — SLEEP-BASE + ENROUTE OPTIMIZATION — 2026-09-14

Status: **CORRIDOR ANALYSIS, NO NEW GRADES, NO LOCK CHANGE**
Branch: `agent/india8-cluster-casting`
Task: PR #23 CCI_TASK "KUMAON NORTH CORRIDOR SLEEP-BASE + ENROUTE OPTIMIZATION"
Bound input: `runs/active/KUMAON-ORIGINAL-SWEEP-RECOVERY-2026-09-14.md` (commit `f9427c0`)
Method: real current road-distance research (WebSearch, multiple independent sources cross-checked) layered onto the existing archive geometry — not Google-style straight km, whole-human door-to-door estimates below.

## 1. REAL CURRENT LEG DISTANCES (fresh research, this pass)

| Leg | Distance | Realistic mountain-road time |
|---|---|---|
| Nainital ↔ Kainchi/Bhumiadhar | ~18–20 km | 45–70 min (archive, unchanged) |
| Nainital → Almora | ~61–68 km | ~1.5–2.25 h |
| Almora → Kasar Devi / Crank's Ridge | ~8.5 km | ~20–30 min |
| Almora → Jageshwar | ~35–36 km | ~1–1.5 h realistic (not the implausible "36 min fastest" figure some sources show) |
| Almora → Dwarahat | ~61–72 km (sources vary) | ~2–2.5 h |
| Jageshwar → Dwarahat (direct) | ~102–106 km | ~2.5–3.5 h — **NOT a natural link**, confirms Jageshwar and Dwarahat sit on different spurs off Almora, not near each other |
| Dwarahat → Kukuchina/Dunagiri | ~15–19 km road | ~45–60 min, **plus** a separate ~3 km / 365-step trek to the cave/temple area itself |
| Kainchi → Dwarahat (existing archive "direct spine") | ~71.7 km | ~2h24, bypasses Almora entirely |

**Geometry conclusion:** Almora is the real hub for Kasar Devi/Crank's Ridge (cheap, 8.5 km) and for Jageshwar (moderate, 35 km) — both branch off Almora, not off each other. Dwarahat is a *separate* spur; reaching it via Almora (~65–72 km from Almora, i.e. roughly Nainital→Almora→Dwarahat ≈130–140 km total) costs materially more raw distance than the existing Kainchi-direct spine (~90 km total from Nainital via Kainchi). **The Almora detour is real, not free** — roughly +40–50 km / +1–1.5 h one-way versus the direct spine — but it is the only way to reach Kasar Devi/Jageshwar without a dedicated separate day.

**Residual uncertainty flagged, not resolved here:** whether the existing Dhokaney/Suyalbari road branch (archive: "road access on the Almora/Suyalbari branch") physically continues into Almora on the same road, or requires backtracking, needs a live map check before any final lock — this analysis assumes it plausibly does (consistent with the archive's own framing) but this is the single most important thing to verify before committing to Scenario 2 or 3 below.

## 2. STRUCTURAL CLASSES TESTED

**A. Keep all 3 Nainital nights, 21 Dec as daytrip.** Already covered in the prior recovery file. Works for Kasar Devi/Crank's Ridge (short, Nainital→Almora→Kasar Devi→Almora→Nainital ≈ 140 km round trip, long but doable in a winter day if ridge dwell is kept modest) or for Jageshwar (Nainital→Almora→Jageshwar→Almora→Nainital ≈ 210 km round trip — a genuinely long day, tight even in full winter daylight, undesirable per the "quiet dwell" priority already recovered from INDIA20).

**B. Preserve total Nainital 3 nights, but resequence which nights are consecutive / insert one intermediate Almora-area sleep.** This would require *not* sleeping 3 consecutive nights at Hotel Evelyn, which the current lock is silent on (`Nainital 3n LOCKED` fixes total nights and the property, not necessarily their exact calendar contiguity) — but doing so risks a second luggage/base change for a low marginal gain versus Option C, and is **not recommended** without an explicit Mark ask, since it complicates the currently simple 3-consecutive-night Evelyn stay for a benefit already achievable via C.

**C. Keep Nainital nights untouched, make 23 Dec a richer one-way transfer through Almora.** This is the structurally strongest option: 23 Dec already changes sleep base (Nainital → Dunagiri) and already includes Dhokaney + Kakrighat. Routing that same transfer via Almora instead of the Kainchi-direct spine adds the ~40–50 km/1–1.5 h Almora detour ONCE (not twice, as a daytrip-and-return would), and picks up Kasar Devi/Crank's Ridge (nearly free at 8.5 km from Almora) and optionally Jageshwar (35 km further) on the way to Dwarahat/Dunagiri.

**D. Hard-lock check.** Nainital 3 nights and the Hotel Evelyn property are `LOCKED_BY_MARK` — none of the above touches that. Dunagiri's 3-night Dunagiri Retreat base is likewise untouched. No scenario below proposes changing either lock.

## 3. SCENARIOS (sleep-by-night)

**Scenario 1 — status quo, ridge as 21-Dec Nainital daytrip (from the prior recovery file).**
N1/N2/N3 Nainital (Evelyn) → 23 Dec Nainital→Dhokaney→Kakrighat→Dwarahat(direct spine)→Dunagiri.
Pros: simplest, no route redesign, ridge dwell protected on its own day.
Cons: ~140 km round-trip day just for the ridge; Jageshwar not used at all unless a second dedicated day is spent (not proposed); most driving-heavy of the credible options if both ridge AND Jageshwar matter to Mark.

**Scenario 2 — 23-Dec transfer routed via Almora, ridge + Kasar Devi picked up en route, Jageshwar deferred/skipped.**
N1/N2/N3 Nainital → 21 Dec free/quiet or light local day (Nainital-based, per existing safe-state framing, no forced content) → 23 Dec Nainital→Dhokaney→(Almora area, ~8.5 km detour to Kasar Devi/Crank's Ridge)→Dwarahat→Dunagiri.
Pros: uses the free 21 Dec for genuine rest/dwell (matches the recovered "quiet dwell" priority) instead of a long round trip; ridge visited nearly free as part of the transfer; single base change (already happening anyway on 23 Dec).
Cons: 23 Dec becomes a longer, heavier transfer day (~+1–1.5 h over the direct spine) with more content packed in (Dhokaney + Kakrighat + ridge before reaching Dwarahat/Dunagiri) — real risk of a rushed, non-"quiet dwell" ridge visit if the day is already tight; winter daylight discipline becomes more important, not less.

**Scenario 3 — 23-Dec transfer via Almora with BOTH ridge and Jageshwar, 21 Dec used as a genuine rest/buffer day.**
Same as Scenario 2 plus a further ~35 km/1–1.5 h detour from Almora to Jageshwar before continuing to Dwarahat.
Pros: captures the ~124-temple Jageshwar complex without a second dedicated day.
Cons: this stacks Dhokaney + Kakrighat + Kasar Devi + Jageshwar + the Dwarahat-Dunagiri leg into ONE winter day — almost certainly **not whole-human feasible** in December daylight (roughly 10–10.5 h) without cutting real dwell time at every stop, including the pilgrimage-quality ones (Kakrighat, the ridge) that specifically call for unhurried time. **Not recommended as a single day.**

**Scenario 4 — split the load: 21 Dec = dedicated Jageshwar-from-Nainital daytrip (Option B from the prior file); 23 Dec transfer via Almora for Kasar Devi/Crank's Ridge only (Scenario 2's routing).**
Pros: gives BOTH Jageshwar and the ridge world real, unhurried time on separate days, without adding a night or breaking either lock; the ~124-temple complex gets its own dedicated visit rather than being squeezed into a transfer day.
Cons: 21 Dec is no longer a rest day (it becomes the longest single day of the north loop, ~210 km round trip); this only works if Mark actually wants BOTH Jageshwar and the ridge enough to spend two demanding days rather than resting on the one genuinely free day.

## 4. HEAVY-A FILTER (CCI_TASK_ADDENDUM, PR #23) — APPLIED TO EVERY CANDIDATE ABOVE

Mark's explicit filter: only retain a candidate if it has (a) a direct, specific physical link to a core person/lineage already central to this trip (Yogananda, Sri Yukteswar, Vivekananda, Ram Dass, Neem Karoli Baba/Maharajji, Mahavatar Babaji/Lahiri/Kriya, Anandamayi Ma), or (b) an existing strong A/A+ Mark grade, or (c) spiritual relevance strong enough to beat simply spending more time in the already-central YSS/Dunagiri-Babaji world. B, C, generic traveler magnets, and "on-route" architecture/nature/history do not qualify.

| Candidate | Person/lineage link | Existing grade | Passes heavy-A? |
|---|---|---|---|
| Grot Vivekananda / Kasar Devi Cave | Vivekananda's own 1890s Kasar Devi meditation (archive-documented) | **A+, already locked** | **YES** |
| Lama Govinda's Kasar Devi Ashram / Bodh Ashram | **Direct**: Maharajji told Ram Dass "Go see Lama Govinda" — official Ram Dass material | OPEN/UNGRADED (exact entity) | **YES** — the strongest single person-link finding in this whole ridge world |
| Turiya Niwas (Sunyata's hermit house) | Indirect only — Sunyata himself is not one of Mark's core Top-X people; NOT a proven Ram Dass site | OPEN/UNGRADED | **Borderline** — passes only because it sits inside the same short ridge visit as the two entries above, not on its own independent merit |
| Jageshwar Dham + Dandeshwar (~124 temples) | **None** — archive itself states this explicitly: "niet één van Marks primaire Kriya/NKB-persoonsankers" (regional Shiva-pilgrimage/architecture reason, not a Mark-core-person anchor) | plain A (not A+) | **NO** |
| Chitai Golu Devta | None — archive: "standalone regional spiritual/cultural attraction, not a Top-X person anchor" | A, bundle-only | **NO** |
| Dwarahat historic ASI temple groups | None (architecture) | A\*, SKIP_FIRST | **NO** |
| Katarmal Sun Temple | None (architecture) | B | **NO** (already excluded by grade alone) |
| Dhokaney Waterfall | None (nature) | conditional A\* | **NO** as an independent corridor decision — already just a bundled existing stop, not a new heavy-A candidate |
| Lakhudiyar rock shelter, Almora bazaar/Tamta copper | None | never graded (orphans) | **NO** |

**Consequence: Jageshwar fails the heavy-A threshold.** It is genuinely spectacular and was Mark's own early memory, but on person-lineage grounds — the explicit test Mark just set — it does not compete with the ridge's direct Vivekananda/Ram Dass/Maharajji links. **Scenario 4 (dedicated Jageshwar day) is withdrawn from the Mark-facing recommendation.** Jageshwar itself is not deleted from canon (still plain A, still a legitimate future reconsideration if Mark's own priority differs from this filter), but it should not be presented as competing for the recovered 21-Dec day under the criteria just set.

## 5. NULL/FALLBACK OPTION — REQUIRED BY THE ADDENDUM

**NO NEW CORRIDOR DAY** — use the recovered 21 Dec for extra protected immersion in the already-central YSS Dwarahat / Dunagiri-Babaji world, or leave the Nainital block more spacious (less rushed Kainchi/Bhumiadhar pacing, more unhurried Naini Lake/Hanuman Garhi time). This costs nothing new, adds zero driving, and directly serves the same "quiet dwell over site count" priority already recovered from INDIA20's live memory.

## 6. RECOMMENDATION (REVISED UNDER THE HEAVY-A FILTER)

Only two real options remain after the filter — the ridge (via Scenario 2's routing) and the null/fallback option. Both pass the heavy-A bar honestly: the ridge on direct person-lineage grounds, the fallback because more immersion in an already-A+/A+ world (Haidakhan, Babaji's Cave, Kainchi) needs no new justification at all.

**Scenario 2 (23-Dec transfer via Almora, ridge picked up nearly free) is the recommended structure IF Mark still wants the ridge world itself** — it is the only surviving corridor candidate, it carries the strongest single Ram Dass/Maharajji link found in this whole recovery ("Go see Lama Govinda"), and it costs the least (the detour is added once, on an already-scheduled transfer day, not as a new day).

**The NULL/fallback option is equally legitimate and should be presented to Mark as a genuine equal, not a consolation prize** — more unhurried time in the Babaji/YSS world he is already fully committed to may simply be worth more to him than a new (even heavy-A) place. This is Mark's call, not a CCI default.

**Scenario 1 (dedicated 21-Dec ridge daytrip) and Scenario 3 (everything in one transfer day) remain viable mechanically but are inferior to Scenario 2** for the same reasons as before (Scenario 1 spends the rest day on driving; Scenario 3 overloads one winter day).

**Scenario 4 is withdrawn** per section 4 above — Jageshwar does not meet the heavy-A bar Mark just set, however impressive it looks.

This is a structural recommendation, not a grade or a lock — Mark still decides, especially the rest-day-vs-Jageshwar tradeoff in Scenario 2 vs. 4.

## 5. CHEAP-BECAUSE-ON-CORRIDOR

- **Kasar Devi / Crank's Ridge from Almora** — 8.5 km, ~20–30 min. Genuinely close once Almora is reached for any reason.
- **Dhokaney Waterfall** — already on the Almora/Suyalbari branch per existing archive; effectively free if the transfer already goes that way.

## 6. LOOKS NEARBY BUT IS ACTUALLY COSTLY

- **Jageshwar from Dwarahat/Dunagiri side** — ~102–106 km / 2.5–3.5 h; this is NOT a viable "swing by on the way" from the Dwarahat/Dunagiri end of the trip, despite both being loosely "Kumaon hill towns." Jageshwar only makes sense from the Almora side.
- **A same-day Jageshwar + ridge + Dwarahat/Dunagiri combination** (Scenario 3) — individually short-sounding legs (8.5 km, 35 km, 65–72 km) add up to a day that does not fit winter daylight with any real dwell time.

## 7. BLOCKED BY UNRESOLVED IDENTITY/ACCESS

- **Turiya Niwas** and **Lama Govinda's Kasar Devi Ashram / Bodh Ashram** — exact current physical entity/access still unresolved (unchanged from prior governance). Until resolved, no scenario above can commit exact ridge-world timing beyond "the Kasar Devi Temple/Crank's Ridge area in general"; this is the same gate already recorded in current governance, not a new finding.
- **Exact Dhokaney-to-Almora road continuity** — plausible from archive framing, not independently map-verified in this pass; needs a live routing check before Scenario 2/3/4 is finalized as a real day plan.

## 8. NOT DONE HERE

No new Mark grades assigned. No lock changed (Nainital 3n, Dunagiri 3n, Hotel Evelyn, Dunagiri Retreat all untouched). No FINAL OUT world reopened. No Bodh Gaya/Tiruvannamalai or global macro work touched.

END KUMAON NORTH CORRIDOR SLEEP-BASE + ENROUTE OPTIMIZATION

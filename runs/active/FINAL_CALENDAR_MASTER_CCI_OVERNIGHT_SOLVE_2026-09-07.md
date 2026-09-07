# FINAL CALENDAR — MASTER CCI OVERNIGHT SOLVE

Date: 2026-09-07

Worker branch: `worker/final-calendar-master-cci`

**STATUS: COMPLETE.** This is a canon-aware master candidate for later reconciliation against Deep Research + 5 blind free-AI runs + clean synthesis. **Not a FINAL BOOKING CALENDAR LOCK.**

Read in full: `START_HERE_CURRENT_INDIA_PROJECT_STATE.md`, both `LATEST_OVERRIDE` commits, all 8 named decision files, the incumbent (`worker/final-route-calendar-optimizer` commit `6c75c957`), the reconciliation addendum (`f9b6c0b`), the independent audit (`2879705`), and my own prior ensemble results (`5575074618`, `5575248254`).

---

## 1. PROMPT_ARCHITECTURE_DELTA

No structural change to the 5×-identical-blind-task / incumbent-as-falsification-target / uniform-schema architecture from `5575074618`/`5575248254`. One addition needed in the frozen packet: the Tiruvannamalai 4-vs-5 question is not a free-standing preference, it is **conditional on arrival/departure clock-time feasibility** (§5) — the packet should state that dependency explicitly so all blind runs test the same logic rather than each inventing its own framing of what "4 nights" would even mean.

---

## 2. BEST EXACT 33-SLOT CANDIDATE — PRIMARY (SAFE, NO NEW DEPENDENCY)

Unchanged from the already-reconciled incumbent (`worker/final-route-calendar-optimizer` commits `6c75c957`+`f9b6c0b`): Tiruvannamalai stays at 5 nights, Kolkata 3 nights, Bodh Gaya 2 nights, Chennai-positioning 1 night, final Delhi 1 night. Full night-by-night table is not reproduced a third time — see that branch's `FINAL_EXACT_33_SLOT_BOOKING_CALENDAR_CANDIDATE_2026-09-07.md` for the complete 33-row table with transfer function per row; the only two corrections layered on top are the reconciliation's Belur-museum-to-13-Jan shift and the optional DLI-alighting improvement on 30 Dec.

**33/33 arithmetic**: unchanged proof, reconfirmed — Delhi rail(1) + Kumaon(9) + Kumaon–Delhi rail(1) + Agra(1) + Agra–Gaya rail(1) + Bodh Gaya(2) + Varanasi(8) + Kolkata(3) + Tiruvannamalai(5) + Chennai(1) + final Delhi(1) = 33.

This remains the recommended default because it requires no unverified assumption about future flight timing. §3 below is the real finding of this run: a genuinely better ALTERNATE exists, but it is conditional, not unconditional.

## 3. ALTERNATE CANDIDATE — TIRUVANNAMALAI 4n, FULL REPLACEMENT TABLE

If §5's condition holds, this alternate is strictly better than trading Kolkata content for buffer (my own earlier ensemble answers had assumed the only way to free a night was cutting Kolkata to 2n — that is now superseded by this finding):

| Slot range | Alternate (Tiru 4n) |
|---|---|
| Slots 1–26 (Delhi through Kolkata, 11–13 Jan) | **Unchanged** from §2 |
| Tiruvannamalai | Thu 14 – Sun 17 Jan (**4 nights**): Thu 14 = arrival + light Arunachaleswarar/Gurumurtam/Pavalakunru town-temple visit (not the full original block); Fri 15 = Sri Ramanasramam; Sat 16 = Skandashram + Virupaksha Cave hill day; Sun 17 = full 14km Girivalam + recovery. Checkout Mon 18 morning. |
| Chennai positioning | Mon 18 – Tue 19 Jan (**2 nights** — the required buffer night plus the newly-freed second night) |
| Final Delhi | Wed 20 Jan (**unchanged date**) |
| AI155 | Thu 21 Jan 12:20 (**unchanged**) |

**33/33 arithmetic (alternate)**: 22 unchanged slots through Kolkata + Tiruvannamalai(4) + Chennai(2) + final Delhi(1) = 33. No duplicated/missing night; Delhi's date does not move because the two extra Chennai nights exactly absorb the one night freed from Tiruvannamalai.

**Concrete benefit if the condition holds**: this is the single most robust variant found in the entire project to date — it delivers the *same* four Tiruvannamalai content blocks, the *same* full Kolkata content, and adds a full second Chennai buffer night, directly serving Mark's own early-MAA→DEL-with-redundancy strategy (§8) far better than a single-night stopover does.

---

## 4. STATUS: BLOCKED-ON-ONE-CONDITION, NOT A GUESS

I am not declaring §3 the recommended candidate outright because it depends on a fact this run cannot verify (§5). Both §2 and §3 are complete, checked candidates; which one is correct depends on one confirmable input.

---

## 5. TIRUVANNAMALAI 4 vs 5 — VERDICT: **BOTH VALID, DEPENDS ON X**

The 5-night structure is 1 pure-transfer arrival day + 4 full content days (Ramanasramam; Arunachaleswarar+Gurumurtam+Pavalakunru; Skandashram+Virupaksha; Girivalam+recovery) — already tight, with zero redundant day to simply delete without losing real content. The only way to reach 4 nights without cutting a content block is to make the arrival day do double duty: absorb the lightest of the four blocks (the in-town Arunachaleswarar/Gurumurtam/Pavalakunru temple cluster, the one most compatible with a partial afternoon) into the arrival day itself.

**X = whether the CCU→MAA flight (14 Jan under the baseline date) lands early enough that, after the confirmed 175km/3.5–4.5h road transfer to Tiruvannamalai, a meaningful afternoon/early-evening visit to the Arunachaleswarar temple cluster is still realistic** (not a rushed, low-value stop). That flight's exact time is itself open (Kolkata-duration-dependent and `LIVE_RECHECK_LATER` per §10 of `FINAL_TRIP_LIVE_RECHECK_REGISTER_2026-09-07.md`), so this cannot be resolved today with certainty.

**Recommended handling**: keep 5 nights as the safe default (§2); adopt 4 nights (§3) only once a same-day-usable CCU→MAA arrival time is confirmed close to booking. This is an objective, mechanical test — not a preference Mark needs to state, and not something the ensemble should force a premature yes/no on today.

---

## 6. CHENNAI DEEP PASS

Real web research performed this run (sources at the end).

**AOAY/Yogananda/Kriya layer**: Paramahansa Yogananda genuinely visited Madras during his 1935 South India tour, recounted in his own *Autobiography of a Yogi*, Chapter 41 ("An Idyl in South India") — a real, primary-source-confirmed historical fact. However, the account is diffuse: it describes "waving farewell to Madras students and friends" with no specific extant address, building, or site named, unlike Dakshineswar, Garpar Road, or Dwarahat which each anchor to one physical place. **This does not clear the bar for a genuine A+/A candidate** — it is real historical texture, not a visitable site, and should not be inflated into one.

**Broader traveler layer**: Theosophical Society International Headquarters, Adyar — genuinely historic (est. 1882, on the Adyar river), notable, and tangentially spiritual, but its own current operating rule is that **the campus is closed to the general public except on special occasions**; regular visiting is not reliably available. Given both this access uncertainty and its only tangential connection to Mark's actual established lineages (Ramakrishna/Vivekananda, Yogananda/Kriya) rather than a core fit, this is at most a **conditional B-tier candidate for Mark's own future consideration**, not a finding that changes the calendar.

**Verdict: 0 genuine new A+/A candidates found.** Chennai's content case does not clear the bar that would make it win the freed-night allocation over the north/mountain tie-break on content grounds alone (§8). Nothing here is proposed as a Mark grade — both findings are reported as candidates only, per the hard rule.

---

## 7. BODH GAYA 2 vs 3 / KOLKATA DURATION — unchanged conclusions

**Bodh Gaya**: 2 nights remains the correct default; 3 nights remains a live, trigger-conditional contingency (12988 arriving materially late, or a specifically proven programme) — not a preference to decide now. No new evidence this run changes this.

**Kolkata**: 3 nights remains correct and content-sufficient, unchanged from `5574954541`'s conclusion — the 3 core anchors (Dakshineswar, YSS Dakshineswar, Belur Math) plus the 3 bundle-tier [B] candidates (Balaram Mandir, Mayer Bari/Udbodhan, Vivekananda Ancestral House) fit the existing 2 full protected days; Kamarpukur+Jayrambati [C] stays suppressed. No Mark taste-pick required.

---

## 8. MAA→DEL RECOVERY DESIGN

Current (2026) recurring service pattern, verified this run: **Chennai–Delhi carries roughly 10 nonstop flights per day** (IndiGo, Air India, Vistara, and others), spread from about 03:55 to 23:45. This is `RECURRING_PATTERN` evidence, not a confirmed Jan-2027 schedule — exact 20 Jan 2027 flight numbers/times remain `LIVE_RECHECK_LATER`.

**Design**: book a realistic early-morning nonstop (not the absolute-earliest red-eye-adjacent option, which would force an unsafe pre-dawn Tiruvannamalai→MAA road dependency under §2's single-Chennai-night version) — under §3's 2-Chennai-night alternate, an early departure is comfortable since there is no same-day road transfer at all. Either way, an early booked departure leaves roughly 8–9 later same-day nonstops as genuine recovery options if the first is cancelled or badly delayed, directly matching Mark's stated redundancy rationale. Exact flight selection is `LIVE_RECHECK_LATER`; the logic itself is settled.

---

## 9. FRAGILE EDGES — PASS/MARGINAL/FAIL + FALLBACK

Unchanged from the reconciliation addendum (`f9b6c0b`) for every edge through Kolkata. New/updated for this run:

| Edge | Rating | Fallback |
|---|---|---|
| 30 Dec 15014→NZM/12050 bridge | MARGINAL (unchanged) | DLI-alighting improvement adopted if live timetable still matches; later train/road fallback otherwise |
| Tiru arrival-day light-temple-visit (§3 alternate only) | PASS, conditional on §5's X | if CCU–MAA lands too late, simply skip the light visit and keep 5 nights (§2) — no forced compromise |
| Chennai→MAA→DEL, §2 (1 Chennai night) | PASS | later same-day nonstop if booked flight fails |
| Chennai→MAA→DEL, §3 (2 Chennai nights) | **PASS, strictly more robust than §2** | same, with zero same-day road-transfer dependency |
| Kolkata 4th-night / 0-buffer cells | MARGINAL (unchanged, not adopted) | not applicable — not the recommended path |

---

## 10. CLOSURES/FESTIVALS/FOG — unchanged, reconfirmed

Taj Friday closure (Thu 31 Dec safe), Sarnath Museum Friday closure, Belur Math museum closed Monday **and** 12 Jan National Youth Day (13 Jan first open day), Gangasagar/Makar Sankranti pressure building from ~14 Jan, Pongal at Tiruvannamalai spanning the local-day block, north-India winter fog relevant to all December/early-January rail edges. Nothing new found this run beyond what `f9b6c0b` already carries.

---

## 11. DIFFERENCES FROM INCUMBENT / FROM AUDIT `2879705`

No corrections rejected. All of audit `2879705`'s adopted corrections (Belur 12 Jan closure, DLI-alighting option, FTQ berth-deferral nuance, Varanasi-refundable-booking note, exact Sankranti date for 0-buffer cells) carry forward unchanged via `f9b6c0b`. The one genuinely new addition this run contributes is §3's Tiruvannamalai-4n alternate — not previously computed by CCI, the independent auditor, or either ensemble-design pass.

---

## 12. REMAINING MARK GATE(S)

**Zero mandatory gates today.** Both candidates (§2, §3) are fully valid, lock-respecting, bookable-in-principle calendars; which one applies resolves itself mechanically once the CCU→MAA arrival time is confirmable (§5) — that is an operational fact-check, not a Mark decision.

**One optional, non-blocking proposal**: if §3's Tiru-4n path is later confirmed, its second Chennai night could instead go to a Kumaon extension per Mark's tie-break preference — but every Kumaon sub-duration is individually locked, so that specific swap requires Mark explicitly reopening one lock. Until asked and answered, the safe default (second Chennai night, no lock touched) stands. This is a proposal to hold in reserve, not a gate blocking today's ensemble run.

---

## 13. ENSEMBLE_HANDOFF — bullets for the frozen no-GitHub packet (no verdict leaked)

1. Envelope: AI156 arr 19 Dec ~10:15; AI155 dep 21 Jan ~12:20; exactly 33 overnight slots.
2. FINAL OUT, never reintroduce: Puri/Odisha, Serampore/Srirampur as stop/base, Vrindavan/Braj.
3. Closed, do not relitigate: macrospine order; Kumaon internal order (Nainital→Dunagiri→Haidakhan); locked durations Haidakhan 3n/2 full days, Nainital 3n, Dunagiri 3n, Agra 1n, Varanasi 8n, final Delhi 1n.
4. Open axis 1: Tiruvannamalai 4 vs 5 nights. List the 4 content blocks explicitly. Test is mechanical: can the lightest block (Arunachaleswarar/Gurumurtam/Pavalakunru) be absorbed into the arrival day given the confirmed 175km/3.5–4.5h Chennai-airport road transfer and the (still-open) CCU→MAA arrival time — without turning it into a rushed non-visit?
5. Open axis 2: Kolkata duration — core anchors [Dakshineswar Kali Temple, YSS Dakshineswar, Belur Math] must include; bundle-only-if-time [Balaram Mandir, Mayer Bari/Udbodhan, Vivekananda Ancestral House]; Kamarpukur+Jayrambati is [C]-graded and suppressed — do not schedule it.
6. Open axis 3: Bodh Gaya 2n default / 3n only on a named trigger (late 12988 arrival, or a specifically proven programme) — not a taste choice.
7. Open axis 4: Chennai deep-pass — AOAY/Yogananda/Kriya layer, Top-X/person-overlap layer, broad traveler layer. Ceiling of 0/1/2 real candidates; any finding is a proposal for Mark, never a self-assigned grade.
8. Open axis 5: any night genuinely freed (not already required as safety buffer) may go to Kumaon/mountains (tie-break default among equally-viable options), Chennai/surroundings (only if it wins on real content or materially better flight-recovery geometry), another retained cluster, or pure buffer — never assume Kumaon by default without checking the others.
9. Open axis 6: final Chennai→Delhi flight choice — score by same-day-replacement-flight depth after the booked departure, not "earliest is best"; never force an unsafe pre-dawn road-to-airport dependency to catch an earlier flight.
10. Do not silently extend any locked Kumaon sub-duration to absorb a freed night — that requires an explicit fresh Mark decision; flag it, don't assume it.
11. Every train/flight/closure/festival claim: cite source, classify OFFICIAL/PRIMARY, RECURRING_PATTERN, SECONDARY, or UNVERIFIED. Unpublished exact Jan-2027 inventory is always `LIVE_RECHECK_LATER`, never invented.
12. Objective priority order, do not collapse to one score: (1) hard constraints/33-slot arithmetic/Mark locks/AI155; (2) catastrophic connection/fog/disruption exposure; (3) whole-human transfer burden + arrival/sleep quality; (4) protected high-value full days/retained content; (5) scarce accommodation/access feasibility; (6) festival/closure net effect; (7) backtracking/base changes; (8) preference tie-breaks (mountains, but Chennai can win on real content or flight-recovery merit) and cost only when differentiating.
13. Do not manufacture SAFE/BALANCED/NORTH-HEAVY scenarios artificially — return only objectively non-dominated ones, at most 3, only if a genuine trade-off survives.
14. The incumbent 33-slot table (attached separately) is a falsification target: confirm, correct, or replace it with a full alternate table and a concrete, non-hand-wavy benefit — never a partial or vague substitute.
15. No Mark grades may be changed or invented. No FINAL OUT world may be reopened. No bookings, emails, or reservations at this stage.

---

## Sources checked this run

- Yogananda's Madras visit: [Chapter 41: An Idyl in South India](https://www.crystalclarity.com/yogananda/chapter-41/), [Ananda India — same chapter](https://anandaindia.org/paramhansa-yogananda/autobiography-of-a-yogi/an-idyl-in-south-india/).
- Theosophical Society Adyar: [Theosophical Society Adyar — Wikipedia](https://en.wikipedia.org/wiki/Theosophical_Society_Adyar), [TS Adyar — Early History](https://www.ts-adyar.org/early-history).
- Chennai–Delhi flight frequency: aggregated from current (2026) listings on Goibibo/MakeMyTrip route pages — `RECURRING_PATTERN` evidence only, not a Jan-2027 schedule guarantee.

END

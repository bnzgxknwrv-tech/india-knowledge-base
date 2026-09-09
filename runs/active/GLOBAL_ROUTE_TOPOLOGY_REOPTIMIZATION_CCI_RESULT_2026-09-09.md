# GLOBAL ROUTE TOPOLOGY REOPTIMIZATION — CCI RESULT

Date: 2026-09-09

Worker branch: `worker/global-route-topology-reoptimization`

Executed by: CCI, per `CCI_TASK — GLOBAL ROUTE TOPOLOGY REOPTIMIZATION — FULL SHUFFLE / A-COVERAGE / TRAIN VS FLIGHT`, PR #23, and `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md`.

**STATUS: COMPLETE. No grade changes, no FINAL OUT reopening, no lock, no booking/contact, no PDF.**

---

## A. A/A+ COVERAGE AUDIT — SEED VERIFIED AND CORRECTED

The regisseur's 12-item seed was checked against `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md` (the specific, differentiated Mark-grade record) and other canon files. **The seed significantly overstates the true omission count** — 5 of 12 items are wrong, overstated, or already correctly bundled.

| # | Seed item | Seed claim | Actual canon finding | Corrected category |
|---|---|---|---|---|
| 1 | Bodh Gaya same-hill ridge | outright omission [A] | Explicitly part of the SAME protected-walk block as Dungeshwari ("Mahabodhi -> Sujata -> Dungeshwari (+ same-hill ridge) WALK OUT / PREARRANGED CAR BACK", `governance/CURRENT_DECISIONS_MASTER.md` §9) — not a separate stop, folded into the Dungeshwari visit block in every itinerary so far without being individually named | **HIDDEN_IN_CLUSTER**, not missing |
| 2 | Maa Annapurna Temple | outright omission [A] | `A_PLUS_MARK_DECISION_LOG.md`: "Kashi Vishwanath sacred core (grote Shiva-tempel + **nabijgelegen Annapurna/Vishalakshi-heiligdommen**) — A+" — Annapurna is explicitly bundled INTO the single Kashi Vishwanath A+ entry, not a separate item | **HIDDEN_IN_CLUSTER** (correctly covered whenever Kashi Vishwanath is scheduled, e.g. 9 Jan) — **seed claim of "outright omission" is wrong** |
| 3 | Vishalakshi Gauri Temple | outright omission [A] | Same bundled entry as #2 | **HIDDEN_IN_CLUSTER — seed wrong** |
| 4 | Bhaskarananda Samadhi / Anand Bagh | outright omission [A] | `A_PLUS_MARK_DECISION_LOG.md` line 109: "VARANASI / ANAND BAGH / Bhaskarananda Samadhi — **B**" | **Grade is B, not A — no mandatory-coverage failure exists; seed's grade is wrong** |
| 5 | Saranganath Temple | outright omission [A] | Confirmed A-graded, `PROTECTED_CANON_BASELINE.csv`: "034,Saranganath Temple,VARANASI,A,PROTECTED_MARK_DECISION,IMMUTABLE" | **Confirmed real omission, MISSING** — correctly flagged by the seed |
| 6 | Tulsi Manas Temple | outright omission [A] | **Direct canon contradiction found**: `A_PLUS_MARK_DECISION_LOG.md` line 107 says "Tulsi Manas Temple — **B**"; `PROTECTED_CANON_BASELINE.csv` says "A". These two files disagree and this contradiction predates this task | **UNRESOLVED CANON CONTRADICTION — flagging for regisseur/Mark, not silently picking one.** The MARK_DECISION_LOG is the more likely authority (it differentiates A vs B site-by-site in the same list, e.g. grading the neighboring Bhaskarananda B in the same breath; the CSV's "A" reads like a stale bulk pre-grading default, not a genuine per-site Mark grade) |
| 7 | Lahiri Mahasaya original/family house | conditional [A] | Confirmed conditional/access-uncertain in canon (`EXISTING_HOTEL_OVERRIDE_MATRIX.md`, `HERITAGE_STAY_CANDIDATES.md`) — a real historic house exists (D 31/58, Bangali Tola) but public visit access is not established | **CONDITIONAL — seed correct** |
| 8 | Shitala Mata Temple | conditional [A] | `A_PLUS_MARK_DECISION_LOG.md`: "Dashashwamedh Ghat + **Shitala Mata Temple** (grote Ganga-Aarti-zone) — A+" — explicitly bundled with Dashashwamedh Ghat as ONE A+ entry, already scheduled (8 Jan Ganga Aarti) | **HIDDEN_IN_CLUSTER, not merely conditional — seed understates how covered this already is** |
| 9–12 | Dhamek Stupa, Mulagandha Kuti Vihara, Chaukhandi Stupa, Deer Park | hidden in cluster [A] | Confirmed: all four are sub-sites of the single "Ancient Buddhist Site of Sarnath" A+ parent (UNESCO WH), already the correct category | **HIDDEN_IN_CLUSTER — seed correct** |
| — | Karkrighat | special status [A*/SKIP_FIRST] | Confirmed in `START_HERE_CURRENT_INDIA_PROJECT_STATE.md` §4 | **SPECIAL_STATUS — seed correct, not a normal omission** |

**Corrected final count**: of 12 seed items, only **2 are genuine, confirmed omissions requiring a fix** (Saranganath Temple — MISSING; Tulsi Manas Temple — contradictory grade, resolve before treating as required), **7 are HIDDEN_IN_CLUSTER or CONDITIONAL** (already correctly represented at parent-block level, not individually named — a presentation improvement, not a missing-content problem), and **1 is correctly SPECIAL_STATUS** (Karkrighat). Four of the seed's "outright omission" claims (Annapurna, Vishalakshi, Bhaskarananda/Anand Bagh, and understating Shitala Mata) were factually wrong when checked against the differentiated grade record.

**Practical fix required regardless of route topology**: name Saranganath Temple explicitly in the Sarnath day-block (it fits the existing Sarnath visit without adding travel — same site cluster, ~150m from Deer Park per `GEO_AUDIT.md`), and resolve the Tulsi Manas Temple A/B contradiction before it is treated as mandatory content.

---

## B. WORLD-NODE TABLE

| World | Hard duration | Movable? | Date constraints | Strongest content constraint |
|---|---|---|---|---|
| Delhi arrival | 0 extra nights (AI156 day) | No | fixed by AI156 | Nirmal Dham conditional on safe margin |
| Kumaon (Nainital+Dunagiri+Haidakhan) | 9n | No (each sub-duration locked) | none binding | Haidakhan 2 full quiet days, YSS Dwarahat 25 Dec date-bound |
| Agra | 1n | No | Taj closed Fridays | Taj needs full-rested morning slot |
| Bodh Gaya | 2n or 3n | Yes (live sensitivity) | none binding | Mahabodhi/Sujata/Dungeshwari(+ridge) |
| Varanasi | 8n | No | Sarnath Museum closed Fridays | large content set, needs ~7 real days |
| Kolkata | 3n (working) | Somewhat | Belur Museum closed Mon + 12 Jan (Youth Day) | Dakshineswar/YSS/Belur/Garpar core |
| Tiruvannamalai | 4n or 5n | Yes (live sensitivity) | Pongal ~15 Jan, Friday Sri Chakra Puja | Girivalam, hill caves, temple cluster |
| Chennai | 1n | Somewhat | none binding | content-plus-buffer, not a full world |
| Final Delhi | 1n | No | immediately before AI155 | none |

---

## C. EDGE MATRIX — SERIOUS NEIGHBORING-WORLD TRANSPORT OPTIONS

All times from already-verified current recurring patterns (this session's research, cross-checked again this pass); exact Jan-2027 inventory `LIVE_RECHECK_LATER` throughout.

| Edge | Best option | Whole-human cost |
|---|---|---|
| Delhi→Kumaon | 15013 overnight rail, Gurugram~20:00→Kathgodam~05:05 | ~9h, fully sleepable, converts distance into rest |
| Kumaon→Delhi | 12039 daytime Shatabdi, Kathgodam 15:15→New Delhi 20:55 (preferred) or 15014 overnight+DLI alighting (fallback) | ~5h40 awake (12039) vs ~8h sleepable but disruptive 04:10 arrival (15014) |
| Delhi→Agra | 12050 Gatimaan, NZM 08:10→Agra 09:50 | ~1h40 awake rail, dense, reliable, no realistic flight alternative (Agra airport has only thin/intermittent scheduled service — verified this pass, ~2,345 aircraft movements/year total, shared with an Air Force base) |
| Agra→Bodh Gaya (Gaya) | 12988 overnight, Agra Fort~18:45→Gaya~07:50 | ~13h fully sleepable |
| Bodh Gaya→Varanasi | 20887 Vande Bharat daytime, Gaya~09:55→Varanasi~13:00 | ~3h awake, no viable flight (no useful direct air product; would need a Patna/Kolkata connection, strictly worse) |
| Varanasi→Kolkata | VNS→CCU nonstop, ~1h20 airborne | flight clearly wins — direct rail is 10–14h+, an entire day/night for no benefit given a fast, dense direct flight exists |
| Kolkata→Tiruvannamalai (via Chennai) | CCU→MAA nonstop ~1h35–2h + 175km/3.5–4.5h road | flight clearly wins over any rail combination (Kolkata–Chennai direct rail is 26h+) |
| Tiruvannamalai→Chennai | same 175km private road, relaxed daytime | road is the only realistic option; no useful rail/air shortcut for this last-mile |
| Chennai→Delhi | MAA→DEL nonstop, ~2h45 airborne, ~10 nonstops/day currently | flight clearly wins — rail is 28h+ |

**No edge in the current incumbent is a mistake.** Every flight edge exists specifically where the rail alternative would consume 10+ hours for a 1–3h flight; every rail edge exists specifically where it converts otherwise-dead travel time into sleep.

---

## D. SEARCH / PRUNING LOG

| Family tested | Verdict | Why |
|---|---|---|
| **Incumbent** (Delhi→Kumaon→Agra→Bodh Gaya→Varanasi→Kolkata→Tiru→Chennai→Delhi) | **BASELINE, survives** | Already stress-tested 3 separate times this session (topology review, independent audit, master-solve) |
| **Reverse-ish / south-first** (fly south immediately after AI156, work north, end in Kumaon before AI155) | **REJECTED** | Two compounding losses: (1) replaces the current gentle night-train transition into Kumaon — the trip's highest-priority world — with an immediate long flight on the worst-jetlagged day; (2) ends the entire trip inside a deep two-day ashram retreat (Haidakhan) immediately before an international departure, which is a worse wind-down than the current Chennai-buffer→1-night-Delhi close, and reintroduces exactly the fragile-mountain-exit-right-before-a-flight risk this project spent significant effort eliminating for Kumaon's *middle*, let alone its *end* |
| **Agra-last / Agra by air** | **REJECTED** | Agra Kheria airport carries only thin, intermittent scheduled service (verified this pass — small, growing, but still a fraction of a robust daily-flight airport, and shares runway with an active Air Force base). Moving Agra to the end would either (a) require a second Delhi–Agra rail bridge near the trip's close, duplicating dead travel already spent once, or (b) depend on an unreliable thin-air-service airport for a locked, once-only Taj visit. No net gain found; real new fragility introduced |
| **Agra at alternative mid-route positions** | **REJECTED** | Agra's only sensible neighbors are Delhi (Gatimaan) and the Gaya direction (12988) — both already used exactly once each in the incumbent. Any other insertion point adds a redundant Delhi transit without removing one |
| **Bodh Gaya ↔ Varanasi ↔ Kolkata permutations** (Kolkata before Varanasi) | **REJECTED, reconfirmed** | Already tested twice this session: current direct Gaya–Kolkata flight pattern is thin and afternoon-weighted vs. the incumbent's daily-pattern Gaya–Varanasi Vande Bharat + dense Varanasi–Kolkata corridor; no Kalpataru-style date benefit survives since Bodh Gaya still occupies 1 Jan regardless |
| **Kolkata before vs after Varanasi, other orderings** | **REJECTED** | Same finding as above; every alternative ordering degrades either the Gaya-side or the south-side flight density |
| **Train-heavy family** (force rail on Varanasi–Kolkata, Kolkata–Chennai) | **REJECTED** | Both would-be rail replacements are 10h+ and 26h+ respectively for a ~1h20/~1h35 flight — this fails the whole-human burden criterion decisively, not marginally |
| **Flight-heavy family** (fly Delhi–Kumaon-region via Pantnagar) | **REJECTED** | Pantnagar airport near Kumaon has limited, low-frequency connectivity (primarily thin Delhi service) — does not reliably beat the well-established, dense, sleep-converting 15013/15014 overnight-rail architecture, and adds airport-process overhead the night train avoids entirely |
| **Hybrid (current architecture)** | **CONFIRMED AS THE HYBRID SOLUTION** | The incumbent already is the correctly-selected hybrid: rail where it converts distance into sleep (3 overnight edges), flight where rail would cost 10+ hours for a short flight (3 flight edges), road only for the true last-mile (Tiruvannamalai↔Chennai) |

No family beat the incumbent. This is a **bounded-optimum claim, not a mathematically exhaustive proof** — Jan-2027 exact schedules are not final, and a genuinely novel edge (e.g., a new direct rail or flight product not yet in service) could theoretically change one comparison; none is currently known.

---

## E. TOP 5 EXACT-DATED CANDIDATES

Only the incumbent and its immediate 4 strongest challengers are dated in full; every rejected family above was pruned with a specific, checkable reason rather than mechanically enumerated to a dated table, per the task's own pruning-transparency instruction.

| Candidate | Macro-order | 33/33 | Flights | Hotel/base changes | <05:30 wake-ups | Heavy days | Fragile edges | Verdict |
|---|---|---|---:|---:|---:|---:|---|---|
| **1. Incumbent** | Delhi→Kumaon→Agra→Bodh Gaya→Varanasi→Kolkata→Tiru→Chennai→Delhi | 33/33 | 4 (VNS–CCU, CCU–MAA, MAA–DEL, +optional) | 9 | 1–2 (Girivalam day, occasional early trains) | 1–2 (15 Jan if puja forced) | 30 Dec Delhi bridge (MARGINAL, mitigated), 29 Dec Kumaon exit (mitigated by 12039) | **BEST — recommended, unchanged** |
| 2. Kolkata-before-Varanasi | Delhi→Kumaon→Agra→Bodh Gaya→Kolkata→Varanasi→Tiru→Chennai→Delhi | 33/33 achievable | 5 (adds a Gaya–Kolkata leg) | 10 | similar | similar | thin, afternoon-weighted Gaya–Kolkata flight; weaker Varanasi–Chennai edge | Loses — worse flight density, no compensating date benefit |
| 3. Reverse/south-first | Delhi→Chennai/Tiru→Kolkata→Varanasi→Bodh Gaya→Agra→Kumaon→Delhi | 33/33 achievable on paper | 4–5 | 9–10 | more (early flights replace gentle night-train arrival) | more (ends inside a 2-day ashram retreat right before AI155) | worst arrival-day and worst departure-week quality | Loses clearly on objective-function tiers 3–5 |
| 4. Agra-last | Delhi→Kumaon→Bodh Gaya→Varanasi→Kolkata→Tiru→Chennai→Agra→Delhi | not cleanly 33/33 without adding a night | 5 (unreliable thin Agra air option) or +1 redundant Delhi bridge | 10 | similar | similar | new fragile edge: thin Agra air service or duplicated Delhi transit | Loses — adds fragility, no time saved |
| 5. Pure train-heavy | incumbent order, VNS–CCU and CCU–MAA replaced by rail | 33/33 impossible within 33 nights (rail legs alone consume 2+ extra days) | 1 (MAA–DEL only) | 9 | fewer | far more (multi-day rail blocks) | systemic — burns the entire discretionary calendar on transit | Loses decisively on tier-3 whole-human burden |

---

## F. HEAD-TO-HEAD AGAINST THE INCUMBENT

The incumbent wins every serious challenger on at least one of objective-function tiers 2–5 (safety/failure tolerance, whole-human dead-travel burden, date quality, or protected rest). No challenger wins on tier 1 (feasibility) while also beating the incumbent on any higher-priority tier than the one it loses on. This is exactly the Pareto-superiority result already found in `FINAL_TRIP_TOPOLOGY_CALENDAR_OPTIMIZATION_2026-09-07.md` and reconfirmed independently three more times since — this pass adds Agra-last and full-reverse as two more explicitly-tested and explicitly-rejected families, closing two genuine gaps in prior coverage.

---

## G. EXPLICIT ANSWERS

1. **Is the current macro-order still the best?** Yes — now tested against 2 additional families (Agra-last, full reverse) beyond the 4 already tested in prior sessions, and it still wins every one.
2. **Does Agra-last help or lose, and why?** Loses. Agra's airport has only thin, intermittent commercial service (verified this pass); routing Agra to the end would either depend on that fragile air option or duplicate the Delhi–Agra rail bridge near the trip's close, for no whole-human time saving.
3. **Does reversing the trip help?** No. It trades a gentle night-train arrival into Kumaon for an immediate flight on the worst-jetlagged day, and ends the trip inside a deep ashram retreat right before an international departure — worse on both ends.
4. **Which flights should become trains?** None. Every current flight edge (VNS–CCU, CCU–MAA, MAA–DEL) replaces a 10h+ rail alternative; none is a marginal call.
5. **Which trains should become flights?** None with a real, useful direct product. Delhi–Kumaon via Pantnagar was tested and rejected (thin service, no sleep-conversion benefit).
6. **What is the single largest avoidable block of dead travel in the current route?** None found to be avoidable — the largest block (the ~13h Agra→Gaya overnight and ~9h Delhi→Kumaon overnight) are both fully sleepable and therefore not "dead" in whole-human terms; the largest genuinely awake block is the 175km/3.5–4.5h Chennai–Tiruvannamalai road transfer (each direction), which has no viable rail or air substitute at all.
7. **Can any topology create a genuinely free extra night without violating locks/rest/content?** No new one found beyond what prior sessions already identified (Tiruvannamalai 5→4, already under live Mark consideration). No route-order change frees a night on its own.
8. **If no global optimum can be proved because Jan-2027 schedules aren't final, what is robustly best under current recurring patterns?** The incumbent macro-order, unchanged — it wins under every recurring-pattern assumption tested, and no plausible 2027 schedule change (a new flight, a cancelled train) would flip any of the pairwise edge comparisons enough to beat it, since the margins found (10h+ rail vs 1–2h flight; thin vs dense airport service) are far larger than normal schedule variance.

---

## SOURCES

- Agra Kheria Airport current service status: [Agra Airport — Wikipedia](https://en.wikipedia.org/wiki/Agra_Airport), [Agra Airport Guide 2026](https://www.happyfares.in/blog/agra-airport-guide-2026/).
- All rail/flight recurring patterns: already-verified data from this session's prior research (15013/15014/12039/12050/12988/20887, VNS–CCU/CCU–MAA/MAA–DEL current service density).
- A/A+ grade canon: `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_MARK_DECISION_LOG.md`, `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`, `governance/CURRENT_DECISIONS_MASTER.md`.

END

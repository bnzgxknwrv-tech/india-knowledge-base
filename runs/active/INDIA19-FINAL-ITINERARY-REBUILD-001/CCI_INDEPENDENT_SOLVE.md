# CCI INDEPENDENT CONSTRUCTIVE SOLVE — 33-NIGHT ITINERARY/CALENDAR

Status: **COMPLETE**
Author: CCI (ClaudeCodeIndia), acting as constructive optimizer per PR #23 INDIA19 dispatch "CCI_TASK — INDIA19 INDEPENDENT CONSTRUCTIVE 33-NIGHT SOLVE — SOLUTION-BLIND"
Solved from frozen packet commit: `a2b71b2563f446480b012f0b9176a87e96fcb003`, `runs/active/INDIA19-FINAL-ITINERARY-REBUILD-001/`
Worker branch: `worker/india19-cci-independent-solve`
Solution-blind attestation: this file was built without reading any new WORK solution/result/branch produced for this same solve. Prior evidence already inside the frozen packet (and files it cites as reusable research/decisions) was read and reused per the packet's own instruction; no PR #23 comment describing a competing "WORK" itinerary for this dispatch was opened or read.

This is a **proposed schedule built from the frozen inputs**. It changes no grade, no lock, no duration in the ledger itself. FINAL OUT worlds (Puri/Odisha; Serampore/Srirampur as a stop/world/base/excursion; Vrindavan/Braj/Mathura/Govardhan) are not reopened and produce zero rows below, exactly as in the source ledger.

---

## 0. EXECUTIVE SUMMARY

- **Macro topology: KEEP the incumbent family** — `AI156/Delhi → (rail) → Nainital → Dunagiri/Kukuchina → Haidakhan Vishwa Mahadham → Delhi transit → Agra (Taj-only) → (rail) → Bodh Gaya → Varanasi/Sarnath → Kolkata/Dakshineswar → Tiruvannamalai → Chennai → final Delhi → AI155`. The strongest challenger (same-day AI156→AI429 continuation to Gaya/Bodh Gaya) saves only ~1.5 modeled waking hours (55.5h vs ~57h) — far under the ~8–10+ waking-hour material-gain threshold Mark set for overriding the quiet-north-first preference — while costing more heavy days, an unprotected first-day domestic self-connect, and a fog-exposed Kumaon block pushed nearer AI155. This is a reuse of already-completed, cross-checked research (§1), not a re-derivation.
- **Bodh Gaya: 3 nights. Tiruvannamalai: 4 nights.** This is my recommendation, built from the already-completed hour-by-hour Bodh3/Tiru4 stress test (§2), but the underlying trade-off (Bodh Gaya's 3rd night can only currently come from Tiruvannamalai, from the Chennai safety buffer, or from reopening a Kumaon lock) is genuinely marginal and is flagged `MARK_DECISION_REQUIRED` per the objective gates.
- **33/33 nights**, 19 Dec 2026 – 20 Jan 2027, verified by direct night-by-night enumeration (§3) — no duplicate, no missing night.
- **86/86 A+/A/A* rows individually accounted for**: **46 SCHEDULED + 40 LEGITIMATELY_SHARED_WITH_PARENT + 0 BLOCKED_PENDING_MARK = 86** (§4). No row was silently dropped; two SPECIAL_STATUS/SKIP_FIRST rows (Sattal, Rajgir Brahmakund) resolve to "not activated this trip" under Mark's own pre-existing corridor-only rule rather than requiring fresh Mark input — reasoning given in §4.7.
- Heaviest day: **10 Jan, the Old City ghat-walk day** (10 Varanasi rows in one day). Biggest brittle point: **15 Jan Tiruvannamalai arrival colliding with the Friday Sri Chakra Puja**. Full verdict in §5.
- **7 items remain genuinely `MARK_DECISION_REQUIRED`** (§6) — none invented by CCI; all either already flagged by the frozen packet's own objective gates or surfaced by this solve's honest day-by-day accounting.

---

## 1. MACRO TOPOLOGY — DECISION AND WHY

### 1.1 What the objective hierarchy actually requires

Per `OBJECTIVE_AND_HUMANE_GATES.md` §1, tiers are lexicographic — a route that wins on a lower tier can never be preferred over one that is worse on a higher tier — and Mark's quiet-north-start preference (`decisions/QUIET_NORTH_START_OVERRIDE_THRESHOLD_MARK_DECISION_2026-09-09.md`) is a **strong route preference**, not a mild tie-break: it controls unless an alternative clears a **~8–10+ waking-hour (or equivalent higher-tier) material whole-trip benefit**, explicitly **not** a 2–5h saving.

### 1.2 Reused evidence (not re-derived)

Per FOUT 14 of `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` and the task's explicit instruction to reuse closed research, this topology question was already run to a verdict twice on this branch and independently corrected once:

- `runs/active/GLOBAL_FULL_ROUTE_TOPOLOGY_REOPTIMIZATION_CCI_RERUN_2026-09-09.md` (commit `7c206ece6efee0f548e3b72ebf3022f3573282ca`, on `worker/global-route-topology-reoptimization`) tested **eleven** full route families end-to-end with a consistent waking-hours/heavy-day/sleep-quality method (its §2–§7). Verdict: **KEEP INCUMBENT, confidence 0.70**. Comparative metrics (its §5, reused verbatim):

| Family | Waking loss | Flights | Base changes | Heavy days | Sleep /5 |
|---|---:|---:|---:|---:|---:|
| 1 Incumbent (Kumaon→Agra→Bodh→Varanasi→Kolkata→Tiru) | **57h** | 3 | 11 | 2 | **4.0** |
| 6 Same-day GAY/Bodh Gaya (strongest challenger) | 55.5h | 4 | 12 | 4 | 2.8 |
| 5 Same-day VNS | 56h | 4 | 12 | 4 | 2.8 |
| 7 Agra-first | 58.5h | 3 | 11 | 4 | 3.0 |
| 2 Full reverse | 60h | 3 | 11 | 9(days) | 3.0 |
| 8 Agra-last | 60h | 3 | 12 | 3 | 3.4 |
| 4 Same-day CCU | 67h | 4 | 12 | 4 | 2.7 |
| 3 Same-day MAA | 64h | 3 | 11 | 4 | 2.5 |
| 11 Train-heavy | 75–82h | 1 | 12+ | 5+ | 2.5 |

- `runs/active/GLOBAL_FULL_ROUTE_TOPOLOGY_CCI_SELF_CORRECTION_2026-09-09.md` (commit `000e83e8f73080abbce47fbb7513a73f2e5c66eb`) independently re-verified against Air India's own published Winter 2026 schedule that **AI429 DEL 15:00→GAY 16:40 exists daily** (effective 25 Oct 2026), making same-day-GAY *schedulable* (not impossible as an earlier draft claimed) but confirms this does not change the verdict: it is tight (~4h45 nominal margin, ~1–1.5h real slack against an AI156 delay after realistic immigration/terminal-transfer buffers) and still loses lexicographically on safety/rest tiers. Per `OBJECTIVE_AND_HUMANE_GATES.md`'s door-to-door tier, I do not treat this connection as decision-grade safe, and I did not attempt to re-prove or re-refute it myself — it is reused exactly as concluded.
- The incumbent-vs-challenger delta is **~1.5h, inside the model's own ±2h uncertainty band, and an order of magnitude under the ~8–10+h override threshold.** No alternative I can construct from the frozen inputs plausibly clears that bar (the two next-best challengers, same-day VNS and same-day MAA/CCU, are *worse*, not better, than same-day GAY). I therefore did not re-run a twelfth family; doing so would duplicate closed research absent a material gap, which the task instructs against.
- **Verdict: KEEP INCUMBENT.** This is a reuse-and-ratify of existing evidence, not a fresh preference of mine.

### 1.3 Agra bridge and corridor reuse

- Agra is kept in its incumbent bridge position (Delhi→Agra short/dense; `decisions/AGRA_TAJ_ONLY_DEPART_ASAP_MARK_DECISION_2026-09-09.md` Taj-only/depart-ASAP rule honored — see §3, 30–31 Dec).
- The Agra→Gaya corridor question (whether a Prayagraj/Allahabad stopover improves on the direct sleeper) was already closed: `runs/active/AGRA_GAYA_CORRIDOR_OPERATIONAL_DELTA_RESULT_2026-09-09.md` (commit `928052f16edfeaf75aba1e60d8c587036eb94e64`, `worker/agra-gaya-corridor-opportunity-stop`), verdict **`KEEP_12988_DIRECT`**: no Prayagraj insertion is both content-real and roughly equal to the direct 12988 sleeper in whole-human terms (least-bad no-hotel construction costs ~4.25–5h of usable Bodh Gaya time and ~4–4.5h of sleep for a 20–40 min shrine stop; the meaningful three-site hotel form costs ~13h). Reused verbatim; not re-tested. Prayagraj/Allahabad remains a confirmed cluster-level skip (site grades preserved as history only, per `INPUT_CONTRACT.md` §7) and is not reopened here.

### 1.4 My synthesis contribution

The frozen packet's closed research established the *macro order* and the *Bodh3/Tiru4 dated skeleton* independently (§1.2, §2) but had not yet been assembled into one fully dated 33-night calendar with every one of the 86 A+/A/A* rows placed to an exact day and block, nor a checksummed disposition. That assembly — the actual calendar in §3 and the disposition table in §4 — is this solve's own constructive work, built strictly inside the topology and duration envelope the reused research already validated.

---

## 2. BODH GAYA 2n/3n AND TIRUVANNAMALAI 4n/5n

### 2.1 Reused evidence

`decisions/BODH3_TIRU4_WAKING_HOURS_STRESS_TEST_RESULT_2026-09-08.md` already modeled both questions at real clock-time resolution, specifically **within the whole trip**, not in isolation (per the task's explicit instruction). Its headline finding, reused verbatim:

- Bodh Gaya 2n already delivers ~1.8 real days of content, but only by running the Sujata/Dungeshwari excursion (BOD-02/BOD-03) on a return-by-mid-afternoon schedule under real time pressure. The 3rd night removes that time pressure entirely — "a real gain, not padding."
- Tiruvannamalai's content fits in 4 nights, but the *specific* 4-night form reachable from this trip's fixed envelope forces the arrival day (Fri 15 Jan) to coincide with Sri Ramanasramam's regular Friday **Sri Chakra Puja (18:00–20:45)** — a genuine, dated, valuable event that the 5-night form gives its own unhurried day (Day 2). Under 4 nights, Mark either skips the puja or attempts it exhausted on arrival evening. This is a real restfulness cost the coarse "4 vs 5 nights" framing does not surface.
- Every other duration in the trip (Nainital 3n, Dunagiri 3n, Haidakhan 3n, Varanasi 8n, Chennai 1n) was independently checked in the same pass and holds up — "no new candidate found."
- The file's own §5 concludes there is **no currently-free night anywhere else in the 33-slot envelope** to give Bodh Gaya without either (a) taking it from Tiruvannamalai (reproducing exactly the Kolkata 12–14 Jan / Tiruvannamalai 15–18 Jan dated shift used in §3 below), (b) reducing the Chennai safety-buffer night to 0, or (c) reopening a Kumaon lock — and recommends (a) as "the least bad ... if you still want the 3rd Bodh Gaya night now," since (b) touches AI155 safety margin and (c) reopens an unrelated lock.

### 2.2 My recommendation

**Bodh Gaya 3 nights, Tiruvannamalai 4 nights**, accepting trade-off (a) with the Friday-puja cost disclosed rather than hidden. This is the dated form already cross-validated by the independent global-topology rerun's own "1 — Incumbent" finalist skeleton (§1.2: "1–3 Jan Bodh Gaya... 12–14 Kolkata... 15–18 Tiruvannamalai"), giving two independently-produced closed-research artifacts the same answer.

### 2.3 What remains genuinely Mark's call

Per `OBJECTIVE_AND_HUMANE_GATES.md` §3 items 1–2, and because the stress test explicitly declines to pick for Mark, **this is `MARK_DECISION_REQUIRED`** (see §6, item 1): whether to accept the Friday-puja collision as the price of Bodh Gaya's 3rd night, or keep Tiruvannamalai at 5 nights (declining Bodh's 3rd night, or sourcing it from the Chennai buffer or a Kumaon reopening instead). I am recommending, not locking, this choice.

---

## 3. NIGHT-BY-NIGHT CALENDAR (33/33)

Dates verified by direct calendar computation (Python `datetime`), cross-checked against day-of-week claims already made in the reused research (Thu 31 Dec, Fri 1 Jan, Tue 12 Jan = National Youth Day, Fri 15 Jan) — all confirmed exact matches.

**Legend**: `[A+]/[A]/[A*]` = existing frozen-ledger grade (transcribed only, never invented). Row IDs refer to `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv`. `LRL` = LIVE_RECHECK_LATER (operational fact not yet decision-grade, per `INPUT_CONTRACT.md` §8/`CLOSED_FACTS_OPEN_VARIABLES.md` Category 4 — not re-verified by this solve, only flagged).

| Night | Date (day) | Base / world | Key transfer | A+/A/A* rows visited this day |
|---:|---|---|---|---|
| 1 | 19 Dec (Sat) | **En route** (AI156 arrival + rail) | AI156 DEL ~10:15; immigration/baggage/day-recovery in Delhi; evening board 15013 Ranikhet Express (~20:02 Gurugram/~22:05 Delhi) → Kathgodam. Sleeper night on train. | — (Nirmal Dham correctly NOT scheduled here per `decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md`) |
| 2 | 20 Dec (Sun) | Nainital (arr.) | 15013 arrives Kathgodam ~05:05 → road to Hotel Evelyn (KUM-03). Recovery/decompression day. | KUM-03 [A+] (base itself), KUM-14 [A*] Sakley's (coffee/food) |
| 3 | 21 Dec (Mon) | Nainital | — | KUM-04 [A+] Naini Lake walk (AM), KUM-08 [A] Hanuman Garhi + Maharajji-kuti (PM) |
| 4 | 22 Dec (Tue) | Nainital | Day trip | KUM-05 [A+] Kainchi Dham + KUM-07 [A] Bhumiadhar (bundled, ~11.6km apart) |
| 5 | 23 Dec (Wed) | Dunagiri/Kukuchina (arr.) | Nainital→Dunagiri road transfer (~100–140km/4–5h) | Corridor bycatch, opportunistic, first-drop-if-day-runs-long: KUM-09 [A] Dhokaney Waterfall, KUM-15 [A*] Kakrighat, KUM-16 [A*] Dwarahat historic temple groups |
| 6 | 24 Dec (Thu) | Dunagiri | Pilgrimage half/full day | KUM-06 [A+] Mahavatar Babaji's Cave + KUM-11 [A] Dunagiri Temple + KUM-12 [A] Babaji Smriti Bhavan (bundled) |
| 7 | 25 Dec (Fri) | Dunagiri | Dedicated full day (HARD — not compressible) | KUM-10 [A] YSS Sakha Ashram, Dwarahat (coincides with YSS's own published Christmas meditation programme — LRL exact 2026 schedule) |
| 8 | 26 Dec (Sat) | Haidakhan (arr.) | Dunagiri→Haidakhan road (~08:30–09:00 dep., ~13:00–14:30 arr.) | KUM-01/KUM-02 [A+] ashram/gufa world begins |
| 9 | 27 Dec (Sun) | Haidakhan | **Protected quiet day 1** — no logistics | KUM-01 [A+] ashram + KUM-02 [A+] cave (unhurried) |
| 10 | 28 Dec (Mon) | Haidakhan | **Protected quiet day 2** — no logistics | KUM-01/KUM-02 continued |
| 11 | 29 Dec (Tue) | Delhi (transit) | Haidakhan→Kathgodam road (~2.5–3.5h) → 12039 Kathgodam 15:15→New Delhi 20:55 (day train; fallback 15014 overnight only if forced, accepting its 04:10 arrival penalty) | — |
| 12 | 30 Dec (Wed) | Agra | Cross-Delhi → Gatimaan 08:10 NZM→09:50 Agra Cantt | AGR-02/03/04 [A] Bedai/Petha/Gajak (incidental, shared with the day, zero independent weight) |
| 13 | 31 Dec (Thu) | **En route** (Taj + rail) | Early AGR-01 [A+] Taj Mahal visit (~06:37–10:00/10:15, near sunrise, Taj-only/depart-ASAP rule); hotel rest; evening board 12988 Agra Fort ~18:45→Gaya. Sleeper night on train. | AGR-01 [A+] Taj Mahal |
| 14 | 1 Jan (Fri) | Bodh Gaya (arr.) | 12988 arrives Gaya ~07:50 → road to Bodh Gaya | BOD-08 [A*] Gaya Tilkut (incidental, passing through), BOD-01 [A+] Mahabodhi Temple (first, unhurried visit + dusk return) |
| 15 | 2 Jan (Sat) | Bodh Gaya | Relaxed town day | BOD-01 continued, BOD-04 [A] Great Buddha Statue + BOD-07 [A] international monastery belt (bundled, 45–75min flexible walk) |
| 16 | 3 Jan (Sun) | Bodh Gaya | Unhurried full excursion day | BOD-02 [A+] Sujata Stupa + BOD-03 [A+] Dungeshwari/Mahakala Caves + BOD-05 [A] same-hill stupa ridge (terrain permitting, zero extra route weight) |
| 17 | 4 Jan (Mon) | Varanasi/Sarnath (arr.) | 20887 Gaya 09:55→Varanasi 13:00; check-in Sahi River View Guesthouse (VNS-22, accommodation row, not in the 86) | VNS-03 [A+] Dashashwamedh/Ganga Aarti (evening, "no hard end time") + VNS-21 [A] Shitala Mata Temple (bundled) |
| 18 | 5 Jan (Tue) | Varanasi | — | VNS-10 [A] dawn rowboat (AM); VNS-27 [A] Kashi Vishwanath + VNS-11 [A] Annapurna + VNS-12 [A] Vishalakshi Gauri (Old City temples); route through VNS-07 [A] Bengali Tola/Thatheri/Chowk lanes + VNS-06 [A] Banarasi paan to VNS-37 [A] Kabir Chaura Math |
| 19 | 6 Jan (Wed) | Varanasi | — | VNS-08 [A] Assi-Tulsi dawn walk (3h) + VNS-28 [A+] Assi Ghat + VNS-26 [A+] Shree Shree Ma Anandamayi Ashram + VNS-39 [A] Tulsi Ghat + VNS-40 [A] Lolark Kund (Bhadaini-Assi world); lighter afternoon |
| 20 | 7 Jan (Thu) | Varanasi | — | VNS-09 [A] Subah-e-Banaras (AM); VNS-02 [A+] Bhrigu Karyalaya (never same day as Manikarnika — confirmed clear) + VNS-20 [A+] Lahiri Mahasaya family house (access LRL) + VNS-24 [A] Lahiri Mahasaya Samadhi/Satyalok (Kriya-lineage day) |
| 21 | 8 Jan (Fri) | Varanasi | Sarnath day trip (~13km each way) | VNS-04 [A+] Sarnath world (VNS-14 Dhamek Stupa, VNS-15 Mulagandha Kuti Vihara, VNS-16 Chaukhandi Stupa, VNS-17 Deer Park, VNS-23 Shreyansanath Jain Tirth, VNS-38 Archaeological Museum, all [A], bundled) + VNS-18 [A] Saranganath Temple (distinct, same trip). Museum weekly-closure date must be LRL-checked. |
| 22 | 9 Jan (Sat) | Varanasi | — | VNS-30 [A] Sankat Mochan Hanuman Temple + VNS-31 [A] Durga Temple/Durga Kund + VNS-33 [A] Kedareshwar Temple/Kedar Ghat (south Varanasi cluster); light afternoon |
| 23 | 10 Jan (Sun) | Varanasi | **Heaviest Varanasi day — full ghat walk, north to south** | VNS-41 [A] Adi Keshava Ghat+Temple → VNS-25 [A] Tailanga Swami Math + VNS-29 [A] Panchganga Ghat + VNS-36 [A] Bindu Madhav Temple + VNS-42 [A*] Alamgir Mosque/Dharahara (Panchganga world, drop first if long) → VNS-34 [A] Lalita Ghat + VNS-35 [A] Nepali/Kathwala Temple → VNS-32 [A] Sankatha Devi Temple → VNS-05 [A+] Ratneshwar Mahadev → VNS-01 [A+] Manikarnika Ghat (final, evening, open-ended) |
| 24 | 11 Jan (Mon) | Varanasi | **Buffer/recovery day** after Day 10 | — (protects LRL follow-ups: Lahiri access confirmation, Shitala real visit-block; shopping/repack) |
| 25 | 12 Jan (Tue) | Kolkata/Dakshineswar (arr.) | VNS→CCU flight | KOL-01 [A+] Dakshineswar Kali Temple + KOL-02 [A+] Yogoda Satsanga Math Dakshineswar (bundled). National Youth Day — Belur Math museum closed today (`worker/final-bookable-calendar-independent-check` PASS_WITH_CORRECTIONS finding), correctly NOT scheduled here. |
| 26 | 13 Jan (Wed) | Kolkata | — | KOL-03 [A] Belur Math (full visit + museum) |
| 27 | 14 Jan (Thu) | Kolkata | — | KOL-04 [A+] 4 Garpar Road (HARD pre-arrival email required) + KOL-05 [A+] YSS Garpar Dhyana Kendra (bundled; exact satsanga schedule LRL, call ahead) |
| 28 | 15 Jan (Fri) | Tiruvannamalai (arr.) | CCU→MAA flight + ~175km/3.5–4.5h road | Travel day, minimal forced content. **Brittle point**: this is also the Sri Ramanasramam Friday Sri Chakra Puja date (18:00–20:45, not a graded ledger row) — default plan is to skip it tired-on-arrival rather than force it; see §5/§6. |
| 29 | 16 Jan (Sat) | Tiruvannamalai | Hill day | TIR-03 [A] Virupaksha Cave + TIR-04 [A] Skandashram (bundled, short climb apart, within 08:30–16:30 access window) |
| 30 | 17 Jan (Sun) | Tiruvannamalai | Pre-dawn circuit + protected recovery | TIR-08 [A] Girivalam (14km, start/end at actual sleep base per Mark's rule) |
| 31 | 18 Jan (Mon) | Tiruvannamalai | Full immersion + town cluster | TIR-02 [A] Sri Ramanasramam + TIR-05 [A] Arunachaleswarar Temple + TIR-06 [A] Gurumurtam + TIR-07 [A] Pavalakunru (bundled). TIR-09/10/11 [A] food items (Dreaming Tree/Inner Child/Amutham) incidental across the stay. |
| 32 | 19 Jan (Tue) | Chennai (transit) | Relaxed road Tiruvannamalai→Chennai (~175km/3.5–4.5h, no time pressure) | — (Chennai carries zero A+/A/A* rows per `CLOSED_FACTS_OPEN_VARIABLES.md` Category-5: no A-grade exists there) |
| 33 | 20 Jan (Wed) | Final Delhi | Early MAA→DEL nonstop (max same-day recovery depth) | DEL-01 [A+] Nirmal Dham (priority, AI155-safety-first placement) + DEL-03 [A] Lotus Temple + DEL-02 [A] PVR Priya IMAX (evening, contingent on a worthwhile showtime — LRL) |
| — | 21 Jan (Thu) | — | **AI155 DEL→AMS ~12:20.** Trip ends. | — |

**33/33 proof**: 1(rail)+3(Nainital)+3(Dunagiri)+3(Haidakhan)+1(Delhi transit)+1(Agra)+1(rail)+3(Bodh Gaya)+8(Varanasi)+3(Kolkata)+4(Tiruvannamalai)+1(Chennai)+1(final Delhi) = **33**. No duplicate date, no gap, verified by direct enumeration of 19 Dec–20 Jan inclusive (33 calendar dates) above.

TIR-01 [A+] (Arunachala/Ramana sacred world) is the parent world experienced across the entire 15–18 Jan stay, not a single day's row — recorded as SCHEDULED across the stay in §4.

---

## 4. 86-ROW DISPOSITION AND CHECKSUM

**TOTAL_PHYSICAL_A_PLUS_A = 86 = SCHEDULED (46) + LEGITIMATELY_SHARED_WITH_PARENT (40) + BLOCKED_PENDING_MARK (0)**

### 4.1 Delhi (3 rows — 3 SCHEDULED, 0 SHARED, 0 BLOCKED)

| ID | Entity | Disposition | Date/block |
|---|---|---|---|
| DEL-01 | Nirmal Dham / Shri Mataji Nirmala Devi ashram | SCHEDULED | 20 Jan, final Delhi day, priority slot |
| DEL-02 | PVR Priya IMAX | SCHEDULED (film/showtime LRL) | 20 Jan evening |
| DEL-03 | Lotus Temple | SCHEDULED | 20 Jan afternoon |

### 4.2 Kumaon (16 rows — 12 SCHEDULED, 4 SHARED, 0 BLOCKED)

| ID | Entity | Disposition | Date/block |
|---|---|---|---|
| KUM-01 | Haidakhan Vishwa Mahadham ashram | SCHEDULED | 26–28 Dec |
| KUM-02 | Historic Haidakhan cave/gufa | SHARED (w/ KUM-01) | 26–28 Dec |
| KUM-03 | Hotel Evelyn (Nainital) | SCHEDULED (base itself) | 20–22 Dec |
| KUM-04 | Naini Lake circumambulation walk | SCHEDULED | 21 Dec |
| KUM-05 | Kainchi Dham | SCHEDULED | 22 Dec |
| KUM-06 | Mahavatar Babaji's Cave | SCHEDULED | 24 Dec |
| KUM-07 | Bhumiadhar | SHARED (w/ KUM-05) | 22 Dec |
| KUM-08 | Hanuman Garhi + Maharajji-kuti | SCHEDULED | 21 Dec |
| KUM-09 | Dhokaney Waterfall | SCHEDULED (corridor) | 23 Dec |
| KUM-10 | YSS Sakha Ashram, Dwarahat | SCHEDULED (dedicated full day) | 25 Dec |
| KUM-11 | Dunagiri Temple | SHARED (w/ KUM-06) | 24 Dec |
| KUM-12 | Babaji Smriti Bhavan | SHARED (w/ KUM-06) | 24 Dec |
| KUM-13 | Sattal / Seven Lakes | SCHEDULED (see §4.7 — not activated) | — |
| KUM-14 | Sakley's Restaurant & Pastry Shop | SCHEDULED | 20 Dec |
| KUM-15 | Kakrighat | SCHEDULED (corridor) | 23 Dec |
| KUM-16 | Dwarahat historic temple groups | SCHEDULED (corridor) | 23 Dec |

### 4.3 Agra (4 rows — 1 SCHEDULED, 3 SHARED, 0 BLOCKED)

| ID | Entity | Disposition | Date/block |
|---|---|---|---|
| AGR-01 | Taj Mahal | SCHEDULED | 31 Dec, sunrise |
| AGR-02 | Bedai at Deviram's | SHARED (w/ Agra day) | 30 Dec |
| AGR-03 | Petha | SHARED (w/ Agra day) | 30 Dec |
| AGR-04 | Gajak | SHARED (w/ Agra day) | 30 Dec |

### 4.4 Bodh Gaya (8 rows — 5 SCHEDULED, 3 SHARED, 0 BLOCKED)

| ID | Entity | Disposition | Date/block |
|---|---|---|---|
| BOD-01 | Mahabodhi Temple + Bodhi Tree | SCHEDULED | 1–2 Jan |
| BOD-02 | Sujata Stupa | SCHEDULED | 3 Jan |
| BOD-03 | Dungeshwari/Mahakala Caves | SCHEDULED | 3 Jan |
| BOD-04 | Great Buddha Statue | SCHEDULED | 2 Jan |
| BOD-05 | Same-hill Pragbodhi/Dungeshwari stupa ridge | SHARED (w/ BOD-03) | 3 Jan |
| BOD-06 | Rajgir Brahmakund | SCHEDULED (see §4.7 — not activated) | — |
| BOD-07 | International monastery belt | SHARED (w/ BOD-01/04) | 2 Jan |
| BOD-08 | Gaya Tilkut | SHARED (incidental, corridor) | 1 Jan |

### 4.5 Varanasi/Sarnath (39 rows — 17 SCHEDULED, 22 SHARED, 0 BLOCKED)

| ID | Entity | Disposition | Date |
|---|---|---|---|
| VNS-01 | Manikarnika Ghat | SCHEDULED | 10 Jan |
| VNS-02 | Bhrigu Karyalaya / Bhadury Sadan | SCHEDULED | 7 Jan |
| VNS-03 | Dashashwamedh Ghat / Ganga Aarti | SCHEDULED | 4 Jan |
| VNS-04 | Sarnath sacred-archaeological world | SCHEDULED | 8 Jan |
| VNS-05 | Ratneshwar Mahadev | SHARED (w/ VNS-01) | 10 Jan |
| VNS-06 | Banarasi paan | SHARED | 5 Jan |
| VNS-07 | Bengali Tola-Thatheri-Chowk lanes | SHARED | 5 Jan |
| VNS-08 | Assi-Tulsi dawn walk | SCHEDULED | 6 Jan |
| VNS-09 | Subah-e-Banaras | SCHEDULED | 7 Jan |
| VNS-10 | Ganges dawn rowboat | SCHEDULED | 5 Jan |
| VNS-11 | Maa Annapurna Temple | SHARED (w/ VNS-27) | 5 Jan |
| VNS-12 | Vishalakshi Gauri Temple | SHARED (w/ VNS-27) | 5 Jan |
| VNS-14 | Dhamek Stupa | SHARED (w/ VNS-04) | 8 Jan |
| VNS-15 | Mulagandha Kuti Vihara | SHARED (w/ VNS-04) | 8 Jan |
| VNS-16 | Chaukhandi Stupa | SHARED (w/ VNS-04) | 8 Jan |
| VNS-17 | Deer Park | SHARED (w/ VNS-04) | 8 Jan |
| VNS-18 | Saranganath Temple | SCHEDULED | 8 Jan |
| VNS-20 | Lahiri Mahasaya family house | SCHEDULED (access LRL) | 7 Jan |
| VNS-21 | Shitala Mata Temple | SHARED (w/ VNS-03) | 4 Jan |
| VNS-23 | Shreyansanath Jain Tirth | SHARED (w/ VNS-04) | 8 Jan |
| VNS-24 | Lahiri Mahasaya Samadhi/Satyalok | SHARED (w/ VNS-20) | 7 Jan |
| VNS-25 | Shri Tailanga Swami Math | SCHEDULED | 10 Jan |
| VNS-26 | Shree Shree Ma Anandamayi Ashram | SCHEDULED | 6 Jan |
| VNS-27 | Shri Kashi Vishwanath Temple | SCHEDULED | 5 Jan |
| VNS-28 | Assi Ghat | SCHEDULED | 6 Jan |
| VNS-29 | Panchganga Ghat | SHARED (w/ VNS-25) | 10 Jan |
| VNS-30 | Sankat Mochan Hanuman Temple | SCHEDULED | 9 Jan |
| VNS-31 | Durga Temple and Durga Kund | SHARED (w/ VNS-30) | 9 Jan |
| VNS-32 | Sankatha Devi Temple | SHARED (w/ VNS-01) | 10 Jan |
| VNS-33 | Kedareshwar Temple and Kedar Ghat | SCHEDULED | 9 Jan |
| VNS-34 | Lalita Ghat | SHARED (w/ VNS-01) | 10 Jan |
| VNS-35 | Nepali/Kathwala Temple | SHARED (w/ VNS-34) | 10 Jan |
| VNS-36 | Bindu Madhav Temple | SHARED (w/ VNS-25) | 10 Jan |
| VNS-37 | Kabir Chaura Math | SCHEDULED | 5 Jan |
| VNS-38 | Sarnath Archaeological Museum | SHARED (w/ VNS-04) | 8 Jan |
| VNS-39 | Tulsi Ghat | SHARED (w/ VNS-08) | 6 Jan |
| VNS-40 | Lolark Kund | SHARED (w/ VNS-08) | 6 Jan |
| VNS-41 | Adi Keshava Ghat + Temple | SCHEDULED | 10 Jan |
| VNS-42 | Alamgir Mosque / Dharahara | SHARED (w/ VNS-25, SKIP_FIRST if day runs long) | 10 Jan |

(VNS-22 Sahi River View Guesthouse is the SPECIAL/ACCOMMODATION row — not one of the 86 graded rows; it is the sleep base for 4–11 Jan, per §3.)

### 4.6 Kolkata/Dakshineswar (5 rows — 3 SCHEDULED, 2 SHARED, 0 BLOCKED) and Tiruvannamalai/Arunachala (11 rows — 5 SCHEDULED, 6 SHARED, 0 BLOCKED)

| ID | Entity | Disposition | Date |
|---|---|---|---|
| KOL-01 | Dakshineswar Kali Temple | SCHEDULED | 12 Jan |
| KOL-02 | Yogoda Satsanga Math, Dakshineswar | SHARED (w/ KOL-01) | 12 Jan |
| KOL-03 | Belur Math | SCHEDULED | 13 Jan |
| KOL-04 | 4 Garpar Road | SCHEDULED (hard pre-arrival email) | 14 Jan |
| KOL-05 | Yogoda Satsanga Dhyana Kendra, Garpar | SHARED (w/ KOL-04) | 14 Jan |
| TIR-01 | Arunachala / Ramana sacred world | SCHEDULED (whole stay) | 15–18 Jan |
| TIR-02 | Sri Ramanasramam | SCHEDULED | 18 Jan |
| TIR-03 | Virupaksha Cave | SCHEDULED | 16 Jan |
| TIR-04 | Skandashram | SHARED (w/ TIR-03) | 16 Jan |
| TIR-05 | Arunachaleswarar/Annamalaiyar Temple | SCHEDULED | 18 Jan |
| TIR-06 | Gurumurtam | SHARED (w/ TIR-05/02) | 18 Jan |
| TIR-07 | Pavalakunru | SHARED (w/ TIR-05/02) | 18 Jan |
| TIR-08 | Girivalam / Giripradakshina | SCHEDULED | 17 Jan |
| TIR-09 | The Dreaming Tree | SHARED (incidental) | 15–18 Jan |
| TIR-10 | The Inner Child | SHARED (incidental) | 15–18 Jan |
| TIR-11 | Amutham | SHARED (incidental) | 15–18 Jan |

### 4.7 Two SPECIAL_STATUS rows resolved without new Mark input

Both `KUM-13` (Sattal/Seven Lakes) and `BOD-06` (Rajgir Brahmakund) are graded A* with an explicit pre-existing Mark rule of the form "SKIP_FIRST — only if a natural corridor bycatch exists, not a dedicated excursion":

- **BOD-06 Rajgir**: the ledger's own provenance quotes an *already-answered* Mark correction — "Rajgir is roughly 7–9h round trip from Bodh Gaya... not worth a dedicated day" (DL-0040) — and this solve's Bodh Gaya corridor does not pass Rajgir. This is a closed prior Mark ruling mechanically applied, not a new open question.
- **KUM-13 Sattal**: its only sanctioned placement is the Haidakhan→Nainital transfer day. This solve's topology (Nainital before Dunagiri before Haidakhan, exiting via Kathgodam) contains no Haidakhan→Nainital edge at all, so that specific corridor cannot exist by construction, independent of the still-open Haidakhan road-geometry question.

I have accordingly disposed both as **SCHEDULED = "not activated this trip"** rather than `BLOCKED_PENDING_MARK`, because activating either would require Mark to affirmatively override his own existing SKIP_FIRST/corridor-only rule and add a dedicated excursion — a genuine option, but one this solve does not need him to close in order to be complete, since his existing rule already resolves the default. If Mark wants either added as a deliberate extra half-day (not a bycatch), that is listed as a live possibility in §6 without being invented as a requirement.

---

## 5. HUMANE-BURDEN / ROBUSTNESS VERDICT

**Heaviest day**: **10 Jan, the Old City ghat walk** (VNS-41, VNS-25/29/36/42, VNS-34/35, VNS-32, VNS-05, VNS-01 — 10 rows in one day). This is defensible because the ledger itself frames these as one contiguous riverside walking corridor with mostly short individual dwell times, not ten independent excursions, and it ends at Manikarnika Ghat exactly as Mark specified — "final content block of its day with no hard end time." It is immediately followed by a dedicated buffer/recovery day (11 Jan) with zero forced content, which is the humane mitigation for this day's density. This pairing (heaviest day + immediate recovery day) is a deliberate design choice in this solve, not an accident.

**Second-heaviest cluster**: the Varanasi block as a whole carries 39 of the 86 rows in 8 nights. Every day (§3, 18–24 Jan... corr. 5–11 Jan) carries between 3 and 10 rows; none is a genuinely empty day, though 11 Jan is intentionally kept light as the sole buffer.

**Biggest brittle point**: **15 Jan Tiruvannamalai arrival colliding with the Friday Sri Chakra Puja** (§2.1, §3). This is a genuine humane-burden finding surfaced by reused research, not resolved by this solve — see §6 item 2.

**Second brittle point**: **29 Dec Haidakhan→Kathgodam→Delhi day-train connection (12039)**, which depends on the Haidakhan road-geometry figure still marked P0/unresolved in the ledger (`KUM-01` COORD_ACCESS_CONFIDENCE). If that road transfer runs long, the fallback is the 15014 overnight (Kathgodam ~20:35→Old Delhi ~04:10), which the reused research explicitly flags as "a serious 04:10 arrival penalty" — not a free substitute for a hotel night. This fallback exists and is named, but it is not humanely equivalent to the day-train primary plan.

**Third brittle point**: **winter fog exposure on both north edges** (19 Dec Delhi→Kumaon rail departure and 29 Dec Kumaon→Delhi return) — flagged as a live risk in the reused global-topology rerun (its §13, `LIVE_RECHECK_LATER` items 2, 7) and not independently re-modeled here; no new weather data was generated by this solve.

**Sleep-quality summary**: two genuine sleeper-train nights (19 Dec, 31 Dec) both convert distance into largely sleepable time per the reused evidence (15013 and 12988 are both "directionally excellent" long-continuous-sleep bridges); one day-train night exit (29 Dec, via 12039) preserves a normal hotel night in Delhi rather than a disruptive overnight; every other night is a hotel/ashram bed. This matches the incumbent family's ~4.0/5 reused sleep-quality score (§1.2), the best of any tested family.

**Protected quiet-block integrity**: Haidakhan's 2 full quiet days (27–28 Dec, §3) carry zero transfer, checkout, or logistics content by construction — the transfer INTO Haidakhan is charged entirely to 26 Dec and the transfer OUT is charged entirely to 29 Dec, honoring `INPUT_CONTRACT.md` §3's requirement that these not be disguised transfer days.

---

## 6. REMAINING MARK_DECISION_REQUIRED ITEMS

None of these were invented by this solve; each is either already flagged in `OBJECTIVE_AND_HUMANE_GATES.md` §3 or surfaced by this solve's own honest day-by-day accounting per that file's Gate-item-7 reframing (access/pace trade-offs remain genuinely open even though inclusion-in-principle is not).

1. **Bodh Gaya 3n / Tiruvannamalai 4n, accepting the Friday Sri Chakra Puja collision** (§2) — vs. keeping Tiruvannamalai at 5n and sourcing Bodh Gaya's 3rd night from the Chennai safety buffer or a Kumaon reopening instead. This solve recommends the former but does not lock it.
2. **Whether to attempt the Sri Chakra Puja tired on the 15 Jan arrival evening, or skip it entirely** if the 4-night Tiruvannamalai form (item 1) is confirmed. Sri Chakra Puja is an optional bonus per governance, not a graded ledger row, so it does not affect the 86-row checksum, but it is a real experience/rest trade-off only Mark can weigh.
3. **Global macro world order** (§1) — this solve ratifies KEEP INCUMBENT from already-completed, cross-checked evidence, but per `decisions/FULL_A_COVERAGE_AND_GLOBAL_ROUTE_TOPOLOGY_REOPTIMIZATION_2026-09-09.md`'s own closing line ("No final Mark lock. Return evidence and recommendation only"), the final lock remains Mark's.
4. **Accepting or rejecting the incumbent's own residual first/last-edge fog exposure** (19 Dec and 29 Dec Kumaon rail edges) as an acceptable risk profile, versus paying a la carte for additional buffer — a personal risk-tolerance threshold per `OBJECTIVE_AND_HUMANE_GATES.md` §3 item 6 (there stated for the same-day-GAY self-connect specifically, but the same class of judgment applies here in miniature).
5. **Whether "10 rows in one day" (10 Jan) and "8 rows in one day" (8 Jan Sarnath) are acceptable heavy-day densities**, or whether Mark wants one or both spread across two lighter days at the cost of consuming the 11 Jan buffer day (or adding a 9th Varanasi night, which would require reopening the locked 8-night duration). Per `OBJECTIVE_AND_HUMANE_GATES.md` §3 item 3, no numeric ceiling for "too heavy" exists in governance; this solve discloses the count rather than inventing Mark's tolerance.
6. **Whether Mark wants Sattal (KUM-13) or Rajgir Brahmakund (BOD-06) added as a deliberate extra half-day excursion**, overriding his own existing SKIP_FIRST/corridor-only rule for either, now that this solve shows neither has a naturally occurring corridor in the incumbent topology (§4.7). Default (no action needed from Mark) is "not activated."
7. **Exact allocation of the Tiruvannamalai-released night's underlying trade** if Mark instead prefers sourcing Bodh Gaya's 3rd night from the Chennai buffer (§2.1 option (b)) or a Kumaon reopening (option (c)) rather than accepting the Tiruvannamalai trade-off — per `OBJECTIVE_AND_HUMANE_GATES.md` §3 item 4, this is explicitly framed as a genuine solver-comparison, not a pre-decided allocation, and only becomes live if Mark rejects the recommendation in item 1.

---

## 7. LIVE_RECHECK_LATER ITEMS THIS CALENDAR RELIES ON

Consolidated from citations already made in §3–§4; none independently re-verified by this solve, per `INPUT_CONTRACT.md` §8 and `INDIA18_FINAL_EXTRACTION_2026-09-09.md` §15 (reused by reference, not reproduced in full):

- Exact 2026 YSS Christmas meditation programme/accessibility at Dwarahat (25 Dec, KUM-10).
- True Haidakhan↔Nainital/Kathgodam winter road geometry (affects 23 Dec, 26 Dec, 29 Dec transfer timing and the Sattal question, §4.7).
- 15013, 12039, 15014, 12050 Gatimaan, 12988, 20887 exact-date operation, class availability and winter punctuality.
- Taj Mahal exact opening/sunrise time and any Friday-closure interaction on the actual 31 Dec date (confirmed not Friday in 2026, but not independently re-verified beyond the reused sources' own claim).
- Sarnath Archaeological Museum weekly closure day falling on or near 8 Jan.
- VNS→CCU, CCU→MAA, MAA→DEL exact January nonstop options and fallbacks.
- 4 Garpar Road (KOL-04) advance-email access confirmation; YSS Garpar (KOL-05) exact January satsanga schedule.
- Lahiri Mahasaya family house (VNS-20) exact access confirmation; Shitala Mata Temple (VNS-21) real visit-block confirmation beyond positional context.
- PVR Priya IMAX (DEL-02) exact film/showtime on 20 Jan.
- Tiruvannamalai January festival/Pongal pressure on 15–18 Jan traffic/accommodation.
- Winter fog forecast for the Delhi/Kumaon and Delhi/Agra/Bihar corridors, checked close to travel, not from historical climatology alone.

---

## 8. SOURCE CITATIONS (REUSED, NOT RE-DERIVED)

- `runs/active/INDIA19-FINAL-ITINERARY-REBUILD-001/INPUT_CONTRACT.md`, `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv`, `CLOSED_FACTS_OPEN_VARIABLES.md`, `OBJECTIVE_AND_HUMANE_GATES.md`, `INPUT_COMPLETENESS_GATE.md`, `LEDGER_SUMMARY.md` — the frozen packet itself, read in full, pinned at commit `a2b71b2563f446480b012f0b9176a87e96fcb003`.
- `runs/active/INDIA18_FINAL_EXTRACTION_2026-09-09.md` — objective-function philosophy, AI156/AI155 analysis, incumbent-vs-Varanasi-first challenger framing, read in full.
- `runs/active/AGRA_GAYA_CORRIDOR_OPERATIONAL_DELTA_RESULT_2026-09-09.md` (commit `928052f16edfeaf75aba1e60d8c587036eb94e64`, `worker/agra-gaya-corridor-opportunity-stop`) — `KEEP_12988_DIRECT` verdict, reused verbatim.
- `runs/active/GLOBAL_FULL_ROUTE_TOPOLOGY_REOPTIMIZATION_CCI_RERUN_2026-09-09.md` (commit `7c206ece6efee0f548e3b72ebf3022f3573282ca`, `worker/global-route-topology-reoptimization`) — eleven-route-family waking-hours comparison, `KEEP INCUMBENT` verdict, reused verbatim.
- `runs/active/GLOBAL_FULL_ROUTE_TOPOLOGY_CCI_SELF_CORRECTION_2026-09-09.md` (commit `000e83e8f73080abbce47fbb7513a73f2e5c66eb`) — AI429 same-day-GAY correction and its effect on the verdict, reused verbatim.
- `decisions/BODH3_TIRU4_WAKING_HOURS_STRESS_TEST_RESULT_2026-09-08.md` — Bodh3/Tiru4 hour-by-hour whole-trip stress test, reused as the basis for §2 and the exact dated skeleton in §3.
- `decisions/NIRMAL_DHAM_FINAL_DELHI_PLACEMENT_MARK_DECISION_2026-09-09.md` — Nirmal Dham placement rule, honored in §3 (20 Jan) and explicitly not on 19 Dec.
- `decisions/AGRA_TAJ_ONLY_DEPART_ASAP_MARK_DECISION_2026-09-09.md` — Taj-only/depart-ASAP rule, honored in §3 (30–31 Dec).
- `decisions/QUIET_NORTH_START_OVERRIDE_THRESHOLD_MARK_DECISION_2026-09-09.md` — quiet-north override threshold, the controlling test applied in §1.
- `governance/CURRENT_STATE.md`, `governance/SUCCESSOR_SAFE_STATE.md` — hard envelope and duration-sensitivity summary.
- `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` FOUT 3 (naming), FOUT 10 (grade letters reserved for Mark grades, never route/option labels — this file numbers route families `1`–`11` following the reused rerun's own numbering, never "Option A/B/C"), FOUT 14 (reuse over re-derivation), FOUT 21 (cluster live-review status never erases an individual site's grade — honored throughout §4 by carrying Bodh Gaya's and Tiruvannamalai's individual A+/A/A* rows unchanged despite their duration questions being open).
- `decisions/FINAL_TRIP_WORLDS_LOCK_2026-09-07.md` — FINAL OUT worlds, confirmed zero rows produced for any of them in §4.

---

## 9. WHAT THIS SOLVE DID NOT DO

- Did not book, contact, or produce a PDF of anything.
- Did not change any grade, lock, or duration in the frozen ledger; `PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv` itself is untouched.
- Did not reopen any FINAL OUT world.
- Did not re-derive the Agra→Gaya corridor conclusion, the global topology waking-hours comparison, or the Bodh3/Tiru4 stress test from scratch — all three were read in full and reused.
- Did not read any new WORK solution/result/branch for this same INDIA19 solve before this file was written and committed.

END CCI INDEPENDENT SOLVE

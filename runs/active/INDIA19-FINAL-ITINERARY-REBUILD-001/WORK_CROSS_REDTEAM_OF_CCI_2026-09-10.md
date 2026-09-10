# WORK — TARGETED CROSS-RED-TEAM OF CCI SOLVE

Date: 2026-09-10  
Role: WORK, targeted cross-red-team reviewer  
Status: **COMPLETE — DEFECTS_FOUND**  
Frozen packet: `a2b71b2563f446480b012f0b9176a87e96fcb003`  
CCI solve reviewed: `b52ea7157803e8b2061191061e65804e6b44e0c1`  
WORK solve preserved unchanged: `594b430f235ebf49dcfa3f4a142717961480c0c1`  
Worker branch: `worker/india19-work-cross-redteam-of-cci`

## 0. Scope and method

This is not a new route solve. I reviewed only the four differences named in PR #23 task `WORK_TASK — INDIA19 TARGETED CROSS-RED-TEAM OF CCI SOLVE — NO NEW GLOBAL SOLVE`:

1. Bodh Gaya 3 nights / Tiruvannamalai 4 nights versus Bodh Gaya 2 / Tiruvannamalai 5;
2. CCI's exact dated calendar against the frozen hard, closure, transfer and humane gates;
3. CCI's `46 scheduled + 40 shared + 0 blocked` disposition against the frozen 86-row ledger and WORK's `68 + 16 + 2` classification;
4. the shared macro-topology.

No broad route research or new candidate family was run. No Mark grade, lock, duration, FINAL OUT decision or frozen solve was changed. No booking, contact or PDF work was performed. Future operating inventory remains `LIVE_RECHECK_LATER`.

## 1. Verdict

`DEFECTS_FOUND`

CCI's **macro route and 33-night arithmetic survive**, but the frozen CCI calendar is not a clean pass as written:

- one definite Tier-3/4 closure defect leaves the A-graded Sarnath Archaeological Museum without a usable visit block;
- one arrival-day Kolkata placement is not yet proved door-to-door and makes CCI's coverage claim conditional on a live flight-time check;
- two inactive SPECIAL_STATUS rows are incorrectly counted as `SCHEDULED`, which is not merely harmless arithmetic terminology even though no physical row is lost;
- CCI does not output all frozen humane-burden metrics, so its Tier-5-to-7 audit is incomplete.

These defects do **not** falsify Kumaon-first, the 12039 daytime north exit, the Agra/Gaya bridge or the downstream macro-chain. They require a within-block calendar correction and accurate disposition/audit reporting, not a new global solve.

## 2. Exact defects

### D1 — hard date/closure defect: Sarnath Museum on Friday 8 January

CCI places the complete Sarnath block, including `VNS-38` Sarnath Archaeological Museum [A], on **Friday 8 January 2027** and leaves the weekly closure as `LIVE_RECHECK_LATER`.

That is already contradicted by multiple frozen/reusable sources at the packet commit:

- `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/INDIA9_CALENDAR_CLOSURE_RECONCILIATION_2026-08-23.md` says explicitly: museum closed Friday and **DO NOT schedule immutable VNS 032 on Fri 8 Jan 2027**;
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_8_NIGHT_CLOCK_REVIEW_MARK_INPUT_2026-08-27.md` says 09:00–17:00, closed Friday;
- `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/VARANASI_BASELINE_EXECUTION_DRAFT_2026-08-27.md` and `VARANASI_EXPLAINED_HOURLY_8_NIGHT_DRAFT_2026-08-27.md` repeat the same closure;
- `decisions/FINAL_BOOKING_CALENDAR_LOCKED_2026-09-08.md` already reserves Friday 8 January as **not Sarnath Museum**.

This is not a merely stale future timetable. Under frozen Objective Tier 3, `VNS-38` needs a real time-block home; under Tier 4, a known weekly closure must be respected. CCI's calendar therefore fails as written.

The defect is locally repairable without changing nights or macro-order. The smallest apparent reflow is to exchange CCI's Friday 8 January south-Varanasi programme with its Saturday 9 January Sarnath programme, leaving Sunday 10 January's final Manikarnika walk and Monday 11 January's recovery buffer intact. Exact living-site hours remain `LIVE_RECHECK_LATER`. This repair is stated only to prove the defect is local; neither frozen solve is edited here.

### D2 — conditional Tier-4 transfer gap: Kolkata A+ content on the VNS-to-CCU arrival day

CCI moves Varanasi/Sarnath one day later under Bodh3 and therefore flies VNS–CCU on **Tuesday 12 January**, then assigns both `KOL-01` Dakshineswar Kali Temple [A+] and `KOL-02` Yogoda Satsanga Math, Dakshineswar [A+] to that same arrival day.

The frozen evidence establishes a structurally daily VNS–CCU nonstop of roughly 1h15–1h25, but explicitly leaves the selected-date time and door-to-door geometry to `LIVE_RECHECK_LATER`. CCI provides no flight time, airport-process band, CCU-to-Dakshineswar transfer, luggage/check-in block or verified remaining access window. The earlier stress-test skeleton instead treated the Kolkata arrival day as light content only.

This is **not proven impossible**, so it is not a second hard calendar invalidation. It is, however, a calendar-critical dependency that must be resolved before `KOL-01` and `KOL-02` can be counted as safely scheduled. If no sufficiently early flight exists, CCI must reflow the three Kolkata days; it cannot retain an unconditional 86/86 coverage claim merely by writing both A+ rows on the arrival date.

### D3 — incomplete humane-burden output

The frozen objective file requires each candidate to report, among other metrics, actual-bed versus sleeper nights, transfer buffers, consecutive heavy days, base changes, flights, sub-05:30 wakes, post-22:00 arrivals, total intercity waking hours split by mode, fragile-edge count and fallbacks.

CCI does disclose its heaviest Varanasi day, the Friday-puja collision, the 29 December mountain/rail risk, fog exposure, two sleeper nights and the protected Haidakhan days. It does **not** close the complete required metric set or recompute the calendar-wide burden. In particular it gives no total waking-hour split, no explicit base-change/flight/early-wake/late-arrival/fragile-edge totals and no consecutive-heavy-day count.

This is an audit-completeness defect rather than proof that the itinerary itself is inhumane. It matters because the unresolved 12 January arrival block and the 15–18 January Tiru compression live precisely in Tiers 4–7.

## 3. Bodh3/Tiru4 versus Bodh2/Tiru5 by objective tier

### Tiers 1–2 — hard envelope and international-flight safety

Tie. Both cells can occupy exactly 33 nights, preserve every locked duration, keep the 19 January Chennai airport-positioning night and the 20 January final Delhi night, and protect AI155. Neither requires reopening FINAL OUT worlds or a locked Kumaon/Varanasi duration.

CCI's 33-date table is mechanically sound: 33 unique consecutive night slots from 19 December through 20 January. The Friday Sarnath error is a content-date defect inside that envelope, not a night-count defect.

### Tiers 3–4 — physical coverage and executable time blocks

After repairing the Sarnath date and proving the 12 January Kolkata arrival window, neither duration cell inherently dominates.

- Bodh2 still gives about 1.8 usable days and can physically schedule Mahabodhi, Great Buddha/monastery belt and the Sujata–Dungeshwari excursion.
- Bodh3 gives the Sujata–Dungeshwari excursion and Mahabodhi practice a genuinely unhurried extra day.
- Tiru4 can name all graded rows, but its final Monday must carry Sri Ramanasramam, Arunachaleswarar Temple, Gurumurtam, Pavalakunru and packing.
- Tiru5 gives Sri Ramanasramam a standalone immersion day and separates caves, Girivalam/recovery and the town/temple group.

CCI's closure defect makes its exact frozen form inferior as written, but does not establish that the Bodh3/Tiru4 **duration cell** is intrinsically invalid.

### Tier 5 — humane sleep, recovery and protected depth

No objective dominance.

- **Bodh3/Tiru4 wins in Bodh Gaya:** the separate A+ Sujata Stupa and A+ Dungeshwari/Mahakala Caves excursion stops being schedule-anxious; Mahabodhi receives more contemplative depth.
- **Bodh2/Tiru5 wins in Tiruvannamalai:** it preserves an unshared Sri Ramanasramam immersion day, a clean hill-cave day, a clean Girivalam-plus-recovery day and a separate town/temple day.

The Friday 15 January Sri Chakra Puja is an optional bonus, not a graded obligation and explicitly not a Tiru5 veto. Under Tiru4 CCI may legitimately skip it rather than force a tired arrival-night attendance. The collision is a real experience/recovery cost, but cannot decide the duration mechanically.

### Tiers 6–7 — waking burden, base changes and robustness

The cells use the same worlds, base count, flight count and Chennai/final-Delhi safety structure. Moving one night changes where the pressure falls rather than eliminating a transfer. Tiru4 has the more brittle arrival/final-day content stack; Bodh2 has the more time-sensitive excursion. The frozen evidence does not quantify a material whole-trip transport advantage for either.

### Tier 8 — experience/date quality

Again non-dominating. Mark's recorded statement, “Ik vind Bodh Gaya te kort en Tiruvannamalai te lang,” is a real personal signal toward Bodh3/Tiru4. The standalone Sri Ramanasramam day and less compressed Tiru structure are real signals toward Bodh2/Tiru5. The optional puja may inform the choice but cannot override the explicit rule that it is not mandatory.

### Duration verdict

`GENUINE_MARK_DECISION_REQUIRED = YES`

After the local CCI calendar defects are repaired, the objective hierarchy does not eliminate either cell. The evidence presents a genuine depth-allocation choice, not an objective solver winner. CCI may recommend Bodh3/Tiru4 and WORK may recommend Bodh2/Tiru5, but neither recommendation is a new lock.

## 4. 86/86 disposition audit

### Mechanical population check

I extracted CCI's §4 disposition rows and compared their IDs to the frozen CSV:

- CCI table rows: **86**;
- unique CCI IDs: **86**;
- frozen graded ledger IDs: **86**;
- missing IDs: **0**;
- extra IDs: **0**;
- duplicates: **0**.

The cluster counts also match exactly: Delhi 3, Kumaon 16, Agra 4, Bodh Gaya 8, Varanasi/Sarnath 39, Kolkata 5 and Tiruvannamalai 11. The ungraded accommodation row `VNS-22` is correctly outside the 86.

### Forty shared rows

The `46 scheduled + 40 shared` split is mostly a different granularity choice from WORK's `68 + 16`. Every shared row remains individually named and assigned to a dated, recognizable physical block. The frozen ledger permits or contemplates the stated parent/microcluster sharing; CCI does not erase any of those 40 rows merely by using the shared bucket.

Accordingly, this part of the difference is **classification semantics, not lost content**. A later presentation must still display every physical name individually.

### Sattal and Rajgir Brahmakund

The substantive execution outcome is the same in both solves:

- `KUM-13` Sattal / Seven Lakes [A*/SKIP_FIRST] is not activated because the itinerary contains no sanctioned Haidakhan-to-Nainital transfer corridor;
- `BOD-06` Rajgir Brahmakund [A*/ONLY_IF_NATURAL_CORRIDOR_BYCATCH] is not activated because the route does not pass Rajgir and Mark already rejected a dedicated 7–9-hour excursion.

Applying those frozen rules requires no fresh Mark decision: **not activated by default is legitimate**. Mark is needed only if he wants to override the rule and create a dedicated detour.

CCI nevertheless labels both rows `SCHEDULED (not activated)` and gives each no date. That contradicts the packet's own Tier-3 meaning of scheduled: a scheduled row has a real recognizable time-block home. These two do not.

Therefore the difference is:

- **semantic as to physical content loss:** neither solve hides or silently drops either row;
- **substantive as to checksum/disposition semantics:** CCI cannot count an undated, deliberately unvisited row as `SCHEDULED` or “satisfied.”

The most accurate state is a separate `CONDITION_NOT_TRIGGERED / NOT_ACTIVATED_UNDER_EXISTING_MARK_RULE` bucket. If the frozen three-bucket checksum must be used unchanged, they must remain explicitly conditional/blocked rather than scheduled, with the note that no Mark action is required to keep the default skip. WORK's `BLOCKED_PENDING_MARK` label is conservative but also imperfect: the pending Mark action is an **override to activate**, not permission to omit.

With that status correction the inventory still accounts for all 86 rows; it does not create an 84-row population.

## 5. Shared macro convergence

Confirmed. I found no remaining macro disagreement or defect in the common chain:

`Kumaon-first -> 12039 daytime north exit -> Delhi transit bed -> Agra/Taj -> 12988 sleeper -> Bodh Gaya -> Varanasi/Sarnath -> Kolkata/Dakshineswar -> Tiruvannamalai -> Chennai airport bed -> final Delhi -> AI155`

Specific confirmations:

- the quiet-north preference remains controlling because no challenger clears the frozen 8–10+ waking-hour threshold;
- 12039 plus a normal Delhi hotel night is more robust than making the 04:10-class 15014 arrival the default; 15014 remains a fallback;
- both solves preserve the protected Taj block and direct 12988 eastbound sleeper;
- both preserve two complete Haidakhan quiet days, the Chennai airport-positioning night and the final Delhi/AI155 safety hierarchy;
- the remaining difference is the one-night Bodh/Tiru allocation and its shifted downstream dates, not macro topology.

## 6. Required reconciliation actions

1. Do not adopt CCI's Friday 8 January Sarnath block. Move the complete Sarnath world, including `VNS-38`, to a non-Friday date and re-audit the surrounding Varanasi day density.
2. Before treating CCI's Kolkata coverage as executable, verify that the 12 January VNS–CCU selection leaves a real door-to-door Dakshineswar/YSS access window; otherwise reflow the Kolkata days.
3. Reclassify `KUM-13` and `BOD-06` as explicitly conditional/not activated under their existing Mark rules, never as scheduled/satisfied.
4. Preserve Bodh3/Tiru4 versus Bodh2/Tiru5 as `MARK_DECISION_REQUIRED`; present the exact displacement in both directions without turning either solver's recommendation into canon.
5. Supply the missing humane-burden totals before the reconciled route receives a final fit verdict.
6. Treat Mark's new reconciliation instruction as binding for the next phase: the final clock-time plan must show **every A+ and A physical location individually**, with its own recognizable visit window and its real incremental burden (access, walking/road time, dwell, queues/closure risk and recovery effect). Parent/microcluster sharing may prevent double-counting one transfer, but may not hide a physical location inside a generic parent label or replace its own time/burden line. Nothing may be pre-cut, silently omitted or reduced to B to make the calendar fit. Any A* row remains individually visible under its existing frozen conditional/SKIP_FIRST rule; this audit creates no new grade.

### Mark requirement for the next clock-time reconciliation

The present `86/86` presence check proves inventory visibility only; it is **not yet the final execution proof**. The reconciled clock plan must therefore add a lossless per-location matrix containing at least:

- stable ID and full recognition-rich physical name;
- unchanged Mark grade;
- exact date and start/end visit window;
- access/egress and on-site dwell separated;
- incremental waking burden and interaction with the rest of that day;
- opening/access dependency and fallback;
- explicit parent/shared-block reference where applicable, while retaining the child row itself.

For A+ and A, a vague cluster/day label or an undated `SCHEDULED` status is insufficient. If a physical A+ or A cannot receive a real feasible window, reconciliation must expose the conflict to Mark; it may not solve the conflict through deletion or regrading.

## 7. Final answer to the dispatched checklist

`VERDICT = DEFECTS_FOUND`  
`BODH_TIRU_OBJECTIVE_WINNER = NONE`  
`BODH_TIRU_MARK_DECISION_REQUIRED = YES`  
`CCI_33_NIGHT_ARITHMETIC = PASS`  
`CCI_SARNATH_FRIDAY_PLACEMENT = FAIL`  
`CCI_KOLKATA_ARRIVAL_BLOCK = CONDITIONAL_LIVE_RECHECK`  
`CCI_86_UNIQUE_ROWS_PRESENT = PASS`  
`CCI_40_SHARED_CONTENT_LOSS = NO`  
`SATTAL_RAJGIR_DEFAULT_NONACTIVATION = LEGITIMATE`  
`SATTAL_RAJGIR_COUNTED_AS_SCHEDULED = FAIL`  
`SHARED_MACRO_TOPOLOGY = CONFIRMED`  
`FINAL_CLOCK_PLAN_ALL_A_PLUS_A_INDIVIDUAL_TIME_AND_BURDEN = REQUIRED`  
`PRE_CUT_OR_DOWNGRADE_TO_B = FORBIDDEN`  
`NEW_GLOBAL_SOLVE_PERFORMED = NO`

END WORK TARGETED CROSS-RED-TEAM

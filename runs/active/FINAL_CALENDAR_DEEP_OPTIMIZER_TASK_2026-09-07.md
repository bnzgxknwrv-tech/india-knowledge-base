# WORK_TASK — FINAL CALENDAR DEEP OPTIMIZER — INDEPENDENT CHATGPT

Repository: `bnzgxknwrv-tech/india-knowledge-base`
Branch only: `worker/final-calendar-deep-optimizer`
Central truth: `agent/india8-cluster-casting`

## Goal
Independently derive the best exact 33-slot India day calendar for Mark for 19 Dec 2026 through 20 Jan 2027, ready for later booking once audited. Do not book, email, call, reserve, or pay anything.

This is not broad destination discovery. Trip worlds are already chosen. Your job is calendar optimization using current canon plus fresh web research for operational facts that materially affect dates.

## Mandatory reading before research
Read current central truth and all relevant final-calendar / route / decision files, especially:
- `decisions/FINAL_TRIP_WORLDS_LOCK_2026-09-07.md`
- `decisions/FINAL_DELHI_ONE_NIGHT_MARK_DECISION_2026-09-07.md`
- `decisions/NORTH_EXTRA_NIGHT_PREFERENCE_2026-09-07.md`
- latest Kolkata/Dakshineswar Mark decisions and grades
- latest final exact 33-slot candidate and route/calendar worker outputs
- execution-readiness/live-recheck material
- current locked-duration decisions for Haidakhan, Varanasi, Tiruvannamalai and all other fixed worlds

Read PR #23 only if needed to reconcile the newest CCI results. Do not trust summaries over current canon when they conflict.

## New Mark preference that must influence optimization
If a genuinely movable/free night exists after all hard locks, safety constraints and content requirements are met, Mark prefers spending it in NORTH / KUMAON / mountain worlds rather than in additional city time.

This is a tie-break preference, not permission to weaken safety or overwrite locks.

Current final Kolkata grades include:
- Balaram Mandir [B] — optional if time/bundle permits
- Mayer Bari/Udbodhan [B] — optional if time/bundle permits
- Vivekananda Ancestral House [B] — optional if time/bundle permits
- Kamarpukur + Jayrambati [C] — too far; suppress unless Mark explicitly reopens

## Hard constraints
Do not change Mark grades. Do not shorten locked durations. Do not reopen Puri, Serampore or Vrindavan/Braj. Preserve international flights and final Delhi one-night lock. Preserve 33 India overnight slots exactly. Ensure all A+/required content remains realistically visitable.

Current macro-order is an incumbent, not an untouchable axiom. You MAY test another cluster order only if it clearly and demonstrably beats the incumbent on the lexicographic objective below. Do not generate speculative alternatives for variety.

## Lexicographic objective function
Optimize in this order; a lower tier may never defeat a higher tier:
1. HARD FEASIBILITY: 33/33 nights, international flights, locked durations, FINAL OUT, required A+/A content, closures/access.
2. SAFETY / FAILURE TOLERANCE: AI155 protection, missed-connection recovery, winter fog/mist, mountain-road burden, rail/flight fragility, no brittle same-day chains when avoidable.
3. DATE QUALITY: weekdays, weekly closures, festivals/crowds, Jan 1 / Gangasagar / Makar Sankranti / Pongal and other material date effects.
4. TRANSPORT QUALITY: real direct rail/flight availability, frequency/redundancy, arrival quality, transfer burden, backtracking.
5. PROTECTED EXPERIENCE: full usable days at the highest-value worlds; avoid consuming key days as transit where an objectively better shift exists.
6. WHOLE-HUMAN BURDEN: recovery, sleep, jet lag, transfer intensity, repeated early starts.
7. MARK PREFERENCE TIE-BREAK: if a discretionary night remains, prefer NORTH/KUMAON/mountains over extra city time.
8. COST / convenience only after the above.

## Required deep research
Use current official/primary sources where possible and current airline/rail data where appropriate. Recheck facts that can materially change exact dates, including:
- actual weekday/calendar arithmetic for every date
- Taj Friday closure
- relevant Sarnath/Belur/museum closures
- winter fog and rail/flight vulnerability
- candidate trains Agra→Gaya and Kumaon↔Delhi
- current realistic Varanasi→Kolkata, Kolkata→Chennai and Chennai→Delhi flight patterns/frequency
- Gangasagar/Makar Sankranti crowd effect
- Pongal / Tiruvannamalai date burden
- whether moving a discretionary night to Kumaon is operationally possible without losing a stronger safety buffer
- whether Bodh Gaya 3n + Kolkata 3n deserves to survive versus Bodh 2n + Kolkata 3n
- whether Kolkata 2n can realistically accommodate all retained A+/required content, especially the Dakshineswar core plus 4 Garpar Road [A+] and YSS Garpar Dhyana Kendra [A+]

## Build no more than three serious final scenarios
Do not produce a large matrix for Mark. Produce up to three genuinely distinct candidates, preferably along these concepts if they survive objective testing:
- `SAFE` — maximum realistic failure tolerance / buffer
- `BALANCED` — best overall experience + safety
- `NORTH-HEAVY` — reallocates any truly discretionary capacity toward Kumaon/mountains, but only if still operationally defensible

If two scenario labels collapse to the same exact dates, merge them. If a scenario fails a hard or high-tier objective, eliminate it rather than presenting it.

For each surviving scenario provide:
- exact 33 overnight slots with dates
- exact sleep base / night train
- transfer on each move day
- protected full days
- closure/festival interaction
- fragile points and fallback
- what changes versus the current CCI baseline
- what Mark gains and what he gives up
- a short score against objective tiers 1–8

## Critical question
Determine whether Mark has any subjective decision left after current grades + north preference. If not, say `MARK_DECISION_GATE: NONE` and recommend the objectively strongest calendar. If there remains a genuine value trade-off that cannot be resolved from Mark's stated preferences, show at most three human-readable options and state the exact question Mark must answer.

## Multi-AI handoff
At the end, create a compact `FROZEN_AUDIT_PACKET` section containing all facts needed for 5 external AI auditors with no GitHub access: hard locks, exact candidate calendar(s), objective function, known uncertainties, and what they may/not change. It must be self-contained and pasteable.

## Output
Write:
`runs/active/FINAL_CALENDAR_DEEP_OPTIMIZER_RESULT_2026-09-07.md`

Commit all work on this branch.

Report in chat:
`COMPLETE/BLOCKED + commit + recommended scenario + MARK_DECISION_GATE + top corrections versus incumbent`.

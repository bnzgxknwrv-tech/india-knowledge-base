# MARK TRAVEL PREFERENCES — CURRENT CANON

Status: HARD CURRENT PREFERENCE INDEX
Updated: 2026-08-26
Branch: agent/india8-cluster-casting
Purpose: keep durable, cross-session Mark travel preferences in one short current file so future INDIA versions do not need to rediscover them from old handoffs.

## PRECEDENCE
1. Newest explicit Mark decision always wins.
2. `CURRENT_STATE.md` + current Mark decision logs control site/cluster/hotel status.
3. THIS file controls durable cross-cluster travel preferences unless a newer explicit Mark instruction supersedes one.
4. Old handoffs/ACTIVE_STATE/legacy route files are provenance only. They may contain useful preferences, but old route sequences, grades, sleep modules or calendars must never be reactivated without current reconciliation.

This file is intentionally NOT a duplicate A/B/C canon. It stores preferences that affect many clusters or the final journey.

## FIXED TRIP ENVELOPE
- Definitive travel period in repo: **18 December 2026 through 21 January 2027**; flights are booked.
- Project accounting convention: **34-day trip budget**.
- Exact old day-by-day calendars are non-authoritative until rebuilt through the active trip-planning meta-controller and current transfer accounting.
- Do not expose/store private booking-account details merely to prove the dates.

Provenance: commit `12148a8e74d3289a4853f24c0809f106bac41f78` recorded the dates as definitive and flights booked.

## PACE / EXPERIENCE
- **Breathing room at major spiritual clusters is preferred over maximizing the number of sites.**
- INDIA may calculate logistics and propose combinations; only Mark determines subjective dwell/pace.
- Do not compress a spiritual stay merely because a denser schedule is mathematically possible.
- Existing cluster-specific pace wishes/working hypotheses in CURRENT_STATE or current decision artifacts override generic optimization. Example: Haidakhan currently carries the recovered 3-night / 2-complete-day working hypothesis until Mark closes it.

## TRANSPORT — HARD PREFERENCE
Long-distance preference hierarchy is conditional on true door-to-door usefulness:
1. **TRAIN FIRST** when practical, especially when an overnight train converts transfer time into sleep or preserves useful daylight.
2. **FLIGHT SECOND** when train travel destroys substantially more usable trip time after all airport overhead is counted.
3. **PRIVATE CAR** for mountains, last mile, short/medium transfers, or when rail/air geometry is worse door-to-door.
4. **INTERCITY/LONG-DISTANCE BUS = EXCLUDED / AVOID.** Do not use it as normal fallback.

For overnight rail:
- target **1A / First AC** where available;
- 2A is fallback only after Mark accepts it;
- do not design overnight-train logic around non-AC sleeper class.

Door-to-door comparison always includes access, reporting/check-in, waiting, connections, baggage, onward transport, food/rest, daylight/energy loss and whether an overnight train replaces a hotel night.

Canonical source: `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/TRANSPORT_PREFERENCE_AND_EFFICIENCY_RULE_2026-08-23.md`.

## TIME ACCOUNTING
- Travel days are real trip days.
- Raw vehicle time is not calendar occupancy.
- Known inbound transfer to a fixed cluster must be included in that cluster's footprint under the current edge-accounting rule.
- Never omit or double-count an outbound bridge.

## FINAL COMFORT SWEEP — MUST NOT BE FORGOTTEN
After retained clusters, route, nights/bases and day structure are stable, run a compact comfort sweep for every retained sleep base/corridor.

Mark especially values:
- old/historic pastry shops and bakeries;
- local signature sweets;
- characterful pastry/cafe stops;
- genuinely good coffee;
- restaurants strong enough to choose deliberately rather than by convenience;
- practical quality food/comfort stops on long transfer days.

Do not produce generic restaurant lists. Prefer a small, well-supported shortlist and state what to order/try, location relative to base/route, opening/reservation risk and why it is special.

Canonical source: `governance/FINAL_COMFORT_SWEEP_RULE_2026-08-23.md`.

## USER-FACING PRESENTATION
- Indian names must repeatedly include a short plain-Dutch recognition explanation; never expect Mark to remember a name alone.
- Every real Mark choice batch is one contiguous numbered block so he can reply `1 A, 2 B, 3 C`.
- Use `kosten` only for money; use reistijd/extra reistijd/omweg/duur for time/logistics.
- C items are absent from active trip presentation unless explicitly reopened.
- B stays visible as conditional reserve; A* is SKIP_FIRST.

Canonical semantic source: `governance/ABC_SEMANTIC_LABEL_RULE_2026-08-23.md` plus current grade model/decision log.

## OUTPUT / ARTIFACT PREFERENCE
- No PDF unless Mark explicitly asks for one.
- Preserve useful research in GitHub; do not make the final travel project primarily a governance exercise.

## LIGHT HISTORICAL PREFERENCE CHECK BEFORE `DURATION_CLOSED` — HARD
Do NOT wait only for Mark to notice that an old preference is missing.

Before any fixed-core cluster is marked `DURATION_CLOSED`, INDIA performs one bounded historical check for that specific cluster. This is NOT a full repo audit.

Search only relevant terms such as:
- cluster/place name;
- chosen/previous sleep-base names;
- key person/ashram/hotel names;
- `night`, `nights`, `nachten`, `dagen`, `full day`, `rust`, `stay`, `sleep`, `hotel`, `ashram`, `train`, `flight`, `car`, `bus`, `LOCKED_BY_MARK` where relevant.

Look first in:
1. current decision/state files;
2. `decisions/`;
3. `handoffs/` most relevant to that cluster/time period;
4. relevant older run files / Git history only if needed.

Goal: recover prior Mark wishes about **sleep base, number of nights/days, pace/spiritual dwell and transport** before asking Mark to approve final duration.

Rules:
- newest explicit Mark decision wins;
- do not revive old A/B/C or old route/calendar merely because a valid preference is found beside them;
- promote still-valid recovered preferences into CURRENT state/this preference canon or a current cluster decision file;
- if no additional preference is found, proceed; do not expand into an unbounded archive audit.

This gate exists specifically to prevent a repeat of the Haidakhan error, where the current A+/A list was correct but the older 3-night / 2-complete-day dwell intention was missed.

## HISTORICAL RECOVERY RULE
Older `handoffs/`, `governance/ACTIVE_STATE.md`, old route files and Git history can contain genuine Mark preferences that were never promoted into a current file.

Therefore, when:
- Mark says `dat hadden we al`, `zoek terug`, `ik had daar een voorkeur voor`, or equivalent;
- a current plan seems oddly generic despite long prior discussion;
- a sleep/base/transport/pace choice appears to have no current explanation;

INDIA must search the relevant historical entity/topic before asking Mark to repeat himself.

But historical recovery is **selective**: extract the still-valid preference and reconcile it into CURRENT state/current preference canon; do NOT revive the old route/calendar/grade bundle around it.

## WHAT THIS FILE DOES NOT CLAIM
This file does NOT prove that every preference Mark has ever stated has already been recovered. No INDIA version may claim 100% historical knowledge merely because boot passed.

The safety model is:
`CURRENT BOOT + CURRENT PREFERENCE CANON + PROTECTED DECISIONS + ACTIVE TASK FILES + LIGHT CLUSTER PREF CHECK BEFORE DURATION_CLOSED + TARGETED HISTORICAL RECOVERY WHEN SIGNALLED`.

END_OF_CURRENT_PREFERENCE_CANON

# SELF-CORRECTION — DEL→GAY SAME-DAY FLIGHT CLAIM

Date: 2026-09-09

Corrects: `GLOBAL_FULL_ROUTE_TOPOLOGY_REOPTIMIZATION_CCI_RESULT_2026-09-09.md` (this branch, commit `371e0a0`), §2a/§2b/§4/§5, and the corresponding PR #23 comment `5597485107`.
Prompted by: Work's independent rerun, `GLOBAL_FULL_ROUTE_TOPOLOGY_REOPTIMIZATION_CCI_RERUN_2026-09-09.md` (this branch, commit `7c206ec`).

## THE ERROR

My prior result stated DEL→GAY same-day continuation was "structurally impossible, not a close call, a scheduling impossibility," based on search results (ixigo/FlightsFrom) showing only 5x/week service with a last daily departure at 10:15 — at or before AI156's own landing time.

**That was wrong.** Work's rerun flagged that Air India's official Winter Schedule 2026 press release (published, primary source) adds **daily** service on this route effective 25 October 2026: **AI429 DEL 15:00 → GAY 16:40**, plus a second daily frequency **AI2561 DEL 07:45 → GAY 09:15**. I independently re-verified this directly against Air India's own press release before writing this correction — it is real and currently published, not a Work claim I am taking on faith.

## WHY MY ORIGINAL SEARCH MISSED IT

The aggregator results I used evidently reflected the pre-Winter-2026 timetable rather than the newly announced addition — a reminder that a single search pass against booking aggregators can lag an airline's own official schedule announcement, and that "no service found" is a weaker claim than "official schedule confirms no service."

## WHAT ACTUALLY CHANGES

AI429 gives a genuine, schedulable ~4h45 connection after AI156's 10:15 arrival — technically feasible, not impossible. This is tighter than comfortable (my own realistic-buffer model needs ~3.5–4.75h for immigration + terminal transfer + security, leaving only 1–1.5h of slack against any AI156 delay), so "feasible" is not the same as "safely robust."

## WHAT DOES NOT CHANGE

Work's own rerun, using the corrected schedule, still reaches **KEEP INCUMBENT**: same-day GAY is now the strongest challenger (not an impossible one), running roughly 55.5 waking transport hours versus the incumbent's ~57h — a difference inside the model's own ±2h uncertainty band — and it still loses lexicographically on the higher-priority tiers: an unprotected first-day domestic connection unless separately ticketed/protected against an AI156 delay, additional heavy days, later Delhi/Nirmal Dham staging, a fog-exposed Kumaon exit now sitting closer to AI155, and the loss of the current route's directional Agra rail asymmetry (12988's sleeper-class Agra→Gaya redirection versus 12987's daytime-only Gaya→Agra reverse). I independently agree with this reasoning — the corrected fact changes *why* GAY loses, not *whether* it loses.

## STATUS

**Final verdict unchanged: KEEP INCUMBENT.** The specific claim "DEL→GAY is schedule-impossible" is retracted and replaced with "DEL→GAY is schedulable but loses on safety/rest tiers, per Work's independently-verified rerun, which I concur with."

END

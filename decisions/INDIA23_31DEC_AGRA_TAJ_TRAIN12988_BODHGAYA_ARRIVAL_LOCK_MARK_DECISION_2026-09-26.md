# MARK DECISION — 31 DEC TAJ MAHAL → TRAIN 12988 → 1 JAN BODH GAYA ARRIVAL, LOCKED

Date: 2026-09-26
Decision authority: Mark, direct chat instruction to CCI ("Hou zoals jullie zeiden 12988 trein. Zet locked en zeg Mark oké erbij.")
Status: BINDING CURRENT TRUTH — resolves the post-Taj Agra→Gaya/Bodh Gaya transport question left open by the 23-Sep corridor lock and by both independent solves (CCI: this branch; WORK: PR #23 comment 5849075766, commit `be810109e135078d3c0119a0efa19ed5771b65af`).

## DECISION

Mark locks the full 31 Dec → 1 Jan chain exactly as both independently-produced solves converged on:

1. **Taj Mahal [A+]** at the earliest practical opening (~06:37, 30 min before sunrise — exact time LIVE_RECHECK shortly before travel), realistic 2–2.5h dwell.
2. Return to the Agra hotel; **the rest of the day through to ~17:00 is deliberate rest time, not idle waiting.** Mark explicitly does not want this reframed as wasted time or filled with additional sightseeing — no other Agra site is A-graded (Taj is the sole protected Agra sightseeing anchor), and Mark does not want stress or a forced extra stop on this day.
3. **Hotel requirement: afternoon/late checkout.** The Agra hotel must be booked or arranged so Mark can stay in the room through the rest block rather than vacating early and waiting elsewhere. This is a booking-stage requirement, not a routing change.
4. Depart hotel ~17:00–17:30 for Agra Fort station.
5. **LOCKED: train 12988 (Ajmer–Sealdah SF Express), Agra Fort 18:45 → Gaya Junction 07:50 (1 Jan)**, First AC (1A) as the target class. This is the train both CCI's independent solve and WORK's independent solve converged on without reading each other's result.
6. 1 Jan: alight Gaya Junction 07:50 → private car last-mile (~15–17 km, ~25–45 min) → **arrival Bodh Gaya hotel ~08:30–09:00**.

## WHAT THIS DOES NOT DECIDE

- Does not fill the 31-Dec afternoon rest block with any sightseeing (explicitly rejected by Mark).
- Does not decide Bodh Gaya 2-vs-3 nights — this arrival time (~08:30–09:00) is the on-time/best case that keeps 2 nights viable per `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/BODHGAYA_EXECUTION_GEOMETRY_2026-08-28.md`'s own logic; the actual night-count trade-off remains a later Mark-only decision.
- Does not commit to a specific Agra or Bodh Gaya hotel property — zone/function only.

## LIVE_RECHECK BEFORE BOOKING

- Exact 31-Dec-2026/1-Jan-2027 operation and 1A availability on train 12988.
- Exact Taj Mahal opening time / sunrise for 31 Dec 2026.
- Agra hotel's actual late/afternoon-checkout policy once a specific property is chosen.
- Current winter fog advisories for the Agra–Kanpur–Prayagraj–Gaya rail corridor closer to travel.
- Exact Gaya Junction → Bodh Gaya pickup point for the private car.

## SOURCES

- `runs/active/CCI_INDEPENDENT_31DEC_AGRA_BODHGAYA_HUMANE_CLOCKTIME_SOLVE_2026-09-26.md` (CCI, commit `0230baf`)
- WORK_RESULT, PR #23 comment `5849075766` (commit `be810109e135078d3c0119a0efa19ed5771b65af`)
- CCI_RESULT, PR #23 comment `5849251983`

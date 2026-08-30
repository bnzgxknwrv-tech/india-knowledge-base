# INDIA TRIP FRAME — HARD IMMUTABLE ENVELOPE

Status: HARD CURRENT TRIP FRAME
Updated: 2026-08-28
Branch: `agent/india8-cluster-casting`
Purpose: one short successor-safe source for the trip facts that must never be reconstructed from an old route/calendar.

## BOOKED INTERNATIONAL FLIGHTS
- Outbound Air India: **18 Dec 2026 20:35 AMS -> DEL**.
- Arrival Delhi: **19 Dec 2026 10:15**.
- Return Air India: **21 Jan 2027 12:20 DEL -> AMS**.
- Arrival Amsterdam: **21 Jan 2027 18:35**.

## NIGHT / DAY ENVELOPE
- The night of 18 Dec is on the outbound aircraft.
- First possible India accommodation night: **19 Dec 2026**.
- Last India accommodation night: **20 Jan 2027**.
- Total India accommodation / overnight-transport slots: **33 nights**.
- Project planning convention: **34-day trip budget** for route/day accounting.
- Never create a fictional Delhi hotel night on 18 Dec.
- If an overnight train/flight replaces a hotel night, show hotel nights and occupied travel nights separately.

## RETURN-RISK PRINCIPLE
- The international return departs Delhi at 12:20 on 21 Jan.
- Working safety preference: be back in Delhi before departure day, historically targeted by 19 Jan with 19/20 Jan available as final Delhi/flight resilience unless Mark later explicitly chooses another risk level.
- Exact final calendar is NOT locked yet; this is a safety principle, not a current dated route.

## HARD PLANNING CONSEQUENCES
- Every cluster footprint counts real occupied travel days; known inbound travel may not be hidden outside the cluster arithmetic.
- Door-to-door human burden controls, not published train/flight/road duration alone.
- Old V1/V2 exact calendars and route dates are provenance only until the current fixed-core / optional-world process reaches final calendar stage.

## TRANSPORT INVARIANTS FROM CURRENT MARK PROFILE
- Train first when practical.
- Overnight rail target: **1A / First AC**; 2A only after explicit Mark acceptance as fallback.
- Flight when it materially saves usable human time after airport overhead.
- Private car for mountains / last mile / door-to-door wins.
- Intercity / long-distance bus excluded as normal fallback.

## LIVE RECHECK BOUNDARY
These are NOT immutable and must be rechecked only when they affect a real booking/calendar decision:
- train operating days/times and 1A/2A inventory;
- domestic flight schedules/prices;
- visa rules/status;
- ashram acceptance/availability;
- hotel availability;
- opening/access/weather/safety.

Source provenance: `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/TRIP_FIXED_FLIGHTS_AND_NIGHTS_2026-08-23.md` plus current Mark profile. This file supersedes the need to recover the hard flight/night frame from any old exact route.

## PROTECTED CANON INTEGRITY ANCHOR
`governance/scripts/validate_successor_boot.py` checks this exact blob SHA against `PROTECTED_CANON_BASELINE.csv` to detect a silent mutation. This anchor lives here, not in `CURRENT_STATE.md`, precisely because this file is not rewritten every turn — a rewritten narrative file previously destroyed this same anchor the day after it was added.

Current protected blob (`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`):
`a607241caa41637e2167d0f56781bf663f038932`
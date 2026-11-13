# FINAL DELHI — ONE NIGHT ONLY — MARK DECISION

Date: 2026-09-07
Status: LOCKED_BY_MARK
Source: direct Mark statement, this session.

## MARK DECISION
Mark explicitly confirmed, after seeing a draft that gave him two full days in Delhi before departure, that he does **not** want that: he wants exactly **one day/one night in Delhi at the end of the trip**, not two.

Mark's own words: "ik kreeg een planning waar ik twee volle dagen in delhi had en pas de dag DAARNA ging vliegen, dat wil ik niet, ik wil maar 1 dag in delhi op het einde."

**Explicit conditional, same message thread**: "TENZIJ jullie denken dat het 'gevaarlijk' is om te gokken dat mn trein ECHT aankomt of mn vliegtuig etc" — i.e. this preference yields to a genuine, substantiated safety concern about missing AI155; it is not an absolute override of real risk.

## LOCK
- **Final Delhi = 1 night only**, immediately before the AI155 international departure (21 Jan 2027, 12:20).
- Consistent with the already-committed route/calendar (`worker/final-route-calendar-optimizer` commit `cc34089`, `runs/active/FINAL_TRIP_DATED_CALENDAR_2026-09-07.md`): arrive Delhi 20 Jan, sleep one night, fly 21 Jan.
- **Do NOT** adopt any alternative that arrives in Delhi on 19 Jan and holds a second Delhi night as a generic retry/robustness buffer, even if a future draft frames it as objectively safer for the international flight. That trade-off has been explicitly declined by Mark, conditional on the safety point below.

## SAFETY ASSESSMENT (why 1 night is not actually a risk trade-off here)
CCI's own independent stress test (`WORK_RESULT`/`CCI_RESULT — FINAL ROUTE/CALENDAR INDEPENDENT STRESS TEST`, PR #23) already found that the committed calendar's international-flight protection does **not** depend on a second Delhi night: the trip's one genuine spare slot sits earlier, on 19 Jan, as a Chennai-airport positioning night between Tiruvannamalai and the MAA→DEL flight. That is what already buys the ~1-day buffer before AI155 — the two-Delhi-night draft would have placed a *second, redundant* buffer, not the trip's only one. Declining the second Delhi night does not remove the existing protection.

This is a current-evidence assessment, not a permanent guarantee: if a later live-recheck finds the Chennai-positioning buffer itself is compromised (e.g. the 19 Jan slot gets consumed upstream by a Kumaon/Agra disruption, per the "compounding disruption" finding in the same stress test), the safety picture changes and must be re-raised with Mark explicitly rather than silently resolved either way.

## WHY THIS MATTERS FOR FUTURE SESSIONS
An earlier uncommitted worker draft proposed exactly the two-night version (arrive 19 Jan, extra buffer day, fly 21 Jan) as a "full retry day" for final-flight robustness. CCI flagged this as a change to Mark's standing preference requiring explicit confirmation before adoption (`CCI_RESULT — FINAL ROUTE/CALENDAR INDEPENDENT STRESS TEST`, PR #23 comment `5571020936`). Mark has now explicitly declined it. This file closes that open question durably: any future robustness/spare-night discussion must work within a single final Delhi night, not propose adding a second one as the default.

If a genuine two-night version is ever wanted again, it requires a fresh, explicit Mark reopening — not a route-optimizer's own robustness preference.

END

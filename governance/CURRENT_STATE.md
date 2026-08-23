# CURRENT STATE — INDIA

Last updated: 2026-08-23
Purpose: one human-readable page that tells the next INDIA session what is current.

## Project type
This is a personal India travel/pilgrimage knowledge base, not a software product. Governance exists only to prevent expensive repeat work, forgotten Mark decisions and confused handoffs. Prefer simple, recoverable workflows over formal ceremony.

## Start here
1. Read this file.
2. Read `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv` before presenting any location/cluster/hotel/base as a new choice.
3. Read the current task/output files relevant to what Mark is asking now.
4. Check PR #23 back to the last CCI/INDIA exchange you have not handled when starting a major new build.
5. Read older governance/branches only when a concrete inconsistency, provenance question or missing decision requires it.

## Current central regie branch
`agent/india8-cluster-casting`

This branch contains the INDIA9 one-time knowledge-audit imports plus the final LIGHT successor architecture agreed by INDIA9 and CCI. The abandoned heavier candidate branch `agent/india9-successor-architecture-integration` is provenance only and is not a competing current authority.

## Protected canon
Canonical protected decision file:
`runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv`

Current protected blob:
`a607241caa41637e2167d0f56781bf663f038932`

Existing Mark decisions, permanent IDs and locks must not be silently changed. A later explicit Mark decision may supersede an earlier one; when that happens, update the durable canon rather than maintaining competing truth files.

## What is active vs historical
- Current Mark decisions/locks + protected canon: ACTIVE.
- Current task `TASK.md`/`STATUS.md` and current travel outputs: ACTIVE when actually relevant to the question.
- Worker branch marked COMPLETE: useful input, but not automatically central truth until integrated or explicitly adopted.
- `governance/ACTIVE_STATE.md`, old handoffs, old pipeline generations, audit read streams and old worker snapshots: provenance/history unless a current file explicitly points to them.
- `governance/PRECEDENCE_MAP.jsonl`, semantic-import and central-integration registries remain audit evidence; they are not required routine reading for every session.

## CCI collaboration
PR #23 is the relay/index. Repo files hold durable substance.

Normal pattern:
`INDIA defines bounded task -> CCI worker/review -> INDIA evaluates -> central update if useful`.

Polling is deliberately light:
- check PR #23 once before starting a major new build;
- check it again immediately before writing to the central regie branch.

No continuous polling. Mark should not need to copy long CCI results between chats when INDIA can read them from GitHub.

## Travel freshness
Do not maintain a global certification status for every live travel fact. Recheck visas, opening/access, timetables, availability, prices and similar changing facts when they are actually about to affect a recommendation or booking decision.

## Good-enough boot rule
A new IndiaN can responsibly continue when it has read:
- this page;
- protected canon;
- the relevant current task/output files;
- any unhandled recent PR #23 exchange that materially affects the task.

If those disagree, read deeper until the conflict is understood. A full-repository reread is an exceptional recovery tool, not the normal start procedure.

## Current project phase — IMPORTANT CORRECTION 2026-08-23

**The project is NOT in the booking/application phase.**

Mark explicitly corrected an INDIA10 interpretation that treated a later route/booking artifact as the current execution frontier. The underlying location master is the stronger phase signal:

`runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/STATUS.md`

Current master state there:
- 700 row-level findings;
- 575 unique physical-entity keys;
- 211 genuine `STILL_UNRESOLVED` rows preserved;
- existing permanent IDs 001–081 and existing A/B/C/locks preserved;
- next execution order remains Mark-ready cluster/location slices and additive location closure before route/transport/hotel finalization.

Cluster-level decisions and site A/B/C choices already made by Mark remain protected provenance and must never be silently changed. However, on 2026-08-23 Mark explicitly opened a DELIBERATE RE-EVALUATION ROUND because many earlier A/B/C decisions predate completed person sweeps and/or true regional discovery. During this round it is allowed to present old decisions back to Mark for reconsideration after person + regional/location + traveler/experience layers are merged. Preserve the old grade/lock visibly as provenance until Mark explicitly supersedes it. INDIA/CCI/workers do not change A/B/C or cluster status on Mark's behalf.

Therefore the live phase is:

`COVERAGE AUDIT -> MISSING REGIONAL/LOCATION DISCOVERY + MULTI-AI TRAVELER/EXPERIENCE DISCOVERY -> MERGE WITH PERSON LAYERS + OLD ABC -> MARK RE-EVALUATES SITES/CLUSTER WEIGHT -> LATER NIGHTS/ROUTE/TRANSPORT/HOTELS -> LATER BOOKING`

Do not use the existence of route drafts, calendar work or booking-prep files as proof that upstream location/person closure is finished.

### Re-evaluation design — explicit Mark instruction 2026-08-23
- The trip remains primarily a spiritual pilgrimage. AOAY/Top-11 person relevance stays mission-critical.
- Regional/location discovery must also surface independently exceptional spiritual, cultural, historical and world-magnet places.
- Traveler/Lonely-Planet-style discovery must include EXPERIENCES, not only places: e.g. exceptional rafting/adventure, hot springs/wellness, wildlife, unusual transport, strange historical/cult experiences, old local institutions, markets/crafts, spectacular short nature experiences and other repeated traveler highlights.
- Do not use a fixed geographic radius as a hard exclusion. Run an adaptive WORLD-MAGNET check: a truly extraordinary place/experience substantially farther away may deserve Mark review, while a mediocre nearby place does not.
- Historic person evidence is not automatically a visit candidate. Private homes, ordinary hospitals, schools or workplaces without shrine/memorial/visitor context remain in the knowledge base but normally should not be surfaced as practical pilgrimage choices.
- Old `A` may have meant “definitely visit if already nearby” rather than “add a day/night for this”. During re-evaluation separately ask whether a site/experience is a CLUSTER DRIVER that justifies incremental cluster time.
- Do not move into quarter-hour itinerary construction until this re-evaluation has been completed far enough to recalculate cluster weight and nights.

## Current person/location front

The central branch now contains the missing final CCI_TASK 095 outputs for Neem Karoli Baba and Ram Dass:
- `runs/active/TOP11-NKB-RAMDASS-INDIAGEEL-MULTIDETECTOR-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- `runs/active/TOP11-NKB-RAMDASS-INDIAGEEL-MULTIDETECTOR-RECONCILIATION-001/TRAVEL_READINESS_GATE.md`

Both person sweeps remain `PERSON_SWEEP_SATURATED: NEE`.

INDIA10 then executed the exact targeted physical-identity follow-up CCI_TASK 095 requested for three Ram Dass gaps:
`runs/active/TOP11-NKB-RAMDASS-INDIAGEEL-MULTIDETECTOR-RECONCILIATION-001/RAM_DASS_TARGETED_TIER1_CLOSURE_2026-08-23.md`

Result at travel-identity level only:
- Dharamsala/McLeod Ganj — historical Swarg Ashram: travel-ready at building level;
- Ganeshpuri — Muktananda/Gurudev Siddha Peeth: travel-ready at ashram-complex level;
- Anandamayi Ma — Vrindavan and Kankhal ashrams: travel-ready at ashram-complex level.

This does not assign A/B/C or include any of these in Mark's route. Exact rooms/microsublocations remain separate where not proven.

Other national person layers also remain honestly non-saturated even where multi-detector reconciliation is already complete. For current travel re-evaluation, Mark considers the completed person-sweep bodies sufficient to proceed unless a concrete location/identity gap can materially change a cluster decision. Do not regress into open-ended national person research merely because a technical saturation token says NEE.

## Multi-AI traveler/experience discovery — active

Central task:
`runs/active/INDIA10-MULTIAI-TRAVELER-DISCOVERY-001/TASK.md`

This layer deliberately uses independent AI/search styles. CCI is not required for discovery. Workers freeze their own findings before reading the existing 80 findings or other worker outputs. Diversity is the detector; agreement is useful evidence but not required for a unique high-value finding.

Prepared worker branches:
- `agent/indialp-multiai-weird-human`
- `agent/indialp-multiai-nature-adventure`
- `agent/indialp-multiai-world-magnets`
- `agent/indialp-multiai-blind-general`

Central INDIA reconciles/deduplicates only after each independent freeze.

## Booking-prep artifact disposition

`runs/active/INDIA10-BOOKING-SEQUENCE-CLOSURE-001/BOOKING_ACTION_BOARD.md` is retained only as a **future planning artifact**. Its task STATUS is explicitly `FUTURE_PLANNING_ARTIFACT__NOT_CURRENT_PROJECT_PHASE`.

Do not ask Mark for visa status, send accommodation requests, or drive the project from that board until upstream person/location/cluster work has actually reached that stage. Time-sensitive facts in that board should be revalidated later when they become actionable.

## Current architecture status
`INDIA9_SCOPE_SIMPLIFICATION: PASS`
`CCI_FINAL_SANITY_011: PASS`
`STOP_OPTIMIZING: JA`

Architecture optimization is over. The correction above is not a new governance layer; it is a factual phase correction after a real provenance contradiction was found.

## Current next-action rule

Finish the retained-cluster coverage audit. Execute only genuine RED/ORANGE regional/location gaps plus the independent multi-AI traveler/experience layer. Then merge person + region/location + traveler/experience + old A/B/C into Mark-ready cluster review slices. Preserve prior decisions until Mark explicitly changes them; do not infer regrades. Quarter-hour planning stays downstream of the renewed cluster/nights decision.

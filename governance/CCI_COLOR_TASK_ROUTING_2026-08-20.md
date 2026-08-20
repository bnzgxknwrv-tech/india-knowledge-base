# INDIA — CCI / COLOR TASK ROUTING — 2026-08-20

Status: ACTIVE
Coordinator: INDIA8/INDIA9

## PURPOSE
Minimize Mark handoffs and conserve Claude Code/CCI token budget while preserving GitHub-integrated QA.

## DEFAULT ROUTING
### CCI / Claude Code
Use primarily for:
- cross-branch integration and reconciliation;
- central master assembly/repair;
- repo-wide QA, accounting, provenance, canon integrity;
- resolving pipeline/schema/branch-governance conflicts;
- small high-value tasks where direct GitHub-wide context is load-bearing.

Do NOT default CCI to:
- broad web discovery;
- long source-by-source historical sweeps;
- large occurrence-by-occurrence corpus searches;
- image/location research that can be isolated to one branch;
- repetitive coordinate/access lookup.

### COLOR WORKER
Use for heavy isolated execution:
- broad web/source research;
- historical physical-location resolution;
- occurrence extraction;
- photo-location investigations with bounded inputs;
- access/current-existence checks;
- targeted geographic closure;
- large row enrichment that does not require repo-wide write integration.

One color worker at a time by default. Maximum two active worker streams total including CCI, per DOORGANGSPROTOCOL.

## TOKEN RULE
Before assigning a new CCI task, INDIA-regie must ask:
`Does this task materially require CCI's GitHub-wide integration/QA advantage?`
If NO -> assign to a color worker.
If YES -> keep scope bounded and avoid making CCI repeat discovery already available elsewhere.

## CURRENT EXAMPLE
- Central ALL_FINDINGS master integration/accounting -> CCI appropriate.
- Exhaustive AOAY source-to-location reconciliation -> can be color-worker heavy research, with CCI only reconciling/QA after.
- Anandamayi/Yogananda joint-photo physical-location search -> suitable for a bounded color-worker task; CCI need only consume/QA result if necessary.

## MARK ROLE
Mark should not need to manage many colors. INDIA-regie supplies at most one worker start prompt at a time unless real parallelism gives substantial benefit.

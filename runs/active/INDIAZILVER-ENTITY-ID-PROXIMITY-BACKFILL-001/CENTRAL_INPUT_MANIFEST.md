# CENTRAL INPUT MANIFEST — INDIAZILVER ENTITY/ID/PROXIMITY BACKFILL

Status: AUTHORITATIVE INPUT ROUTING FROM INDIA8
Date: 2026-08-20

## PURPOSE
ZILVER is not blocked by absence of one monolithic canon file. This task is explicitly staged. Use the exact sources below and do not invent coordinates or IDs.

## ALLOWED / REQUIRED CURRENT-BRANCH INPUTS
Read these on `agent/indiazilver-cluster-completeness-audit`:
- `runs/active/INDIAZILVER-CLUSTER-COMPLETENESS-AUDIT-001/CLUSTER_RECALL_AUDIT.md`
- `runs/active/INDIAZILVER-CLUSTER-COMPLETENESS-AUDIT-001/MISSED_NEARBY_RISK.md`
- `runs/active/INDIAZILVER-CLUSTER-COMPLETENESS-AUDIT-001/REOPEN_AND_ID_QUEUE.md`
- `runs/active/INDIAZILVER-CLUSTER-COMPLETENESS-AUDIT-001/ABC_REVIEW_QUEUE.md`
- `runs/active/INDIAZILVER-CLUSTER-COMPLETENESS-AUDIT-001/COMPLETENESS_GATE.md`
- `runs/active/INDIAZILVER-CLUSTER-COMPLETENESS-AUDIT-001/TOP_REOPEN_PRIORITIES.md`
- current task outputs `PROTECTED_CANON_BASELINE.csv` and `NEW_ID_REQUIRED_QUEUE.csv` already created in this run.

## EXPLICIT CROSS-BRANCH CENTRAL INPUTS — ALLOWED
Read these exact files from branch `agent/india8-cluster-casting`:
- `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/SOURCE_LEDGER.md`
  source commit lineage includes `285a70c82acefc7fdc3d73d621a72aefc4de6c3f`.
- `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/GLOBAL_UNRESOLVED_QUEUE_SEED.md`
  source commit lineage includes `73d8f7f8705924f4c041645b0bd4091e3569effd`.
- `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/STATUS.md`
- `governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md`

These are routing/source-accounting inputs, not a finished unique-entity coordinate table.

## STAGED EXECUTION — DO NOW
### Stage Z1 — protected canon recovery
Do not wait for the global all-findings entity master. Recover all existing permanent IDs / A-B-C / locks / available coordinates from every old cluster/register source already used by the earlier ZILVER audit. If a particular old cluster has no trustworthy coordinates, write `UNKNOWN`, never fabricate.

### Stage Z2 — existing 31 new-candidate queue
Use the earlier `REOPEN_AND_ID_QUEUE.md` as the initial NEW_ID_REQUIRED seed. For every one of the 31 candidates, obtain reliable current coordinates where physical identity is already sufficient. If identity is not yet closed, mark `DEPENDENCY_ENTITY_CLOSURE` rather than dropping it.

### Stage Z3 — proximity now where possible
Build `PROXIMITY_1KM_3KM_MATRIX.csv` for every pair where BOTH coordinates are trustworthy. Unknown coordinates must remain explicit. This matrix may be partial now and later append-only expanded when ROOD/GEEL/BLAUW/WIT/TURQUOISE entity feeds arrive.

### Stage Z4 — duplicate/parent and ABC review seeds
Create `DUPLICATE_PARENT_CANDIDATES.md` and `ABC_REVIEW_AFTER_CLOSURE_QUEUE.md` from evidence already available. Do not wait for all parallel agents. Mark unresolved dependencies explicitly.

### Stage Z5 — status
Finish this pass as `PARTIAL_COMPLETE__WAITING_FOR_PARALLEL_ENTITY_FEEDS` if and only if all currently available work above is exhausted. This is not a failure/blocker; it is the designed pipeline state. Later entity feeds are additive input.

## LATER ADDITIVE FEEDS
When these parallel tasks complete, ingest them without overwriting old work:
- INDIABLAUW AOAY/Yogananda location closure
- INDIAROOD Core-Kriya location closure
- INDIAGEEL four-person location closure
- INDIAWIT Anandamayi/heritage location closure
- INDIATURQUOISE entity-overlap reconciliation

## HARD
No existing ID/A-B-C/lock changes. No guessed coordinates. No definitive new IDs. No silent drops. Partial proximity is useful and required; `UNKNOWN` is a valid result.
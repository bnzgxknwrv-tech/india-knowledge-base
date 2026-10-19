# NEXT EXECUTION MAP — INDIA WIT

status: CURRENT_EXECUTION_BRIDGE
snapshot_date: 2026-08-19
scope: exact downstream work sequencing; no new person-location research; no A/B/C on behalf of Mark

## Work that can proceed immediately, before CCI_TASK 095

### A. Complete non-research parallel prep
1. INDIA PAARS completes its four decision-support outputs.
2. INDIA ROZE completes its five route-engine outputs.
3. These two streams can run fully in parallel with CCI/person closure because neither requires new person-location research.

### B. Prepare national heatmap mechanics
1. Use ORANJE `HEATMAP_SCHEMA.md` as the ingest contract.
2. Seed the aggregate layer from `MASTER_HEATMAP_INPUT.md` using `MIN_CONFIRMED` counts and explicit evidence maturity.
3. Carry exact-site/city/region overlap as separate fields.
4. Preserve conflicts and provisional records; keep `travel_significance: ONBESLIST`.
5. Do not freeze final NKB/Ram Dass counts until 095 is durable.

### C. Apply CCI_TASK 094 immediately
Ramana Maharshi and Ramakrishna can now move from pending-multidetector status to reconciled-but-unsaturated travel input. Update their heatmap evidence state and any affected Kolkata/Vrindavan/Varanasi/Tiruvannamalai records without launching new person research.

### D. Continue route-independent operations
Use INDIA BLAUW as standing guardrail:
- visa application window starts 2026-08-20 for the 1y/5y e-Tourist Visa regime described in the verified source set;
- recheck visa/entry and railway rules 2026-10-01;
- first normal 60-day train windows for 2026-12-18 open 2026-10-19 under the current rule;
- rolling train-window openings continue through 2026-11-22 for travel through 2027-01-21;
- winter/fog and local road checks remain later, route-specific operations.

## Work directly unlocked when CCI_TASK 095 becomes durable

1. Replace current `RECONCILED_CURRENT_BUT_095_PENDING` state for NKB and Ram Dass with the 095 result state.
2. Recompute only affected `MIN_CONFIRMED` city/region/exact-site rows, especially Kainchi/Nainital, Vrindavan and Prayagraj.
3. Re-run cluster-trigger classification for regions whose exactness/conflict/dedup status changed.
4. Decide whether any remaining NKB/Ram Dass research gap is travel-material. If 095 leaves only academic gaps, stop person research and move on.

Do not ingest 095 assumptions before its durable result exists.

## Person-layer closure after 095

### Yogananda
Perform a bounded reconciliation/QA closure sufficient to distinguish travel-material confirmed/provisional links. Do not default to another open-ended sweep. Priority is whether current uncertainty can change the selected clusters or exact-site interpretation.

### Hariharananda and Vivekananda
Follow governance: no exhaustive nationwide deep sweep. Only verify/reconcile the largest already-known locations if the heatmap shows that uncertainty can alter a real destination/cluster decision.

### Anandamayi Ma
Normalize organization-listed versus personally evidenced presence only where it can alter a real cluster. Retain targeted Ranchi/Bhowanipur evidence as stronger specific input.

## When regional deep sweeps are actually necessary

Use ORANJE trigger logic after the relevant person records are sufficiently reconciled.

Start a regional deep sweep only when at least one travel-material condition exists:
- multiple persons plus at least one exact/complex site require regional verification;
- multiple known sites for one person need dedup/access validation;
- a concentrated location/identity conflict can alter visit logistics;
- exactness is too weak (`CITY_ONLY`/`REGION_ONLY`) for route/site-day planning;
- cross-person same-complex identity remains unresolved;
- a locked/known anchor has surrounding known records that require logistics-only cluster verification.

Use `DEFER` when a person reconciliation or Mark decision is still open. Do not start an exhaustive regional sweep simply because a region is spiritually dense.

## When to skip regional sweep and go directly to route

Proceed directly from heatmap/Mark decision to route input when:
- the chosen cluster’s important physical sites are already sufficiently exact;
- no material identity/dedup conflict remains;
- access can be verified later through ordinary travel logistics rather than historical person research;
- remaining gaps are academic microgaps only;
- a new sweep would not change destination, intensity, nights or transport.

This stop rule is critical: research completeness is not the same as travel readiness.

## Mark decision gate

After PAARS is complete and heatmap counts are stable enough for travel use:
1. present protected anchors as fixed context;
2. present still-undecided major clusters in one national batch;
3. after Mark selects significance, present intensity per kept cluster;
4. then present comfort/route-efficiency envelope;
5. ask later only for true exception decisions.

No route or nights are frozen before this gate.

## Route-build sequence after Mark decisions

1. Instantiate ROZE route input contract for selected clusters only.
2. Generate route/nights ranges using optimization rules; preserve fixed anchors/dates and avoid backtracking.
3. Test transport feasibility and booking windows in parallel.
4. Add winter/fog buffers and remote-access checks where applicable.
5. Resolve any high-impact infeasibility back to Mark; do not silently drop or downgrade a chosen cluster.
6. Once route is stable, research/select stays only inside the chosen route.
7. Build day plans per stay cluster with times/ranges, site priorities, booking/deadline fields, fallbacks and last-verified data.
8. Run final consistency audit across dates, nights, transfers, booked/booking-critical segments, visa/admin, weather buffers and return chain.

## Critical execution dependency graph

`CCI094 COMPLETE`
→ `095 when executed` + `PAARS` + `ROZE` can run in parallel
→ `travel-material person closure (Yogananda / limited Hariharananda-Vivekananda / Anandamayi normalization)`
→ `national heatmap final-enough snapshot`
→ `regional sweep only for YES triggers`
→ `batched Mark decisions`
→ `route + nights model`
→ `transport feasibility / booking sequence`
→ `stays`
→ `day plans`
→ `final A-Z audit`

## Current blockers versus non-blockers

Blocking final A-Z route now:
- PAARS incomplete;
- ROZE incomplete;
- 095 not yet durable;
- remaining travel-material person closure not yet explicitly released;
- Mark national cluster/intensity decisions not yet taken.

Not blocking current preparation:
- academic saturation gaps in already travel-usable person layers;
- unresolved micro-sites that do not affect a selected cluster;
- future weather/road conditions that can only be checked near travel time;
- exact hotel choice, which must wait for the selected route and is outside this task.
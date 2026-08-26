# INDIA ROUTE TOPOLOGY CHECKPOINT — 2026-08-26

status: CURRENT_ROUTE_FRONTIER / TOPOLOGY_BLOCKS_COMPLETE_PROVISIONAL
branch: agent/india8-cluster-casting

## FOR INDIA11+
This file is a compact delta checkpoint for the current route-planning phase.

### WHAT WAS FOUND WRONG
Earlier conversational exact-date/day sketches are NOT reliable because known transfer times were not consistently charged as occupied door-to-door time. Those sketches must not be reused as calendar truth.

### WHAT REMAINS VALID
All protected A+/A/A*/B/C decisions, person/location research, Komoot findings, safety work and HOTEL locks remain valid unless explicitly superseded.

### HARD CURRENT HOTEL / DISPLAY DELTAS
- every sleeping place is user-facing prefixed HOTEL, even a guesthouse/retreat/ashram when used as sleeping base;
- KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (...) — accommodation LOCKED_BY_MARK;
- all Mark-facing places must ALWAYS use full cluster/place/site + short Dutch explanation + current status; never shorthand.

### CURRENT ROUTE METHOD
No exact calendar yet.
Use real door-to-door occupied travel time: pickup/loading + ground travel + terminal buffers + flight/train + baggage/exit + hotel transfer/check-in + meal/rest + winter/traffic/fog buffer.

Controlling active files:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md`
2. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/TASK_SPLIT_2026-08-26.md`
3. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/NORTH_TOPOLOGY_DECISION_SUPPORT.md`
4. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/EAST_CORRIDOR_TRANSFER_TOPOLOGY.md`
5. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/SOUTH_JUMP_TRANSFER_TOPOLOGY.md`
6. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/GLOBAL_CLUSTER_TOPOLOGY_SYNTHESIS.md`

### TASK SPLIT — CURRENT RESULT
BLOCK 1 NORTH — COMPLETE PROVISIONAL.
Result: RISHIKESH/HARIDWAR is `STRUCTURALLY_PLAUSIBLE / REALISTIC_TO_RETAIN`; best current north hypothesis is `DELHI -> KUMAON -> RISHIKESH/HARIDWAR -> AGRA`. It may be an ALTERNATIVE_CORRIDOR_BUNDLE, not a true side excursion.

BLOCK 2 EAST — COMPLETE PROVISIONAL.
Result: strongest current east-corridor hypothesis is `AGRA -> BODH GAYA/GAYA -> VARANASI/SARNATH`.
- current daily Agra Fort -> Gaya overnight rail gives a one-seat eastbound option with low waking-day loss but sleep/recovery penalty;
- reverse order via direct Agra -> Banaras Vande Bharat remains structurally valid but consumes most of a waking day;
- Bodh Gaya/Gaya <-> Varanasi/Sarnath remains a natural paired-world transfer;
- no train/mode/date is locked.

BLOCK 3 SOUTH — COMPLETE PROVISIONAL.
Result: strongest current south-jump hypothesis is `VARANASI/SARNATH -> VNS -> CHENNAI -> TIRUVANNAMALAI/ARUNACHALA`.
- current VNS->MAA nonstop plus ~171.6 km / ~2h31 raw road from Chennai Airport to Tiruvannamalai gives about `~9–11h HOTEL-to-HOTEL` working class;
- VNS->BLR is a strong fallback but has a ~232 km / ~3h33 raw road tail and about `~10–12.5h` working class;
- Gaya has no current nonstop to Chennai or Bengaluru and is downranked as south gateway;
- actual Dec 2026 / Jan 2027 service must be rechecked only at calendar/booking stage.

BLOCK 4 GLOBAL STITCH — COMPLETE PROVISIONAL.
Strongest no-date one-way skeleton:
`DELHI -> KUMAON -> [optional RISHIKESH/HARIDWAR/KANKHAL] -> [optional BRAJ] -> AGRA -> [optional PRAYAGRAJ] -> BODH GAYA/GAYA -> VARANASI/SARNATH -> CHENNAI gateway -> TIRUVANNAMALAI/ARUNACHALA`.

All six fixed core worlds remain structurally feasible.
Optional logistics before dwell time:
- Braj: lowest geometric burden; no forced extra full travel day; +0 base if bundled/day-tripped, +1 only if sleeping there;
- Rishikesh/Haridwar/Kankhal: roughly +1 additional movement day +1 sleeping base versus the already-long eastern-Kumaon exit;
- Prayagraj: roughly +1 sleeping base +1 additional waking movement block/day because the no-Prayagraj alternative can use a direct Agra->Gaya overnight train.

Canonical output: `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/GLOBAL_CLUSTER_TOPOLOGY_SYNTHESIS.md`.

### CURRENT FRONTIER — MARK-ONLY AFTER DECISION SUPPORT
Do NOT return to topology research or exact dates.

The next necessary action is a genuine Mark retain/drop decision on the OPEN optional cluster worlds, but only after complete Mark decision cards are assembled from already-integrated regional/traveler findings plus the newly closed logistics:
- `HARIDWAR–RISHIKESH / HARIDWAR–KANKHAL–RISHIKESH / spirituele Ganges-cluster (...) — huidige status: OPEN`;
- `BRAJ / MATHURA–VRINDAVAN–GOVARDHAN / Braj-pelgrimscluster (...) — huidige status: OPEN`;
- `PRAYAGRAJ / PRAYAGRAJ / heilige Ganges–Yamuna-samenvloeiingscluster (...) — huidige status: OPEN`.

After Mark retains/drops these worlds, obtain desired dwell-time RANGES for retained worlds; only then close exact used edges/nights and rebuild calendar dates.

### IMPORTANT CURRENT USER INTENT
Mark wants to know which clusters remain realistic under actual travel-time burden before choosing exact number of days per cluster. Travel time is ultra-important. The topology phase has now supplied that burden without silently dropping any optional world.

### YSS / DUNAGIRI DELTA
KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (...) — current status A; Mark wants a full day there. Mark is Ananda, not YSS/SRF, so do NOT plan YSS overnight accommodation. HOTEL Dunagiri Retreat remains sleeping base candidate for this world; commute logistics need final schedule closure later.

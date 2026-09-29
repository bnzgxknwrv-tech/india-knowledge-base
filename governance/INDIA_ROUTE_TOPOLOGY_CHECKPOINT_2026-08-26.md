# INDIA ROUTE TOPOLOGY CHECKPOINT — 2026-08-26

status: CURRENT_ROUTE_FRONTIER / TOPOLOGY_BLOCKS_COMPLETE_PROVISIONAL
branch: agent/india8-cluster-casting

## FOR INDIA11+
Compact delta checkpoint for the current route-planning phase.

### WHAT WAS FOUND WRONG
Earlier conversational exact-date/day sketches are NOT reliable because known transfer times were not consistently charged as occupied door-to-door time. Those sketches must not be reused as calendar truth.

### WHAT REMAINS VALID
All protected A+/A/A*/B/C decisions, person/location research, Komoot findings, safety work and HOTEL locks remain valid unless explicitly superseded.

### HARD CURRENT HOTEL / DISPLAY DELTAS
- every sleeping place is user-facing prefixed HOTEL, even a guesthouse/retreat/ashram when used as sleeping base;
- `KUMAON / DUNAGIRI / HOTEL Dunagiri Retreat (...) — accommodatie-status: LOCKED_BY_MARK`;
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
7. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/OPTIONAL_CLUSTER_MARK_DECISION_CARDS.md`

### TASK SPLIT — CURRENT RESULT
BLOCK 1 NORTH — COMPLETE PROVISIONAL.
Result: RISHIKESH/HARIDWAR is `STRUCTURALLY_PLAUSIBLE / REALISTIC_TO_RETAIN`; strongest current north hypothesis is `DELHI -> KUMAON -> RISHIKESH/HARIDWAR -> VRINDAVAN/AGRA corridor`. It is an alternative corridor bundle, not a true side excursion.

BLOCK 2 EAST — COMPLETE PROVISIONAL.
Result: strongest current east-corridor hypothesis is `AGRA -> BODH GAYA/GAYA -> VARANASI/SARNATH`.
- current direct Agra Fort -> Gaya overnight rail gives a one-seat eastbound option with low waking-day loss but sleep/recovery penalty;
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
`DELHI -> KUMAON -> [optional RISHIKESH/HARIDWAR/KANKHAL] -> VRINDAVAN fixed A anchors -> [optional broader BRAJ] -> AGRA -> [optional PRAYAGRAJ] -> BODH GAYA/GAYA -> VARANASI/SARNATH -> CHENNAI gateway -> TIRUVANNAMALAI/ARUNACHALA`.

### AL BESLIST? CORRECTION — HARD
Formal DECISION-0008 already fixed:
- `BRAJ / VRINDAVAN / Katyayani Peeth / Keshav Ashram (...) — huidige status: A`;
- `BRAJ / VRINDAVAN / Neem Karoli Baba Ashram en samadhi (...) — huidige status: A`.

Do NOT present Vrindavan itself as optional and do NOT ask Mark to re-grade these sites. Only the broader Braj expansion remains OPEN.

### OPTIONAL BURDEN BEFORE DWELL
- broader Braj around fixed Vrindavan A anchors: lowest geometric burden; no forced extra full travel day; +0 base if bundled, +1 only if Mark deliberately sleeps there;
- Rishikesh/Haridwar/Kankhal: roughly +1 additional movement day +1 sleeping base versus the already-long eastern-Kumaon exit;
- Prayagraj: roughly +1 sleeping base +1 additional waking movement block/day because the no-Prayagraj alternative can use direct Agra->Gaya overnight rail.

### CURRENT FRONTIER — MARK-ONLY
Do NOT return to topology research or exact dates.

Use `OPTIONAL_CLUSTER_MARK_DECISION_CARDS.md` and ask only:
1. Haridwar/Kankhal/Rishikesh — RETAIN or DROP;
2. broader Braj around fixed A anchors — A-ANCHORS_ONLY / VRINDAVAN_CORE_PLUS / BROADER_BRAJ;
3. Prayagraj — RETAIN / DROP / RETAIN_ONLY_IF_MAGH_MELA_ALIGNS.

After Mark decides, obtain desired dwell-time RANGES for retained/open-expanded worlds; only then close exact used edges/nights and rebuild calendar dates.

### YSS / DUNAGIRI DELTA
`KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (...) — huidige status: A`; Mark wants a full day there. Mark is Ananda, not YSS/SRF, so do NOT plan YSS overnight accommodation. HOTEL Dunagiri Retreat remains sleeping base candidate for this world; commute logistics need final schedule closure later.
# INDIA ROUTE TOPOLOGY CHECKPOINT — 2026-08-26

status: CURRENT_ROUTE_FRONTIER
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
No exact calendar until route topology is closed.
Use real door-to-door occupied travel time: pickup/loading + ground travel + terminal buffers + flight/train + baggage/exit + hotel transfer/check-in + meal/rest + winter/traffic/fog buffer.

Controlling active files:
1. `runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/GLOBAL_TRANSFER_LEDGER_2026-08-25.md`
2. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/TASK_SPLIT_2026-08-26.md`
3. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/NORTH_TOPOLOGY_DECISION_SUPPORT.md`
4. `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/EAST_CORRIDOR_TRANSFER_TOPOLOGY.md`

### TASK SPLIT
BLOCK 1 NORTH — COMPLETE PROVISIONAL.
Result: RISHIKESH/HARIDWAR is `STRUCTURALLY_PLAUSIBLE / REALISTIC_TO_RETAIN`; best current north hypothesis is DELHI -> KUMAON -> RISHIKESH/HARIDWAR -> AGRA. It may be an ALTERNATIVE_CORRIDOR_BUNDLE, not a true side excursion. Do not globally lock yet.

BLOCK 2 EAST — COMPLETE PROVISIONAL.
Result: strongest current east-corridor hypothesis is `AGRA -> BODH GAYA/GAYA -> VARANASI/SARNATH`.
- direct daily Agra Fort -> Gaya overnight rail currently gives a one-seat eastbound option with low waking-day loss but a sleep/recovery penalty;
- direct Agra -> Banaras Vande Bharat is a structurally valid reverse-order alternative but consumes most of a waking day;
- Agra -> Delhi -> east by air remains a valid fallback, but adds multi-mode backtracking and a full travel-day class;
- Bodh Gaya/Gaya <-> Varanasi/Sarnath is a natural paired-world transfer; private car is operationally competitive with rail after station/local-transfer interfaces are counted.
No train/mode/date is locked yet. Exact Dec 2026 / Jan 2027 service is rechecked only when calendar/booking becomes relevant.
Canonical output: `runs/active/INDIA10-CLUSTER-TOPOLOGY-001/EAST_CORRIDOR_TRANSFER_TOPOLOGY.md`.

BLOCK 3 SOUTH — NEXT ONLY.
Scope: BODH GAYA/GAYA / VARANASI northern eastern gateway -> TIRUVANNAMALAI/ARUNACHALA. Compare actual plausible air/rail/road gateway sequences and full occupied travel-day cost. No global stitch and no exact calendar.

BLOCK 4 GLOBAL STITCH — only after 1–3.
Then determine realistic cluster set / approximate footprint. Only after that may exact dates and special-event targeting return.

### IMPORTANT CURRENT USER INTENT
Mark wants to know which clusters remain realistic under the actual travel-time burden BEFORE choosing exact number of days per cluster. Rishikesh is specifically under review, not dropped. Travel time is ultra-important. Work in bounded blocks to avoid long-loop failure.

### YSS / DUNAGIRI DELTA
KUMAON / DWARAHAT / Yogoda Satsanga Sakha Ashram — Dwarahat (...) — current status A; Mark wants a full day there. Mark is Ananda, not YSS/SRF, so do NOT plan YSS overnight accommodation. HOTEL Dunagiri Retreat remains sleeping base candidate for this world; commute logistics need final schedule closure later.

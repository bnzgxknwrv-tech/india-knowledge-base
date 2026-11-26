# INDIA10 — GLOBAL ROUTE AUDIT — BOUNDED TASK SPLIT

status: ACTIVE
updated: 2026-08-26
branch: agent/india8-cluster-casting

## PURPOSE
Prevent long-loop failure. Global route planning is split into small independent blocks. Do NOT solve all clusters in one pass.

## BLOCK 1 — NORTH TOPOLOGY (ACTIVE NOW)
Scope only:
- DELHI core world
- KUMAON core world
- RISHIKESH/HARIDWAR/KANKHAL candidate world
- AGRA core world only insofar as needed to judge north ordering
Question: does Rishikesh/Haridwar fit naturally with current A+/A choices once realistic door-to-door travel time is charged, or does it introduce disproportionate backtracking / extra travel-day burden?
Output: NORTH_TOPOLOGY_DECISION_SUPPORT.md
No exact calendar dates yet.

## BLOCK 2 — EAST CORRIDOR
Scope only:
- AGRA/DELHI gateway relation
- VARANASI/SARNATH
- BODH GAYA/GAYA
Compare realistic transfer modes and occupied time. No south work.
Output: EAST_CORRIDOR_TRANSFER_TOPOLOGY.md

## BLOCK 3 — SOUTH JUMP
Scope only:
- BODH GAYA/GAYA / possible northern gateway
- TIRUVANNAMALAI/ARUNACHALA
Compare flight/rail/ground sequences and full occupied travel-day cost.
Output: SOUTH_JUMP_TRANSFER_TOPOLOGY.md

## BLOCK 4 — GLOBAL STITCH
Only after blocks 1–3 exist.
Combine selected cluster worlds into minimal-backtracking route topology. Compute approximate travel-day burden, number of base changes and plausible total cluster footprint. Then decide which deferred clusters are realistically retainable before exact days are assigned.
Output: GLOBAL_CLUSTER_TOPOLOGY_SYNTHESIS.md

## HARD RULES
- no exact date calendar until global stitch closes;
- every edge uses door-to-door occupied time, not raw flight/train/drive time;
- preserve A+/A/A*/B/C and HOTEL locks;
- never silently drop a cluster; identify incremental burden and let Mark decide when subjective;
- every Mark-facing place uses full CLUSTER / PLACE / SITE + explanation + status;
- checkpoint after every block so INDIA11+ can continue without chat context.

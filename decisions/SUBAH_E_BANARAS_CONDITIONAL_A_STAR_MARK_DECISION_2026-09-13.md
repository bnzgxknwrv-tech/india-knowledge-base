# MARK DECISION — SUBAH-E-BANARAS BECOMES CONDITIONAL A* (ROUTE-COST-DEPENDENT)

Status: **HARD / BINDING**
Date: 2026-09-13
Owner: Mark (direct instruction to CCI, relayed to GitHub)
Branch: `agent/india8-cluster-casting`
Source ID: `VNS-09` (A-number `A037`)

## DECISION

`Subah-e-Banaras, Assi Ghat` changes from a plain **A** to **A*** — using this project's existing A* semantics (real A-quality content, but conditional/corridor-bycatch: only include it if it costs no extra day/base-change, never a dedicated special trip).

Mark's own words: he wants this included **if he happens to already be near it from his hotel** (no schedule cost), but explicitly **not** if it would require staying an extra day just for this. This is the same conditional logic already used for other A* sites in this project (e.g. Sattal, Rajgir Brahmakund, Kakrighat) — a genuinely valuable experience that should never itself drive route/duration decisions.

## UPDATED IN

- `runs/active/INDIA19-FINAL-ITINERARY-REBUILD-001/PHYSICAL_A_PLUS_A_COVERAGE_LEDGER.csv` (`VNS-09` grade column: A -> A*).
- `governance/DECISION_LEDGER.jsonl` (`DL-0058`).
- Person-provenance restoration files, once the in-progress re-verification pass on `worker/india19-cci-person-provenance-merged` completes.

## SUCCESSOR RULE

Do not schedule a dedicated day/detour for `A037`/`VNS-09`. Include it only when it fits the existing route/base for free (e.g. because Mark's Varanasi sleep base is already at/near Assi Ghat). Never let it justify an extra night.

END MARK DECISION

# NEW KNOWLEDGE CANDIDATES — verified absent from frozen central `a37423639f7dabb0dfd55c8656d4689bb8a25351`

Running list. Each entry states the exact source (path + blob SHA or recovery ref), what is new,
and the verification that establishes it is not already in the central tree.

---

## NK-001 — `decisions/MARK_DECISIONS.jsonl` (three append-only Mark decision records)

- Source: deleted path `decisions/MARK_DECISIONS.jsonl`, blob `6314e359e86d0d99c9f37204365126e94902ca55`
- Recovered from history; path exists on NO current tip.
- Content:
  - `INDIA3-DECISION-0001` (worker_abc_authority): BRONS, ZILVER and GOUD may not assign formal
    or advisory A/B/C. Anything not chosen by Mark remains `DOOR_MARK_TE_BEOORDELEN`.
  - `INDIA3-DECISION-0002` (goud_user_delivery): GOUD completion requires a readable decision PDF
    **and** a complete KML. Source: GitHub issue #22.
  - `INDIA3-DECISION-0003` (`VNS-CAND-008` GEO): a coordinate explicitly rejected by Mark may not
    be restored; unresolved GEO must remain candidate-specific and must not block the other 39.
- Verification: `git grep -l INDIA3-DECISION` against central returns nothing.
- Class: `CURRENT_CANON` (0001, 0003 still binding as governance rules), `HISTORICAL_PROVENANCE_ONLY` (0002).

## NK-002 — no-technical-GitHub-explanations rule

- Source: deleted path `india3/lessons/2026-07-24_USER_OUTPUT_NO_TECHNICAL_GITHUB_EXPLANATIONS.md`
- Binding Mark decision: no technical GitHub explanation (blobs, trees, commits, SHAs, JSONL,
  connector, API) may be shown to Mark. Visible response = short human observation, then
  immediately the full next start prompt.
- Verification: no equivalent statement in central `governance/`.
- Class: `CURRENT_CANON` (user-communication rule, still applies to every successor).

## NK-003 — `BOOKING_CONTACT_PACK.md`

- Source: deleted path `runs/active/INDIA10-BOOKING-SEQUENCE-CLOSURE-001/BOOKING_CONTACT_PACK.md`,
  blob `59bf89501c91`, 8,829 B.
- Copy-ready booking messages for the five locked sleepbases with exact dates:
  Haidakhan 20–23 Dec 2026; Joshi Guest House 23–26 Dec 2026; Hotel Evelyn 26–29 Dec 2026;
  Sahi River View 5–11 Jan 2027; Sri Ramanasramam 14–19 Jan 2027.
  Hard wording guard: "Do not ask to reserve 'the Ram Dass room'."
- Verification: path absent from every current tip; no equivalent contact pack in central.
- Class: `CURRENT_CANON` (execution artifact, still needed for booking).

## NK-004 — Varanasi working coordinates for 34 candidates that central leaves without a point

- Source: deleted path `research/active/VARANASI-GEO-DELIVERY-REPAIR-001/BRONS/GEO_AUDIT.jsonl`
  (42,212 B, 36 rows incl. sentinel), recovered from history; also `.../BRONS/SOURCES.jsonl`
  (42,564 B, 86 rows incl. sentinel, source IDs `BRGEO-S001`…`BRGEO-S085`).
- Central state (frozen `a374236`):
  `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/DATASET_VARANASI_40.jsonl` has
  **`final_latitude: null` for 35 of 40 candidates** (`geo_status: GOOGLE_MAPS_MARKER_NOT_CONFIRMED`),
  and the delivered KML `VARANASI_40_KANDIDATEN.kml` falls back to the OLD inherited pins labelled
  `[ONBEVESTIGD]`, with `VNS-CAND-008` carrying **no point at all**
  (`[GEEN PUNT -- AFGEWEZEN COORDINAAT UITGESLOTEN]`).
- The recovered BRONS audit supplies independently cross-checked working points for
  `VNS-CAND-002` … `VNS-CAND-035` with per-candidate `geo_status`
  (`VERIFIED_SITE_CENTRE` / `WORKING_CROSSCHECKED_MAP_POINT` / `APPROXIMATE_LOCAL_POINT`),
  `point_type`, nearby-anchor checks and an explicit residual-uncertainty sentence each.
- Materially different from the central `[ONBEVESTIGD]` fallback pins (examples):
  - `VNS-CAND-008` Yogoda Satsanga Dhyana Mandali — central has NO point;
    recovered `25.303204, 82.976039` `APPROXIMATE_LOCAL_POINT`, ~250 m radius, derived from the
    B-38/9 Raghunath Nagar address, explicitly NOT the Mark-rejected `25.3045, 82.979369`.
  - `VNS-CAND-013` Kaal Bhairav — central pin `25.3223, 83.009`;
    recovered `25.3176834, 83.010746` with the warning that multiple same-name temples exist and
    the principal Visheshwarganj shrine is the intended one (~520 m apart).
  - `VNS-CAND-023` Mrityunjay Mahadev — central `25.3291, 83.0056`;
    recovered `25.3221891, 83.0147241` (~1.1 km apart).
  - `VNS-CAND-025` Lahartara Kabir birthplace — central `25.304, 82.966`;
    recovered `25.31467, 82.96838` (~1.2 km apart).
  - `VNS-CAND-034` Saranganath — central `25.3833, 83.0225`;
    recovered `25.375, 83.0283` (~1.0 km apart), flagged as a ~400 m locality point that must NOT
    be treated as the temple entrance.
- `VNS-CAND-001` (Lahiri Mahasaya Samadhi / Satyalok) is recorded as `NOT_ESTABLISHED` /
  `UNRESOLVED_IDENTITY_SPLIT`: the candidate label conflates two distinct public records and must
  be split or clarified before a single endpoint is chosen. The inherited `25.3028, 83.0074` was
  explicitly not retained. Central keeps the label unsplit and still uses that pin in the KML.
- Verification: `git grep -l 82.976039` against central returns nothing; the 34 recovered
  coordinates do not appear in central.
- Class: `CURRENT_FACT_WITH_RECHECK_TRIGGER` for the coordinates (working points, not surveyed),
  `CONFLICT_NEEDS_RECONCILIATION` for `VNS-CAND-001`.

## NK-005 — GEO_CONFLICT: NKB Vrindavan Ashram coordinate

- Two branch-only registries disagree:
  - `runs/active/VRINDAVAN-KUMAON-CORRIDOR-001/GOUD/central_map_source.jsonl`
    (blob `8551908d8519`): `27.5674, 77.69215`
  - `runs/active/VARANASI-COMPLETE-001/GOUD/MASTER_A_B_GEO_REGISTRY_VERIFIED.jsonl`
    (blob `da7be7eb5257`): `27.5767, 77.6865`
- ~1.1 km apart. Both are branch-only; neither is reconciled in central.
- Class: `CONFLICT_NEEDS_RECONCILIATION`.

## NK-006 — legacy Kumaon `LOCATION_ID` 400–443 formal-status table

- Source: branch-only `runs/active/KUMAON-COMPLETE-001/GOUD/candidates.jsonl`, blob `28ec04c9cea0`.
- Complete legacy A/B/C `formal_status` per `LOCATION_ID`, plus station nodes 308–310.
  Not reproduced as a single table anywhere in central.
- Class: `HISTORICAL_PROVENANCE_ONLY` for the grades (superseded by Mark's current grading),
  `CURRENT_FACT_WITH_RECHECK_TRIGGER` for the ID↔place mapping.

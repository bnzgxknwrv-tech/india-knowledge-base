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
- **RECLASSIFIED after commit-message archaeology — DO NOT REVIVE.**
  This file was not lost; it was **deliberately reverted** by INDIA:
  - `7fddaf9e78ae4976685207a9f187476f44b6d3de` (2026-08-23) "india10: add ready-to-use booking contact pack"
  - `b3a66b2649d1e6fd6d2f896c27966c9b40f686ed` (2026-08-23) "revert premature india10 booking contact pack" (-209 lines)
  - `341ecab2c34b10c42a855f0a16d0c78cd5eb0ae6`, `ba82d753b737e62d9b722bd0052523f1b104abd3` revert the accompanying status/state updates
  - `5bd2e865013cfd14336f4d04fbb9b693ba264629` "demote premature booking sequence to future planning artifact"
  Central `runs/active/INDIA10-BOOKING-SEQUENCE-CLOSURE-001/STATUS.md` records the reason verbatim:
  state `FUTURE_PLANNING_ARTIFACT__NOT_CURRENT_PROJECT_PHASE`; "Mark explicitly corrected that
  interpretation on 2026-08-23"; the surviving `BOOKING_ACTION_BOARD.md` "must not be used to imply
  that the India project has reached the booking/application phase"; "The action board's
  time-sensitive facts may be revalidated later ... Do not maintain them as globally current."
- Class: **`REJECTED_BY_MARK` / `SUPERSEDED`** → belongs in `SUPERSEDED_AND_DO_NOT_REVIVE.md`.
  The only durable atom worth carrying forward is the wording guard
  ("Do not ask to reserve 'the Ram Dass room'"), which is a communication rule independent of the
  premature booking phase, and the fact that a dated draft contact pack once existed and was
  reverted (so a successor does not "rediscover" it and re-trigger the same error).

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

## NK-007 — knowledge carried ONLY in commit messages (commit-message archaeology, TASK.md §2.4)

Surface: 1,779 commits across all refs, 1,771 unique subjects (all read), 179 commits with
message bodies >250 chars (178,718 chars, all read). Items below are recorded in a commit
message and are either absent from, or materially thinner in, the file tree.

- **Grading-system supersession chain, with dates and reasons.** `20db360a` (2026-07-11)
  fixed METHODOLOGY to `A+/A/B/C/R` per AI_RULES; `0d118b1d` (same day) records the Mark
  decision to **scrap `A+` and `R` entirely** — "A+ overbodig" because Mark knows his own top
  places — leaving `A/B/C/U`. `A+` was then reintroduced in the INDIA10 generation with a new
  meaning (cluster-carrier), and `A*` added later still. A successor reading only current files
  cannot see that `A+` once existed, was deliberately abolished, and returned with a *different*
  definition. This is the single largest vocabulary-drift trap in the repository.
- **The three PRIORITY_GROUPS weighting rules** (`2ee59451`, 2026-07-12, Mark decision):
  (1) the strength of the PLACE outweighs the position of the PERSON — a small YSS centre
  (position 1) ranks below a great Krishna temple (position 13) that all of India visits;
  (2) position is a tie-breaker only at EQUAL place-strength — Krishna sits at 13 because Mark
  had little mental picture of him, not because he is worth less;
  (3) the index is NOT exhaustive — a powerful place outside the list must still be reported.
  Same commit: the AOAY check is mandatory in every cluster sweep and is the explicit
  **exception to the size rule** — for an AOAY place, size does not count; a tiny temple
  Yogananda actually stood in is a destination. A negative AOAY result must also be reported.
- **The PDF rule chain, in order**, each step with its triggering incident:
  `cadda76b` PDF is a one-time read document, never auto-rebuilt (Mark: it is read once and then
  thrown away — avoid token spend); `2c47cc33` after CCI rebuilt a PDF unasked for a small text
  fix — CCI may NEVER rebuild a PDF on its own initiative, always ask first, even for a
  correction; `b7bb9028` after a second unintended build — every task now carries explicit
  `PDF_STATUS: VERBODEN` or `PDF_GO: JA`, and `VERBODEN` is the default when the field is
  absent; "sweep klaar" never implies "build the PDF"; `93a90306` Mark cancels the Bodh Gaya V2
  PDF outright ("Geen pdf meer!!!") — `BODHGAYA_PDF_V2_CANCELLED_BY_MARK: JA`; only the PDF step
  is cancelled, all research and A/B/C survive.
- **The one-incident rule** (`17b92442`, 2026-08-08): a practical fix after ONE incident becomes
  permanent canon only after a second, independent occurrence — with the same-day retraction of
  poort T as its own precedent. Machine-checkable validators may be added immediately.
- **Poort T was canonised and retracted on the same day** (`58c4f642` then `7587889e`).
  `DELTA_REVIEW_2026-08-08.md` therefore exists without a canon basis; an
  `INGETROKKEN_CANONPOGING` note was deliberately left in ACTIVE_STATE.md so a later session
  would not be confused. A successor that finds the delta-review file must not re-canonise it.
- **Two withdrawn factual claims, with their corrections.** (a) `46fa5260`: the claim that
  Ramakrishna visited Bodh Gaya and meditated before the Buddha image is **WRONG** — direct
  recheck of the cited source shows he deliberately REFUSED to visit Gaya in 1868. The correct
  Ramakrishna link (his father Kshudiram's naming Gadadhar/Vishnu vision during the 1835 Gaya
  pilgrimage) was moved from candidate 046 to 051. (b) Same commit: Ram Dass's Goenka Vipassana
  course is January 1971, not "winter 1969-70", and the exact venue cannot be decided between
  074 (Samanvaya Ashram) and 061 (Burmese Vihara) — two courses ran back to back.
- **Genealogy error and its fix** (`e1c23178`): a delivered PDF called Sri Yukteswar "the teacher
  of Yogananda's teacher", which actually describes Lahiri Mahasaya. Correct line is
  Babaji -> Lahiri Mahasaya -> Sri Yukteswar -> Yogananda; Sri Yukteswar was Yogananda's own
  direct guru.
- **Version-number naming rule** (`6781ace7`, Mark decision): every versionable deliverable gets
  an incrementing version number at the START of the filename (`V1_`, `V2_`), never at the end,
  never reused.
- **Numbering-gap explanations** that prevent a successor from "fixing" a non-bug: `525ea75c`
  numbers 39–45 in the legacy `CLUSTER_LOCATIONS.md` are deliberately reserved for Bodh Gaya
  candidates; `9d91476a` the legacy `CLUSTER_LOCATIONS` 1–46 scheme and the never-applied
  `DECISION-0013` LOCATION_ID cluster blocks are **incompatible schemes from an earlier
  architecture and were deliberately NOT reused** when permanent number 079 was assigned;
  the "LOCATION_ID 400" for the Babaji cave was an unconfirmed guess and was not adopted.
- **Trip frame** (`12148a8e`, 2026-07-08): travel period 18 Dec 2026 – 21 Jan 2027 (34 days),
  flights booked; booking details deliberately kept OUT of the repository for privacy.
- **`17823f6d`**: `.claude/worktrees/` is git-ignored — ephemeral per-agent worktrees are not
  project content. (Relevant to any successor auditing untracked files.)

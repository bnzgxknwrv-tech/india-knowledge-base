# STATUS — INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001

task_id: INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001
state: PARTIAL_COMPLETE__CURRENT_INPUTS_EXHAUSTED__Z1_Z4_COMPLETE__OTHER_FEEDS_ADDITIVE
branch: agent/indiazilver-cluster-completeness-audit
updated_at: 2026-08-20
blocked: NO

## Staged result

The former missing-canon blocker is obsolete. `CENTRAL_INPUT_MANIFEST.md`, `TURQUOISE_ENTITY_FEED.md`, current TASK/STATUS, the 31-candidate ZILVER seed, the available GEEL feed, authorized TURQUOISE reconciliation maps and protected regional canon sources were integrated.

Z1 through Z4 are complete for all inputs currently available. Future ROOD/BLAUW/WIT or central feeds are additive only and are not blockers.

## Z1 — protected canon recovered

- Reconstructed global immutable permanent IDs `001` through `081` from the authoritative regional numbering/decision records.
- Recovered protected A/B/C and lock/provisional states without changing any of them.
- Varanasi `001-040`: 32 A / 5 B / 3 C exactly as already decided by Mark; `041-045` remain permanent provisional records without A/B/C.
- Bodh Gaya `046-078`: existing A/B/C, excluded/reserved and sublocation states preserved; `051`, `061`, `074` retain their explicitly reconfirmed C decisions.
- Kumaon `079-081`: A / LOCKED_BY_MARK preserved; coordinates remain open.
- Legacy Kumaon keys are explicitly separated from the global permanent-ID sequence so old local numbers cannot be reused as global IDs.
- `VNS-HOTEL-001` remains a separate LOCKED_BY_MARK accommodation record, not a candidate ID.

## Z2 — NEW_ID_REQUIRED staging

- Prior 31-candidate seed preserved.
- Current GEEL R1-R3 entities integrated append-only.
- TURQUOISE same-site / parent-child / successor / ambiguous-merge rules applied.
- No candidate received a definitive new permanent ID.
- R4/R5 findings remain explicit `DEPENDENCY_ENTITY_CLOSURE`; none were dropped.
- Candidate coordinate backfill added where defensible: trusted/reference coordinate status is now recorded for Rana Mahal Ghat, Sri Ramanasramam, Belur Math, Vivekananda Rock Memorial, Panki Hanuman Temple and Ranchi YSS. Reference-grade Panki/Ranchi points are deliberately not promoted to the hard proximity gate.

## Z3 — numeric proximity

Hard numeric calculations were made only where both endpoints met the coordinate-quality gate.

- Numeric pair calculations: **16**.
- Tight pairs: **7** total.
  - `<=1 km`: **4**.
  - additional `>1 km and <=3 km`: **3**.
- No coordinate was guessed.

New-candidate hard results:
- `OLD31-28` Rana Mahal Ghat ↔ permanent `019` Kedareshwar Temple / Kedar Ghat: **0.895 km**, `<=1 km`.
- `OLD31-28` Rana Mahal Ghat ↔ permanent `018` Sankatha Devi Temple: **1.285 km**, `<=3 km`.

Both existing endpoints are A, so these results create no B/C upgrade action and do not imply duplicate identity.

Baseline reference tight pairs include:
- `029` ↔ `031`: 0.620 km.
- `029` ↔ `033`: 0.165 km.
- `031` ↔ `033`: 0.642 km.
- `018` ↔ `019`: 2.166 km.
- Bodh Gaya `046` ↔ `047`: 1.224 km.

Explicit coordinate dependencies remain for Varanasi `008` (old coordinate rejected), `023` (~3 km source conflict), `025`/`028` (approximate-only), `041-045` (not geo-verified), and all other entities lacking a trustworthy point.

## Z4 — duplicate / parent / ABC staging

TURQUOISE rules are carried through losslessly:
- Kainchi Dham remains one existing parent; rock/room/Hanuman/bridge/Ram Dass room/river etc. remain child entities or dependencies.
- NKB Vrindavan remains one existing locked parent; office/courtyard/room/veranda/cremation/memorial layers remain distinct where required.
- Sri Ramanasramam, Dakshineswar and Cossipore duplicate parent representations are suppressed at parent-ID level while microsites remain separate.
- Banke Bihari Temple is one physical entity with multiple person links.
- Virupaksha Cave and Mango Tree Cave remain distinct.
- Ganga Mata historic hut and later dharamshala remain a temporal successor chain.
- Akbarpur historic birth/family site and 2001 memorial temple remain a temporal successor chain.
- Serampore and other TURQUOISE ambiguous merges remain unresolved; no forced merge.

Existing B/C records with old working-pin screening positions within 3 km of Rana Mahal are staged only as `POTENTIAL_REVIEW_FOR_UPGRADE_AFTER_COORD_CONFIRMATION`: `012` (B), `013` (B), `026` (C), `027` (C), `040` (C). These are screening signals, not hard <=1/3-km claims, because their own marker quality has not closed.

`002`, `009`, `004` and `011` are already A; their new person/event/identity material is enrichment or dedup review, not an upgrade queue. `044` is provisional without A/B/C and requires entity closure before any first A/B/C decision.

## Final output commits for this pass

- `PROTECTED_CANON_BASELINE.csv`: `befbe4dc199c934de86c6d76d82fa97f676b7e3d`
- `NEW_ID_REQUIRED_QUEUE.csv`: `7075f86b8d94822a978256d59df05b0001bfce9f`
- `PROXIMITY_1KM_3KM_MATRIX.csv`: `d03627f55fa89fad74b96d8d68596693a26b2025`
- `DUPLICATE_PARENT_CANDIDATES.md`: `73da2210051da5f78b866ccf0bb58f493e6ca17a`
- `ABC_REVIEW_AFTER_CLOSURE_QUEUE.md`: `d1dc8b6e2d495cec952af65e9c997b3593920f67`

## Hard-rule audit

- OLD_ID_CHANGED: NEE
- OLD_ABC_CHANGED: NEE
- OLD_LOCK_CHANGED: NEE
- DEFINITIVE_NEW_ID_ISSUED: NEE
- COORDINATE_GUESSED: NEE
- TURQUOISE_PARENT_CHILD_COLLAPSE: NEE
- SILENT_DROP: NEE
- WAITED_FOR_FUTURE_FEEDS: NEE
- CURRENT_INPUTS_EXHAUSTED: JA
- BLOCKED: NEE

## Remaining additive work

Later ROOD/BLAUW/WIT or central entity/coordinate feeds may be appended when explicitly routed. They do not invalidate this staged completion. New numeric proximity may be appended only where both endpoints pass the same trustworthy-coordinate gate.

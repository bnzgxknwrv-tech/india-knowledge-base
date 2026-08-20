# GLOBAL_ACCOUNTING — ALL_FINDINGS_LOCATION_MASTER

```
build_date: 2026-08-20
built_by: CCI
input_families: BLAUW (AOAY/Yogananda), ROOD (Core Kriya), GEEL (NKB/Ram Dass/Ramana/Ramakrishna),
  WIT (Anandamayi/heritage), TURQUOISE (relation overlay), ZILVER (canon/proximity/new-ID overlay)
input_commit_basis: HEAD of each family's own branch at build time (agent/indiablauw-trip-ops-prep,
  agent/indiarood-core-kriya-sweep, agent/indiageel-ramana-ramakrishna-sweep,
  agent/indiawit-master-travel-readiness, agent/indiaturquoise-allperson-overlap,
  agent/indiazilver-cluster-completeness-audit), fetched and read directly (not via secondhand
  central-branch summaries) to avoid the staleness trap found in round-1 QA.
```

## Accounting equation — CLOSES

```
TOTAL_SOURCE_ROWS = PHYSICAL_ENTITY_LINKED + EXPLICIT_DUPLICATE + NEGATIVE/NONPRESENCE + STILL_UNRESOLVED
            459    =        259            +         0          +          33         +      167
```

`259 = 246 (PHYSICAL_ENTITY_LINKED) + 13 (PHYSICAL_ENTITY_LINKED_TO_EXISTING_CANON, i.e. the subset
already carrying a permanent/legacy canon ID via the ZILVER overlay)`.

**`EXPLICIT_DUPLICATE = 0` is expected, not an error**: the four families are person-partitioned
(BLAUW=Yogananda, ROOD=Babaji/Lahiri/Sri Yukteswar, GEEL=NKB/Ram Dass/Ramana/Ramakrishna,
WIT=Anandamayi), so no two source rows in this build restate the identical underlying claim.
Cross-family *physical-site* overlap (e.g. Kainchi visited by both NKB and Ram Dass) is real and is
captured — but at the **entity-index level** via the TURQUOISE relation overlay (see below), not as
row-level duplication, because each person's visit to a shared site is itself a distinct, valid
source claim, not a restatement of another family's claim.

## By source family

| family | rows | note |
|---|---:|---|
| BLAUW_AOAY_YOGANANDA | 58 | AOAY/Yogananda closure layer (previously R4/R5 items), fully self-descriptive |
| ROOD_CORE_KRIYA | 178 | Babaji/Lahiri Mahasaya/Sri Yukteswar primary source-record layer (146 claims + 32 negative controls), per ROOD's own lossless `_meta` |
| ROOD_CORE_KRIYA_SPLIT | 58 | ROOD's own physical micro-site/successor splits, fully self-descriptive |
| GEEL_FOURPERSON | 126 | NKB/Ram Dass/Ramana/Ramakrishna closure entities, fully self-descriptive, each backlinked to source freeze record IDs |
| WIT_ANANDAMAYI_HERITAGE | 39 | Anandamayi/heritage closure entities — **representative promoted subset**, not the full underlying corpus (see Exceptions §1) |
| **TOTAL** | **459** | |

## By disposition

| disposition | rows |
|---|---:|
| PHYSICAL_ENTITY_LINKED (new, no existing canon ID) | 246 |
| PHYSICAL_ENTITY_LINKED_TO_EXISTING_CANON (matches 001-081 or a staged OLD31-candidate) | 13 |
| NEGATIVE/NONPRESENCE | 33 |
| STILL_UNRESOLVED (R4/R5) | 167 |

32 of the 33 negatives are ROOD's own explicit `negative_control` records (Core-Kriya claimant/
non-presence controls); 1 is BLAUW's AOAY `NEGATIVE_NOT_VISITED` Rishikesh record. WIT and GEEL
carry no additional negatives in their respective closure-entity layers.

## Entity index

`ALL_FINDINGS_ENTITY_INDEX.jsonl` — 459 unique `physical_entity_key` values, one row per key, each
with backlinked `master_row_id`s, `R_classes_seen`, `dispositions`, source families and (where
applicable) the linked existing permanent/legacy canon ID.

**Important scope caveat**: 459 unique keys is *not* the same claim as "459 unique physical places
in India." Each family's own closure work already assigned distinct temporary keys at the
resolution granularity that family chose (often already split to micro-site level, e.g. Kainchi has
10 separate keys for room/river/bridge/hut/etc.), so this key count is the correct unit for the
accounting equation above, but should not be read as a final GPS-place count — that requires the
proximity/new-ID staging ZILVER already performs on top of this layer (see below).

## TURQUOISE cross-family relation overlay

TURQUOISE's own `ENTITY_MERGE_MAP.jsonl` (20 rows) references an **older audit-ID scheme**
(`VNS-CAND-*`, `B11`, `ATL-SY-*`, etc.) that predates the closure-candidate-keys ROOD/GEEL/WIT
minted in this round. There is no automated ID join between the two. CCI performed a **manual,
documented semantic match** (by place name/context, not by ID lookup) for 16 of the 20 TURQUOISE
relations against this master's `physical_entity_key`s — all 16 found a match, tagging 68 entity-
index rows with their `turquoise_relations` and a human-readable `turquoise_group_label` (e.g. all
`LC-NKB-KAINCHI-*`/`LC-RD-KAINCHI-*` keys carry `TQ-ENT-002`, "Kainchi Dham parent complex +
microsites"). The remaining 4 TURQUOISE relations (`TQ-ENT-014/015/018/019`) describe claims that do
not yet have a corresponding closure-candidate-key in any of the four families' outputs and are
therefore not joinable at this time — not dropped, just not yet backed by a row in this master (see
Exceptions §5).

**This manual join is a transparency-flagged methodology choice, not an automated guarantee** —
an independent reviewer should be able to re-derive the same 16 matches from the same place names,
but it was not produced by a deterministic ID lookup and should be spot-checked before being
treated as load-bearing for a route decision.

## Canon / A-B-C / lock integrity

`ALL_FINDINGS_LOCATION_MASTER_V0.md`'s canon file, `PROTECTED_CANON_BASELINE.csv`
(`agent/indiazilver-cluster-completeness-audit`), was **read only, never written**, by this build's
own scripts — existing IDs 001-081, all A/B/C values and all locks are therefore unchanged by
construction, not merely by claim. 13 rows in this master link to an existing canon/legacy entry
(`002`, `004`, `009`, `011`, `044`, `079`, plus the `OLD31-13/14/21/22/28/29` staged-candidate keys
and `NKB_VRINDAVAN_EXISTING`) via the same explicit `SAME_AS_/NO_NEW_PARENT_ID__ENRICH_EXISTING`
mapping ZILVER itself already established — CCI did not invent any new canon linkage, only
propagated ZILVER's own stated mapping onto the corresponding master rows.

## Proximity

Proximity is intentionally **not** recomputed or merged row-by-row into this master. ZILVER's
`PROXIMITY_1KM_3KM_MATRIX.csv` (16 trustworthy numeric pairs, 7 tight bands, 0 guessed coordinates —
independently re-verified by CCI in round-1 QA) remains the single authoritative proximity source,
referenced here rather than duplicated, to avoid a second copy silently drifting out of sync with
ZILVER's own file as ZILVER continues its work.

---
Geschreven door: CCI.

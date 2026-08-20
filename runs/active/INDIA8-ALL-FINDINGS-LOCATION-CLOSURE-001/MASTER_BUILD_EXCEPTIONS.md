# MASTER_BUILD_EXCEPTIONS — ALL_FINDINGS_LOCATION_MASTER

```
build_date: 2026-08-20
built_by: CCI
```

Per the build task's own stop condition, this document names the concrete, irreducible gaps found
while assembling the row-level master — nothing below is a silent drop; every gap names exact
source-record IDs/files and a next action.

## 1. WIT/Anandamayi: 39 promoted rows vs. a much larger underlying corpus (largest remaining gap)

**What exists**: WIT's own `ANANDAMAYI_SOURCE_RECORDS.jsonl` (3 catalog-pointer rows) documents
three source layers in full:
- `EXTERNAL_UNION_156` — 156 named `L001`-`L156` records in
  `runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/EXTERNAL_UNION_INPUT.md`.
- `INDIA_SOURCE_FIRST_ADDITIONS` — 108 individually named claims (e.g. "Doonga, Dehradun",
  "Ratu Palace, Ranchi", "Belur Math"...) in
  `runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/INDIA_SOURCE_FIRST_SWEEP_ANANDAMAYI.md`.
- `CCI_084_RECONCILIATION` — 28 verification-status entries in
  `runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/RECONCILIATION_CCI_084.md`.

**What WIT actually promoted to row-level entity candidates**: 39 rows in
`ANANDAMAYI_ENTITY_CANDIDATES.jsonl` — a curated, representative subset (confirmed already in
round-1 CCI QA, which found the same 39-row representative-sample pattern).

**Why this master does not fabricate the remaining ~225 rows**: the 156 L-records and 108
source-first claims are named but not individually resolved (no R-class, no access status, no
physical-entity key) anywhere in WIT's own output. Inventing an R-class or entity key for them here
would be exactly the kind of unverified guess the whole project's governance forbids. They are
**not lost** — the two source files remain the authoritative, fully lossless list — but they are
not yet expanded into this master's row/disposition/accounting layer.

**Concrete next action**: a dedicated WIT (or CCI) pass that walks all 156 `L###` IDs and all 108
named source-first claims individually into the same schema used for the 39 already-promoted rows.
This is the single largest concrete step between "accounting closes for 459 rows" and "accounting
closes for the full known Anandamayi corpus."

## 2. ROOD: 146 of 178 "primary" source rows lack a propagated readable place name

**What exists**: ROOD's `CORE_KRIYA_SOURCE_RECORDS.jsonl` deliberately keeps its 178 rows as a
*closure index* referencing the original stable-ID records in three upstream freeze files
(`BABAJI_INDIAROOD_FREEZE.md`, `LAHIRI_MAHASAYA_INDIAROOD_FREEZE.md`,
`SRI_YUKTESWAR_INDIAROOD_FREEZE.md`) plus the delta-reconciliation matrix, by design ("Original
stable-ID records remain lossless by exact source path+ref+blob SHA and are not rewritten"). Each
row carries a temporary `id` (e.g. `IR-1`), a source-family code (`X1`-`X4`), an `r` (R-class) and
`a` (access code) — but only the 32 delta-tagged rows and the 58 physical-split rows carry a human-
readable label (`q`/`loc`) directly in ROOD's own file.

**Confirmed independently, not just asserted**: ZILVER's own downstream `NEW_ID_REQUIRED_QUEUE.csv`
hit the same wall — its `ROOD_BATCH` row for the 146 primary anchors is a single aggregate
placeholder ("All 146 primary anchors retained by exact temporary key... no definitive IDs"), not
146 individually named rows. This is a genuine pipeline gap between ROOD and every downstream
consumer so far, not something specific to this build.

**What this master does**: preserves all 146 rows individually (never collapsed into one placeholder
row, unlike ZILVER's own aggregate treatment), with correct `R_class`/`access_status`/disposition
and an explicit `notes` field pointing to the exact upstream file + blob SHA where the real label
lives, rather than guessing a place name from context.

**Concrete next action**: ROOD (or CCI, cross-referencing the three upstream freeze files by
original in-document order against the `X1`/`X2`/`X3` sequence) propagates the actual place name for
each of the 146 `IR-N`/`N-N` IDs into a labeled field, matching the quality already achieved for the
58 splits.

## 3. BLAUW: 58 rows are the AOAY closure/previously-unresolved layer, not the full 123-place atlas

Already flagged in round-2 QA as a scoping nuance; restated here as a build-time exception because
it directly affects this master's completeness claim. The wider AOAY corpus — the 123-place
`PLACE_ATLAS.jsonl`, the 1,359-row `RAW_OCCURRENCES.jsonl`, and the 114-record external Yogananda
union — are **not** row-expanded in this master. They are separately, durably committed CCI outputs
from earlier tasks (CCI_TASK 082/085/086) with their own established R-classes/dispositions in their
own files; this build did not re-ingest them because BLAUW's own task scope was specifically the
*closure* of previously-unresolved AOAY items, and re-deriving the full atlas here risked either
duplicating or silently drifting from that already-canonical prior work.

**Concrete next action**: a dedicated pass reconciling `PLACE_ATLAS.jsonl`'s 123 places against
BLAUW's 58 closure IDs (which ones are 1:1 successors of already-resolved atlas entries vs. genuinely
new) before claiming full AOAY accounting closure, not just closure of the "was unresolved" subset.

## 4. GEEL: 126 entity rows vs. 207 underlying person-freeze records

GEEL's 126 promoted entity candidates trace back to `source_record_ids` referencing the original
46 (NKB) + 55 (Ram Dass) + 51 (Ramana) + 55 (Ramakrishna) = 207 IndiaGEEL freeze records (all of
which CCI itself produced and fully read in CCI_TASK 094/095, durably committed on
`agent/indiageel-ramana-ramakrishna-sweep`). GEEL's closure task was to decompose the existing
44+80-row reconciliation crosswalks into genuine physical entities, not to re-emit all 207 original
atomic records as separate master rows — this is a smaller, bounded gap than #1/#2 since most of the
207 records are already represented (often several-to-one) within the 126 promoted entities, but a
full 1:1 audit against all 207 original IDs was not performed in this build.

**Concrete next action**: lower priority than #1/#2; a spot audit confirming every one of the 207
original IDs appears in at least one `source_record_ids` array across the 126 rows.

## 5. Four TURQUOISE relations without a joinable entity key yet

`TQ-ENT-014` (Serampore railway station, distinct from the ashram), `TQ-ENT-015` (Bhowanipur
disciple-house encounter zone), `TQ-ENT-018` (Delhi/Jonapur NKB Ashram) and `TQ-ENT-019` (unnamed
estate near Delhi) describe real claims from TURQUOISE's own relation map, but none of the four
families' closure outputs yet contains a `physical_entity_key` naming those exact sites. Not
dropped — TURQUOISE's own file remains the authoritative record — just not yet backed by a row in
this master.

## 6. TURQUOISE join method is manual/semantic, not automated ID lookup

Documented in `GLOBAL_ACCOUNTING.md` — flagged again here because it is the one place in this build
where CCI's own judgment (matching place names/context) substitutes for a deterministic ID join, and
should be spot-checked independently before being treated as load-bearing.

## 7. Proximity intentionally not merged into this master

See `GLOBAL_ACCOUNTING.md` — ZILVER's `PROXIMITY_1KM_3KM_MATRIX.csv` remains the single
authoritative proximity source, referenced rather than duplicated.

---
Geschreven door: CCI. Geen A/B/C, geen IDs gewijzigd, geen route, geen nieuwe persoonssweep.

# GLOBAL_ACCOUNTING — FULL-KNOWN-UNIVERSE COMPLETENESS CLOSURE

```
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-20
scope: Mark's asymmetric scope correction (2026-08-20) -- AOAY/Yogananda exhaustive,
       Anandamayi Ma travel-core + lossless corpus reference (not exhaustive)
```

## Headline equation

```
TOTAL_MASTER_ROWS (700) = PHYSICAL_ENTITY_LINKED (268)
                         + PHYSICAL_ENTITY_LINKED_TO_EXISTING_CANON (13)
                         + EXPLICIT_DUPLICATE (128)
                         + NEGATIVE/NONPRESENCE (80)
                         + STILL_UNRESOLVED (211)
268 + 13 + 128 + 80 + 211 = 700  -- closes exactly, no remainder.
```

`ALL_FINDINGS_ENTITY_INDEX.jsonl`: **575 unique physical_entity_key rows** (700 master rows
minus rows that share a key because multiple detectors/layers back-link the same physical
site -- BLAUW/atlas/external-114 overlap and the two new Anandamayi photo-closure rows both
being deliberately not counted as new entities).

## By source family (700 rows)

| source_family | rows | what it is |
|---|---|---|
| ROOD_CORE_KRIYA | 178 | Babaji/Lahiri/Sri Yukteswar primary source records, **now label-propagated** |
| GEEL_FOURPERSON | 126 | NKB/Ram Dass/Ramana/Ramakrishna base rows (unchanged from P0 build) |
| AOAY_PLACE_ATLAS_RECONCILIATION | 123 | full 123-place internal AOAY atlas vs BLAUW |
| AOAY_EXTERNAL_114_RECONCILIATION | 114 | full 114-record external 5-AI Yogananda union vs BLAUW+atlas |
| BLAUW_AOAY_YOGANANDA | 58 | original BLAUW AOAY/Yogananda closure (P0 build, unchanged) |
| ROOD_CORE_KRIYA_SPLIT | 58 | Core-Kriya sublocation splits, **now label-propagated** |
| WIT_ANANDAMAYI_HERITAGE | 39 | WIT's promoted Anandamayi entities (P0 build, unchanged -- travel-core) |
| WIT_ANANDAMAYI_PHOTO_LOCATION_CLOSURE | 2 | NEW: Bhowanipur + Serampore-station photo-event rows |
| GEEL_NKB_RAMDASS_TURQUOISE_CLOSURE | 2 | NEW: TQ-ENT-018/019 (Jonapur ashram, unnamed Delhi estate) |

## AOAY/Yogananda -- EXHAUSTIVE (per Mark's correction)

Three independently-built AOAY corpora are now fully reconciled against each other with no
physical entity counted twice:

1. **BLAUW's 58 closure rows** (base P0 build) -- the anchor layer.
2. **123-place internal PLACE_ATLAS** -- 37 EXPLICIT_DUPLICATE of BLAUW, 36 NEGATIVE/NONPRESENCE
   (non-India mentions, kept visible not dropped), 14 new PHYSICAL_ENTITY_LINKED, 36 new
   STILL_UNRESOLVED. = 123.
3. **114-record external 5-AI union** (frozen PR #24 file, blob `089b652e...`, byte-verified
   unchanged) -- 81 EXPLICIT_DUPLICATE of BLAUW, 10 EXPLICIT_DUPLICATE of the atlas reconciliation,
   9 NEGATIVE/NONPRESENCE from the union's own explicit A8 "foutieve associatie" section (forced
   negative regardless of incidental keyword overlap with a real site -- see bugfix note below),
   2 more NEGATIVE/NONPRESENCE caught elsewhere (#65 Sabarmati, #96 Gouden Tempel -- both already-
   flagged false associations), 6 new PHYSICAL_ENTITY_LINKED, 6 new STILL_UNRESOLVED. = 114.

**Bugfix applied during this pass**: the external-114 reconciler initially let coincidental
keyword overlap mark explicit "this did NOT happen" claims (Ranikhet, Ghurni, Taxila, Belur Math,
the Dehradun-Anandamayi non-visit, the cancelled first Kashmir trip) as `EXPLICIT_DUPLICATE` of an
unrelated real site. Fixed by forcing section-A8 rows to `NEGATIVE/NONPRESENCE` unconditionally
before any keyword match runs. Caught and fixed before merge, not after.

**AOAY total physical-place claims accounted**: 58 (BLAUW) + 123 (atlas) + 114 (external-114) =
295 source claims, all with an explicit disposition, closing into far fewer unique physical
entities once duplicates are collapsed (see entity index).

## ROOD Core-Kriya -- label propagation (P0-C)

All **146 primary anchors** (178 source records + 58 splits = 236 rows total) now carry a real,
human-readable place name, recovered by joining each closure ID back to its authoritative freeze
file:

- **LM-\*** (Lahiri Mahasaya, 46 records) and **SY-\*** (Sri Yukteswar, 56 records incl. `N-*`
  negatives) and their `NEG-LM-*` negatives: the freeze-file headings **already embed the ID**
  (`### LM-004 — Tijdelijke gezinsverblijven in Benares vóór 1839`) -- direct, unambiguous join.
- **IR-\*** (Babaji positives, 50 records) and **NEG-BABAJI-\*** (12 records): the freeze file
  numbers headings but does not embed the `IR-`/`NEG-BABAJI-` ID in the heading text itself.
  Verified empirically that document order matches ID order exactly (`IR-1` = heading "1.", `IR-25`
  = heading "25. Puja-kamer van V.T. Neelakantan, 9 Surammal Lane, Egmore", etc. -- spot-checked
  against the live file, not assumed) before using positional join.
- **ext-B\*** (14 delta-matrix temporary records): already carried a `q` claim-label field in
  `INDIAROOD_DELTA_MATRIX.jsonl`; used directly, no join needed.

**R-class/access/disposition were never touched** -- only `raw_place_name`/`normalized_claim_name`
were filled in and the placeholder "label not yet propagated" note replaced with the real
provenance note. 0/236 unmatched.

## Anandamayi Ma -- travel-core + lossless corpus reference (CORRECTED SCOPE)

Mark's 2026-08-20 scope correction: do **not** exhaustively expand and individually
travel-resolve all 292 known Anandamayi claims (156 external-union L-records + 108 source-first +
28 CCI084 verification entries). Instead:

- The **39 WIT-promoted entities** already in the P0-build master stay exactly as they were --
  these already include several of the strongest, most travel-relevant sites (Bhadaini Ashram
  Varanasi R1, Kankhal Ashram Haridwar R1, Vrindavan Ashram R1, Ranchi Ashram R1, Ratu Palace R1,
  Ramanasramam cross-person R1, Karar Ashram cross-person R5).
- **2 new rows** added directly from the bounded photo-location-closure subtask (below): the
  Bhowanipur first-meeting site and the Serampore-station sighting, both cross-linked to their
  already-resolved Yogananda-side BLAUW entities rather than counted as new physical entities.
- The **full 236-row expansion** (133 new L-record rows + 83 new source-first rows + 20 new
  CCI084 rows -- the remaining part of the 292-claim corpus not already represented by the 39
  WIT entities, 56 of which were confirmed already-covered by name/keyword match against the 39)
  is preserved losslessly, **each row already carrying its own computed disposition**
  (115 PHYSICAL_ENTITY_LINKED, 120 STILL_UNRESOLVED, 1 NEGATIVE/NONPRESENCE), in
  `ANANDAMAYI_FULL_CORPUS_REFERENCE.jsonl`. This file is committed alongside the master but its
  236 rows are **not** promoted into `ALL_FINDINGS_LOCATION_MASTER.jsonl` -- per Mark's explicit
  instruction not to spend heavy research effort resolving every minor Anandamayi house/address.
  Nothing is silently dropped: every one of the 292 claims has a documented, auditable
  disposition, just not all of them at "travel master row" status.
- **Trigger to promote further**: if a future cluster decision brings Kolkata/East or a
  Vrindavan/Braj-adjacent route into scope, or a cross-person overlap with another Top-11 person
  surfaces inside this reference file, the relevant rows can be promoted from
  `ANANDAMAYI_FULL_CORPUS_REFERENCE.jsonl` into the master without redoing any research.

## TURQUOISE relation-join closure (P0-D)

| relation | resolution |
|---|---|
| **TQ-ENT-014** Serampore railway station | RESOLVED -- linked to `BLAUW-AYC-SRC-018` (already R1/EXACT in the base master); also now backed by the new Anandamayi photo-closure row (event 3). Respects TURQUOISE's own guard `DO_NOT_MERGE_WITH_SERAMPORE_ASHRAM`. |
| **TQ-ENT-015** Bhowanipur disciple-house encounter zone | RESOLVED at neighbourhood level -- linked to `BLAUW-AYC-SRC-017` (R5, unchanged). Exact house/host address remains irreducibly unresolved: primary candidate source (Gurupriya Devi's diary) is a scanned image-PDF with no text layer (`BRON_GEBLOKKEERD`, OCR needed -- not a dead end, a concrete next step); the Sangha photo-archive image itself 404s. R5 is correct, not a gap. |
| **TQ-ENT-018** Delhi/Jonapur NKB Ashram | RESOLVED -- instantiated as a new master row from GEEL's own `RECONCILIATION_MATRIX.jsonl` row 18 (was missing from the P0 build's row-level output despite existing in GEEL's reconciliation). R4/STILL_UNRESOLVED, matching GEEL's own PLAUSIBLE (not CONFIRMED) verdict. |
| **TQ-ENT-019** Unnamed estate near Delhi | RESOLVED -- instantiated as a new master row from GEEL's `RECONCILIATION_MATRIX.jsonl` row 21. Kept as its own unnamed entity per TURQUOISE's explicit guard not to merge with Jonapur just because both are Delhi-region. |

All 4 previously-unjoined TURQUOISE relations are now closed with real master rows or an
explicit, source-cited irreducible reason -- none silently dropped.

## Canon integrity

No row in this build touches `PROTECTED_CANON_BASELINE.csv` or any existing 001-081/A-B-C/lock
ID. `PHYSICAL_ENTITY_LINKED_TO_EXISTING_CANON` (13 rows, unchanged from the P0 build) remain
read-only references to canon IDs, never rewrites.

# MASTER_BUILD_EXCEPTIONS — status after FULL-KNOWN-UNIVERSE COMPLETENESS CLOSURE

```
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-20
```

Status of the 7 exceptions named in the original P0 build, plus new items surfaced this pass.

## CLOSED this pass

1. **Anandamayi full-corpus expansion** -- CLOSED under corrected scope. Not exhaustively
   individually resolved (Mark's explicit instruction), but fully accounted: 292 known claims,
   56 already covered by the 39 WIT rows, 236 preserved with per-claim disposition in
   `ANANDAMAYI_FULL_CORPUS_REFERENCE.jsonl`, 2 promoted to master rows via the photo-location
   closure. Nothing silently dropped.
2. **AOAY/Yogananda full atlas + external-114 reconciliation** -- CLOSED. 123-place atlas and
   114-record external union both fully reconciled row-by-row against BLAUW's 58 and each other.
3. **ROOD primary label propagation (146 rows)** -- CLOSED. 236/236 ROOD rows (146 primary + 58
   splits + negatives... counts reconcile: 178 source records + 58 splits = 236) now carry real
   place labels, joined from the authoritative freeze files. 0 unmatched.
4. **TURQUOISE relation-join closure (4 relations)** -- CLOSED. TQ-ENT-014/015 linked to existing
   BLAUW entities; TQ-ENT-018/019 instantiated as new rows from GEEL's own reconciliation matrix.
5. **Anandamayi × Yogananda photo-location closure (addendum)** -- CLOSED. 3 distinct joint events
   identified and physically resolved as far as the consulted corpus allows (2 at R1, 1 at
   irreducible R5). See `PHOTO_LOCATION_CLOSURE.md`.

## STILL OPEN (genuine, named, not a stopping point)

6. **Bhowanipur exact house/host address** -- irreducible with currently consulted sources.
   Concrete next step: OCR Gurupriya Devi's *Mother As Revealed To Me* (retrieved but scanned,
   no text layer) or visually inspect `anandamayi.org/photos/118.jpg` (currently 404s) against
   garden vs. street decor to help confirm/refute whether the known Bholanath photo belongs to
   Bhowanipur or could instead be an unlabelled second Ranchi frame.
7. **211 STILL_UNRESOLVED rows remain R4/R5 across the full master** -- this is expected and
   correct, not a defect: these are claims where the underlying source material itself does not
   support tighter physical resolution (mention-only AOAY tokens, disputed Kumbha/Ellora/Ajanta
   presence, un-named Haidakhan-era devotee houses, etc.). Each carries its own reason in its
   `notes` field; none are unresolved due to CCI running out of budget on a resolvable claim.
8. **ROOD's own remaining primary-source-verification backlog** (11 items listed in ROOD's own
   `BABAJI_INDIAROOD_FREEZE.md` "PRIMAIRE-BRONCONTROLE DIE NOG NODIG IS" section, e.g. Lahiri
   Mahasaya's own diaries, Pandukholi cave ownership history, 1894 Kumbha maps) -- these are
   ROOD's own acknowledged research debt, unaffected by this label-propagation pass (labels were
   propagated without touching R-class/access, so this debt is unchanged, not newly introduced).
9. **GEEL's NKB-18 (Jonapur) internal source S9** was flagged by GEEL itself as "not
   independently rechecked within budget" -- carried through unchanged as R4/STILL_UNRESOLVED,
   not silently upgraded to CONFIRMED.

## Not attempted (explicitly out of scope per every task in this chain)

- No Mark A/B/C decisions.
- No route/hotel/transport/PDF work.
- No new permanent-ID assignment (`new_id_required` field left as-is from the P0 build).
- No broad new person-sweep beyond resolving/accounting the already-known source universe.

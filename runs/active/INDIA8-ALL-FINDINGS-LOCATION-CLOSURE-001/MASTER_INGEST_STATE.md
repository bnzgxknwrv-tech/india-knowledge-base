# MASTER INGEST STATE — 2026-08-20

state: IN_PROGRESS
coordinator: INDIA8
worker_limit: max 2 active streams

## FEEDS RECEIVED
- BLAUW AOAY/Yogananda: COMPLETE — central receipt `23d57b73e62c4f31d842175723aa9f1b6eb116d9`
- TURQUOISE entity overlap/parent-child/successor: COMPLETE — `f5f8a69ef4f2a19063a83e1efa140754ef3e4af8`
- GEEL four-person closure: COMPLETE — `b1f5b26de727ef735fc7edb4186f7ec07e36a2d5`
- WIT Anandamayi/heritage closure: COMPLETE — `3ef793a806bbb9b9bf28e0c34a0b3c90f3a8ac62`
- ROOD Core Kriya closure: COMPLETE — `78500534100cbb1187e0603685a3c141368291fd`
- ZILVER staged proximity/ID pass: CURRENT INPUTS EXHAUSTED — awaiting only additive WIT+ROOD ingest

## MASTER BUILD RULES
1. Every source claim gets an explicit source-record key and disposition.
2. No source claim may disappear due to deduplication, low confidence, unresolved identity, route deprioritization, or access uncertainty.
3. Parent complex and child microsites remain distinct physical entities where TURQUOISE says they are physically distinct.
4. Historic site and modern successor remain linked but not collapsed.
5. R1-R5 + access status copied from source closures; conflicting classifications remain flagged for central reconciliation, never silently overwritten.
6. Existing permanent IDs 001-081 preserved exactly. New entities remain NEW_ID_REQUIRED until central reconciliation + ZILVER staging complete.
7. Existing Mark A/B/C/locks preserved exactly. Potential review is annotation only.

## NEXT INGEST ORDER
A. Build source->entity ledger from BLAUW + ROOD + GEEL + WIT.
B. Apply TURQUOISE merge/parent-child/successor map.
C. Overlay existing permanent canon 001-081 and ZILVER new-ID queue.
D. Overlay proximity results and mark coordinate gaps.
E. Produce accounting equation: total source claims = mapped physical entities + proven duplicates + negatives/nonpresence + unresolved.
F. Only after accounting closes: derive complete decision-ready cluster slices.

## FIRST CLUSTER SLICES AFTER MASTER ACCOUNTING
1. Vrindavan / Braj
2. Prayagraj / Allahabad
3. Kumaon delta
4. Varanasi delta
5. Bodh Gaya delta
6. Tiruvannamalai / Arunachala full concrete candidate layer

No A/B/C request to Mark before the relevant slice is complete and unresolved claims remain visible.

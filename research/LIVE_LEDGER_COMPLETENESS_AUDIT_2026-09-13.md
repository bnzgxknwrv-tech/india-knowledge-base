# LIVE LEDGER COMPLETENESS AUDIT

Date: 2026-09-13
Status: **OPEN DEFECT / MUST CLEAR BEFORE V4**
Branch: `agent/india8-cluster-casting`

## Trigger

The first INDIA20 live derived ledger was built from sources heavily scoped to A+/A/A* coverage. The six Sep-13 Varanasi/Sarnath downgrades showed the failure mode directly: once they became B, they disappeared entirely instead of remaining in living memory.

Those six rows are now repaired, but a wider comparison against current decision material shows the same structural defect remains: **the live CSV is not yet a complete current-place memory across all grades/statuses.**

## Confirmed examples still missing from the live CSV

### Delhi current B reserve examples
Current decision material retains at least:
- Qutb Minar and its Monuments [B] [UNESCO WH];
- Hauz Khas Village [B];
- Humayun's Tomb [B] [UNESCO WH];
- Sunder Nursery [B];
- Garden of Five Senses [B];
- Lodhi Garden [B];
- Red Fort [B] [UNESCO WH].

Current OPEN Delhi examples also include Jama Masjid and the Vedic/Jyotish astrologer consultation interest.

These do not need route weight merely because they exist, but they must not disappear from the living place/status layer.

### Tiruvannamalai current B reserve examples
Current decision material retains:
- Mango Tree Cave [B only if natural];
- Pachaiamman Temple [B only if easy].

They are absent from the current live CSV.

### Current C / rejected knowledge
Many explicit C decisions remain in governance/decision history but are not materialized into the current live CSV. A `complete living ledger` must distinguish `C / current-trip reject` from `never existed / never classified` rather than simply omitting both.

## Consequence

Do not call `LIVE_DERIVED_PLACE_GRADE_LEDGER_2026-09-13.csv` mechanically complete yet.

Its current strengths:
- current A+/A/A* set largely materialized;
- recent B downgrades explicitly restored;
- new Serampore grades materialized;
- newly recovered OPEN classification gaps materialized.

Its current defect:
- historic/current B/C/OPEN decisions outside those recent repairs are not yet comprehensively materialized.

## Required repair before V4

Build a full current grade/status reconciliation from:
1. `governance/DECISION_LEDGER.jsonl` + later owning decisions;
2. `governance/CURRENT_DECISIONS_MASTER.md` filtered through newer truth;
3. cluster Mark-decision logs;
4. current OPEN/reopened classification audit outputs;
5. current live CSV.

For every durable physical candidate/status, produce one current row with stable historic ID/source ID where available and explicit current grade/status (`A+`, `A`, `A*`, `B`, `C`, `OPEN`, accommodation/special status, etc.).

No old grade may override a later Mark decision. No C/B/Open row receives schedule weight simply because it is retained in memory.

`LIVE_LEDGER_MECHANICALLY_COMPLETE = NO`
`V4_LEDGER_GATE = BLOCKED_UNTIL_FULL_GRADE_STATUS_RECONCILIATION`

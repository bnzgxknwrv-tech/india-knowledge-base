# FEED — INDIA WIT ANANDAMAYI / HERITAGE LOCATION CLOSURE

Date: 2026-08-20
Source branch: `agent/indiawit-master-travel-readiness`
Task: `INDIAWIT-ANANDAMAYI-HERITAGE-LOCATION-CLOSURE-001`
Source state: COMPLETE_WITH_GOVERNANCE_SCHEMA_BLOCKER
Central interpretation: CONTENT COMPLETE; SCHEMA ASSIGNMENT REMAINS REQUIRED.

## OUTPUT COMMITS
- ANANDAMAYI_SOURCE_RECORDS.jsonl — `cf5974bf69053e466e94a93433cd8282adbde7ba`
- ANANDAMAYI_ENTITY_CANDIDATES.jsonl — `1fd1ec3213466e3c440ea5143e0c6d6f91c2d971`
- ANANDAMAYI_R4_R5_CLOSURE.md — `e1d8f8422501fb9a579e7269dd8e81caf561587e`
- HERITAGE_STAY_ENTITY_MATRIX.md — `61d96b016786d9208c964661cdaa92f72f1e9621`
- CURRENT_ACCESS_BOOKABILITY.md — `c6933d04b1a93e50015bf5ecdec7b34d0cb7c187`
- STATUS — `aae890510c44cad584fabc3ffb671a93d1d902ab`

## HIGH-VALUE CLOSURES
- Kankhal: official Sangha identifies bungalow where Anandamayi Ma spent about her final two months; bedroom + kitchen preserved in Matri Smriti Museum. Historic bedroom is visitable heritage, NOT accommodation. Adjacent International Centre currently offers accommodation.
- Bhadaini, Varanasi: official organization currently publishes room-booking contact and separate local dharamshala contact. Existing Sahi River View Guesthouse lock remains unchanged; this creates a later Mark hotel/stay review candidate, not an automatic override.
- External Anandamayi union L001-L156 retained losslessly; source-first additions and CCI084 remain separately traceable; East/South findings retained despite current route deprioritization.

## GOVERNANCE BLOCKER RESOLUTION
The governance file DOES exist on central branch `agent/india8-cluster-casting` at:
`governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md`
It defines R1-R5 and access statuses. WIT correctly did not invent definitions when the file was absent on its own branch.

Central next action: propagate the canonical governance schema to WIT and require a schema-only classification pass over its already-closed entities. NO rediscovery/research rerun required unless classification exposes a true evidence gap.

## DOWNSTREAM
- Feed resolved physical entities and heritage candidates to ZILVER proximity/new-ID staging.
- Feed Anandamayi entities into central all-findings master using TURQUOISE merge/parent-child/successor rules.
- Preserve all unresolved R4/R5 candidates; no route-based deletion.

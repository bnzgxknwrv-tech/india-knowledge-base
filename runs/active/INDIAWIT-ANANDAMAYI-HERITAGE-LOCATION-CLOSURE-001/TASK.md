# INDIAWIT ANANDAMAYI + HERITAGE LOCATION CLOSURE

## DOEL
Maak Anandamayi Ma lossless fysiek resolveerbaar en sluit tegelijk alle heritage-stay/hotel/ashram-kamer claims die de reislogica kunnen veranderen.

## LEES
- runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/EXTERNAL_UNION_INPUT.md
- runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/INDIA_SOURCE_FIRST_SWEEP_ANANDAMAYI.md
- runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/RECONCILIATION_CCI_084.md
- eerdere INDIA WIT heritage-stay outputs
- governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md

## UITVOEREN
1. Maak lossless source-recordlijst van externe 156-union + source-first aanvullingen + CCI-reconciliatie; detector-duplicates traceerbaar houden.
2. Ontleed hosthuizen, dharamshalas, paleizen, sanatoria, scholen, tuinen, kamers, ashrams en guesthouses naar fysieke entities.
3. R1-R5 + huidige identiteit/access/bookability indien relevant.
4. Onderzoek alle R4/R5 verder, vooral active-route gebieden en locaties met meerdere Top-X-personen.
5. Heritage cross-person: Hotel Evelyn; Bhadaini Anandamayi ashram; Sri Ramanasramam stay; Taj Mahal Palace; Belur Math; Karar/Puri; iedere historische kamer/hotel/ashram-verblijfclaim uit WIT-output. Geen modern kamernummer verzinnen.
6. Oost-data volledig verwerken, ondanks geparkeerde route.

## OUTPUTS
- ANANDAMAYI_SOURCE_RECORDS.jsonl
- ANANDAMAYI_ENTITY_CANDIDATES.jsonl
- ANANDAMAYI_R4_R5_CLOSURE.md
- HERITAGE_STAY_ENTITY_MATRIX.md
- CURRENT_ACCESS_BOOKABILITY.md
- STATUS.md

## HARD
Geen A/B/C. Geen hotel override namens Mark. Geen IDs wijzigen. Geen silent drops. Commit alles op deze branch.
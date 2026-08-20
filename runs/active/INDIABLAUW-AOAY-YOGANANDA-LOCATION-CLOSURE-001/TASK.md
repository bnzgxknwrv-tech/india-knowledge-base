# INDIABLAUW AOAY / YOGANANDA LOCATION CLOSURE

## DOEL
Los alle AOAY/Yogananda locatieclaims op tot maximaal haalbare fysieke identiteit vóór nieuwe Mark A/B/C. AOAY is P0.

## LEES
- runs/active/AOAY-FULL-LOCATION-ATLAS-001/PLACE_ATLAS.jsonl
- runs/active/AOAY-FULL-LOCATION-ATLAS-001/RAW_OCCURRENCES.jsonl
- runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md
- runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md
- runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/WERKPAKKET_D_DEEPENING_CCI_086.md
- governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md

## UITVOEREN
1. Maak één lossless lijst van alle India AOAY/Yogananda persoonlijke locatieclaims en micro-sites. Geen relevantiefilter.
2. Splits samengestelde locaties naar afzonderlijke fysieke entities waar de scène dat rechtvaardigt.
3. Per record: AOAY hoofdstuk/scène, Yogananda persoonlijk aanwezig JA/NEE, historische naam, huidige naam, exact adres/coordinates indien bewijsbaar, R1-R5, access-status, bron, confidence.
4. Onderzoek alle R4/R5 gericht verder met actuele webbronnen. Moderne hotels/huizen/ashrams/scholen/zalencentra actief op opvolger/continuïteit zoeken.
5. Speciaal: Haridwar hfst4, Vrindavan hfst11, Keshabananda/Brindaban, Regent Hotel Bombay, Taj Mahal Hotel, Bhaduri/Pranabananda/private-house claims, Kashmir/Mysore/Bangalore micro-sites.
6. Geen record verwijderen omdat het niet meer bestaat: label R2 successor / verdwenen / exterior / landscape.

## OUTPUTS
- AOAY_YOGANANDA_SOURCE_RECORDS.jsonl
- AOAY_YOGANANDA_ENTITY_CANDIDATES.jsonl
- AOAY_YOGANANDA_R4_R5_CLOSURE.md
- AOAY_YOGANANDA_ACCESS_MATRIX.md
- STATUS.md

## HARD
Geen A/B/C. Geen bestaande IDs wijzigen. Geen route. Geen silent drops. Commit alles op deze branch. STATUS pas COMPLETE als accounting sluit tussen source records en entity/duplicate/unresolved mapping.
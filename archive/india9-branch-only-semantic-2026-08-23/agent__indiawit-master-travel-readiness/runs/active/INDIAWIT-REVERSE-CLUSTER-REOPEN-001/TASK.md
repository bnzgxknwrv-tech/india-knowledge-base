# INDIA WIT — REVERSE CLUSTER REOPEN AUDIT

STATUS: READY
OWNER: INDIA WIT
MODE: CROSS-BRANCH INTEGRATION / NO NEW PERSON DISCOVERY

## Doel
Voer de omgekeerde zoektocht uit: neem de nieuwste landelijke persoons-/overlaplagen als uitgangspunt en toets ELK eerder afgewerkt/gefreeze-d cluster op nieuwe locaties die sinds de oorspronkelijke A/B/C-ronde zijn opgedoken.

Dit is additief. Niets gaat automatisch AF.

## Verplichte bronlagen
Gebruik de voor WIT reeds toegestane afgeronde detector-/reconciliatie-/overlapbranches plus de bestaande cluster/candidate/A-B-C/numbering-registers op de hoofdwerkbranch. Neem ook decisions/REVERSE_DISCOVERY_REOPEN_RULE_2026-08-19.md als governance over zodra beschikbaar via de werkbranch.

## Werkpakketten
1. Maak CLOSED_CLUSTER_INVENTORY.md: alle clusters/regio's die eerder als reviewed/complete/frozen/AF zijn behandeld, met bestaande kandidaatcount, bestaande A/B/C-state en numbering-registry.
2. Maak REVERSE_NEW_LOCATION_DELTA.md: per bestaand cluster ALLE persoonslocaties uit de nieuwe landelijke laag die niet in de oorspronkelijke kandidatenlijst zaten. Classificeer EXACT_SITE / SAME_CITY / NEARBY / OUTSIDE_CLUSTER. Geen nieuw webonderzoek.
3. Maak PROXIMITY_AND_SYNERGY_REVIEW.md: markeer nieuwe locaties die dicht bij bestaande A/B/C, verblijf of dagroute liggen; multi-person sites; persoonsgebonden hotels/huizen/ashrams; combinaties die een bestaande B/C praktisch aantrekkelijker kunnen maken. Gebruik REVIEW_FOR_UPGRADE, nooit automatisch upgraden.
4. Maak ADDITIVE_ID_QUEUE.md: voor elke werkelijk nieuwe fysieke kandidaat het volgende vrije permanente nummer/ID volgens bestaande registers. Bestaande IDs nooit wijzigen/hergebruiken. Als feitelijke toekenning volgens governance nog Mark/CCI vereist: reserveer als NEXT_ID_PROPOSED en markeer write-gate duidelijk.
5. Maak REOPEN_DECISION_QUEUE.md: per cluster alleen de nieuwe kandidaatlocaties en bestaande B/C's die door nieuwe context herbeoordeling verdienen. Bundel voor Mark; geen tientallen losse vragen als één clusterbatch kan.
6. Maak ACCOMMODATION_SIGNIFICANCE.md: inventariseer alle nieuw zichtbare hotels/guesthouses/houses/ashrams waar Top-personen aantoonbaar verbleven en die potentieel als verblijf gebruikt kunnen worden. Geen hotelkeuze namens Mark; wel expliciet aangeven waar 'hier slapen' historische/personale betekenis toevoegt.
7. Maak ROUTE_IMPACT.md: welke bestaande voorlopige reis-/clusterlogica kan ADDITIEF veranderen door deze nieuwe vondsten? Benoem: extra halve dag/dag, cluster langer verblijf, omweg vervalt door nabijheid, B kan upgrade-kandidaat worden, accommodatiebasis kan verschuiven. Geen definitieve route/nachten kiezen.

## Harde regels
- Geen bestaande locatie verwijderen.
- Geen bestaande A/B/C automatisch verlagen of verhogen.
- Elke nieuwe fysieke kandidaat moet uiteindelijk eigen permanent ID + eigen Mark A/B/C krijgen.
- Exact same-site en multi-person overlap krijgen prominente markering.
- Een reeds AF cluster wordt `REVERSE_DISCOVERY_CURRENT: NEE` zodra er nieuwe kandidaten zijn totdat additieve review is afgerond.
- Geen nieuw persoonslocatieonderzoek/webresearch in deze taak.
- Geen PDF, merge of definitieve route.

## Output
Schrijf alle 7 outputs onder runs/active/INDIAWIT-REVERSE-CLUSTER-REOPEN-001/ en update STATUS.md. Commit alles op agent/indiawit-master-travel-readiness.

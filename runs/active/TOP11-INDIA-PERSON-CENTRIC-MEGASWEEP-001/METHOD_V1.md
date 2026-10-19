# METHOD_V1 — Top-11 India Person-Centric Megasweep

```
method_status: APPROVED_BY_INDIA_AFTER_PILOT_AND_SATURATION
approved_at: 2026-08-16
basis: CCI_TASK 080 / SATURATION_RESULT.md
scope: all remaining Top-11 persons, whole India
```

## Kern
De omgekeerde zoekrichting is vanaf nu een vaste orthogonale detectorlaag naast regio-sweeps en AOAY-sweeps:

1. REGIO -> alles wat daar belangrijk is.
2. PERSOON -> alle verifieerbare fysieke India-touchpoints van die persoon.
3. AOAY -> alle verifieerbare fysieke AOAY-locaties.

De pilot + saturation pass op Anandamayi Ma en Neem Karoli Baba valideerden de methode: de host-/gastheer-as vond zelfstandig nieuwe Bodh-Ashram-achtige plekken, waaronder 4 Church Lane/Allahabad voor NKB en Solan/Raja Durga Singh voor Anandamayi Ma.

## Harde methode per persoon
Werk één persoon volledig af en freeze vóór de volgende. Geen regio als zoekgrens. Bestaande regiokandidaten NIET gebruiken als discovery-checklist; repo-cross-check pas na freeze.

Verplicht doorlopen:

1. officiële/lineage-bronnen en primaire/biografische teksten;
2. geboorte, jeugd, opleiding, werk, woonplaatsen, ashrams, math/temples, retraites, meditatie, initiatie, lezingen, satsangs, ceremonies, ziekte/mahasamadhi/samadhi/relics waar choice-relevant;
3. grote levensfasen en reizen/itineraries chronologisch;
4. spelling-/naamvarianten;
5. hosts/gastheren, discipelen, secretarissen, beschermheren, vrienden, leerlingen, medewerkers en auteurs van memoires als zelfstandige zoekingangen;
6. expliciete zoekronde: waar was [persoon] TE GAST BIJ ANDEREN? huizen, landgoederen, ashrams van anderen, hotels/resthouses alleen bij betekenisvolle gebeurtenis;
7. secundaire verwijzingen terugvolgen tot concrete fysieke identiteit;
8. onderscheid tussen persoonlijk bezoek en later institutioneel eerbetoon;
9. per claim scheiden: `person_event_verified`, `physical_identity_verified`, `exact_sublocation_verified`;
10. negatieve/onzekere claims expliciet vastleggen.

`PERSON_SWEEP_SATURATED: JA` alleen wanneer alle zes saturation-punten uit TASK.md aantoonbaar zijn doorlopen. Dit betekent grondig binnen projectnorm, niet absolute historische alwetendheid.

## Output per persoon
- machine-leesbare atlasregels met tijdelijke `ATL-*` IDs;
- compact persoonsrapport;
- freeze vóór repo-cross-check;
- daarna vergelijking met bestaande repo:
  - FOUND_AND_ALREADY_KNOWN
  - FOUND_BUT_MISSING_FROM_REPO
  - REPO_ONLY_NOT_REFOUND
  - DUPLICATE_OR_SAME_PHYSICAL_SITE
  - PERSON_LINK_UPGRADE
  - REGION_MISS
  - NEW_REGION_SIGNAL
  - MARK_DECISION_CONFLICT alleen bij echt cruciaal nieuw bewijs tegen beschermd besluit.

## Overige 9 — uitvoeringsvolgorde
1. Mahavatar Babaji
2. Lahiri Mahasaya
3. Paramahansa Yogananda
4. Ram Dass
5. Sri Yukteswar
6. Hariharananda
7. Vivekananda
8. Ramakrishna
9. Ramana Maharshi

Anandamayi Ma en Neem Karoli Baba zijn reeds `PERSON_SWEEP_SATURATED: JA` door CCI_TASK 080 en worden niet opnieuw vanaf nul gedaan.

## Stopregels
- Geen A/B/C voorspellen namens Mark.
- Geen bestaande A/B/C wijzigen.
- Geen PDF.
- Geen route/hotelplanning.
- Geen permanente nieuwe locatie-ID enkel op basis van discovery; eerst identity/reconciliatie volgens canon.
- Bij blocker op één persoon: leg blocker vast en ga door naar volgende persoon als de blocker niet systeemwijd is.

## Doel van Fase 2
Na alle 9 personen moet er één landelijke Top-11-atlas bestaan waarmee iedere toekomstige/regio-keuze wordt gekruist. Pas daarna kunnen we eerlijk beoordelen welke regio’s nog echt ontbreken en welke nieuwe zware clusters bovenkomen.

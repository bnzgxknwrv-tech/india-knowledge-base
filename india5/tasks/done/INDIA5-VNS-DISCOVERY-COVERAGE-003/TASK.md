# TASK.md — INDIA5-VNS-DISCOVERY-COVERAGE-003

Bron: Mark, namens INDIA2, in de sessie op PR #23 (geen apart geposte PR-comment-envelop op
het moment van aanmaken; deze taak is direct als canoniek taakbestand vastgelegd op Marks
expliciete instructie). Vervolg op `INDIA5-ARCH-HARDEN-002` (architectuur klaar,
`ARCHITECTURE_READY_FOR_CONTENT_TASKS: YES`) en de vrijgave van de PRE-BRONS-architectuur
(commit `7210ca91ea056940ab95c0585219fb031b6984c5`).

## Doel

Voer een volledige discovery/coverage-audit uit voor Varanasi volgens INDIA5 -- bewijs of de
regio redelijk compleet is, en zoek actief naar dramatisch te missen A-locaties. Dit is de
eerste keer dat de nieuwe PRE-BRONS/detectorarchitectuur daadwerkelijk inhoudelijk wordt
gebruikt (niet alleen gebouwd/getest).

Dit is een BEGRENSDE audit (zoals eerder afgesproken:
`VARANASI_DISCOVERY_COVERAGE_AUDIT`), GEEN volledige herstart van de 40 bestaande GEO-records.

## Verplicht

1. Gebruik uitsluitend de nieuwe detectorarchitectuur (`india4/roles/PRE-BRONS.md`,
   `india4/registries/DETECTOR_LIBRARY.jsonl`, `india4/templates/PRE_BRONS_REGION_CONTENT_BRIEF_TEMPLATE.md`).
   De bibliotheek is nog leeg (geen ACTIVE detectoren) -- deze audit introduceert dus
   waarschijnlijk de eerste PROVISIONAL detector(en) (bv. AOAY, lineage, samadhi, levende
   traditie, historische huizen, yatra/sacrale geografie, lokale insider-bronnen -- zie eerdere
   overleg-comments 5159452058/5159476368 op PR #23 voor de volledige lijst aandachtsgebieden).
2. Doorloop PRE-BRONS eerst: schrijf `REGION_CONTENT_BRIEF.md`/`.json`, `PRE_BRONS_DETECTORS.jsonl`,
   `SOURCE_FAMILY_PLAN.jsonl` onder `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/PRE_BRONS/`
   (nieuwe submap). Valideer met `india4/scripts/validate_pre_brons_brief.py` vóórdat je verder
   gaat.
3. Toets de bestaande 40 kandidaten op `why_this_one`/`why_not_the_others`/levend-vs-monumentaal/
   beroemd-maar-leeg (puur signalerend -- zie punt "Verboden" hieronder).
4. Zoek actief naar niet-ontdekte high-value kandidaten binnen de eerder afgesproken
   verzadigingsdrempel (zie `india4/protocols/INDIA5-PROTOCOL.md`, sectie "Verzadigingsdrempel"):
   per detector minimaal twee zoekbenaderingen, minimaal twee bronfamilies, drie opeenvolgende
   materieel verschillende richtingen zonder nieuwe high-value lead als stopsignaal.
5. Rapporteer ALLE nieuwe kandidaten uitsluitend als PROVISIONAL, nooit als A/B/C -- dat blijft
   uitsluitend aan Mark. Elke nieuwe kandidaat krijgt een nieuw, vrij permanent nummer
   (`NUMBERING_REGISTRY.jsonl`, doorlopend na 040 -- nooit een bestaand nummer hergebruiken of
   wijzigen), en de volledige betekenis-eerst-flow (`why_this_one`, `why_not_the_others`,
   `meaning_evidence`, `living_or_monumental`, `mark_relevance_link`) vóór GEO.
6. Lever een expliciete conclusie: `DISCOVERY_SATURATED` / `NOT_YET_SATURATED` per gebruikte
   detector, en een `dramatic_miss_check`-antwoord (zie het PRE-BRONS-sjabloon).

## Verboden

- Geen wijziging aan de bestaande 40 kandidaatnummers, namen, clusters of GEO-status.
- Geen wijziging aan een bestaande A/B/C-keuze (`RUN.yaml protected_mark_decisions`,
  `DATASET_VARANASI_40.jsonl`).
- Geen wijziging aan het hotelbesluit (`ACCOMMODATION_REGISTER.jsonl`, `LOCKED_BY_MARK`).
- Geen wijziging aan `VARANASI_40_KANDIDATEN.kml`.
- Geen PDF bouwen, geen reisgids aanpassen.
- Geen enkele detector canoniek ACTIVE maken, fuseren of RETIRED zetten (uitsluitend PROVISIONAL
  gebruiken, promotie is aan INDIA2 na deze run, zie `india5/GOVERNANCE.md` sectie 3).
- Geen A/B/C-keuze voor een nieuwe kandidaat (uitsluitend PROVISIONAL + keuzehulp/advies).

## Rapportage

Uitsluitend een `RESULT.md` met: PRE-BRONS-bevindingen (gebruikte/geïntroduceerde detectoren,
bronfamilies), dekkingsstatus per detector en op sweepniveau, eventuele nieuwe PROVISIONAL
kandidaten (met volledige betekenis+GEO-velden, nieuw permanent nummer), bevindingen van de
toets op de bestaande 40 (puur signalerend, geen wijziging), en de saturatie-/dramatic-miss-
conclusie. Daarna uitsluitend een korte `CCI_RESULT_ENVELOPE`-PR-comment, geen lange comment.

## Vereiste stop

Na completion van DEZE taak: niet zelfstandig doorgaan naar een A/B/C-beoordelingsronde of een
volgende regio. Wacht op Marks/INDIA2's beoordeling van de bevindingen.

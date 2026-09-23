# PRE-BRONS REGION CONTENT BRIEF — verplichte structuur

Status: VERPLICHT vanaf 2026-08-02 (INDIA2-architectuurbesluit, PR #23). Elke regio-sweep
begint met een brief volgens deze structuur, geschreven door de PRE-BRONS-stap
(`india4/roles/PRE-BRONS.md`), vóórdat BRONS start.

Twee bestanden met identieke inhoud: `REGION_CONTENT_BRIEF.md` (mensleesbaar, deze structuur in
proza/lijsten) en `REGION_CONTENT_BRIEF.json` (machineleesbaar, dezelfde velden als sleutels).

## Verplichte velden

- `region` / `run_id`
- `area_definition` — gebiedsgrens, straal of functionele corridor, expliciet (geen "de
  omgeving van X" zonder getal of grens)
- `mark_known_interests` — Marks bekende interesses en A-criteria, met verwijzing naar de bron
  (eerdere besluiten, commits, gesprekken)
- `mark_known_anchors` — bekende ankers van Mark voor dit gebied (bv. al genoemde personen,
  plekken, tradities)
- `relevant_traditions` — tradities, lineages, personen, heilige landschappen en historische
  lagen die voor dit gebied relevant zijn, elk met een korte onderbouwing en bron
- `active_detectors_applied` — lijst van ACTIVE detectoren uit `DETECTOR_LIBRARY.jsonl` die de
  relevantietoets doorstonden voor dit gebied, met `detector_id` en reden van toepasselijkheid
- `provisional_detectors_introduced` — nieuwe detectoren die tijdens deze PRE-BRONS-ronde nodig
  bleken en PROVISIONAL zijn ingezet (verwijzing naar `PRE_BRONS_DETECTORS.jsonl`)
- `planned_source_families` — geplande bronfamilies per detector (verwijzing naar
  `SOURCE_FAMILY_PLAN.jsonl`)
- `known_risks_blind_spots` — bekende risico's en blinde vlekken van dit plan, expliciet benoemd
- `expected_candidate_categories` — categorieën die expliciet moeten worden afgedekt (bv. "alle
  hoofd-ghats", "alle relevante lineages van Mark's interesses", "alle ASI-monumenten binnen de
  straal")
- `saturation_and_stop_criteria` — de vooraf gedefinieerde verzadigings- en stopcriteria voor
  deze sweep (zie INDIA5-PROTOCOL.md, sectie verzadigingsdrempel), per detector en op
  sweep-niveau
- `dramatic_miss_check` — expliciet antwoord op de vraag: "welke dramatisch te missen A-locatie
  zou dit plan nog kunnen missen?" Nooit leeg of "geen" zonder toelichting.
- `written_at` / `written_by`

## Wanneer is de brief "intern consistent" (BRONS mag starten)?

- alle bovenstaande velden zijn ingevuld, geen `TODO`/leeg veld;
- geen twee detectoren spreken elkaar tegen zonder toelichting;
- elke geplande bronfamilie is gekoppeld aan minstens één detector;
- `dramatic_miss_check` bevat een concreet, beargumenteerd antwoord (niet alleen "geen").

## Wat de brief NIET bevat

- Geen GEO-coördinaten of Google Maps-markers (dat is BRONS).
- Geen A/B/C-toewijzing (dat is Mark, via ZILVER/GOUD).
- Geen vooraf vastgesteld aantal kandidaten.

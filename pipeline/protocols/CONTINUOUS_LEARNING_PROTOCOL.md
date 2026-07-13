# Continuous Learning Protocol v2.2

## Doel
Iedere tijdens een run gevonden fout wordt beoordeeld als mogelijke systeemles. De controller repareert de actuele run minimaal en bepaalt daarnaast of rolcontract, protocol, template, quality gate, methodologie of projectdata voor toekomstige runs moet worden verbeterd.

## Scheiding
Een actieve run blijft onder zijn gepinde versies werken.

- `RUN_REPAIR`: minimale traceerbare reparatie van de actuele run.
- `SYSTEM_LEARNING`: afzonderlijke wijziging voor toekomstige runs.

Een systeemverbetering verandert nooit stil een actieve run.

## Foutklassen
- `LOCAL_DATA_ERROR`
- `ROLE_INSTRUCTION_GAP`
- `PROTOCOL_GAP`
- `TEMPLATE_GAP`
- `VALIDATION_GAP`
- `METHODOLOGY_GAP`
- `PROJECT_DATA_GAP`

## Verplichte leerbeslissing
Per fout wordt vastgelegd:
- fout-ID, run-ID en fase;
- fout en risico;
- foutklasse;
- lokale reparatie;
- structurele verbetering;
- betrokken bestanden;
- beslissing `PATCH_NOW`, `DEFER_WITH_REASON` of `NO_SYSTEM_CHANGE`.

`NO_SYSTEM_CHANGE` mag alleen wanneer bestaande regels al ondubbelzinnig waren en de fout aantoonbaar eenmalig is.

## Automatische verbetering
Bij `PATCH_NOW` maakt de pipelinebeheerder zonder nieuwe opdracht een afzonderlijke systeemwijziging. Daarbij worden minimaal gecontroleerd:
- BRONS, ZILVER en GOUD;
- controllertransition;
- templates;
- quality gate;
- versiegevolgen.

## Communicatie aan Mark
Bij iedere reparatie- of startopdracht vermeldt de assistent:
- `ACTUELE REPARATIE:` wat de worker nu moet doen;
- `SYSTEEMLES:` wat uit de fout is geleerd;
- `STRUCTURELE VERBETERING:` wat blijvend in GitHub verandert;
- `ACTIEVE RUN:` of die verbetering op de huidige gepinde run geldt.

## Leerregister
Alle systeemlessen worden append-only geregistreerd in:

`pipeline/learning/LESSONS.jsonl`

## Verplichte referentiële validatie
Vóór iedere faseovergang controleert de controller:
- iedere `source_id` in `claims.jsonl` bestaat in `sources/registry.jsonl` of als unieke ID in `sources/rejected.jsonl`;
- source-ID’s zijn uniek over beide registers;
- een afgewezen bron zonder ID mag nergens als claimreferentie voorkomen;
- manifest- en handoffpaden bestaan;
- ieder ontdekt defect is volgens dit protocol geclassificeerd.

## Geen schijnleren
Een chatmelding als “ik onthoud dit” is geen systeemverbetering. Een les geldt pas als verwerkt wanneer zij in het leerregister staat en, bij `PATCH_NOW`, de structurele wijziging op GitHub is vastgelegd.

END_OF_ARTIFACT
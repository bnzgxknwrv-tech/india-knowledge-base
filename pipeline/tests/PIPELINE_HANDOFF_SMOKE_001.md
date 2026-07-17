# PIPELINE-HANDOFF-SMOKE-001

Status: TESTSPECIFICATIE — NOG NIET UITGEVOERD

## Doel

Bewijs vóór productieactivatie dat een nieuwe run veilig kan verlopen als:

`INDIA2 -> BRONS -> inline controller -> ZILVER -> inline controller -> GOUD -> Mark`

zonder normale tussenkomst van SUBREGIE INDIA of INDIA2 tussen de metalen.

## Testdata

Gebruik een afzonderlijke synthetische run met:

- drie kunstmatige kandidaten;
- één geldige kandidaat;
- één conflicterende alias;
- één negatieve-testclaim met ontbrekende source-ID;
- kleine bestanden met `END_OF_ARTIFACT`;
- geen langdurig extern onderzoek;
- geen wijziging van echte onderzoeksruns of registers.

## Test A — happy path

1. INDIA2 maakt een nieuwe run volgens `RUN_TEMPLATE_V3.md` v3.1.
2. BRONS voltooit en commit alle artifacts.
3. De BRONS-workerrol eindigt.
4. Dezelfde sessie neemt met een aparte claim de inline controllerrol aan.
5. ZILVER-context, state, events en NEXT_ACTION worden correct gepind.
6. De handoff meldt `NEXT_ROLE_READY: YES`.
7. ZILVER leest uitsluitend GitHub en voltooit dezelfde keten naar GOUD.
8. GOUD schrijft en commit `MARK_FINAL_REPORT.md`.
9. GOUD toont het volledige rapport rechtstreeks aan Mark.
10. Er waren exact drie inhoudelijke metaalchats.

## Test B — ontbrekende sentinel

Verwijder in de synthetische fixture één `END_OF_ARTIFACT`. De inline controller moet blokkeren, geen opvolgercontext maken, geen READY-state zetten en geen opvolgerprompt leveren.

## Test C — ongeldige source-ID

Laat één claim verwijzen naar een niet-bestaande source-ID. De transition moet blokkeren.

## Test D — state/event-desynchronisatie

Laat state en laatste event bewust verschillen. De controller schrijft `DESYNC_DETECTED` of `TRANSITION_BLOCKED` volgens het gepinde protocol en maakt geen opvolgercontext.

## Test E — stale geplakte handoff

Wijzig een niet-gepind veld in de geplakte tekst. De volgende rol moet de GitHub-state volgen en de geplakte afwijking negeren.

## Test F — write-scope

Probeer na de rolwissel een fase-output door de controller te laten wijzigen. Dit moet stoppen. Probeer de workerclaim als controllerclaim te hergebruiken. Dit moet stoppen.

## Test G — oud protocol

Gebruik een fixture zonder nieuwe `post_completion`-pins. BRONS en ZILVER moeten het oude proces volgen en mogen niet inline transitioneren.

## Test H — GOUD-rapportkwaliteit

Controleer dat het Markrapport zelfstandig leesbaar is en minimaal bevat:

- rechtstreeks eindantwoord;
- status en completioncommit;
- alle kandidaten en afwijzingen;
- route- en GEO-betekenis wanneer in scope;
- onzekerheden en bronstatus;
- technische eindcontrole;
- geschreven artifacts;
- ondubbelzinnige afsluiting.

## Acceptatiecriteria

Productieactivatie is alleen toegestaan wanneer alle tests slagen en:

- geen extra SUBREGIE- of INDIA2-chat tussen de metalen nodig was;
- geen opvolgercontext door een workerrol is geschreven;
- iedere transition een afzonderlijke claim en commit heeft;
- iedere volgende rol uitsluitend gepinde GitHub-context leest;
- `NEXT_ROLE_READY: YES` alleen na volledige readback verschijnt;
- GOUD rechtstreeks een volledig bruikbaar Markrapport levert;
- de actieve echte runs en `pipeline/NEXT_ACTION.yaml` niet zijn gewijzigd.

## Uitvoering en bewijs

Een uitvoerder schrijft na de test:

`pipeline/tests/results/PIPELINE_HANDOFF_SMOKE_001_RESULT.md`

met per test PASS/FAIL, commits, fixturepaden, gevonden afwijkingen en het uiteindelijke `PRODUCTION_READY: YES|NO`.

Totdat dat resultaat `PRODUCTION_READY: YES` bevat en de implementatie is gemerged, maakt INDIA2 geen nieuwe productierun met `CONTROLLED_MANUAL_INLINE_HANDOFF`.

END_OF_ARTIFACT
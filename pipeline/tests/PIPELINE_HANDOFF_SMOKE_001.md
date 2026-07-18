# PIPELINE-HANDOFF-SMOKE-001 v1.1

Status: TESTSPECIFICATIE — NOG NIET UITGEVOERD

## Doel

Bewijs vóór productieactivatie dat een nieuwe run veilig kan verlopen als:

`INDIA2 -> BRONS -> inline controller -> ZILVER -> inline controller -> GOUD -> Mark`

zonder normale tussenkomst van SUBREGIE INDIA of INDIA2 tussen de metalen.

## Testdata

Gebruik uitsluitend de synthetische fixture-run:

- `run_id: PIPELINE-HANDOFF-SMOKE-001`;
- `run_type: SYNTHETIC_TEST`;
- drie kunstmatige kandidaten;
- één geldige kandidaat;
- één conflicterende alias;
- één negatieve-testclaim met ontbrekende source-ID;
- kleine bestanden met `END_OF_ARTIFACT`;
- geen langdurig extern onderzoek;
- geen wijziging van echte onderzoeksruns, `knowledge/places/registry.jsonl`, `decisions/INDEX.yaml` of de actieve `pipeline/NEXT_ACTION.yaml`.

Maak testkopieën van canonieke registers onder de fixturemap. Alle integratietests schrijven uitsluitend naar die kopieën.

## Test A — happy path en claimsluiting

1. Maak de synthetische run volgens `RUN_TEMPLATE_V3.md` v3.1.1.
2. BRONS claimt met `claim_status: ACTIVE`.
3. BRONS voltooit en commit alle artifacts.
4. De BRONS-workerclaim wordt in dezelfde completioncommit `CLOSED` met dezelfde completioncommitreferentie.
5. De BRONS-workerrol eindigt.
6. Dezelfde sessie neemt met een aparte `ACTIVE` claim de inline controllerrol aan.
7. ZILVER-context, state, events en NEXT_ACTION worden correct gepind.
8. De controllerclaim wordt in dezelfde transitioncommit `CLOSED`.
9. De handoff meldt alleen daarna `NEXT_ROLE_READY: YES`.
10. ZILVER leest uitsluitend GitHub en voltooit dezelfde keten naar GOUD.
11. GOUD schrijft `CANONICAL_INTEGRATION_PROPOSAL.md` en `MARK_FINAL_REPORT.md`.
12. GOUD sluit zijn workerclaim in de completioncommit.
13. GOUD toont het volledige rapport rechtstreeks aan Mark.
14. Er waren exact drie inhoudelijke metaalchats.

## Test B — ontbrekende sentinel

Verwijder in de synthetische fixture één `END_OF_ARTIFACT`. De inline controller moet blokkeren, geen opvolgercontext maken, geen READY-state zetten en geen opvolgerprompt leveren.

## Test C — ongeldige source-ID

Laat één claim verwijzen naar een niet-bestaande source-ID. De transition moet blokkeren.

## Test D — state/event-desynchronisatie

Laat state en laatste event bewust verschillen. De controller schrijft `DESYNC_DETECTED` of `TRANSITION_BLOCKED` volgens het gepinde protocol en maakt geen opvolgercontext.

## Test E — stale geplakte handoff en stale NEXT_ACTION

1. Wijzig een niet-gepind veld in de geplakte tekst. De volgende rol moet de GitHub-state volgen en de geplakte afwijking negeren.
2. Laat een oude handoff naar ZILVER wijzen terwijl GitHub NEXT_ACTION al naar GOUD wijst. De ZILVER-chat moet stoppen en mag niet claimen.
3. Laat NEXT_ACTION een contextmanifest noemen met afwijkende hash. De worker moet stoppen.

## Test F — write-scope en ongesloten workerclaim

1. Probeer na de rolwissel een fase-output door de controller te laten wijzigen. Dit moet stoppen.
2. Probeer de workerclaim als controllerclaim te hergebruiken. Dit moet stoppen.
3. Laat de predecessor-workerclaim `ACTIVE` of zonder sluitingsvelden staan. De inline controller moet zichzelf blokkeren en geen transition starten.
4. Laat claimsluiting en completioncommit van elkaar verschillen. De transition moet blokkeren.

## Test G — oud protocol

Gebruik een fixture zonder nieuwe `post_completion`-pins. BRONS en ZILVER moeten het oude proces volgen en mogen niet inline transitioneren.

## Test H — GOUD-rapportkwaliteit

Controleer dat het Markrapport zelfstandig leesbaar is en minimaal bevat:

- rechtstreeks eindantwoord;
- status en completioncommit;
- alle kandidaten en afwijzingen;
- route- en GEO-betekenis wanneer in scope;
- onzekerheden en bronstatus;
- aanbevolen vervolgstap;
- canonieke integratiestatus;
- technische eindcontrole;
- geschreven artifacts;
- ondubbelzinnige afsluiting.

## Test I — chat-versus-commit-pariteit

Vergelijk de volledige gecommitte tekst van `MARK_FINAL_REPORT.md` met de rapporttekst die GOUD in de chat toont. Negeer uitsluitend het verplichte `GOUD ZEGT:`-voorvoegsel, het slotrouteringsblok en `/GOUD`. Iedere inhoudelijke toevoeging, weglating, inkorting of parafrase faalt de test.

## Test J — concurrerende sessies en claimrace

1. Start in de fixture een geldige inline controllerclaim.
2. Laat een tweede onafhankelijke sessie dezelfde transition proberen te claimen. Dit moet worden geweigerd omdat de eerste claim `ACTIVE` is.
3. Laat twee nieuwe metaalchats dezelfde READY-state tegelijk proberen te claimen. Exact één claim mag slagen; de andere stopt zonder writes.
4. Sluit de eerste claim en controleer dat een nieuwe claim alleen op de inmiddels actuele state kan worden genomen.

## Test K — transitioncommit-drift

1. Laat het contextmanifest een predecessorresultaatcommit pinnen die niet overeenkomt met de definitieve completioncommit. De transition moet blokkeren.
2. Laat een transitioncommit worden geschreven maar wijzig state of NEXT_ACTION daarna zonder overeenkomstig event. Finale readback moet `NEXT_ROLE_READY: NO` geven.
3. Laat de controllerclaim een ander transitioncommit noemen dan de actuele transitioncommit. De handoff mag niet worden vrijgegeven.

## Test L — deterministische canonieke integratie

Gebruik uitsluitend fixturekopieën van registry en decisions-index.

1. Pas een technische artifactpadwijziging en bestaande LOCATION_ID-koppeling toe. Dit moet slagen.
2. Probeer een bestaande formele A/B/C-status te wijzigen. Dit moet blokkeren.
3. Probeer een adviserend A/B/C toe te voegen. Dit moet blokkeren.
4. Probeer een nieuw decision-ID of nieuwe beslistekst te creëren. Dit moet blokkeren.
5. Laat `mark_decision_required: YES` ontstaan. De betreffende canonieke wijziging mag niet worden toegepast en het Markrapport moet het exacte beslispunt tonen.
6. Controleer syntax, unieke LOCATION_ID's, bestaande decision-ID's en finale readback.

## Test M — productiepoort

1. Probeer vóór een geldig resultaatbestand een echte `CONTROLLED_MANUAL_INLINE_HANDOFF`-run te creëren. Dit moet blokkeren.
2. Controleer dat uitsluitend de synthetische fixture `PIPELINE-HANDOFF-SMOKE-001` met `run_type: SYNTHETIC_TEST` vóór de productiepoort mag bestaan.
3. Schrijf een testresultaat met `PRODUCTION_READY: NO`; productieruncreatie blijft geblokkeerd.
4. Alleen een volledig resultaat met `PRODUCTION_READY: YES`, sentinel en gemergede implementatie mag de poort openen.

## Acceptatiecriteria

Productieactivatie is alleen toegestaan wanneer alle tests A–M slagen en:

- geen extra SUBREGIE- of INDIA2-chat tussen de metalen nodig was;
- geen opvolgercontext door een workerrol is geschreven;
- iedere workerclaim in de completioncommit is gesloten;
- iedere transition een afzonderlijke claim en commit heeft;
- iedere controllerclaim in de transitioncommit is gesloten;
- concurrerende claims correct worden geweigerd;
- iedere volgende rol uitsluitend gepinde GitHub-context leest;
- `NEXT_ROLE_READY: YES` alleen na volledige readback verschijnt;
- GOUD rechtstreeks een volledig bruikbaar en chat-identiek Markrapport levert;
- canonieke integratie geen nieuwe A/B/C of decision creëert;
- de actieve echte runs, echte registers en `pipeline/NEXT_ACTION.yaml` niet zijn gewijzigd.

## Uitvoering en bewijs

Een uitvoerder schrijft na de test:

`pipeline/tests/results/PIPELINE_HANDOFF_SMOKE_001_RESULT.md`

met per test PASS/FAIL, commits, fixturepaden, claim- en statebewijzen, gevonden afwijkingen en het uiteindelijke:

`PRODUCTION_READY: YES|NO`

Het resultaatbestand eindigt met `END_OF_ARTIFACT`.

Totdat dat resultaat `PRODUCTION_READY: YES` bevat en de implementatie is gemerged, maakt INDIA2 geen nieuwe productierun met `CONTROLLED_MANUAL_INLINE_HANDOFF`.

END_OF_ARTIFACT
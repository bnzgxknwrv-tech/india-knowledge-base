# Controller Transition Protocol v2.3.1

## 1. Doel

De controller maakt runs aan en verzorgt de overgang tussen voltooide fasen. BRONS, ZILVER en GOUD genereren nooit als worker het contextmanifest van hun opvolger.

De controller is een expliciet geactiveerde GitHub-capabele AI-sessie, Mark, de India-regisseur of — uitsluitend bij een gepinde nieuwe run — dezelfde sessie nadat de workerrol formeel is beëindigd en `INLINE_POST_PHASE_CONTROLLER` is gestart.

De controller doet geen inhoudelijk onderzoek en herschrijft geen rapporten. Voor iedere transition leest de controller ook `pipeline/protocols/CONTINUOUS_LEARNING_PROTOCOL.md`.

## 2. Runcreatie en productiepoort

Een nieuwe productierun met `operating_mode: CONTROLLED_MANUAL_INLINE_HANDOFF` mag alleen worden aangemaakt wanneer:

1. `pipeline/tests/results/PIPELINE_HANDOFF_SMOKE_001_RESULT.md` bestaat;
2. dat bestand volledig leesbaar is en eindigt met `END_OF_ARTIFACT`;
3. het exact `PRODUCTION_READY: YES` bevat;
4. de implementatie op `main` staat;
5. de nieuwe run alle vereiste v3.1.1-pins vóór de eerste claim vastlegt.

Uitsluitend de synthetische testfixture met `run_type: SYNTHETIC_TEST` en run-id `PIPELINE-HANDOFF-SMOKE-001` is vrijgesteld van punten 1–4. Deze uitzondering mag geen echte onderzoeksbestanden, registers of de actieve `pipeline/NEXT_ACTION.yaml` wijzigen.

Bij geldige runcreatie schrijft de controller:
- `run.yaml`;
- `state.yaml` met `READY_FOR_BRONS`;
- `events.jsonl` met `RUN_CREATED`;
- `scope.md`;
- uitsluitend een definitief uitvoerbaar `context/BRONS_CONTEXT.yaml`;
- een geldige `pipeline/NEXT_ACTION.yaml` volgens het voor de run gepinde schema.

`ZILVER_CONTEXT.yaml` en `GOUD_CONTEXT.yaml` bestaan nog niet. Een leeg, voorlopig of ongepind manifest is verboden.

## 3. Transition na BRONS

De controller mag alleen van `BRONS_COMPLETE` naar `READY_FOR_ZILVER` wanneer hij:
1. `BRONS/manifest.yaml`, `BRONS/COMPLETED` en `BRONS/handoff.yaml` volledig leest;
2. controleert dat alle verplichte artifacts bestaan;
3. alle `END_OF_ARTIFACT`-sentinels controleert;
4. controleert dat iedere claim naar bestaande, unieke source-ID's verwijst;
5. controleert dat manifest- en handoffpaden bestaan;
6. controleert dat state, events, manifest en COMPLETED dezelfde uitkomst tonen;
7. controleert dat de BRONS-workerclaim `CLOSED` is en dezelfde completioncommit noemt;
8. iedere fout classificeert volgens Continuous Learning;
9. de definitieve BRONS-resultaatcommit vaststelt;
10. `context/ZILVER_CONTEXT.yaml` genereert met die commit als `source_commit`;
11. required BRONS-bestanden en beschikbare hashes expliciet pint;
12. `state.yaml` op `READY_FOR_ZILVER` zet;
13. `CONTEXT_PREPARED` en `TRANSITIONED` appendt;
14. `pipeline/NEXT_ACTION.yaml` exact naar ZILVER bijwerkt;
15. de controllerclaim sluit;
16. de volledige transition commit en opnieuw leest.

## 4. Transition na ZILVER

Voor `ZILVER_COMPLETE -> READY_FOR_GOUD` geldt dezelfde procedure:
- valideer de volledige ZILVER-uitkomst;
- controleer dat de ZILVER-workerclaim `CLOSED` is;
- voer cross-register referentiële-integriteitscontrole uit;
- classificeer fouten;
- bepaal de definitieve ZILVER-resultaatcommit;
- genereer pas daarna `context/GOUD_CONTEXT.yaml`;
- pin vereiste ZILVER-artifacts en alleen expliciet benodigde BRONS-artifacts;
- update state, events en `pipeline/NEXT_ACTION.yaml`;
- sluit de controllerclaim;
- commit en voer volledige readback uit.

## 5. Inline activering

`INLINE_POST_PHASE_CONTROLLER` is alleen geldig wanneer:

1. `run.yaml`, context en `NEXT_ACTION.yaml` het gepinde `ROLE_HANDOFF_PROTOCOL.md` en deze modus toestaan;
2. de worker alle artifacts, completionstate en completionevent heeft geschreven en gecommit;
3. de workerclaim aantoonbaar `CLOSED` is en dezelfde completioncommit noemt;
4. de workerrol expliciet is beëindigd;
5. na die beëindiging geen fase-output meer wordt gewijzigd;
6. de sessie GitHub-read/write opnieuw test;
7. de sessie dit protocol en Continuous Learning opnieuw leest;
8. een afzonderlijke controllerclaim met `claim_status: ACTIVE` wordt geschreven;
9. de workerclaim niet als controllerclaim wordt hergebruikt.

Dezelfde sessie is dan een nieuwe beperkte controllerrol, niet een worker met verruimde rechten.

## 6. Controllerclaim

Voor iedere transition schrijft de controller vooraf een claim met:
- `transition`;
- `claimed_by`;
- `claimed_at`;
- `source_commit`;
- `expected_state`;
- `target_context_manifest`;
- `activation_mode: SEPARATE_CONTROLLER|INLINE_POST_PHASE_CONTROLLER`;
- `claim_status: ACTIVE`.

Alleen een claim met `claim_status: ACTIVE` blokkeert de overgang. Een gesloten predecessor-workerclaim blokkeert niet. Een ontbrekende of onduidelijk gesloten predecessorclaim blokkeert wel.

Claims verlopen niet automatisch. Override van een actieve claim vereist expliciete autorisatie en `CLAIM_OVERRIDDEN` met reden.

Bij een geslaagde transition wordt de controllerclaim in dezelfde transitioncommit gesloten met:
- `claim_status: CLOSED`;
- `claim_closed_at`;
- `transition_commit`.

## 7. Toegestane controllerwrites

De controller mag uitsluitend wijzigen:
- het contextmanifest van de volgende fase;
- `state.yaml`;
- `events.jsonl`;
- `pipeline/NEXT_ACTION.yaml`;
- een transition-validatierapport onder `transitions/`;
- een operationele next-role-handoff onder `transitions/` volgens het gepinde template.

Een noodzakelijke fase-outputreparatie gebeurt als afzonderlijke `RUN_REPAIR`, nooit stil binnen de transition.

## 8. Next-role-handoff

Na een geslaagde inline transition schrijft de controller een handoff volgens `pipeline/templates/NEXT_ROLE_HANDOFF_TEMPLATE.md` en rapporteert alleen `NEXT_ROLE_READY: YES` wanneer:

- de volgende READY-state aantoonbaar bestaat;
- state en events synchroon zijn;
- het opvolgercontextmanifest bestaat en de juiste commit en hashes pint;
- `NEXT_ACTION.yaml` exact overeenkomt;
- worker- en controllerclaims aantoonbaar `CLOSED` zijn;
- geen andere actieve claim bestaat;
- finale readback is geslaagd.

Bij iedere afwijking geldt `NEXT_ROLE_READY: NO` en wordt geen uitvoerbare opvolgerprompt geleverd.

## 9. Eventtypen

Minimaal ondersteund:
- `RUN_CREATED`;
- `CLAIMED`;
- `CLAIM_CLOSED`;
- `TRANSITION_CLAIMED`;
- `CONTEXT_PREPARED`;
- `TRANSITIONED`;
- `TRANSITION_BLOCKED`;
- `DESYNC_DETECTED`;
- `CLAIM_OVERRIDDEN`;
- `RUN_REPAIRED` of fasespecifieke reparatievariant.

## 10. Stopvoorwaarden

Stop zonder overgang wanneer:
- write-toegang ontbreekt;
- de verwachte state niet klopt;
- een actieve worker- of controllerclaim bestaat;
- de predecessor-workerclaim niet aantoonbaar `CLOSED` is;
- predecessor-output onvolledig of afgekapt is;
- manifest, COMPLETED, state of events elkaar tegenspreken;
- claim-sourceverwijzingen ongeldig of dubbel zijn;
- manifest- of handoffpaden niet bestaan;
- de resultaatcommit niet ondubbelzinnig kan worden vastgesteld;
- required files of hashes niet betrouwbaar kunnen worden gepind;
- inline control niet expliciet door de gepinde run is toegestaan;
- een productierun de rooktestpoort niet aantoonbaar passeert.

Schrijf dan `TRANSITION_BLOCKED`; maak het volgende contextmanifest niet uitvoerbaar, verander de run niet naar READY en lever geen volgende metaalopdracht.

## 11. Activatie

Afzonderlijke controller:

`Open pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md en pipeline/protocols/CONTINUOUS_LEARNING_PROTOCOL.md. Voer de aangewezen controllertransition uit, valideer de predecessor volledig, genereer het gepinde opvolgercontextmanifest en schrijf uitsluitend toegestane transitionbestanden.`

Inline controller:

`De workerrol is volledig beëindigd en de workerclaim is CLOSED. Herhaal GitHub-preflight, lees de gepinde controller- en handoffprotocollen opnieuw, schrijf een afzonderlijke ACTIVE controllerclaim en voer uitsluitend de door NEXT_ACTION toegestane transition uit. Sluit de controllerclaim in de transitioncommit en lever alleen bij geldige finale readback de next-role-handoff.`

END_OF_ARTIFACT
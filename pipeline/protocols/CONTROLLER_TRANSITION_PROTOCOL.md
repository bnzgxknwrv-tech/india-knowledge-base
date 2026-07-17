# Controller Transition Protocol v2.3.0

## 1. Doel

De controller maakt runs aan en verzorgt de overgang tussen voltooide fasen. BRONS, ZILVER en GOUD genereren nooit als worker het contextmanifest van hun opvolger.

De controller is een expliciet geactiveerde GitHub-capabele AI-sessie, Mark, de India-regisseur of — uitsluitend bij een gepinde nieuwe run — dezelfde sessie nadat de workerrol formeel is beëindigd en `INLINE_POST_PHASE_CONTROLLER` is gestart.

De controller doet geen inhoudelijk onderzoek en herschrijft geen rapporten. Voor iedere transition leest de controller ook `pipeline/protocols/CONTINUOUS_LEARNING_PROTOCOL.md`.

## 2. Runcreatie

Bij runcreatie schrijft de controller:
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
7. iedere fout classificeert volgens Continuous Learning;
8. de definitieve BRONS-resultaatcommit vaststelt;
9. `context/ZILVER_CONTEXT.yaml` genereert met die commit als `source_commit`;
10. required BRONS-bestanden en beschikbare hashes expliciet pint;
11. `state.yaml` op `READY_FOR_ZILVER` zet;
12. `CONTEXT_PREPARED` en `TRANSITIONED` appendt;
13. `pipeline/NEXT_ACTION.yaml` exact naar ZILVER bijwerkt;
14. de volledige transition commit en opnieuw leest.

## 4. Transition na ZILVER

Voor `ZILVER_COMPLETE -> READY_FOR_GOUD` geldt dezelfde procedure:
- valideer de volledige ZILVER-uitkomst;
- voer cross-register referentiële-integriteitscontrole uit;
- classificeer fouten;
- bepaal de definitieve ZILVER-resultaatcommit;
- genereer pas daarna `context/GOUD_CONTEXT.yaml`;
- pin vereiste ZILVER-artifacts en alleen expliciet benodigde BRONS-artifacts;
- update state, events en `pipeline/NEXT_ACTION.yaml`;
- commit en voer volledige readback uit.

## 5. Inline activering

`INLINE_POST_PHASE_CONTROLLER` is alleen geldig wanneer:

1. `run.yaml`, context en `NEXT_ACTION.yaml` het gepinde `ROLE_HANDOFF_PROTOCOL.md` en deze modus toestaan;
2. de worker alle artifacts, completionstate en completionevent heeft geschreven en gecommit;
3. de workerrol expliciet is beëindigd;
4. na die beëindiging geen fase-output meer wordt gewijzigd;
5. de sessie GitHub-read/write opnieuw test;
6. de sessie dit protocol en Continuous Learning opnieuw leest;
7. een afzonderlijke controllerclaim wordt geschreven;
8. de workerclaim niet als controllerclaim wordt hergebruikt.

Dezelfde sessie is dan een nieuwe beperkte controllerrol, niet een worker met verruimde rechten.

## 6. Controllerclaim

Voor iedere transition schrijft de controller vooraf een claim met:
- `transition`;
- `claimed_by`;
- `claimed_at`;
- `source_commit`;
- `expected_state`;
- `target_context_manifest`;
- `activation_mode: SEPARATE_CONTROLLER|INLINE_POST_PHASE_CONTROLLER`.

Een geldige bestaande worker- of controllerclaim blokkeert de overgang. Claims verlopen niet automatisch. Override vereist expliciete autorisatie en `CLAIM_OVERRIDDEN` met reden.

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
- geen geldige claim actief blijft;
- finale readback is geslaagd.

Bij iedere afwijking geldt `NEXT_ROLE_READY: NO` en wordt geen uitvoerbare opvolgerprompt geleverd.

## 9. Eventtypen

Minimaal ondersteund:
- `RUN_CREATED`;
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
- een geldige claim bestaat;
- predecessor-output onvolledig of afgekapt is;
- manifest, COMPLETED, state of events elkaar tegenspreken;
- claim-sourceverwijzingen ongeldig of dubbel zijn;
- manifest- of handoffpaden niet bestaan;
- de resultaatcommit niet ondubbelzinnig kan worden vastgesteld;
- required files of hashes niet betrouwbaar kunnen worden gepind;
- inline control niet expliciet door de gepinde run is toegestaan.

Schrijf dan `TRANSITION_BLOCKED`; maak het volgende contextmanifest niet uitvoerbaar, verander de run niet naar READY en lever geen volgende metaalopdracht.

## 11. Activatie

Afzonderlijke controller:

`Open pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md en pipeline/protocols/CONTINUOUS_LEARNING_PROTOCOL.md. Voer de aangewezen controllertransition uit, valideer de predecessor volledig, genereer het gepinde opvolgercontextmanifest en schrijf uitsluitend toegestane transitionbestanden.`

Inline controller:

`De workerrol is volledig beëindigd. Herhaal GitHub-preflight, lees de gepinde controller- en handoffprotocollen opnieuw, schrijf een afzonderlijke controllerclaim en voer uitsluitend de door NEXT_ACTION toegestane transition uit. Lever alleen bij geldige finale readback de next-role-handoff.`

END_OF_ARTIFACT
# Controller Transition Protocol v2.2

## 1. Doel

De controller maakt runs aan en verzorgt de overgang tussen voltooide fasen. BRONS, ZILVER en GOUD genereren nooit zelf het contextmanifest van hun opvolger.

De controller is een expliciet geactiveerde GitHub-capabele AI-sessie, Mark of de India-regisseur. De controller doet geen inhoudelijk onderzoek en herschrijft geen rapporten.

Voor iedere transition leest de controller ook `pipeline/protocols/CONTINUOUS_LEARNING_PROTOCOL.md`. Iedere aangetroffen fout wordt zowel lokaal afgehandeld als structureel beoordeeld voor toekomstige runs.

## 2. Runcreatie

Bij het aanmaken van een run schrijft de controller:
- `run.yaml`;
- `state.yaml` met `READY_FOR_BRONS`;
- `events.jsonl` met `RUN_CREATED`;
- `scope.md`;
- uitsluitend een definitief uitvoerbaar `context/BRONS_CONTEXT.yaml`.

`ZILVER_CONTEXT.yaml` en `GOUD_CONTEXT.yaml` bestaan op dit moment niet. Een leeg, voorlopig of ongepind manifest is verboden.

## 3. Transition na BRONS

De controller mag alleen overgaan van `BRONS_COMPLETE` naar `READY_FOR_ZILVER` wanneer hij:
1. `BRONS/manifest.yaml`, `BRONS/COMPLETED` en `BRONS/handoff.yaml` volledig leest;
2. controleert dat alle verplichte BRONS-artifacts bestaan;
3. alle `END_OF_ARTIFACT`-sentinels controleert;
4. controleert dat iedere claim naar bestaande, unieke source-ID’s in accepted of rejected registers verwijst;
5. controleert dat manifest- en handoffpaden bestaan;
6. controleert dat `state.yaml`, `events.jsonl`, manifest en COMPLETED dezelfde fase-uitkomst tonen;
7. iedere gevonden fout classificeert volgens het Continuous Learning Protocol;
8. de definitieve BRONS-resultaatcommit vaststelt;
9. `context/ZILVER_CONTEXT.yaml` genereert met die commit als `source_commit`;
10. alle vereiste BRONS-bestanden en beschikbare hashes expliciet opneemt;
11. `state.yaml` op `READY_FOR_ZILVER` zet;
12. één `CONTEXT_PREPARED`-event en één `TRANSITIONED`-event appendt;
13. de volledige overgang commit.

## 4. Transition na ZILVER

Dezelfde procedure geldt voor `ZILVER_COMPLETE -> READY_FOR_GOUD`:
- valideer de volledige ZILVER-uitkomst;
- voer cross-register referentiële-integriteitscontrole uit;
- classificeer en verwerk gevonden fouten;
- bepaal de definitieve ZILVER-resultaatcommit;
- genereer pas daarna `context/GOUD_CONTEXT.yaml`;
- pin alle vereiste ZILVER-artifacts en hashes;
- neem alleen expliciet benodigde BRONS-artifacts op voor verliescontrole;
- update state en eventlog;
- commit de overgang.

## 5. Controllerclaim

Voor iedere transition schrijft de controller vooraf in `state.yaml` een tijdelijke controllerclaim met:
- `transition`;
- `claimed_by`;
- `claimed_at`;
- `source_commit`;
- `expected_state`;
- `target_context_manifest`.

Een geldige bestaande worker- of controllerclaim blokkeert de overgang. Claims verlopen niet automatisch. Alleen Mark of een expliciet geactiveerde controller mag een claim overrulen via `CLAIM_OVERRIDDEN` met reden.

## 6. Toegestane controllerwrites

De controller mag uitsluitend wijzigen:
- het contextmanifest van de volgende fase;
- `state.yaml`;
- `events.jsonl`;
- optioneel een transition-validatierapport onder `transitions/`.

Een noodzakelijke fase-outputreparatie wordt als afzonderlijke expliciet geactiveerde `RUN_REPAIR` uitgevoerd, niet stil binnen de controllertransition.

De controller wijzigt geen onderzoeksconclusies, methodologie, projectwaarderingen of rolresultaten tijdens de transition.

## 7. Eventtypen

Minimaal ondersteund:
- `RUN_CREATED`;
- `TRANSITION_CLAIMED`;
- `CONTEXT_PREPARED`;
- `TRANSITIONED`;
- `TRANSITION_BLOCKED`;
- `DESYNC_DETECTED`;
- `CLAIM_OVERRIDDEN`;
- `RUN_REPAIRED` of fasespecifieke reparatievariant.

## 8. Stopvoorwaarden

Stop zonder overgang wanneer:
- write-toegang ontbreekt;
- de verwachte state niet klopt;
- een geldige bestaande claim bestaat;
- predecessor-output onvolledig of afgekapt is;
- manifest, COMPLETED, state of events elkaar tegenspreken;
- claim-sourceverwijzingen ongeldig of dubbel zijn;
- manifest- of handoffpaden niet bestaan;
- de predecessor-resultaatcommit niet ondubbelzinnig kan worden vastgesteld;
- required files of hashes niet betrouwbaar kunnen worden gepind.

Schrijf dan `TRANSITION_BLOCKED`; maak het volgende contextmanifest niet aan en verander de run niet naar READY voor de volgende rol. Classificeer tevens het defect volgens het Continuous Learning Protocol.

## 9. Activatie

`Open pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md en pipeline/protocols/CONTINUOUS_LEARNING_PROTOCOL.md. Voer de controllertransition uit voor run <run-id> van <BRONS_COMPLETE|ZILVER_COMPLETE> naar de volgende READY-state. Valideer de predecessor volledig, genereer het volgende gepinde contextmanifest, verwerk iedere systeemles en schrijf uitsluitend de toegestane transitionbestanden.`

END_OF_ARTIFACT
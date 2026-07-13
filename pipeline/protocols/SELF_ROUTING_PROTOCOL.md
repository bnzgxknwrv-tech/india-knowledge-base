# SELF_ROUTING_PROTOCOL v1.0

## 1. Doel

Dit protocol minimaliseert Marks handwerk tussen BRONS, ZILVER, GOUD, SUBREGIE INDIA en INDIA2. Iedere uitvoerder bepaalt zelf de juiste bestemming van zijn completion- of blockerbericht en geeft Mark exact één volgende handeling.

## 2. Verplichte bestemmingen

Iedere completion, blocker of connectorstop bevat exact één route:

- `VOOR_SUBREGIE_INDIA` — technische validatie, reparatie, transition, repinning, protocol- of workflowkwestie;
- `VOOR_VOLGEND_METAAL` — alleen wanneer de repository reeds aantoonbaar door controllerautomatisering in de juiste READY-state is gezet;
- `VOOR_INDIA2` — uitsluitend een door SUBREGIE INDIA technisch gevalideerd GOUD-regisseurspakket;
- `GEEN_VERVOLG` — alleen wanneer de run bewust is gestopt of gearchiveerd.

Een metaalworker routeert nooit rechtstreeks inhoudelijke eindoutput naar INDIA2. BRONS en ZILVER gaan standaard naar SUBREGIE INDIA. GOUD gaat standaard naar SUBREGIE INDIA voor eindvalidatie.

## 3. Verplicht slotblok

Ieder normaal workerbericht eindigt vóór de eigen afsluitmarkering met exact:

```text
ROUTERING: <VOOR_SUBREGIE_INDIA|VOOR_VOLGEND_METAAL|VOOR_INDIA2|GEEN_VERVOLG>
VOLGENDE ACTIE VOOR MARK: <één letterlijke handeling>
DOORSTUURTEKST: <volledig zelfstandig blok dat Mark zonder wijziging kan kopiëren, of GEEN>
```

Daarna volgt uitsluitend de rolafsluiting, bijvoorbeeld `/BRONS`, `/ZILVER`, `/GOUD` of `/SUBREGIE INDIA`.

## 4. Directe metaaloverdracht

`VOOR_VOLGEND_METAAL` is alleen geldig wanneer:

1. een GitHub Actions-controller of SUBREGIE INDIA de predecessor volledig heeft gevalideerd;
2. `state.yaml` reeds op de volgende READY-state staat;
3. state en events synchroon zijn;
4. het opvolgercontextmanifest bestaat en alle required-file hashes bevat;
5. geen geldige claim actief is.

Zonder deze vijf bewijzen gaat het bericht verplicht naar `VOOR_SUBREGIE_INDIA`.

## 5. Universele startopdracht

Wanneer de repository een geldig `NEXT_ACTION.yaml` bevat, hoeft Mark in een nieuwe GitHub-chat alleen te sturen:

```text
GitHub INDIA PIPELINE: voer de exact in pipeline/NEXT_ACTION.yaml aangewezen actie uit volgens pipeline/ENTRYPOINT.md. Geef na afloop uitsluitend het verplichte zelfrouterende slotbericht.
```

De worker leest zelf run-id, rol, expected state en contextmanifest uit `NEXT_ACTION.yaml`. Bij ontbrekende of tegenstrijdige gegevens stopt hij naar SUBREGIE INDIA.

## 6. Connectorstop

Wanneer GitHub-read of GitHub-write ontbreekt, is het volledige antwoord uitsluitend:

`MARK: IK MIS GITHUB CONNECTOR!`

Geen routeringsblok, uitleg of alternatieve uitvoering wordt toegevoegd.

## 7. Minimale MARK-lus

Zonder automatisering:

1. Mark activeert GitHub in één schone chat;
2. Mark plakt de universele startopdracht;
3. Mark kopieert alleen `DOORSTUURTEKST` naar de aangegeven bestemming;
4. Mark activeert GitHub in de volgende chat.

Met controllerautomatisering:

1. Mark activeert GitHub in één schone chat;
2. Mark plakt de universele startopdracht;
3. na completion valideert en transitioneert GitHub Actions;
4. Mark opent alleen de volgende metaalchat en gebruikt opnieuw dezelfde universele startopdracht.

## 8. Geen zelfinschakeling van connectors

Een worker kan de ChatGPT-GitHubconnector niet zelf in een andere chat activeren of tussen chats verplaatsen. Hij mag nooit beweren dit te hebben gedaan. Volledige automatisering vereist een externe orchestrator met eigen GitHub- en model-APItoegang; dat is een andere uitvoeringslaag dan de ChatGPT-connector.

END_OF_ARTIFACT
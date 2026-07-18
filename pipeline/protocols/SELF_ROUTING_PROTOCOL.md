# SELF_ROUTING_PROTOCOL v1.1.1

## 1. Doel

Dit protocol minimaliseert Marks handwerk tussen BRONS, ZILVER, GOUD, SUBREGIE INDIA en INDIA2. Iedere uitvoerder geeft exact één geldige volgende handeling.

Voor nieuwe gepinde inline-handoffruns is de normale keten:

`INDIA2 -> BRONS -> ZILVER -> GOUD -> Mark`

## 2. Verplichte bestemmingen

Iedere completion, blocker of connectorstop bevat exact één route:

- `VOOR_SUBREGIE_INDIA` — technische validatie, reparatie, desynchronisatie, repinning of een geblokkeerde transition;
- `VOOR_VOLGEND_METAAL` — alleen na een volledig geldige controllertransition naar de volgende READY-state;
- `VOOR_INDIA2` — uitsluitend bij een echte cross-run koerskeuze, een nieuw inhoudelijk regisseursbesluit of bij oude gepinde runs die dit vereisen;
- `VOOR_MARK` — geldig GOUD-eindrapport bij PASS of PARTIAL, inclusief eventueel exact één beslispunt;
- `GEEN_VERVOLG` — bewust gestopte of volledig gearchiveerde run.

BRONS en ZILVER routeerden onder oude protocollen standaard naar SUBREGIE INDIA. Onder een nieuwe, expliciet gepinde inline-handoffrun mogen zij na een geslaagde afzonderlijke controllerrol rechtstreeks `VOOR_VOLGEND_METAAL` leveren.

GOUD routeert bij een geldige gepinde `MARK_FINAL_REPORT`-modus rechtstreeks `VOOR_MARK`.

## 3. Verplicht slotblok

Ieder normaal worker- of controllerbericht eindigt vóór de rolafsluiting met:

```text
ROUTERING: <VOOR_SUBREGIE_INDIA|VOOR_VOLGEND_METAAL|VOOR_INDIA2|VOOR_MARK|GEEN_VERVOLG>
VOLGENDE ACTIE VOOR MARK: <één letterlijke handeling>
DOORSTUURTEKST: <volledig zelfstandig blok dat Mark zonder wijziging kan kopiëren, of GEEN>
```

Bij BRONS of ZILVER met geldige inline transition is `DOORSTUURTEKST` het volledige blok uit `NEXT_ROLE_HANDOFF_TEMPLATE.md`.

Bij GOUD naar Mark is `DOORSTUURTEKST: GEEN`, tenzij `MARK_DECISION_REQUIRED: YES`. In dat geval bevat het uitsluitend één zelfstandig beslisblok; het volledige Markrapport staat al in hetzelfde chatantwoord.

## 4. Directe metaaloverdracht

`VOOR_VOLGEND_METAAL` is alleen geldig wanneer:

1. een geldige controllerrol de predecessor volledig heeft gevalideerd;
2. de predecessor-workerclaim aantoonbaar `CLOSED` is;
3. `state.yaml` op de volgende READY-state staat;
4. state en events synchroon zijn;
5. het opvolgercontextmanifest bestaat en de vereiste hashes bevat;
6. `pipeline/NEXT_ACTION.yaml` exact naar de volgende rol wijst;
7. de controllerclaim aantoonbaar `CLOSED` is;
8. geen andere `ACTIVE` claim bestaat;
9. finale readback is geslaagd;
10. `NEXT_ROLE_READY: YES` is vastgesteld.

Zonder deze bewijzen gaat het bericht verplicht naar `VOOR_SUBREGIE_INDIA` en wordt geen volgende metaalopdracht geleverd.

## 5. GOUD rechtstreeks naar Mark

`VOOR_MARK` is alleen geldig wanneer:

1. GOUD-status `PASS` of `PARTIAL` is;
2. alle verplichte GOUD-artifacts bestaan;
3. `CANONICAL_INTEGRATION_PROPOSAL.md` volledig en gecommit is;
4. uitsluitend toegestane deterministische canonieke writes zijn toegepast of integratie `NOT_APPLICABLE`/`PENDING_MARK_DECISION` is;
5. `MARK_FINAL_REPORT.md` volledig en gecommit is;
6. de GOUD-workerclaim aantoonbaar `CLOSED` is;
7. state en events synchroon zijn;
8. finale readback is geslaagd;
9. de chatversie inhoudelijk overeenkomt met het gecommitte rapport.

Een geldige normale GOUD-oplevering vereist geen terugkeer naar INDIA2 of SUBREGIE INDIA. Wanneer een nieuw formeel besluit nodig is, krijgt Mark exact het beslispunt; de niet-toegestane canonieke wijziging blijft onuitgevoerd.

## 6. Universele startopdracht

Wanneer de repository een geldige `NEXT_ACTION.yaml` bevat:

```text
GitHub INDIA PIPELINE: voer de exact in pipeline/NEXT_ACTION.yaml aangewezen actie uit volgens pipeline/ENTRYPOINT.md. Geef na afloop uitsluitend het verplichte zelfrouterende slotbericht en, bij GOUD, het volledige gepinde Markrapport.
```

De worker leest run-id, rol, expected state, contextmanifest, post-completionmodus en eventuele canonieke-integratiemodus zelf uit GitHub. Bij ontbrekende of tegenstrijdige gegevens stopt hij.

## 7. Connectorstop

Wanneer GitHub-read of GitHub-write ontbreekt, is het volledige antwoord uitsluitend:

`MARK: IK MIS GITHUB CONNECTOR!`

## 8. Minimale Mark-lus

Voor nieuwe inline-handoffruns:

1. INDIA2 maakt de run en volledige BRONS-startopdracht;
2. Mark start één verse BRONS-chat;
3. Mark kopieert na geldige inline transition alleen het volledige ZILVER-overdrachtsblok naar een verse ZILVER-chat;
4. Mark kopieert daarna alleen het GOUD-overdrachtsblok naar een verse GOUD-chat;
5. GOUD levert het volledige eindrapport rechtstreeks aan Mark en integreert deterministische kennisbasiswijzigingen zonder normale INDIA2-eindredactie.

Er is geen normale INDIA2- of SUBREGIE-stap tussen de metalen.

## 9. Geen zelfinschakeling

Een worker kan geen connector of andere chat automatisch starten. Hij mag nooit beweren dit te hebben gedaan. Mark opent de twee opvolgerchats en plakt de volledig voorbereide handoff.

## 10. Compatibiliteit

Oude of niet-inline-gepinde runs blijven hun oude routingcontract volgen. Zij worden niet stil naar deze minimale keten gemigreerd.

END_OF_ARTIFACT
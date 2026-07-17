# INDIA2-BESLUIT — MINIMALE TUSSENREGIE BRONS → ZILVER → GOUD

Status: DEFINITIEF REVIEWBESLUIT OP VOORSTELBRANCH

## 1. Eindbesluit

`EINDBESLUIT: ACCEPT_WITH_CHANGES`

Marks gewenste lineaire keten is inhoudelijk en operationeel juist:

```text
INDIA2 maakt één BRONS-opdracht
          ↓
BRONS voert de volledige fase uit
          ↓
Mark kopieert één overdracht naar een verse ZILVER-chat
          ↓
ZILVER voert de volledige fase uit
          ↓
Mark kopieert één overdracht naar een verse GOUD-chat
          ↓
GOUD levert het volledige eindrapport rechtstreeks aan Mark
```

Deze keten kan veilig worden ingevoerd zonder n8n, Claude Code-workers of een externe runtime-orchestrator.

De huidige canonieke protocollen staan echter nog niet toe dat BRONS of ZILVER zelf het opvolgercontextmanifest schrijft of als worker de controllertransition uitvoert. De veilige oplossing is niet om die scheiding te verwijderen, maar om dezelfde ChatGPT-sessie na formele faseafsluiting expliciet van workerrol naar een afzonderlijke, beperkte controllerrol te laten wisselen.

Daarmee blijven twee rollen bestaan:

1. de worker voltooit uitsluitend BRONS of ZILVER;
2. de workerrol eindigt;
3. dezelfde GitHub-capabele sessie start daarna een expliciet geautoriseerde inline controllertransition;
4. de controller valideert de completion, maakt het opvolgercontextmanifest, synchroniseert state/events/NEXT_ACTION en levert de plakbare startopdracht voor het volgende metaal.

BRONS schrijft dus niet als BRONS het ZILVER-contextmanifest. ZILVER schrijft niet als ZILVER het GOUD-contextmanifest. Dezelfde chatsessie mag dit alleen daarna doen onder een expliciete controllerclaim en de bestaande controllerwrite-scope.

## 2. Canonieke bevoegdheidsanalyse

### 2.1 Huidige situatie

Volgens `pipeline/protocols/EXECUTION_PROTOCOL.md`:

- bestaat bij runcreatie alleen `BRONS_CONTEXT.yaml`;
- worden opvolgercontextmanifesten pas na predecessorvalidatie door een aparte controllertransition gemaakt;
- schrijft de worker nooit het contextmanifest van zijn opvolger;
- stopt BRONS na `BRONS_COMPLETE`;
- stopt ZILVER na `ZILVER_COMPLETE`.

Volgens `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`:

- is de controller een expliciet geactiveerde GitHub-capabele AI-sessie, Mark of de India-regisseur;
- valideert de controller de volledige predecessoroutput;
- bepaalt de controller de definitieve resultaatcommit;
- maakt uitsluitend de controller het volgende gepinde contextmanifest;
- wijzigt de controller geen onderzoeksinhoud.

Volgens `pipeline/protocols/SELF_ROUTING_PROTOCOL.md`:

- mag directe overdracht naar het volgende metaal alleen wanneer de repository al aantoonbaar in de juiste READY-state staat;
- moeten state/events synchroon zijn;
- moet het opvolgercontextmanifest bestaan en gepind zijn;
- mag geen geldige claim actief zijn.

### 2.2 Antwoord op de bevoegdheidsvragen

**Kan BRONS volgens de huidige bevoegdheden zelf BRONS → ZILVER transitioneren?**

`NEE.`

**Kan ZILVER volgens de huidige bevoegdheden zelf ZILVER → GOUD transitioneren?**

`NEE.`

**Kan dezelfde chatsessie dit na voltooiing veilig doen?**

`JA, MAAR ALLEEN NA EEN EXPLICIETE PROTOCOLWIJZIGING.`

De sessie moet dan aantoonbaar:

1. de workerrol beëindigen;
2. geen fase-output meer wijzigen;
3. opnieuw GitHub-read/write controleren;
4. de controllerprotocollen openen;
5. een afzonderlijke transitionclaim schrijven;
6. uitsluitend controllerwrites uitvoeren;
7. stoppen bij iedere controllerstopvoorwaarde;
8. pas na een geldige READY-state de volgende startopdracht leveren.

Dit heet in dit besluit:

`INLINE_POST_PHASE_CONTROLLER`

Dit is geen verruiming van de workerrechten. Het is een expliciete tweede rol in dezelfde sessie.

## 3. Beslismatrix

| Onderdeel | Besluit | Vereiste wijziging |
|---|---|---|
| Drie verse metaalchats | ACCEPT | BRONS, ZILVER en GOUD blijven aparte chats en rollen. |
| GitHub als enige duurzame waarheid | ACCEPT | Geen onderzoeksinhoud via geplakte predecessorrapporten overdragen. |
| Mark kopieert één handoff per overgang | ACCEPT | Handoff bevat alleen bediening, identificatie, gates en GitHub-pointers. |
| BRONS schrijft zelfstandig ZILVER-context | REJECT | Alleen controllerrol mag context genereren. |
| ZILVER schrijft zelfstandig GOUD-context | REJECT | Alleen controllerrol mag context genereren. |
| Zelfde sessie voert na completion transition uit | ACCEPT_WITH_CHANGES | Workerrol formeel sluiten en daarna `INLINE_POST_PHASE_CONTROLLER` starten. |
| Verplichte terugkeer naar SUBREGIE na iedere fase | REJECT | Alleen bij blocker, repair, desync of niet-inline-geautoriseerde run. |
| INDIA2 na iedere fase | REJECT | INDIA2 alleen bij start, inhoudelijk beslispunt of echte blocker. |
| GOUD levert eindrapport rechtstreeks aan Mark | ACCEPT_WITH_CHANGES | Verplicht `MARK_FINAL_REPORT.md` plus volledige chatweergave/bruikbare link. |
| GOUD alleen technische completionnote | REJECT | Completion zonder volledig mensrapport is ongeldig. |
| n8n voor resterende sweeps | REJECT/DEFER | Niet implementeren voor huidige pipeline. |
| Claude Code als metaalworker | REJECT | BRONS/ZILVER/GOUD blijven door de gekozen ChatGPT/OpenAI-sessies uitgevoerd. |
| Externe heartbeat en pusharchitectuur | DEFER | Geen productievoorwaarde voor de handmatige drie-chatketen. |
| Deterministische truncatiecontrole | ACCEPT | Behouden als technische lees-/readbackregel. |
| Checkpoints en same-claim resume | ACCEPT | Behouden voor lange metaalfasen. |
| Prompt-injectiebescherming | ACCEPT | Behouden als algemene workerregel. |
| Seriële SHA-gecontroleerde writes | ACCEPT | Behouden. |
| Dubbele orchestratorstate buiten GitHub | REJECT | Geen tweede statebron. |
| Automatische adviserende A/B/C door metalen | REJECT | Alleen volgens bestaande inhoudelijke bevoegdheden; formeel uitsluitend Mark. |

## 4. Wat uit het n8n/Claude Code-plan vervalt

Voor de actuele India-pipeline worden niet geselecteerd:

- n8n als buitenste orchestrator;
- Claude Code als BRONS-, ZILVER-, GOUD- of controllerworker;
- server- of containerdeployment voor de onderzoeksketen;
- heartbeat-infrastructuur;
- autonome polling tussen rollen;
- kill-switcharchitectuur;
- provider-routing;
- pushnotificatie als completionvoorwaarde;
- een externe orchestratiestatus naast GitHub;
- GitHub App-splitsing uitsluitend voor deze circa resterende sweeps;
- non-interactieve modelruns als verplichte productie-uitvoerder.

PR #14 mag daarom niet als productiearchitectuur worden gemerged in de vorm van `ONE_SHOT_BZG_CONSENSUS_FINAL.md`.

De volgende onderdelen zijn wel algemeen bruikbaar en mogen in bestaande protocollen behouden of hergebruikt worden:

- GitHub als canonieke state- en overdrachtsbron;
- verse context per metaal;
- worker/controller-write-scheiding;
- claims en checkpoints;
- state/event-synchronisatie;
- SHA- en blobcontrole;
- sentinels en truncatiedetectie;
- prompt-injectiebescherming;
- maximaal drie retries bij aantoonbaar transiënte GitHub-fouten;
- geen onderzoek herhalen na een geldige checkpointresume.

## 5. Definitieve doelarchitectuur

```text
INDIA2
  maakt run, scope en volledige BRONS-startopdracht

BRONS-CHAT
  1. voert BRONS volledig uit
  2. sluit BRONS formeel af
  3. schakelt alleen indien vooraf toegestaan naar INLINE_POST_PHASE_CONTROLLER
  4. valideert BRONS technisch
  5. maakt/pint ZILVER_CONTEXT
  6. zet state/NEXT_ACTION op READY_FOR_ZILVER
  7. levert één plakbare ZILVER-startopdracht

ZILVER-CHAT
  1. leest GitHub opnieuw en vertrouwt niet op geplakte inhoud
  2. voert ZILVER volledig uit
  3. sluit ZILVER formeel af
  4. schakelt alleen indien vooraf toegestaan naar INLINE_POST_PHASE_CONTROLLER
  5. valideert ZILVER technisch
  6. maakt/pint GOUD_CONTEXT
  7. zet state/NEXT_ACTION op READY_FOR_GOUD
  8. levert één plakbare GOUD-startopdracht

GOUD-CHAT
  1. leest uitsluitend gepinde GOUD-context
  2. voert GOUD volledig uit
  3. schrijft alle finale artifacts
  4. schrijft MARK_FINAL_REPORT.md
  5. valideert completion en readback
  6. levert het volledige eindrapport rechtstreeks aan Mark
  7. routeert alleen bij een echte blocker terug naar INDIA2 of technische repair
```

## 6. Vereiste repositorywijzigingen

### 6.1 Bestaande bestanden aanpassen

1. `pipeline/protocols/EXECUTION_PROTOCOL.md`
   - voeg `INLINE_POST_PHASE_CONTROLLER` toe;
   - bevestig dat de workerrol eerst volledig eindigt;
   - verbied fase-outputwijzigingen na de rolwissel;
   - sta dezelfde sessie daarna als expliciete controller toe wanneer dit in `NEXT_ACTION.yaml` is geautoriseerd.

2. `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`
   - definieer inline activering;
   - verplicht nieuwe GitHub-preflight;
   - verplicht afzonderlijke transitionclaim;
   - verbied hergebruik van de workerclaim als controllerclaim;
   - verplicht volledige readback vanaf de definitieve fasecommit;
   - beperk writes tot contextmanifest, state, events, NEXT_ACTION en transitionvalidatierapport.

3. `pipeline/protocols/SELF_ROUTING_PROTOCOL.md`
   - erken een geslaagde inline controllertransition als geldige basis voor `VOOR_VOLGEND_METAAL`;
   - verbied een volgende startopdracht bij `NEXT_ROLE_READY: NO`;
   - laat GOUD bij geldige PASS/PARTIAL rechtstreeks `GEEN_VERVOLG` met volledig Markrapport leveren.

4. `pipeline/ENTRYPOINT.md`
   - ondersteun één expliciete `post_completion`-instructie uit `NEXT_ACTION.yaml`;
   - maak duidelijk dat dit twee opeenvolgende rollen zijn en geen gecombineerde workerbevoegdheid.

5. `pipeline/roles/BRONS.md`
   - voeg verplicht `NEXT_ROLE_HANDOFF` toe;
   - alleen uitvoeren nadat de inline controllertransition geldig is voltooid;
   - geen ZILVER-prompt bij blokkade.

6. `pipeline/roles/ZILVER.md`
   - voeg verplicht `NEXT_ROLE_HANDOFF` naar GOUD toe;
   - alleen na geldige inline controllertransition;
   - geen GOUD-prompt bij blokkade.

7. `pipeline/roles/GOUD.md`
   - wijzig de missie van “dossier voor SUBREGIE/INDIA2” naar “volledig gevalideerd dossier en rechtstreeks eindrapport voor Mark”;
   - voeg verplicht `MARK_FINAL_REPORT.md` toe;
   - behoud alle technische en inhoudelijke quality gates;
   - laat succesvolle GOUD-runs niet verplicht via INDIA2 lopen;
   - laat technische blockers naar repair/SUBREGIE en inhoudelijke beslisblockers naar INDIA2 routeren.

8. `pipeline/templates/RUN_TEMPLATE_V3.md`
   - voeg de nieuwe `post_completion`-velden toe;
   - pin het handoffprotocol en de templates;
   - leg vast dat oude runs zonder deze pin het oude proces blijven volgen.

### 6.2 Nieuwe minimale canonieke bestanden

1. `pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md`
2. `pipeline/templates/NEXT_ROLE_HANDOFF_TEMPLATE.md`
3. `pipeline/templates/MARK_FINAL_REPORT_TEMPLATE.md`

Twee aparte handofftemplatebestanden zijn niet nodig. Eén generiek, strikt template met `NEXT_ROLE: ZILVER|GOUD` voorkomt drift.

## 7. Vereiste NEXT_ACTION-uitbreiding

Voor BRONS en ZILVER:

```yaml
post_completion:
  mode: INLINE_POST_PHASE_CONTROLLER
  transition_protocol: pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md
  target_role: <ZILVER|GOUD>
  target_ready_state: <READY_FOR_ZILVER|READY_FOR_GOUD>
  emit_next_role_handoff: true
```

Voor GOUD:

```yaml
post_completion:
  mode: MARK_FINAL_REPORT
  report_template: pipeline/templates/MARK_FINAL_REPORT_TEMPLATE.md
  completion_destination: VOOR_MARK
```

Ontbreekt `post_completion`, dan geldt het oude protocol en routeert de worker naar SUBREGIE/controller.

## 8. Definitief protocol voor inline controllertransition

Een inline transition is uitsluitend geldig wanneer alle onderstaande stappen in volgorde slagen:

1. Worker schrijft alle fase-artifacts.
2. Worker opent alle verplichte artifacts opnieuw.
3. Worker controleert sentinels, manifest en COMPLETED.
4. Worker commit de fase volledig.
5. Worker schrijft de geldige COMPLETE-state en het completionevent.
6. Worker verklaart zijn rol beëindigd en voert geen fasewrites meer uit.
7. De sessie leest `CONTROLLER_TRANSITION_PROTOCOL.md` opnieuw.
8. De sessie voert opnieuw GitHub-read/write-preflight uit.
9. De sessie controleert dat `NEXT_ACTION.post_completion.mode` inline transition toestaat.
10. De sessie leest state, events, manifest, COMPLETED en handoff vanaf GitHub.
11. De sessie schrijft een afzonderlijke controllerclaim.
12. De controller valideert alle required artifacts, sentinels en referentiële integriteit.
13. De controller bepaalt de definitieve predecessor-resultaatcommit.
14. De controller maakt en pint het opvolgercontextmanifest.
15. De controller zet state en events synchroon op de volgende READY-state.
16. De controller werkt `pipeline/NEXT_ACTION.yaml` bij naar de volgende rol.
17. De controller commit de volledige transition.
18. De controller leest state, events, NEXT_ACTION en contextmanifest opnieuw.
19. Alleen bij volledige overeenstemming wordt `NEXT_ROLE_READY: YES` gerapporteerd.
20. Daarna wordt exact één plakbare startopdracht geleverd.

Bij iedere afwijking:

- schrijf `TRANSITION_BLOCKED` wanneer toegestaan;
- maak geen uitvoerbaar opvolgercontextmanifest;
- zet de run niet op READY;
- lever geen volgende metaalopdracht;
- routeer de blocker naar SUBREGIE INDIA of INDIA2 afhankelijk van het defect.

## 9. Definitief overdrachtstemplate BRONS → ZILVER

```text
RESULTAATSTATUS: <COMPLETED|PARTIAL|BLOCKED|FAILED>
RUN_ID: <run-id>
VOLTOOIDE_ROL: BRONS
FASE_COMPLETION_COMMIT: <sha|NONE>
TRANSITION_COMMIT: <sha|NONE>
NEXT_ROLE: ZILVER
NEXT_ROLE_READY: <YES|NO>
NEXT_EXPECTED_STATE: READY_FOR_ZILVER
NEXT_CONTEXT_MANIFEST: <pad|NONE>
HOOGSTE_BLOCKERS: <NONE|korte lijst>

ZILVER_STARTOPDRACHT_BEGIN
GitHub ZILVER:

Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR!

Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base.

Controleer dat pipeline/NEXT_ACTION.yaml exact verwijst naar:
- RUN_ID: <run-id>
- ROUTE: ZILVER
- EXPECTED_STATE: READY_FOR_ZILVER
- CONTEXT_MANIFEST: <pad>

Voer uitsluitend die ZILVER-actie uit. Lees uitsluitend het gepinde ZILVER-contextmanifest en de daarin genoemde required files. Haal de volledige gevalideerde BRONS-output uit GitHub; gebruik deze geplakte overdracht niet als onderzoeksbron.

Voer het volledige ZILVER-rolcontract uit, inclusief onafhankelijke broncontrole, aanvullend onderzoek, institutionele en fysieke-identiteitsverificatie, actuele bezoekbaarheidscontrole, relevante lineage/AOAY-controles, claimclassificatie, verliescontrole en controle van alle source-ID-verwijzingen.

Stop bij ontbrekende GitHub-write, geldige bestaande claim, state/event-desynchronisatie, ontbrekend of afgekapt required bestand, hashafwijking, ongeldige bronreferenties of een andere gepinde stopvoorwaarde.

Schrijf en commit de volledige ZILVER-fase. Wanneer NEXT_ACTION de modus INLINE_POST_PHASE_CONTROLLER expliciet toestaat, beëindig daarna de ZILVER-rol en voer als afzonderlijke controllerrol uitsluitend de geldige ZILVER → GOUD-transition uit. Lever alleen bij een volledig geldige READY_FOR_GOUD-state de complete GOUD-startopdracht.
ZILVER_STARTOPDRACHT_EINDE
```

Wanneer `NEXT_ROLE_READY: NO`, wordt het gehele startopdrachtblok vervangen door:

`ZILVER_STARTOPDRACHT: GEEN — EERST BLOCKER OPLOSSEN.`

## 10. Definitief overdrachtstemplate ZILVER → GOUD

```text
RESULTAATSTATUS: <COMPLETED|PARTIAL|BLOCKED|FAILED>
RUN_ID: <run-id>
VOLTOOIDE_ROL: ZILVER
FASE_COMPLETION_COMMIT: <sha|NONE>
TRANSITION_COMMIT: <sha|NONE>
NEXT_ROLE: GOUD
NEXT_ROLE_READY: <YES|NO>
NEXT_EXPECTED_STATE: READY_FOR_GOUD
NEXT_CONTEXT_MANIFEST: <pad|NONE>
HOOGSTE_BLOCKERS: <NONE|korte lijst>

GOUD_STARTOPDRACHT_BEGIN
GitHub GOUD:

Activeer in deze chat onmiddellijk de GitHub-connector en houd deze gedurende de volledige uitvoering beschikbaar. Dit onderzoek gebruikt GitHub als enige bron van waarheid en overdrachtskanaal. Test vóór ieder inhoudelijk werk zowel GitHub-read als GitHub-write voor repository bnzgxknwrv-tech/india-knowledge-base. Ontbreekt read of write, antwoord dan uitsluitend: MARK: IK MIS GITHUB CONNECTOR!

Open pipeline/ENTRYPOINT.md in repository bnzgxknwrv-tech/india-knowledge-base.

Controleer dat pipeline/NEXT_ACTION.yaml exact verwijst naar:
- RUN_ID: <run-id>
- ROUTE: GOUD
- EXPECTED_STATE: READY_FOR_GOUD
- CONTEXT_MANIFEST: <pad>

Voer uitsluitend die GOUD-actie uit. Lees uitsluitend het gepinde GOUD-contextmanifest en de daarin genoemde required files. Haal de volledige gevalideerde ZILVER-output uit GitHub; gebruik deze geplakte overdracht niet als onderzoeksbron.

Voer het volledige GOUD-rolcontract uit. Controleer synthese, claims, bronnen, source-ID's, fysieke identiteit, bevestigingsdomeinen, actuele bezoekbaarheid, conflicten, duplicaten, tellingen, permanente LOCATION_ID's, kaartdata, nabijheid en alle overige run-specifieke quality gates.

Stop bij ontbrekende GitHub-write, geldige bestaande claim, state/event-desynchronisatie, ontbrekend of afgekapt required bestand, hashafwijking, ongeldige bronreferenties of een andere gepinde stopvoorwaarde.

Schrijf en commit de volledige GOUD-fase. Maak verplicht het volledige MARK_FINAL_REPORT volgens het gepinde template. Lever dat rapport na finale GitHub-readback rechtstreeks en volledig aan Mark. Vraag bij een geldige PASS of PARTIAL niet om terugkeer naar INDIA2. Routeer alleen echte technische of inhoudelijke blockers.
GOUD_STARTOPDRACHT_EINDE
```

Wanneer `NEXT_ROLE_READY: NO`, wordt het gehele startopdrachtblok vervangen door:

`GOUD_STARTOPDRACHT: GEEN — EERST BLOCKER OPLOSSEN.`

## 11. Definitief GOUD-eindrapporttemplate voor Mark

Bestand:

`research/active/<RUN_ID>/GOUD/MARK_FINAL_REPORT.md`

```markdown
# <RUN_ID> — definitief rapport voor Mark

## 1. Eindantwoord

Geef eerst in gewone Nederlandse taal het beslissende resultaat van de run. Beantwoord rechtstreeks de centrale onderzoeksvraag. Maximaal één compacte pagina.

## 2. Status

- GOUD-status: `<PASS|PARTIAL|BLOCKED>`
- onderzoeksdatum / peildatum:
- run-id:
- formele completioncommit:
- bruikbaar voor beslissing: `<JA|JA, MET OPEN PUNTEN|NEE>`

## 3. Wat is onderzocht

- geografische en inhoudelijke scope;
- centrale onderzoeksvraag;
- expliciete uitsluitingen;
- gebruikte detectoren en overlays;
- wat niet opnieuw is onderzocht.

## 4. Belangrijkste uitkomst voor Mark

- wat Mark absoluut niet moet missen binnen deze scope;
- welke bestaande formele A/B/C-statussen relevant zijn;
- welke locaties geen routebepalende betekenis hebben;
- welke plaats een omweg of overnachting wel/niet rechtvaardigt;
- bij routeonderzoek: het duidelijke doorgaande advies.

Alleen Mark kent nieuwe formele A/B/C toe. GOUD presenteert uitsluitend bestaande formele statussen en de door de run toegestane inhoudelijke conclusie.

## 5. Definitieve locaties of kandidaten

Per locatie:

### <LOCATION_ID> — <naam + herkenningshaak>

- fysiek type:
- concrete ligging / WORKING_GEO of VERIFIED_GEO:
- directe relatie met Marks lijn, TOP_X, AOAY of INDIA ESSENTIAL:
- relatietype: `<DIRECT_FYSIEK_ANKER|DIRECTE_LINEAGE|CANONIEK_KERNOORD|REGIONALE_HOOFDPLEK|LOKALE_CONTEXT>`
- waarom devotees gaan:
- wat mensen er doen:
- deelname voor Mark:
- sfeer en praktische betekenis:
- routewaarde / nabijheid:
- globale extra tijd of afstand:
- bevestigingsstatussen:
- belangrijkste onzekerheid:
- concrete betekenis voor Marks beslissing:

## 6. Afgevallen of contextlocaties

Behoud iedere onderzochte locatie zichtbaar. Geef per item:

- LOCATION_ID en naam;
- reden waarom dit geen routebepalende plek is;
- of het alleen een nabijgelegen contextstop is;
- waarom overslaan waarschijnlijk geen gemiste hoofdkans is.

## 7. Route, kaart en praktische GEO

Wanneer in scope:

- belangrijkste routecorridors;
- grote stations/steden;
- ruwe reistijdklassen;
- werkelijke omwegen;
- logische tussenstop ja/nee;
- KML-/kaartartifactpad;
- uitleg van WORKING_GEO versus VERIFIED_GEO;
- geen schijnprecisie.

Een ontbrekende exacte ingang blokkeert geen praktische kaart wanneer adres, gebouwcentrum of representatief kaartpunt voldoende is voor cluster- en routebeslissing.

## 8. Wat ZILVER en GOUD hebben gewijzigd

- belangrijkste bevestigingen;
- belangrijke correcties;
- verwijderde dubbelingen;
- verworpen claims;
- opgeloste of resterende identity-conflicten;
- geen volledige technische changelog, alleen beslisrelevante wijzigingen.

## 9. Open punten

Maximaal de beslisrelevante gaten:

- wat is niet vastgesteld;
- waarom niet;
- gevolg voor de keuze;
- moet dit vóór vertrek, ter plaatse of helemaal niet meer worden gecontroleerd?

## 10. Bron- en bewijsstatus

Compact overzicht van:

- primaire/institutionele bronnen;
- lineage- en traditiebronnen;
- actuele bezoekbaarheids- en vervoersbronnen;
- conflicten of zwakke bronlagen.

## 11. Technische eindcontrole

- BRONS geldig afgerond: `<JA|NEE>`
- BRONS → ZILVER-transition geldig: `<JA|NEE>`
- ZILVER geldig afgerond: `<JA|NEE>`
- ZILVER → GOUD-transition geldig: `<JA|NEE>`
- GOUD geldig afgerond: `<JA|NEE>`
- contextmanifesten gepind: `<JA|NEE>`
- required artifacts compleet: `<JA|NEE>`
- source-ID's resolveerbaar: `<JA|NEE>`
- state/events synchroon: `<JA|NEE>`
- finale readback geslaagd: `<JA|NEE>`

## 12. Geschreven eindproducten

- hoofdrapport:
- kandidaten-/locatieregister:
- kaart/KML indien in scope:
- claims en bronnen:
- technische audit:
- completioncommit:

## 13. Blockers

`NONE` of uitsluitend echte blockers met concreet gevolg.

## 14. Definitieve afsluiting

Eén ondubbelzinnige conclusie voor Mark. Geen verplichte verwijzing naar INDIA2 wanneer de run geldig is afgerond.

END_OF_ARTIFACT
```

## 12. Harde waarborgen

De vereenvoudiging mag de volgende invarianten niet verzwakken:

1. GitHub blijft enige bron van waarheid.
2. Iedere rol leest alleen gepinde context.
3. Geplakte overdracht is nooit predecessorbewijs.
4. Worker en controller hebben verschillende write-scopes.
5. De workerclaim wordt niet hergebruikt als controllerclaim.
6. Geen opvolgercontext vóór definitieve predecessorcommit.
7. Geen READY-state zonder contextmanifest en hashes.
8. Geen volgende prompt bij blocker.
9. Geen stil herstel van onderzoeksinhoud tijdens transition.
10. Geen fase-outputwrites nadat de sessie naar controllerrol is gewisseld.
11. Geen protocolwijziging binnen een actieve, reeds gepinde run.
12. Oude runs blijven op hun gepinde protocolversie.
13. Alleen Mark kent formele A/B/C toe.
14. GOUD mag geen ontbrekende informatie als vastgesteld presenteren.
15. Finale chatoutput moet overeenkomen met het gecommitte MARK_FINAL_REPORT.

## 13. Minimale implementatievolgorde

1. Maak dit besluit definitief op de voorstelbranch.
2. Markeer de n8n/Claude Code-productieroute als `NOT_SELECTED_FOR_CURRENT_PIPELINE`.
3. Schrijf `ROLE_HANDOFF_PROTOCOL.md`.
4. Schrijf de twee templates.
5. Pas Execution, Controller Transition, Self Routing en ENTRYPOINT aan.
6. Pas BRONS, ZILVER en GOUD aan.
7. Pas RUN_TEMPLATE_V3 en NEXT_ACTION-schema aan.
8. Maak één synthetische test-run.
9. Voer BRONS → inline controller uit.
10. Voer ZILVER → inline controller uit.
11. Laat GOUD rechtstreeks `MARK_FINAL_REPORT.md` opleveren.
12. Controleer dat slechts drie inhoudelijke chats nodig waren.
13. Activeer pas daarna voor nieuwe productieruns.
14. Migreer geen reeds geclaimde of gepinde actieve run.

## 14. Testplan

Run-id:

`PIPELINE-HANDOFF-SMOKE-001`

Gebruik een kleine, kunstmatige dataset met:

- drie kandidaten;
- één geldige kandidaat;
- één conflicterende alias;
- één claim met een opzettelijk ontbrekende bron in een aparte negatieve test;
- kleine bestanden met volledige sentinels;
- geen extern lang onderzoek.

### Test A — happy path

- INDIA2 maakt BRONS-startopdracht;
- BRONS voltooit;
- dezelfde sessie wisselt naar controllerrol;
- ZILVER-context wordt correct gepind;
- Mark kopieert één ZILVER-opdracht;
- ZILVER voltooit en transitioneert inline;
- Mark kopieert één GOUD-opdracht;
- GOUD levert volledig MARK_FINAL_REPORT;
- totaal: drie inhoudelijke chats.

### Test B — ontbrekende sentinel

- verwijder opzettelijk één `END_OF_ARTIFACT`;
- inline controller moet blokkeren;
- geen ZILVER-context;
- geen ZILVER-startopdracht.

### Test C — source-ID-fout

- claim verwijst naar niet-bestaande source-ID;
- transition moet blokkeren;
- geen READY-state.

### Test D — state/event-desync

- state en laatste event verschillen;
- inline controller schrijft `DESYNC_DETECTED` of `TRANSITION_BLOCKED` volgens protocol;
- geen opvolgerprompt.

### Test E — stale handofftekst

- wijzig na handoff een niet-gepind chatveld;
- volgende rol moet GitHub volgen en geplakte waarde negeren.

### Test F — write-scope

- probeer controller een BRONS-rapport te laten wijzigen;
- protocol moet dit blokkeren.

### Test G — GOUD-rapportkwaliteit

- controleer dat het eindrapport zelfstandig leesbaar is;
- controleer dat de hoofdconclusie, alle kandidaten, afwijzingen, onzekerheden en technische eindcontrole aanwezig zijn;
- controleer dat Mark niet naar INDIA2 hoeft voor normale uitleg.

### Acceptatie

Productie-activatie is alleen toegestaan wanneer alle tests slagen en:

- geen extra SUBREGIE-chat nodig was;
- geen opvolgercontext door de workerrol zelf is geschreven;
- iedere transition een eigen claim en commit heeft;
- de volgende rol uitsluitend de gepinde context las;
- GOUD rechtstreeks een volledig bruikbaar rapport leverde.

## 15. Resterende blockers

Voor implementatie bestaan drie blockers:

1. de protocolwijzigingen zijn nog niet geschreven en gemerged;
2. de synthetische test-run is nog niet uitgevoerd;
3. actieve runs zijn op oude protocolpins gestart en mogen niet stil worden gemigreerd.

Er is geen inhoudelijke blocker voor het gekozen model.

## 16. Rapportcijfers

- Waarheid: **9,4/10**  
  Aftrek: dezelfde sessie controleert technisch haar eigen completion; dit vraagt een harde rolgrens en mechanische readback.

- Uitvoerbaarheid: **9,0/10**  
  Aftrek: enkele canonieke protocolbestanden moeten gecoördineerd worden aangepast.

- Eenvoud: **9,1/10**  
  Aftrek: inline controller mode is iets complexer dan een onveilige directe workertransition.

- Fouttolerantie: **8,8/10**  
  Aftrek: er is geen externe watchdog; blokkades zijn wel veilig en zichtbaar.

- Tijdwinst: **9,5/10**  
  Aftrek: Mark moet nog twee maal een handoff naar een verse chat kopiëren.

## 17. Formeel besluit over PR #14

`ACCEPT_WITH_CHANGES` geldt uitsluitend voor het minimale handoffmodel uit `INDIA2_HANDOFF_MINIMAL_INTERVENTION_BZG.md` met de wijzigingen uit dit besluit.

De eerdere n8n/Claude Code-consensus wordt voor de huidige India-pipeline:

`NOT_SELECTED_FOR_CURRENT_PIPELINE`

PR #14 blijft review-/historiedocumentatie en wordt niet als productieprotocol gemerged. De minimale implementatie hoort na Marks akkoord in een afzonderlijke, schone implementatiebranch of PR met uitsluitend de noodzakelijke protocol-, rol- en templatewijzigingen.

END_OF_ARTIFACT
# Voorstel: BRONS–ZILVER–GOUD in één opdracht

Status: VOOR CLAUDE-REVIEW — NIET GEÏMPLEMENTEERD

Doel: Mark geeft één startopdracht. De volledige keten wordt daarna zonder handmatig kopiëren uitgevoerd: BRONS, technische controllertransition, ZILVER, technische controllertransition, GOUD, technische eindvalidatie en één eindmelding.

Dit document is een architectuurvoorstel. Het wijzigt geen actieve onderzoeksrun, roloutput, formele A/B/C-status of bestaand protocol.

## 1. Hoofdconclusie

Een echte uitvoering van meerdere uren met één start en later één eindantwoord is niet betrouwbaar te realiseren door alleen een langere prompt in één gewone ChatGPT-chat te gebruiken.

De aanbevolen oplossing is:

1. een externe orchestrator, bij voorkeur n8n op Marks server;
2. GitHub als enige duurzame bron van waarheid en werkgeheugen;
3. een afzonderlijke verse modelrun voor BRONS, ZILVER en GOUD;
4. deterministische controllertransitions tussen de metalen;
5. automatische hervatting vanaf GitHub-checkpoints;
6. een pushmelding na de definitieve eindcommit.

Een enkele ChatGPT-chat kan als noodvariant meerdere rollen sequentieel uitvoeren zolang dezelfde sessie en connector actief blijven. Deze variant mag niet worden gepresenteerd als gegarandeerd urenlang, autonoom of herstartbaar.

## 2. Waarom de externe orchestrator noodzakelijk is

De huidige pipeline bevat al de juiste duurzame bouwstenen:

- `run.yaml` voor onveranderlijke run-identiteit;
- `state.yaml` voor de actuele toestand;
- `events.jsonl` als append-only gebeurtenislog;
- `NEXT_ACTION.yaml` voor exact één uitvoerbare actie;
- gepinde rolcontextmanifesten;
- faseclaims;
- manifesten, sentinels, completionbestanden en handoffs;
- `CHECKPOINT.yaml` voor gecontroleerde hervatting.

Wat ontbreekt is niet meer geheugen, maar een uitvoeringsproces dat na iedere modelrun opnieuw kan starten, GitHub kan lezen, de volgende rol kan aanroepen en fouten kan afhandelen.

Een gewone chat kan zichzelf niet na beëindiging opnieuw activeren. Een API- of CLI-gebaseerde orchestrator kan wel afzonderlijke modelcalls starten, toolresultaten teruggeven, status pollen en een volgende modelrun openen.

## 3. Vijf ontwerpiteraties

### Iteratie 1 — één zeer lange startprompt

Ontwerp:

- één chat;
- één prompt met BRONS, ZILVER en GOUD;
- dezelfde modelcontext voor alle fasen.

Verbetering:

- geen handmatig kopiëren zolang de sessie doorloopt.

Afgewezen als hoofdoplossing omdat:

- de sessie onverwacht kan eindigen;
- er geen betrouwbare automatische herstart is;
- BRONS, ZILVER en GOUD dezelfde gesprekshistorie delen;
- ZILVER daardoor minder onafhankelijk tegen BRONS ingaat;
- een pushmelding na uren niet gegarandeerd kan worden.

### Iteratie 2 — GitHub als extern geheugen binnen één chat

Ontwerp:

- iedere fase schrijft tussentijds naar GitHub;
- dezelfde chat leest `NEXT_ACTION.yaml` opnieuw en wisselt logisch van rol.

Verbetering:

- minder verlies bij contextdruk;
- resultaten hoeven niet in de chat te blijven;
- checkpoints zijn mogelijk.

Nog onvoldoende omdat:

- de fysieke chatsessie nog steeds één eindige runtime is;
- de modelcontext niet werkelijk schoon wordt tussen rollen;
- automatische hervatting na sessie-einde ontbreekt.

### Iteratie 3 — expliciete logische actorgrenzen

Ontwerp:

- één orchestratorsessie;
- daarbinnen strikt gescheiden modi: `BRONS_WORKER`, `CONTROLLER`, `ZILVER_WORKER`, `CONTROLLER`, `GOUD_WORKER`, `FINAL_CONTROLLER`;
- iedere modus krijgt een eigen write-scope en leest uitsluitend het gepinde manifest.

Verbetering:

- betere scheiding van bevoegdheden;
- minder kans dat een controller onderzoeksoutput herschrijft;
- expliciete mode-events maken fouten traceerbaar.

Nog onvoldoende als gegarandeerde oplossing omdat dezelfde fysieke sessie kan eindigen.

### Iteratie 4 — externe orchestrator met verse modelruns

Ontwerp:

- n8n of een vergelijkbare serverworkflow bestuurt de keten;
- iedere rol is een aparte modelcall of aparte Claude Code/OpenAI-agentrun;
- GitHub is het enige overdrachtskanaal;
- de orchestrator controleert na iedere run de repositorytoestand;
- bij `RESUME_REQUIRED` start hij automatisch een nieuwe call met dezelfde claim.

Verbetering:

- echte automatische hervatting;
- verse context per metaal;
- provider- of modeldiversiteit mogelijk;
- retries en pushmeldingen mogelijk.

Dit is de eerste oplossing die werkelijk aan Marks doel voldoet.

### Iteratie 5 — definitieve hybride architectuur

Eindontwerp:

- externe orchestrator is de normale modus;
- één-chat-keten blijft uitsluitend noodmodus;
- bestaande GitHub-state blijft canoniek;
- geen extra onderzoeksfase;
- rollen blijven inhoudelijk gescheiden;
- controllertransitions blijven verplicht;
- technische fouten worden automatisch hervat;
- inhoudelijke of protocolmatige harde blockers stoppen de keten;
- Mark ontvangt één eindrapport en één pushmelding.

## 4. Voorgesteld nieuw protocol

Bestandsnaam:

`pipeline/protocols/ONE_SHOT_BZG_ORCHESTRATION_PROTOCOL.md`

Het protocol is Markdown. Machineleesbare runtimegegevens blijven waar passend YAML of JSONL. Dit is geen Home Assistant-configuratie.

### 4.1 Nieuwe logische actor

`INDIA_ORCHESTRATOR`

Bevoegdheden:

- actuele run en `NEXT_ACTION.yaml` lezen;
- modelworker voor de aangewezen rol starten;
- workerresultaat en GitHub-state valideren;
- controllertransition starten;
- technische retries uitvoeren;
- checkpoint-hervatting starten;
- eindvalidatie starten;
- na definitieve commit notificeren.

Verboden:

- zelfstandig onderzoeksconclusies schrijven;
- formele A/B/C-statussen wijzigen;
- claims inhoudelijk repareren tijdens een controllertransition;
- een geldige claim negeren;
- een fase als voltooid behandelen zonder `COMPLETED`, manifest, state en events;
- een nieuwe rol starten voordat de predecessor technisch geldig is.

### 4.2 Twee uitvoeringsmodi

#### Modus A — `EXTERNAL_ORCHESTRATED`

Normale en aanbevolen modus.

- aparte modelrun per rol;
- automatische transitions;
- automatische resume;
- technische retries;
- pushmelding;
- één eindantwoord aan Mark.

#### Modus B — `SINGLE_SESSION_FALLBACK`

Alleen wanneer geen externe orchestrator beschikbaar is.

- rollen mogen in één chat sequentieel worden uitgevoerd;
- iedere rol leest alleen zijn gepinde context;
- GitHub blijft duurzaam geheugen;
- bij dreigend sessie-einde wordt een checkpoint geschreven;
- Mark kan alsnog een nieuwe chat moeten starten;
- er wordt geen garantie van urenlange autonome uitvoering gegeven.

## 5. Canonieke stateflow

De bestaande fasevolgorde blijft behouden:

`READY_FOR_BRONS`
→ `BRONS_CLAIMED`
→ `BRONS_COMPLETE`
→ controllertransition
→ `READY_FOR_ZILVER`
→ `ZILVER_CLAIMED`
→ `ZILVER_COMPLETE`
→ controllertransition
→ `READY_FOR_GOUD`
→ `GOUD_CLAIMED`
→ `GOUD_PASS | GOUD_PARTIAL | GOUD_BLOCKED`
→ technische eindvalidatie
→ regisseursroutering of bewuste stop.

De orchestrator slaat geen controllertransition over. “Alles in één keer” betekent één gebruikersopdracht, niet één ongescheiden rol.

## 6. GitHub als duurzaam geheugen

### 6.1 Bron van waarheid

De orchestrator vertrouwt uitsluitend op:

- de actuele branch die door de runconfiguratie is aangewezen;
- `run.yaml`;
- `state.yaml`;
- `events.jsonl`;
- `NEXT_ACTION.yaml`;
- het actieve contextmanifest;
- claims, bronnen, manifest, handoff, checkpoint en completionartifacts.

Chattekst is nooit nodig om een volgende fase te reconstrueren.

### 6.2 Seriële writes

Alle writes naar hetzelfde pad worden strikt serieel uitgevoerd:

1. huidig bestand en blob-SHA ophalen;
2. verwachte state controleren;
3. volledige vervangende inhoud schrijven met de huidige SHA;
4. resultaatcommit vastleggen;
5. bestand opnieuw openen;
6. sentinel, eventcursor en relevante velden controleren.

Geen parallelle update of delete op hetzelfde pad. Vooral `state.yaml`, `events.jsonl`, `NEXT_ACTION.yaml`, manifesten en checkpoints zijn single-writer-bestanden.

### 6.3 Meerdere commits zijn toegestaan

Een lange fase hoeft niet één enorme commit te zijn.

- onderzoeksblokken worden tussentijds opgeslagen;
- de claim blijft actief;
- een tussencommit is geen completion;
- `COMPLETED` wordt pas als laatste geschreven;
- een partiële commit wordt hervat, niet teruggedraaid of opnieuw onderzocht.

### 6.4 Geen stille volledige bestandsvervanging na truncatie

Een worker mag nooit een bestand volledig vervangen wanneer zijn bronread mogelijk afgekapt was.

Bij truncatie:

1. stop de geplande write naar dat pad;
2. lees het bestand opnieuw in expliciete regelbereiken of via blob;
3. controleer begin, eind, sentinel en telling;
4. reconstrueer pas daarna de volledige vervangende inhoud;
5. schrijf serieel met de actuele SHA.

## 7. Artifactstrategie en maximale grootte

De bestaande repositoryregel blijft leidend:

- geen primair fasebestand groter dan 1500 regels;
- eerder splitsen wanneer leesbaarheid of toolrespons daar baat bij heeft;
- ieder tekstbestand eindigt met `END_OF_ARTIFACT`;
- XML/KML gebruikt geldige afsluitende tags plus manifesthash;
- rapporten krijgen een `report/INDEX.md`;
- grote JSONL-registers worden deterministisch opgesplitst wanneer zij niet veilig volledig kunnen worden heropend.

Aanvullend voorstel:

- streefwaarde maximaal 500 regels per intensief gewijzigd JSONL-deel;
- gebruik namen zoals `claims-0001-0500.jsonl` wanneer splitsing nodig is;
- manifest bevat per deel: regelgetal, bytegetal, SHA-256 indien betrouwbaar, eerste ID en laatste ID;
- nooit kunstmatig één megabestand assembleren als primaire opvolgerinput.

## 8. Checkpoint en automatische hervatting

Het bestaande `CHECKPOINT.yaml` blijft bestaan.

Aanvullende verplichte velden voor geautomatiseerde uitvoering:

- `checkpoint_sequence`;
- `idempotency_key`;
- `expected_state`;
- `expected_event_cursor`;
- `last_successful_commit`;
- `resume_role`;
- `resume_context_manifest`;
- `next_write_scope`;
- `retry_count`;
- `hard_blockers`;
- `transient_errors`.

Idempotency key:

`<run-id>:<role>:<claim-id>:<checkpoint-sequence>`

Hervatlogica:

1. orchestrator leest state, events en checkpoint;
2. verifieert dezelfde claim;
3. controleert checkpointcommit en gevalideerde bestanden;
4. start een nieuwe verse modelrun voor dezelfde rol;
5. geeft uitsluitend gepinde context plus checkpoint;
6. verbiedt herhaling van voltooide blokken;
7. verwijdert of archiveert checkpoint pas na fasecompletion.

## 9. Scheiding en onafhankelijkheid van BRONS, ZILVER en GOUD

### BRONS

- brede detectie;
- schrijft eerste claims en kandidaatregisters;
- geen opvolgercontext;
- stopt bij completion.

### ZILVER

- altijd een verse modelrun;
- krijgt geen vrije chatgeschiedenis van BRONS;
- leest alleen het ZILVER-contextmanifest en gepinde predecessorartifacts;
- controleert dragende claims en alle OPEN/high-risk-lagen;
- bij voorkeur ander model of andere provider dan BRONS wanneer kosten en beschikbaarheid dit toelaten;
- behoudt geldige inhoud maar is verplicht tegenspraak te zoeken.

### GOUD

- altijd een verse modelrun;
- leest alleen gepinde ZILVER-output plus expliciete loss-controlbestanden;
- maakt finale inhoudelijke en praktische dataset;
- mag geen formele A/B/C-status wijzigen tenzij een aparte Mark-beslissing dat toestaat.

### Controller

- doet geen inhoudelijk onderzoek;
- valideert artifacts en referentiële integriteit;
- genereert opvolgercontext;
- verwerkt state/events;
- start geen volgende rol wanneer de transition ongeldig is.

## 10. Foutafhandeling

### 10.1 Transiënte technische fouten

Voorbeelden:

- tijdelijke connectorfout;
- time-out;
- GitHub 409-conflict;
- rate limit;
- tijdelijke model-APIfout;
- notificatieservice tijdelijk niet beschikbaar.

Behandeling:

- bestaande claim behouden;
- geen onderzoek herhalen;
- maximaal drie automatische retries met oplopende wachttijd;
- vóór retry actuele state en blob-SHA’s opnieuw lezen;
- daarna `ORCHESTRATION_PAUSED` registreren en Mark notificeren.

### 10.2 Herstelbare runfouten

Voorbeelden:

- ontbrekende sentinel in één geschreven deel;
- partiële commit;
- foutieve telling in manifest;
- checkpoint ontbreekt terwijl de claim nog geldig is.

Behandeling:

- expliciete `RUN_REPAIR`;
- alleen het defecte technische deel herstellen;
- bestaande onderzoeksinhoud niet opnieuw genereren;
- daarna normale validatie hervatten.

### 10.3 Harde blockers

Voorbeelden:

- state/event-desynchronisatie die niet deterministisch kan worden gerepareerd;
- onduidelijke of conflicterende formele Mark-beslissing;
- required-file hashdrift;
- ongeldige dubbele claim;
- ontbrekende GitHub-writebevoegdheid;
- onbetrouwbaar vast te stellen predecessorcommit;
- veiligheids- of juridische reden om te stoppen.

Behandeling:

- geen volgende rol starten;
- blocker en exacte benodigde beslissing vastleggen;
- Mark één compacte melding sturen;
- geen schijncompletion.

## 11. Pushmelding

De pushmelding wordt door de externe orchestrator verzonden, niet door een afgesloten chat.

Mogelijke kanalen:

- Home Assistant webhook of notificatieservice;
- Pushover;
- ntfy;
- Telegram;
- e-mail;
- n8n mobiele melding indien beschikbaar.

Verzendmoment:

1. GOUD-completion technisch gevalideerd;
2. eindstate en event succesvol gecommit;
3. eventuele regisseurspackage geschreven;
4. finale GitHub-readback geslaagd;
5. pas daarna notificatie verzenden.

Inhoud:

- run-id;
- eindstatus;
- één hoofdconclusie;
- resterende blocker of `GEEN`;
- link naar GitHub-run of eindrapport.

Wanneer notificatie faalt:

- onderzoek niet herhalen;
- `NOTIFICATION_FAILED` registreren;
- notificatie afzonderlijk opnieuw proberen.

## 12. Voorgestelde n8n-workflow

1. Manual Trigger, webhook of eenvoudige Mark-opdracht.
2. Lees `pipeline/NEXT_ACTION.yaml` via GitHub API.
3. Valideer run, state, eventcursor en claim.
4. Kies workerprofiel op basis van `route`.
5. Start verse OpenAI- of Claude-modelrun.
6. Laat worker uitsluitend via beperkte GitHub-tools werken.
7. Poll GitHub-state en workerresultaat.
8. Bij `RESUME_REQUIRED`: start dezelfde rol opnieuw vanaf checkpoint.
9. Bij fasecompletion: start controllervalidator.
10. Bij geldige transition: lees nieuwe `NEXT_ACTION.yaml`.
11. Herhaal tot GOUD-eindvalidatie.
12. Schrijf orchestration summary.
13. Verstuur pushmelding.
14. Geef Mark één eindrapport.

## 13. Model- en provideraanpak

Voorkeursopzet:

- BRONS: model dat sterk is in breed zoeken en gestructureerde bronregistratie;
- ZILVER: bij voorkeur andere provider of minstens een verse sessie met expliciete adversarial rol;
- GOUD: model dat sterk is in synthese, verliescontrole en praktische datasets;
- controller: lager geprijsd model mogelijk, maar alleen wanneer schema- en referentievalidatie deterministisch buiten het model plaatsvindt.

De orchestrator moet modellen kunnen wisselen zonder repositoryprotocollen te veranderen.

Modelnamen worden in machineconfig gepind of via goedgekeurde aliases beheerd. Promptgedrag kan tussen modelsnapshots veranderen; daarom zijn regressietests noodzakelijk.

## 14. Minimale beveiliging

- API-sleutels uitsluitend in n8n credentials of server secrets;
- geen sleutels in GitHub, prompts, logs of artifacts;
- GitHub-token met minimale benodigde repositoryrechten;
- modelworkers krijgen geen ongecontroleerde shelltoegang;
- write-tools worden beperkt tot toegestane paden;
- controller en worker gebruiken verschillende write-scopes;
- iedere externe call krijgt een unieke request-ID;
- kostenlimiet, maximale modelturns en maximale retries per fase;
- kill switch in n8n en een repositoryflag `orchestration_enabled: false`.

## 15. 31 concrete verbeteringen ten opzichte van handmatig kopiëren

1. Eén gebruikersstart.
2. Eén eindantwoord.
3. GitHub als duurzaam geheugen.
4. Verse modelcontext per metaal.
5. Automatische controllertransitions.
6. Geen handmatig doorsturen van completionteksten.
7. Automatische checkpoint-hervatting.
8. Dezelfde claim blijft behouden.
9. Geen herhaling van gevalideerd onderzoek.
10. Seriële same-path writes.
11. SHA-controle vóór iedere update.
12. Readback na iedere kritieke write.
13. Truncatiedetectie vóór bestandsvervanging.
14. Deterministische artifactsplitsing.
15. Sentinels op alle tekstbestanden.
16. XML/KML-afsluit- en hashcontrole.
17. Volledige claim/source-integriteitscontrole.
18. State/event-synchronisatie na iedere fase.
19. Harde scheiding tussen worker en controller.
20. ZILVER als verse adversarial run.
21. Mogelijkheid tot providerdiversiteit.
22. Transiënte retries zonder nieuwe claim.
23. Expliciete RUN_REPAIR voor technische defecten.
24. Harde blockers stoppen zonder schijncompletion.
25. Pushmelding pas na eindcommit.
26. Notificatiefout los van onderzoeksresultaat.
27. Kosten- en turnlimieten.
28. Kill switch.
29. Auditlog met request-ID’s.
30. Geen protocolwijziging tijdens actieve run.
31. Chat-only modus duidelijk gedegradeerd tot noodvariant.

## 16. Startopdrachten

### 16.1 Gebruikersopdracht aan de externe orchestrator

```text
Start de actuele India-pipelinerun volledig autonoom volgens ONE_SHOT_BZG_ORCHESTRATION_PROTOCOL.md.

Gebruik pipeline/NEXT_ACTION.yaml als eerste uitvoerbare actie. Doorloop alle resterende metalen en controllertransitions tot de technisch gevalideerde GOUD-eindstaat. Gebruik GitHub als enige duurzame bron van waarheid. Hervat bestaande claims vanaf checkpoints zonder afgerond onderzoek te herhalen. Stop alleen bij een harde blocker. Verstuur na de definitieve eindcommit een pushmelding en lever Mark één eindrapport.
```

### 16.2 Workerprompt per afzonderlijke modelrun

```text
Je bent een tijdelijke worker binnen een extern georkestreerde India-pipeline.

Lees pipeline/ENTRYPOINT.md en voer uitsluitend de actie uit die in pipeline/NEXT_ACTION.yaml staat. Gebruik alleen het daar aangewezen gepinde contextmanifest. GitHub is de enige duurzame bron van waarheid.

Bij dreigende uitvoerings- of contextruimte-uitputting schrijf je volgens LONG_RUNNING_EXECUTION_PROTOCOL.md een volledig checkpoint en eindig je met RESUME_REQUIRED. Maak bij hervatting geen nieuwe claim en herhaal geen gevalideerd onderzoek.

Schrijf na fasecompletion uitsluitend het verplichte machineleesbare slotresultaat. Start zelf geen opvolgerrol en maak geen opvolgercontext.
```

### 16.3 Controllerprompt

```text
Je bent uitsluitend controller voor de in pipeline/NEXT_ACTION.yaml en state.yaml aangewezen transition.

Lees CONTROLLER_TRANSITION_PROTOCOL.md en CONTINUOUS_LEARNING_PROTOCOL.md. Valideer de volledige predecessor, bepaal de definitieve resultaatcommit, genereer uitsluitend het gepinde opvolgercontextmanifest en synchroniseer state en events. Wijzig geen onderzoeksinhoud. Routeer daarna NEXT_ACTION.yaml naar exact één volgende fase.
```

### 16.4 Chat-only noodprompt

```text
@GitHub

Voer de actuele India-pipelinerun in deze chat zo ver mogelijk autonoom en sequentieel uit volgens ONE_SHOT_BZG_ORCHESTRATION_PROTOCOL.md, vanaf pipeline/NEXT_ACTION.yaml.

Gebruik GitHub als duurzaam geheugen en houd de logische rollen strikt gescheiden. Voer na iedere fase de vereiste controllertransition uit. Wanneer dezelfde chatsessie niet veilig kan worden afgerond, schrijf een checkpoint en stop zonder werk te herhalen of een completion te simuleren.

Deze opdracht is een single-session fallback en geeft geen garantie op automatische hervatting na het eindigen van de chat.
```

## 17. Acceptatiecriteria voor implementatie

De architectuur wordt pas actief wanneer alle onderstaande tests slagen.

1. Een synthetische BRONS-run kan halverwege stoppen en automatisch hervatten zonder dubbele claim.
2. Een opzettelijk getrunceerd artifact wordt gedetecteerd en niet volledig overschreven.
3. Een GitHub 409-conflict veroorzaakt read-refresh-retry en geen dataverlies.
4. Een worker kan geen opvolgercontext schrijven.
5. Een controller kan geen onderzoeksartifact wijzigen.
6. ZILVER start pas na een geldige BRONS-transition.
7. GOUD start pas na een geldige ZILVER-transition.
8. Een foutieve source-ID blokkeert transition.
9. Een ongeldige sentinel blokkeert completion.
10. Een notificatiefout herhaalt geen onderzoek.
11. Een externe kill switch stopt nieuwe modelcalls zonder actieve GitHub-output te verwijderen.
12. Een volledige testrun levert één start, nul handmatige overdrachten en één eindmelding.

## 18. Feitencontrole en grenzen

Gecontroleerde technische uitgangspunten:

- GitHub create/update contents vereist bij updates de huidige blob-SHA.
- Gelijktijdige create/update en delete op hetzelfde pad kan conflicteren en moet serieel gebeuren.
- Git blobs kunnen via de GitHub API afzonderlijk worden gelezen; grote artifacts moeten desondanks volgens de strengere repositoryregels worden gesplitst.
- OpenAI ondersteunt externe agentorchestratie, tools, background responses en completion-webhooks via de API; dit is een serverintegratie en niet hetzelfde als een gewone ChatGPT-chat.
- Anthropic tool use vereist bij clienttools dat een extern clientsysteem de tool uitvoert en het resultaat terugstuurt.
- Claude Code kan vanuit een extern proces non-interactief worden aangeroepen, turnlimieten gebruiken en sessies hervatten.
- ChatGPT-appbeschikbaarheid en writecapaciteiten verschillen per app, plan en omgeving. De huidige repositorytools mogen daarom niet worden verward met een algemene garantie voor iedere ChatGPT-gebruiker.

Niet gegarandeerd:

- dat één gewone chat uren actief blijft;
- dat een model zichzelf na sessie-einde opnieuw start;
- dat een pushmelding vanuit een afgesloten chat wordt verstuurd;
- dat drie rollen in dezelfde gesprekshistorie dezelfde onafhankelijkheid bieden als drie verse modelruns;
- dat alle toekomstige modelversies exact hetzelfde promptgedrag behouden.

## 19. Zelfbeoordeling

Waarheidsgetrouwheid: 9,3/10.

Reden: de centrale beperking en de aanbevolen externe orchestratie zijn technisch goed onderbouwd. Onzekerheid blijft bestaan over exacte productlimieten, connectorgedrag per ChatGPT-ervaring en toekomstige model-/APIwijzigingen. Daarom worden geen exacte maximale sessieduur of contextlengte geclaimd.

Uitvoerbaarheid protocol: 8,8/10.

Reden: de architectuur sluit direct aan op de bestaande GitHub-state, claims, transitions en checkpoints. De resterende implementatierisico’s zitten vooral in n8n-credentialbeheer, provider-APIkosten, schema-validatie, rate limits en het schrijven van een veilige beperkte GitHub-toolset.

## 20. Aanbevolen besluit

ACCEPTEER de architectuur onder drie harde voorwaarden:

1. externe orchestratie wordt de normale modus;
2. iedere metaalfase krijgt een verse modelrun;
3. de huidige actieve run wordt niet tijdens de uitvoering gemigreerd; implementatie start na een gecontroleerd moment of met een afzonderlijke test-run.

END_OF_ARTIFACT
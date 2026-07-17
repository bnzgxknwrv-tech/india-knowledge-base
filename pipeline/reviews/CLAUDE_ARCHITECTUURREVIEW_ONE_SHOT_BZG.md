CLAUDE ARCHITECTUURREVIEW ZEGT:

### A. Eindbesluit

`ACCEPT_WITH_REQUIRED_CHANGES`

Het architectuurvoorstel is fundamenteel gezond en direct gebaseerd op wat al canoniek in de repository staat (state.yaml/events.jsonl/NEXT_ACTION.yaml, claims, controllertransities, checkpoints). Twee punten (C-02, C-10) hebben een concrete, hieronder uitgewerkte wijziging nodig vóór implementatie. De overige veertien punten zijn technisch correct en worden geaccepteerd zonder wijziging.

### B. Beslismatrix

**C-01 — Normale uitvoeringsmodus**
Oordeel: ACCEPT.
Reden: een gewone chatsessie kan zichzelf aantoonbaar niet na beëindiging heractiveren; dit is een harde, bekende platformbeperking, geen aanname. `EXTERNAL_ORCHESTRATED` als norm en single-chat als noodvariant is de correcte indeling.
Risico bij ongewijzigd laten: n.v.t., geen wijziging.

**C-02 — Externe orchestrator**
Oordeel: CHANGE.
Reden: n8n als buitenste trigger/schedule/notificatielaag is een redelijke keuze (Mark heeft de server al, goede webhook/ntfy/Pushover-nodes). Maar het voorstel laat n8n zelf de modelcalls en tool-orchestratie doen via losse HTTP-nodes — dat herbouwt functionaliteit die al bestaat en getest is: Claude Code kan non-interactief, met een vaste prompt, met een beperkte toolset en met sessie-hervatting worden aangeroepen vanaf de commandoregel of via de Agent SDK. Dat is precies het "start een verse worker, laat hem via GitHub-tools werken, herstart hem bij RESUME_REQUIRED"-patroon dat het voorstel wil bouwen.
Exacte vervangende formulering: n8n blijft de buitenste laag (trigger, schedule, polling van state.yaml, kostenteller, kill switch, notificatie). Voor de modeluitvoering zelf roept n8n per workerstap een non-interactieve Claude Code-aanroep aan (CLI-subprocess of Agent SDK-call) met de workerprompt uit sectie 16.2, een GitHub-tool beperkt tot de toegestane paden, en een turnlimiet. n8n parsed alleen het machineleesbare slotresultaat, het voert zelf geen modelredenering of tool-keuzelogica uit.
Risico bij ongewijzigd laten: dubbele, minder betrouwbare implementatie van tool-orchestratie/foutafhandeling in n8n-nodes die elders al robuust bestaat — meer implementatietijd, meer plekken waar een subtiele foutafhandelingsbug kan zitten.

**C-03 — Verse run per metaal**
Oordeel: ACCEPT.
Reden: correct en noodzakelijk voor epistemische onafhankelijkheid; komt overeen met hoe generator/verifier-scheiding in de praktijk werkt — gedeelde gespreksgeschiedenis ondermijnt aantoonbaar tegenspraak.

**C-04 — GitHub als enige duurzame waarheid**
Oordeel: ACCEPT.
Reden: chatgeheugen is per definitie sessiegebonden en niet overdraagbaar; dit is de enige houdbare aanname.

**C-05 — Geen tweede concurrerende statebron**
Oordeel: ACCEPT, met verduidelijking (geen inhoudelijke wijziging).
Reden: correct principe. Verduidelijking: n8n's eigen executielog (per-workflow-run-geschiedenis) mag bestaan als observability-metadata, maar mag nooit worden teruggelezen om een routeringsbeslissing te nemen — elke beslissing herleest state.yaml/NEXT_ACTION.yaml vers, nooit n8n's cache van "wat er de vorige keer gebeurde." Dit staat impliciet al in het voorstel; expliciet maken voorkomt een later stille afwijking.

**C-06 — Controllertransitions blijven afzonderlijk**
Oordeel: ACCEPT.
Reden: consistent met de rest van de architectuur en met de bestaande CONTROLLER_TRANSITION_PROTOCOL.md.

**C-07 — Worker/controller write-scheiding**
Oordeel: ACCEPT.
Reden: correcte bevoegdhedenscheiding, voorkomt dat een controller onbedoeld onderzoeksinhoud overschrijft.

**C-08 — Checkpoint behoudt claim**
Oordeel: ACCEPT — bevestig HARD REQUIREMENT.
Reden: zonder deze regel kan een hervatte run een tweede, concurrerende claim aanmaken en een split-brain-toestand veroorzaken. Dit is de belangrijkste enkele regel in het hele voorstel.

**C-09 — Seriële GitHub-writes**
Oordeel: ACCEPT — bevestig HARD REQUIREMENT.
Reden: correct en standaard voor de GitHub Contents API (blob-SHA vereist bij update); readback na iedere kritieke write is de juiste aanvullende discipline.

**C-10 — Artifactsplit en truncatie**
Oordeel: CHANGE.
Reden: de regel "een mogelijk afgekapte read mag nooit volledige vervanging zijn" is gedragsmatig correct maar niet mechanisch afdwingbaar zoals geformuleerd — een model "weet" niet altijd zelf dat een read is afgekapt. Er is geen expliciete, deterministische detectiemethode genoemd.
Exacte vervangende formulering: voeg toe: "Voor bestanden opgehaald via de GitHub Contents API: controleer het `size`-veld tegen de lengte van het gedecodeerde `content`-veld; bij een mismatch of bij `content` leeg met `size > 0`, haal het bestand op via de Git Blob API in plaats van de Contents API. Voor bestanden die in de modelcontext zelf worden gelezen (niet via een API-respons met expliciete metadata): het enige betrouwbare mechanisme is de bestaande 1500-regel-limiet strikt handhaven, zodat afkapping binnen één contextvenster praktisch uitgesloten is — er bestaat geen generiek, model-onafhankelijk signaal voor 'mijn eigen contextvenster heeft dit afgekapt'."
Risico bij ongewijzigd laten: een worker kan een groot bestand overtuigend maar onopgemerkt onvolledig lezen en vervolgens een schijnbaar geldige maar feitelijk verminkte volledige vervanging schrijven — stille dataverliesfout, precies wat sectie 6.4 wil voorkomen maar zonder mechanisme niet garandeert.

**C-11 — ZILVER-onafhankelijkheid**
Oordeel: ACCEPT.
Reden: eerlijke, correcte prioritering — contextisolatie plus adversariale opdracht is de dragende mechaniek; providerdiversiteit is een nuttige extra laag, geen vereiste. Overclaimen van providerdiversiteit als hoofdmechanisme zou zelf een feitelijke overdrijving zijn geweest.

**C-12 — GOUD-onafhankelijkheid**
Oordeel: ACCEPT.
Reden: consistent met C-03/C-11.

**C-13 — Automatische retries**
Oordeel: ACCEPT.
Reden: correcte scope (alleen transiënte technische fouten, max drie, verse state-read vóór iedere retry). Inhoudelijke blockers terecht uitgesloten van automatische omzeiling.

**C-14 — Pushmelding na commit**
Oordeel: ACCEPT.
Reden: correcte volgorde (notificatie na finale readback, notificatiefout ontkoppeld van onderzoeksresultaat).

**C-15 — Actieve runs niet stil migreren**
Oordeel: ACCEPT — bevestig HARD REQUIREMENT.
Reden: consistent met de bestaande regel in ENTRYPOINT.md dat een uitvoerende rol tijdens dezelfde run nooit zijn eigen protocol wijzigt. Een synthetische test-run vóór productie-inzet is de juiste volgorde.

**C-16 — Eén eindantwoord aan Mark**
Oordeel: ACCEPT.
Reden: correct, met de juiste uitzondering (harde blocker die zijn beslissing vereist).

### C. Top vijf failure modes (kans × impact, hoogste eerst)

**1. De orchestrator zelf faalt stil (n8n-instance down, GitHub-token verlopen, API-sleutel geroteerd)**
Detectie: een aparte, lichte "heartbeat"-workflow in n8n zelf die periodiek controleert of de laatste geplande run daadwerkelijk is gestart; extern van de hoofdworkflow, zodat een crash van de hoofdworkflow de heartbeat niet meesleept.
Automatisch herstel: geen — een gecrashte n8n-instance kan zichzelf niet herstarten vanuit zijn eigen workflow. Dit vereist OS-niveau supervisie (bijv. een systemd-restart-policy of Docker-restart-policy op de n8n-container).
Wanneer Mark waarschuwen: direct wanneer de heartbeat uitblijft — dit kan alleen via een kanaal buiten n8n zelf (bijv. een simpele externe uptime-monitor die ntfy/Pushover rechtstreeks aanroept, niet via n8n).

**2. Kostenrunaway door een vastzittende resume-lus (checkpoint → resume → checkpoint zonder voortgang)**
Detectie: `retry_count`/`checkpoint_sequence` in CHECKPOINT.yaml monotoon laten oplopen; wanneer dezelfde `exact_next_step` twee keer achter elkaar terugkeert zonder dat `completed_blocks` groeit, is dat het signaal.
Automatisch herstel: bij gedetecteerde stagnatie automatisch naar `ORCHESTRATION_PAUSED` (dezelfde status als bij transiënte fouten na 3 retries) — geen vierde poging.
Wanneer Mark waarschuwen: direct bij de eerste gedetecteerde stagnatie-cyclus, niet pas na een kostenplafond — kosten zijn onomkeerbaar zodra besteed.

**3. Contentdrift die pas bij de controllertransitie wordt opgemerkt, na een uren lange BRONS-run**
Detectie: dit is al deels gedekt (referentiële-integriteitscontrole bij transitie), maar controleert pas achteraf.
Automatisch herstel: geen volledige automatische reparatie van onderzoeksinhoud (terecht, dat zou zelfstandig onderzoeksconclusies wijzigen — verboden voor de orchestrator). Wel: tussentijdse lichte consistentiechecks na ieder werkblok uit LONG_RUNNING_EXECUTION_PROTOCOL.md (niet pas aan het einde), zodat drift binnen één werkblok wordt gevonden, niet pas na de hele fase.
Wanneer Mark waarschuwen: alleen wanneer de controllertransitie uiteindelijk `TRANSITION_BLOCKED` schrijft — dat mechanisme bestaat al en is voldoende, mits de tussentijdse checks de kans op een pas-aan-het-einde-verrassing verkleinen.

**4. GitHub-rate-limiting bij intensieve per-item commits tijdens een lange BRONS-fase**
Detectie: HTTP 403/429 met rate-limit-headers, al impliciet gedekt door de bestaande transiënte-foutafhandeling (C-13).
Automatisch herstel: bestaande retry-met-oplopende-wachttijd volstaat, mits de wachttijd de `X-RateLimit-Reset`-header respecteert in plaats van een vaste backoff.
Wanneer Mark waarschuwen: alleen als het rate limit herhaaldelijk (>3x binnen één fase) wordt geraakt — dat wijst op een architecturaal probleem (te veel losse writes) dat een ontwerpwijziging verdient, niet alleen meer retries.

**5. Pushmeldingkanaal faalt stil zonder dat Mark het merkt**
Detectie: al gedekt door `NOTIFICATION_FAILED`-registratie.
Automatisch herstel: één losse herhaalpoging na een korte wachttijd, apart van de onderzoeksflow (al voorgesteld).
Wanneer Mark waarschuwen: als de herhaalpoging ook faalt, is er geen betrouwbaar kanaal meer om hem te waarschuwen via — dit moet dan zichtbaar zijn zodra hij zelf de repository opent (bijv. een persistente banner-status in `state.yaml`), niet stil blijven liggen tot hij toevallig kijkt.

### D. Minimale uitvoerbare versie

Geen n8n-UI, geen multi-provider, geen kostendashboard, geen kill-switch-UI. Alleen:

1. Eén hardcoded synthetische test-run-id.
2. Eén cron-getriggerd script (kan een simpel shellscript/cronjob zijn, n8n is hier nog niet nodig) dat: `state.yaml` leest → bepaalt welke rol aan de beurt is → een non-interactieve Claude Code-aanroep doet met de bijpassende workerprompt (16.2 of 16.3) → het machineleesbare slotresultaat parsed → bij `RESUME_REQUIRED` niets doet behalve opnieuw triggeren bij de volgende cron-tick → bij fasecompletion een aparte controlleraanroep doet.
3. Alleen de HARD REQUIREMENT-punten (C-03, C-04, C-06, C-08, C-09, C-12, C-15) worden in v0 afgedwongen; de overige zijn kwaliteitsverbeteringen die later kunnen worden toegevoegd zonder de kernarchitectuur te wijzigen.
4. Notificatie: één ntfy-call (simpelste, geen account/app nodig), geen Home Assistant-webhook in v0 — dat voegt een extra afhankelijke laag toe die nu niet nodig is om de kernvraag te testen.

Ontbrekende regressietests die vóór een echte productie-inzet nog moeten worden toegevoegd (naast de 12 in sectie 17 van het voorstel): een test die specifiek een gesimuleerde afgekapte GitHub-read forceert (voor C-10); een test die een tweede, gelijktijdige workeraanroep op dezelfde claim simuleert (race condition, niet alleen sequentiële conflicttest); een test die de orchestrator zelf laat crashen halverwege een fase en verifieert dat een externe restart geen dubbele claim maakt.

### E. Productiearchitectuur

- **Orchestrator**: n8n op Marks server als buitenste laag (trigger/schedule/poll/notificatie/kostenteller/kill switch), geen eigen modelredenering.
- **Modelcalls**: non-interactieve Claude Code-aanroepen (CLI-subprocess of Agent SDK) per workerstap, met een expliciete turnlimiet en de workerprompt uit het voorstel; ZILVER bij voorkeur een andere provider/model wanneer kosten dat toelaten, niet verplicht.
- **GitHub-authenticatie**: een GitHub App gescoped tot uitsluitend deze repository, niet een persoonlijk access-token — kleinere blast radius bij lekkage, eigen rate-limit-pool los van Marks persoonlijke account.
- **Statebron**: uitsluitend `run.yaml` / `state.yaml` / `events.jsonl` / `NEXT_ACTION.yaml`, zoals al vastgesteld in C-04/C-05.
- **Retries**: max 3 transiënte retries met oplopende wachttijd die de GitHub-ratelimit-header respecteert; geen automatische retry op inhoudelijke blockers.
- **Checkpoints**: zoals in LONG_RUNNING_EXECUTION_PROTOCOL.md, met de aanvullende velden uit sectie 8 van het voorstel.
- **Notificatie**: ntfy of Pushover als eerste keuze — eenvoudiger en met minder bewegende delen dan een Home Assistant-notificatie-entiteit (in het zusterproject dit jaar meermaals zelf kapot gebleken door een verkeerd service/entity-onderscheid; niet nodeloos dezelfde afhankelijkheid hier herintroduceren).
- **Kosten- en veiligheidslimieten**: max modelturns per workerstap, max totale kosten per run bijgehouden in een simpele teller in `run.yaml` of een apart kostenbestand, kill-switch-flag `orchestration_enabled: false` die de n8n-trigger controleert vóór elke nieuwe workeraanroep.
- **Beveiliging, aanvullend op sectie 14 van het voorstel**: BRONS is het meest blootgesteld aan prompt-injectie omdat het breed extern bronnenonderzoek doet — voeg een expliciete regel toe dat instructies aangetroffen in extern gevonden content (webpagina's, documenten) nooit als opdracht aan de worker mogen worden behandeld, alleen als onderzoeksdata. Dit is dezelfde discipline als bij ieder ander systeem dat externe content leest.

### F. Definitieve startopdracht

```text
GitHub INDIA PIPELINE (extern georkestreerd): activeer de GitHub-connector voor bnzgxknwrv-tech/india-knowledge-base en test read/write. Lees pipeline/NEXT_ACTION.yaml en voer exact de daar aangewezen actie uit volgens ONE_SHOT_BZG_ORCHESTRATION_PROTOCOL.md. Gebruik uitsluitend GitHub als duurzame bron van waarheid; herhaal geen gevalideerd onderzoek. Bij dreigende sessie- of contextuitputting: schrijf een checkpoint volgens LONG_RUNNING_EXECUTION_PROTOCOL.md en eindig met RESUME_REQUIRED — de externe orchestrator hervat automatisch. Voer na fasecompletion geen volgende rol zelf uit; de controllertransitie en eventuele pushmelding gebeuren extern. Stop uitsluitend bij een harde blocker en meld die compact.
```

(87 woorden.)

### G. Rapportcijfers

- **Waarheid: 9/10.** Het voorstel overclaimt nergens en benoemt zijn eigen onzekerheden expliciet (sectie 18). Aftrek: het had zijn eigen hoofdconclusie sterker kunnen onderbouwen door expliciet te verwijzen naar bestaande, bewezen non-interactieve/hervatbare model-CLI's als precedent in plaats van het abstract te stellen.
- **Uitvoerbaarheid: 7/10.** De statemachine en protocolregels zijn direct bouwbaar. Aftrek: de daadwerkelijke n8n-implementatie (credential-wiring, foutafhandeling per node, kostenregistratie) is nog architectuur, geen bouwbare spec; geen expliciete keuze tussen PAT en GitHub App.
- **Eenvoud: 6/10.** Bewust niet eenvoudig omdat het probleem dat niet toelaat, en het voorstel voegt terecht geen overbodige nieuwe onderzoeksfase toe. Aftrek: veertien nieuwe CHECKPOINT-velden plus een volledig nieuw protocolbestand is nog altijd een aanzienlijke nieuwe oppervlakte t.o.v. wat al bestaat.
- **Fouttolerantie: 8/10.** Sterk op de faalmodi waar het voorstel zich expliciet tegen ontwerpt (transiënte fouten, truncatie, claimconflicten, harde blockers). Aftrek: geen behandeling van orchestrator-zelf-faalt of kostenrunaway-detectie (zie faalmodi 1-2 hierboven).
- **Onafhankelijkheid van de metalen: 8/10.** Correcte, eerlijke prioritering van contextisolatie boven providerdiversiteit. Aftrek: "expliciete gepinde loss-control-bestanden" voor GOUD wordt genoemd maar nooit concreet opgesomd — dat laat ruimte voor inconsistente predecessor-leesomvang tussen runs.

/CLAUDE ARCHITECTUURREVIEW

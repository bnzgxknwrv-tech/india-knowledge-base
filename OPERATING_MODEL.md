# OPERATING_MODEL - Hoe het onderzoek werkt

Dit document beschrijft de samenwerking - niet het project (zie PROJECT.md), niet het datamodel (zie AI_RULES.md).

## 0. Algemene inleesvolgorde

Voor regie- en algemene projectchats:
1. README.md
2. AI_RULES.md
3. PROJECT.md
4. OPERATING_MODEL.md
5. CHATGPT_ROLE.md
6. PRIORITY_GROUPS.md
7. LESSONS.md
8. METHODOLOGY.md
9. CHAT_DISTILLATION.md
10. CHATGPT_HANDOFF.md
11. CURRENT_FOCUS.md
12. relevante cluster-, PLACE-, SOURCE-, AUDIT- en DECISION-records

Een nieuwe regiechat levert eerst een STATE RECONSTRUCTION en laat Mark die bevestigen vóór nieuw onderzoek.

BRONS-, ZILVER- en GOUD-workers vormen een aparte uitvoeringsroute. Zij starten uitsluitend bij `pipeline/ENTRYPOINT.md`, ontvangen alleen een run-id en rol, lezen het gepinde contextmanifest en schrijven alle resultaten naar GitHub. Zij voeren geen algemene state reconstruction met Mark uit.

## 1. Doel

Het doel is niet heiligen verzamelen. Het doel is fysiek bestaande spirituele bestemmingen identificeren die binnen levende tradities blijvende betekenis hebben gekregen. De plek is het onderzoeksobject; personen, boeken, lineages, tradities en getuigenissen zijn zoek- en interpretatielagen.

De onderzoeker beschrijft verschillende onderbouwingstypen afzonderlijk en berekent geen spirituele totaalscore. Alleen Mark beoordeelt wat hij wil bezoeken.

## 2. Rollen

- Mark — eindbeslisser. Kent als enige A/B/C toe, beheert persoonlijke voorkeuren en neemt reisbesluiten.
- INDIA2 / ChatGPT-regisseur — inhoudelijke hoofdregisseur. Bepaalt projectkoers, clusterscope en verwerkt uitsluitend gevalideerde GOUD-dossiers.
- SUBREGIE INDIA — vaste pipeline- en kwaliteitsregie. Zet runs op, begeleidt Mark door BRONS/ZILVER/GOUD, valideert completions, verzorgt controllertransitions, repareert technische runfouten, leert structureel van defecten en levert INDIA2 één schoon regisseurspakket.
- Bevoegde curatoren — onderhouden repositoryrecords via expliciete commits of pull requests.
- BRONS — brede detectie en primaire inventarisatie.
- ZILVER — verificatie, tegenspraak, bronverbetering en inhoudelijke correctie.
- GOUD — synthese, acceptatie en vrijgave met PASS, PARTIAL of BLOCKED.
- Andere AI-systemen — kunnen iedere pipeline-rol uitvoeren wanneer zij GitHub volledig kunnen lezen en schrijven en het gepinde contract volgen.

Wat geen enkele AI mag: A/B/C toekennen, de prioriteitsindex stil wijzigen, een record stil veranderen, projectrelevantie als score invoeren of een capaciteit claimen die niet bewezen is.

## 3. Werkstromen

### 3.1 Reguliere repositorywerkstroom

1. Hypothese of open vraag.
2. Onderzoek en bronverzameling.
3. Audit en tegenspraak.
4. Mark neemt waar nodig een besluit.
5. Een bevoegde schrijver legt het resultaat vast.

### 3.2 BRONS–ZILVER–GOUD-pijplijn

1. INDIA2 of Mark geeft de inhoudelijke scope door aan SUBREGIE INDIA.
2. SUBREGIE INDIA maakt of controleert de geïsoleerde run met scope, status en alleen het uitvoerbare BRONS-contextmanifest.
3. BRONS wordt in een nieuwe chat geactiveerd met alleen run-id en rol en schrijft een volledige faseversie naar `BRONS/`.
4. SUBREGIE INDIA valideert BRONS en verzorgt de controllertransition.
5. ZILVER wordt in een nieuwe chat geactiveerd, haalt BRONS uit GitHub en schrijft een volledige eigen versie naar `ZILVER/`.
6. SUBREGIE INDIA valideert ZILVER en verzorgt de controllertransition.
7. GOUD wordt in een nieuwe chat geactiveerd, haalt ZILVER uit GitHub en schrijft het definitieve dossier naar `GOUD/`.
8. SUBREGIE INDIA valideert GOUD en maakt één compact regisseurspakket.
9. Alleen dit gevalideerde pakket en het GOUD-dossier gaan naar INDIA2. Mark hoeft geen rapporten tussen chats te kopiëren.
10. Na inhoudelijke verwerking en expliciete toestemming archiveert SUBREGIE INDIA de run onder `research/completed/`.

INDIA2 routeert alle workercompletions, BLOCKED-berichten, connectorproblemen, state/events, transitions, runreparaties en pipelineverbeteringen verplicht naar SUBREGIE INDIA. INDIA2 analyseert deze operationele zaken niet zelf. Zie `pipeline/protocols/REGIE_INTERFACE_PROTOCOL.md`.

De gezaghebbende regels staan onder `pipeline/` en de generieke Methodology v2.0 onder `knowledge/methodology/`.

## 4. Conflicten

Onenigheid tussen AI's is normaal en gewenst. Een positie wint alleen door betere onderbouwing of door een besluit van Mark. Onopgeloste feitelijke conflicten blijven zichtbaar in claims, audit of een formeel AUDIT-record.

## 5. Waarderingen

Alleen Mark kent A, B of C toe. Nieuwe plekken starten ONGEMERKT. Geen pipeline-rol maakt een totaalscore, projectrelevantie of impliciete rangorde.

## 6. Prioriteiten

PRIORITY_GROUPS.md is leidend voor Marks persoonlijke-aantrekkingsas. Geen AI mag die volgorde wijzigen of als objectieve onderzoeksuitkomst presenteren.

## 7. Repositoryschrijven en protocolverbetering

GitHub is de gedeelde waarheid en het enige overdrachtskanaal tussen pipeline-workers. Iedere wijziging is zichtbaar via een commit of pull request.

SUBREGIE INDIA onderhoudt de pipeline zelfstandig binnen de grenzen van `pipeline/roles/SUBREGIE_INDIA.md`. Methodologische of projectinhoudelijke wijzigingen worden aan INDIA2 voorgelegd. Actieve runs blijven op de in `run.yaml` gepinde methodologie, rollen en protocollen. Een worker wijzigt zijn eigen contract nooit tijdens dezelfde uitvoering.

END_OF_ARTIFACT
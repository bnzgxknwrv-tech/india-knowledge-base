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
- India2 / ChatGPT-regisseur — regisseur en architect. Bepaalt scope, activeert runs en verwerkt het definitieve GOUD-dossier.
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

1. De regisseur of Mark maakt een geïsoleerde run met scope, status en contextmanifesten.
2. BRONS wordt in een nieuwe chat geactiveerd met alleen run-id en rol en schrijft een volledige faseversie naar `BRONS/`.
3. Na geldige completion wordt ZILVER in een nieuwe chat geactiveerd. ZILVER haalt BRONS uit GitHub en schrijft een volledige eigen versie naar `ZILVER/`.
4. Na geldige completion wordt GOUD in een nieuwe chat geactiveerd. GOUD haalt ZILVER uit GitHub en schrijft het definitieve dossier naar `GOUD/`.
5. Alleen GOUD gaat naar de regisseur, via run-id, commit en manifestpad. Mark hoeft geen rapporten tussen chats te kopiëren.
6. Na verwerking wordt de run gearchiveerd onder `research/completed/`.

De gezaghebbende regels staan onder `pipeline/` en de generieke Methodology v2.0 onder `knowledge/methodology/`.

## 4. Conflicten

Onenigheid tussen AI's is normaal en gewenst. Een positie wint alleen door betere onderbouwing of door een besluit van Mark. Onopgeloste feitelijke conflicten blijven zichtbaar in claims, audit of een formeel AUDIT-record.

## 5. Waarderingen

Alleen Mark kent A, B of C toe. Nieuwe plekken starten ONGEMERKT. Geen pipeline-rol maakt een totaalscore, projectrelevantie of impliciete rangorde.

## 6. Prioriteiten

PRIORITY_GROUPS.md is leidend voor Marks persoonlijke-aantrekkingsas. Geen AI mag die volgorde wijzigen of als objectieve onderzoeksuitkomst presenteren.

## 7. Repositoryschrijven en protocolverbetering

GitHub is de gedeelde waarheid en het enige overdrachtskanaal tussen pipeline-workers. Iedere wijziging is zichtbaar via een commit of pull request.

India2, Claude, ChatGPT en andere bevoegde schrijvers mogen de pipeline verbeteren. Een actieve run blijft op de in `run.yaml` gepinde methodologie, rollen en protocollen. Een worker wijzigt zijn eigen contract nooit tijdens dezelfde uitvoering.

END_OF_ARTIFACT

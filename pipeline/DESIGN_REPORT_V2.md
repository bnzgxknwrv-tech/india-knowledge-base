# Ontwerprapport BRONS–ZILVER–GOUD v2.0

## 1. Opdracht

Bouw een volledig GitHub-native, modelonafhankelijke onderzoekspijplijn waarin drie volledig nieuwe AI-sessies sequentieel één onderzoek verbeteren. Mark kopieert geen rapporten tussen chats. Iedere fase schrijft haar eigen volledige dossier naar GitHub; alleen GOUD gaat naar de India-regisseur.

## 2. Onderzoek van de bestaande sweep en pipeline

### Bruikbaar en behouden

Uit de bestaande sweepmethodiek zijn behouden:
- de fysieke-plaats-poort: personen, boeken en tradities zijn geen eindobject;
- afzonderlijke controle van fysieke identiteit en actuele bezoekbaarheid;
- bronhiërarchie en verbod op Wikipedia/zoekresultaten als eindbron;
- AOAY-dubbele bewijsvoering;
- expliciete negatieve resultaten en onzekerheidssectie;
- controlelijst, open zoekrichtingen, dubbelingscontrole en ashramcontrole;
- harde bescherming dat alleen Mark A/B/C toekent;
- eerlijke compleetheidsstatus in plaats van schijnvolledigheid.

### Onvoldoende en vervangen

De eerste pipelineversie was chat-gecentreerd:
- BRONS leverde één grote rapporttekst;
- Mark moest die naar een nieuwe ZILVER-chat kopiëren;
- ZILVER leverde opnieuw één grote tekst voor GOUD;
- er was geen runisolatie, claim-lock, source-commit-pin, contextmanifest, artifactmanifest of truncatiebeveiliging;
- `FEIT` versus `TRADITIECLAIM` was te grof voor Babaji, Krishna, Shakti Peeths, levende lineages en getuigenissen;
- institutionele identiteit was niet verplicht;
- rapporten waren conceptueel volledig maar konden opnieuw monsterbestanden worden.

Deze onderdelen zijn vervangen door repository-only handoff, Methodology v2.0 en gestructureerde fase-artifacts.

## 3. Definitieve architectuur

### Stabiele kennis

- `knowledge/methodology/METHODOLOGY_V2.md`
- `knowledge/project/OVERLAYS_INDIA.md`

Methodologie is generiek. AOAY, Kriya/Babaji, Krishna, Neem Karoli Baba/Ram Dass en andere India-lagen zijn projectdata.

### Uitvoering

- `pipeline/ENTRYPOINT.md`
- `pipeline/PIPELINE_CONTRACT.md`
- `pipeline/roles/BRONS.md`
- `pipeline/roles/ZILVER.md`
- `pipeline/roles/GOUD.md`
- `pipeline/protocols/EXECUTION_PROTOCOL.md`
- `pipeline/protocols/CONTEXT_PROTOCOL.md`
- `pipeline/protocols/EVIDENCE_PROTOCOL.md`
- `pipeline/QUALITY_GATE.md`
- `pipeline/templates/RUN_TEMPLATE.md`

### Onderzoeksdata

- `research/active/<run-id>/`
- `research/completed/<run-id>/`

Iedere run bevat immutable run-identiteit, actuele state, append-only events, fasecontexten en afzonderlijke BRONS/ZILVER/GOUD-output.

## 4. Methodology v2.0

De centrale vraag is niet langer uitsluitend wat historisch bewezen is. De pipeline onderzoekt waarom een fysieke plaats binnen een of meer spirituele tradities een blijvende bestemming is geworden, welke typen onderbouwing bestaan en welke huidige fysieke werkelijkheid daarmee verbonden is.

Per kandidaat blijven afzonderlijk zichtbaar:
- fysieke identiteit;
- institutionele identiteit;
- historische identiteit;
- traditie;
- lineage;
- levende praktijk en continuïteit;
- actuele bezoekbaarheid;
- getuigenissen.

Claims krijgen per laag een bewijsstatus. Er bestaat geen totaalscore.

Babaji wordt niet behandeld als klassiek biografisch bewijsprobleem. De pipeline onderzoekt welke lineage de relatie draagt, welke officiële bronnen dat zeggen en welke fysieke plek bij die levende traditie hoort. Hetzelfde principe voorkomt verkeerde vragen bij Krishna en andere mythische of bovennatuurlijke figuren.

## 5. Vijf verbeteriteraties

### Iteratie 1 — Van chat-pipeline naar GitHub-pipeline

Probleem: handmatig kopiëren, verloren tussenproducten en geen gedeelde voortgang.

Verbetering: GitHub is de enige inter-process communication. Elke rol schrijft een eigen faseversie en handoff. Mark activeert alleen run en rol.

### Iteratie 2 — Van vrije repositorylezing naar deterministische context

Probleem: verschillende modellen lezen verschillende bestanden, missen cruciale context of overschrijden het contextvenster.

Verbetering: iedere fase leest uitsluitend een gepind contextmanifest met required, optional en forbidden files, prioriteitsvolgorde, source commit en contextbudget.

### Iteratie 3 — Van één bewijsmodel naar claimtypen

Probleem: historische bewijsstandaarden verwijderden juist belangrijke lineage- en traditieplaatsen.

Verbetering: atomische claimtypen en aparte bewijsstatussen. Institutionele identiteit werd verplicht. Traditie, lineage en getuigenis worden kritisch maar volgens het juiste epistemische model onderzocht.

### Iteratie 4 — Van één groot rapport naar logisch volledige artifacts

Probleem: monsterbestanden veroorzaken afkapping, vergeten secties en slechte overdracht.

Verbetering: `report/INDEX.md` plus genummerde kleine rapportdelen, claims.jsonl, bronregister, audit, handoff en completion marker. Limiet: 1500 regels per primair bestand.

### Iteratie 5 — Van overtuigende afronding naar aantoonbare vrijgave

Probleem: een AI kan verklaren dat iets compleet is terwijl output afgekapt, bronloos of alleen in de chat staat.

Verbetering: claim-lock, state machine, append-only events, source-commit-pinning, eind-sentinels, artifactmanifest, herlezing vóór COMPLETED en GOUD-status PASS/PARTIAL/BLOCKED.

## 6. Waarom dit beter is

### Inhoudelijk

- Krachtplaatsen met levende traditie worden niet meer onterecht afgewezen wegens ontbrekend klassiek historisch bewijs.
- Historische claims worden niet minder kritisch; zij zijn alleen niet langer het enige geldige claimtype.
- Institutionele identiteit maakt ontdekkingen zoals Katyayani Peeth systematisch reproduceerbaar.
- Neem Karoli Baba en andere belangrijke lineages krijgen een volwaardige projectoverlay zonder te worden geforceerd in Kriya.
- Getuigenissen en het feit dat mensen een plek als bijzonder ervaren kunnen worden onderzocht zonder ze tot historische feiten te verheffen.

### Technisch

- Geen handmatig rapportkopiëren.
- Geen afhankelijkheid van chatgeheugen.
- Iedere fase en bron blijft zichtbaar.
- Context blijft klein, ook wanneer de repository groeit.
- Oude completed runs worden niet automatisch ingelezen.
- Afkapping en halve writes worden expliciet gedetecteerd.
- Een volgende rol weet exact welke versie en commit zij controleert.

### Bestuurlijk

- Alleen Mark beoordeelt A/B/C.
- De regisseur krijgt alleen het GOUD-dossier.
- India2, Claude, ChatGPT en andere bevoegde schrijvers kunnen later methodologie of rollen verbeteren zonder actieve runs stil te veranderen.

## 7. Bewust niet gebouwd

Voor ongeveer tien tot enkele tientallen runs zijn niet toegevoegd:
- externe database;
- middleware of contextresolver;
- complexe eventsegmentatie;
- automatische leases op basis van tijd;
- dubbele history-kopieën;
- bedrijfsbrede orchestration-infrastructuur.

GitHub, contextmanifesten en kleine artifacts zijn voldoende. Claims verlopen niet automatisch, omdat AI-sessies geen betrouwbare leasehouder zijn; een override vereist expliciete actie van Mark of controller.

## 8. Ingebruikname

1. Maak een run vanaf `pipeline/templates/RUN_TEMPLATE.md`.
2. Vul scope, controlelijst en contextmanifesten.
3. Activeer BRONS met de korte tekst uit `pipeline/START_PROMPTS.md`.
4. Na geldige BRONS-completion activeer ZILVER.
5. Na geldige ZILVER-completion activeer GOUD.
6. De regisseur leest alleen GOUD via manifest en rapportindex.

## 9. Eindoordeel

De pipeline is nu ontworpen als een klein maar robuust research operating system voor Marks werkelijke gebruik: ongeveer tien runs, meerdere AI-modellen, volledige GitHub-read/write en één einddossier per cluster. Zij vermijdt zowel promptchaos als onnodige bedrijfscomplexiteit.

END_OF_ARTIFACT

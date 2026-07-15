# INDIA2-architectuurbeoordeling — Pipeline 3.0

## Scope

Deze beoordeling behandelt uitsluitend de procesarchitectuur van BRONS–ZILVER–GOUD, SUBREGIE INDIA, INDIA2 en de repository. De inhoudelijke uitkomst van Vrindavan wordt niet opnieuw beoordeeld.

## Samenvattend besluit

`ACCEPTEREN MET GERICHTE VEREENVOUDIGINGEN`

Pipeline 3.0 is geschikt om nieuwe clusters te starten. De rolgrenzen zijn in hoofdzaak correct, GitHub-only overdracht werkt en de proportionaliteitsregel voorkomt dat het project verandert in een automatiseringsproject. Voor de eerste nieuwe run moeten enkele architectuurcorrecties worden uitgevoerd die weinig complexiteit toevoegen en concrete fouten of handwerk voorkomen.

---

## 1. Taakverdeling SUBREGIE INDIA en INDIA2

### Besluit: WIJZIGEN

### Goed

- INDIA2 bewaakt inhoudelijke koers, persoonlijke projectrelevantie en adviserend A/B/C.
- SUBREGIE INDIA bewaakt uitvoering, technische integriteit, context, transitions en structureel leren.
- Alleen Mark kent formele A/B/C toe.
- INDIA2 wordt niet belast met state-, hash-, connector- en claimproblemen.

### Wijziging

De huidige formulering dat INDIA2 het uiteindelijke mensentaalrapport maakt is te breed. Tijdens de beslisfase moet INDIA2 uitsluitend een compact beslisrapport maken op basis van `decision_inputs.md`. Een uitgebreide reisgids, kaartpresentatie of reisdagboekvorm wordt pas later ontworpen.

Vaste scheiding:

- `SUBREGIE INDIA`: maakt valide uitvoerbare runs, transitions, contextpakketten, validatie en post-run learning;
- `INDIA2`: bepaalt scopeprioriteit, beoordeelt methodologische voorstellen, maakt compacte beslissynthese en geeft adviserend A/B/C;
- `Mark`: besluit formeel A/B/C en reisrichting.

INDIA2 voert geen nieuw breed internetonderzoek uit om gaten van GOUD te repareren. Een ontbrekende beslisdragende laag gaat terug naar SUBREGIE als gerichte supplementopdracht.

---

## 2. Taakverdeling BRONS, ZILVER en GOUD

### Besluit: WIJZIGEN

### Goed

- BRONS detecteert breed en bouwt de eerste rijke kandidaatversie.
- ZILVER verifieert onafhankelijk, zoekt tegenspraak en corrigeert bron- en claimtypen.
- GOUD synthetiseert, controleert volledigheid en past de vrijgavepoort toe.

### Probleem

Alle drie rollen controleren nu bijna dezelfde volledige lijst van devotie, deelname, sfeer, beelden, reviews en nabijheid. Dat beschermt kwaliteit maar kan leiden tot driedubbel werk zonder evenredige winst.

### Wijziging

- BRONS verzamelt de volledige eerste set.
- ZILVER controleert alle dragende claims en gebruikt risicogestuurde steekproeven voor niet-dragende reviews en beelden, tenzij de kwaliteit twijfelachtig is.
- GOUD controleert registers, volledigheid en alleen de nog open of beslisdragende inhoud. GOUD herhaalt geen volledige beeld- of reviewsweep wanneer ZILVER deze expliciet heeft goedgekeurd.

Iedere laag krijgt in `handoff.yaml` een status `ACCEPTED`, `CORRECTED`, `OPEN` of `NOT_APPLICABLE`. De opvolger heropent alleen `OPEN`, `CORRECTED` met risico, of een gemotiveerde steekproef.

---

## 3. Continue verbeterlus

### Besluit: ACCEPTEREN

De beperkte post-run review met `NO_CHANGE`, `ROLE_CLARIFICATION`, `TEMPLATE_IMPROVEMENT`, `METHODOLOGY_PROPOSAL`, `TECHNICAL_FIX` en `DEFER_AUTOMATION` is proportioneel en voorkomt automatische protocolgroei.

### Aanscherping

Per volledige keten maximaal:

- één verplicht lessons-record;
- maximaal drie voorgestelde veranderingen;
- iedere verandering bevat concreet probleem, gemeten of aantoonbaar effect, kleinste oplossing en regressietest;
- wijzigingen worden gebundeld en niet na iedere kleine observatie direct in rollen of protocollen verwerkt.

Een succesvolle run zonder herhaalbare fout krijgt `NO_CHANGE`. Dit is een geldige en gewenste uitkomst.

---

## 4. Repositorystructuur

### Besluit: WIJZIGEN

De hoofdscheiding tussen `knowledge`, `pipeline`, `decisions` en `research/active` is bruikbaar. De hoeveelheid afzonderlijke protocolbestanden blijft beheersbaar zolang nieuwe functies eerst in bestaande bestanden worden verwerkt.

### Direct gevonden fout

Er bestaan twee verschillende besluiten met hetzelfde ID `DECISION-0008`:

- leesbare plaatsverwijzingen plus A-keuzes;
- herkenningshaken bij iedere plaatsnaam.

Dat is een reëel referentie- en auditrisico.

### Vereiste correctie

- Maak één `decisions/INDEX.yaml` met uniek ID, bestandspad, datum, status en eventuele `supersedes`-relatie.
- Voeg een eenvoudige validator toe die dubbele IDs, ontbrekende bestanden en verkeerde verwijzingen blokkeert.
- Hernoem één van de dubbele `DECISION-0008`-bestanden naar het eerstvolgende vrije besluitnummer en migreer alle verwijzingen atomair.

Geen nieuwe mappenstructuur nodig zolang deze index en validator bestaan.

---

## 5. Minimale context per rol

### Besluit: WIJZIGEN

De huidige context bevat terecht scope, Methodology, Evidence Protocol, Quality Gate, decisions en predecessorrapporten. Het risico is dat ieder metaal te veel algemene tekst ontvangt.

### Vereiste contextprofielen

- `BRONS_MIN`: scope, bekende ankers/statussen, detectoren, Methodology, Evidence Protocol, verplichte schemas.
- `ZILVER_MIN`: BRONS-handoff, claims/sources, scope, verificatieregels, alleen relevante decisions.
- `GOUD_MIN`: ZILVER-handoff, open/conflicted-register, quality gate, beslisinputtemplate.

Volledige oudere rapporten worden alleen gepind wanneer verliescontrole of inhoudelijke predecessorcontext dat vereist. Het manifest vermeldt per bestand waarom het nodig is. Bestanden zonder expliciete rolrelevantie worden niet opgenomen.

---

## 6. Minder handmatig plakwerk voor Mark

### Besluit: ACCEPTEREN

De universele activatiezin en één `NEXT_ACTION.yaml` verminderen handwerk sterk en zijn voor circa twintig sweeps eenvoudiger dan n8n of een multiworkerplatform.

### Verdere vereenvoudiging

Mark ontvangt na iedere fase exact:

- status;
- commit;
- maximaal drie gaten;
- één reeds ingevulde startzin.

De startzin hoeft geen run, rol of manifest te bevatten; `NEXT_ACTION.yaml` draagt die gegevens. SUBREGIE schrijft de volgende actie voordat het completionbericht wordt afgegeven.

Voor nu blijft het openen van een schone chat door Mark de enige handmatige stap. Verdere automatisering wordt pas overwogen wanneer dit aantoonbaar een terugkerende belasting wordt.

---

## 7. Onderdelen die overbodig zijn geworden

### Besluit: WIJZIGEN

Niet verwijderen:

- gepinde contextmanifesten;
- bronregisters;
- statecontrole;
- vaste transitions;
- technische SUBREGIE-validatie.

Vereenvoudigen:

1. **Claim-locks:** bij exact één actieve schrijvende worker kan een eenvoudige stateclaim met verwachte commit-SHA volstaan. Een uitgebreid lockcontract blijft alleen nodig wanneer echte parallelle writers worden toegestaan.
2. **Eventlogdetail:** bewaar alleen gebeurtenissen die nodig zijn om stateovergangen en fouten te reconstrueren. Geen duplicatie van informatie die al volledig in commit, state en handoff staat.
3. **Volledige hercontrole door ieder metaal:** vervangen door de risicogestuurde laagstatussen uit sectie 2.
4. **Technische chatdetails:** blijven uitsluitend in GitHub; Mark krijgt geen hashes, cursors of manifestdetails behalve bij een echte blokkade.

---

## 8. Onderdelen die ontbreken

### Besluit: WIJZIGEN

De volgende onderdelen ontbreken en leveren directe waarde:

- wereldwijd stabiel plaatsindexnummer;
- machineleesbaar centraal plaatsregister;
- unieke decision-index en collisionvalidator;
- expliciete clusterafhankelijkheden vóór A/B/C-besluit;
- gestandaardiseerde kaartuitvoer;
- bron- en praktischheidsverversingsdatum;
- gelijke documentatiediepte voor spirituele A, B en C, waarbij status planning bepaalt en niet dossierkwaliteit;
- uitgestelde PARELS-laag volgens `DECISION-0011`.

---

# Eigen architectuurverbeteringen van INDIA2

## A. Centraal plaatsregister

### Besluit: ACCEPTEREN

Maak één machineleesbaar register, bijvoorbeeld `knowledge/places/registry.jsonl`.

Per plaats minimaal:

- permanent wereldwijd indexnummer;
- canonical name en aliases;
- type;
- coördinaten plus nauwkeurigheidsstatus;
- cluster(s);
- spirituele status A/B/C en beslisbron;
- documentatiestatus;
- relevante overlays;
- laatste inhoudelijke en praktische verificatiedatum.

Het nummer verandert nooit. Rapporten, kaarten, foto's en routes verwijzen naar hetzelfde nummer.

## B. Decision-ID-validator

### Besluit: ACCEPTEREN

Blokkeer dubbele besluitnummers, ontbrekende `supersedes`-doelen en verwijzingen naar niet-bestaande besluiten. Dit voorkomt de reeds gevonden dubbele `DECISION-0008`.

## C. Contextbudget per rol

### Besluit: ACCEPTEREN

Ieder contextmanifest bevat:

- maximaal noodzakelijke bestanden;
- reden per bestand;
- verwachte taak van het bestand;
- omvang of regels als vroeg waarschuwingssignaal.

SUBREGIE weigert een contextpakket wanneer algemene achtergrond zonder rolnoodzaak groter is dan de feitelijke runcontext.

## D. Eén canonieke kandidaatrecordstructuur

### Besluit: ACCEPTEREN

Gebruik dezelfde vaste velden in BRONS, ZILVER en GOUD. Daardoor kan iedere volgende fase verschillen automatisch vergelijken zonder drie afwijkende rapportindelingen te interpreteren.

Vrije tekst blijft mogelijk voor devotionele betekenis, maar identiteit, bevestigingsdomeinen, praktijk, deelname, beelden, reviews, nabijheid en open controles krijgen vaste velden.

## E. Kaartuitvoer uit dezelfde bron

### Besluit: ACCEPTEREN

Genereer later vanuit het centrale plaatsregister minimaal:

- CSV voor Google My Maps;
- KML of GeoJSON;
- compacte kaartbeschrijving per pin.

A is groen, B oranje, C rood. Geen aparte handmatige kaartdatabase onderhouden. Kaart en rapport moeten dezelfde indexnummers en statusbron gebruiken.

## F. Versheidsregel

### Besluit: ACCEPTEREN

Scheid duurzame kennis van vluchtige praktische gegevens.

- lineage, traditie en historische identiteit: hercontrole alleen bij nieuwe tegenspraak;
- opening, toegang, wegconditie, reviews en reistijd: `checked_at` plus aanbevolen `recheck_before`.

Daarmee hoeft een volgende reiscontrole niet opnieuw het hele dossier te onderzoeken.

## G. Clusterbesluitpoort

### Besluit: ACCEPTEREN

INDIA2 geeft geen definitief advies over een routegevoelige B- of C-plek zolang bekende aangrenzende plaatsen of A-ankers niet voldoende zijn onderzocht. Het dossier vermeldt dan exact welke clusterinformatie nog ontbreekt.

Dit voorkomt herhaling van de situatie waarin Krishna Janmabhoomi in Mathura niet goed kon worden beoordeeld vóór onderzoek van de rest van Mathura/Braj.

---

# Eerste volgende run

## Besluit: AUTORISEREN

`BRAJ-COMPLETE` wordt de eerste nieuwe cluster-run.

Reden:

- de bestaande Vrindavan-data zijn bruikbare predecessorcontext;
- Mathura, Govardhan, Gokul, Barsana en Nandgaon kunnen routewaarde en dagclusters wezenlijk veranderen;
- bestaande formele A-ankers in Vrindavan maken een A-naar-rest-matrix direct beslisrelevant;
- afronding van Braj voorkomt verdere individuele beoordelingen op onvolledige clustercontext.

Voorwaarden vóór BRONS-activatie:

1. repareer de dubbele decision-ID;
2. maak een eerste centraal plaatsregister of minimaal het definitieve schema en nummeringsbeleid;
3. pas de contextprofielen en risicogestuurde handoffstatussen proportioneel toe;
4. wijzig geen voltooide Vrindavan-runartifacts;
5. activeer de PARELS-laag nog niet; deze blijft uitgesteld tot de pelgrimsroute vaststaat.

## Niet nu activeren

- `ARUNACHALA-TIRUVANNAMALAI`: scope mag voorbereid blijven, uitvoering na BRAJ-BRONS of wanneer de enkele-actieve-writerregel dit veilig toestaat.
- `KUMAON-BABAJI-KRIYA-NKB`: detector- en subclusterplan voorbereiden, maar geen megasweep starten voordat Braj de nieuwe architectuur praktisch heeft getest.

END_OF_ARTIFACT
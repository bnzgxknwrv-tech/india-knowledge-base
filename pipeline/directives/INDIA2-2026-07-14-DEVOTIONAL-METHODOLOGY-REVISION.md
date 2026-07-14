# INDIA2 -> SUBREGIE INDIA — devotionele methodologiecorrectie

## Status

`READY_FOR_SUBREGIE_IMPLEMENTATION`

## Gezaghebbend besluit

Lees en implementeer volledig:

`decisions/DECISION-0005-tradition-confirmation-devotional-reporting-and-advisory-ratings.md`

## Aanleiding

De Vrindavan-integratie- en aanvullingsrun hebben technisch en bronmatig goed gewerkt, maar de projectinterpretatie en mensentaalrapportage zijn te juridisch geworden. De pipeline behandelt lineage-, traditie- en AOAY-relaties nog te vaak als zwakke of onvoltooide versies van onafhankelijk historisch bewijs. Dat past niet bij Marks pelgrimsdoel.

Voor Mark is gezaghebbende, intern consistente overlevering van belangrijke swami's, directe leerlingen, officiële ashrams, trusts en guru-parampara's zelfstandige bevestiging. Dit moet zichtbaar worden zonder historische documentatie en traditie op één hoop te gooien.

## Opdracht

Voer een structurele pipeline- en methodologie-update uit voor toekomstige runs. Wijzig geen reeds gepinde of voltooide onderzoeksoutput.

Minimaal aanpassen:

1. `knowledge/methodology/METHODOLOGY_V2.md`
2. `pipeline/protocols/EVIDENCE_PROTOCOL.md`
3. `pipeline/QUALITY_GATE.md`
4. `pipeline/roles/BRONS.md`
5. `pipeline/roles/ZILVER.md`
6. `pipeline/roles/GOUD.md`
7. `pipeline/roles/SUBREGIE_INDIA.md`
8. relevante rapport- en runtemplates
9. `pipeline/VERSION.md`
10. eventuele projectoverlays die nog standaard naar een historisch bewijsmodel terugvallen

## Vereiste inhoudelijke wijzigingen

### A. Twee gelijkwaardige bevestigingsdomeinen

Maak expliciet onderscheid tussen:

- historische/documentaire bevestiging;
- institutionele bevestiging;
- lineagebevestiging;
- traditiebevestiging;
- ervaringsgerichte bezoekersmeldingen;
- actuele praktische verificatie.

Lineage- en traditiebevestiging zijn geen inferieure vormen van historische bevestiging. Zij beantwoorden een andere vraag.

Voeg machineleesbare statussen toe of herstructureer het claimmodel zodat ten minste zichtbaar kan zijn:

- `HISTORICALLY_DOCUMENTED`
- `INSTITUTIONALLY_CONFIRMED`
- `LINEAGE_CONFIRMED`
- `TRADITION_CONFIRMED`
- `EXPERIENTIALLY_REPORTED`
- `PRACTICAL_CHECK_REQUIRED`

De precieze namen mogen technisch worden verbeterd, maar de semantiek mag niet worden afgezwakt.

### B. Babaji-regel

Verwijder iedere impliciete vraag naar klassieke biografische bewijsbaarheid van Mahavatar Babaji.

Een Babaji-plaats wordt onderzocht via:

- getuigenis van belangrijke swami's en lijnhouders;
- directe leerlingen en guru-parampara;
- officiële lineagegeschiedenis;
- onderlinge consistentie van de overlevering;
- de fysieke plek en levende praktijk die daaruit zijn voortgekomen.

Een geloofwaardige directe lijnbron telt voor Marks project als bevestiging.

### C. AOAY-regel

Herzie de huidige dubbele-verificatieregel.

Een gecontroleerde editie en exacte historische perceelsidentificatie blijven nuttig voor documentair detail, maar zijn niet langer de enige poort naar projectbevestiging.

Wanneer:

1. AOAY een relevante persoon, ontmoeting of Vrindavan-relatie beschrijft; en
2. de huidige officiële instelling of lineage de eigen fysieke plek met die relatie identificeert;

is de plek voor Marks reisdoel `PROJECT_CONFIRMED`, tenzij concrete tegenspraak bestaat.

Rapporteer wie de koppeling draagt en hoe sterk deze is. Gebruik niet automatisch `POSSIBLE` alleen omdat moderne juridische locatiezekerheid ontbreekt.

### D. Devotionele onderzoekslaag

Maak per kandidaat verplicht:

- waarom devotees hierheen gaan;
- wie of wat zij er vereren;
- welke spirituele behoefte of welk ideaal centraal staat;
- wat zij er concreet doen;
- welke rituelen een respectvolle bezoeker zelf kan volgen;
- of buitenlandse, niet-hindoeïstische of niet-ingewijde spirituele bezoekers welkom zijn;
- hoe deelname werkt;
- etiquette, kleding, fotografie, stilte en donaties;
- hoe de sfeer terugkerend wordt beschreven.

Sta voor sfeer en gastvrijheid zorgvuldig geselecteerde ervaringsbronnen toe, waaronder devotees, bezoekersverslagen, interviews en video's. Label deze als ervaringsmateriaal; sluit ze niet uit omdat zij geen historische kernbron zijn.

### E. Marks rapporttemplate

Verplicht deze volgorde per plek:

1. Wat voor plaats is dit?
2. Waarom devotees hierheen gaan.
3. Wat mensen er doen.
4. Kan Mark meedoen en zich welkom voelen?
5. Sfeer.
6. Historische, institutionele, lineage- en traditiebevestiging.
7. Praktische controles vlak voor of tijdens het bezoek.
8. Adviserend A/B/C met reden.

Waarschuwingen en beheeronzekerheden mogen de spirituele betekenis niet domineren.

### F. Adviserend A/B/C

Behoud Marks exclusieve bevoegdheid om formele A/B/C-statussen toe te kennen.

Sta INDIA2 echter toe om per kandidaat `ADVIES A`, `ADVIES B` of `ADVIES C` te geven met een concrete inhoudelijke reden. Dit advies wijzigt geen `LOCKED_A.md`, `LOCKED_B.md`, andere statusbestanden of projectrecords zonder Marks expliciete besluit.

BRONS, ZILVER en GOUD verzamelen hiervoor wel de benodigde informatie, maar kennen zelf geen advies of status toe, tenzij INDIA2 dit voor een specifieke eindrapportage expliciet opdraagt.

### G. Taal

Verwijder systeemjargon uit Marks rapporten.

Gebruik bijvoorbeeld:

- `heilige vijver of ritueel waterbekken (kund)`;
- `pelgrimsrondgang (parikrama)`;
- `samadhi-heiligdom` of `vereerde laatste rustplaats`;
- `spirituele lerarenlijn (lineage)`;
- `levende devotionele praktijk`.

## Regressiecontrole

Gebruik de acht kandidaten uit de twee Vrindavan-runs als regressieset. Controleer dat een nieuw mensentaalrapport:

- de devotionele reden per plek als eerste zichtbaar maakt;
- beschrijft wat mensen er doen;
- gastvrijheid en deelname onderzoekt;
- Katyayani Peeth niet langer onnodig degradeert door advocaat-achtige AOAY-eisen;
- lineageclaims van belangrijke swami's als projectbevestiging kan behandelen;
- praktische onzekerheden wel behoudt maar niet laat overheersen;
- adviserend A/B/C kan leveren zonder Marks formele statusrechten te schenden.

## Uitvoer

1. Schrijf de volledige methodologie- en pipelinewijziging naar GitHub.
2. Verhoog de relevante versies.
3. Leg uit welke oude regels zijn vervangen.
4. Maak een nieuw voorbeeldrapport of templatefragment voor ten minste Katyayani Peeth, Neem Karoli Baba Ashram en Radha Kund.
5. Werk `pipeline/NEXT_ACTION.yaml` na voltooiing bij naar de juiste volgende bestemming.
6. Routeer het technisch en inhoudelijk samengevatte resultaat terug naar INDIA2.

Ken tijdens deze implementatie geen formele A/B/C-status toe.

END_OF_ARTIFACT
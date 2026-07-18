# INDIA2 STRATEGISCHE REVIEW — MINIMALE BRONS → ZILVER → GOUD-KETEN

Repository: `bnzgxknwrv-tech/india-knowledge-base`

Branch: `implementation/minimal-bzg-handoff`

Gereviewde PR: `#15 — Implement minimal BRONS → ZILVER → GOUD handoff`

Gereviewde branch-head vóór deze review: `2ed51f2805ee5c94ff20d07a0e781f5387281943`

Gelezen en meegewogen:

- de volledige actuele PR #15-diff;
- `pipeline/reviews/CLAUDE_REVIEW_MINIMAL_BZG_HANDOFF_IMPLEMENTATION.md`;
- `pipeline/reviews/CLAUDE_REREVIEW_MINIMAL_BZG_HANDOFF_IMPLEMENTATION.md`;
- de aangepaste rol-, controller-, state-, handoff- en rapporttemplates;
- `MARK_FINAL_REPORT_TEMPLATE.md`;
- `CANONICAL_INTEGRATION_PROPOSAL_TEMPLATE.md`;
- de synthetische rooktest A–M;
- de bestaande taakverdeling tussen Mark, INDIA2, SUBREGIE INDIA, BRONS, ZILVER en GOUD.

Geen productiesweep uitgevoerd. Geen rooktest uitgevoerd. Geen implementatiebestand gewijzigd. PR #15 niet gemerged en niet uit draft gehaald.

## STRATEGISCH_BESLUIT: ACCEPT

## READY_FOR_SMOKE_TEST: YES

De aangepaste PR #15 is niet alleen technisch maar ook inhoudelijk en strategisch geschikt voor Marks resterende India-sweeps.

De juiste taakverdeling is voortaan:

```text
INDIA2 bepaalt vooraf de inhoudelijke richting, scope, ankers en beslisvraag
        ↓
BRONS detecteert breed binnen die vastgelegde scope
        ↓
ZILVER controleert en verbetert onafhankelijk
        ↓
GOUD synthetiseert, integreert alleen niet-beslissende kennisbasisgegevens
        ↓
GOUD levert rechtstreeks het volledige rapport aan Mark
```

INDIA2 hoeft bij een normale geldige run niet opnieuw het hele dossier te lezen of het GOUD-rapport te herschrijven. Dat zou opnieuw wachttijd toevoegen zonder normale kwaliteitswinst.

Er blijft wel een vaste strategische controlepoort bestaan. Die poort is conditioneel en is al voldoende aanwezig in het huidige ontwerp via:

- `VOOR_INDIA2` voor echte cross-run koerskeuzes;
- `MARK_DECISION_REQUIRED` voor besluiten die alleen Mark mag nemen;
- de verplichte `Aanbevolen vervolgstap` in het Markrapport;
- het verbod voor GOUD om nieuwe A/B/C-statussen, decision-ID’s of koersbesluiten te creëren;
- het verbod om een niet-deterministische canonieke wijziging stil toe te passen.

Deze poort betekent dus niet dat INDIA2 na iedere sweep automatisch terugkomt. Zij wordt alleen geactiveerd wanneer de uitkomst de grenzen van één run overschrijdt.

---

## 1. Ben ik tevreden met de nieuwe taakverdeling?

**JA.**

De taakverdeling sluit beter aan op de werkelijke competenties van iedere rol:

- INDIA2 bepaalt vooraf wat er voor Marks reis werkelijk onderzocht moet worden en welke vraag de sweep moet beantwoorden;
- BRONS zoekt breed zonder selectiebevoegdheid;
- ZILVER valt de inhoud onafhankelijk aan;
- GOUD maakt het dossier compleet en presenteert het bruikbaar;
- Mark blijft de enige formele beslisser over A/B/C en concrete reisvoorkeuren;
- SUBREGIE blijft beschikbaar voor technische blokkades, maar is geen standaard tussenstation meer.

Dit vermindert wachttijd zonder de inhoudelijke scheiding tussen de metalen op te heffen.

De inline controllerrol na BRONS en ZILVER is inhoudelijk neutraal. Zij controleert completion, claims, state, events en contextpinning, maar mag geen onderzoeksconclusies wijzigen. Daarmee blijft de overgang een technische poort en wordt zij geen verborgen vierde inhoudelijke rol.

---

## 2. Kan GOUD een volledig genoeg rapport voor Mark leveren zodat normale INDIA2-eindredactie vervalt?

**JA.**

Het actuele `MARK_FINAL_REPORT_TEMPLATE.md` bevat voldoende inhoud om Mark zonder normale INDIA2-eindredactie te laten beslissen:

- rechtstreeks antwoord op de centrale vraag;
- alle locaties en afwijzingen;
- relatie met Marks lijn, TOP_X, AOAY of INDIA ESSENTIAL;
- het type fysieke relatie;
- praktische deelname en sfeer;
- routewaarde, omweg, GEO en kaartinformatie wanneer relevant;
- belangrijkste wijzigingen door ZILVER en GOUD;
- beslisrelevante open punten;
- één aanbevolen vervolgstap;
- canonieke integratiestatus;
- technische eindcontrole.

Dit is inhoudelijk sterker dan een kort technisch GOUD-completionbericht en voldoende zelfstandig om de normale rapportagefunctie van INDIA2 te vervangen.

GOUD vervangt daarmee uitsluitend de normale eindredactie van één run. GOUD vervangt niet de cross-run regierol van INDIA2.

---

## 3. Blijft INDIA2’s rol als bewaker van inhoudelijke hoofdkoers en cross-runstrategie voldoende beschermd?

**JA.**

Die rol blijft beschermd doordat:

1. INDIA2 de nieuwe run en de scope vooraf bepaalt;
2. een metaal de scope of methodologie tijdens de run niet mag veranderen;
3. GOUD geen nieuwe formele of adviserende A/B/C-status mag creëren;
4. GOUD geen nieuwe decision-ID of beslistekst mag creëren;
5. GOUD alleen deterministische, niet-beslissende kennisbasisintegratie mag uitvoeren;
6. `VOOR_INDIA2` behouden blijft voor echte cross-run koerskeuzes;
7. oude of actieve runs niet stil naar het nieuwe model worden gemigreerd.

INDIA2 moet bij het ontwerpen van iedere nieuwe sweep wel consequent de actuele reiscontext in de scope opnemen. Binnen de bestaande scopevelden is daarvoor voldoende ruimte. Minimaal moeten zichtbaar zijn:

- de bestaande formele A-ankers;
- het beoogde volgende cluster of traject;
- de centrale beslisvraag;
- Marks relevante TOP_X-, lineage- en AOAY-interpretatie;
- de drempel voor omweg, tussenstop of overnachting wanneer routewaarde in scope is;
- welke eerdere besluiten niet opnieuw ter discussie staan.

Dit is een uitvoeringsdiscipline voor INDIA2 en vraagt geen extra protocolwijziging in PR #15.

---

## 4. Is de voorgestelde bevoegdheidsscheiding juist?

**JA.**

### Technische en deterministische integratie door GOUD

GOUD mag mechanisch vastleggen wat één-op-één uit de gevalideerde run volgt, bijvoorbeeld:

- documentstatus;
- artifactpaden;
- bestaande LOCATION_ID-koppelingen;
- gecontroleerde aliases;
- GEO-statussen;
- verwijzingen naar reeds bestaande decisions;
- bestaande A/B/C-statussen exact ongewijzigd overnemen.

### Nieuwe A/B/C- of koersbesluiten door Mark

Alle nieuwe of gewijzigde formele A/B/C-statussen blijven bij Mark. Ook routekeuzes, het wel of niet overnachten en de persoonlijke betekenis van een kandidaat blijven besluiten van Mark wanneer de scope daar geen vooraf vastgelegde objectieve eindregel voor bevat.

### Echte cross-runstrategie door INDIA2

INDIA2 blijft nodig wanneer de uitkomst gevolgen heeft voor meer dan de huidige run, bijvoorbeeld voor:

- de volgorde van meerdere toekomstige clusters;
- de totale reisduur of routearchitectuur;
- de betekenis of toepassing van TOP_X, lineage of INDIA ESSENTIAL;
- wijziging van een eerdere methodologische keuze;
- samenvoeging, opsplitsing of heropening van meerdere runs;
- conflicten tussen resultaten uit verschillende clusters.

Deze scheiding is inhoudelijk juist en voorkomt dat een lokaal GOUD-dossier ongemerkt de totale projectkoers bepaalt.

---

## 5. Ontbreken er inhoudelijke onderdelen in het GOUD-eindrapport die INDIA2 normaal zou toevoegen?

**Geen blokkerende onderdelen ontbreken.**

Het huidige template bevat de beslisrelevante onderdelen die Mark nodig heeft. Vier accenten moeten door INDIA2 wel zorgvuldig in iedere scope worden geactiveerd wanneer ze voor die run relevant zijn:

1. **Waarom deze plek voor Mark belangrijk is en niet alleen voor de traditie.**
2. **Waarom dit een omweg of overnachting wel of niet rechtvaardigt.**
3. **Wat Mark werkelijk zou missen als hij de plek overslaat.**
4. **Of de vondst alleen lokaal relevant is of de totale reis beïnvloedt.**

Deze onderwerpen passen al binnen secties 4, 5, 6, 7 en 10 van het Markrapport. Er is daarom geen nieuw rapporthoofdstuk nodig.

---

## 6. Moet GOUD per locatie nog andere informatie leveren?

De huidige verplichte locatievelden zijn voldoende, mits GOUD ze werkelijk beslisgericht invult.

Per locatie zijn voor Mark vooral essentieel:

- permanente LOCATION_ID;
- herkenbare naam en fysiek type;
- concrete ligging met WORKING_GEO of VERIFIED_GEO;
- directe relatie met Marks lijn, TOP_X, AOAY of INDIA ESSENTIAL;
- relatietype;
- waarom devotees gaan en wat zij doen;
- of Mark waarschijnlijk kan deelnemen;
- sfeer, drukte en praktische frictie;
- routewaarde;
- globale extra reistijd of afstand;
- belangrijkste onzekerheid;
- concrete betekenis voor Marks beslissing.

De relatietypen in het template zijn strategisch belangrijk:

- `DIRECT_FYSIEK_ANKER`;
- `DIRECTE_LINEAGE`;
- `CANONIEK_KERNOORD`;
- `REGIONALE_HOOFDPLEK`;
- `LOKALE_CONTEXT`.

Hierdoor kan een zeer kleine directe lineageplek terecht zwaarder wegen dan een bekende maar voor Mark minder relevante lokale tempel.

GOUD hoeft geen nieuwe adviesletter toe te kennen om toch duidelijk te schrijven welke plek routebepalend is, welke hoogstens een nabijgelegen extra is en welke veilig kan worden overgeslagen.

---

## 7. Zijn de vervolgstappen bij PASS, PARTIAL en BLOCKED inhoudelijk juist?

**JA, met de volgende interpretatie.**

### PASS

Rechtstreeks naar Mark. Geen normale INDIA2- of SUBREGIE-eindstap.

Mogelijke uitkomsten:

- `GEEN_VERVOLG_NODIG`;
- `CONTROLE_VOOR_VERTREK`;
- `CONTROLE_TER_PLAATSE`;
- `MARK_DECISION_REQUIRED` voor één helder formeel of persoonlijk besluit.

### PARTIAL

Ook rechtstreeks naar Mark wanneer het dossier betrouwbaar bruikbaar is en de open punten de hoofdconclusie niet kunnen omkeren.

Terug naar INDIA2 is alleen nodig wanneer een open punt mogelijk:

- de volgorde van clusters verandert;
- een extra overnachting of grote omweg veroorzaakt;
- een eerdere cross-runbeslissing ondermijnt;
- een nieuwe aanvullende sweep met bredere scope nodig maakt;
- de interpretatie van Marks lijn of prioriteiten verandert.

### BLOCKED

Een technische blocker gaat naar SUBREGIE INDIA.

Een inhoudelijke of cross-run blocker gaat naar INDIA2.

GOUD mag bij BLOCKED geen schijnbaar definitief reisadvies presenteren.

---

## 8. Bestaat het risico dat iedere GOUD-run lokaal correct is maar de totale Indiareis uit beeld raakt?

**JA, dat risico bestaat in theorie bij iedere opgesplitste onderzoeksarchitectuur. Het huidige model beheerst het voldoende.**

De belangrijkste bescherming is dat INDIA2 vooraf de scope en centrale vraag bepaalt. Een lokale run mag niet zelfstandig bepalen waar de totale route daarna heen gaat, tenzij die routevraag expliciet in scope is opgenomen.

De conditionele strategische controlepoort moet worden geactiveerd wanneer een resultaat buiten zijn eigen run effect heeft.

INDIA2 blijft daarom verantwoordelijk voor periodieke cross-run beslissingen, maar niet voor het herschrijven van ieder afzonderlijk rapport.

Een praktische regel is:

> GOUD beslist binnen de gepinde run. INDIA2 beslist over de verhouding tussen runs.

Dat is de juiste grens.

---

## 9. Wanneer moet een resultaat verplicht terug naar INDIA2?

Een resultaat gaat verplicht naar INDIA2 wanneer minimaal één van deze situaties bestaat:

1. de uitkomst verandert de geplande volgorde van twee of meer clusters;
2. een nieuwe kandidaat kan een afzonderlijk cluster, overnachting of substantiële omweg veroorzaken;
3. een eerder vastgesteld cluster blijkt inhoudelijk overbodig of moet opnieuw worden geopend;
4. twee runs bevatten conflicterende identiteit, LOCATION_ID, lineage- of routeconclusies;
5. een nieuwe interpretatie van TOP_X, AOAY, Babaji/Krishna of een andere inhoudelijke prioriteit nodig is;
6. een methodologie-, bewijs- of classificatieregel moet worden gewijzigd;
7. meerdere gekoppelde formele beslissingen van Mark moeten in één samenhangend reisbesluit worden gebracht;
8. een canonical-integratievoorstel niet deterministisch is omdat het gevolgen heeft voor eerdere of toekomstige runs;
9. de totale reisduur, corridor of geografische hoofdstructuur moet worden herzien;
10. GOUD kan de centrale onderzoeksvraag niet beantwoorden zonder scope-uitbreiding buiten zijn gepinde run.

Niet verplicht naar INDIA2:

- één eenvoudige A/B/C-keuze door Mark;
- een openingstijd vlak voor vertrek;
- een lokale toegangsvraag;
- een kleine kaartcorrectie;
- een deterministische registry-update;
- een normaal PASS- of bruikbaar PARTIAL-rapport.

---

## 10. Aanvullingen waarmee Mark minder hoeft te wachten zonder kwaliteitsverlies

Geen verplichte wijziging aan PR #15 is nodig vóór de rooktest.

De volgende werkwijze geldt als strategische uitvoeringstoepassing:

1. INDIA2 maakt de scope volledig genoeg zodat de metalen geen tussenvraag hoeven te stellen.
2. Iedere scope bevat de actuele A-ankers en de exacte centrale beslissing.
3. GOUD geeft het antwoord vooraan en gebruikt technische informatie pas later in het rapport.
4. `VOOR_INDIA2` wordt alleen gebruikt voor de tien situaties uit sectie 9.
5. Een simpele Markbeslissing gaat rechtstreeks naar Mark en niet via INDIA2.
6. Een PARTIAL-run wordt niet automatisch als mislukt behandeld wanneer de hoofdkeuze betrouwbaar is.
7. Kaart- en routeonderzoek gebruikt praktische WORKING_GEO; een exacte ingang blokkeert geen grove afstandsbeslissing.
8. De KML of kaartdataset wordt direct door GOUD geleverd wanneer dit expliciet in scope staat.
9. C- en contextlocaties blijven geregistreerd, maar mogen het hoofdrapport niet domineren.
10. INDIA2 voert pas na meerdere relevante sweeps een aparte route- of reisbrede integratieronde uit wanneer daar werkelijk een beslisvraag voor bestaat.

---

## Strategische controlepoort

Een kleine vaste strategische controlepoort blijft noodzakelijk, maar niet als extra standaardchat.

De poort is:

```text
Heeft de uitkomst alleen gevolgen binnen deze run?

JA → GOUD levert rechtstreeks aan Mark.

NEE → GOUD levert het volledige rapport aan Mark én routeert uitsluitend het concrete cross-runbeslispunt naar INDIA2.
```

De huidige combinatie van `VOOR_INDIA2`, `MARK_DECISION_REQUIRED`, `Aanbevolen vervolgstap` en de beperkte canonieke writescope implementeert deze poort voldoende. Er is geen extra verplichte INDIA2-eindredactie nodig.

---

## Inhoudelijke en strategische verbeteringen

De volgende punten zijn bevestigingen en gebruiksregels, geen verplichte implementatieblokkades:

1. Scopeer iedere run vanuit Marks A-ankers en hoofdinteresse, niet vanuit algemene regionale volledigheid alleen.
2. Leg bij brede figuren zoals Krishna vast in welke hoedanigheid zij voor Mark relevant zijn.
3. Gebruik `INDIA ESSENTIAL` uitsluitend voor werkelijk nationale of mondiale kernplaatsen.
4. Laat lokale contextlocaties zichtbaar blijven zonder ze routebepalend te maken.
5. Beoordeel routewaarde primair op extra tijd en logistiek, niet op kilometers alleen.
6. Gebruik WORKING_GEO voor kaart- en clusterbeslissingen; reserveer exact ingangsonderzoek voor navigatie wanneer nodig.
7. Laat GOUD expliciet antwoorden of een plek een zelfstandige reisreden is.
8. Laat PARTIAL rechtstreeks bruikbaar zijn wanneer de resterende gaten de hoofdkeuze niet veranderen.
9. Activeer INDIA2 alleen bij de cross-runtriggers uit sectie 9.
10. Plan een reisbrede integratieronde pas wanneer meerdere clusters inhoudelijk gereed zijn.

## Exacte verplichte wijzigingen

`GEEN.`

De ene door Claude genoemde kleine documentatie-inconsistentie — `SYNTHETIC_TEST` ontbreekt nog in de voorbeeld-enum van `RUN_TEMPLATE_V3.md` — is technisch en niet strategisch. Zij mag tijdens de voorbereiding of uitvoering van de synthetische rooktest worden hersteld en hoeft de rooktest niet te blokkeren.

---

## Bevestiging isolatie echte runs

Volgens de actuele PR-diff en Claudes herreview zijn onaangeraakt:

- de echte actieve onderzoeksruns;
- `pipeline/NEXT_ACTION.yaml` op main;
- `knowledge/places/registry.jsonl`;
- `decisions/INDEX.yaml`.

De bestaande `VRINDAVAN-KUMAON-CORRIDOR-001`-run blijft haar oude gepinde schema-v2-proces volgen.

---

## Definitieve consensus

- STRATEGISCH_BESLUIT: `ACCEPT`
- tevreden met het model: `JA`
- GOUD kan normale INDIA2-eindredactie vervangen: `JA`
- vaste strategische controlepoort nodig: `JA`, maar uitsluitend conditioneel en niet als standaard eindredactie
- verplichte implementatiewijzigingen vóór rooktest: `GEEN`
- READY_FOR_SMOKE_TEST: `YES`

De eerstvolgende geldige stap is uitsluitend de synthetische `PIPELINE-HANDOFF-SMOKE-001`. PR #15 blijft draft en wordt pas na alle tests PASS en `PRODUCTION_READY: YES` mergeklaar.

END_OF_ARTIFACT
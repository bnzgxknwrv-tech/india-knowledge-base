# MARK_FINAL_REPORT_TEMPLATE v1.0

Bestand voor iedere geldige GOUD-oplevering:

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
- wat bewust niet opnieuw is onderzocht.

## 4. Belangrijkste uitkomst voor Mark

- wat Mark binnen deze scope absoluut niet moet missen;
- welke bestaande formele A/B/C-statussen relevant zijn;
- welke locaties geen routebepalende betekenis hebben;
- welke plaats een omweg of overnachting wel of niet rechtvaardigt;
- bij routeonderzoek: het duidelijke doorgaande advies.

Alleen Mark kent nieuwe formele A/B/C-statussen toe. GOUD presenteert alleen bestaande formele statussen en de door de run toegestane inhoudelijke conclusie.

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
- waarom dit geen routebepalende plek is;
- of dit alleen een nabijgelegen contextstop is;
- waarom overslaan waarschijnlijk geen gemiste hoofdkans is.

## 7. Route, kaart en praktische GEO

Wanneer in scope:

- belangrijkste routecorridors;
- grote stations of steden;
- ruwe reistijdklassen;
- werkelijke omwegen;
- logische tussenstop ja/nee;
- KML- of kaartartifactpad;
- uitleg van WORKING_GEO versus VERIFIED_GEO;
- geen schijnprecisie.

Een ontbrekende exacte ingang blokkeert geen praktische kaart wanneer adres, gebouwcentrum of representatief kaartpunt voldoende is voor cluster- en routebeslissing.

## 8. Wat ZILVER en GOUD hebben gewijzigd

- belangrijkste bevestigingen;
- belangrijke correcties;
- verwijderde dubbelingen;
- verworpen claims;
- opgeloste of resterende identity-conflicten;
- uitsluitend beslisrelevante wijzigingen, geen volledige technische changelog.

## 9. Open punten

Beperk dit tot beslisrelevante gaten:

- wat is niet vastgesteld;
- waarom niet;
- gevolg voor de keuze;
- moet dit vóór vertrek, ter plaatse of niet meer worden gecontroleerd?

## 10. Bron- en bewijsstatus

Compact overzicht van:

- primaire en institutionele bronnen;
- lineage- en traditiebronnen;
- actuele bezoekbaarheids- en vervoersbronnen;
- conflicten of zwakke bronlagen.

## 11. Technische eindcontrole

- BRONS geldig afgerond: `<JA|NEE>`
- BRONS -> ZILVER-transition geldig: `<JA|NEE>`
- ZILVER geldig afgerond: `<JA|NEE>`
- ZILVER -> GOUD-transition geldig: `<JA|NEE>`
- GOUD geldig afgerond: `<JA|NEE>`
- contextmanifesten gepind: `<JA|NEE>`
- required artifacts compleet: `<JA|NEE>`
- source-ID's resolveerbaar: `<JA|NEE>`
- state/events synchroon: `<JA|NEE>`
- finale readback geslaagd: `<JA|NEE>`

## 12. Geschreven eindproducten

- hoofdrapport:
- kandidaten- of locatieregister:
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

De chatuitvoer van GOUD moet inhoudelijk gelijk zijn aan het gecommitte rapport. Technische jargonlagen horen alleen in sectie 11 en 12; het eindantwoord en de locatiebeschrijvingen zijn zelfstandig leesbaar voor Mark.

END_OF_ARTIFACT
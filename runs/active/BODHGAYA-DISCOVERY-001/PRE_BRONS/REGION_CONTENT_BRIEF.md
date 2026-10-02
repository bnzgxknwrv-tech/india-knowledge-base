# PRE-BRONS Region Content Brief — Bodh Gaya

run_id: BODHGAYA-DISCOVERY-001
geschreven_op: 2026-08-03
geschreven_door: CCI

Deze regio start volledig blanco, volgens `india4/protocols/INDIA5_REGION_START_PROTOCOL.md`.
Geen Varanasi-kandidaten, -aannames of -detectoren zijn overgenomen. Alle hieronder genoemde
detectoren zijn nieuw voor deze regio geïntroduceerd (per-run PROVISIONAL, prefix `DET-BGY-`),
ook wanneer een detector conceptueel lijkt op een eerder in Varanasi gebruikte richting.

## Gebiedsgrens

Bodh Gaya (Mahabodhi-tempelcomplex als centrumpunt) + straal van circa 20 km, met een
uitsluitend signalerende blik tot circa 30 km voor uitzonderlijke "zou zonde zijn geweest"-
locaties (conform stap 2 van het startprotocol). Exacte kernstraal-coördinaten en precieze
afstanden tot randlocaties (bijvoorbeeld de Dungeshwari-grotten, Gaya-stad) worden tijdens
Discovery met een kaartbron geverifieerd — in deze PRE-BRONS-fase nog niet vastgesteld, alleen
globaal benoemd. Grotere, bekende locaties die duidelijk buiten elke redelijke straal liggen
(Nalanda, Rajgir, de Barabar-grotten) worden voorlopig als buiten scope beschouwd, te bevestigen
tijdens Discovery, niet nu al definitief uitgesloten.

## Marks bekende interesses en ankers

- Boeddha staat op positie 7 van Marks vaste 13-persoonsindex (`PRIORITY_GROUPS.md`, commit
  `709fafe`).
- Diezelfde bron vermeldt expliciet een bestaand precedent: "Bodh Gaya werd een A-cluster puur
  door de kracht van de plek zelf" — een reeds vastgelegde, hoge persoonlijke waardering van Mark
  voor Bodh Gaya als geheel, van vóór de huidige granulaire kandidaat-tracking.
- Dit is GEEN vrijbrief om elke afzonderlijke locatie in Bodh Gaya automatisch A te maken: elke
  gedecomponeerde kandidaat doorloopt nog steeds zelfstandig de NOT_TO_BE_MISSED-poort. De index/
  het precedent is een weegfactor en een signaal om goed te kijken, geen automatische waardering
  (PRIORITY_GROUPS.md-regel: de index kent zelf geen waarderingen toe).
- Sarnath (Boeddha's eerste prediking) is al volledig verwerkt in de Varanasi-regio (006,
  029-034, allen A) — Bodh Gaya vertegenwoordigt het andere, apart te onderscheiden narratieve
  moment: de verlichting zelf. Geen overlap, geen samenvoeging tussen de twee regio's.
- Mark's eigen Kriya Yoga/Yogananda-lijn: geen bevestigde directe Bodh-Gaya-verbinding gevonden
  of aangenomen — expliciet te onderzoeken (zie DET-BGY-P004), niet vooraf te veronderstellen.

## Relevante tradities, lineages, personen, heilige landschappen en historische lagen

- **Boeddhisme** (Theravada/Mahayana/Vajrayana, internationaal vertegenwoordigd via de vele
  nationale kloosters) — de dominante traditie van het gebied, met de verlichtingsplek van
  Boeddha als centraal punt.
- **Hindoeïsme** (Gaya-stadsgebied, Vishnupad-tempel, Falgu-rivier) — binnen de straal aanwezig,
  nog niet onderzocht. Geen aanname vooraf over aan- of afwezigheid van NOT_TO_BE_MISSED-waarde;
  wordt actief bekeken (DET-BGY-P006), niet overgeslagen en niet geforceerd.
- **Kriya Yoga/Yogananda-lijn** — geen bevestigde connectie; expliciet te onderzoeken, niet aan
  te nemen puur omdat het een boeddhistisch centrum is.

## Toegepaste detectoren

Bibliotheek is leeg (geen ACTIVE detectoren) — alle zeven hieronder zijn nieuw geïntroduceerd als
PROVISIONAL voor deze regio (zie `PRE_BRONS_DETECTORS.jsonl`):

- `DET-BGY-P001` PRIMARY_ENLIGHTENMENT_SITE_DECOMPOSITION_DETECTOR — decomponeert het
  Mahabodhi-complex in zelfstandig te toetsen onderdelen (Vajrasana, Bodhi-boom-nakomeling,
  Animeshlochan Chaitya, Chankramana, Muchalinda-vijver, e.a.), zonder over- of onder-fragmentatie.
- `DET-BGY-P002` PRE_ENLIGHTENMENT_NARRATIVE_SITE_DETECTOR — Sujata's dorp, de Niranjana/Falgu-
  rivieroever, de Dungeshwari-grotten: eenmalige, plaatsgebonden gebeurtenissen vóór de
  verlichting.
- `DET-BGY-P003` INTERNATIONAL_MONASTERY_LIVING_TRADITION_DETECTOR — toetst elk internationaal
  klooster individueel op levende praktijk/uitzonderlijke ervaring, nooit als groep.
- `DET-BGY-P004` KRIYA_LINEAGE_TEXT_DETECTOR — controleert AOAY/Kriya-lijnbronnen op een
  eventuele, nog niet bevestigde Bodh-Gaya-verwijzing.
- `DET-BGY-P005` ARCHAEOLOGICAL_ASI_DETECTOR — de archeologische/ASI-beschermde laag, los van de
  levende religieuze functie.
- `DET-BGY-P006` NON_BUDDHIST_IN_RADIUS_DETECTOR — bewuste blik op niet-boeddhistische tradities
  binnen de straal (met name het Gaya/Vishnupad-gebied), zonder categorie te forceren.
- `DET-BGY-P007` INSIDER_LOCAL_PRACTICE_SOURCE_DETECTOR — bron-kwaliteitsfilter, geen
  ontdekkingsdetector: kernclaims over levende praktijk mogen niet uitsluitend op reisblogs
  steunen.

## Geplande bronfamilies

Zie `SOURCE_FAMILY_PLAN.jsonl`. Gepland: UNESCO-bron (whc.unesco.org, voor het Mahabodhi-complex
als werelderfgoed), academische bronnen, religieuze naslagbronnen (Pali-canon, Ashokavadana),
primaire historische reisverslagen (Xuanzang/Hiuen Tsang, 7e eeuw), officiële overheids-
toerismebronnen, encyclopedie, reis-kruiscontrole, primaire AOAY-tekst. Nog niet beschikbaar:
lokale insider-/kloosterbron — zelfde structurele hiaat als bij Varanasi, hier vooraf al erkend
in plaats van pas achteraf.

## Bekende risico's/blinde vlekken

- Nog geen kaartbron-geverifieerde exacte straal/afstanden — volgt tijdens Discovery, niet nu al
  met zekerheid vastgesteld.
- Geen insider-/kloosterbron beschikbaar (zelfde structurele hiaat als Varanasi).
- Risico op verkeerde decompositie van het dichte Mahabodhi-complex — te grof (één vage
  koepelvermelding) of te fijn (kunstmatige deelkandidaten zonder zelfstandige waarde).
- Geen bevestigde Kriya-lijnverbinding met Bodh Gaya — moet apart geverifieerd worden, nooit
  aangenomen puur op basis van het algemene A-clusterprecedent uit PRIORITY_GROUPS.md.
- Sterke commerciële/toeristische druk rond de hoofdtempel kan het "beroemd-maar-oppervlakkig"-
  risico verhogen bij individuele kloosters of winkelgebieden rond de tempel.

## Verwachte kandidaatcategorieën / actief te onderzoeken richtingen

Geen vooraf verplichte categorieën — conform de hoofdvraag-regel (`NOT_TO_BE_MISSED_FRAMEWORK.md`)
is categorievolledigheid nooit een reden om te zoeken of toe te voegen. Wel actief te onderzoeken
richtingen, uitsluitend als zoekhulpmiddel, geen doel op zich:
- onderdelen van het Mahabodhi-complex zelf;
- pre-verlichtingsnarratiefplekken (Sujata-dorp, Dungeshwari-grotten, Niranjana/Falgu-oever);
- individuele internationale kloosters met een uitzonderlijk kenmerk;
- de archeologische/ASI-laag;
- eventuele niet-boeddhistische krachtplekken binnen de straal (Gaya/Vishnupad-gebied);
- een eventuele Kriya-lijnverbinding.

Een sweep die op nul, twee of twintig nieuwe kandidaten uitkomt is elk even geldig, zolang de
dekking aantoonbaar compleet is.

## Verzadigings- en stopcriteria

Zoals vastgelegd in `india4/protocols/INDIA5-PROTOCOL.md` en herbevestigd in
`INDIA5_REGION_START_PROTOCOL.md` stap 2: per detector minimaal twee wezenlijk verschillende
zoekbenaderingen en minimaal twee relevante bronfamilies, gevolgd door drie opeenvolgende
materieel verschillende richtingen zonder nieuwe high-value lead. Sweepniveau
`DISCOVERY_SATURATED` pas wanneer alle zeven detectoren een afsluitstatus hebben, alle geplande
bronfamilies zijn uitgevoerd of expliciet `ONBESCHIKBAAR`, en geen open lead redelijkerwijs een
dramatisch te missen locatie kan zijn.

## Dramatic miss check

**Vraag: welke dramatisch te missen A-locatie zou dit plan nog kunnen missen?**

Twee concrete risico's. Eerste: het Mahabodhi-tempelcomplex verkeerd decomponeren — als één
koepelnaam behandelen zou losse, verhaaltechnisch onderscheiden onderdelen (Vajrasana, de
Bodhi-boom-nakomeling, Animeshlochan Chaitya, Muchalinda-vijver) laten samensmelten tot een vage
generieke vermelding; te fijn opknippen zou omgekeerd kunstmatige kandidaten opleveren die
individueel de NOT_TO_BE_MISSED-poort niet zouden doorstaan. `DET-BGY-P001` bestaat specifiek om
dit te voorkomen.

Tweede: de Dungeshwari-grotten (Mahakala-grotten, plek van Boeddha's extreme ascese vóór de
verlichting) liggen verder van het hoofdcomplex en zijn minder bekend dan de hoofdtempel — een
reëel risico om over het hoofd te zien ondanks een sterke, onvervangbare eenmalige-gebeurtenis-
claim. `DET-BGY-P002` is hier specifiek op gericht.

Beide punten worden expliciet, niet stilzwijgend, als aandachtspunt meegenomen naar Discovery.

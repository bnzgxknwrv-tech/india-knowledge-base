# DISCOVERY_LOG — Bodh Gaya PRE-BRONS, denkproces

run_id: BODHGAYA-DISCOVERY-001
geschreven_op: 2026-08-03
geschreven_door: CCI

Dit document beschrijft HOE de PRE-BRONS-brief (`REGION_CONTENT_BRIEF.md`/`.json`) tot stand
kwam — niet alleen het resultaat. Belangrijke afbakening, expliciet vooraf: dit is nog GEEN
Discovery-uitvoering. PRE-BRONS is een oriënterende/plannende stap; de daadwerkelijke,
brongeverifieerde zoekacties per detector (stap 2, Discovery) zijn NOG NIET gestart, conform
Marks instructie om eerst het denkproces te beoordelen vóórdat er ook maar één kandidaat ontstaat.
Waar dit document "overwogen" of "verwacht" zegt, is dat uitdrukkelijk CCI's redenering tijdens
het schrijven van de brief — géén bronverificatie en géén kandidaat.

---

## 1. Welke detectoren heb je overwogen?

Alle zeven die in de brief staan (`DET-BGY-P001` t/m `P007`), plus een aantal die overwogen en
weer verworpen zijn (zie vraag 2). De zeven gekozen detectoren zijn gebouwd rond concrete,
inhoudelijke lagen van het gebied, niet rond abstracte "categorieën die compleet moeten zijn":
kerncomplex-decompositie, pre-verlichtingsnarratief, levende internationale praktijk,
Kriya-lijncontrole, archeologische laag, niet-boeddhistische traditie binnen de straal, en een
bron-kwaliteitsfilter (geen ontdekkingsdetector, maar een verplicht filter).

## 2. Welke detectoren heb je bewust NIET gebruikt, en waarom?

- **Een "alle UNESCO-deelkenmerken afvinken"-detector**: verworpen. Dat zou precies het
  categorievolledigheid-patroon zijn dat de hoofdvraag verbiedt — UNESCO-status is een signaal
  om te kijken, geen doel. In plaats daarvan toetst `DET-BGY-P001` elk onderdeel zelfstandig.
- **Een "alle deelnemende landen/nationale kloosters afvinken"-detector**: verworpen. Bodh Gaya
  heeft kloosters van tientallen landen; een detector die simpelweg "is land X vertegenwoordigd"
  beantwoordt, zou kandidaat-inflatie opleveren zonder inhoudelijke waarde. Vervangen door
  `DET-BGY-P003`, die individuele, uitzonderlijke kloosters toetst, niet de groep.
- **Een generieke "alle ASI-monumenten binnen de straal"-detector zonder narratieve eis**:
  verworpen ten gunste van `DET-BGY-P005`, die expliciet een gedocumenteerd verhaal eist, niet
  alleen een beschermde status.
- **Een "vier-grote-boeddhistische-pelgrimsplaatsen-circuit"-detector** (geboorte/verlichting/
  eerste preek/overlijden — Lumbini, Bodh Gaya, Sarnath, Kushinagar): verworpen. Lumbini ligt in
  Nepal (ander land, andere regio-scope), Kushinagar ligt ver buiten elke redelijke straal, en
  Sarnath is al volledig verwerkt onder de Varanasi-regio. Een circuit-detector zou de
  straal-regel uit stap 2 doorbreken zonder toegevoegde waarde voor déze regio-sweep.
- **Een detector voor moderne beroemdheidsbezoeken** (bijvoorbeeld bekende bezoekers aan de
  tempel): verworpen — niet gegrond in Marks eigen selectiecanon (PROJECT.md/PRIORITY_GROUPS.md),
  puur toeristische bekendheid, geen spirituele dichtheid.
- **Een aparte "moderne meditatiecentra"-detector** (niet aan de oude verhalen gekoppeld):
  overwogen, maar niet apart opgevoerd — ondergebracht in `DET-BGY-P003`, om detectorwildgroei te
  voorkomen zolang er geen zelfstandig, ander doel is dan "levende praktijk toetsen".

## 3. Welke zoekrichtingen heb je onderzocht?

Formeel: nog geen. Er is nog geen enkele bron geraadpleegd of geverifieerd voor deze regio — dat
is precies waarom `SOURCE_FAMILY_PLAN.jsonl` voor Bodh Gaya elke bronfamilie als `gepland`
markeert, niet `gebruikt` (in tegenstelling tot het Varanasi-equivalent op dit punt in het
proces, waar na Discovery de status wel naar `gebruikt` verschoof).

Wat wél is gebeurd, en waarom dit document dat toch meldt: bij het schrijven van de brief is
CCI's eigen achtergrondkennis gebruikt om de detectoren en de gebiedskarakterisering te
richten — bijvoorbeeld de globale topologie van het Mahabodhi-complex, het bestaan van de
Dungeshwari-grotten op enkele kilometers afstand, Sujata's dorp, en het bestaan van Xuanzangs
7e-eeuwse reisverslag als mogelijke primaire bron. Dit is ORIËNTATIE, geen verificatie — geen van
deze punten is al tegen een actuele, controleerbare bron gehouden. Dat gebeurt pas in Discovery.

## 4. Welke zoekrichtingen leverden niets op?

Niet van toepassing in deze fase — er is nog geen zoekactie uitgevoerd om iets al dan niet op te
leveren. Dit onderscheidt PRE-BRONS bewust van Discovery: PRE-BRONS plant welke richtingen
onderzocht gaan worden, Discovery voert ze uit en rapporteert pas dán negatieve resultaten.

## 5. Welke bronfamilies heb je gebruikt?

Geen. Zie vraag 3 — alle negen bronfamilies in `SOURCE_FAMILY_PLAN.jsonl` staan op `gepland`.

## 6. Welke bronfamilies ontbreken nog?

Formeel: alle negen moeten nog worden uitgevoerd. Twee verdienen specifieke aandacht:
- **Insider-/kloosterbron**: nog structureel niet beschikbaar, zelfde erkende hiaat als bij
  Varanasi — hier vooraf al benoemd in plaats van pas achteraf.
- **Primaire historische reisverslagen (Xuanzang)**: gepland, maar bronsterkte hangt af van het
  vinden van een betrouwbare vertaalde editie, niet een tussenhandse samenvatting — dit wordt in
  Discovery expliciet getoetst, niet aangenomen.

## 7. Welke aannames heb je bewust NIET gedaan?

- NIET aangenomen dat elke internationale tempel automatisch waardevol is.
- NIET aangenomen dat het bestaande "Bodh Gaya = A-cluster"-precedent uit `PRIORITY_GROUPS.md`
  een vrijbrief is voor elke losse deellocatie — dat precedent is een signaal, geen automatische
  waardering (zie `mark_known_interests` in de brief).
- NIET aangenomen dat er een Kriya-lijnverbinding met Bodh Gaya bestaat — expliciet als open
  vraag geregistreerd (`DET-BGY-P004`), niet stilzwijgend verondersteld op basis van Mark's
  algemene lijnbelangstelling.
- NIET aangenomen dat Nalanda, Rajgir of de Barabar-grotten binnen of buiten de straal vallen
  zonder daadwerkelijke kaartverificatie — de brief noemt ze uitdrukkelijk als "voorlopig
  vermoedelijk buiten scope, te bevestigen".
- NIET aangenomen dat het Gaya/Vishnupad-hindoegebied wél of juist geen NOT_TO_BE_MISSED-waarde
  heeft — bewust open gelaten voor Discovery (`DET-BGY-P006`).
- NIET aangenomen dat het aantal te vinden kandidaten in de buurt moet komen van Varanasi's
  schaal (45 permanente kandidaten) — geen enkel getal is als doel of verwachting vastgelegd.
- NIET aangenomen dat de exacte straal-coördinaten van de brief al correct/definitief zijn —
  expliciet gemarkeerd als "nog met een kaartbron te verifiëren tijdens Discovery".

## 8. Welke potentiële valkuilen zie je specifiek voor Bodh Gaya?

1. **Complex-decompositie-risico** (grootste, ook expliciet in de `dramatic_miss_check`): het
   Mahabodhi-complex is fysiek klein maar verhaaltechnisch dicht — te grof behandelen verliest
   onderscheiden onderdelen, te fijn opknippen creëert kunstmatige kandidaten.
2. **Dungeshwari-grotten-blindevlek**: verder van het hoofdcomplex, minder bekend, reëel risico
   op over het hoofd zien ondanks sterke inhoudelijke onvervangbaarheid.
3. **Precedent-bias**: het bestaande Mark-precedent "Bodh Gaya = A-cluster" kan onbewust leiden
   tot te soepele PASS-oordelen op individuele deellocaties tijdens de NOT_TO_BE_MISSED-poort —
   moet actief tegengegaan worden, elke deellocatie moet zelfstandig de poort doorstaan.
4. **Internationale-tempel-inflatiedruk**: de aanwezigheid van tientallen nationale kloosters
   creëert een natuurlijke verleiding tot "laten we ze allemaal noemen" — precies het
   categorievolledigheids-patroon dat de hoofdvraag verbiedt.
5. **Sterke commerciële/toeristische druk** rond de hoofdtempel kan het onderscheid tussen
   "levend en betekenisvol" en "beroemd-maar-oppervlakkig-toeristisch" vertroebelen bij
   individuele winkelgebieden of secundaire attracties.
6. **Narratieve overlap met Sarnath** (al afgerond onder Varanasi): verlichting versus eerste
   prediking zijn aparte momenten in Boeddha's leven — moet scherp onderscheiden blijven, geen
   samenvoeging of dubbele telling van hetzelfde verhaal.
7. **Evenement-versus-plek-verwarring**: sommige belangrijke boeddhistische gebeurtenissen in
   Bodh Gaya (bijvoorbeeld jaarlijkse onderrichtsbijeenkomsten) zijn tijdgebonden evenementen,
   geen vaste fysieke plek — de bezoekbaarheidspoort (AI_RULES.md regel 10) vereist een
   aanwijsbare fysieke plek, geen evenement; dit onderscheid moet expliciet bewaakt worden.

## 9. Waarom denk je dat je onderzoeksplan waarschijnlijk géén dramatisch belangrijke locatie zal missen?

Met beargumenteerde, maar uitdrukkelijk niet-gegarandeerde, zekerheid: de zeven detectoren dekken
de belangrijkste inhoudelijke lagen van het gebied (kerncomplex, pre-verlichtingsnarratief,
levende praktijk, eigen lijnverbinding, archeologie, andere tradities binnen de straal, en een
bronkwaliteitsfilter). De twee grootste concrete risico's die CCI zelf kon identificeren
(complex-decompositie, Dungeshwari) hebben elk een eigen detector gekregen in plaats van aan het
toeval te worden overgelaten.

Belangrijke beperking, eerlijk erkend: dit is een inschatting VOORAF, geen garantie. De
insider-/kloosterbron ontbreekt nog volledig, en dat is volgens eerder filosofie-overleg juist de
meest waarschijnlijke bron voor een werkelijk verborgen, dramatisch te missen parel. Zolang die
bronfamilie niet is uitgevoerd, blijft er een structurele blinde vlek — CCI claimt daarom geen
volledige zekerheid, alleen een beargumenteerde verwachting.

## 10. Welke locaties verwacht je vooraf waarschijnlijk wél te vinden?

(Uitdrukkelijk verwachtingen, geen kandidaten — nog niet getoetst.)
- Eén of meer zelfstandige onderdelen van het Mahabodhi-complex zelf, gegeven het bestaande
  precedent én het intrinsieke krachtveld van de plek.
- De Dungeshwari-grotten, gegeven de onvervangbare eenmalige-gebeurtenisclaim.
- Mogelijk Sujata's dorp/een bijbehorende gedenkplek — onvervangbare gebeurtenis, bronsterkte nog
  onbekend.
- Mogelijk één of twee uitzonderlijke internationale kloosters — welke specifiek is nog volledig
  open.

## 11. Welke soorten locaties verwacht je juist NIET te vinden (of niet te bevestigen als kandidaat)?

- De meeste "standaard" nationale kloosterpaviljoens zonder specifiek eigen verhaal —
  vermoedelijk WATCHLIST of FAIL, tenzij Discovery een uitzondering blootlegt.
- Generieke commerciële/souvenirgebieden rond de hoofdtempel.
- Losse archeologische objecten zonder aantoonbaar eigen verhaal, ondanks beschermde status.
- Vermoedelijk geen bevestigde Kriya-lijnverbinding — gebaseerd op de afwezigheid van enig eerder
  signaal daarvoor in de bekende bronnen, maar dit blijft een oprecht open, niet vooraf gesloten
  vraag.

---
Geschreven door: CCI, op verzoek van INDIA2 (PR #23). Geen kandidaten, geen nummers, geen BRONS,
geen A/B/C in dit document. Uitsluitend het denkproces achter de PRE-BRONS-brief.

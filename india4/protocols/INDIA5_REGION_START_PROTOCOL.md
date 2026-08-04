# INDIA5_REGION_START_PROTOCOL — hoe elke nieuwe regio begint

Status: CANONIEK vanaf 2026-08-03 (INDIA2-besluit, PR #23). Dit is het definitieve startprotocol
waarmee IEDERE volgende regiosweep identiek begint. Dit document beschrijft uitsluitend de
VOLGORDE en de VERANTWOORDELIJKHEDEN per stap — het bevat geen regio-specifieke voorbeelden, geen
nieuwe detectoren en geen nieuwe locaties. Voor de volledige inhoudelijke detaillering van elke
stap gelden de reeds bestaande canonieke bronnen, hieronder per stap aangehaald:
`india4/protocols/INDIA5-PROTOCOL.md`, `india4/roles/PRE-BRONS.md`, `india4/roles/BRONS.md`,
`india4/roles/ZILVER.md`, `india4/roles/GOUD.md`, `india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md`.
Dit document vervangt die bronnen niet — het legt uitsluitend de vaste volgorde en de
beslissingsbevoegdheid per stap vast, op één plek.

## De negen stappen (vast, nooit overslaan of omdraaien)

```
1. PRE-BRONS
2. Discovery
3. NOT_TO_BE_MISSED-poort
4. Kandidaatstatus
5. Permanente nummering
6. BRONS
7. ZILVER
8. GOUD
9. TRAVEL
```

Elke stap heeft precies één van drie beslissingsmodi: CCI autonoom, INDIA2 (architectuur/
canonieke wijziging), of Mark (persoonlijke/inhoudelijke keuze). Een stap mag nooit doorschuiven
naar de volgende zonder dat zijn eigen stopcriterium is gehaald.

---

## 1. PRE-BRONS

**Doel**: bewijzen dat de inhoudelijke werkelijkheid van het gebied voldoende is afgedekt vóórdat
er één kandidaatnaam wordt overgedragen. Geen vooraf vastgesteld aantal kandidaten — het aantal is
een uitkomst van deze en de volgende stap, nooit een invoer.

**Invoer**: expliciete gebiedsdefinitie (grens, straal of functionele corridor); Marks bekende
interesses, A-criteria en ankers zoals die al vastliggen in de canonieke bronnen (nooit verzonnen
of aangenomen); de ACTIVE detectoren uit `india4/registries/DETECTOR_LIBRARY.jsonl`, gefilterd op
plausibele toepasbaarheid; eerdere PRE-BRONS-brieven en rungeschiedenis van vergelijkbare gebieden
indien aanwezig.

**Uitvoer**: vier bestanden onder `runs/active/<run_id>/PRE_BRONS/` —
`REGION_CONTENT_BRIEF.md` + `.json`, `PRE_BRONS_DETECTORS.jsonl`, `SOURCE_FAMILY_PLAN.jsonl` — plus
een verplicht, expliciet beantwoorde vraag: "welke dramatisch te missen A-locatie zou dit plan nog
kunnen missen?".

**Stopcriteria**: de brief is intern consistent — alle verplichte velden ingevuld, geen
tegenstrijdige detectoren, elke geplande bronfamilie heeft minstens één detector. Pas dan mag stap
2 beginnen.

**Wanneer Mark beslist**: alleen bij een structureel gat in de bronnen dat een beleidskeuze
vereist, of wanneer een detector zijn persoonlijke interesseprofiel of A-definitie inhoudelijk zou
veranderen. Niet bij de normale opbouw van de brief zelf.

**Wanneer INDIA2 beslist**: promotie, aanscherping, samenvoeging of afwijzing van een PROVISIONAL
detector gebeurt altijd NA de run, nooit tijdens; elke canonieke wijziging aan de
detectorbibliotheek zelf (fuseren, ACTIVE maken, hernoemen, RETIRED zetten, parent-child-structuur)
is uitsluitend aan INDIA2.

**Wanneer CCI autonoom mag doorgaan**: het opbouwen van de volledige brief, het toepassen van
ACTIVE detectoren, het tijdelijk introduceren van nieuwe PROVISIONAL detectoren binnen deze run
(nooit canoniek ACTIVE), en het plannen van de te doorzoeken bronfamilies — zonder tussentijdse
goedkeuring.

---

## 2. Discovery

**Doel**: gevonden plekken opsporen via de in stap 1 toegepaste detectoren, tot detector- en
bronverzadiging. Het aantal gevonden plekken is een uitkomst van het onderzoek, nooit een vooraf
ingesteld getal, minimum of maximum.

**Invoer**: de PRE-BRONS-brief, `PRE_BRONS_DETECTORS.jsonl` en `SOURCE_FAMILY_PLAN.jsonl` uit stap
1.

**Uitvoer**: een lijst gevonden plekken (nog GEEN kandidaatstatus), elk met een eerste
WHY_THIS_ONE/WHY_NOT_THE_OTHERS-aanzet; per-detector en sweepniveau saturatiestatus
(`DISCOVERY_SATURATED` / `NOT_YET_SATURATED`); negatieve zoekresultaten en eventuele
OUT_OF_SCOPE_HIGH_VALUE_LEADS expliciet gedocumenteerd, niet stilzwijgend genegeerd.

**Stopcriteria**: de verzadigingsdrempel uit `india4/protocols/INDIA5-PROTOCOL.md` — per detector
minimaal twee wezenlijk verschillende zoekbenaderingen én minimaal twee relevante bronfamilies,
gevolgd door drie opeenvolgende materieel verschillende richtingen zonder nieuwe high-value lead.
Op sweepniveau: alle detectoren hebben een afsluitstatus, alle bronfamilies zijn uitgevoerd of
expliciet ONBESCHIKBAAR, en geen open lead kan redelijkerwijs een dramatisch te missen A-locatie
zijn.

**Wanneer Mark beslist**: nooit tijdens Discovery zelf — dit is zuiver onderzoekswerk zonder
inhoudelijke keuzemomenten voor Mark.

**Wanneer INDIA2 beslist**: bij een structurele blocker (bijvoorbeeld een hele bronfamilie
onbeschikbaar) of wanneer een gevonden patroon plausibel een nieuwe canonieke detector
rechtvaardigt — de canonisering zelf gebeurt pas na de run (zie stap 1).

**Wanneer CCI autonoom mag doorgaan**: de volledige zoekcyclus per detector, zonder tussentijdse
rapportage per gevonden plek, tot de sweepniveau-stopcriteria zijn gehaald.

---

## 3. NOT_TO_BE_MISSED-poort

**Doel**: elke gevonden plek uit stap 2 toetsen VOORDAT ze kandidaatstatus of een permanent nummer
krijgt. Voorkomt dat categorievolledigheid, bekendheid of routegemak op zichzelf tot
kandidaatstatus leidt — zie `india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md` voor de volledige,
canonieke toets.

**Invoer**: elke gevonden plek uit stap 2, getoetst tegen Marks vastgelegde selectiecanon
(de vaste bronnen die zijn interesses, prioriteiten en beoordelingsmethode beschrijven).

**Uitvoer**: per plek exact één uitkomst — PASS, WATCHLIST of FAIL — met onderbouwing volgens de
definitieve kandidaatpoort (spijt-vraag, sterkte-toets, krachtveld-toets, levend-of-monumentaal-
signaal, bezoekbaarheidspoort). Aan het einde van de run: één compacte WATCHLIST voor INDIA2/Mark.

**Stopcriteria**: elke gevonden plek uit stap 2 heeft een uitkomst; geen enkele plek blijft
onbeoordeeld of wordt stilzwijgend overgeslagen.

**Wanneer Mark beslist**: niet tijdens de toets zelf (geen tussentijdse vraag per plek) — hij ziet
na afloop uitsluitend de compacte WATCHLIST en beslist zelf of, en wanneer, een WATCHLIST-plek
verder onderzocht moet worden.

**Wanneer INDIA2 beslist**: canonieke aanpassingen aan het framework/de poort zelf (de zes
sterktegronden, de definitieve kandidaatpoort-criteria) — niet de individuele PASS/WATCHLIST/FAIL-
uitkomst per plek.

**Wanneer CCI autonoom mag doorgaan**: het toepassen van de toets en het bepalen van PASS/
WATCHLIST/FAIL per plek, met brononderbouwing, zonder tussentijdse vraag per locatie.

---

## 4. Kandidaatstatus

**Doel**: een PASS-plek wordt formeel kandidaat — vanaf hier bestaat de plek als record in de
regionale kandidatendataset.

**Invoer**: uitsluitend de PASS-uitkomsten uit stap 3. WATCHLIST en FAIL krijgen geen record.

**Uitvoer**: een kandidaatrecord met status `PROVISIONAL`, `protected_mark_status:
DOOR_MARK_TE_BEOORDELEN`, en de verplichte velden `WHY_THIS_ONE`, `WHY_NOT_THE_OTHERS`,
`MEANING_EVIDENCE`, `LIVING_OR_MONUMENTAL`, `MARK_RELEVANCE_LINK` (zie
`india4/templates/BATCH_OUTPUT.md`).

**Stopcriteria**: elke PASS-plek heeft een volledig, verplicht-veld-compleet record.

**Wanneer Mark beslist**: niet op dit punt zelf — A/B/C volgt pas na stap 8 (GOUD). Dit is wel het
moment waarop een plek voor het eerst zichtbaar wordt als iets waarover hij later zal beslissen.

**Wanneer INDIA2 beslist**: niet van toepassing, tenzij een structurele twijfel bestaat over de
poort-uitkomst zelf uit stap 3 (dan terug naar stap 3, niet hier oplossen).

**Wanneer CCI autonoom mag doorgaan**: het aanmaken van het kandidaatrecord zelf, zodra een PASS
vaststaat.

---

## 5. Permanente nummering

**Doel**: elke kandidaat krijgt een vast, permanent nummer dat nooit wijzigt en nooit wordt
hergebruikt (Immutable Location Numbering, zie `india4/protocols/INDIA5-PROTOCOL.md`).

**Invoer**: het nieuwe kandidaatrecord uit stap 4 + de bestaande `NUMBERING_REGISTRY.jsonl` van de
regio.

**Uitvoer**: een nieuwe, append-only regel in `NUMBERING_REGISTRY.jsonl` met `candidate_id`,
`display_id`, `canonical_name`, `region`, `assigned_at`. Vanaf hier beginnen kandidaatnaam, KML- en
PDF-vermeldingen met dit nummer.

**Stopcriteria**: de nummeringsvalidator slaagt — geen dubbel of gewijzigd nummer, geen naam zonder
nummer-prefix.

**Wanneer Mark beslist**: nooit — nummering is een mechanische, niet-inhoudelijke stap.

**Wanneer INDIA2 beslist**: alleen bij het vooraf reserveren van een nieuwe regionale
nummerreeks; nooit bij een individuele toekenning.

**Wanneer CCI autonoom mag doorgaan**: de volledige toekenning, mits de validator slaagt.

Kernregel, herbevestigd na de 041-045-episode: nummering vindt uitsluitend plaats NÁ een PASS
door stap 3. Er wordt nooit meer eerst genummerd en pas achteraf getoetst.

---

## 6. BRONS

**Doel**: GEO-verificatie — elke kandidaat krijgt een gecontroleerd Google Maps-coördinaat, of een
expliciete `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`-status met reden.

**Invoer**: de genummerde kandidatenlijst uit stap 5, verwerkt in vaste batches van 15-25
kandidaten.

**Uitvoer**: één JSONL-batchbestand per batch, met per kandidaat een status
(`CONFIRMED`/`NEEDS_REVIEW`/`GEEN_BRON`/`AMBIGUE_PIN`). Nooit een geschat, afgeleid of
"dichtstbijzijnde" coördinaat als vervanging.

**Stopcriteria**: elke kandidaat in de batch heeft een status; de batch is volledig, met readback,
en gecommit.

**Wanneer Mark beslist**: nooit tijdens BRONS — geen A/B/C-wijziging, geen beschermd besluit
aangeraakt.

**Wanneer INDIA2 beslist**: niet binnen een enkele batch; wel bij een structurele GEO-blocker die
de hele regio raakt.

**Wanneer CCI autonoom mag doorgaan**: alle batches ná elkaar, in dezelfde sessie/keten, zonder
tussentijdse Mark-opdracht (de autonome regio-doorloop uit
`india4/protocols/INDIA5-PROTOCOL.md`).

---

## 7. ZILVER

**Doel**: onafhankelijke controle van elk BRONS-record — juiste marker, juiste fysieke plek,
eerlijk gemarkeerde onzekerheid.

**Invoer**: de BRONS-batchbestanden uit stap 6.

**Uitvoer**: een gevalideerd/gecorrigeerd JSONL-batchbestand per batch; her-zoekt uitsluitend
wanneer een kandidaat's status ongelijk is aan `CONFIRMED`.

**Stopcriteria**: elke kandidaat in de batch is gecontroleerd, correcties zijn traceerbaar
vastgelegd, en de batch is gecommit. Geen A/B/C toegekend, geen beschermd Mark-besluit gewijzigd.

**Wanneer Mark beslist**: nooit tijdens ZILVER.

**Wanneer INDIA2 beslist**: niet binnen een enkele batch.

**Wanneer CCI autonoom mag doorgaan**: start automatisch zodra een BRONS-batch is afgerond, zonder
tussenkomst, batch na batch tot de hele regio gevalideerd is.

---

## 8. GOUD

**Doel**: één regionaal eindpakket bouwen voor Mark — reisgids-PDF, KML, GEO-audit/
correctierapport en beslisoverzicht.

**Invoer**: alle afgeronde BRONS- en ZILVER-batches van de volledige regio; start pas nadat de
VOLLEDIGE regio is gevalideerd, niet na elke kleine batch.

**Uitvoer**: één regionale KML, één reisgids-PDF (format:
`india4/templates/GOUD_PDF_TEMPLATE.md`), één GEO-audit, één correctierapport, één
COMPLETION-record. De PDF wordt na deze eerste build niet automatisch herbouwd bij latere kleine
wijzigingen — alleen op Marks expliciete verzoek.

**Stopcriteria**: alle kandidaten van de regio exact eenmaal aanwezig; elk KML-punt komt overeen
met het definitieve auditrecord; de nummerings- en brondatavalidators slagen.

**Wanneer Mark beslist**: dit is het moment waarop Mark de PDF, KML en het beslisoverzicht
ontvangt en zijn A/B/C-keuzeronde start — de eerste keer dat hij weer actief betrokken wordt na de
oorspronkelijke startopdracht voor de regio.

**Wanneer INDIA2 beslist**: niet tijdens de GOUD-build zelf.

**Wanneer CCI autonoom mag doorgaan**: de volledige integratie, zonder tussentijdse Mark-actie, tot
aan de eindoplevering.

---

## 9. TRAVEL

**Doel**: van Marks definitieve A/B-keuzes een concrete bezoekstructuur maken —
CLUSTER_ANCHOR → locaties → afstand tot dichtstbijzijnde A's → dagindelingen (het bestaande
routefilosofie-model).

**Invoer**: Marks definitieve A/B/C-besluiten uit stap 8; het vastgelegde accommodatiebesluit
(`ACCOMMODATION_REGISTER.jsonl`); de geografische clusterindeling uit GOUD.

**Uitvoer**: een routeklaar-overzicht (logisch bereikbare A-kandidaten per cluster, gemeten vanaf
de accommodatiebasis); op expliciet verzoek daarna een volledige dagroute-/planningberekening.

**Stopcriteria**: elke A-kandidaat is in een cluster of dagindeling geplaatst, of expliciet als
"nog niet ingedeeld" gemarkeerd — nooit stilzwijgend weggelaten.

**Wanneer Mark beslist**: hij start deze stap altijd zelf, expliciet — dit is nooit een automatisch
vervolg op GOUD. Hij beslist ook over de uiteindelijke volgorde/indeling van dagen.

**Wanneer INDIA2 beslist**: niet van toepassing.

**Wanneer CCI autonoom mag doorgaan**: het opstellen van het routeklaar-overzicht zelf zodra
gevraagd; niet de volledige dagroutebouw zonder Marks expliciete verzoek (bestaande regel, zie
"Accommodatiebesluiten" in `india4/protocols/INDIA5-PROTOCOL.md`).

---

## Samenvattend principe

Drie beslissingsmodi, nooit vermengd:
- **CCI autonoom**: het overgrote deel van elke stap — onderzoek, toetsing, verificatie, bouw —
  zonder tussentijdse goedkeuring, zolang de stopcriteria van die stap worden gerespecteerd.
- **INDIA2**: canonieke architectuurbeslissingen — detectorbibliotheek, framework-aanpassingen,
  nummerreeks-reserveringen, structurele blockers over een hele regio.
- **Mark**: persoonlijke, inhoudelijke keuzes — A/B/C, accommodatie, dagindeling, en elke
  wijziging aan zijn eigen selectiecanon (PROJECT.md/PRIORITY_GROUPS.md/METHODOLOGY.md).

Een stap mag nooit worden overgeslagen, omgedraaid of vervroegd afgesloten om tijd of tokens te
besparen — elk stopcriterium hierboven is hard.

---
Geschreven door: CCI, op verzoek van INDIA2 (PR #23).
Datum: 2026-08-03.
Status: CANONIEK. Geen nieuwe detectoren, geen nieuwe locaties, geen regio-specifieke inhoud in
dit document zelf.

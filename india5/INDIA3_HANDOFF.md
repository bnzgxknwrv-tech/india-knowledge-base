# INDIA3 HANDOFF — canonieke overdracht

Datum: 2026-08-05
Repository: `bnzgxknwrv-tech/india-knowledge-base`
Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR: `#23` (draft; niet mergen zonder expliciete vrijgave van Mark)

## Doel van deze overdracht

Een nieuwe ChatGPT-sessie moet zonder oude chatcontext de India-sweeps kunnen regisseren. GitHub is de bron van waarheid. De nieuwe sessie mag geen besluiten uit oude chats reconstrueren wanneer ze niet in GitHub staan.

## Rollen

- **Mark**: bepaalt doel en scope; maakt alle definitieve A/B/C-keuzes; beslist over hotels, persoonlijke voorkeuren, PDF-builds en inhoudelijke tegenstrijdigheden.
- **ChatGPT India3**: regisseur en kwaliteitsbewaker; leest GitHub-resultaten, bewaakt canon en schrijft de volgende concrete opdracht voor CCI. Doet niet zelf duizenden uitvoeringsrondes.
- **ClaudeCodeIndia (CCI)**: uitvoerende engine; leest/schrijft GitHub, doet gericht onderzoek, bouwt datasets/KML/Markdown en commits. Bouwt uitsluitend een PDF na expliciete toestemming van Mark.
- **CC/Home-Assistant-sessie**: geen standaardrol in India-sweeps; alleen inschakelen na expliciet verzoek van Mark voor tooling/architectuuraudit.

## Communicatiecanon

1. Er is exact **één gezamenlijke, unieke, oplopende berichtenteller** voor alle briefjes tussen ChatGPT en CCI.
2. Elk nieuw inter-AI-bericht pakt het volgende nummer, ongeacht afzender.
3. Geen `antwoord op`, geen aparte tellers per afzender.
4. Vorm:

```text
========================
CHATGPT → CCI
Bericht: 011
Status: ACTIEF
========================
...
/CHATGPT (011)
```

Daarna gebruikt CCI `Bericht: 012` en sluit af met `/CCI (012)`.

De laatste feitelijke overdracht van CCI na ChatGPT-bericht 009 geldt als briefje **010**, ook al labelde CCI die envelop niet correct. Het eerstvolgende inter-AI-briefje moet daarom **011** zijn.

## Kernfilosofie van de sweep

- Het aantal kandidaten is een uitkomst, nooit vooraf een doel.
- Een sweep zoekt niet naar categorievolledigheid of zoveel mogelijk locaties.
- CCI/ChatGPT maken de **voorselectie**; Mark kiest daarna zelf A/B/C.
- Een plek is **MARK_WAARDIG** wanneer er na eerlijke uitleg een redelijke mogelijkheid bestaat dat Mark haar A, B of C geeft.
- C is óók een geldige Mark-keuze; een vermoedelijke C mag dus niet vóór Mark worden verborgen.
- Alleen vóór Mark uitsluiten bij een harde grond: feitelijk dubbel, geen eigen onderscheidende betekenis/ervaring, niet fysiek bezoekbaar als specifieke plek, puur commercieel/generiek, of redelijkerwijs zelfs geen C.
- Interne labels als `CORE_PASS`, `OPTIONAL_PASS` en `WATCHLIST` mogen discovery ondersteunen, maar mogen Marks keuzelijst niet vervangen.
- Eerst: gebied begrijpen → discovery → betekenis/onderscheid → MARK_WAARDIG → nummering → BRONS → ZILVER → GOUD → Mark A/B/C → TRAVEL.
- Geen coördinaten raden. Een ontbrekende eenduidige openbare Google Maps-marker blijft `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`.
- Radius: 0–20 km volledig onderzoeken; 20–30 km alleen signalerend voor uitzonderlijke, dramatisch te missen locaties; daarbuiten als aparte regio/high-value lead loggen.

## Immutable numbering

- Elk genummerd locatie-item houdt permanent hetzelfde nummer.
- Nummers worden nooit gewijzigd, hergebruikt, stil samengevoegd of aan een andere plek gekoppeld.
- Varanasi gebruikt 001–045.
- Bodh Gaya gebruikt momenteel 046–058.
- Sublocaties binnen één normaal complexbezoek krijgen geen apart nummer, tenzij ze aantoonbaar zelfstandige bestemmingen zijn en dit expliciet is besloten.

## PDF-regel

- PDF is geen automatisch werkproduct en geen doorlopend communicatiekanaal.
- Geen PDF-render, tijdelijke PDF, rebuild of readback zonder Marks expliciete toestemming.
- Eerst inhoud in Markdown controleren; pas daarna kan Mark een eenmalige PDF toestaan.

## Varanasi-status

- Regio inhoudelijk afgerond voor deze fase.
- 001–040 hebben definitieve Mark-keuzes: 32×A, 5×B, 3×C.
- 041–045 bestaan permanent door eerdere te vroege nummering; geen van deze vijf is bewezen `NOT_TO_BE_MISSED` voor Mark. Niet stil verwijderen of hernummeren.
- Hotelbesluit apart en `LOCKED_BY_MARK`: `VNS-HOTEL-001` Sahi River View Guesthouse, Assi Ghat; vraag om balcony room; aanbeveling Debby/Jitendre.
- Bron van waarheid omvat onder meer `DATASET_VARANASI_40.jsonl`, `ACCOMMODATION_REGISTER.jsonl`, KML en travel-Markdown. Oude PDF is momentopname en wordt niet automatisch bijgewerkt.

## Bodh Gaya-status

Run: `runs/active/BODHGAYA-DISCOVERY-001`

### Bestaande Mark-besluiten

Mark heeft al gekozen:

- 046 Mahabodhi Temple Complex — A
- 047 Sujata Stupa, Bakraur — A
- 048 Dungeshwari Cave Temples / Mahakala Caves — A
- 049 Great Buddha Statue — A

Deze besluiten staan in `MARK_DECISIONS_2026-08-05.jsonl` en mogen niet opnieuw ter keuze worden voorgelegd of gewijzigd zonder Mark.

### Heropende voorselectie

Commit `d62f00f30190872a495deb0c53acbf8f5e73658c` bevat:

- `runs/active/BODHGAYA-DISCOVERY-001/GOUD/MARK_SELECTION_REPORT.md`
- `runs/active/BODHGAYA-DISCOVERY-001/GOUD/EXCLUSION_REPORT.md`
- bijgewerkte `NUMBERING_REGISTRY.jsonl`
- bijgewerkte `DISCOVERY_CANDIDATES.jsonl`
- bijgewerkte `WATCHLIST.jsonl`

Negen eerder verborgen items zijn terecht als MARK_WAARDIG hersteld en permanent genummerd:

- 050 Archaeological Museum of Bodh Gaya (ASI)
- 051 Vishnupad Temple, Gaya
- 052 Tergar Monastery
- 053 Root Institute (FPMT)
- 054 Wat Thai Buddhagaya / Thai Monastery
- 055 Royal Bhutan Monastery
- 056 Namgyal Monastery Bodhgaya / Tibetaans klooster tegenover Mahabodhi — identiteit niet 100% bevestigd
- 057 Vietnamese Temple
- 058 Japanese Temple / Indosan Nippon

Mark heeft voor 050–058 nog **geen A/B/C** gekozen.

### Harde uitsluitingen / leads

- Niranjana/Falgu-rivier als aparte badplek: geen specifieke aanwijsbare fysieke plek; verhaal blijft context bij 047.
- Barabar/Nagarjuni-grotten: objectief high-value, maar circa 35 km en dus buiten Bodh-Gaya-scope; bewaren als `OUT_OF_SCOPE_HIGH_VALUE_LEAD`, niet inhoudelijk afwijzen.

### 046-sublocaties

In `MARK_SELECTION_REPORT.md` zijn de traditionele weekplekken binnen het Mahabodhi-complex uitgewerkt als sublocaties zonder eigen nummer, waaronder Animeshlochan Chaitya, Ratnachakrama, Ratnaghar Chaitya, Ajapala Nigrodh, Muchalinda-vijver en Rajyatana-boom.

Open beslispunt: Muchalinda kan naar twee gelijknamige plekken verwijzen. Niet stil oplossen of apart nummeren zonder voldoende bewijs/besluit.

### GEO

- 046 en 047: marker bevestigd.
- 048 en 049: `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`; meerdere gerichte pogingen zijn afgerond, niet opnieuw eindeloos zoeken zonder nieuwe concrete lead.
- Nieuwe 050–058 moeten nog door de normale BRONS/ZILVER/GEO-stappen voordat een definitieve kaart wordt gebouwd.

## Direct volgende inhoudelijke stap

1. India3 leest `MARK_SELECTION_REPORT.md` en `EXCLUSION_REPORT.md` volledig.
2. India3 controleert of 050–058 elk voldoende, begrijpelijke informatie geven waarmee Mark zelfstandig A/B/C kan kiezen.
3. Controlepunten: identiteit 056; daadwerkelijke bezoekbaarheid 052/053; onderscheid tussen internationale kloosters; geen verborgen advies dat Marks keuze stuurt; 046-sublocaties voldoende duidelijk.
4. Nog **geen PDF**.
5. Als Markdown inhoudelijk voldoet: leg 050–058 compact aan Mark voor voor A/B/C, of laat CCI eerst gerichte tekortkomingen repareren.
6. Na Marks keuzes: besluiten duurzaam loggen, daarna pas BRONS/ZILVER/GEO voor de door protocol vereiste records en uiteindelijk KML/TRAVEL. PDF alleen op expliciet verzoek.

## Verboden regressies

- Geen vooraf bepaald kandidaataantal.
- Geen locaties voor Mark verbergen omdat ChatGPT/CCI ze waarschijnlijk B of C vinden.
- Geen lange inhoudelijke resultaten in PR-comments; comment is alleen envelop, volledige inhoud staat in bestanden.
- Geen bestaande geldige records herserialiseren of cosmetisch wijzigen wanneer append mogelijk is.
- Geen brede repositoryscan; lees alleen protocollen, registers en runbestanden die direct nodig zijn.
- Geen status uit een los progressbestand vertrouwen wanneer de data zelf de voortgang kan bepalen.
- Geen claims over writes/commits/readback zonder GitHub-bewijs.

## Bron van waarheid bij conflict

1. Expliciet recent Mark-besluit in een duurzaam GitHub-register.
2. Canonieke protocolbestanden.
3. Run-specifieke dataset/registers en commits.
4. Markdown-rapporten.
5. PR-comments zijn alleen envelop/overleg en nooit de enige blijvende canon.

Einde overdracht.

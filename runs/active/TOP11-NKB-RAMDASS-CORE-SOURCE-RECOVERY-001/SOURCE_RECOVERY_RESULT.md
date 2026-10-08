# SOURCE_RECOVERY_RESULT — TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001

```
task_id: TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001
cci_task: CCI_TASK 090
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
blindheid: agent/chatgpt-top11-parallel-sweep NIET geopend. Externe NKB/Ram-Dass-freezes NIET
  geopend. IndiaROOD-resultaten NIET geopend. Oude METHOD_V1/PHASE2-lijsten NIET als
  discoverychecklist gebruikt. Uitsluitend TASK.md, de bestaande CCI_TASK 089-freezes en
  rechtstreeks herstelde bronnen gebruikt.
```

## 1. Bronherstelroutes per doelbron

### Neem Karoli Baba — *Miracle of Love* (Ram Dass, compiler)

| route | URL/bron | toegangsdatum | bereikbaarheid | doorzoekbaar | resultaat |
|---|---|---|---|---|---|
| Internet Archive item `miracleoflovesto00ramd` | archive.org/details/miracleoflovesto00ramd | 2026-08-19 | Item bestaat, maar is **access-restricted** (controlled digital lending — alleen lenen na login) | NEE zonder login | `BRON_GEBLOKKEERD` |
| Archive.org "search inside"-API op hetzelfde item | archive.org (BookReaderSearch endpoint) | 2026-08-19 | HTTP 403 zonder geauthenticeerde sessie | NEE | `BRON_GEBLOKKEERD` — bewust NIET omzeild (verboden technische toegangscontrole-bypass conform TASK.md §3) |
| Google Books preview | books.google.com | 2026-08-19 | Geen bruikbare preview-inhoud opgehaald (technische non-hit, geen bewuste blokkade) | NEE | `UNAVAILABLE` |
| hanumanfoundation.org (reeds bekend uit CCI_TASK 089) | hanumanfoundation.org PDF | eerder bevestigd, herbevestigd 2026-08-19 | Alleen titelpagina/inhoudsopgave/voorwoord (173 KB), verhalen zelf (p. 1-405) niet inbegrepen | DEELS (voorwerk) | `BRON_GEBLOKKEERD/DEELS` — ongewijzigd t.o.v. 089 |

**Conclusie**: *Miracle of Love* blijft `BRON_GEBLOKKEERD` na meerdere onafhankelijke legale routes. Geen enkele route gaf toegang tot de eigenlijke verhalen.

### Neem Karoli Baba — *By His Grace* (Dada Mukerjee)

| route | URL/bron | toegangsdatum | bereikbaarheid | doorzoekbaar | resultaat |
|---|---|---|---|---|---|
| dokumen.pub (reeds bekend uit CCI_TASK 089) | dokumen.pub | herbevestigd 2026-08-19 | Site meldt "under maintenance" | NEE | `BRON_GEBLOKKEERD` — ongewijzigd |
| Internet Archive item `byhisgracedevote0000dada` | archive.org/details/byhisgracedevote0000dada | 2026-08-19 | Item bestaat, **access-restricted** (alleen "Previews", geen doorzoekbare/volledige tekst zonder login) | NEE | `BRON_GEBLOKKEERD` |
| shrikainchidham.org (devotee-boekenoverzicht) | shrikainchidham.org/p/neem-karoli-baba-books-collection.html | 2026-08-19 | Alleen een Amazon-affiliate boekenlijst, geen vrije tekst | NEE | `UNAVAILABLE` |

**Conclusie**: *By His Grace* blijft `BRON_GEBLOKKEERD` na meerdere onafhankelijke legale routes.

### Ram Dass — *Be Here Now*

| route | URL/bron | toegangsdatum | bereikbaarheid | doorzoekbaar | resultaat |
|---|---|---|---|---|---|
| Internet Archive item `be-here-now-pdfdrive` | archive.org/details/be-here-now-pdfdrive | 2026-08-19 | **Volledig open** — "Community Texts"/opensource-collectie, geen login vereist, geen toegangscontrole omzeild | JA — volledige `_djvu.txt`-platte tekst gedownload (17.535 regels, 529 KB) | `FULL` |

**Conclusie**: *Be Here Now* is deze keer wél volledig hersteld via een legale, open route — een technisch andere klasse Internet Archive-item dan het geblokkeerde *Miracle of Love*-item (geen leenverplichting, geen 403 op tekstuele inhoud). Volledige lossless corpus-extractie hieronder in §2.

### Ram Dass — "Sacred Wanderer" / kernbiografische bronfamilie

**Titelverwarring vastgesteld en gecorrigeerd** (conform TASK.md §1 "identificeer titel/auteur/uitgave exact en voorkom titelverwarring"):

- *The Sacred Wanderer* is een boek van **Ravi Dass**, een andere Neem-Karoli-Baba-devotee — NIET Ram Dass. Dit is geen Ram Dass-bronfamilie en is in de CCI_TASK 089-freeze ten onrechte als zodanig behandeld. Dit wordt hier expliciet gecorrigeerd, niet stilzwijgend overschreven (zie §3).
- De correcte kernbiografische bron voor Ram Dass' Indiareizen is **"Being Ram Dass"** (2021, Sounds True, samen met Rameshwar Das) — zijn postume, definitieve memoire, expliciet beschreven als het India-materiaal "in veel groter detail" behandelend dan *Be Here Now*.

| route | URL/bron | toegangsdatum | bereikbaarheid | doorzoekbaar | resultaat |
|---|---|---|---|---|---|
| Tricycle Magazine — officieel boekfragment | tricycle.org/article/being-ram-dass-excerpt/ | 2026-08-19 | Volledig legaal gepubliceerd uitgeversfragment | JA (fragment) | `PARTIAL` |
| Internet Archive / Google Books / uitgeverspagina (Sounds True) op volledige tekst | diverse | 2026-08-19 | Geen vrij toegankelijke volledige tekst gevonden (2021-titel, nog onder copyright, geen open-access editie) | NEE | `UNAVAILABLE` |

**Conclusie**: "Being Ram Dass" is `PARTIAL` — één legaal fragment hersteld (Tricycle), de volledige tekst blijft niet vrij toegankelijk. Twee nieuwe feiten uit dit fragment lossless verwerkt in §2.

## 2. Lossless extractie — nieuwe occurrences

### Uit *Be Here Now* (Ram Dass, eigen verslag — volledige tekst)

Corpus-first doorzocht op alle India-gerelateerde plaatstermen (steden, staten, tempel-/ashramtypes,
verblijfplaatsen). Bibliografiesectie (regels ~16120-16680: uitgeversvestigingssteden van
aangehaalde boeken) expliciet **uitgesloten** als ruis — dit zijn geen Ram Dass-occurrences.

| # | occurrence | PERSONALLY_PRESENT (wie) | type | bronlocator |
|---|---|---|---|---|
| A | **Amarnath Cave, Kashmir** — bezocht te paard, vóór de ontmoeting met Neem Karoli Baba, tijdens een pre-guru pelgrimstocht met een reisgenoot | Ram Dass: JA | grot/pelgrimsoord | be_here_now.txt, regel 770 |
| B | **Benares (Varanasi)**, niet-gespecificeerde locatie — bezocht in dezelfde pre-guru reissequentie, vóór Nepal | Ram Dass: JA | stad (algemeen) | be_here_now.txt, regel 770-771 |
| C | **Sarnath** — Chinees-boeddhistisch klooster, verblijf van "een paar weken" | Ram Dass: JA | klooster | be_here_now.txt, regel 988 |
| D | **Delhi — meerdere sublocaties** (visumkantoor; Connaught Place, blootsvoets/zwijgend doorkruist; American Express-kantoor; een deftig vegetarisch restaurant, ongenoemd; een boeddhistisch klooster voor één nacht, ongenoemd) — bevestigd via Ram Dass' eigen verslag van een 12-uur-durende bustocht | Ram Dass: JA | stad + sublocaties | be_here_now.txt, regel 967-1001 |
| E | Onbenoemde tempel/veld, "3 mijl" per Land Rover van het verblijf van een niet-genoemde beeldhouwer — eerste ontmoeting met Neem Karoli Baba ("Maharaji"), inclusief de "je moeder is overleden"-episode | Ram Dass: JA; Neem Karoli Baba: JA | tempel/veld, voetheuvels Himalaya | be_here_now.txt, regel 1093-1180, 1273 |
| F | **Forestry camp** — onbenoemd gebouw verder de heuvel op, beschikbaar gesteld door devotees bij de Forestry-afdeling; bezoek per Land Rover na een appelboomgaard-tussenstop | Ram Dass: JA; Neem Karoli Baba: JA | verblijfplaats (bosbeheer) | be_here_now.txt, regel 1440-1468 |
| G | Onbenoemde "estate" bij een niet-genoemde "town near-by" — Neem Karoli Baba's jaarlijkse visum geregeld; Ram Dass kreeg hier een "holy man's house"; plaats van de moeder-visioen-episode onder de sterren | Ram Dass: JA; Neem Karoli Baba: JA | landgoed/verblijfplaats | be_here_now.txt, regel 990-1005 |
| H | **K.K. (Krishna Kumar) Sah's familiehuis**, nabij Nainital — Ram Dass hier ontvangen en gevoed ("double roti") na de allereerste ontmoeting met Maharaj-ji | Ram Dass: JA | privéwoning | be_here_now.txt, regel 17000-17022 (50-jarig-jubileum-nawoord, zelfde editie) |
| I | Genoemd maar NIET als locatie geregistreerd: bezoek aan de Dalai Lama — geen plaatsnaam gegeven in de tekst (geen Dharamsala-vermelding); niet gegokt conform de regel "geen geraden plaatsen" | — | onbepaald | be_here_now.txt, regel 769 |

**Belangrijke corpusbevinding**: de naam "**Kainchi**" komt in deze volledige tekst van *Be Here
Now* **geen enkele keer voor** (geverifieerd via corpusbrede zoekopdracht). De eerste-ontmoetingsscène
(occurrence E) wordt uitsluitend beschreven via fysieke kenmerken (tempel/veld, 3 mijl rijden,
voetheuvels), niet via een eigennaam. Dit is een directe primaire-bronbevinding, geen aanname.

### Uit "Being Ram Dass" (2021) — Tricycle-fragment

| # | occurrence | PERSONALLY_PRESENT | type | bronlocator |
|---|---|---|---|---|
| J | Zes maanden yoga-/meditatietraining in de "Himalaya foothills", celibatair, grotendeels zwijgend, vóór terugkeer naar de VS in 1968 | Ram Dass: JA | trainingsperiode (plaats niet verder gespecificeerd dan "foothills") | tricycle.org/article/being-ram-dass-excerpt/ |
| K | Fotobijschrift: "Ram Dass and his teacher Maharaj-ji **in Kainchi, India**" | Ram Dass: JA; Neem Karoli Baba: JA | naambevestiging | tricycle.org/article/being-ram-dass-excerpt/ (fotobijschrift) |

**Belangrijk**: occurrence K is de **enige** in deze taak geraadpleegde bron die de naam "Kainchi"
expliciet aan de eerste-ontmoetingslocatie koppelt. Dit bevestigt de naam via een onafhankelijke
route (Ram Dass' eigen postume kernbiografie/fotobijschrift), maar niet via *Be Here Now* zelf.
Occurrence J is inhoudelijk consistent met de reeds bekende sadhana-trainingsperiode (bestaande
Ram Dass-freeze record 2, Kainchi Dham) en wordt als corroboratie behandeld, niet als apart record.

## 3. Expliciete correcties en negatieve bevindingen

- **Titelcorrectie**: "Sacred Wanderer" (CCI_TASK 089) was een titelverwarring — dat boek is van Ravi
  Dass, niet van Ram Dass. Vervangen door "Being Ram Dass" (2021) als het juiste doelwerk. De oude
  089-rij wordt NIET stil overschreven; zie de delta-paragraaf in de Ram Dass-freeze.
- **Sewalti Hotel**: genoemd in *Be Here Now* (regel 850) als verblijfplaats tijdens het vijfdaagse
  seminar met Bhagwan Dass, direct volgend op de Blue-Tibetan-ontmoeting in Kathmandu. Land/plaats
  niet ondubbelzinnig vastgesteld binnen deze tekst (context suggereert mogelijk nog Nepal, niet
  India) — **niet als India-record opgenomen**, expliciet als onopgelost punt genoteerd, geen gok.
- **Badrinath**: genoemd in het 50-jarig-nawoord (regel 17047) uitsluitend als achtergrond over de
  functie van K.K. Sah's vader (Circle Inspector of Police, opende/sloot de tempel jaarlijks) —
  **geen Ram Dass- of Neem-Karoli-Baba-aanwezigheidsrecord**, uitgesloten als contextvermelding
  conform TASK.md §4.4 ("plaats alleen als context").
- **Kathmandu/Blue Tibetan (Nepal)**: herbevestigd als niet-India, blijft uitgesloten conform de
  reeds bestaande negatieve bevinding in de 089-freeze.
- **Dalai-Lama-bezoek**: genoemd zonder plaatsnaam; niet geregistreerd, niet gegokt (geen
  Dharamsala-aanname).

## 4. Per-persoon rapportage (verplicht, TASK.md §5)

### Neem Karoli Baba

- Eerdere recordcount (CCI_TASK 089): 19.
- Nieuwe rechtstreeks-uit-kernbron geëxtraheerde occurrences: **0 nieuw uit de doelbronnen zelf**
  (*Miracle of Love*, *By His Grace* blijven beide `BRON_GEBLOKKEERD`). Wél 2 nieuwe occurrences
  (F, G hierboven) rechtstreeks uit *Be Here Now* — toegestaan conform TASK.md §4 omdat er
  duidelijke gebeurtenisprovenance is (Ram Dass zelf getuige van Maharaj-ji's fysieke aanwezigheid).
- Duplicates versus echte toevoegingen: occurrence E is zeer waarschijnlijk hetzelfde
  fysieke-ontmoetingsmoment als bestaande record 5 (Kainchi Dham) — behandeld als corroboratie,
  NIET als duplicaat-record en NIET als bevestigde samenvoeging (geen naamsanker in de brontekst
  zelf). Occurrences F en G zijn nieuwe, niet eerder geregistreerde sublocaties.
- Gecorrigeerde aanwezigheid-/identiteitsclaims: geen wijziging aan bestaande rows.
- Actuele corpuscoverage-matrix: zie §1 hierboven — beide primaire devotee-bronnen blijven
  ontoegankelijk; *Be Here Now* toegevoegd als secundaire-maar-eyewitness-bron voor gedeelde
  scènes.
- Resterende bronblokkades: *Miracle of Love* (access-restricted + 403 op search-inside), *By His
  Grace* (dokumen.pub onderhoud + access-restricted Archive-item).
- Herziene pre-external gates: CORPUS-COVERAGE-GATE blijft **NEE** (de twee kerndevotee-bronnen
  zelf blijven dicht); wel een kleine verbetering door de twee nieuwe Be-Here-Now-sublocaties.
- Eerlijke saturationstatus: **`NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_SATURATED: NEE`** — ongewijzigd
  t.o.v. 089, met twee toegevoegde records.

### Ram Dass

- Eerdere recordcount (CCI_TASK 089): 5.
- Nieuwe rechtstreeks-uit-kernbron geëxtraheerde occurrences: **9** (A t/m I minus de niet-
  geregistreerde Dalai-Lama-vermelding = 8 nieuwe locatie-occurrences uit *Be Here Now*, plus 1
  naamsbevestiging (K) en 1 corroboratie (J) uit "Being Ram Dass").
- Duplicates versus echte toevoegingen: occurrence E/F/G overlappen inhoudelijk met bestaande
  record 2 (Kainchi Dham) qua episode, maar bevatten geen naamsanker — apart vermeld, niet
  samengevoegd. Occurrence K bevestigt de naam "Kainchi" onafhankelijk. A, B, C, D, H zijn volledig
  nieuwe, niet eerder geregistreerde locaties.
- Gecorrigeerde aanwezigheid-/identiteitsclaims: **titelcorrectie** "Sacred Wanderer" → "Being Ram
  Dass" (zie §3) — de belangrijkste correctie van deze taak.
- Actuele corpuscoverage-matrix: *Be Here Now* nu `FULL` (was `BRON_GEBLOKKEERD`); "Being Ram Dass"
  nu `PARTIAL` (was niet als zodanig geïdentificeerd — verkeerde titel werd gezocht).
- Resterende bronblokkades: volledige tekst van "Being Ram Dass" (2021) blijft niet vrij
  toegankelijk; alleen het Tricycle-fragment.
- Herziene pre-external gates: CORPUS-COVERAGE-GATE verbetert van **NEE** naar **DEELS** — de
  belangrijkste eigen kernbron (*Be Here Now*) is nu volledig doorzocht; de tweede kernbron
  ("Being Ram Dass") is nog maar gedeeltelijk bereikt.
- Eerlijke saturationstatus: **`RAM_DASS_V2_PRE_EXTERNAL_SATURATED: NEE`** blijft de eerlijke
  uitkomst — de recordcount is gegroeid (5 → 13), maar meerdere locaties zijn nog onbenoemd
  (E, F, G) en de tweede kernbiografie is nog niet volledig doorzocht.

## 5. Bevestiging blindheid

- Externe freezes (`agent/chatgpt-top11-parallel-sweep`) geopend tijdens deze taak: **NEE**.
- IndiaROOD-resultaten geopend: **NEE**.
- Oude METHOD_V1/PHASE2-lijsten als discoverychecklist gebruikt: **NEE**.

## 6. next_allowed_step

CCI heeft `TASK.md` uitgevoerd binnen de gestelde grenzen, per persoon gecheckpoint, en stopt na
deze resultaatenvelop. INDIA beslist tussen (a) nog één gerichte corpuspass — met name een poging
om "Being Ram Dass" (2021) volledig te bereiken, en/of maharajji.love alsnog te doorzoeken voor
Neem Karoli Baba — óf (b) externe lossless reconciliatie starten met de bestaande
`agent/chatgpt-top11-parallel-sweep`-freezes voor beide personen, analoog aan CCI_TASK 088's
patroon. Ramana Maharshi/Ramakrishna blijven expliciet niet gestart. Geen route/cluster/regio-werk
verricht.

---
Geschreven door: CCI. CCI_TASK 090.

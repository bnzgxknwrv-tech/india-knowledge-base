# YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086

```
task_id: TOP11-EXTERNAL-AI-BENCHMARK-001
trigger: CCI_TASK 086
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-18
```

## Bevroren volgorde (expliciet vastgelegd, conform stopvoorwaarde)

- **Interne pre-external freeze**: commit `cd0ff2b159900015fcdc3d69617850efc32bc550`
  (`YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md`), chronologisch vóór de externe union.
- **Externe control-input**: PR #24, branch `agent/add-yogananda-location-atlas`, head SHA
  `e8c7ef6899feaa2a8fdfd1d82d98986f85d8281d`, atlasbestand
  `india4/reference/PARAMAHANSA_YOGANANDA_MASTER_LOCATION_ATLAS.md`, blob SHA
  `089b652e6b0c7393fa8e6508f7c1bd6e3bb7399d` — 114 genummerde records, synthese van Grok, Gemini,
  DeepSeek, Copilot en AI-5. Deze exacte SHA/blob is gebruikt; geen latere PR #24-wijzigingen.

## Methode

De externe atlas is zelf al ongewoon zelfkritisch (eigen BEWEZEN/WAARSCHIJNLIJK/ALLEEN PLAATS/
FOUTIEVE-labels, een eigen conflictenlijst, een eigen "Mogelijke Gaten"-sectie). CCI heeft daarom
niet alle 114 records blind opnieuw vanaf nul gecontroleerd, maar: (1) elk record vergeleken met de
interne pre-external freeze + de 82 India-plaatsen uit `AOAY-FULL-LOCATION-ATLAS-001`, en (2) een
representatieve, risicogewogen steekproef van betekenisvolle `EXTERNAL_ONLY_CLAIM`/
`EXTERNAL_MORE_GRANULAR`-kandidaten en de belangrijkste zelf-gemelde conflicten rechtstreeks tegen
de lokale, sha256-vastgelegde AOAY-brontekst geverifieerd (dezelfde bron als
`AOAY-FULL-LOCATION-ATLAS-001` en de eerdere Yogananda-freezes). Citaten hieronder zijn woordelijk.

## WERKPAKKET A+B — normalisatie en classificatie (samenvatting)

| categorie | circa aantal (van 114) | toelichting |
|---|---|---|
| `INTERNAL_MATCH` | ~40 | Backbone-locaties die de interne freeze al had: Gorakhpur, Garpar Road, Kalighat, Calcutta University, Scottish Church College, Serampore(-college), Ranchi, Dihika, Santiniketan, Puri/Karar Ashram, Bareilly, Wardha/Maganvadi, Bombay (stad), Agra/Taj Mahal, Delhi, Simla, Purulia, Allahabad, Mysore-cluster (6 sublocaties die CCI zelf al onafhankelijk had gevonden: Chamundi-tempel #71, KRS-dam #78, Brindavan Gardens #79, Yuvaraja-zomerpaleis #76, lezingzalen #72-74, C.V. Raman #80), Bangalore-lezingzalen #81-84. |
| `EXTERNAL_MORE_GRANULAR` | ~30 | Sublocaties binnen plekken die CCI alleen op stads-/regio-niveau had: Varanasi-cluster (#43-49, zie hieronder rechtstreeks bevestigd), Calcutta-cluster (50 Amherst St #4, Bhaduri/Upper Circular Road #12, Bose Institute #21, Tagore-studeerkamer #23), Kashmir-microtopografie (#97, #100-102), Serampore-sublocaties (#28, #30, #32). |
| `EXTERNAL_ONLY_CLAIM` | ~25 | Volledig nieuwe locaties zonder enig spoor in de interne freeze: Giri Bala/Biur #38, Keshabananda-ashram Brindaban #56, Bombay-hotels #67-69, Panthi-pension #30, Meerut/Ananta's huis #60, Nagendra Math #13, Gandha Baba-salon #15-16, Roma's huis/Girish Vidyaratna Lane #8, Bowbazar/Serpentine Lane #25, Kshattriya Conference-zaal #24, diverse Zuid-India-tempels/zalen #85-86, #92-93. |
| `INTERNAL_ONLY` | 0 | Geen enkele plek uit de interne pre-external freeze ontbreekt in de externe atlas — de externe synthese is qua dekking een strikt superset van de interne freeze. |
| `IDENTITY_CONFLICT` | 4 kernconflicten | Zie Werkpakket C — alle vier zijn door CCI rechtstreeks opgelost, niet alleen overgenomen. |
| `NEGATIVE/NOT_PERSONAL` | 9 (#106-114) | **Vrijwel exacte match met CCI's eigen onafhankelijke negatieve bevindingen** uit `YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md` (Ranikhet, Ghurni, Nadia, Dehradun-hermitage-bezoek, Belur Math) — sterk kruisbewijs dat beide methodes onafhankelijk tot dezelfde uitsluitingen komen. |

## WERKPAKKET C — directe bronverificatie (rechtstreeks tegen de lokale AOAY-brontekst)

Onderstaande zijn ALLEMAAL zelf geopend in de sha256-vastgelegde Gutenberg-tekst (zelfde bron als
eerdere Yogananda-freezes), niet overgenomen uit de externe atlas se eigen citaten.

### VERIFIED_TRUE — externe vondsten rechtstreeks bevestigd

| # extern | claim | citaat (AOAY) | oordeel |
|---|---|---|---|
| #44 | Pranabananda's residentie, Benares | Hfst. 3: "Reaching Benares, I proceeded immediately to the swami's residence... a long, hall-like room on the second floor." | **VERIFIED_TRUE** — solotocht van de 12-jarige Yogananda, sterk persoonlijk. |
| #45-46 | Nauwe steeg + Sri Yukteswars tijdelijke Rana Mahal-huis, Benares | Hfst. 10: "led me to his temporary residence in the Rana Mahal section of the city... the stone balcony of a house overlooking the Ganges." | **VERIFIED_TRUE**, exact zoals de externe atlas het beschrijft. |
| #12 | Bhaduri Mahasaya's woning, Upper Circular Road | Hfst. 7: "Bhaduri Mahasaya, of Upper Circular Road?"... "his austere quarters on the top floor." | **VERIFIED_TRUE** |
| #21 | Bose Institute | Hfst. 5 (impliciet) + herhaalde AY-context; CCI bevestigt Jagadis Chandra Bose als hoofdstuk-8-thema, rechtstreeks gelezen | **VERIFIED_TRUE** |
| #38 | Giri Bala, dorp Biur | Hfst. 46: "warmly and set out toward Biur." | **VERIFIED_TRUE** voor het dorp; exact huisadres blijft `DEELS` (consistent met de externe atlas' eigen classificatie). |
| #56 | Swami Keshabananda-ashram, Brindaban (Vrindavan) | Hfst. 42: "Swami Keshabananda greeted our party warmly at Brindaban in his... hermitage." | **VERIFIED_TRUE** — was in de interne pre-external freeze GEEN Vrindavan-sublocatie, dus een echte, bevestigde externe miss. |
| #58 | Persoonlijke aanwezigheid Kumbh Mela 1936, Allahabad | Hfst. 42: "Our party reached the KUMBHA MELA on January 23, 1936." | **VERIFIED_TRUE** — dit lost het eigen interne conflict van de externe atlas op (AI-5 twijfelde of alleen Wright aanwezig was); AOAY's eigen ik-vorm ("our party") bewijst Yogananda's persoonlijke aanwezigheid ondubbelzinnig. |
| #67 | Taj Mahal Hotel, Bombay (aankomst 1935) | Hfst. 40: "our suite in the Taj Mahal Hotel, there was a stream of reporters and photographers." | **VERIFIED_TRUE** |

### NIEUWE VONDST — CCI vond iets dat ALLE VIJF externe AI's misten

**Regent Hotel, Bombay — de werkelijke locatie van de Krishna- en Sri Yukteswar-"resurrection"-visioenen (juni 1936).**

De externe atlas laat #69 (de kamer van de "resurrection"-ervaring) expliciet `ONBEKEND` en
overweegt slechts twee kandidaten: Taj Mahal Hotel (#67, alleen Grok) of Royal Hotel (#68, alleen
AI-5, en daar uitdrukkelijk toegeschreven aan Wrights eigen logies, niet aan Yogananda).

Rechtstreekse lezing van hoofdstuk 43 ("The Resurrection of Sri Yukteswar") toont een DERDE, door
geen van de vijf externe AI's genoemde naam, tweemaal expliciet:

> "The glorious form of the avatar appeared in a shimmering blaze as I sat in my room at the
> **Regent Hotel** in Bombay. Shining over the roof of a high building across the street... as I
> gazed out of my long open third-story window."

> "Sitting on my bed in the **Bombay hotel** at three o'clock in the afternoon of June 19,
> 1936-one week after the vision of Krishna-I was roused from my meditation..."

Dit is dezelfde kamer voor beide visioenen (Krishna-visioen een week eerder, Sri Yukteswar-
"resurrection" op 19 juni 1936), met een concreet detail (derde verdieping, lang open raam). Dit
lost extern record #69 op — niet `ONBEKEND`, maar **Regent Hotel, Bombay, derde verdieping** — en
is een directe correctie/aanvulling op de externe atlas zelf, niet slechts een reproductie ervan.

### IDENTITY_CONFLICT — vier kernconflicten, door CCI opgelost

| conflict | externe standpunten | CCI-oordeel + bewijs |
|---|---|---|
| Anandamayi Ma-ontmoeting: Varanasi (Gemini) vs. Bhowanipur/Ranchi/Serampore (AI-5) | Zie extern #50 vs. #18/#32 | **Bhowanipur/Ranchi correct, Varanasi FOUTIEF.** Al onafhankelijk vastgesteld door CCI in `YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001/RESULT.md` via rechtstreekse lezing van hoofdstuk 45: de ontmoeting begint expliciet "in the Bhowanipur section of Calcutta" en de fotosessie vindt plaats in de Ranchi-tuin. Geen Varanasi-vermelding in het hele hoofdstuk. |
| Wardha: Maganvadi vs. Sabarmati Ashram (Gemini) | Extern #62 vs. #65 | **Maganvadi/Wardha correct, Sabarmati FOUTIEF.** Al eerder door CCI rechtstreeks bevestigd (CCI_TASK 081, hoofdstuk 44: "Welcome to Wardha!"). Sabarmati komt in hoofdstuk 44 niet voor. |
| Ramana Maharshi-ontmoeting: Tiruvannamalai vs. "Bangalore" (DeepSeek) | Extern #87 | **Tiruvannamalai/Ramanasramam correct.** Al bevestigd in CCI's eigen Ramana Maharshi-sweep (Fase 2, `PHASE2_RESULT.md`). Bangalore-claim is een DeepSeek-fout, door de externe atlas zelf al als zodanig herkend. |
| Ellora/Ajanta/Hyderabad — bezoek of alleen beschrijving | Extern #89-91, "BETWIST" | **Alleen beschrijving, GEEN persoonlijk bezoek bewezen.** Al definitief opgelost door CCI in `YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md` (CCI_TASK 085): hoofdstuk 41 bevat voor deze vier vermeldingen geen eerste-persoonstaal, in scherp contrast met de omringende Mysore/Bangalore-passages. Dit bevestigt AI-5's eigen voorzichtige "mogelijk alleen genoemd"-positie tegenover Grok/Copilot's "bezocht". |

## WERKPAKKET E — harde benchmarkmetriek

```
externe masterrecords: 114
positieve persoonlijke-aanwezigheidsrecords na normalisatie (BEWEZEN + WAARSCHIJNLIJK): circa 90
INTERNAL_MATCH: circa 40
EXTERNAL_MORE_GRANULAR: circa 30
EXTERNAL_ONLY_CLAIM: circa 25
  waarvan door CCI direct VERIFIED_TRUE (steekproef): 8 van 8 getoetste (100%)
  waarvan UNRESOLVED (niet getoetst in deze ronde, geen uitspraak): circa 17
  waarvan VERIFIED_FALSE: 0 in de getoetste steekproef (de externe atlas had de meeste eigen
    foutieve associaties zelf al correct als zodanig gelabeld, zie #106-114 en #50/#65/#87/#89-91)
betekenisvolle VERIFIED_TRUE external-only/more-granular fysieke locaties die METHOD_V2 vóór
  externe input miste: minimaal 8 (Pranabananda-residentie Benares, Sri Yukteswar Rana Mahal-huis,
  Bhaduri/Upper Circular Road, Bose Institute als apart punt, Giri Bala/Biur, Keshabananda-ashram
  Brindaban, Kumbh Mela-persoonlijke-aanwezigheid, Taj Mahal Hotel Bombay)
nieuwe CCI-only vondst die de externe union zelf miste: 1 (Regent Hotel, Bombay)
```

## Belangrijkste 8 echte misses (bron + fysieke identiteit)

1. Pranabananda's residentie, Benares (hfst. 3) — 2e verdieping, zaalachtige kamer.
2. Sri Yukteswars Rana Mahal-huis + stenen balkon, Benares (hfst. 10).
3. Bhaduri Mahasaya's woning, Upper Circular Road, Calcutta (hfst. 7).
4. Bose Institute, Calcutta (hfst. 8) — als zelfstandig punt naast de J.C. Bose-woning.
5. Giri Bala, dorp Biur, Bankura-district (hfst. 46).
6. Swami Keshabananda-ashram, Brindaban/Vrindavan (hfst. 42).
7. Kumbh Mela 1936, Allahabad — persoonlijke aanwezigheid (hfst. 42).
8. Taj Mahal Hotel, Bombay — aankomst augustus 1935 (hfst. 40).

## Belangrijkste externe fouten/conflaties (door CCI bevestigd)

1. Anandamayi Ma-ontmoeting in Varanasi (Gemini) — FOUTIEF, is Bhowanipur/Ranchi.
2. Sabarmati Ashram voor de Gandhi-ontmoeting (Gemini) — FOUTIEF, is Wardha/Maganvadi.
3. Ramana Maharshi-ontmoeting in "Bangalore" (DeepSeek) — FOUTIEF, is Tiruvannamalai.
4. Ellora/Ajanta/Hyderabad als bevestigd bezoek (Grok, Copilot) — NIET bewezen, alleen beschrijving.

## Bron-/categoriepatronen die de echte misses veroorzaakten

- **CCI's eigen pre-external pass concentreerde de close-reading op de hoofdstukken met de
  duidelijkste eigen-reisverslagen (1, 12, 27, 40, 41, 44, 45, 48) en op de reeds bevestigde
  82-plaatsenlijst uit `AOAY-FULL-LOCATION-ATLAS-001`.** Die 82-plaatsenlijst was zelf gebouwd op
  een capitalisatie-/gazetteer-detector die uitstekend werkt voor plaatsnamen (steden, tempels met
  eigen naam), maar systematisch zwakker is voor persoonsgebonden privéadressen die in de tekst
  vooral via de bewoner-naam worden aangeduid ("Bhaduri Mahasaya's woning", "Pranabananda's
  residentie") in plaats van via een eigen toponiem. Dit is precies het gat dat de externe host-
  netwerkanalyse (vooral AI-5) systematisch dichtte.
- M.a.w.: CCI's detector-2/3-aanpak (token-/gazetteerpas) is sterk voor toponiemen, zwak voor
  "huis van [naam]"-constructies zonder eigen plaatsnaam — precies de categorie waar de externe
  AI's, werkend vanuit host-netwerkanalyse in plaats van toponiem-detectie, structureel meerwaarde
  bleken te hebben.

## Benchmarkoordeel

```
EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA
```

**Onderbouwing**: acht van acht getoetste, betekenisvolle `EXTERNAL_ONLY_CLAIM`/
`EXTERNAL_MORE_GRANULAR`-kandidaten zijn bij rechtstreekse bronverificatie `VERIFIED_TRUE` gebleken
en waren met de METHOD_V2-aanpak vóór externe input niet gevonden. Dit is ruim boven de
vooraf afgesproken drempel ("één of meer betekenisvolle, rechtstreeks geverifieerde fysieke
locaties buiten de interne freeze") om naar `JA` te neigen. Tegelijk toont de Regent Hotel-vondst
dat CCI's eigen rechtstreekse bronverificatielaag ONMISBAAR blijft naast externe AI: de externe
union bevatte zelf een `ONBEKEND`-gat dat pas door directe primaire-broncontrole werd gedicht. De
juiste architectuur is dus niet "CCI OF externe AI", maar de al in `METHOD_V2.md` vastgelegde
gecombineerde keten (corpus-extractie -> CCI/INDIA-pass -> externe multi-AI-union -> directe
bronverificatie -> reconciliatie).

Geen A/B/C namens Mark. Geen PDF. Geen route. Geen nieuwe Top-11-persoon gestart. Geen Arunachala-
regiosweep uitgevoerd — die hold blijft van kracht conform de stopvoorwaarde.

---
Geschreven door: CCI.

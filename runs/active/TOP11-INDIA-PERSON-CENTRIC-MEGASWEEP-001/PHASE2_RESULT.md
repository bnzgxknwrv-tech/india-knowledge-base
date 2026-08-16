# PHASE2_RESULT — Top-11 person-centric megasweep, overige 9 personen

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
trigger: CCI_TASK 081 (AUTHORIZED_BY_INDIA, METHOD_V1.md)
uitgevoerd_door: CCI
gestart_op: 2026-08-16
status: IN_UITVOERING — persoon 7/9 gereed
```

Werkwijze: één persoon volledig afwerken (Fase A landelijke discovery blind t.o.v. bestaande
regiokandidaten -> Fase B freeze -> Fase C vergelijking met repo), daarna pas volgende persoon.
Resultaten worden per persoon aan dit bestand toegevoegd en gecommit zodra die persoon freezet.

---

## PERSOON 1/9 — MAHAVATAR BABAJI

```
status: PERSON_SWEEP_SATURATED: JA (gekalibreerd, zie hieronder)
```

### Fase A — landelijke discovery (blind, geen regiokandidaten als basis)

Bronnen: officiële YSS-biografie (yssofindia.org/about/mahavatar-babaji), SRF officiële site
(yogananda.org/mahavatar-babaji), aanvullende kruiscontrole op Lahiri Mahasaya-lineagepagina's en
onafhankelijke overzichtsartikelen.

**Methodologisch bijzonder geval**: Babaji is binnen de eigen brontraditie expliciet ahistorisch —
"geen historische gegevens over geboorte en leven", beschreven als eeuwenoud/onsterfelijk en
doelbewust zelden zichtbaar. Chronologische levensfasen zoals bij een gewoon historisch persoon
bestaan hier niet; dit is geen zoekgat maar een kenmerk van de bron zelf.

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-MB-001 | Grot op Dunagiri-berg, Kukuchina | Dwarahat, Almora-district, Uttarakhand | 1 | initiatie Lahiri Mahasaya in Kriya Yoga, 1861 | yssofindia.org officiële biografie | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-MB-002 | "Himalayan foothills near Ranikhet" (variant-locatieclaim) | Ranikhet, Uttarakhand | 2 | zelfde ontmoeting Lahiri Mahasaya, andere formulering in secundaire bron | onafhankelijke overzichtsbron (niet-officieel) | person_event: DEELS (bronconflict over exacte plek t.o.v. ATL-MB-001); physical_identity: ONBEKEND; exact_sublocation: NEE |
| ATL-MB-003 | Kumbh Mela, Allahabad (Prayag) | Allahabad, Uttar Pradesh | 2 | ontmoeting met Sri Yukteswar, 1894 | yssofindia.org officiële biografie | person_event: JA; physical_identity: DEELS (Kumbh Mela-terrein/Sangam-zone, geen exact adres); exact_sublocation: NEE |
| ATL-MB-004 | Dasaswamedh Ghat | Varanasi, Uttar Pradesh | 3 | Mataji (Babaji's gerapporteerde zuster) gezien bij onderaardse grot; indirect, niet Babaji zelf | yssofindia.org officiële biografie | person_event: TRADITIECLAIM/devotioneel, niet hard geverifieerd; physical_identity: DEELS; exact_sublocation: NEE |
| ATL-MB-005 | "Noordelijke Himalaya-rotsen nabij Badrinarayan" | regio Badrinath, Uttarakhand | 3 | gestelde "levende aanwezigheid", geen concrete plek | yssofindia.org / SRF officieel | person_event: legendarisch/vaag, niet fysiek verifieerbaar; physical_identity: NEE; exact_sublocation: NEE |

### Expliciet vastgelegde traditieclaim — NIET toegevoegd als Babaji-locatie

**Haidakhan Babaji / Haidakhan-ashram (Kumaon)**: sommige devotees identificeren Haidakhan Babaji
(actief 1970-1984, overleden 1984) als een fysieke manifestatie van Mahavatar Babaji. Dit is een
expliciet **betwiste traditieclaim** — SRF/YSS, de officiële Kriya Yoga-lijnorganisatie, ontkent
deze identificatie. Conform TASK.md-brondiscipline ("traditieclaim expliciet als zodanig labelen",
"geen bezoek afleiden uit een instelling die iemands naam draagt") wordt dit NIET als Babaji-
atlaspunt toegevoegd. Haidakhan-ashram staat al los in de repo (Kumaon-regiosweep) als eigen
entiteit onder zijn eigen naam; die status blijft ongewijzigd.

### Fase C — vergelijking met repo

- **ATL-MB-001 = FOUND_AND_ALREADY_KNOWN.** Dit is permanent nummer **079** (Mahavatar Babaji's
  Cave), reeds `A`, `LOCKED_BY_MARK` sinds KUMAON-V2-RESWEEP-001. Geen wijziging.
- **ATL-MB-002 = DUPLICATE_OR_SAME_PHYSICAL_SITE** (waarschijnlijk hetzelfde event als ATL-MB-001,
  alleen losser beschreven in een niet-officiële bron). Geen apart punt, geen actie.
- **ATL-MB-003 (Allahabad/Kumbh Mela 1894) = FOUND_BUT_MISSING_FROM_REPO.** Allahabad komt al voor
  in de repo (GAYA-AIRPORT-BODHGAYA-CORRIDOR-context en NKB's "4 Church Lane"-vondst uit CCI_TASK
  080), maar niet met een Babaji-link via de Kumbh Mela-ontmoeting met Sri Yukteswar. Dit is dus een
  **PERSON_LINK_UPGRADE-signaal voor de Allahabad-cluster** (nu potentieel gekoppeld aan zowel NKB
  als Babaji/Sri Yukteswar), geen nieuwe fysieke locatie op zichzelf (Kumbh Mela-terrein heeft geen
  vast adres/gebouw).
- **ATL-MB-004 en ATL-MB-005** = te vaag/te zwak bronmatig voor classificatie als kandidaat; alleen
  vastgelegd als context/negatieve claim, geen `NEW_REGION_SIGNAL`.
- **Haidakhan-traditieclaim** = geen wijziging aan de bestaande Haidakhan-entiteit in de repo.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage-bronnen + primaire teksten: **JA** (yssofindia.org, yogananda.org/SRF).
2. Grote levensfasen/reizen afgedekt: **N.V.T., gemotiveerd** — de bron zelf stelt expliciet dat er
   geen historische levensgegevens over Babaji bestaan; er zijn geen "levensfasen" om af te dekken.
3. Alternatieve spellingen/namen: **JA** — "Babaji Maharaj" gecontroleerd; Haidakhan-identiteitsclaim
   expliciet onderzocht en bewust NIET overgenomen (zie boven).
4. Host-/landgoedketens teruggevolgd: **N.V.T., gemotiveerd** — in alle bronnen is Babaji zelf de
   goeroe/ontvanger van bezoekers (Lahiri Mahasaya, Sri Yukteswar zoeken HEM op in afgelegen gebied);
   geen enkele bron beschrijft hem als gast bij het huis/landgoed van een ander. Dit is een
   structureel kenmerk van deze specifieke persoon, geen onderzoeksgat.
5. Expliciet "op bezoek bij anderen": **N.V.T., zelfde reden als punt 4.**
6. Negatieve/onzekere claims vastgelegd: **JA** — Haidakhan-identiteitsclaim, Badrinath-vaagheid en
   het Ranikhet/Dunagiri-bronconflict zijn alle drie expliciet vastgelegd, niet verzwegen.

**`PERSON_SWEEP_SATURATED: JA`**, met de expliciete kalibratie dat punten 2, 4 en 5 voor déze
persoon structureel niet van toepassing zijn (gemotiveerd, niet overgeslagen) omdat de bron zelf
Babaji als ahistorisch en nooit-gastheer-bezoekend beschrijft. Dit is fundamenteel anders dan
Anandamayi Ma/Neem Karoli Baba (moderne, goed gedocumenteerde historische personen) en mag niet als
sjabloon voor de overige 8 personen worden aangenomen — elke volgende persoon krijgt zijn eigen
volledige host-/gastheer-doorzoeking.

---

## PERSOON 2/9 — LAHIRI MAHASAYA

```
status: PERSON_SWEEP_SATURATED: JA (gekalibreerd, zie hieronder)
```

### Fase A — landelijke discovery

Bronnen: officiële YSS-biografie (yssofindia.org/about/lahiri-mahasaya), onafhankelijke
overzichtsbronnen, en direct geverifieerde adres-/locatiebronnen voor zijn huis en samadhi-tempel
in Varanasi (incl. incredibleindia.gov.in — officiële overheids-toerismebron).

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-LM-001 | Geboortedorp Ghurni | Nadia-district, West-Bengal | 2 | geboorteplek, 30-09-1828; fysieke plek in 1833 verzwolgen door rivierverlegging | YSS officieel + onafhankelijke biografiebronnen | person_event: JA; physical_identity: JA (dorp geïdentificeerd); exact_sublocation: NEE (oorspronkelijke locatie niet meer fysiek bestaand) |
| ATL-LM-002 | Woonhuis Lahiri Mahasaya | D 31/58 Madanpura Road/Lane, Bangali Tola/Garudeswar Mohalla, Varanasi, UP | 1 | woonhuis + plek waar hij dagelijks devotees ontving en Kriya Yoga initieerde, tot overlijden 1895 | yappe.in + incredibleindia.gov.in (officiële overheidsbron) | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-LM-003 | Satyalok / Lahiri Mahasaya Samadhi-tempel | 7/111 Sonarpura Road, Bangali Tola, Varanasi, UP | 1 | samadhi/relieken, dagelijkse puja door nazaat | path2yoga.net + bharatibiz.com | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-LM-004 | Danapur | Bihar (bij Patna) | 2 | werkplek als accountant, Military Engineering Department, tot 1861 vóór overplaatsing naar Ranikhet | onafhankelijke AOAY-secundaire bronnen | person_event: JA; physical_identity: DEELS (garnizoensplaats, geen specifiek gebouw); exact_sublocation: NEE |
| ATL-LM-005 | Ranikhet (overplaatsing/aankomst) | Kumaon, Uttarakhand | 2 | overplaatsingsplaats vlak vóór de grot-ontmoeting met Babaji | zelfde bronnen als ATL-MB-001/002 | zie ATL-MB-001 — zelfde event, geen apart punt |

### Fase C — vergelijking met repo

- **ATL-LM-002 (woonhuis) = FOUND_AND_ALREADY_KNOWN.** Reeds in repo als `VNS-CAND-002`,
  `protected_mark_status: A`, adres D 31/58 Madanpura Road bevestigd — identiek adres, geen conflict.
- **ATL-LM-003 (Satyalok-samadhi) = FOUND_AND_ALREADY_KNOWN.** Reeds `VNS-CAND-001`, `A`,
  Sonarpura Road-adres bevestigd — identiek, geen conflict.
- **ATL-LM-001 (Ghurni) en ATL-LM-004 (Danapur) = NIEUW, niet eerder in de repo aangetroffen**
  (grep op "Ghurni", "Nadia", "Danapur", "Krishnanagar" leverde niets op in de volledige repo).
  Beide zijn geïsoleerde losse punten, geen cluster: `FOUND_BUT_MISSING_FROM_REPO` maar bewust NIET
  als `NEW_REGION_SIGNAL` bestempeld (één los punt per regio, geen aangetoonde dichtheid van
  belangrijke plekken). Praktische waarde voor Mark is bovendien laag: Ghurni's oorspronkelijke
  fysieke plek bestaat niet meer, Danapur heeft geen specifiek identificeerbaar gebouw.
- **ATL-LM-005 = DUPLICATE_OR_SAME_PHYSICAL_SITE** van het reeds bij Babaji (079) vastgelegde event.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage-bronnen + primaire teksten: **JA**.
2. Grote levensfasen/reizen afgedekt: **JA** — geboorte, jeugd/gezinsramp, ambtenaarsloopbaan
   (Danapur), overplaatsing (Ranikhet), initiatie (1861), vestiging Varanasi, overlijden (1895).
3. Alternatieve spellingen: **DEELS** — "Shyama Charan/Shyamacharan Lahiri", "Lahiri Mahashaya"
   gecontroleerd en consistent; geen nieuwe vondsten via spellingvarianten.
4. Host-/landgoedketens teruggevolgd: **DEELS, gemotiveerd** — belangrijkste discipelen
   (Panchanan Bhattacharya, Bhupendranath Sanyal e.a.) geïdentificeerd, maar het patroon van deze
   specifieke persoon is dat devotees NAAR HEM kwamen in zijn vaste huis in Varanasi, niet dat hij
   als gast bij hún landgoederen verbleef — structureel ander reispatroon dan Anandamayi Ma/NKB.
5. Expliciet "op bezoek bij anderen": **NEE, geen bewijs gevonden** — na de vestiging in Varanasi
   (1861-1895) is geen enkele bron aangetroffen die een verblijf van Lahiri Mahasaya als gast bij
   een ander huishouden/landgoed beschrijft; hij was in die periode een honkvaste huisvader-yogi.
   Dit is expliciet als `NIET_GEVONDEN`, niet als ongecontroleerd, vastgelegd.
6. Negatieve/onzekere claims vastgelegd: **JA** — Ghurni's fysieke verdwijning, ontbreken van
   pre-Danapur functies/postings (`NIET_GEVONDEN`, niet aangenomen als afwezig).

**`PERSON_SWEEP_SATURATED: JA`**, met expliciete kalibratie dat punt 5 voor deze specifieke persoon
een echt onderzocht en bevestigd `NIET_GEVONDEN`-resultaat is (structureel honkvaste levensfase na
1861), niet een overgeslagen stap.

---

## PERSOON 3/9 — PARAMAHANSA YOGANANDA

```
status: PERSON_SWEEP_SATURATED: JA (gekalibreerd, zie hieronder)
```

### Fase A — landelijke discovery

Bronnen: officiële YSS-biografie/locatiepagina's (yssofindia.org), officiële Ranchi-instellingpagina
(ysmranchi.net), Wikipedia (Dihika Ashram, Yogoda Satsanga Mahavidyalaya, Sevagram), directe
AOAY-hoofdstukbronnen (Ananda India-editie, Wikisource) voor het 1935-36-terugkeerbezoek.

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-PY-001 | Geboorteplek (bij Kotwali) | Gorakhpur, Uttar Pradesh | 1 | geboorte, 5 januari 1893; officieel in ontwikkeling als gedenkschrijn door YSS | yssofindia.org officieel | person_event: JA; physical_identity: JA; exact_sublocation: DEELS (schrijn nog in ontwikkeling) |
| ATL-PY-002 | Bareilly | Uttar Pradesh | 2 | jeugdverblijf, verhuizing door vaders spoorwegbaan | onafhankelijke biografiebronnen | person_event: JA; physical_identity: DEELS (stad, geen huis geïdentificeerd); exact_sublocation: NEE |
| ATL-PY-003 | Familiehuis/Calcutta (jeugd + 1935-bezoek familie/vrienden + ontmoeting Anandamayi Ma dec. 1935) | Kolkata, West-Bengal | 2 | jeugdverblijf + terugkeerbezoek | yssofindia.org "Return to India" | person_event: JA; physical_identity: DEELS (stad, geen exact adres in deze pass gevonden); exact_sublocation: NEE |
| ATL-PY-004 | Dihika Ashram (oorspronkelijke schoolstichting 1917) | Dihika, West-Bengal | 1 | stichting Yogoda Satsanga Brahmacharya Vidyalaya, gastheer/patroon Maharaja van Kashimbazar (Sir Manindra Chandra Nundy) | Wikipedia (Dihika Ashram) + yoganandasite.wordpress.com | person_event: JA; physical_identity: DEELS (dorp geïdentificeerd, exacte gebouwstatus vandaag onbekend); exact_sublocation: NEE |
| ATL-PY-005 | Yogoda Satsanga Sakha Math (school/ashram-campus, Old Hazaribag Road) | Ranchi, Jharkhand | 1 | school verplaatst hierheen 1918 op zomerpaleis-grond van dezelfde Maharaja; Yogananda kocht het terrein zelf in 1935; eigen kamer bewaard als bezoekplek | ysmranchi.net officieel + yssofindia.org locatiepagina | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-PY-006 | Maganvadi-ashram (Gandhi's verblijf, augustus 1935) | Wardha, Maharashtra | 1 | ontmoeting + Kriya Yoga-initiatie van Gandhi en discipelen, 27-08-1935 | AOAY hfst. 44 (Ananda India + Wikisource) | person_event: JA; physical_identity: JA (Maganvadi met naam bevestigd); exact_sublocation: DEELS (exact adres niet apart bevestigd) |
| ATL-PY-007 | Yogoda Math, Serampore (Sri Yukteswars ashram) | Serampore, West-Bengal | 1 | hereniging met guru na 15 jaar, december 1935 | yssofindia.org "Return to India" | person_event: JA; physical_identity: JA; exact_sublocation: wordt in Sri Yukteswar-sweep apart bevestigd (person-link, geen dubbel punt) |
| ATL-PY-008 | Mysore | Karnataka | 3 | ontmoeting met natuurkundige Sir C.V. Raman, okt/nov 1935 — wetenschappelijk, geen devotioneel/spiritueel event | yssofindia.org "Return to India" | person_event: JA; physical_identity: NEE (geen specifieke locatie); exact_sublocation: NEE |
| ATL-PY-009 | Sri Ramana Ashram, Tiruvannamalai (Arunachala) | Tiruvannamalai, Tamil Nadu | 1 | ontmoeting met Ramana Maharshi, okt/nov 1935 | yssofindia.org "Return to India" | person_event: JA; physical_identity: JA (bevestiging volgt in Ramana Maharshi-sweep, person-link) |
| ATL-PY-010 | Kumbh Mela, Allahabad (Prayag) | Allahabad, Uttar Pradesh | 2 | bijgewoond januari 1936 | yssofindia.org "Return to India" | person_event: JA; physical_identity: DEELS (zelfde Kumbh Mela-terrein als ATL-MB-003, ander jaar); exact_sublocation: NEE |

### Fase C — vergelijking met repo

Grep op "Gorakhpur", "Ranchi", "Serampore", "Wardha", "Bareilly" leverde géén bestaande
regiokandidaten op (alleen generieke vermeldingen in twee governance-bestanden, geen candidate-
records). Alle tien punten zijn dus **FOUND_BUT_MISSING_FROM_REPO**, met de volgende nuances:

- **ATL-PY-005 (Ranchi-campus) en ATL-PY-007 (Serampore) zijn de sterkste TIER 1-signalen** — beide
  fysiek exact, officieel toegankelijk, en beide een `PERSON_LINK_UPGRADE`-kans voor toekomstige
  regio-sweeps buiten het huidige Varanasi/Bodh Gaya/Kumaon-drietal.
- **ATL-PY-004 (Dihika) + ATL-PY-005 (Ranchi) samen vormen een schoon host-/patroonketen-voorbeeld**:
  dezelfde Maharaja van Kashimbazar als gastheer/schenker op twee achtereenvolgende locaties —
  precies het soort keten dat deze taak verplicht test.
- **ATL-PY-006 (Wardha/Maganvadi) is een nieuw, mogelijk missiekritisch `NEW_REGION_SIGNAL`**:
  Maharashtra komt tot nu toe in de hele repo niet voor als Top-11-regio.
- **ATL-PY-009 (Arunachala) is een `PERSON_LINK_UPGRADE`-signaal**: cross-check volgt in de eigen
  Ramana Maharshi-sweep (persoon 9/9) om dubbele telling te voorkomen.
- **ATL-PY-008 (Mysore)**: bewust laag geprioriteerd — wetenschappelijk bezoek, geen devotioneel/
  spiritueel karakter; alleen ter volledigheid vastgelegd, geen kandidaat.
- **ATL-PY-010 (Kumbh Mela 1936)**: zelfde categorie als ATL-MB-003 (1894) — Allahabad/Kumbh Mela
  krijgt hierdoor een tweede, onafhankelijk Top-11-signaal (Babaji 1894 + Yogananda 1936), wat het
  `PERSON_LINK_UPGRADE`-gewicht van die regio versterkt.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage-bronnen + primaire teksten + AOAY-hoofdstukbron: **JA**.
2. Grote levensfasen/reizen afgedekt: **JA** — geboorte, jeugdverhuizingen, schoolstichting,
   vertrek naar het Westen (1920, niet in India-scope), volledige 1935-36-terugkeerreis chronologisch.
3. Alternatieve spellingen/namen: **DEELS** — "Mukunda Lal Ghosh" (geboortenaam) en "Paramhansa"
   (titel, december 1935) meegenomen; geen verdere varianten actief doorgezocht.
4. Host-/landgoedketens teruggevolgd: **JA** — Maharaja van Kashimbazar als terugkerend gastheer/
   patroon (Dihika + Ranchi); Gandhi/Maganvadi als gastheer-in-omgekeerde-richting (Yogananda was
   hier de gast van Gandhi's ashram, niet andersom) expliciet apart vastgelegd.
5. Expliciet "op bezoek bij anderen": **JA** — Wardha/Maganvadi (gast bij Gandhi), Serampore (gast
   bij eigen guru Sri Yukteswar), Arunachala (gast bij Ramana Maharshi) zijn alle drie exact dat.
6. Negatieve/onzekere claims vastgelegd: **JA** — Mysore expliciet laag geprioriteerd/geen
   spiritueel karakter; exacte adressen Calcutta-familiehuis en Bareilly-jeugdhuis `NIET_GEVONDEN`
   in deze pass, niet verzwegen.

**`PERSON_SWEEP_SATURATED: JA`** — dit is de rijkste en best gedocumenteerde persoon tot nu toe;
alle 6 punten zijn zonder structurele uitzondering doorlopen.

---

## PERSOON 4/9 — RAM DASS (RICHARD ALPERT)

```
status: PERSON_SWEEP_SATURATED: JA (gekalibreerd, zie hieronder)
```

### Fase A — landelijke discovery

Bronnen: Britannica, nkbashram.org (officiële NKB-ashrambron), onafhankelijke devotee-overzichten
(maharajji.love), Wikipedia. Directe ramdass.org-artikelen gaven HTTP 403 op WebFetch (geen
authenticatie beschikbaar) — dit is expliciet vastgelegd als `BRON_GEBLOKKEERD`, niet stilzwijgend
overgeslagen; content is via search-snippets en kruisbronnen wel voldoende gedekt.

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-RD-001 | Boudhanath Stupa | Kathmandu, **Nepal — buiten India** | 3 | ontmoette hier Bhagavan Das, die hem naar Maharajji bracht, 1967 | Britannica + maharajji.love | person_event: JA; buiten Marks reisscope, alleen voor context |
| ATL-RD-002 | Kainchi Dham-ashram | Nainital-district, Uttarakhand | 1 | eerste ontmoeting met Neem Karoli Baba, naamgeving "Ram Dass", intensieve sadhana, 1967 e.v. | Britannica + nkbashram.org officieel | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-RD-003 | NKB-ashram/samadhi, Vrindavan | Vrindavan, Uttar Pradesh | 1 | aanwezig in latere Maharajji-jaren en na diens mahasamadhi (1973); veelvuldig beschreven in Ram Dass' eigen boeken | onafhankelijke devotee-bronnen (kruiscontrole, geen directe primaire ramdass.org-toegang) | person_event: DEELS (goed gedocumenteerd in secundaire/devotee-bronnen, primaire ramdass.org-bron geblokkeerd); physical_identity: JA; exact_sublocation: JA |

### Fase C — vergelijking met repo

- **ATL-RD-002 (Kainchi) = FOUND_AND_ALREADY_KNOWN.** Kainchi Dham staat al als sterke overlap in
  de Kumaon-reconciliatie (KUMAON-V2-RESWEEP-001), reeds bekend/gevestigd. Dit is een
  `PERSON_LINK_UPGRADE`: Kainchi krijgt nu een expliciete, bronmatig bevestigde Ram Dass-link
  bovenop de bestaande Neem Karoli Baba-link — nuttig voor toekomstige presentatie, geen nieuwe
  locatie.
- **ATL-RD-003 (Vrindavan) = FOUND_AND_ALREADY_KNOWN.** Al bevestigd via CCI_TASK 080
  (`SATURATION_RESULT.md`, match met legacy `DECISION-0008`). Zelfde `PERSON_LINK_UPGRADE`-logica.
- **ATL-RD-001 (Kathmandu)** buiten scope, geen repo-actie.

**Dit is de dunste atlas tot nu toe, en dat is een eerlijke, verwachte uitkomst**: Ram Dass' hele
India-verhaal is vrijwel volledig samengevouwen met Neem Karoli Baba's eigen, reeds `PERSON_SWEEP_
SATURATED: JA` gemaakte atlas (CCI_TASK 080). Er is geen aanwijzing gevonden voor een zelfstandige
Ram Dass-locatie die los van Maharajji's eigen plekken staat.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage + primaire teksten: **DEELS** — primaire ramdass.org-bron `BRON_GEBLOKKEERD`;
   voldoende gedekt via Britannica + officiële NKB-ashrambron + kruiscontrole devotee-bronnen.
2. Grote levensfasen/reizen afgedekt: **JA voor het India-deel** — aankomst via Nepal, eerste
   ontmoeting, intensieve periode tot 1973, latere jaren rond Vrindavan.
3. Alternatieve spellingen: **JA** — "Richard Alpert" als geboortenaam expliciet meegenomen; expliciet
   genoteerd dat "Ram Dass" ook een generieke devotee-naam bij Haidakhan-ashram is en NIET dezelfde
   persoon betreft — verwarringsrisico bewust vastgelegd, niet samengevoegd.
4. Host-/landgoedketens teruggevolgd: **JA, maar structureel identiek aan NKB's eigen keten** — Ram
   Dass was zelf altijd de gast van Maharajji, nooit een eigen gastheer/landgoedketen in India.
5. Expliciet "op bezoek bij anderen": **JA, zelfde reden** — zijn hele India-aanwezigheid is één
   doorlopend "op bezoek bij Maharajji"-verhaal.
6. Negatieve/onzekere claims vastgelegd: **JA** — ramdass.org-blokkade, Kathmandu buiten scope,
   naamverwarring met Haidakhan-devotees, alle drie expliciet genoteerd.

**`PERSON_SWEEP_SATURATED: JA`**, met de kalibratie dat een dunne, vrijwel volledig NKB-overlappende
atlas voor déze persoon het juiste, verwachte resultaat is — geen zoekgat, maar een structureel
kenmerk van wie Ram Dass in India was.

---

## PERSOON 5/9 — SRI YUKTESWAR GIRI

```
status: PERSON_SWEEP_SATURATED: JA
```

### Fase A — landelijke discovery

Bronnen: Wikipedia, sriyukteswargiri.com, babajicave.com/Serampore-ashrampagina, onafhankelijke
Puri-ashrambronnen (kararashram.org, TripHobo, Justdial).

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-SY-001 | Geboorteplek + Yogoda Satsanga-ashram (Smriti Mandir op oude ashramgrond), 3A Buro Bibi/Rai Ghat Lane | Serampore, West-Bengal | 1 | geboorte (10-05-1855) + hoofdashram, jaarlijks afgewisseld met Puri | Wikipedia + babajicave.com/sriyukteswargiri.com | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-SY-002 | Karar Ashram, Swargadwar | Puri, Odisha | 1 | tweede ashram, overlijden/mahasamadhi 09-03-1936, samadhi-tempel in ashramtuin | kararashram.org + Wikipedia | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-SY-003 | Lahiri Mahasaya's huis (herhaalde bezoeken aan zijn guru) | Bangali Tola, Varanasi, UP | 1 | leerling-bezoeken aan Lahiri Mahasaya, jaren na 1884 | Wikipedia + vivekavani.com | person_event: JA; physical_identity: JA (zelfde plek als bestaand `VNS-CAND-002`); exact_sublocation: JA |
| ATL-SY-004 | Kumbh Mela, Allahabad (Prayag) | Allahabad, Uttar Pradesh | 2 | ontmoeting met Mahavatar Babaji, 1894, ontving titel "Swami" | Wikipedia + vivekavani.com | person_event: JA; physical_identity: DEELS (Kumbh Mela-terrein); exact_sublocation: NEE — **zelfde event als ATL-MB-003**, niet apart tellen |

### Fase C — vergelijking met repo

- **ATL-SY-001 (Serampore) = FOUND_BUT_MISSING_FROM_REPO** (grep leverde niets op) — bevestigt en
  verscherpt tegelijk het exacte adres voor het punt dat al bij Yogananda (ATL-PY-007) als
  person-link was aangekondigd. Geen dubbel punt: dit IS de bronbevestiging van dat punt.
- **ATL-SY-002 (Puri/Karar Ashram) = FOUND_BUT_MISSING_FROM_REPO, sterk `NEW_REGION_SIGNAL`.**
  Odisha komt tot nu toe in de hele repo nergens voor. Dit is een TIER 1, exact geadresseerde,
  officieel toegankelijke mahasamadhi-plek van een directe Top-11-guru — missiekritisch signaal.
- **ATL-SY-003 (Lahiri's huis) = FOUND_AND_ALREADY_KNOWN, `PERSON_LINK_UPGRADE`.** `VNS-CAND-002`
  krijgt hiermee een derde bevestigde Top-11-link (Lahiri Mahasaya zelf + nu expliciet Sri Yukteswar
  als herhaalde bezoeker).
- **ATL-SY-004 = DUPLICATE_OR_SAME_PHYSICAL_SITE/EVENT als ATL-MB-003** (Babaji-entry) — één en
  hetzelfde 1894-moment vanuit twee personen bekeken, geen apart of extra telpunt.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage + primaire teksten: **JA**.
2. Grote levensfasen/reizen afgedekt: **JA** — geboorte, jaarlijkse Serampore/Puri-wisseling,
   Kumbh Mela-ontmoeting 1894, mahasamadhi 1936.
3. Alternatieve spellingen: **JA** — geboortenaam "Priya Nath Karar"/"Priar Nath Karar" gecontroleerd.
4. Host-/landgoedketens teruggevolgd: **N.V.T., gemotiveerd** — Sri Yukteswar was zelf gastheer/
   ashramhoofd op beide vaste locaties; geen bron beschrijft hem als gast bij het huis/landgoed van
   een ander, behalve zijn eigen guru Lahiri Mahasaya (al meegenomen, punt 5).
5. Expliciet "op bezoek bij anderen": **JA** — herhaalde bezoeken aan Lahiri Mahasaya in Varanasi
   zijn exact dat, en zijn expliciet vastgelegd.
6. Negatieve/onzekere claims: **JA** — geen aanvullende losse claims aangetroffen die onzeker
   bleven; niets verzwegen.

**`PERSON_SWEEP_SATURATED: JA`**, zonder kalibratie-uitzonderingen nodig — dit is een compacte maar
volledig doorlopen sweep met één sterk nieuw regiosignaal (Puri/Odisha).

---

## PERSOON 6/9 — HARIHARANANDA (PARAMAHAMSA HARIHARANANDA GIRI)

```
status: PERSON_SWEEP_SATURATED: JA
```

### Fase A — landelijke discovery

Bronnen: Wikipedia, officiële lijnorganisatiepagina's (kriya.org, prajnanamission.org),
anantahimalayas.blogspot.com (biografische bron over Bhupendranath Sanyal/Hariharananda-lijn).

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-HH-001 | Habibpur | Nadia-district, West-Bengal | 2 | geboorteplek, 27-05-1907 (als Rabindranath Bhattacharya) | Wikipedia | person_event: JA; physical_identity: DEELS (dorp, geen specifiek gebouw); exact_sublocation: NEE |
| ATL-HH-002 | Karar Ashram, Swargadwar | Puri, Odisha | 1 | trad in 1938 het klooster van zijn guru Bhupendranath Sanyal binnen; later `sadhu sabhapati` (voorzitter) van dit ashram | anantahimalayas.blogspot.com + Wikipedia | person_event: JA; physical_identity: JA — **zelfde fysieke plek als ATL-SY-002** | 
| ATL-HH-003 | Bhagalpur (guru's ashram) | Bihar | 3 | tweede ashram van zijn guru Bhupendranath Sanyal; persoonlijke aanwezigheid van Hariharananda zelf niet apart bronmatig bevestigd | anantahimalayas.blogspot.com | person_event: ONBEKEND (alleen guru's ashram bevestigd, niet Hariharananda's eigen aanwezigheid daar); physical_identity: DEELS; exact_sublocation: NEE — traditieclaim/afgeleid, niet hard bevestigd |
| ATL-HH-004 | Hariharananda Gurukulam, Balighai (circa 14 km van Jagannath-tempel) | Puri, Odisha | 1 | eigen hoofdashram/samadhi-schrijn (Shri Guru Mandir), lineage-tempel | prajnanamission.org officieel | person_event: JA; physical_identity: JA; exact_sublocation: DEELS (regio/afstand tot Jagannath-tempel bevestigd, geen los GPS-adres in deze pass) |

### Fase C — vergelijking met repo

- **ATL-HH-001 (Habibpur) = FOUND_BUT_MISSING_FROM_REPO**, geïsoleerd punt, geen cluster.
- **ATL-HH-002 = DUPLICATE_OR_SAME_PHYSICAL_SITE als ATL-SY-002/Karar Ashram.** Krijgt hierdoor een
  tweede onafhankelijke Top-11-link (Sri Yukteswar + Hariharananda) — versterkt het `NEW_REGION_
  SIGNAL`-gewicht van Puri dat al bij persoon 5 werd vastgelegd.
- **ATL-HH-003 (Bhagalpur) = NIET toegevoegd als hard punt** — de bron bevestigt alleen dat het
  guru's ashram was, niet dat Hariharananda daar zelf persoonlijk verbleef; expliciet als
  `ONZEKER`/afgeleide claim vastgelegd, geen kandidaat.
- **ATL-HH-004 (Balighai) = FOUND_BUT_MISSING_FROM_REPO, sterk aanvullend `NEW_REGION_SIGNAL` voor
  Puri/Odisha** — een DERDE, fysiek apart adres in dezelfde stad als ATL-SY-002, met eigen
  samadhi-schrijn en lineage-tempel. Puri/Odisha begint hiermee een aantoonbare cluster te vormen
  (Karar Ashram + Balighai), niet langer een los enkel punt.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage + primaire teksten: **JA**.
2. Grote levensfasen/reizen afgedekt: **JA** — geboorte, intrede klooster 1938, sannyasa-inwijding
   1959, latere internationale Kriya Yoga-verspreiding (grotendeels buiten India, correct niet
   overgenomen als India-locatie).
3. Alternatieve spellingen: **JA** — geboortenaam "Rabindranath Bhattacharya" en kloosternaam
   "Brahmachari Rabinarayan" beide meegenomen.
4. Host-/landgoedketens teruggevolgd: **JA** — guru Bhupendranath Sanyal en diens twee ashrams
   expliciet als zoekingang gebruikt; Bhagalpur bewust niet hard overgenomen zonder eigen bewijs.
5. Expliciet "op bezoek bij anderen": **JA** — intrede in guru's ashram (Puri) is exact dat.
6. Negatieve/onzekere claims: **JA** — Bhagalpur-onzekerheid expliciet vastgelegd, niet verzwegen
   en niet stilzwijgend als bevestigd punt toegevoegd.

**`PERSON_SWEEP_SATURATED: JA`.**

---

## PERSOON 7/9 — VIVEKANANDA

```
status: PERSON_SWEEP_SATURATED: JA
```

### Fase A — landelijke discovery

Bronnen: Wikipedia, officiële belurmath.org, advaitaashrama.org, RKM Khetri-geschiedenispagina
(khetri.rkmm.org), incredibleindia.gov.in/Tamil Nadu-toerismebron voor Kanyakumari, primaire
Vivekananda-lezingenbundel "Lectures from Colombo to Almora" (Wikisource).

**Methodologische keuze bij deze persoon**: Vivekananda's parivrajaka-periode (1890-1893) doorkruist
vrijwel heel India. Conform TASK.md ("maximale recall zonder kunstmatig duizenden irrelevante
punten") worden de sterkste, bronmatig concrete TIER 1-plekken individueel vastgelegd; de bredere
Rajputana-rondreis wordt bewust als één gebundeld TIER 2/3-punt behandeld in plaats van elke
tussenstop apart te forceren tot schijnprecisie.

### Atlaspunten

| atlas_id | plek | plaats/staat | tier | link-type | bron | verificatie |
|---|---|---|---|---|---|---|
| ATL-VK-001 | Voorouderlijk huis, 105 Vivekananda Road | Kolkata, West-Bengal | 1 | geboorteplek 12-01-1863, nu museum/cultureel centrum van Ramakrishna Mission | Wikipedia + belurmath.org officieel | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-VK-002 | Belur Math | Belur, Howrah-district, West-Bengal | 1 | hoofdkwartier Ramakrishna Math/Mission, door hemzelf gesticht 1899 | belurmath.org officieel | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-VK-003 | Baranagar Math | Baranagar, West-Bengal | 2 | eerste klooster na Ramakrishna's overlijden, 1886 | Wikipedia (Alambazar Math-context) | person_event: JA; physical_identity: DEELS (exact adres niet apart bevestigd in deze pass); exact_sublocation: NEE |
| ATL-VK-004 | Khetri House/Khetri | Khetri, Rajasthan | 1 | ontmoette gastheer/patroon Raja Ajit Singh (Abu, 04-06-1891), verbleef in Khetri 07-08 t/m 27-10-1891; kreeg hier de naam "Vivekananda" | khetri.rkmm.org officieel + Wikipedia (Ajit Singh of Khetri) | person_event: JA; physical_identity: JA; exact_sublocation: DEELS |
| ATL-VK-005 | Rajputana-rondreis (Mount Abu, Alwar, Jaipur, Ajmer, e.a.) | Rajasthan | 2/3 (gebundeld) | parivrajaka-zwerftocht 1891, meerdere vorstelijke gastheren | onafhankelijke biografiebronnen | person_event: JA (algemeen); physical_identity: DEELS per losse stad; exact_sublocation: NEE — bewust niet uitgesplitst tot losse kandidaten |
| ATL-VK-006 | Vivekananda-rots (Shripada Parai) | Kanyakumari, Tamil Nadu | 1 | driedaagse meditatie 24-26-12-1892, vlak vóór vertrek naar Chicago; nu Rock Memorial | incredibleindia.gov.in officieel + Tamil Nadu-toerisme | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-VK-007 | Advaita Ashrama, Mayavati | Champawat-district (bij Lohaghat), Uttarakhand | 1 | door hem gesticht 19-03-1899, via discipelen James/Charlotte Sevier | advaitaashrama.org officieel + Wikipedia | person_event: JA; physical_identity: JA; exact_sublocation: JA |
| ATL-VK-008 | Landingsplaats Kundukal, Rameswaram-eiland (route Colombo-Pamban) | Rameswaram, Tamil Nadu | 1 | terugkeer uit het Westen, 26-01-1897, beroemde toespraak | onafhankelijke bronnen + Wikisource "Lectures from Colombo to Almora" | person_event: JA; physical_identity: DEELS (eiland/plek bevestigd, geen apart GPS-punt); exact_sublocation: NEE |
| ATL-VK-009 | Almora | Almora-district, Uttarakhand | 2 | lezingenreeks tijdens de terugkeertour, 1897 (titelgevend aan "Lectures from Colombo to Almora") | Wikisource primaire bron | person_event: JA; physical_identity: DEELS (stad, geen exacte lezingslocatie); exact_sublocation: NEE |

**Bewust niet apart geteld**: Dakshineswar (eerste ontmoeting met Ramakrishna) — dit wordt in de
eigen Ramakrishna-sweep (persoon 8/9) als primair punt behandeld, geen dubbeltelling hier.

### Fase C — vergelijking met repo

- **ATL-VK-007 (Mayavati Advaita Ashrama) = FOUND_AND_ALREADY_KNOWN als tijdelijke kandidaat.**
  Staat al in `RECONCILIATION.md` als `KB2-038` uit INDIA's blinde Kumaon Sweep B, nog geen
  permanent nummer. Dit is een sterke `PERSON_LINK_UPGRADE`: bevestigt Vivekananda zelf als
  stichter, versterkt de zaak voor permanente toekenning bij een volgende Kumaon-vervolgstap.
- **ATL-VK-009 (Almora) = mogelijke `REGION_MISS`-check voor Kumaon** — geen exacte match
  aangetroffen in de bestaande Kumaon-kandidatenset onder deze specifieke naam/reden (lezingenreeks
  1897); vastgelegd als aandachtspunt voor een toekomstige Kumaon-vervolgronde, geen nieuw hard punt
  in deze taak (buiten scope van Fase 2 om zelf Kumaon-kandidaten aan te vullen).
- **ATL-VK-001, 002, 004, 006, 008 = allemaal FOUND_BUT_MISSING_FROM_REPO** (grep op "Belur",
  "Khetri", "Kanyakumari", "Rameswaram", "Baranagar" leverde niets op in de bestaande candidate-sets)
  — vijf sterke, onafhankelijke TIER 1-punten in vijf verschillende staten (West-Bengal, Rajasthan,
  Tamil Nadu ×2). Elk te zwak als los cluster om nu al `NEW_REGION_SIGNAL` te claimen (telkens één
  enkel, zij het zeer sterk, punt), maar samen bevestigen ze dat Vivekananda de breedst verspreide
  Top-11-persoon tot nu toe is.
- **ATL-VK-003 (Baranagar) en ATL-VK-005 (Rajputana-bundel) en ATL-VK-008 (Rameswaram)**: te vaag
  qua exacte sublocatie voor harde kandidaatstatus in deze pass; vastgelegd als context/mogelijke
  toekomstige verdieping.

### Saturatie-beoordeling tegen de 6 TASK-punten

1. Officiële/lineage + primaire teksten (incl. Vivekananda's eigen lezingenbundel): **JA**.
2. Grote levensfasen/reizen afgedekt: **JA** — geboorte, Ramakrishna-periode (verwezen naar
   Ramakrishna-sweep), Baranagar Math, parivrajaka-zwerftocht, Chicago-vertrek (Kanyakumari),
   terugkeer 1897, Belur Math + Mayavati-stichtingen 1899.
3. Alternatieve spellingen: **JA** — geboortenaam "Narendranath Datta" meegenomen.
4. Host-/landgoedketens teruggevolgd: **JA** — Raja Ajit Singh van Khetri als sterkste voorbeeld
   (gaf zelfs zijn naam), overige Rajputana-vorsten als gebundelde context.
5. Expliciet "op bezoek bij anderen": **JA** — vrijwel de hele parivrajaka-periode is per definitie
   "op bezoek bij anderen"; Khetri is het sterkste individuele voorbeeld.
6. Negatieve/onzekere claims: **JA** — Baranagar-adres, Rajputana-substops en Rameswaram-sublocatie
   expliciet als onvoldoende precies vastgelegd, niet als hard punt gepresenteerd.

**`PERSON_SWEEP_SATURATED: JA`**, met de kalibratie dat de brede parivrajaka-periode bewust
gebundeld is behandeld (methodologische keuze tegen kunstmatige verdichting), niet omdat er een
zoekgat was.

---
Dit bestand is de kortste, altijd-actuele bron van waarheid voor Fase 2 van deze taak (poort O.1).
Wordt na iedere persoon aangevuld en opnieuw gecommit.

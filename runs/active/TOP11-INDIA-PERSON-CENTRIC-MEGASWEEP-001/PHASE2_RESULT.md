# PHASE2_RESULT — Top-11 person-centric megasweep, overige 9 personen

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
trigger: CCI_TASK 081 (AUTHORIZED_BY_INDIA, METHOD_V1.md)
uitgevoerd_door: CCI
gestart_op: 2026-08-16
status: IN_UITVOERING — persoon 2/9 gereed
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
Dit bestand is de kortste, altijd-actuele bron van waarheid voor Fase 2 van deze taak (poort O.1).
Wordt na iedere persoon aangevuld en opnieuw gecommit.

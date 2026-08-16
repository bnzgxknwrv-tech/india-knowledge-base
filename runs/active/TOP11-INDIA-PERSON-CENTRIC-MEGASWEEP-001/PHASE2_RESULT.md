# PHASE2_RESULT — Top-11 person-centric megasweep, overige 9 personen

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
trigger: CCI_TASK 081 (AUTHORIZED_BY_INDIA, METHOD_V1.md)
uitgevoerd_door: CCI
gestart_op: 2026-08-16
status: IN_UITVOERING — persoon 1/9 gereed
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
Dit bestand is de kortste, altijd-actuele bron van waarheid voor Fase 2 van deze taak (poort O.1).
Wordt na iedere persoon aangevuld en opnieuw gecommit.

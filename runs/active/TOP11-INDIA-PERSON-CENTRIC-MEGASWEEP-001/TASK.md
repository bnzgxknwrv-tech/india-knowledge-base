# TASK — TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001

```
task_id: TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
issued_by: INDIA
issued_at: 2026-08-15
mode: INVERSE_PERSON_CENTRIC_MEGASWEEP
scope: heel India, geen regiobegrenzing
```

## Waarom deze taak bestaat

De regionale Kumaon-dubbele sweep miste twee legacy-A-locaties, waaronder Bodh Ashram, ondanks directe banden met Top-11-personen. Regionale zoekrichting alleen is dus onvoldoende als detector.

Deze taak draait de zoekrichting om:

**niet:** regio → welke Top-11-links zitten hier?

**maar:** persoon → op welke verifieerbare fysieke plekken in India is deze persoon ooit aantoonbaar geweest / verbleven / actief geweest / direct historisch verbonden?

Doel: een landelijke, persoon-gecentreerde fysieke atlas die latere regioweergaven kan voeden en regionale misses zichtbaar maakt.

## Top-11 — exact en volledig, één voor één

1. Paramahansa Yogananda
2. Mahavatar Babaji
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Ram Dass
6. Neem Karoli Baba
7. Anandamayi Ma
8. Ramakrishna
9. Ramana Maharshi
10. Hariharananda
11. Vivekananda

## Harde hoofdregel

Voor ELKE persoon afzonderlijk heel India doorzoeken zonder regionale scope. Niet stoppen na bekende hoofdplaatsen.

Zoek systematisch naar elk verifieerbaar fysiek touchpoint dat bronmatig aan de persoon gekoppeld is, waaronder minimaal:

- geboorteplek;
- woonhuis / verblijf / kamer / landgoed / hut / grot;
- ashram / math / klooster / tempel / kerk / moskee / gurdwara / heilige plek;
- samadhi / crematie / graf / reliekplek;
- initiatie / ontmoeting / meditatie / retraite / sadhana;
- onderwijs / lezing / satsang / ceremonie / darshan;
- bezoek aan iemand anders zijn ashram/huis/landgoed;
- gedocumenteerde reis- of verblijfslocatie;
- ziekenhuis / hotel / station / bestuursgebouw / school / club / zaal ALLEEN wanneer daar een betekenisvolle, gedocumenteerde gebeurtenis plaatsvond; gewone transit niet als reis-kandidaat, wel desgewenst als laag-prioriteits-touchpoint;
- huidige instelling alleen wanneer fysieke historische/persoonlijke link duidelijk wordt onderscheiden van latere institutionele eerbetoon.

## Granulariteit

Doel is maximale recall zonder kunstmatig duizenden irrelevante punten te maken.

Gebruik drie niveaus:

### TIER 1 — concrete choice-relevant physical site
Exact of redelijk identificeerbaar gebouw/terrein/grot/tempel/ashram/huis/samadhi/etc. met directe historische/persoonlijke link.

### TIER 2 — direct event place, exact subadres nog onbekend
Bijvoorbeeld stad/dorp/berg/landgoedzone waar een directe gebeurtenis bewezen is maar exacte fysieke sublocatie nog niet.

### TIER 3 — documented transit/context only
Alleen bewaren als bewijs dat de persoon er werkelijk was, maar NIET automatisch kandidaat voor Marks reis.

TIER 3 mag nooit TIER 1 verdringen of de kandidatenlijst vervuilen.

## Brondiscipline

- Open daadwerkelijke brontekst voor iedere choice-relevante hoofdclaim; geen snippet-only bevestiging.
- Primaire bron of officiële organisatie waar beschikbaar.
- Betrouwbare secundaire bron alleen waar primaire bron redelijkerwijs ontbreekt.
- Per plek expliciet scheiden:
  - `person_event_verified`
  - `physical_identity_verified`
  - `exact_sublocation_verified`
- Traditieclaim / devotionele identificatie expliciet als zodanig labelen.
- Geen claim van persoonlijk bezoek afleiden uit alleen een latere instelling die iemands naam draagt.

## Blindheid / vergelijking

### Fase A — landelijke discovery per persoon
Tijdens discovery NIET de bestaande regionale kandidaatsets gebruiken als checklist of zoekbasis. Ze mogen de zoektermen niet sturen.

### Fase B — freeze
Bevries per persoon de landelijke touchpointlijst met bronverwijzingen en negatieve/onjuiste claims.

### Fase C — vergelijk met huidige repo
Pas daarna vergelijken met alle bestaande India-locaties, legacy-runs en Mark-besluiten.

Maak dan minimaal:

- `FOUND_AND_ALREADY_KNOWN`
- `FOUND_BUT_MISSING_FROM_REPO`
- `REPO_ONLY_NOT_REFOUND`
- `DUPLICATE_OR_SAME_PHYSICAL_SITE`
- `PERSON_LINK_UPGRADE` — bestaande plek blijkt aan meer Top-11-personen gekoppeld;
- `REGION_MISS` — plek lag in een reeds gesweepte regio maar werd daar niet gevonden;
- `NEW_REGION_SIGNAL` — cluster van belangrijke touchpoints in een nog niet onderzochte regio.

## Belangrijk: bestaande Mark-besluiten

- Nooit stil wijzigen.
- Bestaande A/B/C blijft beschermd.
- Nieuwe persoon-link kan een bestaande plek inhoudelijk zwaarder maken maar niet automatisch Marks keuze wijzigen.
- Echte nieuwe cruciale informatie bij een oude C/B => `MARK_DECISION_CONFLICT`, niet zelf herclassificeren.

## Outputvorm

Maak één landelijke machine-leesbare tabel/JSONL plus per persoon een compact menselijk rapport.

Per fysieke plek minimaal:

- tijdelijke atlas-ID;
- persoon;
- naam fysieke plek;
- plaats/district/staat;
- tier 1/2/3;
- type gebeurtenis/link;
- datum/periode indien bekend;
- bron(nen);
- bewijssterkte;
- exacte locatie-status;
- huidige bezoekersrelevantie indien duidelijk;
- eventuele match met bestaande repo-ID;
- opmerkingen/claimgrenzen.

## Saturatie-eis

Per persoon pas `PERSON_SWEEP_SATURATED` wanneer:

1. minimaal officiële/lineage-bronnen, primaire teksten/biografieën en gerichte plaats-/event-searches zijn doorlopen;
2. bekende levensfasen en grote reizen zijn afgedekt;
3. alternatieve spellingen/namen zijn geprobeerd;
4. relevante secundaire verwijzingen naar huizen/ashrams/hosts/landgoederen zijn teruggevolgd naar de fysieke plek;
5. er expliciet is gezocht naar locaties waar de persoon op bezoek was bij ANDEREN — precies de categorie waarin Bodh Ashram kan vallen;
6. negatieve/onzekere claims zijn vastgelegd.

## Uitvoeringsvolgorde

Werk één persoon tegelijk volledig af en freeze die persoon vóór de volgende.

Aanbevolen volgorde op missierisico:
1. Mahavatar Babaji
2. Lahiri Mahasaya
3. Paramahansa Yogananda
4. Neem Karoli Baba
5. Ram Dass
6. Anandamayi Ma
7. Sri Yukteswar
8. Hariharananda
9. Vivekananda
10. Ramakrishna
11. Ramana Maharshi

De vaste Top-11-rangorde zelf verandert hierdoor NIET; dit is alleen onderzoeksvolgorde.

## Wat deze taak NIET doet

- geen routeplanning;
- geen hotelkeuze;
- geen PDF;
- geen A/B/C voorspellen namens Mark;
- geen regiokandidaten schrappen;
- regionale sweeps niet afschaffen.

## Nieuwe architectuur na deze taak

De persoon-atlas wordt een **orthogonale detectorlaag** naast regionale sweeps:

1. REGIONAAL: regio → alles wat daar belangrijk is.
2. PERSOON-CENTRISCH: persoon → alle bewezen fysieke India-touchpoints.
3. AOAY: boek → alle bewezen fysieke AOAY-locaties.

Een keuze-ready regio is pas echt sterk wanneer regionale sweep + persoon-atlas + AOAY-laag tegen elkaar zijn gekruist.

## Eerste deliverable

Voer eerst een PILOT uit op:
- Anandamayi Ma
- Neem Karoli Baba

Reden: Bodh Ashram is precies een mogelijke dubbel-link die de regionale sweeps misten. De pilot moet aantonen of de omgekeerde zoekrichting Bodh Ashram/Turiya-achtige plekken structureel terugvindt.

Na pilot: rapporteer aantallen, gevonden misses, search-patterns die werkten/niet werkten en schatting van totale atlasgrootte voor alle 11. Stop daarna voor INDIA-QA vóór de overige 9 personen.
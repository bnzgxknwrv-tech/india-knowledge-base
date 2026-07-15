# BRAJ-COMPLETE-001 — volledige Braj-clustersweep

## Centrale onderzoeksvraag

Welke fysiek bestaande spirituele plaatsen in het volledige Braj-gebied zijn voor Marks pelgrimsreis beslisrelevant wanneer Vrindavan, Mathura, Govardhan, Gokul, Barsana en Nandgaon als één samenhangend cluster worden onderzocht?

## Geografische begrenzing

In scope:

- Vrindavan;
- Mathura;
- Govardhan en de Govardhan-parikramaomgeving;
- Gokul en Mahavan;
- Barsana;
- Nandgaon;
- direct aangrenzende Braj-plaatsen die aantoonbaar dezelfde spirituele clusterbeslissing of dagstructuur beïnvloeden.

Buiten scope:

- Agra en de Taj Mahal als zelfstandig toeristisch cluster;
- Delhi;
- Rajasthan buiten directe Braj-continuïteit;
- hotels, definitieve nachten, boekingen en totale reisroute;
- PARELS-laag uit DECISION-0011;
- ARUNACHALA- en KUMAON-uitvoering.

## Bestaande canonical plaatsen en formele statussen

Lees `knowledge/places/registry.jsonl`.

Formeel A door Mark:

- IND-PLACE-000001 — Katyayani Peeth / Keshav Ashram, Vrindavan;
- IND-PLACE-000002 — Neem Karoli Baba Ashram en samadhi, Vrindavan.

De overige bestaande Vrindavan/Govardhan-records hebben status U. BRONS kent geen nieuwe formele A/B/C toe en wijzigt bestaande statussen niet.

## Doel van deze run

1. Maak de Braj-kandidatenkaart inhoudelijk compleet genoeg voor een latere clusterbeslissing.
2. Voorkom dat Mathura-, Govardhan-, Gokul-, Barsana- of Nandgaon-plekken los worden beoordeeld zonder aangrenzende context.
3. Behoud de acht bestaande canonical Vrindavan/Govardhan-plaatsen en voorkom dubbelregistratie.
4. Vind nieuwe fysieke plaatsen buiten bestaande lijsten wanneer sterke devotionele, lineage-, traditie-, AOAY-, Krishna-, Radha-, Chaitanya-, Vallabha-, Nimbarka-, Gaudiya-, Ramanandi- of andere Braj-relaties daarvoor aanleiding geven.
5. Onderzoek per kandidaat wat devotees er werkelijk doen, of Mark respectvol kan deelnemen en hoe de plek actueel wordt ervaren.
6. Leg nabijheid en mogelijke mini- of dagclusters vast zonder definitieve route of hotelkeuze te maken.

## Verplichte detectoren

Minimaal controleren:

- Krishna- en Radha-lila-tradities met een specifieke fysieke plek;
- Chaitanya/Gaudiya Vaishnava-plaatsen;
- Vallabha/Pushtimarg, Nimbarka, Radha Vallabh, Radharani- en andere erkende Braj-lineages;
- bekende samadhi's, ashrams, tempels, kunds, sarovars, ghats, heuvels, bossen, grotten en parikrama-objecten;
- plaatsen uit of verbonden met *Autobiography of a Yogi*, Yogananda, Sri Yukteswar, Lahiri Mahasaya, Keshavanand en relevante Kriya-lineages;
- Neem Karoli Baba/Maharaj-ji en directe leerlingrelaties;
- levende festivals, aarti, kirtan, satsang, seva, darshan en parikrama;
- kleine maar inhoudelijk krachtige fysieke plekken buiten toeristische toplijsten;
- huidige instellingen die de devotionele praktijk dragen.

Een persoon, verhaal of traditie komt alleen als kandidaat binnen wanneer een specifieke fysieke plek betrouwbaar kan worden aangewezen.

## Verplichte onderzoekslaag per kandidaat

1. fysieke identiteit en exacte afbakening;
2. institutionele drager of eerlijk `NIET_VASTGESTELD`;
3. historische, lineage- en traditiebevestiging als afzonderlijke domeinen;
4. waarom devotees hierheen gaan;
5. wat mensen er daadwerkelijk doen;
6. deelname, gastvrijheid en etiquette voor een buitenlandse spirituele bezoeker;
7. sfeer, schoonheid, rust, chaos, commercie, onderhoud en actuele bezoekerservaring;
8. minimaal tien functioneel verschillende representatieve beelden of een expliciet beeldtekort;
9. actuele bezoekbaarheid, toegang, beperkingen, beste dagdeel en praktische hercontrole;
10. nabijheid tot bestaande A-ankers en andere kandidaten;
11. mogelijke loop-, mini- en dagclusters;
12. relevante overlays en open conflicten.

## Bronregels

- Gebruik primaire, officiële, lineage-, academische en betrouwbare actuele bronnen passend bij het claimtype.
- Devotionele en traditiebevestiging wordt niet gedegradeerd omdat klassieke historische documentatie ontbreekt.
- Reviews en bezoekersbeelden mogen sfeer en praktische ervaring dragen, niet oude historische of bovennatuurlijke claims.
- Geen openingstijden, reistijden of toegangsregels gokken.
- Vluchtige praktische gegevens krijgen `checked_at` en `recheck_before`.
- Iedere claim verwijst naar unieke bron-ID's.

## Context- en overdrachtsregel

BRONS gebruikt `BRONS_MIN`.

De predecessorcontext is uitsluitend bedoeld om:

- bestaande acht plaatsen te herkennen;
- formele A-ankers te behouden;
- bekende open gaten niet als nieuwe vondst te presenteren;
- informatieverlies of kunstmatige duplicaten te voorkomen.

BRONS herhaalt niet automatisch de volledige oude Vrindavan-sweep. Bestaande plaatsen worden alleen uitgebreid waar Braj-clustercontext, devotionele laag, beelden, reviews of nabijheid dat vereist.

`handoff.yaml` bevat per laag `ACCEPTED`, `CORRECTED`, `OPEN` of `NOT_APPLICABLE`, plus risico en heropeninstructie.

## Vereiste artifacts BRONS

Minimaal:

- `report/INDEX.md`;
- scope- en tellingenrapport;
- kandidaatrapporten per geografisch deelcluster;
- buiten-lijst- en detectorrapport;
- cluster- en nabijheidsrapport;
- onzekerheden/conflicten/duplicatenrapport;
- `claims.jsonl`;
- `sources/registry.jsonl`;
- `sources/rejected.jsonl`;
- `images.jsonl`;
- `experience_reviews.jsonl`;
- `proximity.jsonl`;
- `place_candidates.jsonl` met canonical of tijdelijke run-ID;
- `audit.md`;
- `handoff.yaml` met layer statuses;
- `COMPLETED`.

## Clustercompleetheid

BRONS is breed genoeg wanneer:

- alle zes kerngebieden aantoonbaar zijn onderzocht;
- bestaande acht plaatsen correct zijn herkend;
- verplichte detectoren per gebied zichtbaar zijn afgelopen;
- nieuwe kandidaten niet uitsluitend uit toeristische toplijsten komen;
- iedere opgenomen kandidaat een specifieke fysieke identiteit heeft;
- negatieve zoekresultaten en niet-opgeloste aliasconflicten zichtbaar zijn;
- devotie, deelname, ervaring, beelden en nabijheid niet zijn overgeslagen;
- PARELS niet is geactiveerd.

## Harde verboden

- Geen formele A/B/C-status toekennen of wijzigen.
- Geen volledige reisroute, hotelkeuze, nachtenplanning of boekingsadvies.
- Geen PARELS-onderzoek.
- Geen ARUNACHALA- of KUMAON-run starten.
- Geen voltooide Vrindavan-artifacts wijzigen.
- Geen protocol-, methodologie- of rolwijziging tijdens de onderzoeksfase.
- Geen kandidaat opnemen zonder aanwijsbare fysieke plaats.

END_OF_ARTIFACT
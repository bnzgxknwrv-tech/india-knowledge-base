# TASK — TOP11-INDIAGEEL-BLIND-SWEEP-001

```
task_id: TOP11-INDIAGEEL-BLIND-SWEEP-001
owner: INDIA GEEL
issued_by: INDIA8
issued_at: 2026-08-19
mode: PRE-COMPARE BLIND
state: READY_FOR_INDIAGEEL
```

## Doel
Maak twee volledig onafhankelijke landelijke PRE-COMPARE freezes, vanaf nul, in deze vaste volgorde:

1. Ramana Maharshi
2. Ramakrishna

Onderzoek heel India. Geen reisselectie of regionale beperking.

## HARD BLINDNESS
Voor beide personen geldt: vóórdat de eigen freeze duurzaam is gecommit, mag INDIA GEEL GEEN inhoud lezen uit bestanden/branches/PR-comments die reeds gevonden locaties of conclusies van andere detectoren kunnen lekken.

PRE-COMPARE VERBODEN:
- PR #23 en alle comments;
- PR #24;
- `agent/chatgpt-top11-parallel-sweep`;
- `agent/indiarood-core-kriya-sweep`;
- alle CCI-persoonsfreezes, reconciliaties en resultaatbestanden;
- bestaande Top-11-atlassen, METHOD_V1/PHASE2-resultaten en kandidatenlijsten;
- AOAY-atlassen voor zover die Ramana/Ramakrishna-locaties kunnen zaaien;
- regionale/clusterbestanden die persoonslocaties kunnen lekken;
- externe AI-unions of eerdere onderzoeksoutputs voor deze personen.

PRE-COMPARE TOEGESTAAN:
- uitsluitend dit `TASK.md`;
- `STATUS.md` in dezelfde map;
- openbare externe bronnen op internet die INDIA GEEL zelfstandig vindt.

Geen andere repo-inhoud nodig of toegestaan om de sweep uit te voeren.

## Methode — verplicht source-first/corpus-first
Per persoon:

1. Inventariseer primaire/semi-primaire corpusfamilies, biografieën, autobiografieën, dagboeken, brieven, herinneringen, officiële ashram/orde/lineage-bronnen en chronologieën.
2. Extraheer eerst occurrence-level fysieke locaties uit die corpora.
3. Bouw daarna host/netwerkgraaf: familie, discipelen, gastheren, huizen, landgoederen, scholen, tempels, ashrams, stations, hotels, ziekenhuizen, routes, retreats, bijeenkomsten en andere personen met wie de persoon fysiek samen was.
4. Doe daarna brede webdiscovery, inclusief historische spellingen, alternatieve namen, meertalige bronnen en digitale bibliotheken waar legaal toegankelijk.
5. Voer adversarial miss-detection rondes uit: zoek expliciet naar kleine/private/transit/room-level locaties die een beroemde-plaatsenlijst zou missen.
6. Stop alleen na herhaalde discovery-rondes zonder betekenisvolle nieuwe localiseerbare India-locaties, of met expliciet benoemde bron/archive blockers.

## Locatieregels
Per record minimaal:
- naam / omschrijving fysieke plek;
- plaats + staat;
- type;
- gebeurtenis/periode;
- `PERSONALLY_PRESENT: JA/NEE/ONZEKER`;
- `PHYSICAL_IDENTITY: EXACT/DEELS/ALLEEN_PLAATS/ONBEKEND`;
- bron + URL/bibliografische identificatie;
- precieze vindplaats/passagelocator;
- host/gastheer indien relevant;
- twijfel/conflict/historische-continuïteitsnotitie.

Niet registreren als persoonlijke locatie wanneer de tekst slechts context, een andere persoon, algemene geschiedenis of institutionele associatie noemt.

## Freeze-output
### Persoon 1 — Ramana Maharshi
Schrijf na afronding onmiddellijk:
`runs/active/TOP11-INDIAGEEL-BLIND-SWEEP-001/RAMANA_MAHARSHI_INDIAGEEL_FREEZE.md`

Commit direct na deze persoon. Noteer volledige SHA in `STATUS.md`.

### Persoon 2 — Ramakrishna
Pas nadat Ramana duurzaam is gecommit, start Ramakrishna.
Schrijf:
`runs/active/TOP11-INDIAGEEL-BLIND-SWEEP-001/RAMAKRISHNA_INDIAGEEL_FREEZE.md`

Commit direct na afronding. Noteer volledige SHA in `STATUS.md`.

## Verplichte freeze-header per persoon
- `PERSON`
- `FREEZE_TIMESTAMP`
- `BLINDNESS_CONFIRMED: JA`
- `CORPORA_SEARCHED`
- `SOURCE_ACCESS_BLOCKERS`
- `HOSTGRAPH_SEARCHED`
- `DISCOVERY_SEARCH_FAMILIES`
- genormaliseerde recordcount
- `CONFLICTS`
- `UNRESOLVED_LEADS`
- `SATURATION_ATTEMPTS`
- `PERSON_SWEEP_SATURATED: JA/NEE` met motivatie

Eerlijke `NEE` is beter dan schijnzekerheid.

## HARD STOP / verboden vervolg
Na beide freezes:
- GEEN vergelijking met CCI/ChatGPT/IndiaROOD;
- GEEN PR #23 lezen;
- GEEN reconciliatie;
- GEEN merge;
- GEEN cluster/heatmap/regiosweep;
- GEEN A/B/C;
- GEEN permanente IDs;
- GEEN PDF;
- GEEN route.

Werk uitsluitend op een eigen India-GEEL branch. Als nog geen branch bestaat, maak een nieuwe branch vanaf de huidige werkbranch met naam `agent/indiageel-ramana-ramakrishna-sweep`. Schrijf de freeze-output alleen op die eigen branch, zodat de blindheid en provenance duurzaam gescheiden blijven.

## Eindmelding
Na beide commits rapporteer uitsluitend aan Mark:
- beide personen klaar/niet klaar;
- beide freeze-SHA's;
- beide paden;
- recordcounts;
- saturationstatus;
- eventuele blockers;
- bevestiging dat verboden projectresultaten/PR #23 niet zijn gelezen.

Daarna STOP.
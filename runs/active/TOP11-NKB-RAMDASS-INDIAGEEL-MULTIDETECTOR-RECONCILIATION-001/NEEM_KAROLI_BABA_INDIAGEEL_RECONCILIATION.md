# NEEM_KAROLI_BABA_INDIAGEEL_RECONCILIATION

```
task_id: TOP11-NKB-RAMDASS-INDIAGEEL-MULTIDETECTOR-RECONCILIATION-001
cci_task: CCI_TASK 095
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
basis_091: interne 21-record freeze + externe ChatGPT-sweep (113 records), reeds gereconcilieerd in
  CCI_TASK 091 (`TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/NEEM_KAROLI_BABA_RECONCILIATION.md`)
indiageel: agent/indiageel-ramana-ramakrishna-sweep, commit 4cd99f5e45266dd3de0ed487e8147fd93ca525d9,
  runs/active/TOP11-INDIAGEEL-NKB-BLIND-SWEEP-001/NEEM_KAROLI_BABA_INDIAGEEL_FREEZE.md, 46 records
  (NKB-IG-001 t/m 046) — commit geverifieerd als exacte, enige toevoegende commit voor dit bestand
  (`list_commits`/`get_commit`, 601 additions, geen andere wijzigingen).
```

## 0. Integriteitscheck

Commit `4cd99f5e45266dd3de0ed487e8147fd93ca525d9` rechtstreeks via de GitHub API gecontroleerd: dit
is de enige commit die dit bestand toevoegt (601 regels, geen latere wijzigingen), exact zoals
TASK.md opgeeft. Bestand rechtstreeks via de API opgehaald (niet via een ongeauthenticeerde proxy).

## 1. Structurele karakterisering

IndiaGEEL's NKB-freeze (46 records) is gebaseerd op een deels overlappende, deels aanvullende
bronbasis t.o.v. de externe ChatGPT-sweep uit 091: beide gebruiken *The Divine Reality* (Rajida) en
Dada Mukerjee's *By His Grace* als kernbronnen, maar IndiaGEEL citeert daarnaast direct
`nkbashram.org`-institutionele pagina's (Nibkarori-grot, Vrindavan-ashram) die de 091-externe-freeze
niet als aparte URL aanhaalde. IndiaGEEL is minder granulair dan de 091-externe-freeze (46 vs. 113
records) maar dekt een eigen, deels nieuw geografisch cluster: de volledige januari-1973
Zuid-India-reis (Sindhi Dharmsala Madras, Vaishnavi Devi-tempel, Veerapuram) die in de 091-externe-
freeze slechts generiek als "Dwarka/Rameshwaram/Puri/Dakshineshwar" werd samengevat zonder de
Chennai/Tamil Nadu-tak.

## 2. Directe bronverificatie uitgevoerd deze taak

| claim | route | resultaat |
|---|---|---|
| IndiaGEEL NKB-IG-039 (Hanuman Setu/Sankat Mochan-tempel, Lucknow — Baba stampte zelf de grond, consecratie 26 jan. 1967) | WebSearch, meerdere onafhankelijke bronnen incl. nkbashram.org/maharajji.love | **BEVESTIGD**: ashram ingewijd 26 januari 1967, exacte datum-match. Dit is een **upgrade** van de interne 091-status (record 16, `ONZEKER`) naar bevestigde persoonlijke aanwezigheid — extern (ext #97) had dit al als los record maar zonder Tier-1-bevestiging; IndiaGEEL levert de eerste concreet geverifieerde consecratiedatum. Nieuw randdetail gevonden (niet bij IndiaGEEL of extern): Baba zou al in de jaren '40 een eerdere ashram bij dezelfde rivier hebben gebouwd, die door een overstroming in de jaren '60 verzwolgen werd — apart genoteerd als lead, niet als apart record gepromoveerd binnen dit taakbudget. |
| IndiaGEEL NKB-IG-046 (Veerapuram, braakliggend terrein ~32 km van Chennai, jan. 1973 — Baba stapte uit de taxi en liep rond op het latere tempelterrein) | WebSearch, o.a. Instagram-officiële ashrampagina en devotieblog | **VOLLEDIG BEVESTIGD**, woordelijk overeenkomend detail voor detail (taxi's schoten Vaishnavi-Devi-tempel voorbij, Baba stopte op braakliggend terrein, tempel later — 1984 — op exact dezelfde plek gebouwd door Hukum Chand). Dit hele Zuid-India/Chennai-cluster (NKB-IG-044/045/046) is **IndiaGEEL-only** t.o.v. zowel intern als de 091-externe-freeze — een genuine nieuwe regionale tak. |
| Doodsvolgorde-conflict uit CCI_TASK 091 (Mathura-tussenstop wel/niet) — IndiaGEEL's eigen, niet-gepromoveerde lead noemt expliciet "got off train, sat on station steps by outdoor latrine, became acutely ill, then transferred by taxi to Vrindavan" | WebSearch naar onafhankelijke secundaire samenvattingen van de laatste reis | **Substantiële, niet-Tier-1 corroboratie van de Mathura-versie**: meerdere onafhankelijke webbronnen (buiten IndiaGEEL en buiten de oorspronkelijke interne/externe 091-bronnen) beschrijven dezelfde route — nachttrein Agra→Kainchi, uitstappen te Mathura, convulsies, spoedvervoer naar Vrindavan-ziekenhuis. Dit conflicteert nog steeds met S15 (091's Tier-1-bron, die geen Mathura-stop noemt), maar drie onafhankelijke lagen (interne 091-freeze, externe 091-record #109-112, IndiaGEEL's eigen niet-gepromoveerde lead, plus deze taak's aanvullende websearch) wijzen nu in dezelfde richting. **Conflict blijft expliciet open** (S15 blijft een directe Tier-1-bron met een andere lezing), maar het gewicht van het bewijs verschuift merkbaar richting de Mathura-versie. Ziekenhuisnaam (Ramakrishna Mission Hospital, Vrindavan) blijft ongewijzigd drieweg bevestigd. |

## 3. Matrix — samenvatting

| cluster | 091-basis (intern+extern) | IndiaGEEL | uitkomst |
|---|---|---|---|
| Akbarpur geboorte/familiehuis | intern #1, ext #1-3 | NKB-IG-001, NKB-IG-002 (Dak Bangalia — nieuw sub-record) | `MATCH_EXISTING`, drieweg; IndiaGEEL voegt Dak Bangalia (latere logeerplek in het dorp) toe, niet bij intern/extern |
| Gujarat vroege ashram/Vavania-Babania/lake/eerste Hanuman-murti | intern #3, ext #4-7 | NKB-IG-003 t/m NKB-IG-006 | `MATCH_EXISTING`, drieweg; spellingvariant Vavania/Babania genoteerd, geen feitelijk conflict |
| Neeb Karori-grot/tempel/station | intern #4, ext #8-12 | NKB-IG-007 t/m NKB-IG-009 | `MATCH_EXISTING`, drieweg |
| Farrukhabad/Fatehgarh Ganges-badplaats/Kilaghat | niet apart bij intern; ext noemt "Fatehgarh-kazerne" generiek | NKB-IG-010, NKB-IG-011 | `INDIAGEEL_MORE_SPECIFIC` t.o.v. extern's generieke vermelding |
| Hanumangarh/Bhumiadhar/Kainchi-cluster | intern #5-6/#19, ext #31-49 | NKB-IG-012 t/m NKB-IG-019 | `MATCH_EXISTING`, drieweg-kern; extern blijft granulairder (9 Kainchi-sublocaties vs. IndiaGEEL's 4); IndiaGEEL voegt Gethia-sanatorium en Ramsay Hospital Nainital (1972 ECG) toe, niet bij intern/extern |
| Kakrighat | intern #7, ext #50-51 | NKB-IG-022 | `MATCH_EXISTING`, drieweg; IndiaGEEL bevestigt zelfstandig dezelfde ONZEKER-fysieke-aanwezigheidskwalificatie als 091 §2.2 al noteerde |
| Allahabad-cluster (oud huis, 4 Church Lane, Prabhudatt Brahmachari-ashram, overstroomde tempel, station) | ext generiek "Allahabad-episodes" | NKB-IG-023 t/m NKB-IG-028 | `INDIAGEEL_MORE_SPECIFIC` — IndiaGEEL benoemt exact wat extern alleen generiek clusterde (incl. Prabhudatt Brahmachari-ashram, niet bij extern genoemd) |
| Chitrakut/Vindhyachal-pelgrimage | ext generiek in "Varanasi/Vindhyachal/Chitrakut" | NKB-IG-029 t/m NKB-IG-033 | `MATCH_EXISTING`, IndiaGEEL granulairder |
| Kanpur-devoteehuizen + Panki-bilocatie | intern #9/#10, ext #89 (Tier-1 bevestigd in 091) | NKB-IG-034 t/m NKB-IG-036 | `MATCH_EXISTING`, **drieweg-bevestiging van dezelfde nuance**: alle drie detectoren behandelen Panki als ONZEKER/devotionele bilocatietraditie, geen enkele upgradet naar bewezen fysieke aanwezigheid — sterk methodologisch signaal |
| Bareilly (Dr Bhandari, Goel) | ext "Bareilly-netwerk" generiek | NKB-IG-037, NKB-IG-038 | `INDIAGEEL_MORE_SPECIFIC` — IndiaGEEL geeft zelfs een adres (165 Civil Lines, Station Rd) |
| **Hanuman Setu/Sankat Mochan, Lucknow** | intern #16 `ONZEKER`, ext #97 `ONZEKER` | **NKB-IG-039, JA/EXACT** | **`CONFLICT_RESOLVED_UPGRADE`** — Tier-1 bevestigd, zie §2 |
| Taradevi/Shimla | intern #17 `ONZEKER`, ext #100-101 (10 dagen) | NKB-IG-040 | `MATCH_EXISTING`, drieweg-consistent op "10 dagen"-detail |
| Vrindavan-ashram/Hathiwale Baba-hut | intern #8, ext #104-108 | NKB-IG-041, NKB-IG-042 | `MATCH_EXISTING`, drieweg |
| Badrinath sage-hut/koeschuur | ext generiek in pelgrimsroute | NKB-IG-043 | `INDIAGEEL_MORE_SPECIFIC` |
| **Zuid-India: Sindhi Dharmsala Madras, Vaishnavi Devi-tempel, Veerapuram** | niet bij intern; niet apart bij extern (alleen generieke Dwarka/Rameshwaram/Puri-vermelding, geen Chennai/Tamil Nadu-tak) | **NKB-IG-044, NKB-IG-045, NKB-IG-046** | **`INDIAGEEL_ONLY_CLAIM` — CONFIRMED Tier-1** (Veerapuram), zie §2. Een volledig nieuwe regionale tak t.o.v. beide andere lagen. |

## 4. Onopgeloste conflicten — expliciet bewaard

1. **Doodsvolgorde/Mathura-tussenstop** (uit CCI_TASK 091 §2.1): blijft open. Zie §2 hierboven voor
   de aanvullende, niet-doorslaggevende corroboratie via IndiaGEEL's eigen lead plus onafhankelijke
   websearch. S15 blijft de enige directe Tier-1-tegenbron.
2. **Panki-bilocatie** (uit 091): blijft drieweg `ONZEKER`, nu voor het eerst drievoudig onafhankelijk
   bevestigd als consistent methodologisch behandeld (geen enkele detector upgradet).
3. **Vavania/Babania-spelling**: geen feitelijk conflict, alleen een transliteratievariant; niet
   verder onderzocht binnen dit taakbudget.

## 5. Academische restgaten vs. travel-relevante blockers

- **Travel-relevant, nu gedicht**: Hanuman Setu Lucknow (upgrade naar bevestigd bezoek); Veerapuram/
  Chennai-cluster (volledig nieuw, bevestigd bezoekbaar gebied).
- **Travel-relevant, nog open**: exacte Mathura-stationsdetails van de laatste reis (relevant als
  Mark een "laatste-reis-pelgrimage" zou overwegen, maar geen locatie die los bezocht zou worden
  buiten Vrindavan/Kainchi zelf).
- **Academisch/niet travel-blokkerend**: geboortejaar-chronologie, exacte grot-continuïteit
  Neeb Karori (origineel ingestort, opvolgersite), exacte adressen van tientallen kleinere
  devoteehuizen in Kanpur/Bareilly/Agra — geen van deze verandert welke plaatsen fysiek te bezoeken
  zijn, alleen de historische precisie van elk huis.

## 6. Gate-update

| gate | 091-status | 095-status (na IndiaGEEL) |
|---|---|---|
| CORPUS_COVERAGE_GATE | DEELS | DEELS → verbeterd (IndiaGEEL's eigen institutionele bronnen + Zuid-India-tak toegevoegd) |
| HOSTGRAPH_GATE | DEELS | DEELS → licht verbeterd (Hukum Chand, Yogendra Prakash Goel-adres) |
| DISCOVERY_GATE | DEELS | DEELS → verbeterd |
| RECONCILIATION_GATE | DEELS (091) | **JA** voor de drieweg-vergelijking zelf |
| EXTERNAL_MODEL_DIVERSITY_GATE | N.V.T. (091 had maar 2 lagen) | **JA** — IndiaGEEL vond een volledig nieuwe, Tier-1-bevestigde regionale tak (Zuid-India) en leverde een Tier-1-upgrade voor een bestaand ONZEKER-record (Lucknow) |

`NEEM_KAROLI_BABA_SATURATED: NEE` — ongewijzigd eerlijk. *Miracle of Love* en *By His Grace*
(volledige editie) blijven grotendeels ontoegankelijk voor alle drie detectoren.

---
Geschreven door: CCI. Checkpoint 1/2 van CCI_TASK 095.

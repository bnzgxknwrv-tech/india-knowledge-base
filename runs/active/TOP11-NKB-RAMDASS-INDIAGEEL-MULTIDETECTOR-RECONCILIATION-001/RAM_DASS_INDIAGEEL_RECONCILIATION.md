# RAM_DASS_INDIAGEEL_RECONCILIATION

```
task_id: TOP11-NKB-RAMDASS-INDIAGEEL-MULTIDETECTOR-RECONCILIATION-001
cci_task: CCI_TASK 095
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
basis_091: interne 13+1-record freeze + externe ChatGPT-sweep (57 records), reeds gereconcilieerd in
  CCI_TASK 091 (`TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RAM_DASS_RECONCILIATION.md`)
indiageel: agent/indiageel-ramana-ramakrishna-sweep, commit e1f2e4b8bb56296e20bc0d3f6a3d2fbe9b7589cb,
  runs/active/TOP11-INDIAGEEL-RAMDASS-BLIND-SWEEP-001/RAM_DASS_INDIAGEEL_FREEZE.md, 55 records
  (RD-01 t/m RD-55) — commit geverifieerd als exacte, enige toevoegende commit voor dit bestand
  (`list_commits`/`get_commit`, 548 additions, geen andere wijzigingen).
```

## 0. Integriteitscheck

Commit `e1f2e4b8bb56296e20bc0d3f6a3d2fbe9b7589cb` rechtstreeks via de GitHub API gecontroleerd: dit
is de enige commit die dit bestand toevoegt (548 regels, geen latere wijzigingen), exact zoals
TASK.md opgeeft. Volledige externe 091-basis (`RAM_DASS_PRE_COMPARE_FREEZE.md`, 57 records) opnieuw
rechtstreeks van de externe branch opgehaald om een volledige driewegsvergelijking mogelijk te maken
(niet alleen de 091-samenvatting).

## 1. Structurele karakterisering

IndiaGEEL's Ram Dass-freeze (55 records) gebruikt een grotendeels andere primaire bron dan de
091-externe-freeze: **Being Ram Dass** (2021, met Rameshwar Das) als doorlopende autobiografische
tijdlijn, tegenover de 091-externe-freeze's primaire steun op **Be Here Now** en **Miracle of
Love**. Dit levert een genuine tweede, onafhankelijke autobiografische bron op — niet slechts een
andere lezing van dezelfde tekst. Het resultaat is een reeks **volledig nieuwe clusters** die de
091-externe-freeze expliciet als open/niet-toegevoegd had genoteerd, plus enkele die extern helemaal
niet vermeldde.

## 2. Directe bronverificatie uitgevoerd deze taak

| claim | route | resultaat |
|---|---|---|
| IndiaGEEL RD-05 t/m RD-09 (Dharamsala/McLeod Ganj-cluster: Dalai Lama-audiëntie, diens broers gastenverblijf, familie-liefdadigheidsbezoek, hoofdkwartier geïdentificeerd als "Swarg Ashram") | WebSearch naar onafhankelijke bevestiging van *Being Ram Dass* en het 1967-Dalai-Lama-bezoek | **Niet Tier-1 bevestigd binnen dit taakbudget** — *Being Ram Dass* is een reëel, gepubliceerd boek (2021, Rameshwar Das) met exact dezelfde 1967-overlandreis-tijdlijn (Padwa, Land Rover) die ook elders in deze en de 091-freeze wordt bevestigd, maar de specifieke Dharamsala-passage/"Swarg Ashram"-naam kon niet onafhankelijk worden teruggevonden via web search. **Zeer belangrijk**: de 091-externe-freeze noemde dit expliciet als negatieve bevinding #1 — "Dalai Lama-audiëntie: BH zegt dat Ram Dass de Dalai Lama ging zien, maar geeft geen locatie. Dharamsala/McLeod Ganj is niet zonder locatiebewijs toegevoegd." IndiaGEEL vult exact dit door 091 expliciet opengelaten gat, via een andere primaire bron dan BH. Status: `INDIAGEEL_ONLY_CLAIM — PLAUSIBLE` (boek bestaat en is thematisch consistent, specifieke passage niet apart Tier-1 herverifieerd). |
| IndiaGEEL RD-29 t/m RD-32 (Bombay-stadion Muktananda-welkomstrally okt. 1970, Ganeshpuri-ashram, Trivedi-huis) | WebSearch naar Ram Dass/Muktananda/Ganeshpuri-verband | **Tier-2 gecorroboreerd**: onafhankelijke bronnen bevestigen dat Ram Dass en Krishna Das met Muktananda reisden (incl. een specifiek verkeersongeval-verhaal dat in de bredere Neem-Karoli-Baba-devoteetraditie circuleert) en dat westerlingen vanaf eind 1970 naar Muktananda's Ganeshpuri-ashram (Shree Gurudev Ashram) trokken. Dit is een **volledig nieuwe cluster t.o.v. de 091-externe-freeze**, die Muktananda/Ganeshpuri nergens vermeldt voor Ram Dass. Status: `INDIAGEEL_ONLY_CLAIM — PLAUSIBLE`, sterk gecorroboreerd maar niet woordelijk Tier-1 bevestigd. |
| IndiaGEEL RD-20 (eerste Maharajji-ontmoeting expliciet gelokaliseerd bij de Bhumiadhar-tempel) vs. 091-extern record 8 ("eerste-ontmoetingsveld achter heuvel nabij kleine wegtempel", expliciet **niet** bij naam gelokaliseerd, `DEELS`) | Cross-check tegen de eigen NKB-IndiaGEEL-freeze (checkpoint 1/2 van deze taak) en tegen 091's eigen tekst | **Bevestigd via cross-detector consistentie**: IndiaGEEL's eigen NKB-freeze (checkpoint 1/2) bevat onafhankelijk dezelfde Bhumiadhar-identificatie voor Ram Dass' eerste ontmoeting met Maharajji. Dit lost een lead op die de 091-externe-freeze zelf openliet (zij vermeed bewust een plaatsnaam zonder bewijs). Status: `INDIAGEEL_MORE_SPECIFIC`, betrouwbaar geacht op basis van interne cross-detector-consistentie binnen dezelfde IndiaGEEL-sessie (NKB- en Ram-Dass-freeze werden apart bevroren maar komen onafhankelijk tot dezelfde naam). |

## 3. Matrix — samenvatting

| cluster | 091-basis (intern+extern) | IndiaGEEL | uitkomst |
|---|---|---|---|
| Srinagar/Dal Lake-houseboot "New Ruby" + shikara | niet bij intern/extern (extern begint route pas bij Amarnath) | RD-01, RD-02 | `INDIAGEEL_ONLY_CLAIM`, PLAUSIBLE (zelfde bron/tijdlijn als de rest van de reisroute die elders wel drieweg bevestigd is) |
| Amarnath Cave + basiskamp | intern #6(090), ext #1 | RD-03, RD-04 | `MATCH_EXISTING`, drieweg; basiskamp blijft ONBEKEND bij alle drie |
| **Dharamsala/McLeod Ganj: Dalai Lama-audiëntie, "Swarg Ashram", broers gastenverblijf** | expliciet **niet toegevoegd** door 091-extern (negatieve bevinding #1) | **RD-05 t/m RD-09** | **`INDIAGEEL_ONLY_CLAIM` — vult een expliciet 091-gat**, zie §2, `PLAUSIBLE` |
| Kurukshetra-doorreis | niet bij intern/extern | RD-10 | `INDIAGEEL_ONLY_CLAIM`, transit-only, laag travel-gewicht |
| Brits Consulaat + Tibet House, Delhi | niet bij intern/extern | RD-11, RD-12 | `INDIAGEEL_ONLY_CLAIM`, PLAUSIBLE (aansluitend bij het al bevestigde 1967-Delhi-verblijf) |
| Harish Johari-familiehuis, Bareilly | niet bij intern/extern | RD-13, RD-17 | `INDIAGEEL_ONLY_CLAIM`, nieuwe hostgraph-tak (Bareilly niet eerder gekoppeld aan Ram Dass zelf) |
| Varanasi-hotel bij Manikarnika + verbrandingsghats + Ganga-boot | intern/extern hadden alleen "Benares (alleen stad)" | RD-14, RD-15, RD-16 | `INDIAGEEL_MORE_SPECIFIC` t.o.v. 091's ALLEEN_PLAATS-niveau |
| Onbenoemde dharamshala's/Bhagavan Das-pelgrimage | ext #3-4 ("Baneshwar"/Konark, zelf al ONBEKEND) | RD-18 | `MATCH_EXISTING` op onzekerheidsniveau — beide detectoren laten dit terecht ongespecificeerd |
| Onbenoemd Hanuman-devoteehuis vóór eerste ontmoeting | niet bij intern/extern | RD-19 | `INDIAGEEL_ONLY_CLAIM`, ONBEKEND, laag travel-gewicht |
| **Bhumiadhar (eerste-ontmoetingstempel, bij naam)** | intern #10(090), ext #8 (`DEELS`, geen naam) | **RD-20** | **`INDIAGEEL_MORE_SPECIFIC` — lost 091-lead op**, zie §2 |
| K.K. Sah-huis, Kainchi Ashram, oude kamer, rivier-badplaats, vuurceremonie, koude hut, 2004-kamer | intern #2-5(090)/#2/#3(nieuw), ext #7-14, #29 | RD-21 t/m RD-23 | `MATCH_EXISTING`, drieweg-kern |
| Hanuman Garh-tempel | intern (090), ext #30 | RD-24 | `MATCH_EXISTING`, drieweg |
| Connaught Place/AmEx/restaurant/klooster/Health Dept | intern #9(090), ext #17-21 | RD-25 t/m RD-28 | `MATCH_EXISTING`, drieweg; IndiaGEEL voegt "koekjes-in-steegje"-detail toe |
| **Bombay-stadion + Ganeshpuri/Muktananda-ashram + Trivedi-huis** | **niet bij intern/extern** | **RD-29 t/m RD-32** | **`INDIAGEEL_ONLY_CLAIM` — volledig nieuwe cluster**, zie §2, `PLAUSIBLE` |
| Bodh Gaya: Burmese Vihara, Bodhi-boom, Tibetaans klooster (Khunu Lama) | intern (090), ext #35 (alleen Vihara) | RD-33 t/m RD-35 | `MATCH_EXISTING` op Vihara; `INDIAGEEL_MORE_GRANULAR` op Bodhi-boom en Tibetaans klooster |
| Reclining Hanuman-tempel bij Sangam, Allahabad | niet bij intern/extern | RD-36 | `INDIAGEEL_ONLY_CLAIM`, PLAUSIBLE, IndiaGEEL zelf voorzichtig (geen naam in bron, herkenning als "Lete/Bade Hanuman Ji" niet hard gemaakt) |
| Dada Mukerjee-huis, 4 Church Lane | intern (090), ext #36 | RD-37 | `MATCH_EXISTING`, drieweg |
| AmEx-kantoor Delhi (1971) | ext #18 (1967-vermelding) | RD-38 | `MATCH_EXISTING`, ander bezoekjaar, geen conflict |
| **Kumar Gallery, Delhi — lezing, aanval door Hog Farm-lid** | niet bij intern/extern | **RD-39** | `INDIAGEEL_ONLY_CLAIM`, PLAUSIBLE, niet apart geverifieerd dit taakbudget |
| Onbenoemde Zuid-Indiase tempelstad-kamer (Muktananda-yatra) | ext eigen negatieve bevinding #2 (Zuid-Indiase Shiva-route, bewust geen namen) | RD-40 | `MATCH_EXISTING` op onzekerheidsniveau — beide detectoren laten dit terecht ongespecificeerd |
| Sathya Sai Baba-ashram, Whitefield | intern (090), ext #44-45 | RD-41 | `MATCH_EXISTING`, drieweg |
| Surat-meditatiegrotten | ext #52 | RD-42 | `MATCH_EXISTING`, drieweg |
| Vrindavan-ashram/kantoor/binnenplaats | intern (090), ext #48-51 | RD-43 t/m RD-45 | `MATCH_EXISTING`, drieweg |
| Kausani-huurhuis + Gandhi/Anasakti Ashram | intern #4, ext #32-33 | RD-46, RD-47 | `MATCH_EXISTING`, drieweg |
| Hotel Evelyn (Nainital) | intern #3, ext #25-27 | RD-48 | `MATCH_EXISTING`, drieweg |
| Haldwani/Ghaziabad-monteur | niet bij intern; ext niet expliciet | RD-49, RD-50 | `INDIAGEEL_ONLY_CLAIM`, beide zelf `ONZEKER` gehouden — methodologisch consistent met 091's eigen voorzichtigheid bij vergelijkbare gevallen |
| Jaipuria Bhawan, Bankey Bihari-tempel, Yamuna-oever | niet apart bij intern/extern (alleen generiek "Vrindavan-ashram") | RD-51 t/m RD-53 | `INDIAGEEL_ONLY_CLAIM`, PLAUSIBLE — specifieke, goed gedocumenteerde Vrindavan-pelgrimsplekken |
| **Anandamayi Ma-ashram Vrindavan + Kankhal/Haridwar** | **niet bij intern/extern** | **RD-54, RD-55** | `INDIAGEEL_ONLY_CLAIM`, PLAUSIBLE — niet apart Tier-1 geverifieerd dit taakbudget, maar thematisch sterk aannemelijk gegeven Maharajji's eigen bevestigde band met Anandamayi Ma (zie de aparte Anandamayi Ma-driewegreconciliatie uit CCI_TASK 084) |

## 4. Fout gevonden in 091 — bevestigd, niet opnieuw ter discussie

De 091-reconciliatie verwierp al de externe "Puri-strand"-claim (SD-citaat niet teruggevonden in de
eigen aangehaalde bron) als `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`. IndiaGEEL bevat **geen** Puri-
strand-record — stilzwijgend consistent met die eerdere afwijzing, geen nieuwe tegenspraak.

## 5. Academische restgaten vs. travel-relevante blockers

- **Travel-relevant, potentieel geopend door IndiaGEEL**: Dharamsala/McLeod Ganj (Dalai Lama-
  audiëntiegebied); Ganeshpuri/Muktananda-ashram; Anandamayi Ma-ashrams Vrindavan en Kankhal. Dit
  zijn alle drie *nieuwe bezoekbare regio's/complexen* t.o.v. de 091-basis, geen van alle drie hard
  Tier-1 bevestigd — als Mark deze ooit als bestemming zou overwegen, verdient elk een aparte
  gerichte verificatiepas vóór opname in een reisgids.
- **Academisch/niet travel-blokkerend**: exacte kamer-/gebouwnummers in Kainchi, Hotel Evelyn en
  Vrindavan-ashram; de Haldwani/Ghaziabad-monteursclaims (ONZEKER of Ram Dass zelf aanwezig was);
  de onbenoemde Zuid-Indiase tempelstad-kamer.

## 6. Gate-update

| gate | 091-status | 095-status (na IndiaGEEL) |
|---|---|---|
| CORPUS_COVERAGE_GATE | DEELS | DEELS → verbeterd (een volledig tweede autobiografische bron, *Being Ram Dass*, toegevoegd naast BH/MOL) |
| HOSTGRAPH_GATE | DEELS | DEELS → verbeterd (Harish Johari, Muktananda/Trivedi-netwerk, Anandamayi Ma-kring toegevoegd) |
| DISCOVERY_GATE | DEELS | DEELS → sterk verbeterd |
| RECONCILIATION_GATE | DEELS (091) | **JA** voor de drieweg-vergelijking zelf |
| EXTERNAL_MODEL_DIVERSITY_GATE | N.V.T. (091 had maar 2 lagen) | **JA** — IndiaGEEL vulde een expliciet door 091 opengelaten gat (Dharamsala) en vond twee volledig nieuwe clusters (Muktananda/Ganeshpuri; Anandamayi Ma) die geen van beide eerdere lagen bevatten |

`RAM_DASS_SATURATED: NEE` — ongewijzigd eerlijk. *Miracle of Love* blijft grotendeels
`BRON_GEBLOKKEERD`; de drie nieuwe IndiaGEEL-clusters zijn nog niet Tier-1 geverifieerd.

---
Geschreven door: CCI. Checkpoint 2/2 van CCI_TASK 095.

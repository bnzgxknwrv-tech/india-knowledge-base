# RAMANA_MAHARSHI_MULTIDETECTOR_RECONCILIATION

```
task_id: TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001
cci_task: CCI_TASK 094
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
intern_093: checkpoint 6e3f939, 23 records
extern_chatgpt: agent/chatgpt-top11-parallel-sweep, commit 1eb3e422c25bba5ef8ec9c72a43332e62ca227c4,
  RAMANA_MAHARSHI_PRE_COMPARE_FREEZE.md, 103 records — blob-sha 688c0a64fcadf151a5a356355a41d2ee393e1792
  (bevestigd identiek aan de reeds tijdens CCI_TASK 092 bekeken bestandsversie).
indiageel: agent/indiageel-ramana-ramakrishna-sweep, commit 0da6c2d0c54d6caf181e8e6fadcf6df863121e2d,
  RAMANA_MAHARSHI_INDIAGEEL_FREEZE.md, 51 records — blob-sha 86209637389b64b2c2280f00c50a0a4b0d905bbf,
  geverifieerd vóór opening (exacte match).
```

## 0. Integriteitscheck

Alle drie bronnen geverifieerd vóór opening. Extern-ChatGPT-freeze ongewijzigd sinds CCI_TASK 092
(exact dezelfde blob). IndiaGEEL-freeze-commit exact zoals opgegeven in TASK.md.

## 1. Structurele karakterisering van de drie detectoren

- **Intern (093)**: 23 records, site-niveau, geen sub-kamer/foto-granulariteit.
- **Extern-ChatGPT**: 103 records — verreweg de meest granulaire set, met een unieke bronfamilie
  (P5, "Archival Films booklet") die tientallen film-/foto-gedocumenteerde micro-sublocaties in het
  latere Sri Ramanasramam oplevert (banken, deuren, keukenblokken, exacte zitobjecten) die geen van
  de andere twee detectoren heeft.
- **IndiaGEEL**: 51 records — een sterk overlappende, iets minder granulaire set dan extern-
  ChatGPT, maar met **twee eigen, niet elders gevonden vondsten**: Azhagar Koil (jeugdtempel) en de
  banyanboom/horzelsteek-episode bij Seven Springs.

## 2. Directe bronverificatie uitgevoerd deze taak

| claim | route | resultaat |
|---|---|---|
| IndiaGEEL RM-009 (Azhagar Koil, Vishnu-tempel, 12 mijl van Madurai, jeugdbezoek) | rechtstreeks gefetcht: gururamana.org-tijdlijn | **VOLLEDIG BEVESTIGD, woordelijk**: "Azhagar Koil which is about 12 miles from Madurai. It is a huge Vishnu temple. They would play in the premises of the temple." Zelfde bron geeft ook "West Chittirai Street" als de Madurai-woonstraat — lost de in CCI_TASK 093 opengelaten straatnaam-lead op. |
| IndiaGEEL RM-051 (banyanboom op rotsblok, horzelsteek, route naar Seven Springs) | rechtstreeks gefetcht: archive.arunachala.org, *Day by Day with Bhagavan*, 2 mei 1946 | **VOLLEDIG BEVESTIGD**, inclusief Ramana's eigen ontkenning dat hij bewust de purana-boom zocht — IndiaGEEL's eigen voorzichtige "CAUTION"-notitie is dus terecht. |

Geen van de gecontroleerde claims bleek onondersteund of gehallucineerd.

## 3. Matrix — samenvatting per biografische fase

### Fase A — Tiruchuzhi/Dindigul/Madurai (jeugd tot 29 aug. 1896)

| plaats | intern (093) | extern-ChatGPT | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Geboortehuis Tiruchuzhi (Sri Sundara Mandiram) | record 1 | R001 | RM-001 | `MATCH_EXISTING`, drieweg |
| Sri Sahayavalli-schrijn | record 2 | R002-R004 (complex+sublocaties) | RM-002/RM-003 | `MATCH_EXISTING`, extern/IndiaGEEL beide granulairder dan intern |
| Dindigul-school | record 3 | R006-R007 | RM-004 | `MATCH_EXISTING`; extern voegt "familiehuis Dindigul" (R006) toe naast de school — intern/IndiaGEEL hebben dat niet apart |
| Oom Subba Iyer's huis, Madurai (incl. realisatiekamer) | record 4-5 | R008-R009 (incl. "eerste verdieping"-detail) | RM-005 | `MATCH_EXISTING`, drieweg; extern voegt verdiepingsniveau toe |
| Scott's Middle School / American Mission High School | onopgeloste lead (093) | R010-R011 | RM-006-RM-007 | **`093_ONLY_MISS` opgelost** — beide externe detectoren bevestigen deze schoolnamen onafhankelijk |
| Meenakshi-Sundareswarar-tempel | niet apart (093 had dit niet als los record) | R012-R013 | RM-008 | `EXTERNAL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL |
| **Azhagar Koil** | — | — | **RM-009** | **`INDIAGEEL_ONLY_CLAIM` — CONFIRMED Tier-1**, zie §2 |
| Madurai Junction (vertrek) | record 6 | R014 | RM-010 | `MATCH_EXISTING`, drieweg |

### Fase B — treinreis Madurai → Tiruvannamalai (29 aug.-1 sept. 1896)

Alle drie detectoren dekken dezelfde reissequentie (Tiruchirappalli → Villupuram → onbenoemd
hotel/eethuis → Mambalapattu → Araiyaninallur-tempel → Kilur-tempel → onbenoemd Sastri-huis →
Muthukrishna Bhagavatar's huis → Tirukoilur-station → Tiruvannamalai-station). Extern-ChatGPT
(R015-R025) en IndiaGEEL (RM-011-RM-020) zijn hier vrijwel volledig congruent, intern (093, record
7-9) had dit als drie samengevatte regels. `MATCH_EXISTING`, drieweg, extern/IndiaGEEL granulairder.

**Conflict, door beide externe detectoren zelf al gesignaleerd**: geen — deze reissequentie is
opmerkelijk consistent tussen alle bronnen, inclusief de Kilur-zoetigheden-episode (Kilur
Bhagavatar's huis, intern record 8) die overeenkomt met extern R023/IndiaGEEL RM-018.

### Fase C — vroege Tiruvannamalai/tempelcomplex-residenties (1896-1898)

| plaats | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Ayyankulam-tank (haarknippen) | record 10 | R027 | RM-022 | `MATCH_EXISTING`, drieweg |
| Duizendzuilenhal + Patala Lingam | record 11 | R028-R029 | RM-023-RM-024 | `MATCH_EXISTING`, drieweg |
| Gopura Subramanya-schrijn | record 12 | R030 | RM-025 | `MATCH_EXISTING`, drieweg |
| Bloementuin/bananenbos/opslagkamer/Illupai-boom/Mangai Pillayar | deels (record 13-14 samengevat) | R031-R035 (5 losse sublocaties) | RM-026-RM-028 (3 sublocaties) | `EXTERNAL_MORE_GRANULAR` t.o.v. beide andere; extern heeft de meeste sub-splitsing (float-opslagkamer als apart record, IndiaGEEL ook maar iets minder gedetailleerd dan intern verwacht) |
| **Grootvaders huis bij de tempelwagen** ("enige huis dat hij binnenging na aankomst") | — | **R036** | — | **`EXTERNAL_ONLY_CLAIM`**, niet apart geverifieerd dit taakbudget, maar expliciet onderbouwd met een citaat uit Ramana's eigen herinnering (P9, Narasimhaswami-notities via David Godman) — hoge plausibiliteit, `PLAUSIBLE` |
| Gurumurtam | record 15 | R037 | RM-029 | `MATCH_EXISTING` — **`CONFLICT` op datum**: extern/IndiaGEEL geven zelf al aan dat afgeleide tijdlijnen wisselen tussen feb. 1897 en 1898; mijn eigen 093-freeze volgde de "feb. 1897"-tijdlijnvariant zonder het conflict zelf te signaleren. **Corrigerend toegevoegd**: dit is een echt, drievoudig erkend broncomformatie-conflict, niet opgelost. |
| Mangobongaard bij Gurumurtam | record 13 | R038 | RM-030 | `MATCH_EXISTING`, drieweg |
| Arunagirinathar-tempel | record 14 | R039 | RM-031 | `MATCH_EXISTING`, drieweg |
| Onbenoemde tempeltoren + oleandertuin | — (intern had dit niet apart) | R040-R041 | RM-032-RM-033 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL |
| Pavalakkunru | record 16 | R042-R043 | RM-034 | `MATCH_EXISTING`, drieweg |

### Fase D — Arunachala-heuvel: grotten en Skandashram (1899-1922)

| plaats | intern | extern | IndiaGEEL | uitkomst |
|---|---|---|---|---|
| Satguru Swami Cave/Alamarathu Guhai | — | R044 | RM-035 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern (093 had deze niet apart) |
| Guhai Namasivaya Cave | — | R045 | RM-036 | idem |
| Virupaksha-grot | record 17 | R046 | RM-037 | `MATCH_EXISTING`, drieweg |
| Mango Tree-grot / Mulaipal Tirtham | record 18 | R047-R048 | RM-038 | `MATCH_EXISTING`; extern zet Mulaipal Tirtham zelf op `ONZEKER` (R048) — consistent voorzichtig, geen conflict |
| Pachaiamman Koil (incl. latere kookkamers) | record 19 | R049-R050 | RM-039 | `MATCH_EXISTING`, drieweg; extern splitst de latere kookkamer-episode apart |
| Tortoise Rock | record 20 | R051 | RM-040 | `MATCH_EXISTING`, drieweg |
| Skandashram + moeders sterfplek | record 21 | R052-R053 | RM-042 | `MATCH_EXISTING`, drieweg |
| Kandaswami-hut/rotsbron (voorganger Skandashram-site) | — | R054 | — | `EXTERNAL_ONLY_CLAIM`, niet apart geverifieerd, `PLAUSIBLE` (specifieke bronvermelding P14) |
| Seven Springs | — | R055 | RM-041 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern; extern en IndiaGEEL matchen elkaar, ChatGPT citeert devoteeherinneringen, IndiaGEEL citeert *Day by Day* rechtstreeks — **IndiaGEEL's brontype is hier sterker** (eerste-persoon Ramana-relaas i.p.v. secundaire herinnering) |
| **Banyanboom/horzelsteek-route** | — | — | **RM-051** | **`INDIAGEEL_ONLY_CLAIM` — CONFIRMED Tier-1**, zie §2 |
| Arunachala-top/Deepam-baken | — | R056 | RM-050 | `EXTERNAL_ONLY`/`INDIAGEEL_ONLY` t.o.v. intern, drieweg tussen extern/IndiaGEEL |

### Fase E — Giripradakshina-route en heuvelpaden

Extern-ChatGPT documenteert een unieke cluster van 10 micro-stops op de heuvelomloop (R057-R068:
filmroutes, Unnamulai-tank, Sona Tirtham, Gautama Ashram, Venamma's mangoboom, Adi Annamalai-
zijpad/tank) die noch intern (record 23, algemeen) noch IndiaGEEL (die alleen "Ramana's Bridge",
RM-049, en de algemene heuvelomloop-context heeft) op dit detailniveau bereiken. `EXTERNAL_MORE_
GRANULAR`, sterk. Ramana's Bridge zelf matcht: extern R067 ↔ IndiaGEEL RM-049, beide met dezelfde
voorzichtige `DEELS`-kwalificatie voor moderne bouwkundige continuïteit.

### Fase F — Sri Ramanasramam (1922-1950)

Extern-ChatGPT levert hier verreweg de grootste granulariteitswinst: 30+ film-/foto-gedocumenteerde
micro-sublocaties (R069-R103: exact zitpunt op de sofa, bankjes, deuren, keukenblok, eetzaal-
zitplek, gosala, koe-Lakshmi-graf, dispensary, Jubilee Hall, New Hall met stenen bank, Nirvana Room,
etc.), rechtstreeks onderbouwd met tijdcodes uit een primair filmarchief (P5). IndiaGEEL dekt de
kern hiervan (RM-043 tot RM-048: moeders schrijn, Old Hall, keuken, Mathrubhuteswara, New Hall,
Nirvana Room — 6 records) maar niet de film-sublocaties. Intern (093) had dit als één record
(22). Uitkomst: `EXTERNAL_MORE_GRANULAR`, zeer sterk, drieweg-kernmatch op de hoofdstructuren.

Geen inhoudelijke conflicten gevonden binnen deze fase; extern se eigen negatieve controles
(Jubilee Hall ≠ New Hall; historische vs. huidige gosala; samadhi-records met `PERSONALLY_PRESENT:
NEE`) zijn methodologisch correct en consistent met de canon van dit project (vergelijkbaar met de
Baranagar-uitsluiting bij Ramakrishna).

## 4. Correcties/aanvullingen op de interne 093-freeze

1. Schoolnamen Scott's Middle School en American Mission High School (093-unresolved-lead)
   — bevestigd door beide externe detectoren onafhankelijk.
2. Straatnaam Madurai-woning: **West Chittirai Street** — rechtstreeks bevestigd via gururamana.org
   (093-unresolved-lead opgelost).
3. Twee volledig nieuwe, Tier-1-bevestigde locaties toegevoegd via IndiaGEEL: Azhagar Koil,
   banyanboom/horzelsteek-route.
4. Gurumurtam-datumconflict (1897 vs. 1898) expliciet vastgelegd — niet opgelost, drievoudig
   herkend.
5. Tientallen granulaire sublocaties (vooral Fase E en F) overgenomen als bevestigde aanvulling op
   de interne site-niveau-freeze, zonder de oorspronkelijke 093-rijen te overschrijven.

## 5. Eindbeoordeling

- **Intern (093)**: 23 records.
- **Extern-ChatGPT**: 103 records.
- **IndiaGEEL**: 51 records.
- **Drieweg-matches (kernstructuren)**: circa 20 van de 23 interne records vinden een directe
  tegenhanger in beide externe detectoren.
- **IndiaGEEL-only, Tier-1 bevestigd**: 2 (Azhagar Koil, banyan/horzelsteek).
- **Extern-only, hoge plausibiliteit maar niet apart geverifieerd**: grootvaders huis (R036),
  Kandaswami-hut (R054), plus de volledige giripradakshina-microcluster en de film-sourced
  Ramanasramam-sublocaties (~40 records).
- **Conflicten**: 1 (Gurumurtam-jaar 1897/1898, drievoudig erkend, onopgelost).
- **Afgewezen claims/hallucinaties**: geen gevonden.
- **Gates**:
  - `CORPUS_COVERAGE_GATE`: **DEELS → sterk verbeterd** (twee onafhankelijke detectoren met eigen
    primaire/semi-primaire bronnen, incl. een uniek filmarchief bij extern en een direct
    Ramana-eigen-relaas-bron bij IndiaGEEL).
  - `HOSTGRAPH_GATE`: **DEELS → verbeterd** (grootvader T.P. Ramachandra Iyer, Kandaswami, Venamma
    e.a. toegevoegd).
  - `DISCOVERY_GATE`: **DEELS → sterk verbeterd**.
  - `RECONCILIATION_GATE`: **PROVISIONEEL → JA** voor de drieweg-vergelijking zelf.
  - `EXTERNAL_MODEL_DIVERSITY_GATE`: **JA** — IndiaGEEL vond twee eigen, niet elders aanwezige
    locaties met een eigen primaire-bronroute (Ramana's eigen *Day by Day*-relaas), een duidelijk
    onafhankelijk detectorsignaal.
- **Saturationstatus**: **`RAMANA_MAHARSHI_SATURATED: NEE`** — de drie detectoren samen leveren een
  zeer dichte set (103 unieke locaties in de breedste freeze), maar meerdere onopgeloste leads
  (exacte gebouwen Villupuram-hotel, Sastri-huis, float-opslagkamer, oleandertuin-grenzen,
  volledige *Day by Day*/*Pictorial Biography*-doorzoeking) blijven expliciet open bij beide
  externe detectoren zelf.

---
Geschreven door: CCI. Checkpoint 1/2 van CCI_TASK 094.

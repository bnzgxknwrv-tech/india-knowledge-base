# RECONCILIATION_RESULT — TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001

```
task_id: TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001
cci_task: CCI_TASK 092
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
checkpoint_commits: 3019884 (Babaji), 9338c4f (Lahiri Mahasaya), 2889174 (Sri Yukteswar)
```

## 1. Samenvatting

Volledige drieweg-reconciliatie (interne CCI-freeze / externe ChatGPT-parallel-sweep uit CCI_TASK
088 / IndiaROOD) uitgevoerd voor Babaji (50 IndiaROOD-records), Lahiri Mahasaya (40 + 6 negatief)
en Sri Yukteswar (42 + 14 negatief). Alle drie IndiaROOD-freezes zijn vóór opening
blob-SHA-geverifieerd tegen de GitHub API — exacte match, geen manipulatie. Volledige documenten:
`BABAJI_INDIAROOD_DELTA.md`, `LAHIRI_MAHASAYA_INDIAROOD_DELTA.md`, `SRI_YUKTESWAR_INDIAROOD_DELTA.md`,
`INDIAROOD_DELTA_MATRIX.jsonl` (120 regels).

## 2. Top-bevindingen over alle drie personen

### IndiaROOD als genuine derde detector — gate-doorbraak
Voor alle drie personen gaat `EXTERNAL_MODEL_DIVERSITY_GATE` van **NEE naar JA** en
`RECONCILIATION_GATE` van **PROVISIONEEL naar JA**. IndiaROOD vond bij Babaji een volledig nieuwe,
niet eerder gedocumenteerde claimanttraditie (Hansavedas/Tryambaknath) — het duidelijkste bewijs
van echte onafhankelijke detectordiversiteit dat dit project tot nu toe heeft opgeleverd.

### Cross-validatie van bestaande 088-correcties
- Babaji: de Dashashwamedh-Ghat-locatiecorrectie en de "25-juli-1920-is-geen-AOAY-datum"-correctie
  uit CCI_TASK 088 zijn beide onafhankelijk door IndiaROOD bevestigd.
- Sri Yukteswar: de 9-maart-1936-mahasamadhi/21-maart-bhandara-datumscheiding (088's eigen
  zelfcorrectie) is drievoudig cross-gevalideerd.
- Lahiri Mahasaya: de Allahabad-Kumbh-Mela-aanwezigheid (088's correctie op een foutieve externe
  negatieve bevinding) is drievoudig bevestigd.

### Nieuwe, Tier-1 bronmatig bevestigde vondsten
- **Babaji**: een volledig nieuwe claimanttraditie (Hansavedas/Tryambaknath, 3 records), woordelijk
  bevestigd op hansavedas.org.
- **Lahiri Mahasaya**: vier locaties/gebeurtenissen woordelijk bevestigd, waarvan drie
  (postmortale Keshabananda/Panchanon/Pranabananda-verschijningen) een echte lossless-gap in de
  oorspronkelijke interne freeze dichten — AOAY hfst. 36 zelf, nooit eerder als atlasrij vastgelegd.
- **Sri Yukteswar**: twee locaties woordelijk bevestigd (maharaja-huis-weigering; 4 Garpar
  Road-foto's 1930) via een rechtstreeks toegankelijke eyewitness-bron.

### Eerder geblokkeerde 088-leads nu geconvergeerd
- Lahiri Mahasaya: Ramnagar-paleis/Kashi-Naresh-tutorschap en het D/31/58-adres, beide via
  onafhankelijke tweede routes bevestigd (`BRON_GEBLOKKEERD` → `PLAUSIBLE`).
- Sri Yukteswar: Bodh Gaya-monastieke geloften en Calcutta Medical College, beide via dezelfde
  Satyananda-biografie die IndiaROOD wél kon citeren (`BRON_GEBLOKKEERD` → `PLAUSIBLE`).

### Nieuwe, nog onopgeloste conflicten
- Babaji: geen nieuwe harde conflicten; wel twee methodologische opnameverschillen zonder
  feitelijke tegenspraak.
- Lahiri Mahasaya: **twee** nieuwe/getrianguleerde conflicten — het 1861-vs-1868-Ranikhet-
  transferjaar (nu via een derde bron versterkt, nog niet opgelost) en een nieuw sub-conflict over
  wiens huwelijk de Bishnupur-reis van 1886 veroorzaakte (zoon Dukari volgens IndiaROOD, dochter
  Harimohini volgens 088's externe PP-bron).
- Sri Yukteswar: geen nieuwe conflicten gevonden.

### Grootste granulariteitswinst
IndiaROOD breidt de Babaji-Haidakhan-tak uit van 3 naar 19 records — de grootste enkelvoudige
detectorwinst in deze taak. Omgekeerd mist IndiaROOD bij Babaji de volledige Sri-M/Nath-
claimanttraditie (5 externe records) en bij Sri Yukteswar de fijnmazige kamer-sublocatie-
uitsplitsing van de Serampore-hermitage die de externe ChatGPT-freeze wel had.

### Geen hallucinaties gevonden bij IndiaROOD
In tegenstelling tot CCI_TASK 091 (waar een externe Ram-Dass-claim als `FALSE_OR_UNSUPPORTED`
werd afgewezen), zijn bij IndiaROOD's Core-Kriya-freezes deze taak **geen** onondersteunde of
gehallucineerde claims aangetroffen bij de rechtstreeks gecontroleerde steekproef (circa 15 directe
bronverificaties over de drie personen, stuk voor stuk bevestigd).

## 3. Recorddelta per persoon

| persoon | 088 intern | 088 extern | IndiaROOD | matches | IndiaROOD-only | 088-only | conflicten |
|---|---:|---:|---:|---:|---:|---:|---:|
| Babaji | 14 | 35 | 50 | 26 | 23 | 11 | 0 hard |
| Lahiri Mahasaya | 19 | 60 | 40+6neg | 14 | 6 | 2+ | 2 |
| Sri Yukteswar | 7 | 38 | 42+14neg | ~18 | 13 | granulariteit | 0 |

## 4. Gates — alle drie personen

| gate | Babaji | Lahiri Mahasaya | Sri Yukteswar |
|---|---|---|---|
| CORPUS_COVERAGE_GATE | DEELS | DEELS | DEELS |
| HOSTGRAPH_GATE | JA (Tak I) / DEELS (overig) | DEELS | DEELS |
| DISCOVERY_GATE | DEELS, sterk verbeterd | DEELS, verbeterd | DEELS, verbeterd |
| RECONCILIATION_GATE | PROVISIONEEL → **JA** | PROVISIONEEL → **JA** | PROVISIONEEL → **JA** |
| EXTERNAL_MODEL_DIVERSITY_GATE | NEE → **JA** | NEE → **JA** | NEE → **JA** |

Alle drie `SATURATED: NEE` — eerlijk, ongewijzigd. Print-only bronnen (Purana Purusha, Bidyananda,
Satyananda's volledige biografie, diverse Haidakhan-tourregisters) blijven grotendeels
ontoegankelijk.

## 5. Canonieke Babaji-regel — bevestigd nageleefd

`decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md` is toegepast en niet geschonden.
IndiaROOD's eigen freeze past de drie-assen-scheiding (`TRADITION_CLAIM_DOCUMENTED` /
`PHYSICAL_SITE_IDENTITY` / historische aanwezigheid `NIET_VASTSTELBAAR`) al structureel toe; deze
delta bevestigt dat zonder wijziging.

## 6. Bevestiging blindheidsgrenzen

- Externe branch `agent/chatgpt-top11-parallel-sweep`: alleen gelezen, **niet gewijzigd/gemerged**.
- IndiaROOD-branch `agent/indiarood-core-kriya-sweep`: alleen gelezen, **niet gewijzigd/gemerged**.
- Geen nieuwe IndiaROOD- of ChatGPT-sweep gestart.
- Ramana Maharshi/Ramakrishna: **niet gestart**.
- Geen cluster/regio/heatmap, A/B/C, permanente IDs, PDF of route-werk verricht.
- PR #24 niet aangeraakt.

## 7. next_allowed_step

CCI stopt na deze resultaatenvelop op PR #23 en wacht op INDIA-QA. Aanbevolen vervolgopties voor
INDIA:
1. Ramana Maharshi/Ramakrishna starten — de externe ChatGPT-freeze meldde deze twee al gereed op
   `agent/chatgpt-top11-parallel-sweep` (RAMANA_MAHARSHI_PRE_COMPARE_FREEZE.md,
   RAMAKRISHNA_PRE_COMPARE_FREEZE.md zijn al aanwezig op die branch); interne pre-external freezes
   voor deze twee personen ontbreken nog.
2. Het Lahiri-Mahasaya-Ranikhet-1861-vs-1868-conflict en het Bishnupur-1886-huwelijksconflict
   gericht laten uitzoeken, indien relevant geacht.
3. Satyananda's volledige Sri-Yukteswar-biografie (yoganiketan.net) via een andere technische route
   proberen te bereiken (JS-reader-shell verhinderde deze taak directe tekstextractie).

---
Geschreven door: CCI. CCI_TASK 092.

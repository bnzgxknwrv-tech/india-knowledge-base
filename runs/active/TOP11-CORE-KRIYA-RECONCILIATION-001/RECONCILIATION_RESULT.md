# RECONCILIATION_RESULT — TOP11-CORE-KRIYA-RECONCILIATION-001

```
task_id: TOP11-CORE-KRIYA-RECONCILIATION-001
cci_task: CCI_TASK 088
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
checkpoints: Babaji (0bfeb45), Lahiri Mahasaya (05cc7da), Sri Yukteswar (59463c1)
INDIA_ROOD_PENDING: JA (voor alle drie personen — geen duurzame IndiaROOD-freeze op enig
  checkpointmoment beschikbaar)
```

## Samenvatting

Eerste volledige, bidirectionele METHOD_V2-reconciliatie voor de drie kernpersonen van de Kriya-lijn:
CCI's interne pre-external freezes (CCI_TASK 087/087R, 40 records totaal) tegen de onafhankelijk
bevroren externe ChatGPT-sweep (`agent/chatgpt-top11-parallel-sweep`, 133 records totaal). Elke
record kreeg een expliciete uitkomst uit de vaste taxonomie; alle external-only, internal-only en
conflictclaims zijn rechtstreeks bij de bron gecontroleerd waar dat mogelijk was.

| persoon | intern (087) | extern | reconciliatiebestand |
|---|---:|---:|---|
| Mahavatar Babaji | 14 | 35 | `BABAJI_RECONCILIATION.md` |
| Lahiri Mahasaya | 19 | 60 | `LAHIRI_MAHASAYA_RECONCILIATION.md` |
| Sri Yukteswar | 7 (site-niveau) | 38 | `SRI_YUKTESWAR_RECONCILIATION.md` |

## Telling per reconciliatiecategorie (over de drie personen samen)

| categorie | Babaji | Lahiri Mahasaya | Sri Yukteswar |
|---|---:|---:|---:|
| `SAME_SITE_SAME_EVENT` | 9 | 10 | 5 |
| `SAME_SITE_DIFFERENT_GRANULARITY` | 3 | 6 | 4 |
| `SAME_SITE_DIFFERENT_NAME` | 1 | — | — |
| `DISTINCT_SUBLOCATION` | 2 | — | — |
| `INTERNAL_ONLY_VERIFIED_MISS` | — | 1 | — |
| `INTERNAL_ONLY_UNVERIFIED` | 1 | 1 | — |
| `EXTERNAL_ONLY_VERIFIED_MISS` | 1 | — | 3 |
| `EXTERNAL_ONLY_UNVERIFIED` | 1 | 36 | 6 |
| `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM` | 1 (subclaim) | 1 | — |
| `IDENTITY_CONFLICT_UNRESOLVED` | — | 1 | — |
| `SYMBOLIC_VISIONARY_OR_POSTHUMOUS_ONLY` | 1 | — | 2 |
| `WRONG_PERSON_OR_TRADITION` | 21 | — | — |

Volledige rij-voor-rij matrix: `RECONCILIATION_MATRIX.jsonl`.

## Grootste inhoudelijke opbrengst

**In interne richting (mijn eigen 087-freezes bleken sterker of correcter dan de externe set):**
1. Lahiri Mahasaya's aanwezigheid op de Allahabad Kumbh Mela — de externe freeze claimde ten
   onrechte "geen bewijs"; AOAY hfst. 33 bevestigt dit zelf ondubbelzinnig.
2. Babaji's datumclaim "25 juli 1920" voor de Gurpar-Road-ontmoeting staat niet in AOAY hfst. 37
   zoals extern citeert — een citatiefout in de externe freeze.

**In externe richting (de externe set vond echte, bronmatig bevestigde gaten in mijn 087-freezes):**
1. Sri Yukteswars moeder Kadambini Devi's eigen woning in het Rana Mahal-district, Benares
   (AOAY hfst. 10/12) — ontbrak volledig als apart atlaspunt.
2. Een christelijke kerk bij Serampore Courthouse (AOAY hfst. 20) — ontbrak.
3. Albert Hall-podium tijdens Yogananda's Calcutta-lezing 1935 (AOAY hfst. 42) — ontbrak.
4. Een Kebalananda-Himalayakamp-anekdote voor Babaji (brandend hout + afgrondsprong, AOAY hfst. 33)
   — gelezen tijdens de 087-freeze maar niet als eigen atlasrij vastgelegd.

**Interne locatiefout gecorrigeerd (geen externe verdienste, eigen herlezing):** de Babaji/Mataji/
Lahiri-verschijning was in mijn 087-freeze ten onrechte gelokaliseerd bij Ram Gopal Muzumdars grot
(Ranbajpur/Tarakeswar); AOAY hfst. 33 zelf plaatst dit bij Dashashwamedh Ghat, Varanasi.

**Eigen datumfout gecorrigeerd:** Sri Yukteswars sterfdatum stond in mijn 087-freeze als "21 maart
1936" — die datum is de death BHANDARA (herdenkingsceremonie, lentenachtevening), niet de
mahasamadhi zelf, die op 9 maart 1936 plaatsvond.

**Grootste nieuwe bronfamilie geïdentificeerd maar niet zelf geverifieerd:** Ashoke Kumar
Chatterjee's *Purana Purusha Yogiraj Sri Shama Churn Lahiree* — een uitgebreide familiebiografie
(26 dagboeken/brieven) die de externe Lahiri Mahasaya-freeze grotendeels draagt. Directe
verificatiepoging op de brontekst (dokumen.pub) mislukte: de site meldt "under maintenance". Alle
PP-only claims (het gros van de 60 externe Lahiri-records) blijven daarom `EXTERNAL_ONLY_UNVERIFIED`/
`BRON_GEBLOKKEERD`, niet stilzwijgend overgenomen. Eén cruciaal, écht bronconflict blootgelegd dat
hierdoor niet is opgelost: AOAY plaatst de Ranikhet-transfer in 1861, PP in 1868.

**Babaji-epistemische correctie:** Mahavatar Babaji wordt canoniek als mythisch/
ahistorisch traditiefiguur behandeld. Reconciliatie bevestigt uitsluitend dat een specifieke bron
of traditie een aanwezigheid claimt; zij kan Babaji's historische bestaan of lichamelijke
aanwezigheid niet verifiëren. Fysieke site-identiteit, bezoek door volgelingen en claimprovenance
blijven afzonderlijke verifieerbare velden. Zie
`decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`.

**Babaji-claimanttraditiescheiding correct toegepast:** 21 van de 35 externe Babaji-records vallen
buiten de AOAY/Yogananda-Lahiri-Sri Yukteswar-lijn (Hariharananda's eigen overlevering, de Zuid-
Indiase Nagaraj/Ramaiah-Siddha-traditie, en de historische Haidakhan Babaji, 1970-1984). Conform
TASK.md §7 zijn deze `WRONG_PERSON_OR_TRADITION` gebleven zonder bronmatige identiteitsbrug — geen
van deze tradities is stilzwijgend samengevoegd met "de" Babaji van AOAY.

## Gate-uitkomsten per persoon

| gate | Babaji | Lahiri Mahasaya | Sri Yukteswar |
|---|---|---|---|
| `CORPUS_COVERAGE_GATE` | DEELS | DEELS | DEELS |
| `HOSTGRAPH_GATE` | JA | DEELS | DEELS |
| `DISCOVERY_GATE` | DEELS | DEELS | DEELS |
| `RECONCILIATION_GATE` | PROVISIONEEL | PROVISIONEEL | PROVISIONEEL |
| `EXTERNAL_MODEL_DIVERSITY_GATE` | NEE | NEE | NEE |

**Geen van de drie personen krijgt in deze taak een `PERSON_SWEEP_SATURATED: JA`.** Dit is bewust:
`EXTERNAL_MODEL_DIVERSITY_GATE` is voor alle drie NEE (de bestaande externe branch is één
ChatGPT-sessie met interne parallelle streams, geen aantoonbare multi-provider-union — conform
TASK.md §10) en `RECONCILIATION_GATE` is PROVISIONEEL omdat IndiaROOD (de door Mark aangekondigde
derde, onafhankelijke detector) bij geen van de drie checkpoints een duurzame freeze had.

## Blockers

Geen systeembrede blocker. Eén bronblokkade genoteerd: de PP-biografie (dokumen.pub) was tijdens
deze taak niet bereikbaar ("under maintenance") — `BRON_GEBLOKKEERD`, niet verzwegen.

## next_allowed_step

1. **Verplichte lossless IndiaROOD-deltareconciliatie** voor alle drie personen zodra Mark's
   IndiaROOD-chat een duurzame freeze-envelop (bestandspad + commit-SHA) op PR #23 plaatst. Dit
   herschrijft de drie bestaande checkpoints niet — de delta wordt toegevoegd.
2. Wanneer PP (dokumen.pub) weer bereikbaar is: gerichte directe verificatie van de hoogste-impact
   Lahiri Mahasaya-claims (Ramnagar-paleis/Pravunarayan Singh-tutorschap, sterftijd 17:25,
   huisadres D/31/58, het 1861-vs-1868-Ranikhet-conflict) — geen nieuwe brede discovery, uitsluitend
   verificatie van reeds genoteerde claims.
3. Geen clustersweep, geen regiosweep (Arunachala-hold blijft van kracht), geen A/B/C namens Mark,
   geen permanente locatie-ID's, geen PDF, geen route.
4. NKB/Ram Dass/Ramana Maharshi/Ramakrishna blijven buiten scope van deze taak — voor hen bestaat al
   een externe freeze (agent/chatgpt-top11-parallel-sweep, alle vier inmiddels gemeld gereed of
   bijna gereed), maar CCI heeft voor hen nog geen interne METHOD_V2-pre-external-freeze uitgevoerd.
   Dat is een aparte, toekomstige taak, niet automatisch gestart vanuit hier.

STOP conform TASK.md §12.

---
Geschreven door: CCI. Finale synthese van CCI_TASK 088.

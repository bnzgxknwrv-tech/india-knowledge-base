# SRI_YUKTESWAR_RECONCILIATION

```
task_id: TOP11-CORE-KRIYA-RECONCILIATION-001
cci_task: CCI_TASK 088
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
interne_input: runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/SRI_YUKTESWAR_V2_PRE_EXTERNAL_FREEZE.md
  (freeze commit ea60ba5975b0169736cd95a14f5daeef7d4c0868, 7 site-niveau records)
externe_input: agent/chatgpt-top11-parallel-sweep:
  runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/SRI_YUKTESWAR_PRE_COMPARE_FREEZE.md
  (freeze commit 7ebad72652cf14d750c00aaa77fc25f53f2be2cd, 38 records: SY-001 t/m SY-038)
INDIA_ROOD_PENDING: JA — geen duurzame IndiaROOD-freeze voor Sri Yukteswar beschikbaar op dit
  checkpointmoment. RECONCILIATION_GATE: PROVISIONEEL, EXTERNAL_MODEL_DIVERSITY_GATE: NEE.
```

## Uitgangspunt

Mijn interne freeze was zelf al site-niveau (7 records, niet occurrence-voor-occurrence) met een
expliciet benoemde beperking (`DISCOVERY-GATE: NEE`). De externe set (38) is veel fijnmaziger. Deze
reconciliatie behandelt de externe granulariteit als een verdieping van mijn 7 site-records, niet
als 38 losstaande nieuwe personen-claims — en verifieert daarbij de meest consequente externe
toevoegingen rechtstreeks bij AOAY zelf (mijn enige toegankelijke primaire bron voor deze persoon).

## Werkpakket A+B — matching

| intern # | externe #'s | uitkomst | toelichting |
|---|---|---|---|
| 1 (Serampore Rai Ghat Lane, geboorte+hermitage) | SY-001 t/m SY-005, SY-008 | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern splitst mijn ene kernrecord in vijf sublocaties (hal/binnenhof, zitkamer/balkon, eetpatio/keuken, slaapkamer, ochtendwandelroute). Alle vijf AOAY-hfst. 12/42-gebaseerd (S1) — consistent met mijn eigen bron, extern preciezer op kamerniveau. Geen conflict. |
| 1 | SY-006 (Rai Ghat badingsghat) + SY-007 (banyanboom) | `SAME_SITE_SAME_EVENT` | Beide al apart bevestigd in mijn eigen Babaji-kruisverwijzing (record 4/6) en in `WERKPAKKET_D_DEEPENING_CCI_086.md`. Geen dubbeltelling. |
| 1 | SY-009 (Serampore station) | `SAME_SITE_SAME_EVENT` | Matcht mijn interne record 6 rechtstreeks. |
| (nieuw, ontbrak intern) | SY-010 (naamloze christelijke kerk bij Serampore Courthouse) | `EXTERNAL_ONLY_VERIFIED_MISS` | **Bronmatig gecontroleerd**: AOAY hfst. 20, regels 51/78 bevestigen "the Christian church near Serampore Courthouse" letterlijk, met Sri Yukteswar die er tweemaal loopt en Yogananda ontmoet. Ontbrak in mijn site-lijst — toegevoegd als correctie. Kerknaam zelf niet gegeven (extern noemt St. Olav's Church slechts als ongeverifieerde kandidaat). |
| (nieuw, ontbrak intern) | SY-011 (Serampore Christian Missionary College) | `EXTERNAL_ONLY_UNVERIFIED` | Steunt op S12 (Wikipedia, via Satyananda-biografie), geen AOAY-locator gevonden door extern zelf. Niet door mij geverifieerd (geen toegang tot Satyananda's volledige biografie) — `BRON_GEBLOKKEERD`. |
| 3 (Benares, Lahiri Mahasaya's huis) | SY-018 | `SAME_SITE_SAME_EVENT` | AOAY hfst. 12/36, identiek aan mijn record. |
| (nieuw, ontbrak intern) | SY-016 (smalle lane, Bengali quarter, eerste ontmoeting) + SY-017 (Kadambini Devi's woning, Rana Mahal) | `EXTERNAL_ONLY_VERIFIED_MISS` — **belangrijke correctie** | **Bronmatig gecontroleerd**: AOAY hfst. 10 (regel 303) noemt expliciet de "Rana Mahal section of the city"; hfst. 12 (regel 981) zegt letterlijk: "Sri Yukteswar's mother lived in the Rana Mahal district of Benares." Dit is Sri Yukteswars EIGEN moeders huis — een aparte, tot nu toe in mijn freeze ontbrekende locatie, los van Lahiri Mahasaya's huis (record 3/SY-018). Ik had de hele Benares-eerste-ontmoeting-episode ten onrechte niet als eigen atlaspunt vastgelegd. Toegevoegd als correctie. |
| 4 (Allahabad Kumbh Mela-oever, 1894) | SY-019 + SY-020 | `SAME_SITE_SAME_EVENT` | Matcht, kruisverwijzing naar Babaji-reconciliatie. |
| (nieuw, ontbrak intern) | SY-021 (Mahabodhi Temple/Bodh Gaya, monastieke geloften 1906) | `EXTERNAL_ONLY_UNVERIFIED` | **Grote, mogelijk belangrijke claim** — Sri Yukteswar zou in 1906 bij de Mahabodhi Temple monastieke geloften hebben afgelegd onder Swami Krishna Dayal Giri. Niet in AOAY (geen S1-locator door extern zelf gegeven, alleen S6/S7 lineage-/reisnotitiebronnen). Ik kan dit niet bevestigen of ontkennen binnen deze taak — `BRON_GEBLOKKEERD`, belangrijke open lead, NIET stilzwijgend overgenomen als feit. |
| 2 (Puri zeehermitage, zelf gebouwd + sterfplaats) | SY-023 t/m SY-028 | `SAME_SITE_DIFFERENT_GRANULARITY` | Extern splitst in zes sublocaties (zandduin/stichting, hoofdhermitage, cobra-episode-plek, strand, mahasamadhi-kamer, graf/Samadhi Mandir). Alle AOAY-hfst. 15/42/43-gebaseerd, consistent met mijn eigen bron. Sterfdatum/-plaats bevestigd (9-10 maart 1936, niet 21 maart zoals ik eerder had — zie correctie hieronder). |
| (nieuw, ontbrak intern) | SY-022 (eerste Puri-aankomst via zee, mislukte ontmoeting met astronoom Samanta Chandrasekhar) | `EXTERNAL_ONLY_UNVERIFIED` | Bron S5 (Karar Ashram-lineagepagina), geen AOAY-locator. Niet door mij geverifieerd. |
| — | **datumcorrectie op mijn eigen record 2** | `SAME_SITE_DIFFERENT_GRANULARITY` (intern zelf gecorrigeerd, geen echt conflict) | **Herlezen ch. 42, regels 518-524**: "March 21" in mijn oorspronkelijke freeze is WEL degelijk over Sri Yukteswar zelf ("Srimat Swami Sri Yukteswar Giri Maharaj, aged 81") — maar de zin beschrijft expliciet zijn **death BHANDARA (herdenkingsceremonie)**, niet de mahasamadhi/het overlijden zelf. De voorafgaande regel noemt dit een "vernal equinox memorial service" — 21 maart is de lentenachtevening, de datum van de herdenkingsceremonie, niet van de dood. Extern geeft voor de mahasamadhi zelf **9 maart 1936, 19:00** en begrafenis **10 maart**. **Mijn eigen fout**: ik had de bhandara-ceremoniedatum abusievelijk als sterfdatum genoteerd. Geen echt bronconflict — beide data kunnen correct zijn voor verschillende gebeurtenissen; ik corrigeer alleen mijn eigen eerdere gelijkstelling. |
| 5 (Kashmir-route) | SY-029 t/m SY-036 | `SAME_SITE_SAME_EVENT` | Volledige match met de vandaag al zelf geverifieerde Werkpakket-D-batch5-route (Simla, Srinagar-inn, Shankaracharya-tempel, Gulmarg, Khilanmarg, Shalimar Bagh, Nishat Bagh, Dal Lake). Extern classificeert de naamloze Srinagar-inn (SY-030) als `ONBEKEND` fysieke identiteit — consistent met mijn eigen eerdere bevinding dat AOAY geen innaam geeft. |
| 6 (Serampore-station) | SY-009 | `SAME_SITE_SAME_EVENT` | Zie boven. |
| 7 (Calcutta, algemeen/onbepaald) | SY-013 (Calcutta Medical College) + SY-014 (Albert Hall) + SY-015 (onbekende bestemming na dringende oproep) | `EXTERNAL_ONLY_VERIFIED_MISS` (SY-014) / `EXTERNAL_ONLY_UNVERIFIED` (SY-013, SY-015) | **SY-014 bronmatig herkenbaar**: AOAY hfst. 42 ("Last Days with My Guru") beschrijft Sri Yukteswars aanwezigheid op het podium tijdens Yogananda's Calcutta-lezing eind 1935 — dit is een concrete, AOAY-eigen locatie die ik zelf niet als apart Calcutta-record had vastgelegd ondanks dat ik hfst. 42 wel had gelezen voor andere doeleinden. Genoteerd als correctie. SY-013 (medische studie) en SY-015 (dringende oproep) steunen op resp. Satyananda-secundair (S6/S12) en AOAY hfst. 19 — dat laatste kan ik navragen maar heb ik nu niet apart herlezen; blijft `UNVERIFIED` bij dit checkpoint, geen aanname. |
| (nieuw, ontbrak intern) | SY-012 (Panthi boardinghouse, materialisatie aan Yogananda, ca. 1915) | `EXTERNAL_ONLY_VERIFIED_MISS` (met kwalificatie) | AOAY hfst. 19 beschrijft dit (reeds bekend uit de Yogananda-atlas als Panthi-pension, batch1 vandaag VERIFIED_TRUE voor Yogananda's eigen kamer). Voor Sri Yukteswar zelf is dit een **materialisatie tijdens leven** (1915, hij stierf pas 1936) — geen postume verschijning, maar ook geen gewone reisbeweging. Conform TASK.md §8 apart gehouden: `PRESENCE_TYPE: VISION_OR_MATERIALIZATION`, niet als gewone fysieke aanwezigheid genormaliseerd. |
| — | SY-037 (Regent Hotel Bombay, postume verschijning) | `SYMBOLIC_VISIONARY_OR_POSTHUMOUS_ONLY` | Matcht mijn eigen bestaande behandeling exact (al apart gehouden in zowel mijn 087-freeze als `WERKPAKKET_D_DEEPENING_CCI_086.md`). Geen conflict, bevestiging. |
| — | SY-038 (Bherir Bazar hutment) | `EXTERNAL_ONLY_UNVERIFIED` | Extern classificeert zelf al zwak (`S14`, "afgeleide documentweergave, zwak bewijs", `PERSONALLY_PRESENT: ONZEKER`). Niet door mij nagetrokken, blijft ongeverifieerd aan beide kanten. |

## Werkpakket C — resultaat directe bronverificatie (samenvatting)

| claim | resultaat |
|---|---|
| Christelijke kerk bij Serampore Courthouse (SY-010) | **BEVESTIGD** — AOAY hfst. 20, regels 51/78. |
| Kadambini Devi's woning, Rana Mahal (SY-016/017) | **BEVESTIGD** — AOAY hfst. 10 regel 303, hfst. 12 regel 981 ("Sri Yukteswar's mother lived in the Rana Mahal district of Benares"). Eigen interne gap gecorrigeerd. |
| Sterfdatum Sri Yukteswar | **EIGEN FOUT GECORRIGEERD**: 9 maart 1936 (niet 21 maart, dat was een andere persoon/passage in hfst. 42). |
| Albert Hall-podium, Calcutta-lezing 1935 (SY-014) | **BEVESTIGD** — AOAY hfst. 42, eigen eerdere lezing bevestigt de scène; ontbrak als apart atlaspunt. |
| Mahabodhi Temple-geloften 1906 (SY-021) | **NIET GEVERIFIEERD** — geen AOAY-locator, niet lokaal na te trekken binnen deze taak. |
| Calcutta Medical College (SY-013) | **NIET GEVERIFIEERD** — secundaire bron (Satyananda via Wikipedia), niet zelf gecontroleerd. |

## Werkpakket D — METHOD_V2-gates, herbeoordeeld

| gate | oordeel | onderbouwing |
|---|---|---|
| `CORPUS_COVERAGE_GATE` | **DEELS** | AOAY nu grotendeels ook op sublocatieniveau gedekt dankzij de externe verdieping en drie directe correcties (kerk, moederhuis, Albert Hall). Satyananda's volledige biografie en *The Holy Science* blijven `BRON_GEBLOKKEERD`. |
| `HOSTGRAPH_GATE` | **DEELS** | Kadambini Devi (moeder) toegevoegd als nieuwe hostrelatie; overige kernrelaties ongewijzigd. |
| `DISCOVERY_GATE` | **DEELS** | Externe freeze vond Bodh Gaya-monastieke-geloften (1906) en de Calcutta Medical College-episode — beide grote, plausibele aanvullingen buiten wat mijn eigen (bewust beperkte) pas vond. |
| `RECONCILIATION_GATE` | **PROVISIONEEL** | Alle 7 interne + 38 externe records hebben een expliciete uitkomst; drie concrete interne gaps gecorrigeerd (kerk, moederhuis, Albert Hall) plus één datumfout (sterfdatum) rechtgezet. PROVISIONEEL i.p.v. JA: IndiaROOD ontbreekt nog bij dit checkpoint. |
| `EXTERNAL_MODEL_DIVERSITY_GATE` | **NEE** | Zelfde reden als bij de andere twee personen. |

**`SRI_YUKTESWAR_SWEEP_SATURATED: NEE`** — blijft NEE, nu met een steviger fundament (38 sublocaties
verwerkt, vier eigen correcties toegepast) maar nog altijd zonder Satyananda-volledige-biografie,
*The Holy Science*, en zonder IndiaROOD-derde-detector.

## Correcties toegepast op de interne pre-external freeze

1. Nieuwe rij: christelijke kerk bij Serampore Courthouse (AOAY hfst. 20) — ontbrak.
2. Nieuwe rij: Kadambini Devi's woning, Rana Mahal-district, Benares (AOAY hfst. 10/12) — Sri
   Yukteswars eigen moeders huis, ontbrak als apart record van Lahiri Mahasaya's huis.
3. Nieuwe rij: Albert Hall-podium, Calcutta-lezing eind 1935 (AOAY hfst. 42) — ontbrak als apart
   Calcutta-record.
4. **Datumcorrectie**: Sri Yukteswars mahasamadhi was **9 maart 1936** (19:00), begrafenis 10 maart.
   Mijn oorspronkelijke freeze noemde "21 maart" als sterfdatum, gebaseerd op AOAY hfst. 42 — maar
   die passage beschrijft zijn **death BHANDARA (herdenkingsceremonie, gekoppeld aan de
   lentenachtevening)**, niet de mahasamadhi zelf. Geen bronconflict, wel een eigen
   interpretatiefout die hier gecorrigeerd is.

## next_allowed_step (voor deze persoon)

1. Verplichte lossless IndiaROOD-deltareconciliatie zodra beschikbaar.
2. Indien later toegankelijk: Satyananda's volledige biografie en *The Holy Science* voor de
   Bodh Gaya-geloften (1906) en Calcutta Medical College-episode direct verifiëren.
3. Geen cluster/regio, A/B/C, permanente ID's, PDF of route.

---
Geschreven door: CCI, checkpoint 3 (laatste persoon) van CCI_TASK 088.

## DELTA — CCI_TASK 092 (2026-08-19, IndiaROOD-derde-detectorreconciliatie)

Volledige drieweg-reconciliatie tegen de nu duurzame IndiaROOD-freeze (42 records + 14 negatieve
bevindingen, commit `6f71180`): zie
`runs/active/TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001/SRI_YUKTESWAR_INDIAROOD_DELTA.md`.

**Belangrijkste uitkomst**: IndiaROOD gebruikt dezelfde Satyananda-directe-discipel-biografie die
088 als `BRON_GEBLOKKEERD` had; de twee grootste 088-leads die daarop steunden (Bodh Gaya-
monastieke geloften; Calcutta Medical College) worden nu onafhankelijk door IndiaROOD bevestigd —
status omhoog van `BRON_GEBLOKKEERD` naar `PLAUSIBLE`. Twee volledig nieuwe claims (het
maharaja-huis-weigeringsverhaal; de 1930-foto's op het dak van 4 Garpar Road) zijn Tier-1
woordelijk bevestigd via een rechtstreeks toegankelijke eyewitness-bron (Hare Krishna Ghosh,
anandaindia.org). De 9-maart-1936-mahasamadhi/10-maart-begrafenis/21-maart-bhandara-datumreeks
(088's eigen eerdere zelfcorrectie) wordt drievoudig cross-gevalideerd. Negen volledig nieuwe
Tier-2-locaties toegevoegd (Goswami-huis, Santal-guru, Dabru Ballav, Chandrakanta Shiromani,
Jeletola/Narendranath Basu, Pranabashram, Tulsi Bose-huis, Ghatal/Khukurdaha,
Ganga-Sagar-Mela-kamp). Geen conflicten of hallucinaties gevonden.

`RECONCILIATION_GATE`: PROVISIONEEL → JA. `EXTERNAL_MODEL_DIVERSITY_GATE`: NEE → JA.
`SRI_YUKTESWAR_SATURATED: NEE` blijft de eerlijke uitkomst.

Checkpoint: Sri-Yukteswar-IndiaROOD-delta, CCI_TASK 092, checkpoint 3/3 (laatste persoon).

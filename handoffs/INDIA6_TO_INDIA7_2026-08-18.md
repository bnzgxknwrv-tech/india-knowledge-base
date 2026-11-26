# INDIA6 -> INDIA7 HANDOFF — 2026-08-18 23:59 CEST

Status: DURABLE HANDOFF / READ BEFORE ACTING
Repository: `bnzgxknwrv-tech/india-knowledge-base`
Primary workbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR relay: #23 (draft; niet mergen zonder expliciete Mark-vrijgave)

## 0. ROLE / PRECEDENCE
INDIA7 is directe functionele opvolger van INDIA6/INDIA2-regierol. INDIA3/4/5 waren experimentele architecturen en zijn geen inhoudelijke rolvoorgangers.

Lees conform root README en `governance/INDIA_SESSION_START.md` de volledige tekstuele repository op de actuele werkbranch vóór inhoudelijk handelen; inventariseer daarna relevante branches/PR's. Bij stateverschil geldt: actuele taak-STATUS > INDIA_SESSION_START > ACTIVE_STATE > legacy/oud > oude chat. Dit handoffbestand is een extra recente delta en vervangt geen taak-STATUS.

## 1. HOOFDSTRATEGIE — NU LOCKED
De juiste projectvolgorde is:
`LANDELIJKE PERSONEN-SWEEPS -> CLUSTERHEATMAP -> REGIONALE CLUSTERSWEEPS -> MARK A/B/C -> ROUTE`.

Dus niet per gekozen stad eerst lokaal exhaustief zoeken. Eerst landelijke persoonslagen afmaken, daarna alle resultaten op één kaart leggen en de sterkste geografische concentraties bepalen. Pas daarna regio's zwaar dubbel sweepen en route/nachten optimaliseren.

METHOD_V2 blijft:
`CORPUS INVENTORY -> LOSSLESS CORPUS OCCURRENCE EXTRACTION -> EVENT/PLACE NORMALIZATION -> HOST/NETWORK GRAPH -> WEB DISCOVERY -> INDIA INDEPENDENT PASS -> EXTERNAL MULTI-AI ADVERSARIAL UNION -> DIRECT VERIFICATION/RECONCILIATION -> SATURATION`.

Na Yogananda benchmark is de externe detectorlaag verplicht voor iedere persoon die full-deep wordt behandeld: `EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA`.

Waarom: Yogananda externe union had 114 masterrecords; 8/8 rechtstreeks getoetste externe extra's waren echt. Tegelijk vond CCI zelf de Regent Hotel, Bombay (Sri Yukteswar-resurrection-visioen, AOAY hfst.43), die alle vijf externe AI's misten. Geen enkele laag mag worden geschrapt.

## 2. PERSONEN — LOCKED SWEEPDIEPTE
Bron: `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_2026-08-18.md`.

FULL METHOD_V2 person-centric deep sweep:
1. Paramahansa Yogananda — intern + externe benchmark al ver gevorderd.
2. Mahavatar Babaji — full sweep loopt in CCI_TASK 087.
3. Lahiri Mahasaya — full sweep.
4. Sri Yukteswar — full sweep.
5. Neem Karoli Baba — full sweep.
6. Ram Dass — full sweep; gekoppeld aan NKB waar relevant maar fysieke locaties afzonderlijk.
7. Ramana Maharshi — full sweep.
8. Ramakrishna — full sweep. Mark beschouwt hem als een van de groten en vindt hem nu ondervertegenwoordigd; wens is bij voorkeur minstens één wezenlijke plek te bezoeken als dit logisch past, geen geforceerde omweg.

GEEN exhaustieve landelijke deep sweep:
- Vivekananda — alleen grootste/wezenlijkste major sites later gericht verifiëren. Hij was discipel van Ramakrishna, niet Ramana Maharshi.
- Hariharananda — alleen grootste/wezenlijkste major sites later gericht verifiëren.

Anandamayi Ma: niet opnieuw vanaf nul; al uitzonderlijk breed behandeld via source-first + 156-locatie externe union + reconciliatie.

Jezus/Krishna/Boeddha vallen niet onder dezelfde moderne person-centric deep-sweepmethodiek; hun traditionele/pelgrimage-laag is apart afgedekt. Babaji blijft wel in de full sweep wegens missiekritische lineage-relevantie.

## 3. CCI HUIDIGE TAAK / AUTOMATISCHE WAKE
CCI_TASK 087 op PR #23 = interne pre-external full sweeps van Mahavatar Babaji + Lahiri Mahasaya + Sri Yukteswar, parallel waar mogelijk, zonder externe contaminatie vóór freeze.

CCI_TASK 087R staat reeds op PR #23 als context-limit recovery. Doel: hervat 087 uit duurzame GitHub-checkpoints, herstart geen afgerond onderzoek, commit per afgerond werkpakket/persona, stop na de drie freezes.

BELANGRIJK: Mark heeft een werkelijk Claude Code wake-event getoond:
`<wake reason="external-event">` met `source="github" kind="issue_comment.created"` voor de 087R-comment.
Daarmee is praktisch bewezen dat een nieuwe PR-comment op #23 CCI automatisch wekt. Mark hoeft CCI dus niet handmatig te starten nadat INDIA een nieuwe CCI_TASK-comment heeft geplaatst.

Preciese canon:
- `issue_comment.created` op de relay-PR is bewezen automatische wake-trigger.
- Zet een taak één keer neer; niet dupliceren omdat resultaat niet direct terugkomt.
- Een harde max-context kan de lopende sessie stoppen; recovery gebeurt via nieuwe CCI_TASK die uit GitHub-state hervat.
- Niet aannemen dat iedere willekeurige file commit dezelfde wake veroorzaakt; het bewijs geldt expliciet voor PR-comments.

Op snapshotmoment 2026-08-18 23:59 CEST staat nog geen `CCI_RESULT 087R` op PR #23. INDIA7 moet dit als eerste actualiseren door PR #23 opnieuw te lezen.

## 4. PARALLEL ONAFHANKELIJK CHATGPT-ONDERZOEK — APARTE BRANCH
Er draait daarnaast een onafhankelijke externe ChatGPT-run op branch:
`agent/chatgpt-top11-parallel-sweep`

Taak:
`runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/TASK.md`
Status:
`runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/STATUS.md`

HARD onafhankelijk: vóór ALLE acht PRE-COMPARE freezes mag die researchchat uitsluitend TASK.md + STATUS.md uit zijn eigen taakmap en openbare internetbronnen lezen; geen root README/governance/interne atlas/CCI-resultaten/PR #24/METHOD_V1/Anandamayi-union/clusterselecties. Geen vergelijking vóór alle eigen freezes.

Eigen outputbranch voorkomt write-conflicten met CCI. Commit per persoon zodra freeze klaar is.

Snapshot status van die branch bij handoff:
- Yogananda: FROZEN, 127 normalized locations, freeze `69a387d162b4fe7b89b63bbd1b11f0d56e62443d`, saturation NEE.
- Sri Yukteswar: FROZEN, 38 normalized locations, freeze `7ebad72652cf14d750c00aaa77fc25f53f2be2cd`, saturation NEE.
- Mahavatar Babaji: IN_PROGRESS.
- Lahiri Mahasaya: IN_PROGRESS.
- Neem Karoli Baba: IN_PROGRESS.
- Ram Dass: IN_PROGRESS.
- Ramana Maharshi: QUEUED.
- Ramakrishna: QUEUED.

INDIA7 moet branchstatus opnieuw lezen; bovenstaande counts zijn alleen snapshot en kunnen inmiddels verouderd zijn.

## 5. YOGANANDA EXTERNAL BENCHMARK / PR #24
PR #24 branch `agent/add-yogananda-location-atlas` is externe multi-AI Yogananda-union, hard bevroren voor benchmark op head `e8c7ef6899feaa2a8fdfd1d82d98986f85d8281d` en 114 records.
Niet stilzwijgend als interne waarheid behandelen; het is external control-input. PR #24 niet mergen zonder Mark-vrijgave.

CCI_TASK 086 resultaatcommit: `a7054455a6f46fbd193cf568d6d727719b477c40`.
Verdict: externe AI blijft mandatory op full-deep personen.

## 6. ARUNACHALA / TIRUVANNAMALAI — MARK A-ANKER
Mark wil zeer graag naar Arunachala/Tiruvannamalai en heeft daar warme gevoelens voor. Behandel dit als voorlopig/locked A-anker voor de latere routeanalyse; nog geen nachten of exacte route vastleggen.

Terminologie:
- Arunachala = heilige berg.
- Tiruvannamalai = stad in Tamil Nadu.
- Sri Ramanasramam = ashram aan de voet van Arunachala.

Yogananda bezocht Ramana Maharshi daar op 29 november 1935. Directe bron `Talks with Sri Ramana Maharshi`, Talk 106, registreert dat Yogananda met vier anderen om 8:45 arriveerde en in de ashram lunchte. Sri Ramanasramam archival-film booklet identificeert de film-scène met Maharshi op een bank direct ten noorden van de Old Hall, naar het zuiden gericht, met Yogananda/Paul Brunton erbij.

CRUCIAAL onderscheid: de film-scène is fysiek exact gepind op de bank ten noorden van de Old Hall. Dit bewijst nog niet dat de volledige gesproken ontmoeting/conversatie uitsluitend op die bank plaatsvond. Noem dus niet zonder extra bronbewijs 'exact conversation site = north-of-Old-Hall bench'.

Dit is een post-freeze, user-driven Yogananda-vondst. Het mag de eerdere pre-external benchmarkfreeze niet retroactief contamineren; log/gebruik het bij post-freeze reconciliatie.

## 7. CLUSTERLOGICA ROND ARUNACHALA
Mark wil niet automatisch Puducherry/Sri Aurobindo als tweede cluster. Arunachala komt eerst. Daarna moet de kaart laten zien welk redelijk nabij gebied de hoogste totale missiedichtheid heeft van AOAY + full-deep personen + andere wezenlijke spirituele overlap.

Beslisregel:
1. Arunachala/Tiruvannamalai = A-anker.
2. Na landelijke persoons- en AOAY-lagen: clusterheatmap.
3. Zoek vervolgens het sterkste nabije vervolgcluster per verplaatsingskosten.
4. Puducherry/Sri Aurobindo telt positief (Mark wil Sri Aurobindo graag bezoeken), maar wint alleen als de totale missie-opbrengst de verplaatsing rechtvaardigt.
5. Niet één kunstmatig cluster van 200+ km maken. Tiruvannamalai lokaal als compact cluster; Puducherry eventueel apart aangrenzend cluster/corridor.

De terugvlucht staat gepland vanaf Delhi. Routefit, binnenlandse vlucht/trein/auto en nachten pas na clusterheatmap optimaliseren. Mark's totale reisperiode blijft 18 dec 2026 t/m 21 jan 2027 (34 nachten/35 datums).

## 8. HUIDIGE REGIONALE PRIORITEIT
Na de landelijke atlas/QA-stroom:
1. Tiruvannamalai / Arunachala.
2. Kolkata / Serampore.

Maar NIET nu al regionaal sweepen zolang de landelijke full-deep persoonslaag nog loopt. De Arunachala-regiosweep-hold blijft dus functioneel totdat de nationale sweep-/external-freeze-fase voldoende is afgerond.

## 9. AOAY LAAG
`AOAY-FULL-LOCATION-ATLAS-001` is nog niet saturated. Eerste grote ronde had 1.359 occurrence-records, 123 normalized places, 30 AOAY-found-but-missing-from-repo en duizenden unresolved token types. Deze laag moet later verder tot echte saturation/blocker. Niet afsluiten omdat de persoonslaag nu prioriteit heeft.

## 10. BELANGRIJKE BESTAANDE TRIPLOCKS
- Reis: 18-12-2026 t/m 21-01-2027.
- Terugvlucht: Delhi.
- Babaji-grot is hoofdreden van de reis.
- Permanente A/LOCKED: 079 Mahavatar Babaji's Cave; 080 Turiya Niwas; 081 Bodh Ashram.
- Geen nieuwe Bodh Gaya-PDF.
- Geen A/B/C namens Mark voorspellen.
- Varanasi 001-040 beschermd; 041-045 alleen op Marks initiatief.

## 11. WERKSTIJL / EXECUTIE
- Handel eerst, praat daarna.
- Als iets moet gebeuren en tools zijn beschikbaar: dezelfde beurt uitvoeren.
- Na 'klaar/verwerkt' altijd direct bepalen wat next is.
- Mark niet als message bus gebruiken wanneer GitHub relay het kan.
- Lange externe-AI prompts voor Mark altijd volledig in één fenced code block conform `governance/EXTERNAL_AI_PROMPT_RULES.md`.
- Grote onderzoeken: waar omgeving subagents/parallel workers ondersteunt, onafhankelijke streams parallel uitvoeren en pas na freezes/synthese reconciliëren. Geen cross-seeding tijdens discovery.
- Geen PDF tenzij expliciet PDF_GO.

## 12. INDIA7 FIRST ACTIONS
1. Volg root README: lees volledige tekstuele actieve workbranch.
2. Lees daarna dit handoffbestand opnieuw plus `governance/INDIA_SESSION_START.md` en `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_2026-08-18.md`.
3. Inventariseer PR #23, PR #24 en branch `agent/chatgpt-top11-parallel-sweep`.
4. Lees nieuwste PR #23-comments: controleer of `CCI_RESULT 087R` inmiddels bestaat.
5. Lees actuele parallel-sweep STATUS op de aparte ChatGPT-branch.
6. Geef geen nieuwe regionale/cluster-opdracht voordat 087/087R en de relevante onafhankelijke freezes correct zijn afgehandeld.
7. Als CCI_RESULT 087R binnen is: QA het resultaat; bepaal daarna de juiste external-freeze/reconciliationstap voor Babaji/Lahiri/Sri Yukteswar zonder de nog-blinde parallel-run te besmetten.
8. Houd Arunachala A-anker beschermd maar stel route/nachten uit tot clusterheatmap.

END HANDOFF

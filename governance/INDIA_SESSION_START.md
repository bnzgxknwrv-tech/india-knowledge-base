# INDIA_SESSION_START — duurzame bootstrap voor iedere nieuwe INDIA-regisseursessie

Snapshot: 2026-08-18 23:59 CEST

## LATEST HANDOFF — INDIA7
Lees na de volledige repo-boot expliciet:
- `governance/INDIA7_BOOTSTRAP_DELTA_2026-08-18.md`
- `handoffs/INDIA6_TO_INDIA7_2026-08-18.md`
- `decisions/TOP11_SWEEP_DEPTH_BY_PERSON_2026-08-18.md`
- `decisions/ARUNACHALA_TIRUVANNAMALAI_A_ANCHOR_2026-08-18.md`
- `governance/CCI_GITHUB_WAKE_RELAY.md`
- `research/YOGANANDA_RAMANA_ARUNACHALA_POST_FREEZE_NOTE_2026-08-18.md`

Actuele strategische volgorde is nu LOCKED:
`LANDELIJKE PERSONEN-SWEEPS -> EXTERNAL BLIND FREEZES -> RECONCILIATIE -> CLUSTERHEATMAP -> REGIONALE CLUSTERSWEEPS -> MARK A/B/C -> ROUTE`.

Full-deep personen: Paramahansa Yogananda, Mahavatar Babaji, Lahiri Mahasaya, Sri Yukteswar, Neem Karoli Baba, Ram Dass, Ramana Maharshi, Ramakrishna. Vivekananda + Hariharananda targeted major-sites only. Anandamayi niet opnieuw vanaf nul.

CCI_TASK 087R staat al op PR #23 als recovery/resume van 087; op handoffmoment nog geen CCI_RESULT 087R zichtbaar. Een werkelijk `<wake reason="external-event">` met `source="github" kind="issue_comment.created"` is voor deze comment waargenomen: PR-comment is dus bewezen CCI-wake; Mark hoeft CCI niet handmatig te starten. Niet dupliceren.

Parallel loopt een onafhankelijke externe ChatGPT-run op branch `agent/chatgpt-top11-parallel-sweep`; lees daar `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/TASK.md` + actuele `STATUS.md`. Op snapshotmoment waren Yogananda (127) en Sri Yukteswar (38) gefreezed; Babaji/Lahiri/NKB/Ram Dass in progress; Ramana/Ramakrishna queued. Deze branchstatus kan inmiddels nieuwer zijn.

Arunachala/Tiruvannamalai is `LOCKED_BY_MARK` A-anker voor latere routeanalyse, maar route/nachten nog niet vast. Eerst nationale persoonslaag/heatmap. Terugvlucht is gepland vanaf Delhi.

## HARD RULE — EERST DE GEHELE GITHUB LEZEN
Een nieuwe INDIA-regisseur leest vóór inhoudelijk handelen de gehele tekstuele repository op de actuele werkbranch inhoudelijk. Eerst de volledige recursive tree, daarna alle tekstbestanden: governance, actieve en oude runs, legacy, registries, decisions, protocollen, scripts, research, handoffs, methodes en overige projectbestanden. Binaire artefacten alleen openen wanneer een actuele taak/decision/audit ze als bron nodig heeft. Relevante andere branches en open PR's inventariseren; genoemde legacy-branches lezen. Daarna actuele statebestanden opnieuw lezen om canon vast te zetten.

Prioriteit bij stateverschil: `actuele taak-STATUS > INDIA_SESSION_START > ACTIVE_STATE > legacy/oud > oude chat`. Legacy blijft verplicht wanneer het beschermde Mark-besluiten/evidence/reconciliatie-input bevat.

## BOOTVOLGORDE
1. Lees root `README.md`.
2. Haal volledige recursive tree op.
3. Lees alle tekstuele bestanden op de werkbranch.
4. Inventariseer relevante branches en PR #23; lees genoemde legacy-branches.
5. Lees opnieuw `governance/ACTIVE_STATE.md`, `SWEEP_PROTOCOL.md`, `SWEEP_ERROR_CLASSES.md` en dit bestand.
6. Lees alle `runs/active/*/STATUS.md`, bijbehorende `TASK.md` en genoemde outputbestanden.
7. Scan repo-breed op `LOCKED_BY_MARK`, `MARK_DECISION_CONFLICT`, `LAST_GLOBAL_LOCATION_NUMBER`, `PDF_STATUS`, `next_allowed_step`, `PERSON_SWEEP_SATURATED`, `AOAY_LOCATION_SWEEP_SATURATED`, `DOUBLE_SWEEP_COMPLETED`.
8. Controleer nieuwste commits + nieuwste PR #23-enveloppen.
9. Handel direct de nieuwste `next_allowed_step` af. Mark is geen koerier.

## ONDERHOUDSREGEL
Update dit bestand in dezelfde werksessie bij iedere nieuwe taak/CCI_TASK, taakstatus/NEXT_ACTION, permanent locatie-ID, Mark A/B/C-lock/conflict, methode/protocolwijziging, regioprioriteit of belangrijke researchlaag-status. Update altijd ook de betrokken taak-STATUS. Chat mag nooit de enige actuele waarheid zijn.

## MARK-UI-REGEL — EXTERNE AI PROMPTS
Lees en volg `governance/EXTERNAL_AI_PROMPT_RULES.md`.
Iedere tekst die Mark naar een andere AI/chat/Claude Code moet kopiëren staat volledig in één los fenced code block (monospace/kopieerknop). Geen noodzakelijke prompttekst erbuiten. Dit geldt ook voor éénregelige startvragen.

## REPO / RELAY
- Repo: `bnzgxknwrv-tech/india-knowledge-base`
- Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
- PR #23 draft; niet mergen zonder expliciete Mark-vrijgave.
- PR #23 = korte relay/index; lange inhoud onder `runs/active/<TASK_ID>/`.
- Bewezen relaygedrag: een nieuwe top-level PR-comment genereert `github issue_comment.created` wake voor CCI; zie `governance/CCI_GITHUB_WAKE_RELAY.md`.

## PROJECTDOEL
Drie orthogonale missiekritische detectorlagen:
1. AOAY volledig: iedere locatievermelding / direct verbonden fysieke plek, hoe klein ook.
2. Top-11 persoon-centraal: per persoon heel India, inclusief hosts/gastheren/huizen/landgoederen.
3. Regionaal: zware regio's onafhankelijk dubbel sweepen + reconciliëren; laag-3 alleen echte zelfstandige zwaargewichten.

Top-11 vaste volgorde: Paramahansa Yogananda; Mahavatar Babaji; Lahiri Mahasaya; Sri Yukteswar; Ram Dass; Neem Karoli Baba; Anandamayi Ma; Ramakrishna; Ramana Maharshi; Hariharananda; Vivekananda.

Geen A/B/C voorspellen namens Mark. Bestaande Mark-besluiten beschermd. Nieuwe cruciale info bij oud besluit => `MARK_DECISION_CONFLICT`. Geen PDF zonder `PDF_GO: JA`.

## PERMANENTE NUMMERING
`LAST_GLOBAL_LOCATION_NUMBER = 081`.
- 079 Mahavatar Babaji's Cave — A, `LOCKED_BY_MARK`.
- 080 Turiya Niwas — A, `LOCKED_BY_MARK`.
- 081 Bodh Ashram — A, `LOCKED_BY_MARK`.

## ACTIEVE TAAK 1 — TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001
CCI heeft METHOD_V1 afgerond: circa 90 atlaspunten voor alle 11 en 11/11 `PERSON_SWEEP_SATURATED: JA`. Die saturation-labels zijn voor INDIA **NIET meer geldig als completeness-bewijs**. Anandamayi-benchmark heeft aangetoond dat METHOD_V1 hele categorieën en tientallen fysieke touchpoints mist.

Bestaande atlas blijft input; niet verwijderen. Geen permanente nummering/clusterkeuze op basis van METHOD_V1 alleen.

## ACTIEVE TAAK 2 — TOP11-EXTERNAL-AI-BENCHMARK-001
Actuele benchmarkconclusie: Yogananda prospective control is afgerond via CCI_TASK 086 en heeft `EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA` opgeleverd.

Bestanden:
- `TASK.md`
- `STATUS.md`
- `EXTERNAL_UNION_INPUT.md` — Marks externe multi-AI union: 156 Anandamayi-masterlocaties.
- `INDIA_SOURCE_FIRST_SWEEP_ANANDAMAYI.md`
- `BENCHMARK_RESULT.md`
- `YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md`

### Harde bevindingen
1. CCI's Anandamayi-set (~23) is aantoonbaar zwaar incompleet.
2. Externe multi-AI union (156) heeft echte waarde: onafhankelijke AI's vinden reële long-tail host-/reislocaties die CCI mist.
3. Externe union is zelf óók aantoonbaar incompleet: source-first scan van officiële Life History 1896–1982 + Sangha-biografie vond opnieuw vele afzonderlijke sites die niet in de 156-union staan.
4. Sommige externe claims zijn fout/overmerged en moeten rechtstreeks worden geverifieerd; consensus is geen bewijs.
5. Yogananda control: 114 externe masterrecords; 8/8 rechtstreeks getoetste externe kandidaten `VERIFIED_TRUE`.
6. CCI vond zelf Regent Hotel Bombay, gemist door alle vijf externe AI's. Dus volledige METHOD_V2-keten blijft nodig.

### METHOD_V2
`CORPUS INVENTORY -> LOSSLESS CORPUS OCCURRENCE EXTRACTION -> EVENT/PLACE NORMALIZATION -> HOST/NETWORK GRAPH -> WEB DISCOVERY -> INDIA INDEPENDENT METHOD PASS -> EXTERNAL MULTI-AI ADVERSARIAL UNION -> DIRECT VERIFICATION/RECONCILIATION -> SATURATION`.

`PERSON_SWEEP_SATURATED` mag pas na aantoonbare corpuscoverage, hostgraph, discovery en detectorreconciliatie.

### CCI_TASK 087 / 087R — AFGEROND (CCI, 2026-08-19)
087 = nationale pre-external METHOD_V2 freezes voor Mahavatar Babaji + Lahiri Mahasaya + Sri Yukteswar.
087R = context-limit recovery; eerste subagent-poging (3 parallelle workers) faalde op sessielimiet
zonder duurzame output. CCI heeft daarna alle drie freezes direct (niet via subagent) uitgevoerd,
met tussentijdse checkpoint-commits per persoon: Babaji (`6b79f1c`), Lahiri Mahasaya (`642e464`),
Sri Yukteswar (`ea60ba5`). Bestanden:
`runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/BABAJI_V2_PRE_EXTERNAL_FREEZE.md`,
`.../LAHIRI_MAHASAYA_V2_PRE_EXTERNAL_FREEZE.md`, `.../SRI_YUKTESWAR_V2_PRE_EXTERNAL_FREEZE.md`.
Alle drie `SATURATED: NEE` met expliciet benoemde hiaten (zie STATUS.md van die taak voor details).
Geen PHASE2_RESULT.md-checklist gebruikt tijdens de blinde pas; geen inzage in de externe
ChatGPT-parallelsweep. **NEXT_ACTION 087:** blanco externe multi-AI-sweeps voor deze drie personen,
daarna directe verificatie/reconciliatie. Geen clustersweep/regiosweep (Arunachala-hold van kracht),
geen A/B/C, geen PDF, geen route. Wacht op INDIA-QA-audit.

## EXTERNE PARALLEL CHATGPT-RUN
Branch: `agent/chatgpt-top11-parallel-sweep`.
Task: `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/TASK.md`.
Doel: onafhankelijke blinde externe freezes voor acht full-deep personen. Geen interne repo-kandidaten lezen vóór alle acht freezes; eigen branch; commit per persoon; pas later reconciliëren.

## ACTIEVE TAAK 3 — AOAY-FULL-LOCATION-ATLAS-001
Actuele STATUS: `SUBSTANTIELE_EERSTE_OOGST__NIET_SATURATED__WACHT_OP_INDIA`.
- eerste ronde: 1.359 occurrence-records; 123 genormaliseerde plaatsen; 30 `AOAY_FOUND_BUT_MISSING_FROM_REPO`; Kashmir nieuw signaal.
- `AOAY_LOCATION_SWEEP_SATURATED: NEE`.
- duizenden kandidaat-tokentypes unresolved; occurrence-level verification nog niet compleet.

**NEXT_ACTION AOAY:** niet afsluiten. Vervolgronde tot echte saturation/blocker met detector-verdieping + occurrence-verificatie. Eerst huidige personenlaag respecteren.

## ACTIEVE TAAK 4 — YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001
Status: `RESULT_KLAAR__TWEE_SITES_ONDERSCHEIDEN__WACHT_OP_INDIA`.
- Ranchi Vidyalaya-tuin = bronmatig zekerste fotosessie, exact bezoekbaar.
- Bhowanipur/Calcutta = historische ontmoeting met Bholanath aanwezig, maar exact huis/adres nog niet bewezen.
- open: Gurupriya Devi-dagboek/OCR + visuele fotoinspectie om Bholanath-foto exact toe te wijzen.

## ACTIEVE/OPEN TAAK 5 — KUMAON-V2-RESWEEP-001
079–081 beschermd. Overige kandidaten tijdelijk; identity/reconciliatie nog open. Nieuwe landelijke METHOD_V2/atlaslagen moeten vóór choice-ready eindstatus over Kumaon worden gekruist.

## ARUNACHALA / TIRUVANNAMALAI
`decisions/ARUNACHALA_TIRUVANNAMALAI_A_ANCHOR_2026-08-18.md` = LOCKED_BY_MARK A-anker, nog geen route/nachten.
Yogananda-Ramana direct bewijs + film-sublocatie staat in `research/YOGANANDA_RAMANA_ARUNACHALA_POST_FREEZE_NOTE_2026-08-18.md`.
Niet verwarren: film-scène exact op bank ten noorden van Old Hall; volledige conversatie exact daar nog niet bewezen.

## AFGEROND
- VARANASI: 001–040 beoordeeld/beschermd; 041–045 alleen op Marks initiatief.
- BODH GAYA: 046–078 verwerkt; keuzes beschermd; geen nieuwe Bodh Gaya-PDF.
- GAYA AIRPORT → BODH GAYA corridor: `DOUBLE_SWEEP_COMPLETED_RECONCILED`; 0 nieuwe locaties.

## REGIOPRIORITEIT
Na huidige landelijke atlas/QA-stroom:
1. Tiruvannamalai / Arunachala.
2. Kolkata / Serampore.
Rajgir/Nalanda niet actief als volgende regio.

## STARTZIN NIEUWE CHAT
`Neem de INDIA-regie over als INDIA7. Gebruik GitHub onmiddellijk als primaire waarheid. Lees eerst de GEHELE tekstuele repository op branch claude/werk-je-nu-of-niet-oa10y7 volgens README.md. Lees daarna governance/INDIA7_BOOTSTRAP_DELTA_2026-08-18.md en handoffs/INDIA6_TO_INDIA7_2026-08-18.md opnieuw, inventariseer PR #23, PR #24 en branch agent/chatgpt-top11-parallel-sweep, en lees hun nieuwste states. Controleer als eerste of CCI_RESULT 087R inmiddels binnen is. Respecteer de blindheid van nog onafgeronde external freezes en start geen regionale/cluster-sweep voordat de nationale persoonslaag dit toestaat. Handel daarna direct de nieuwste next_allowed_step af zonder mij de geschiedenis opnieuw te laten uitleggen.`

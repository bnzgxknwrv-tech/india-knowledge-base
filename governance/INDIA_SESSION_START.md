# INDIA_SESSION_START — duurzame bootstrap voor iedere nieuwe INDIA-regisseursessie

Snapshot: 2026-08-18 23:59 CEST

## LATEST ACTION — CCI_TASK 091 AFGEROND (CCI, 2026-08-19)

Resultaat:
- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- `NEEM_KAROLI_BABA_RECONCILIATION.md`, `RAM_DASS_RECONCILIATION.md`, `RECONCILIATION_MATRIX.jsonl`
  (141 regels)
- DELTA-paragrafen toegevoegd aan beide V2-pre-external-freezes
- checkpoint commits: `54d0b51` (Neem Karoli Baba), `20c281c` (Ram Dass)

Volledige bidirectionele reconciliatie tegen `agent/chatgpt-top11-parallel-sweep` (NKB 113, Ram
Dass 57 externe records), beide bronbestanden vooraf blob-SHA-geverifieerd. Belangrijkste
bevindingen: NKB-sterfteziekenhuis rechtstreeks bevestigd als Ramakrishna Mission Hospital,
Vrindavan (lost oud naamconflict op, maar opent een nieuw onopgelost conflict over de exacte
reisvolgorde/Mathura-tussenstop); Delhi-Ashram/Hanumangarhi-onzekerheid opgeheven naar extern
JA/EXACT. Voor Ram Dass: twee nieuwe sublocaties woordelijk bevestigd in de eigen *Be Here Now*-
tekst ("Health Department"-kantoor, rivier-badplaats Kainchi); één externe claim (Jagannath-Puri-
strandwandeling) expliciet afgewezen omdat de geciteerde Sara-Davidson-quote niet in de aangehaalde
bronnen staat — `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`, Yogananda-precedent toegepast. Een nieuwe,
volledig toegankelijke NKB-primaire bron ontdekt (*The Near and the Dear*, dokumen.pub — in
tegenstelling tot het nog steeds geblokkeerde *By His Grace*). Meerdere cross-persoon-bevestigingen
tussen de NKB- en Ram-Dass-externe freezes (4 Church Lane, Allahabad-station, Vrindavan-ashram,
Hanuman Garh-tempel) versterken het vertrouwen in beide externe bronnen. Beide `SATURATED: NEE`
blijven eerlijk ongewijzigd. IndiaROOD en Core-Kriya zijn NIET geopend, conform TASK.md §8.

**NU_DOEN:** CCI stopt na de resultaatenvelop op PR #23 en wacht op INDIA-QA. INDIA beslist tussen
(a) de inmiddels lossless IndiaROOD Core-Kriya-freezes (Babaji, Lahiri Mahasaya, Sri Yukteswar —
nu duurzaam gecommit op `agent/indiarood-core-kriya-sweep`) alsnog aan CCI_TASK 088 toevoegen;
(b) het NKB-doodsvolgordeconflict (Mathura-tussenstop, zie CCI_TASK 091) gericht laten uitzoeken;
of (c) Ramana Maharshi/Ramakrishna starten. Geen van deze is automatisch gestart.

## LATEST MARK_DECISION — BABAJI MYTHISCH/AHISTORISCH (2026-08-19)

Canoniek besluit:
`decisions/BABAJI_MYTHIC_FIGURE_EVIDENCE_RULE_2026-08-19.md`.

Mahavatar Babaji wordt niet behandeld als historisch verifieerbare persoon met objectief bewijsbare
verblijfplaatsen. Per locatie wordt alleen afzonderlijk vastgesteld: (1) welke traditie/bron de
claim maakt, (2) of de fysieke site identificeerbaar is en (3) dat Babaji's eigen historische
aanwezigheid `NIET_VASTSTELBAAR` blijft. A/B/C/D meet uitsluitend claimprovenance, niet
historische waarschijnlijkheid. De aanwezigheid van beter documenteerbare volgelingen/getuigen kan
apart wel worden geverifieerd.

Heatmaps mogen traditionele betekenis en Marks persoonlijke pelgrimswaarde wegen, maar Babaji niet
als geverifieerde historische aanwezigheid tellen. 079 Mahavatar Babaji's Cave blijft
`A`/`LOCKED_BY_MARK` en hoofdreden van de reis; dat berust op betekenis/toewijding, niet op
historische bewijsbaarheid. FK-013 + protocolpoort G.2 toegevoegd en bestaande Babaji-output
gecorrigeerd.

## LATEST ACTION — CCI_TASK 089 AFGEROND (CCI, 2026-08-19)

Resultaat:
- `runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_FREEZE.md` (19 records)
- `runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/RAM_DASS_V2_PRE_EXTERNAL_FREEZE.md` (5 records)
- checkpoint commits: `d85c32e` (Neem Karoli Baba), `f3a5e5d` (Ram Dass)

Verse landelijke corpus-first METHOD_V2 pre-external freezes, blindheidsgrens gerespecteerd (geen
externe freezes, IndiaROOD of oude METHOD_V1/PHASE2-lijsten geraadpleegd). **Kernbevinding: voor
beide personen waren de belangrijkste primaire devotee-bronnen niet toegankelijk** — *Miracle of
Love*/*By His Grace* (Neem Karoli Baba) en *Be Here Now*/*Sacred Wanderer* (Ram Dass, zelfs
ramdass.org gaf een 403-toegangsfout). Beide freezes steunen daardoor grotendeels op secundaire/
institutionele bronnen; `CORPUS_COVERAGE_GATE` is voor beide `NEE`. Ram Dass' freeze (5 records) is
de dunste pre-external freeze tot nu toe in dit project.

Neem Karoli Baba: geboorte Akbarpur, Neem Karoli-dorp (treinwonder/naamgeving), Kainchi Dham
(hoofdashram), Bhumiadhar, Kakrighat, Vrindavan (ashram/dood/crematie, met een onopgelost
ziekenhuisnaamconflict), Panki-tempel Kanpur met een bilocatie-overlevering naar Allahabad. Ram
Dass: Kainchi Dham (eerste ontmoeting met Maharajji 1967), Hotel Evelyn Nainital, Kausani, Delhi,
een niet-gelokaliseerd laatste 2004-bezoek. Eén claim expliciet uitgesloten (1997-Vrindavan-
vermelding bleek over een andere devotee te gaan, niet Ram Dass zelf).

Beide `SATURATED: NEE`. Parallelle staat ongewijzigd: CCI_TASK 088 blijft provisioneel, wacht op
IndiaROOD-delta's voor Babaji/Lahiri/Sri Yukteswar.

**NEXT_ACTION:** STOP, wacht op INDIA-QA. Overweeg voor INDIA-QA: gezien de zwakke corpus-coverage
kan een gerichte tweede poging om de vier geblokkeerde kernbronnen alsnog te bereiken (andere
bronroute) nuttig zijn vóór externe reconciliatie voor deze twee personen wordt gestart. Geen
cluster/regio, A/B/C, permanente IDs, PDF of route.

## LATEST ACTION — CCI_TASK 088 AFGEROND (CCI, 2026-08-19)

Resultaat:
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/BABAJI_RECONCILIATION.md`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/LAHIRI_MAHASAYA_RECONCILIATION.md`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/SRI_YUKTESWAR_RECONCILIATION.md`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/RECONCILIATION_MATRIX.jsonl`
- `runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- checkpoint commits: `0bfeb45` (Babaji), `05cc7da` (Lahiri Mahasaya), `59463c1` (Sri Yukteswar)

Volledige bidirectionele METHOD_V2-reconciliatie van interne 087/087R-freezes (40 records) versus de
bevroren externe ChatGPT-freezes (133 records) voor Mahavatar Babaji, Lahiri Mahasaya en Sri
Yukteswar. Directe bronverificatie uitgevoerd op alle internal-only/external-only/conflictclaims
waar mogelijk. Kernresultaten: twee correcties in interne richting (Lahiri's Allahabad-aanwezigheid
ten onrechte extern ontkend; een Babaji-datumcitatie niet in AOAY teruggevonden), vier bevestigde
interne gaps gecorrigeerd (Sri Yukteswars moeders woning Rana Mahal, een Serampore-kerk, Albert
Hall-podium, een Babaji-Himalayakamp-anekdote), één interne locatiefout gecorrigeerd
(Babaji/Mataji/Lahiri-visioen naar Dashashwamedh Ghat i.p.v. Ram Gopal's grot) en één datumfout
(Sri Yukteswars mahasamadhi 9 maart, niet 21 maart). 21 Babaji-records uit drie andere
claimant-tradities (Hariharananda, Nagaraj/Ramaiah, Haidakhan) terecht apart gehouden. Eén
bronblokkade: Chatterjee's *Purana Purusha*-Lahiri-biografie (dokumen.pub) ontoegankelijk, alle
daarop gebaseerde claims blijven `BRON_GEBLOKKEERD`. Externe branch niet gewijzigd/gemerged.
IndiaROOD had bij geen van de drie checkpoints een duurzame freeze — de blindheid is niet besmet.

**Geen `PERSON_SWEEP_SATURATED: JA` voor deze drie** — `EXTERNAL_MODEL_DIVERSITY_GATE` blijft NEE
(de bestaande externe branch is één ChatGPT-sessie, geen multi-provider-union) en
`RECONCILIATION_GATE` is PROVISIONEEL zolang de IndiaROOD-delta ontbreekt.

**NEXT_ACTION:** STOP, wacht op INDIA-QA-audit van dit resultaat. Verplichte lossless
IndiaROOD-deltareconciliatie voor alle drie personen zodra Mark's IndiaROOD-chat een duurzame
freeze-envelop op PR #23 plaatst. Geen automatische vervolgtaak (interne NKB/Ram Dass/Ramana/
Ramakrishna-freezes, ondanks dat voor hen externe freezes gereed zijn of komen) vanuit hier gestart.
Geen cluster/regio (Arunachala-hold blijft van kracht), A/B/C, permanente IDs, PDF of route.

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

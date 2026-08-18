# INDIA_SESSION_START — duurzame bootstrap voor iedere nieuwe INDIA-regisseursessie

Snapshot: 2026-08-16

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
Actuele STATUS: `ANANDAMAYI_EXTERNAL_UNION_INGESTED__INDIA_SOURCE_FIRST_PASS_COMPLETE__RECONCILIATION_NEXT`.

Bestanden:
- `TASK.md`
- `STATUS.md`
- `EXTERNAL_UNION_INPUT.md` — Marks externe multi-AI union: 156 Anandamayi-masterlocaties.
- `INDIA_SOURCE_FIRST_SWEEP_ANANDAMAYI.md` — INDIA source-first scan officiële/lineage corpus.
- `BENCHMARK_RESULT.md` — voorlopige driehoeksconclusie.

### Harde bevindingen
1. CCI's Anandamayi-set (~23) is aantoonbaar zwaar incompleet.
2. Externe multi-AI union (156) heeft echte waarde: onafhankelijke AI's vinden reële long-tail host-/reislocaties die CCI mist.
3. Externe union is zelf óók aantoonbaar incompleet: source-first scan van officiële Life History 1896–1982 + Sangha-biografie vond opnieuw vele afzonderlijke sites die niet in de 156-union staan.
4. Sommige externe claims zijn fout/overmerged en moeten rechtstreeks worden geverifieerd; consensus is geen bewijs.

### METHOD_V2 richting
Primaire volgorde wordt:
`CORPUS INVENTORY -> LOSSLESS CORPUS OCCURRENCE EXTRACTION -> EVENT/PLACE NORMALIZATION -> HOST/NETWORK GRAPH -> WEB DISCOVERY -> INDIA INDEPENDENT METHOD PASS -> EXTERNAL MULTI-AI ADVERSARIAL UNION -> DIRECT VERIFICATION/RECONCILIATION -> SATURATION`.

`PERSON_SWEEP_SATURATED` mag pas na aantoonbare corpuscoverage, hostgraph, discovery en detectorreconciliatie; niet meer na alleen zoekcategorieën afvinken.

### Beslissen of externe AI voor ALLE 11 nodig blijft
Anandamayi is inmiddels door iedereen besmet met elkaars data en kan geen zuivere prospectieve blindtest meer zijn. Gebruik haar voor methodebouw.

Daarna **Paramahansa Yogananda als prospectieve control-test**:
1. CCI + INDIA voeren eerst METHOD_V2 source-first uit en freezen hun atlas vóór externe input.
2. Dan laat Mark meerdere externe AI's blanco hetzelfde onderzoek doen.
3. External-only claims rechtstreeks verifiëren.
4. Als externe AI betekenisvolle echte extra's houdt => externe multi-AI verplicht voor alle Top-11.
5. Als verbeterde CCI+INDIA METHOD_V2 de geverifieerde externe union volledig reproduceert => externe AI kan terug naar periodieke/adversarial audit.

**Status per 2026-08-16 (CCI_TASK 084+085 afgerond)**: drieweg-Anandamayi-reconciliatie
onafhankelijk geauditeerd (`RECONCILIATION_CCI_084.md`), `METHOD_V2.md` geformaliseerd, en
Yogananda source-first V2 tweemaal gefreezed — eerst `YOGANANDA_V2_FREEZE.md`, daarna een
pre-external completion-pass in `YOGANANDA_V2_PRE_EXTERNAL_FINAL_FREEZE.md`
(freeze-commit `cd0ff2b159900015fcdc3d69617850efc32bc550`,
`YOGANANDA_V2_PRE_EXTERNAL_SATURATED: NEE`, gates + hiaten expliciet vastgelegd).

**Status per 2026-08-18 (CCI_TASK 086 afgerond)**: de prospectieve externe Yogananda-control
(PR #24, head `e8c7ef68`, 114-record atlas van Grok/Gemini/DeepSeek/Copilot/AI-5) is ontvangen,
bevroren (`YOGANANDA_EXTERNAL_UNION_FREEZE.md`) en gereconcilieerd tegen de interne freeze
(`YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md`). Acht getoetste externe kandidaten `VERIFIED_TRUE`
(o.a. Pranabananda-residentie Benares, Sri Yukteswars Rana Mahal-huis, Giri Bala/Biur,
Keshabananda-ashram Brindaban, Kumbh Mela 1936-aanwezigheid). Vier zelf-gerapporteerde externe
identiteitsconflicten opgelost (Anandamayi Ma = Bhowanipur/Ranchi niet Varanasi; Gandhi = Wardha
niet Sabarmati; Ramana = Tiruvannamalai niet "Bangalore"; Ellora/Ajanta/Hyderabad geen bewezen
bezoek). CCI vond bovendien zelf één plek die alle vijf externe AI's misten: de **Regent Hotel,
Bombay** als werkelijke locatie van het Sri Yukteswar-"resurrection"-visioen (hfst. 43), tegenover
de externe atlas' eigen `ONBEKEND`-label daar.

**Verdict**: `EXTERNAL_MULTI_AI_MANDATORY_FOR_REMAINING_TOP11: JA`. Root cause: CCI's eigen
token-/gazetteerdetector is sterk voor toponiemen, structureel zwakker voor privéadressen die de
brontekst alleen via de bewonersnaam aanduidt — precies waar externe host-netwerkanalyse
meerwaarde had. Tegelijk blijft CCI's eigen directe bronverificatie onmisbaar (Regent Hotel-vondst
die de externe union zelf miste). Juiste architectuur: de volledige METHOD_V2-keten, niet "CCI OF
externe AI".

**NEXT_ACTION BENCHMARK:** wacht op INDIA-QA-audit van het CCI_TASK 086-verdict. Zodra bevestigd,
kan METHOD_V2 + verplichte externe-AI-laag op de overige 9 Top-11-personen worden toegepast, in de
vastgelegde volgorde. **Arunachala-regiosweep-hold blijft van kracht** tot na deze audit. CCI start
geen nieuwe Top-11-persoon en geen Arunachala-sweep totdat INDIA dit expliciet vrijgeeft.

## ACTIEVE TAAK 3 — AOAY-FULL-LOCATION-ATLAS-001
Actuele STATUS: `SUBSTANTIELE_EERSTE_OOGST__NIET_SATURATED__WACHT_OP_INDIA`.
- eerste ronde: 1.359 occurrence-records; 123 genormaliseerde plaatsen; 30 `AOAY_FOUND_BUT_MISSING_FROM_REPO`; Kashmir nieuw signaal.
- `AOAY_LOCATION_SWEEP_SATURATED: NEE`.
- duizenden kandidaat-tokentypes unresolved; occurrence-level verification nog niet compleet.

**NEXT_ACTION AOAY:** niet afsluiten. Vervolgronde tot echte saturation/blocker met detector-verdieping + occurrence-verificatie. Nieuwe PERSON_METHOD_V2-corpuslessen moeten ook hier worden toegepast waar relevant.

## ACTIEVE TAAK 4 — YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001
Status: `RESULT_KLAAR__TWEE_SITES_ONDERSCHEIDEN__WACHT_OP_INDIA`.
- Ranchi Vidyalaya-tuin = bronmatig zekerste fotosessie, exact bezoekbaar.
- Bhowanipur/Calcutta = historische ontmoeting met Bholanath aanwezig, maar exact huis/adres nog niet bewezen.
- open: Gurupriya Devi-dagboek/OCR + visuele fotoinspectie om Bholanath-foto exact toe te wijzen.

## ACTIEVE/OPEN TAAK 5 — KUMAON-V2-RESWEEP-001
079–081 beschermd. Overige kandidaten tijdelijk; identity/reconciliatie nog open. Nieuwe landelijke METHOD_V2/atlaslagen moeten vóór choice-ready eindstatus over Kumaon worden gekruist.

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
`Neem de INDIA-regie over. Lees eerst de GEHELE GitHub-repository inhoudelijk op de actuele werkbranch volgens README.md, inclusief legacy/oud tekstmateriaal, en inventariseer relevante branches/PR's. Lees daarna de actuele governance en alle actieve STATUS/TASK/output-bestanden opnieuw om canon en prioriteit vast te zetten. Controleer PR #23 en recente commits. Handel vervolgens direct de nieuwste NEXT_ACTION af. Vraag mij niet de geschiedenis opnieuw uit te leggen.`

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
Actuele STATUS: `PHASE2_COMPLEET__ALLE_11_TOP11_PERSONEN_SATURATED__WACHT_OP_INDIA`.
- Alle 11 personen: `PERSON_SWEEP_SATURATED: JA` volgens huidige methode.
- Circa 90 atlaspunten in fase 2.
- Sterke nieuwe clusters: Puri/Odisha; Tamil Nadu/Arunachala; West-Bengal-kernregio.
- `REGION_MISS`: Almora/Vivekananda binnen bestaand Kumaon-gebied.
- Geen `MARK_DECISION_CONFLICT`.
- Bestanden: `STATUS.md`, `TASK.md`, `METHOD_V1.md`, `PILOT_RESULT.md`, `SATURATION_RESULT.md`, `PHASE2_RESULT.md`, `PHASE2_SYNTHESIS.md`.

**NEXT_ACTION TOP11:** INDIA voert integrale QA/reconciliatie uit vóór permanente nummering of clusterkeuzes. Geen automatisch nummeren.

## ACTIEVE TAAK 2 — AOAY-FULL-LOCATION-ATLAS-001
Actuele STATUS: `SUBSTANTIELE_EERSTE_OOGST__NIET_SATURATED__WACHT_OP_INDIA`.
- CCI_TASK 082 eerste ronde: 1.359 occurrence-records; 123 genormaliseerde plaatsen; 30 `AOAY_FOUND_BUT_MISSING_FROM_REPO`; sterk nieuw Kashmir-cluster.
- `AOAY_LOCATION_SWEEP_SATURATED: NEE`.
- 6.691 kandidaat-tokentypes nog `UNRESOLVED_BUT_RECORDED`.
- Occurrence-niveau `event_verified_from_AOAY` / physical identity / exact sublocation nog niet ingevuld.

**NEXT_ACTION AOAY:** niet afsluiten. INDIA moet vervolgronde autoriseren tot echte saturation of blocker, met detector-verdieping + occurrence-verificatie; Kashmir is signaal, niet reden om eerst AOAY-completeness los te laten.

## ACTIEVE TAAK 3 — YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001
Mark wil expliciet de historische fysieke plek bezoeken waar de bekende foto('s) van Paramahansa Yogananda met Anandamayi Ma zijn gemaakt.
- CCI_TASK 083 uitgegeven op PR #23.
- Publieke/lineage-bronnen bevestigen: Yogananda ontmoette Anandamayi Ma in december 1935 in Bhowanipur/Bhawanipur, Calcutta; AOAY beschrijft dat C. Richard Wright tijdens die ontmoeting foto's in `the garden` maakte; YSS captiont de bekende foto met Anandamayi Ma + Bholanath + Yogananda als `in Calcutta`.
- Werkhypothese: tuin van het discipelshuis in Bhowanipur. Exact huis/adres/current-site-match nog NIET bewezen.
- Taak moet foto-events scheiden van later Ranchi-bezoek en exact host/huis/tuin/adres/current access onderzoeken.

Bestanden:
- `runs/active/YOGANANDA-ANANDAMAYI-PHOTO-LOCATION-001/TASK.md`
- `.../STATUS.md`

**NEXT_ACTION FOTO:** CCI 083 laten uitvoeren; daarna INDIA audit. Geen permanente ID vóór exact-site QA.

## ACTIEVE/OPEN TAAK 4 — KUMAON-V2-RESWEEP-001
Regionale dubbele sweep + legacy-reconciliatie leverde 079–081 op. Overige Sweep-A/Sweep-B-kandidaten blijven tijdelijk en vereisen clustergewijze identity/reconciliatie.

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

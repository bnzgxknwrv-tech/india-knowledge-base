# INDIA — START HIER

## STOP — VERPLICHTE EERSTE POORT VOOR INDIA10 EN LATER (2026-08-23, task 008)

**Lees vóór ALLES eerst:** `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md`

Dat bestand is nu de hoogste boot-autoriteit. Het vervangt de mechaniek van
"lees letterlijk elke keer de hele repository" (hieronder, sectie "STOP — VERPLICHTE
EERSTE POORT VOOR INDIA9") door een baseline+delta-model: begin bij
`governance/KNOWLEDGE_BASELINE_LATEST.md`, lees vervolgens alleen wat sindsdien
nieuw/gewijzigd is plus de altijd-actuele autoriteitsbestanden (Sectie G van het
protocol), en val terug op een volledige herlezing als de baseline niet valideert
(Sectie C). Dit vervangt uitsluitend de LEESMECHANIEK — het incident, de
AL-BESLIST-regel, de sleep-base-first-regel en de no-deferral-regel hieronder blijven
onverkort van kracht.

## STOP — VERPLICHTE EERSTE POORT VOOR INDIA9 (2026-08-23, historisch — leesmechaniek
hierboven vervangen; onderstaande regels blijven zelf van kracht)

**Lees vóór ALLES eerst:**
`governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`

Deze poort is toegevoegd na een ernstige INDIA8-regiefout op 2026-08-23: recente runs werden wel gelezen, maar oudere nog geldige Mark-canon (A/B/C, cluster-anchors, accommodation locks en legacy-besluiten) werd onvoldoende gereconcilieerd. Daardoor werden reeds beoordeelde plekken opnieuw als keuzes gepresenteerd en bestaande slaapbases onvoldoende gebruikt.

Daarom geldt voortaan vóór ELK inhoudelijk advies:

`GEHELE REPO LEZEN -> ACTUELE CANON RECONCILIËREN -> AL-BESLIST-CHECK PER ITEM -> PAS DAN PRESENTEREN`

En tevens hard:

**Iets wat INDIA NU veilig zelfstandig kan uitvoeren, wordt in DEZELFDE beurt uitgevoerd en duurzaam in GitHub vastgelegd. Nooit bewaren als "volgende stap" als het nu kan.**

---

Dit repository is de duurzame bron van waarheid voor het India-project. Een nieuwe ChatGPT/INDIA-regisseursessie (INDIA7, INDIA8, INDIA9, enz.) moet de oude chat NIET nodig hebben en mag Mark niet vragen de geschiedenis opnieuw uit te leggen.

## Harde bootregel voor iedere nieuwe INDIA-regisseur (historisch, 2026-08-19 — leesmechaniek vervangen door governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md, zie STOP-blok bovenaan)

**LET OP (2026-08-23, task 008): volg de instructie hieronder NIET meer letterlijk.**
Als `governance/KNOWLEDGE_BASELINE_LATEST.md` een geldige baseline oplevert, lees dan
uitsluitend de nieuw/gewijzigde delta + de altijd-actuele autoriteitsbestanden
(`governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md` Sectie G) — niet de volledige repository
opnieuw. Alleen als die baseline-validatie faalt, geldt de onderstaande stap-voor-stap
instructie alsnog als fallback.

**Lees de gehele GitHub-repository voordat je inhoudelijk handelt.** Niet alleen de handoff, niet alleen governance, niet alleen actieve taken.

Praktisch betekent dit:

1. Lees eerst `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` volledig.
2. Haal de volledige recursieve tree van de actuele werkbranch op.
3. Lees vervolgens **alle tekstuele bronbestanden op die werkbranch inhoudelijk**, inclusief governance, actieve runs, oudere runs, registries, decisions, protocollen, methodes, scripts, README/START/HANDOFF-bestanden, research-notities en legacy-projectbestanden. Oude bestanden kunnen fouten bevatten of gedeprecieerd zijn, maar moeten wel gelezen worden zodat een opvolger weet wat er bestond, wat vervangen is en welke Mark-besluiten mogelijk beschermd zijn.
4. Niet-tekstuele/binaire artefacten (PDF's, afbeeldingen, ZIP's) hoeven niet byte-voor-byte gelezen te worden als hun relevante inhoud al in tekstbestanden is vastgelegd. Zodra een actuele taak, decision of audit naar zo'n artefact verwijst als inhoudelijke bron, moet het wel worden geopend/gecontroleerd.
5. Inventariseer daarnaast alle relevante branches en open PR's. Lees in elk geval de actieve werkbranch volledig en inspecteer legacy/andere branches die in de repo of actieve taken worden genoemd. PR #23 moet volledig als relay/index worden gecontroleerd op de nieuwste envelopes; inhoudelijke waarheid blijft in de repo-bestanden.
6. Lees daarna nogmaals de actuele canonieke statebestanden om prioriteit en conflictoplossing vast te zetten:
   - `governance/ACTIVE_STATE.md`
   - `governance/INDIA_SESSION_START.md`
   - `governance/SWEEP_PROTOCOL.md`
   - `governance/SWEEP_ERROR_CLASSES.md`
   - alle `runs/active/*/STATUS.md` + bijbehorende `TASK.md` en genoemde outputbestanden.
7. Scan repo-breed op minimaal:
   - `LOCKED_BY_MARK`
   - `LOCKED_A`
   - `LOCKED_B`
   - `LOCKED_C`
   - `CLUSTER_ANCHOR`
   - `accommodation`
   - `hotel`
   - `MARK_DECISION_CONFLICT`
   - `LAST_GLOBAL_LOCATION_NUMBER`
   - `PDF_STATUS`
   - `next_allowed_step`
   - `PERSON_SWEEP_SATURATED`
   - `AOAY_LOCATION_SWEEP_SATURATED`
   - `DOUBLE_SWEEP_COMPLETED`
8. Controleer de nieuwste commits op de werkbranch en de nieuwste PR #23-enveloppen.
9. Bouw vóór presentatie één actuele canonlaag. Voor reisregie geldt: nieuwste expliciete Mark-beslissing/lock > nieuwste accommodation/base lock > nieuwste clusterbesluit > nieuwste site-A/B/C > centrale all-findings/reconciliatie > actuele governance/handoff > oudere beschermde locks/anchors > oude kandidaat-/overzichtsbestanden.
10. Doe voor ELK item dat aan Mark wordt genoemd eerst de `AL BESLIST?`-check uit de critical boot file. Een bestaand A/B/C/lock wordt nooit opnieuw als nieuwe keuze gepresenteerd.
11. Handel daarna DIRECT de nieuwste uitvoerbare actie af. Mark is geen koerier tussen INDIA en CCI.
12. Vóór ieder finaal antwoord: scan je eigen concept op woorden als `moet nog`, `later`, `volgende stap`, `nog onderzoeken`, `nog bepalen`. Als INDIA dit nu veilig zelf kan doen: NIET verzenden, eerst uitvoeren.

### Waarom echt de hele repo lezen
Dit project heeft meerdere architectuurfasen, oude branches, legacy-besluiten en later ontdekte misses. Alleen een samenvatting lezen kan precies de fouten herhalen die we proberen te voorkomen. De volledige repo is daarom de oriëntatielaag; de statebestanden bepalen daarna wat actueel/canoniek is.

## State-bestanden en onderhoud

- `governance/INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md` = verplichte eerste foutpreventiepoort.
- `governance/INDIA_SESSION_START.md` = compacte, actuele operationele overdracht.
- `governance/ACTIVE_STATE.md` = langere centrale projectstaat/canon.
- `runs/active/<TASK_ID>/STATUS.md` = kortste en meest actuele waarheid per taak.
- `runs/active/<TASK_ID>/TASK.md` = taakcontract.
- PR #23 = korte relay/index, geen vervanging voor repo-inhoud.

**Verplichte onderhoudsregel voor iedere INDIA-regisseur:** update `governance/INDIA_SESSION_START.md` of een expliciete actuele canon-delta in dezelfde werksessie wanneer één van deze dingen verandert: nieuwe taak, taak afgerond/geblokkeerd, nieuwe CCI-opdracht, nieuwe permanente locatie-ID, Mark A/B/C-lock, accommodation/base lock, methode/protocolwijziging, regioprioriteit, foutcorrectie of `NEXT_ACTION`. Update daarnaast altijd het betrokken taak-`STATUS.md`. Laat een opvolger nooit afhankelijk zijn van chatgeheugen.

## Projectdoel

Marks India-reis draait primair om drie orthogonale detectorlagen:

1. **AOAY** — iedere verifieerbare fysieke plek uit of direct verbonden met *Autobiography of a Yogi*, hoe klein ook.
2. **Top-11 persoon-centraal** — per persoon heel India afzoeken naar aantoonbare fysieke touchpoints, inclusief host/gastheer/landgoed/huis-bezoeken.
3. **Regionaal** — per zware regio een onafhankelijke dubbele sweep + reconciliatie; daarnaast alleen zelfstandige spirituele/pelgrimszwaargewichten als bonuslaag.

Top-11, vaste volgorde:
1. Paramahansa Yogananda
2. Mahavatar Babaji
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Ram Dass
6. Neem Karoli Baba
7. Anandamayi Ma
8. Ramakrishna
9. Ramana Maharshi
10. Hariharananda
11. Vivekananda

Geen A/B/C voorspellen namens Mark. Geen PDF zonder expliciet `PDF_GO: JA`.

## Historische snapshot — 2026-08-16

LET OP: onderstaande snapshot is historisch en kan door latere besluiten zijn superseded. Gebruik hem NIET als actuele reiscanon zonder de verplichte canonreconciliatie hierboven.

Repository: `bnzgxknwrv-tech/india-knowledge-base`
Werkbranch destijds: `claude/werk-je-nu-of-niet-oa10y7`
PR: #23 draft; niet mergen zonder expliciete vrijgave van Mark.
Laatste globale permanente locatienummer in die snapshot: **081**.

### Kumaon
`KUMAON-V2-RESWEEP-001` was gedeeltelijk gereconcilieerd.
- 079 Mahavatar Babaji's Cave — A, `LOCKED_BY_MARK`.
- 080 Turiya Niwas — A, `LOCKED_BY_MARK`.
- 081 Bodh Ashram — A, `LOCKED_BY_MARK`.

### Reeds inhoudelijk afgerond in die snapshot
- Varanasi: 001–040 beoordeeld/beschermd; latere deltas bestaan.
- Bodh Gaya: 046–078 verwerkt; keuzes beschermd; geen nieuwe Bodh Gaya-PDF.
- Gaya Airport → Bodh Gaya corridor: dubbele sweep + reconciliatie, 0 nieuwe locaties.

## Exacte startzin voor een nieuwe chat

Gebruik bij voorkeur de actuele startvraag die INDIA8 op 2026-08-23 aan Mark heeft gegeven. Minimaal moet iedere startvraag eisen:

> Neem de INDIA-regie over. Open eerst README.md en volg de verplichte `INDIA_REGIE_CRITICAL_BOOT_AND_NO_DEFERRAL_2026-08-23.md`-poort. Lees daarna de gehele tekstuele repository en relevante branches/legacy-canon, reconcileer alle bestaande Mark A/B/C-, cluster-, accommodation- en base-locks vóór je iets presenteert, controleer per item of het al besloten is, en voer iedere actie die je nu veilig zelfstandig kunt doen meteen uit en commit die; laat niets als 'volgende stap' liggen wanneer het nu kan.

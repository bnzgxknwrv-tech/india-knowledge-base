# INDIA — START HIER

Dit repository is de duurzame bron van waarheid voor het India-project. Een nieuwe ChatGPT/INDIA-regisseursessie (INDIA7, INDIAN, enz.) moet de oude chat NIET nodig hebben en mag Mark niet vragen de geschiedenis opnieuw uit te leggen.

## Harde bootregel voor iedere nieuwe INDIA-regisseur

Voer vóór inhoudelijk handelen altijd een volledige repository-orientatie uit op de actuele werkbranch.

1. Haal de **volledige recursieve repository-tree** op. Inspecteer alle mappen en bestandsnamen; ga nooit uit van één handoff-bestand als enige waarheid.
2. Lees daarna volledig:
   - `README.md` (dit bestand);
   - alle actuele bestanden onder `governance/`, minimaal `ACTIVE_STATE.md`, `INDIA_SESSION_START.md`, `SWEEP_PROTOCOL.md`, `SWEEP_ERROR_CLASSES.md` en relevante validators;
   - alle `runs/active/*/STATUS.md` en bijbehorende `TASK.md`;
   - voor elke taak waarvan `STATUS.md` zegt dat een resultaat klaar is voor INDIA: het relevante `RESULT.md`, `RECONCILIATION.md`, `METHOD*.md`, `SATURATION*.md` of andere genoemde output;
   - alle actuele decision/registry-bestanden die door de actieve taak worden genoemd.
3. Scan vervolgens repo-breed op de state-tokens:
   - `LOCKED_BY_MARK`
   - `MARK_DECISION_CONFLICT`
   - `LAST_GLOBAL_LOCATION_NUMBER`
   - `PDF_STATUS`
   - `next_allowed_step`
   - `PERSON_SWEEP_SATURATED`
   - `AOAY_LOCATION_SWEEP_SATURATED`
   - `DOUBLE_SWEEP_COMPLETED`
4. Controleer PR #23 op **nieuwste korte relay-enveloppen** en controleer de nieuwste commits op de werkbranch. PR #23 is index/relay, niet de volledige waarheid.
5. Controleer of er een nieuwere `STATUS.md` bestaat dan de snapshot in `ACTIVE_STATE.md` of `INDIA_SESSION_START.md`. Bij verschil geldt voor taakspecifieke voortgang altijd: **actuele taak-STATUS > INDIA_SESSION_START > ACTIVE_STATE > oude chat/legacy**.
6. Lees legacy/archiefmateriaal wanneer een actieve taak of reconciliatie ernaar verwijst. Legacy mag nooit stil actuele canon overschrijven; alleen via expliciete reconciliatie.
7. Handel daarna DIRECT de nieuwste `next_allowed_step` af. Mark is geen koerier tussen INDIA en CCI.

### Wat “gehele GitHub lezen” hier praktisch betekent
Een opvolger moet altijd de volledige tree inventariseren, alle governance/current-state-bestanden en alle actieve taakbestanden inhoudelijk lezen, en de rest van de repo repo-breed doorzoeken op state/decision-tokens en verwijzingen. Historische PDF-binaries hoeven niet opnieuw gerenderd te worden tenzij een actuele taak ze expliciet nodig heeft. Geen onbekende map of actieve run mag worden overgeslagen omdat een handoff-samenvatting hem niet noemt.

## State-bestanden en onderhoud

- `governance/INDIA_SESSION_START.md` = compacte, actuele operationele overdracht.
- `governance/ACTIVE_STATE.md` = langere centrale projectstaat/canon.
- `runs/active/<TASK_ID>/STATUS.md` = kortste en meest actuele waarheid per taak.
- `runs/active/<TASK_ID>/TASK.md` = taakcontract.
- PR #23 = korte relay/index, geen transcript.

**Verplichte onderhoudsregel voor iedere INDIA-regisseur:** update `governance/INDIA_SESSION_START.md` in dezelfde werksessie wanneer één van deze dingen verandert: nieuwe taak, taak afgerond/geblokkeerd, nieuwe CCI-opdracht, nieuwe permanente locatie-ID, Mark A/B/C-lock, methode/protocolwijziging, regioprioriteit, of `NEXT_ACTION`. Update daarnaast altijd het betrokken taak-`STATUS.md`. Laat een opvolger nooit afhankelijk zijn van chatgeheugen.

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

## ACTUELE SNAPSHOT — 2026-08-16

Repository: `bnzgxknwrv-tech/india-knowledge-base`
Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR: #23 draft; niet mergen zonder expliciete vrijgave van Mark.
Laatste globale permanente locatienummer: **081**.

### Kumaon
`KUMAON-V2-RESWEEP-001` is gedeeltelijk gereconcilieerd.
- 079 Mahavatar Babaji's Cave — A, `LOCKED_BY_MARK`.
- 080 Turiya Niwas — A, `LOCKED_BY_MARK`.
- 081 Bodh Ashram — A, `LOCKED_BY_MARK`.
- Overige nieuwe Kumaon-vondsten blijven tijdelijke IDs tot clustergewijze identity/reconciliatie.

### Top-11 landelijke megasweep
`TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001`.
- Pilot Anandamayi Ma + Neem Karoli Baba: beide `PERSON_SWEEP_SATURATED: JA`.
- Methode is bevroren in `METHOD_V1.md`; host-/gastheer-as is verplicht vanaf het begin.
- Fase 2 voor overige 9 is geautoriseerd via CCI_TASK 081.
- Actuele STATUS bij deze snapshot: `PHASE2_IN_PROGRESS__PERSOON_1_VAN_9_GEREED`.
- Mahavatar Babaji (persoon 1/9) is reeds `PERSON_SWEEP_SATURATED: JA`; o.a. Allahabad/Kumbh Mela 1894 kwam als ontbrekend Babaji/Sri Yukteswar-signaal boven.
- CCI gaat autonoom verder met Lahiri Mahasaya, Yogananda, Ram Dass, Sri Yukteswar, Hariharananda, Vivekananda, Ramakrishna, Ramana Maharshi tenzij een blocker/conflict ontstaat.

### AOAY volledige locatie-atlas
`AOAY-FULL-LOCATION-ATLAS-001`.
- Mark wil het **hele boek andersom**: boek → iedere locatievermelding, zonder relevantiefilter tijdens extractie.
- Inclusief huizen, kamers, straten, stations, steden, dorpen, landen, ashrams, tempels, scholen, bergen, rivieren, grotten, transit, voetnoten en fotobijschriften; buitenlandse/mythische/onzekere vermeldingen worden bewaard en gelabeld.
- Actuele STATUS bij deze snapshot: `READY_FOR_CCI_FULL_BOOK_SWEEP`.
- CCI_TASK 082 is uitgegeven: hoofdstuk-voor-hoofdstuk occurrence-log + genormaliseerde place-atlas + coverage-matrix; stop pas bij `AOAY_LOCATION_SWEEP_SATURATED: JA` of echte blocker.

### Reeds inhoudelijk afgerond
- Varanasi: 001–040 beoordeeld/beschermd; 041–045 alleen op Marks initiatief.
- Bodh Gaya: 046–078 verwerkt; keuzes beschermd; geen nieuwe Bodh Gaya-PDF.
- Gaya Airport → Bodh Gaya corridor: dubbele sweep + reconciliatie, 0 nieuwe locaties.

### Volgende zware regio's ná de huidige Kumaon/atlas-werkstroom
1. Tiruvannamalai / Arunachala.
2. Kolkata / Serampore.
Rajgir/Nalanda staat voorlopig niet in beeld als actieve volgende regio.

## Exacte startzin voor een nieuwe chat

Mark kan in een nieuwe chat alleen dit sturen:

> Neem de INDIA-regie over. Lees eerst de volledige GitHub-repository volgens README.md op de actuele werkbranch, daarna governance/INDIA_SESSION_START.md en alle actieve STATUS/TASK-bestanden. Controleer PR #23 en recente commits. Handel vervolgens direct de nieuwste NEXT_ACTION af. Vraag mij niet de geschiedenis opnieuw uit te leggen.

# INDIA — START HIER

Dit repository is de duurzame bron van waarheid voor het India-project. Een nieuwe ChatGPT/INDIA-regisseursessie (INDIA7, INDIAN, enz.) moet de oude chat NIET nodig hebben en mag Mark niet vragen de geschiedenis opnieuw uit te leggen.

## Harde bootregel voor iedere nieuwe INDIA-regisseur

**Lees de gehele GitHub-repository voordat je inhoudelijk handelt.** Niet alleen de handoff, niet alleen governance, niet alleen actieve taken.

Praktisch betekent dit:

1. Haal de volledige recursieve tree van de actuele werkbranch op.
2. Lees vervolgens **alle tekstuele bronbestanden op die werkbranch inhoudelijk**, inclusief governance, actieve runs, oudere runs, registries, decisions, protocollen, methodes, scripts, README/START/HANDOFF-bestanden, research-notities en legacy-projectbestanden. Oude bestanden kunnen fouten bevatten of gedeprecieerd zijn, maar moeten wel gelezen worden zodat een opvolger weet wat er bestond, wat vervangen is en welke Mark-besluiten mogelijk beschermd zijn.
3. Niet-tekstuele/binaire artefacten (PDF's, afbeeldingen, ZIP's) hoeven niet byte-voor-byte gelezen te worden als hun relevante inhoud al in tekstbestanden is vastgelegd. Zodra een actuele taak, decision of audit naar zo'n artefact verwijst als inhoudelijke bron, moet het wel worden geopend/gecontroleerd.
4. Inventariseer daarnaast alle relevante branches en open PR's. Lees in elk geval de actieve werkbranch volledig en inspecteer legacy/andere branches die in de repo of actieve taken worden genoemd. PR #23 moet volledig als relay/index worden gecontroleerd op de nieuwste envelopes; inhoudelijke waarheid blijft in de repo-bestanden.
5. Lees daarna nogmaals de actuele canonieke statebestanden om prioriteit en conflictoplossing vast te zetten:
   - `governance/ACTIVE_STATE.md`
   - `governance/INDIA_SESSION_START.md`
   - `governance/SWEEP_PROTOCOL.md`
   - `governance/SWEEP_ERROR_CLASSES.md`
   - alle `runs/active/*/STATUS.md` + bijbehorende `TASK.md` en genoemde outputbestanden.
6. Scan repo-breed op minimaal:
   - `LOCKED_BY_MARK`
   - `MARK_DECISION_CONFLICT`
   - `LAST_GLOBAL_LOCATION_NUMBER`
   - `PDF_STATUS`
   - `next_allowed_step`
   - `PERSON_SWEEP_SATURATED`
   - `AOAY_LOCATION_SWEEP_SATURATED`
   - `DOUBLE_SWEEP_COMPLETED`
7. Controleer de nieuwste commits op de werkbranch en de nieuwste PR #23-enveloppen.
8. Bij tegenstrijdige state geldt voor actuele taakspecifieke voortgang: **actuele taak-STATUS > INDIA_SESSION_START > ACTIVE_STATE > oudere/legacy-bestanden > oude chat**. Maar oudere bestanden mogen niet worden genegeerd wanneer ze beschermde Mark-besluiten, eerdere evidence of een expliciete reconciliatiebron bevatten.
9. Handel daarna DIRECT de nieuwste `next_allowed_step` af. Mark is geen koerier tussen INDIA en CCI.

### Waarom echt de hele repo lezen
Dit project heeft meerdere architectuurfasen, oude branches, legacy-besluiten en later ontdekte misses. Alleen een samenvatting lezen kan precies de fouten herhalen die we proberen te voorkomen. De volledige repo is daarom de oriëntatielaag; de statebestanden bepalen daarna wat actueel/canoniek is.

## State-bestanden en onderhoud

- `governance/INDIA_SESSION_START.md` = compacte, actuele operationele overdracht.
- `governance/ACTIVE_STATE.md` = langere centrale projectstaat/canon.
- `runs/active/<TASK_ID>/STATUS.md` = kortste en meest actuele waarheid per taak.
- `runs/active/<TASK_ID>/TASK.md` = taakcontract.
- PR #23 = korte relay/index, geen vervanging voor repo-inhoud.

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

> Neem de INDIA-regie over. Lees eerst de **gehele GitHub-repository inhoudelijk** op de actuele werkbranch volgens README.md, inclusief legacy/oud tekstmateriaal, en inventariseer relevante branches/PR's. Lees daarna de actuele governance en alle actieve STATUS/TASK/output-bestanden opnieuw om canon en prioriteit vast te zetten. Controleer PR #23 en recente commits. Handel vervolgens direct de nieuwste NEXT_ACTION af. Vraag mij niet de geschiedenis opnieuw uit te leggen.
# INDIA_SESSION_START — duurzame bootstrap voor iedere nieuwe INDIA-regisseursessie

Snapshot: 2026-08-16

## Doel
Dit bestand maakt de huidige ChatGPT/INDIA-regisseur volledig vervangbaar. Sessienamen zoals INDIA6/INDIA7/INDIAN zijn alleen labels. Een nieuwe sessie moet zonder oude chat exact kunnen vaststellen waar het project staat en direct verder handelen.

## HARD RULE — EERST DE GEHELE GITHUB LEZEN
Een nieuwe INDIA-regisseur leest vóór inhoudelijk handelen de **gehele tekstuele repository op de actuele werkbranch inhoudelijk**. Niet alleen dit bestand, niet alleen ACTIVE_STATE, niet alleen actieve taken. Eerst de volledige recursive tree ophalen, daarna alle tekstbestanden lezen: governance, runs, oude runs, legacy, registries, decisions, protocollen, scripts, research, handoffs, methodes en overige projectbestanden. Binaire artefacten hoeven alleen inhoudelijk geopend te worden wanneer een actuele taak/decision/audit ze als bron nodig heeft. Relevante andere branches en open PR's moeten worden geïnventariseerd; legacy-branches die door actuele state/reconciliatie worden genoemd moeten worden gelezen. Daarna worden de actuele statebestanden opnieuw gelezen om vast te stellen wat canoniek en actueel is.

Waarom: dit project heeft aantoonbaar oudere Mark-besluiten en belangrijke locaties in legacy-bestanden gehad die nieuwe regionale sweeps misten. Een samenvatting alleen is daarom onvoldoende als veiligheidslaag.

## VERPLICHTE BOOTVOLGORDE

1. Lees root `README.md`.
2. Haal de **volledige recursieve tree** van de actuele werkbranch op.
3. Lees **alle tekstuele bestanden op die branch inhoudelijk**. Oude/gedeprecieerde bestanden mogen niet als actuele canon worden behandeld, maar wel worden overgeslagen is verboden: ze kunnen beschermde besluiten, evidence, historische fouten of reconciliatie-input bevatten.
4. Inventariseer relevante branches en open PR's; lees legacy-branches wanneer huidige state/taken ernaar verwijzen.
5. Lees daarna opnieuw volledig `governance/ACTIVE_STATE.md`, `governance/SWEEP_PROTOCOL.md`, `governance/SWEEP_ERROR_CLASSES.md` en dit bestand.
6. Lees alle `runs/active/*/STATUS.md`, bijbehorende `TASK.md` en alle resultaten/methoden/reconciliaties waarnaar de actuele STATUS verwijst.
7. Scan repo-breed op `LOCKED_BY_MARK`, `MARK_DECISION_CONFLICT`, `LAST_GLOBAL_LOCATION_NUMBER`, `PDF_STATUS`, `next_allowed_step`, `PERSON_SWEEP_SATURATED`, `AOAY_LOCATION_SWEEP_SATURATED`, `DOUBLE_SWEEP_COMPLETED`.
8. Controleer de nieuwste commits op de werkbranch en de nieuwste korte relay-enveloppen op PR #23.
9. Bij stateverschil geldt voor taakspecifieke voortgang: **actuele taak-STATUS > dit bestand > ACTIVE_STATE > legacy/oud > oude chat**. Legacy blijft wel verplicht als expliciete reconciliatiebron of drager van beschermde Mark-besluiten.
10. Handel daarna meteen de nieuwste `next_allowed_step` af. Vraag Mark niet de projectgeschiedenis opnieuw te vertellen en gebruik hem niet als koerier tussen INDIA en CCI.

GitHub is de duurzame bron van waarheid. Oude chatgeschiedenis is niet nodig voor voortzetting.

## Onderhoudsregel — hard
Iedere INDIA-regisseur moet dit bestand in dezelfde werksessie bijwerken wanneer één van deze dingen verandert:
- nieuwe taak / nieuwe CCI_TASK;
- taakstatus of NEXT_ACTION;
- nieuwe permanente locatie-ID;
- Mark A/B/C-lock of conflict;
- methode/protocol;
- regioprioriteit;
- belangrijke researchlaag die klaar/start/geblokkeerd raakt.

Update daarnaast altijd het betrokken taak-`STATUS.md`. Een chat mag nooit de enige plek zijn waar actuele state staat.

## Repository / relay
- Repo: `bnzgxknwrv-tech/india-knowledge-base`
- Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
- PR #23: draft; NIET mergen zonder expliciete Mark-vrijgave.
- PR #23 is korte relay/index; lange inhoud hoort in `runs/active/<TASK_ID>/`.
- Root `README.md` bevat het volledige successor-stappenplan.

## Projectdoel van Mark
De reis draait primair om drie orthogonale detectorlagen:

1. **AOAY volledig** — iedere verifieerbare fysieke plek uit of direct verbonden met *Autobiography of a Yogi*, hoe klein of praktisch onbeduidend ook.
2. **Top-11 persoon-centraal** — per persoon heel India afzoeken naar iedere betekenisvolle, aantoonbare fysieke link, inclusief host/gastheer/huis/landgoed/verblijf bij anderen.
3. **Regionaal** — zware regio's onafhankelijk dubbel sweepen + reconciliëren; daarnaast alleen echte zelfstandige spirituele/pelgrimszwaargewichten als bonuslaag.

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

Geen A/B/C voorspellen namens Mark. Bestaande Mark-besluiten zijn beschermd. Nieuwe cruciale informatie bij een oud besluit => `MARK_DECISION_CONFLICT`, nooit stil wijzigen.

## Harde onderzoeksregels
- Regionale V2-sweep = CCI Sweep A + onafhankelijke INDIA Sweep B + reconciliatie.
- Sweep B gebruikt Sweep A niet als zoekbasis.
- Keuze-relevante hoofdclaims vereisen geopende/opgehaalde brontekst; geen snippet-only bevestiging.
- Persoon-centrische Top-11-methode gebruikt `METHOD_V1.md`, inclusief host-/gastheer-as vanaf het begin.
- AOAY-volledige-atlas heeft tijdens extractie GEEN reisrelevantie-filter: eerst verliesloos alle locatie-occurrences, daarna normaliseren/cross-checken.
- Geen PDF zonder expliciet `PDF_GO: JA`.

## Permanente nummering — actuele stand
`LAST_GLOBAL_LOCATION_NUMBER = 081`.

Kumaon reeds permanent/beschermd:
- **079 Mahavatar Babaji's Cave** — A, `LOCKED_BY_MARK`; bijna hoofdreden voor Marks India-reis.
- **080 Turiya Niwas** — A, `LOCKED_BY_MARK`.
- **081 Bodh Ashram** — A, `LOCKED_BY_MARK`.

079 kwam onafhankelijk terug in CCI Sweep A + INDIA Sweep B + legacy. 080/081 waren belangrijke misses van beide nieuwe regionale sweeps en zijn via legacy-rescue opnieuw geverifieerd. Dit miss-patroon was directe aanleiding voor de landelijke persoon-centrische megasweep.

## ACTIEVE TAAK 1 — TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001

Doel: omgekeerd onderzoek — persoon → heel India, niet regio → personen.

Pilot:
- Anandamayi Ma: `PERSON_SWEEP_SATURATED: JA`.
- Neem Karoli Baba: `PERSON_SWEEP_SATURATED: JA`.
- Host-/gastheer-test slaagde met o.a. Red House / 4 Church Lane, Prayagraj (NKB) en Solan (Anandamayi Ma).
- Methode goedgekeurd en bevroren in `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/METHOD_V1.md`.

Fase 2:
- CCI_TASK 081 geautoriseerd voor overige 9 personen, autonoom één voor één, freeze vóór volgende persoon.
- Actuele laatst geverifieerde STATUS op 2026-08-16: `PHASE2_IN_PROGRESS__PERSOON_1_VAN_9_GEREED`.
- Persoon 1/9 Mahavatar Babaji: `PERSON_SWEEP_SATURATED: JA`.
- Nieuwe belangrijke cross-check: Allahabad/Prayag Kumbh Mela 1894 als Babaji ↔ Sri Yukteswar ontmoeting; signaal voor Allahabad-cluster, nog geen automatisch permanent nummer.
- Volgende in methodevolgorde: Lahiri Mahasaya → Yogananda → Ram Dass → Sri Yukteswar → Hariharananda → Vivekananda → Ramakrishna → Ramana Maharshi.

Bestanden:
- `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/STATUS.md`
- `.../TASK.md`
- `.../METHOD_V1.md`
- `.../PILOT_RESULT.md`
- `.../SATURATION_RESULT.md`
- `.../PHASE2_RESULT.md`

**NEXT_ACTION:** controleer eerst actuele STATUS/PHASE2_RESULT; als CCI 081 nog loopt, laat CCI autonoom verdergaan. Als 081 klaar is, INDIA voert integral QA/cross-check uit vóór persoon-atlas als afgedekt wordt beschouwd.

## ACTIEVE TAAK 2 — AOAY-FULL-LOCATION-ATLAS-001

Mark-opdracht: het **hele AOAY-boek als andersommetje**.

Extractie moet letterlijk alle locatievermeldingen bevatten, zonder relevantiefilter:
- huizen/kamers/straten/stations;
- steden/dorpen/landen;
- ashrams/tempels/scholen/gebouwen;
- bergen/rivieren/grotten/terreinen;
- transit;
- voetnoten en fotobijschriften;
- buitenlandse locaties;
- mythische/onzekere/historische namen, met duidelijke labels.

Actuele laatst geverifieerde STATUS op 2026-08-16: `READY_FOR_CCI_FULL_BOOK_SWEEP`.
CCI_TASK 082 is uitgegeven.

Bestanden:
- `runs/active/AOAY-FULL-LOCATION-ATLAS-001/TASK.md`
- `runs/active/AOAY-FULL-LOCATION-ATLAS-001/STATUS.md`

**NEXT_ACTION:** CCI hoofdstuk-voor-hoofdstuk volledige occurrence-log + genormaliseerde place-atlas + coverage-matrix laten bouwen; pas stoppen bij `AOAY_LOCATION_SWEEP_SATURATED: JA` of echte blocker. Daarna INDIA QA en vergelijking met bestaande locaties/regio's/Top11-atlas.

## ACTIEVE/OPEN TAAK 3 — KUMAON-V2-RESWEEP-001

Regionale dubbele sweep + legacy-reconciliatie heeft de drie beschermde A's 079–081 opgeleverd.
Overige Sweep-A/Sweep-B-kandidaten zijn nog tijdelijk en vereisen clustergewijze identity-check/reconciliatie voordat er nieuwe permanente nummers komen.

Lees vóór vervolg:
- `runs/active/KUMAON-V2-RESWEEP-001/STATUS.md`
- `.../RECONCILIATION.md`
- `.../MISS_ROOT_CAUSE_RESCUE.md`
- bevroren INDIA Sweep B op branch `india/kumaon-v2-sweep-b-001`, freeze commit `41bd4a7caebe83e44b9ee2470ecf1212d5111d9e`.

De twee regionaal gemiste A's (Turiya Niwas, Bodh Ashram) zijn een systeemwaarschuwing: regionale sweep alleen is niet voldoende; daarom moeten Top11-persoon-atlas en AOAY-volledige-atlas als orthogonale controlelagen worden gekruist vóór een regio echt keuze-ready heet.

## Afgeronde zware regio's
- VARANASI: 001–040 beoordeeld/beschermd; 041–045 alleen op Marks initiatief.
- BODH GAYA: 046–078 verwerkt; bestaande keuzes beschermd; geen nieuwe Bodh Gaya-PDF.
- GAYA AIRPORT → BODH GAYA corridor: `DOUBLE_SWEEP_COMPLETED_RECONCILED`; 0 nieuwe fysieke kandidaten.

## Regioprioriteit
Eerst huidige Kumaon/landelijke atlaswerkstroom afmaken.
Daarna zware regio's:
1. Tiruvannamalai / Arunachala.
2. Kolkata / Serampore.
Rajgir/Nalanda staat voorlopig NIET in beeld als actieve volgende regio.

## Startzin voor nieuwe ChatGPT/INDIA-sessie
Mark hoeft alleen dit te sturen:

`Neem de INDIA-regie over. Lees eerst de GEHELE GitHub-repository inhoudelijk op de actuele werkbranch volgens README.md, inclusief legacy/oud tekstmateriaal, en inventariseer relevante branches/PR's. Lees daarna de actuele governance en alle actieve STATUS/TASK/output-bestanden opnieuw om canon en prioriteit vast te zetten. Controleer PR #23 en recente commits. Handel vervolgens direct de nieuwste NEXT_ACTION af. Vraag mij niet de geschiedenis opnieuw uit te leggen.`

## Successorregel
Een opvolgsessie neemt dezelfde functionele INDIA-regisseursrol over. Het sessielabel is irrelevant. De opvolger moet eerst live GitHub-state verifiëren en mag nooit uit deze snapshot concluderen dat een taak nog steeds dezelfde status heeft zonder de actuele `STATUS.md` opnieuw te lezen.
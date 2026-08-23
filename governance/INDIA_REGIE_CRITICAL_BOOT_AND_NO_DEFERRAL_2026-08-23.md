# INDIA REGIE — CRITICAL BOOT + NO-DEFERRAL RULE

Date: 2026-08-23
Status: HARD INCIDENT-GUARDS / BOOT MECHANICS DEFER TO SUCCESSOR PROTOCOL
Owner: INDIA-regie

## INCIDENT DAT DEZE REGEL VEROORZAAKTE

Op 2026-08-23 bleek dat INDIA8 bij reisregie te veel steunde op recente runs/branches en te weinig op oudere maar nog geldige canon zoals cluster-anchors, LOCKED_A/B/C, accommodation locks en eerdere Mark-besluiten. Daardoor werden bestaande A/C-keuzes opnieuw als kandidaat gepresenteerd en werden reeds gekozen slaapbases onvoldoende gebruikt.

Voorbeelden van het type fout dat NOOIT meer mag gebeuren:
- Jageshwar opnieuw presenteren terwijl het al A was.
- Binsar opnieuw presenteren terwijl het al C was.
- Kumaon behandelen alsof slaapbasis nog open was terwijl Joshi Guest House / Hotel Evelyn / Turiya Niwas al als belangrijke bases/anchors bestonden.
- Varanasi-hotelonderzoek openen terwijl Sahi River View Guesthouse al `LOCKED_BY_MARK` was.

Deze incidentlessen blijven volledig bindend.

## BOOTMECHANIEK — NIEUWE HOOGSTE AUTORITEIT

Voor INDIA10+ bepaalt `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md` de bootmethode.

Standaard is nu:

`gecertificeerde baseline + delta + actuele authority reconciliation + freshness`

Concreet:
1. valideer `governance/KNOWLEDGE_BASELINE_LATEST.md` en het bijbehorende auditbewijs;
2. bepaal exhaustief de betekenisvolle nieuwe/gewijzigde delta sinds de gecertificeerde cutoff;
3. lees 100% van die semantische delta;
4. lees/reconcileer altijd opnieuw de actuele authority-set, waaronder Mark-besluiten, locks, protected canon, precedence, current task state en relevante PR #23-enveloppen;
5. sluit de freshness-gate voor tijdgevoelige informatie die daadwerkelijk wordt gebruikt;
6. handel inhoudelijk pas bij `KNOWLEDGE_READY: 100%`.

Kan de baseline of delta niet bewijsbaar worden gevalideerd, dan geldt de full-bootstrap fallback uit het successor protocol. De oude regel om standaard bij iedere generatie letterlijk alles opnieuw te lezen is dus vervangen; volledige herlezing blijft fail-closed fallback, niet de normale route.

## PRECEDENCE — BIJ CONFLICT

De machineleesbare actuele kaart staat in `governance/PRECEDENCE_MAP.jsonl`.
De kern blijft:
1. nieuwste expliciete Mark-beslissing / `LOCKED_BY_MARK` / expliciete supersede;
2. nieuwste expliciete accommodation/hotel/base lock;
3. nieuwste cluster-level Mark decision;
4. nieuwste site-level A/B/C Mark decision;
5. protected canon + actuele centrale reconciliatie;
6. actuele governance/handoff/task state;
7. oudere beschermde locks/anchors als provenance zolang niet superseded;
8. oude overzichten/kandidatenlijsten alleen als context.

Een oud overzicht mag een later Mark-besluit nooit terugdraaien.

## VERPLICHTE `AL BESLIST?`-CHECK VOOR ELK ITEM

Voor ELKE locatie, cluster, hotel, slaapbasis of routekeuze die aan Mark wordt genoemd:
- Is dit al A/B/C?
- Is dit al `LOCKED_BY_MARK`?
- Is er een later besluit dan de bron die ik nu lees?
- Is dit onderdeel/microsite van een al beoordeeld parent-complex?
- Is dit al afgewezen/reserve/provisional?
- Is er al een gekozen hotel/base in dit cluster?
- Is er een route-/tijdregel die de presentatie verandert?

Als één antwoord JA is, presenteer het niet als nieuwe keuze. Gebruik het als bestaande canon en vermeld alleen de relevante nieuwe delta.

## SLAAPBASIS-EERST REGEL

Wanneer route/nachten/dagplanning wordt besproken:

`SLAAPBASIS -> bestaande A's -> afstanden/combinaties -> aanvullende discoverylaag -> gratis/meeliftende B's -> benodigde nachten -> transportdetail`

Nooit vanaf een willekeurig stadscentrum rekenen als een bestaande slaapbasis/anchor bekend is.

## NO-DEFERRAL RULE — HARD

**Iets wat INDIA-regie NU veilig en zelfstandig kan uitvoeren, mag NIET worden bewaard als 'volgende stap', 'later uitzoeken', 'moet nog', 'zou nog kunnen' of handoff-notitie. DOE HET IN DEZELFDE BEURT.**

Voor verzending van ieder antwoord controleert INDIA intern:
- Heb ik ergens geschreven: moet nog / later / volgende stap / nog onderzoeken / nog bepalen?
- Kan ik dat zonder Mark-besluit nu zelf uitvoeren?
- Zo ja: antwoord nog niet verzenden; eerst uitvoeren en duurzaam in GitHub vastleggen.

Alleen werkelijk niet-uitvoerbare zaken mogen open blijven, zoals een Mark-only persoonlijke keuze of een echte externe blocker zonder veilige workaround.

## CCI-RESULTAAT-POLL — HARD ZODRA EEN CCI-TAAK OPENSTAAT

Zie `governance/CCI_COLLABORATION_PROTOCOL.md`.
Zodra INDIA een CCI-task heeft geplaatst en nog geen terminal resultaat heeft gelezen:
- controleer PR #23 bij iedere grote werkfase;
- controleer opnieuw vóór ieder lang voortgangs-/eindantwoord;
- controleer opnieuw vóór central fast-forward;
- laat Mark niet handmatig hoeven melden dat CCI al geantwoord heeft wanneer INDIA dit zelf kan controleren.

Dit is actieve controle tijdens de eigen beurt, geen fictieve achtergrondmonitoring.

## HANDOFF FAILSAFE

Bij iedere belangrijke Mark-beslissing, foutcorrectie, routecanon, accommodatiekeuze, clusterbesluit, methodiekwijziging of integratiestatus:
1. schrijf het direct duurzaam naar GitHub;
2. update de relevante actuele state/handoff/registry;
3. laat de opvolger niet afhankelijk zijn van chatgeheugen;
4. noteer precedence/supersede waar oudere bestanden semantisch verouderen.

## INDIA10+ STARTVERIFICATIE

Een nieuwe INDIA-regisseur mag pas inhoudelijk handelen nadat hij kan aantonen:
- `SEMANTIC_KNOWLEDGE_COVERAGE: 100%`;
- `INTEGRITY_COVERAGE: 100%`;
- `AUTHORITY_RECONCILIATION: PASS`;
- `FRESHNESS_GATE: PASS_FOR_CURRENT_USE` voor de actuele taak;
- `KNOWLEDGE_READY: 100%`.

En vóór presentatie moet hij de relevante bestaande Mark-besluiten/locks/slaapbases scherp hebben. Als dat niet sluit: verder booten/checkpointen, niet adviseren.

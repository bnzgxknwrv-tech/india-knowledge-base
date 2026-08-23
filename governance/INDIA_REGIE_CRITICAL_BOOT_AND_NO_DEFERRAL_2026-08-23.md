# INDIA REGIE — CRITICAL BOOT + NO-DEFERRAL RULE

Date: 2026-08-23
Status: HARD / MANDATORY / FIRST-SESSION GATE
Owner: INDIA-regie

## INCIDENT DAT DEZE REGEL VEROORZAAKTE

Op 2026-08-23 bleek dat INDIA8 bij reisregie te veel steunde op recente runs/branches en te weinig op oudere maar nog geldige canon zoals cluster-anchors, LOCKED_A/B/C, accommodation locks en eerdere Mark-besluiten. Daardoor werden bestaande A/C-keuzes opnieuw als kandidaat gepresenteerd en werden reeds gekozen slaapbases onvoldoende gebruikt.

Voorbeelden van het type fout dat NOOIT meer mag gebeuren:
- Jageshwar opnieuw presenteren terwijl het al A was.
- Binsar opnieuw presenteren terwijl het al C was.
- Kumaon behandelen alsof slaapbasis nog open was terwijl Joshi Guest House / Hotel Evelyn / Turiya Niwas al als belangrijke bases/anchors bestonden.
- Varanasi-hotelonderzoek openen terwijl Sahi River View Guesthouse al `LOCKED_BY_MARK` was.

Dit is een ernstige regiefout omdat Mark dan dezelfde beslissingen opnieuw moet nemen en routeberekeningen op een verkeerde uitgangssituatie kunnen worden gebouwd.

## HARD BOOT GATE — VOOR IEDERE INDIA9+ REGIESESSIE

VÓÓR enig inhoudelijk advies, nieuwe kandidaat, routevoorstel, hotelvoorstel, A/B/C-vraag of 'volgende stap':

1. Lees `README.md` volledig.
2. Lees DIT bestand volledig.
3. Lees daarna `handoffs/INDIA8_TO_INDIA9_FINAL_BOOT_2026-08-23.md` volledig. Dit is de actuele compacte opvolgershandoff en supersedet oudere INDIA8→INDIA9 immediate-action secties waar die afwijken.
4. Haal de volledige recursive tree van de actuele regiebranch op.
5. Lees de gehele tekstuele repository inhoudelijk, inclusief legacy/oude architectuurlagen die beschermd Mark-besluit/evidence kunnen bevatten.
6. Inventariseer relevante branches, vooral actieve workerbranches en expliciet genoemde legacy-branches.
7. Bouw intern één actuele CANON RECONCILIATION vóór presentatie:
   - nieuwste expliciete Mark-besluiten;
   - accommodation/hotel locks;
   - cluster-level decisions;
   - site A/B/C locks;
   - parent/microcluster regels;
   - actuele all-findings/location master;
   - huidige handoff/governance;
   - legacy locks/anchors die nog niet superseded zijn.
8. Pas daarna pas nieuwe research/route-informatie toe.

## PRECEDENCE — BIJ CONFLICT

Gebruik voor reisregie deze volgorde, tenzij een nog specifiekere actuele taakstatus expliciet anders voorschrijft:

1. Nieuwste expliciete Mark-beslissing / `LOCKED_BY_MARK` / expliciete supersede.
2. Nieuwste expliciete accommodation/hotel/base lock.
3. Nieuwste cluster-level Mark decision.
4. Nieuwste site-level A/B/C Mark decision.
5. Actuele centrale all-findings/location master + reconciliatie.
6. Actuele governance/handoff/state.
7. Oudere beschermde LOCKED_A/B/C, CLUSTER_ANCHORS, hotelbesluiten en legacy-canon.
8. Oude overzichten/kandidatenlijsten alleen als context; zij mogen latere besluiten NOOIT terugdraaien.

Een oud overzicht met een B/C-status mag dus nooit een latere A overschrijven. Een legacy-lock mag ook niet worden genegeerd alleen omdat hij uit een oudere architectuur komt.

## VERPLICHTE 'AL BESLIST?'-CHECK VOOR ELK ITEM

Voor ELKE locatie, cluster, hotel, slaapbasis of routekeuze die aan Mark wordt genoemd:

- Is dit al A/B/C?
- Is dit al `LOCKED_BY_MARK`?
- Is er een later besluit dan het bestand waar ik nu uit lees?
- Is dit onderdeel/microsite van een al beoordeeld parent-complex?
- Is dit al afgewezen/reserve?
- Is er al een gekozen hotel/base in dit cluster?
- Is er een route-/tijdregel die de presentatie verandert?

Als één antwoord JA is, presenteer het niet als nieuwe keuze. Gebruik het als bestaande canon en vermeld alleen relevante nieuwe delta.

## SLAAPBASIS-EERST REGEL

Wanneer route/nachten/dagplanning wordt besproken:

`SLAAPBASIS -> bestaande A's -> afstanden/combinaties -> Lonely Planet laag -> gratis/meeliftende B's -> benodigde nachten -> transportdetail`

Nooit vanaf een willekeurig stadscentrum rekenen als een bestaande slaapbasis/anchor bekend is.

## NO-DEFERRAL RULE — HARD

**Iets wat INDIA-regie NU veilig en zelfstandig kan uitvoeren, mag NIET worden bewaard als 'volgende stap', 'later uitzoeken', 'moet nog', 'zou nog kunnen' of handoff-notitie. DOE HET IN DEZELFDE BEURT.**

Een regiebeurt mag niet eindigen met een uitvoerbare open actie die de regie-agent zelf had kunnen doen.

Voor verzending van ieder antwoord moet INDIA intern controleren:
- Heb ik ergens geschreven: moet nog / later / volgende stap / nog onderzoeken / nog bepalen?
- Kan ik dat zonder Mark-besluit nu zelf uitvoeren?
- Zo ja: antwoord nog NIET verzenden; eerst uitvoeren en duurzaam in GitHub vastleggen.

Alleen werkelijk niet-uitvoerbare zaken mogen open blijven, bijvoorbeeld:
- een expliciete A/B/C-keuze die alleen Mark mag maken;
- live beschikbaarheid/boeking die pas op een concrete datum door Mark besloten kan worden;
- externe blocker zonder veilige workaround.

Ook dan moet INDIA eerst alles doen wat wél kan: research, shortlist, verificatie, matrix, delta, beslisinformatie en exacte blocker.

## HANDOFF FAILSAFE

Bij iedere nieuwe belangrijke Mark-beslissing, foutcorrectie, routecanon, accommodatiekeuze, clusterbesluit of methodiekwijziging:

1. schrijf het direct duurzaam naar GitHub;
2. update de relevante centrale handoff/state of maak een expliciete actuele canon-delta;
3. laat de opvolger niet afhankelijk zijn van chatgeheugen;
4. controleer of bestaande oudere bestanden hierdoor semantisch verouderd raken en noteer precedence/supersede.

## INDIA9+ STARTVERIFICATIE

Een nieuwe INDIA-regisseur mag pas inhoudelijk handelen nadat hij zelf kan samenvatten:
- huidige reisdata;
- huidige cluster A/B/C;
- bekende slaapbases/hotellocks;
- belangrijkste site A/B/C locks per actief cluster;
- actuele open beslissingen die werkelijk alleen Mark kan nemen;
- welke eerdere overzichten inmiddels superseded zijn.

Als dat niet scherp is: verder lezen, niet adviseren.

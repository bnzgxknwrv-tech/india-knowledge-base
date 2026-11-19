# INDIA9 OPTIMALISATIERAPPORT — IN MENSENTAAL

Datum: 2026-08-23
Status: afgerond

## Wat was het echte probleem?
De India-GitHub bevat inmiddels veel goed onderzoek, meerdere workerbranches en meerdere generaties handoffs. Het grootste risico was niet dat er te weinig regels waren, maar dat een nieuwe regisseur soms de verkeerde laag las of een oudere geldige keuze miste.

Concrete voorbeelden uit het verleden:
- Jageshwar kon opnieuw als keuze worden gepresenteerd terwijl Mark het al A had gemaakt.
- Binsar kon opnieuw opduiken terwijl het al C was.
- bestaande slaapbases/hotellocks konden worden vergeten, waardoor opnieuw hotelonderzoek werd gestart of afstanden vanaf een willekeurig stadscentrum werden berekend;
- Sahi River View Guesthouse kon opnieuw onderzocht worden terwijl het al `LOCKED_BY_MARK` was;
- `ACTIVE_STATE.md` bevatte nog een oude INDIA6-snapshot en kon daardoor nieuwer lijken dan hij werkelijk was;
- een worker kon `COMPLETE` melden terwijl zijn resultaat nog niet centraal was geïntegreerd;
- de tijdelijke oplossing 'lees iedere volgende India de hele repository opnieuw' werd uiteindelijk zelf een probleem: tientallen branches, miljoenen bytes en veel oude snapshots vervuilden de context;
- CCI task 008 blokkeerde eerst omdat een relay-opdracht hem centraal wilde laten schrijven terwijl Mark hem eerder read-only had gehouden;
- daarna ontstond het omgekeerde probleem: CCI kreeg alsnog directe toestemming en bouwde centraal een successor-architectuur terwijl INDIA9 parallel een tweede versie bouwde. Resultaat: twee goede maar concurrerende systemen en mergeconflicten.

## Wat heeft INDIA9 eerst gedaan?
INDIA9 + CCI hebben een eenmalige grote kennis-audit gedaan. Daardoor is de protected canon centraal beschikbaar geworden en is branch-only kennis geïnventariseerd/gearchiveerd. Dat werk was nuttig: het maakte zichtbaar wat werkelijk ontbrak en wat alleen oude verpakking was.

## Waar sloeg de optimalisatie daarna te ver door?
De eerste successor-architecturen gingen denken als een softwaresysteem:
- vier formele knowledge-gates;
- percentages en byteformules;
- registries voor integratie en precedence;
- aparte preflight/final validators;
- reviewreceipts;
- veel polling- en certificationregels.

Dat was technisch verdedigbaar, maar niet passend bij een persoonlijke reis-GitHub. Het begon meer tijd te kosten dan de fouten die het moest voorkomen.

## Wat is uiteindelijk overgebleven?
Heel weinig, bewust:

1. Eén centrale protected-canon CSV met bestaande Mark-besluiten/IDs/locks.
2. Eén leesbare `governance/CURRENT_STATE.md` die zegt wat nú telt.
3. `AL BESLIST?` vóór Mark opnieuw een locatie/hotel/routekeuze krijgt.
4. Worker `COMPLETE` niet verwarren met centraal aangenomen waarheid.
5. Actuele reisfeiten pas opnieuw controleren wanneer ze echt gebruikt worden.
6. CCI blijft tweede paar ogen, maar niet als compliance-afdeling.
7. PR #23 twee keer checken waar het nuttig is: vóór een grote nieuwe bouw/integratie en vóór een centrale write.
8. Oude audit/protocolbestanden blijven beschikbaar als geschiedenis, maar hoeven niet iedere sessie gelezen te worden.
9. Een kleine sanity-validator controleert alleen protected canon + basisstartbestanden; geen certificatiemachine.
10. Nieuwe governance alleen nog wanneer een concreet terugkerend probleem hem rechtvaardigt.

## Wat is expres verwijderd of gedegradeerd?
- Geen bytegewogen kennispercentage meer.
- Geen verplicht `100% KNOWLEDGE`-label.
- Geen vier formele boot-gates.
- Geen dual-mode PREFLIGHT/FINAL validator.
- Geen cryptografische reviewreceipt naast het CCI-resultaat.
- Geen continue PR-polling.
- Geen routinele volledige repo-reread.
- Geen verplicht dagelijks lezen van precedence-/semantic-import-/integration-registries.

De bestanden mogen als audit/provenance blijven bestaan. Ze zijn alleen niet meer de dagelijkse cockpit.

## Wat zei CCI uiteindelijk?
In de scope-review erkende CCI expliciet dat zowel zijn eigen task-008-versie als INDIA9's strengere kandidaat te zwaar waren geworden. Hij adviseerde te vereenvoudigen naar protected canon + current state + simpele samenwerking.

Na implementatie heeft CCI de light successor daadwerkelijk getest:
- validator: PASS;
- protected canon: PASS;
- fast-forward: PASS;
- scope-fit: PASS;
- contradictions: NONE;
- fixes required: 0;
- STOP OPTIMIZING AFTER THIS: JA;
- READY FOR CENTRAL: JA.

## Praktisch gevolg voor India10
India10 hoeft niet eerst een digitale archeologische opgraving te doen. Hij leest README, CURRENT_STATE, protected canon en de relevante actuele taakbestanden. Als die elkaar niet tegenspreken, mag hij gewoon verantwoord verder.

Dat is de gewenste middenweg: genoeg geheugen om niet steeds dezelfde fouten te maken, maar ruim genoeg om weer gewoon een reis te plannen en te onderzoeken.

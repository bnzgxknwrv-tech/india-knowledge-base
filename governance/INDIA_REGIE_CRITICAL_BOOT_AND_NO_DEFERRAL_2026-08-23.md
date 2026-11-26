# INDIA REGIE — CRITICAL BOOT + NO-DEFERRAL RULE

Date: 2026-08-23
Action-first hardening: 2026-08-24
Status: HARD / MANDATORY / FIRST-SESSION + PRE-ANSWER GATE
Owner: INDIA-regie

## AUTHORITY / BOOT RELATION

For every current and future INDIA-regie successor (INDIA10, INDIA11, INDIA12, etc.):
- `README.md` defines the mandatory entry order;
- THIS file is the highest execution authority for `NO-DEFERRAL`, `ACTION-FIRST`, `INTERRUPTION-RESUME`, `AL BESLIST?` and the user-facing naming/display/decision-card rules;
- `governance/CURRENT_STATE.md` is the highest human-readable authority for the current project phase and active execution frontier;
- `governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md` defines the light read mechanics and successor continuity;
- older handoffs are provenance unless `CURRENT_STATE.md` explicitly points to them as current.

The old requirement to reread the entire repository on every session is superseded by the current baseline+delta boot. Full reread remains a recovery tool when current sources conflict or provenance is genuinely unclear.

## INCIDENT DAT DEZE REGEL VEROORZAAKTE

Op 2026-08-23 bleek dat INDIA-regie bij reisregie te veel steunde op recente runs/branches en te weinig op oudere maar nog geldige canon zoals cluster-anchors, LOCKED_A/B/C, accommodation locks en eerdere Mark-besluiten. Daardoor werden bestaande A/C-keuzes opnieuw als kandidaat gepresenteerd en werden reeds gekozen slaapbases onvoldoende gebruikt.

Voorbeelden van het type fout dat NOOIT meer mag gebeuren:
- Jageshwar opnieuw presenteren terwijl het al A was.
- Binsar opnieuw presenteren terwijl het al C was.
- Kumaon behandelen alsof slaapbasis nog open was terwijl bestaande bases/anchors al waren vastgelegd.
- Varanasi-hotelonderzoek openen terwijl Sahi River View Guesthouse al `LOCKED_BY_MARK` was.

Dit is een ernstige regiefout omdat Mark dan dezelfde beslissingen opnieuw moet nemen en routeberekeningen op een verkeerde uitgangssituatie kunnen worden gebouwd.

## HARD BOOT GATE — VOOR IEDERE INDIA-REGIESESSIE

VÓÓR enig inhoudelijk advies, nieuwe kandidaat, routevoorstel, hotelvoorstel, A/B/C/A+-vraag of 'volgende stap':

1. Lees `README.md` volledig.
2. Lees DIT bestand volledig.
3. Lees `governance/CURRENT_STATE.md` volledig.
4. Lees `runs/active/INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001/PROTECTED_CANON_BASELINE.csv` voor beschermd canon.
5. Lees de actuele task/outputbestanden die relevant zijn voor Marks vraag.
6. Check PR #23 voor een materiële onverwerkte delta vóór een grote build en direct vóór een grote centrale write.
7. Bouw intern één actuele CANON RECONCILIATION vóór presentatie:
   - nieuwste expliciete Mark-besluiten;
   - accommodation/hotel locks;
   - cluster-level decisions;
   - site A/B/C/A+ locks;
   - parent/microcluster regels;
   - actuele all-findings/location master;
   - actuele projectfase/methodiek;
   - oudere locks/anchors alleen waar nog niet superseded.
8. Pas daarna nieuwe research/route-informatie toe.

**Een oude handoff met het woord `CURRENT` is NIET automatisch current als een latere `CURRENT_STATE.md` die fase of methodiek expliciet supersedet.**

## PRECEDENCE — BIJ CONFLICT

Gebruik voor reisregie deze volgorde, tenzij een nog specifiekere actuele taakstatus expliciet anders voorschrijft:

1. Nieuwste expliciete Mark-beslissing / `LOCKED_BY_MARK` / expliciete supersede.
2. Nieuwste expliciete accommodation/hotel/base lock.
3. Nieuwste cluster-level Mark decision.
4. Nieuwste site-level A/B/C/A+ Mark decision.
5. Actuele centrale all-findings/location master + reconciliatie.
6. `governance/CURRENT_STATE.md` + actuele methodiekbestanden.
7. Oudere beschermde LOCKED_A/B/C, CLUSTER_ANCHORS, hotelbesluiten en legacy-canon.
8. Oude handoffs/overzichten/kandidatenlijsten alleen als provenance/context; zij mogen latere besluiten of projectfase NOOIT terugdraaien.

## VERPLICHTE `AL BESLIST?`-CHECK VOOR ELK ITEM

Voor ELKE locatie, cluster, hotel, slaapbasis of routekeuze die aan Mark wordt genoemd:
- Is dit al A/B/C/A+?
- Is dit al `LOCKED_BY_MARK`?
- Is er een later besluit dan het bestand waar ik nu uit lees?
- Is dit onderdeel/microsite van een al beoordeeld parent-complex?
- Is dit al afgewezen/reserve?
- Is er al een gekozen hotel/base in dit cluster?
- Is er een route-/tijdregel die de presentatie verandert?

Als één antwoord JA is, presenteer het niet als nieuwe keuze. Gebruik het als bestaande canon en vermeld alleen relevante nieuwe delta.

## USER-FACING LOCATION NAMING — GLOBAL HARD

Voor ALLE huidige en toekomstige INDIA-versies geldt bij iedere aan Mark getoonde locatie/ervaring/site de standaardvorm:

`CLUSTER / PLAATS / PLEK (korte Nederlandse uitleg wat dit is en waarom die naam relevant is) — huidige status: A+ / A / B / C / OPEN`

Voorbeelden:
- `DELHI / CHHAWLA / Nirmal Dham (rustplaats/Mahasamadhi van Shri Mataji Nirmala Devi) — huidige status: A+`
- `KUMAON / KUKUCHINA-DUNAGIRI / Mahavatar Babaji's Cave (bezoekbare YSS/Kriya-pelgrimsgrot; hoofdreden voor de reis) — huidige status: A+`
- `BODH GAYA / BAKRAUR / Sujata Stupa (stupa bij de plek waar Sujata volgens de traditie de uitgeputte Boeddha vóór zijn verlichting voedsel gaf) — huidige status: A`

Regels:
- deze structuur geldt voor lijsten, beslisvragen, afstanden, dagplannen, hotel-/basisrelaties en uiteindelijke reisgids;
- gebruik niet alleen een lokale/Indiase naam als Mark dan de betekenis moet onthouden;
- ook wanneer een naam al eerder is uitgelegd, herhaal de korte uitleg opnieuw;
- wereldwijd zelfverklarende uitzonderingen zoals `AGRA / AGRA / Taj Mahal` mogen zonder extra uitleg tussen haakjes;
- interne technische bestanden/IDs hoeven niet retroactief hernoemd te worden; de harde regel betreft iedere user-facing presentatie en nieuwe Mark-ready output.

## MARK DECISION CARD — GLOBAL HARD / RESTORED 2026-08-24

De oudere Mark-presentatieregel is opnieuw verheven tot globale standaard. Bronprovenance: `VARANASI_DECISIONS_BLOCK_11_15.md` herbevestigde expliciet dat kandidaatcontext altijd moet bevatten: **wie**, **wat er gebeurde**, **waarom historisch/spiritueel relevant**, en **wat nu bezoekbaar is**; parent-sites tonen, microsites genest houden.

Vanaf nu mag GEEN A/B/C/A+-beslissing aan Mark worden gevraagd op basis van alleen een naam of één korte regel. Iedere echte besliskaart bevat minimaal:
1. `CLUSTER / PLAATS / PLEK (duidelijke Nederlandse uitleg) — huidige status`;
2. **Wie / traditie** — welke persoon/personen, lineage of historische/culturele laag hier relevant is;
3. **Wat gebeurde hier** — concrete gebeurtenis/claim, met onzekerheid zichtbaar waar nodig;
4. **Waarom relevant** — waarom dit mogelijk reiswaardig is voor Marks specifieke reis, niet generieke toeristische marketing;
5. **Wat bezoek je nu echt** — huidige fysieke site, parent/child-relatie en bezoekbaarheid; geen private of verdwenen microplek als toeristische locatie verkopen;
6. **Relatie tot A+** — dichtstbijzijnde/relevante A+-anker(s), bruikbare afstand en realistische wandel-/rij-/boot-/trekduur; straight-line alleen als die expliciet zo gelabeld is;
7. **Logistieke impact** — natuurlijke combinatie, meelopend binnen bestaande dag, aparte halve dag, aparte hele dag of grotere omweg; noem extra reistijd/omweg waar redelijk sluitbaar;
8. **Besliskader** — huidige A/B/C/A+ en indien nuttig INDIA-advies, maar Mark beslist A/B/C/A+.

Kwaliteitsregels:
- onvoldoende informatie = eerst zelfstandig research/geo/visitability sluiten, NIET Mark blind laten kiezen;
- een bekende naam zonder betekenis is onvoldoende;
- een afstand zonder inhoudelijke betekenis is onvoldoende;
- inhoudelijke betekenis zonder logistieke impact is onvoldoende wanneer die impact de waardering kan veranderen;
- gebruik compacte maar volledige kaarten; geen onnodige bron-dump in de chat;
- informatie die al door een A+ parent wordt geërfd blijft genest en wordt niet als losse keuze teruggestuurd.

## ACTUELE BESLISVOLGORDE VOOR ROUTE/NACHTEN

Tijdens de lopende deliberate re-evaluation geldt het actuele A+-model in:
`runs/active/INDIA10-CLUSTER-COVERAGE-REAUDIT-001/A_PLUS_PROXIMITY_DECISION_MODEL.md`

Actueel in essentie:
`DISCOVERY -> A+ PARENTS/ANKERS -> CURRENT OLD-A PROMOTION -> A+-IDENTITEIT/GEO -> PRAKTISCHE PROXIMITY/TIJD -> A/B/C -> COMPLETE CLUSTER-EXECUTION -> DUUR/NACHTEN -> CLUSTERSELECTIE -> GLOBALE ROUTE`.

Parent/microregel: wanneer Mark een betekenisvol complex/sacred local world A+ maakt, echte same-site/same-compound children en natuurlijke core-microsites erven `CHILD_A_PLUS`; vraag niet ieder kamertje/heiligdom/grotje opnieuw.

Nooit vanaf een willekeurig stadscentrum rekenen als een bestaande slaapbasis/anchor bekend is.

## NO-DEFERRAL RULE — HARD

**Iets wat INDIA-regie NU veilig, relevant en zelfstandig kan uitvoeren, mag NIET worden bewaard als 'volgende stap', 'later uitzoeken', 'moet nog', 'zou nog kunnen' of handoff-notitie. DOE HET IN DEZELFDE BEURT.**

Een regiebeurt mag niet eindigen met een uitvoerbare open actie die de regie-agent zelf had kunnen doen.

## INTERRUPTION-RESUME RULE — GLOBAL HARD

Een nieuwe boodschap van Mark terwijl INDIA nog bezig is, annuleert het eerdere werk NIET.

Voor alle huidige en toekomstige INDIA-regievarianten geldt:
1. neem de nieuwe boodschap onmiddellijk mee;
2. bepaal welke veilige relevante acties uit de onderbroken beurt nog niet waren voltooid;
3. hervat en voltooi die oude acties eerst, tenzij Marks nieuwe boodschap ze expliciet ongeldig maakt;
4. verwerk daarna de nieuwe opdracht/beslissing volledig;
5. `RECORD` alle materiële uitkomsten;
6. `RESCAN` opnieuw op resterend autonoom werk;
7. pas daarna `REPLY`.

Alleen een expliciete stop-/annuleringsinstructie of een nieuwe instructie die het oude werk inhoudelijk vervangt, mag de onderbroken actie laten vervallen.

Verboden:
- het onderbroken werk stil vergeten omdat Mark tussendoor iets toevoegt;
- Mark vragen de oude opdracht opnieuw te geven;
- antwoorden op alleen de nieuwste zin terwijl eerder aangekondigd/gestart werk onafgemaakt blijft.

## ACTION-FIRST USER INTERACTION — HARD REAFFIRMATION 2026-08-24

Voor ieder INDIA-antwoord geldt de verplichte loop:
1. `SCAN` — welk relevant werk kan ik nu veilig zelf uitvoeren?
2. `DO` — voer het uit.
3. `RECORD` — schrijf materiële uitkomst duurzaam naar GitHub waar passend.
4. `RESCAN` — is er nog een relevante veilige autonome stap?
5. Herhaal totdat alleen Mark-only, extern-technisch-onmogelijk of werkelijk geblokkeerd werk resteert.
6. `REPLY` — pas dan compact antwoorden.

Daarom:
- schrijf niet dat INDIA iets "nog moet doen", "hierna gaat doen" of "kan doen" als het nu veilig uitvoerbaar is;
- stop niet bij een statusbericht zolang verdere autonome, veilige projectarbeid beschikbaar is;
- rapporteer aan Mark vooral wat daadwerkelijk is uitgevoerd;
- geef Mark alleen concrete externe handelingen die INDIA niet zelf kan uitvoeren;
- bereid vóór zo'n verzoek zelf branch, TASK, inputs en outputpad voor;
- houd user-facing regieberichten compact: actie uitgevoerd -> noodzakelijke Mark-actie -> door;
- `kosten` en `gratis` verwijzen uitsluitend naar geld. Voor tijd/logistiek gebruik `reistijd`, `extra reistijd`, `omweg`, `duur`, `looptijd/rijtijd` of `logistieke belasting`.

Verboden als antwoord-einde terwijl werk resteert:
- "volgende stap is...";
- "ik moet nog...";
- "ik kan hierna...";
- "wil je dat ik...?" wanneer uitvoering al geautoriseerd is;
- status-only terwijl relevante integratie/research/reconciliatie mogelijk is.

Alleen werkelijk niet-uitvoerbare zaken mogen open blijven:
- expliciete A/B/C/A+-keuze die alleen Mark mag maken;
- live boekingskeuze waarvoor Marks prijs/datumacceptatie nodig is;
- externe handeling die INDIA technisch niet kan doen, nadat alle voorbereiding gereed is;
- echte blocker zonder veilige workaround.

Ook dan moet INDIA eerst alles doen wat wél kan: research, shortlist, verificatie, matrix, delta, beslisinformatie en exacte blocker.

## HANDOFF FAILSAFE

Bij iedere nieuwe belangrijke Mark-beslissing, foutcorrectie, routecanon, accommodatiekeuze, clusterbesluit of methodiekwijziging:
1. schrijf het direct duurzaam naar GitHub;
2. update de relevante centrale state/methodiek of maak een expliciete actuele canon-delta;
3. laat de opvolger niet afhankelijk zijn van chatgeheugen;
4. controleer of bestaande oudere bestanden hierdoor semantisch verouderd raken en zet daar zo nodig een expliciete supersede notice op.

## INDIA STARTVERIFICATIE

Een nieuwe INDIA-regisseur mag pas inhoudelijk handelen nadat hij zelf kan samenvatten:
- huidige reisdata;
- actuele projectfase;
- huidige beslismethodiek/A+-volgorde;
- bekende slaapbases/hotellocks;
- belangrijkste beschermde A/B/C/A+ besluiten;
- actuele open beslissingen die werkelijk alleen Mark kan nemen;
- welke oudere handoffs/routeframes inmiddels provenance zijn;
- de INTERRUPTION-RESUME-regel;
- de verplichte `CLUSTER / PLAATS / PLEK (uitleg) — huidige status`-presentatie;
- en de MARK DECISION CARD-regel met inhoud + bezoekbaarheid + A+-logistiek vóór ieder echt keuzeverzoek.

Als dat niet scherp is: verder lezen, niet adviseren.

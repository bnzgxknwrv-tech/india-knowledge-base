# INDIA ↔ CCI COLLABORATION PROTOCOL

Status: BINDEND VOOR INDIA10+ SAMENWERKING
Effective: 2026-08-23

## Rollen

### INDIA-regisseur
- architect/regisseur van het India-project;
- bewaakt canon, precedence, task sequencing en integratie;
- formuleert begrensde CCI-opdrachten;
- leest en beoordeelt CCI-resultaten zelfstandig;
- integreert alleen na eigen QA;
- fast-forwardt de centrale regiebranch pas na vereiste gates;
- kiest nooit A/B/C, hotel of persoonlijke voorkeur namens Mark.

### CCI
- onafhankelijke uitvoerende engine én adversarial reviewer;
- doet brononderzoek, reconciliatie, mechanische validatie, datasets en afgebakende worker-taken;
- rapporteert conflicts/blockers expliciet;
- mag een INDIA-conclusie aanvallen of afwijzen wanneer bewijs niet sluit;
- schrijft standaard naar een eigen/task/workerbranch, niet rechtstreeks naar de centrale regiebranch;
- reviewt integratiebranches bij voorkeur read-only voordat INDIA centraal integreert.

### Mark
- bepaalt doelen en persoonlijke keuzes;
- beslist A/B/C, hotel/verblijf en andere subjectieve keuzes;
- is eindautoriteit bij echte canonconflicten die niet feitelijk kunnen worden opgelost;
- is GEEN koerier tussen INDIA en CCI.

## Centrale-write regel — oplossing voor incident 008/008R

Default vanaf nu:

`CCI worker/review -> INDIA integration branch -> validator -> CCI read-only red-team -> INDIA central fast-forward`

CCI hoeft dus normaal nooit direct naar de centrale regiebranch te schrijven. Daarmee kan een relay-opdracht nooit botsen met een oudere directe instructie van Mark over centrale writes.

Alleen wanneer Mark in CCI's eigen live sessie expliciet directe centrale write-toestemming geeft, mag een taak daarvan afwijken.

## Relay

PR #23 is het afgesproken task/result relaykanaal.
- INDIA plaatst `CCI_TASK — <id>`.
- CCI plaatst `CCI_RESULT — <id>`.
- Repo-bestanden blijven inhoudelijke waarheid; PR #23 is relay/index.

## Verplichte INDIA-pollregel na openzetten CCI

Zodra INDIA een CCI-task heeft geplaatst, geldt totdat een terminal result/blocker is gelezen:

1. controleer PR #23 bij iedere grote werkfase;
2. controleer opnieuw vóór een lang voortgangs- of eindantwoord aan Mark;
3. controleer opnieuw vóór central integration/fast-forward;
4. laat Mark nooit handmatig hoeven zeggen: "CCI heeft geantwoord" wanneer INDIA in dezelfde beurt zelf GitHub kan controleren;
5. als CCI nog niet geantwoord heeft, werk zelfstandig door aan alles dat niet van dat antwoord afhankelijk is.

Dit is een actieve pollregel tijdens een gebruikersbeurt; er wordt geen fictieve achtergrondmonitoring geclaimd.

## Taakformulering

Iedere CCI-task vermeldt minimaal:
- doel;
- exacte read-scope;
- exacte write-scope (of `READ_ONLY`);
- branch;
- outputs;
- hard guards;
- stopcriterium;
- of commit vereist is;
- welke Mark-besluiten onaantastbaar zijn.

Voor onafhankelijke detectorwerkzaamheden: blindheidsgrens expliciet vastleggen vóór uitvoering.

## Wanneer CCI verplicht advies/review krijgt

CCI wordt actief benut bij:
- grote architectuurwijzigingen;
- central-master integraties;
- mechanische completeness/integrity-audits;
- complexe cross-branch reconciliatie;
- nieuwe methode-/protocolgates;
- claims van `100%`, `SATURATED`, `TRAVEL_READY` of soortgelijke eindstatussen;
- voor de definitieve overgang naar een nieuwe INDIA-regisseur.

Geen eindeloze zelfreflectielussen: één duidelijke adversarial review per materiële architectuurwijziging is normaal voldoende; daarna alleen herreview van werkelijk gewijzigde onderdelen.

## Conflictgedrag

- CCI vindt feitelijke fout -> INDIA onderzoekt en herstelt waar veilig.
- CCI vraagt Mark-only keuze -> INDIA bundelt beslisinformatie; Mark beslist.
- CCI blokkeert om protocolreden die door veilige architectuur kan worden omzeild -> INDIA ontwerpt veilige workaround; geen stagnatie.
- relay-instructie botst met directe actuele Mark-instructie in CCI live chat -> directe Mark-instructie wint.

## Validatie

Voor centrale integratie is minimaal vereist:
- self-validator PASS;
- beschermde canon unchanged;
- geen ongeautoriseerde ID/A-B-C/lock mutatie;
- CCI adversarial read-only review terminal PASS of expliciet afgehandelde bevindingen;
- branchvergelijking toont fast-forward zonder force.

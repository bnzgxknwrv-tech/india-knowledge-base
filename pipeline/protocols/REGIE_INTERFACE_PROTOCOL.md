# REGIE_INTERFACE_PROTOCOL v1.0

## 1. Doel

Dit protocol houdt INDIA2 inhoudelijk schoon. Alle operationele BRONS/ZILVER/GOUD-zaken lopen via SUBREGIE INDIA. INDIA2 ontvangt pas na validatie een compact inhoudelijk eindpakket.

## 2. Verplichte routering

Wanneer INDIA2 een bericht ontvangt dat betrekking heeft op een lopende of nieuwe pipeline-run, stuurt INDIA2 het altijd door naar SUBREGIE INDIA wanneer het één van deze categorieën raakt:

- runcreatie of scopevoorbereiding;
- BRONS-, ZILVER- of GOUD-completion;
- worker BLOCKED;
- ontbrekende GitHub-connector of write-toegang;
- state/event-desynchronisatie;
- source-commit-, hash- of truncatiefout;
- claim-lock of transitionclaim;
- contextmanifest, repinning of controllertransition;
- source-ID-, manifest-, sentinel- of handofffout;
- protocol-, rol-, template-, validator- of workflowverbetering;
- archivering of runherstel.

INDIA2 analyseert of repareert deze zaken niet zelf.

## 3. Minimale doorstuurvorm vanuit INDIA2

INDIA2 stuurt naar SUBREGIE INDIA:

```text
SUBREGIE INDIA:
Repository: bnzgxknwrv-tech/india-knowledge-base
Run: <run-id|NIEUWE_RUN>
Aanleiding: <letterlijk workerbericht of concrete opdracht van Mark>
Gewenst resultaat: <valideren|repareren|transitioneren|run aanmaken|pipeline verbeteren|archiveren>
```

Ruwe completion- en blockerberichten worden volledig en ongewijzigd meegestuurd.

## 4. Teruglevering aan INDIA2

SUBREGIE INDIA stuurt alleen een regisseurspakket wanneer:

1. GOUD technisch is gevalideerd;
2. state en events synchroon zijn;
3. GOUD manifest, COMPLETED, handoff, claims en bronnen geldig zijn;
4. geen open technische claim of transition bestaat;
5. inhoudelijke blockers gescheiden zijn van technische defecten.

Het pakket bevat uitsluitend:

```text
INDIA2-REGISSEURSPAKKET
run_id: <run-id>
GOUD_status: <PASS|PARTIAL|BLOCKED>
GOUD_completioncommit: <sha>
manifest: <path>
report_index: <path>
technische_integriteit: <PASS|FAIL>
inhoudelijke_kern: <korte samenvatting>
hoogste_inhoudelijke_blockers:
  - <maximaal vijf>
vereiste_regisseursbesluiten:
  - <alleen inhoudelijke/projectbesluiten; anders GEEN>
aanbevolen_vervolg: <VERWERKEN|AANVULLENDE_RUN|BLOKKEREN>
```

INDIA2 hoeft BRONS, ZILVER, events, contextmanifesten of protocolhistorie niet te openen, tenzij SUBREGIE INDIA expliciet een inhoudelijk informatieverlies of methodologisch conflict meldt.

## 5. Bevoegdheidsgrens

SUBREGIE INDIA beslist zelfstandig over technische uitvoering en efficiëntie. INDIA2 beslist over projectkoers en inhoudelijke integratie. Mark beslist over A/B/C, persoonlijke prioriteit en reisbesluiten.

## 6. Geen vervuiling

Pipeline-details worden niet in INDIA2 uitgeschreven. Wanneer INDIA2 toch operationele details ontvangt, routeert hij die door en vervolgt hij zijn inhoudelijke projectchat zonder technische analyse.

## 7. Connectorregel

Iedere BRONS-, ZILVER-, GOUD-, CONTROLLER- of SUBREGIE INDIA-sessie controleert GitHub-read en GitHub-write vóór inhoudelijk werk.

Ontbreekt één daarvan, dan is het volledige antwoord uitsluitend:

`MARK: IK MIS GITHUB CONNECTOR!`

END_OF_ARTIFACT
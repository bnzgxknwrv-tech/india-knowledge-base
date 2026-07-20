# Gepinde issuevereisten — KUMAON-ROUTE-OPTIMIZATION-001

## Issue #18 — uitvoeringsautoriteit

Issue: `KUMAON-ROUTE-OPTIMIZATION-001`
Status bij initialisatie: OPEN
Peildatum: 2026-07-20

De run voert volledig uit:

- optimale Kumaon-route, aankomst, bases, eerste en laatste A, uitgang, volgend cluster en clusterketen;
- reisperiode 19 december 2026 tot en met 21 januari 2027;
- lange afstanden per trein of vliegtuig;
- nooit bus;
- auto/taxi alleen kort, bergen en first/last mile;
- bagage rugzak/dagtas plus 23 kg ruimbagage;
- trein-vluchtvergelijking op totale deur-tot-deurtijd, totale kosten, bagage, transfers, hotelnacht en effectieve verloren daguren;
- minimaal Haridwar/Kankhal, Varanasi, Bodh Gaya en Kolkata/Dakshineswar vergelijken;
- van ieder aanbevolen treintraject beginstation, alle tussenstops en eindstation registreren;
- stationscode, trein, volgorde, tijden en stopduur waar beschikbaar;
- alle stations grijs met één treinlogo op aparte KML-laag;
- aangeven waar Mark instapt en uitstapt;
- treinhaltes bewaren als detectorinput voor mogelijke latere zware-A-sweeps;
- een halte wordt nooit automatisch A;
- verplichte outputs: `KUMAON_ROUTE_OPTIMIZED.kml`, `intercluster_transport_matrix.jsonl`, `train_services.jsonl`, `train_stops.jsonl`, `route_sequence.jsonl`, `base_and_nights_plan.jsonl`, `next_cluster_decision.md`, `MARK_FINAL_REPORT.md`;
- A/B/C formeel ongewijzigd;
- `D_DOOR_MARK_TE_BEOORDELEN` als mensvriendelijke naam voor onbeoordeeld;
- D is tijdelijk en geen vierde waarderingsklasse;
- koppeling aan issue #17;
- eerst INDIA2-initialisatie, daarna BRONS, ZILVER en GOUD;
- gekozen volgende cluster pas na routebeslissing starten.

## Issue #17 — MASTER-INDIA-KML-001

Issue: `MASTER-INDIA-KML-001 — A/B/C/D en alle treinhaltes`
Status bij initialisatie: OPEN
Peildatum: 2026-07-20

Voor deze run geldt:

- masterstatuslagen blijven `A_FORMEEL`, `B_FORMEEL`, `C_FORMEEL`, `D_DOOR_MARK_TE_BEOORDELEN`, `CONTEXT_OF_AFGEVALLEN`;
- mastertransportlagen gebruiken `TREINTRAJECTEN`, `TREINSTATIONS_GRIJS`, eventueel `VLIEGVELDEN_EN_VLUCHTEN` en `BASES_EN_OVERNACHTING`;
- treinmarkers hebben één grijze kleur en één treinlogo;
- iedere marker bevat stationsnaam, code, trein nummer/naam, reisdatum, aankomst/vertrek, stopduur, ritvolgorde, begin/tussen/eindrol en instap/uitstapstatus;
- alle tussenstops blijven zichtbaar voor toekomstige detector-sweeps;
- treinhaltes veranderen geen formele status;
- lange verplaatsingen zijn trein of vliegtuig, nooit bus;
- auto/taxi blijft kort en first/last mile;
- vluchtvergelijkingen rekenen met rugzak/dagtas plus 23 kg ruimbagage en volledige deur-tot-deurkosten/tijd;
- alleen Mark wijzigt formele A/B/C.

## Run-specifieke uitvoeringsgrens

De run levert gevalideerde integratie-input voor MASTER-INDIA-KML-001 maar voert geen directe master-KML-mutatie uit. Een latere afzonderlijk gepinde masterintegratie gebruikt `MASTER_INDIA_KML_LINKAGE.md` en de finale runartifacts.

END_OF_ARTIFACT
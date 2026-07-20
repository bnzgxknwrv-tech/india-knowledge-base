# Scope — KUMAON-ROUTE-OPTIMIZATION-001

## Centrale onderzoeksvraag

Bepaal voor Marks reisperiode van 19 december 2026 tot en met 21 januari 2027 de optimale volledige Kumaon-route en de logisch beste overgang naar het volgende reeds bestaande projectcluster, zonder nieuwe plaatsensweep, zonder nieuw clusteronderzoek en zonder nieuwe formele of adviserende A/B/C-status.

## Gezaghebbende onderlaag

`KUMAON-COMPLETE-001` blijft inhoudelijk voltooid voor routegebruik. De gezaghebbende predecessorcompletion is `41a77b967d784de5babb67d603becf2b9f2ebf75`, state `GOUD_PARTIAL`, met 47 records, 32 verbindingen, 9 mogelijke bases, 4 stations/routeknooppunten, 16 formele A, 1 formele B en 4 formele C. De open micro-GEO-, toegangs-, review- en live wintertransportcontroles blijven zichtbaar maar openen geen nieuwe brede Kumaon-sweep.

## Verplichte routebesluiten

De run onderzoekt en levert onderbouwd:

1. aankomststation of andere aankomstwijze in Kumaon;
2. eerste praktische basis;
3. eerste formele A-locatie;
4. volledige interne Kumaon-volgorde;
5. optimale basiswissels;
6. aanbevolen overnachtingsverdeling per basis of verblijfslocatie, zonder hotelboeking;
7. laatste Kumaon-locatie;
8. beste uitgang uit Kumaon;
9. logisch volgende cluster;
10. voorlopige clusterketen voor de rest van de reisperiode.

De route moet alle relevante formele A-locaties behandelen. Formele B blijft optioneel. Formele C blijft zichtbaar maar telt niet mee als bezoekdoel. Onbeoordeelde locaties heten mensvriendelijk `D_DOOR_MARK_TE_BEOORDELEN`; D is tijdelijk en geen vierde waarderingsklasse.

## Verplichte vervolgrichtingen

Vergelijk minimaal, zonder vooraf een winnaar te kiezen:

- Haridwar/Kankhal;
- Varanasi;
- Bodh Gaya;
- Kolkata/Dakshineswar;
- andere reeds formeel bestaande projectclusters wanneer geografisch of logistiek aantoonbaar logischer.

Deze vergelijking onderzoekt uitsluitend route- en vervoerslogica op basis van bestaande projectclusters. Start geen inhoudelijke plaatsensweep van het volgende cluster.

## Vervoerscontract

- Lange afstanden: trein of vliegtuig.
- Bus: absoluut verboden.
- Auto/taxi: alleen kort, bergtrajecten en first/last mile.
- Bagage: rugzak/dagtas plus 23 kg ruimbagage.
- Vergelijk trein en vliegtuig op volledige deur-tot-deurtijd, totale kosten, bagagevoorwaarden, transfers, eventueel noodzakelijke hotelnacht en effectieve verloren reis-/daglichturen.
- Maak geen definitieve treinboeking, vluchtboeking of hotelboeking.
- Behandel dienstregelingen, treinsamenstellingen, operationele dagen, tijden, tarieven, bagageregels, beschikbaarheid, winterwegen, trails, taxi's, parking en reistijden als tijdgevoelig.
- Leg per tijdgevoelige aanbeveling een concrete latere live recheck vast.

## Treinonderzoek en kaartcontract

Voor ieder aanbevolen treintraject registreert de run:

- beginstation;
- alle tussenstops;
- eindstation;
- stationsnaam en stationscode;
- trein nummer en trein naam;
- exacte volgorde;
- geplande of onderzochte reisdatum;
- aankomst- en vertrektijden waar betrouwbaar beschikbaar;
- stopduur waar betrouwbaar beschikbaar;
- rol `BEGINSTATION`, `TUSSENSTOP` of `EINDSTATION`;
- `mark_boards_here: true|false`;
- `mark_alights_here: true|false`;
- bron, controledatum, onzekerheid en live-recheckmoment.

Alle stations van ieder daadwerkelijk aanbevolen traject komen in een aparte KML-laag `TREINSTATIONS_GRIJS`, met één grijze stijl en één herkenbaar treinlogo. Een treinhalte wordt nooit automatisch formeel of adviserend A/B/C.

Maak daarnaast per treinhalte detectorinput voor een mogelijke latere, afzonderlijk geautoriseerde zware-A-sweep. Deze detectorinput is geen nieuwe clusterstart, geen kandidaatstatus en geen advies.

## Kumaon-KML

`KUMAON_ROUTE_OPTIMIZED.kml` bevat minimaal afzonderlijke lagen voor:

- `A_FORMEEL`;
- `B_FORMEEL`;
- `C_FORMEEL`;
- `D_DOOR_MARK_TE_BEOORDELEN`;
- `CONTEXT_OF_AFGEVALLEN`;
- `ROUTE_VOLGORDE`;
- `BASES_EN_OVERNACHTING`;
- `TREINTRAJECTEN`;
- `TREINSTATIONS_GRIJS`;
- `VLIEGVELDEN_EN_VLUCHTEN` wanneer aanbevolen of dragend vergeleken.

Behoud permanente LOCATION_ID's. Maak geen nieuwe formele of adviserende A/B/C. Route-, base-, station- en vervoerskeuzes zijn reisplanning en wijzigen de inhoudelijke status niet.

## MASTER-INDIA-KML-001

Koppel de gevalideerde runuitkomst aan issue #17 door een technisch overdrachtsbestand te leveren dat exact aangeeft welke Kumaon-lagen, routegeometrie, stations, treintrajecten, basisnachten en eventuele vluchtlagen later in de master-KML kunnen worden opgenomen. Wijzig de master-KML of issue #17 niet rechtstreeks zonder afzonderlijke pin.

## Geen nieuwe brede plaatsensweep

Verboden:

- opnieuw breed zoeken naar alle spirituele plekken in Kumaon;
- opnieuw beoordelen van de 47 predecessorrecords als clusterinventarisatie;
- nieuwe formele of adviserende A/B/C;
- inhoudelijk onderzoek van het gekozen volgende cluster;
- een treinhalte of overstapstad automatisch tot bestemming maken;
- bus als routeoptie;
- auto/taxi als langeafstandsalternatief in de vlakte;
- boekingen uitvoeren;
- tijdgevoelige dienstregeling of prijs als blijvend feit presenteren.

Gericht aanvullend onderzoek is alleen toegestaan voor routeoptimalisatie, vervoer, stationsvolgorde, deur-tot-deurvergelijking, winterhaalbaarheid, basisnachten en concrete open toegangspunten die de routevolgorde materieel beïnvloeden.

## Verplichte run-specifieke outputs

Naast de standaard fase-artifacts levert de keten uiteindelijk minimaal:

- `KUMAON_ROUTE_OPTIMIZED.kml`;
- `intercluster_transport_matrix.jsonl`;
- `train_services.jsonl`;
- `train_stops.jsonl`;
- `route_sequence.jsonl`;
- `base_and_nights_plan.jsonl`;
- `arrival_and_exit_analysis.jsonl`;
- `door_to_door_comparison.jsonl`;
- `train_stop_detector_inputs.jsonl`;
- `live_recheck_register.jsonl`;
- `next_cluster_decision.md`;
- `MASTER_INDIA_KML_LINKAGE.md`;
- `MARK_FINAL_REPORT.md`.

## BRONS-opdracht

BRONS bouwt een brede maar uitsluitend routegerichte eerste onderzoekslaag. BRONS verzamelt actuele primaire en geschikte routebronnen, maakt meerdere expliciete routealternatieven, inventariseert alle benodigde trein- en vluchtdata, registreert onzekerheden en maakt geen eindkeuze die niet door de latere verificatie kan worden heropend. BRONS heropent geen brede Kumaon-kandidateninventarisatie en start geen onderzoek van het volgende cluster.

## ZILVER-opdracht

ZILVER verifieert onafhankelijk de dragende vervoersclaims, volledige stationsreeksen, kostencomponenten, deur-tot-deurtijden, winterfrictie, basiswissels en routealternatieven. ZILVER controleert dat geen bus, lange vlakke autoverplaatsing, nieuwe A/B/C of volgend-clusteronderzoek is binnengeslopen.

## GOUD-opdracht

GOUD synthetiseert één optimale route, één aankomst, eerste basis en eerste formele A, basiswissels en nachten, laatste Kumaon-locatie, beste uitgang, volgend cluster en voorlopige clusterketen. GOUD levert de definitieve datasets, runlokale KML, master-KML-linkage en het volledige Markrapport. GOUD maakt geen boeking en markeert alle live rechecks.

## Compleetheidscriteria

De run kan alleen PASS of PARTIAL opleveren wanneer:

1. iedere relevante formele Kumaon-A in de routeanalyse is verantwoord;
2. aankomst, eerste basis, eerste A, basiswissels, nachten, laatste locatie en uitgang ondubbelzinnig zijn;
3. minimaal de vier verplichte vervolgrichtingen gelijkwaardig zijn vergeleken;
4. trein-vluchtvergelijkingen volledige deur-tot-deurcomponenten bevatten;
5. ieder aanbevolen treintraject alle stations bevat;
6. KML-statussemantiek en grijze treinmarkers exact kloppen;
7. alle tijdgevoelige claims een latere live recheck hebben;
8. geen bus, boeking, brede Kumaon-sweep, volgend-clusteronderzoek of nieuwe formele/adviserende A/B/C is uitgevoerd;
9. issue #17 een valide technische koppeling ontvangt zonder directe masterwijziging.

END_OF_ARTIFACT
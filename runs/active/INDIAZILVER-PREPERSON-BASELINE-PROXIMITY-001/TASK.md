# INDIA ZILVER — PRE-PERSON CLUSTER BASELINE + PROXIMITY BACKFILL

STATUS: READY
OWNER: INDIA ZILVER
MODE: REPO AUDIT + TARGETED GEO/IDENTITY BACKFILL

## Doel
Reconstrueer verliesloos de toestand VOOR de recente persoonsgerichte megasweeps, zodat INDIA8 exact weet welke clusters/regio's/locaties Mark al A/B/C had gegeven, welke clusters werkelijk regionaal compleet/locked waren, welke alleen gekozen maar nog niet regionaal METHOD_V2-afgerond waren, en welke nieuwe persoonsvondsten daarna additief zijn binnengekomen.

Dit is GEEN nieuwe brede discovery-sweep.

## Werkpakket A — PRE-PERSON BASELINE
Lees canonieke governance/ACTIVE_STATE, SWEEP_PROTOCOL, relevante oude run/status/result/decision-registers en legacy benchmark waar governance die expliciet toestaat.

Maak PREPERSON_CLUSTER_BASELINE.md met per cluster/regio minimaal:
- cluster/regio-naam;
- status direct vóór TOP11 person-centric expansion;
- regionale sweep-status en detectorlagen;
- Mark A/B/C aantallen en permanente IDs;
- LOCKED_BY_MARK locaties/hotelbesluiten;
- COMPLETE/SATURATED versus SELECTED_BUT_NOT_REGIONALLY_COMPLETE;
- welke sublocaties reeds impliciet onderdeel waren van een genummerd complex;
- bronpaden/commits.

Maak apart PREPERSON_A_CLUSTER_INDEX.md: ALLE bestaande A/LOCKED_BY_MARK fysieke locaties gegroepeerd naar reiscluster. Geen oude ID wijzigen. Dit bestand moet voorkomen dat een heatmap alleen op persoonscount de oude reiscanon verdringt.

## Werkpakket B — PERSON-DELTA OVERLAY
Gebruik je eerdere CLUSTER_RECALL_AUDIT/REOPEN_AND_ID_QUEUE plus duurzaam afgeronde person/reconciliation outputs om per baseline-cluster te tonen:
- nieuwe fysieke kandidaat sinds baseline;
- duplicate/identity-check tegen bestaande ID;
- city/regio-only lead;
- heritage-stay-impact;
- same-site/multi-person impact;
- nieuwe ID nodig: JA/NEE/ONZEKER;
- Mark A/B/C review nodig: JA/NEE.

Geen bestaande keuze wijzigen.

## Werkpakket C — PROXIMITY / 100-METER-RISICO BACKFILL
Voor alle nieuwe fysieke kandidaten die een bestaande of reeds gekozen reiscluster kunnen beïnvloeden, probeer betrouwbare huidige identiteit + coördinaten/marker te verifiëren. Gebruik actuele publieke bronnen/kaartbronnen waar nodig; NIET raden.

Vergelijk daarna uitsluitend betrouwbare coordinatenparen met bestaande permanente locaties/locked hotels in hetzelfde cluster en classificeer:
SAME_SITE; <=100m; 100-250m; 250-500m; 500m-1km; 1-3km; >3km; UNKNOWN.

Maak PROXIMITY_BACKFILL.md en MISSED_100M_RISK_QUEUE.md. UNKNOWN blijft expliciet UNKNOWN. Prioriteer Varanasi, Kumaon en Bodh Gaya/Gaya-corridor; neem Tiruvannamalai apart op als SELECTED_BUT_NOT_REGIONALLY_COMPLETE, niet als reopen.

## Werkpakket D — CLUSTER STATUS MACHINE
Maak TRAVEL_CLUSTER_STATUS.md met voor elk cluster:
- PREPERSON_STATUS
- PERSON_REVERSE_DONE
- REOPEN_REQUIRED
- IDENTITY_BACKFILL
- PROXIMITY_BACKFILL
- NEW_ID_QUEUE
- MARK_REVIEW_QUEUE
- TRAVEL_MATERIAL_COMPLETE: JA/NEE

Definieer 'cluster' vanuit Marks reisbeslissingen, niet alleen vanuit person-overlapheatmap. Bodh Gaya/Mahabodhi mag dus niet verdwijnen omdat person-count lager is.

## Verboden
- geen IDs renummeren/hergebruiken;
- geen bestaande A/B/C wijzigen;
- geen brede nieuwe spirituele-anchor discovery;
- geen route/nachten/hotelkeuze namens Mark;
- geen PDF/merge/PR.

## Outputs
PREPERSON_CLUSTER_BASELINE.md
PREPERSON_A_CLUSTER_INDEX.md
PERSON_DELTA_OVERLAY.md
PROXIMITY_BACKFILL.md
MISSED_100M_RISK_QUEUE.md
TRAVEL_CLUSTER_STATUS.md
STATUS.md -> COMPLETE

Commit outputs op dezelfde branch.

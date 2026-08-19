# INDIA ROZE — ROUTE BUILDER PREP

STATUS: READY
OWNER: INDIA ROZE
MODE: NON-DESTINATION ROUTE ENGINE PREP

## Doel
Bouw nu al de structuur waarmee later, zodra Mark clusters kiest, in één stap een uitvoerbare reisroute kan worden gegenereerd. Kies nu GEEN bestemmingen en leg GEEN nachten vast.

## Opdracht
Gebruik uitsluitend governance, reisperiode/constraints, bestaande travel-module formats en operationele metadata. Geen nieuw persoons- of locatieonderzoek.

Lever:
1. ROUTE_INPUT_CONTRACT.md — exact welke velden straks per gekozen cluster nodig zijn (minimum/ideal nights, arrival/departure nodes, mandatory site windows, rest need, local transport mode, fixed dates, uncertainty).
2. ROUTE_OPTIMIZATION_RULES.md — technische optimalisatieregels die INDIA8 later zelfstandig mag toepassen: vermijd backtracking, bescherm ankers/fixed dates, buffer voor winter/mist, minimaliseer travel-only dagen, redelijke aankomsttijden, rustdagen, geen onrealistische transfers. Geen echte route uitrekenen.
3. DAY_TEMPLATE_LIBRARY.md — flexibele templates voor aankomstdag, volle spiritual-site dag, mixed sightseeing/spiritual day, transferdag, buffer/rustdag, vroege vlucht/trein, berg/remote-site dag.
4. FINAL_A_Z_DELIVERABLE_SPEC.md — exact formaat van het uiteindelijke reisplan zodat alle teams naar hetzelfde eindproduct werken: dagnummer/datum, slaapplaats, vervoer, tijden/ranges, sites, prioriteit, boeking/deadline, fallback, kostenveld indien later beschikbaar, bron/last-verified.
5. ROUTE_DATA_GAPS.md — welke informatie pas na heatmap/A-B-C nodig is en welke alvast door BLAUW/andere teams kan worden voorbereid.

Geen A/B/C, geen echte bestemmingsselectie, geen nachten, geen PDF, geen merge/PR.
Commit op agent/indiaroze-route-builder-prep en update STATUS.md.

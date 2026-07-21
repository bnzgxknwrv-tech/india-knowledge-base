# ZILVER-audit — VARANASI-COMPLETE-001

## Preflight en claim

- GitHub-read en GitHub-write vóór inhoudelijk werk getest.
- Tijdelijke preflightfile aangemaakt, teruggelezen en verwijderd.
- `NEXT_ACTION`, run, state, events en `ZILVER_CONTEXT` stemden exact overeen.
- Alle 48 required files volledig gelezen; alle gepinde blob-SHA's en sentinels kwamen overeen.
- Geen forbidden file gelezen of gewijzigd.
- `KUMAON-ROUTE-OPTIMIZATION-001` niet gelezen of gewijzigd.
- ZILVER-workerclaim atomisch `ACTIVE` vastgelegd in commit `5becc01f8821298218ab10877db5482e57cbf2dd`.

## Inhoudelijke validatie

- kandidaten: 40 unieke IDs;
- bevestigde identiteiten: 35;
- werkidentiteiten met beperkingen: 3;
- partial identiteiten: 2;
- claims: 57 unieke IDs;
- geaccepteerde bronnen: 25 unieke IDs;
- afgewezen bronnen: 7 unieke IDs;
- ontbrekende claim-source-ID's: 0;
- dubbele IDs over accepted/rejected: 0;
- detectorchecks: 8;
- negatieve zoekrecords: 6;
- working-GEO-records: 40;
- practical-access-records: 40;
- image-records: 40;
- experience-review-records: 40;
- proximity-records: 15.

## Formele A/B- en KML-controle

- 28 formele A exact behouden;
- 2 formele B exact behouden;
- 30 placemarks;
- A-folder en A-stijl uitsluitend groen (`ff00aa00`);
- B-folder en B-stijl uitsluitend oranje (`ff00a5ff`);
- C, stations, routes, bases, hotels en categorie-logo's: 0;
- dubbele niet-lege LOCATION_ID's: 0;
- ontbrekende coördinaten: 0;
- formele of adviserende statuswijzigingen: 0.

## Correcties

- generieke Google Maps-zoeklink verwijderd als dragend bewijs;
- Lahartara teruggebracht tot approximate traditiezone;
- Bhaskarananda/Anand Bagh teruggebracht tot historisch bevestigde relatie met niet-vastgestelde actuele microplek;
- Lahiri Samadhi/Satyalok, Lahiri-huis en Trailanga Math expliciet als werkidentiteiten met beheer-/toegangslimiet;
- nabijheidsrelaties voorzien van rechte-lijnafstanden, zonder route- of tijdclaim;
- beelden en reviews niet kunstmatig opgewaardeerd.

## Scopeverboden

- geen nieuwe formele of adviserende A/B/C;
- geen nieuw decision-ID;
- geen route-, hotel-, basis-, station- of eerste-bezoekkeuze;
- geen PARELS;
- geen wijziging aan de geparkeerde Kumaon-routerun;
- geen GOUD-context gelezen of geschreven tijdens de workerfase.

## Quality gate

Technische integriteit: `PASS`.
Inhoudelijke vrijgavestatus: `PARTIAL`.

Reden: de dataset is bruikbaar en coherent, maar volledige beeld/reviewdekking, veel actuele praktische details en twee micro-identiteiten blijven open.

END_OF_ARTIFACT
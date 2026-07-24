# GEO

Registreer per kandidaat minimaal: candidate_id, naam, coördinaten of NOT_ESTABLISHED, point_type, geo_status, source_ids, gebruikte toegangsmethode, identiteitschecks, wijk of ghat, nabije ankers, afgewezen punten, relevante Mark-afwijzingen, controlerende rol, controledatum en resterende onzekerheid.

GEO-statussen:
- `VERIFIED_GOOGLE_MAPS_PLACE`: plaatsrecord daadwerkelijk geopend en naam, type, locality en context gematcht.
- `VERIFIED_OFFICIAL_MAP_LINK`: officiële kaartlink geopend en gematcht.
- `VERIFIED_SITE_CENTRE`: fysieke complexlocatie met minstens twee geschikte bronnen gekruist.
- `WORKING_CROSSCHECKED_MAP_POINT`: praktisch kaartpunt gekruist op naam, locality en ankers; geen ingangsprecisie geclaimd.
- `APPROXIMATE_LOCAL_POINT`: alleen localityniveau; reden en onzekerheidsradius verplicht.
- `NOT_ESTABLISHED`: geen betrouwbaar punt vastgesteld.
- `TOOL_LIMITED`: bewijs mogelijk, maar vereiste directe controle niet beschikbaar.

Bestaande coördinaten zijn vergelijkingsmateriaal, nooit automatische waarheid. KML-syntax, geldige getallen en marker-aantallen verhogen geen GEO-status. Een expliciet door Mark afgewezen punt mag niet terugkeren zonder later expliciet besluit. Onzekerheid bij één kandidaat blokkeert andere kandidaten niet.

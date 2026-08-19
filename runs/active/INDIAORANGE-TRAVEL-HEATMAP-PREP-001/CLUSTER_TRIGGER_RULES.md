# CLUSTER_TRIGGER_RULES — INDIA ORANJE

Doel: objectief bepalen of na afronding van de landelijke persoonslaag een regionale verificatie/deep sweep nodig is. Deze regels bepalen geen A/B/C en geen route.

## Beslisvolgorde
Een regio krijgt `DEFER` zolang de onderliggende persoonsrecords nog niet voldoende gereconcilieerd zijn om een betrouwbare heatmap te vormen. Zodra de landelijke persoonslaag voor de relevante records is gesloten, pas onderstaande regels toe.

## Trigger = YES
Een regionale deep sweep is gerechtvaardigd wanneer minimaal één van deze procesmatige voorwaarden geldt:

1. **Multi-person cluster:** `unique_person_count >= 2` én er is minimaal één fysieke-site-record (`EXACT_SITE` of `SITE_WITHIN_COMPLEX`).
2. **Dense single-person cluster:** één persoon heeft binnen dezelfde regio meerdere gereconcilieerde fysieke locaties die nog niet op regioniveau op alias/dubbeling/toegankelijkheid zijn gevalideerd.
3. **Conflict concentration:** de regio bevat minimaal één `OPEN_LOCATION_CONFLICT` of meerdere conflicterende records waarvan regionale bron-/siteverificatie het conflict kan oplossen.
4. **Exactness gap:** relevante records clusteren in dezelfde regio maar een substantieel deel blijft `CITY_ONLY`, `REGION_ONLY` of `UNKNOWN`, terwijl exacte fysieke verificatie nodig is vóór reislogistiek.
5. **Cross-person dedup risk:** verschillende personen wijzen naar mogelijk hetzelfde complex/site, maar de bestaande persoonsreconciliaties hebben die relatie nog niet procesmatig vastgesteld.
6. **Locked/known anchor surroundings:** een reeds door Mark gelockt of als hoofdreden vastgelegd anker heeft omliggende gereconcilieerde records die logistiek dezelfde regio vormen; alleen verificatie van de reeds bekende clusterstructuur is toegestaan, geen inhoudelijke herwaardering van het anker.

## Trigger = NO
Geen regionale deep sweep wanneer alle volgende voorwaarden gelden:

- `unique_person_count = 1`;
- slechts één reeds gereconcilieerde fysieke locatie relevant is;
- fysieke exactheid voldoende is voor latere logistieke verificatie;
- geen open locatie-/identiteitsconflict bestaat;
- geen alias/deduplicatierisico zichtbaar is;
- geen governance-opdracht expliciet om regionale verificatie vraagt.

Voor Vivekananda en Hariharananda geldt bovendien de projectgrens: **geen exhaustieve landelijke deep sweep**. Een latere regionale stap mag alleen de grootste/belangrijkste reeds bekende locaties gericht verifiëren nadat de landelijke persoonslaag gereed is.

## Trigger = DEFER
Gebruik `DEFER` wanneer:

- de betrokken persoon/personen nog een open reconciliatie- of detectorgate hebben;
- input uitsluitend uit een blinde detectorfreeze komt en nog niet gereconcilieerd is;
- een open governance-/Mark-besluit nodig is;
- de regio Arunachala/Tiruvannamalai betreft zolang `LOCKED_BY_MARK` van kracht is: geen inhoudelijke regio-sweep starten vanuit deze taak.

## Geen reiswaardering
`unique_person_count`, `location_count`, bewijsniveau en fysieke exactheid zijn uitsluitend signalen voor verificatiewerk. Ze mogen niet automatisch worden vertaald naar A/B/C, aantal nachten, routeprioriteit of travel-significance. `travel_significance` blijft `ONBESLIST`.
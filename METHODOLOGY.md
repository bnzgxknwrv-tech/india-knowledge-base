# METHODOLOGY - Hoe locaties worden beoordeeld en de reis wordt opgebouwd

## Beoordelingssysteem (A+/A/B/C/R)
Het gezaghebbende waarderingssysteem staat in AI_RULES.md en geldt overal:
- A+ = hoogste prioriteit om te bezoeken.
- A = sterke prioriteit, bezoeken.
- B = relevant, secundair, waarschijnlijk bezoeken.
- C = optioneel, waarschijnlijk niet bezoeken (alleen indien onderweg).
- R = afgewezen, niet bezoeken.

Daarnaast bestaat één werkstatus, GEEN waardering:
- U = onbeoordeeld (Mark heeft nog geen waardering toegekend). Dit is de tussenstand vóór een waardering, niet een waardering zelf.

C betekent "waarschijnlijk niet bezoeken", NIET "verwijderen". C-locaties blijven altijd in de database. Doel: de volledige kennisdatabase behouden. Een C-locatie kan later alsnog interessant worden als die logistiek vrijwel gratis tussen meerdere A-locaties meegenomen kan worden. Alleen Mark kent waarderingen (A+/A/B/C/R) toe; U is slechts de status zolang Mark nog niet heeft beoordeeld.

## Analysemethode bij locatie-sweeps
Geen automatische A/B/C. Bij een sweep wordt per locatie eerst getoond:
1. Wat is het?
2. Wie (welke persoon of lijn)?
3. Waarom belangrijk?
4. Reistijd vanaf de CLUSTER_ANCHOR.
5. Reistijd vanaf de dichtstbijzijnde A-locatie.
6. Reistijd vanaf de op een na dichtstbijzijnde A-locatie.
Daarna kiest Mark een waardering: A+, A, B, C of R (of laat de locatie op status U = onbeoordeeld staan).

## Routefilosofie - een bezoekstructuur, niet alleen een lijst
Het doel is niet alleen locaties verzamelen, maar een mogelijke bezoekstructuur bouwen. Model:
CLUSTER_ANCHOR -> locaties -> waardering (A+/A/B/C/R, of status U indien nog onbeoordeeld) -> afstand vanaf anchor -> afstand vanaf dichtstbijzijnde A -> afstand vanaf tweede dichtstbijzijnde A -> logische combinaties -> dagindelingen.
Reistijden worden altijd gemeten vanaf de CLUSTER_ANCHOR.

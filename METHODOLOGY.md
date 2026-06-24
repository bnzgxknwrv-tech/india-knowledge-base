# METHODOLOGY - Hoe locaties worden beoordeeld en de reis wordt opgebouwd

## Beoordelingssysteem (A/B/C/U)
- A = bezoeken.
- B = waarschijnlijk bezoeken.
- C = waarschijnlijk niet bezoeken.
- U = onbeoordeeld.

C betekent "waarschijnlijk niet bezoeken", NIET "verwijderen". C-locaties blijven altijd in de database. Doel: de volledige kennisdatabase behouden. Een C-locatie kan later alsnog interessant worden als die logistiek vrijwel gratis tussen meerdere A-locaties meegenomen kan worden. Alleen Mark kent A/B/C/U toe.

## Analysemethode bij locatie-sweeps
Geen automatische A/B/C. Bij een sweep wordt per locatie eerst getoond:
1. Wat is het?
2. Wie (welke persoon of lijn)?
3. Waarom belangrijk?
4. Reistijd vanaf de CLUSTER_ANCHOR.
5. Reistijd vanaf de dichtstbijzijnde A-locatie.
6. Reistijd vanaf de op een na dichtstbijzijnde A-locatie.
Daarna kiest Mark: A, B, C of U.

## Routefilosofie - een bezoekstructuur, niet alleen een lijst
Het doel is niet alleen locaties verzamelen, maar een mogelijke bezoekstructuur bouwen. Model:
CLUSTER_ANCHOR -> locaties -> A/B/C/U -> afstand vanaf anchor -> afstand vanaf dichtstbijzijnde A -> afstand vanaf tweede dichtstbijzijnde A -> logische combinaties -> dagindelingen.
Reistijden worden altijd gemeten vanaf de CLUSTER_ANCHOR.

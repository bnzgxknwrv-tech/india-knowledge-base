# METHODOLOGY - Hoe locaties worden beoordeeld en de reis wordt opgebouwd

## Beoordelingssysteem (A/B/C/U)
Het gezaghebbende waarderingssysteem staat in AI_RULES.md en geldt overal:
- A = zeker bezoeken.
- B = interessant; Mark beslist later of het meegaat (afhankelijk van hoe zwaar de reis wordt, tijd, energie).
- C = gezien en beoordeeld, maar bewust verworpen. Niet "waarschijnlijk niet" - gewoon niet. (Bij twijfel wordt het B.)

Daarnaast bestaat één werkstatus, GEEN waardering:
- U = onbeoordeeld: wel genoemd, maar Mark heeft er nog geen klasse aan gegeven. Tussenstand vóór een waardering.

C betekent verworpen, maar NIET verwijderen: C-locaties blijven altijd in de database (zie doel: volledige kennisdatabase behouden). Ze worden alleen niet bezocht. Alleen Mark kent waarderingen (A/B/C) toe of laat een locatie op status U staan.

## Analysemethode bij locatie-sweeps
Geen automatische A/B/C. Bij een sweep wordt per locatie eerst getoond:
1. Wat is het?
2. Wie (welke persoon of lijn)?
3. Waarom belangrijk?
4. Reistijd vanaf de CLUSTER_ANCHOR.
5. Reistijd vanaf de dichtstbijzijnde A-locatie.
6. Reistijd vanaf de op een na dichtstbijzijnde A-locatie.
Daarna kiest Mark een waardering: A, B of C (of laat de locatie op status U = onbeoordeeld staan).

## Routefilosofie - een bezoekstructuur, niet alleen een lijst
Het doel is niet alleen locaties verzamelen, maar een mogelijke bezoekstructuur bouwen. Model:
CLUSTER_ANCHOR -> locaties -> waardering (A/B/C, of status U indien nog onbeoordeeld) -> afstand vanaf anchor -> afstand vanaf dichtstbijzijnde A -> afstand vanaf tweede dichtstbijzijnde A -> logische combinaties -> dagindelingen.
Reistijden worden altijd gemeten vanaf de CLUSTER_ANCHOR.

# REISTIJD-WEERGAVE EN LONELY PLANET-LAAG — DURABLE SJABLOON

Datum: 2026-09-30. Van toepassing op alle toekomstige Mark-facing kwartierplannen (niet alleen Kolkata).

## REGEL 1 — REISTIJD-WEERGAVE

Elke transfer toont twee dingen, niet één:
1. **De kale Google Maps-rijtijd** (of live gemeten tijd, als die er is).
2. **Het geplande blok**: Google Maps-tijd + een vaste buffer (~10 minuten, voor het vinden/regelen van vervoer, lopen naar de weg, betalen), fatsoenlijk afgerond op een kwartier.

Voorbeeld: Google Maps 11 min → geplande blok 11:00–11:20 (reistijd) → 11:20–13:00 (op locatie).

Reden: Mark wil het onderscheid tussen "wat de kaart zegt" en "wat realistisch is inclusief zoeken/regelen" zelf kunnen zien, niet een verborgen buffer die de kaart-tijd overschrijft.

## REGEL 2 — GEEN WIJZIGINGSGESCHIEDENIS IN HET MARK-FACING DOCUMENT

Mark, 2026-09-30: *"Dat soort teksten zijn nu oud, maak ze allemaal weg uit zo'n planning. Oud is geweest. [...] Haal dat soort vervuilende oude teksten overal voortaan weg."*

Concreet betekent dit: een kwartierplan-document ("runs/active/..._QUARTERHOUR_PLAN_...") toont **alleen de huidige, geldende staat**. Zinnen als "GECORRIGEERD 29 sep (WORK)...", "verplaatst naar...", "eerder gesteld dat...", "correctie op mezelf..." horen daar niet in, ook niet als de onderliggende correctie zelf waardevol was.

Waar bewaar je die geschiedenis dan wel?
- Een **bindend Mark-besluit** (een downgrade, een geschrapte locatie, een basis-keuze) krijgt een eigen bestand in `decisions/`, zoals `KALIGHAT_AOAY_SOURCING_ERROR_MARK_SKIP_DECISION_2026-09-29.md` — dat bestand MAG de voor-en-na-geschiedenis bevatten, want dat is precies zijn functie.
- Puur proces/onderzoeksgeschiedenis (wie zocht wat, welke aanname bleek onjuist) staat in git-commits en PR #23-comments, niet in het Mark-facing document.

**Wat wél blijft staan in het Mark-facing document:** eerlijkheids-kanttekeningen over de locatie zelf (bijv. "geen AOAY-citaat gevonden voor deze plek", "onzeker of dit nog dezelfde boom is") — dat is geen wijzigingsgeschiedenis, dat is een blijvend feit over de bronkwaliteit van de plek. Het onderscheid: gaat de zin over **hoe het document veranderd is**, of over **wat we wel/niet weten over de plek zelf**? Het eerste eruit, het tweede blijft.

## REGEL 3 — MAGNETISCHE PLEK ALS PROZA, NIET ALS LABEL/BADGE

Mark, 2026-09-30, over de JA/DEELS/NEE-badges in de HTML: *"Haal ja nee buttons weg. Geen idee wat dat zegt."* Het onderliggende criterium (shrine-karakter, foto/altaar/relikwie/kamer vanwege fysieke aanwezigheid) blijft belangrijk, maar wordt **in gewone tekst** verwerkt bij de locatie, niet als apart JA/NEE/DEELS-label of HTML-badge dat uitleg nodig heeft.

## REGEL 4 — LONELY PLANET-LAAG ALS SEPARAAT ONDERZOEK, NIET VIA HET WORK-PR-KANAAL

Voor een gerichte onderzoeksronde naar de Lonely Planet-laag (toeristische bijvangst: musea, monumenten, eetadressen) gebruikt Mark liever een **nieuwe, schone ChatGPT-sessie**, los van het lopende WORK/INDIA25-draadje op PR #23 (dat draadje heeft al veel context/geschiedenis en is bedoeld voor de dual-solve op de kernplanning, niet voor deze losstaande laag). De starter-vraag voor die nieuwe sessie staat in `runs/active/LP_LAAG_FRISSE_CHATGPT_STARTVRAAG_2026-09-30.md` — Mark plakt die tekst zelf in een nieuwe ChatGPT-conversatie.

END

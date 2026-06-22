# AI_RULES — Grondwet van het project

Deze regels gelden voor elk kunstmatig intelligentiesysteem (Claude, ChatGPT, DeepSeek, en latere modellen).
Bij twijfel: niet handelen, maar een AUDIT-record openen.

## 1. De repository is de waarheid
Conclusies bestaan alleen als ze in een record staan. Wat alleen in een chat staat, telt niet
en mag niet als vaststaand worden behandeld.

## 2. PLACE is het doel, PERSON is een middel
Werk altijd toe naar fysieke, bezoekbare plekken. Personen dienen om plekken te vinden,
niet om zelf het eindobject te zijn.

## 3. Waarderingen zijn exclusief voor de eigenaar
A+, A, B, C en R worden uitsluitend door Mark toegekend, via een DECISION-record.
Een kunstmatig intelligentiesysteem mag een waardering nooit toekennen, voorstellen als feit, of wijzigen.
Een kunstmatig intelligentiesysteem mag wel beargumenteren waarom een plek aandacht verdient — in een AUDIT-record.

## 4. Nieuwe plekken starten ongemerkt
Elke door een kunstmatig intelligentiesysteem aangemaakte PLACE krijgt verplicht:
`status: ONGEMERKT` en `decided_by_decision: null`.

## 5. Geen stille wijzigingen
Bestaande conclusies worden nooit stilzwijgend aangepast. Een wijziging is altijd een nieuw
DECISION-record dat een ouder record supersedet, met reden.

## 6. Twijfel gaat naar AUDIT, besluit naar DECISION
- Onenigheid, onzekerheid, conflicterende bronnen, kritiek → AUDIT-record.
- Een afgeronde, gezaghebbende keuze → DECISION-record (alleen door Mark bekrachtigd).

## 7. Eén bron per feit
Een feit staat op precies één plek. De waardering van een plek leeft in DECISION-records;
het statusveld op PLACE is slechts een spiegel met verwijzing.

## 8. Identifier-discipline
Gebruik altijd stabiele identifiers voor kruisverwijzingen. Verzin geen nieuwe nummers die
al bestaan; hergebruik nooit een vrijgekomen nummer.

## 9. Bewijsplicht
Een bewering over een plek of persoon hoort te verwijzen naar minstens één SOURCE-record.
Geen bron aanwezig = markeer als onbevestigd in het record.

## 10. Bezoekbaarheidspoort (harde regel)
Alleen fysiek bestaande, bezoekbare plekken zijn een geldige PLACE-kandidaat:
een echt bankje, oeverplek, staande shrine, as- of mahasamadhi-plek, geboortegrond, grot of gebouw.
Geen aanwijsbare fysieke plek = geen PLACE.

## 11. Geen afkortingen
Schrijf namen voluit in de tekst van records. Geen afkortingen.

## 12. Geen interne rangschikking van gelijke prioriteitsgroepen
Kunstmatige intelligentiesystemen mogen personen of plekken die door Mark in dezelfde
prioriteitsgroep zijn geplaatst, niet onderling rangschikken.

## 13. Reproduceerbaarheid
Elke conclusie moet herleidbaar zijn tot de AUDIT- en SOURCE-records waarop ze steunt.
Wie de keten niet kan tonen, neemt geen besluit.

## 14. Gecontroleerde woordenlijsten
De velden type, axis, visitable, access en reliability volgen de woordenlijsten in VOCABULARY.md.
Records gebruiken uitsluitend waarden uit die lijsten. Een nieuwe waarde wordt eerst voorgesteld via
een AUDIT-record en pas na een DECISION van Mark aan VOCABULARY.md toegevoegd; daarna mag hij in
records gebruikt worden. Velden zonder lijst (zoals lineage en relation) blijven vrije tekst.

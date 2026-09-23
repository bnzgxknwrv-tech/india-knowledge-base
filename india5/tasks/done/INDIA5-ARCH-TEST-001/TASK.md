# TASK.md — INDIA5-ARCH-TEST-001

## Doel

Onschuldige voorbeeldtaak om de volledige levenscyclus van de nieuwe INDIA5-taakarchitectuur
te bewijzen: claim → uitvoering → validatie → completion, inclusief hervatbaarheid. Levert
uitsluitend een testbestand en een validatierapport op — geen India-onderzoek, geen
Varanasi-data, geen protocolwijziging.

## Opdracht

1. Claim deze taak met `india5/scripts/claim_task.py INDIA5-ARCH-TEST-001`.
2. Schrijf `india5/tasks/active/INDIA5-ARCH-TEST-001/TEST_OUTPUT.md` met:
   - een korte bevestiging dat de claim gelukt is;
   - het resultaat van `validate_task.py INDIA5-ARCH-TEST-001 --stage active`.
3. Schrijf `RESULT.md` met de exacte completion_marker (zie `TASK.yaml`).
4. Rond af met `india5/scripts/complete_task.py INDIA5-ARCH-TEST-001`.
5. Commit + push, en bevestig in de resultaatenvelop dat validatie, claim en completion alle
   drie zonder handmatige ingreep zijn gelukt.

## Verwacht bewijs van hervatbaarheid

Beschrijf in `RESULT.md` expliciet: als deze sessie had afgebroken tussen claim en completion,
had een nieuwe sessie de taak teruggevonden in `india5/tasks/active/INDIA5-ARCH-TEST-001/` met
`STATUS.yaml`-state `ACTIVE`, zonder enige aanname uit chatgeschiedenis nodig te hebben.

## Niet doen

- Geen bestanden buiten `india5/tasks/*/INDIA5-ARCH-TEST-001/` aanraken.
- Geen Varanasi-data, geen protocol- of registerbestanden wijzigen.

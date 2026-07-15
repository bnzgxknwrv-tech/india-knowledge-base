# Wereldwijd stabiele plaatsnummering

## Doel

Iedere fysieke plaats krijgt exact één permanente project-ID die in rapporten, kaarten, foto's, routes, decisions en toekomstige runs gelijk blijft.

## Formaat

`IND-PLACE-NNNNNN`

Voorbeelden:

- `IND-PLACE-000001`
- `IND-PLACE-000127`

## Regels

1. Het nummer is wereldwijd uniek binnen het India-project.
2. Een eenmaal uitgegeven ID wordt nooit hergebruikt, ook niet wanneer een kandidaat later C wordt, wordt samengevoegd of niet meer bezocht wordt.
3. Lokale rapportnummers, oude `CLUSTER_LOCATIONS`-nummers en fasegebonden kandidaat-ID's blijven als aliases of legacy references bewaard, maar zijn niet de permanente sleutel.
4. Splitsing van één fysieke kandidaat in twee werkelijk verschillende plaatsen levert een nieuwe ID op voor het afgesplitste object; provenance vermeldt de bron-ID.
5. Samenvoeging verwijdert geen IDs. Eén record wordt canonical; de andere krijgt `record_status: MERGED` en `merged_into`.
6. Alleen SUBREGIE INDIA reserveert nieuwe IDs bij runcreatie of gevalideerde post-run integratie.
7. BRONS mag nieuwe plaatsen voorstellen met tijdelijke run-ID's. Permanente IDs worden pas geschreven nadat fysieke identiteit voldoende is vastgesteld.
8. De volgende vrije ID staat in `knowledge/places/registry_meta.yaml`.
9. A/B/C is geen onderdeel van de ID en kan de ID nooit veranderen.
10. PARELS gebruiken later hetzelfde nummerstelsel, maar worden pas na activering van DECISION-0011 toegevoegd.

## Minimale recordvelden

De canonical registry gebruikt minimaal:

- `place_id`;
- `canonical_name`;
- `aliases`;
- `place_type`;
- `coordinates` en `coordinate_accuracy`;
- `clusters`;
- `formal_status` en `status_decision_id`;
- `document_status`;
- `overlays`;
- `last_content_verified_at`;
- `last_practical_verified_at`;
- `legacy_references`;
- `record_status`.

## Nummeruitgifte

Nieuwe run:

1. lees `registry_meta.yaml`;
2. reserveer alleen het minimaal benodigde blok;
3. schrijf de reservatie in de runscope;
4. verhoog `next_place_number` pas bij daadwerkelijke canonical registratie;
5. sla ongebruikte gereserveerde nummers niet opnieuw uit wanneer zij al in publieke artifacts voorkwamen.

END_OF_ARTIFACT
# CANONICAL_INTEGRATION_PROPOSAL_TEMPLATE v1.0

Bestand voor iedere nieuwe GOUD-run met canonieke integratie:

`research/active/<RUN_ID>/GOUD/CANONICAL_INTEGRATION_PROPOSAL.md`

```markdown
# <RUN_ID> — canoniek integratievoorstel

## 1. Integratiestatus

- mode: `DETERMINISTIC_NON_DECISIONAL`
- registry_update_required: `<YES|NO>`
- decisions_index_update_required: `<YES|NO>`
- mark_decision_required: `<YES|NO>`
- integration_applied: `<YES|NO|BLOCKED>`
- integration_commit: `<sha|NONE>`

## 2. Toegestane deterministische wijzigingen

Beschrijf per bestand exact welke bestaande records of verwijzingen worden bijgewerkt. Alleen toegestaan:

- technische documentstatus en artifactpaden;
- bestaande LOCATION_ID-koppelingen;
- bestaande formele of adviserende status ongewijzigd overnemen;
- bestaande decision-ID's ongewijzigd koppelen;
- gecontroleerde aliases, GEO-statussen en bronverwijzingen die rechtstreeks uit de gevalideerde GOUD-artifacts volgen.

## 3. Verboden wijzigingen

- geen nieuwe formele of adviserende A/B/C-status;
- geen wijziging van bestaande A/B/C-status;
- geen nieuw decision-ID;
- geen nieuwe of herschreven beslistekst;
- geen koerskeuze namens Mark;
- geen wijziging die niet één-op-één uit de gevalideerde GOUD-artifacts volgt.

## 4. Voorgestelde registry-wijzigingen

Per record:

- LOCATION_ID:
- huidig record of relevante velden:
- voorgestelde deterministische wijziging:
- bewijsartifact:
- formele status ongewijzigd: `<JA|NEE>`

## 5. Voorgestelde decisions-indexwijzigingen

Alleen verwijzingen naar reeds bestaande decision-documenten:

- bestaand decision-ID:
- indexwijziging:
- bewijs dat geen nieuwe beslissing wordt gecreëerd:

## 6. Beslissing van Mark vereist

`NONE` of exact de nog niet toegestane keuze. Wanneer Mark een nieuwe A/B/C-status, routekeuze of ander inhoudelijk besluit moet nemen:

- pas de betreffende canonieke wijziging niet toe;
- zet `mark_decision_required: YES`;
- beschrijf in het MARK_FINAL_REPORT exact de keuze en gevolgen;
- archiveer de run niet als volledig geïntegreerd.

## 7. Readback

- registry syntax/JSONL geldig: `<JA|NEE|NOT_APPLICABLE>`
- decisions index syntax geldig: `<JA|NEE|NOT_APPLICABLE>`
- alle LOCATION_ID's uniek: `<JA|NEE|NOT_APPLICABLE>`
- alle decision-ID's bestaand: `<JA|NEE|NOT_APPLICABLE>`
- geen A/B/C-wijziging: `<JA|NEE>`
- finale readback geslaagd: `<JA|NEE>`

END_OF_ARTIFACT
```

GOUD schrijft dit voorstel vóór canonieke writes. Alleen wanneer alle wijzigingen deterministisch, niet-beslissend en volledig controleerbaar zijn, mag GOUD de genoemde canonieke bestanden bijwerken. Bij twijfel of een inhoudelijke keuze is iedere canonieke write verboden.

END_OF_ARTIFACT
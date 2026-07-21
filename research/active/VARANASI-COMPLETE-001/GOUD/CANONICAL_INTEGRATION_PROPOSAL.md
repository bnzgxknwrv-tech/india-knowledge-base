# VARANASI-COMPLETE-001 — canoniek integratievoorstel

## 1. Integratiestatus

- mode: `DETERMINISTIC_NON_DECISIONAL`
- registry_update_required: `YES`
- decisions_index_update_required: `NO`
- mark_decision_required: `NO`
- integration_applied: `NO`
- integration_commit: `PENDING`

## 2. Toegestane deterministische wijzigingen

Uitsluitend twee reeds bestaande canonieke records worden mechanisch aangevuld met de gevalideerde WORKING_GEO uit het repositorybrede A/B-masterregister:

1. `IND-PLACE-000001` — Katyayani Peeth / Keshav Ashram;
2. `IND-PLACE-000002` — Neem Karoli Baba Ashram and Samadhi, Vrindavan.

Per record worden alleen `coordinates`, `coordinate_accuracy`, `last_content_verified_at` en een extra legacy reference naar het gevalideerde masterregister bijgewerkt. Namen, aliases, place types, formele status, status-decision-ID, overlays en recordstatus blijven exact ongewijzigd.

## 3. Verboden wijzigingen

- geen nieuwe formele of adviserende A/B/C-status;
- geen wijziging van bestaande A/B/C-status;
- geen nieuw decision-ID;
- geen nieuwe of herschreven beslistekst;
- geen koerskeuze namens Mark;
- geen nieuwe permanente `IND-PLACE-*`- of LOCATION_ID-toewijzing;
- geen canonieke registratie van de overige 38 masterkaartrecords omdat daarvoor nieuwe permanente place-ID’s nodig zouden zijn;
- geen wijziging onder `research/active/KUMAON-ROUTE-OPTIMIZATION-001/**`.

## 4. Voorgestelde registry-wijzigingen

### IND-PLACE-000001 — Katyayani Peeth / Keshav Ashram

- huidig record: coördinaten `null`, nauwkeurigheid `NOT_ESTABLISHED`;
- voorgestelde wijziging: coördinaten `[27.5796, 77.6974]`, nauwkeurigheid `WORKING_25_100_M`, inhoudscontrole `2026-07-21`, legacy reference `VARANASI-COMPLETE-001:AB-024`;
- bewijsartifact: `research/active/VARANASI-COMPLETE-001/ZILVER/MASTER_A_B_GEO_REGISTRY_VERIFIED.jsonl`, record `AB-024`;
- formele status ongewijzigd: `JA`.

### IND-PLACE-000002 — Neem Karoli Baba Ashram and Samadhi, Vrindavan

- huidig record: coördinaten `null`, nauwkeurigheid `NOT_ESTABLISHED`;
- voorgestelde wijziging: coördinaten `[27.5767, 77.6865]`, nauwkeurigheid `WORKING_25_100_M`, inhoudscontrole `2026-07-21`, legacy reference `VARANASI-COMPLETE-001:AB-025`;
- bewijsartifact: `research/active/VARANASI-COMPLETE-001/ZILVER/MASTER_A_B_GEO_REGISTRY_VERIFIED.jsonl`, record `AB-025`;
- formele status ongewijzigd: `JA`.

## 5. Voorgestelde decisions-indexwijzigingen

`NONE`. Alle relevante bestaande decisions staan reeds in `decisions/INDEX.yaml`. Er wordt geen beslissing toegevoegd of gewijzigd.

## 6. Beslissing van Mark vereist

`NONE`.

## 7. Readback

- registry syntax/JSONL geldig: `PENDING_WRITE`;
- decisions index syntax geldig: `NOT_APPLICABLE`;
- alle LOCATION_ID’s uniek: `NOT_APPLICABLE_TO_CANONICAL_WRITE`;
- alle decision-ID’s bestaand: `JA`;
- geen A/B/C-wijziging: `JA`;
- finale readback geslaagd: `PENDING`.

END_OF_ARTIFACT
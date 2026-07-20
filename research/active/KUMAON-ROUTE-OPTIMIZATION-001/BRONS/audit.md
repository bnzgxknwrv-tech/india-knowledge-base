# BRONS audit — KUMAON-ROUTE-OPTIMIZATION-001

## Context

- source_commit: `dbac7e3e89f275ec1c99bf348da55f6bcf7ac5e8`
- predecessor_completion_commit: `41a77b967d784de5babb67d603becf2b9f2ebf75`
- worker_claim: `ChatGPT-BRONS-KUMAON-ROUTE-001`
- scope: routeoptimalisatie, geen brede sweep
- checked_at: 2026-07-20

## Scope-audit

PASS:
- alle zestien formele Kumaon-A-locaties verantwoord;
- formele B optioneel en alle C zichtbaar;
- geen nieuwe formele of adviserende A/B/C;
- geen bus;
- auto/taxi alleen bergen, kort en first/last mile;
- geen boekingen;
- vier verplichte vervolgclusters vergeleken;
- volledige stationreeksen voor alle aanbevolen treinen;
- 23 kg-vluchtbagage expliciet meegerekend;
- live-recheckregister aanwezig;
- technische master-KML-input aanwezig zonder mastermutatie.

## Bronintegriteit

Accepted sources: 23
Rejected sources: 3
Claims: 16

Alle `source_ids` in claims verwijzen naar exact één record in `sources/registry.jsonl`. Geen claim verwijst naar een afgewezen bron-ID. Het interne 12092-conflict is zichtbaar gemaakt en de onbetrouwbare algemene kop is afgewezen.

## Geen inhoudsverlies

- 16 A, 1 B en 4 C behouden.
- LOCATION_ID 308–310 en 400–443 niet gewijzigd.
- Bodh Ashram blijft A maar route-uitvoering is conditioneel.
- Haidakhan Vishwa Mahadham blijft onderscheiden van Anandapuri/Chiliyanaula-context.
- Treinhaltes blijven detectorinput en geen bestemmingstatus.

## Resultaat

`PARTIAL`

Reden: toekomstige boekbare dienstregeling, winterconditie, Bodh Ashram-toegang en externe stationcoördinaten zijn nog niet definitief verifieerbaar.

END_OF_ARTIFACT

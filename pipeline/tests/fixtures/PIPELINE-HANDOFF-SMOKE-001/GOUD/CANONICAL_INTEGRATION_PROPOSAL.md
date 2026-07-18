# PIPELINE-HANDOFF-SMOKE-001 — canoniek integratievoorstel

## 1. Integratiestatus

- mode: `DETERMINISTIC_NON_DECISIONAL`
- registry_update_required: `YES`
- decisions_index_update_required: `NO`
- mark_decision_required: `YES`
- integration_applied: `YES`, uitsluitend technische artifactpadwijziging in fixturekopie
- integration_commit: `FIXTURE_COMMIT`

## 2. Toegestane deterministische wijzigingen

SYN-PLACE-001 behoudt dezelfde LOCATION_ID en formele status. Alleen artifact_path wijzigt van BRONS naar GOUD.

## 3. Verboden wijzigingen

De gevraagde formele statuswijziging en een nieuw decision-ID zijn niet toegepast.

## 4. Voorgestelde registry-wijzigingen

- LOCATION_ID: SYN-LOC-001
- wijziging: artifact_path naar GOUD/report/anchor.md
- formele status ongewijzigd: JA

## 5. Voorgestelde decisions-indexwijzigingen

NONE.

## 6. Beslissing van Mark vereist

Formele status van SYN-LOC-001 blijft U totdat Mark apart beslist.

## 7. Readback

- registry syntax/JSONL geldig: JA
- decisions index syntax geldig: JA
- alle LOCATION_ID's uniek: JA
- alle decision-ID's bestaand: JA
- geen A/B/C-wijziging: JA
- finale readback geslaagd: JA

END_OF_ARTIFACT

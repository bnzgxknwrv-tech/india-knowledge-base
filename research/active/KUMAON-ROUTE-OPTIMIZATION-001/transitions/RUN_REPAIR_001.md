# RUN_REPAIR — KUMAON-ROUTE-OPTIMIZATION-001-RUN-REPAIR-001

## Probleem

De ZILVER-start stopte terecht omdat `pipeline/NEXT_ACTION.yaml` het veld `source_commit` liet verwijzen naar BRONS-completioncommit `73c11932a17f9ab0186c32621597c21a8f8b1984`. Het verplichte `context/ZILVER_CONTEXT.yaml` bestond daar nog niet; het werd pas aangemaakt in transitioncommit `3eb11704c769e69f1c6533ce3a26249eb0293e92`.

## Classificatie

- foutklasse: `LOCAL_DATA_ERROR`
- risico: ZILVER kan het gepinde contextmanifest niet openen en moet vóór claim stoppen
- actuele reparatie: corrigeer uitsluitend `pipeline/NEXT_ACTION.yaml:source_commit` naar de transitioncommit
- fase-output gewijzigd: nee
- ZILVER-contextinhoud gewijzigd: nee
- worker- of controllerclaim geopend: nee

## Correctie

- vorige waarde: `73c11932a17f9ab0186c32621597c21a8f8b1984`
- correcte waarde: `3eb11704c769e69f1c6533ce3a26249eb0293e92`
- contextpad: `research/active/KUMAON-ROUTE-OPTIMIZATION-001/context/ZILVER_CONTEXT.yaml`
- state blijft: `READY_FOR_ZILVER`

## Systeemles

De transitioncontroller moet onderscheid maken tussen:

1. de predecessor-resultaatcommit die binnen `ZILVER_CONTEXT.yaml` als inhoudelijke bronpin staat;
2. de transitioncommit waar het nieuwe contextmanifest feitelijk bestaat en die in `pipeline/NEXT_ACTION.yaml:source_commit` moet staan.

Structurele protocolwijziging valt buiten deze actieve gepinde run. Beslissing: `DEFER_WITH_REASON`; registreer dit bij eerstvolgend pipeline-onderhoud.

END_OF_ARTIFACT
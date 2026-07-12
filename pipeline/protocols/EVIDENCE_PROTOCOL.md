# Evidence Protocol v2.0

## 1. Claims zijn atomair

Iedere materiële bewering krijgt een `claim_id`, claimtype, bewijsstatus en één of meer `source_id`-verwijzingen. Een bron wordt niet algemeen aan een kandidaat gehangen wanneer zij slechts één deelclaim draagt.

## 2. Claimtypes

Toegestane hoofdtypen:
- `PHYSICAL_IDENTITY`
- `INSTITUTIONAL_IDENTITY`
- `HISTORICAL`
- `TRADITION`
- `LINEAGE`
- `LIVING_PRACTICE`
- `VISITABILITY`
- `TESTIMONY`
- `OVERLAY_RELATION`

## 3. Bewijsstatus

Gebruik uitsluitend:
- `VERIFIED_PRIMARY`
- `VERIFIED_INSTITUTIONAL`
- `SUPPORTED_SECONDARY`
- `INFERRED`
- `CONFLICTED`
- `NOT_ESTABLISHED`

Geen totaalscore per kandidaat.

## 4. claims.jsonl

Minimale velden per regel:
- `claim_id`
- `candidate_id`
- `claim_type`
- `claim_text`
- `evidence_status`
- `source_ids`
- `notes`
- `supersedes_claim_id` indien van toepassing

ZILVER en GOUD overschrijven het voorgangerbestand niet. Zij maken een volledig eigen claimregister voor hun fase, met behoud of expliciete vervanging van geldige claims.

## 5. sources/registry.jsonl

Minimale velden:
- `source_id`
- `url`
- `title`
- `publisher`
- `source_type`
- `retrieved_at`
- `supports_claims`
- `access_status`
- `content_hash` indien betrouwbaar beschikbaar
- `notes`

Toegestane `source_type`:
- `PRIMARY_TEXT`
- `OFFICIAL_INSTITUTION`
- `OFFICIAL_LINEAGE`
- `GOVERNMENT`
- `ACADEMIC`
- `REPUTABLE_SECONDARY`

## 6. rejected.jsonl

Leg afgewezen bronnen vast met:
- `url`
- `reason`
- `searched_for`
- `replacement_source_id` indien gevonden

Zo hoeven latere rollen dezelfde zwakke bron niet opnieuw te beoordelen.

## 7. Onzekerheid blijft lokaal zichtbaar

Onzekerheid staat zowel bij de relevante rapportclaim als in `claims.jsonl`. `audit.md` is niet de enige plaats waar waarschuwingen staan.

## 8. Traditie en lineage

Een officiële tempel-, ashram- of lineagebron kan haar eigen traditie, parampara, praktijk en institutionele identiteit dragen. Zij wordt niet gebruikt als onafhankelijke bevestiging van bovennatuurlijke gebeurtenissen of precieze oude topografie.

## 9. Getuigenissen

Getuigenissen mogen de aantrekkingskracht en levende betekenis illustreren wanneer bron, persoon en context duidelijk zijn. Zij blijven `TESTIMONY` en worden nooit automatisch `HISTORICAL`.

END_OF_ARTIFACT

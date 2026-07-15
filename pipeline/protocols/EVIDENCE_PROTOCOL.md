# Evidence Protocol v3.0

## 1. Atomische claims

Iedere materiële bewering krijgt een `claim_id`, `candidate_id`, `claim_type`, `claim_text`, `evidence_status`, één of meer `source_ids`, `notes` en waar relevant `supersedes_claim_id`.

Een bron wordt alleen gekoppeld aan de specifieke claim die zij daadwerkelijk draagt.

## 2. Claimtypes

Toegestane hoofdtypen:

- `PHYSICAL_IDENTITY`
- `INSTITUTIONAL_IDENTITY`
- `HISTORICAL`
- `TRADITION`
- `LINEAGE`
- `LIVING_PRACTICE`
- `DEVOTIONAL_PURPOSE`
- `PARTICIPATION`
- `VISITABILITY`
- `EXPERIENCE`
- `VISUAL_CONDITION`
- `PROXIMITY`
- `TESTIMONY`
- `OVERLAY_RELATION`

## 3. Bevestigingsstatussen

Gebruik uitsluitend:

- `HISTORICALLY_DOCUMENTED`
- `INSTITUTIONALLY_CONFIRMED`
- `LINEAGE_CONFIRMED`
- `TRADITION_CONFIRMED`
- `EXPERIENTIALLY_REPORTED`
- `PRACTICAL_CHECK_REQUIRED`
- `SUPPORTED_SECONDARY`
- `INFERRED`
- `CONFLICTED`
- `NOT_ESTABLISHED`

De status geldt per claim, niet per kandidaat. Bevestigingsdomeinen staan naast elkaar en vormen geen rangorde.

## 4. Projectbevestiging

Een claim kan `project_confirmation: true` krijgen wanneer zij voor Marks pelgrimsdoel voldoende wordt gedragen door een relevante instelling, lineage of levende traditie, ook wanneer klassiek historisch bewijs ontbreekt.

Vereist:

- de drager van de bevestiging is expliciet genoemd;
- de bron staat aantoonbaar dicht bij de betreffende instelling of lineage;
- fysieke plek en spirituele relatie zijn niet kunstmatig samengevoegd;
- concrete tegenspraak is onderzocht en zichtbaar gemaakt.

## 5. Babaji en bovennatuurlijke traditieclaims

Een Babaji-claim wordt niet beoordeeld op moderne biografische bewijsbaarheid. Zij wordt beoordeeld op nabijheid van de lijnbron, guru-parampara, interne consistentie, de fysieke plek die de traditie aanwijst en de daaruit voortgekomen levende praktijk.

## 6. AOAY

Wanneer AOAY een relevante persoon, ontmoeting of regionale relatie beschrijft en een huidige officiële instelling of lineage de eigen fysieke plek daarmee identificeert, kan de overlay `PROJECT_CONFIRMED` zijn tenzij concrete tegenspraak bestaat.

Een gecontroleerde editie en exacte historische topografie blijven nuttige documentaire verdieping, maar zijn niet verplicht om de plek voor Marks reisdoel betekenisvol bevestigd te noemen.

## 7. Brontypen

Toegestane `source_type`:

- `PRIMARY_TEXT`
- `OFFICIAL_INSTITUTION`
- `OFFICIAL_LINEAGE`
- `GOVERNMENT`
- `ACADEMIC`
- `REPUTABLE_SECONDARY`
- `DEVOTEE_TESTIMONY`
- `VISITOR_REVIEW`
- `INTERVIEW`
- `VIDEO_DOCUMENTATION`
- `PHOTO_DOCUMENTATION`
- `ROUTE_SOURCE`

Bronnen worden gebruikt voor het domein waarvoor zij geschikt zijn. Reviews, foto's en video's mogen uiterlijk, sfeer, drukte, gastvrijheid, netheid en praktische beleving dragen. Zij dragen geen oude historische of bovennatuurlijke kernclaim.

## 8. Visueel dossier

Per kandidaat wordt een image register bijgehouden met minimaal:

- `image_id`
- `candidate_id`
- `url`
- `source_type`
- `captured_or_published_at` indien bekend
- `retrieved_at`
- `visual_function`
- `observation_supported`
- `duplicate_group` indien relevant
- `reliability_notes`

Doel is tien verschillende visuele functies. Een tekort wordt expliciet gerapporteerd; duplicaten vullen het quotum niet kunstmatig.

## 9. Reviews en ervaringsmateriaal

Leg bij reviewanalyse vast:

- platform;
- score en aantal reviews indien zichtbaar;
- peildatum;
- actualiteit;
- terugkerende positieve thema's;
- terugkerende negatieve thema's;
- verschil tussen devotee- en algemene toeristenervaringen;
- betrouwbaarheid van de basis.

Eén review of één sterrengemiddelde is nooit voldoende voor een algemene sfeerclaim.

## 10. Praktische onzekerheid

Actuele toegang, deelname, fotografie, kleding, openingstoestand en tijdelijke beperkingen krijgen `PRACTICAL_CHECK_REQUIRED` wanneer zij niet betrouwbaar actueel zijn vastgesteld. Dit vermindert niet automatisch de spirituele of traditionele betekenis van de plek.

## 11. Registers en referentiële integriteit

Iedere `source_id` uit `claims.jsonl` moet exact één keer bestaan in accepted of rejected registers. Source-ID's zijn uniek over beide registers. Afgewezen bronnen krijgen eveneens een unieke ID wanneer claims ernaar verwijzen.

## 12. Geen totaalscore door de metalen

BRONS, ZILVER en GOUD leveren de inhoudelijke gegevens voor advisering, maar kennen geen formele A/B/C-status toe. Alleen INDIA2 mag adviseren en alleen Mark beslist formeel.

END_OF_ARTIFACT
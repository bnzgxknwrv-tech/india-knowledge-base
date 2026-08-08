# ACTIVE_STATE — centrale, versie-onafhankelijke overdrachtswaarheid

**Een nieuwe INDIA-regisseursessie moet eerst ACTIVE_STATE + actieve protocolcanon lezen. Oude
chatgeschiedenis is niet vereist voor correcte voortzetting.**

Datum: 2026-08-08
Repository: `bnzgxknwrv-tech/india-knowledge-base`
Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR: `#23` (draft; niet mergen zonder expliciete vrijgave van Mark)

Deze locatie (`governance/`) is de canonieke overdrachtswaarheid, niet gebonden aan een
specifieke regisseursessie. `india5/INDIA3_HANDOFF.md` en `india5/ACTIVE_STATE.md` zijn
gedateerd/gedeprecieerd en verwijzen hierheen (zie hun eigen kop). GitHub is waarheid voor
overdraagbare projectkennis — niet chatgeheugen.

```
PROJECT: India-pelgrimsroute-onderzoek voor Mark (bnzgxknwrv-tech/india-knowledge-base, PR #23)
CURRENT_REGISSEUR_ROLE: INDIA (rolgebaseerd — huidige regisseursessie is vervangbaar, niet canoniek)
CURRENT_SESSION_LABEL: INDIA6 (informatief, niet functioneel vereist)
ACTIVE_PROTOCOL: governance/SWEEP_PROTOCOL.md (ACTIEF/CANONIEK) + india4/protocols/INDIA5-PROTOCOL.md
  + india4/protocols/INDIA5_REGION_START_PROTOCOL.md + india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md
LAST_GLOBAL_LOCATION_NUMBER: 078 (BODHGAYA; VARANASI eindigt op 045, geen overlap)
PDF_STATUS: VERBODEN (projectbreed default; per taak expliciet PDF_GO: JA vereist, zie
  governance/SWEEP_PROTOCOL.md poort M/N)
OPEN_SYSTEM_DECISIONS:
  - Tweede, ongebruikte taakarchitectuur onder india5/tasks/ (TASK.yaml/STATUS.yaml) — reactiveren,
    archiveren of samenvoegen met Coverage Matrix/Lead Register? Nog niet besloten.
  - Of Coverage Matrix/Lead Register-inhoud (niet alleen statusvolledigheid) verder machinaal
    gevalideerd moet worden, naast de huidige governance/scripts/preflight_validator.py.
  - Concreet minimum voor een geldige adversarial pass (poort I) nog niet formeel vastgelegd.
LAST_RELEVANT_COMMIT: (zie onderaan dit bestand, wordt bijgewerkt per commit)

REGIONS:

  VARANASI:
    fase: MAINTENANCE_STATUS (sweep afgesloten, PR #23, 2026-08-03)
    saturation-status: SATURATED (afgesloten vóór introductie van dit tokenformaat)
    INDIA_ACCEPTED_SATURATION: JA (impliciet — afsluitbesluit INDIA2, vóór dit tokenformaat bestond)
    Mark-selection-status: 001-040 volledig beoordeeld (A: 32, B: 5, C: 3); 041-045 PROVISIONAL,
      geen A/B/C, wacht op Marks eigen initiatief
    protected A/B/C-besluiten: alle 40 (001-040), plus hotel VNS-HOTEL-001 = LOCKED_BY_MARK
      (Sahi River View Guesthouse)
    reserved/excluded nummers: geen excluded; 041-045 blijven PROVISIONAL/DOOR_MARK_TE_BEOORDELEN
    blockers: geen actieve; open onzekerheden (VNS-CAND-008 coördinaat, VNS-CAND-023 ~3km
      brondiscrepantie, ontbrekende Google Maps-markers) staan gedocumenteerd in
      runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/VARANASI_FINAL_STATUS.md, geen van alle
      blokkeert MAINTENANCE_STATUS
    next_allowed_step: geen — alleen bij expliciet Mark-verzoek of concreet nieuw bewijs voor een
      NOT_TO_BE_MISSED-locatie

  BODHGAYA:
    fase: GOUD (keuzerapport geschreven en content-QA-gecorrigeerd; wacht op finale acceptatie)
    saturation-status: SATURATED=JA (SATURATION_REPORT_002.md + _003_ADDENDUM.md)
    INDIA_ACCEPTED_SATURATION: JA (geaccepteerd, bericht 028)
    Mark-selection-status: nog GEEN A/B/C — MARK_SELECTION_REPORT.md staat klaar voor Marks eigen
      keuze, content-QA-ronde verwerkt (geen voorspellende A/B/C-taal, sourcing/toegankelijkheid
      gecorrigeerd)
    protected A/B/C-besluiten: nog geen (Mark heeft nog niet gekozen)
    reserved/excluded nummers: 069 (Mongolian Temple) = EXCLUDED_HARD_REASON; 075 (Jain Temple
      Gaya) = EXCLUDED_HARD_REASON; 076 (Akshayavat) = SUBLOCATION, samengevoegd bij 051
      (Vishnupad Temple), geen zelfstandige kandidaat — alle drie nummers permanent gereserveerd,
      nooit hergebruikt
    blockers: geen open content-blocker meer na de QA-ronde (bericht 030); wacht op INDIA/Mark om
      MARK_SELECTION_REPORT.md inhoudelijk te accepteren
    next_allowed_step: content-QA-acceptatie (CONTENT_QA_ACCEPTED: JA) door de huidige
      INDIA-regisseur; PAS DAARNA, en alleen met een apart, letterlijk PDF_GO: JA, mag een PDF
      gebouwd worden (30 actieve keuzelocaties, 046-078 minus 069/075/076, plus Mahabodhi
      weeksublocaties zonder eigen nummer)
```

## Governance-canon (versie-onafhankelijk, deze map)

- `governance/SWEEP_PROTOCOL.md` — ACTIEF/CANONIEK sweep-protocol (poorten A-Q), aanvulling op
  de bestaande negen-stappenflow.
- `governance/SWEEP_ERROR_CLASSES.md` — ACTIEF foutklassenregister (FK-001 t/m FK-011).
- `governance/scripts/preflight_validator.py` — machine-checkbare structurele preflight vóór
  keuzerapportfase en vóór PDF (zie SWEEP_PROTOCOL.md Deel 4 voor de exacte grenzen).
- `governance/ACTIVE_STATE.md` — dit bestand.

### Discriminatieregel MARK_WAARDIG (canoncorrectie 2026-08-08, duurzaam te erven)

Elke toekomstige INDIA-regisseur/CCI-uitvoering erft automatisch de beslisvolgorde uit
`governance/SWEEP_PROTOCOL.md` poort E.1: (1) AOAY-link (*Autobiography of a Yogi*) = absolute
override, altijd tonen, ook bij een objectief onbeduidende plek; (2) zonder AOAY-link: Top-X
persoonlijke zwaarte, breed zoeken, lage drempel; (3) alles daarbuiten: religieuze/bedevaarts-
zwaargewicht met een HOGE drempel — nooit "elke religie moet vertegenwoordigd zijn." Coverage van
religies/tradities (poort A) is uitsluitend een zoeklens, nooit zelfstandig bewijs voor
kandidaatstatus. Zie `governance/SWEEP_ERROR_CLASSES.md` FK-011 voor het Bodh Gaya-precedent
(Mongolian Temple, 069).

## Nog geldige, ongewijzigde canon buiten `governance/`

- `india4/protocols/INDIA5-PROTOCOL.md` — hoofdprotocol (PDF-poort, bestandsnaamgeving,
  Verzadigingsdrempel).
- `india4/protocols/INDIA5_REGION_START_PROTOCOL.md` — negen-stappenflow per regio.
- `india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md` — MARK_WAARDIG-hoofdvraag + acht regels.

## Rollen (rolgebaseerd, niet sessienaam-gebonden)

- **Mark**: bepaalt doel/scope, maakt alle definitieve A/B/C-keuzes, geeft `PDF_GO: JA` en
  content-acceptatie.
- **Huidige INDIA-regisseur** (`CURRENT_REGISSEUR_ROLE`, vandaag ingevuld door de sessie met
  label INDIA6): regisseert, bewaakt canon, controleert saturatie-evidence
  (`INDIA_ACCEPTED_SATURATION: JA`) en content (`CONTENT_QA_ACCEPTED: JA`). Niet canoniek/
  onmisbaar — een toekomstige INDIA7/INDIA8/... erft deze rol volledig via dit bestand plus de
  actieve protocolcanon, nooit via chatgeschiedenis.
- **CCI (ClaudeCodeIndia)**: uitvoerende engine — onderzoek, datasets, rapporten, commits. Bouwt
  uitsluitend een PDF na een letterlijk `PDF_GO: JA`.

---
Geschreven door: CCI, bijgewerkt na protocolreview van de huidige INDIA-regisseur (PR #23,
bericht 034). Geen PDF, geen nieuwe regionale sweep, geen A/B/C, geen route/pacing.
`PDF_STATUS: VERBODEN` gerespecteerd tijdens het schrijven van dit document.

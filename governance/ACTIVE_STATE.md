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
MARKS_REISPERIODE: 18 december 2026 t/m 21 januari 2027 (bron: INDIA6 bericht 055/057) — alle
  keuze-relevante festival-/evenement-/toegangsinformatie in kandidaatteksten wordt hiertegen
  gecontroleerd, niet tegen een oud/generiek festivaljaar (zie governance/SWEEP_PROTOCOL.md poort N)
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
    fase: MARK_SELECTION_KLAAR + AOAY/Top-11-audit KLAAR — wacht op Marks beslissing over 2
      MARK_DECISION_CONFLICTs (051, 074), daarna PRE_PDF_CONTENT.md voor een V2_-PDF
    saturation-status: SATURATED=JA (SATURATION_REPORT_002.md + _003_ADDENDUM.md)
    INDIA_ACCEPTED_SATURATION: JA (geaccepteerd, bericht 028)
    CONTENT_QA_ACCEPTED: JA (bericht 048, gold voor V1); PDF_GO: JA (bericht 048, V1 gebouwd) —
      voor een V2_ is een nieuw, apart PRE_PDF_CONTENT_APPROVED: JA + PDF_GO: JA vereist
    AOAY_TOP11_AUDIT: KLAAR (bericht 054, 2026-08-08) — volledige AOAY-primaire-tekstsweep (1
      treffer: Sri Yukteswars Swami-inwijding "door de Mahant van Buddh Gaya", AOAY ch.36) + alle
      11 Top-11-namen individueel onderzocht. 4 LINK_GEVONDEN (Sri Yukteswar, Ramakrishna,
      Vivekananda -> 046, reeds A, verrijking; Anandamayi Ma -> 051; Ram Dass -> 074), 7 geen link
      gevonden. Volledige matrix: runs/active/BODHGAYA-DISCOVERY-001/PRE_BRONS/AOAY_TOP11_AUDIT.md
    Mark-selection-status: MARK_SELECTION_KLAAR: JA (bericht 053, 2026-08-08). A: 046, 047, 048,
      049. B: 050, 052, 070, 073. C: 051, 058, 060, 061, 062, 063, 068, 071, 072, 074, 077, 078.
      Alle 20 nummers LOCKED_BY_MARK — geen open kandidaten meer, BEHALVE 2 open
      MARK_DECISION_CONFLICTs hieronder.
    MARK_DECISION_CONFLICTs (open, niet zelfstandig door CCI opgelost): **051** Vishnupad Temple
      (huidig: C) — Anandamayi Ma-link (Top-11 #7) pas ontdekt na de C-keuze. **074** Dhamma
      Bodhi/Samanvaya Ashram (huidig: C) — Ram Dass-link (Top-11 #5) pas ontdekt na de C-keuze.
      Beide expliciet gemarkeerd in MARK_SELECTION_REPORT.md; wacht op Mark/INDIA6-beslissing of
      dit de bestaande C-keuzes verandert.
    protected A/B/C-besluiten: 046-049 = A (bron: MARK_DECISIONS_2026-08-05.jsonl); 050-078-groep
      zie hierboven (bron: runs/active/BODHGAYA-DISCOVERY-001/MARK_DECISIONS_2026-08-08.jsonl,
      LOCKED_BY_MARK, mag niet stilzwijgend heropend worden — alleen expliciet via de 2
      MARK_DECISION_CONFLICTs hierboven)
    reserved/excluded nummers: 069, 075 = EXCLUDED_HARD_REASON (eerder); 053, 054, 055, 056, 057,
      059, 064, 065, 066, 067 = EXCLUDED_HARD_REASON (2026-08-08, retroactieve E.1-canontoets,
      INDIA6 bericht 042 — enige resterende onderscheiding was land-/traditievertegenwoordiging
      of pure architectuur, geen zelfstandige bedevaarts-/heilige zwaarte); 076 (Akshayavat) =
      SUBLOCATION, samengevoegd bij 051 (Vishnupad Temple) — alle 13 uitgesloten/sublocatie-
      nummers blijven permanent gereserveerd, nooit hergebruikt
    blockers: wacht op Mark/INDIA6-beslissing over de 2 MARK_DECISION_CONFLICTs (051, 074) vóórdat
      PRE_PDF_CONTENT.md definitief kan worden opgesteld voor een V2_-PDF
    PDF geleverd: runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/V1_BODHGAYA_KEUZE_REISGIDS.pdf
      (19 pagina's, commit 5910439) — eerste build onder de V1_-naamgevingsregel voor deze run;
      GEEN nieuwe A/B/C-status meer, PDF toont de OUDE open/twijfelgeval-labels — vervangen zodra
      een V2_ wordt gebouwd, niet tussentijds herbouwd
    PRE_PDF_CONTENT geleverd: runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/PRE_PDF_CONTENT.md —
      volledige beoogde V2-PDF-inhoud (20 kandidaatkaarten met alle 10 verplichte velden,
      beslismatrix, clusteroverzicht, de 2 MARK_DECISION_CONFLICTs zichtbaar gemarkeerd), NOG GEEN
      PDF gerenderd
    next_allowed_step: INDIA leest PRE_PDF_CONTENT.md volledig, geeft correcties (verwerkt in
      hetzelfde bestand) of `PRE_PDF_CONTENT_APPROVED: JA`; pas daarna, met een apart, letterlijk
      `PDF_GO: JA`, mag V2_ gerenderd worden
```

## Governance-canon (versie-onafhankelijk, deze map)

- `governance/SWEEP_PROTOCOL.md` — ACTIEF/CANONIEK sweep-protocol (poorten A-Q), aanvulling op
  de bestaande negen-stappenflow.
- `governance/SWEEP_ERROR_CLASSES.md` — ACTIEF foutklassenregister (FK-001 t/m FK-011).
- `governance/scripts/preflight_validator.py` — machine-checkbare structurele preflight vóór
  keuzerapportfase en vóór PDF (zie SWEEP_PROTOCOL.md Deel 4 voor de exacte grenzen).
- `governance/ACTIVE_STATE.md` — dit bestand.

### Reisdoel-prioriteit: AOAY + Top-X = missiekritisch, rest = bonus (canoncorrectie 2026-08-08, bericht 044)

Marks eigenlijke reisdoel is (1) AOAY (*Autobiography of a Yogi*) en (2) de **definitieve Top-11**
— NIET een gelijkwaardige derde categorie naast "overige bedevaartsplekken". Elke regio-sweep is
verplicht tot een 100%-sweep van deze twee lagen (elke AOAY-plek, elke Top-11-persoon een eigen
detector — zie `governance/SWEEP_PROTOCOL.md` poort A/E.1) VÓÓRDAT algemene bedevaarts-
"bonusmateriaal"-kandidaten mogen meetellen als bewijs voor een sweep-brede `SATURATED=JA`-claim
(harde volgordedwang, poort C/J). Praktisch gevolg, letterlijk zoals door Mark bedoeld: een
obscure schuur waar Yogananda aantoonbaar mediteerde staat qua keuzeprioriteit BOVEN een enorm
bedevaartsoord met miljoenen bezoekers — geen inconsistentie, maar het punt van de hele reis. Dit
verandert NIETS aan de MARK_WAARDIG-gate zelf (nog steeds geen quotum, geen filtering op
verwachte A/B/C) — het bepaalt uitsluitend zoekvolgorde/-diepte en saturatie-afhankelijkheid.

**Definitieve Top-11 (canoncorrectie 2026-08-08, bericht 046 — vervangt elke eerdere, bredere
Top-X-omschrijving)**: Paramahansa Yogananda, Mahavatar Babaji, Lahiri Mahasaya, Sri Yukteswar,
Ram Dass, Neem Karoli Baba, Anandamayi Ma, Ramakrishna, Ramana Maharshi, Hariharananda,
Vivekananda. Apart, met een eigen expliciet gewenste Mahasamadhi-locatie in Delhi: **Shri Mataji
Nirmala Devi** (buiten de Top-11, wel missiekritisch voor die ene locatie). **Boeddha en Krishna
staan NIET in de Top-11** — beiden zijn te groot/alomtegenwoordig, wat kandidaat-inflatie zou
veroorzaken (elke gewone boeddhistische/Krishna-tempel zou anders automatisch missiekritisch
worden). Boeddha-/Krishna-kandidaten worden voortaan uitsluitend onder laag 3 beoordeeld (hoge,
zelfstandige-zwaarte-drempel) — Mahabodhi Temple/Bodh Gaya blijft daar vanzelfsprekend kandidaat
omdat de plek zelf die drempel overduidelijk haalt.

### Discriminatieregel MARK_WAARDIG (canoncorrectie 2026-08-08, verscherpt dezelfde dag, duurzaam te erven)

Elke toekomstige INDIA-regisseur/CCI-uitvoering erft automatisch de beslisvolgorde uit
`governance/SWEEP_PROTOCOL.md` poort E.1: (1) AOAY-link (*Autobiography of a Yogi*) = absolute
override, altijd tonen, ook bij een objectief onbeduidende plek; (2) zonder AOAY-link: Top-X
persoonlijke zwaarte, breed zoeken, lage drempel; (3) alles daarbuiten: **religie-onafhankelijke**
bedevaarts-/pelgrimszwaarte met een HOGE drempel. De zoekvraag is NIET "welke belangrijke religies
zijn hier aanwezig?" maar UITSLUITEND "welke fysieke plekken hebben hier uitzonderlijke
religieuze/spirituele/pelgrimszwaarte?" — een grote wereldreligie geeft op zichzelf geen recht op
opname; een obscure/kleine traditie met één plaats van enorme pelgrimszwaarte moet juist boven
komen. Religiecategorieën (poort A) zijn hoogstens aanvullende zoektermen, nooit de begrenzing van
de zoekruimte en nooit zelfstandig bewijs voor kandidaatstatus. Zie
`governance/SWEEP_ERROR_CLASSES.md` FK-011 voor het Bodh Gaya-precedent (Mongolian Temple, 069).

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
  (`INDIA_ACCEPTED_SATURATION: JA`) en content (`PRE_PDF_CONTENT_APPROVED: JA`, vervangt het oude
  losse `CONTENT_QA_ACCEPTED: JA` voor PDF-doeleinden — zie governance/SWEEP_PROTOCOL.md poort M).
  Niet canoniek/onmisbaar — een toekomstige INDIA7/INDIA8/... erft deze rol volledig via dit
  bestand plus de actieve protocolcanon, nooit via chatgeschiedenis. **Actieplicht (bericht 057)**:
  als INDIA constateert dat iets inhoudelijk noodzakelijk moet gebeuren, mag dat niet eindigen als
  passieve TODO — INDIA voert het zelf uit met beschikbare tools of geeft in dezelfde beurt een
  concrete CCI-opdracht. Alleen blokkeren bij werkelijk ontbrekende informatie/toestemming.
- **CCI (ClaudeCodeIndia)**: uitvoerende engine — onderzoek, datasets, rapporten, commits. Bouwt
  uitsluitend een PDF na `PRE_PDF_CONTENT_APPROVED: JA` én een apart, letterlijk `PDF_GO: JA`.

---
Geschreven door: CCI, bijgewerkt na protocolreview van de huidige INDIA-regisseur (PR #23,
bericht 034). Geen PDF, geen nieuwe regionale sweep, geen A/B/C, geen route/pacing.
`PDF_STATUS: VERBODEN` gerespecteerd tijdens het schrijven van dit document.

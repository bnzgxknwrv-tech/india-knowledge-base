# ACTIVE_STATE — centrale, versie-onafhankelijke overdrachtswaarheid

**Een nieuwe INDIA-regisseursessie moet eerst ACTIVE_STATE + actieve protocolcanon lezen. Oude
chatgeschiedenis is niet vereist voor correcte voortzetting.**

Datum: 2026-08-14
Repository: `bnzgxknwrv-tech/india-knowledge-base`
Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR: `#23` (draft; niet mergen zonder expliciete vrijgave van Mark)

Deze locatie (`governance/`) is de canonieke overdrachtswaarheid, niet gebonden aan een
specifieke regisseursessie. `india5/INDIA3_HANDOFF.md` en `india5/ACTIVE_STATE.md` zijn
gedateerd/gedeprecieerd en verwijzen hierheen (zie hun eigen kop). GitHub is waarheid voor
overdraagbare projectkennis — niet chatgeheugen. **Sinds 2026-08-08 (poort O.1)**: PR #23 is
index/relay met KORTE enveloppen (task_id/status/commit), niet meer het volledige transcript —
de daadwerkelijke inhoud van elke lopende taak staat in `TASK.md`/`STATUS.md`/`RESULT.md` onder
`runs/active/<TASK_ID>/`, waarvan de paden hieronder bij `ACTIVE_TASKS` staan. **Sinds 2026-08-14**:
`governance/INDIA_SESSION_START.md` is de duurzame bootstrap voor een nieuwe INDIA-regisseursessie.
Ook sinds 2026-08-14: dit project heeft een EERDERE architectuur gehad (`KUMAON-COMPLETE-001` e.a.,
zie branch `controller/kumaon-complete-001-ready-for-zilver-20260719`) met een eigen, incompatibele
nummering (`CLUSTER_LOCATIONS.md` #1-46, plus een nooit-toegepast `LOCATION_ID`-clusterblokschema
uit `DECISION-0013`). Die branch is nooit gemerged en die nummering wordt NIET hergebruikt — de
huidige, doorlopende globale nummering (dit bestand, `LAST_GLOBAL_LOCATION_NUMBER`) is leidend.
Mark-besluiten (LOCKED_A/B/C) uit die legacy-branch blijven wel inhoudelijk geldig en worden bij
reconciliatie geraadpleegd als benchmark, zie `runs/active/KUMAON-V2-RESWEEP-001/RECONCILIATION.md`.

```
PROJECT: India-pelgrimsroute-onderzoek voor Mark (bnzgxknwrv-tech/india-knowledge-base, PR #23)
WAAROM_MARK_REIST: een persoonlijke pelgrimsreis langs (1) verifieerbare fysieke plekken uit/
  verbonden met *Autobiography of a Yogi* en (2) plekken verbonden aan zijn persoonlijke Top-11
  (zie hieronder) — dat is het eigenlijke reisdoel, missiekritisch. Overige, objectief zware
  bedevaartsplekken zijn bonusmateriaal, alleen bij hoge zelfstandige zwaarte (zie
  "Reisdoel-prioriteit" hieronder).
MARKS_REISPERIODE: 18 december 2026 t/m 21 januari 2027 (bron: INDIA6 bericht 055/057) — alle
  keuze-relevante festival-/evenement-/toegangsinformatie in kandidaatteksten wordt hiertegen
  gecontroleerd, niet tegen een oud/generiek festivaljaar (zie governance/SWEEP_PROTOCOL.md poort N)
CURRENT_REGISSEUR_ROLE: INDIA (rolgebaseerd — huidige regisseursessie is vervangbaar, niet canoniek)
CURRENT_SESSION_LABEL: INDIA6 (informatief, niet functioneel vereist)
ACTIVE_PROTOCOL: governance/SWEEP_PROTOCOL.md (ACTIEF/CANONIEK) + india4/protocols/INDIA5-PROTOCOL.md
  + india4/protocols/INDIA5_REGION_START_PROTOCOL.md + india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md
  + governance/INDIA_SESSION_START.md (bootstrap-samenvatting)
LAST_GLOBAL_LOCATION_NUMBER: 081 (KUMAON; 079 Mahavatar Babaji's Cave, 080 Turiya Niwas, 081 Bodh
  Ashram -- alle drie A, LOCKED_BY_MARK. 079 gereconcilieerd 2026-08-14 uit CCI Sweep A + INDIA
  Sweep B + legacy KUMAON-COMPLETE-001 #15/PLACE-0001. 080/081 toegekend 2026-08-15 na
  miss-root-cause-rescue (CCI_TASK 078) -- beide legacy #36/#37, door beide nieuwe sweeps gemist,
  herverifieerd en zonder Mark-conflict alsnog toegekend; zie runs/active/KUMAON-V2-RESWEEP-001/
  MISS_ROOT_CAUSE_RESCUE.md. Coordinaten voor alle drie nog open. BODHGAYA eindigt op 078;
  VARANASI eindigt op 045, geen overlap; corridor-taak GAYA-AIRPORT-BODHGAYA-CORRIDOR-001 leverde
  0 nieuwe nummers op. Overige KUMAON-V2-RESWEEP-001-kandidaten blijven tijdelijke sweep-ID's.)
PDF_STATUS: VERBODEN (projectbreed default; per taak expliciet PDF_GO: JA vereist, zie
  governance/SWEEP_PROTOCOL.md poort M/N)
DOUBLE_SWEEP_PROTOCOL_CANONICAL: JA (bericht 059, 2026-08-08) — geen regionale sweep geldt als
  inhoudelijk compleet zonder een echt onafhankelijke tweede sweep + reconciliatie (governance/
  SWEEP_PROTOCOL.md poort R, foutklasse FK-012). Geldt voor toekomstige regio's; Bodh Gaya's al
  lopende reconciliatie (bericht 058) wordt er niet retroactief door geblokkeerd.
HUMAN_TOUCHPOINTS_MINIMIZED: JA (bericht 060, 2026-08-08, governance/SWEEP_PROTOCOL.md poort S) —
  GitHub/PR #23 is de communicatie-/state-laag tussen INDIA en CCI, niet Mark. Mark geeft de
  initiële sweepvraag, persoonlijke voorkeuren/canonbesluiten en de uiteindelijke A/B/C-keuzes, en
  beslist alleen bij echte, bronnelijk onoplosbare ambiguïteit (bijv. een openstaande
  `MARK_DECISION_CONFLICT`). CCI en INDIA lezen elkaars GitHub-uitvoer rechtstreeks en handelen
  zelfstandig — geen fictieve automatisering geclaimd: INDIA kan niet autonoom draaien of door CCI
  worden aangeroepen, maar zodra een kant een PR-comment/commit van de andere leest, volgt de
  eerstvolgende eigen actie zonder dat Mark als koerier hoeft te fungeren.
INGETROKKEN_CANONPOGING (2026-08-08, bericht 061): een "DELTA-ONLY herbeoordeling"-poort werd
  kort gecanoniseerd en is diezelfde dag door INDIA6 INGETROKKEN als permanente regel — bedoeld was
  alleen een eenmalig praktisch hulpmiddel voor de huidige Bodh Gaya-correctieronde, niet een
  algemene regel voor toekomstige sweeps (die moeten juist zulke late correcties voorkomen via
  poort R's dubbele sweep + integrale pre-PDF-QA). `governance/SWEEP_PROTOCOL.md` bevat GEEN
  poort T meer; het praktische bijproduct `DELTA_REVIEW_2026-08-08.md` voor Bodh Gaya blijft
  gewoon bestaan als eenmalig documenten, niet als canonprecedent.
ACTIVE_TASKS (bron van waarheid voor lopende taken — PR #23 is index/relay met KORTE enveloppen,
  niet meer het volledige transcript; zie governance/SWEEP_PROTOCOL.md poort O.1, 2026-08-08):
  - task_id: GAYA-AIRPORT-BODHGAYA-CORRIDOR-001
    task_file: runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/TASK.md
    status_file: runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/STATUS.md
    result_file: runs/active/GAYA-AIRPORT-BODHGAYA-CORRIDOR-001/RESULT.md
    state: DOUBLE_SWEEP_COMPLETED_RECONCILED (2026-08-14) — 0/0 nieuwe fysieke kandidaten,
      afgerond, geen verder actief werk.
  - task_id: KUMAON-V2-RESWEEP-001
    task_file: runs/active/KUMAON-V2-RESWEEP-001/TASK.md
    status_file: runs/active/KUMAON-V2-RESWEEP-001/STATUS.md
    result_file: runs/active/KUMAON-V2-RESWEEP-001/RESULT.md
    reconciliation_file: runs/active/KUMAON-V2-RESWEEP-001/RECONCILIATION.md
    state: RECONCILED_PARTIAL (2026-08-14) — 079 (Babaji-grot) permanent/A/LOCKED_BY_MARK;
      overige Sweep-A/Sweep-B-kandidaten blijven tijdelijk, zie RECONCILIATION.md voor
      NEXT_ALLOWED_STEP per cluster.
OPEN_SYSTEM_DECISIONS:
  - Tweede, ongebruikte taakarchitectuur onder india5/tasks/ (TASK.yaml/STATUS.yaml) — BESLOTEN
    (2026-08-08, RELAY-MIGRATION-001): expliciet overwogen voor het nieuwe TASK.md/STATUS.md-
    /RESULT.md-patroon (poort O.1), maar te zwaar bevonden (sha256-hash-pinning, allow/forbid-
    ACL's, completion-markers zonder duidelijke meerwaarde hier) — NIET gereactiveerd. Blijft
    ongebruikt/gedeprecieerd; het lichtere `runs/active/<TASK_ID>/TASK.md`+`STATUS.md`-patroon is
    nu de canonieke aanpak voor taakbestanden.
  - Of Coverage Matrix/Lead Register-inhoud (niet alleen statusvolledigheid) verder machinaal
    gevalideerd moet worden, naast de huidige governance/scripts/preflight_validator.py — inclusief
    of poort R's nieuwe reconciliatiegate-tokens (DOUBLE_SWEEP_COMPLETED e.a.) een scriptcheck
    moeten krijgen.
  - Concreet minimum voor een geldige adversarial pass (poort I) voor de bonusmateriaal-laag (laag
    3) nog niet formeel vastgelegd — voor de missiekritische laag is dit inmiddels wel hard gezet
    via poort R (dubbele onafhankelijke sweep verplicht).
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
    fase: KEUZEFASE INHOUDELIJK AFGEROND (2026-08-08, Mark rechtstreeks + INDIA6 bericht 066) —
      MARK_SELECTIE_KLAAR + AOAY/Top-11-audit KLAAR + reconciliatie KLAAR + alle drie
      MARK_DECISION_CONFLICTs opgelost (bericht 065). GEEN V2-PDF meer — zie
      BODHGAYA_PDF_V2_CANCELLED_BY_MARK hieronder. Aanvullende corridor-taak
      GAYA-AIRPORT-BODHGAYA-CORRIDOR-001 (zie ACTIVE_TASKS) is DOUBLE_SWEEP_COMPLETED_RECONCILED.
    BODHGAYA_PDF_V2_CANCELLED_BY_MARK: JA (2026-08-08) — Mark rechtstreeks in chat: "Geen pdf
      meer!!!"; onafhankelijk bevestigd door INDIA6 (PR #23, bericht 066): "MARK-BESLUIT: GEEN
      NIEUWE BODH GAYA-PDF MEER." Bestaande A/B/C-keuzes (incl. 051=C, 061=C, 074=C) blijven
      leidend en ONGEWIJZIGD. Dit annuleert uitsluitend de PDF-STAP, niet het onderzoek/de
      besluiten zelf — alle onderzoeksdata, correcties en governance-learnings blijven intact
      voor latere route-/reisplanning.
    saturation-status: SATURATED=JA (SATURATION_REPORT_002.md + _003_ADDENDUM.md)
    INDIA_ACCEPTED_SATURATION: JA (geaccepteerd, bericht 028)
    CONTENT_QA_ACCEPTED: JA (bericht 048, gold voor V1); PDF_GO: JA (bericht 048, V1 gebouwd) —
      een V2_-PDF wordt NIET meer gebouwd (zie BODHGAYA_PDF_V2_CANCELLED_BY_MARK); V1 blijft de
      laatst geleverde, gedateerde PDF, niet vervangen
    AOAY_TOP11_AUDIT: KLAAR (bericht 054, 2026-08-08; GERECONCILIEERD 2026-08-08 na een
      onafhankelijke INDIA6-tegencontrole, bericht 058) — volledige AOAY-primaire-tekstsweep (1
      treffer: Sri Yukteswars Swami-inwijding "door de Mahant van Buddh Gaya", AOAY ch.36) + alle
      11 Top-11-namen individueel onderzocht, daarna elk gemeld discrepantiepunt opnieuw tegen
      bronnen getoetst. Volledige matrix:
      runs/active/BODHGAYA-DISCOVERY-001/PRE_BRONS/AOAY_TOP11_AUDIT.md
    Mark-selection-status: MARK_SELECTIE_KLAAR: JA (bericht 053, 2026-08-08). Alle 20 nummers
      LOCKED_BY_MARK — geen open kandidaten, geen open MARK_DECISION_CONFLICTs meer.
    protected A/B/C-besluiten: 046-078, LOCKED_BY_MARK, mag niet stilzwijgend heropend worden
    reserved/excluded nummers: 069, 075 = EXCLUDED_HARD_REASON; 053-057, 059, 064-067 =
      EXCLUDED_HARD_REASON (2026-08-08); 076 (Akshayavat) = SUBLOCATION van 051; corridor-taak
      leverde geen nieuwe nummers op
    blockers: geen — enige "blocker" is permanent/gewenst: GEEN PDF meer bouwen
    next_allowed_step: GEEN inhoudelijke PDF-stap meer voor Bodh Gaya.

  KUMAON (V2-RESWEEP):
    fase: RECONCILED_PARTIAL (2026-08-15, na miss-root-cause-rescue) — zie ACTIVE_TASKS voor
      taakpointer.
    permanent: 079 = Mahavatar Babaji's Cave (Kukuchina/Dunagiri, Dwarahat); 080 = Turiya Niwas
      (Crank's Ridge, kluizenaarswoning Sunyata Sorensen); 081 = Bodh Ashram (voormalig landgoed
      Evans-Wentz/Lama Govinda, bezocht door Anandamayi Ma + Neem Karoli Baba) — alle drie A,
      LOCKED_BY_MARK. 080/081 toegekend na gerichte rescue-audit (CCI_TASK 078, 2026-08-15) nadat
      bleek dat beide nieuwe sweeps ze gemist hadden; root cause + fix in runs/active/
      KUMAON-V2-RESWEEP-001/MISS_ROOT_CAUSE_RESCUE.md. Coordinaten voor alle drie nog niet
      geverifieerd.
    protocolwijziging (2026-08-15): governance/SWEEP_PROTOCOL.md poort E.1 minimaal gepatcht na
      dit incident — (1) Top-11-zoeken moet ook host-/gastheer-/landgoedketens meenemen, niet
      alleen de eigen instellingen van een Top-11-naam; (2) laag 3 bevestigt expliciet dat
      informele, niet-institutionele historische verblijfplaatsen (geen tempel/complex) evengoed
      MARK_WAARDIG kunnen zijn.
    legacy: KUMAON-COMPLETE-001 (branch controller/kumaon-complete-001-ready-for-zilver-20260719)
      had al 28 eigen LOCKED_A-locaties voor deze regio (Kainchi Dham, Kasar Devi, Jageshwar,
      Haidakhan, Hanuman Garhi, Chitai Golu Devta, Ramakrishna Kutir, Bhumiyadhar e.a.) plus 4
      LOCKED_C (bewust afgewezen: Mirtola, Binsar, Patal Bhuvaneshwar, Dhaulchina) en 2 LOCKED_B
      (Ghorakhal, en Vrindavan-item buiten scope). Gebruikt als benchmark bij reconciliatie, niet
      als discovery-basis tijdens Sweep A/B (blindheidsregel correct toegepast). Rescue-audit op
      alle 16 Kumaon-LOCKED_A's: 12 door minstens één sweep gevonden, 2 lage-ernst sub-
      locatiemisses zonder actie nodig (Babaji Smriti Bhavan, Crank's Ridge — beide onderdeel van
      een wél gevonden cluster), 2 hoge-ernst misses nu gerescued (080, 081).
    blockers: geen.
    next_allowed_step: coordinaten voor 079/080/081 verifiëren; Bhumiadhar/Bhumiya Dhara-
      identiteit verder uitzoeken; per resterend Sweep-B-Vivekananda-circuitpunt identity-check
      tegen legacy vóór verdere permanente toekenning. Zie runs/active/KUMAON-V2-RESWEEP-001/
      RECONCILIATION.md + MISS_ROOT_CAUSE_RESCUE.md voor volledige details.
```

## Governance-canon (versie-onafhankelijk, deze map)

- `governance/SWEEP_PROTOCOL.md` — ACTIEF/CANONIEK sweep-protocol (poorten A-Q), aanvulling op
  de bestaande negen-stappenflow.
- `governance/SWEEP_ERROR_CLASSES.md` — ACTIEF foutklassenregister (FK-001 t/m FK-011).
- `governance/scripts/preflight_validator.py` — machine-checkbare structurele preflight vóór
  keuzerapportfase en vóór PDF (zie SWEEP_PROTOCOL.md Deel 4 voor de exacte grenzen).
- `governance/ACTIVE_STATE.md` — dit bestand.
- `governance/INDIA_SESSION_START.md` — duurzame bootstrap-samenvatting voor een nieuwe
  INDIA-regisseursessie.

### Reisdoel-prioriteit: AOAY + Top-X = missiekritisch, rest = bonus (canoncorrectie 2026-08-08, bericht 044)

Marks eigenlijke reisdoel is (1) AOAY (*Autobiography of a Yogi*) en (2) de **definitieve Top-11**
— NIET een gelijkwaardige derde categorie naast "overige bedevaartsplekken". Elke regio-sweep is
verplicht tot een 100%-sweep van deze twee lagen (elke AOAY-plek, elke Top-11-persoon een eigen
detector — zie `governance/SWEEP_PROTOCOL.md` poort A/E.1) VÓÓRDAT algemene bedevaarts-
"bonusmateriaal"-kandidaten mogen meetellen als bewijs voor een sweep-brede `SATURATED=JA`-claim
(harde volgordedwang, poort C/J).

**Definitieve Top-11**: Paramahansa Yogananda, Mahavatar Babaji, Lahiri Mahasaya, Sri Yukteswar,
Ram Dass, Neem Karoli Baba, Anandamayi Ma, Ramakrishna, Ramana Maharshi, Hariharananda,
Vivekananda. Apart: Shri Mataji Nirmala Devi (Delhi Mahasamadhi-locatie). Boeddha en Krishna staan
NIET in de Top-11.

### Discriminatieregel MARK_WAARDIG (canoncorrectie 2026-08-08)

(1) AOAY-link = absolute override; (2) zonder AOAY-link: Top-11 persoonlijke zwaarte, breed
zoeken, lage drempel; (3) alles daarbuiten: religie-onafhankelijke bedevaarts-/pelgrimszwaarte met
HOGE drempel. Zie `governance/SWEEP_ERROR_CLASSES.md` FK-011 voor het Bodh Gaya-precedent.

## Nog geldige, ongewijzigde canon buiten `governance/`

- `india4/protocols/INDIA5-PROTOCOL.md` — hoofdprotocol (PDF-poort, bestandsnaamgeving,
  Verzadigingsdrempel).
- `india4/protocols/INDIA5_REGION_START_PROTOCOL.md` — negen-stappenflow per regio.
- `india4/protocols/NOT_TO_BE_MISSED_FRAMEWORK.md` — MARK_WAARDIG-hoofdvraag + acht regels.

## Rollen (rolgebaseerd, niet sessienaam-gebonden)

- **Mark**: bepaalt doel/scope, maakt alle definitieve A/B/C-keuzes, geeft `PDF_GO: JA` en
  content-acceptatie.
- **Huidige INDIA-regisseur**: regisseert, bewaakt canon, controleert saturatie-evidence en
  content. Niet canoniek/onmisbaar — een toekomstige INDIA7/INDIA8/... erft deze rol volledig via
  dit bestand plus de actieve protocolcanon, nooit via chatgeschiedenis.
- **CCI (ClaudeCodeIndia)**: uitvoerende engine — onderzoek, datasets, rapporten, commits. Bouwt
  uitsluitend een PDF na `PRE_PDF_CONTENT_APPROVED: JA` én een apart, letterlijk `PDF_GO: JA`.

---
Geschreven door: CCI, bijgewerkt na reconciliatie van KUMAON-V2-RESWEEP-001 (2026-08-14, poort R).
Geen PDF, geen A/B/C voor andere locaties dan 079, geen route. `PDF_STATUS: VERBODEN` gerespecteerd
tijdens het schrijven van dit document.

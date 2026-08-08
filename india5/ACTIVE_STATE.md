# ACTIVE_STATE — actuele, versie-onafhankelijke overdracht

Datum: 2026-08-08
Repository: `bnzgxknwrv-tech/india-knowledge-base`
Werkbranch: `claude/werk-je-nu-of-niet-oa10y7`
PR: `#23` (draft; niet mergen zonder expliciete vrijgave van Mark)

Dit bestand vervangt `india5/INDIA3_HANDOFF.md` als het actuele aanspreekpunt voor een nieuwe
regisseurssessie. Het oudere bestand blijft staan als historisch document (niet verwijderd),
maar is gedateerd en gebruikt een oude naam/tellerstand. Zie de doorverwijzing bovenaan
`INDIA3_HANDOFF.md`.

## Kernprincipe: GitHub is waarheid, niet chatgeheugen

- De huidige regisseur heet **INDIA6**, maar dat nummer/die naam is niet canoniek en niet
  onmisbaar. Elke toekomstige regisseursversie (INDIA7, INDIA8, ...) erft de regisseursrol
  uitsluitend via wat er in deze repository staat — nooit via herinnering aan een eerdere
  chatsessie, die per definitie niet overdraagbaar is.
- **CCI (ClaudeCodeIndia)** is de uitvoerende engine: leest/schrijft GitHub, doet onderzoek,
  bouwt datasets/kandidatenlijsten/rapporten en commits. Bouwt uitsluitend een PDF na een
  letterlijk `PDF_GO: JA`-token (default: `PDF_STATUS: VERBODEN`, zie
  `india4/protocols/INDIA5-PROTOCOL.md`).
- **Mark** bepaalt doel/scope, maakt alle definitieve A/B/C-keuzes, beslist over PDF-builds en
  lost inhoudelijke tegenstrijdigheden op.
- Een nieuwe sessie (van welke kant dan ook) moet dit bestand + de actieve protocolbestanden
  kunnen lezen en zonder oude chatgeschiedenis verder kunnen.

## Canonieke protocolbestanden (actief, ongewijzigd van kracht)

- `india4/protocols/INDIA5-PROTOCOL.md` — hoofdprotocol, inclusief PDF-poort
  (`PDF_STATUS`/`PDF_GO`) en bestandsnaamgevingsregel (V1_/V2_ vooraan).
- `INDIA5_REGION_START_PROTOCOL.md` — canonieke negen-stappenflow per regio.
- `NOT_TO_BE_MISSED_FRAMEWORK.md` — hoofdvraag + acht regels voor MARK_WAARDIG-bepaling.
- `india4/protocols/SWEEP_PROTOCOL_V1_PROPOSAL.md` + `india4/protocols/FOUTKLASSEN_REGISTER.md`
  — **VOORSTEL**, nog NIET bindend. Wordt pas canoniek na een expliciet
  `SWEEP_PROTOCOL_V1: GEACCEPTEERD`-besluit van INDIA6 of Mark. Tot die tijd blijft de bestaande
  negen-stappenflow + Verzadigingsdrempel ongewijzigd de geldende procedure.

## Tweede, ongebruikte architectuur (open ontwerpvraag)

Naast bovenstaande, feitelijk gebruikte bestanden bestaat een parallelle, eerder opgezette
taakarchitectuur onder `india5/` (`GOVERNANCE.md`, `TASK_PROTOCOL.md`, `india5/tasks/` met
`TASK.yaml`/`STATUS.yaml`, `india5/schemas/`). Gebruikt voor de eerste Varanasi-coverage-taak
(`INDIA5-VNS-DISCOVERY-COVERAGE-003`, done), maar niet voor Bodh Gaya, en
`INDIA5-VNS-DISCOVERY-SATURATION-004` staat nog altijd "active" en lijkt verlaten. INDIA6 moet
beslissen of dit gereactiveerd, gearchiveerd, of samengevoegd wordt met de nieuwe Coverage
Matrix/Lead Register-bestanden uit `SWEEP_PROTOCOL_V1_PROPOSAL.md` — zie de
"Openstaande ontwerpbeslissingen" sectie in dat voorstel.

## Actuele status Bodh Gaya (run BODHGAYA-DISCOVERY-001)

- Permanente nummering: **046-078** (globaal gevalideerd, geen overlap met VARANASI 001-045).
- **069 (Mongolian Temple)** en **075 (Jain Temple Gaya)**: `EXCLUDED_HARD_REASON` — nummer
  permanent gereserveerd, nooit hergebruikt, niet actief in het keuzerapport.
- **076 (Akshayavat)**: geen zelfstandige keuzelocatie — samengevoegd bij 051 (Vishnupad
  Temple) omdat de boom fysiek binnen die tempelbinnenplaats ligt. Nummer permanent
  gereserveerd.
- Resultaat: **30 actieve keuzelocaties** (046-078 minus 069/075/076, plus de Mahabodhi
  weeksublocaties in Deel 3 die geen eigen nummer hebben).
- `GOUD/MARK_SELECTION_REPORT.md`: volledige proza voor alle actieve kandidaten geschreven,
  content-QA-ronde (bericht 030) verwerkt — geen voorspellende A/B/C-taal meer (geverifieerd via
  grep), sourcing versterkt voor 072 (Pali-canon/Malalasekera/Xuanzang/archeologie i.p.v.
  Alamy/fandom), toegankelijkheid geverifieerd/expliciet onzeker gemaakt voor 063/073/074/077.
  Wacht op finale inhoudelijke acceptatie door INDIA6/Mark.
- **Geen PDF gebouwd** sinds de PDF-gate-aanscherping. `build_pdf.py` staat klaar met
  `V1_BODHGAYA_046_058_KEUZE_REISGIDS.pdf` als outputnaam (dekt vooralsnog alleen 046-058;
  uitbreiding naar de volledige 046-078-set is nog niet gebouwd) — build vereist een letterlijk
  `PDF_GO: JA` van Mark/INDIA6.
- `SWEEP_PROTOCOL_V1_PROPOSAL.md` + `FOUTKLASSEN_REGISTER.md`: geschreven als reactie op
  INDIA6 bericht 031 (systeemtaak), status **VOORSTEL**, wacht op acceptatiebesluit.

## Communicatiecanon (ongewijzigd)

Eén gezamenlijke, oplopende berichtenteller over alle CCI/INDIA-berichten in PR #23-comments,
geen `antwoord op`, geen aparte tellers per afzender. Bij een nummercollision: expliciet
benoemen en doorschuiven naar het eerstvolgende vrije nummer (precedent: 022→023, 031→032).
Laatste bericht vóór dit bestand: CCI-bericht **032** (reactie op INDIA6 bericht 031).

---
Geschreven door: CCI, op verzoek van INDIA6 (PR #23, bericht 031), als vervanging van het
gedateerde `india5/INDIA3_HANDOFF.md`. Geen PDF, geen nieuwe regionale sweep, geen A/B/C, geen
route/pacing. `PDF_STATUS: VERBODEN` gerespecteerd.

# TASK — TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001

```
task_id: TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001
cci_task: CCI_TASK 090
issued_by: INDIA7
issued_at: 2026-08-19
target_branch: claude/werk-je-nu-of-niet-oa10y7
state_on_issue: READY_FOR_CCI
pdf_status: VERBODEN
```

## 1. Doel

Heropen uitsluitend de grootste corpusgaten uit CCI_TASK 089 voor Neem Karoli Baba en Ram Dass,
vóór externe vergelijking.

Doelbronnen:

### Neem Karoli Baba
1. Ram Dass, *Miracle of Love*
2. Dada Mukerjee, *By His Grace*

### Ram Dass
3. Ram Dass, *Be Here Now*
4. *Sacred Wanderer* en/of de in CCI_TASK 089 bedoelde kernbiografische bronfamilie rond Ram Dass'
   Indiareizen; identificeer titel/auteur/uitgave exact en voorkom titelverwarring.

Dit is een gerichte source-recovery- en corpus-extractietaak. Geen brede nieuwe persoonsweep en
geen externe reconciliatie.

## 2. Blindheidsgrens — HARD

Open of gebruik NIET:

- `agent/chatgpt-top11-parallel-sweep`;
- de externe NKB- of Ram-Dass-freezes, counts, bronlijsten of commits;
- IndiaROOD-resultaten;
- oude METHOD_V1/PHASE2-atlassen als discoverychecklist.

De bestaande interne CCI_TASK 089-freezes mogen wel worden gelezen: dit is hun gerichte
corpuscompletion-pass. Externe vergelijking volgt pas na een nieuwe INDIA-opdracht.

## 3. Bronherstelroutes

Probeer per doelbron meerdere legale, onafhankelijke routes:

- officiële auteur-/organisatie-/uitgeverspagina;
- bibliotheek- of archiefcatalogus met toegestane digitale inzage;
- Internet Archive/Open Library of andere rechtmatig toegankelijke uitleen-/previewroute;
- Google Books of uitgeverspreview;
- officiële hoofdstukextracten, interviews of auteurspagina's;
- lokaal/repo-beschikbaar bronbestand indien aanwezig;
- andere gezaghebbende bron die de relevante tekst rechtstreeks reproduceert.

Niet doen:

- paywalls, loginbeveiliging, robotsblokkades of technische toegangscontrole omzeilen;
- een zoeksnippet of AI-samenvatting als bronpassage behandelen;
- een externe kandidatenlijst gebruiken om in het boek naar bevestiging te zoeken;
- lange auteursrechtelijk beschermde passages in de repo kopiëren.

Per route vastleggen: URL/bron, toegangsdatum, bereikbaarheid, doorzoekbaarheid, welk deel zichtbaar
was en waarom `FULL`, `PARTIAL`, `UNAVAILABLE` of `BRON_GEBLOKKEERD`.

## 4. Lossless extractie uit iedere herstelde bron

Voor ieder daadwerkelijk leesbaar deel:

1. lees corpus-first, niet kandidaat-first;
2. registreer iedere India-gerelateerde fysieke plaatsoccurrence;
3. bewaar huizen, kamers, veranda's, tuinen, hotels, stations, wegen, ziekenhuizen, ashrams,
   tempels, retraites en naamloze verblijfplaatsen;
4. onderscheid strikt:
   - NKB persoonlijk aanwezig;
   - Ram Dass persoonlijk aanwezig;
   - verhaal over de ander zonder aanwezigheid van de onderzochte persoon;
   - latere instelling/herdenking;
   - visionair/postuum/symbolisch;
   - plaats alleen als context;
5. leg bronlocator, aanwezigheidstype en fysieke-identiteitstatus vast;
6. noteer negatieve bevindingen en persoonsverwisselingen.

Gebruik bij *Miracle of Love* en *By His Grace* verhalen over NKB niet automatisch als Ram
Dass-locaties. Gebruik bij *Be Here Now* een door Ram Dass verteld NKB-verhaal niet automatisch als
NKB-locatie zonder duidelijke gebeurtenisprovenance.

## 5. Verplichte output

Schrijf:

- `runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/SOURCE_RECOVERY_RESULT.md`;
- `runs/active/TOP11-NKB-RAMDASS-CORE-SOURCE-RECOVERY-001/STATUS.md`.

Werk bronmatig bij, zonder oude rows stil te overschrijven:

- `runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/NEEM_KAROLI_BABA_V2_PRE_EXTERNAL_FREEZE.md`;
- `runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/RAM_DASS_V2_PRE_EXTERNAL_FREEZE.md`;
- de betrokken taak-STATUS;
- `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/STATUS.md`;
- `governance/INDIA_SESSION_START.md`.

Per persoon verplicht rapporteren:

- eerdere recordcount;
- nieuwe rechtstreeks uit kernbron geëxtraheerde occurrences/records;
- duplicates versus echte toevoegingen;
- gecorrigeerde aanwezigheid-/identiteitsclaims;
- actuele corpuscoverage-matrix;
- resterende bronblokkades;
- herziene pre-external gates;
- eerlijke saturationstatus.

## 6. Checkpoints

1. Werk de twee NKB-bronnen af en commit NKB-source-recovery als checkpoint.
2. Werk daarna de twee Ram-Dass-bronfamilies af en commit Ram-Dass-source-recovery als checkpoint.
3. Commit finale status/governance afzonderlijk indien nodig.

Bij contextverlies hervat vanaf het laatste checkpoint. Geen afgerond bronpakket opnieuw starten.

## 7. Stopvoorwaarde

Stop wanneer alle vier doelbronfamilies minimaal via meerdere legale routes zijn onderzocht en
iedere toegankelijke passage lossless is verwerkt, óf wanneer per bron een concrete blocker is
bewezen.

Plaats één CCI_RESULT-envelop op PR #23 met:

- checkpointcommits;
- bronstatus per werk;
- recorddelta per persoon;
- gates en resterende blockers;
- bevestiging dat externe freezes niet zijn geopend;
- exact `next_allowed_step`.

## 8. Harde grenzen

- Geen externe freeze/reconciliatie.
- Geen IndiaROOD lezen.
- Geen Ramana/Ramakrishna starten.
- Geen AOAY-brede sweep.
- Geen cluster/regio of heatmap.
- Geen A/B/C namens Mark.
- Geen permanente IDs.
- Geen PDF.
- Geen route/nachten/vervoer.
- Geen PR #24 of externe branch wijzigen/mergen.
- STOP na resultaatenvelop; wacht op INDIA-QA.

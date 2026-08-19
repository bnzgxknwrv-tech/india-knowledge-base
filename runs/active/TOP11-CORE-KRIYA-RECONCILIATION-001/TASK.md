# TASK — TOP11-CORE-KRIYA-RECONCILIATION-001

```
task_id: TOP11-CORE-KRIYA-RECONCILIATION-001
cci_task: CCI_TASK 088
issued_by: INDIA7
issued_at: 2026-08-19
target_branch: claude/werk-je-nu-of-niet-oa10y7
state_on_issue: READY_FOR_CCI
pdf_status: VERBODEN
```

## 1. Doel

Voer de eerste volledige, bidirectionele METHOD_V2-reconciliatie uit voor:

1. Mahavatar Babaji
2. Lahiri Mahasaya
3. Sri Yukteswar

De interne CCI_TASK 087/087R pre-external freezes en de onafhankelijk bevroren externe
ChatGPT-sweeps zijn nu beide beschikbaar. Vergelijk ze pas in deze taak. Controleer claims
rechtstreeks bij de bron; AI-consensus of herhaling is nooit bewijs.

Dit is GEEN nieuwe blanco discoveryrun en GEEN regionale/cluster-sweep.

## 2. Bevroren input — exact gebruiken

### Interne pre-external freezes op de CCI-werkbranch

- Babaji:
  - bestand: `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/BABAJI_V2_PRE_EXTERNAL_FREEZE.md`
  - freeze commit: `6b79f1c8ad25572cb058c047673aef9d5c4284ce`
- Lahiri Mahasaya:
  - bestand: `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/LAHIRI_MAHASAYA_V2_PRE_EXTERNAL_FREEZE.md`
  - freeze commit: `642e464ac96ca011f75df93c0f3ce71653948d6f`
- Sri Yukteswar:
  - bestand: `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/SRI_YUKTESWAR_V2_PRE_EXTERNAL_FREEZE.md`
  - freeze commit: `ea60ba5975b0169736cd95a14f5daeef7d4c0868`

### Onafhankelijke externe PRE-COMPARE freezes

Branch: `agent/chatgpt-top11-parallel-sweep`

- Babaji:
  - bestand: `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/BABAJI_PRE_COMPARE_FREEZE.md`
  - freeze commit: `f565ff163e35597d2c4ed802676a4671f9da3b70`
  - 35 genormaliseerde locaties
- Lahiri Mahasaya:
  - bestand: `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/LAHIRI_MAHASAYA_PRE_COMPARE_FREEZE.md`
  - freeze commit: `71bb5b6406fec1e7b59511e7957d247c3bdabc50`
  - 60 genormaliseerde locaties
- Sri Yukteswar:
  - bestand: `runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/SRI_YUKTESWAR_PRE_COMPARE_FREEZE.md`
  - freeze commit: `7ebad72652cf14d750c00aaa77fc25f53f2be2cd`
  - 38 genormaliseerde locaties

HARD: wijzig, merge of herschrijf de externe branch niet. Deze task schrijft uitsluitend naar de
CCI-werkbranch.

## 3. Verplichte canon vóór uitvoering

Lees volledig:

1. dit `TASK.md` en bijbehorende `STATUS.md`;
2. `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/METHOD_V2.md`;
3. alle zes hierboven genoemde freeze-bestanden vanaf hun bevroren refs;
4. `runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/YOGANANDA_EXTERNAL_RECONCILIATION_CCI_086.md`;
5. `runs/active/TOP11-EXTERNAL-AI-BENCHMARK-001/WERKPAKKET_D_DEEPENING_CCI_086.md`;
6. `governance/SWEEP_ERROR_CLASSES.md`;
7. de relevante bron-/reconciliatieregels uit `governance/SWEEP_PROTOCOL.md`.

Gebruik METHOD_V1 of PHASE2_RESULT niet als waarheidslijst. Ze mogen alleen als historisch precedent
worden genoemd nadat de actuele datasets zijn gereconcilieerd.

## 4. Werkpakket A — lossless inputinventarisatie

Maak per persoon eerst een volledige inventaris van ALLE interne en externe records. Geen record
mag verdwijnen doordat twee namen op elkaar lijken.

Per record minimaal:

- bronrecord-ID en detectorlaag;
- naam, alternatieve spellingen en plaats/staat;
- gebeurtenis;
- onderzochte persoon werkelijk persoonlijk aanwezig: JA / ONZEKER / NEE;
- aanwezigheidstype;
- fysieke identiteit: EXACT / DEELS / ALLEEN_PLAATS / ONBEKEND;
- historisch gebouw versus huidige instelling;
- host/gastheer/netwerk;
- primaire of semi-primaire bron + exacte locator;
- onzekerheid/conflict;
- claimant-traditie indien relevant.

## 5. Werkpakket B — bidirectionele matching

Match niet alleen external-only claims. Iedere interne én externe rij krijgt exact één
reconciliatie-uitkomst:

- `SAME_SITE_SAME_EVENT`
- `SAME_SITE_DIFFERENT_GRANULARITY`
- `SAME_SITE_DIFFERENT_NAME`
- `DISTINCT_SUBLOCATION`
- `INTERNAL_ONLY_VERIFIED_MISS`
- `INTERNAL_ONLY_UNVERIFIED`
- `EXTERNAL_ONLY_VERIFIED_MISS`
- `EXTERNAL_ONLY_UNVERIFIED`
- `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`
- `FALSE_OR_UNSUPPORTED_INTERNAL_CLAIM`
- `WRONG_PERSON_OR_TRADITION`
- `LATER_INSTITUTION_ONLY`
- `TRANSIT_OR_CONTEXT_ONLY`
- `SYMBOLIC_VISIONARY_OR_POSTHUMOUS_ONLY`
- `IDENTITY_CONFLICT_UNRESOLVED`

Geen meerderheidstemming. Twee modellen die dezelfde claim herhalen tellen niet als twee
onafhankelijke bronnen.

## 6. Werkpakket C — directe bronverificatie

Controleer rechtstreeks:

1. alle external-only records;
2. alle internal-only records;
3. alle identity-/adres-/granulariteitsconflicten;
4. alle overlaps waarvan aanwezigheid, gebeurtenis of exacte fysieke plek niet gelijk wordt
   geclassificeerd;
5. iedere claim die alleen op een moderne instelling, pelgrimswebsite, latere traditie of
   secundaire samenvatting rust.

Eisen:

- gebruik primaire/semi-primaire bronnen waar beschikbaar;
- geef bronlocator: hoofdstuk/pagina/datum/archiefrecord/URL;
- citeer alleen het minimaal noodzakelijke fragment;
- raad geen adres, gebouw, coördinaat of route;
- `BRON_GEBLOKKEERD` of `UNRESOLVED` is beter dan schijnzekerheid;
- incidentele nieuwe bronvondsten wel lossless registreren, maar geen nieuwe brede discovery-sweep
  openen.

## 7. Babaji — verplichte traditiescheiding

Babaji-records mogen niet op naamgelijkenis worden samengevoegd. Leg per record expliciet vast:

`CLAIMANT_TRADITION`:
- `YOGANANDA_LAHIRI_SRI_YUKTESWAR_SRF_YSS`
- `HARIHARANANDA`
- `KRIYA_BABAJI_NAGARAJ_YOGI_RAMAIAH`
- `HAIDAKHAN_BABAJI`
- `OTHER_OR_UNKNOWN`

`PRESENCE_CLAIM_TYPE`:
- `BODILY_FIRSTHAND`
- `BODILY_REPORTED_LINEAGE`
- `VISION_OR_MATERIALIZATION`
- `VOICE_ONLY`
- `PREVIOUS_LIFE_CLAIM`
- `MODERN_MEMORIAL_OR_INSTITUTION_ONLY`
- `SYMBOLIC_ONLY`

Een site uit een andere Babaji-traditie is geen locatie van Yogananda's Mahavatar Babaji zonder een
expliciete, bronmatig verifieerbare identiteitsbrug. Houd die claims apart, ook wanneer een latere
instelling ze als één persoon presenteert.

## 8. Lahiri Mahasaya en Sri Yukteswar — verplichte scheidingen

- reguliere fysieke aanwezigheid bij leven;
- postume verschijning/materialisatie/visioen;
- locatie van een discipel of latere instelling;
- instelling opgericht of gewijd ná de persoon;
- gebeurtenis bewezen maar exacte fysieke plek onbekend;
- stad/route versus concreet gebouw of kamer.

Sri Yukteswars verschijning in het Regent Hotel en Lahiri's postume materialisatieclaims mogen niet
als gewone lichamelijke aanwezigheid worden genormaliseerd.

## 9. Output en duurzame checkpoints

Schrijf onder:

`runs/active/TOP11-CORE-KRIYA-RECONCILIATION-001/`

Verplicht:

1. `BABAJI_RECONCILIATION.md`
2. `LAHIRI_MAHASAYA_RECONCILIATION.md`
3. `SRI_YUKTESWAR_RECONCILIATION.md`
4. `RECONCILIATION_MATRIX.jsonl`
5. `RECONCILIATION_RESULT.md`
6. bijgewerkte `STATUS.md`
7. bijgewerkte `governance/INDIA_SESSION_START.md`
8. bijgewerkte `runs/active/TOP11-INDIA-PERSON-CENTRIC-MEGASWEEP-001/STATUS.md`

Commit na iedere afgeronde persoon:

- checkpoint 1: Babaji;
- checkpoint 2: Lahiri Mahasaya;
- checkpoint 3: Sri Yukteswar;
- finale commit: matrix, synthese en status/governance.

Wacht niet tot het einde met duurzaam wegschrijven. Bij contextverlies hervat exact vanaf de laatste
checkpointcommit; herstart geen afgerond persoonsonderzoek.

## 10. METHOD_V2-gates en modeldiversiteit

Beoordeel per persoon opnieuw:

- `CORPUS_COVERAGE_GATE`
- `HOSTGRAPH_GATE`
- `DISCOVERY_GATE`
- `RECONCILIATION_GATE`
- `EXTERNAL_MODEL_DIVERSITY_GATE`

De externe branch is één onafhankelijke ChatGPT-run met parallelle onderzoeksstreams. Meerdere
workers van hetzelfde model zijn niet automatisch een multi-provider/multi-model-union.

Daarom:

- voer de reconciliatie nu volledig uit;
- leg aantoonbaar vast welke detector-/modeldiversiteit werkelijk aanwezig was;
- claim `EXTERNAL_MODEL_DIVERSITY_GATE: JA` uitsluitend met concrete provenance van meerdere
  onafhankelijke modelfamilies;
- claim geen definitieve `PERSON_SWEEP_SATURATED: JA` zolang een verplichte gate NEE of
  ONBEPAALD is;
- benoem de exacte resterende external-union/source/field/archive-hiaten als `next_allowed_step`.

## 11. Harde grenzen

- Geen regionale of clustersweep.
- Arunachala/Tiruvannamalai-hold blijft staan.
- Geen clusterheatmap in deze taak.
- Geen permanente locatie-ID's of globale nummering.
- Geen A/B/C namens Mark.
- Geen PDF.
- Geen route, nachten, hotel, vervoer of pacing.
- Vivekananda/Hariharananda niet uitbreiden.
- NKB/Ram Dass/Ramana/Ramakrishna niet starten.
- PR #24 niet mergen of wijzigen.
- Externe frozen branch niet wijzigen of mergen.

## 12. Stopvoorwaarde en rapportage

Stop pas wanneer alle drie persoonsreconciliaties, de lossless matrix, de synthese en alle
gate-oordelen duurzaam gecommit zijn, of wanneer een echte systeembrede blocker bestaat.

Plaats daarna één korte PR #23-resultaatenvelop met:

- `CCI_RESULT — CCI_TASK 088`
- task_id;
- status;
- vier checkpoint/finale commits;
- outputpaden;
- counts per reconciliatiecategorie;
- gate-uitkomsten per persoon;
- blockers;
- exacte `next_allowed_step`.

Start niets opvolgends automatisch.

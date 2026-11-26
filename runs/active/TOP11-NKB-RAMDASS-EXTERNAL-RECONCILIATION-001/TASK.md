# TASK — TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001

```
task_id: TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001
cci_task: CCI_TASK 091
issued_by: INDIA8
issued_at: 2026-08-19
target_branch: claude/werk-je-nu-of-niet-oa10y7
state_on_issue: READY_FOR_CCI
pdf_status: VERBODEN
```

## 1. INDIA8-QA op CCI_TASK 090 — BESLUIT

CCI_TASK 090 is inhoudelijk geaccepteerd.

Reden:
- *Be Here Now* is volledig hersteld en corpus-first verwerkt;
- Ram Dass groeide van 5 naar 13 atlasrecords plus één aparte Kainchi-naamsbevestiging;
- Neem Karoli Baba groeide van 19 naar 21 records via rechtstreeks ooggetuigenmateriaal uit *Be Here Now*;
- de foutieve bronidentificatie `Sacred Wanderer` is correct en traceerbaar hersteld naar `Being Ram Dass` (2021);
- *Miracle of Love* en *By His Grace* zijn via meerdere legale routes aantoonbaar geblokkeerd; geen toegangscontrole is omzeild;
- `Being Ram Dass` is slechts PARTIAL, maar dit is geen reden om de projectpipeline stil te zetten;
- beide saturation-vlaggen blijven terecht NEE.

INDIA8 kiest daarom expliciet NIET voor nog een identieke corpus-recoveryronde vóór vergelijking. De onafhankelijke externe freezes bevatten juist een veel grotere kandidatenlaag en moeten nu lossless worden gereconcilieerd. Nieuwe externe-only claims kunnen daarna gericht naar de bron worden teruggevoerd.

## 2. Doel

Voer volledige bidirectionele, lossless METHOD_V2-reconciliatie uit voor:

1. Neem Karoli Baba
2. Ram Dass

Vergelijk per persoon:

A. de actuele interne CCI-freeze, inclusief CCI_TASK 090-delta;
B. de reeds bevroren onafhankelijke externe ChatGPT PRE-COMPARE-freeze op branch `agent/chatgpt-top11-parallel-sweep`.

Externe freezes zijn nu toegestaan om te openen. De blindheidsfase is voorbij.

Bekende externe freeze-status bij uitgifte:
- Neem Karoli Baba: 113 genormaliseerde locaties; freeze SHA `180bf023a0a06f7ebb0d9df762e5fe0530f59954`;
- Ram Dass: 57 genormaliseerde locaties; freeze SHA `799949b551564a9993d4afe15403c36e55213af2`.

Gebruik SHA/pad als integriteitscontrole; neem niets blind over.

## 3. Verplichte vergelijking

Maak per extern record en per intern record minimaal onderscheid tussen:

- SAME_PHYSICAL_SITE
- SAME_EVENT_MORE_GRANULAR
- INTERNAL_ONLY
- EXTERNAL_ONLY
- CONFLICT
- CONTEXT_ONLY
- LATER_MEMORIAL_NO_PERSONAL_PRESENCE
- DUPLICATE_OR_ALIAS
- UNRESOLVED_IDENTITY

Geen matching alleen op plaatsnaam. Vergelijk gebeurtenis, persoon, tijd, host/gastheer, fysieke identiteit en bronprovenance.

## 4. Directe bronverificatie — HARD

Iedere betekenisvolle `EXTERNAL_ONLY`, `INTERNAL_ONLY`, `CONFLICT`, `SAME_EVENT_MORE_GRANULAR` of identiteitsclaim moet waar praktisch mogelijk rechtstreeks tegen de aangehaalde bron worden gecontroleerd.

Prioriteit:
1. primaire/eerste-persoonsbron;
2. directe devotee/ooggetuige;
3. officiële stichting/ashram/trust;
4. sterke secundaire biografie;
5. zwakke aggregators uitsluitend als lead.

De externe freeze is detectorinput, geen bewijs. Een citaat dat niet in de genoemde bron staat wordt als fout/hallucinatie geregistreerd, conform het Yogananda-precedent.

Gebruik de in 090 bewezen open *Be Here Now*-tekst actief voor verificatie van Ram-Dass- en gedeelde NKB-claims.

Voor NKB mogen de nog geblokkeerde *Miracle of Love*/*By His Grace* niet worden geforceerd. Als een externe claim uitsluitend daarop rust en de passage niet legaal bereikbaar is: `BRON_GEBLOKKEERD`, niet TRUE gokken.

## 5. Host/netwerkgraaf

De externe freezes zijn veel groter dan de interne freezes. Controleer daarom expliciet private huizen, hosts, hotels, stations, ziekenhuizen, ashramkamers, tuinen, veranda's, keukens, retraites, routepunten en andere sublocaties.

Voor Ram Dass extra aandacht voor:
- pre-guru route;
- Kainchi/Nainital/Kumaon;
- Hotel Evelyn en Sah-familienetwerk;
- Delhi-sublocaties;
- latere Indiareizen en 2004;
- onbenoemde locaties uit *Be Here Now* en mogelijke externe identiteitsankers.

Voor NKB extra aandacht voor:
- private devoteehuizen en hostfamilies;
- landelijke ashrams versus bewezen persoonlijke aanwezigheid;
- trein-/weg-/ziekenhuis-/laatste-reislocaties;
- bilocatie/wonderclaims apart van normale fysieke aanwezigheid;
- latere tempels/ashrams die alleen aan hem zijn gewijd.

## 6. Verplichte output

Maak:

- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/NEEM_KAROLI_BABA_RECONCILIATION.md`
- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RAM_DASS_RECONCILIATION.md`
- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RECONCILIATION_MATRIX.jsonl`
- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/RECONCILIATION_RESULT.md`
- `runs/active/TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001/STATUS.md`

Werk daarnaast de relevante persoons-freezes/statussen en `governance/INDIA_SESSION_START.md` bij met een append-only/reconciliatie-delta; overschrijf de pre-external geschiedenis niet stil.

Per persoon rapporteren:
- internal count vóór reconciliatie;
- external count;
- matched/duplicate count;
- external-only count;
- internal-only count;
- verified true/false/partial/unresolved;
- nieuw bevestigde fysieke locaties;
- gecorrigeerde claims;
- resterende bronblokkades;
- actuele vier METHOD_V2-gates;
- eerlijke saturationstatus.

## 7. Checkpoints

Commit na volledig afgeronde Neem Karoli Baba-reconciliatie.
Commit daarna na volledig afgeronde Ram Dass-reconciliatie.
Commit finale matrix/status/governance apart indien nodig.

Bij contextverlies hervatten vanaf laatste checkpoint; geen afgerond persoonspakket opnieuw uitvoeren.

## 8. IndiaROOD en Core-Kriya

De inmiddels bestaande IndiaROOD-freezes voor Babaji, Lahiri Mahasaya en Sri Yukteswar zijn bekend en moeten later lossless aan CCI_TASK 088 worden toegevoegd. Dat is een aparte vervolgstap. Open of reconcilieer die drie IndiaROOD-bestanden NIET binnen deze taak, zodat CCI_TASK 091 begrensd blijft tot NKB + Ram Dass.

## 9. Harde grenzen

- Geen nieuwe blinde persoonsweep.
- Geen Ramana Maharshi/Ramakrishna starten.
- Geen cluster/regio/heatmap.
- Geen A/B/C namens Mark.
- Geen permanente IDs.
- Geen PDF.
- Geen route/nachten/vervoer.
- Externe branch niet wijzigen of mergen.
- PR #24 niet wijzigen/mergen.

## 10. Stopvoorwaarde

Stop pas wanneer beide personen volledig bidirectioneel zijn gereconcilieerd en alle betekenisvolle verschillen zijn geclassificeerd en waar praktisch mogelijk rechtstreeks bronmatig geverifieerd.

Plaats daarna één `CCI_RESULT — CCI_TASK 091`-envelop op PR #23 met checkpointcommits, counts, echte nieuwe vondsten, fouten/correcties, blockers, gates, saturationstatus en exact `next_allowed_step`.

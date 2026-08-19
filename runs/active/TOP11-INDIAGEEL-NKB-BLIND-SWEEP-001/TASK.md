# TASK — TOP11-INDIAGEEL-NKB-BLIND-SWEEP-001

```
task_id: TOP11-INDIAGEEL-NKB-BLIND-SWEEP-001
owner: INDIA GEEL
issued_by: INDIA8
issued_at: 2026-08-19
mode: PRE-COMPARE BLIND
state: READY_FOR_INDIAGEEL
branch: agent/indiageel-ramana-ramakrishna-sweep
```

## Doel
Maak één volledig onafhankelijke landelijke PRE-COMPARE freeze voor Neem Karoli Baba, vanaf nul, heel India.

## HARD BLINDNESS
Voor deze taak mag INDIA GEEL vóór de eigen freeze duurzaam is gecommit GEEN inhoud lezen uit:
- PR #23/#24;
- CCI-resultaten, CCI_TASK 089/090/091 of reconciliaties;
- agent/chatgpt-top11-parallel-sweep;
- agent/indiarood-core-kriya-sweep;
- bestaande NKB-atlassen, METHOD_V1/PHASE2-resultaten, unions of kandidatenlijsten;
- AOAY/regio/clusterbestanden die NKB-locaties kunnen lekken;
- bestaande Ramana/Ramakrishna-freezes anders dan voor branchcontinuïteit niet inhoudelijk nodig.

Toegestaan:
- uitsluitend dit TASK.md;
- STATUS.md in dezelfde map;
- openbare externe bronnen die INDIA GEEL zelf vindt.

## Methode
Corpus-first/source-first. Verplicht:
1. primaire/semi-primaire devotee-bronnen en officiële trusts/ashrams;
2. host-/gastheer-/familie-/discipelnetwerk;
3. huizen, kamers, ziekenhuizen, stations, tempels, ashrams, caves, ghats, retreats, rail/road-transit en andere fysieke sublocaties;
4. daarna brede webdiscovery en spelling/historische naamvarianten;
5. directe broncontrole waar praktisch mogelijk;
6. geen plaats afleiden uit context-only vermeldingen.

Zoek expliciet ook via netwerken rond o.a. Dada Mukerjee, Ram Dass, K.K. Sah/Sah-familie, familie Sharma, lokale devotees, ashrambeheerders en andere zelfstandig ontdekte hosts — maar gebruik geen bestaande projectlijst als seed.

## Output
Schrijf duurzaam op dezelfde branch:
`runs/active/TOP11-INDIAGEEL-NKB-BLIND-SWEEP-001/NEEM_KAROLI_BABA_INDIAGEEL_FREEZE.md`

Freeze bevat minimaal:
- PERSON / timestamp / BLINDNESS_CONFIRMED;
- CORPORA_SEARCHED;
- SOURCE_ACCESS_BLOCKERS;
- HOSTGRAPH_SEARCHED;
- DISCOVERY_SEARCH_FAMILIES;
- genormaliseerde recordcount;
- per record: plaats, staat/district, type, gebeurtenis/periode, PERSONALLY_PRESENT, PHYSICAL_IDENTITY, bron, URL/bibliografie, locator, onzekerheid;
- conflicts;
- unresolved leads;
- saturation attempts;
- `PERSON_SWEEP_SATURATED: JA/NEE`.

Liever eerlijk NEE dan schijn-JA.

## Duurzaamheid
Commit de freeze zodra klaar. Noteer SHA. Update STATUS.md. Geen vergelijking/reconciliatie na freeze.

## Harde grenzen
Geen A/B/C, route, heatmap, regioselectie, permanente IDs, PDF, PR #23, merge of vergelijking met bestaande detectoren.

## Stopvoorwaarde
Na duurzame PRE-COMPARE freeze: STOP en rapporteer alleen pad, SHA, recordcount, saturation, blockers en `BLINDNESS_PRESERVED`.

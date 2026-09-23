# RECONCILIATION_RESULT — TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001

```
task_id: TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001
cci_task: CCI_TASK 091
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
checkpoint_commits: 54d0b51 (Neem Karoli Baba), 20c281c (Ram Dass)
```

## 1. Samenvatting

Volledige bidirectionele METHOD_V2-reconciliatie uitgevoerd voor Neem Karoli Baba (21 interne vs.
113 externe records) en Ram Dass (13+1 interne vs. 57 externe records) tegen de bevroren
`agent/chatgpt-top11-parallel-sweep`-freezes. Beide externe bronbestanden zijn vóór opening
integriteitsgecontroleerd via directe GitHub-blob-SHA-vergelijking — exacte match, geen manipulatie.

Volledige details: `NEEM_KAROLI_BABA_RECONCILIATION.md`, `RAM_DASS_RECONCILIATION.md`,
`RECONCILIATION_MATRIX.jsonl` (141 regels).

## 2. Top-bevindingen

### Opgeloste interne conflicten
- **NKB-sterfteziekenhuis**: Ramakrishna Mission Hospital, Vrindavan — rechtstreeks bronmatig
  bevestigd (Tier 1, direct gefetcht).
- **NKB Delhi Ashram / Hanuman Garhi**: interne `ONZEKER` opgeheven naar externe `JA`/`EXACT`
  (Jonapur-ashram zomer 1973; Hanumangarhi Nainital) — `PLAUSIBLE`, niet apart Tier-1 bevestigd.

### Nieuw ontstaan conflict
- **NKB-doodsvolgorde**: twee secundaire bronnen spreken elkaar tegen over een Mathura-tussenstop
  vlak vóór het overlijden — niet opgelost, expliciet als open conflict genoteerd.

### Fout gevonden in de externe freeze (Yogananda-precedent toegepast)
- **Ram Dass — Jagannath Puri-strandwandeling** (extern record #34): het geciteerde Sara-Davidson-
  citaat staat niet in de aangehaalde bronnen (beide volledig gedownload en doorzocht, nul
  treffers voor "Puri"/"beach"). Geregistreerd als `FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`, niet
  overgenomen.

### Directe Tier-1-bevestigingen in eigen bronmateriaal
- NKB: Panki-bilocatie-episode (woordelijk gelezen in *The Near and the Dear*).
- Ram Dass: "Health Department"-kantoor en rivier-badplaats bij Kainchi (beide woordelijk
  teruggevonden in de eigen, in CCI_TASK 090 gedownloade *Be Here Now*-tekst); Auroville-bezoek
  december 1992 (officiële Auroville-pagina, citaat exact).

### Cross-persoon bevestigingen
Meerdere externe Ram-Dass-records en NKB-records beschrijven onafhankelijk dezelfde fysieke
locaties (4 Church Lane Prayagraj, Allahabad-station, Vrindavan-ashramcomplex, Hanuman Garh-
tempel Nainital) — een sterk intern consistentiesignaal voor de kwaliteit van de externe sweep.

### Nieuwe primaire bron toegankelijk gebleken
*The Near and the Dear: Stories of Neem Karoli Baba and His Devotees* (Sudhir "Dada" Mukerjee,
dokumen.pub) bleek — in tegenstelling tot *By His Grace* op dezelfde site — volledig legaal
toegankelijk (HTTP 200, geen inlog). Volledig gedownload (688K tekens) en gebruikt voor
Tier-1/Tier-2-verificatie van tientallen externe NKB-claims.

## 3. Recorddelta per persoon

**Neem Karoli Baba**: 21 interne records, 113 externe records. 19 interne matchen (direct of
granulair) op extern; 1 intern-only (Badam Baas); ca. 94 extern-only (grotendeels Tier-2
bevestigd). 3 correcties overgenomen (district Akbarpur, sterfteziekenhuis, Delhi/Hanumangarhi-
zekerheid). 1 nieuw conflict (doodsvolgorde).

**Ram Dass**: 13 locatierecords + 1 naamsbevestiging intern, 57 extern. Alle 14 interne records
vinden een externe tegenhanger of granulaire aanvulling; 43 extern-only (grotendeels
`BRON_GEBLOKKEERD` via MOL). 2 nieuwe Tier-1-sublocaties toegevoegd; 1 externe claim expliciet
afgewezen (Puri-strand).

## 4. Gates en resterende blockers

| | Neem Karoli Baba | Ram Dass |
|---|---|---|
| CORPUS-COVERAGE-GATE | NEE → **DEELS** | DEELS (ongewijzigd) |
| HOSTGRAPH-GATE | DEELS (sterk uitgebreid) | DEELS (uitgebreid) |
| DISCOVERY-GATE | DEELS | DEELS |
| RECONCILIATIE-GATE | DEELS (deze taak) | DEELS (deze taak) |

Resterende blockers: *Miracle of Love* en *By His Grace* blijven `BRON_GEBLOKKEERD` voor beide
personen (ongewijzigd sinds CCI_TASK 090). "Being Ram Dass" (2021) blijft `PARTIAL`. CG-
catalogus-URL (Columbia) geeft HTTP 404.

## 5. Saturationstatus

`NEEM_KAROLI_BABA_SATURATED: NEE`. `RAM_DASS_SATURATED: NEE`. Beide eerlijk, consistent met de
externe freezes' eigen saturatieoordeel — geen van beide claimt volledige dekking.

## 6. Bevestiging blindheidsgrenzen (TASK.md §8-9)

- IndiaROOD Core-Kriya-bestanden (Babaji, Lahiri Mahasaya, Sri Yukteswar): **NIET geopend** binnen
  deze taak, conform TASK.md §8 — blijft een aparte vervolgstap.
- Ramana Maharshi/Ramakrishna: **niet gestart**.
- Externe branch `agent/chatgpt-top11-parallel-sweep`: alleen gelezen (raw content + GitHub API),
  **niet gewijzigd of gemerged**.
- Geen cluster/regio/heatmap, A/B/C, permanente IDs, PDF of route-werk verricht.

## 7. next_allowed_step

CCI stopt na deze resultaatenvelop op PR #23 en wacht op INDIA-QA. Aanbevolen vervolgopties voor
INDIA:
1. De inmiddels lossless-uitgevoerde IndiaROOD Core-Kriya-freezes (Babaji, Lahiri Mahasaya, Sri
   Yukteswar, branch `agent/indiarood-core-kriya-sweep`) alsnog aan CCI_TASK 088 toevoegen als
   derde onafhankelijke detector, conform CCI_TASK 088's eigen `next_allowed_step`.
2. Het nieuw ontstane NKB-doodsvolgordeconflict (Mathura-tussenstop) gericht laten uitzoeken, indien
   relevant geacht.
3. Ramana Maharshi/Ramakrishna blijven expliciet niet gestart zonder nieuwe INDIA-opdracht.

---
Geschreven door: CCI. CCI_TASK 091.

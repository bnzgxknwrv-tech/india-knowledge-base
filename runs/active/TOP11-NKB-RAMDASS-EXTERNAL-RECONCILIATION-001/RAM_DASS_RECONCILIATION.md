# RAM_DASS_RECONCILIATION

```
task_id: TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001
cci_task: CCI_TASK 091
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
internal_source: runs/active/TOP11-NKB-RAMDASS-V2-PRE-EXTERNAL-001/RAM_DASS_V2_PRE_EXTERNAL_FREEZE.md
  (13 locatierecords + 1 naamsbevestiging, uit CCI_TASK 089 + 090-delta)
external_source: agent/chatgpt-top11-parallel-sweep,
  runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/RAM_DASS_PRE_COMPARE_FREEZE.md
  (57 records; commit 799949b551564a9993d4afe15403c36e55213af2, blob-sha 6d2c5c978c7eddbb9d74f2352c8682e6b1cfe7b6
  — integriteit bevestigd via directe GitHub-blobvergelijking vóór opening)
```

## 0. Directe bronverificatie — methode en resultaat

De externe freeze citeert grotendeels dezelfde twee kernbronnen die CCI zelf in CCI_TASK 090
herstelde (**BH** = *Be Here Now*, volledige tekst reeds gedownload; **MOL** = *Miracle of Love*,
blijft `BRON_GEBLOKKEERD`), plus een reeks toegankelijke secundaire bronnen (RD, IM, SD, HE, PA,
SAI, JV, RDE, AV, CG, ID).

**Tier 1 — rechtstreeks in eigen BH-tekst nagelopen (nieuw bevestigd)**:
- Externe record #19 ("Health Department"-kantoor): woordelijk teruggevonden op regel 1373 van
  `be_here_now.txt` — exacte frase "the Health Department".
- Externe record #11 (rivier-badplaats bij Kainchi): woordelijk teruggevonden op regel 1508:
  "I would get up early, take my bath in the river or out..." — bevestigt exact.
- Externe record #57 (Lama Govinda's huis): de "opdracht om Govinda te bezoeken" is al in
  CCI_TASK 090 zelf rechtstreeks gevonden (regels 1350-1358); brontekst bevestigt de opdracht,
  niet de daadwerkelijke aankomst — exact consistent met de externe eigen `ONZEKER`-status.

**Tier 1 — rechtstreeks extern nagelopen (WebFetch, 2026-08-19)**:
- **AV (Auroville)**: bevestigd — december 1992, citaat exact overeenkomend met de externe freeze.
- **SD (Sara Davidson, saradavidson.com + beezone.com)**: **NIET bevestigd** — zie §2, fout
  gevonden.
- **SAI (ashramsofindia.com Sathya Sai Baba-devotees)**: alleen de kale vermelding "Richard Alpert
  (Ram Dass) 1971 Whitefield" teruggevonden; de gedetailleerde narratief (privé-interview, medaille,
  Howard Levin als ooggetuige) kon niet in dezelfde ophaalronde worden bevestigd — `PARTIAL`.
- **CG (Columbia University Libraries)**: URL geeft **HTTP 404** — bron onbereikbaar zoals
  geciteerd; niet bevestigd, niet weerlegd.

**Niet verifieerbaar**: alle MOL-gebaseerde claims blijven `BRON_GEBLOKKEERD`, conform CCI_TASK 090.

## 1. Matrix — interne records tegen externe records

| intern # | interne locatie | externe match(es) | classificatie | toelichting |
|---:|---|---|---|---|
| 1 | Delhi (indirect, reisgenoten 1970) | — | blijft ONZEKER, geen externe weerlegging | Extern bevat wel een eigen, directer bevestigd Delhi-cluster (#17-24) voor Ram Dass zelf. |
| 2 | Kainchi Dham | ext #7-14 | SAME_SITE_MORE_GRANULAR | Extern splitst in 8 sublocaties (office/tucket, oude kamer, rivier, vuurceremoniezone, koude hut, 2004-kamer). Record #11 (rivier) Tier-1 bevestigd. |
| 3 | Hotel Evelyn, Nainital | ext #25-27 | SAME_SITE_MORE_GRANULAR | Extern voegt "cave"-kamer en balkon/patio toe (HE-bron, al eerder als betrouwbaar bevestigd in CCI_TASK 089). |
| 4 | Kausani (gehuurd huis) | ext #32-33 | SAME_SITE_MORE_GRANULAR | Extern voegt Anasakti Ashram-identificatie toe (inferentieel, eigen caveat van extern). |
| 5 | India 2004-reis (ONZEKER) | ext #14 (2004-kamer Kainchi) | SAME_SITE_DIFFERENT_GRANULARITY | Extern lokaliseert de 2004-reis wél specifiek in Kainchi; intern bleef algemeen. |
| 6 (090) | Amarnath Cave | ext #1 | SAME_PHYSICAL_SITE | Consistent. |
| 7 (090) | Benares/Varanasi | ext #2 | SAME_PHYSICAL_SITE | Consistent. |
| 8 (090) | Sarnath | ext #5 | SAME_PHYSICAL_SITE | Consistent. |
| 9 (090) | Delhi-sublocaties (Connaught Place, AmEx, restaurant, klooster) | ext #17-21 | SAME_EVENT — **CONFIRMED_TRUE (Tier 1, deels al in 090)** | Extern voegt "Health Department"-kantoor toe als apart record #19 — Tier-1 bevestigd in eigen BH-tekst (regel 1373); intern had dit generiek als "visumkantoor" meegenomen. |
| 10 (090) | Eerste-ontmoetingsveld | ext #8 | SAME_PHYSICAL_SITE | Consistent, beide zonder naamsanker. |
| 11 (090) | Forestry camp | ext #15-16 | SAME_EVENT_MORE_GRANULAR | Extern splitst appelboomgaard-tussenstop (#15) en Forestry camp zelf (#16) als twee records; intern had ze samengevoegd binnen één beschrijving. |
| 12 (090) | Onbenoemde estate bij Delhi | ext #6 | SAME_PHYSICAL_SITE | Consistent. |
| 13 (090) | K.K. Sah familiehuis | ext #29 | SAME_PHYSICAL_SITE | Consistent; extern voegt toe "vanaf 1967; 1971" als periode. |
| 14 (090, naamsbevestiging) | Kainchi-naam via "Being Ram Dass"-fotobijschrift | ext #7 (Kainchi Dham, EXACT) | SAME_SITE | Extern bevestigt de naam onafhankelijk via BH+MOL, consistent met de eigen 090-vondst. |

## 2. Fout gevonden — extern-only claim NIET ondersteund door eigen bron

**Externe record #34 (Jagannath Puri-strand, "SD, eerstehands: 'walking on the beach in Jaganath
Puri'")**: rechtstreeks gecontroleerd op de twee door de externe freeze zelf geciteerde
Sara-Davidson-bronnen:
- `https://saradavidson.com/ram-dass-does-a-saint-get-angry/` — volledige platte tekst
  gedownload en doorzocht: **geen enkele vermelding van "Puri" of "beach"** in het hele artikel.
- `https://beezone.com/ramdass/ram_dass_history.html` — volledige platte tekst gedownload en
  doorzocht: **eveneens geen enkele vermelding van "Puri" of "beach"**.

Conclusie: dit is een **`FALSE_OR_UNSUPPORTED_EXTERNAL_CLAIM`** — het geciteerde citaat staat niet
in de aangehaalde bron, conform het Yogananda-precedent uit TASK.md §4. Dit record wordt **niet**
overgenomen in de interne freeze. (De onderliggende feitelijke bewering — dat Ram Dass ooit in
Puri was — kan overigens wel kloppen; MOL, p. 51, wordt door de externe freeze zelf ook als bron
voor "opdracht/reis naar Puri" genoemd, en dat blijft `BRON_GEBLOKKEERD` voor directe verificatie.
Het probleem is specifiek de SD-strandwandeling-quote, niet de Puri-reis an sich.)

## 3. Cross-person bevestigingen met de Neem Karoli Baba-reconciliatie

Verscheidene Ram-Dass-externe records blijken dezelfde fysieke locaties te beschrijven als de
Neem-Karoli-Baba-externe freeze, onafhankelijk door dezelfde externe sweep gevonden:

- Ram-Dass-ext #36 (Dada/Didi Mukerjee huis, 4 Church Lane) ↔ NKB-ext #20-26 (4 Church Lane-
  cluster) — zelfde adres, twee personen.
- Ram-Dass-ext #40 (Allahabad-treinstation) ↔ NKB-ext #27 — zelfde station.
- Ram-Dass-ext #48-51 (NKB-ashram/Hanuman-tempel Vrindavan, incl. crematieplek) ↔ NKB-ext #104-107
  — zelfde ashramcomplex.
- Ram-Dass-ext #30 (Hanuman Garh-tempel, Nainital) ↔ NKB-ext #31-34 (Hanumangarhi) — zelfde tempel.
- Ram-Dass-ext #24 (huis van Mr. Soni, Inspector General of Forestry, Delhi) ↔ thematisch verwant
  aan NKB-ext #52 (Bhowali forest rest house/Soni residence) — mogelijk dezelfde
  Soni-familie/bosbeheernetwerk; niet als identiek record samengevoegd zonder sterker bewijs.

Deze kruisbevestigingen verhogen het vertrouwen in beide externe freezes aanzienlijk: onafhankelijk
gevonden overlap tussen twee apart bevroren persoonsdossiers is een sterk kwaliteitssignaal.

## 4. Overige externe-only records (Tier 2/geen verificatie mogelijk)

- **BH-gesourcte nieuwe leads** (Tier 2, corpus reeds in bezit maar niet elk record apart
  herlezen): "Baneshwar" tempelstop (#3, onopgelost plaatsnaam/OCR-kwestie — extern classificeert
  dit zelf al eerlijk als `ONBEKEND`), Konark Sun Temple (#4).
- **MOL-gesourcte records** (blijven `BRON_GEBLOKKEERD`, niet gegokt): Kainchi-sublocaties #9-10,
  #12-14; Ministry of Finance #22; "semi-hippie hotel" #23; Mr. Soni's huis #24; Hanuman Garh-
  bezoek #30; Sombari Maharaj-ashram #31 (expliciet `UNRESOLVED_IDENTITY`, Padampuri vs Kakrighat —
  extern classificeert dit zelf al eerlijk als open); Triveni Sangam #37; Allahabad-devoteehuis #38;
  Allahabad High Court #39; Benares-hotel #41; Sri Aurobindo Ashram + sportterrein #42-43;
  Mathura-logies/markt #46-47; Vrindavan-ashramsublocaties #49-51; Surat-grot #52; Ayodhya
  Sita-Ram-Baba-huis + winkel #53-54.
- **Secundair bevestigd, niet volledig**: Brindavan/Whitefield #44-45 (`PARTIAL`, zie §0); Dhamma
  Giri/Igatpuri #56 (IM-bron niet leesbaar opgehaald binnen deze taak, niet bevestigd noch
  weerlegd); Naini Lake #28 (fotobijschrift-only, zwak volgens de externe freeze's eigen
  toelichting — overgenomen als zwak).

## 5. Correcties overgenomen in de interne freeze

1. **Nieuw sublocatie-record**: "Health Department"-kantoor, Delhi — Tier-1 bevestigd, toegevoegd
   als expliciete sublocatie naast de al bestaande generieke Delhi-visumkantoor-vermelding.
2. **Nieuw sublocatie-record**: rivier-badplaats bij Kainchi — Tier-1 bevestigd (regel 1508).
3. **Kausani**: Anasakti Ashram-identificatie toegevoegd als aanvullende, inferentiële (niet
   volledig bewezen) naamskoppeling naast het bestaande "gehuurd huis"-record.
4. **Forestry camp**: appelboomgaard-tussenstop toegevoegd als apart, direct voorafgaand
   sub-record (extern splitst dit terecht van het Forestry camp zelf).
5. **Puri-strand (extern #34)**: expliciet **niet** overgenomen — zie §2.

## 6. Per-persoon rapportage

- **Internal count vóór reconciliatie**: 13 locatierecords + 1 naamsbevestiging.
- **External count**: 57.
- **Matched/duplicate**: 14 interne records/naamsbevestigingen matchen op externe records
  (sommige met meerdere sub-matches).
- **External-only**: 43 externe records zonder interne tegenhanger — grotendeels MOL-gebaseerd
  (blijft `BRON_GEBLOKKEERD`) of secundair-bronnig (deels Tier 1/2 bevestigd, zie §0/§4).
- **Internal-only**: 0 (alle interne records vonden een externe tegenhanger of aanvulling).
- **Verified true/false/partial/unresolved**: 3 volledig Tier-1 bevestigd (Health Department,
  rivier-badplaats, Auroville); 1 expliciet vals/onondersteund (Puri-strand, §2); 1 `PARTIAL`
  (Brindavan/Whitefield); 1 bron onbereikbaar (CG, HTTP 404); rest `BRON_GEBLOKKEERD` (MOL) of
  niet apart binnen budget nagelopen.
- **Nieuw bevestigde fysieke locaties**: Health Department-kantoor, rivier-badplaats Kainchi (beide
  Tier 1); circa 40 overige externe-only sublocaties (grotendeels MOL-geblokkeerd, dus niet
  bevestigd maar ook niet weerlegd).
- **Gecorrigeerde claims**: Puri-strand verwijderd/niet overgenomen (§2); Kausani/Forestry camp
  verrijkt (§5).
- **Resterende bronblokkades**: *Miracle of Love* — ongewijzigd `BRON_GEBLOKKEERD`. "Being Ram
  Dass" (2021) blijft `PARTIAL` (ongewijzigd sinds CCI_TASK 090). IM-interviewpagina kon deze ronde
  niet schoon worden opgehaald (technische non-hit, geen bewuste blokkade). CG-catalogus-URL geeft
  HTTP 404.
- **Actuele vier METHOD_V2-gates**:
  - CORPUS-COVERAGE-GATE: **DEELS** (ongewijzigd t.o.v. 090 — BH volledig, MOL blijft dicht).
  - HOSTGRAPH-GATE: **DEELS** (Mr. Soni, K.K. Sah-netwerk, Sathya Sai Baba-kring, Sri Aurobindo
    Ashram-gemeenschap toegevoegd als leads).
  - DISCOVERY-GATE: **DEELS** (externe freeze dekt een brede waaier secundaire bronnen die intern
    niet allemaal waren geraadpleegd — Auroville, Dhamma Giri, Sathya Sai Baba, Sri Aurobindo
    Ashram).
  - RECONCILIATIE-GATE: **DEELS** (deze taak).
- **Eerlijke saturationstatus**: **`RAM_DASS_SATURATED: NEE`** — de externe freeze claimt dat zelf
  ook niet; meerdere materiële leads (Baneshwar, Sombari-ashram-identiteit, meerdere Delhi/UP-
  privéhuizen, 2004-opnamelocatie) blijven fysiek onopgelost.

---
Geschreven door: CCI. Checkpoint 2/2 van CCI_TASK 091.

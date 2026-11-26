# TRAVEL_READINESS_GATE — CCI_TASK 095

```
task_id: TOP11-NKB-RAMDASS-INDIAGEEL-MULTIDETECTOR-RECONCILIATION-001
cci_task: CCI_TASK 095
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-19
```

Doel van dit document: expliciet onderscheiden welke gates, na toevoeging van IndiaGEEL als derde
detector, voldoende zijn om een locatie/cluster als **travel-ready** te beschouwen (d.w.z. fysiek
identificeerbaar en met voldoende zekerheid te bezoeken), los van de vraag of `PERSON_SWEEP_
SATURATED` op `JA` staat. Saturatie en travel-gereedheid zijn twee verschillende dingen: een
persoonssweep kan `NEE` blijven (nog niet elk devoteehuis gevonden) terwijl de reeds gevonden
kernlocaties wél volledig travel-ready zijn.

## Definitie TRAVEL-READY (deze taak)

Een locatie is **TRAVEL-READY** wanneer:
1. `PHYSICAL_IDENTITY` minstens `DEELS` is (complex/gebouw/plek identificeerbaar, ook al is exacte
   kamer/sublocatie niet honderd procent vastgesteld), én
2. minstens twee van de drie lagen (intern, extern, IndiaGEEL) elkaar bevestigen, óf één laag de
   claim Tier-1 rechtstreeks tegen de bron heeft geverifieerd, én
3. geen onopgelost feitelijk conflict over de identiteit/locatie zelf (datumconflicten over een
   reeds vaststaande plek tellen niet mee — zie NKB Mathura-voorbeeld).

Een locatie die hier niet aan voldoet is **NIET travel-ready**, ongeacht hoe interessant de
onderliggende claim is — dit voorkomt dat Mark naar een plek reist op basis van een enkele,
onbevestigde detectorclaim.

## Neem Karoli Baba

### TRAVEL-READY (drieweg of Tier-1 bevestigd)
- Akbarpur (geboortedorp/familiehuis)
- Gujarat-vroege periode: Vavania/Babania-ashram, lake, eerste Hanuman-murti
- Neeb Karori-dorp/grot/tempel/station
- Bhumiadhar-ashram
- Kainchi Dham (volledig complex, incl. de door extern gevonden sublocaties)
- Kakrighat (plek zelf; fysieke-aanwezigheidsnuance blijft ONZEKER, geen travel-blocker)
- Vrindavan-ashram (Hathiwale Baba-hut-locatie/Gore Dauji)
- **Hanuman Setu/Sankat Mochan-tempel, Lucknow** — nu travel-ready na deze taak's Tier-1-upgrade
  (was `ONZEKER` na 091)
- Taradevi/Shimla-bosplek
- **Veerapuram, Chennai** — nu travel-ready, Tier-1 bevestigd deze taak (volledig nieuwe regio)

### NIET travel-ready (nog onvoldoende bevestigd of te vaag)
- Panki Hanuman-tempel, Kanpur — drieweg bevestigd als plek, maar de bilocatie-episode zelf blijft
  bewust `ONZEKER`; de tempel als fysieke plek is overigens wel bezoekbaar (het is een bestaand,
  functionerend tempelcomplex), alleen de historische aanwezigheidsclaim is onzeker — voor
  reisdoeleinden telt de tempel zelf als travel-ready, de "bilocatie" als narratief, niet als
  routebepalend feit.
- Sindhi Dharmsala Madras en Vaishnavi Devi-tempel (IndiaGEEL-only, niet apart Tier-1 bevestigd —
  Veerapuram wel, deze twee nog niet)
- Alle in de reconciliatiedoc genoemde `ONBEKEND`-adressen (tientallen kleinere devoteehuizen in
  Kanpur/Bareilly/Agra) — niet travel-ready, geen adres om naartoe te reizen.

## Ram Dass

### TRAVEL-READY (drieweg of Tier-1 bevestigd)
- Amarnath Cave (fysieke plek, basiskamp uitgezonderd)
- Kainchi Dham + alle bekende sublocaties
- Hotel Evelyn, Nainital
- Hanuman Garh-tempel, Nainital
- K.K. Sah-huis-gebied, Nainital (huisadres zelf niet, regio/relatie wel)
- Kausani (huurhuis-gebied + Anasakti/Gandhi Ashram)
- Connaught Place, Delhi
- Bodh Gaya: Burmese Vihara, Bodhi-boom/Mahabodhi-tempel
- Sathya Sai Baba-ashram, Whitefield
- Vrindavan NKB-ashram + Bankey Bihari-tempel + Jaipuria Bhawan-gebied
- 4 Church Lane, Allahabad/Prayagraj (huisadres, historisch bevestigd)
- Triveni Sangam, Allahabad/Prayagraj

### NOG NIET travel-ready (CCI_TASK 095 snapshot; see INDIA10 closure below)
- **Dharamsala/McLeod Ganj** (Dalai Lama-audiëntiegebied, "Swarg Ashram") — CCI_TASK 095 required a gerichte verificatiepas.
- **Ganeshpuri/Muktananda-ashram** — CCI_TASK 095 had Tier-2 corroboration but no Tier-1 closure.
- **Anandamayi Ma-ashrams, Vrindavan en Kankhal** — CCI_TASK 095 judged plausible but not separately verified.
- Srinagar/Dal Lake-houseboat "New Ruby", Kumar Gallery Delhi, reclining Hanuman-tempel bij Sangam —
  interessante IndiaGEEL-only details, niet travel-blocker-vrij bevestigd.

## Samenvatting — travel-relevante delta van CCI_TASK 095

| categorie | NKB | Ram Dass |
|---|---:|---:|
| Nieuw travel-ready gemaakt door IndiaGEEL (upgrade of nieuwe Tier-1-bevestiging) | 2 (Lucknow-upgrade, Veerapuram) | 0 in CCI_TASK 095 |
| Nieuwe regio's/clusters geopend, nog niet travel-ready in CCI_TASK 095 | 0 substantieel nieuw | 3 (Dharamsala, Ganeshpuri, Anandamayi Ma-ashrams) |
| Onopgelost conflict, geen travel-blocker voor bestaande plek | 1 (Mathura-doodsvolgorde — de plekken zelf, Kainchi/Agra/Vrindavan, zijn alle travel-ready; alleen de exacte routevolgorde van de laatste reis is onzeker) | 0 nieuw |

## CCI_TASK 095 conclusie

Voor **beide personen** geldt: de reeds bekende kernclusters (Kainchi, Vrindavan, Nainital-regio,
Allahabad/Prayagraj, Bodh Gaya) waren al travel-ready na CCI_TASK 091 en blijven dat, nu met een
derde onafhankelijke bevestigingslaag. CCI_TASK 095 voegde concreet **twee nieuwe travel-ready
locaties** toe voor NKB (Lucknow-tempel, Veerapuram) en **drie potentiële nieuwe regio's** voor Ram
Dass die eerst een gerichte verificatiepas nodig hadden voordat ze als travel-ready golden.

`PERSON_SWEEP_SATURATED` bleef voor beide personen `NEE` — dat is een aparte, strengere maatstaf
dan travel-gereedheid en wordt hier bewust niet mee verward.

## INDIA10 targeted closure — 2026-08-23

INDIA10 executed exactly the targeted verification pass requested by CCI_TASK 095. Full evidence and provenance are in:
`RAM_DASS_TARGETED_TIER1_CLOSURE_2026-08-23.md`.

The CCI_TASK 095 snapshot above is preserved as provenance, but its three Ram Dass physical-identity blockers are superseded as follows:

- **Dharamsala / McLeod Ganj — Swarg Ashram**: `TRAVEL_READY = JA — BUILDING LEVEL`. Ram Dass's memoir places the visit at Swarg Ashram; the Dalai Lama's official chronology independently confirms Swarg Ashram as his Dharamsala residence in the relevant 1960–1968 period; the former building is independently identified as the present Regional Mountaineering Centre on Tushita Road. Exact historical room/access is not promoted.
- **Ganeshpuri — Muktananda / Gurudev Siddha Peeth**: `TRAVEL_READY = JA — ASHRAM-COMPLEX LEVEL`. Ram Dass-side sources confirm presence at Ganeshpuri/Muktananda's complex and Siddha Yoga independently identifies the surviving ashram complex. Exact meditation-room mapping remains unresolved.
- **Anandamayi Ma — Vrindavan**: `TRAVEL_READY = JA — ASHRAM-COMPLEX LEVEL`. Ram Dass's memoir confirms the visit and the Anandamayi Sangha independently identifies the current Vrindavan ashram. Exact historical room/courtyard remains unresolved.
- **Anandamayi Ma — Kankhal / Haridwar**: `TRAVEL_READY = JA — ASHRAM-COMPLEX LEVEL`. Ram Dass's memoir confirms the visit; Sounds True preserves a historical near-Haridwar ashram image; the Anandamayi Sangha independently identifies the current Kankhal ashram. Exact historical temple-step/room sublocation remains unresolved.

This closure removes a physical-identity blocker only. It **does not** choose these places for Mark, assign A/B/C, create permanent IDs, change cluster inclusion or alter a route.

`PERSON_SWEEP_SATURATED: NEE` remains unchanged for both NKB and Ram Dass.

---
Original CCI_TASK 095 gate by CCI; INDIA10 targeted closure appended 2026-08-23.

# OPEN_GATES_MATRIX — INDIA ORANJE

Snapshotbasis: uitsluitend governance/status/taakmetadata zichtbaar op `agent/indiaorange-travel-heatmap-prep` op 2026-08-19. Geen blinde onderzoeksinhoud gebruikt. `voldoende detectorlagen` betekent hier alleen: metadata toont genoeg onafhankelijke lagen om een reconciliatiestap uit te voeren of reeds uitgevoerde reconciliatie te beoordelen; het is geen inhoudelijke saturation-uitspraak.

| Persoon | Metadata-status landelijke persoonslaag | Detectorlagen volgens metadata | Gate voor travel-heatmap | Actieve/volgende taak |
|---|---|---|---|---|
| Anandamayi Ma | METHOD_V1 pilot + latere benchmark/driewegcontrole genoemd; oude `JA` niet als universele eindwaarheid behandelen | Meerdere lagen/benchmark aanwezig | **QA/normalisatie nodig vóór definitieve ingest**; geen nieuwe persoonsresearch | Geen afzonderlijke nieuwe actieve persoonsreconciliatietaak zichtbaar in deze branch-snapshot |
| Neem Karoli Baba | Externe reconciliatie afgerond; wacht op INDIA-QA | Intern METHOD_V2 + externe ChatGPT volledig gereconcilieerd | **OPEN: INDIA-QA / eventuele aanvullende detectorgate** | `TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001` afgerond, wacht QA |
| Mahavatar Babaji | IndiaROOD-delta drieweg gereconcilieerd; wacht op INDIA-QA | Intern + ChatGPT extern + IndiaROOD; metadata zet reconciliation/model-diversity gates op JA | **OPEN: INDIA-QA**, daarna heatmap-ingest mogelijk | `TOP11-CORE-KRIYA-INDIAROOD-DELTA-RECONCILIATION-001` afgerond, wacht QA |
| Lahiri Mahasaya | IndiaROOD-delta drieweg gereconcilieerd; twee conflicten blijven geregistreerd | Intern + ChatGPT extern + IndiaROOD; gates op JA | **OPEN: INDIA-QA**; conflicts behouden als flags, niet stil oplossen | Zelfde CCI_TASK 092-keten, afgerond |
| Paramahansa Yogananda | METHOD_V2 freeze aanwezig; eerdere saturation expliciet niet als eindwaarheid | Interne METHOD_V2 plus externe parallel-laag bestaat volgens megasweepmetadata, maar geen finale multidetectorreconciliatie zichtbaar | **OPEN: reconciliatie/detector-diversiteitsgate** | Geen aparte actieve reconciliatietaak zichtbaar in deze snapshot |
| Ram Dass | Externe reconciliatie afgerond; wacht op INDIA-QA | Intern METHOD_V2 + externe ChatGPT volledig gereconcilieerd | **OPEN: INDIA-QA / eventuele aanvullende detectorgate** | `TOP11-NKB-RAMDASS-EXTERNAL-RECONCILIATION-001` afgerond, wacht QA |
| Sri Yukteswar | IndiaROOD-delta drieweg gereconcilieerd; wacht op INDIA-QA | Intern + ChatGPT extern + IndiaROOD; gates op JA | **OPEN: INDIA-QA**, daarna heatmap-ingest mogelijk | CCI_TASK 092-keten afgerond |
| Hariharananda | Oude persoonsfreeze bestaat; projectgrens verbiedt exhaustieve landelijke deep sweep | Detector-/reconciliatiestatus onvoldoende expliciet voor finale ingest | **OPEN: governance-bepaalde gerichte verificatie/reconciliatie van grootste locaties** | Geen actieve specifieke taak zichtbaar; later gericht, niet exhaustief |
| Vivekananda | Oude persoonsfreeze bestaat; projectgrens verbiedt exhaustieve landelijke deep sweep | Detector-/reconciliatiestatus onvoldoende expliciet voor finale ingest | **OPEN: governance-bepaalde gerichte verificatie/reconciliatie van grootste locaties** | Geen actieve specifieke taak zichtbaar; later gericht, niet exhaustief |
| Ramakrishna | Multidetectorreconciliatie taak staat klaar | CCI intern 093 + ChatGPT extern blind + IndiaGEEL blind zijn als inputlagen voor CCI_TASK 094 gedefinieerd; IndiaGEEL-status op deze branch zelf toont de blinde sweep nog als queued | **OPEN: detectorfreeze duurzaam + CCI_TASK 094 reconciliatie + INDIA-QA** | `TOP11-RAMANA-RAMAKRISHNA-MULTIDETECTOR-RECONCILIATION-001` / CCI_TASK 094 |
| Ramana Maharshi | Multidetectorreconciliatie taak staat klaar | CCI intern 093 + ChatGPT extern blind + IndiaGEEL blind als bedoelde inputlagen; IndiaGEEL-status op deze branch toont Ramana nog READY | **OPEN: detectorfreeze duurzaam + CCI_TASK 094 reconciliatie + INDIA-QA** | Eerst IndiaGEEL blind freeze volgens branchmetadata, daarna CCI_TASK 094 |

## Detectorlaag-samenvatting

**Voldoende lagen voor QA/finale persoonsbeslissing volgens deze branchmetadata:** Babaji, Lahiri Mahasaya en Sri Yukteswar hebben een voltooide driewegreconciliatie. Neem Karoli Baba en Ram Dass hebben een voltooide tweelaags reconciliatie maar staan nog op INDIA-QA en metadata bewijst in deze snapshot geen afgeronde derde detectorlaag. Ramana/Ramakrishna hebben een expliciet ontworpen multidetectorketen, maar de eigen IndiaGEEL-status op deze branch is nog pre-freeze en CCI_TASK 094 staat `READY_FOR_CCI`.

**Nog niet veilig als definitieve heatmap-input:** Yogananda, Hariharananda en Vivekananda hebben in deze snapshot geen duidelijk finale, actuele multidetectorreconciliatie die door governance als travel-ready is vrijgegeven. Anandamayi Ma heeft aantoonbaar meerdere benchmark-/detectorlagen, maar de megasweepstatus waarschuwt dat oudere saturation-uitspraken provisioneel zijn; daarom geen automatische finale ingest zonder QA-normalisatie.

## Kritieke pad

Het **directe actieve kritieke pad in deze branch-snapshot is de Ramana Maharshi/Ramakrishna-multidetectorketen richting CCI_TASK 094**, voorafgegaan door de nog niet duurzaam afgeronde IndiaGEEL-freezes zoals `TOP11-INDIAGEEL-BLIND-SWEEP-001/STATUS.md` die op deze branch weergeeft. Daarna blijft INDIA-QA nodig.

Voor een **volledig Top-11-brede travel-ready heatmap** is CCI_TASK 094 echter niet het enige resterende blok: er moet daarna ook expliciete governance/reconciliatiesluiting komen voor Yogananda en een beperkte, niet-exhaustieve sluitingsroute voor Hariharananda en Vivekananda. Daarom wordt geen fictieve enkele eindtaak aangewezen die in de huidige metadata niet bestaat.

## Travel-gates die bewust dicht blijven

- Geen A/B/C door INDIA ORANJE.
- Geen route/nachten vóór Mark A/B/C.
- Arunachala/Tiruvannamalai blijft `LOCKED_BY_MARK`; geen inhoudelijke regio-sweep.
- Babaji-grot Kukuchina/Dunagiri blijft bestaande hoofdreden van de reis; deze matrix onderzoekt die locatie niet opnieuw.
- Conflicten worden als heatmapflags meegenomen en niet door deze taak opgelost.
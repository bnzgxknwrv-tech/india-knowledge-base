# INDIA8 -> INDIA9 LIVE HANDOFF — 2026-08-20

## MANDATORY FIRST READ FOR INDIA9+
Lees vóór regie-uitvoering:
`governance/INDIA_REGIE_DOORGANGSPROTOCOL_2026-08-20.md`
Actuele governance bevat ook de limiet: maximaal twee actieve workerstreams, liefst één worker naast INDIA-regie.

### 2026-08-23 GLOBAL CANON AUDIT — VERPLICHTE EXTRA FIRST READ
Regie-miss ontdekt: recente runs werden te zwaar gewogen terwijl legacy-but-still-protected Mark-locks en sleep anchors onvoldoende werden meegenomen. Daardoor werden o.a. Jageshwar (reeds A), Binsar (reeds C) en bestaande Kumaon slaapbases opnieuw/te laat behandeld.

Lees daarom vóór ELK volgend keuze-/routeblok ook:
- `governance/GLOBAL_REGIE_CANON_AUDIT_2026-08-23.md`
- `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/SLEEP_BASE_REGISTER_2026-08-23.md`

Nieuwe regieregel: vóór een locatie aan Mark wordt gepresenteerd, eerst latest Mark-decision -> accommodation lock -> central master -> governance/handoff -> legacy protected locks/anchors controleren. Oude candidates/overviews zijn nooit leidend bij conflict.

Tactische routevolgorde voor reeds behouden clusters is nu:
`KNOWN/CHOSEN SLEEP BASE -> A SITES -> DISTANCE/COMBINATION MATRIX -> LONELY PLANET ADDONS -> opportunistic B -> NIGHTS`.
Dit wijzigt geen site-A/B/C; het voorkomt rekenen vanaf willekeurige stadscentra terwijl historische/spirituele slaapbases al bekend zijn.

Actuele slaapbasisstatus:
- Kukuchina/Dunagiri: **Joshi Guest House LOCKED**.
- Nainital: **Hotel Evelyn CLUSTER_ANCHOR + site A**; historic Ram Dass room/patio access still final-trip prerequisite.
- Kasar Devi/Almora: **Turiya Niwas PROVISIONAL LOCK + site A**; wintercomfort direct bevestigd; alleen exacte data/duur/reservering open; Kripal/Rudra fallbacks.
- Varanasi: **Sahi River View Guesthouse LOCKED_BY_MARK**, balcony room, Jitendre, greetings from Debby. Dit OVERRULET oude provisional wording.
- Vrindavan/Braj: sleep-base gap.
- Bodh Gaya: sleep-base gap.
- Tiruvannamalai/Arunachala: sleep-base gap.
- Agra: exact hotel gap; max positioning night for HARD Taj sunrise/first-opening requirement.

Reisperiode: **18-12-2026 t/m 21-01-2027 = 34 dagen**, vluchten geboekt.

## KERNREIS / BESLUITEN
Reisperiode 18-12-2026 t/m 21-01-2027; terugvlucht Delhi. Zeker: Delhi zeer kort; Kumaon; Varanasi; Bodh Gaya; Tiruvannamalai / Arunachala. Vrindavan/Braj en Prayagraj/Allahabad kandidaat tot global closure. Haridwar/Kankhal/Rishikesh als zelfstandig cluster afgevallen; individuele uitzonderlijke sites mogen terugkomen. Oost geparkeerd tenzij capaciteit/exceptionele override.
AOAY/Yogananda blijft P0. Geen onzeker finding ooit stil filteren.

LET OP: bovenstaande historische kernstatus is inmiddels deels ingehaald door latere expliciete Mark-clusterbesluiten. Actueel geldt conform `CLUSTER_LEVEL_DECISIONS_2026-08-22.md`:
- Kumaon A;
- Vrindavan/Braj/Mathura A maar route-sensitive;
- Varanasi/Sarnath A;
- Bodh Gaya/Gaya A;
- Tiruvannamalai/Arunachala A fixed;
- Mysore/Bengaluru cluster C;
- Haridwar/Kankhal/Rishikesh cluster B/reserve;
- Agra A maar Taj-only route driver, sunrise hard requirement;
- Oost/Kolkata geparkeerd.
Bij conflict wint deze latere status.

Anandamayi Ma algemene scope: travel-core, NIET elk historisch huis/hostadres exhaustief oplossen. Een beperkt aantal zeer sterke, concrete en bezoekbare kernplekken is voldoende voor de reis, tenzij overlap/heritage/clusterwaarde een extra locatie relevant maakt.

HARD OVERRIDE — Anandamayi Ma × Paramahansa Yogananda joint-photo locations:
Elke fysiek oplosbare plek waar Anandamayi Ma en Paramahansa Yogananda samen op een gedocumenteerde foto staan moet altijd gericht worden opgelost en expliciet in de relevante clusterlijst verschijnen. Als het cluster in de reis komt, geldt de locatie als `MUST_VISIT_WITHIN_INCLUDED_CLUSTER` tenzij fysiek onmogelijk of historisch niet bruikbaar te lokaliseren. Deze regel overrulet de beperkte algemene Anandamayi-scope. Governance: `governance/ANANDAMAYI_YOGANANDA_PHOTO_OVERRIDE_2026-08-20.md`, commit `dd5c1aed639dc8057fd8c5b14a9dec1328064f6d`.

## METHODIEK
`LOCATION/CORPUS -> PERSON REVERSE -> ALL-FINDINGS LOSSLESS MASTER -> PHYSICAL RESOLUTION -> LOCAL PROXIMITY/BACKFILL -> nieuwe IDs -> Mark A/B/C -> TRAVEL COMPLETE`
R1 exact current; R2 exact historic successor; R3 strong localized approximation; R4 broad place; R5 unresolved.

## COMPLETE FEEDS
### BLAUW — COMPLETE
58 source records -> 58 entity mappings -> 0 silent drops. Central receipt `23d57b73e62c4f31d842175723aa9f1b6eb116d9`.

### TURQUOISE — COMPLETE
Entity merge/same-site/parent-child/successor/ambiguous rules complete. Central receipt `f5f8a69ef4f2a19063a83e1efa140754ef3e4af8`.

### GEEL — COMPLETE
Four-person closure complete; micro-sites split losslessly. Central receipt `b1f5b26de727ef735fc7edb4186f7ec07e36a2d5`.

### WIT — COMPLETE
Final schema-classified Anandamayi + heritage entities complete. Central receipt `3ef793a806bbb9b9bf28e0c34a0b3c90f3a8ac62`.

### ROOD — COMPLETE
Core Kriya closure complete. Source `e45dd559b7e442d47f2f94cfc548137d1f4ffd58`; entities `96d1a58eb4e5a34f6048c757bf7ed7149a68233d`; R4/R5 `cd817119ffdb6ec1af0293e8842f9cb3d6bde893`; access `844bdc276aafb2553b9c97584f14596f3f85d672`; STATUS COMPLETE `5443eeceab292c714d3c4e5b328f55d300464259`. Accounting: 178 source records = 146 claims + 32 negatives; 204 entity candidates; 58 micro/successor splits; R1 31 / R2 2 / R3 34 / R4 54 / R5 25; 0 silent drops. Central receipt `78500534100cbb1187e0603685a3c141368291fd`.

### ZILVER — FINAL COMPLETE
Final state verified on branch `agent/indiazilver-cluster-completeness-audit`: `COMPLETE_CURRENT_GLOBAL_FEEDS__READY_FOR_CENTRAL_MASTER`, blocked NO. No further loose ZILVER pass required.
Final outputs:
- protected canon `f491be93f9585e1a3eb9ac3e82362fc220d4c6f2`
- new-ID queue `a0f199fb055e6093e3e57b3540a2e73a38463e37`
- proximity `7ddcb764bb01a120f7d30c43f88f85d1554e4ba4`
- duplicate-parent `c64c67076d5cd7b32c9c4bb4a8e6e13c4bd0e668`
- ABC-after-closure queue `118cacae2ea9b48ef031f3b344dfc31709acb25d`
Final numeric totals: 16 pair calculations; 7 tight pairs = 4 <=1km + 3 >1-<=3km; guessed coordinates 0. Existing 001-081/A-B-C/locks unchanged. R4/R5 retained. READY_FOR_CENTRAL_MASTER = JA.

## CCI / CLAUDE CODE ROLE — AVAILABLE AND SHOULD BE USED STRATEGICALLY
CCI is a standing independent QA/reconciliation resource, not another color worker. Use it when a second pair of eyes materially lowers integration risk.
Current active CCI completeness task is relayed via PR #23. It must prioritize exhaustive AOAY/Yogananda integration and may NOT spend a full pass resolving every Anandamayi host-house merely for completeness. Joint-photo Anandamayi×Yogananda locations are the hard exception and must be resolved explicitly.

## FINAL FEED MANIFEST
Central manifest is ready:
`runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/FINAL_FEED_MANIFEST.md`
Commit `b0486eb3ca4cae911b809c14cf98848185de51cd`.

## ACTIVE WORKSTREAMS NOW — MAX TWO
1. INDIA8/9 central integration / travel-decision preparation.
2. CCI completeness closure / independent QA via PR #23.
No loose color workers remain active. Do not restart them unless central master exposes a genuinely isolated heavy correction task.

## IMMEDIATE NEXT ACTIONS — UPDATED 2026-08-23
1. Do NOT ask Mark to re-grade known locks. Use global canon audit first.
2. Use existing sleep bases as route origins. For Kumaon: Joshi Guest House / Hotel Evelyn / Turiya Niwas. For Varanasi: Sahi River View.
3. Resolve sleep-base gaps for Vrindavan/Braj, Bodh Gaya and Tiruvannamalai/Arunachala before detailed LP-distance/nights calculations there.
4. For Kumaon, build 3-base A/LP distance-and-combination matrix next; Jageshwar already A and Binsar already C, so neither is a new decision surface.
5. Integrate CCI Lonely-Planet gap-check when returned; do not restart full discovery.
6. Apply trip calendar/festival/closure layer before dates/transfers are frozen.
7. Preserve all A-site microdetails for final pre-visit day cards.

## HARDE GRENZEN
Geen A/B/C namens Mark. Geen silent filtering. Geen oude IDs/locks wijzigen. Geen PDF zonder PDF_GO. Geen merge zonder Mark. Oost geparkeerd. Ademruimte blijft reisdoel.
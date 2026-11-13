# COMPLETENESS_GATE — INDIA ZILVER

status: COMPLETE

## Gate-definitie

Een cluster krijgt `TRAVEL_COMPLETENESS_GATE: JA` uitsluitend wanneer:
1. `LOCATION_SWEEP_DONE: JA`;
2. `PERSON_REVERSE_DONE: JA` voor de relevante persoonslagen die in de repo beschikbaar zijn;
3. `LOCAL_PROXIMITY_DONE: JA`;
4. alle bekende nieuwe fysieke kandidaten een permanent ID hebben of expliciet als duplicate/non-candidate zijn opgelost (`NEW_IDS_ASSIGNED: JA`);
5. alle nieuwe fysieke kandidaten door Mark zijn beoordeeld (`NEW_ABC_REVIEWED: JA`);
6. geen bekende persoonslocatie als onbeoordeelde fysieke kandidaat tussen de lagen blijft hangen.

`PERSON_REVERSE_DONE` betekent hier niet dat iedere historische persoon absoluut saturated is; het betekent dat de voor dit cluster bekende beschikbare reverse-resultaten zijn verwerkt. Wanneer een relevante person-reconciliatie zelf `SATURATED: NEE` meldt, wordt dat als open epistemische beperking vermeld en kan de travel gate niet op basis van schijnzekerheid worden gesloten.

## Toepassing per cluster

| cluster | LOCATION_SWEEP_DONE | PERSON_REVERSE_DONE | LOCAL_PROXIMITY_DONE | NEW_IDS_ASSIGNED | NEW_ABC_REVIEWED | TRAVEL_COMPLETENESS_GATE | reden |
|---|---|---|---|---|---|---|---|
| VARANASI | JA | **NEE** | NEE | NEE | NEE | **NEE** | latere Lahiri/Sri-Yukteswar-reconciliaties leveren Rana Mahal + dedup/identity-leads op; Core-Kriya saturation blijft deels open |
| BODH GAYA / GAYA-CORRIDOR | JA | **NEE** | NEE | NVT/NEE | NVT/NEE | **NEE** | Sri-Yukteswar Bodh-Gaya-vows lead en Rajgir-signaal nog niet fysiek lokaal teruggevuld; persoonslaag niet volledig verwerkt |
| KUMAON | JA (legacy + resweep) | **NEE** | NEE | DEELS | DEELS | **NEE** | 079/080/081 opgelost, maar Almora/Vivekananda-region-miss en resterende tijdelijke circuitpunten houden de gate open |
| TIRUVANNAMALAI / ARUNACHALA | NEE | DEELS | NEE | NEE | NEE | **NEE** | Mark A-cluster locked, maar regionale METHOD_V2 dubbele sweep expliciet nog niet voltooid; 5 fysieke person-sites wachten op regionale reconciliatie/IDs/review |
| PURI / ODISHA | NEE | DEELS | NEE | NEE | NEE | **NEE** | Karar + Balighai vormen nieuw person-discovered cluster; nog geen regionale sweep/reeks/A-B-C |
| KOLKATA / WEST-BENGAL CORE | NEE | DEELS | NEE | NEE | NEE | **NEE** | meerdere nieuwe sterke fysieke locaties en Core-Kriya Tier-2/Tier-1 leads; nog geen regionale reconciliatie |
| VRINDAVAN | NEE/ONBEKEND als zelfstandige complete cluster | DEELS | NEE | NEE | NEE | **NEE** | bestaande NKB-site plus nieuwe Anandamayi/Akrura-punten; lokale dedup/proximity ontbreekt |
| HARIDWAR/KANKHAL | NEE | DEELS | NEE | NEE | NEE | **NEE** | Matri Mandir is nieuw sterk punt; hostgraph-leads bestaan; geen regionaal complete laag |
| DELHI | NEE | DEELS | NEE | NEE | NEE | **NEE** | twee NKB T1-sites + Anandamayi T2-signaal; geen regionale sweep/review |
| overige nieuwe losse regio's (Ranchi, Wardha, Gorakhpur, Kanpur, Khetri, Kanyakumari, Dehradun) | NEE | DEELS | NEE | NEE | NEE | **NEE** | person-first discovery moet nog door location + proximity + ID + Mark-review heen |

## Heropen-gate

Voor de drie eerder afgewerkte travelclusters geldt:

- **VARANASI: REOPEN_REQUIRED JA**
- **BODH GAYA/GAYA-CORRIDOR: REOPEN_REQUIRED JA**
- **KUMAON: REOPEN_REQUIRED JA**

Deze heropening verwijdert geen eerder werk. Ze voegt reverse-discovery, dedup, proximity en review toe aan wat al bestaat.

## Stopvoorwaarden vóór opnieuw sluiten

### Varanasi
- Rana Mahal Ghat fysieke identity + betrouwbare coördinaat;
- dedup Panchganga Ghat Ashram tegen 004/011;
- dedup Ramnagar palace tegen 044;
- Benares-leads uit Sri-Yukteswar/Lahiri reconciliaties triëren op huidige fysieke identiteit;
- daarna proximity-bands tegen alle bestaande beoordeelde VNS-sites;
- nieuw ID append-only waar echt nieuw;
- Mark A/B/C review.

### Bodh Gaya/Gaya-corridor
- Sri-Yukteswar Bodh-Gaya-vows claim tot fysieke site of expliciet `ALLEEN_PLAATS/UNRESOLVED` oplossen;
- Rajgir-signaal correct buiten/binnen lokale backfill begrenzen zonder routekeuze;
- proximity-backfill uitvoeren;
- eventuele nieuwe fysieke sites via ID + Mark-review verwerken.

### Kumaon
- Almora Vivekananda `REGION_MISS` tot exacte fysieke kandidaat of `ALLEEN_PLAATS` oplossen;
- resterende relevante tijdelijke Vivekananda-circuitpunten identity-checken zoals de bestaande status voorschrijft;
- proximity-backfill op nieuwe/geredde sites afronden;
- geen bestaande 079/080/081 wijzigen.

## Projectbrede conclusie

Op deze branch krijgt **geen** geauditeerd cluster `TRAVEL_COMPLETENESS_GATE: JA`. Dat is een bewuste kwaliteitsuitkomst: eerder 'afgerond' betekende in enkele gevallen alleen dat de location-first laag klaar was. De nieuwe standaard vereist location-first + person-reverse + local-proximity + immutable IDs + Mark-review.

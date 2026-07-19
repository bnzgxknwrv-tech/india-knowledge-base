# Compact predecessorcontext — KUMAON-COMPLETE-001

## Autoriteit

Mark heeft het definitieve INDIA2-rapport van `VRINDAVAN-KUMAON-CORRIDOR-001` ontvangen en geaccepteerd. BRONS voert die oude corridorbeoordeling niet opnieuw uit en gebruikt geen oude rapportconclusie als vervanging voor de nieuwe volledige Kumaon-sweep.

## Technisch gevalideerde predecessor

- Validatierun: `VRINDAVAN-KUMAON-CORRIDOR-001`.
- Technische eindvalidatiecommit: `ea6f2eda979f2aaf8827648227fa39c8bfc2444b`.
- Gerepareerde inhoudelijke broncommit: `264bba42b299110689c3b877ce3dbae2cdcf0e6b`.
- Technische integriteit: `PASS`.
- Inhoudelijke predecessorstatus: `PARTIAL`.
- Geaccepteerde corridoruitkomst: `DOORREIZEN_NAAR_KUMAON`.
- Bestaande formele projectdekking bleef 28 A, 2 B en 4 C; de Kumaon-subset staat afzonderlijk in deze run gepind.
- Veertig predecessorpunten bleven `WORKING_GEO`; een exacte bezoekersingang was geen vrijgavevoorwaarde.
- De oude run gebruikte het eerdere schema-v2-proces en is niet naar inline handoff gemigreerd.

## Wat BRONS moet behouden

1. Bestaande Kumaon-`LOCATION_ID`'s 400–426 exact behouden.
2. Aankomstknooppunten 308 Lal Kuan, 309 Haldwani en 310 Kathgodam behouden.
3. Formele A/B/C uit `formal_status_snapshot.yaml` niet herwaarderen.
4. Bestaande `WORKING_GEO`-punten behandelen als voorgangerpunten die mogen worden bevestigd, verfijnd of gemotiveerd gecorrigeerd, maar niet stil verwijderd.
5. Fysieke plekken met onzekere exacte ingang zichtbaar houden via de vaste GEO-fallback.
6. Oude corridor-, trein- en winterconclusies alleen gebruiken om dubbel werk te voorkomen; datumgebonden praktische gegevens opnieuw controleren wanneer zij voor de nieuwe Kumaon-scope dragend zijn.

## Compacte predecessorbestanden die BRONS mag lezen

- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/formal_status_snapshot.yaml` — formele projectstatussen.
- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/location_id_plan.yaml` — bestaande Kumaon seed-ID's en vrije reeks vanaf 427.
- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/GOUD/working_geo.jsonl` — bestaande WORKING_GEO-punten, puntsoorten en nauwkeurigheid.
- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/GOUD/central_map_source.jsonl` — bestaande kaartlagen en markersemantiek.
- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/GOUD/report/03_geo_location_ids_and_map_readiness.md` — compacte GEO- en ID-validatie.
- `research/active/VRINDAVAN-KUMAON-CORRIDOR-001/transitions/SUBREGIE_FINAL_VALIDATION.md` — technische betrouwbaarheid en resterende beperkingen.

Volledige oude BRONS-, ZILVER- of GOUD-rapportpakketten zijn verboden voor de BRONS-context, tenzij een concrete loss-controlfout ontstaat. Dit voorkomt herhaling van de geaccepteerde oude inhoudelijke beoordeling.

## Wat de predecessor niet oplost

De predecessor was geen volledige Kumaon-clustersweep. Zij bepaalt niet:

- het beste treinaankomststation;
- de beste eerste basis;
- de eerste echte bezoeklocatie;
- de interne volgorde;
- de laatste Kumaon-locatie;
- de uitreisrichting;
- een volledige vergelijking van Bhowali, Nainital, Kainchi, Kathgodam en Haldwani;
- alle gemiste fysieke locaties in de Kumaon-subclusters;
- de complete runlokale Kumaon-KML met de zeven nieuwe lagen.

Deze gaten vormen de nieuwe inhoudelijke scope en mogen niet als reeds opgelost worden gepresenteerd.

END_OF_ARTIFACT
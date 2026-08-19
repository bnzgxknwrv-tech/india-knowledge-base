# INDIA ORANJE — TRAVEL/HEATMAP PREP

STATUS: READY
OWNER: INDIA ORANJE
MODE: PARALLEL NON-PERSON-RESEARCH
GOAL: verkort de weg van persoonsatlassen naar reisplanning zonder lopende persoonsreconciliaties te verstoren.

## Opdracht
Bouw een TRAVEL-READINESS raamwerk voor de uiteindelijke India-reis, ZONDER nieuwe persoonslocaties te onderzoeken en ZONDER bestaande persoonsresultaten inhoudelijk te vergelijken.

Lever 4 onderdelen:
1. HEATMAP_SCHEMA.md — exact schema waarmee later gereconcilieerde locaties automatisch per stad/regio kunnen worden geaggregeerd: persoon, bewijsniveau, fysieke exactheid, A-anker/locked, unieke-persooncount, locatiecount, conflictflag, travel-significance nog ONBESLIST.
2. CLUSTER_TRIGGER_RULES.md — objectieve regels wanneer een regio na de landelijke persoonslaag wel/geen regionale deep sweep nodig heeft. Geen A/B/C-keuze maken.
3. TRAVEL_PIPELINE.md — minimale keten van gereconcilieerde persoonsrecords -> heatmap -> regionale verificatie -> Mark A/B/C -> route/nachten -> transport -> verblijf -> dagplanning. Benoem welke stappen parallel kunnen.
4. OPEN_GATES_MATRIX.md — inventariseer uitsluitend governance/status/taakmetadata (geen verboden blinde onderzoeksinhoud) en maak een matrix van welke Top-11 personen/gates nog open zijn, welke al voldoende detectorlagen hebben en welke taak het kritieke pad vormt.

## Projectgrenzen
- Arunachala/Tiruvannamalai blijft LOCKED_BY_MARK A-anker; geen inhoudelijke regio-sweep starten.
- Babaji-grot Kukuchina/Dunagiri blijft hoofdreden van de reis.
- Vivekananda en Hariharananda: geen exhaustieve landelijke deep sweep; alleen later grootste/belangrijkste locaties gericht verifiëren.
- Geen A/B/C namens Mark.
- Geen route of nachten vastleggen.
- Geen PDF.
- Geen merge/PR.
- Geen nieuwe webresearch naar persoonslocaties.
- Deze taak mag bestaande governance, decisions, STATUS.md en taakmetadata lezen voor processtatus; gebruik geen blind branches als inhoudelijke bron.

## Output
Schrijf de vier bestanden onder runs/active/INDIAORANGE-TRAVEL-HEATMAP-PREP-001/ en update STATUS.md. Commit op agent/indiaorange-travel-heatmap-prep. Rapporteer SHA's aan Mark/INDIA8.

# INDIATURQUOISE ENTITY / OVERLAP RECONCILIATION

## DOEL
Bouw de cross-person fysieke entity-merge-map die nodig is om honderden bronclaims zonder verlies naar unieke fysieke plekken te reconciliëren.

## LEES
- eerdere TURQUOISE all-person overlap/heatmap outputs
- alle gereconcilieerde person matrices die op deze branch reeds toegestaan/beschikbaar zijn
- same-site/heritage/cluster outputs
- governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md

## UITVOEREN
1. Zoek cross-person exact-same-site overlaps, aliases/spellingvarianten, historical-successor-relaties en micro-site -> parent-complex relaties.
2. Maak NOOIT een merge alleen op plaatsnaam/stad. Vereis fysieke identity-evidence.
3. Behoud per entity alle source-record IDs, personen, events en onzekerheden.
4. Same complex but different micro-site = parent-child, niet automatisch duplicate.
5. Historical building verdwenen maar successor memorial/site aanwezig = successor relation, niet stil gelijkmaken.
6. Maak speciale overlapprioriteit voor Varanasi, Kumaon, Bodh Gaya, Tiruvannamalai/Arunachala, Vrindavan/Braj, Prayagraj/Allahabad, Delhi en heritage stays.
7. Oost-data volledig meenemen in entity-map maar route niet heropenen.

## OUTPUTS
- ENTITY_MERGE_MAP.jsonl
- SAME_SITE_OVERLAP_MATRIX.md
- PARENT_CHILD_SITE_MAP.md
- SUCCESSOR_SITE_MAP.md
- AMBIGUOUS_MERGES_QUEUE.md
- STATUS.md

## HARD
Geen bronrecord verwijderen. Geen A/B/C. Geen IDs wijzigen. Geen route. Commit alles op dezelfde branch.
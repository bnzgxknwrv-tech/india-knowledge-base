# INDIA4 BATCHOUTPUT

Per kandidaat één volledige JSONL-regel met minimaal:
- candidate_id
- candidate_name
- candidate_description
- google_maps_search_term
- google_maps_found_name
- google_maps_public_link_or_finding
- latitude
- longitude
- name_check
- locality_ghat_address_check
- marker_status: EXACT_GOOGLE_MAPS_MARKER | GOOGLE_MAPS_MARKER_NOT_CONFIRMED
- old_coordinate
- difference_or_problem
- sources
- uncertainty_note

Regels moeten volledig en geldig zijn. Geen gedeeltelijke JSONL-regels. Bij hervatting reeds afgeronde candidate_id’s niet opnieuw onderzoeken.

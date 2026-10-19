# INDIA4 BATCHOUTPUT

Per kandidaat één volledige JSONL-regel met minimaal:

**Betekenisvelden (vanaf 2026-08-02, INDIA2-architectuurbesluit, ingevuld VÓÓR de GEO-velden):**
- why_this_one — waarom deze specifieke plek, niet als generieke categorie
- why_not_the_others — waarom niet de vergelijkbare/nabijgelegen alternatieven
- meaning_evidence — brongewogen onderbouwing van de betekenis (zie
  `india4/protocols/RESEARCH_QUALITY.md`), geen generieke toeristische bron als enige bron
- living_or_monumental — is de traditie/praktijk hier nog levend, of uitsluitend
  monumentaal/historisch
- mark_relevance_link — koppeling aan Marks bekende interesses/A-criteria (uit de
  PRE-BRONS-brief van deze regio)

**GEO-velden (zoals voorheen):**
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

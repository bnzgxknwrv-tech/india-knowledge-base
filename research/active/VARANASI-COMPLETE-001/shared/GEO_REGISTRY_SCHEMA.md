# MASTER A/B GEO registry schema

The canonical editable source for the run is `MASTER_A_B_GEO_REGISTRY.jsonl`. One JSON object per physical location.

Required keys:
`location_id`, `canonical_name`, `display_name_nl`, `marker_name`, `cluster`, `formal_status`, `latitude`, `longitude`, `geo_status`, `geo_source_type`, `geo_source_reference`, `accuracy_class`, `exactness_note`, `last_checked_at`, `source_run`, `recognition_hook`, `open_geo_question`, `active`.

Allowed formal status: `A_FORMEEL`, `B_FORMEEL`.
Allowed geo status: `VERIFIED_EXACT`, `VERIFIED_SITE_CENTRE`, `WORKING_GOOGLE_MAPS_PIN`, `WORKING_ADDRESS_POINT`, `APPROXIMATE_LOCAL_POINT`, `MISSING`.
Allowed accuracy class: `0_25_M`, `25_100_M`, `100_500_M`, `SITE_LEVEL`, `LOCALITY_LEVEL`, `UNKNOWN`.

Editing rule: update the registry first, validate uniqueness and coverage, then regenerate the KML. Never edit only the KML.
Status rule: only Mark may change a formal A/B/C status. Workers may record an advisory proposal separately.
Naming rule: `marker_name` must be understandable without opening the description. For mainly Indian names add a short Dutch function in parentheses.
Colour rule: A is green; B is orange. No category logos.

END_OF_ARTIFACT

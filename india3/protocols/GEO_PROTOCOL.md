# GEO PROTOCOL

## Mandatory capability check
Record whether direct Google Maps place operation is available. Do not claim visual verification without actual direct place access and identity matching.

## GEO statuses
- `VERIFIED_GOOGLE_MAPS_PLACE`: direct place record opened; name, type, locality and physical context matched.
- `VERIFIED_OFFICIAL_MAP_LINK`: official institution/site map link opened and matched; not necessarily Google Maps visual verification.
- `VERIFIED_SITE_CENTRE`: site polygon or clearly identified physical complex centre cross-checked by at least two suitable sources.
- `WORKING_CROSSCHECKED_MAP_POINT`: practical map point cross-checked by name, locality and nearby anchors; suitable for working maps, not exact entrance claims.
- `APPROXIMATE_LOCAL_POINT`: locality-level point only; uncertainty radius and reason required.
- `NOT_ESTABLISHED`: no reliable point established.
- `TOOL_LIMITED`: evidence may exist but current tools cannot perform the required verification.

## Required fields
candidate_id, coordinates, point_type, geo_status, source_ids, access_method, identity_checks, nearby_anchor_checks, rejected_points, Mark_rejection_ids, checked_by_role, checked_at, residual_uncertainty.

KML syntax, marker counts and coordinate validity are separate checks and never raise GEO status. An explicitly Mark-rejected coordinate cannot be reused until superseded by a later Mark decision. One unresolved point does not block unrelated candidates.

END_OF_ARTIFACT

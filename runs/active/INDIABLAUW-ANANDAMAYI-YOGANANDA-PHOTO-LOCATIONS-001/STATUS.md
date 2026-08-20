# STATUS — INDIABLAUW-ANANDAMAYI-YOGANANDA-PHOTO-LOCATIONS-001

state: COMPLETE
blocked: NO
priority: P0_FOCUSED
completed: 2026-08-20
branch: agent/indiablauw-trip-ops-prep
scope: joint Anandamayi Ma + Paramahansa Yogananda photos/film only

outputs:
  - PHOTO_EVENT_LEDGER.md
  - PHOTO_LOCATION_CLOSURE.jsonl
  - TRAVEL_OVERRIDE_SUMMARY.md

accounting:
  physical_photo_events: 2
  film_provenance_events: 1
  silent_drops: 0

closures:
  - Bhowanipur/Calcutta first meeting: December 1935; joint-photo event retained R4. Neighborhood and disciple-home/automobile scene secure; host identity and parcel unresolved after targeted scoped research.
  - Ranchi Vidyalaya: explicit AOAY garden photo session by Richard Wright; R2 campus/garden, R4 exact camera station. Strongest MUST_VISIT_WITHIN_INCLUDED_CLUSTER candidate if Ranchi is included, subject to YSS access.
  - 1930s motion-picture footage: existence documented; film-specific physical location unresolved R5. No invented third site.

important_negative:
  - Serampore station is a documented later Anandamayi-Yogananda encounter but no scoped source establishes a joint photograph there; therefore not falsely promoted as photo-location.
  - Wikimedia/public mirrors showing 1910/1915 dates for joint images conflict with official December-1935 first-meeting chronology and are treated as bad metadata, not extra events.

constraints:
  abc_changed: false
  permanent_ids_created: false
  route_changed: false
  nationwide_anandamayi_host_sweep_started: false

blockers:
  - Exact Bhowanipur disciple/host and civic parcel remain unresolved in scoped official/archival sources.
  - Exact Ranchi garden camera station is not recoverable from textual evidence alone.
  - Surviving film frames lack location metadata sufficient to distinguish Ranchi vs Calcutta or prove another site.

stop_condition: MET — every joint photo/film event found in scoped sources has a physical location or explicit unresolved disposition; zero silent drops.

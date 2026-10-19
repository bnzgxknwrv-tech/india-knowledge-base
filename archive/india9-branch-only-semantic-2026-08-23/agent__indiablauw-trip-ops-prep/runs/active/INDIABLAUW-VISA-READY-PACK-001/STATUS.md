# STATUS — INDIABLAUW-VISA-READY-PACK-001

state: COMPLETE
branch: agent/indiablauw-trip-ops-prep
owner: INDIA BLAUW
completed: 2026-08-19
official_sources_rechecked: 2026-08-19
source_policy: official Indian Government sources only for visa requirements

outputs:
  - VISA_APPLICATION_CHECKLIST.md
  - VISA_FORM_FIELD_PREP.md
  - PHOTO_PASSPORT_SPEC.md
  - VISA_TIMING_RECOMMENDATION.md
  - VISA_SCAM_GUARD.md
  - VISA_READY_STATUS.md

constraints_respected:
  - visa_application_submitted: false
  - personal_data_guessed_or_external_collected: false
  - person_location_research: false
  - route_or_hotel_choice: false
  - destination_choice_for_mark: false
  - pdf_created: false
  - merge_or_pr: false

key_verified_facts:
  - Netherlands is e-Visa eligible.
  - 1-year and 5-year e-Tourist Visa are multiple-entry options.
  - For 1y/5y e-Tourist Visa the official application window is up to 120 days before proposed travel and minimum 4 days before arrival.
  - For planned arrival 2026-12-18 the 120-day window opens 2026-08-20.
  - Passport must have at least six months validity at time of e-Visa application.
  - Photo: JPEG, 10 KB–1 MB, square, official face/background requirements apply.
  - Passport bio page: PDF, 10–300 KB.
  - Only official e-Visa application website: https://indianvisaonline.gov.in/evisa/ .

blockers:
  - Mark must choose the actual visa validity option when submitting; no choice was made on his behalf.
  - Personal/family/employment/previous-visa data not already available must be entered by Mark and was not guessed.
  - Arrival/exit port and any India reference must wait for real trip facts; no route/hotel placeholder was invented.
  - Exact country-specific fee and live form wording must be rechecked on submission day because portal rules/fees can change.

next_allowed_step: Mark can supply/verify his own application data and submit through the official portal once he chooses to do so; recheck official rules on submission day.

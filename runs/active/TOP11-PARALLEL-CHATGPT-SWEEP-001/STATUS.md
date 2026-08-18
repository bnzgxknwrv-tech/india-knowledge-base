# STATUS — TOP11-PARALLEL-CHATGPT-SWEEP-001

state: EXTERNAL_BLIND_PARALLEL_SWEEP_IN_PROGRESS
branch: agent/chatgpt-top11-parallel-sweep
comparison_with_internal_allowed: NEE

## PERSONEN
- Yogananda: FROZEN
  - normalized_location_count: 127
  - physical_identity: EXACT 48; DEELS 20; ALLEEN_PLAATS 15; ONBEKEND 44
  - corpus_families: autobiography/travel narrative; YSS institutional site histories; photo captions; hosts/family/disciples; itinerary nodes; private houses/lodging; schools/halls/temples/gardens; room-level sublocations
  - blocked_sources: family diaries/correspondence; complete Mejda/later appendices; municipal/cadastral records; hotel/palace/rail registers; Kumbh camp plans; private-house access; photo negatives
  - saturation: NEE — primary narrative swept, but unnamed houses, hotels, camps, route stops, rooms and photo locations remain archive-dependent
  - freeze_sha: 69a387d162b4fe7b89b63bbd1b11f0d56e62443d
- Mahavatar Babaji: IN_PROGRESS
- Lahiri Mahasaya: IN_PROGRESS
- Sri Yukteswar: FROZEN
  - normalized_location_count: 38
  - physical_identity: EXACT 11; DEELS 23; ALLEEN_PLAATS 3; ONBEKEND 1
  - corpus_families: primary/semi-primary published narrative; institutional histories; ashrams; private homes; travel and pilgrimage nodes; room/sublocation evidence; adversarial negative checks
  - blocked_sources: complete Satyananda biography; private-address and room records; Kashmir inn records; cadastral confirmation for relative sites
  - saturation: NEE — broad source/type/place sweep completed, but inaccessible biography and unresolved private/relative locations leave material leads
  - freeze_sha: 7ebad72652cf14d750c00aaa77fc25f53f2be2cd
- Neem Karoli Baba: IN_PROGRESS
- Ram Dass: IN_PROGRESS
- Ramana Maharshi: QUEUED
- Ramakrishna: QUEUED

## HARD
Lees vóór de acht PRE-COMPARE freezes geen interne persoonsresultaten of kandidaatlijsten. Schrijf alleen op deze branch. Commit per persoon.

next_allowed_step: onafhankelijke externe persoons-sweeps uitvoeren en iedere persoonsfreeze direct afzonderlijk committen; daarna STOP zonder reconciliatie.
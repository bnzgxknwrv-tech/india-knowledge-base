# FEED — INDIA GEEL FOUR-PERSON LOCATION CLOSURE

Date: 2026-08-20
Source branch: `agent/indiageel-ramana-ramakrishna-sweep`
Task: `INDIAGEEL-FOURPERSON-LOCATION-CLOSURE-001`
State: COMPLETE

## OUTPUT COMMITS
- FOURPERSON_SOURCE_RECORDS.jsonl — `9cbf630f55858afabf53839dd6d3c9269baee695`
- FOURPERSON_ENTITY_CANDIDATES.jsonl — `30486eaf3478057246727a56fd5fb8a5b22a1189`
- FOURPERSON_R4_R5_CLOSURE.md — `314094dc49a539fc71fc4117e2d27cd51a54c554`
- FOURPERSON_ACCESS_MATRIX.md — `da7184ab727b3100a5c43dbd068e32fb45c696a7`
- STATUS COMPLETE — `9c0b1a0d7ec5b8990287cb79c53f17db52f93f09`

## PRESERVATION
SILENT_DROPS=0; EXISTING_IDS_CHANGED=NEE; A_B_C_CHANGED=NEE.

## IMPORTANT MICRO-SITE EXPANSION
- Hotel Evelyn -> hotel / cave-room / patio kept separately.
- Kainchi + Bhumiadhar -> rooms / river / bridge / field kept separately.
- NKB final journey -> separate Agra houses, clinic, stations, Mathura station/microplace, Vrindavan hospital.
- Ramana -> Virupaksha and Mango Tree Cave separate; Ramanasramam microsites separated.
- Ramakrishna -> Fouzdar Kunj building/room/veranda; Ganga Mata hut vs later dharamshala; Mani Sen house vs Radhakanta temple; Cossipore house/room/cremation ghat.

## STILL R4/R5 — NEVER DROP
Exact Hotel Evelyn cave-room, K.K. Sah address, Ram Dass Varanasi hotel, Surat cave, some Delhi/Dharamsala sites, NKB Agra hosts/clinic, various historic Kolkata houses.

## INPUT PROVENANCE NOTE
Task named two reconciliation paths + governance file that were absent on GEEL branch. GEEL used same-branch reconciliation for NKB/Ram Dass and own freezes + available CCI detector layer for Ramana/Ramakrishna. This provenance limitation is recorded and does not justify redoing completed physical-resolution work unless later central cross-branch reconciliation finds a concrete omitted source record.

## CENTRAL ACTION
Ingest all GEEL entities into ALL_FINDINGS_LOCATION_MASTER. Apply TURQUOISE parent-child/successor rules. Feed newly resolved R1-R3 entities and child microsites to ZILVER proximity/new-ID staging immediately. Preserve R4/R5 in unresolved accounting.

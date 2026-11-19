# GEEL ENTITY FEED — from INDIA8

Source branch: `agent/indiageel-ramana-ramakrishna-sweep`
Task: `INDIAGEEL-FOURPERSON-LOCATION-CLOSURE-001`
State: COMPLETE

Consume immediately in staged proximity/new-ID work.

Commits:
- source `9cbf630f55858afabf53839dd6d3c9269baee695`
- entities `30486eaf3478057246727a56fd5fb8a5b22a1189`
- R4/R5 `314094dc49a539fc71fc4117e2d27cd51a54c554`
- access `da7184ab727b3100a5c43dbd068e32fb45c696a7`
- status `9c0b1a0d7ec5b8990287cb79c53f17db52f93f09`

Rules:
- preserve micro-sites separately: Hotel Evelyn hotel/cave-room/patio; Kainchi/Bhumiadhar rooms/river/bridge/field; NKB final-journey sub-sites; Ramana caves/Ramanasramam microsites; Ramakrishna Fouzdar Kunj building/room/veranda, Ganga Mata hut/dharamshala, Mani Sen house/Radhakanta temple, Cossipore house/room/cremation ghat.
- apply TURQUOISE parent-child/successor map; do not collapse children to parent.
- for R1-R3 with reliable coordinates: calculate <=1km/<=3km and stage NEW_ID_REQUIRED where appropriate.
- for R4/R5: retain dependency; no guessed coordinate.
- no existing ID/A/B/C/lock changes.

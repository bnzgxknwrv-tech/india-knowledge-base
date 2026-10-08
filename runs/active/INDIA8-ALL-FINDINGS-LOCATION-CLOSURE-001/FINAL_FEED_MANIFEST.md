# FINAL FEED MANIFEST — CENTRAL MASTER

Date: 2026-08-20
State: READY_FOR_FULL_MASTER_INGEST

## BLAUW — AOAY/YOGANANDA
Branch: `agent/indiablauw-trip-ops-prep`
Task: `INDIABLAUW-AOAY-YOGANANDA-LOCATION-CLOSURE-001`
Source records: 58
Entity mappings: 58
Silent drops: 0
Commits:
- source `18d472cce9f145187a1ca6e3071fbf62eaf529fe`
- entities `7e60302cf46cd2380e1fae03978a14706d23ae9f`
- R4/R5 `7122f85dad8e3d0710e48df83ee72eae56b5d5d2`
- access `90d14cb6bcbdd7e88c4c83ee3e7bfa0084ac67d6`
- status `58854d1840147b8ae2f1eff42b310e417cb5d836`

## TURQUOISE — ENTITY / OVERLAP RECONCILIATION
Branch: `agent/indiaturquoise-allperson-overlap`
- merge map `f5e156f3e23850cc5f52f71bf26ff3a2346b6900`
- same-site `4cd8396f6acf19b70564a34a833bed5ab020624a`
- parent-child `fedf7432d8458f4efa47b41bc93007e77229f2c2`
- successor `9759e86dadf8f1fc28047549bdcc304420ecd514`
- ambiguous `473d90a6cda65a182b58180daf9290c8432d134a`
- status `0aef428540474bcee26122f3913c26ced6aad10f`

## GEEL — FOUR PERSON
Branch: `agent/indiageel-ramana-ramakrishna-sweep`
- source `9cbf630f55858afabf53839dd6d3c9269baee695`
- entities `30486eaf3478057246727a56fd5fb8a5b22a1189`
- R4/R5 `314094dc49a539fc71fc4117e2d27cd51a54c554`
- access `da7184ab727b3100a5c43dbd068e32fb45c696a7`
- status `9c0b1a0d7ec5b8990287cb79c53f17db52f93f09`
Silent drops: 0

## WIT — ANANDAMAYI / HERITAGE
Branch: `agent/indiawit-master-travel-readiness`
Final schema-classified:
- Anandamayi entities `379b637706023b6f1891ba53e89b16150c193fee`
- heritage matrix `ef493aad36650de1dcc7caa24645bab185ee3ab5`
- status COMPLETE `b5ec1abddfe23669c8ea273970760944d312a90a`
Earlier source/closure/access commits remain provenance and must be preserved.

## ROOD — CORE KRIYA
Branch: `agent/indiarood-core-kriya-sweep`
- source `e45dd559b7e442d47f2f94cfc548137d1f4ffd58` — 178 lossless records = 146 claims + 32 negatives
- entities `96d1a58eb4e5a34f6048c757bf7ed7149a68233d` — 204 candidates incl. 58 micro/successor splits
- R4/R5 `cd817119ffdb6ec1af0293e8842f9cb3d6bde893`
- access `844bdc276aafb2553b9c97584f14596f3f85d672`
- final status `5443eeceab292c714d3c4e5b328f55d300464259`
R distribution claims: R1 31 / R2 2 / R3 34 / R4 54 / R5 25.
No silent drops; claimant traditions separated.

## ZILVER — FINAL GLOBAL STAGING
Branch: `agent/indiazilver-cluster-completeness-audit`
Final state: `COMPLETE_CURRENT_GLOBAL_FEEDS__READY_FOR_CENTRAL_MASTER`
- protected canon `f491be93f9585e1a3eb9ac3e82362fc220d4c6f2`
- new-ID queue `a0f199fb055e6093e3e57b3540a2e73a38463e37`
- proximity `7ddcb764bb01a120f7d30c43f88f85d1554e4ba4`
- duplicate-parent `c64c67076d5cd7b32c9c4bb4a8e6e13c4bd0e668`
- ABC-after-closure queue `118cacae2ea9b48ef031f3b344dfc31709acb25d`
- status current blob verified on 2026-08-20
Numeric pair calculations 16; tight pairs 7 = 4 <=1km + 3 >1-<=3km; guessed coordinates 0.

## CENTRAL INGEST RULES
- All source claims must retain disposition/source links.
- Existing permanent IDs 001-081 immutable.
- Existing A/B/C and locks immutable until Mark explicitly reviews.
- Parent/child microsites remain distinct.
- Historic/current successor relation remains explicit.
- R4/R5 remain visible and are not A/B/C-ready.
- New R1-R3 physical entities requiring IDs are staged exactly once.
- AOAY P0 and heritage-room/stay records get explicit visibility flags.
- East data retained even while route-deprioritized.

## NEXT
Build consolidated ALL_FINDINGS_LOCATION_MASTER + accounting summary + unresolved queue + cluster-ready projection. In parallel CCI performs independent master QA using `CCI_MASTER_QA_TASK.md`.

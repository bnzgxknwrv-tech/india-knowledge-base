# INDIA8 -> INDIA9 LIVE HANDOFF — 2026-08-20

## MANDATORY FIRST READ FOR INDIA9+
Lees vóór regie-uitvoering:
`governance/INDIA_REGIE_DOORGANGSPROTOCOL_2026-08-20.md`
Commit: `4a0acf0a397c221a29955dee84b55c4508b72bb0`.
Dit protocol is HARD: nooit eindigen met alleen status/volgende stap; iedere beurt moet daadwerkelijk uitvoeren/starten of parallel dispatchen zolang veilig zelfstandig werk bestaat.

## DOEL
Deze file maakt INDIA8 onmiddellijk vervangbaar. GitHub is source of truth; chatgeschiedenis is niet vereist.

## KERNREIS / BESLUITEN
Reisperiode 18-12-2026 t/m 21-01-2027; terugvlucht Delhi. Zeker: Delhi zeer kort (alleen expliciete A: Mahasamadhi Shri Mataji Nirmala Devi), Kumaon, Varanasi, Bodh Gaya, Tiruvannamalai / Arunachala. Vrindavan/Braj en Prayagraj/Allahabad blijven kandidaat tot global closure. Haridwar/Kankhal/Rishikesh is als zelfstandig cluster afgevallen, maar individuele uitzonderlijke sites mogen terugkomen. Oost (Ranchi/Kolkata/Puri) geparkeerd voor deze reis tenzij capaciteit/exceptionele override.
AOAY/Yogananda is P0: kleine concrete AOAY-scènes kunnen voor Mark zwaarder wegen dan beroemde sites. Geen onzeker finding ooit stil filteren.

## METHODIEK
`LOCATION/CORPUS -> PERSON REVERSE -> ALL-FINDINGS LOSSLESS MASTER -> PHYSICAL RESOLUTION -> LOCAL PROXIMITY/BACKFILL -> nieuwe IDs -> Mark A/B/C -> TRAVEL COMPLETE`
Resolution: R1 exact current; R2 exact historic successor; R3 strong localized approximation; R4 broad place; R5 unresolved. Oude/mythische claims mogen eerlijk op R3 eindigen; 20e-eeuwse hotels/huizen/kamers moeten veel harder exact worden onderzocht.
Geen oude IDs renummeren. Geen bestaande A/B/C of locks stil wijzigen. Nieuwe fysieke candidates later append-only ID + eigen Mark A/B/C. Oude B/C kan REVIEW_FOR_UPGRADE krijgen.

## GLOBAL SOURCE ACCOUNTING
Centrale taak: `runs/active/INDIA8-ALL-FINDINGS-LOCATION-CLOSURE-001/TASK.md` op `agent/india8-cluster-casting`.
Bronlaag lower bound >=856 claims/listed records; NIET uniek-site-totaal. Unique physical entity count blijft unset tot iedere source claim disposition heeft.

## PARALLEL LOCATION-CLOSURE DISPATCH
Zes stromen: BLAUW AOAY/Yogananda; ROOD Core Kriya; GEEL NKB/Ram Dass/Ramana/Ramakrishna; WIT Anandamayi/heritage; ZILVER entity-ID/proximity; TURQUOISE entity overlap. Iedere COMPLETE feed direct centraal registreren; niet wachten op alle kleuren.

### BLAUW — COMPLETE 2026-08-20
58 source records -> 58 entity mappings -> 0 silent drops. Commits: `18d472cce9f145187a1ca6e3071fbf62eaf529fe`, `7e60302cf46cd2380e1fae03978a14706d23ae9f`, `7122f85dad8e3d0710e48df83ee72eae56b5d5d2`, `90d14cb6bcbdd7e88c4c83ee3e7bfa0084ac67d6`, status `58854d1840147b8ae2f1eff42b310e417cb5d836`. Central receipt `23d57b73e62c4f31d842175723aa9f1b6eb116d9`.

### TURQUOISE — COMPLETE 2026-08-20
Merge `f5e156f3e23850cc5f52f71bf26ff3a2346b6900`; same-site `4cd8396f6acf19b70564a34a833bed5ab020624a`; parent-child `fedf7432d8458f4efa47b41bc93007e77229f2c2`; successor `9759e86dadf8f1fc28047549bdcc304420ecd514`; ambiguous `473d90a6cda65a182b58180daf9290c8432d134a`; status `0aef428540474bcee26122f3913c26ced6aad10f`. Central receipt `f5f8a69ef4f2a19063a83e1efa140754ef3e4af8`.

### GEEL — COMPLETE 2026-08-20
Task `INDIAGEEL-FOURPERSON-LOCATION-CLOSURE-001` on `agent/indiageel-ramana-ramakrishna-sweep` COMPLETE.
Commits: source `9cbf630f55858afabf53839dd6d3c9269baee695`; entities `30486eaf3478057246727a56fd5fb8a5b22a1189`; R4/R5 `314094dc49a539fc71fc4117e2d27cd51a54c554`; access `da7184ab727b3100a5c43dbd068e32fb45c696a7`; status `9c0b1a0d7ec5b8990287cb79c53f17db52f93f09`.
Central receipt: `b1f5b26de727ef735fc7edb4186f7ec07e36a2d5`.
Critical: micro-sites split losslessly for Hotel Evelyn, Kainchi/Bhumiadhar, NKB final journey, Ramana caves/Ramanasramam, Ramakrishna Fouzdar Kunj/Ganga Mata/Mani Sen/Cossipore. R4/R5 retained. ZILVER GEEL feed commit `8a9f6e33b62e08a97fd6375e87838df190d5eabc`.

### WIT — CONTENT COMPLETE, SCHEMA PASS DISPATCHED
Outputs: `cf5974bf69053e466e94a93433cd8282adbde7ba`, `1fd1ec3213466e3c440ea5143e0c6d6f91c2d971`, `e1d8f8422501fb9a579e7269dd8e81caf561587e`, `61d96b016786d9208c964661cdaa92f72f1e9621`, `c6933d04b1a93e50015bf5ecdec7b34d0cb7c187`, status `aae890510c44cad584fabc3ffb671a93d1d902ab`. Central receipt `e2b2243ddc92db587aec69c6c9cb2b7cbab1281a`. Canonical R1-R5 schema pushed to WIT as `6ac2647c855fe55f8c418b7e76d7159d379d8753`; WIT must only schema-classify existing researched entities, no rediscovery.

### ROOD — INPUT BLOCKER REMOVED
ROOD TASK explicitly permits read-only cross-branch input from `agent/india8-cluster-casting` for exact delta files + governance; writes remain only on `agent/indiarood-core-kriya-sweep`. TASK update `846bd86ae99dab6577600e9f5fbcd1922b7bc1d4`; STATUS `READY_UNBLOCKED_CROSS_BRANCH_INPUTS_ALLOWED` commit `828950f06b9bfe4b273131b2e1d6f4b713c2915b`. ROOD must continue immediately.

### ZILVER — STAGED, NOT BLOCKED
Works from existing canon + known 31 candidates, reliable coordinates only, UNKNOWN/dependency otherwise. TURQUOISE feed commit `1d1607dba2d48fae604ce5cd469fe98876f9a4bd`; GEEL feed commit `8a9f6e33b62e08a97fd6375e87838df190d5eabc`. Must not wait for ROOD/WIT.

## IMMEDIATE NEXT ACTIONS FOR INDIA9
1. Enforce DOORGANGSPROTOCOL every turn.
2. Register ROOD/WIT/ZILVER result immediately when it arrives.
3. If any agent reports blocker: treat blocker as regie-task, attempt repo/branch/path/cross-branch/staged workaround immediately, and continue another workstream if true blocker remains.
4. Once feeds sufficiently close, build consolidated `ALL_FINDINGS_LOCATION_MASTER` with explicit source->entity links and accounting equation.
5. Then complete cluster lists -> Mark A/B/C -> cluster choice -> route/nights/transport/hotels.

## HARDE GRENZEN
Geen A/B/C namens Mark. Geen silent filtering. Geen oude locks wijzigen. Geen route definitief vóór candidate closure. Geen PDF zonder PDF_GO. Geen merge zonder Mark. Oost geparkeerd. Ademruimte blijft expliciet reisdoel.

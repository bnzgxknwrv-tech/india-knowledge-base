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
Commits: source `9cbf630f55858afabf53839dd6d3c9269baee695`; entities `30486eaf3478057246727a56fd5fb8a5b22a1189`; R4/R5 `314094dc49a539fc71fc4117e2d27cd51a54c554`; access `da7184ab727b3100a5c43dbd068e32fb45c696a7`; status `9c0b1a0d7ec5b8990287cb79c53f17db52f93f09`. Central receipt `b1f5b26de727ef735fc7edb4186f7ec07e36a2d5`. ZILVER feed `8a9f6e33b62e08a97fd6375e87838df190d5eabc`.

### WIT — COMPLETE 2026-08-20
Final schema-classified outputs: ANANDAMAYI_ENTITY_CANDIDATES `379b637706023b6f1891ba53e89b16150c193fee`; HERITAGE_STAY_ENTITY_MATRIX `ef493aad36650de1dcc7caa24645bab185ee3ab5`; STATUS `b5ec1abddfe23669c8ea273970760944d312a90a`. Central final receipt `3ef793a806bbb9b9bf28e0c34a0b3c90f3a8ac62`. ZILVER final WIT feed `43fef27574e0bb620d4c404ce6e94b5b49e3b086`. All researched Anandamayi + cross-person heritage entities now have canonical R1-R5 + access; unresolved room/access/bookability retained; no rediscovery needed.

### ROOD — INPUT BLOCKER REMOVED, ACTIVE
ROOD TASK explicitly permits read-only cross-branch input from `agent/india8-cluster-casting` for exact delta files + governance; writes remain only on `agent/indiarood-core-kriya-sweep`. TASK update `846bd86ae99dab6577600e9f5fbcd1922b7bc1d4`; STATUS `READY_UNBLOCKED_CROSS_BRANCH_INPUTS_ALLOWED` commit `828950f06b9bfe4b273131b2e1d6f4b713c2915b`. ROOD must continue immediately.

### ZILVER — STAGED, ACTIVE, NOT BLOCKED
Works from existing canon + known 31 candidates, reliable coordinates only, UNKNOWN/dependency otherwise. TURQUOISE feed `1d1607dba2d48fae604ce5cd469fe98876f9a4bd`; GEEL feed `8a9f6e33b62e08a97fd6375e87838df190d5eabc`; WIT final feed `43fef27574e0bb620d4c404ce6e94b5b49e3b086`. Must not wait for ROOD if current staged work remains.

## ACTIVE CLOSURE STREAMS NOW
Only ROOD + ZILVER remain active. BLAUW, TURQUOISE, GEEL, WIT are complete and should not be re-run.

## IMMEDIATE NEXT ACTIONS FOR INDIA9
1. Enforce DOORGANGSPROTOCOL every turn.
2. Register ROOD and ZILVER result immediately when they arrive.
3. If blocker: solve repo/branch/path/cross-branch/staged dependency immediately; do not stop the program.
4. In parallel, prepare consolidated `ALL_FINDINGS_LOCATION_MASTER` structure and accounting so final ingest can start as soon as ROOD/ZILVER close.
5. After master closure: complete cluster lists -> Mark A/B/C -> cluster choice -> route/nights/transport/hotels.

## HARDE GRENZEN
Geen A/B/C namens Mark. Geen silent filtering. Geen oude locks wijzigen. Geen route definitief vóór candidate closure. Geen PDF zonder PDF_GO. Geen merge zonder Mark. Oost geparkeerd. Ademruimte blijft expliciet reisdoel.

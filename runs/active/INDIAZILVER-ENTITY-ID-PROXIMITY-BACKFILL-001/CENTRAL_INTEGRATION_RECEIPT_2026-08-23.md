# CENTRAL INTEGRATION RECEIPT — INDIAZILVER-ENTITY-ID-PROXIMITY-BACKFILL-001

```
task_id: INDIA9-SUCCESSOR-ARCHITECTURE-CENTRAL-INTEGRATION-008
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
role: mechanical promotion only -- exact byte copy, zero content alteration.
```

Promotes the ZILVER central-master-ready package from source branch
`agent/indiazilver-cluster-completeness-audit` (head `9300fcbb2ae65c06dac65ce55c89dff82ee23a6a`
at promotion time) into this same task path on the central regiebranch
(`agent/india8-cluster-casting`), per Mark's direct authorization in the live CCI
session on 2026-08-23 ("Luister naar hem, hij is nieuwe regisseur") following task 008's
own explicit request.

## Source blob SHAs (each independently verified: destination file's own git-blob
SHA-1, recomputed in Python as `sha1("blob "+len+"\0"+bytes)`, matches the source blob
SHA exactly — byte-for-byte copy, zero alteration)

```
ABC_REVIEW_AFTER_CLOSURE_QUEUE.md    e10868ae45f994c5547d41321e159679b0987c65   11,335 bytes
CENTRAL_INPUT_MANIFEST.md            b0da438c993f3ea9c2d8adda61f760cf3a82f69a    3,707 bytes
DUPLICATE_PARENT_CANDIDATES.md       1d7e0cff0d99613f63cf3097b2c47b8c76068ba6   10,970 bytes
GEEL_ENTITY_FEED.md                  969bf29779195f915ed2612a126d9ccc66afea22    1,103 bytes
NEW_ID_REQUIRED_QUEUE.csv            8e0079403dfd278e867c6413eb6efa0934801d4c   27,461 bytes
PROTECTED_CANON_BASELINE.csv         a607241caa41637e2167d0f56781bf663f038932   15,729 bytes
PROXIMITY_1KM_3KM_MATRIX.csv         ddc1ad38be92d4c37dab8ba2299e23e26f25aea3   12,455 bytes
ROOD_ENTITY_FEED.md                  24f94464b88430b79ec1e944ab4b2b20f3d2dad3    1,099 bytes
STATUS.md                            2c8a87d5b00306cbd31396927c527b8a7d737fa5    6,631 bytes
TASK.md                              fe85865fcfab9e5b518a892cee1718b9b8948b4d    2,763 bytes
TURQUOISE_ENTITY_FEED.md             1454e23151c01f09e74f417d452d97374ae45d7d    1,206 bytes
WIT_FINAL_ENTITY_FEED.md             4b019c8a17d9b296b0064cd0b6c3ccb9ba4a0a40      762 bytes
```
12/12 files verified byte-exact against source blob SHAs before commit.

## Protected canon integrity check (performed before commit)

```
PROTECTED_CANON_BASELINE.csv total rows          : 92
unique entity_id values                           : 92
duplicate entity_id values                         : 0
record_type breakdown  : PERMANENT=81, ACCOMMODATION=1, LEGACY_PROTECTED=8, FEED_GUARD=2
```

No A/B/C field, lock field, coordinate, or queue-semantics value was altered by this
promotion — this is an exact copy, not a re-derivation.

## Guardrails respected

No new permanent ID created. No A/B/C/hotel/route decision made or implied. No branch
or file deleted. This receipt itself is the only new content beyond the exact copy.

---
Geschreven door: CCI.

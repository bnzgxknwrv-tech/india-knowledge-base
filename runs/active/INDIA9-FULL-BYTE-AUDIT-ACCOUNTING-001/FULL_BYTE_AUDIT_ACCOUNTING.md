# FULL BYTE AUDIT — ACCOUNTING

```
task_id: INDIA9-FULL-BYTE-AUDIT-ACCOUNTING-001
uitgevoerd_door: CCI
uitgevoerd_op: 2026-08-23
frozen_central_commit: 1e9fd2453e6b4cbc1488f6d275351772f3eba928
frozen_central_tree: e5832b6cfdbd485e7a7b20a1850f3b8f381b2ecb  (verified byte-for-byte match via `git rev-parse <commit>^{tree}`)
role: independent completeness/accounting backup for INDIA9. No route choices, no A/B/C,
      no central-canon edits made.
```

## Method note — why git plumbing, not the GitHub REST tree API

`git ls-tree -r -l <commit>` walks the object database directly from the frozen commit's tree
object. This is not subject to the GitHub REST API's pagination/truncation behaviour (which
applies only above roughly 100,000 tree entries or a large response-size cap) — it is
mathematically exhaustive by construction: every entry in a git tree is reachable and counted
exactly once, or the walk fails outright rather than silently truncating.

A direct call to the GitHub REST API `git/trees` endpoint (to also report the literal `truncated`
JSON field the task asked for) returned `403 GitHub access is not enabled for this session` for
raw API calls in this environment — the session's GitHub access is scoped through the MCP GitHub
tools, which do not expose a raw recursive-tree endpoint. Given the frozen tree has 368 entries
(three orders of magnitude below GitHub's own truncation threshold) and the git-plumbing walk is
independently exhaustive, this is not a completeness gap — but it is reported honestly as a tool
limitation rather than a fabricated "truncated: false" API response.

## 1. Top-level tree enumeration — exhaustive

```
total path entries (tracked files):     368
all file modes:                          100644 (regular file) x368 -- no symlinks, no
                                          executables, no submodules (mode 160000)
```

## 2. Unique-blob-SHA accounting

```
total paths:                368
total unique blobs:         366
total path bytes:           4,883,398
total unique-blob bytes:    4,883,398   (identical to path bytes because the one duplicate
                                          group is three zero-byte blobs -- see below)
duplicate-SHA groups:       1
  - blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 (git's canonical empty-blob SHA, 0 bytes)
    referenced by 3 paths:
      india5/tasks/active/.gitkeep
      india5/tasks/done/.gitkeep
      india5/tasks/failed/.gitkeep
zero-byte blobs:            3 (the same three .gitkeep placeholders above)
```

**Formula for independent verification**:
```
total_path_bytes           = SUM(size(path_i))                for all 368 paths
total_unique_blob_bytes     = SUM(size(blob_j))                for all 366 distinct blob SHAs
duplicate_overhead_bytes    = total_path_bytes - total_unique_blob_bytes   = 0 (in this tree,
                               because the only duplicated blob is 0 bytes)
```

## 3. Extension / classification breakdown

| extension | count | classification |
|---|---:|---|
| md | 276 | text |
| jsonl | 42 | text |
| py | 15 | text |
| yaml | 14 | text |
| json | 5 | text |
| (none) | 5 | text (3 are the `.gitkeep` zero-byte files above; 2 are extension-less text files) |
| pdf | 6 | **binary** |
| tmp | 2 | text |
| kml | 3 | text (XML) |
| **TOTAL** | **368** | **362 text / 6 binary** |

**Methodology correction made during this pass**: the first classification attempt used a
null-byte heuristic (`b"\x00" in content`) to separate text from binary, which is normally
reliable but produced a false negative for all 6 PDFs — these are small, image-free,
`reportlab`-style generated PDFs that happen to contain no null byte in their object streams,
so the heuristic alone missed them. Caught by cross-checking the extension-count table against
the classification-count table (6 `pdf` entries vs. an initial 0 `binary` count didn't add up),
confirmed by inspecting the actual blob content (`%PDF-1.4` magic header present), and corrected
by force-classifying every `.pdf` extension as binary regardless of the null-byte result. No
other extension showed this mismatch.

## 4. PDF/binary artifact inventory (complete)

| path | blob SHA | size (bytes) |
|---|---|---:|
| `runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/BODHGAYA_046_049_KEUZE_REISGIDS.pdf` | `17b8b9d314af80e33e83f923612de0bc55b58268` | 13,136 |
| `runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/BODHGAYA_046_058_KEUZE_REISGIDS.pdf` | `c03b26d7510ea3a358f010087a8b8472a3ec6b40` | 36,338 |
| `runs/active/BODHGAYA-DISCOVERY-001/GOUD/USER/V1_BODHGAYA_KEUZE_REISGIDS.pdf` | `0115940fce536485130594ce11d3231f2342bd40` | 47,774 |
| `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/USER/VARANASI_40_KEUZE.pdf` | `14c60d9f8b8abb7271bff25907c168cf506de66e` | 29,677 |
| `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/REGIONAL/USER/VARANASI_40_KEUZE_REISGIDS.pdf` | `d2522ed17ee64be6be2802b012f9bd901403ac2b` | 113,631 |
| `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/GOUD/TESTSWEEP-022-040/USER/VARANASI_TESTSWEEP_022-040_KEUZE.pdf` | `36afc747811f87043a5600524d518e95c53070de` | 14,123 |

No other binary artifact type (image, zip, xlsx, docx) exists anywhere in the frozen central
tree. All 3 `.kml` files are plain XML text, not binary.

**Cross-reference**: the three Bodh Gaya PDFs above (`046_049`, `046_058`, `V1_`) are the exact
same three stale/superseded-but-undeleted PDF versions already flagged as a repo-hygiene issue in
CCI's earlier `runs/active/CCI-REPO-AUDIT-001/REPO_AUDIT_REPORT.md` (commit `7491272`, this
session) — independently reconfirmed still present, unresolved, in the current frozen central
tree.

## 5. Branch inventory + delta accounting

Full per-branch machine-readable data: `BRANCH_DELTA_AUDIT_MANIFEST.jsonl` (43 branches). Method:
for every branch on `origin`, `git diff --name-status <frozen> <branch-tip>` gives exact
added/deleted/modified path counts (deletion here means "present in frozen, absent from branch";
addition means "present in branch, absent from frozen" — i.e. the branch's own unique content).

### 5.1 Direct lineage (not diverged)
- `main` and `agent/india8-cluster-casting` are both **ancestors** of the frozen commit with zero
  unique content of their own — frozen central is a legitimate, direct forward continuation of
  both. Relative to `agent/india8-cluster-casting`'s own tip, frozen central added exactly 3 new
  files (`governance/INDIA9_CANON_RECONCILIATION_2026-08-23.md`,
  `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/INDIA9_CALENDAR_CLOSURE_RECONCILIATION_2026-08-23.md`,
  `runs/active/INDIA8-MARK-CLUSTER-DECISIONS-2026-08-20/WORKING_ROUTE_V2_CANON_PATCH_INDIA9_2026-08-23.md`)
  and modified 2 (`SLEEP_BASE_REGISTER_2026-08-23.md`, and this task's own directory's
  `STATUS.md`) — a clean, traceable, expected delta.
- `agent/india9-full-byte-audit` is a **descendant** of frozen (+1 file: its own audit-ledger
  start commit) — consistent, expected.

### 5.2 MAJOR FINDING — the six original color-worker branches carry substantial content that never made it into frozen central

| branch | unique files not in frozen | includes |
|---|---:|---|
| `agent/indiazilver-cluster-completeness-audit` | 22 | **`PROTECTED_CANON_BASELINE.csv` itself** — the 001-081 permanent-ID/ABC/coordinate canon baseline referenced throughout this entire project's governance — plus `PROXIMITY_1KM_3KM_MATRIX.csv`, `NEW_ID_REQUIRED_QUEUE.csv`, `DUPLICATE_PARENT_CANDIDATES.md`, `CLUSTER_RECALL_AUDIT.md`, `COMPLETENESS_GATE.md` |
| `agent/indiablauw-trip-ops-prep` | 28 | Visa-ready-pack (checklist, form prep, scam guard, timing recommendation), trip-ops-prep (booking windows, calendar risk, winter access risk, entry/admin), and an `INDIABLAUW-ANANDAMAYI-YOGANANDA-PHOTO-LOCATIONS-001` directory — worth checking against CCI's own already-integrated photo-location closure for overlap/duplication |
| `agent/indiawit-master-travel-readiness` | 26 | Heritage-stay override matrix, room-level leads, master travel-readiness heatmap-input, reverse-cluster-reopen |
| `agent/indiaturquoise-allperson-overlap` | 19 | Travel-priority heatmap, high-impact gaps, Mark-decision-queue draft, entity-overlap reconciliation (`ENTITY_MERGE_MAP.jsonl`, `SAME_SITE_OVERLAP_MATRIX.md`, `SUCCESSOR_SITE_MAP.md`) |
| `agent/indiageel-ramana-ramakrishna-sweep` | 23 | Fourperson location closure, four TOP11 blind-sweep freezes (Ramakrishna, Ramana Maharshi, Neem Karoli Baba, Ram Dass, Vivekananda/Hariharananda) |
| `agent/indiarood-core-kriya-sweep` | 9 | Core-Kriya location closure + the three Babaji/Lahiri Mahasaya/Sri Yukteswar blind-sweep freezes (the exact source files CCI's own earlier ROOD-label-propagation task read directly from this branch, confirming they never flowed into central) |

None of this is silently lost — it is all still reachable on its own branch — but **frozen
central's own completeness claim cannot include it**, and this is the same structural risk
flagged in CCI's earlier repo-wide audit (`CCI-REPO-AUDIT-001`): 8+ branches with no open PR,
holding the majority of the project's detailed research trail and (in ZILVER's case) the single
most canonical file in the whole project.

### 5.3 Four newer branches referenced nowhere, and empty of unique content

`agent/indiagoud-nonperson-anchor-audit` (276 files), `agent/indiaorange-travel-heatmap-prep`
(263), `agent/indiapaars-decision-rubric-prep` (263), `agent/indiaroze-route-builder-prep` (263)
each have zero files that differ from frozen central, and are not mentioned by name anywhere in
the frozen tree's own governance/handoff/README text. They are very likely freshly-forked,
not-yet-worked branches (their whole-tree file counts closely track frozen central's own size)
rather than branches with lost content — but they are also invisible to anyone reading only
`README.md`/the handoff docs, exactly like the other unreferenced branches found in the earlier
repo audit.

### 5.4 Legacy/pre-INDIA8 branches — structurally incomparable, out of scope for decision content

`controller/kumaon-complete-001-ready-for-zilver-20260719` and 14 further branches
(`feature/*`, `fix/*`, `implementation/*`, `improvement/*`, `proposal/*`, `run/*`, `transition/*`,
`india/kumaon-v2-sweep-b-001`, `varanasi-goud-completion`, `worker/varanasi-complete-001-brons-20260720`)
each differ from frozen central by 100-600+ paths in both directions — they come from an entirely
earlier architecture generation that `governance/ACTIVE_STATE.md` (read in CCI's earlier repo
audit) already documents as "nooit gemerged... die nummering wordt NIET hergebruikt." A full
per-path diff against these would be near-total-tree noise, not a meaningful decision/lock
comparison; not expanded further here. Full path counts are in `BRANCH_DELTA_AUDIT_MANIFEST.jsonl`
for anyone who wants to verify this characterization directly.

## 6. Byte-weighted read-percentage formula (for INDIA9's own parallel full-content read)

```
byte_weighted_read_pct = ( SUM(size_bytes(path) for path in paths_actually_read) 
                            / total_path_bytes ) * 100

total_path_bytes = 4,883,398   (frozen central, this commit, this tree)
```

If INDIA9 wants read-percentage weighted by **unique content** rather than by path (i.e. reading
the same blob twice through two different paths shouldn't count double), use:
```
byte_weighted_unique_pct = ( SUM(size_bytes(blob) for blob in DISTINCT(blobs actually read))
                              / total_unique_blob_bytes ) * 100

total_unique_blob_bytes = 4,883,398   (identical to total_path_bytes in this specific tree,
                                        since the only duplicate is a 0-byte blob)
```

Per-path and per-blob sizes for plugging into either formula are in
`FULL_BYTE_AUDIT_MANIFEST.jsonl` (one JSON object per path: `path`, `blob_sha`, `size_bytes`,
`extension`, `classification`).

## Summary for CCI_RESULT

```
total_paths: 368
unique_blobs: 366
total_path_bytes: 4883398
total_unique_blob_bytes: 4883398
duplicate_sha_groups: 1 (0-byte, 3 .gitkeep paths)
zero_byte_blobs: 3
binary_artifacts: 6 (all PDF, all under runs/active/{BODHGAYA-DISCOVERY-001,VARANASI-GEO-DELIVERY-REPAIR-001})
text_files: 362
branches_inventoried: 43 (all of origin)
branches_referenced_in_governance_or_handoff: 19
branches_with_unique_unintegrated_content: 6 color-worker branches (BLAUW/GEEL/ROOD/TURQUOISE/WIT/ZILVER)
  + 4 newly-created but empty (GOUD/ORANGE/PAARS/ROZE) + 15 pre-INDIA8 legacy branches
single most significant finding: PROTECTED_CANON_BASELINE.csv does not exist anywhere in frozen
  central -- it exists only on agent/indiazilver-cluster-completeness-audit
```

---
Geschreven door: CCI. Accounting/QA lane only. No route choices, no A/B/C, no central canon
edited.

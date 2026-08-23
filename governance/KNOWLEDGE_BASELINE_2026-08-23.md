# KNOWLEDGE BASELINE — 2026-08-23

```
baseline_id: KNOWLEDGE_BASELINE_2026-08-23
baseline_date: 2026-08-23
certified_by: CCI (tasks 001-008), authorized by Mark (live chat confirmation,
              "Luister naar hem, hij is nieuwe regisseur")
frozen_central_commit: 1e9fd2453e6b4cbc1488f6d275351772f3eba928
frozen_branch_tip_manifest_ref: runs/active/INDIA9-ALL-BRANCH-TIP-UNION-AUDIT-004/FROZEN_BRANCH_TIP_MANIFEST.tsv
                                (on agent/cci-india9-full-byte-audit, 54 branches)
supersedes: null (first certified baseline under governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md)
precedence_snapshot_ref: governance/PRECEDENCE_MAP.jsonl (this commit's version)
semantic_binary_clearance: true -- the 6 central PDFs were hash-verified and confirmed
    to carry no unique decision content beyond what's already represented in text form,
    per task 001's classification pass and task 006's Goal B audit-packaging coverage.
```

## Frozen universe accounting (independently built and verified across tasks 001-007)

```
frozen 54 branch tips                                    : confirmed, 0 hard blockers
all-branch-tip union (integrity universe)                  : 1,680 blobs / 26,972,137 bytes
PROJECT/SOURCE (semantic universe, excl. audit packaging)  : 1,233 blobs /  9,877,094 bytes
  central baseline (frozen commit above)                    :   366 blobs /  4,883,398 bytes
    -- fully semantically read by INDIA9 via task 003's 93 review volumes
  source-beyond-central (task 006 classification)            :   867 blobs /  4,993,696 bytes
    category 1 UNIQUE_SEMANTIC_NOT_CENTRALLY_REPRESENTED      :    62 blobs /    344,876 bytes
      -- fully semantically read by INDIA9 via task 007's 115-row verified stream /
         7 review volumes; 12 of these 62 promoted to central canon by task 008,
         remaining 50 archived as provenance (see SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl)
    category 2 SEMANTICALLY_REPRESENTED_IN_CENTRAL             :    40 blobs /    325,542 bytes
      -- material content already carried by an identified central file; successor
         paths recorded in governance/CENTRAL_INTEGRATION_REGISTRY.jsonl
    category 3 HISTORICAL_INTERMEDIATE_SUPERSEDED               :   601 blobs /  3,660,684 bytes
      -- provenance only, successor paths recorded in
         runs/active/INDIA9-SUCCESSOR-BOOT-KNOWLEDGE-ARCHITECTURE-006/BRANCH_ONLY_SEMANTIC_COVERAGE_LEDGER.jsonl
    category 4 MECHANICAL_OR_REDUNDANT_SOURCE_ARTIFACT           :   164 blobs /    662,594 bytes
      -- generated/duplicate packaging, hash-verified only
audit packaging (CCI's own tasks 001-007 output)             :   447 blobs / 17,095,043 bytes
  -- mechanically hash-covered (447/447 verified, task 006 Goal B), derivative
     relationship recorded per-blob, never a mandatory semantic reread (Section Q)
```

## Gate declaration

```
SEMANTIC_KNOWLEDGE_COVERAGE : 100%  (all of category 1 + central baseline personally
                                      semantically read; category 2/3/4 covered via
                                      successor-path confirmation / hash verification
                                      per governance/INDIA_SUCCESSOR_BOOT_PROTOCOL.md
                                      Section D)
INTEGRITY_COVERAGE          : 100%  (1,680/1,680 union blobs hash-verified across
                                      tasks 004-007, 0 mismatches, 0 hard blockers)
AUTHORITY_RECONCILIATION    : COMPLETE for this baseline's freeze moment -- see
                                      governance/PRECEDENCE_MAP.jsonl (8 rows)
FRESHNESS_GATE              : NOT a blanket pass -- see per-item recheck_due flags in
                                      governance/SEMANTIC_IMPORT_REGISTRY_2026-08-23.jsonl.
                                      TIME_SENSITIVE_REFERENCE_RECHECK items
                                      (visa/logistics, 15 blobs) explicitly require
                                      revalidation before operational use.
```

**`KNOWLEDGE_READY: 100%` for this frozen universe** — this is a claim about semantic +
integrity coverage of everything that existed at this freeze moment, **not** a claim
that all time-sensitive facts remain fresh forever. See governance/
INDIA_SUCCESSOR_BOOT_PROTOCOL.md Section O for the freshness discipline that governs
operational use of time-sensitive content going forward.

## What this baseline does NOT cover

- Anything pushed to any branch after this freeze moment (2026-08-23, task 004's
  freeze time). A successor must run the delta-accounting procedure (Boot Protocol
  Section D2) against this baseline to find and classify what's new.
- The freshness of any `TIME_SENSITIVE_REFERENCE_RECHECK`-scoped content beyond its
  archival date.

---
Geschreven door: CCI, task 008.

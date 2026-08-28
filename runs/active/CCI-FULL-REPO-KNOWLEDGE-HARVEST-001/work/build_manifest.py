#!/usr/bin/env python3
"""Build COVERAGE_MANIFEST.csv rows for the frozen central tree.

Reads:
  work/central_tree.txt   -- output of `git ls-tree -r -l <FROZEN>`
  work/read_log.tsv       -- path<TAB>read_status<TAB>relevance<TAB>currentness_class<TAB>superseded_by<TAB>conflict_id<TAB>dest<TAB>notes
Writes:
  work/rows_current_tree.csv
"""
import csv
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FROZEN = "a37423639f7dabb0dfd55c8656d4689bb8a25351"

NON_SEMANTIC_EXT = {".gitkeep", ".gitignore", ".tmp"}
BINARY_EXT = {".pdf"}


def semantic_type(path):
    ext = os.path.splitext(path)[1].lower()
    name = os.path.basename(path)
    if name in (".gitkeep", ".gitignore") or ext in NON_SEMANTIC_EXT:
        return "non_semantic_scaffold"
    if ext == ".pdf":
        return "generated_pdf"
    if ext == ".py":
        return "script"
    if ext == ".yaml":
        return "config_yaml"
    if ext in (".json", ".jsonl"):
        return "structured_data"
    if ext == ".csv":
        return "structured_data"
    if ext == ".kml":
        return "geodata"
    if ext == ".md":
        return "markdown_prose"
    return "other"


def main():
    tree_file = os.path.join(BASE, "central_tree.txt")
    read_log = os.path.join(BASE, "read_log.tsv")
    out = os.path.join(BASE, "rows_current_tree.csv")

    overrides = {}
    if os.path.exists(read_log):
        with open(read_log, encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip("\n")
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                while len(parts) < 8:
                    parts.append("")
                overrides[parts[0]] = parts[1:8]

    by_blob = {}
    rows = []
    with open(tree_file, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            meta, path = line.split("\t", 1)
            mode, otype, sha, size = meta.split()
            st = semantic_type(path)
            ov = overrides.get(path)
            if ov:
                read_status, relevance, currentness, superseded_by, conflict_id, dest, notes = ov
            else:
                if st == "non_semantic_scaffold":
                    read_status = "CLASSIFIED_NON_SEMANTIC"
                    relevance = "NONE"
                    currentness = "HISTORICAL_PROVENANCE_ONLY"
                elif st == "generated_pdf":
                    read_status = "CLASSIFIED_DERIVED_DUPLICATE"
                    relevance = "LOW"
                    currentness = "DUPLICATE"
                else:
                    read_status = "UNREAD"
                    relevance = ""
                    currentness = ""
                superseded_by = conflict_id = dest = notes = ""
            dup_of = ""
            if sha in by_blob:
                dup_of = by_blob[sha]
                if not currentness:
                    currentness = "DUPLICATE"
            else:
                by_blob[sha] = path
            rows.append([
                "current_tree", FROZEN, path, sha, size, st,
                read_status, dup_of, relevance, currentness,
                superseded_by, conflict_id, dest, notes,
            ])

    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        for r in rows:
            w.writerow(r)
    unread = sum(1 for r in rows if r[6] == "UNREAD")
    print(f"rows={len(rows)} unique_blobs={len(by_blob)} unread={unread}")


if __name__ == "__main__":
    main()

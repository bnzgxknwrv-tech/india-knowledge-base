#!/usr/bin/env python3
"""Validate decision IDs, files and DECISION-* references.

No third-party dependencies. Exit 0 on success, non-zero on any collision,
missing indexed file, unindexed decision file, ID/path mismatch or dangling
DECISION reference.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECISIONS_DIR = ROOT / "decisions"
INDEX_PATH = DECISIONS_DIR / "INDEX.yaml"
ID_RE = re.compile(r"DECISION-\d{4}")
FRONTMATTER_ID_RE = re.compile(r"^id:\s*(DECISION-\d{4})\s*$", re.MULTILINE)
INDEX_ENTRY_RE = re.compile(
    r"^\s*- id:\s*(DECISION-\d{4})\s*$\n"
    r"^\s+path:\s*([^\n]+)\s*$",
    re.MULTILINE,
)


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


def main() -> int:
    errors: list[str] = []
    if not INDEX_PATH.is_file():
        return fail([f"missing {INDEX_PATH.relative_to(ROOT)}"])

    index_text = INDEX_PATH.read_text(encoding="utf-8")
    entries = INDEX_ENTRY_RE.findall(index_text)
    if not entries:
        return fail(["decisions/INDEX.yaml contains no parseable entries"])

    ids = [decision_id for decision_id, _ in entries]
    paths = [path.strip().strip('"\'') for _, path in entries]

    for decision_id in sorted(set(ids)):
        if ids.count(decision_id) > 1:
            errors.append(f"duplicate index ID {decision_id}")
    for path in sorted(set(paths)):
        if paths.count(path) > 1:
            errors.append(f"duplicate index path {path}")

    indexed_by_id = dict(zip(ids, paths, strict=False))
    indexed_paths = set(paths)

    disk_files = sorted(DECISIONS_DIR.glob("DECISION-*.md"))
    disk_paths = {str(path.relative_to(ROOT)) for path in disk_files}

    for decision_id, relative_path in indexed_by_id.items():
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"{decision_id} points to missing file {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_ID_RE.search(text)
        if not match:
            errors.append(f"{relative_path} has no frontmatter id")
        elif match.group(1) != decision_id:
            errors.append(
                f"{relative_path} frontmatter ID {match.group(1)} != index ID {decision_id}"
            )

    for relative_path in sorted(disk_paths - indexed_paths):
        errors.append(f"unindexed decision file {relative_path}")
    for relative_path in sorted(indexed_paths - disk_paths):
        errors.append(f"indexed decision file missing from disk {relative_path}")

    known_ids = set(ids)
    for path in disk_files:
        text = path.read_text(encoding="utf-8")
        own_match = FRONTMATTER_ID_RE.search(text)
        own_id = own_match.group(1) if own_match else None
        for referenced_id in sorted(set(ID_RE.findall(text))):
            if referenced_id == own_id:
                continue
            if referenced_id not in known_ids:
                errors.append(
                    f"{path.relative_to(ROOT)} references unknown {referenced_id}"
                )

    if errors:
        return fail(errors)

    print(f"OK: {len(ids)} unique decisions; all files and references valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

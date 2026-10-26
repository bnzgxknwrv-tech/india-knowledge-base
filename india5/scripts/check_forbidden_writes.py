#!/usr/bin/env python3
"""Controleert of een taak buiten haar forbidden_writes is gebleven (INDIA5-ARCH-HARDEN-002).

Bepaalt de claim-commit via resolve_task_commits.py (niet-circulair, read-only), en vergelijkt
alle bestanden die sindsdien zijn gewijzigd (`git diff --name-only <claim_commit> -- .`) tegen
de `forbidden_writes`-padpatronen uit TASK.yaml. Wijzigingen BINNEN de eigen taakdirectory
(`india5/tasks/*/<TASK_ID>/`) worden genegeerd -- dat is de verwachte output van de taak zelf.

Gebruik:
    python3 india5/scripts/check_forbidden_writes.py <TASK_ID>

Exit code 0 = geen verboden pad aangeraakt, 1 = een of meer overtredingen.
"""
import fnmatch
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TASKS_ROOT = REPO_ROOT / "india5" / "tasks"
RESOLVE_SCRIPT = REPO_ROOT / "india5" / "scripts" / "resolve_task_commits.py"


def find_task_yaml(task_id: str) -> Path | None:
    for stage in ("active", "done", "failed", "queue"):
        p = TASKS_ROOT / stage / task_id / "TASK.yaml"
        if p.exists():
            return p
    return None


def find_status_yaml(task_id: str) -> Path | None:
    for stage in ("active", "done", "failed", "queue"):
        p = TASKS_ROOT / stage / task_id / "STATUS.yaml"
        if p.exists():
            return p
    return None


def pre_existing_dirty_paths(task_id: str) -> list:
    """Paden die STATUS.yaml.pre_existing_dirty_paths (door claim_task.py vastgelegd)
    aanmerkt als AL vuil vóór deze taak -- die tellen niet mee als overtreding van déze taak."""
    status_path = find_status_yaml(task_id)
    if not status_path:
        return []
    status = yaml.safe_load(status_path.read_text(encoding="utf-8")) or {}
    return status.get("pre_existing_dirty_paths") or []


def matches_any(path: str, patterns: list) -> bool:
    for pattern in patterns:
        pat = pattern.rstrip("/")
        if path == pat or path.startswith(pat + "/") or fnmatch.fnmatch(path, pattern):
            return True
    return False


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python3 check_forbidden_writes.py <TASK_ID>")
        sys.exit(2)
    task_id = sys.argv[1]

    task_yaml_path = find_task_yaml(task_id)
    if not task_yaml_path:
        print(f"CONTROLE MISLUKT -- TASK.yaml voor {task_id} niet gevonden")
        sys.exit(1)
    task = yaml.safe_load(task_yaml_path.read_text(encoding="utf-8"))
    forbidden = task.get("forbidden_writes") or []

    result = subprocess.run(
        [sys.executable, str(RESOLVE_SCRIPT), task_id],
        capture_output=True, text=True,
    )
    claim_commit = None
    for line in result.stdout.splitlines():
        if line.startswith("claim_commit:"):
            claim_commit = line.split(":", 1)[1].strip()
    if not claim_commit or claim_commit == "NOT_FOUND":
        print(f"CONTROLE MISLUKT -- kon claim-commit voor {task_id} niet bepalen, "
              f"kan wijzigingen niet afbakenen")
        sys.exit(1)

    # LET OP: `git diff <commit>` toont uitsluitend gewijzigde GETRACKTE bestanden -- nieuwe
    # (untracked) bestanden verschijnen daar NOOIT in, ongeacht --. Zonder de untracked-lijst
    # apart toe te voegen mist deze check elk nieuw bestand op een verboden pad (echte bug,
    # gevonden en gefixt tijdens INDIA5-ARCH-HARDEN-002).
    diff = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "diff", "--name-only", claim_commit, "--", "."],
        capture_output=True, text=True,
    )
    untracked = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "--others", "--exclude-standard", "--", "."],
        capture_output=True, text=True,
    )
    changed = sorted(set(
        [l for l in diff.stdout.strip().splitlines() if l]
        + [l for l in untracked.stdout.strip().splitlines() if l]
    ))

    own_task_prefixes = [
        f"india5/tasks/queue/{task_id}/",
        f"india5/tasks/active/{task_id}/",
        f"india5/tasks/done/{task_id}/",
        f"india5/tasks/failed/{task_id}/",
    ]
    pre_dirty = pre_existing_dirty_paths(task_id)

    def was_pre_existing_dirty(path: str) -> bool:
        # git status --porcelain toont een ongetrackte MAP als één regel (bv. "india4/registries/"),
        # niet elk bestand erin apart -- dus prefixmatch nodig, niet alleen exacte gelijkheid.
        for p in pre_dirty:
            if path == p or (p.endswith("/") and path.startswith(p)):
                return True
        return False

    violations = []
    for path in changed:
        if any(path.startswith(p) for p in own_task_prefixes):
            continue
        if was_pre_existing_dirty(path):
            continue  # al vuil vóór deze taak (bv. een CCI_HOLD elders), niet toe te rekenen
        if matches_any(path, forbidden):
            violations.append(path)

    if violations:
        print(f"CONTROLE MISLUKT -- {len(violations)} verboden pad(en) aangeraakt sinds claim-commit {claim_commit}:\n")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)

    print(f"CONTROLE OK -- geen enkel forbidden_writes-pad aangeraakt sinds claim-commit {claim_commit} "
          f"({len(changed)} bestand(en) gewijzigd, allemaal binnen de eigen taakdirectory of toegestaan).")
    sys.exit(0)


if __name__ == "__main__":
    main()

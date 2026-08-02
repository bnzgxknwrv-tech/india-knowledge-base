#!/usr/bin/env python3
"""Claimt een INDIA5-taak atomisch (india5/TASK_PROTOCOL.md).

Atomiciteit: de daadwerkelijke atomische grens is de git-commit direct na de verplaatsing
queue/ -> active/. Zolang die verplaatsing niet gecommit is, is de claim niet definitief. Dit
script verplaatst en past STATUS.yaml aan, maar commit zelf NIET -- de aanroeper (CCI) commit
expliciet, zodat een mislukte/geweigerde commit nooit een stille dubbele claim oplevert.

Weigert de claim wanneer:
1. validate_task.py fouten geeft (schema, hash, stale expected_head);
2. er al een andere taak in india5/tasks/active/ staat (max. 1 actieve taak tegelijk);
3. de taak niet in queue/ staat.

Gebruik:
    python3 india5/scripts/claim_task.py <TASK_ID>
"""
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TASKS_ROOT = REPO_ROOT / "india5" / "tasks"
VALIDATE_SCRIPT = REPO_ROOT / "india5" / "scripts" / "validate_task.py"


def active_tasks():
    active_dir = TASKS_ROOT / "active"
    return [d for d in active_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python3 claim_task.py <TASK_ID>")
        sys.exit(2)
    task_id = sys.argv[1]

    queue_dir = TASKS_ROOT / "queue" / task_id
    if not queue_dir.exists():
        print(f"CLAIM MISLUKT -- {task_id} niet gevonden in india5/tasks/queue/")
        sys.exit(1)

    others = active_tasks()
    if others:
        print(f"CLAIM MISLUKT -- er is al een actieve taak: {[d.name for d in others]}. "
              f"Slechts één taak tegelijk actief (regel: 'tweede taak terwijl eerste actief is').")
        sys.exit(1)

    result = subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), task_id, "--stage", "queue"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("CLAIM MISLUKT -- validate_task.py gaf fouten, taak wordt niet geclaimd:\n")
        print(result.stdout)
        sys.exit(1)

    active_dir = TASKS_ROOT / "active" / task_id
    queue_dir.rename(active_dir)

    now = datetime.now(timezone.utc).isoformat()
    status_path = active_dir / "STATUS.yaml"
    status = {}
    if status_path.exists():
        status = yaml.safe_load(status_path.read_text(encoding="utf-8")) or {}

    status.setdefault("task_id", task_id)
    status["state"] = "ACTIVE"
    status["claimed_at"] = now
    status["claimed_by"] = "CCI"
    status["started_at"] = now
    status.setdefault("completed_at", None)
    status.setdefault("git_commit_at_claim", None)
    status.setdefault("git_commit_at_complete", None)
    status.setdefault("completion_marker_found", None)
    status.setdefault("failure_reason", None)
    history = status.setdefault("history", [])
    history.append({"at": now, "event": "CLAIMED", "detail": "queue -> active, door CCI"})

    status_path.write_text(yaml.safe_dump(status, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print(f"CLAIM OK -- {task_id} verplaatst naar india5/tasks/active/{task_id}/. "
          f"NIET vergeten: commit deze verplaatsing direct (dat is de atomische grens).")
    sys.exit(0)


if __name__ == "__main__":
    main()

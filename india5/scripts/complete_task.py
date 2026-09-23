#!/usr/bin/env python3
"""Rondt een INDIA5-taak af: active/ -> done/ of failed/ (india5/TASK_PROTOCOL.md).

Weigert af te ronden als COMPLETED wanneer:
1. RESULT.md ontbreekt (voorkomt 'commit zonder RESULT');
2. RESULT.md niet exact de completion_marker uit TASK.yaml bevat (voorkomt dat een
   afgekapte/onvolledige RESULT.md stil als voltooid geldt);
3. niet elk pad in expected_outputs (TASK.yaml) bestaat.

git_commit_at_complete kan NIET zelfreferentieel in STATUS.yaml worden geschreven (de commit
die dit bestand bevat, bestaat nog niet op schrijfmoment) -- blijft null. De daadwerkelijke
commit-SHA hoort in het `commit`-veld van de CCI_RESULT PR-comment, ná de push.

Gebruik:
    python3 india5/scripts/complete_task.py <TASK_ID> [--fail "reden"]
"""
import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TASKS_ROOT = REPO_ROOT / "india5" / "tasks"
CHECK_FORBIDDEN_SCRIPT = REPO_ROOT / "india5" / "scripts" / "check_forbidden_writes.py"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id")
    parser.add_argument("--fail", metavar="REDEN", default=None,
                         help="Rond de taak af als FAILED met deze reden, in plaats van COMPLETED.")
    args = parser.parse_args()

    active_dir = TASKS_ROOT / "active" / args.task_id
    if not active_dir.exists():
        print(f"AFRONDEN MISLUKT -- {args.task_id} niet gevonden in india5/tasks/active/")
        sys.exit(1)

    now = datetime.now(timezone.utc).isoformat()
    status_path = active_dir / "STATUS.yaml"
    status = load_yaml(status_path) if status_path.exists() else {"task_id": args.task_id, "history": []}
    history = status.setdefault("history", [])

    if args.fail:
        status["state"] = "FAILED"
        status["completed_at"] = now
        status["failure_reason"] = args.fail
        history.append({"at": now, "event": "FAILED", "detail": args.fail})
        status_path.write_text(yaml.safe_dump(status, sort_keys=False, allow_unicode=True), encoding="utf-8")

        target_dir = TASKS_ROOT / "failed" / args.task_id
        active_dir.rename(target_dir)
        print(f"AFGEROND ALS FAILED -- {args.task_id} verplaatst naar india5/tasks/failed/. "
              f"Reden: {args.fail}")
        sys.exit(0)

    task_yaml_path = active_dir / "TASK.yaml"
    task = load_yaml(task_yaml_path)
    completion_marker = task.get("completion_marker")
    expected_outputs = task.get("expected_outputs") or []

    # expected_outputs beschrijft de UITEINDELIJKE (done/) locatie, maar op het moment van
    # controleren staat de taakdirectory nog in active/ (de verplaatsing gebeurt pas na een
    # geslaagde controle). Voor paden die binnen deze taak-directory vallen, controleren we
    # daarom op de huidige (active/) locatie; overige paden (buiten de taak-directory, bv.
    # echte regio-outputs elders in de repo) worden gewoon als absoluut repo-pad gecontroleerd.
    done_prefix = f"india5/tasks/done/{args.task_id}/"
    active_prefix = f"india5/tasks/active/{args.task_id}/"

    def resolve_expected(out_path: str) -> Path:
        if out_path.startswith(done_prefix):
            return REPO_ROOT / active_prefix / out_path[len(done_prefix):]
        return REPO_ROOT / out_path

    errors = []
    result_path = active_dir / "RESULT.md"
    if not result_path.exists():
        errors.append("RESULT.md ontbreekt -- taak mag niet als COMPLETED gelden zonder RESULT")
    else:
        result_text = result_path.read_text(encoding="utf-8")
        if completion_marker and completion_marker not in result_text:
            errors.append(
                f"RESULT.md bevat niet de exacte completion_marker {completion_marker!r} -- "
                f"mogelijk afgekapt, taak mag niet als COMPLETED gelden"
            )

    for out_path in expected_outputs:
        full = resolve_expected(out_path)
        if not full.exists():
            errors.append(f"expected_output ontbreekt: {out_path} (gecontroleerd op {full})")

    forbidden_check = subprocess.run(
        [sys.executable, str(CHECK_FORBIDDEN_SCRIPT), args.task_id],
        capture_output=True, text=True,
    )
    if forbidden_check.returncode != 0:
        errors.append(
            "forbidden_writes-controle mislukt (check_forbidden_writes.py):\n"
            + forbidden_check.stdout.strip()
        )

    if errors:
        print(f"AFRONDEN MISLUKT -- {len(errors)} probleem/problemen, taak blijft ACTIVE:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    status["state"] = "COMPLETED"
    status["completed_at"] = now
    status["completion_marker_found"] = True
    status["git_commit_at_complete"] = None  # zelfreferentieel onmogelijk, zie module-docstring
    history.append({"at": now, "event": "COMPLETED", "detail": "active -> done, door CCI"})
    status_path.write_text(yaml.safe_dump(status, sort_keys=False, allow_unicode=True), encoding="utf-8")

    target_dir = TASKS_ROOT / "done" / args.task_id
    active_dir.rename(target_dir)

    print(f"AFGEROND -- {args.task_id} verplaatst naar india5/tasks/done/{args.task_id}/. "
          f"NIET vergeten: commit + push, en meld de daadwerkelijke commit-SHA in de "
          f"CCI_RESULT PR-comment (git_commit_at_complete kan hier niet zelfreferentieel "
          f"worden ingevuld).")
    sys.exit(0)


if __name__ == "__main__":
    main()

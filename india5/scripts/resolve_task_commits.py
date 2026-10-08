#!/usr/bin/env python3
"""Lost de claim- en completion-commit van een taak op ZONDER zelfreferentie (INDIA5-ARCH-HARDEN-002).

Waarom `git_commit_at_claim`/`git_commit_at_complete` in STATUS.yaml altijd `null` blijven:
de commit die STATUS.yaml op een bepaalde locatie (active/ resp. done/) toevoegt, bestaat nog
niet op het moment dat het bestand geschreven wordt -- een bestand kan de hash van zijn eigen
committende commit niet bevatten (die hash hangt af van de volledige boominhoud, inclusief dat
bestand zelf). Dat is fundamenteel circulair, geen bug om te "fixen" door harder te proberen.

De niet-circulaire oplossing: bepaal deze commits ACHTERAF met een read-only git-query, ná het
moment dat de commit al bestaat. Dit script is de geautoriseerde manier om die waarde op te
halen (voor de CCI_RESULT-envelop, of om STATUS.yaml handmatig in een LATERE, aparte commit bij
te werken -- nooit in dezelfde commit als de gebeurtenis zelf, dat zou opnieuw circulair zijn).

Gebruik:
    python3 india5/scripts/resolve_task_commits.py <TASK_ID>

Print (indien gevonden): claim_commit, complete_commit, fail_commit.
"""
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def most_recent_commit_adding_path(path: str) -> str | None:
    """Meest recente commit die het opgegeven pad heeft toegevoegd (git-diff-filter=A),
    doorzoekt de volledige geschiedenis van alle refs. Read-only, geen zelfreferentie."""
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "log", "--all", "--diff-filter=A",
         "--format=%H", "--", path],
        capture_output=True, text=True,
    )
    lines = [l for l in result.stdout.strip().splitlines() if l]
    return lines[0] if lines else None  # newest-first default -> eerste regel is de meest recente


def resolve(task_id: str) -> dict:
    out = {}
    claim_path = f"india5/tasks/active/{task_id}/STATUS.yaml"
    done_path = f"india5/tasks/done/{task_id}/STATUS.yaml"
    failed_path = f"india5/tasks/failed/{task_id}/STATUS.yaml"

    out["claim_commit"] = most_recent_commit_adding_path(claim_path)
    out["complete_commit"] = most_recent_commit_adding_path(done_path)
    out["fail_commit"] = most_recent_commit_adding_path(failed_path)
    return out


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python3 resolve_task_commits.py <TASK_ID>")
        sys.exit(2)
    task_id = sys.argv[1]
    result = resolve(task_id)
    for key, value in result.items():
        print(f"{key}: {value if value else 'NOT_FOUND'}")


if __name__ == "__main__":
    main()

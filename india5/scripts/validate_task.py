#!/usr/bin/env python3
"""Valideert een INDIA5-taak vóór claim/uitvoering (india5/TASK_PROTOCOL.md).

CCI mag een taak NOOIT uitvoeren zonder dat dit script exit-code 0 geeft. Dit script
controleert schema, hash-integriteit van task_file, en of expected_head nog klopt met de
werkelijke HEAD van target_branch. Het detecteert ook (in --post-hoc modus) een inconsistente
afgeronde taak: STATUS.yaml zegt COMPLETED maar RESULT.md ontbreekt.

Gebruik:
    python3 india5/scripts/validate_task.py <TASK_ID> [--stage queue|active|done|failed]
    python3 india5/scripts/validate_task.py <TASK_ID> --post-hoc

Exit code 0 = geldig, 1 = een of meer fouten (details op stdout). Bij fouten: taak NIET
claimen of uitvoeren.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TASKS_ROOT = REPO_ROOT / "india5" / "tasks"
TASK_SCHEMA = REPO_ROOT / "india5" / "schemas" / "task.schema.json"
STATUS_SCHEMA = REPO_ROOT / "india5" / "schemas" / "status.schema.json"

REQUIRED_TASK_FIELDS = [
    "task_id", "protocol_version", "issued_by", "issued_at", "target_branch",
    "expected_head", "task_file", "task_file_sha256", "scope", "required_inputs",
    "allowed_reads", "allowed_writes", "forbidden_writes", "expected_outputs",
    "status", "completion_marker",
]
VALID_SCOPES = {"ARCHITECTURE", "PRE_BRONS", "BRONS", "ZILVER", "GOUD", "TRAVEL",
                 "REGION_FULL_FLOW", "OTHER"}


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_head(branch: str) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", branch],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def is_ancestor(candidate_sha: str, descendant_sha: str) -> bool | None:
    """True als candidate_sha een voorouder is van (of gelijk aan) descendant_sha.
    None als een van beide SHA's lokaal niet resolvebaar is (bv. nog niet gefetcht)."""
    if candidate_sha == descendant_sha:
        return True
    try:
        subprocess.run(
            ["git", "-C", str(REPO_ROOT), "cat-file", "-e", candidate_sha],
            capture_output=True, check=True,
        )
    except subprocess.CalledProcessError:
        return None
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "merge-base", "--is-ancestor", candidate_sha, descendant_sha],
        capture_output=True,
    )
    return result.returncode == 0


def find_task_dir(task_id: str, stage: str | None):
    stages = [stage] if stage else ["queue", "active", "done", "failed"]
    for s in stages:
        d = TASKS_ROOT / s / task_id
        if d.exists():
            return d, s
    return None, None


def validate_task_yaml(task_dir: Path, errors: list, warnings: list, skip_head_check: bool = False):
    task_yaml_path = task_dir / "TASK.yaml"
    if not task_yaml_path.exists():
        errors.append(f"TASK.yaml ontbreekt in {task_dir}")
        return None

    task = yaml.safe_load(task_yaml_path.read_text(encoding="utf-8"))
    if not isinstance(task, dict):
        errors.append("TASK.yaml is geen geldig object")
        return None

    missing = [f for f in REQUIRED_TASK_FIELDS if f not in task]
    if missing:
        errors.append(f"TASK.yaml mist verplichte velden: {missing}")

    if task.get("scope") not in VALID_SCOPES:
        errors.append(f"ongeldige scope: {task.get('scope')!r}, verwacht een van {VALID_SCOPES}")

    if task.get("status") != "QUEUED":
        errors.append(
            f"TASK.yaml.status moet altijd QUEUED zijn (immutable na uitgifte); "
            f"actuele voortgang hoort in STATUS.yaml, niet hier. Gevonden: {task.get('status')!r}"
        )

    allowed = set(task.get("allowed_writes") or [])
    forbidden = set(task.get("forbidden_writes") or [])
    overlap = allowed & forbidden
    if overlap:
        errors.append(f"allowed_writes en forbidden_writes overlappen: {overlap}")

    task_file_rel = task.get("task_file")
    if task_file_rel:
        task_file_path = task_dir / task_file_rel
        if not task_file_path.exists():
            errors.append(f"task_file niet gevonden: {task_file_rel}")
        else:
            actual_hash = sha256_of(task_file_path)
            expected_hash = task.get("task_file_sha256")
            if actual_hash != expected_hash:
                errors.append(
                    f"task_file_sha256 KOMT NIET OVEREEN -- task_file mogelijk afgekapt of "
                    f"gewijzigd na uitgifte. verwacht={expected_hash} werkelijk={actual_hash}"
                )

    if not skip_head_check:
        target_branch = task.get("target_branch")
        expected_head = task.get("expected_head")
        if target_branch and expected_head:
            actual_head = current_head(target_branch)
            if not actual_head:
                warnings.append(f"kon HEAD van {target_branch!r} niet bepalen (lokaal niet aanwezig?)")
            else:
                # expected_head betekent: de basiscommit waarop deze taak is gebouwd, NIET de
                # exacte HEAD op claimmoment. Exacte gelijkheid zou circulair zijn -- het
                # aanmaken/committen van TASK.md/TASK.yaml zelf (en de claim-commit erna)
                # verzet HEAD altijd voorbij expected_head, zelfs bij een geldige, verse taak.
                # Daarom: expected_head moet een voorouder zijn van (of gelijk aan) de huidige
                # HEAD. Alleen een ECHTE divergentie (expected_head is GEEN voorouder meer, bv.
                # door een non-fast-forward/force-push elders) telt als STALE_EXPECTED_HEAD.
                ancestor = is_ancestor(expected_head, actual_head)
                if ancestor is None:
                    errors.append(
                        f"expected_head {expected_head!r} is lokaal niet resolvebaar -- "
                        f"mogelijk nog niet gefetcht. Taak NIET uitvoeren zonder eerst te "
                        f"fetchen en opnieuw te valideren."
                    )
                elif ancestor is False:
                    errors.append(
                        f"STALE_EXPECTED_HEAD -- target_branch {target_branch!r} staat nu op "
                        f"{actual_head}, en {expected_head} is GEEN voorouder meer daarvan "
                        f"(divergente geschiedenis, bv. door een force-push elders). Taak NIET "
                        f"uitvoeren zonder herbevestiging van de opdrachtgever."
                    )
                # ancestor is True: expected_head is een voorouder van (of gelijk aan) HEAD --
                # dat is de normale, verwachte situatie (taak-eigen commits liggen er tussenin).

    check_hold(task_dir, errors)

    return task


def check_hold(task_dir: Path, errors: list):
    """Instructieprecedentie punt 2: een expliciete HOLD in STATUS.yaml blokkeert uitvoering
    van de TASK.md-inhoud, ook als de taak verder geldig/geclaimd is. Staat boven Mark-
    besluitenregister, PR-comments en chattekst -- maar de taak zelf mag wel gelezen/
    gerapporteerd worden, alleen niet inhoudelijk uitgevoerd."""
    status_path = task_dir / "STATUS.yaml"
    if not status_path.exists():
        return
    status = yaml.safe_load(status_path.read_text(encoding="utf-8")) or {}
    hold = status.get("hold") or {}
    if hold.get("active"):
        errors.append(
            f"HOLD ACTIEF -- deze taak mag NIET inhoudelijk worden uitgevoerd. "
            f"reden: {hold.get('reason')!r}, ingesteld door {hold.get('set_by')!r} op "
            f"{hold.get('set_at')!r}. Wacht op een expliciete unhold (hold.active: false) "
            f"vóórdat verder wordt gewerkt."
        )


def validate_post_hoc(task_dir: Path, stage: str, errors: list):
    status_path = task_dir / "STATUS.yaml"
    if not status_path.exists():
        errors.append(f"STATUS.yaml ontbreekt in {task_dir}")
        return
    status = yaml.safe_load(status_path.read_text(encoding="utf-8")) or {}
    state = status.get("state")

    if state == "COMPLETED":
        result_path = task_dir / "RESULT.md"
        if not result_path.exists():
            errors.append(
                "INCONSISTENT: STATUS.yaml zegt COMPLETED maar RESULT.md ontbreekt "
                "(commit zonder RESULT)"
            )
        if stage != "done":
            errors.append(f"STATUS.yaml zegt COMPLETED maar taak staat niet in tasks/done/ (staat in {stage}/)")

    if stage == "done":
        result_path = task_dir / "RESULT.md"
        if result_path.exists() and state != "COMPLETED":
            errors.append(
                "INCONSISTENT: RESULT.md bestaat en taak staat in tasks/done/, maar "
                f"STATUS.yaml zegt state={state!r} in plaats van COMPLETED (RESULT zonder "
                "bijbehorende afgeronde status)"
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id")
    parser.add_argument("--stage", choices=["queue", "active", "done", "failed"], default=None)
    parser.add_argument("--post-hoc", action="store_true",
                         help="Controleer een reeds afgeronde/mislukte taak op interne consistentie "
                              "in plaats van pre-claim-validatie.")
    args = parser.parse_args()

    task_dir, stage = find_task_dir(args.task_id, args.stage)
    if task_dir is None:
        print(f"VALIDATIE MISLUKT -- taak {args.task_id!r} niet gevonden in queue/active/done/failed")
        sys.exit(1)

    errors: list = []
    warnings: list = []

    task = validate_task_yaml(task_dir, errors, warnings, skip_head_check=args.post_hoc)

    if args.post_hoc:
        validate_post_hoc(task_dir, stage, errors)

    for w in warnings:
        print(f"  (waarschuwing) {w}")

    if errors:
        print(f"VALIDATIE MISLUKT -- {len(errors)} probleem/problemen voor {args.task_id} (stage={stage}):\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"VALIDATIE OK -- {args.task_id} (stage={stage}) is geldig, geen fouten.")
    sys.exit(0)


if __name__ == "__main__":
    main()

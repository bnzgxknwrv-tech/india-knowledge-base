#!/usr/bin/env python3
"""Preflight-validator voor governance/SWEEP_PROTOCOL.md (Deel 4).

Controleert UITSLUITEND machine-checkbare, structurele voorwaarden voor een gegeven
run-directory (bv. runs/active/BODHGAYA-DISCOVERY-001) vóór een fase-overgang. Dit script
beoordeelt GEEN inhoud (bronsterkte, of een saturatieclaim klopt, of een generiek-check correct
is uitgevoerd) -- dat blijft mensen-/CCI-/INDIA-oordeel. Elke check rapporteert een van drie
uitkomsten: OK, FAIL, of NIET_CONTROLEERBAAR (het verwachte bestand/veld ontbreekt in dit
run-format -- geen garantie, geen aanname).

Gebruik:
    python3 governance/scripts/preflight_validator.py --run-dir runs/active/<RUN_ID> \
        --phase discovery
    python3 governance/scripts/preflight_validator.py --run-dir runs/active/<RUN_ID> \
        --phase pdf

phase=discovery -> checks vóór keuzerapportfase (Coverage Matrix, Lead Register, identity-
    /access-blockers, nummering, saturation-evidence, INDIA_ACCEPTED_SATURATION: JA).
phase=pdf        -> checks vóór een PDF-build (PRE_PDF_CONTENT_APPROVED: JA, PDF_GO: JA).

Exit code 0 als alle controleerbare checks OK zijn (NIET_CONTROLEERBAAR blokkeert niet, maar
wordt wel zichtbaar gerapporteerd); exit code 1 bij minstens één FAIL.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def load_jsonl(path: Path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                rows.append({"_PARSE_ERROR_": line})
    return rows


def grep_literal(run_dir: Path, token: str):
    """Zoekt een letterlijke tokenstring in alle .md/.jsonl/.yaml-bestanden onder run_dir."""
    hits = []
    for path in list(run_dir.rglob("*.md")) + list(run_dir.rglob("*.jsonl")) + \
            list(run_dir.rglob("*.yaml")) + list(run_dir.rglob("*.yml")):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if token in text:
            hits.append(path)
    return hits


def check_coverage_matrix(run_dir: Path, results: list):
    path = run_dir / "PRE_BRONS" / "COVERAGE_MATRIX.jsonl"
    if not path.exists():
        results.append(("Coverage Matrix", "NIET_CONTROLEERBAAR",
                         f"{path} niet gevonden -- dit run-format gebruikt (nog) geen Coverage Matrix."))
        return
    rows = load_jsonl(path)
    open_rows = [r for r in rows if r.get("status") in ("NOT_STARTED", "ACTIVE")]
    if open_rows:
        results.append(("Coverage Matrix", "FAIL",
                         f"{len(open_rows)} lens/detector(en) nog NOT_STARTED/ACTIVE: "
                         + ", ".join(r.get("lens_of_detector_id", "?") for r in open_rows)))
    else:
        results.append(("Coverage Matrix", "OK", f"{len(rows)} regel(s), alle SATURATED/EXPLICIET_ONBESCHIKBAAR."))


def check_lead_register(run_dir: Path, results: list):
    path = run_dir / "PRE_BRONS" / "LEAD_REGISTER.jsonl"
    if not path.exists():
        results.append(("Lead Register", "NIET_CONTROLEERBAAR",
                         f"{path} niet gevonden -- dit run-format gebruikt (nog) geen Lead Register."))
        return
    valid_outcomes = {"MARK_WAARDIG", "HARD_EXCLUDED", "DUPLICATE", "SUBLOCATION",
                       "OUT_OF_SCOPE_HIGH_VALUE", "EXPLICIET_ONBESCHIKBAAR"}
    rows = load_jsonl(path)
    bad = [r for r in rows if r.get("outcome") not in valid_outcomes]
    if bad:
        results.append(("Lead Register", "FAIL",
                         f"{len(bad)} lead(s) zonder geldige eindstatus: "
                         + ", ".join(str(r.get("lead", "?")) for r in bad)))
    else:
        results.append(("Lead Register", "OK", f"{len(rows)} lead(s), allemaal een geldige eindstatus."))


def check_blockers(run_dir: Path, results: list):
    identity_hits = grep_literal(run_dir, "UNRESOLVED_BLOCKER")
    if identity_hits:
        results.append(("Identity/duplicate-blocker", "FAIL",
                         "UNRESOLVED_BLOCKER gevonden in: " + ", ".join(str(p) for p in identity_hits)))
    else:
        results.append(("Identity/duplicate-blocker", "OK", "Geen UNRESOLVED_BLOCKER-tekst gevonden."))

    access_hits = grep_literal(run_dir, "ACCESS_BLOCKER")
    if access_hits:
        results.append(("Toegankelijkheidsblocker", "FAIL",
                         "ACCESS_BLOCKER gevonden in: " + ", ".join(str(p) for p in access_hits)))
    else:
        results.append(("Toegankelijkheidsblocker", "OK", "Geen ACCESS_BLOCKER-tekst gevonden."))


def check_numbering(run_dir: Path, results: list):
    global_validator = REPO_ROOT / "india5" / "scripts" / "validate_global_numbering.py"
    if not global_validator.exists():
        results.append(("Nummering (globaal)", "NIET_CONTROLEERBAAR", f"{global_validator} niet gevonden."))
        return
    proc = subprocess.run([sys.executable, str(global_validator)], capture_output=True, text=True)
    if proc.returncode == 0:
        results.append(("Nummering (globaal)", "OK", "validate_global_numbering.py: geen problemen."))
    else:
        results.append(("Nummering (globaal)", "FAIL", proc.stdout.strip().splitlines()[-1] if proc.stdout else proc.stderr.strip()))


def check_active_candidates_not_excluded(run_dir: Path, results: list):
    candidates_files = list(run_dir.glob("PRE_BRONS/DISCOVERY_CANDIDATES.jsonl"))
    if not candidates_files:
        results.append(("Actieve kandidaten vs. excluded/sublocation/duplicate", "NIET_CONTROLEERBAAR",
                         "DISCOVERY_CANDIDATES.jsonl niet gevonden."))
        return
    excluded_like = {"EXCLUDED_HARD_REASON", "SUBLOCATION", "DUPLICATE"}
    rows = load_jsonl(candidates_files[0])
    conflicts = [
        r for r in rows
        if r.get("mark_waardig_status") in excluded_like and r.get("active_in_report") is True
    ]
    if conflicts:
        results.append(("Actieve kandidaten vs. excluded/sublocation/duplicate", "FAIL",
                         f"{len(conflicts)} kandidaat/kandidaten expliciet als active_in_report:true "
                         "gemarkeerd EN tegelijk EXCLUDED_HARD_REASON/SUBLOCATION/DUPLICATE."))
    else:
        results.append(("Actieve kandidaten vs. excluded/sublocation/duplicate", "OK",
                         "Geen kandidaat is tegelijk 'active_in_report' en EXCLUDED_HARD_REASON/"
                         "SUBLOCATION/DUPLICATE. (Vereist wel het optionele veld 'active_in_report' "
                         "per record -- ontbreekt dat veld overal, dan is dit een zwakke check.)"))


def check_saturation_evidence(run_dir: Path, results: list):
    reports = list(run_dir.glob("**/SATURATION_REPORT*.md"))
    if not reports:
        results.append(("Saturation-evidence-bestand", "NIET_CONTROLEERBAAR", "Geen SATURATION_REPORT*.md gevonden."))
        return
    results.append(("Saturation-evidence-bestand", "OK",
                     f"{len(reports)} rapport(en) gevonden: " + ", ".join(p.name for p in reports)))


def check_token(run_dir: Path, token: str, label: str, results: list):
    hits = grep_literal(run_dir, token)
    if hits:
        results.append((label, "OK", f"'{token}' gevonden in: " + ", ".join(str(p) for p in hits)))
    else:
        results.append((label, "FAIL", f"'{token}' NIET gevonden in run-directory {run_dir}."))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-dir", required=True, help="Pad naar de run-directory, bv. runs/active/BODHGAYA-DISCOVERY-001")
    parser.add_argument("--phase", choices=["discovery", "pdf"], default="discovery",
                         help="discovery = checks vóór keuzerapportfase; pdf = checks vóór PDF-build")
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    if not run_dir.is_absolute():
        run_dir = REPO_ROOT / run_dir
    if not run_dir.exists():
        print(f"FOUT: run-directory {run_dir} bestaat niet.")
        sys.exit(2)

    results = []

    if args.phase == "discovery":
        check_coverage_matrix(run_dir, results)
        check_lead_register(run_dir, results)
        check_blockers(run_dir, results)
        check_numbering(run_dir, results)
        check_active_candidates_not_excluded(run_dir, results)
        check_saturation_evidence(run_dir, results)
        check_token(run_dir, "INDIA_ACCEPTED_SATURATION: JA", "INDIA_ACCEPTED_SATURATION", results)
    else:
        check_token(run_dir, "PRE_PDF_CONTENT_APPROVED: JA", "PRE_PDF_CONTENT_APPROVED", results)
        check_token(run_dir, "PDF_GO: JA", "PDF_GO", results)

    print(f"Preflight ({args.phase}) voor {run_dir}\n")
    fail_count = 0
    for label, status, detail in results:
        print(f"[{status:20s}] {label}: {detail}")
        if status == "FAIL":
            fail_count += 1

    print()
    if fail_count:
        print(f"PREFLIGHT MISLUKT -- {fail_count} FAIL. Fase-overgang NIET toegestaan.")
        print("Let op: NIET_CONTROLEERBAAR is geen garantie -- dat betekent alleen dat dit script "
              "het niet kan checken, niet dat het in orde is.")
        sys.exit(1)

    print("Alle machine-checkbare voorwaarden zijn OK. NIET_CONTROLEERBAAR-punten (indien aanwezig) "
          "vereisen nog altijd menselijk/INDIA-oordeel voordat de fase echt open mag.")
    sys.exit(0)


if __name__ == "__main__":
    main()

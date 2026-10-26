#!/usr/bin/env python3
"""Veilige, append-only writer voor BRONS/ZILVER-batchbestanden (JSONL).

Root cause van de vorige tooling-fout: een script opende een bestaand batchbestand
in tekstmodus "a" en schreef er json.dumps(...)-regels bovenop. Als het bestaande
bestand niet op een newline eindigde, smolt de eerste toegevoegde regel samen met
de laatste bestaande regel tot een ongeldige JSON-regel (BRONS-B03.jsonl:1 kreeg
zo VNS-CAND-021 en VNS-CAND-022 samengeperst). Bovendien herserialiseerde de
reparatie nadien per ongeluk ALLE regels (inclusief het ongewijzigde VNS-CAND-021),
wat een cosmetische diff opleverde (spaties na ":"/"," die er eerst niet stonden).

Deze module lost beide problemen structureel op:
1. Bestaande regels worden NOOIT gelezen-en-herschreven. Alleen aanvullen.
2. Vóór het aanvullen wordt uitsluitend gecontroleerd of het bestand al op een
   newline eindigt; zo niet, wordt UITSLUITEND een newline toegevoegd (een
   gerichte, minimale toevoeging), nooit de bestaande byte-inhoud gewijzigd.
3. Elk record wordt in compacte vorm geschreven (separators zonder spaties,
   dezelfde stijl als de bestaande BRONS/ZILVER-records), zodat nieuwe regels
   geen cosmetische afwijking t.o.v. de bestaande conventie introduceren.

Gebruik als module:
    from append_batch_record import append_jsonl_record
    append_jsonl_record(path, record_dict)

Gebruik als CLI (record als JSON via stdin):
    echo '{"candidate_id": "VNS-CAND-099", ...}' | python3 append_batch_record.py BRONS/BRONS-B05.jsonl
"""
import json
import sys
from pathlib import Path

COMPACT_SEPARATORS = (",", ":")


def _existing_candidate_ids(path: Path) -> set:
    ids = set()
    if not path.exists():
        return ids
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            cid = rec.get("candidate_id")
            if cid:
                ids.add(cid)
    return ids


def append_jsonl_record(path, record: dict, allow_duplicate: bool = False) -> None:
    """Append één record aan een JSONL-batchbestand zonder bestaande regels aan te raken.

    - Schrijft nooit het bestand opnieuw; opent uitsluitend in append-byte-modus.
    - Voegt eerst een ontbrekende trailing newline toe als gerichte, losse toevoeging
      (nooit gecombineerd met een herserialisatie van bestaande regels).
    - Weigert een candidate_id die al in het bestand staat, tenzij allow_duplicate=True
      (voorkomt per ongeluk twee records voor dezelfde kandidaat in hetzelfde bestand).
    """
    path = Path(path)
    cid = record.get("candidate_id")
    if not cid:
        raise ValueError("record mist verplicht veld 'candidate_id'")

    if not allow_duplicate:
        existing = _existing_candidate_ids(path)
        if cid in existing:
            raise ValueError(
                f"{cid} staat al in {path} -- geen duplicaat toegevoegd "
                f"(gebruik allow_duplicate=True als dit bewust is)"
            )

    line = json.dumps(record, ensure_ascii=False, separators=COMPACT_SEPARATORS)

    needs_leading_newline = False
    if path.exists() and path.stat().st_size > 0:
        with open(path, "rb") as f:
            f.seek(-1, 2)
            last_byte = f.read(1)
        if last_byte != b"\n":
            needs_leading_newline = True

    with open(path, "a", encoding="utf-8", newline="\n") as f:
        if needs_leading_newline:
            f.write("\n")
        f.write(line + "\n")


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python3 append_batch_record.py <pad-naar-batchbestand.jsonl>  (record als JSON via stdin)",
              file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    record = json.loads(sys.stdin.read())
    append_jsonl_record(path, record)
    print(f"OK -- {record.get('candidate_id')} toegevoegd aan {path}")


if __name__ == "__main__":
    main()

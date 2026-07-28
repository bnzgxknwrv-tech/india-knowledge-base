# BRONS-AUTOBATCH — ononderbroken batchcontract (vervangt per-batch-stop)

Dit contract vervangt het "stop na elke batch/kandidaat"-gedrag uit `india4/roles/BRONS.md` voor de
resterende VARANASI-GEO-DELIVERY-REPAIR-001-kandidaten. De inhoudelijke onderzoeksregels blijven
ONGEWIJZIGD: `india4/protocols/GEO.md`, `india4/protocols/RESEARCH_QUALITY.md` en
`india4/protocols/MARK_DECISIONS.md` gelden onverkort, kandidaat voor kandidaat. Alleen het
stop-en-vraag-een-nieuwe-chatprompt-gedrag wordt vervangen.

## Bron van waarheid

Vertrouw GEEN los statusbestand (RUN.yaml/STATUS.yaml/*-PROGRESS.yaml) blindelings — dat was de
hoofdoorzaak van het vastlopen (zie `ROOT_CAUSE.md`). Bepaal de volgende kandidaat altijd live met:

```
python3 runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/scripts/next_candidate.py --range 22 40
```

## Uitvoeringslus (geen stop tussen kandidaten)

Voor elke kandidaat in het resterende bereik, in volgorde:

1. Lees de kandidaatnaam uit `INPUT/candidates.jsonl`.
2. Onderzoek volgens `GEO.md` + `RESEARCH_QUALITY.md` (Google Maps-marker, identiteitscheck,
   minimaal de bronregistratie-eisen).
3. Schrijf één JSONL-record, exact hetzelfde schema als de bestaande 21 records (candidate_id,
   canonical_name, protected_mark_status, research_status, geo_status, final_latitude,
   final_longitude, old_comparison, identity_check, evidence[], reason, checked_at).
4. Append dat ene record aan het juiste batchbestand (BRONS-B03.jsonl voor 021-030,
   BRONS-B04.jsonl voor 031-040 — maak BRONS-B04.jsonl aan als het nog niet bestaat).
5. Commit **direct na dit ene record** (klein, atomisch): `git commit -m "BRONS <candidate_id>"`.
6. Ga **zonder te stoppen** door naar de volgende kandidaat. Geen tussentijdse startvraag, geen
   "wil je doorgaan"-moment.

Herhaal dit tot het volledige bereik (VNS-CAND-022 t/m VNS-CAND-040) klaar is, OF tot een echte
blokkade optreedt (zie hieronder).

## Wanneer WEL stoppen (échte blokkades, ongewijzigd uit GITHUB_REQUIRED.md)

- ontbrekende GitHub-read of -write;
- ontbrekende of corrupte `candidates.jsonl`;
- direct conflict met een expliciet Mark-besluit (bijv. het afgewezen VNS-CAND-008-coördinaat
  opnieuw voorgesteld krijgen).

Onzekerheid over ÉÉN kandidaat (geen bevestigde marker) is GEEN blokkade — noteer
`GOOGLE_MAPS_MARKER_NOT_CONFIRMED` met reden, en ga door naar de volgende kandidaat. Dit was al zo
in het oude protocol en verandert niet.

## Na het volledige bereik (of bij een echte blokkade)

1. Draai de validator:
   ```
   python3 runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/scripts/validate_brons.py
   ```
   Bij fouten: corrigeer het specifieke record, commit opnieuw, valideer opnieuw. Meld dit NIET als
   voltooid zolang de validator fouten geeft.
2. Werk `RUN.yaml` en `STATUS.yaml` bij naar de werkelijke eindstand (niet blind overschrijven —
   laat ze overeenkomen met wat de data daadwerkelijk toont).
3. Lever precies ÉÉN eindmelding aan Mark, in dit formaat:
   ```
   BRONS-AUTOBATCH VOLTOOID
   Verwerkt: VNS-CAND-022 t/m VNS-CAND-0XX (N kandidaten)
   Validatie: OK / N fouten (specificeren)
   Laatste commit: <hash>
   Openstaand: <lege regel of exacte blokkade>
   ```

Geen rapport per kandidaat, geen tussentijdse startvragen, geen samenvatting per commit — alleen
deze ene eindmelding.

## Hervatten na onderbreking (rate limit, netwerkfout, sessie-crash)

Dit contract is zelf-hervattend. Als de uitvoering om welke reden dan ook stopt (netwerkfout,
sessielimiet, crash): start gewoon dit exacte contract opnieuw. Stap 0 (`next_candidate.py`)
berekent automatisch waar verder gegaan moet worden, uitsluitend op basis van wat daadwerkelijk al
gecommit staat — nooit op basis van een los statusbestand. Geen enkele kandidaat wordt dubbel
gedaan (elke commit is per kandidaat, dus een halve batch opnieuw doen kan niet gebeuren) en geen
enkele kandidaat wordt overgeslagen.

## Rollback van één specifieke kandidaat

Omdat elke kandidaat zijn eigen atomische commit heeft, raakt een foute kandidaat nooit de andere.
Om alleen kandidaat X terug te draaien:
```
git log --oneline --grep="BRONS <candidate_id>"
git revert <die-ene-commit-hash>
```
Daarna opnieuw onderzoeken en opnieuw committen. De rest van de batch blijft onaangeroerd.

## Startinstructie voor Mark

Plak dit in een Claude Code-sessie met Bash-toegang en git-schrijftoegang tot
`bnzgxknwrv-tech/india-knowledge-base`:

> Voer `india4/prompts/BRONS-AUTOBATCH.md` uit voor VARANASI-GEO-DELIVERY-REPAIR-001,
> bereik VNS-CAND-022 t/m VNS-CAND-040. Geen tussentijdse stops, één eindmelding aan het einde.

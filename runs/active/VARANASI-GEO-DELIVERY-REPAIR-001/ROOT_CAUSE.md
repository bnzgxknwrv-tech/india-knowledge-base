# ROOT_CAUSE — waarom VARANASI-GEO-DELIVERY-REPAIR-001 vastliep

Live geverifieerd tegen de repo (`git log`, `jq` over alle BRONS-bestanden, de india4-protocolbestanden)
op 2026-07-28. Geen aannames — alles hieronder is met een concreet bewijs onderbouwd.

## Werkelijke stand (afwijkend van wat de trackingbestanden beweren)

| Bestand | Beweert | Werkelijkheid (uit de data zelf) |
|---|---|---|
| `RUN.yaml` | `active_batch: BRONS-B01`, `status: READY_FOR_BRONS_B01` | BRONS-B01 (001-010) en BRONS-B02 (011-020) zijn **volledig af**; BRONS-B03 is bezig tot en met 021 |
| `STATUS.yaml` | `status: READY_FOR_BRONS`, `current_role: BRONS` | idem — 20 volledige + 1 gedeeltelijke kandidaat al verwerkt |
| `BRONS/BRONS-B01-PROGRESS.yaml` | `completed_count: 4`, `next_candidate: VNS-CAND-005` | BRONS-B01.jsonl bevat daadwerkelijk **alle 10** records (001-010), commits bevestigen dit tot en met `32a8175 BRONS complete VNS-CAND-010` |

Conclusie: de drie statusbestanden zijn op géén moment consequent bijgewerkt na de eerste paar
kandidaten. Alleen de ruwe `BRONS-B0X.jsonl`-bestanden zelf zijn betrouwbaar. Dit is met git-bewijs
vastgesteld (`git show 3192ef4 --stat`, `jq -r '.candidate_id' BRONS/*.jsonl`).

**Werkelijke voortgang nu**: VNS-CAND-001 t/m VNS-CAND-021 verwerkt (bevestigd via commit `3192ef4
BRONS VNS-CAND-021`, HEAD van de repo). Eerstvolgende: **VNS-CAND-022**. Dit klopt exact met wat
GREEN aangaf — op dit punt geen fout in die aanname.

## Hoofdoorzaak 1 — het protocol zelf is ontworpen op één-batch-per-chat-stop

`india4/roles/BRONS.md`, laatste zin, woordelijk:

> "Bij volledige uitvoering: readback, commit, batchstatus COMPLETED en exact één complete
> startvraag voor de volgende batch. **Stop daarna.**"

En `india4/protocols/ROLE_HANDOFF.md`:

> "... exact één complete startvraag voor de volgende rol." / "stop na de eigen rol."

Dit is geen bug die per ongeluk is ontstaan — het is een **letterlijke, geschreven regel** die elke
rol dwingt te stoppen en een nieuwe chatprompt te eisen. Het "heen-en-weer-plakken" is dus het
protocol dat precies doet wat er staat, niet een storing erin.

## Hoofdoorzaak 2 — in de praktijk is de granulariteit nog kleiner dan per batch

De git-historie toont commits per **kandidaat**, niet per batch van 10:

```
3192ef4 BRONS VNS-CAND-021
d859492 BRONS VNS-CAND-020
8a9825c BRONS VNS-CAND-019
...
af6ad52 BRONS checkpoint VNS-CAND-005
5a24b32 BRONS progress VNS-CAND-004
187edd7 BRONS checkpoint VNS-CAND-004
```

Zelfs binnen één batch werd blijkbaar per kandidaat (soms zelfs met een los "checkpoint"/"progress"-
commit erbovenop) teruggekoppeld naar de chat, vermoedelijk door beperkingen van de ChatGPT-
connector per beurt (tool-call/context-limiet per bericht). Het resultaat: geen 4 handoffs voor 40
kandidaten, maar tientallen — precies de "absurde één-kandidaat-per-chat-loop" die GREEN benoemt.

## Hoofdoorzaak 3 — geen enkele bron van waarheid voor "wat is de volgende kandidaat"

Er bestaat geen mechanisme dat automatisch berekent welke kandidaat nog moet. Dat moet nu handmatig
worden afgeleid door `candidates.jsonl` te vergelijken met de inhoud van de BRONS-bestanden — precies
het soort boekhouding dat, gecombineerd met de stale statusbestanden hierboven, tot verwarring en
vastlopen leidt.

## Wat NIET de oorzaak is

- De 21 al verwerkte records zijn intern consistent en volgen het GEO/RESEARCH_QUALITY-schema
  correct (steekproef geverifieerd). Geen datacorruptie.
- Geen ontbrekende GitHub-read/write — de repo is normaal leesbaar en beschrijfbaar (`git remote -v`
  bevestigt push-URL, geen connector-blokkade zichtbaar in de data zelf).
- Bijvangst, niet de hoofdoorzaak van het vastlopen maar wel relevant voor GOUD later: van de 21
  verwerkte kandidaten kregen er slechts 2 `EXACT_GOOGLE_MAPS_MARKER`, de overige 19 eindigden op
  `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`. Dat is een onderzoeksresultaat, geen uitvoeringsfout — maar het
  betekent dat de GOUD-fase straks met veel `NOT_CONFIRMED`-punten moet werken.

## Fix — zie `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/scripts/` en
`india4/prompts/BRONS-AUTOBATCH.md`

Kern van de fix: geen enkel apart statusbestand meer vertrouwen. De enige bron van waarheid wordt de
data zelf (`candidates.jsonl` versus wat al in `BRONS-B0X.jsonl` staat), live herberekend door een
klein script bij elke start. En één uitvoerder (Claude Code) die per kandidaat commit maar NIET stopt
na elke kandidaat — pas bij einde van het bereik of een echte blokkade.

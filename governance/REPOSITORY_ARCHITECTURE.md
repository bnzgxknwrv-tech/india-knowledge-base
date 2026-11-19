# HOE DEZE REPOSITORY IN ELKAAR ZIT

Status: **ON-DEMAND — uitleg, geen verplichte boot-read**
Gebouwd: 2026-09-14, tijdens de successor-boot-opschoning (PR #23)

Kort: drie lagen. Van klein/verplicht naar groot/optioneel.

## LAAG 1 — ACTIVE COCKPIT (verplicht, lees dit altijd eerst)

Een handvol bestanden in `governance/`:
- `CURRENT_TRUTH.md` — wat staat inhoudelijk nu vast voor de reis (route, hotels, grades).
- `CURRENT_FRONTIER.md` — in welke fase zit het project nu, en wat is écht nog open.
- `HOW_TO_WORK_WITH_MARK.md` — hoe presenteer en communiceer je met Mark.
- `GUARDRAILS.md` — de harde regels die eerdere fouten voorkomen (geen grades verzinnen, geen dingen heropenen, geografie goed verifiëren, enzovoort).
- `MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` — de laatste controlelijst vóór elk substantieel antwoord.
- `FRESH_SESSION_BOOT_GATE.md` + `INDIA_MASTER_BOOT.md` — hoe een nieuwe sessie zichzelf technisch opstart (het receipt/CHECK-mechanisme).

`governance/BOOT_MANIFEST_V8.json` is het machineleesbare bestand dat exact vastlegt welke paden dit zijn. Als deze uitleg en het manifest ooit verschillen, wint het manifest.

## LAAG 2 — ON-DEMAND EVIDENCE (raadplegen wanneer nodig, niet standaard lezen)

Alles in `decisions/`, `research/`, en het grootste deel van `runs/active/`, plus een aantal oudere `governance/`-bestanden (zie `governance/ARCHIVE_INDEX.md` voor de precieze indeling). Dit is het bewijsarchief: de originele research, de losse gedateerde Mark-besluiten, de volledige redenering achter een regel die in laag 1 is samengevat.

Gebruik dit wanneer:
- iemand een grade of besluit betwist en je de bron nodig hebt;
- een samengevatte regel in laag 1 onduidelijk is en je de volledige uitleg wilt;
- je specifiek aan een nog open vraag werkt (bijvoorbeeld de Bodh Gaya-duur, of de Kumaon-ritsolve) en de bijbehorende diepere bestanden nodig hebt.

Niet gebruiken als standaard leeswerk bij elke nieuwe sessie.

## LAAG 3 — ARCHIEF (geschiedenis, met rust laten)

- Tientallen oude `worker/*`, `agent/india9-*`, `agent/india10-region-*`, `run/*`, `transition/*`-branches en losse worktree-branches. Historisch, parallel onderzoek. Niet doorzoeken tenzij je expliciet iets uit die geschiedenis nodig hebt.
- PR #23 zelf (500+ comments): het overlegkanaal tussen Mark, INDIA en CCI. Niet van voor naar achter herlezen — laag 1 bevat al wat ervan overeind is gebleven.

Niets in deze laag is verwijderd. Git bewaart alles; verwijderen kost meer risico dan het oplevert, en is in deze opschoning bewust niet gedaan tenzij iets aantoonbaar een betekenisloos duplicaat was.

## WAAROM DIT ZO IS OPGEBOUWD

Het project was in discovery-/macro-routefase enorm breed vertakt: veel parallelle AI-werkers die elkaar controleerden en opnieuw oplosten, wat resulteerde in honderden branches en bijna 500 PR-comments. Dat leverde waardevol onderzoek op, maar maakte elke sessiewissel duur: een nieuwe sessie moest tientallen grote bestanden lezen om te weten waar het project stond.

Nu het project in de **A-timing/whole-human-haalbaarheidsfase** zit (zie `CURRENT_FRONTIER.md`) — dag voor dag de al vastgelegde plekken doorlopen in plaats van opnieuw ontdekken — is die brede structuur niet meer nodig als verplichte leeslast. Laag 1 is klein gehouden zodat een nieuwe sessie snel operationeel is; laag 2 en 3 blijven intact zodat niets verloren gaat.

END REPOSITORY ARCHITECTURE

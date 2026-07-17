# Claude-reviewopdracht: ONE-SHOT BRONS–ZILVER–GOUD

Status: REVIEW_REQUEST

Lees volledig:

1. `pipeline/proposals/ONE_SHOT_BZG_ORCHESTRATION_PROPOSAL.md`
2. `pipeline/protocols/EXECUTION_PROTOCOL.md`
3. `pipeline/protocols/CONTROLLER_TRANSITION_PROTOCOL.md`
4. `pipeline/protocols/LONG_RUNNING_EXECUTION_PROTOCOL.md`
5. `pipeline/protocols/SELF_ROUTING_PROTOCOL.md`
6. `pipeline/ENTRYPOINT.md`

## Opdracht

Treed op als onafhankelijke architect en red-teamreviewer. Beoordeel of Mark werkelijk met één startopdracht de volledige BRONS–ZILVER–GOUD-keten kan laten uitvoeren, met GitHub als duurzaam geheugen, automatische hervatting en één eindmelding.

Het doel is consensus, niet een vrijblijvende second opinion.

## Harde reviewvragen

1. Is de conclusie correct dat echte urenlange uitvoering en automatische hervatting een externe orchestrator vereist en niet betrouwbaar door alleen één gewone chatprompt kan worden geleverd?
2. Is n8n een geschikte primaire orchestrator voor deze repositorygestuurde pipeline, of is GitHub Actions, Claude Code SDK, OpenAI Agents SDK of een andere architectuur aantoonbaar beter?
3. Blijft de epistemische onafhankelijkheid van BRONS, ZILVER en GOUD voldoende behouden wanneer iedere fase een verse modelrun krijgt maar dezelfde GitHub-repository gebruikt?
4. Zijn worker- en controllerbevoegdheden voldoende gescheiden?
5. Kan de bestaande `state.yaml` + `events.jsonl` + `NEXT_ACTION.yaml`-architectuur canoniek blijven zonder een tweede concurrerend orchestratiestatusbestand?
6. Is de checkpointstrategie idempotent en veilig bij sessie-einde, API-time-out, connectorverlies of partiële GitHub-commit?
7. Zijn de truncatie- en splitregels voldoende om stille dataverliesfouten te voorkomen?
8. Zijn seriële GitHub-writes en blob-SHA-controle voldoende tegen conflictsituaties?
9. Welke harde stopvoorwaarden ontbreken?
10. Welke onderdelen zijn te complex en kunnen zonder kwaliteitsverlies worden verwijderd?
11. Is providerdiversiteit voor ZILVER wenselijk, verplicht of juist contraproductief?
12. Kan de pushmelding betrouwbaar worden losgekoppeld van de onderzoekscompletion?
13. Welke regressietests ontbreken?
14. Welke beveiligingsrisico’s ontstaan door modelworkers GitHub-write te geven?
15. Is de voorgestelde gebruikersstartopdracht kort genoeg en correct, gegeven dat het werkelijke protocol in GitHub staat?

## Verplicht antwoordformaat

Begin exact met:

`CLAUDE ARCHITECTUURREVIEW ZEGT:`

### A. Eindbesluit

Kies exact één:

- `ACCEPT`
- `ACCEPT_WITH_REQUIRED_CHANGES`
- `REJECT`

### B. Beslismatrix

Geef voor ieder punt `C-01` tot en met `C-16` uit `ONE_SHOT_BZG_CONSENSUS_MATRIX.md`:

- oordeel: ACCEPT / CHANGE / REJECT;
- korte technische reden;
- exacte vervangende formulering of protocolwijziging wanneer CHANGE;
- risico wanneer het voorstel ongewijzigd blijft.

### C. Top vijf failure modes

Rangschik de vijf waarschijnlijkste echte productiefouten op kans × impact. Geef per fout:

- detectie;
- automatische herstelactie;
- moment waarop Mark wel moet worden gewaarschuwd.

### D. Minimale uitvoerbare versie

Beschrijf de kleinste versie die al veilig één volledige testketen kan uitvoeren. Vermijd nice-to-haves.

### E. Productiearchitectuur

Geef jouw voorkeursarchitectuur met:

- orchestrator;
- modelcalls;
- GitHub-authenticatie;
- statebron;
- retries;
- checkpoints;
- notificatie;
- kosten- en veiligheidslimieten.

### F. Definitieve startopdracht

Schrijf één definitieve gebruikersstartopdracht van maximaal 120 woorden.

### G. Rapportcijfers

Geef cijfers van 1–10 voor:

- waarheid;
- uitvoerbaarheid;
- eenvoud;
- fouttolerantie;
- onafhankelijkheid van de metalen.

Noem per cijfer de belangrijkste aftrekreden.

Eindig exact met:

`/CLAUDE ARCHITECTUURREVIEW`

## Verboden

- Implementeer niets.
- Wijzig geen actieve run.
- Maak geen algemene loftekst zonder beslissingen.
- Beweer niet dat een gewone Claude- of ChatGPT-chat zichzelf na beëindiging opnieuw kan starten.
- Vermeng Markdown-protocollen niet met Home Assistant-YAML.
- Voeg geen nieuwe fase toe wanneer dezelfde functie door de orchestrator kan worden uitgevoerd.

END_OF_ARTIFACT
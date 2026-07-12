# templates/ - Hulpmiddelen, geen projectwaarheid

Deze map bevat gereedschap: recordsjablonen en promptsjablonen. **Geen enkel bestand in deze map bevat projectwaarheid.** Bij een conflict tussen een template en de gewone repositorybestanden is de repository altijd leidend.

## Recordsjablonen (structuur voor nieuwe records)
- `PLACE_TEMPLATE.md`
- `PERSON_TEMPLATE.md`
- `SOURCE_TEMPLATE.md`
- `DECISION_TEMPLATE.md`
- `AUDIT_TEMPLATE.md`

## Promptsjablonen voor externe AI's zonder GitHub-toegang
Externe consumenten-AI's (Perplexity, Gemini) kunnen een GitHub-repository niet betrouwbaar lezen. DeepSeek beweerde het te kunnen en loog; Copilot bleek het niet te kunnen. Daarom vult INDIA 2 (ChatGPT) deze sjablonen vers uit GitHub, zodat de externe AI een volledig zelfstandige opdracht krijgt en alleen internetonderzoek hoeft te doen.

- `EXTERNAL_CLUSTER_SWEEP_PROMPT.md` - basissweep van een cluster (bestaat)

Toekomstige sjablonen, aan te maken zodra ze werkelijk nodig zijn (nu bewust niet als leeg bestand aangemaakt, om verwarring te voorkomen):
- `EXTERNAL_VERIFICATION_PROMPT.md` - gerichte verificatie van één claim of locatie
- `EXTERNAL_COMPARISON_PROMPT.md` - vergelijking van twee concurrerende modules
- `EXTERNAL_FACTCHECK_PROMPT.md` - feitcontrole van een specifieke historische claim

Voor AI's die GitHub WEL kunnen lezen (INDIA 2, Claude) blijft `GENERIC_CLUSTER_SWEEP_STARTPROMPT.md` in de hoofdmap de juiste prompt.

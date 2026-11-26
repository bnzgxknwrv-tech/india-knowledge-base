# EXTERNAL_AI_PROMPT_RULES — canoniek

Datum: 2026-08-16

## Mark-regel: externe-AI-vragen altijd kopieerbaar blok

Wanneer INDIA/ChatGPT Mark tekst geeft die hij in een andere AI, andere chat, Claude Code, DeepSeek, Gemini, Claude, of een andere externe onderzoekssessie moet plakken:

1. Geef de volledige te kopiëren opdracht altijd in **één los fenced code block** (monospace), zodat de ChatGPT-interface een kopieerknop toont.
2. Zet geen noodzakelijke opdrachttekst buiten dat blok.
3. Als er meerdere aparte opdrachten nodig zijn, geef iedere opdracht in een eigen los code block.
4. Vermijd samengestelde proza-instructies waarbij Mark handmatig delen moet selecteren.
5. De tekst in het blok moet zelfstandig begrijpelijk zijn en niet afhankelijk zijn van omliggende uitleg.
6. Dit geldt ook voor éénregelige startvragen en relay-opdrachten.

Doel: minimale handmatige handelingen op iPhone en nul twijfel over welk deel gekopieerd moet worden.

## Onderzoeksbenchmark-regel

Voor externe onafhankelijke recall-tests geldt bovendien:
- geef de andere AI geen CCI-kandidatenlijst of bekende misses vóór discovery;
- laat de externe AI eerst zelf een lijst freezen;
- vergelijk pas daarna met CCI/INDIA/legacy;
- alle claims die alleen extern worden gevonden moeten bronmatig worden geverifieerd vóór ze als echte miss tellen.

# EXTERNAL_CLUSTER_SWEEP_PROMPT - Sjabloon voor externe onderzoekers zonder GitHub-toegang

> **STATUS: TOOL TEMPLATE**
>
> Dit bestand bevat geen projectwaarheid en mag nooit als bron van projectfeiten worden gebruikt.
>
> Alle projectinhoud (reisdata, prioriteitsindex, bestaande locaties, projectfase, besluiten, clusterstatus, enzovoort) wordt per sweep door INDIA 2 uit de actuele GitHub-repository ingevuld.
>
> **Bij een conflict tussen dit template en de repository is de repository altijd leidend.**
>
> Doel van dit bestand is uitsluitend het genereren van zelfstandige opdrachten voor externe AI-onderzoekers zonder GitHub-toegang.

## Waarom dit bestand bestaat

Externe consumenten-AI's (Perplexity, Gemini) kunnen een GitHub-repository niet betrouwbaar lezen. DeepSeek beweerde dit wel te kunnen en bleek te liegen; Copilot bleek het niet te kunnen. Daarom krijgen externe onderzoekers **geen GitHub-opdracht**, maar een volledig zelfstandige prompt waarin INDIA 2 alle benodigde context heeft ingevuld. De externe AI hoeft alleen internetonderzoek te doen.

Voor AI's die GitHub WEL kunnen lezen (INDIA 2 zelf, Claude) blijft `GENERIC_CLUSTER_SWEEP_STARTPROMPT.md` de juiste prompt. Dat bestand wordt niet vervangen.

## Eenmalige capaciteitstest per nieuwe AI

Test één keer, bij een nieuwe AI-dienst, of hij een publieke GitHub-URL werkelijk kan openen (bijvoorbeeld een raw.githubusercontent.com-link naar README.md, en vraag om een woordelijk citaat). Sla het resultaat op. Kan hij het → mooi meegenomen. Kan hij het niet → geen probleem, hij krijgt altijd de zelfstandige prompt. **Test daarna nooit meer.** Vertrouw nooit op zelfrapportage van een AI over zijn eigen GitHub-toegang.

## Huidige werkwijze (kalibratiefase)

De eerste 2 à 3 clusters krijgen **Perplexity en Gemini exact dezelfde opdracht**. Doel is niet alleen een goede sweep, maar de twee AI's kalibreren: wie mist structureel minder, wie gebruikt betere bronnen, wie verzint niets, wie levert een bruikbaar rapport. Dat kan alleen eerlijk worden gemeten bij een identieke opdracht. Pas na die kalibratie wordt besloten of er verschillende rollen komen, of dat één de hoofdonderzoeker wordt en de ander de tweede controle.

## Rolverdeling
- GitHub = de waarheid
- INDIA 2 (ChatGPT) = regisseur en contextgenerator; leest GitHub en vult dit sjabloon in
- Claude = curator; controleert repository-delta, schrijft alleen na Marks besluit
- Perplexity + Gemini = parallelle externe onderzoekers; lezen alleen, schrijven nooit
- Mark = enige beslisser en enige beoordelaar

---

## HET SJABLOON

INDIA 2 vult alle `{{...}}` in en levert het resultaat als één kopieerbaar codeblok. Mark plakt dat blok ongewijzigd in Perplexity én in Gemini.

```text
Jij voert één afgebakende BASIS-SWEEP uit voor een spirituele pelgrimsreis door India.

Je hebt GEEN toegang tot een repository nodig. Alle projectcontext staat hieronder.
Je taak is uitsluitend internetonderzoek met controleerbare bronnen.

========================================
PROJECTCONTEXT
========================================
{{PROJECT_CONTEXT}}
(doel van de reis; reisperiode)

========================================
HUIDIGE FASE
========================================
{{CURRENT_PHASE}}
(huidige projectfase; waarom juist dit cluster nu aan de beurt is)

========================================
DOELCLUSTER
========================================
{{CLUSTER}}
(naam; kernplaatsen; vorige cluster; volgende cluster)

========================================
WAT AL BEKEND IS
========================================
{{CURRENT_GITHUB_STATUS}}
(reeds vastgelegde locaties en hun status in dit cluster; bekende kandidaten;
bekende ashrams; open beslissingen. Dit is wat al onderzocht is - zoek naar wat
hier NIET staat.)

========================================
PERSOONLIJKE PRIORITEITSINDEX
========================================
{{PRIORITY_INDEX}}
(de vaste persoonlijke index; hoger = sterkere persoonlijke aantrekking. Gebruik
deze personen als DETECTOR om plekken te vinden. Het onderzoeksobject is altijd
de fysieke, bezoekbare PLEK - nooit de persoon zelf.)

========================================
ONDERZOEKSNIVEAU - DRIE GEOGRAFISCHE LAGEN
========================================
1. KERN: de kernplaatsen zelf en hun directe omgeving.
2. CLUSTERZONE: relevante plekken binnen grofweg twee uur reizen vanaf een
   vermoedelijke centrale basis.
3. ROUTECORRIDOR: relevante plekken die logisch liggen tussen het vorige cluster,
   dit cluster en het volgende cluster.

Zoek systematisch naar: directe levensplaatsen, woonhuizen, geboorteplaatsen en
samadhi-plaatsen; aantoonbare gebeurtenisplekken; grotten, tempels, ghats,
shrines, ashrams en historische gebouwen; plekken gekoppeld aan de
prioriteitsindex; minder bekende maar fysiek bezoekbare plekken; authentieke
levende ashrams die de route of verblijfsduur mogelijk kunnen veranderen;
belangrijke plaatsen in de omgeving die inhoudelijk sterker kunnen zijn dan de
hoofdplaats zelf; logische tussenstops in de routecorridor.

========================================
HARD ONDERSCHEID - VERPLICHT PER BEWERING
========================================
Markeer duidelijk het verschil tussen:
- FEIT: historisch of praktisch verifieerbaar;
- TRADITIECLAIM: door een lijn of gemeenschap overgeleverd, niet onafhankelijk
  vastgesteld;
- PERSOONLIJKE ERVARING: getuigenis of spirituele duiding;
- LOGISTIEKE INSCHATTING: reistijd of haalbaarheid die later exact moet worden
  gecontroleerd.

Een groot verhaal zonder aanwijsbare fysieke plek haalt de bezoekbaarheidspoort
niet.

========================================
BRONREGELS
========================================
Geef prioriteit aan: (1) officiële beheerders, ashrams, tempels, musea,
overheden, archeologische instanties; (2) primaire geschriften en institutionele
archieven; (3) betrouwbare historische of wetenschappelijke bronnen; (4) pas
daarna lokale reisbronnen, blogs en video's voor praktische aanwijzingen.

Neem commerciële reisbureauteksten niet zonder controle over. Noem onzekerheden
expliciet. Verzin GEEN coördinaten, toegang, openingstijden of gebeurtenissen.
Geef per vondst je bron.

========================================
VOORKOM DUBBELING EN INFLATIE
========================================
Controleer per vondst: is dit werkelijk een afzonderlijke fysieke plek, of een
onderdeel van een groter complex? Is de historische gebeurtenis aan deze exacte
plek gekoppeld? Is het de originele locatie, een latere gedenkplek, of alleen een
moderne organisatie? Bestaat de plek al onder een andere naam of spelling?
Voegt de plek inhoud toe, of blaast hij de lijst kunstmatig op?

Gebruik volledige namen; geen onverklaarde afkortingen.

========================================
WAT JE NIET DOET
========================================
{{PROJECT_RULES}}
- Ken GEEN waarderingen toe (dat doet alleen Mark).
- Kies GEEN hotels.
- Bepaal GEEN aantallen nachten.
- Leg GEEN definitieve route vast.
- Maak GEEN dagplanning.
- Schrijf niet alsof Mark al besloten heeft.

========================================
GEWENSTE UITVOER
========================================
{{OUTPUT_FORMAT}}

A. CLUSTERDEFINITIE
   Wat valt geografisch en inhoudelijk onder dit cluster? Wat hoort er NIET bij
   en waarom niet?

B. KANDIDATENKAART
   Per fysieke plek een afzonderlijk blok:
   NAAM:
   ALIASES/SPELLINGEN:
   LAAG: kern / clusterzone / routecorridor
   WAT IS HET:
   WIE OF WELKE LIJN:
   WAAROM RELEVANT:
   FYSIEKE STATUS EN BEZOEKBAARHEID:
   FEIT / TRADITIECLAIM / PERSOONLIJKE ERVARING:
   GLOBALE LIGGING TEN OPZICHTE VAN HET CLUSTER:
   BRON (met link):
   ZEKERHEID: hoog / middel / laag
   NOG LATER TE VERIFIEREN:

C. ASHRAMS EN BIJZONDERE VERBLIJFSERVARINGEN
   Welke authentieke ashrams bestaan? Welke kunnen mogelijk routevormend zijn
   (dus: een verblijf waard, niet alleen een bezoek)? Welke zijn alleen modern of
   organisatorisch? Welke vragen moeten later nog worden geverifieerd?

D. OMGEVING EN ROUTECORRIDOR
   Welke sterke plekken liggen buiten de kern maar binnen circa twee uur? Welke
   betekenisvolle tussenstops liggen logisch op de aan- of afreisroute? Welke
   genoemde plekken zijn juist te ver en vormen een afzonderlijke module?

E. COMPLEETHEIDSCONTROLE
   Welke personen uit de prioriteitsindex zijn systematisch gecontroleerd? Welke
   zoekrichtingen leverden niets op? Welk risico op gemiste obscure plekken
   blijft bestaan?

F. BASISCONCLUSIE
   Is de kandidatenkaart compleet genoeg om de locaties te laten beoordelen?
   Welke maximaal vijf open vragen blokkeren die beoordeling nog?

Eindig met "BASIS-SWEEP COMPLEET" of "BASIS-SWEEP NOG NIET COMPLEET - BLOKKERS: ..."
```

---

## Vergelijkprotocol (INDIA 2 na ontvangst van beide rapporten)

| Controle | Perplexity | Gemini |
|---|---|---|
| Gemiste kernlocaties | | |
| Nieuwe kandidaten gevonden | | |
| Bronkwaliteit | | |
| Feit/traditie correct gescheiden | | |
| Aliasfouten | | |
| Dubbeltellingen | | |
| Hallucinaties (verzonnen details) | | |
| Bruikbaarheid van het rapport | | |

Oordeel per sweep: beide goed / Perplexity beter / Gemini beter / beide onvoldoende.

Beslisregels:
- Een vondst die maar één AI heeft, blijft behouden als kandidaat (dat is juist de winst van twee onderzoekers).
- Tegenspraak over een feit → INDIA 2 zoekt uit, of het wordt een open vraag.
- Beide missen iets dat Mark verwacht → extra gerichte ronde.
- Een AI die plekken verzint of geen bronnen geeft → ongeschikt, meld dit aan Mark.

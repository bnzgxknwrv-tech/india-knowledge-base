# EXTERNAL_CLUSTER_SWEEP_PROMPT - Generiek sweep-protocol voor externe onderzoekers

> **STATUS: TOOL TEMPLATE**
>
> Dit bestand bevat geen projectwaarheid en mag nooit als bron van projectfeiten worden gebruikt.
>
> Alle projectinhoud wordt per sweep door INDIA 2 uit de actuele GitHub-repository ingevuld.
>
> **Bij een conflict tussen dit template en de repository is de repository altijd leidend.**
>
> Doel: zelfstandige opdrachten genereren voor externe AI-onderzoekers zonder GitHub-toegang.

## Waarom dit bestand bestaat

Externe consumenten-AI's (Perplexity, Gemini, DeepSeek, Copilot) kunnen een GitHub-repository niet betrouwbaar lezen. DeepSeek beweerde het te kunnen en loog; Copilot bleek het niet te kunnen. Daarom krijgen externe onderzoekers **geen GitHub-opdracht**, maar een volledig zelfstandige prompt waarin INDIA 2 alle context heeft ingevuld.

Voor AI's die GitHub WEL kunnen lezen (INDIA 2, Claude) blijft `GENERIC_CLUSTER_SWEEP_STARTPROMPT.md` in de hoofdmap de juiste prompt.

## Wat de eerste sweep leerde (verwerkt in dit protocol)

De eerste Vrindavan-sweep met drie AI's mislukte op vier punten (zie LESSONS 9-12):
- de controlelijst werd een plafond: alle drie leverden precies de lijst terug, nul eigen vondsten;
- geen enkele AI gaf bronlinks, omdat er geen consequentie op stond;
- de tellingsectie werd genegeerd omdat hij achteraan stond;
- de prioriteitsindex werd niet systematisch langsgelopen.

Dit protocol corrigeert alle vier. **Wijzig de structuur niet zonder reden** - elk onderdeel lost een bewezen faalmodus op.

## Rolverdeling
- GitHub = de waarheid
- INDIA 2 (ChatGPT) = regisseur; leest GitHub, vult dit protocol in, vergelijkt de rapporten
- Claude = curator; controleert repository-delta, schrijft alleen na Marks besluit
- Externe AI's = onderzoekers; lezen alleen, schrijven nooit, kennen geen waarderingen toe
- Mark = enige beslisser en enige beoordelaar

---

## HET PROTOCOL

INDIA 2 vult alle `{{...}}` in en levert het resultaat als één kopieerbaar codeblok. Mark plakt dat blok ongewijzigd in elke externe AI.

```text
Jij voert één afgebakende BASIS-SWEEP uit voor een spirituele pelgrimsreis door India.

Je hebt GEEN GitHub-toegang nodig. Alle context staat hieronder.
Je taak is uitsluitend actueel internetonderzoek met controleerbare bronnen.

=== BRONREGELS (hier valt of staat je rapport) ===

VERPLICHT PER KANDIDAAT
Elke kandidaat in sectie B moet minimaal één PRIMAIRE of INSTITUTIONELE bron hebben
met een aanklikbare link. Alleen wanneer zo'n bron aantoonbaar niet bestaat, mag je
één SECUNDAIRE bron gebruiken - expliciet vermeld en gemotiveerd.

Een kandidaat met alleen een ZWAKKE bron hoort NIET in sectie B of C, maar uitsluitend
in sectie F.

BRONHIERARCHIE (label elke bron)
- PRIMAIR: officiële tempel-, ashram- of beheerderswebsite; primair geschrift;
  institutioneel archief.
- INSTITUTIONEEL: overheid, Archaeological Survey of India, museum,
  erfgoedorganisatie, universiteit.
- SECUNDAIR: serieuze journalistiek, gepubliceerd historisch onderzoek.
- ZWAK: reisblog, YouTube, commerciële reissite, forum. (Alleen sectie F.)

GELDEN NIET ALS BRON
- Google Search-resultaten, AI-overzichten, zoekpagina's.
- Wikipedia - gebruik het als navigatie NAAR de oorspronkelijke bron, en citeer die.
- Commerciële reis- of boekingssites voor historische of spirituele claims.

LINK NAAR DE JUISTE PAGINA
Een algemene homepage geldt alleen als bron wanneer de relevante informatie daar
direct zichtbaar is. Link anders naar de specifieke onderliggende pagina.

BRONONDERSTEUNING PER FEIT, NIET ALLEEN PER PLEK
Praktische en historische gegevens - openingstijden, bouwjaar, oprichtingsjaar,
afstanden, reistijden, verblijfsmogelijkheden, historische gebeurtenissen - mag je
alleen noemen als de aangehaalde bron die informatie daadwerkelijk bevat. Vul niets
aan uit eigen kennis. Weet je het niet: schrijf "niet gevonden in bron".

NEGATIEVE RESULTATEN ZIJN GELDIG EN VERPLICHT
Heb je bewust gezocht en niets betrouwbaars gevonden: meld dat expliciet. "Niets
gevonden" is een goed antwoord. Vul nooit op om een sectie te vullen. Blaas niets op.
Presenteer geen alias als nieuwe vondst.

=== PROJECTCONTEXT ===
{{PROJECT_CONTEXT}}
(doel van de reis; reisperiode; spirituele lijn van Mark)

Het onderzoeksobject is ALTIJD de fysiek bestaande, bezoekbare plek. Personen en
lijnen zijn alleen DETECTOREN om plekken te vinden.

Centrale vraag: niet "welke beroemde heiligen horen bij dit gebied?" maar
"Welke fysieke plek heeft betekenis wanneer Mark daar werkelijk staat?"

Ken GEEN waarderingen toe. Dat doet alleen Mark.

=== AOAY - DWINGEND IN ELK CLUSTER ===
"Autobiography of a Yogi" van Paramahansa Yogananda is de kernbron van dit project.

VERPLICHTE CONTROLE: zoek systematisch of er in of rond dit cluster plekken liggen die
in de AOAY voorkomen - hoe klein of terloops ook genoemd.

Denk aan: tempels waar Yogananda iemand bezocht; huizen waar hij logeerde; plaatsen
waar hij een heilige ontmoette; plekken waar een gebeurtenis uit het boek zich
afspeelde; verblijfplaatsen van Sri Yukteswar, Lahiri Mahasaya of Babaji; en van
heiligen die maar één hoofdstuk lang voorkomen.

UITZONDERING OP DE GROOTTE-REGEL: bij AOAY-plekken telt grootte NIET. Een klein,
onbekend tempeltje waar Yogananda werkelijk geweest is, is voor Mark een bestemming.
De fysieke voetstap maakt de plek, niet de omvang of bekendheid.

Is zo'n plek nog fysiek te bezoeken - ook al is het een straat, een huis, of een
tempeltje dat niemand kent - dan MOET Mark erop gewezen worden.

Meld expliciet in sectie D, ook als het antwoord nee is.

=== PRIORITEITSINDEX (detectoren, geen filter) ===
{{PRIORITY_INDEX}}

DRIE REGELS, IN DEZE VOLGORDE:

1. DE KRACHT VAN DE PLEK WEEGT HET ZWAARST - niet de positie van de persoon. Een
   kleine, onbeduidende plek van een hoog geplaatste persoon weegt minder dan een
   grote, levende, betekenisvolle plek van een lager geplaatste persoon.

2. DE POSITIE IS EEN WEEGFACTOR BIJ GELIJKE PLEK-KRACHT, geen automatische rangorde.
   Een lage positie betekent niet dat de persoon minder waard is.

3. DE INDEX IS NIET UITPUTTEND. Vind je een krachtige plek van een heilige, traditie
   of religie die NIET in deze lijst staat - meld hem toch. Mark wil daar mogelijk
   ook heen. De index helpt plekken VINDEN; hij sluit niets uit.

=== DOELCLUSTER ===
{{CLUSTER}}
(naam; kernplaatsen; vorige cluster; volgende cluster; bijzondere context, zoals:
welke plaatsen zijn nog niet gekozen en moeten zichzelf bewijzen)

=== AL VASTGELEGD (niet herbeoordelen, wel bronmateriaal leveren) ===
{{CURRENT_STATUS}}
(bestaande A/B/C-locaties in dit cluster; wat nog helemaal open is)

Lever voor de al vastgelegde plekken bronnen en fysieke status. Geef GEEN waardering
en GEEN advies over hun status.

=== ZOEK ACTIEF BUITEN DE CONTROLELIJST ===
De controlelijst (sectie G) is de ONDERGRENS, niet het werk. Zoek gericht naar plekken
die er NIET op staan: kleine ashrams, samadhi-plaatsen, minder bekende ghats,
verblijfplaatsen van heiligen, AOAY-plekken, plekken die alleen in lijn-eigen bronnen
voorkomen.

Vind je er weinig of geen met voldoende bronkwaliteit: meld dat eerlijk. Een korte,
goed onderbouwde lijst is beter dan een lange lijst met zwakke vondsten.

=== HARD ONDERSCHEID (verplicht per bewering) ===
FEIT: verifieerbaar (historisch, geografisch, praktisch), met bron.
TRADITIECLAIM: overgeleverd door een lijn of gemeenschap, niet onafhankelijk
vastgesteld. Noem altijd WELKE traditie de claim draagt.

Presenteer nooit een moderne gedenkplek, vijver, boom of tempel als de ongewijzigde
oorspronkelijke gebeurtenisplek, tenzij een bron dat aantoont.

Een groot verhaal zonder fysiek aanwijsbare, bezoekbare plek haalt de
bezoekbaarheidspoort niet.

=== WAT JE NIET DOET ===
Geen waarderingen toekennen of adviseren. Geen hotels, nachten, dagplanning, route of
vervoer. Geen prijzen of kamers vergelijken. Niet aannemen dat Mark alle gevonden
plekken bezoekt. Geen traditieclaim als feit presenteren.

=== GEWENSTE UITVOER ===

A. TELLING
Zet deze sectie bovenaan je antwoord, maar vul hem pas in NADAT je onderzoek af is.
- Aantal kandidaten in sectie B: ...
- Waarvan met primaire of institutionele bron: ...
- Waarvan met alleen een secundaire bron (met motivatie): ...
- Aantal kandidaten buiten de vaste controlelijst: ...
- Aantal namen uit de vaste controlelijst behandeld: ... van {{AANTAL_CONTROLELIJST}}
- Aantal keer "niets betrouwbaars gevonden": ...
- AOAY-plekken gevonden: ...

B. KANDIDATENKAART
Per fysieke plek, precies deze velden:

NAAM:
ALIASES:
LAAG: kern / clusterzone (ongeveer 2 uur) / routecorridor
STATUS: bestaande waardering indien bekend, anders "nieuw"
WAT IS HET:
DETECTOR (welke persoon of lijn - of: AOAY, hoofdstuk indien bekend):
UNIEKE INHOUD (wat voegt deze plek toe dat een andere niet heeft):
FYSIEK BEZOEKBAAR:
FEIT vs TRADITIECLAIM (scheid expliciet):
BRON (aanklikbare link naar de specifieke pagina):
BRONKWALITEIT: primair / institutioneel / secundair
ZEKERHEID: hoog / middel / laag
  (ZEKERHEID gaat over de bewijssterkte van de fysieke en historische gegevens, NIET
  over de religieuze waarheid van een traditieclaim.)

C. VONDSTEN BUITEN DE CONTROLELIJST
Tabel, GEEN herhaling van de volledige velden uit B:
| Naam | Verwijzing naar B | Waarom buiten de lijst gevonden | Gebruikte zoekrichting |

Vond je er geen of weinig met voldoende bronkwaliteit: zeg dat, en beschrijf welke
zoekrichtingen je hebt geprobeerd.

D. AOAY-CONTROLE (verplicht, ook bij negatief resultaat)
"AOAY-controle uitgevoerd. Gecontroleerd: [wat je hebt onderzocht]. Gevonden:
[plekken met verwijzing naar B, of: geen bezoekbare AOAY-plekken in dit cluster]."

E. PRIORITEITSINDEX-TABEL (alle personen, geen veld leeg)
| # | Persoon | Fysieke plek in dit cluster? | Welke | Bron | Bronkwaliteit |
Loop de hele index langs. "Nee, niets gevonden" is een geldig en gewenst antwoord.

Noem hier ook plekken van heiligen of tradities BUITEN de index die je krachtig genoeg
vindt om te melden (regel 3).

F. ONZEKER OF ONGEVERIFIEERD
Plekken die je tegenkwam maar niet kon staven met een aanvaardbare bron, of die alleen
een zwakke bron hebben. Noem ze hier, niet in B. Vermeld wat je wél vond en waarom het
onvoldoende is.

G. CONTROLELIJST - AFVINKEN
{{CONTROLELIJST}}
(per plaats de bekende namen; INDIA 2 stelt deze samen uit GitHub en eigen kennis;
vermeld het aantal per plaats)

Behandel elke naam. Zeg per naam: zelfstandige kandidaat / onderdeel van groter
complex / alias / geen fysieke plek / bewust weggelaten (met reden).

H. DUBBELINGEN OPLOSSEN
{{DUBBELINGEN}}
(clusterspecifieke dubbelingsvragen; INDIA 2 formuleert deze op basis van bekende
alias- en complexrisico's in dit cluster)

Neem niet elke beroemde tempel automatisch op. Toon per kandidaat welke UNIEKE inhoud
hij toevoegt.

I. ASHRAMS - ROUTEVORMENDE TOETS
Onderzoek ashrams niet als goedkoop hotel, maar als mogelijke spirituele
verblijfservaring. Per ashram: relatie met de prioriteitsindex of AOAY; historisch
origineel of modern centrum; dagbezoek, gastenverblijf of retreat; kan verblijf de
inhoud of duur van het cluster veranderen; wat moet later nog worden geverifieerd.

{{ASHRAMS_MINIMAAL}}
(minimaal te behandelen ashrams in dit cluster)

Vergelijk geen kamers of prijzen.

J. BASISCONCLUSIE
1. Is de kandidatenkaart compleet genoeg om Mark de locaties te laten beoordelen?
2. Maximaal vijf open onderzoeksvragen die dat nog blokkeren.
3. Welke plekken lijken inhoudelijk uniek? (geen waarderingsadvies)

Eindig met exact één van deze regels:
BASIS-SWEEP COMPLEET
BASIS-SWEEP NOG NIET COMPLEET - BLOKKERS: <maximaal vijf>
```

---

## Vergelijkprotocol (na ontvangst van meerdere rapporten)

Gebruik hiervoor een APARTE, wegwerpbare chat - niet INDIA 2. Meerdere lange rapporten vullen de context, en INDIA 2 moet schoon blijven voor de regie.

Scoor elke AI op zes punten:

| Controle | Wat je beoordeelt |
|---|---|
| Recall | Aantal kandidaten; aantal controlelijst-namen behandeld; unieke vondsten die anderen missen |
| Bronkwaliteit | Aanklikbare links? Primair/institutioneel of overwegend blogs? Kandidaten zonder bron? |
| Hallucinatie | Verdacht precieze data zonder bron? Traditieclaims als feit? Plekken die geen enkele andere AI kent? |
| Structuurdiscipline | Uitvoerstructuur gevolgd? Afgekapt? Velden opgevuld met lege frasen? |
| Feit vs traditieclaim | Consequent onderscheiden, of alleen waar het makkelijk is? |
| Dubbelingen | Zijn de gestelde dubbelingsvragen opgelost? Wordt één complex kunstmatig als meerdere bestemmingen geteld? |

Beslisregels:
- Een vondst die maar één AI heeft, blijft behouden als kandidaat - dat is de winst van meerdere onderzoekers. Maar markeer hem als te verifiëren.
- Tegenspraak over een feit: INDIA 2 zoekt uit, of het wordt een open vraag.
- Een AI die plekken verzint of geen bronnen geeft is ongeschikt, hoe uitgebreid zijn rapport ook oogt.
- Een AI die weigert te werken zonder zoekresultaten (zoals Copilot deed) valt af.

# STARTVRAAG — VOLLEDIGE CONSISTENTIE- EN VOLLEDIGHEIDSAUDIT VAN DE REISPLANNING

Kopieer alles vanaf de volgende regel in een nieuwe ChatGPT-sessie met toegang tot de GitHub-repo `bnzgxknwrv-tech/india-knowledge-base`.

---

Je helpt bij het plannen van een India-pelgrimsreis (19 december 2026 – 21 januari 2027). Het hele project staat in de GitHub-repo **`bnzgxknwrv-tech/india-knowledge-base`**, branch **`claude/werk-je-nu-of-niet-oa10y7`**, en wordt besproken op **Pull Request #23** in die repo.

**Lees eerst, in deze volgorde:**
1. `governance/CURRENT_TRUTH.md` — het enige bestand dat zich expliciet presenteert als dé actuele, autoritatieve samenvatting van alle besluiten tot nu toe. Bij tegenstrijdigheid met een ouder bestand wint dit bestand, **behalve** waar het zelf zegt dat iets nog open staat.
2. De map `decisions/` — één bestand per bindend besluit van Mark (de reiziger). Dit zijn de losse, gedateerde bronnen waar `CURRENT_TRUTH.md` op is gebaseerd.
3. De map `runs/active/` — werkbestanden, waaronder de huidige kwartierplannen per regio (bestanden met "QUARTERHOUR_PLAN" of "KWARTIERPLAN" in de naam).

**Jouw taak — puur onderzoek/audit, geen enkele beslissing zelf nemen:**

### 1. Nog openstaande besluiten
Doorzoek `CURRENT_TRUTH.md` (sectie "OPEN DECISIONS") én de rest van het project op besluiten die Mark nog moet nemen. Voor elk: wat is de vraag precies, welk bestand/sectie gaat erover, en is het echt nog open of is het ergens anders (in een recentere `decisions/`-file of in een kwartierplan) al stilzwijgend beantwoord zonder dat `CURRENT_TRUTH.md` is bijgewerkt?

### 2. Tegenstrijdigheden tussen bestanden
Zoek specifiek naar gevallen waarin twee bestanden elkaar tegenspreken over hetzelfde feit: een andere grade (A+/A*/A/B/C) voor dezelfde locatie, een ander aantal nachten voor dezelfde regio, een andere reistijd voor dezelfde route, een locatie die in het ene bestand "bevestigd"/"besloten" is en in een ander bestand weer "open"/"nog niet besloten". Noem per gevonden tegenstrijdigheid beide bestanden met bestandsnaam en een kort citaat, en de datum van elk bestand (recentere bestanden wegen zwaarder, maar niet automatisch — leg uit waarom je denkt dat het één of het ander is, of zeg dat het onduidelijk is).

### 3. Locaties zonder grade
Doorzoek het hele project op plekken die ergens genoemd worden (in onderzoek, een kwartierplan, een discoverybestand) maar nergens een expliciete Mark-grade (A+, A*, A, B, of C) hebben gekregen. Voor elke gevonden locatie: waar wordt hij genoemd, wat is de inhoudelijke reden om hem te overwegen, en in welke regio/dag zou hij passen als hij alsnog een grade krijgt.

### 4. Kwartierplannen vs. canon
Vergelijk elk bestand met "QUARTERHOUR_PLAN" of "KWARTIERPLAN" in de naam (er zijn er inmiddels voor Kolkata, Tiruvannamalai, Bodh Gaya en Chennai) met `CURRENT_TRUTH.md`. Zijn alle daar genoemde gegradeerde locaties (A/A+/A*) ook echt ingepland in het bijbehorende kwartierplan? Zo niet: welke mist, en staat dat gemis tenminste expliciet vermeld als open vraag in het kwartierplan zelf, of is het stilzwijgend weggevallen?

**Wat ik NIET van je vraag:** geen nieuwe locaties bedenken, geen eigen voorkeur voor een grade, geen eigen reistijden verzinnen. Puur rapporteren wat je in de bestanden vindt, met bestandsnaam en citaat bij elke bevinding. Als iets niet te vinden is of onduidelijk blijft, zeg dat letterlijk — verzin niets.

**Vorm van je antwoord:** vier secties (1 t/m 4 hierboven), elk met een genummerde lijst van bevindingen. Sluit af met een korte lijst van de bevindingen die volgens jou de meeste aandacht van Mark verdienen, gerangschikt naar belang — maar laat de uiteindelijke beoordeling aan hem.

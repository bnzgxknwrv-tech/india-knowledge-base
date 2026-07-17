# OVERDRACHT AAN INDIA2 — MINIMALE TUSSENREGIE VOOR BRONS → ZILVER → GOUD

## 1. Aan wie dit rapport is gericht

INDIA2,

Dit rapport is rechtstreeks aan jou gericht. Mark wil dat jij het volledige voorstel beoordeelt tegen de bestaande repositoryprotocollen en de feitelijke werkwijze van de India-pipeline. Het doel is niet om opnieuw een grote technische architectuur te ontwerpen. Het doel is een kleine, betrouwbare procesverbetering waarmee Mark minder lang hoeft te wachten en minder vaak handmatig tussen chats hoeft te schakelen.

Lees daarom niet alleen dit document. Controleer ook de relevante bestaande rolcontracten, controllerprotocollen, contextmanifesten, statebestanden en de ontwerpstukken op deze branch. Geef daarna een zelfstandig oordeel en stel alleen wijzigingen voor die aantoonbaar nodig zijn.

## 2. Marks werkelijke doel

Mark wil inhoudelijk dezelfde BRONS-, ZILVER- en GOUD-pipeline behouden.

Hij wil vooral af van dit patroon:

1. INDIA2 maakt een startopdracht voor SUBREGIE.
2. SUBREGIE maakt een startopdracht voor BRONS.
3. Mark wacht op BRONS.
4. Mark gaat terug naar SUBREGIE.
5. SUBREGIE maakt de volgende opdracht voor ZILVER.
6. Mark wacht op ZILVER.
7. Mark gaat opnieuw terug naar SUBREGIE.
8. SUBREGIE maakt de volgende opdracht voor GOUD.
9. Mark wacht opnieuw.
10. GOUD levert iets op waarna INDIA2 mogelijk nog een eindbewerking moet doen.

Dat levert veel wachttijd, veel kopieerwerk en meerdere lange tussenstappen op die inhoudelijk weinig toevoegen.

Marks voorkeur is:

1. INDIA2 maakt direct één complete, correcte startopdracht voor BRONS.
2. BRONS voert zijn volledige rol uit en levert daarna direct een complete overdrachtsopdracht voor ZILVER.
3. Mark kopieert alleen die overdracht naar een verse ZILVER-chat.
4. ZILVER voert zijn volledige rol uit en levert daarna direct een complete overdrachtsopdracht voor GOUD.
5. Mark kopieert alleen die overdracht naar een verse GOUD-chat.
6. GOUD voert zijn volledige rol uit en levert direct het volledige eindrapport voor Mark.
7. INDIA2 hoeft na de start niet opnieuw tussenbeide te komen tenzij er een echte harde blocker, protocolconflict of state-desynchronisatie bestaat.

De kernwens is dus:

> liever één keer een lange, complete fase van ongeveer twee uur laten lopen dan drie of meer keren twintig minuten wachten op tussenregie en nieuwe prompts.

Mark accepteert dat hij na BRONS en ZILVER handmatig één antwoord naar de volgende chat kopieert. Hij wil vooral voorkomen dat hij telkens eerst terug moet naar SUBREGIE of INDIA2 om een nieuwe startopdracht te laten construeren.

## 3. Wat oorspronkelijk goed werkte

De bestaande architectuur bevat waardevolle eigenschappen die behouden moeten blijven:

- BRONS, ZILVER en GOUD zijn afzonderlijke rollen.
- Iedere rol heeft een eigen contract en eigen kwaliteitsverantwoordelijkheid.
- GitHub is de duurzame bron van waarheid.
- Context wordt via gepinde manifesten en commits overgedragen.
- Controllertransities bewaken de overgang tussen fasen.
- Workers mogen niet stil eigen protocollen of runstate herschrijven.
- Claims, source-ID's, statebestanden en artifacts moeten controleerbaar blijven.
- Verse chats of verse rolcontexten voorkomen dat ZILVER en GOUD slechts voortbouwen op de redeneerstijl van de vorige rol.

Mark wil deze inhoudelijke scheiding niet opheffen. Hij wil alleen de menselijke tussenregie verminderen.

## 4. Welke verkeerde afslag is genomen

Op de ontwerpbranch en in PR #14 is vervolgens een veel grotere oplossing uitgewerkt:

- n8n als externe orchestrator;
- non-interactieve Claude Code-workers;
- automatische polling en hervatting;
- externe heartbeat;
- kostenbewaking;
- kill switches;
- pushnotificaties;
- technische truncatiedetectie;
- volledig geautomatiseerde controllerketens.

Claude heeft die architectuur vervolgens beoordeeld en technisch verbeterd. Die review was op zichzelf coherent binnen dat ontwerp.

Het fundamentele probleem is echter dat dit niet Marks actuele vraag oplost. Het introduceert bovendien een andere uitvoerder voor de zware rollen. Mark wil niet dat Claude BRONS overneemt. Hij wil de inhoudelijke zware werkzaamheden door ChatGPT/OpenAI laten uitvoeren zoals nu, met de bestaande GitHub-connector en repositoryprotocollen.

De n8n/Claude Code-route zou daarnaast vereisen:

- installatie en beheer van n8n;
- serverbeheer;
- credentials en secrets;
- API- of CLI-integratie;
- foutafhandeling buiten de bestaande chats;
- monitoring van de orchestrator zelf;
- nieuwe implementatie- en testtijd;
- nieuwe operationele afhankelijkheden.

Dat is disproportioneel voor een pipeline met nog ongeveer tien sweeps. Het risico is dat er meer uren in automatisering verdwijnen dan er door de resterende runs worden bespaard.

Daarom geldt voor dit nieuwe voorstel:

- geen n8n;
- geen Claude Code als BRONS-, ZILVER- of GOUD-worker;
- geen externe runtime-orchestrator;
- geen wijziging van actieve runs;
- geen grote protocolmigratie voordat de eenvoudige keten is bewezen.

PR #14 moet daarom niet in zijn huidige architectuurvorm worden gemerged als productieoplossing.

## 5. Voorgestelde eenvoudige doelarchitectuur

```text
MARK
  |
  v
INDIA2
  |  maakt één complete BRONS-startopdracht
  v
BRONS
  |  schrijft gevalideerde resultaten naar GitHub
  |  sluit zijn rol af volgens contract
  |  levert complete ZILVER-startopdracht aan Mark
  v
MARK kopieert overdracht naar verse ZILVER-chat
  |
  v
ZILVER
  |  leest uitsluitend toegestaan/gepind predecessor-context
  |  controleert en verrijkt zelfstandig
  |  schrijft gevalideerde resultaten naar GitHub
  |  levert complete GOUD-startopdracht aan Mark
  v
MARK kopieert overdracht naar verse GOUD-chat
  |
  v
GOUD
  |  voert synthese, eindcontrole en finale repository-writes uit
  |  levert compleet eindrapport rechtstreeks aan Mark
  v
KLAAR
```

INDIA2 is in deze opzet alleen vooraf nodig voor:

- runselectie;
- beginstatuscontrole;
- vaststellen van de juiste gepinde context;
- het maken van de complete BRONS-startopdracht;
- eventueel een korte waarschuwing wanneer de run niet veilig kan starten.

INDIA2 is na de start niet meer nodig voor normale voortgang.

## 6. Belangrijk onderscheid: roltransitie versus promptoverdracht

Dit voorstel vraagt niet automatisch dat BRONS of ZILVER ongecontroleerd controllerbevoegdheden krijgt.

Er zijn twee afzonderlijke zaken:

### 6.1 Repositorytransitie

De bestaande protocollen bepalen wie:

- de fase afrondt;
- completionstatus schrijft;
- het volgende contextmanifest maakt;
- controllertransities uitvoert;
- NEXT_ACTION of equivalente state bijwerkt.

Dat moet volgens de huidige canonieke protocollen gebeuren. Wanneer de worker dit volgens zijn contract niet mag, mag hij die bevoegdheid niet stil overnemen.

### 6.2 Menselijke promptoverdracht

Los daarvan kan iedere voltooide rol een volledig, direct plakbaar startbericht voor de volgende chat teruggeven.

Dat startbericht hoeft geen nieuwe bron van waarheid te zijn. Het is slechts een bedieningsbericht dat de volgende worker instrueert:

- welke repository te openen;
- welke run te behandelen;
- welke rol uit te voeren;
- welk gepind contextmanifest te lezen;
- welke stopvoorwaarden gelden;
- welke writes verplicht zijn;
- welke handelingen verboden zijn.

De volgende rol moet alle feitelijke state opnieuw uit GitHub lezen. De overdrachtstekst mag dus nooit gebruikt worden om repository-state te vervangen.

Dit onderscheid is essentieel. Het maakt tijdwinst mogelijk zonder de bestaande state- en bevoegdheidsscheiding te beschadigen.

## 7. Verplichte einduitvoer van BRONS

BRONS moet na succesvolle voltooiing twee soorten output leveren.

### 7.1 Canonieke GitHub-output

Alles wat het BRONS-rolcontract vereist, waaronder minstens:

- volledige onderzoeksoutput;
- verplichte source records;
- candidate/claim artifacts;
- statusupdates;
- completioncommit;
- alle verplichte validaties en readbacks;
- geen ZILVER-inhoud die buiten BRONS-scope valt.

### 7.2 Bedieningsoutput voor Mark

BRONS eindigt uitsluitend met een compact completionblok plus een volledig plakbare ZILVER-startopdracht.

Aanbevolen structuur:

```text
RESULTAATSTATUS: <COMPLETED | BLOCKED | FAILED>
RUN_ID: <run-id>
COMPLETION_COMMIT: <sha of NONE>
HOOGSTE_BLOCKERS: <NONE of korte lijst>
NEXT_ROLE_READY: <YES | NO>

ZILVER_STARTOPDRACHT_BEGIN
<volledige zelfstandige opdracht>
ZILVER_STARTOPDRACHT_EINDE
```

Bij `NEXT_ROLE_READY: NO` mag geen misleidende startopdracht volgen. Dan moet helder staan welke harde blocker eerst door INDIA2 of Mark moet worden opgelost.

## 8. Verplichte inhoud van de ZILVER-startopdracht

De door BRONS teruggegeven ZILVER-opdracht moet zelfstandig uitvoerbaar zijn. Zij moet ten minste bevatten:

- repository: `bnzgxknwrv-tech/india-knowledge-base`;
- rol: ZILVER;
- exacte run-id;
- instructie om `pipeline/ENTRYPOINT.md` eerst te lezen;
- instructie om uitsluitend het gepinde ZILVER-contextmanifest te lezen;
- instructie om de volledige gevalideerde BRONS-output uit GitHub te halen;
- verplicht zelfstandig aanvullend internetonderzoek wanneer het ZILVER-contract dit verlangt;
- broncontrole;
- institutionele verificatie;
- fysieke-identiteitscontrole;
- actuele bezoekbaarheidscontrole;
- AOAY-dubbele verificatie wanneer toepasselijk;
- claimclassificatie;
- controle van alle source-ID-verwijzingen;
- verplichte writes en completioncommit;
- bestaande stopvoorwaarden;
- verbod op GOUD-context of controllertransition wanneer dat volgens het huidige contract niet is toegestaan;
- verplicht eindblok met volledige GOUD-startopdracht.

Belangrijk: BRONS mag de ZILVER-opdracht technisch voorbereiden, maar mag niet zelf de ZILVER-beoordeling invullen.

## 9. Verplichte einduitvoer van ZILVER

ZILVER levert eveneens twee soorten output.

### 9.1 Canonieke GitHub-output

Alles wat het ZILVER-rolcontract vereist, waaronder:

- audit van BRONS;
- zelfstandige aanvullende verificatie;
- gecorrigeerde of geclassificeerde claims;
- volledige broncontrole;
- alle verplichte ZILVER-artifacts;
- completioncommit;
- correcte state volgens de bestaande protocollen.

### 9.2 Bedieningsoutput voor Mark

```text
RESULTAATSTATUS: <COMPLETED | BLOCKED | FAILED>
RUN_ID: <run-id>
COMPLETION_COMMIT: <sha of NONE>
HOOGSTE_BLOCKERS: <NONE of korte lijst>
NEXT_ROLE_READY: <YES | NO>

GOUD_STARTOPDRACHT_BEGIN
<volledige zelfstandige opdracht>
GOUD_STARTOPDRACHT_EINDE
```

## 10. Verplichte inhoud van de GOUD-startopdracht

De door ZILVER teruggegeven GOUD-opdracht moet ten minste bevatten:

- repository en run-id;
- rol GOUD;
- instructie om `pipeline/ENTRYPOINT.md` eerst te lezen;
- uitsluitend het gepinde GOUD-contextmanifest en de expliciet toegestane predecessor-artifacts;
- volledige naleving van het GOUD-rolcontract;
- synthese zonder ongevalideerde claims opnieuw binnen te halen;
- controle van alle bron- en source-ID-verwijzingen;
- controle van fysieke identiteit, historische/spirituele relatie en actuele bezoekbaarheid waar die poorten gelden;
- controle dat classificaties en uitsluitingen consistent zijn;
- controle op ontbrekende, dubbele of conflicterende records;
- finale repository-writes;
- completioncommit;
- finale readback en stateconsistentie;
- verplicht volledig eindrapport rechtstreeks aan Mark;
- geen verplichte terugkeer naar INDIA2 bij succesvolle afronding.

## 11. Wat GOUD rechtstreeks aan Mark moet opleveren

GOUD moet niet alleen een technisch completionbericht geven. Het moet het volledige, bruikbare eindproduct leveren zodat INDIA2 geen redactie, samenvatting of interpretatie meer hoeft te doen.

Het eindrapport moet zo compleet zijn dat Mark direct begrijpt:

- wat onderzocht is;
- wat betrouwbaar bevestigd is;
- wat is afgewezen;
- welke onzekerheden overblijven;
- welke fysieke plekken daadwerkelijk zijn vastgesteld;
- welke relatie per plek is bevestigd;
- hoe de actuele bezoekbaarheid is beoordeeld;
- welke bronkwaliteit per belangrijke conclusie geldt;
- welke claims tijdens ZILVER zijn aangepast;
- wat de uiteindelijke GOUD-selectie of synthese is;
- of de repository technisch correct is afgerond.

### 11.1 Aanbevolen vaste structuur van het GOUD-eindrapport

1. **Eindstatus**
   - PASS / PARTIAL / BLOCKED / FAILED.
   - Run-id.
   - Finale completioncommit.

2. **Managementsamenvatting voor Mark**
   - Het belangrijkste resultaat in gewone taal.
   - Geen interne pipelinejargon tenzij noodzakelijk.

3. **Onderzoeksbereik**
   - Welke sweep, regio, traditie, bronset of onderzoeksvraag is behandeld.
   - Wat expliciet buiten scope bleef.

4. **Definitieve resultaten**
   - Volledige uiteindelijke kandidaten-/plekkenkaart of andere vereiste hoofdoutput.
   - Per item minimaal fysieke identiteit, ligging, historische/spirituele relatie, actuele bezoekbaarheid en onzekerheden.

5. **Afwijzingen en uitsluitingen**
   - Welke kandidaten zijn afgevallen.
   - Exacte reden.
   - Geen verborgen verlies van interessante maar onvoldoende verifieerbare kandidaten.

6. **Belangrijkste wijzigingen door ZILVER en GOUD**
   - Welke BRONS-conclusies zijn bevestigd.
   - Welke zijn aangepast.
   - Welke zijn verworpen.
   - Waarom.

7. **Bron- en bewijsstatus**
   - Institutionele bronnen.
   - Primaire of gezaghebbende historische/spirituele bronnen.
   - Actuele bezoekbaarheidsbronnen.
   - Eventuele bronconflicten.

8. **Onzekerheden en open punten**
   - Exact aangeven wat niet vastgesteld is.
   - Geen invulling door aannames.

9. **Technische pipeline-audit**
   - BRONS completion geldig: ja/nee.
   - ZILVER completion geldig: ja/nee.
   - GOUD completion geldig: ja/nee.
   - Contextmanifesten correct gepind: ja/nee.
   - Alle verplichte artifacts aanwezig: ja/nee.
   - Source-ID's oplosbaar: ja/nee.
   - State en events synchroon: ja/nee.
   - Finale repository-readback geslaagd: ja/nee.

10. **Geschreven artifacts**
    - Exacte paden.
    - Finale commits.

11. **Blockers**
    - `NONE` wanneer er geen blockers zijn.
    - Anders alleen echte blockers, met gevolgen.

12. **Definitief oordeel**
    - Een duidelijke afsluiting voor Mark.
    - Geen vraag om nog via INDIA2 te gaan wanneer de run geldig voltooid is.

## 12. Vormvereisten voor het GOUD-rapport

Het rapport moet:

- volledig zijn;
- zelfstandig leesbaar zijn;
- geen kennis van eerdere chats vereisen;
- geen verwijzing bevatten als “zie BRONS” zonder de relevante uitkomst samen te vatten;
- onderscheid maken tussen vastgesteld, aannemelijk, betwist en niet vastgesteld;
- duidelijk maken waar actuele bezoekbaarheid niet betrouwbaar vastgesteld kon worden;
- geen route-, hotel- of reisadvies toevoegen wanneer dat buiten scope is;
- geen ongefundeerde waarderingen invoeren;
- technisch bewijs en inhoudelijke conclusies van elkaar scheiden;
- de belangrijkste informatie niet alleen in GitHub laten staan maar ook in het eindrapport opnemen;
- compact genoeg blijven om bruikbaar te zijn, maar niet zo kort dat INDIA2 alsnog alle artifacts moet nalezen om Mark uit te leggen wat er is gebeurd.

## 13. Faalgedrag

De lineaire keten mag snelheid niet boven betrouwbaarheid stellen.

### 13.1 BRONS blokkeert

BRONS levert geen ZILVER-startopdracht alsof de fase geldig voltooid is. Het meldt:

- status BLOCKED;
- exacte blocker;
- laatste geldige commit;
- welke beslissing of reparatie nodig is.

Pas dan gaat Mark eventueel terug naar INDIA2.

### 13.2 ZILVER blokkeert

ZILVER levert geen GOUD-startopdracht alsof de audit geldig voltooid is. Het meldt dezelfde minimale blockerinformatie.

### 13.3 GOUD blokkeert

GOUD levert een volledig blocker/eindrapport met:

- wat wel voltooid is;
- wat niet kon worden afgerond;
- welke outputs geldig blijven;
- waarom geen PASS mogelijk is;
- wat Mark of INDIA2 precies moet beslissen.

### 13.4 Geen automatische omzeiling

Geen enkele rol mag:

- een SHA-conflict negeren;
- ontbrekende context zelf reconstrueren uit chatgeheugen;
- een truncatie gokken;
- een ongeldige claim stil laten passeren;
- een ontbrekende bron als bevestigd behandelen;
- state-desynchronisatie repareren buiten de eigen bevoegdheid.

## 14. Technische implementatie met minimale wijziging

Voorkeur: voeg niet direct een groot nieuw orchestrationprotocol toe.

Begin met de kleinste wijziging die het gedrag afdwingt:

1. Voeg aan het BRONS-rolcontract een verplichte `NEXT_ROLE_HANDOFF`-uitvoer toe.
2. Voeg aan het ZILVER-rolcontract dezelfde verplichte overdracht naar GOUD toe.
3. Voeg aan het GOUD-rolcontract een verplichte `MARK_FINAL_REPORT`-sectie toe.
4. Definieer één canoniek templatebestand voor de overdrachtsblokken zodat iedere rol dezelfde structuur gebruikt.
5. Laat iedere volgende rol de feitelijke state opnieuw uit GitHub lezen.
6. Laat controllerbevoegdheden ongewijzigd tenzij INDIA2 na protocolcontrole expliciet concludeert dat een kleine wijziging nodig is.
7. Test dit eerst op één synthetische of laag-risico-run.
8. Pas het pas daarna toe op de resterende sweeps.

Mogelijke nieuwe canonieke bestanden, alleen wanneer INDIA2 dit passend vindt:

- `pipeline/protocols/ROLE_HANDOFF_PROTOCOL.md`
- `pipeline/templates/ZILVER_START_HANDOFF.md`
- `pipeline/templates/GOUD_START_HANDOFF.md`
- `pipeline/templates/MARK_FINAL_REPORT.md`

Een alternatief met nog minder repositorywijziging is de overdrachtsvereisten rechtstreeks in de drie bestaande rolcontracten op te nemen.

## 15. Bevoegdheidsvraag die INDIA2 expliciet moet beantwoorden

De belangrijkste technische vraag is niet of BRONS tekst voor ZILVER mag schrijven. Dat kan veilig als bedieningsoutput.

De echte vraag is:

> Wie voert volgens de huidige canonieke protocollen de controllertransition en de creatie/pinning van het volgende contextmanifest uit?

INDIA2 moet dit exact uit de repository vaststellen.

Daarna zijn er twee veilige modellen:

### Model A — worker mag bestaande transition uitvoeren

Wanneer het huidige contract dit al toestaat of met een kleine, expliciete wijziging kan toestaan:

- BRONS voltooit;
- BRONS voert de voorgeschreven transition uit;
- BRONS controleert het nieuwe gepinde ZILVER-contextmanifest;
- BRONS genereert de ZILVER-startopdracht met uitsluitend die vastgelegde verwijzingen;
- BRONS stopt.

Hetzelfde geldt voor ZILVER → GOUD.

Dit model levert de meeste tijdwinst.

### Model B — transition blijft apart, maar zonder SUBREGIE

Wanneer rol-/controllerseparatie vereist dat de worker nooit zelf transition uitvoert:

- BRONS voltooit en schrijft een machineleesbare transition request;
- een zeer korte, vaste controllerchat voert uitsluitend de transition uit;
- die controller geeft direct de ZILVER-startopdracht terug;
- geen inhoudelijke SUBREGIE-analyse.

Dit bespaart minder stappen dan Model A maar blijft veel sneller dan de huidige lange tussenregie.

Marks voorkeur is Model A wanneer dit protocoltechnisch veilig kan. INDIA2 moet echter geen bevoegdheden verruimen enkel voor gemak zonder eerst de bestaande invarianten te controleren.

## 16. Waarom dit voorstel waarschijnlijk beter past dan volledige automatisering

- Het verandert niet wie het inhoudelijke onderzoek uitvoert.
- Het vraagt geen server- of n8n-beheer.
- Het vraagt geen Claude Code-worker.
- Het behoudt verse chats per rol.
- Het behoudt GitHub als waarheid.
- Het vermindert Marks handelingen tot kopiëren en plakken tussen drie rollen.
- Het voorkomt lange SUBREGIE-wachttijden.
- Het is binnen één of enkele protocolwijzigingen testbaar.
- Het is passend voor ongeveer tien resterende sweeps.
- Het kan later alsnog verder worden geautomatiseerd zonder de inhoudelijke rolcontracten opnieuw te ontwerpen.

## 17. Risico's die INDIA2 moet beoordelen

1. **Overdrachtstekst loopt achter op GitHub-state**
   - Mitigatie: volgende rol leest state altijd opnieuw uit GitHub.

2. **BRONS schrijft een ZILVER-prompt met teveel inhoudelijke sturing**
   - Mitigatie: canoniek template; alleen role scope, pointers, gates en stopvoorwaarden.

3. **ZILVER krijgt onbedoeld niet-gepinde BRONS-context**
   - Mitigatie: startopdracht noemt uitsluitend het daadwerkelijk gepinde contextmanifest.

4. **Worker voert controllertransition uit zonder bevoegdheid**
   - Mitigatie: INDIA2 stelt eerst het geldende bevoegdheidsmodel vast.

5. **GOUD-rapport wordt te technisch en niet bruikbaar voor Mark**
   - Mitigatie: verplicht managementdeel plus volledige inhoudelijke resultaten en aparte technische audit.

6. **GOUD vat alleen artifacts samen en levert niet de volledige einduitkomst**
   - Mitigatie: expliciet `MARK_FINAL_REPORT` als primair deliverable, niet als korte completionnote.

7. **Een blokkade wordt doorgeschoven naar de volgende rol**
   - Mitigatie: `NEXT_ROLE_READY: YES/NO`; geen prompt bij NO.

8. **De overdracht wordt te lang en kost opnieuw veel tijd**
   - Mitigatie: vaste template; geen kopie van onderzoeksinhoud; alleen noodzakelijke instructies en GitHub-pointers.

## 18. Voorgestelde acceptatiecriteria

De wijziging is geslaagd wanneer een test-run aantoont dat:

1. INDIA2 één complete BRONS-startopdracht kan leveren.
2. BRONS zonder terugkeer naar INDIA2 volledig kan afronden.
3. BRONS een correcte, direct plakbare ZILVER-opdracht levert.
4. ZILVER uitsluitend de juiste gepinde context leest.
5. ZILVER zonder terugkeer naar INDIA2 volledig kan afronden.
6. ZILVER een correcte, direct plakbare GOUD-opdracht levert.
7. GOUD het volledige eindrapport rechtstreeks aan Mark levert.
8. INDIA2 na de start niet nodig was bij een foutloze run.
9. Alle bestaande state-, claim-, bron- en transitioninvarianten intact bleven.
10. Bij een gesimuleerde blocker geen volgende rol onterecht werd gestart.
11. Mark niet meer dan drie inhoudelijke chats hoefde te gebruiken: BRONS, ZILVER en GOUD.
12. De totale menselijke wachttijd tussen fasen aantoonbaar lager was dan bij de oude SUBREGIE-route.

## 19. Concrete vragen aan INDIA2

INDIA2, geef na volledige repositorycontrole antwoord op de volgende punten:

1. Is de hierboven beschreven lineaire keten verenigbaar met de huidige canonieke rol- en controllerprotocollen?
2. Kan BRONS volgens de huidige bevoegdheden zelf de BRONS → ZILVER-controllertransition uitvoeren?
3. Kan ZILVER volgens de huidige bevoegdheden zelf de ZILVER → GOUD-controllertransition uitvoeren?
4. Zo nee: wat is de kleinst mogelijke controllerstap zonder terugkeer naar inhoudelijke SUBREGIE?
5. Welke bestaande bestanden moeten exact worden aangepast?
6. Is een nieuw `ROLE_HANDOFF_PROTOCOL.md` nodig of volstaan kleine wijzigingen in bestaande rolcontracten?
7. Welke informatie moet verplicht in de BRONS → ZILVER-overdracht staan?
8. Welke informatie moet verplicht in de ZILVER → GOUD-overdracht staan?
9. Welke informatie mist nog in de voorgestelde structuur van het GOUD-eindrapport?
10. Hoe garanderen we dat GOUD een volledig inhoudelijk rapport voor Mark oplevert en niet alleen een pipelinecompletion?
11. Welke bestaande invarianten of quality gates dreigen door dit voorstel te worden verzwakt?
12. Zie je een eenvoudiger variant die evenveel tijd bespaart zonder extra risico?
13. Welke delen van PR #14 moeten worden verworpen, behouden of hergebruikt?
14. Is het veilig om de n8n/Claude Code-architectuur volledig als niet-geselecteerd ontwerp te markeren?
15. Welke synthetische test-run adviseer je voordat dit op de resterende sweeps wordt toegepast?

## 20. Gevraagde besluitvormingsvorm

Lever geen vrijblijvende brainstorm. Lever een besluitdocument met:

- `EINDBESLUIT: ACCEPT | ACCEPT_WITH_CHANGES | REJECT`;
- een puntsgewijze beslismatrix voor alle hoofdonderdelen;
- exacte vereiste wijzigingen;
- exacte repositorypaden;
- bevoegdheidsanalyse voor de transitions;
- definitief overdrachtstemplate BRONS → ZILVER;
- definitief overdrachtstemplate ZILVER → GOUD;
- definitief GOUD-eindrapporttemplate voor Mark;
- minimale implementatievolgorde;
- testplan;
- resterende blockers;
- rapportcijfers voor waarheid, uitvoerbaarheid, eenvoud, fouttolerantie en tijdwinst.

Schrijf je review op dezelfde branch of in PR #14 zodat beide partijen vanuit dezelfde repositoryversie werken.

## 21. Voorlopige aanbeveling van ChatGPT aan INDIA2

Mijn voorlopige oordeel is:

- verwerp n8n/Claude Code als huidige productiearchitectuur;
- behoud GitHub als enige duurzame waarheid;
- behoud verse rolcontexten voor BRONS, ZILVER en GOUD;
- maak INDIA2 alleen verantwoordelijk voor de start en uitzonderingen;
- laat BRONS en ZILVER een volledige bedieningshandoff voor de volgende rol leveren;
- laat GOUD een volledig eindrapport rechtstreeks aan Mark leveren;
- verander controllerbevoegdheden alleen wanneer de bestaande protocollen dit veilig toelaten;
- voer eerst één kleine test-run uit;
- merge niets uit PR #14 voordat consensus over deze kleinere route is vastgelegd.

Dit is een voorstel, geen definitieve protocolwijziging. INDIA2 wordt gevraagd dit tegen de daadwerkelijke repository te toetsen, ontbrekende punten aan te vullen en tot een expliciete consensus te komen.
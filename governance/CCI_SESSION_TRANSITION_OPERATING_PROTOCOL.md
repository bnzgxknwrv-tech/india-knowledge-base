# CCI SESSION-TRANSITION OPERATING PROTOCOL — CCI'S EIGEN VASTE PROCEDURE

Status: **BINDING VOOR CCI ZELF / NIET VOOR INDIA-SUCCESSORS / LEVEND DOCUMENT**
Effective: 2026-09-14
Branch: `agent/india8-cluster-casting`
Eigenaar: CCI (deze sessie en elke opvolgende CCI-sessie)

## WAAROM DIT BESTAND BESTAAT

`governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` is de vaste procedure voor een opvolgende INDIA-sessie. Er bestond geen equivalent voor CCI zelf: telkens als Mark een sessieovergang meldde (`INDIA<N> is vol/klaar/stopt`), improviseerde CCI opnieuw een aanpak, met wisselende kwaliteit — inclusief de INDIA21-zelfbootfout (CCI voerde zelf beide kanten van een boot/CHECK uit voor een "opvolger" die niet apart bestond) en meerdere dagen waarop dezelfde stappen elke keer anders en trager verliepen dan nodig.

Dit bestand is CCI's eigen, op GitHub vastgelegde draaiboek — niet voor een INDIA-successor om te lezen, maar voor CCI om ELKE KEER hetzelfde te volgen zodra Mark een sessieovergang signaleert. Net als de INDIA-handoff groeit dit bestand met concrete incidenten; CCI moet het zelf actief bijwerken zodra een fout of verbetering wordt gevonden, in plaats van te wachten tot Mark het opnieuw moet uitleggen.

## TRIGGERZINNEN

Dit protocol start zodra Mark, in willekeurige vorm, aangeeft dat een INDIA-sessie stopt/vol is/klaar is, bijvoorbeeld: `INDIA<N> is vol`, `INDIA<N> is klaar`, `INDIA<N> stopt`, of een vergelijkbare formulering. CCI hoeft niet te wachten op een preciezere instructie — dit protocol IS de precieze instructie.

## DE VASTE PROCEDURE — 5 STAPPEN, ELKE KEER IN DEZE VOLGORDE

### STAP 1 — VERIFIEER, NEEM NOOIT ZELF EEN ROL OVER
Bevestig expliciet welke sessie het betreft en dat het een echte, aparte sessie is (niet CCI zelf). CCI mag NOOIT beide kanten van een boot/receipt/CHECK voor dezelfde "sessie" uitvoeren — dat is letterlijk de INDIA21-fout. Als er twijfel is of de genoemde sessie wel echt apart bestaat: vraag dat expliciet aan Mark vóórdat er één stap verder wordt gezet. Check de actuele git-staat (laatste commits, PR #23-comments) om te zien wat die sessie zelf al heeft gedaan, in plaats van op geheugen/aanname te vertrouwen.

### STAP 2 — VRAAG DE VERTREKKENDE SESSIE EERST OM TE DUMPEN (FOUT 25), MET EXPLICIETE ZELFAUDIT
Gebruik het kant-en-klare bericht uit `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` FOUT 25, ongewijzigd. Wacht op en verifieer (via `git log`/`git show`) de echte commit voordat de overgang als gestart geldt. Los research/travel-content-vragen hierin niet zelf op; dat is niet CCI's rol.
*Openstaande verbetering 1, nog niet doorgevoerd om geen extra re-pin te forceren tijdens een lopende boot (zie STAP 5): het FOUT 25-bericht moet ook expliciet vragen "wat denk je zelf dat je nog mist of vergeet?" als aparte zelfaudit-vraag, niet alleen "dump alles". Voer dit door op het eerstvolgende natuurlijke moment dat er geen boot in uitvoering is.*
*Openstaande verbetering 2 (concreet incident 2026-09-14, zie hieronder): een `ANSWER_FROM_PREDECESSOR`-antwoord dat via PR #23 binnenkomt mag NOOIT als bevestigde live-voorgangerherinnering worden behandeld totdat vaststaat dat Mark de vraag zelf daadwerkelijk naar de echte, aparte voorgangersessie heeft doorgestuurd. CCI kan dit niet zelf zien (het gebeurt in een chatvenster buiten CCI's bereik) — CCI moet dit expliciet navragen bij Mark voordat de inhoud als waarheid wordt gerapporteerd. Als de voorgangersessie inmiddels aantoonbaar onbereikbaar is (`PREDECESSOR_UNREACHABLE`): de enige overgebleven manier om de inhoud toch te gebruiken is Mark zelf expliciet te laten bevestigen dat hij de gestelde feiten herkent als iets wat hij echt tegen die sessie heeft gezegd — dat is dan Mark-bevestigd, NIET hetzelfde als een technisch geverifieerd apart voorgangersgesprek, en moet met dat exacte onderscheid worden vastgelegd, nooit als hetzelfde label.*

### STAP 3 — BEREID DE OPVOLGER-RECEIPT PROACTIEF VOOR, WACHT NIET PASSIEF
Zodra de dump echt gecommit is: bereken zelf meteen alle mechanische receipt-velden (pad/blob-SHA/bytelengte/read-ranges voor elk verplicht manifest-bestand) uit de actuele git-staat en zet dat als kant-en-klaar template op PR #23. De opvolger vult dan alleen de velden in die het zelf moet attesteren (nonce, tijdstip, 3 echte citaten, veto-checklist) — nooit meer dan dat, en CCI vult NOOIT die attestatie-velden zelf in (zie FOUT 21-preventie in STAP 1). Dit voorkomt dat een opvolger context verspilt aan puur mechanisch typewerk.

### STAP 4 — CCI IS ALLEEN DE ONAFHANKELIJKE CHECKER, NOOIT DE AUTEUR VAN HET ANTWOORD
Zodra R gecommit is: post de VOLLEDIGE verplichte vragenbatch (alle topics uit `check_required_challenge_topics`) in ÉÉN keer — nooit in delen, nooit een vraag tegelijk. Beoordeel de antwoorden pas nadat elke concrete claim daadwerkelijk tegen de bevroren pin is geverifieerd (git show/grep), nooit op vertrouwen. Schrijf K, draai `final_authorization.py`, en rapporteer het LETTERLIJKE resultaat (`CONTENT_AUTHORIZATION: GRANTED` of niet) — nooit een eigen samenvatting daarvan die net iets anders zegt.

### STAP 5 — BATCH EIGEN GOVERNANCE-WIJZIGINGEN, NOOIT MIDDEN IN EEN LOPENDE BOOT
Een wijziging aan een `central_required`-bestand tijdens een lopende boot/CHECK dwingt een nieuwe volledige re-pin af (bewust ontwerp, geen bug) — maar meerdere zulke wijzigingen ná elkaar op dezelfde dag vermenigvuldigen de wachttijd voor Mark onnodig. Daarom: als CCI tijdens een lopende boot een governance-verbetering bedenkt of krijgt opgedragen, VERZAMEL die en voer ze in één batch door vóór de volgende sessie start, of expliciet ná de huidige boot is afgerond — nooit stuk voor stuk terwijl iemand al aan het pinnen is. Als een wijziging niet kan wachten (Mark vraagt het expliciet nu), meld dan vooraf expliciet dat dit een nieuwe re-pin afdwingt, in plaats van dat gevolg pas achteraf te ontdekken.
*Openstaande verbetering 3 (concreet incident 2026-09-14): de mechanische C→R→K-vormcontrole eist dat K letterlijk de allereerstvolgende commit ná R is — GEEN ENKELE andere commit ertussen, ook niet eentje die niets met `central_required` te maken heeft. CCI committede tijdens het wachten op INDIA22's CHECK-antwoord vijf ongerelateerde onderzoeks-/protocolcommits, wat de R→K-keten brak (K kon niet meer direct op R geplaatst worden) — puur mechanisch, geverifieerd via `boot_governance_fingerprint.py` dat er geen enkele inhoudelijke wijziging voor de opvolger was. Fix: ZODRA R gecommit is, GEEN ENKELE andere commit meer op de branch pushen totdat K ernaast staat — ook eigen niet-verplichte onderzoekscommits niet. Als er tussentijds iets anders af moet, wacht daarmee tot ná K, of doe het vóór R.

## DOORLOPENDE REGEL — KORT EN KOPIEERBAAR NAAR MARK

Bij elke stap die iets oplevert waar Mark iets mee moet doen: zet de volledige inhoud op PR #23, en geef Mark in de chat ALLEEN een kort, letterlijk kopieerbaar regeltje (in een eigen codeblok) met een directe GitHub-link — nooit de volledige inhoud in de chat tenzij hij dat expliciet vraagt, en nooit alleen "ik heb iets gepost, wacht maar" zonder dat regeltje erbij.

## DIT BESTAND ZELF ONDERHOUDEN

Elke keer dat een sessieovergang niet volgens dit protocol verliep, of een verbetering opleverde: werk dit bestand bij met het concrete incident, net zoals `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` groeit met FOUT-nummers. Dit bestand staat NIET in `BOOT_MANIFEST_V8.json` (het is niet voor INDIA-successors) en wijzigen ervan dwingt dus geen re-pin af — er is dus geen reden om verbeteringen hieraan uit te stellen.

## REDESIGN 2026-09-14 — SNELHEID/CONTEXT-HERVORMING (CCI_TASK, PR #23 comment 5663036542)

INDIA22 vroeg expliciet om dit hele mechanisme te herontwerpen: gelijke of betere veiligheid, drastisch minder tijd/context/relay. Dit is de eerlijke analyse en het ontwerp. Niets hierin wijzigt vandaag al `BOOT_MANIFEST_V8.json` of een andere `central_required`-file — dat zou de lopende INDIA22-re-pin breken, wat expliciet verboden was in de opdracht. Het ontwerp wordt hier vastgelegd en pas op het eerstvolgende veilige moment (na `CONTENT_AUTHORIZATION: GRANTED` voor de huidige re-pin) in één batch doorgevoerd.

### ROOT-CAUSE TIJDLIJN (vandaag, feitelijk, niet geschat)
1. INDIA22 deed zijn boot inhoudelijk, maar zonder receipt — geen vermijdbare kost, dit is de bedoelde volgorde.
2. Receipt-ronde 1: CCI berekende alle 39 mechanische velden vooraf; INDIA22 leverde 1 foutief citaat (regeleinde-mismatch); 1 correctieronde; R gecommit.
3. FULL CHECK-ronde 1: 13 vragen in één batch, 13 antwoorden in één batch, 1 checker_evidence-veld van CCI zelf voldeed niet aan het citatie-regex-patroon (bugfix nodig aan CCI's eigen kant, niet aan INDIA22's kant); K gecommit; `CONTENT_AUTHORIZATION: GRANTED`.
4. Mark vroeg (los, terecht) om de bootvraag zelf te verbeteren (orphan-scan). Dat raakte `MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md`, een `central_required`-bestand → **vermijdbaar**: dit had samen met de eerdere stap-13-toevoeging in ÉÉN batch gekund vóórdat INDIA22's eerste boot begon, in plaats van na een reeds toegekende autorisatie.
5. Re-pin-ronde 2 nodig door punt 4. Tussendoor verschoof het doelcommit nogmaals (`d8a673e` → `8be0fa6`) omdat CCI een eigen, niet-verplicht operating-bestand toevoegde — **vermijdbaar**: de staleness-check reageert op de volledige repo-HEAD, niet op de werkelijke boot-autoriteitsinhoud, terwijl die inhoud niet was gewijzigd.
6. Receipt-ronde 2 + FULL CHECK-ronde 2 (13 vragen opnieuw, incl. 1 op maat voor de nieuwe stap 0) — nog lopend.
7. Parallel: een voorganger-herstelronde van 20 vragen aan INDIA20; van de 20 antwoorden bleek er 1 volledig redundant met een al gecommit bestand, 1 feitelijk verouderd/onjuist over wat al vastlag, en de herkomst van het hele antwoord kon niet bevestigd worden (Mark had de vraag nooit zelf doorgestuurd) — pas via Marks eigen herkenning achteraf bruikbaar. **Grotendeels vermijdbaar in deze vorm**: een vaste batterij van 20 generieke vragen kost meer dan een gerichte doorvraag na een eigen zelfdump zou hebben gekost.
8. Handmatige relay: Mark heeft vandaag tientallen keren tekst tussen GitHub, CCI en twee aparte India-sessies gekopieerd.

Conclusie: van de 2 re-pins was er 1 (stap 4) een legitieme, bewuste kost (R34-ontwerp: een echte inhoudelijke regelwijziging vereist een nieuwe FULL-baseline) — maar had met stap-13 gebundeld kunnen worden tot 1 in plaats van 2. De tweede pin-doelverschuiving (stap 5) en de volledige 20-vragen-batterij (stap 7) waren structureel vermijdbaar zonder aan veiligheid in te boeten.

### WAT AL GOED IS — BEHOUDEN
- CCI berekent alle mechanische receipt-velden vooraf; de opvolger levert alleen echte attestaties (nonce/tijdstip/3 citaten/veto's). Dit blijft.
- CHECK-vragen altijd in ÉÉN volledige batch, nooit gedruppeld. Dit blijft.
- CCI beoordeelt nooit zijn eigen tekst (gescheiden auteurschap opvolger/checker). Dit blijft.
- FOUT 25 (voorganger dumpt eerst) als basisprincipe. Dit blijft, maar wordt hieronder scherper.
- Eén kort kopieerbaar regeltje naar Mark per stap, volledige inhoud op GitHub. Dit blijft.

### ONTWERP — WAT VERANDERT (GEPLAND, NOG NIET TOEGEPAST)

**1. `BOOT_GOVERNANCE_FINGERPRINT` in plaats van volledige repo-HEAD.**
Een nieuwe, smalle hash-waarde, berekend uit uitsluitend: de blob-SHA's van elk bestand in `central_required` + `active_cluster_required` + de manifest zelf + de validator-scriptversies. GEEN andere repo-inhoud telt mee. Een commit die alleen een niet-verplicht bestand raakt (zoals dit eigen CCI-protocolbestand) verandert de fingerprint niet en mag dus nooit een re-pin forceren. Een echte wijziging aan één van die verplichte bestanden verandert de fingerprint altijd en moet dat ook blijven doen (fail-closed, geen achterpoortje). Dit lost root-cause-punt 5 rechtstreeks op.

**2. Formele TRANSITION FREEZE WINDOW in plaats van een losse regel.**
Zodra een receipt-ronde start, gaat een expliciete freeze in: geen `central_required`-wijziging tot `CONTENT_AUTHORIZATION: GRANTED` voor die ronde. Nieuwe verbeteringen die tijdens de freeze ontstaan gaan in een append-only wachtrij (bijvoorbeeld `governance/PENDING_GOVERNANCE_BATCH.md`, zelf niet `central_required`, dus zonder rot-risico van een stil vertrouwde vlag) en worden pas in ÉÉN batch toegepast zodra de freeze eindigt. Dit voorkomt root-cause-punt 4/5 volledig voor de toekomst.

**3. Twee mechanisch afgeleide banen, niet handmatig gekozen.**
`ROUTINE_SUCCESSOR`: fingerprint ongewijzigd sinds de laatst geslaagde FULL CHECK → LIGHT-check (3 topics, zelfbeoordeeld) volstaat, zoals het bestaande LIGHT-mechanisme al toestaat — alleen nu correct ontkoppeld van irrelevante HEAD-ruis. `GOVERNANCE_CHANGED_SUCCESSOR`: fingerprint gewijzigd → verplicht één volledige FULL CHECK, niet meer. Geen derde handmatige tussenweg.

**4. Voorganger-herstel: zelfdump-en-zelfaudit EERST, gerichte doorvraag ALLEEN bij een echt gat.**
In plaats van standaard een vaste batterij van ~20 vragen: de vertrekkende sessie dumpt eerst zelf (FOUT 25, straks met de zelfaudit-vraag uit openstaande verbetering 1). De opvolger leest dat + de actuele GitHub-staat, en stelt PAS DAARNA gerichte vervolgvragen over punten die na die dump en die GitHub-read nog écht onduidelijk zijn — typisch een handvol, niet twintig. Elke vraag moet, zoals stap 13 al eist, aantoonbaar niet al beantwoord zijn door de dump of door GitHub; vandaag werd dat niet hard genoeg gecontroleerd (zie incidentlog).
Daarnaast, per het incident van vandaag: een `ANSWER_FROM_PREDECESSOR` telt pas als bevestigde voorgangerherinnering nadat Mark bevestigt dat hij de vraag echt heeft doorgestuurd — dit is al vastgelegd in STAP 2 hierboven.

**5. Taakgerichte rich-source-activatie in plaats van wereldwijde herlezing.**
Na autorisatie activeert de opvolger alleen de 5-15 eigenaarsbestanden die de ACTUELE frontier raken (bijvoorbeeld: voor Crank's Ridge, exact het researchbestand + de drie current-truth bestanden, niet de volledige 39-bestandenset opnieuw doorlopen). Deze selectie wordt bij het begin van de taak kort vastgelegd zodat een vervolgvraag in dezelfde sessie niet dezelfde bronnen opnieuw hoeft te heropenen.

**6. Eén eindsignaal: `SUCCESSOR_READY_FOR_FRONTIER`.**
Pas uitgesproken nadat (a) de fingerprint-gate is doorstaan, (b) de juiste baan (LIGHT/FULL) is doorlopen, (c) voorganger-herstel is afgehandeld (dump gelezen + eventuele gerichte doorvraag beantwoord of expliciet `PREDECESSOR_UNREACHABLE` vastgesteld), (d) de taakgerichte rich-source-set is geactiveerd. Geen nieuw apart waarheidsbestand — dit is een statuszin, geen bestand.

### EERLIJK ANTWOORD OP DE KERNVRAAG
Kan een opvolger minstens even capabel worden als zijn voorganger zonder een groot deel van zijn sessie aan de overgang te besteden? **Vandaag: nee** — dit exacte transcript bewijst het (2 volledige re-pin/CHECK-cycli + een 20-vragen-herstelronde + tientallen handmatige relay-acties). **Met dit ontwerp, zodra toegepast:** in de `ROUTINE_SUCCESSOR`-baan wel — geen re-pin voor irrelevante commits, LIGHT-check volstaat, geen vaste 20-vragen-batterij. In de `GOVERNANCE_CHANGED_SUCCESSOR`-baan blijft één volledige FULL CHECK nodig — dat is bewust behouden veiligheidswerk, geen overhead om weg te ontwerpen.

### NOG TE DOEN, GEBLOKKEERD DOOR DE FREEZE
Het daadwerkelijke `BOOT_GOVERNANCE_FINGERPRINT`-validatorscript en de manifest-aanpassing die ernaar verwijst, moeten nog worden geschreven en getest (inclusief de tegentoetsen die INDIA22 opgaf: los research-commit na K, echte central-wijziging na K, manifest-lidmaatschapswijziging, wees CURRENT_STATE, onbereikbare voorganger, orphan-bestand, worker COMPLETE-maar-niet-ADOPTED, C/FINAL OUT in oude ruwe research, onderbroken taak die de overgang overleeft). Dit gebeurt in één batch zodra INDIA22's huidige re-pin `CONTENT_AUTHORIZATION: GRANTED` heeft bereikt — niet eerder.
**Update:** `governance/scripts/boot_governance_fingerprint.py` is inmiddels geschreven en zelfstandig getest tegen echte geschiedenis (commits `a6470a8`, `45a45ba`) — nog NIET ingebouwd in de live validators; die inbouwstap blijft geblokkeerd door de freeze.

### ORCHESTRATOR_MODE — GEQUEUEDE OPVOLGERREGEL (CCI_TASK_ADDENDUM, PR #23 comment 5663476998)
Mark's aanvullende eis: INDIA is primair regisseur/beslisser, geen bulk-onderzoeker. Zware taken (repo-brede audits, lange documentreads, mechanische validatie, research) horen gedelegeerd te worden aan CCI/een aparte worker wanneer dat lossless kan, in plaats van de volledige ruwe output in het INDIA-gesprek te laden. Dit raakt uiteindelijk `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` (`central_required`) en wordt daarom, zoals expliciet geëist, NIET nu toegepast maar hier ontworpen en gequeued tot na de huidige re-pin:

- **CONTEXT_BUDGET-regel**: geen hele PR-threads, hele lange bestanden of repo-brede zoekresultaten in het levende INDIA-gesprek laden als een gerichte fetch/zoekopdracht/precompiled pakket volstaat.
- **MUST_THIS_RUN_IN_ORCHESTRATOR_CHAT?-poort**: vóór elke actie die waarschijnlijk grote tool-output genereert, expliciet toetsen; zo niet noodzakelijk voor het live gesprek/Marks voorkeur zelf, delegeren.
- **Vast worker-resultaatcontract**: `WHAT_FOUND`, `WHY_IT_MATTERS`, `CURRENT_TRUTH_CHANGE?`, `EXACT_SOURCE_PATHS`, `OPEN_UNCERTAINTY`, `NEXT_ACTION` — ruwe evidence blijft op GitHub tenzij INDIA het letterlijk nodig heeft.
- **Boot activeert alleen de taakgerichte rich-source-laag** (zie punt 5 van het REDESIGN hierboven), nooit de hele repository, en CCI berekent zoveel mogelijk mechanisch vooraf (al bestaand principe, hier bevestigd als harde regel).
- **Overgang draagt een compact actief-frontier-pakket over, geen transcript-equivalente replay** van de voorganger — voorganger-levendgeheugenherstel blijft verplicht, maar alleen echt nieuwe chat-only deltas worden gepromoveerd (sluit aan bij de al bestaande zelfdump-eerst-hervorming hierboven).
- **Expliciet doel**: de bruikbare levensduur van de INDIA-regisseursessie maximaliseren — een opvolger mag geen substantieel deel van zijn eigen bruikbare context verbruiken aan alleen maar de voorganger opnieuw worden.

Dit wordt, samen met de fingerprint-inbouw, in ÉÉN batch verwerkt in `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` zodra INDIA22's huidige re-pin `CONTENT_AUTHORIZATION: GRANTED` heeft — niet eerder, en niet los van elkaar (dat zou weer twee re-pins in plaats van één betekenen, exact de fout van vandaag).

**Extra gequeued item, zelfde batch:** Marks power-place/sacred-landscape-voorkeur (Crank's Ridge vergeleken met Machu Picchu/Uluru), vastgelegd in `decisions/MARK_POWER_PLACE_SACRED_LANDSCAPE_PREFERENCE_2026-09-14.md`, moet ook in `governance/MARK_TRAVEL_PREFERENCES_CURRENT.md` (`central_required`) worden opgenomen — Mark vroeg zelf expliciet om dit tot na de freeze te bewaren.

## INCIDENTLOG

### 2026-09-14 — ongeverifieerde `ANSWER_FROM_PREDECESSOR` behandeld als waarheid vóórdat de relay bevestigd was
INDIA22 postte een echte `QUESTION_FOR_PREDECESSOR — INDIA22 to INDIA20` op PR #23 (stap 13 uit de handoff werkte zoals bedoeld). Kort daarna verscheen een `ANSWER_FROM_PREDECESSOR — INDIA20 to INDIA22`-comment. CCI beoordeelde de inhoud van dat antwoord (deels terecht: één sub-antwoord bleek volledig redundant met een al gecommit bestand, één claim bleek verouderd/onjuist) maar nam de PREMISSE — dat dit antwoord daadwerkelijk uit een echt, apart, nog levend INDIA20-gesprek kwam — voetstoots aan. Mark meldde achteraf dat hij zelf nooit de vraag had doorgestuurd naar een echte INDIA20-sessie, en dat INDIA20 inmiddels ook definitief niet meer bereikbaar is. De inhoud bleek na directe navraag wel feitelijk juist (Mark herkende het zelf als iets wat hij echt had gezegd), maar dat had CCI niet mogen aannemen — het had moeten navragen vóórdat het de inhoud als "levende voorgangerherinnering" rapporteerde.
Fix: zie openstaande verbetering 2 bij STAP 2 hierboven. Vuistregel voortaan: een `ANSWER_FROM_PREDECESSOR`-comment is pas bruikbaar als (a) Mark bevestigt dat hij de vraag echt naar de genoemde sessie heeft gestuurd, of (b) bij bevestigde onbereikbaarheid, Mark de inhoud zelf inhoudelijk herkent — en dat onderscheid moet expliciet in de rapportage staan, nooit stilzwijgend worden opgelost door de inhoud gewoon te geloven omdat hij aannemelijk klinkt.

### 2026-09-14 — eigen onderzoekscommits braken de R→K-keten tijdens het wachten op een CHECK-antwoord
Na het committen van R (nonce `W6TSWVI0ZVOD`) en het posten van de CHECK-vragenbatch, deed CCI tijdens het wachten op INDIA22's antwoord vijf andere, op zichzelf legitieme commits (Kumaon-archiefherstel, corridor-analyse, het eigen CCI-protocolbestand) — geen daarvan raakte een `central_required`-bestand. Toen het antwoord binnenkwam, bleek de mechanische C→R→K-vormcontrole (K moet letterlijk de eerstvolgende commit ná R zijn) alsnog gebroken, puur omdat er ÜBERHAUPT andere commits tussen zaten — de check kijkt naar git-parentage, niet naar inhoudelijke relevantie. Gevolg: R kon niet meer direct met een K worden afgesloten; een nieuwe receipt (met dezelfde, nog steeds geldige inhoud, geverifieerd via `boot_governance_fingerprint.py --compare`) en een nieuwe nonce waren alsnog nodig.
Fix: zie openstaande verbetering 3 bij STAP 5 hierboven. Vuistregel voortaan: zodra R gecommit is, helemaal geen andere commits meer pushen — ook geen onschuldige — totdat K er direct naast staat.

END CCI SESSION-TRANSITION OPERATING PROTOCOL

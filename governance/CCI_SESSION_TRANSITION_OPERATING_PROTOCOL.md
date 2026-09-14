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

## DOORLOPENDE REGEL — KORT EN KOPIEERBAAR NAAR MARK

Bij elke stap die iets oplevert waar Mark iets mee moet doen: zet de volledige inhoud op PR #23, en geef Mark in de chat ALLEEN een kort, letterlijk kopieerbaar regeltje (in een eigen codeblok) met een directe GitHub-link — nooit de volledige inhoud in de chat tenzij hij dat expliciet vraagt, en nooit alleen "ik heb iets gepost, wacht maar" zonder dat regeltje erbij.

## DIT BESTAND ZELF ONDERHOUDEN

Elke keer dat een sessieovergang niet volgens dit protocol verliep, of een verbetering opleverde: werk dit bestand bij met het concrete incident, net zoals `governance/MARK_TO_INDIA_SUCCESSOR_HUMAN_HANDOFF.md` groeit met FOUT-nummers. Dit bestand staat NIET in `BOOT_MANIFEST_V8.json` (het is niet voor INDIA-successors) en wijzigen ervan dwingt dus geen re-pin af — er is dus geen reden om verbeteringen hieraan uit te stellen.

## INCIDENTLOG

### 2026-09-14 — ongeverifieerde `ANSWER_FROM_PREDECESSOR` behandeld als waarheid vóórdat de relay bevestigd was
INDIA22 postte een echte `QUESTION_FOR_PREDECESSOR — INDIA22 to INDIA20` op PR #23 (stap 13 uit de handoff werkte zoals bedoeld). Kort daarna verscheen een `ANSWER_FROM_PREDECESSOR — INDIA20 to INDIA22`-comment. CCI beoordeelde de inhoud van dat antwoord (deels terecht: één sub-antwoord bleek volledig redundant met een al gecommit bestand, één claim bleek verouderd/onjuist) maar nam de PREMISSE — dat dit antwoord daadwerkelijk uit een echt, apart, nog levend INDIA20-gesprek kwam — voetstoots aan. Mark meldde achteraf dat hij zelf nooit de vraag had doorgestuurd naar een echte INDIA20-sessie, en dat INDIA20 inmiddels ook definitief niet meer bereikbaar is. De inhoud bleek na directe navraag wel feitelijk juist (Mark herkende het zelf als iets wat hij echt had gezegd), maar dat had CCI niet mogen aannemen — het had moeten navragen vóórdat het de inhoud als "levende voorgangerherinnering" rapporteerde.
Fix: zie openstaande verbetering 2 bij STAP 2 hierboven. Vuistregel voortaan: een `ANSWER_FROM_PREDECESSOR`-comment is pas bruikbaar als (a) Mark bevestigt dat hij de vraag echt naar de genoemde sessie heeft gestuurd, of (b) bij bevestigde onbereikbaarheid, Mark de inhoud zelf inhoudelijk herkent — en dat onderscheid moet expliciet in de rapportage staan, nooit stilzwijgend worden opgelost door de inhoud gewoon te geloven omdat hij aannemelijk klinkt.

END CCI SESSION-TRANSITION OPERATING PROTOCOL

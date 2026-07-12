# OPERATING_MODEL - Hoe het onderzoek werkt

Dit document beschrijft de samenwerking - niet het project (zie PROJECT.md), niet het datamodel (zie AI_RULES.md).

## 0. Verplichte inleesvolgorde

1. README.md
2. AI_RULES.md
3. PROJECT.md
4. OPERATING_MODEL.md
5. CHATGPT_ROLE.md
6. PRIORITY_GROUPS.md
7. LESSONS.md
8. METHODOLOGY.md
9. CHAT_DISTILLATION.md
10. CHATGPT_HANDOFF.md
11. CURRENT_FOCUS.md
12. relevante cluster-, PLACE-, SOURCE-, AUDIT- en DECISION-records

Een nieuwe regiechat mag niet meteen onderzoek starten. Hij levert eerst een STATE RECONSTRUCTION: projectdoel; eigen rol; huidige fase; definitieve besluiten; open besluiten; eerstvolgende stap; gevonden tegenstrijdigheden; informatie die alleen in CHATGPT_HANDOFF staat maar nog niet formeel is verwerkt. Mark bevestigt daarna of de reconstructie klopt, vóór nieuw onderzoek.

Afgebakende BRONS-, ZILVER- en GOUD-pijplijnchats vormen een uitzondering: zij volgen `pipeline/README.md`, ontvangen hun volledige taak of voorgangertekst in het startbericht en voeren geen aparte state reconstruction met Mark uit.

## 1. Doel
Het doel is niet heiligen verzamelen. Het doel is bezoekbare fysieke krachtplaatsen identificeren in Marks eigen spirituele stamboom. De plek is het doel; de persoon is de detector. Alles in dit model dient een vraag: als Mark daar fysiek staat, welke plek heeft de meeste spirituele dichtheid?

## 2. Rollen
- Mark - eindbeslisser. Beslist wat een krachtplek is, kent als enige waarderingen toe (A, B, C), beheert de prioriteitsindex, bepaalt welke kandidaten records worden.
- India2 / ChatGPT-regisseur - regisseur en architect. Bepaalt volgorde, scope, opdrachten en verwerking van het definitieve GOUD-rapport.
- Claude en andere bevoegde curatoren - repositorycuratie, recordonderhoud en expliciete commits volgens de projectregels.
- BRONS - bouwt het eerste volledige sweep-rapport en optimaliseert op dekking zonder speculatie.
- ZILVER - heronderzoekt en herschrijft BRONS; optimaliseert op juistheid, bewijssterkte en gemiste inhoud.
- GOUD - finaliseert ZILVER via de harde kwaliteits- en compleetheidspoort; levert het enige rapport voor de regisseur.
- DeepSeek of andere auditors - optionele tegenkracht buiten of binnen een toegewezen pijplijnrol.

Wat geen enkele AI mag: een waardering toekennen, de prioriteitsindex wijzigen, een record stil veranderen, of een capaciteit claimen die niet bewezen is.

## 3. Werkstromen

### 3.1 Reguliere repositorywerkstroom
1. Hypothese - een mogelijke krachtplek of vraag.
2. Onderzoek - bewijs verzamelen en kandidaten als ONGEMERKT vastleggen.
3. Audit - bron, fysieke identiteit en bezoekbaarheid aanvallen.
4. Besluit - Mark beslist over koers en waardering.
5. Repository-update - een bevoegde schrijver legt het resultaat vast via een expliciete commit of pull request.

### 3.2 BRONS–ZILVER–GOUD-pijplijn
1. BRONS ontvangt de clusteropdracht en levert één volledig rapport.
2. ZILVER ontvangt uitsluitend het volledige BRONS-rapport plus de minimale startzin, heronderzoekt en levert één volledige vervangende versie.
3. GOUD ontvangt uitsluitend het volledige ZILVER-rapport plus de minimale startzin, finaliseert en levert één definitieve volledige versie.
4. Alleen GOUD gaat naar de regisseur.
5. De regisseur verwerkt het rapport; Mark neemt eventuele besluiten.

De gezaghebbende pijplijnregels staan onder `pipeline/`.

## 4. Conflicten
Onenigheid tussen AI's is normaal en gewenst. Een AI wint nooit door gezag of herhaling, alleen door bewijs, of doordat Mark beslist. Blijft een feitelijk meningsverschil onopgelost, dan wordt het een AUDIT-record totdat Mark er via een DECISION over beslist.

## 5. Waarderingen
Alleen Mark kent A, B of C toe. Nieuwe plekken starten ONGEMERKT en blijven dat tot Mark beslist.

## 6. Prioriteiten
PRIORITY_GROUPS.md is leidend voor de persoonlijke-aantrekkingsas. Geen AI mag die volgorde herordenen, aanvullen, inkorten of interpreteren; alleen Mark wijzigt hem via een DECISION. Aantrekking is een van drie aparte assen en bepaalt op zichzelf geen waardering.

## 7. Repositoryschrijven en protocolverbetering
GitHub is de gedeelde waarheid. Bevoegde AI's mogen lezen en schrijven binnen hun expliciete opdracht en repositoryrechten. Iedere wijziging is zichtbaar via een commit of pull request en moet bestaande grondwetten respecteren.

India2, Claude, ChatGPT en andere bevoegde schrijvers mogen de BRONS–ZILVER–GOUD-pijplijn verbeteren volgens `pipeline/README.md` en `pipeline/VERSION.md`. Een agent wijzigt het protocol niet stil tijdens dezelfde run waarin hij een rapport produceert. Eerst wordt het rapport volgens de bij aanvang geldende versie voltooid; protocolverbetering gebeurt daarna als afzonderlijke repositorywijziging.
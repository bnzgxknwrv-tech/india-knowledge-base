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

Een nieuwe chat mag niet meteen onderzoek starten. Hij levert eerst een STATE RECONSTRUCTION: projectdoel; eigen rol; huidige fase; definitieve besluiten; open besluiten; eerstvolgende stap; gevonden tegenstrijdigheden; informatie die alleen in CHATGPT_HANDOFF staat maar nog niet formeel is verwerkt. Mark bevestigt daarna of de reconstructie klopt, vóór nieuw onderzoek.

## 1. Doel
Het doel is niet heiligen verzamelen. Het doel is bezoekbare fysieke krachtplaatsen identificeren in Marks eigen spirituele stamboom. De plek is het doel; de persoon is de detector. Alles in dit model dient een vraag: als Mark daar fysiek staat, welke plek heeft de meeste spirituele dichtheid?

## 2. Rollen
- Mark - eindbeslisser. Beslist wat een krachtplek is, kent als enige waarderingen toe (A+, A, B, C, R), beheert de prioriteitsindex, bepaalt welke kandidaten records worden.
- Claude - curator en schrijver. Leest en schrijft in de repository, verzamelt kandidaat-plekken, levert bewijs en onderbouwing, onderhoudt de records.
- ChatGPT - regisseur en architect. Bepaalt de volgorde van werk, structureert, bewaakt scope, formuleert opdrachten.
- DeepSeek - auditor en tegenkracht. Schiet gaten, levert tegenargumenten, bron- en architectuurkritiek. Leest de publieke repository.

Wat geen enkele AI mag: een waardering toekennen, de prioriteitsindex wijzigen, een record stil veranderen, of een capaciteit claimen die niet bewezen is.

## 3. Werkstroom
1. Hypothese - een mogelijke krachtplek of vraag (van Mark, ChatGPT of Claude).
2. Onderzoek - Claude verzamelt bewijs en legt kandidaten vast als ONGEMERKT, met SOURCE-onderbouwing.
3. Audit - DeepSeek en ChatGPT vallen het aan: klopt de plek, klopt de bron, haalt het de bezoekbaarheidspoort?
4. Besluit - Mark beslist: wel of geen record, en later de waardering. Vastgelegd als DECISION wanneer het een waardering of koerswijziging betreft.
5. Repository-update - Claude schrijft het resultaat weg via een expliciete commit.

## 4. Conflicten
Onenigheid tussen AI's is normaal en gewenst; DeepSeek hoort het oneens te zijn. Kritiek leidt niet automatisch tot wijziging - Claude weegt haar. Een AI wint nooit door gezag of herhaling, alleen door bewijs, of doordat Mark beslist. Blijft een feitelijk meningsverschil onopgelost, dan wordt het een AUDIT-record (beide posities vastgelegd, open gelaten) totdat Mark er via een DECISION over beslist.

## 5. Waarderingen
Alleen Mark kent A+, A, B, C of R toe. Een AI doet dat nooit, ook niet impliciet. Nieuwe plekken starten ONGEMERKT en blijven dat tot Mark beslist.

## 6. Prioriteiten
PRIORITY_GROUPS.md is leidend voor de persoonlijke-aantrekkingsas. Geen AI mag die volgorde herordenen, aanvullen, inkorten of interpreteren; alleen Mark wijzigt hem via een DECISION. Aantrekking is een van drie aparte assen (krachtveld-gewicht, persoonlijke aantrekking, route-prioriteit) en bepaalt op zichzelf geen waardering.

## 7. Samenwerking
GitHub is de gedeelde waarheid. Er bestaat geen directe AI-naar-AI-uitwisseling; iedere AI werkt via de repository. Wat geschreven wordt loopt via Claude, de enige bewezen schrijver, met Mark als beslisser.

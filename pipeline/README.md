# BRONS–ZILVER–GOUD-pijplijn

## Doel
Eén rapport wordt in drie opeenvolgende, schone chats opgebouwd. Er ontstaan geen drie concurrerende rapporten.

1. **BRONS** bouwt het eerste volledige onderzoeksrapport.
2. **ZILVER** controleert, heronderzoekt en herschrijft BRONS tot een aantoonbaar betere volledige versie.
3. **GOUD** voert de laatste inhoudelijke en structurele kwaliteitscontrole uit en levert het enige rapport dat naar de regisseur gaat.

Elke rol ontvangt uitsluitend:
- een korte startzin;
- de volledige tekst van de voorganger, behalve BRONS, dat de clusteropdracht ontvangt.

Alle duurzame instructies staan in deze repository. Chatprompts bevatten geen gekopieerde protocollen.

## Verplichte inleesvolgorde voor iedere rol
1. `README.md`
2. `AI_RULES.md`
3. `pipeline/PIPELINE_CONTRACT.md`
4. het eigen rolbestand in `pipeline/roles/`
5. `pipeline/QUALITY_GATE.md`
6. `CURRENT_FOCUS.md`
7. relevante project-, cluster- en recordbestanden

De rol gebruikt de versie die bij aanvang van de run op de standaardbranch staat. Een rol wijzigt het protocol niet tijdens dezelfde rapportproductie.

## Enig overdrachtsobject
Iedere stap levert één volledige vervangende rapporttekst. Geen annotaties, verschillenlijst, adviesmemo of losse correcties naast het rapport.

## Doorontwikkeling
India2, Claude, ChatGPT en andere bevoegde schrijvers mogen deze pijplijn verbeteren via een expliciete commit of pull request. Iedere wijziging moet:
- een concrete waargenomen fout of kwaliteitswinst benoemen;
- alle drie rollen op onderlinge consistentie controleren;
- `pipeline/VERSION.md` bijwerken;
- bestaande projectgrondwetten respecteren;
- nooit een A/B/C-waardering aan een kunstmatig intelligentiesysteem delegeren.

Mark blijft eindbeslisser. GOUD finaliseert onderzoek, maar neemt geen reis- of waarderingsbesluit.
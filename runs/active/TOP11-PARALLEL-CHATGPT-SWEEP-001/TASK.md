# TOP11-PARALLEL-CHATGPT-SWEEP-001

Doel: één onafhankelijke ChatGPT-onderzoekschat laat parallel landelijke fysieke-locatiesweeps uitvoeren voor de door Mark als deep-sweepwaardig aangemerkte personen/lijnen, als externe detectorlaag naast CCI.

## PERSONEN
1. Paramahansa Yogananda
2. Mahavatar Babaji
3. Lahiri Mahasaya
4. Sri Yukteswar
5. Neem Karoli Baba
6. Ram Dass
7. Ramana Maharshi
8. Ramakrishna

Vivekananda en Hariharananda zijn expliciet NIET in scope voor exhaustieve sweeps; zij krijgen later alleen major-site audits.

## ONAFHANKELIJKHEID — HARD
Dit is een externe/adversarial sweep. Tijdens discovery mag de onderzoeks-chat GEEN bestaande interne kandidatenlijsten, CCI-atlassen, eerdere persoonsresultaten, externe union-resultaten of regionale selectie-output uit deze repository lezen.

Toegestaan vóór de freeze:
- uitsluitend dit TASK-bestand;
- openbare externe bronnen op internet;
- eigen onafhankelijke bronanalyse.

Niet toegestaan vóór de freeze:
- root README / governance die naar interne resultaten leidt;
- bestaande person-centric atlasbestanden;
- Yogananda PR #24 atlas;
- CCI 084–087 output;
- METHOD_V1 kandidaten;
- eerdere Anandamayi union;
- cluster-/A/B/C-besluiten als bron voor kandidaten.

Per persoon eerst de eigen ruwe atlas volledig afronden en als PRE-COMPARE FREEZE naar GitHub schrijven. Pas nadat ALLE acht persoonsfreezes zijn geschreven, mag een latere aparte reconciliatietaak de reporesultaten vergelijken.

## PARALLEL WERKEN
Gebruik waar beschikbaar onafhankelijke subagents/workers, minimaal één primaire worker per persoon. Werk de acht personen parallel, niet sequentieel. Subagents mogen tijdens discovery elkaars kandidaten niet gebruiken.

Binnen iedere persoon mag verder parallel worden opgesplitst in:
- primaire/lineage corpus;
- biografie/memoires/brieven;
- host/gastheer/netwerk;
- reisroutes/chronologie;
- privéhuizen, ashrams, tempels, zalen, hotels, stations, landgoederen;
- foto/archief-identificatie;
- adversarial miss-finder.

## RECALL-DOEL
Vind iedere verifieerbare fysieke locatie in India waar de persoon aantoonbaar persoonlijk aanwezig was of die als directe, concrete levens-/lineage-locatie relevant is. Bewaar kleine touchpoints; geen toeristische selectie.

Per locatie minimaal:
- fysieke locatienaam;
- stad/dorp + staat;
- type;
- wat de persoon daar deed;
- datum/periode;
- PERSONALLY_PRESENT: JA / ONZEKER / NEE;
- PHYSICAL_IDENTITY: EXACT / DEELS / ALLEEN_PLAATS / ONBEKEND;
- host/gastheer/netwerkpersoon indien relevant;
- primaire/semi-primaire bron + locator waar mogelijk;
- secundaire steun;
- historisch versus huidig gebouw indien bekend;
- onzekerheden/conflicten;
- unresolved lead indien fysieke identiteit nog te achterhalen lijkt.

## HARD REGELS
- Vermelding van een plaats in een boek is geen bewijs van persoonlijke aanwezigheid.
- Biografische locatie van iemand anders is geen locatie van de onderzochte persoon.
- Later instituut/ashram is geen bewijs dat de persoon daar zelf was.
- Geen adressen of coördinaten raden.
- Stad en concreet gebouw zijn verschillende granulariteitsniveaus.
- Verschillende fysieke sublocaties op één terrein apart bewaren als de bron dat ondersteunt.
- Twijfel behouden maar expliciet markeren.
- Negatieve bevindingen bewaren wanneer bekende claims na controle niet blijken te kloppen.
- Geen A/B/C, geen routeadvies, geen clusterkeuze.

## OUTPUTBRANCH EN PADEN
Schrijf uitsluitend naar de aparte branch:
`agent/chatgpt-top11-parallel-sweep`

Niet naar de actieve CCI-werkbranch, zodat CCI en ChatGPT echt parallel zonder write-conflicten kunnen werken.

Onder:
`runs/active/TOP11-PARALLEL-CHATGPT-SWEEP-001/`

Bestanden:
- `YOGANANDA_PRE_COMPARE_FREEZE.md`
- `BABAJI_PRE_COMPARE_FREEZE.md`
- `LAHIRI_MAHASAYA_PRE_COMPARE_FREEZE.md`
- `SRI_YUKTESWAR_PRE_COMPARE_FREEZE.md`
- `NEEM_KAROLI_BABA_PRE_COMPARE_FREEZE.md`
- `RAM_DASS_PRE_COMPARE_FREEZE.md`
- `RAMANA_MAHARSHI_PRE_COMPARE_FREEZE.md`
- `RAMAKRISHNA_PRE_COMPARE_FREEZE.md`
- `STATUS.md`

Commit per persoon zodra die persoonsfreeze klaar is. Wacht niet tot alle acht klaar zijn om duurzaam op te slaan.

## STATUS
STATUS.md bevat per persoon:
- state;
- aantal genormaliseerde masterlocaties;
- aantal EXACT/DEELS/ALLEEN_PLAATS/ONBEKEND;
- belangrijkste corpusfamilies onderzocht;
- belangrijkste blocked/unavailable bronnen;
- SATURATION: JA/NEE + waarom;
- freeze commit SHA.

## STOPVOORWAARDE
Na alle acht onafhankelijke freezes:
- schrijf eindstatus;
- vergelijk NIET met CCI/interne atlas;
- merge niets;
- maak geen A/B/C;
- stop en meld alleen welke freezes klaar zijn, counts en commit-SHA's.

De reconciliatie met CCI gebeurt later door INDIA/een aparte taak.
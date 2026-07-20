# Scope — VARANASI-COMPLETE-001

## Centrale opdracht
Voer één volledige, brede Varanasi/Kashi-clustersweep uit en lever tegelijkertijd één complete, eenvoudig te onderhouden India-KML met alle formele A- en B-locaties die op het moment van de GOUD-release in de repository gelden.

## Geografische begrenzing
Onderzoek Varanasi/Kashi inclusief de stedelijke ghats, relevante historische woonhuizen, samadhi's, ashrams, tempels, lineageplaatsen en Sarnath wanneer die inhoudelijk tot het bezoekcluster behoort. Plaatsen buiten deze functionele Varanasi-corridor worden alleen als detector of vergelijking genoemd en niet als nieuwe clustersweep onderzocht.

## Bestaande formele A-ankers in Varanasi
- Lahiri Mahasaya Samadhi
- Lahiri-huis
- Manikarnika Ghat
- Trailanga Swami-samadhi
- Anandamayi Ma Ashram
- Sarnath
- Kashi Vishwanath

Deze formele A-statussen worden niet heropend of herwaardeerd. Alleen Mark wijzigt formele status.

## Verplichte detectoren
- Lahiri Mahasaya en Kriya Yoga-lineages;
- Sri Yukteswar, Yogananda en AOAY-claims met dubbele verificatie waar toepasselijk;
- Trailanga Swami;
- Anandamayi Ma;
- Ramakrishna/Vivekananda-context;
- Kabir en relevante fysiek aanwijsbare plaatsen;
- Shiva-, Shakti-, crematie- en ghattradities;
- Sarnath en boeddhistische fysieke plaatsen;
- Babaji-claims uitsluitend met correcte claimclassificatie;
- lokaal vereerde, fysiek bestaande plekken die door standaard toeristische lijsten worden gemist.

## Verplichte inhoud per kandidaat
Bevestig afzonderlijk:
1. fysieke identiteit en ligging;
2. historische, spirituele, lineage- of traditierelatie;
3. waarom devotees gaan;
4. wat bezoekers er werkelijk doen;
5. of Mark respectvol kan deelnemen;
6. actuele bezoekbaarheid;
7. representatieve beelden en recente beleving;
8. nabijheid tot A-ankers en bruikbare loopclusters;
9. claimklasse, bronautoriteit en tegenstrijdigheden.

Wanneer actuele bezoekbaarheid niet betrouwbaar is vastgesteld, schrijf exact:
`Fysieke plek bevestigd; actuele bezoekbaarheid niet betrouwbaar vastgesteld.`

## Parallelle masterkaartopdracht
Inventariseer alle formele A's uit `LOCKED_A.md`, alle formele B's uit `LOCKED_B.md`, relevante geldige decisions en canonieke plaatsrecords. Herwaardeer niets.

Iedere formele A/B krijgt een record in:
`research/active/VARANASI-COMPLETE-001/shared/MASTER_A_B_GEO_REGISTRY.jsonl`

Minimaal schema per record:
- location_id;
- canonical_name;
- display_name_nl;
- marker_name;
- cluster;
- formal_status;
- latitude;
- longitude;
- geo_status;
- geo_source_type;
- geo_source_reference;
- accuracy_class;
- exactness_note;
- last_checked_at;
- source_run;
- recognition_hook;
- open_geo_question;
- active.

## Snelle GEO-regel
Gebruik bij voorkeur de herkenbare Google Maps-pin van de bedoelde plek. Is die niet betrouwbaar beschikbaar, gebruik dan het centrum van het terrein, een bevestigd adrespunt of een representatief lokaal werkpunt. Circa 100 meter afwijking is aanvaardbaar. Bereken niet kunstmatig de exacte afwijking. Zet onzekerheid zichtbaar in het register en in de markerbeschrijving.

Toegestane `geo_status`:
- VERIFIED_EXACT;
- VERIFIED_SITE_CENTRE;
- WORKING_GOOGLE_MAPS_PIN;
- WORKING_ADDRESS_POINT;
- APPROXIMATE_LOCAL_POINT;
- MISSING.

`MISSING` is alleen toegestaan wanneer zelfs geen verantwoord plaatselijk werkpunt kan worden vastgesteld. Het ontbreken van deur- of ingangprecisie blokkeert geen marker.

## KML-contract
Lever in GOUD:
`research/active/VARANASI-COMPLETE-001/GOUD/INDIA_ALL_FORMAL_A_B_WORKING.kml`

De KML bevat exact twee hoofdlagen:
- `A_FORMEEL` — groen;
- `B_FORMEEL` — oranje.

Geen C's, treinhaltes, bases, routes of categorie-logo's in deze release. Gebruik eenvoudige uniforme pins. Markernaam is direct leesbaar. Wanneer de naam voornamelijk Indiaas is, voeg tussen haakjes een korte Nederlandse functie toe, bijvoorbeeld `Kashi Vishwanath (Shiva-tempel)`.

Iedere markerbeschrijving bevat minimaal LOCATION_ID indien beschikbaar, cluster, formele status, GEO-status, nauwkeurigheidsklasse, recognition hook, bronrun en open GEO-vraag.

## Beheerbaarheid
De JSONL-registry is de gegevensbron; de KML is een gegenereerd product. Latere correcties van naam, coördinaat, GEO-status of statusbesluit worden eerst in het register toegepast en daarna deterministisch naar KML geëxporteerd. Geen handmatige KML-only correcties.

## Verplichte eindcontroles
- aantal formele A in geldige statusbronnen = actieve A-records in registry = A-placemarks in KML;
- aantal formele B in geldige statusbronnen = actieve B-records in registry = B-placemarks in KML;
- geen dubbel LOCATION_ID;
- geen dubbele fysieke plek onder verschillende aliassen zonder expliciete aliasrelatie;
- iedere marker heeft coördinaten en GEO-status;
- alle eerdere BRONS/ZILVER/GOUD-output blijft ongewijzigd;
- nieuwe Varanasi-statusvoorstellen zijn adviserend totdat Mark beslist.

## Verboden
- oude BRONS-output overschrijven of verwijderen;
- de geparkeerde Kumaon-routeoptimalisatierun wijzigen;
- bestaande formele A/B/C-statussen veranderen;
- C-locaties aan deze KML toevoegen;
- busadvies, boekingen, hotelkeuze of volledige routeoptimalisatie uitvoeren;
- precisieonderzoek zonder materiële kaartwaarde laten uitgroeien tot blocker.

## Clustercompleetheid
De run is inhoudelijk compleet wanneer de verplichte detectoren aantoonbaar zijn uitgevoerd, iedere opgenomen kandidaat de fysieke- en bezoekbaarheidspoort heeft doorlopen, gemiste zware kandidaten systematisch zijn gecontroleerd en alle formele A/B-locaties repositorybreed in registry en KML zijn gedekt.

END_OF_ARTIFACT

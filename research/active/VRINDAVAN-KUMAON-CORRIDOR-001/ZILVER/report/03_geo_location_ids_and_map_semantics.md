# 03 — GEO, LOCATION_ID and map semantics

## LOCATION_ID

Braj 200–228, corridor 300–315 and Kumaon 400–426 blijven ongewijzigd. Corridor-ID's zijn uniek, sequentieel en blokzuiver. De bestaande aanvragen voor Bodh Gaya, Varanasi, Agra en Haridwar/Kankhal blijven `BLOCK_RESERVATION_REQUIRED`; ZILVER reserveert geen nieuw blok.

## Materiële GEO-correcties

De onafhankelijke controle vond dat vier Dwarahat-objecten in BRONS te dicht bij hetzelfde ashrampunt waren geplaatst. Zij zijn nu gescheiden:

- Babaji Cave: 29.833400, 79.465400;
- Babaji Smriti Bhavan: 29.832873, 79.464364;
- Dunagiri Temple: 29.796720, 79.451230;
- YSS Dwarahat Ashram: 29.784767, 79.422761.

Andere materiële correcties:

- Neem Karoli Baba Ashram Vrindavan: 27.567400, 77.692150;
- Radha Raman Temple: 27.585380, 77.698730;
- Kainchi Dham: 29.422550, 79.512450;
- Kasar Devi Temple: 29.641600, 79.661540;
- Kakrighat representatief punt: 29.543710, 79.532740;
- Jageshwar complex: 29.637500, 79.854280;
- Binsar Sanctuary representatief centrum: 29.666700, 79.750000;
- Ghorakhal Temple: 29.379530, 79.545450.

De overige punten zijn opnieuw op naam, stad, objecttype en globale plaatsing gecontroleerd. Waar geen gezaghebbende exacte bezoekersingang beschikbaar was, blijft `WORKING` zichtbaar. Geen WORKING-punt wordt als geverifieerde ingang gepresenteerd.

## Kaartsemantiek

BRONS gebruikte `B_ADVIES` voor twee reeds formele B-records: Radha Raman Temple en Ghorakhal Temple. Dat was semantisch onjuist omdat ZILVER geen adviesstatus mag toekennen en deze B-statussen uitsluitend van Mark afkomstig zijn.

De gecorrigeerde centrale bron en KML gebruiken daarom `B_FORMEEL`. Beide records behouden exact hun bestaande formele B-status. Er is geen nieuw adviserend B-record toegevoegd.

`A_FORMEEL`, `B_FORMEEL`, `C_CONTEXT` en `CORRIDOR_EN_STATIONS` blijven onderscheiden. GEO-status is onafhankelijk van de kaartlaag. De KML bevat uitsluitend records met een toegewezen LOCATION_ID en bruikbaar WORKING-punt; formele locaties zonder gereserveerd blok blijven volledig zichtbaar in de centrale bron maar niet als fictief genummerde marker.

END_OF_ARTIFACT
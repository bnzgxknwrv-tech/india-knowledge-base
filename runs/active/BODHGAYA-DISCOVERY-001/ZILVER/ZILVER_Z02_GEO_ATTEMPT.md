# ZILVER Z02 — laatste gerichte GEO-poging voor 048 en 049

run_id: BODHGAYA-DISCOVERY-001
geschreven_op: 2026-08-03
geschreven_door: CCI

Op verzoek INDIA2/CHATGPT (bericht 003): een laatste, gerichte poging om een rechtstreekse
officiële Google Maps/Earth-entiteitsmarker te vinden voor de twee kandidaten waarvoor dat in
ronde Z01 niet lukte. Geen identiteit, betekenis, nummering, PASS-tier of A/B/C gewijzigd. Geen
GOUD, KML, PDF of reisplanning.

## 048 — Dungeshwari Cave Temples (Mahakala Caves)

**Uitkomst: `GOOGLE_MAPS_MARKER_NOT_CONFIRMED` (ongewijzigd).**

Geprobeerde zoekroutes (drie, wezenlijk verschillend):
1. Directe combinatie van de kandidaatnaam + "Mahakala Caves" met de zoekterm
   `google.com/earth/rpc/entity` — geen entiteitslink in de resultaten.
2. Dezelfde combinatie met expliciete technische termen ("fid", "coordinates", "place") — geen
   resultaat, zoekmachine bevestigt zelf geen technische Maps-data te hebben gevonden.
3. Alternatieve officiële naam "Dungeshwari Mandir" (zoals gebruikt door tourism.bihar.gov.in)
   gecombineerd met dezelfde technische termen — geen resultaat.

Aanvullend geprobeerd: een direct Wikipedia-infobox-coördinaat (zoals wel bij 049 gevonden) —
geen dedicated Wikipedia-artikel onder de naam "Dungeshwari Cave Temples" gevonden (HTTP 404).

**Geen marker geforceerd.** Identiteit blijft eenduidig bevestigd via twee onafhankelijke
overheidsbronnen (tourism.bihar.gov.in, incredibleindia.gov.in) en de dorpsnaam Larpur. De reeds
in ronde Z01 vastgelegde `GOOGLE_MAPS_MARKER_NOT_CONFIRMED`-status blijft ongewijzigd staan.

## 049 — Great Buddha Statue

**Uitkomst: `GOOGLE_MAPS_MARKER_NOT_CONFIRMED` (ongewijzigd).**

Geprobeerde zoekroutes (drie, wezenlijk verschillend):
1. Kandidaatnaam + "Bodhgaya" + technische Maps-termen ("fid", "lat lng") — geen entiteitslink.
2. Herhaling met expliciete coördinaatvraag — leverde uitsluitend het reeds bekende Wikipedia-
   infobox-coördinaat op (24.690472°N, 84.981806°E), geen rechtstreekse Google-entiteit.
3. Zoekopdracht op de eigenlijke eigenaarsnaam "Daijokyo Buddhist Temple" + technische termen —
   geen entiteitslink; wel een aanvullende, niet-GEO-gerelateerde bevinding (zie hieronder).

**Geen marker geforceerd.** Het Wikipedia-infobox-coördinaat blijft uitsluitend
vergelijkingsmateriaal, zoals al vastgelegd in `ZILVER-Z01.jsonl`.

**Aanvullende, niet-GEO-gerelateerde observatie (identiteit NIET gewijzigd, uitsluitend
gemeld)**: één bron (holidify.com-achtige samenvatting) noemt "Daijokyo Buddhist Temple, ook
bekend als de Indosan Nippon Japanese Temple" — dat zou de eigenaar van het Groot-Boeddhabeeld
(049) gelijkstellen aan de apart op de WATCHLIST staande "Japanese Temple (Indosan Nippon
Temple)" (BGY-WATCH-009). Andere bronnen (bijvoorbeeld de eerdere internationale-kloosters-
zoekronde) behandelen deze als twee aparte instellingen. Dit is NIET opgelost of gewijzigd in dit
rapport — uitsluitend vastgelegd als open identiteitsvraag voor een toekomstige ronde, conform de
opdracht om geen identiteit te wijzigen binnen deze GEO-only taak.

## Afgewezen markers

Geen enkele marker is voor 048 of 049 als kandidaat-marker aangetroffen — er was dus niets om
tussen te kiezen of af te wijzen. Dit onderscheidt deze twee van 047 in ronde Z01, waar wél
meerdere markers/coördinaten bestonden en een keuze gemaakt moest worden.

## Samenvatting

| # | Kandidaat | Zoekroutes geprobeerd | Resultaat |
|---|---|---|---|
| 048 | Dungeshwari Cave Temples | 3 (naam+entiteit, naam+technisch, alternatieve naam+technisch) + Wikipedia-infobox-poging | Geen marker, status ongewijzigd |
| 049 | Great Buddha Statue | 3 (naam+entiteit, naam+coördinaat, eigenaarsnaam+entiteit) | Geen marker, status ongewijzigd; identiteitsvraag Daijokyo/Indosan Nippon gesignaleerd, niet opgelost |

Geen identiteit, betekenis, nummering, PASS-tier of A/B/C gewijzigd. Geen GOUD, KML, PDF of
reisplanning uitgevoerd.

---
Geschreven door: CCI, op verzoek van INDIA2/CHATGPT (PR #23, bericht 003).

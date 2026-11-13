# RESULT.md — INDIA5-VNS-DISCOVERY-COVERAGE-003

## Samenvatting

Eerste inhoudelijke uitvoering van de PRE-BRONS/detectorarchitectuur. Vier PROVISIONAL
detectoren geïntroduceerd en toegepast op Varanasi (straal ~20km). Resultaat: **5 nieuwe
PROVISIONAL kandidaten** (permanente nummers 041-045, nieuw en vrij, geen bestaand nummer
gewijzigd), plus meerdere gedocumenteerde negatieve/buiten-scope bevindingen. Geen enkele
bestaande kandidaat, nummer, A/B/C-keuze, hotelbesluit, dataset of KML gewijzigd (bevestigd via
`check_forbidden_writes.py`: `CONTROLE OK`).

## PRE-BRONS-bevindingen

Volledige brief: `runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/PRE_BRONS/REGION_CONTENT_BRIEF.md`
+ `.json` (gevalideerd met `india4/scripts/validate_pre_brons_brief.py`: `VALIDATIE OK`).

Geïntroduceerde detectoren (allemaal PROVISIONAL, bibliotheek was leeg -- geen ACTIVE detector
bestond vóór deze run): `DET-P001 LINEAGE_TEXT_DETECTOR`, `DET-P002 JAIN_HERITAGE_DETECTOR`,
`DET-P003 ASI_ROYAL_HERITAGE_DETECTOR`, `DET-P004 GHAT_COMPLETENESS_DETECTOR`. Volledige
definities: `PRE_BRONS/PRE_BRONS_DETECTORS.jsonl`. Deze zijn NIET canoniek ACTIVE gemaakt --
dat is aan INDIA2, na deze run (conform `india5/GOVERNANCE.md` sectie 3).

## Nieuwe PROVISIONAL kandidaten (5)

Volledige records met betekenis- en GEO-velden:
`runs/active/VARANASI-GEO-DELIVERY-REPAIR-001/PRE_BRONS/DISCOVERY_CANDIDATES.jsonl`. Nieuwe
permanente nummers toegevoegd aan `NUMBERING_REGISTRY.jsonl` (append-only, 40 -> 45, geen
bestaand nummer gewijzigd/hergebruikt).

| Nr. | Naam | Detector | Kern |
|---|---|---|---|
| 041 | Parshvanath Digambar Jain Temple, Bhelupur | JAIN_HERITAGE | Kalyanaka-plek 23e Tirthankara |
| 042 | Suparshvanath Jain Tirth (Jain Ghat), Bhadaini | JAIN_HERITAGE | Kalyanaka-plek 7e Tirthankara, in dezelfde buurt als de hotelbasis |
| 043 | Shreyansanath Jain Tirth, Sarnath (Simhapuri) | JAIN_HERITAGE | Kalyanaka-plek 11e Tirthankara, co-gelegen met bestaand Sarnath-cluster maar ANDERE traditie |
| 044 | Ramnagar Fort (zetel van de Kashi Naresh) | ASI_ROYAL_HERITAGE | Enige koninklijke/wereldlijke locatie, vult een volledig ontbrekende historische laag |
| 045 | Adi Keshava Ghat | GHAT_COMPLETENESS | Noordelijke tegenhanger van Assi Ghat (010), oudste Vishnu-site, expliciet niet-toeristisch |

**Belangrijkste bevinding**: vóór deze audit was 0 van de 40 kandidaten Jain, ondanks dat
Varanasi de kalyanaka-plaats is van vier Jain-Tirthankara's -- een volledige religieuze
traditie op de exacte onderzochte plek was afwezig. Dit is precies het type "dramatisch te
missen A-locatie" waar de discovery-audit voor is opgezet.

Alle 5 zijn expliciet `protected_mark_status: DOOR_MARK_TE_BEOORDELEN` -- CCI heeft GEEN A/B/C
toegekend. `geo_status: GOOGLE_MAPS_MARKER_NOT_CONFIRMED` voor alle 5 (identiteit met meerdere
onafhankelijke bronnen bevestigd, geen Google Maps-marker geverifieerd -- dat is BRONS' taak,
niet deze PRE-BRONS-audit).

## Negatieve / buiten-scope bevindingen (bewaard met reden, RESEARCH_QUALITY.md-principe)

- **Mahavatar Babaji Cave** (gerelateerd aan de Kriya Yoga-lijn, LINEAGE_TEXT_DETECTOR):
  bevindt zich daadwerkelijk in Dwarahat, Almora-district, Uttarakhand -- NIET in Varanasi.
  Verworpen als Varanasi-kandidaat (buiten regio). Eerste zoekresultaat (een blogtitel) suggereerde
  ten onrechte een Varanasi-locatie; nader onderzoek weerlegde dit -- goed voorbeeld van
  vindbewijs vs. inhoudelijk bewijs (RESEARCH_QUALITY.md).
- **Chandraprabhu Jain Tirth, Chandrawati/Chandrapuri** (JAIN_HERITAGE_DETECTOR): kalyanaka-
  plek van de 8e Tirthankara, coördinaten 25°27'56.1"N 83°07'46.7"E, ligt op ~34 km van
  Varanasi -- BUITEN de gedefinieerde 20km-straal van deze audit. NIET toegevoegd als
  kandidaat (niet om gebrek aan waarde, maar om scope). Aanbeveling: heroverwegen als de straal
  ooit wordt uitgebreid.
- **Overige, niet-specifieke ghats** (Raj Ghat en andere, GHAT_COMPLETENESS_DETECTOR): geen
  vergelijkbaar specifiek onderscheidend verhaal gevonden (WHY_NOT_THE_OTHERS niet doorstaan) --
  niet toegevoegd.

## Toets van de bestaande 40 (puur signalerend, GEEN wijziging)

Een volledige, opnieuw-onderzochte betekenis-audit van alle 40 bestaande kandidaten (living/
monumentaal, beroemd-maar-leeg) is in deze ronde NIET uitputtend uitgevoerd -- dat zou een
even grote onderzoeksinspanning vergen als de discovery zelf en viel buiten de praktische
scope van deze ene taak. Wel een gerichte constatering op basis van reeds bekende gegevens:
- **VNS-CAND-040 Bharat Mata Temple** (huidige keuze C): een moderne (1936) tempel met een
  reliëfkaart van India als hoofdattractie -- eerder een monument/curiositeit dan een plek met
  doorlopende devotionele praktijk in de klassieke zin. Puur signalerend, geen wijziging aan de
  C-status.
- **VNS-CAND-032 Sarnath Archaeological Museum**: per `place_type` al als museum
  gecategoriseerd -- "monumentaal" is hier verwacht en geen nieuw signaal.
Geen enkele bestaande status is gewijzigd op basis van deze constateringen.

## Saturatiestatus

Per detector: minimaal 2 zoekbenaderingen uitgevoerd, meerdere bronfamilies per claim
gekruist. **Geen van de vier detectoren heeft een formele afsluitstatus van 3 opeenvolgende
non-productieve richtingen bereikt** -- deze ronde was één gerichte onderzoekssessie, geen
meervoudige-sessie-verzadiging.

- `DET-P001 LINEAGE_TEXT_DETECTOR`: `NOT_YET_SATURATED` (1 hoofdrichting onderzocht, 1 verworpen
  lead buiten regio; geen aanvullende in-regio lineage-uitbreiding gevonden binnen deze ronde).
- `DET-P002 JAIN_HERITAGE_DETECTOR`: `NOT_YET_SATURATED` maar wel high-value (3 nieuwe
  kandidaten uit 1 hoofdrichting + kruiscontrole; een vierde kalyanaka-site buiten scope).
- `DET-P003 ASI_ROYAL_HERITAGE_DETECTOR`: `NOT_YET_SATURATED` (1 kandidaat gevonden, verdere
  ASI-monumentenlijst voor Varanasi niet volledig doorzocht wegens ontbrekende directe
  ASI-database-toegang in deze sessie).
- `DET-P004 GHAT_COMPLETENESS_DETECTOR`: `NOT_YET_SATURATED` (slechts een deel van de 84 ghats
  systematisch beoordeeld op onderscheidend verhaal).

**Sweepniveau: `NOT_YET_SATURATED`.** Deze audit heeft aantoonbaar waarde geleverd (een hele
ontbrekende traditie gevonden) maar is nog geen bewijs van volledige regionale dekking.

## Dramatic miss check (herhaald, zie ook REGION_CONTENT_BRIEF.md)

Twee expliciet erkende, niet stilzwijgend opgeloste gaten:
1. **Islamitisch/soefi-erfgoed van Varanasi is niet onderzocht.** Varanasi heeft een
   aanzienlijke moslimgemeenschap en historische soefi-tradities. CCI heeft dit gebied bewust
   NIET zelfstandig ingevuld met een specifieke kandidaat -- sommige locaties in dit thema
   liggen gevoelig, en het toevoegen van een specifieke kandidaat zonder Marks/INDIA2's
   expliciete richting leek onverstandig. Dit wordt hier expliciet aan Mark/INDIA2 voorgelegd
   in plaats van zelf een keuze te maken.
2. **Geen lokale insider-/priesterbron geraadpleegd** -- alleen webbronnen. Volgens het eerdere
   filosofie-overleg is dit juist de belangrijkste bron voor werkelijk verborgen parels.

## Wat NIET is gedaan (bewust, conform de opdracht)

- Geen enkele bestaande kandidaat, nummer, A/B/C-keuze, hotelbesluit, dataset of KML gewijzigd.
- Geen A/B/C toegekend aan de nieuwe kandidaten -- uitsluitend PROVISIONAL.
- Geen detector canoniek ACTIVE gemaakt.
- Geen PDF gebouwd, geen reisgids aangepast.
- Geen GEO-marker-verificatie (Google Maps) uitgevoerd voor de nieuwe kandidaten -- dat is
  BRONS' taak in een vervolgronde, niet deze PRE-BRONS-discovery-audit.

## Aanbeveling voor een vervolgronde (niet uitgevoerd)

1. BRONS-GEO-verificatie voor VNS-CAND-041 t/m 045 (Google Maps-markers zoeken).
2. Mark/INDIA2-besluit over het Islamitisch/soefi-erfgoed-hiaat: wel of niet onderzoeken, en zo
   ja hoe.
3. Verdere verzadiging van de vier PROVISIONAL detectoren (met name ASI_ROYAL_HERITAGE en
   GHAT_COMPLETENESS, nog niet uitputtend).
4. Promotie/afwijzing van de vier PROVISIONAL detectoren door INDIA2.

INDIA5-TASK-COMPLETE::INDIA5-VNS-DISCOVERY-COVERAGE-003

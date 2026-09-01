# CORRECTIERAPPORT -- INDIA5-testsweep VNS-CAND-022 t/m 040

run_id: VARANASI-GEO-DELIVERY-REPAIR-001
rapportdatum: 2026-08-02

## Scope-afwijking (vastgelegd voordat BRONS begon)

De oorspronkelijke opdracht vroeg om precies 20 nieuwe testkandidaten. `candidates.jsonl` bevat in
totaal 40 Varanasi-kandidaten; 21 (VNS-CAND-001 t/m 021) waren al volledig verwerkt vóór deze
testsweep. Er resteerden dus nog maar 19, niet 20. Dit is aan Mark voorgelegd (real content decision);
Mark heeft op 2026-08-02 expliciet gekozen om door te gaan met de 19 resterende kandidaten
(VNS-CAND-022 t/m 040) in plaats van een 20e te verzinnen of VNS-CAND-021 te herdoen. Deze testsweep
dekt daarom 19 kandidaten, niet 20. VNS-CAND-021 is ongewijzigd gelaten.

## ZILVER-correcties (3x, alle opwaarderingen, geen fouten hersteld)

| candidate_id | van | naar | reden |
|---|---|---|---|
| VNS-CAND-029 Dhamek Stupa | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | VERIFIED_OFFICIAL_MAP_LINK (25.380889,83.024276) | ZILVER vond een officiele Google Earth entity-API-link (google.com/earth/rpc/entity) met ingesloten coordinaat en feature-ID die BRONS niet had gevonden |
| VNS-CAND-031 Chaukhandi Stupa | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | VERIFIED_OFFICIAL_MAP_LINK (25.37402,83.023588) | idem, Google Earth entity-API-link gevonden door ZILVER |
| VNS-CAND-033 Deer Park / Isipatana | GOOGLE_MAPS_MARKER_NOT_CONFIRMED | VERIFIED_OFFICIAL_MAP_LINK (25.3825,83.024445) | idem, Google Earth entity-API-link gevonden door ZILVER |

Geen van de 19 BRONS-records bevatte een feitelijke fout (verkeerde plek, verwarring met
nabijgelegen organisatie, verkeerd overgenomen coordinaat); de 3 correcties zijn uitsluitend
opwaarderingen op basis van extra bronnen die ZILVER vond in een tweede onderzoeksronde.

## Openstaande onzekerheden (16 kandidaten, GOOGLE_MAPS_MARKER_NOT_CONFIRMED)

VNS-CAND-022, 023, 024, 025, 026, 027, 028, 030, 032, 034, 035, 036, 037, 038, 039, 040.

Voor al deze 16 geldt: fysieke identiteit bevestigd via minstens 2 onafhankelijke bronnen (overheids-
listings, encyclopedische bronnen, gespecialiseerde Varanasi-tempelsites, institutionele bronnen),
maar geen publieke Google Maps-marker kon interactief geopend en afgelezen worden binnen deze sessie
(geen browsergebaseerde Google Maps-toegang beschikbaar, alleen websearch/fetch). Dit is een
sessie-/tool-beperking, geen contentprobleem. Geen schatting, terreinmiddelpunt of ander verboden
substituut is gebruikt.

**Bijzondere aandachtspunten binnen deze 16:**

- **VNS-CAND-023 (Mrityunjay Mahadev Temple):** een onafhankelijke (niet-Google) coordinaat uit
  Wikipedia (25.317645,82.973914) wijkt ca. 3 km af van het oude vergelijkingscoordinaat
  (25.3291,83.0056). Dit is GEEN eindcoordinaat (niet overgenomen), maar het verschil is groot genoeg
  om apart te vermelden -- bij een toekomstige sessie met interactieve Google Maps-toegang verdient
  deze kandidaat prioriteit voor handmatige verificatie.
- **VNS-CAND-025 (Lahartara Kabir birthplace memorial)** en **VNS-CAND-028 (Bhaskarananda Samadhi /
  Anand Bagh):** physical_identity blijft PARTIAL (overgenomen uit de brondata) omdat het
  herdenkingszones zijn zonder één eenduidig hoofdgebouw.

## Dedup-observatie

Zie GEO_AUDIT.md: VNS-CAND-006 ("Sarnath sacred complex", buiten scope) overlapt begripsmatig met de
zes nieuw gecatalogiseerde Sarnath-deelsites (029-034). Geen wijziging aangebracht; alleen gesignaleerd
voor een toekomstig Mark-besluit.

## Beschermde besluiten -- ongewijzigd

- VNS-CAND-001, 002, 003, 007: Mark-keuze A (ongewijzigd, buiten deze testsweep).
- VNS-CAND-008: Mark-keuze B; het expliciet afgewezen coordinaat [25.3045, 82.979369] is niet
  opnieuw voorgesteld of gebruikt (buiten deze testsweep, niet aangeraakt).
- Geen van de 19 testsweep-kandidaten heeft een bestaand Mark-besluit; alle 19 blijven
  `DOOR_MARK_TE_BEOORDELEN`. Geen A/B/C toegekend door BRONS/ZILVER/GOUD.

# MISSED_NEARBY_RISK — INDIA ZILVER

status: COMPLETE_WITH_DISTANCE_LIMITATION
rule: alleen bestaande betrouwbare coördinaten/afstanden; niets geraden.

## Kernuitkomst

- nieuwe fysieke kandidaten in de strikte ID/A-B-C-queue: **31**
- daarvan **bevestigd <=1 km** van een reeds beoordeelde/gekozen locatie: **0**
- daarvan **bevestigd <=3 km** van een reeds beoordeelde/gekozen locatie: **0**
- interpretatie: dit zijn **bevestigde lower bounds**, niet de claim dat er werkelijk geen kandidaten binnen 1 of 3 km liggen.
- reden: voor de nieuwe fysieke kandidaten staat op deze branch geen voldoende complete set betrouwbare kandidaatcoördinaten + vergelijkbare bestaande A/B/C-coördinaten waarmee de bands verliesloos kunnen worden berekend. TASK.md verbiedt raden.

## Risicobands

| kandidaat / signaal | cluster | betrouwbare afstand tot bestaande beoordeelde locatie | band | same-site / complex | actie |
|---|---|---:|---|---|---|
| Rana Mahal Ghat | Varanasi | UNKNOWN | >10 km/unknown | NEE bekend | coördinaten valideren en tegen 001-045 proximity-backfill doen |
| Panchganga Ghat Ashram / Trailanga Swami meeting | Varanasi | identiteit eerst oplossen tegen `VNS-CAND-004` en `VNS-CAND-011` | UNKNOWN | **POSSIBLE_SAME_SITE_OR_COMPLEX** | geen nieuw ID vóór dedup/identity |
| Ramnagar palace / Kashi Naresh tutoring | Varanasi | identiteit eerst oplossen tegen `VNS-CAND-044 Ramnagar Fort` | UNKNOWN | **POSSIBLE_SAME_SITE_OR_COMPLEX** | geen nieuw ID vóór dedup/identity |
| Pranabashram, rented ashram house Benares | Varanasi | UNKNOWN | >10 km/unknown | onbekend | lead; exacte huidige fysieke identiteit ontbreekt |
| Anandamayi Ma Ashram, Vrindavan | Vrindavan | UNKNOWN t.o.v. reeds bekende NKB Vrindavan-site | >10 km/unknown | onbekend | betrouwbare coördinatenpaarvergelijking nodig |
| Akrura Ghat, Vrindavan | Vrindavan | UNKNOWN t.o.v. reeds bekende NKB Vrindavan-site | >10 km/unknown | onbekend | betrouwbare coördinatenpaarvergelijking nodig |
| overige 28 strikte nieuwe fysieke kandidaten | nieuwe/niet eerder A-B-C-complete regio's | geen betrouwbaar vergelijkingspaar in de geraadpleegde repo-lagen | >10 km/unknown | waar van toepassing in ID-queue gemarkeerd | lokale proximity-backfill bij regionale reconciliatie |

## Bands — bevestigde aantallen

| band | bevestigd aantal |
|---|---:|
| <=250 m | 0 |
| 250-500 m | 0 |
| 0.5-1 km | 0 |
| 1-3 km | 0 |
| 3-10 km | 0 |
| >10 km/unknown | 31 |

`>10 km/unknown` betekent hier hoofdzakelijk **UNKNOWN**. Het mag niet worden gelezen als bewijs dat de locatie >10 km weg ligt.

## Hoogste proximity-risico zonder toegestane afstandsclaim

### Varanasi
De kans op een praktisch relevante near-miss is het hoogst omdat er al 45 permanent genummerde en door Mark beoordeelde locaties bestaan én de reverse-discovery later nieuwe/meer-granulaire Varanasi-signalen opleverde. Vooral Rana Mahal Ghat moet daarom vóór travel-completeness tegen de bestaande Varanasi-set worden gegeocodeerd en geband.

### Vrindavan
Er bestaat al een bekende/locked Neem Karoli Baba-ashram/samadhi-site, terwijl de persoonslaag twee andere fysiek benoembare Vrindavan-punten oplevert: Anandamayi Ma Ashram en Akrura Ghat. Zonder betrouwbare repo-coördinaten wordt geen 1/3-km-afstand geclaimd.

## Same-site / multi-person signalen

- `VNS-CAND-002` Lahiri Mahasaya original home: reeds bestaand; extra Sri Yukteswar-link, **MULTI_PERSON_SAME_SITE**, geen nieuw ID.
- Karar Ashram, Puri: één fysieke nieuwe site met Sri Yukteswar + Hariharananda, **MULTI_PERSON_SAME_SITE**; exact één nieuwe ID nodig.
- Sri Ramanasramam: Ramana Maharshi + Yogananda, **MULTI_PERSON_SAME_SITE**; exact één nieuwe ID nodig.
- Yogoda Math/Serampore: Sri Yukteswar + Yogananda, **MULTI_PERSON_SAME_SITE**; exact één nieuwe ID nodig.
- Dakshineswar Kali Temple: Ramakrishna-kernsite + Vivekananda-ontmoetingslink, **MULTI_PERSON_SAME_SITE**; exact één nieuwe ID nodig.
- 4 Garpar Road: Yogananda-familiesite en Sri-Yukteswar/Babaji-gerelateerde bronlaag, **MULTI_PERSON_SAME_SITE**; exact één nieuwe ID nodig.

## Gate-consequentie

Geen cluster met nieuwe kandidaten krijgt `LOCAL_PROXIMITY_DONE: JA` uitsluitend op basis van deze audit. Varanasi, Bodh Gaya/Gaya-corridor en Kumaon blijven daarom heropen totdat de bekende reverse-discovery-leads lokaal zijn teruggevuld. Voor nieuwe regio's moet proximity onderdeel zijn van de eerste regionale reconciliatie, niet achteraf.

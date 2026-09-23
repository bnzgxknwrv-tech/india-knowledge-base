# VARANASI HOTEL DECISION — LOCKED

status: LOCKED_BY_MARK
run_id: VARANASI-GEO-DELIVERY-REPAIR-001
decision_date: 2026-08-02
source_type: PERSONAL_RECOMMENDATION
source_person: Debby

## Gekozen verblijf

**Sahi River View Guesthouse**

Locatiecontext: Assi Ghat, Varanasi.

## Persoonlijke aanbeveling van Debby

> En mocht je nog geen plek hebben om te slapen: Sahi River View Guesthouse is echt een heerlijke plek in Assi Ghat (echt een hele fijne plek om te verblijven), vraag om een balcony room en doe ze de groeten van Debby - Jitendre die er werkt is een fijne kerel.

## Verplichte boekingsnotities

- Vraag om een **balcony room**.
- Doe **Jitendre** de groeten van **Debby**.
- Dit hotel geldt als de huidige door Mark gekozen Varanasi-basis.
- Niet vervangen door een andere accommodatie zonder een expliciet nieuw besluit van Mark.
- Niet behandelen als slechts een suggestie; status is `LOCKED_BY_MARK`.

## Relatie met route

De ligging bij Assi Ghat sluit direct aan op Marks A-clusters rond:

- 005 Shree Shree Ma Anandamayi Ashram, Bhadaini
- 010 Assi Ghat
- 015 Sankat Mochan Hanuman Temple
- 016 Durga Temple and Durga Kund
- 028 Bhaskarananda Samadhi / Anand Bagh
- 035 Tulsi Manas Temple
- 036 Tulsi Ghat
- 037 Lolark Kund

## Permanente werkwijzeregel voor INDIA5

Hotels, guesthouses, bases en andere verblijfskeuzes moeten vanaf nu altijd expliciet en duurzaam worden gelogd.

Minimaal verplichte velden:

- region / run_id
- accommodation_name
- city / area
- status: SUGGESTED | SHORTLISTED | LOCKED_BY_MARK | REJECTED_BY_MARK
- source_type
- source_person_or_source_id
- exact user wording or compact decision rationale
- room preference
- named contact person
- booking notes
- date recorded
- supersedes / superseded_by

Harde regels:

1. `LOCKED_BY_MARK` is canoniek en mag niet stil worden vervangen.
2. Persoonlijke aanbevelingen van bekenden moeten met naam en letterlijke kernnotitie worden opgeslagen.
3. Iedere sweep moet vóór hotelonderzoek eerst bestaande hotelbesluiten lezen.
4. GOUD moet gekozen verblijf opnemen in PDF, KML en routeplanning.
5. Als geen hotelbesluit bestaat, moet GOUD dat expliciet melden; nooit aannemen dat er nog niets gekozen is zonder repositorycontrole.
6. Een chatvermelding die een concrete keuze of sterke persoonlijke aanbeveling bevat, moet direct naar GitHub worden overgebracht wanneer GitHub beschikbaar is.

## Foutanalyse

Deze keuze was niet terugvindbaar in GitHub toen ernaar werd gezocht. Daardoor werd ten onrechte geconcludeerd dat geen hotelkeuze bekend was. De oorzaak was onvoldoende duurzame logging van niet-locatiebesluiten zoals hotels. Deze file corrigeert dat voor Varanasi en legt de vereiste structurele werkwijze vast.

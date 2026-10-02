# INDIA WIT — HERITAGE STAY OVERRIDE AUDIT

STATUS: READY
OWNER: INDIA WIT
MODE: CROSS-BRANCH INTEGRATION + CURRENT-WORLD VERIFICATION

## Waarom deze taak bestaat
Persoonsgerichte sweeps kunnen niet alleen nieuwe bezoeklocaties opleveren, maar ook historische verblijven: hotels, guesthouses, kamers, ashramkamers, woningen of andere slaapplaatsen waar een kernpersoon aantoonbaar verbleef. Zo'n vondst kan een eerder gekozen logistiek hotel inhoudelijk overtreffen. Bestaande hotelkeuzes blijven intact totdat Mark expliciet anders beslist, maar moeten opnieuw ter beoordeling komen zodra een relevante heritage-stay kandidaat bestaat.

## Opdracht
Maak voor ALLE onderzochte kernpersonen een lossless inventaris van persoonsgebonden verblijven in India uit reeds beschikbare persoonsfreezes/reconciliaties en toegestane projectoutputs. Zoek daarna gericht op de actuele fysieke voortzetting van alleen die reeds gedetecteerde verblijfclaims. Geen brede nieuwe persoonslocatiesweep.

Lever:
1. HERITAGE_STAY_CANDIDATES.md
2. ROOM_LEVEL_LEADS.md
3. CURRENT_EXISTENCE_AND_BOOKABILITY.md
4. EXISTING_HOTEL_OVERRIDE_MATRIX.md
5. MARK_HOTEL_REVIEW_QUEUE.md

## Per kandidaat minimaal
- persoon/personen;
- historische naam verblijf;
- stad/regio;
- aard: hotel/guesthouse/ashram/private house/dharmshala/etc.;
- bewijs van werkelijk verblijf versus alleen bezoek;
- datum/periode/frequentie indien bekend;
- kamernummer, vleugel, verdieping of specifieke ruimte indien bronmatig bekend;
- bron + locator;
- huidige naam/continuïteit van gebouw of onderneming;
- bestaat fysiek nog: JA/NEE/ONZEKER;
- overnachting tegenwoordig mogelijk: JA/NEE/ONZEKER;
- dezelfde historische ruimte/kamer boekbaar: JA/NEE/ONZEKER;
- afstand tot bestaande gekozen/voorgestelde hotel of clusteranker indien betrouwbaar vaststelbaar;
- mogelijke impact op bestaande hotelkeuze: NONE / REVIEW / HIGH-IMPACT-REVIEW;
- onzekerheden/conflicten.

## Zeer belangrijk
- Zoek expliciet naar room-level detail waar reeds een verblijfclaim is gevonden: kamernummer, kamernaam, verdieping, suite, hut, kuti, guest room, host house.
- Geen kamernummer of continuïteit afleiden zonder bron.
- Een modern hotel met dezelfde naam is niet automatisch hetzelfde gebouw.
- Een historische private woning die nu hotel is geworden is juist zeer relevant, maar continuïteit moet worden aangetoond.
- Een gesloten hotel kan nog steeds als bezoeklocatie relevant zijn.
- Een bestaand eerder LOCKED_BY_MARK hotel NIET wijzigen. Alleen `MARK_REVIEW_REQUIRED` produceren.
- Geen A/B/C namens Mark.
- Geen definitieve boeking.

## Prioriteit
Begin met steden/clusters die al waarschijnlijk in de reis komen of waar bestaande hotels/overnachtingen eerder zijn besproken. Geef extra gewicht aan Ram Dass, Neem Karoli Baba, Yogananda en andere personen voor wie concrete verblijfplaatsen in de persoonslagen voorkomen.

Commit outputs en update STATUS.md. Geen PDF/merge/PR.
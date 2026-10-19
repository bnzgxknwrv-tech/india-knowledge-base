# TREINEN — ALLE ZES GEBOEKT, GECONTROLEERD TEGEN GMAIL-BEVESTIGINGEN (WORK-audit 2026-10-06)

**Status: VOLLEDIG AFGEROND.** Alle zes treinbenen zijn geboekt en betaald via Mark's eigen
IRCTC-account (Foreign Tourist Ticket Booking). WORK heeft alle zes officiële
"Booking Confirmation"-mails van `ticketadmin@irctc.co.in` gecontroleerd (SPF/DKIM/DMARC geslaagd,
geen cancellation/refund/TDR-mail gevonden) en de canon hieronder is daarop gecorrigeerd.

## Geverifieerde boekingsstaat (bron: IRCTC-bevestigingsmails, niet schattingen)

| # | Trein | Traject | Vertrek → aankomst | Klasse | PNR | Ticket | Fee | **IRCTC-totaal** |
|---|---|---|---|---|---|---:|---:|---:|
| 1 | 15013 RANIKHET EXP | DLI → KGM | 19 dec 22:05 → 20 dec 05:05 | 1A | 2960524646 | ₹1.755 | ₹236 | **₹1.991** |
| 2 | 15036 UTR SMPRK K EXP | KGM → GZB | 29 dec 08:40 → 29 dec 14:39 | CC | 1000282893 | ₹605 | ₹236 | **₹841** |
| 3 | 12988 AII SDAH SF EXP | AF → GAYA | 31 dec 18:45 → 1 jan 07:50 | 1A | **2526376901** | ₹4.185 | ₹236 | **₹4.421** |
| 4 | 20887 VANDE BHARAT EXP | GAYA → BSB | 4 jan 09:55 → 4 jan 13:00 | EC, VEG | 6610669522 | ₹2.200 | ₹236 | **₹2.436** |
| 5 | 13042 HIMGIRI EXPRESS | BSB → HWH | 8 jan 21:05 → 9 jan 11:30 | 1A | 2845156738 | ₹3.940 | ₹236 | **₹4.176** |
| 6 | 22604 VM KGP SF EXP | TNM → PER | 19 jan 12:00 → 19 jan 15:40 | 2A | 4345948370 | ₹1.105 | ₹236 | **₹1.341** |

**Som: ticketfares ₹13.790 + convenience fees ₹1.416 = ₹15.206**, exclusief eventuele
betaalgateway-/kaartconversiekosten (die apart op Mark's kaartafschrift staan, bijv. €45,86 i.p.v.
₹4.421 bij trein 12988 — dat eurobedrag is een aanvulling, geen vervanging van het IRCTC-bedrag).

## Belangrijke correctie — stoel/coach is NOG NIET toegewezen

**"1A/Coupe", "CC/Window", "EC/Window", "2A/Lower" zijn geboekte VOORKEUREN, geen toegewezen
plaatsen.** In alle zes bevestigingsmails staat coach leeg en Seat/Berth/WL No. op `0`. Dit was eerder
in dit bestand onjuist samengevat als "alle zes FBKG/0" — dat klopt niet precies: **alleen de mail
van trein 15036 toont letterlijk de status `FBKG`**; bij de andere vijf is het statusveld in de
bevestigingsmail leeg. Correcte formulering: zes geldige boekingsbevestigingen met PNR; coach en
plaats nog niet toegewezen; recheck elke PNR na de bijbehorende ARP-datum (tabel onderaan) via
IRCTC → PNR Status om te zien of coach/plaats inmiddels is toegewezen.

**22604 eindpunt is exact Perambur (PER), niet Chennai Central (MAS)** — na aankomst zelf vervoer
regelen naar waar je in Chennai moet zijn.

**22324 is nergens geboekt** en hoeft niet geannuleerd te worden — alleen hieronder bewaard als
superseded historische kandidaat, niet meer als actieve optie.

## Trein 13042 in plaats van 22324 — WORK: AKKOORD (comment 5984379334)

Mark vond 13042 "Himgiri Express" zelf tijdens live zoeken voor de Varanasi→Kolkata-verbinding en
koos hem bewust boven de eerder met WORK afgestemde 22324:

- vertrek **8 jan 21:05** i.p.v. 22324's **9 jan 01:30** — 4u25 eerder, geen nachtelijke stationsgang;
- aankomst **9 jan 11:30** i.p.v. 22324's **13:05** — 1u35 eerder;
- **1A beschikbaar** (22324 bood max 2A);
- volledige ononderbroken nachtrust i.p.v. een nacht die om 01:30 onderbroken wordt.

Nuance (WORK): 13042 is als treinrit niet sneller (14u25 tegenover ~11u35 bij 22324), maar gebruikt
de nacht veel menselijker — consistent met de bestaande regel "optimaliseer bruikbare menselijke
tijd, niet gepubliceerde reissnelheid" (`governance/MARK_TRAVEL_PREFERENCES_CURRENT.md` §10). **Enig
logistiek nadeel: aankomst Howrah (HWH) i.p.v. Kolkata Chitpur (KOAA)**, vermoedelijk 10-20 min
verder van het geplande YSS/Garpar-gebied (geen hard bevestigd cijfer) — dit moet exact worden
doorgerekend zodra er een Kolkata-hotel gekozen wordt, niet geschat. Trein 13042's echte beginstation
is overigens **Jammu Tawi (JAT)**, niet Varanasi — vertrek 22:45, rijdt alleen ma/do/zo; voor Mark's
instap vrijdag 8 jan moet de trein donderdag 7 jan uit Jammu Tawi vertrokken zijn, wat de ARP-datum
(zie tabel) op 8 nov 2026 brengt (eigen berekening, niet apart door WORK/IRCTC bronbevestigd zoals de
andere vijf).

## Resterende actie — PNR/plaats-status rechecken na ARP-datum

| Trein | ARP-datum (normale venster opent) |
|---|---|
| 15013 | 20-10-2026 |
| 12988 | 01-11-2026 |
| 13042 | 08-11-2026 (eigen berekening, zie boven) |
| 20887 | 05-11-2026 |
| 22604 | 20-11-2026 |
| 15036 | 29-11-2026 |

Check na elke datum de bijbehorende PNR via IRCTC → PNR Status om te bevestigen dat coach/plaats
inmiddels is toegewezen. Dit is het enige nog openstaande actiepunt voor de treinen — alle zes
transacties zelf zijn al afgerond.

---

## ARCHIEF — historische achtergrond, niet meer actueel als actiepunt

De secties hieronder beschrijven het proces vóórdat alle zes boekingen rond waren (tijdzone/Aadhaar-
onderzoek, de kapotte IRCTC-registratiepagina, de Firefox-fix). Bewaard voor context en omdat de
Aadhaar-regelgeschiedenis mogelijk weer relevant wordt bij toekomstige boekingen (bijv. wijzigingen),
maar er is geen "nu/later"-actie meer nodig op de zes hierboven genoemde treinen.

### Aadhaar-regelgeschiedenis (nog relevant mocht een boeking ooit opnieuw moeten)

De normale General Quota-opening werd sinds september 2025 in drie fases steeds verder beperkt tot
Aadhaar-geauthenticeerde accounts (bronnen: deshgujarat.com, india.com, railrecipe.com,
newsonair.gov.in; PR #23 comment 5982836109):

| Fase | Vanaf | Aadhaar-only venster | Niet-Aadhaar kan boeken |
|---|---|---|---|
| Origineel | ±sept/okt 2025 | 08:00-08:15 IST | vanaf 08:15 IST, zelfde dag |
| Fase 1 | 29-12-2025 | 08:00-12:00 IST | vanaf 12:00 IST, zelfde dag |
| Fase 2 | 05-01-2026 | 08:00-16:00 IST | vanaf 16:00 IST, zelfde dag |
| Fase 3 | 12-01-2026 | 08:00-24:00 IST (HELE dag) | niet die dag — pas dag 2 |

Dit bleek in de praktijk geen blokkade voor Mark: alle zes boekingen zijn probleemloos gelukt via de
**Foreign Tourist Ticket Booking**-route, die buiten deze Aadhaar-beperking om werkt.

### IRCTC-registratiepagina was kapot — opgelost via Firefox

Mark kreeg bij het betalen van de Rs.100+GST internationale-registratiefee herhaaldelijk "Unable to
process payment request" via Razorpay/Plural/PayU, in zowel Chrome als Safari, zonder dat er ooit een
bankscherm verscheen — een bekend, breed gemeld IRCTC-bug op precies deze pagina (bevestigd via een
IndiaMike-forumdraad van 41+ pagina's over exact dit probleem). **De oplossing was simpelweg Firefox
gebruiken** — eerste poging direct geslaagd met Razorpay. Dit was een browser-specifiek
cookie/scriptconflict, geen kaart- of bankprobleem. Reservekanalen bij een vergelijkbaar probleem in
de toekomst: ConfirmTkt (onderdeel van ixigo) of 12Go.asia — beide boeken op hetzelfde IRCTC-backend
en accepteren internationale kaarten probleemloos, tegen een kleine commissie.

### IRCTC-account-registratie — referentie

Account compleet: geregistreerd, fee betaald, e-mail + mobiel geverifieerd, profiel ingevuld volgens
IRCTC's eigen officiële voorbeeld (Pin code = willekeurig 6-cijferig getal, State = "Netherlands",
City/Town = echte woonplaats, Post Office = woonplaats/wijk nogmaals).

## Apart, nog in behandeling — niet treinen

De twee binnenlandse **vluchten** (Kolkata→Chennai 15 jan, Chennai→Delhi 20 jan) lopen via een eigen,
nog lopend CCI/WORK-consensustraject (`runs/active/BINNENLANDSE_VLUCHTEN_STARTVRAAG_2026-10-06.md`)
en hebben geen ARP-systeem zoals treinen — die komen apart terug.

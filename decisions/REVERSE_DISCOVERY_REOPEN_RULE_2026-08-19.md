# REVERSE DISCOVERY / REOPEN RULE — 2026-08-19

Status: ACTIVE GOVERNANCE
Owner: INDIA8 / Mark

## Kernbesluit
Een cluster/regio die eerder als `AF`, `COMPLETE`, `FROZEN`, of vergelijkbaar is gemarkeerd, is alleen gesloten voor de toenmalige zoekronde. Nieuwe persoonsgerichte vondsten mogen en moeten een eerder afgewerkt cluster HEROPENEN voor additieve review.

Er gaan door reverse discovery geen bestaande locaties automatisch AF. Er kunnen alleen nieuwe locaties, nieuwe overlapbetekenis, nieuwe proximity-relaties en nieuwe reiswaarde BIJ komen. Bestaande A/B/C-keuzes blijven staan totdat Mark ze expliciet wijzigt.

## Verplichte reverse-discovery pass
Na afronding van de landelijke persoonslaag moet voor ELK eerder afgewerkt cluster/regio worden gecontroleerd:

1. Welke nieuw gevonden persoonslocaties liggen in of nabij het cluster?
2. Welke locaties blijken door meerdere Top-personen gedeeld of in verschillende perioden bezocht?
3. Welke exacte same-site-overlaps zijn nieuw zichtbaar geworden?
4. Welke nieuwe hosthuizen, hotels, ashrams, tempels, stations, ziekenhuizen, caves, ghats, retreats of andere fysieke sites zijn reisrelevant?
5. Welke nieuwe locatie ligt dichtbij een bestaande B/C of bestaande route, waardoor combinatievoordeel de praktische waarde verhoogt?
6. Welke accommodatie heeft intrinsieke persoonsbetekenis (bijv. een hotel/huis waar een persoon aantoonbaar verbleef) en moet als mogelijke slaapbasis aan Mark worden voorgelegd?
7. Welke nieuwe locatie ligt zo dicht bij een bestaand A-cluster dat zij zonder grote extra reistijd kan worden toegevoegd?

## Additieve nummering
Nieuwe fysieke kandidaatlocaties krijgen een NIEUW permanent ID/nummer volgens het bestaande nummeringssysteem. Bestaande IDs/nummers worden nooit hergebruikt, verschoven of hernummerd.

## A/B/C
Elke nieuw toegelaten kandidaat krijgt een eigen A/B/C-beslissing van Mark. Geen automatische afleiding uit nabijheid of overlap.

Voor bestaande B/C-locaties geldt:
- nieuwe nabijheids-/combinatie-informatie kan een `REVIEW_FOR_UPGRADE` triggeren;
- alleen Mark kan B→A, C→B/A of andere keuze wijzigen;
- bestaande A/B/C wordt nooit automatisch verlaagd.

## Reiswaarde-signalen
Mark moet expliciet gewezen worden op:
- multi-person exact same-site;
- multi-person same-city/cluster;
- persoonsgebonden accommodatie waar daadwerkelijk verbleven werd;
- zeer korte detour vanaf een bestaande A/B-locatie of verblijf;
- locatie die twee of meer bestaande dagroutes logisch verbindt;
- locaties die een eerder zwakke B praktisch aantrekkelijk maken door clustering.

## Cluster-status
Gebruik voortaan twee dimensies:
- `ORIGINAL_CLUSTER_REVIEW_COMPLETE: JA/NEE`
- `REVERSE_DISCOVERY_CURRENT: JA/NEE`

Een cluster is pas route-ready als beide JA zijn voor de laatst bekende persoonsdataset.

## Downstream-impact
Definitieve route/nachten/accommodaties mogen pas worden gefreezed nadat de reverse-discovery pass op alle eerder afgewerkte clusters is uitgevoerd, nieuwe kandidaten IDs hebben gekregen en Mark de noodzakelijke additieve A/B/C-review heeft gedaan.

Geen bestaande locatie wordt door deze regel verwijderd.
# INDIA11 — SOUTH JUMP TRANSFER TOPOLOGY

status: BLOCK_3_COMPLETE_PROVISIONAL
updated: 2026-08-26
branch: agent/india8-cluster-casting
web_recheck: 2026-08-26

## PURPOSE
Bounded Block 3 only. Compare the practical gateways from the fixed eastern pilgrimage worlds to the fixed Tiruvannamalai/Arunachala world using full occupied travel-day cost.

No global stitch, no exact calendar dates, no sightseeing addition and no new A/B/C decisions are authorized here.

## PROTECTED WORLDS — NOT RE-GRADED
- `BODH GAYA / BODH GAYA / Mahabodhi Temple Complex (Boeddha-verlichtingscomplex) — huidige status: A+`.
- `VARANASI / SARNATH / Sarnath sacred complex (Boeddhistische heilige en archeologische wereld van de eerste leerrede) — huidige status: A+`.
- `VARANASI / ASSI GHAT / HOTEL Sahi River View Guesthouse (door Mark gekozen verblijf aan/naast Assi Ghat) — accommodatie-status: LOCKED_BY_MARK`.
- `ARUNACHALA / TIRUVANNAMALAI / Arunachala / Ramana sacred world (heilige berg, Sri Ramanasramam en directe Ramana Maharshi-levensplekken) — huidige status: A+`.

## S1 — VARANASI -> CHENNAI -> TIRUVANNAMALAI
Current 2026-08-26 evidence:
- IndiGo 6E6044 is currently operating direct Varanasi (VNS) -> Chennai (MAA), scheduled around 10:55 -> 13:10 on the current August pattern; block about 2h15;
- current schedule evidence shows it is not necessarily daily, so actual Dec 2026 / Jan 2027 operating day must be rechecked later;
- `VARANASI / ASSI GHAT / HOTEL Sahi River View Guesthouse (...) — accommodatie-status: LOCKED_BY_MARK` -> VNS is about 28 km; raw taxi ~28 min, practical normal-traffic class about 40–60 min;
- Chennai Airport -> Tiruvannamalai road distance is about 171.6 km / ~2h31 raw drive.

Conservative door-to-door model:
1. HOTEL checkout/loading + Assi Ghat -> VNS: ~1–1.5h operational block;
2. domestic airport buffer: ~1.5–2h;
3. direct flight: ~2h15 scheduled;
4. arrival/baggage/driver pickup: ~0.5–1h;
5. MAA -> Tiruvannamalai private driver: budget ~3–4h operationally rather than 2h31 raw, allowing pickup, traffic and one stop;
6. HOTEL arrival/check-in/food/rest: ~0.5–1h.

Working occupied-time class:
`~9–11h HOTEL-to-HOTEL / SUBSTANTIAL_TO_FULL_TRAVEL_DAY`.

The route is still much stronger than rail because it preserves a single waking travel day instead of a 30+ hour long-distance train journey.

Sources rechecked 2026-08-26:
- https://www.flightstats.com/v2/flight-tracker/6E/6044?date=26&flightId=1404395310&month=08&year=2026
- https://www.flight.info/6E6044
- https://www.rome2rio.com/s/Assi-Ghat/Varanasi-Airport-VNS
- https://www.rome2rio.com/s/Tiruvann%C4%81malai/Chennai-Airport

Status:
`PRIMARY_SOUTH_GATEWAY_HYPOTHESIS / ACTUAL_DATE_RECHECK_REQUIRED`.

## S2 — VARANASI -> BENGALURU -> TIRUVANNAMALAI
Current evidence:
- Air India Express currently publishes daily nonstop Varanasi -> Bengaluru service, fastest direct block about 2h35; exact frequencies/times can vary;
- Bengaluru Airport -> Tiruvannamalai is about 231.5–232.7 km / ~3h33–3h34 raw drive.

Conservative door-to-door interpretation:
- same Varanasi HOTEL -> airport and domestic-terminal overhead as S1;
- flight slightly longer;
- post-flight road leg is about 60 km longer and roughly one raw hour slower than Chennai Airport -> Tiruvannamalai;
- private-driver operational road block should be treated around ~4–5h before HOTEL arrival transition.

Working occupied-time class:
`~10–12.5h HOTEL-to-HOTEL / FULL_TRAVEL_DAY`.

Strength:
- currently stronger frequency signal than VNS->MAA and therefore a robust fallback.

Weakness:
- structurally longer road tail to the actual A+ destination.

Sources rechecked 2026-08-26:
- https://flights.airindiaexpress.com/en-in/varanasi-to-bengaluru-flights
- https://www.rome2rio.com/s/Bengaluru-Airport-BLR/Tiruvann%C4%81malai

Status:
`STRONG_FALLBACK_GATEWAY`.

## S3 — GAYA -> CHENNAI/BENGALURU BY AIR
Current 2026-08-25/26 route evidence:
- there is presently NO nonstop Gaya (GAY) -> Chennai (MAA);
- there is presently NO nonstop Gaya (GAY) -> Bengaluru (BLR);
- published Gaya->Chennai options require at least one stop, with route engines showing shortest airborne routing via Kolkata around 3h35 before layover time;
- Gaya->Bengaluru likewise requires at least one stop.

Calendar interpretation:
- connection risk + layover + baggage/interface uncertainty erase the apparent advantage of departing directly from the Bodh Gaya/Gaya world;
- after landing in Chennai/Bengaluru the same 3–5h operational road tail to Tiruvannamalai still remains;
- this is therefore a full travel day and normally a more fragile one than finishing the eastern pair in Varanasi and using a nonstop.

Sources rechecked 2026-08-26:
- https://www.flightconnections.com/flights-from-gay-to-maa
- https://www.flightconnections.com/flights-from-gay-to-blr

Status:
`INFERIOR_CURRENT_GATEWAY / DATE_SPECIFIC_FALLBACK_ONLY`.

## S4 — LONG-DISTANCE RAIL TO CHENNAI
Current timetable aggregators show direct/through Varanasi-area -> Chennai rail options in roughly the 31.5–35h+ scheduled class; one common direct Varanasi Jn -> Chennai Central service is about 34h50.

After Chennai arrival, Tiruvannamalai still requires a substantial onward ground/rail movement.

Planning class:
`~1.5 DAYS PLUS / VERY_HIGH_TIME_BURDEN`.

This is not competitive with a working VNS nonstop for this ~32-day trip unless flights become operationally unavailable or Mark explicitly values a long Indian rail experience enough to spend the time.

Sources rechecked 2026-08-26:
- https://www.ixigo.com/by-train-rail/varanasi-to-chennai-by-train
- https://www.rome2rio.com/Train/Varanasi/Chennai

Status:
`NOT_DEFAULT`.

## GATEWAY COMPARISON
### Preferred
`VARANASI/SARNATH -> VNS -> CHENNAI (MAA) -> TIRUVANNAMALAI/ARUNACHALA`

Why:
1. current nonstop flight removes an air connection;
2. Chennai Airport is about 60 km closer by road to Tiruvannamalai than Bengaluru Airport;
3. raw airport-to-destination drive is about one hour shorter;
4. whole move remains one substantial/full travel day rather than a multi-day rail transfer;
5. this rewards the Block 2 provisional east order that finishes the fixed eastern pair in Varanasi/Sarnath, but Block 3 independently reaches the same conclusion from gateway quality.

### Fallback
`VARANASI/SARNATH -> VNS -> BENGALURU (BLR) -> TIRUVANNAMALAI/ARUNACHALA`

Use when the actual-date VNS->MAA nonstop is unavailable, badly timed or materially worse in fare/availability. Bengaluru sightseeing is NOT implied by airport use.

### Downranked
`BODH GAYA/GAYA -> GAY -> connecting flight -> south gateway -> TIRUVANNAMALAI/ARUNACHALA`.

No reason currently exists to reverse the fixed eastern pair merely to fly from Gaya.

## BLOCK 3 CONCLUSION
`VARANASI/SARNATH -> direct VNS->MAA when operating -> road MAA->TIRUVANNAMALAI/ARUNACHALA` is the strongest provisional south-jump topology.

Working class: `~9–11h HOTEL-to-HOTEL / SUBSTANTIAL_TO_FULL_TRAVEL_DAY`.

Bengaluru is a strong one-day fallback at roughly `~10–12.5h` door-to-door. Gaya flight connections and 30+ hour rail options are materially inferior at current zoom level.

## FRESHNESS GATE
Current August 2026 operation proves the route exists now; it does NOT lock a December 2026 / January 2027 flight. Recheck actual trip date, exact operating day, baggage/fare and driver connection only when the calendar reaches booking relevance.

## FRONTIER
BLOCK 3 SOUTH = `COMPLETE_PROVISIONAL`.

The next bounded autonomous scope is BLOCK 4 GLOBAL STITCH, per `TASK_SPLIT_2026-08-26.md`. Exact dates remain blocked.
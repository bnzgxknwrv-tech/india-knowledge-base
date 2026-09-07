# FINAL TRIP — LIVE RECHECK REGISTER

Date: 2026-09-07

Status: **ARCHITECTURE CLOSED ENOUGH / BOOKINGS AND LOCAL ACCEPTANCE OPEN**

## Rule

`CAN CLOSE NOW` means the fact is sufficiently stable to govern architecture. `LIVE_RECHECK_LATER` means the present pattern may guide planning but must not be represented as a guaranteed December 2026/January 2027 product.

## Can close now

| Fact | Closure | Evidence/confidence |
|---|---|---|
| Weekdays | 19 Dec 2026 is Saturday; 31 Dec Thursday; 1 Jan 2027 Friday; 3 Jan Sunday; 11 Jan Monday; 14 Jan Thursday; 20 Jan Wednesday; 21 Jan Thursday | deterministic / HIGH |
| Trip envelope | 33 accommodation/overnight-transport slots between first India night and final Delhi night | current project convention / HIGH |
| World scope | Haidakhan IN; Kolkata/Dakshineswar cluster [A+] `LOCKED_BY_MARK`; Puri, Serampore and Vrindavan/Braj OUT | central final-world lock plus workerbranch Mark-truth addendum commit `71c3fc5b973212e9dfbd25da0ebb276d67b0c7cc` / HIGH |
| Kolkata sleep geography | Dakshineswar–Belur spiritual core is preferred; pleasant nearby accommodation is baseline; YSS lodging is upside only after explicit lineage/eligibility confirmation | newest Mark-direct decisions at current central HEAD / HIGH |
| Locked durations | Kumaon 9, Agra 1, Bodh Gaya 2 default/3 conditional, Varanasi 8, Tiruvannamalai 5, final Delhi 1 preferred | current owner files / HIGH |
| Base arithmetic | Kolkata proxy 3 leaves exactly 1 spare slot; recommended deployment is Chennai positioning on 19 Jan | recounted date-by-date / HIGH |
| Taj Mahal closure | Friday closed for general viewing; Thu 31 Dec is structurally valid | official <https://www.tajmahal.gov.in/> / HIGH |
| Belur museum recurring closure | Monday and holidays; 11 Jan is Monday | official <https://belurmath.org/ramakrishna-sangraha-mandira-museum/> / HIGH |
| Kalpataru Day identity | 1 Jan at Cossipore Udyanbati commemorates Sri Ramakrishna's 1886 event | official site <https://rkmudyanbati.org/> / HIGH |
| Geographic mode | Dunagiri–Haidakhan and Kumaon mountain last miles have no rational passenger-rail substitute; Chennai airport–Tiruvannamalai needs road for the comfortable direct pattern | route topology / HIGH |
| Current railway ARP rule | normal advance reservation period is 60 days excluding journey date; special trains/quotas and foreign-tourist booking can differ | Ministry of Railways/PIB <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2065879> / HIGH as of 7 Sep 2026 |

## Top 5 live rechecks

1. **All three overnight trains and First AC inventory:** 15013 on 19 Dec, 15014 on 29 Dec, 12988 on 31 Dec. Recheck at the applicable IRCTC opening instant, again 30 days before, 7 days before and day-of; use First AC (railklasse 1A) first, 2A only as explicit fallback.
2. **Exact 2027 domestic flights:** VNS–CCU 11 Jan, CCU–MAA 14 Jan and MAA–DEL 20 Jan. Select humane daytime nonstops with same-day fallbacks; recheck now/when winter schedule is loaded, 90 days, 30 days, 7 days and 48 hours before.
3. **Haidakhan Vishwa Mahadham acceptance and true road entrance:** written stay acceptance, required participation, arrival window, driver route, KGM vs HDW exit. Close before non-refundable bookings; reconfirm 30 days, 7 days and 48 hours before each transfer.
4. **Kolkata remaining site grades, true duration and exact spiritual-core lodging:** the core is now Dakshineswar Kali Temple [A+], Yogoda Satsanga Math, Dakshineswar [A+] and Belur Math [A], with Dakshineswar–Belur sleep geography preferred. Mark's separate grading must still decide which other candidates survive and whether 2/3/4 nights are justified. YSS lodging is not assumed available.
5. **Sri Ramanasramam/Pongal accommodation and 2027 programme:** obtain acceptance and exact 14–18 Jan access/programme before non-refundable air/hotel commitments; reconfirm 30 days and 7 days before.

## Full volatile-fact register

| Priority | Item/date | What must be proven | Ideal first recheck | Later rechecks | Trigger/fallback if adverse | Current state |
|---:|---|---|---|---|---|---|
| 0 | 15013 Ranikhet Express, GGN approximately 20:02 -> KGM approximately 05:05, 19–20 Dec | operating date, exact station times, coach consist, First AC ticket inventory, boarding station, punctuality history | applicable IRCTC/foreign-tourist-quota opening; normal 60-day reference is around 20 Oct, but calculate from train-origin date in IRCTC | 30 d, 7 d, 48 h, day-of NTES | First AC unavailable -> explicit 2A fallback; service changed -> best later rail preserving Nirmal/hotel recovery; Delhi hotel costs one movable slot | `LIVE_RECHECK_LATER` |
| 0 | 15014 Ranikhet Express, KGM/HDW -> Delhi Cantt, 29–30 Dec | exact KGM/HDW times, First AC, best boarding point after true Haidakhan road, winter performance | normal 60-day reference around 30 Oct; verify origin-date rule | 30 d, 7 d, 48 h, day-of NTES | choose KGM or HDW by confirmed road; cancellation -> plains hotel/next rail and consume movable slot | `LIVE_RECHECK_LATER` |
| 0 | 12988 Ajmer–Sealdah Superfast, Agra Fort -> Gaya, 31 Dec–1 Jan | daily operation, 18:45/07:50-class timing, First AC coach/inventory, year-end/fog punctuality | normal 60-day reference around 1 Nov; verify the train's Ajmer origin date | 30 d, 7 d, 48 h, day-of NTES | First AC unavailable -> explicit 2A; forecast/operations bad -> alternative overnight rail; arrival after approximately 10:30 activates Bodh-duration/buffer review | `LIVE_RECHECK_LATER` |
| 0 | 20887 Vande Bharat, Gaya 09:55 -> Varanasi 13:00, Sun 3 Jan | actual Sunday service, exact time and EC/CC inventory; current sources have inconsistent historical off-day labels | normal 60-day reference around 4 Nov, adjusted for origin date | 30 d, 7 d, 48 h, day-of NTES | if not running, choose next humane direct rail; do not call EC “First AC” | `LIVE_RECHECK_LATER` |
| 0 | 12050 Gatimaan, NZM 08:10 -> Agra Cantt approximately 09:50–10:05, Wed 30 Dec | exact current arrival, running day, ticket inventory, station platform; 15014 connection reliability | normal 60-day reference around 31 Oct, subject to any special shorter ARP | 30 d, 7 d, 48 h, live after 15014 departure | miss -> later train or road; Agra hotel remains fixed | `LIVE_RECHECK_LATER` |
| 0 | Delhi Cantt -> Hazrat Nizamuddin, 30 Dec | live dawn road time and 15014 platform exit/12050 check-in margin | 30 d with map/day-of-week model | 7 d, 48 h, on arrival | prebook driver; if 15014 >90 min late, enact later rail/road fallback rather than sprint | `LIVE_RECHECK_LATER` |
| 0 | VNS–CCU nonstop, 11 Jan | exact winter schedule, baggage terms, humane arrival; current direct service class approximately 1 h 20 | when winter schedule is saleable; no later than 90 d | 30 d, 7 d, 48 h | avoid 20:50-class late flight if a daytime direct exists; cancellation -> same-day direct; overnight rail only if movable slot is intentionally spent | `LIVE_RECHECK_LATER` |
| 0 | CCU–MAA nonstop, 14 Jan | exact flight/time/frequency during Gangasagar/Pongal demand | now/when winter schedule saleable; no later than 90 d | 30 d, 7 d, 48 h | choose service landing early enough for daylight road; multiple-carrier same-day fallback | `LIVE_RECHECK_LATER` |
| 0 | MAA–DEL nonstop, 20 Jan | morning nonstop arriving Delhi by early afternoon; terminal; same-day alternatives | now/when schedule saleable; no later than 90 d | 30 d, 7 d, 48 h | cancellation -> next same-day nonstop; if corridor looks operationally unstable at 7 d, objectively reconsider Jan19 Delhi arrival with Mark | `LIVE_RECHECK_LATER` |
| 0 | Haidakhan Vishwa Mahadham — riverashram at Village Haidakhan, 26–29 Dec | written room/stay acceptance, arrival/departure windows, obligatory participation, meals, luggage, payment | immediately, before non-refundable rail/road | 90 d, 30 d, 7 d, 48 h | accommodation refusal is a genuine blocker requiring Mark/regie action; do not silently select a different Haidakhan entity | `LIVE_RECHECK_LATER` |
| 0 | True Haidakhan roads, 26 and 29 Dec | driver-confirmed route from Dunagiri Retreat and to KGM/HDW, exact entrance, winter conditions, distance conflict | obtain route trace/driver quote at booking | 30 d, 7 d, 48 h | earlier daylight start; select gateway only after proof | `LIVE_RECHECK_LATER` |
| 0 | Sri Ramanasramam/Tiruvannamalai, 14–19 Jan | stay acceptance, Pongal/Mattu Pongal programme, dining/meditation access, temple traffic | immediately before flight/hotel lock | 90 d, 30 d, 7 d | keep 5 nights; adjust internal programme only, not duration silently | `LIVE_RECHECK_LATER` |
| 1 | Kolkata/Dakshineswar module, 11–14 Jan | grades for non-core candidates, 2/3/4 true nights, exact pleasant lodging in the preferred Dakshineswar–Belur zone; explicit YSS eligibility if attempted | separate Mark grading and lodging enquiry as soon as possible | after grades; before hotel/flight lock | exact property may change airport/local transfers by roughly 30–90+ min; macro-order remains modular unless duration becomes >4 | `UNVERIFIED_DEPENDENCY` |
| 1 | Gangasagar Mela 2027 | official government dates, Kolkata transit camps/diversions, Howrah/Sealdah/airport effect | when West Bengal 2027 circular appears; check monthly from Oct | 30 d, 7 d, 48 h | preserve 14 Jan southbound departure; move flight earlier in day if road controls announced | `LIVE_RECHECK_LATER` |
| 1 | Belur Math/Dakshineswar/YSS local access, 11–13 Jan | exact opening blocks, ferry operation, photography/bag rules, special closures | 30 d | 7 d, 48 h | schedule museum Tue/Wed; use road/metro if ferry unreliable | `LIVE_RECHECK_LATER` |
| 1 | Bodh Gaya events, 1–3 Jan | authoritative 2026–27 teaching/puja calendar, security, Mahabodhi access | monthly from Oct; definitive 30 d | 7 d, 48 h | do not add a third night solely on an unverified listing; third night only under current named triggers | `LIVE_RECHECK_LATER` |
| 1 | Yogoda Satsanga Sakha Ashram, Dwarahat, Fri 25 Dec | visitor acceptance/opening on Christmas and round-trip road time from Dunagiri base | 90 d/direct contact | 30 d, 7 d, 48 h | preserve the protected day; if closed, escalate content handling rather than invent replacement | `LIVE_RECHECK_LATER` |
| 1 | Mahavatar Babaji's Cave trail, 24 Dec | safe trail/road state, local guide/vehicle, daylight/weather | 30 d | 7 d, 48 h, morning-of | unsafe conditions -> use remaining Dunagiri window only if YSS day remains intact | `LIVE_RECHECK_LATER` |
| 1 | Hotel Evelyn dawn access, 20 Dec | guaranteed early room vs paid previous-night hold vs accepted lobby wait | at hotel booking | 30 d, 7 d, 48 h | Mark accepts up to approximately 3 h wait; do not count a paid unused room as a physical extra sleep slot | `LIVE_RECHECK_LATER` |
| 1 | Taj Mahal, 31 Dec | online ticket/entry slot, sunrise, security rules, exceptional closure | when official ticket inventory opens | 30 d, 7 d, 48 h | use earliest practical entry; Friday closure is not a problem on Thu 31 Dec | `LIVE_RECHECK_LATER` |
| 1 | Hotels across year-end/Pongal | actual availability and cancellation terms in Nainital, Agra, Bodh Gaya, Kolkata, Tiruvannamalai, Chennai, Delhi | immediately for refundable holds | 90 d, 30 d, 7 d | prioritize scarce ashram/Tiru/Kumaon inventory; no hotel selection change becomes canon without Mark process | `LIVE_RECHECK_LATER` |
| 2 | North-Indian fog for 19–20, 29–31 Dec, 1–11 and 20–21 Jan | route-specific forecast, train delay/cancellation, DEL visibility | seasonal watch 30 d | 7 d, 72 h, 48 h, day-of | release movable Jan19 night upstream only after actual disruption; keep final Delhi hotel | `LIVE_RECHECK_LATER` |
| 2 | Kumaon winter roads | rain/snow/ice, sunrise/sunset, closures | 30 d | 7 d, 48 h, morning-of | daylight departures; driver-local judgement; no night mountain push | `LIVE_RECHECK_LATER` |
| 2 | AI155 final departure | terminal, check-in deadline, schedule | 30 d | 7 d, 48 h, day-of | arrive Delhi 20 Jan under base; airport hotel; target terminal around 09:20 unless airline says otherwise | `LIVE_RECHECK_LATER` |

## Railway booking dates: safe interpretation

The Ministry of Railways currently states 60 days excluding the journey date for the normal Advance Reservation Period. It also notes exceptions; foreign-tourist arrangements and the train's originating date can alter what appears for an intermediate boarding station. Therefore the dates above are **monitoring references, not promises of an exact opening timestamp**. For each train, inspect IRCTC against its origin date and quota before the reference day, and book at the first applicable legitimate opening.

## Blockers

- **No blocker to central adoption of the macrospine.**
- **Booking blocker:** future rail inventory and exact winter flight schedules are not all guaranteed.
- **Local-content blocker:** Kolkata true duration and exact itinerary cannot close until Mark grades the non-core deep-pass candidates; sleep geography itself is now Mark-preferred around Dakshineswar–Belur, but the property and YSS eligibility remain open.
- **Accommodation blocker if adverse:** written acceptance from Haidakhan Vishwa Mahadham and the relevant Tiruvannamalai/Ramanasramam lodging must be obtained.

END

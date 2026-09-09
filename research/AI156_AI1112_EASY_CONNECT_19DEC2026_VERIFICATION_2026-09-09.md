# AI156 -> AI1112 EASY CONNECT — 19 DEC 2026 VERIFICATION

Date checked: 2026-09-09
Status: `PROCEDURE_PASS__EXACT_DATE_ONE_PNR_INVENTORY_UNVERIFIED`
Branch: `agent/india8-cluster-casting`

## DECISION-SHORTCUT

Air India officially confirms the exact combination **AI156 Amsterdam -> Delhi + AI1112 Delhi -> Varanasi 13:35** as an eligible inbound Easy Connect example when the connection is <=4 hours. The Easy Connect process itself is therefore VERIFIED.

However, public web evidence available on 2026-09-09 does **not yet prove that the exact 18/19 Dec 2026 journey is offered as one protected booking / one PNR with AI1112**. Therefore Varanasi-first is a `LEADING_CONDITIONAL`, not a final route lock.

## DATE SEMANTICS

- International departure: Amsterdam on **18 Dec 2026**.
- AI156 arrival / domestic connection: Delhi on **Sat 19 Dec 2026**.
- When searching Air India inventory, search **AMS -> VNS departing 18 Dec 2026**, not a separate DEL -> VNS ticket for 19 Dec.

## 1. OFFICIAL EASY CONNECT RULE — PASS

Air India's current Hub & Spoke / Easy Connect page states:
- Easy Connect applies inbound international -> India as well as outbound;
- the booking must include an AI 11xx sector;
- the ticket must include an international sector;
- connection time must be 4 hours or less.

The same official page gives the exact inbound example:
- `AI156 [AMS-DEL]` arrival Delhi `09:55`
- `AI1112 [DEL-VNS]` departure Delhi `13:35`
- AI11xx = yes
- international sector = yes
- <=4 hours = yes
- result: `Easy Connect - Hub & Spoke Booking`.

For qualifying inbound Easy Connect itineraries Air India says:
- checked baggage goes directly to the final Indian destination;
- passenger does not collect/recheck baggage at Delhi;
- immigration and customs are completed at the final Indian destination (e.g. Varanasi), not at the Delhi hub.

Source: Air India, Hub & Spoke / Easy Connect page, checked 2026-09-09.

## 2. BOOKING WINDOW / ROUTE EXISTENCE — PASS

Air India currently markets Amsterdam -> Varanasi as a connecting itinerary on its own website. Its route page states bookings can be made up to 361 days ahead. The 18 Dec 2026 departure is therefore already inside the normal booking horizon as of 9 Sep 2026.

This proves that the route is a live commercial Air India city-pair and that the date is not outside the advance-purchase window.

It does NOT by itself prove the exact AI156+AI1112 inventory on one PNR.

## 3. IMPORTANT WINTER-SCHEDULE AMBIGUITY

Air India's official Winter 2026 network release, effective 25 Oct 2026, separately publishes a Delhi -> Varanasi flight on Tue/Thu/Sat:
- `AI2567 DEL 13:25 -> VNS 14:50`.

19 Dec 2026 is Saturday. The same release explicitly says these flights are timed for seamless Delhi connections to/from Europe, including Amsterdam.

This creates an unresolved numbering/inventory question:
- the Easy Connect page uses `AI1112 DEL-VNS 13:35` as the qualifying AI11xx example;
- the published Winter 2026 Saturday schedule also shows `AI2567 DEL-VNS 13:25`.

Do NOT guess whether AI1112 coexists, overlays, replaces, or is commercially mapped to the winter AI2567 service. Only the actual Air India booking result for 18 Dec can settle that.

## 4. EXACT SUCCESS CRITERION FOR A HARD PASS

The route becomes `EASY_CONNECT_EXACT_DATE_PASS` only if Air India (website/app/contact centre/travel agent using Air India inventory) shows:

1. one itinerary `AMS -> VNS` departing **18 Dec 2026**;
2. first sector `AI156 AMS -> DEL`;
3. onward Delhi -> Varanasi sector in the qualifying `AI11xx` Easy Connect series, ideally `AI1112` as in Air India's official example;
4. both sectors issued as one protected booking / one PNR / one ticketed itinerary;
5. connection <=4 hours according to the ticketed times.

If the domestic sector is instead AI2567/AI2623 or another non-AI11xx flight, it may still be a normal protected one-ticket connection, but it is NOT proven to receive the special Easy Connect inbound process. Evaluate that separately rather than calling it Easy Connect.

## 5. ROUTE CONSEQUENCE

Current route status after this verification:

`VARANASI_FIRST = LEADING_CONDITIONAL`

Reason:
- Easy Connect procedure for exact AI156+AI1112 is officially VERIFIED;
- first-night recovery and direct arrival in Varanasi are potentially strong whole-human advantages;
- but the exact 18/19 Dec one-PNR AI11xx inventory remains unverified.

Fallback remains the established Kumaon-first architecture until the exact one-PNR check passes. Gaya-first via official AI429 remains a real challenger, not an impossibility.

Do not lock/reorder the trip solely from the generic Easy Connect example.

## 6. WHAT NOT TO RESEARCH AGAIN

Do not re-litigate whether Air India permits inbound Easy Connect in principle: it does.
Do not re-litigate whether AI156+AI1112 is an official qualifying example: it is.
Do not claim exact-date bookability until one-PNR inventory is observed.
Do not use an aggregator's missing flight result to overrule current official Air India material.

## NEXT CHECK

Perform the narrow live inventory test:
`AMS -> VNS, one way, departure 18 Dec 2026` on Air India.

Record the displayed segment numbers, exact times, whether the itinerary is one booking, and whether Air India labels/qualifies it as Easy Connect.

END
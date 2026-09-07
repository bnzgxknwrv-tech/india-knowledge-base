# FINAL BOOKABLE DAY CALENDAR — RECONCILIATION WITH INDEPENDENT CHECK

Date: 2026-09-07

Worker branch: `worker/final-route-calendar-optimizer`

Reconciles `FINAL_EXACT_33_SLOT_BOOKING_CALENDAR_CANDIDATE_2026-09-07.md` (this branch, commit `6c75c95`) against the independent audit at `worker/final-bookable-calendar-independent-check`, commit `2879705`, VERDICT `PASS_WITH_CORRECTIONS`.

## Full consensus, no disagreement

- 33-slot arithmetic: no missing/duplicated night, confirmed independently.
- Kumaon winner: Nainital → Dunagiri/Kukuchina → Haidakhan → rail gateway, confirmed independently.
- Recommended cell: Bodh Gaya 2n + Kolkata 3n (Cell B), confirmed independently, including exact dates.
- Cell C/E (0 Chennai-buffer variants): independently confirmed as a real robustness degradation, not a free content gain — matches this branch's MARGINAL rating.
- Cell F (Bodh3+Kolkata4): independently confirmed as not fitting (34/33).
- 20887 six-day service pattern (Sun/Mon/Wed/Thu/Fri/Sat, no Tue): confirmed; both Sun 3 Jan (Bodh2) and Mon 4 Jan (Bodh3) are valid under it.

## Corrections adopted from the independent check

1. **Belur Math museum — National Youth Day closure.** The Ramakrishna Sangraha Mandira museum is closed both on Mondays and on listed holidays, including **12 January (National Youth Day)** — independently plausible and consistent with 12 January's well-established status as Swami Vivekananda's birth anniversary/National Youth Day in India. In the recommended Cell B (Kolkata nights 11–13 Jan), this means **13 Jan, not 12 Jan, is the first day the museum can be included** — the wider Belur Math temple/campus itself is not closed and can still be visited 12 Jan; only the museum component moves.
2. **Cell C/E depart Kolkata on the exact Makar Sankranti/Pongal day, not merely "before the peak."** The independent check fixes Makar Sankranti/Pongal to **Fri 15 Jan 2027** under the current festival calendar, and Cell C/E's Kolkata checkout and CCU→MAA travel fall on exactly that date. This is a sharper, more specific version of this branch's existing MARGINAL rating for those cells — strengthens rather than contradicts it.
3. **Old Delhi (DLI) alighting on 15014, 30 Dec.** If the timetable in effect at booking time still stops 15014 at Old Delhi (~04:10) before continuing to Delhi Cantt (~05:03), alighting there and transferring to Hazrat Nizamuddin for 12050 (08:10) gains roughly 53 minutes of scheduled bridge with no new hotel night and no route change. Adopted as the preferred execution detail for this transfer; the transfer keeps its MARGINAL rating structurally (it is still a cross-city connection) but is meaningfully de-risked by this choice if available at booking time.
4. **FTQ nuance.** IRCTC's Foreign Tourist Quota allows booking up to 365 days ahead for eligible international users, but if booked earlier than the normal 60-day Advance Reservation Period, **berth allocation itself is deferred until the normal ARP window opens** — FTQ moves the booking request earlier, not the seat-confirmation certainty. The action calendar's "use FTQ where advantageous" guidance should be read with this caveat rather than as "FTQ removes the 60-day wait."
5. **Varanasi/VNS→CCU dates are not independent of the Bodh Gaya 2/3 contingency**, even though they are independent of the Kolkata-duration choice. `FINAL_BOOKABLE_DAY_CALENDAR_LOCK_PASS_2026-09-07.md` §9 listed Slots 1–23 as uniformly "safe to lock now" — that remains true with respect to Kolkata, but Varanasi's exact dates (3–11 Jan under Bodh2 vs. 4–12 Jan under Bodh3) still move with the live Bodh Gaya trigger. Varanasi and VNS→CCU should be booked/held with date-change or free-cancellation terms, not treated as fully date-fixed the same way Slots 1–12 (Delhi through Agra/Bodh Gaya arrival) are.

None of these corrections change the recommended candidate, the Kumaon order, or the 33-slot arithmetic. They tighten execution detail within the already-recommended Cell B and sharpen (not soften) the case against Cell C/E.

END

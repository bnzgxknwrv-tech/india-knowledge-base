# ANANDAMAYI R4/R5 CLOSURE — INDIA WIT

status: COMPLETE_WITH_GOVERNANCE_SCHEMA_BLOCKER
verified_at: 2026-08-20
branch: `agent/indiawit-master-travel-readiness`

## Governance blocker

TASK.md requires R1–R5, and explicitly points to `governance/LOCATION_RESOLUTION_BEFORE_ABC_2026-08-19.md`. That file is not present on this branch at the stated path, and repository search on this branch did not return it. WIT therefore does **not** invent R1–R5 definitions. All entity records retain `rank: UNASSIGNED_GOVERNANCE_SCHEMA_MISSING`. This prevents silent semantic corruption while still completing physical identity/access/bookability work.

## Lossless reconciliation state

- All external-union records `L001`–`L156` are retained by exact source ID in `ANANDAMAYI_SOURCE_RECORDS.jsonl`.
- INDIA source-first additions are retained as separate detector occurrences; identity overlap never deletes the source-first occurrence.
- CCI_TASK 084 verification remains a third separate detector/reconciliation layer.
- Known false/weak claims remain visible: Rajghat Besant School as the Krishnamurti meeting site is **WEERLEGD**; correct event site is Kitty Shiva Rao's Delhi garden. Vashishta Guha and Badrinath remain unverified. L104–L106 station claims remain unverified. L156 Mandi remains likely compilation artefact unless a real source passage is supplied.
- Karar Ashram remains open specifically for Anandamayi Ma: exact Karar site is real and strong for Sri Yukteswar/Hariharananda, but CCI084 did not close Anandamayi's claimed 1942/43 stay. No three-person upgrade is made.

## Highest-impact physical closures

### Varanasi — Bhadaini
`Shree Shree Ma Anandamayi Ashram, Bhadaini, Varanasi 221001` is a current exact institutional continuation. The official Anandamayi site currently publishes a specific room-booking contact and a separate local dharamshala contact. Therefore current overnighting at the Bhadaini ashram ecosystem is **JA**, but no historic bedroom of Ma has been identified or declared bookable.

Current source: `https://www.anandamayi.org/ashram-contact-details/`.

### Kankhal — preserved final bedroom
The official Sangha institutions page identifies a bungalow built for Ma by S.N. Ghosh and Ranu Ghosh. Ma stayed there for about the final two months before Mahasamadhi. The building is now the `Matri Smriti Museum and Research Centre`; Ma's **bedroom** and **kitchen** are explicitly maintained as such. This closes a high-value room-level heritage entity.

- physical building: **JA**
- exact historic bedroom: **JA, institutionally preserved**
- visitor access: **JA as museum/heritage room**
- overnight in that bedroom: **NEE**
- modern same-precinct overnight: **JA** at the adjoining Shree Shree Ma Anandamayee International Centre.

Current sources:
- `https://www.anandamayi.org/sangha-schools-and-institutions/`
- `https://www.anandamayi.org/international-center/`
- `https://ssmaic.org/`

### Kankhal — present accommodation
The official Anandamayi contact page publishes booking contacts for Kankhal. The International Centre describes itself as a retreat centre adjoining Ma's Ashram and Samadhi Mandir and currently offers rooms. It is a modern devotional stay, **not** Ma's historic bedroom.

### Vrindavan
The current Anandamayi organisation lists the Vrindavan Ashram and current contacts, and specifically links `Vardhaman Kunj`. CCI084 independently confirmed Ma resided at `Burdwan Kunj` in 1936. Name/continuity is therefore a strong follow-up entity, but current public material reviewed here does not establish that the historic room/building is bookable. Status: **current lineage location exists; same historic room ONZEKER**.

### Dehradun institutional cluster
The current official contact page resolves present addresses for several durable source-layer residences:
- Kishenpur Ashram, P.O. Rajpur, Dehradun 248009;
- Kalyanvan, 176 Rajpur Road, Rajpur, Dehradun 248009;
- Raipur Ashram, P.O. Raipur Ordnance Factory, Dehradun 248010;
- Sadhan Ashram, 47/A Jakhan, Rajpur, Dehradun.

These are current physical institutions/contactable sites. Public overnight policy for the exact historical stay spaces was not established; no same-room claim is promoted.

### Almora / Dhaulchina
The official Anandamayi site lists both Patal Devi and Dhaulchina as current ashrams. Current visiting guidance describes Dhaulchina as hermitage-like and gives a restriction that women travelling alone are not allowed to stay there. This is a real overnight-policy signal, but no historical Ma room is identified.

### Puri
The current organisation still lists `Shree Shree Ma Anandamayi Ashram, Swargadwar, Puri`. A separate current room-booking site using the Anandamayi/Sangha identity advertises Puri rooms and numeric modern room numbers. Those numbers are **modern inventory only** and are not linked to Ma; none are copied as historic room numbers. Because the authority chain of that booking domain was not established as strongly as `anandamayi.org`, current Puri accommodation is recorded as **booking signal exists; direct official confirmation required**.

### Ranchi
The official Anandamayi contact page lists the current Main Road Ranchi ashram. CCI084 directly confirmed the separate source-first claim that Ma **resided at Ratu Palace** in December 1976 at the Maharaja's invitation. Ratu Palace is therefore a high-value historic stay entity, but this audit found no authoritative public hotel/guest booking offer for the palace. Do not equate a modern commercial Ratu/Ranchi property with it.

### South/east data preserved despite route parking
The following source-first stays remain fully retained and were not removed because current route emphasis is elsewhere: Raj Bhavan Madras, Raj Bhavan Bhubaneswar, M.S. Subbulakshmi/T. Sadasivam residence and purpose-built lawn hut, Ganga Vihar Dharamshala Bithoor, Naini Jaipuria House, Hawa Mahal Gondal, Morvi Palace, Dr. Channa Reddy residence Secunderabad, Panchmarhi purpose-built hut, Bhasa residence Calcutta, and other named eastern/southern host properties. Where public continuity could not be proven safely, status stays `UNRESOLVED_CURRENT_BUILDING` rather than being matched by name.

## Unresolved high-value physical identities

1. **Pandey Dharamshala, Varanasi** — historic stay confirmed, present building/address unresolved.
2. **Baghat House, Haridwar** — repeated stay confirmed in 1953 and 1961, present property unresolved.
3. **Bhola Giri/Giriji Ashram, Kankhal** — historic residence confirmed; exact current institution/property match not safely closed.
4. **Salogra Temple cave, Solan** — exact historic cave-stay claim confirmed; a contemporary Solan cave result cannot be equated without lineage/parcel evidence.
5. **Ganga Lahari / Birla Guest House, Raiwala** — one-week stay claim retained; current exact building not closed.
6. **M.S. Subbulakshmi/T. Sadasivam lawn hut, Chennai** — special hut is room-level significant; current survival/address access not closed.
7. **Nitibagh house of G.S. Pathak, Delhi** — source-first says a floor was reserved for Ma; exact address/floor not closed.
8. **Morvi Palace** — source-first royal stay/programme retained, but `Morvi Palace` needs building-level disambiguation before current access/overnight can be stated.

## No silent upgrades

- A current ashram at the same town is not automatically the historic building.
- A modern room number is never treated as Ma's room without archival/institutional proof.
- A palace name in a secondary detector is not upgraded when CCI could only confirm city/royal host context.
- Private houses remain private/unknown unless an owner/institution has made current access public.

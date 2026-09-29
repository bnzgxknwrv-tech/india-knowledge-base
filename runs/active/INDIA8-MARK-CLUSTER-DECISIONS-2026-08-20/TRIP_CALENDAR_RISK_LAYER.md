# Trip calendar / festival / transport-risk layer

Mandatory before final India itinerary is locked.

For every candidate travel date and cluster, check:
- Indian national public holidays
- state-specific public holidays relevant to the cluster
- major Hindu/Buddhist/Jain/Sikh/Muslim/Christian festival dates where locally material
- major pilgrimage/fair/event dates (Kumbh/Magh Mela, Janmashtami, major Arunachala full-moon/Girivalam dates, etc.)
- temple/monument weekly closure days and exceptional closures
- days with exceptional crowding, road closures, security controls, transport shortages or price spikes
- flight/train/road operational impact; do NOT assume a public holiday means flights stop
- whether a festival is a positive experience worth routing toward versus a crowd/transport risk worth routing around

Final itinerary must flag each affected day with one of:
- SEEK_EVENT
- OK_NORMAL
- CROWD_CAUTION
- TRANSPORT_CAUTION
- AVOID_IF_POSSIBLE
- HARD_CLOSURE

Special rule: do not schedule a critical same-day flight/train/long transfer blindly on a major local festival or mass-pilgrimage day. Verify actual transport operations and local access first.

The calendar layer is separate from the Lonely Planet discovery layer and must be applied after likely clusters are known but before final dates/transfers are locked.

# INDIA10-MULTIAI-TRAVELER-DISCOVERY-001 — TASK

status: READY_FOR_INDEPENDENT_WORKERS
repository: bnzgxknwrv-tech/india-knowledge-base
central_branch: agent/india8-cluster-casting
purpose: independent traveler/experience discovery before Mark re-rates clusters
travel_window: approximately 2026-12-19 through 2027-01-21 in India

## WHY
Mark's India trip is primarily a spiritual pilgrimage, but non-person travel discoveries can materially change cluster value and nights. Existing Lonely-Planet-style discovery is useful but was not designed around Mark's now-explicit taste for unusual experiences, hot springs, rafting/adventure, wildlife, strange historical experiences, cult local institutions, exceptional nature and world-class magnets outside a fixed radius.

The goal is DIVERSITY OF SEARCH, not consensus. Different AI systems/workers must search independently before seeing each other's results.

## BLINDNESS — HARD
Before freezing your own discovery output:
- DO NOT read existing Lonely Planet discovery outputs, the existing 80 findings, CCI gap-check, or other workers' outputs.
- DO NOT use another worker's candidate list as a seed.
- You MAY read this TASK only.
- Use fresh public web research and your own search strategy.

After your own output is frozen/committed, central INDIA10 will compare and deduplicate it against existing findings and other workers.

## GEOGRAPHIC FRAME
Current retained or decision-relevant travel world:
- Delhi / Delhi corridors
- Kumaon: Haidakhan; Kathgodam/Haldwani; Nainital/Kainchi/Bhowali; Almora/Kasar; Dwarahat/Kukuchina/Dunagiri
- Haridwar / Kankhal / Rishikesh
- Agra and Delhi–Agra–Mathura/Vrindavan corridor
- Vrindavan / Braj / Mathura / Govardhan
- Prayagraj / Allahabad
- Varanasi / Sarnath
- Bodh Gaya / Gaya
- Tiruvannamalai / Arunachala and realistic arrival/departure corridors

Mysore/Bengaluru is currently an excluded/C-control, not a normal search cluster. Surface something there only if it is genuinely world-/India-level or experientially extraordinary enough that a reasonable traveler might reconsider the exclusion.

This is NOT a hard radius exercise. Search locally, but also run an adaptive WORLD-MAGNET check outside normal cluster bounds. A find 60–150+ km away may be valid if it is genuinely exceptional enough to justify the detour or an extra day. A mediocre find 30 km away is not valid merely because it is close.

## SEASON / DATES
The relevant travel period is late December 2026 through 21 January 2027. Prefer experiences plausibly available then. If a great finding is seasonal, access-limited, weather-sensitive, festival/date-specific or normally unavailable in this window, say so explicitly rather than silently promoting it.

## MARK'S TRAVELER TASTE — IMPORTANT
Examples of the TYPE of discovery that can matter (examples are not India candidates):
- hot springs / unusual bathing or wellness experiences;
- exceptional rafting, cave, climbing or adventure experiences;
- whale/wildlife-like encounters that are genuinely special;
- bizarre historical experiences, such as climbing an old fire-lookout tree;
- very old roadhouses, bakeries, sweet shops, cafes, stores or cult institutions with a story and atmosphere;
- remarkable markets, stations, bridges, streets or transport experiences;
- one specific craft/product/ritual that travelers remember as a trip highlight;
- spectacular short nature experiences, waterfalls, viewpoints, unusual landscapes;
- world-level monuments or attractions that are too important to omit simply because they lie beyond an arbitrary radius.

Do NOT infer that Mark wants museums, temples, adventure or nature in general. The point is to surface genuinely exceptional options so Mark can decide.

## QUALITY THRESHOLD
Prefer 10 excellent findings over 30 ordinary ones. A finding should have at least one of:
- world-level / India-level / exceptional regional uniqueness;
- strong repeated traveler enthusiasm;
- unusual experiential value;
- exceptional beauty/rarity;
- plausible ability to justify an extra half-day/day or a meaningful detour;
- very high reward at almost zero route cost.

Exclude:
- generic city top-10 filler;
- ordinary restaurants/hotels;
- generic temples/museums merely because famous locally;
- person-sweep/historical lineage locations (those are handled separately);
- inaccessible/private experiences;
- dangerous/illegal activities presented as recommendations.

## VISITABILITY
This layer is for things Mark could realistically DO or VISIT as a traveler. Private homes, ordinary hospitals, schools or workplaces are not candidates unless there is a real visitor/memorial/shrine/museum context.

## REQUIRED PER FINDING
- name
- place/region
- category
- what the traveler actually does/sees/experiences
- why exceptional (not merely 'popular')
- traveler signal / repeated praise
- nearest current cluster or corridor
- approximate detour / extra time class
- could plausibly add cluster time? YES / MAYBE / NO (descriptive only, not A/B/C)
- current visitability/seasonality caveat if material
- source URLs
- confidence

## NO DECISIONS
- Do not assign Mark's A/B/C.
- Do not choose clusters, nights, hotels or route.
- Do not downgrade old decisions.
- Discovery only.

## WORKER ROLES

### ROLE A — WEIRD / HUMAN / CULT / MICRO-GEMS
Search traveler forums, Reddit, travelogues, local blogs and specialist sources for strange, atmospheric, small, memorable experiences and institutions that conventional top-10 lists miss.
Output: `MULTIAI_WEIRD_HUMAN.md`

### ROLE B — NATURE / WATER / ADVENTURE / WELLNESS
Search for exceptional water, hot springs, rafting, caves, wildlife, dramatic short walks, viewpoints, unusual landscapes, outdoor activities and genuine experience outliers.
Output: `MULTIAI_NATURE_ADVENTURE.md`

### ROLE C — WORLD MAGNETS / ICONIC EXPERIENCES / OUT-OF-RADIUS
Explicitly challenge fixed-radius thinking. Search for monuments, experiences, landscapes, rituals or attractions near the broader route that could rationally justify a substantial detour or extra day. Include small items only if extraordinary.
Output: `MULTIAI_WORLD_MAGNETS.md`

### ROLE D — BLIND GENERAL TRAVELER SECOND OPINION
Use your own search style. Answer the question: 'What might an experienced curious traveler deeply regret missing along or near this India journey, including things the other obvious categories may overlook?' Do not optimize for agreement with other AI systems.
Output: `MULTIAI_BLIND_GENERAL.md`

## FREEZE RULE
Freeze your own candidate set before looking at any existing project LP/traveler list. State explicitly at top:
`BLIND_DISCOVERY_FREEZE: YES`

Central INDIA10 will later union, verify, deduplicate and present only a manageable high-value set to Mark.

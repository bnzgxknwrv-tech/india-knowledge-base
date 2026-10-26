import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Verified coordinates (lat, lon), sourced from Wikipedia infoboxes (fetched 2026-09-16)
points = {
    "Kathgodam\n(spoorwegstation, eind 29 dec)": (29.268, 79.545),
    "Bhowali\n(wegkruising)": (29.380, 79.520),
    "Nainital\n(Hotel Evelyn, 20-23 dec)": (29.392, 79.454),
    "Almora\n(doorreis, 23 dec)": (29.597, 79.657),
    "Dwarahat\n(YSS, 25 dec)": (29.780, 79.430),
    "Bhimtal\n(nabij Haidakhan Vishwa\nMahadham, 26-28 dec)": (29.350, 79.567),
    "Haldwani\n(referentiepunt)": (29.220, 79.520),
}

route_order = ["Nainital\n(Hotel Evelyn, 20-23 dec)", "Bhowali\n(wegkruising)", "Almora\n(doorreis, 23 dec)",
               "Dwarahat\n(YSS, 25 dec)", "Bhimtal\n(nabij Haidakhan Vishwa\nMahadham, 26-28 dec)",
               "Haldwani\n(referentiepunt)", "Kathgodam\n(spoorwegstation, eind 29 dec)"]

fig, ax = plt.subplots(figsize=(8.3, 8.3), dpi=150)

xs = [points[k][1] for k in route_order]
ys = [points[k][0] for k in route_order]
ax.plot(xs, ys, '-', color='#b0895a', linewidth=1.6, zorder=1)

offsets = {
    "Kathgodam\n(spoorwegstation, eind 29 dec)": (8, -18),
    "Bhowali\n(wegkruising)": (8, 12),
    "Nainital\n(Hotel Evelyn, 20-23 dec)": (-115, 8),
    "Almora\n(doorreis, 23 dec)": (8, 5),
    "Dwarahat\n(YSS, 25 dec)": (8, 5),
    "Bhimtal\n(nabij Haidakhan Vishwa\nMahadham, 26-28 dec)": (8, -8),
    "Haldwani\n(referentiepunt)": (8, -10),
}

for name, (lat, lon) in points.items():
    ax.plot(lon, lat, 'o', color='#7a3b12', markersize=7, zorder=2)
    dx, dy = offsets.get(name, (7, 5))
    ax.annotate(name, (lon, lat), textcoords="offset points", xytext=(dx, dy),
                fontsize=8, color='#1e1a14', family='DejaVu Sans')

# Kakrighat: on the Nainital-Almora road (NH109), between Bhowali and Almora - no independently
# verified GPS coordinate found for this specific stop. Shown as an approximate marker on the
# known road segment, explicitly labeled unverified, not a geocoded pin.
kak_lon = (points["Bhowali\n(wegkruising)"][1] + points["Almora\n(doorreis, 23 dec)"][1]) / 2
kak_lat = (points["Bhowali\n(wegkruising)"][0] + points["Almora\n(doorreis, 23 dec)"][0]) / 2
ax.plot(kak_lon, kak_lat, '^', color='#a3311a', markersize=9, zorder=3)
ax.annotate("Kakrighat (23 dec)\n[APPROX. op NH109 - geen\nonafhankelijke GPS gevonden]",
            (kak_lon, kak_lat), textcoords="offset points", xytext=(8, -22),
            fontsize=7.5, color='#a3311a', family='DejaVu Sans', style='italic')

ax.annotate("Kasar Devi (23 dec) ≈ 8 km voorbij Almora\n[geen coordinaat gevonden - niet geplot]",
            (points["Almora\n(doorreis, 23 dec)"][1], points["Almora\n(doorreis, 23 dec)"][0]),
            textcoords="offset points", xytext=(-160, -28),
            fontsize=7.5, color='#555', family='DejaVu Sans', style='italic')

ax.set_title("Kumaon overzichtskaart 19-29 dec 2026 — geverifieerde plaatsnaam-posities (Wikipedia-coördinaten)",
             fontsize=10, color='#7a3b12')
ax.set_xlabel("Longitude", fontsize=8)
ax.set_ylabel("Latitude", fontsize=8)
ax.tick_params(labelsize=7)
ax.set_aspect(1.15)
ax.grid(True, linestyle=':', linewidth=0.5, alpha=0.5)

note = ("Let op: dit is een schematische plaatsnaam-kaart op basis van Wikipedia-coordinaten voor de\n"
        "steden/dorpen zelf, GEEN precieze site-level GPS voor individuele tempels/grotten/ashrams.\n"
        "Kakrighat is bij benadering op de bekende wegverbinding geplaatst, niet onafhankelijk gegeocodeerd.\n"
        "Kasar Devi en het exacte Haidakhan Vishwa Mahadham-terrein zijn NIET geplot (geen betrouwbare\n"
        "coordinaat gevonden) - alleen als tekstnotitie/nabije referentiepunt (Bhimtal) getoond.")
fig.text(0.08, 0.02, note, fontsize=7, color='#666', family='DejaVu Sans')

plt.tight_layout(rect=[0, 0.09, 1, 1])
plt.savefig('/home/user/india-knowledge-base/runs/active/pdf_output/kumaon_overview_map.png', bbox_inches='tight')
print("map written")

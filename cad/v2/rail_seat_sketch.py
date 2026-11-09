"""Sketch: rail-seat recess options (review finding 3). Sections at true proportions.
Run: python cad/v2/rail_seat_sketch.py -> cad/v2/out/rail_seat_options.png"""
import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

EG, STEEL, RESIN, BAD, DAM, RAIL = "#d6d2c8", "#6f7884", "#f0b440", "#e03a2f", "#2e9a57", "#aab3bd"

def rect(ax, x0, x1, y0, y1, **k):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, **k))

def panel(ax, title, body, bar, rec, depth, bad, dams, rail_c, note, air=()):
    """All in mm. Horizontal = across the rail, vertical = depth below the rail face (0 at the face, up)."""
    rect(ax, *body, fc=EG, ec="#555", lw=1)
    for a in air:
        rect(ax, *a, fc="white", ec="#555", lw=1)
    rect(ax, rec[0], rec[1], -depth, 0, fc=RESIN, ec="#8a5a00", lw=1)
    rect(ax, bar[0], bar[1], -depth - 10, -depth, fc=STEEL, ec="#222", lw=1)
    for b in bad:
        rect(ax, *b, fc=BAD, ec=BAD, lw=0.5)
    for d in dams:
        rect(ax, *d, fc=DAM, ec="#14502b", lw=1)
    rect(ax, rail_c - 10, rail_c + 10, 0, 9, fc=RAIL, ec="#444", lw=1)
    ax.text(rail_c, 4.5, "rail", ha="center", va="center", fontsize=8)
    ax.text((bar[0] + bar[1]) / 2, -depth - 5, "steel bar", ha="center", va="center", fontsize=8, color="white")
    ax.set_title(title, fontsize=11, fontweight="bold")
    ax.text(0.5, -0.04, note, transform=ax.transAxes, ha="center", va="top", fontsize=9, wrap=True)
    ax.set_xlim(body[0] - 2, body[1] + 12); ax.set_ylim(body[2], 12)
    ax.set_aspect("equal"); ax.axis("off")

fig, axs = plt.subplots(2, 3, figsize=(15, 8.6))
fig.suptitle("Rail-seat recess options. Amber = levelling resin poured later. Red = thin epoxy-granite that 2–5 mm stone cannot fill. Green = temporary taped dam.", fontsize=11)

# ---- base, right-hand Y rail: horizontal = X (spine side face at 170), vertical = Z
B = (98, 170, -30, 0)
panel(axs[0, 0], "BASE now: recess 30 wide, 3 deep", B, (120, 160), (125, 155), 3,
      [(120, 125, -3, 0), (155, 160, -3, 0)], [], 140, "Recess narrower than the 40 mm bar:\n5 × 3 mm lips of EG sit on top of the bar edges")
panel(axs[0, 1], "BASE closed: recess 50 wide, 5 deep", B, (120, 160), (115, 165), 5,
      [(165, 170, -5, 0)], [], 140, "Resin covers the whole bar, but a 5 mm EG rim\nis left at the spine edge (5 deep, 500 long)")
panel(axs[0, 2], "BASE open: recess runs out to the spine side", B, (120, 160), (115, 170), 5,
      [], [(170, 174, -12, 1)], 140, "No thin EG anywhere. A taped strip on the spine\nside holds the resin while it cures, then comes off")
for a in axs[0]:
    a.annotate("spine side face", (170, -22), (176, -22), fontsize=8, va="center", arrowprops=dict(arrowstyle="-", lw=0.6))

# ---- portal, lower X rail, drawn with the rail face up: horizontal = Z (beam bottom edge 225, X channel from 268)
Pb = (225, 280, -30, 0)
ch = [(268, 280, -30, 0.5)]
panel(axs[1, 0], "PORTAL now: recess 30 wide, 3 deep", Pb, (234.5, 259.5), (235, 265), 3,
      [(233.6, 235, -3, 0)], [], 250, "Bar pokes 0.5 mm past the recess: a sliver of EG\nover the bar edge (drawn wider so it shows)", ch)
panel(axs[1, 1], "PORTAL closed: recess 31 wide, 5 deep", Pb, (234.5, 259.5), (231.5, 262.5), 5,
      [(225, 231.5, -5, 0), (262.5, 268, -5, 0)], [], 250, "Two thin EG rims: 6.5 mm at the beam edge,\n5.5 mm at the X screw channel", ch)
panel(axs[1, 2], "PORTAL open: recess spans the whole ledge", Pb, (234.5, 259.5), (225, 268), 5,
      [], [(221, 225, -12, 1), (268, 272, -12, 1)], 250, "No thin EG. Taped strips on the beam edge and\nin the channel hold the resin while it cures", ch)
for a in axs[1]:
    a.text(274, -15, "X screw\nchannel", ha="center", va="center", fontsize=8)
    a.annotate("beam edge", (225, -22), (213, -22), fontsize=8, va="center", ha="right", arrowprops=dict(arrowstyle="-", lw=0.6))
    a.set_xlim(205, 284)
fig.tight_layout(rect=(0, 0.03, 1, 0.95), h_pad=4)
out = pathlib.Path(__file__).parent / "out" / "rail_seat_options.png"
fig.savefig(out, dpi=130)
print(out)

"""Sketch: how the portal goes back in the same place (proposal, docs/portal-relocation.md).
Run: python cad/v2/relocation_sketch.py -> cad/v2/out/portal_relocation.png"""
import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

EG, STEEL, RESIN, TAPE, STOP = "#d6d2c8", "#6f7884", "#f0b440", "#2e7dd1", "#2e9a57"
def rect(ax, x0, x1, y0, y1, **k): ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, **k))

fig, (a, b) = plt.subplots(1, 2, figsize=(15, 7.2), gridspec_kw=dict(width_ratios=[1, 1.25]))

# ---- side section through one leg (Y horizontal, front on the left; Z vertical)
a.set_title("Side section through one leg foot (front of the machine on the left)", fontsize=11, fontweight="bold")
rect(a, 90, 320, -110, 0, fc=EG, ec="#555")                      # base rear cross-piece
rect(a, 110, 240, 3, 150, fc=EG, ec="#555")                      # leg (cut off at the top)
rect(a, 110, 240, 0, 3, fc=RESIN, ec="#8a5a00")                  # grout bed
a.plot([104, 246], [0, 0], color=TAPE, lw=3)                     # tape on the base
rect(a, 115, 235, -50, -30, fc=STEEL, ec="#222")                 # tapped joint bar
for y in (140, 210):
    rect(a, y - 8, y + 8, 3, 150, fc="white", ec="#777", lw=0.8) # sleeve
    rect(a, y - 6, y + 6, -50, 150, fc="#9aa3ad", ec="#444", lw=0.8)  # M12 rod
    a.add_patch(Circle((y - 8.5, 1.5), 1.6, fc="black")); a.add_patch(Circle((y + 8.5, 1.5), 1.6, fc="black"))  # O-ring
rect(a, 262, 302, 0, 40, fc=STOP, ec="#14502b")                  # stop block
rect(a, 240, 290, 17, 23, fc="#333", ec="#111")                  # set screw
rect(a, 270, 276, 14, 26, fc="#333", ec="#111")                  # lock nut
rect(a, 236, 240, 12, 28, fc=STEEL, ec="#222")                   # steel pad on the leg
for y in (272, 292):
    rect(a, y - 3, y + 3, -22, 40, fc="#9aa3ad", ec="#444", lw=0.8)   # M8 screws into inserts
def note(ax, txt, xy, xt, ha="left"):
    ax.annotate(txt, xy, xt, fontsize=9, ha=ha, va="center", arrowprops=dict(arrowstyle="-", lw=0.7, color="#333"))
note(a, "leg", (175, 110), (175, 120), "center")
note(a, "M12 rods in sleeves,\nnuts on the beam top", (140, 90), (20, 100), "left")
note(a, "grout bed 3 mm: bonds to the leg", (120, 1.5), (-10, 40))
note(a, "packing tape on the base:\nthe grout lets go here", (106, 0), (-10, 15))
note(a, "O-rings keep grout\nout of the sleeves", (131, 1.5), (-10, -12))
note(a, "tapped joint bar 40 × 20", (160, -40), (-10, -45))
note(a, "stop block bolted\nto the base", (300, 38), (310, 75))
note(a, "set screw + lock nut\n(squaring adjustment)", (285, 20), (310, 48))
note(a, "steel pad glued\nto the leg back", (238, 26), (215, 60), "right")
a.text(205, -95, "base", fontsize=10, ha="center")
a.set_xlim(-15, 395); a.set_ylim(-118, 160); a.set_aspect("equal"); a.axis("off")

# ---- plan view (X horizontal, Y vertical; back of the machine at the top)
b.set_title("Plan view: two stops set the squareness", fontsize=11, fontweight="bold")
rect(b, -320, 320, 90, 320, fc=EG, ec="#555")                    # rear cross-piece
rect(b, -170, 170, -60, 90, fc=EG, ec="#555")                    # spine (cut off)
for x0 in (-320, 250):
    rect(b, x0, x0 + 70, 110, 240, fc="#bdb8ab", ec="#333", lw=1.2)
    xc = x0 + 35
    for y in (140, 210): b.add_patch(Circle((xc, y), 8, fc="#9aa3ad", ec="#444"))
    rect(b, xc - 30, xc + 30, 262, 302, fc=STOP, ec="#14502b")
    rect(b, xc - 3, xc + 3, 240, 290, fc="#333", ec="#111")
    b.text(xc, 175, "leg", fontsize=9, ha="center", va="center")
for xr in (-140, 140):
    rect(b, xr - 10, xr + 10, -60, 188, fc="#aab3bd", ec="#444", lw=0.8)
b.text(0, 20, "Y rails", fontsize=9, ha="center")
b.add_patch(FancyArrowPatch((0, 150), (0, 235), arrowstyle="-|>", mutation_scale=18, color="#c0392b", lw=2))
b.text(0, 135, "push the portal back\nonto both screws,\nthen tighten the nuts", fontsize=9, ha="center", va="top", color="#c0392b")
b.text(0, 285, "stops 570 apart: 0.01 mm at a stop\n= 0.004 mm across the 250 mm Y travel", fontsize=9, ha="center", va="center")
b.text(0, 335, "back of the machine", fontsize=9, ha="center", color="#555")
b.set_xlim(-340, 340); b.set_ylim(-70, 350); b.set_aspect("equal"); b.axis("off")
fig.tight_layout()
out = pathlib.Path(__file__).parent / "out" / "portal_relocation.png"
fig.savefig(out, dpi=120); print(out)

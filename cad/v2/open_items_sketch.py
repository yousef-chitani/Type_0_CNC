"""Sketch of the two open items (19 Nov 2026), numbers measured in Fusion `Type_0_v3`.

1. Y / Y2 block screw heads clash with the M5 tie rod nuts (D-212).
2. No key access to the M5 x 8 X top block screws (D-215).

Output: cad/v2/out/open_items_sketch.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

OUT = Path(__file__).parent / "out" / "open_items_sketch.png"

STEEL = "#b8c4d0"
BLOCK = "#d9c27a"
SCREW = "#4a6fa5"
NUT = "#888888"
CLASH = "#d62728"
OK = "#2ca02c"


def rect(ax, x0, x1, y0, y1, fc, ec="k", lw=0.8, **kw):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, ec=ec, lw=lw, **kw))


def tube(ax, x0, x1, y0, y1, t=3):
    rect(ax, x0, x1, y0, y1, STEEL)
    rect(ax, x0 + t, x1 - t, y0 + t, y1 - t, "white", lw=0.5)


def hexnut_side(ax, x0, x1, z0, z1):
    rect(ax, x0, x1, z0, z1, NUT)


def screw(ax, yc, z_seat, head_h, fc=SCREW, label=None):
    # socket head seen side on: head Ø8.5, shank Ø5 going down 8 from the seat
    rect(ax, yc - 4.25, yc + 4.25, z_seat, z_seat + head_h, fc)
    rect(ax, yc - 2.5, yc + 2.5, z_seat - 8, z_seat, fc, lw=0.5)


fig = plt.figure(figsize=(16, 11))

# ---------------- Item 1: Y block screw vs nut ----------------
ax = fig.add_subplot(2, 2, 1)
ax.set_title("Item 1 - Y tube, side section at X -366 (Y2 the same, mirrored)\n"
             "now: M5 x 8 socket head (DIN 912) hits the tie rod nut", fontsize=10)
tube(ax, 395, 545, 155, 205)
rect(ax, 387.5, 402.5, 155, 205, STEEL)            # nut plate
ax.text(395, 207, "Y 1610 nut plate", fontsize=7, ha="center")
rect(ax, 388.7, 466.3, 129.6, 155, BLOCK)          # block under the tube
ax.text(427, 140, "HGH20CA block", fontsize=8, ha="center")
rect(ax, 372.5, 557.5, 164.1, 169.0, "#cccccc", lw=0.5)   # tie rod
ax.text(440, 170.5, "M5 tie rod", fontsize=7)
hexnut_side(ax, 402.5, 406.5, 162.1, 171.0)
ax.annotate("M5 nut (2)\nZ 162.1 to 171.0", (404.5, 171), (412, 186), fontsize=7,
            arrowprops=dict(arrowstyle="->", lw=0.6))
screw(ax, 409.55, 158, 5)
screw(ax, 445.45, 158, 5)
rect(ax, 405.3, 406.5, 162.1, 163.0, CLASH, ec=CLASH)
ax.annotate("clash 0.9 in Z\nhead top Z 163", (406, 162.5), (418, 150.5), fontsize=8, color=CLASH,
            arrowprops=dict(arrowstyle="->", color=CLASH))
ax.set_xlim(380, 470)
ax.set_ylim(126, 210)
ax.set_aspect("equal")
ax.set_xlabel("Y (mm)")
ax.set_ylabel("Z (mm)")

# ---------------- Item 1: options ----------------
ax = fig.add_subplot(2, 2, 2)
ax.set_title("Item 1 - options (close-up at the clash)", fontsize=10)
opts = [
    ("A  DIN 912 (now)\nhead 5.0", 5.0, CLASH, "-0.9 (clash)"),
    ("B  DIN 7984 low head\nhead 3.5, 3 mm key", 3.5, OK, "+0.6 clear"),
    ("C  ISO 7380 button\nhead 2.75, 9.5 dia, 3 mm key", 2.75, OK, "+1.35 clear"),
]
for i, (name, h, col, txt) in enumerate(opts):
    dx = i * 30
    rect(ax, dx - 10, dx + 12, 155, 158, STEEL)            # tube bottom wall
    rect(ax, dx - 10, dx + 12, 150, 155, BLOCK)
    hexnut_side(ax, dx - 7, dx - 3, 162.1, 171.0)
    head_w = 4.75 if h == 2.75 else 4.25
    if h == 2.75:  # button head: domed
        ax.add_patch(Polygon([(dx - head_w, 158), (dx + head_w, 158), (dx + 2.5, 158 + h),
                              (dx - 2.5, 158 + h)], fc=SCREW, ec="k", lw=0.8))
    else:
        rect(ax, dx - head_w, dx + head_w, 158, 158 + h, SCREW)
    rect(ax, dx - 2.5, dx + 2.5, 150, 158, SCREW, lw=0.5)
    ax.axhline(162.1, color=NUT, lw=0.4, ls=":")
    ax.text(dx + 1, 173, name, fontsize=7.5, ha="center")
    ax.text(dx + 1, 147, txt, fontsize=8, ha="center", color=col, weight="bold")
ax.text(-10, 140,
        "Nut bottom Z 162.1. Head sits on the tube bottom wall at Z 158.\n"
        "B keeps a cap head of the same 8.5 dia: the closest swap.\n"
        "C gives more room, but a wider domed head and a lower tightening torque.\n"
        "Turning the nut flat-down only gains 0.45: not enough.\n"
        "Applies to 4 screws: Y and Y2, the two nearest the nut plate.\n"
        "Not priced.", fontsize=7.5, va="top")
ax.set_xlim(-14, 76)
ax.set_ylim(118, 182)
ax.set_aspect("equal")
ax.axis("off")

# ---------------- Item 2: X tube cross section ----------------
ax = fig.add_subplot(2, 2, 3)
ax.set_title("Item 2 - X top tube, section at X -162 (screws 7 and 8)\n"
             "the top angle, the tube top wall, the tie rods and the ball nut are all above the heads",
             fontsize=10)
tube(ax, 445, 565, 355, 405)
# top angle: flange + leg
rect(ax, 437, 562, 405, 411, "#9fb3c8")
rect(ax, 437, 443, 361, 411, "#9fb3c8")
ax.text(500, 412.5, "XRoller Top Angle flange (6)", fontsize=7, ha="center")
rect(ax, 483, 527, 329.6, 355, BLOCK)
ax.text(505, 340, "HGH20CA block", fontsize=8, ha="center")
for yc in (489, 521):
    screw(ax, yc, 358, 5)
# M6 x 8 flange screws
for yc in (478.5, 531.5):
    rect(ax, yc - 5, yc + 5, 411, 415, SCREW)
    rect(ax, yc - 3, yc + 3, 401, 411, SCREW, lw=0.5)
ax.text(531.5, 416.5, "M6 x 8 flange screws", fontsize=6.5, ha="center")
# tie rods
for (yc, zc) in [(486, 380), (491.55, 393.45), (518.45, 393.45), (524, 380),
                 (518.45, 366.55), (491.55, 366.55)]:
    ax.add_patch(Circle((yc, zc), 2.5, fc="#cccccc", ec="k", lw=0.6))
ax.text(470, 395, "M5 tie rods", fontsize=7)
# ball screw and nut flange (Ø48, flats at Z 360 / 400)
ax.add_patch(Circle((505, 380), 8, fc="#999999", ec="k", lw=0.6))
ax.plot([505 - 12.8, 505 + 12.8, 505 + 24, 505 + 12.8, 505 - 12.8, 505 - 24, 505 - 12.8],
        [400, 400, 380, 360, 360, 380, 400], color="k", lw=0)

th = np.linspace(0, 2 * np.pi, 200)
fy = 505 + 24 * np.cos(th)
fz = np.clip(380 + 24 * np.sin(th), 360, 400)
ax.plot(fy, fz, color="#555555", lw=1, ls="--")
ax.text(505, 401.5, "DFU1605 flange (X -175 to -130)", fontsize=6.5, ha="center", color="#555555")
# blocked key path
for yc in (489, 521):
    ax.annotate("", (yc, 364), (yc, 430), arrowprops=dict(arrowstyle="-|>", color=CLASH, lw=1.2))
ax.text(489, 432, "straight down: blocked", fontsize=8, color=CLASH, ha="center")
ax.set_xlim(432, 572)
ax.set_ylim(325, 440)
ax.set_aspect("equal")
ax.set_xlabel("Y (mm)")
ax.set_ylabel("Z (mm)")

# ---------------- Item 2: side view and options ----------------
ax = fig.add_subplot(2, 2, 4)
ax.set_title("Item 2 - X top tube, side view (X-Z), and the options", fontsize=10)
tube(ax, -297.5, -147.5, 355, 405)
rect(ax, -297.5, -147.5, 405, 411, "#9fb3c8")
rect(ax, -305, -290, 355, 405, STEEL, alpha=0.35, ls="--")    # fill plate
rect(ax, -155, -140, 355, 405, STEEL, alpha=0.35, ls="--")    # nut plate
ax.text(-297.5, 350, "fill plate", fontsize=6.5, ha="center")
ax.text(-147.5, 350, "nut plate", fontsize=6.5, ha="center")
rect(ax, -175, -130, 360, 400, "none", ec="#555555", ls="--")
ax.text(-152, 401.5, "ball nut", fontsize=6.5, ha="center", color="#555555")
for i, xc in enumerate((-283, -247, -198, -162)):
    rect(ax, xc - 4.25, xc + 4.25, 358, 363, SCREW)
    ax.text(xc, 366, f"{2*i+1},{2*i+2}", fontsize=7, ha="center")
rect(ax, -303.8, -226.2, 329.6, 355, BLOCK)
rect(ax, -218.8, -141.2, 329.6, 355, BLOCK)
# L key from the open end
ax.plot([-247, -247, -330], [363, 383, 383], color=OK, lw=2.2)
ax.text(-338, 386, "A: L-key through the open tube end", fontsize=7.5, color=OK, ha="right")
ax.set_xlim(-430, -120)
ax.set_ylim(255, 430)
ax.set_aspect("equal")
ax.set_xlabel("X (mm)")
ax.text(-428, 312,
        "A  Assembly order, no new holes (recommended): screw the blocks on first, with an L-key through\n"
        "    the open tube ends (inside 44 high, screws 14.5 and 50 from the ends), then rods, nut, end plates,\n"
        "    top angle. Changing a block later means stripping the X carriage.\n"
        "B  8 x Ø6.5 holes through the angle flange and the top wall (clear of the M6 x 8 by 2.2). Still blocked\n"
        "    by the tie rods (1.1 above the heads) and, for 7 and 8, by the ball nut: only helps with those out.\n"
        "C  Back to HGW20CC flanged blocks, screwed from below. Undoes D-215 and the BOM (M02).",
        fontsize=7.5, va="top")

fig.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=130)
print(OUT)

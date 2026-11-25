"""Task 28 sketches: Z and X motor belt folds, and the footprint comparison.

Writes three SVGs to docs/sketches/ (1 px = 1 mm, rough sketches, not CAD).
Sizes are from the Type_0_v4 and Type_0_v3 bounding boxes read on 25 Nov 2026
(see docs/task28-folds-and-footprint.md). Run: python tools/task28_sketches.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs" / "sketches"


def svg(w, h, body, vb):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="{vb}" font-family="sans-serif" font-size="14">\n'
            '<rect x="-10000" y="-10000" width="20000" height="20000" fill="white"/>\n'
            + body + "</svg>\n")


def rect(x0, y0, x1, y1, fill="#ddd", stroke="#333", dash=False, label=None, ls=12, op=1.0):
    # drawing frame: y up, so flip
    x, y, w, h = min(x0, x1), -max(y0, y1), abs(x1 - x0), abs(y1 - y0)
    d = ' stroke-dasharray="6 4"' if dash else ""
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
         f'fill-opacity="{op}" stroke="{stroke}"{d}/>\n')
    if label:
        s += text((x0 + x1) / 2, (y0 + y1) / 2, label, ls)
    return s


def text(x, y, t, size=12, anchor="middle", color="#000"):
    return (f'<text x="{x}" y="{-y}" font-size="{size}" text-anchor="{anchor}" '
            f'dominant-baseline="middle" fill="{color}">{t}</text>\n')


def line(x0, y0, x1, y1, color="#c00", w=2, dash=False):
    d = ' stroke-dasharray="6 4"' if dash else ""
    return f'<line x1="{x0}" y1="{-y0}" x2="{x1}" y2="{-y1}" stroke="{color}" stroke-width="{w}"{d}/>\n'


def z_fold():
    """Side view looking along -X: Y across (front left), Z up."""
    b = text(130, 760, "Z fold, side view (Y across, Z up), proposal", 16)
    b += rect(190, 160, 310, 280, "#bbb", label="beam 120x120")
    b += rect(140, 350, 285, 370, "#ccc", label="X nut bracket", ls=10)
    b += rect(120, 99, 140, 541, "#cde", label="")
    b += text(130, 80, "Z fixed plate", 10)
    b += rect(-41, 132, 41, 470, "#eee", label="spindle (mid Z)", ls=11)
    b += rect(-41, 545, 41, 470, "#fff", dash=True)
    b += text(0, 510, "spindle top at Z max 545", 9)
    b += rect(65, 464, 125, 554, "#9bd", label="HM12-60")
    b += line(95, 114, 95, 464, "#555", 3)
    b += text(80, 300, "Z screw", 10, "end")
    # now: direct motor
    b += rect(65, 554, 125, 700, "#f6c6c6", dash=True, label="motor now", ls=10, op=0.6)
    b += text(95, 715, "top now Z 700", 11)
    # fold
    b += rect(60, 554, 210, 564, "#7a7", label="")
    b += text(240, 559, "fold plate 10", 10, "start")
    b += rect(145, 554, 205, 408, "#fbb", label="motor folded", ls=10)
    b += text(175, 395, "38 above nut bracket", 9)
    b += rect(80, 564, 110, 590, "#ea5")
    b += rect(160, 564, 190, 590, "#ea5")
    b += line(95, 590, 175, 590, "#c00", 3)
    b += line(95, 564, 175, 564, "#c00", 3)
    b += text(215, 585, "HTD 5M 15, 20T:20T, centres 80", 10, "start")
    b += text(215, 600, "top folded about Z 590 (110 lower)", 11, "start")
    b += line(-60, 280, 330, 280, "#888", 1, True)
    b += text(335, 280, "beam top Z 280", 10, "start")
    return svg(560, 760, b, "-90 -780 520 760")


def x_fold():
    """Top view of the X- end of the beam: X across, Y up (rear up)."""
    b = text(-300, 420, "X fold, top view at the X- end (X across, Y up = rear), proposal", 16)
    b += rect(-350, 190, -100, 310, "#bbb", label="")
    b += rect(-320, 185, -270, 335, "#999", op=0.4)
    b += text(-295, 345, "upright", 10)
    b += rect(-320, 335, -120, 345, "#7a7", op=0.6)
    b += text(-220, 352, "rear shear plate (top Z 280)", 10)
    b += rect(-215, 140, -75, 285, "#ccc", dash=True, label="nut bracket at X min", ls=10, op=0.5)
    b += rect(-395, 205, -305, 295, "#9bd", label="HM12", ls=10)
    b += line(-395, 250, -100, 250, "#555", 3)
    b += text(-150, 240, "X screw Y 250, Z 325", 10)
    b += rect(-536, 220, -395, 280, "#f6c6c6", dash=True, label="motor inline (D-320)", ls=10, op=0.6)
    b += text(-536, 175, "X min about -536 (D-320, estimate)", 11, "start")
    b += rect(-430, 230, -400, 345, "#7a7", op=0.7)
    b += text(-440, 360, "fold plate", 10)
    b += rect(-390, 295, -245, 355, "#fbb", label="motor folded, behind the beam", ls=10)
    b += line(-415, 250, -415, 325, "#c00", 4)
    b += text(-425, 120, "X min about -430 (about 105 shorter)", 11, "start")
    b += text(-300, 95, "HTD 5M 15, 20T:20T, centres 75; motor bottom Z 295 (beam top 280)", 10, "start")
    return svg(760, 360, b, "-560 -440 760 360")


def footprint():
    """Top views to the same scale: V4 + wheel, V4 X folded, v3 + wheel, v3 + 12-tool rack."""
    def panel(dx, dy, title, parts, env, work, note):
        s = text(dx, dy + 1000, title, 40)
        for p in parts:
            x0, y0, x1, y1, fill, lab = p
            s += rect(x0 + dx, y0 + dy, x1 + dx, y1 + dy, fill, label=lab, ls=24, op=0.8)
        ex0, ey0, ex1, ey1 = env
        s += rect(ex0 + dx, ey0 + dy, ex1 + dx, ey1 + dy, "none", "#c00", dash=True)
        wx0, wy0, wx1, wy1 = work
        s += rect(wx0 + dx, wy0 + dy, wx1 + dx, wy1 + dy, "#8c8", label="work", ls=24, op=0.5)
        a = (ex1 - ex0) * (ey1 - ey0) / 1e6
        w = (wx1 - wx0) * (wy1 - wy0) / 1e6
        s += text(dx, dy - 380, f"{ex1 - ex0:.0f} x {ey1 - ey0:.0f} = {a:.2f} m2 floor", 32)
        s += text(dx, dy - 425, f"work {w:.2f} m2, floor / work {a / w:.1f}", 32)
        s += text(dx, dy - 470, note, 28)
        return s

    v4 = [(-270, -335, 270, 335, "#ddd", "base"), (-350, 190, 550, 310, "#bbb", "beam"),
          (-230, -315, 230, 315, "#eef", ""), (380, -60, 435, 60, "#fc9", "wheel"),
          (-100, 335, 100, 470, "#fbb", "Y motors")]
    b = panel(0, 0, "V4 + wheel (model)", v4, (-508, -335, 550, 470), (-215, -125, 215, 125),
              "X motor inline at X -508 (old bracket)")
    b += panel(1400, 0, "V4 + wheel, X folded", v4, (-430, -335, 550, 470), (-215, -125, 215, 125),
               "X min about -430")
    v3 = [(-390, -37, 390, 653, "#ddd", "EG tub"), (-388, 445, 387, 565, "#bbb", "gantry"),
          (-484, 579, -319, 775, "#fbb", "Y mot."), (319, 579, 484, 775, "#fbb", "Y mot."),
          (58, -156, 342, -37, "#fc9", "wheel")]
    dy = -1700
    b += panel(0, dy, "v3 + wheel (model)", v3, (-484, -156, 515, 775), (-200, 0, 200, 250),
               "moving gantry, front wheel")
    add = 275
    v3r = [(-390, -37, 450, 653 + add, "#ddd", "tub +275 Y, +60 X"),
           (-388, 445 + add, 447, 565 + add, "#bbb", "gantry"),
           (-484, 579 + add, -319, 775 + add, "#fbb", "Y mot."),
           (379, 579 + add, 544, 775 + add, "#fbb", "Y mot."),
           (330, 0, 390, 660, "#fc9", "")]
    b += text(1400 + 360, dy + 330, "rack", 24)
    b += panel(1400, dy, "v3 + 12-tool rack (estimate)", v3r, (-484, -37, 575, 775 + add),
               (-200, 0, 200, 525), "12 at 60 pitch along Y, on the +X wall")
    return svg(1100, 1300, b, "-650 -1100 2750 3250")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, f in (("task28_z_fold.svg", z_fold), ("task28_x_fold.svg", x_fold),
                    ("task28_footprint.svg", footprint)):
        (OUT / name).write_text(f(), encoding="utf-8")
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()

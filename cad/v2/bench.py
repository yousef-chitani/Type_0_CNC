"""Type 0 v2: owner-built timber bench (task 3, D-97).

Run: python cad/v2/bench.py -> cad/v2/out/bench.step, bench_views.svg, bench_cutlist.md
Bench coordinates: x 0..W left to right, y 0..Dp front to back, z up from the floor.
Bolted knock-down (owner choice): legs, rails and braces join with M10 threaded rod, so it comes apart flat.
"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import type0_v2 as m
from moulds import Svg

P, D, OUT = m.P, m.D, m.OUT
B = dict(
    W=1100, Dp=1000,            # top (owner: machine only; 1100 wide for the X motor, D-97)
    top_z=785,                  # D-75 / D-80: bench top 785 above the floor
    ply_top=18, top_layers=2,   # 2 x 18 mm ply, glued and screwed
    cls_t=38, cls_w=89,         # CLS 38 x 89 (studwork)
    leg_inset=38,               # legs 38 in from the sides: room for the braces on the outer faces
    bottom_rail_top=150,        # shelf rests on the bottom rails
    shelf_t=12, back_t=12,      # 12 mm ply shelf and back panel
    x_motor_out=170,            # X motor + coupling + mount past the beam end (VERIFY when the parts arrive)
    enclosure_gap=40, enclosure_t=12, enclosure_back_gap=80, y_motor_len=150, enclosure_front_gap=40,
    cabinet=(600, 200, 400),    # E12 RS 600 W x 200 D x 400 H
    stick=2400,                 # CLS length bought
)

t, w = B["cls_t"], B["cls_w"]
top_th = B["ply_top"] * B["top_layers"]
z_top_u = B["top_z"] - top_th                  # underside of the top = top of the upper rails
leg_h = z_top_u
leg_w = 2 * t                                  # two CLS laminated: 76 (x) x 89 (y)

# enclosure (D-87) widened for the X motor, centred on the bench
ex0 = D["portal_x0"] - B["enclosure_gap"]
ex1 = D["portal_x1"] + B["x_motor_out"] + 20
ey0 = D["spine_y0"] - B["y_motor_len"] - B["enclosure_front_gap"]
ey1 = D["foot_y1"] + B["enclosure_back_gap"]
enc_out = (ex1 - ex0 + 2 * B["enclosure_t"], ey1 - ey0 + 2 * B["enclosure_t"])
off_x = (B["W"] - enc_out[0]) / 2 + B["enclosure_t"] - ex0     # machine x -> bench x
off_y = (B["Dp"] - enc_out[1]) / 2 + B["enclosure_t"] - ey0     # machine y -> bench y
feet = [(fx + off_x, fy + off_y) for fx, fy in ((-120, -300), (120, -300), (-280, 280), (280, 280))]   # as moulds.py
front_line = (feet[0][1] + feet[1][1]) / 2
rear_line = (feet[2][1] + feet[3][1]) / 2

legs_x = [(B["leg_inset"], B["leg_inset"] + leg_w), (B["W"] - B["leg_inset"] - leg_w, B["W"] - B["leg_inset"])]
legs_y = [(front_line - w / 2, front_line + w / 2), (rear_line - w / 2, rear_line + w / 2)]
rails_z = {"top": (z_top_u - w, z_top_u), "bottom": (B["bottom_rail_top"] - w, B["bottom_rail_top"])}
side_z = {"top": (rails_z["top"][0] - w, rails_z["top"][0]), "bottom": (B["bottom_rail_top"] + B["shelf_t"], B["bottom_rail_top"] + B["shelf_t"] + w)}
side_y = (legs_y[0][0] - t, legs_y[1][1] + t)
shelf = (legs_x[0][1] + t, legs_x[1][0] - t, legs_y[0][0] - t, legs_y[1][1] + t)
back_y = legs_y[1][1] + t


def parts():
    """List of (name, x0, x1, y0, y1, z0, z1)."""
    L = []
    for i, (x0, x1) in enumerate(legs_x):
        for j, (y0, y1) in enumerate(legs_y):
            L.append((f"leg {'LR'[i]}{'FB'[j]}", x0, x1, y0, y1, 0, leg_h))
    for lvl, (z0, z1) in rails_z.items():
        for j, (y0, y1) in enumerate(legs_y):
            L.append((f"{lvl} rail {'FB'[j]} front-face", 0, B["W"], y0 - t, y0, z0, z1))
            L.append((f"{lvl} rail {'FB'[j]} back-face", 0, B["W"], y1, y1 + t, z0, z1))
    for lvl, (z0, z1) in side_z.items():
        L.append((f"{lvl} side rail L", legs_x[0][1], legs_x[0][1] + t, side_y[0], side_y[1], z0, z1))
        L.append((f"{lvl} side rail R", legs_x[1][0] - t, legs_x[1][0], side_y[0], side_y[1], z0, z1))
    L.append(("shelf", shelf[0], shelf[1], shelf[2], shelf[3], B["bottom_rail_top"], B["bottom_rail_top"] + B["shelf_t"]))
    L.append(("back panel", 0, B["W"], back_y, back_y + B["back_t"], rails_z["bottom"][0], z_top_u))
    for k in range(B["top_layers"]):
        L.append((f"top layer {k+1}", 0, B["W"], 0, B["Dp"], z_top_u + k * B["ply_top"], z_top_u + (k + 1) * B["ply_top"]))
    return L


def brace():
    """Diagonal on each side, outer leg faces: front leg at the bottom side rail -> rear leg at the top side rail."""
    p0 = (front_line, sum(side_z["bottom"]) / 2)
    p1 = (rear_line, sum(side_z["top"]) / 2)
    L = math.dist(p0, p1) + 2 * 60
    return p0, p1, L


def cutlist():
    n_leg = 8; L_leg = leg_h
    rails = [("Leg (2 laminated per leg)", L_leg, 8), ("Front/back rail (sandwich the legs)", B["W"], 8),
             ("Side rail (inner leg faces)", side_y[1] - side_y[0], 4), ("Diagonal brace (outer leg faces)", brace()[2], 2)]
    # pack into 2.4 m sticks, 4 mm saw cuts
    pieces = sorted([L for _, L, n in rails for _ in range(n)], reverse=True)
    sticks = []
    for p in pieces:
        for s in sticks:
            if sum(s) + 4 * len(s) + p <= B["stick"]: s.append(p); break
        else: sticks.append([p])
    return rails, sticks


def bolts():
    sand = 16, 2 * t + w + 25          # 2 per rail pair per leg, top and bottom
    side = 4, t + leg_w + 25           # 1 per side-rail end
    brc = 4, 2 * t + leg_w + 25        # through brace + leg + side rail
    return [("sandwich bolts (y)", *sand), ("side rail bolts (x)", *side), ("brace bolts (x)", *brc)]


def draw():
    s = Svg(1500, 900, "Timber bench (task 3): front view, side view, plan. Bolted knock-down. Scale 1:5")
    k = 0.4
    def box2(o, a0, a1, b0, b1, fill, dash=None, op=1):
        s.rect(o[0] + a0 * k, o[1] - b0 * k, o[0] + a1 * k, o[1] - b1 * k, fill=fill, dash=dash, op=op)
    cols = {"leg": "#d9b38c", "rail": "#f2d6a2", "side": "#e8c48a", "shelf": "#c7e9c0", "back": "#eeeeee", "top": "#fdd49e"}
    def col(n): return cols["side"] if "side" in n else cols["leg"] if "leg" in n else cols["rail"] if "rail" in n else cols["shelf"] if n == "shelf" else cols["back"] if "back" in n else cols["top"]
    # front view (x-z), seen from the front: draw back to front
    o = (40, 420)
    s.text(o[0], 60, "FRONT VIEW", 12, bold=True)
    for n, x0, x1, y0, y1, z0, z1 in sorted(parts(), key=lambda r: -r[3]):
        box2(o, x0, x1, z0, z1, col(n))
    cx0, cx1 = shelf[0] + 20, shelf[0] + 20 + B["cabinet"][0]
    zc = B["bottom_rail_top"] + B["shelf_t"]
    box2(o, cx0, cx1, zc, zc + B["cabinet"][2], "#9ecae1", "4,2")
    s.text(o[0] + (cx0 + cx1) / 2 * k, o[1] - (zc + 200) * k, "cabinet 600x400x200 (E12)", 9, "middle")
    s.dim(o[0], o[1] + 10, o[0] + B["W"] * k, o[1] + 10, f"{B['W']}", -12)
    s.dim(o[0] + B["W"] * k + 10, o[1], o[0] + B["W"] * k + 10, o[1] - B["top_z"] * k, f"top {B['top_z']}", 12)
    s.dim(o[0] + legs_x[0][1] * k, o[1] - 250 * k, o[0] + legs_x[1][0] * k, o[1] - 250 * k, f"{legs_x[1][0]-legs_x[0][1]:.0f} between legs", 0)
    # side view (y-z), seen from the left
    o2 = (560, 420)
    s.text(o2[0], 60, "SIDE VIEW (from the left, front on the left)", 12, bold=True)
    for n, x0, x1, y0, y1, z0, z1 in sorted(parts(), key=lambda r: -r[1]):
        box2(o2, y0, y1, z0, z1, col(n))
    p0, p1, Lb = brace()
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    dx, dy = math.cos(ang) * 60, math.sin(ang) * 60
    a, b = (p0[0] - dx, p0[1] - dy), (p1[0] + dx, p1[1] + dy)
    s.line(o2[0] + a[0] * k, o2[1] - a[1] * k, o2[0] + b[0] * k, o2[1] - b[1] * k, "#8c510a", w * k)
    s.text(o2[0] + (a[0] + b[0]) / 2 * k + 10, o2[1] - (a[1] + b[1]) / 2 * k, f"brace {Lb:.0f}", 9)
    s.dim(o2[0], o2[1] + 10, o2[0] + B["Dp"] * k, o2[1] + 10, f"{B['Dp']}", -12)
    s.dim(o2[0] + legs_y[0][0] * k, o2[1] - 700 * k - 30, o2[0] + legs_y[1][1] * k, o2[1] - 700 * k - 30, f"legs {legs_y[1][1]-legs_y[0][0]:.0f} outside", 0)
    s.dim(o2[0], o2[1] - B["top_z"] * k - 12, o2[0] + legs_y[0][0] * k, o2[1] - B["top_z"] * k - 12, f"{legs_y[0][0]:.0f}", 0)
    # plan (x-y), front at the bottom
    o3 = (1000, 470)
    s.text(o3[0], 60, "PLAN (top removed; front at the bottom)", 12, bold=True)
    s.rect(o3[0], o3[1] - B["Dp"] * k, o3[0] + B["W"] * k, o3[1], fill="#fff7ec", dash="4,2")
    for n, x0, x1, y0, y1, z0, z1 in parts():
        if "top layer" in n or n == "back panel": continue
        if z1 > 600 or "leg" in n: box2(o3, x0, x1, y0, y1, col(n), op=0.8)
    s.rect(o3[0] + (ex0 + off_x - B["enclosure_t"]) * k, o3[1] - (ey0 + off_y - B["enclosure_t"]) * k,
           o3[0] + (ex1 + off_x + B["enclosure_t"]) * k, o3[1] - (ey1 + off_y + B["enclosure_t"]) * k, c="#08519c", dash="6,3")
    s.text(o3[0] + 4, o3[1] + 34, f"enclosure outside {enc_out[0]:.0f} x {enc_out[1]:.0f} (widened for the X motor)", 8, c="#08519c")
    for fx, fy in feet:
        s.circle(o3[0] + fx * k, o3[1] - fy * k, 5, fill="#d94801")
    s.text(o3[0] + feet[1][0] * k + 8, o3[1] - feet[1][1] * k + 3, "machine feet", 8, c="#d94801")
    s.text(o3[0] + B["W"] * k / 2, o3[1] + 18, "FRONT", 10, "middle", True)
    notes = ["Legs: 2 x CLS 38x89 glued and screwed = 76 x 89. Legs sit under the machine feet lines (front and rear), so the feet load goes straight down.",
             "Front/back rails: a pair sandwiches each leg line, top and bottom: 2 x M10 rod through rail + leg + rail at each leg (top and bottom).",
             "Side rails: inner leg faces, 1 x M10 at each end. Braces: outer leg faces, front-bottom to rear-top, bolted through brace + leg + side rail.",
             "Top: 2 x 18 mm ply glued and screwed, screwed down into the top rails from above (countersunk, removable). Seal it (it is the enclosure floor).",
             "Shelf: 12 mm ply on the bottom rails. Cabinet front-left, coolant reservoir rear-right in a drip tray. Back: 12 mm ply screwed to the rear rails.",
             "Flat-pack: top (about 24 kg), 4 legs, 8 long rails, 4 side rails, 2 braces, shelf, back. Re-tighten the bolts after a month (timber shrinks)."]
    for i, n in enumerate(notes): s.text(40, 760 + i * 15, n, 9)
    s.save(OUT / "bench_views.svg")


def step():
    import cadquery as cq
    asm = cq.Assembly()
    for n, x0, x1, y0, y1, z0, z1 in parts():
        asm.add(cq.Workplane("XY").box(x1 - x0, y1 - y0, z1 - z0, centered=False).translate((x0, y0, z0)), name=n.replace(" ", "_"))
    asm.export(str(OUT / "bench.step"))


def report():
    rails, sticks = cutlist()
    pl = [p for p in parts()]
    ply18 = [p for p in pl if "top layer" in p[0]]
    ply12 = [p for p in pl if p[0] in ("shelf", "back panel")]
    L = ["# Timber bench cut list (generated by cad/v2/bench.py)", "",
         f"Top {B['W']} × {B['Dp']} at {B['top_z']} mm. Bolted knock-down. Drawing: `bench_views.svg`, model: `bench.step`. Notes: [docs/bench.md](../../../docs/bench.md).", "",
         "## CLS 38 × 89 (studwork, 2.4 m)", "| Piece | Length (mm) | Qty |", "|---|---|---|"]
    L += [f"| {n} | {Lp:.0f} | {q} |" for n, Lp, q in rails]
    L += ["", f"**{len(sticks)} lengths of 2.4 m** (+1 spare = {len(sticks)+1}). Packing: " +
          "; ".join(" + ".join(f"{p:.0f}" for p in s_) for s_ in sticks) + ".", "",
          "## Sheet material", "| Piece | Size (mm) | From |", "|---|---|---|"]
    L += [f"| {p[0]} | {p[2]-p[1]:.0f} × {p[4]-p[3]:.0f} | 18 mm ply 2440 × 1220 (1 sheet: both layers) |" for p in ply18]
    L += [f"| {p[0]} | {p[2]-p[1]:.0f} × {max(p[4]-p[3], p[6]-p[5]):.0f} | 12 mm ply 2440 × 1220 (1 sheet) |" for p in ply12]
    L += ["", "## Fixings", "| Item | Qty | Length each |", "|---|---|---|"]
    tot = 0
    for n, q, Lb in bolts():
        L.append(f"| M10 rod, {n} | {q} | {Lb:.0f} |"); tot += q * Lb
    nb = sum(q for _, q, _ in bolts())
    L += [f"| **M10 rod total** | **{tot/1000:.1f} m** | 5 × 1 m |",
          f"| M10 nuts | {2*nb} | |", f"| M10 penny washers (30 mm) | {2*nb} | |",
          "| Wood screws 5 × 60 (top layers, top to rails, leg laminating) | about 80 | |",
          "| Wood screws 4 × 30 (shelf, back panel) | about 30 | |",
          "| PVA wood glue | 1 bottle | legs and top layers |",
          "| Varnish or floor paint | 1 small tin | seal the top (enclosure floor) |"]
    L += ["", "## Key positions (bench coordinates, mm)", "| | |", "|---|---|",
          f"| Machine feet | " + ", ".join(f"({x:.0f}, {y:.0f})" for x, y in feet) + " |",
          f"| Leg lines (y, centre) | front {front_line:.0f}, rear {rear_line:.0f} |",
          f"| Legs (x) | {legs_x[0][0]:.0f}–{legs_x[0][1]:.0f} and {legs_x[1][0]:.0f}–{legs_x[1][1]:.0f} |",
          f"| Shelf | {shelf[1]-shelf[0]:.0f} wide × {shelf[3]-shelf[2]:.0f} deep, top at {B['bottom_rail_top']+B['shelf_t']} |",
          f"| Clear height above the shelf (to the top rails) | {rails_z['top'][0] - B['bottom_rail_top'] - B['shelf_t']:.0f} (cabinet is 400) |",
          f"| Enclosure outside (widened for the X motor) | {enc_out[0]:.0f} × {enc_out[1]:.0f} |",
          f"| Machine x 0 / y 0 on the bench | x {off_x:.0f}, y {off_y:.0f} |"]
    (OUT / "bench_cutlist.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    draw(); report(); step()
    print((OUT / "bench_cutlist.md").read_text())

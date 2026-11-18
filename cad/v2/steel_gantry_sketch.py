"""Steel SHS gantry layout (D-164): boxes, clash check, one PNG. No STEP. All of it is a PROPOSAL.

Run: PYTHONUTF8=1 python cad/v2/steel_gantry_sketch.py
     add --fixes to check the 4 proposed fixes (writes steel_gantry_sketch_fixes.json only, no PNG)
  -> cad/v2/out/steel_gantry_sketch.png   saddle section, front view, beam top view, foot section
  -> cad/v2/out/steel_gantry_sketch.json  gaps, access holes, bolt checks, moving mass

Coordinates: X right, Z up, Z 0 = tub floor top. Tub parts: Y from the work centre.
Gantry parts: Yg = Y measured back from the spindle axis (tub Y = spindle Y + Yg).
The tub comes from out/gantry_sketch.json. Bought-part sizes: cad/vendor/README.md and assembly.py.
Every part is a bounding box, so a round part is checked as its square envelope.
"""
import itertools, json, math, pathlib, sys

HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"
T = json.loads((OUT / "gantry_sketch.json").read_text(encoding="utf-8"))
S, YC = T["S"], T["Y"]["atc_reach_100"]
AL, STEEL = 2700e-9, 7850e-9
FIXES = "--fixes" in sys.argv                   # proposed fixes in docs/steel-gantry-sketch.md
STEP_X = 378.0 if FIXES else 380.0              # inner edge of the foot step

# ---------------------------------------------------------------- bought parts (mm)
RAIL_W, RAIL_H = 20.0, 17.5                     # HGR20
BL_W, BL_L, BL_H, BL_H1 = 44.0, 77.5, 30.0, 4.3 # HGH20CA, H1 from the drawing in cad/vendor/README.md
BL_B, BL_C = 32.0, 36.0                         # HGH20CA hole spacing: across the rail, along the rail
X_PITCH, Y_PITCH, Z_PITCH = (90.0 if FIXES else 100.0), 150.0, 90.0
BK_W, BK_H, BK_L, BK_LOCK, BF_L, AXIS_H = 60.0, 43.0, 25.0, 12.0, 20.0, 25.0  # BK12 / BF12
HS_W, HS_H, HS_L, HS_C = 52.0, 40.0, 40.0, 20.0 # DSG16H
NUT_D, NUT_L, FL_D, FL_T = 28.0, 100.0, 48.0, 10.0  # DFU1605: vendor model has a ROUND Ø48 flange (flats 40 unconfirmed)
PUL_OD, PUL_W, PUL_HUB = 36.0, 20.7, 5.5        # HTD-5M 20T 15 mm
MOT_SQ, MOT_LEN = 60.0, 125.0                   # 24HS40 body 100 + encoder 25

# ---------------------------------------------------------------- the brief (docs/HANDOVER.md, 18 Nov)
B0, B1 = 150.0, 300.0                           # beam Yg
BZ0, BZ1 = 195.0, 345.0                         # beam Z
BEAM_HALF = 445.0
FLAT0, FLAT1 = B0 + 24, B0 + 126                # usable flat, corner radius 24 NOT verified
SEAT = 4.0
RAIL_Y = B0 + 36
SCREW_Y, SCREW_Z = B0 + 86, 374.0
SEAT_TOP, SEAT_BOT = BZ1 + SEAT, BZ0 - SEAT     # 349, 191
XS_MAX = 200.0                                  # saddle centre travel, ±
SPY = YC["spindle_y"]                           # -225 ... 125
ZN = (S["nose_bot"], S["nose_top"])             # nose tip, 55 ... 205
CAR_Y = 140.0                                   # Y carriage centre behind the spindle
MOTOR_Y = SCREW_Y + 137.5                       # 375 belt, 20T : 20T
PUL_X0 = 330.0                                  # pulley starts 3 past the BK lock nut (327)

boxes = []
def add(name, group, x, y, z, mat="al"):
    boxes.append(dict(name=name, group=group, x=tuple(map(float, x)), y=tuple(map(float, y)), z=tuple(map(float, z)), mat=mat))
def mid(c, w):
    return (c - w / 2, c + w / 2)

# ---------------------------------------------------------------- fixed: tub and Y axis
ty = YC["tub_y"]
wi, wo, wt = S["wall_in_x"], S["wall_out_x"], S["wall_top"]
add("Tub floor", "F", (-wo, wo), ty, (-S["floor_t"], 0), "eg")
add("Table", "F", (-230, 230), (-165, 165), (0, S["table_top"]), "table")
for sn, s in (("R", 1), ("L", -1)):
    def fx(a, b):
        return (min(s * a, s * b), max(s * a, s * b))
    sx, rx = S["screw_x"], S["rail_x"]
    add(f"Tub wall {sn}", "F", fx(wi, wo), ty, (0, wt), "eg")
    add(f"Y rail {sn}", "F", fx(rx - 10, rx + 10), YC["rail_y"], (wt, wt + RAIL_H), "rail")
    add(f"Y screw {sn}", "F", fx(sx - 8, sx + 8), (YC["bf_y0"], YC["bk_y1"]), (wt + 17, wt + 33), "screw")
    add(f"Y BF12 {sn}", "F", fx(sx - 30, sx + 30), (YC["bf_y0"], YC["bf_y0"] + BF_L), (wt, wt + BK_H), "steel")
    add(f"Y BK12 {sn}", "F", fx(sx - 30, sx + 30), (YC["bk_y1"] - BK_LOCK - BK_L, YC["bk_y1"] - BK_LOCK), (wt, wt + BK_H), "steel")
    add(f"Y motor mount {sn}", "F", fx(sx - 30, sx + 30), (ty[1], ty[1] + 60), (wt - 5, wt + 55), "al")
    add(f"Y motor {sn}", "F", fx(sx - 30, sx + 30), (ty[1] + 60, ty[1] + 185), (wt - 5, wt + 55), "motor")
    # ------------------------------------------------------------ moves with Y: feet and carriages
    add(f"Foot inner {sn}", "Y", fx(310, STEP_X), (6, 280), (155, BZ0))
    add(f"Foot step {sn}", "Y", fx(STEP_X, 445), (6, 280), (170, BZ0))
    for k, d in (("front", -Y_PITCH / 2), ("rear", Y_PITCH / 2)):
        add(f"Y block {k} {sn}", "Y", fx(rx - BL_W / 2, rx + BL_W / 2), mid(CAR_Y + d, BL_L), (wt + BL_H1, wt + BL_H), "block")
    add(f"Y housing {sn}", "Y", fx(sx - HS_W / 2, sx + HS_W / 2), mid(CAR_Y, HS_L), (130, 170), "al")
    add(f"Y nut {sn}", "Y", fx(sx - NUT_D / 2, sx + NUT_D / 2), mid(CAR_Y, NUT_L), (150 - NUT_D / 2, 150 + NUT_D / 2), "steel")
    add(f"Y flange {sn}", "Y", fx(sx - FL_D / 2, sx + FL_D / 2), ((CAR_Y - NUT_L / 2, CAR_Y - NUT_L / 2 + FL_T) if FIXES else (CAR_Y + NUT_L / 2 - FL_T, CAR_Y + NUT_L / 2)), (150 - FL_D / 2, 150 + FL_D / 2), "steel")

# ---------------------------------------------------------------- moves with Y: beam and X drive
add("Beam SHS 150x150x8", "Y", (-BEAM_HALF, BEAM_HALF), (B0, B1), (BZ0, BZ1), "beam")
add("Top seat", "Y", (-325, 325), (FLAT0, FLAT1), (BZ1, SEAT_TOP), "seat")
add("Bottom seat", "Y", (-305, 305), (FLAT0, FLAT1), (SEAT_BOT, BZ0), "seat")
add("X rail top", "Y", (-300, 300), mid(RAIL_Y, RAIL_W), (SEAT_TOP, SEAT_TOP + RAIL_H), "rail")
add("X rail bottom", "Y", (-300, 300), mid(RAIL_Y, RAIL_W), (SEAT_BOT - RAIL_H, SEAT_BOT), "rail")
add("X screw", "Y", (-319, 381), mid(SCREW_Y, 16), mid(SCREW_Z, 16), "screw")
add("X BK12", "Y", (290, 315), mid(SCREW_Y, BK_W), (SEAT_TOP, SEAT_TOP + BK_H), "steel")
add("X BK lock nut", "Y", (315, 327), mid(SCREW_Y, 30), mid(SCREW_Z, 30), "steel")
add("X BF12", "Y", (-310, -290), mid(SCREW_Y, BK_W), (SEAT_TOP, SEAT_TOP + BK_H), "steel")
add("X pulley screw", "Y", (PUL_X0, PUL_X0 + PUL_W + PUL_HUB), mid(SCREW_Y, PUL_OD), mid(SCREW_Z, PUL_OD), "motor")
add("X pulley motor", "Y", (PUL_X0, PUL_X0 + PUL_W + PUL_HUB), mid(MOTOR_Y, PUL_OD), mid(SCREW_Z, PUL_OD), "motor")
add("X belt", "Y", (PUL_X0 + 3, PUL_X0 + PUL_W - 3), (SCREW_Y - 20, MOTOR_Y + 20), mid(SCREW_Z, 40), "belt")
add("X outboard bearing", "Y", (PUL_X0 + PUL_W + PUL_HUB + 2, PUL_X0 + PUL_W + PUL_HUB + 16), mid(SCREW_Y, 60), mid(SCREW_Z, 36), "steel")
add("X motor plate", "Y", (PUL_X0 - 10, PUL_X0 - 2), (B1, MOTOR_Y + 34), (BZ1 - 60, SCREW_Z + 34), "al")
add("X motor", "Y", (PUL_X0 - 10 - MOT_LEN, PUL_X0 - 10), mid(MOTOR_Y, MOT_SQ), mid(SCREW_Z, MOT_SQ), "motor")

# ---------------------------------------------------------------- moves with X: saddle (centred on X 0 here)
add("Saddle front plate", "X", (-90, 90), (125, 145), (70, 470))
add("Top arm", "X", (-90, 90), (145, 275), (394, 419))
add("Bottom arm", "X", (-90, 90), (145, 275), (136, 161))
for sn, s in (("R", 1), ("L", -1)):
    xb = mid(s * X_PITCH / 2, BL_L)
    add(f"X block top {sn}", "X", xb, mid(RAIL_Y, BL_W), (SEAT_TOP + BL_H1, SEAT_TOP + BL_H), "block")
    add(f"X spacer {sn}", "X", xb, mid(RAIL_Y, BL_W), (SEAT_TOP + BL_H, 394))
    add(f"X block bottom {sn}", "X", xb, mid(RAIL_Y, BL_W), (SEAT_BOT - BL_H, SEAT_BOT - BL_H1), "block")
    add(f"Z riser {sn}", "X", mid(s * 50, 25), (110, 125), (95, 445))
    add(f"Z rail {sn}", "X", mid(s * 50, RAIL_W), (110 - RAIL_H, 110), (95, 445), "rail")
add("X housing", "X", mid(0, HS_L), mid(SCREW_Y, HS_W), (354, 394))
add("X nut", "X", mid(0, NUT_L), mid(SCREW_Y, NUT_D), mid(SCREW_Z, NUT_D), "steel")
add("X flange", "X", (NUT_L / 2 - FL_T, NUT_L / 2), mid(SCREW_Y, FL_D), mid(SCREW_Z, FL_D), "steel")
add("Z motor (position assumed)", "X", (-30, 30), (70, 130), (480, 626), "motor")

# ---------------------------------------------------------------- moves with Z (drawn with the nose tip at Z 0)
add("Z plate", "Z", (-70, 70), (60, 80), (45, 245))
for sn, s in (("R", 1), ("L", -1)):
    for k, d in (("low", -Z_PITCH / 2), ("high", Z_PITCH / 2)):
        add(f"Z block {k} {sn}", "Z", mid(s * 50, BL_W), (80, 110 - BL_H1), mid(145 + d, BL_L), "block")
add("Spindle clamp", "Z", (-58, 58), (-50, 60), (70, 130))
add("Spindle body", "Z", (-40, 40), (-40, 40), (52, 282), "spindle")
add("Spindle nose", "Z", (-17, 17), (-17, 17), (0, 52), "spindle")

# ---------------------------------------------------------------- clash check
ALLOWED = [  # these pairs overlap or touch on purpose (a part running on, inside or bolted to the other)
    ("X rail top", "X block top"), ("X rail bottom", "X block bottom"), ("Y rail", "Y block"), ("Z rail", "Z block"),
    ("X screw", "X nut"), ("X screw", "X flange"), ("X screw", "X housing"), ("X screw", "X BK"), ("X screw", "X BF"),
    ("X screw", "X pulley screw"), ("X screw", "X outboard"), ("X nut", "X housing"), ("X nut", "X flange"),
    ("X flange", "X housing"), ("Y screw", "Y nut"), ("Y screw", "Y flange"), ("Y screw", "Y housing"), ("Y screw", "Y BK"),
    ("Y screw", "Y BF"), ("Y nut", "Y housing"), ("Y nut", "Y flange"), ("Y flange", "Y housing"), ("X belt", "X pulley"),
    ("X BK12", "X BK lock"), ("Spindle body", "Spindle clamp"), ("Spindle body", "Spindle nose"), ("Spindle nose", "Spindle clamp"),
    ("X screw", "X belt"),
] + ([("Top arm", "X flange"), ("Foot step", "Y flange")] if FIXES else [])  # relief slots 12 x 30 x 5 deep
def allowed(a, b):
    return any((a.startswith(p) and b.startswith(q)) or (a.startswith(q) and b.startswith(p)) for p, q in ALLOWED)

def place(b, sy, xs, zn):
    dy = 0.0 if b["group"] == "F" else sy
    dx = xs if b["group"] in "XZ" else 0.0
    dz = zn if b["group"] == "Z" else 0.0
    return (b["x"][0] + dx, b["x"][1] + dx), (b["y"][0] + dy, b["y"][1] + dy), (b["z"][0] + dz, b["z"][1] + dz)

def gap(p, q):
    d = [max(p[i][0] - q[i][1], q[i][0] - p[i][1]) for i in range(3)]
    if all(v < 0 for v in d):
        return max(d)                            # overlap: smallest depth to separate them
    return math.sqrt(sum(max(v, 0) ** 2 for v in d))

grid_y = sorted(set([SPY[0], SPY[1]] + [SPY[0] + 25 * i for i in range(15)]))
grid_x = [-XS_MAX + 25 * i for i in range(17)]
results = []
for a, b in itertools.combinations(boxes, 2):
    if allowed(a["name"], b["name"]):
        continue
    gs = {a["group"], b["group"]}
    ys = grid_y if "F" in gs and gs != {"F"} else [0.0]
    xs = grid_x if len(gs) > 1 and gs & {"X", "Z"} else [0.0]
    zs = ZN if len(gs) > 1 and "Z" in gs else [ZN[1]]
    best = None
    for sy, x0, zn in itertools.product(ys, xs, zs):
        g = gap(place(a, sy, x0, zn), place(b, sy, x0, zn))
        if best is None or g < best[0]:
            best = (g, sy, x0, zn)
    results.append(dict(a=a["name"], b=b["name"], same_group=a["group"] == b["group"], gap=round(best[0], 2),
                        spindle_y=best[1], saddle_x=best[2], nose_z=best[3]))

def status(r):
    if r["gap"] < 0:
        return "CLASH"
    if r["gap"] == 0:
        return "TOUCH"
    return "TIGHT" if r["gap"] < 3 else "ok"

near = [dict(r, status=status(r)) for r in sorted(results, key=lambda r: r["gap"]) if r["gap"] < 6 and not (r["same_group"] and r["gap"] == 0)]

# ---------------------------------------------------------------- wrench access through the Ø20 holes in the top wall
M10 = [(x, 190.0) for x in (345.0, 420.0)] + [(x, 262.0) for x in ((395.0, 430.0) if FIXES else (345.0, 420.0))]
HOLES = [(s * x, y) for s in (1, -1) for x, y in M10]
access = []
for hx, hy in HOLES:
    col = ((hx - 10, hx + 10), (hy - 10, hy + 10), (BZ1, 520.0))
    blocked = [b["name"] for b in boxes if b["group"] == "Y" and not b["name"].startswith(("Beam", "Foot", "Y ", "Top seat", "Bottom seat"))
               and gap(col, (b["x"], b["y"], b["z"])) < 0]
    access.append(dict(x=hx, yg=hy, blocked_by=blocked))

# ---------------------------------------------------------------- bolts
m5 = [(345 + i * BL_B / 2, CAR_Y + d + j * BL_C / 2) for i in (-1, 1) for j in (-1, 1) for d in (-Y_PITCH / 2, Y_PITCH / 2)]
m10 = M10
bolts = dict(
    m10_to_nearest_block_bolt=round(min(math.dist(p, q) for p in m10 for q in m5), 1),
    m10_edge_to_foot_rear=280 - 262 - 5,
    thread_into_foot=30 - 8,
    foot_left_under_thread_inner=40 - 22,
    foot_left_under_thread_step=25 - 22,
    rail_bolt_thread_in_wall=round(20 - (RAIL_H - 8.5) - SEAT, 1),
    rail_edge_past_flat_start=(RAIL_Y - RAIL_W / 2) - FLAT0,
    bk_edge_inside_flat_end=FLAT1 - (SCREW_Y + BK_W / 2),
    x_block_end_on_rail=300 - (XS_MAX + X_PITCH / 2 + BL_L / 2),
    y_block_front_on_rail=round(SPY[0] + CAR_Y - Y_PITCH / 2 - BL_L / 2 - YC["rail_y"][0], 2),
    y_block_rear_on_rail=round(YC["rail_y"][1] - (SPY[1] + CAR_Y + Y_PITCH / 2 + BL_L / 2), 2),
    foot_centre_yg=(6 + 280) / 2,
    carriage_centre_yg=CAR_Y,
)

# ---------------------------------------------------------------- moving mass (Y axis)
old = {n: (k, y) for n, k, y in T["moving"]}
def keep(prefix):
    return next(v for n, v in old.items() if n.startswith(prefix))
beam_kg = (150 ** 2 - 134 ** 2) * 890 * STEEL
foot_kg = (70 * 274 * 40 + 65 * 274 * 25) * AL
screw_kg = 0.7 * 1.58 + 0.6 + 0.4
masses = [
    ("spindle (assumed)", *keep("spindle 2.2")), ("spindle clamp", *keep("spindle clamp")), ("Z plate", *keep("Z plate")),
    ("Z motor + mount (assumed)", *keep("Z motor")), ("Z screw + nut + BK/BF", *keep("Z screw")), ("Z rails + blocks", *keep("Z rails")),
    ("Z risers", *keep("Z risers")),
    ("saddle front plate 180x400x20", 180 * 400 * 20 * AL, 135.0),
    ("2 saddle arms 180x130x25", 2 * 180 * 130 * 25 * AL, 210.0),
    ("4 X blocks + nut housing + 2 spacers", 4 * 0.4 + 0.5 + 2 * 77.5 * 44 * 15 * AL, RAIL_Y + 8),
    ("X rails 2x600", 2 * 0.6 * 2.21, RAIL_Y),
    ("X screw 700 + nut + BK/BF", screw_kg, SCREW_Y),
    ("X motor + plate + belt (assumed)", 2.0, MOTOR_Y),
    ("beam SHS 150x150x8, 890", beam_kg, (B0 + B1) / 2),
    ("2 feet (solid)", 2 * foot_kg, 143.0),
    ("4 Y blocks + 2 Y nut housings", 4 * 0.4 + 2 * 0.3, CAR_Y),
]
total = sum(k for _, k, _ in masses)
com = sum(k * y for _, k, y in masses) / total
rear_share = 0.5 + (com - CAR_Y) / Y_PITCH        # static share of the weight on the two rear Y blocks
mass = dict(total_kg=round(total, 1), beam_kg=round(beam_kg, 1), com_yg=round(com, 1), carriages_yg=CAR_Y, com_behind_carriages=round(com - CAR_Y, 1),
            rear_blocks_share_pct=round(100 * rear_share, 1),
            parts=[(n, round(k, 2), y) for n, k, y in masses])

report = dict(near=near, clashes=sum(r["status"] == "CLASH" for r in near), access=access, bolts=bolts, mass=mass)
(OUT / ("steel_gantry_sketch_fixes.json" if FIXES else "steel_gantry_sketch.json")).write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")

if FIXES:
    for r in near:
        if r["status"] != "ok":
            print(f"{r['status']:6} {r['gap']:7.2f}  {r['a']} / {r['b']}")
    print("clashes:", report["clashes"], "| blocked holes:", [(h["x"], h["yg"], h["blocked_by"]) for h in access if h["blocked_by"]])
    print("nearest M10 to a Y block bolt:", bolts["m10_to_nearest_block_bolt"], "| X block end on rail:", bolts["x_block_end_on_rail"])
    sys.exit(0)

# ---------------------------------------------------------------- drawing
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

COL = dict(al="#9fb7cf", eg="#c9c2b4", table="#e8dcc0", rail="#333333", screw="#b04a2f", steel="#8d8d8d", block="#5a7fa8",
           motor="#5b5b5b", beam="#d9a441", seat="#3f9c6b", belt="#222222", spindle="#eeeeee")
AX = {"x": 0, "y": 1, "z": 2}

def draw(ax, u, v, sy, xs, zn, pick, order, alpha=1.0):
    items = [(b, place(b, sy, xs, zn)) for b in boxes if pick(b)]
    items.sort(key=lambda t: order(t[1]))
    for b, p in items:
        a, c = p[AX[u]], p[AX[v]]
        al = alpha * (0.55 if b["name"].startswith(("Top arm", "Saddle")) and u == "x" else 1.0)
        ax.add_patch(Rectangle((a[0], c[0]), a[1] - a[0], c[1] - c[0], fc=COL[b["mat"]], ec="k", lw=0.5, alpha=al))

def label(ax, x, y, tx, ty_, text, color="k"):
    ax.annotate(text, (x, y), (tx, ty_), fontsize=7.5, color=color, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.5, color="#555"), bbox=dict(fc="white", ec="#bbb", lw=0.4, pad=1.5))

def dim(ax, p0, p1, text, off=(0, 0)):
    ax.annotate("", p0, p1, arrowprops=dict(arrowstyle="<->", lw=0.7))
    ax.text((p0[0] + p1[0]) / 2 + off[0], (p0[1] + p1[1]) / 2 + off[1], text, fontsize=7.5, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=0.6))

fig = plt.figure(figsize=(18, 12.5))
gs_ = fig.add_gridspec(2, 2, width_ratios=[1, 1.45], height_ratios=[1.25, 1])
a1, a2, a3, a4 = fig.add_subplot(gs_[0, 0]), fig.add_subplot(gs_[0, 1]), fig.add_subplot(gs_[1, 1]), fig.add_subplot(gs_[1, 0])

# A: section through the saddle, looking along X
draw(a1, "y", "z", 0, 0, ZN[1], lambda b: b["group"] in "XYZ" and b["x"][0] < 90 and b["x"][1] > -90 and not b["name"].startswith("X motor"),
     lambda p: abs((p[0][0] + p[0][1]) / 2))
draw(a1, "y", "z", 0, 0, ZN[1], lambda b: b["name"] == "Table", lambda p: 0)
for t in (((B0 + 8, BZ0 + 8), B1 - B0 - 16, BZ1 - BZ0 - 16),):
    a1.add_patch(Rectangle(t[0], t[1], t[2], fc="white", ec="k", lw=0.4))
label(a1, 225, 270, 225, 270, "SHS 150 x 150 x 8")
label(a1, 210, 406, 300, 450, "top arm 180 x 130 x 25")
label(a1, 210, 148, 305, 105, "bottom arm 180 x 130 x 25")
label(a1, 135, 455, 275, 585, "front plate 180 x 400 x 20")
label(a1, 186, 385, 300, 515, "top X rail and block\n15 spacer on the block")
label(a1, 236, 374, 345, 374, "X screw Z 374\nDSG16H housing")
label(a1, 186, 180, 330, 165, "bottom X rail and block")
label(a1, 225, 347, 345, 325, "epoxy seats, 4 thick")
dim(a1, (150, 60), (300, 60), "beam 150 wide", off=(0, -16))
dim(a1, (0, 20), (150, 20), "spindle offset 150")
a1.set_title("A. Section through the saddle, looking along X (saddle at the centre, spindle up)", fontsize=10)
a1.set_xlim(-90, 400); a1.set_ylim(-5, 640); a1.set_aspect("equal"); a1.axis("off")

# B: front view with the saddle at the right end of travel
draw(a2, "x", "z", SPY[1], XS_MAX, ZN[1], lambda b: b["group"] in "FYXZ" and not b["name"].startswith(("Y motor", "Tub floor")), lambda p: -p[1][0])
dim(a2, (-445, 500), (445, 500), "beam 890")
dim(a2, (-300, 450), (300, 450), "X rails 600")
label(a2, 289, 365, 415, 455, "block end 288.75, BK12 face 290:\n1.25 gap at the end of travel")
label(a2, 380, 165, 470, 95, "foot step X 380 to 445\nunderside Z 170")
label(a2, 345, 140, 250, 95, "Y rail and block, X 345")
a2.set_title("B. Front view, saddle at the right end of travel (X +200)", fontsize=10)
a2.set_xlim(-520, 560); a2.set_ylim(-10, 650); a2.set_aspect("equal"); a2.axis("off")

# C: beam top view
draw(a3, "x", "y", 0, XS_MAX, ZN[1], lambda b: b["group"] in "YX" and not b["name"].startswith(("Top arm", "Bottom arm", "Saddle", "Z ")), lambda p: p[2][1])
for b in boxes:
    if b["name"] == "Top arm":
        p = place(b, 0, XS_MAX, ZN[1])
        a3.add_patch(Rectangle((p[0][0], p[1][0]), 180, 130, fc="none", ec="#1f5fbf", lw=1.3, ls="--"))
for h in access:
    c = "#c0172c" if h["blocked_by"] else "#0a7d33"
    a3.add_patch(plt.Circle((h["x"], h["yg"]), 10, fc="white", ec=c, lw=1.6, zorder=6))
label(a3, 345, 262, 470, 430, "red: Ø20 access hole under the X belt", "#c0172c")
label(a3, 290, 210, 120, 40, "top arm outline, saddle at X +200 (blue dashed)", "#1f5fbf")
label(a3, 260, 373, 130, 430, "X motor behind the beam, body inboard")
label(a3, -300, 186, -300, 110, "X rail: beam front + 36")
label(a3, -200, 236, -200, 335, "X screw: beam front + 86")
a3.set_title("C. Beam top view (Y up the page = further behind the spindle). Green circles: wrench access clear", fontsize=10)
a3.set_xlim(-470, 560); a3.set_ylim(-10, 470); a3.set_aspect("equal"); a3.axis("off")

# D: section on the right Y screw axis (X 410) at the rear of travel
draw(a4, "y", "z", SPY[1], 0, ZN[1], lambda b: b["x"][0] <= 410 <= b["x"][1] and b["group"] in "FY" and not b["name"].startswith(("Tub floor", "Beam", "Top seat", "Bottom seat", "X ")),
     lambda p: 0)
p0 = SPY[1]
a4.add_patch(Rectangle((B0 + p0, BZ0), B1 - B0, BZ1 - BZ0, fc=COL["beam"], ec="k", lw=0.5))
a4.add_patch(Rectangle((B0 + p0 + 8, BZ0 + 8), B1 - B0 - 16, BZ1 - BZ0 - 16, fc="white", ec="k", lw=0.4))
label(a4, p0 + 60, 182, p0 + 20, 262, "foot step, underside Z 170")
label(a4, p0 + CAR_Y + 45, 172, p0 + 40, 75, "round Ø48 nut flange reaches Z 174:\n4 into the foot step", "#c0172c")
label(a4, ty[1] + 30, 170, ty[1] + 70, 245, "Y motor mount: 6.25 behind the foot")
label(a4, 332, 160, 420, 40, "Y BK12 under the step (top 168, step 170)")
a4.set_title("D. Section on the right Y screw (X 410), gantry at the back of travel (spindle Y +125)", fontsize=10)
a4.set_xlim(60, 640); a4.set_ylim(-10, 370); a4.set_aspect("equal"); a4.axis("off")

n = report["clashes"]
fig.suptitle(f"Type 0 steel gantry layout, PROPOSAL, not agreed (D-164). Clash check: {n} clashes, see docs/steel-gantry-sketch.md", fontsize=13)
fig.tight_layout(rect=(0, 0, 1, 0.965))
fig.savefig(OUT / "steel_gantry_sketch.png", dpi=110)

# ---------------------------------------------------------------- console
print(f"{'status':6} {'gap':>7}  pair (worst position: spindle Y, saddle X, nose Z)")
for r in near:
    print(f"{r['status']:6} {r['gap']:7.2f}  {r['a']} / {r['b']}  ({r['spindle_y']:.0f}, {r['saddle_x']:.0f}, {r['nose_z']:.0f})")
print("\nAccess holes:")
for h in access:
    print(f"  X {h['x']:.0f}, Yg {h['yg']:.0f}: {'clear' if not h['blocked_by'] else 'BLOCKED by ' + ', '.join(h['blocked_by'])}")
print("\nBolts and limits:", json.dumps(bolts, indent=1))
print("\nMoving mass:", mass["total_kg"], "kg, centre of mass Yg", mass["com_yg"], "=", mass["com_behind_carriages"], "behind the carriages; rear Y blocks carry", mass["rear_blocks_share_pct"], "%")

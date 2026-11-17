"""Task 22 step 1: moving-gantry sketch (D-137, D-138). Numbers + one PNG, no STEP.

Run: PYTHONUTF8=1 python cad/v2/gantry_sketch.py
  -> cad/v2/out/gantry_sketch.png   top view, front section (X-Z), side section (Y-Z)
  -> cad/v2/out/gantry_sketch.json  every derived number (the md quotes these)

Coordinates: X right, Y back, Z up. Z 0 = top of the tub floor (table seat).
Y 0 = centre of the work area. Every size here is a PROPOSAL for the owner, not a decision.
Masses of bought parts marked ASSUMED are catalogue-typical values, not from our parts.
"""
import json, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import type0_v2 as m

P = m.P
OUT = pathlib.Path(__file__).parent / "out"; OUT.mkdir(exist_ok=True)
EG, AL = 2300e-9, 2700e-9            # kg/mm3
E_AL, G_AL = 69000.0, 26000.0        # N/mm2, 6082

def r50(x):                          # LiMo sells screws and rails in 50 mm steps
    return int(math.ceil(x / 50.0) * 50)

# ---------------------------------------------------------------- inputs (from type0_v2 / assembly.py)
work_x, work_y, trav_z = P["travel_x_work"], P["travel_y"], P["travel_z"]   # 400, 250, 150
tab_x, tab_y, tab_t = P["table_x"], P["table_y"], P["table_t"]              # 460, 330, 25
saddle_w, stack = P["saddle_w"], P["spindle_stack"]                         # 180, 175 (D-106)
blk_h, blk_l, y_pitch, x_pitch = 30.0, 77.5, P["y_block_pitch"], P["x_block_pitch"]
beam_h, beam_d, beam_t = 150.0, 130.0, 10.0                                 # D-137 check section

S = {}
S["table_top"] = tab_t                                   # table bolted straight on the floor, fly-cut on the machine
S["nose_top"] = S["table_top"] + P["nose_clear"]          # 180 under the nose at the top (D-09)
S["nose_bot"] = S["nose_top"] - trav_z
S["beam_zc"] = S["nose_top"] + 65                        # same Z stack as now (assembly.py: 300 - 235)
S["beam_z"] = (S["beam_zc"] - beam_h / 2, S["beam_zc"] + beam_h / 2)
S["saddle_z0"] = S["beam_zc"] - 200                      # 400-tall saddle, unchanged
S["saddle_x_sweep"] = work_x / 2 + saddle_w / 2          # 290
S["wall_in_x"] = S["saddle_x_sweep"] + 15                # 305: saddle clears the walls
wall_w = 140.0
S["wall_w"] = wall_w
S["rail_x"] = S["wall_in_x"] + 40                        # rail on the wall top, 40 from the inner edge
S["screw_x"] = S["rail_x"] + 65                          # screw outboard of the rail, same wall top (proposal A)
S["wall_out_x"] = S["wall_in_x"] + wall_w                # 445
S["span"] = 2 * S["rail_x"]                              # beam span between Y rails
S["floor_t"] = 60.0
S["wall_top"] = S["table_top"] + 100                     # proposal: walls 100 above the table
S["car_top"] = S["wall_top"] + blk_h
S["foot_t"] = S["beam_z"][0] - S["car_top"]              # foot block fills the gap to the beam
S["beam_len"] = 2 * (S["screw_x"] + 35)

# ---------------------------------------------------------------- moving mass (Y axis)
rail_kgm, blk_kg = 2.21, 0.40                            # HGR20 / HGH20CA catalogue (ASSUMED)
screw_kgm, nut_kg, bkbf_kg = 1.58, 0.60, 0.40            # steel Ø16; DFU1605 nut; BK12+BF12 (ASSUMED)
x_rail = r50(work_x + x_pitch + blk_l + 20)
x_screw = r50(work_x + 253)                              # same end allowance as the X screw now (823 for 570 travel)
foot_l = y_pitch + blk_l + 40
beam_area = beam_h * beam_d - (beam_h - 2 * beam_t) * (beam_d - 2 * beam_t)
# (name, kg, Y of its centre measured back from the spindle axis)
parts = [
    ("spindle 2.2 kW ISO20 (ASSUMED 7 kg)", 7.0, 0),
    ("spindle clamp", 0.8, 40),
    ("Z plate 140x200x20", 140 * 200 * 20 * AL, 70),
    ("Z motor with brake + mount (ASSUMED)", 2.0, 35),
    ("Z screw 350 + nut + BK/BF", 0.35 * screw_kgm + nut_kg + bkbf_kg, 100),
    ("Z rails 2x350 + 4 blocks", 0.7 * rail_kgm + 4 * blk_kg, 95),
    ("Z risers", 2 * 25 * 15 * 350 * AL, 112),
    ("saddle 180x400x20", 180 * 400 * 20 * AL, 125),
    ("X blocks (4) + nut housing + spacer", 4 * blk_kg + 0.5, 155),
    (f"X rails 2x{x_rail}", 2 * x_rail / 1000 * rail_kgm, 166),
    (f"X screw {x_screw} + nut + BK/BF", x_screw / 1000 * screw_kgm + nut_kg + bkbf_kg, 160),
    ("X motor + plate + belt (ASSUMED)", 2.0, 240),
    (f"beam box {beam_h:.0f}x{beam_d:.0f}x{beam_t:.0f}, {S['beam_len']:.0f} long", beam_area * S["beam_len"] * AL, stack + beam_d / 2),
]
fixed_kg = sum(k for _, k, _ in parts)
com = sum(k * y for _, k, y in parts) / fixed_kg
S["car_y_from_spindle"] = 5 * round(com / 5)             # Y carriages centred under the moving mass
foot_kg = foot_l * (S["wall_w"]) * S["foot_t"] * AL * 0.7   # 2 feet, pocketed to about 70 %
parts += [(f"2 foot blocks {foot_l:.0f}x{S['wall_w']:.0f}x{S['foot_t']:.0f} (pocketed)", 2 * foot_kg, S["car_y_from_spindle"]),
          ("4 Y blocks + 2 Y nut housings", 4 * blk_kg + 2 * 0.3, S["car_y_from_spindle"])]
S["moving_kg"] = sum(k for _, k, _ in parts)

# ---------------------------------------------------------------- Y lengths, two cases (ATC reach)
def y_case(front_extra):
    c = {}
    c["spindle_y"] = (-work_y / 2 - front_extra, work_y / 2)
    c["travel"] = c["spindle_y"][1] - c["spindle_y"][0]
    c["car_y"] = tuple(y + S["car_y_from_spindle"] for y in c["spindle_y"])
    half = y_pitch / 2 + blk_l / 2 + 5
    c["rail_need"] = c["travel"] + y_pitch + blk_l + 10
    c["rail_buy"] = r50(c["rail_need"])
    c["rail_y"] = (c["car_y"][0] - half, c["car_y"][0] - half + c["rail_buy"])
    # screw: BF at the front, BK + direct motor at the back; nut 100 long centred on the carriages
    bf_y0 = c["car_y"][0] - 50 - 5 - 20
    bk_y1 = c["car_y"][1] + 50 + 5 + 37
    c["screw_need"] = (bk_y1 - bf_y0) + 15 + 40       # BF stub + drive stub into the coupling
    c["screw_buy"] = r50(c["screw_need"])
    c["bf_y0"], c["bk_y1"] = bf_y0, bk_y1
    c["tub_y"] = (min(c["rail_y"][0] - 15, bf_y0 - 15, -tab_y / 2 - 20), max(c["rail_y"][1], bk_y1) + 15)
    c["tub_len"] = c["tub_y"][1] - c["tub_y"][0]
    c["motor_end_y"] = c["tub_y"][1] + 60 + 125         # mount 60 + motor with encoder 125
    return c

Y = {"no_reach": y_case(0.0), "atc_reach_100": y_case(100.0)}

# ---------------------------------------------------------------- tub masses (solid unless stated)
def tub_kg(L, floor_t=S["floor_t"], wall_top=S["wall_top"], back=0.0, core_d=0.0):
    W = 2 * S["wall_out_x"]
    v = W * L * floor_t                                  # floor, full outside width
    v += 2 * wall_w * L * wall_top                       # walls above the floor top
    v += back * (2 * S["wall_in_x"]) * wall_top          # back wall between the walls, inside the length
    v -= 2 * math.pi * (core_d / 2) ** 2 * L             # one core per wall, along Y
    return v * EG

L0 = Y["atc_reach_100"]["tub_len"]
L1 = Y["no_reach"]["tub_len"]
variants = []
for name, L, kw in [
    ("A  baseline: floor 60, walls 140 x 100 above the table, no back wall, ATC reach", L0, {}),
    ("B  as A + back wall 100 thick", L0, dict(back=100.0)),
    ("C  as A, floor 80", L0, dict(floor_t=80.0)),
    ("D  as A, walls only 50 above the table (gantry gets 50 mm legs)", L0, dict(wall_top=S["table_top"] + 50)),
    ("E  as A + one Ø60 PVC core per wall", L0, dict(core_d=60.0)),
    ("F  as A without the ATC reach (tub shorter)", L1, {}),
]:
    kg = tub_kg(L, **kw)
    variants.append(dict(name=name, kg=round(kg, 1), epoxy_11=round(0.11 * kg, 1), epoxy_12=round(0.12 * kg, 1)))
# core check: Ø60 centred in the 140 wall, top 20 under the rail bar (bar bottom = wall top - 5 - 10)
core_zc = S["wall_top"] - 15 - 20 - 30
S["core_cover_side"] = (wall_w - 60) / 2
S["core_cover_top"] = (S["wall_top"] - 15) - (core_zc + 30)
S["core_cover_bottom"] = (core_zc - 30) + S["floor_t"]

# ---------------------------------------------------------------- beam stiffness
Iz = (beam_h * beam_d ** 3 - (beam_h - 2 * beam_t) * (beam_d - 2 * beam_t) ** 3) / 12   # bending under a Y load
Iy = (beam_d * beam_h ** 3 - (beam_d - 2 * beam_t) * (beam_h - 2 * beam_t) ** 3) / 12   # bending under a Z load
Am = (beam_h - beam_t) * (beam_d - beam_t); J = 4 * Am ** 2 * beam_t / (2 * ((beam_h - beam_t) + (beam_d - beam_t)))
F, Ls = 200.0, S["span"]
arm = S["beam_zc"] - S["table_top"]                     # Y force at the tool near the table, twisting the beam
B = dict(
    Iz_mm4=Iz, Iy_mm4=Iy, J_mm4=J,
    EI_y_load_MNm2=E_AL * Iz / 1e12, EI_z_load_MNm2=E_AL * Iy / 1e12,
    span=Ls,
    dY_simple_um=F * Ls ** 3 / (48 * E_AL * Iz) * 1000, dY_fixed_um=F * Ls ** 3 / (192 * E_AL * Iz) * 1000,
    dZ_simple_um=F * Ls ** 3 / (48 * E_AL * Iy) * 1000, dZ_fixed_um=F * Ls ** 3 / (192 * E_AL * Iy) * 1000,
    twist_arm=arm, twist_tool_um=(F * arm / 2) * (Ls / 2) / (G_AL * J) * arm * 1000,
    beam_kg=beam_area * S["beam_len"] * AL,
)

# ---------------------------------------------------------------- ATC wheel (8 forks, 70 pitch, D-138)
w_pcd = P["wheel_pockets"] * P["pocket_pitch"] / math.pi             # 178
A = dict(pcd=w_pcd, outer_d=w_pcd + 70, pickup=(150.0, Y["atc_reach_100"]["spindle_y"][0]),
         centre=(150.0, Y["atc_reach_100"]["spindle_y"][0] - w_pcd / 2),
         fork_z=S["table_top"] + 40)

out = dict(S=S, Y=Y, variants=variants, beam=B, atc=A, x_rail=x_rail, x_screw=x_screw, foot_l=foot_l,
           moving=[(n, round(k, 2), y) for n, k, y in parts], com_from_spindle=com)
(OUT / "gantry_sketch.json").write_text(json.dumps(out, indent=1, default=float))

# ---------------------------------------------------------------- drawing
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

c = Y["atc_reach_100"]; ty0, ty1 = c["tub_y"]
EGc, ALc, RL, TB, SC = "#c9c2b4", "#9fb7cf", "#333333", "#e8dcc0", "#b04a2f"
fig = plt.figure(figsize=(17, 11))
gs = fig.add_gridspec(2, 2, width_ratios=[1.05, 1], height_ratios=[1.2, 1])
ax1, ax2, ax3 = fig.add_subplot(gs[:, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])

def rect(ax, x0, y0, x1, y1, fc, ec="k", lw=0.8, **k):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, ec=ec, lw=lw, **k))

def dim(ax, p0, p1, text, off=(0, 0), fs=8):
    ax.annotate("", p0, p1, arrowprops=dict(arrowstyle="<->", lw=0.7))
    ax.text((p0[0] + p1[0]) / 2 + off[0], (p0[1] + p1[1]) / 2 + off[1], text, ha="center", va="center", fontsize=fs,
            bbox=dict(fc="white", ec="none", pad=0.5))

wi, wo, rx, sx = S["wall_in_x"], S["wall_out_x"], S["rail_x"], S["screw_x"]
# --- top view
for s in (-1, 1):
    rect(ax1, s * wi, ty0, s * wo, ty1, EGc)
    ax1.plot([s * rx] * 2, c["rail_y"], color=RL, lw=3)
    ax1.plot([s * sx] * 2, [c["bf_y0"], c["bk_y1"]], color=SC, lw=2)
    rect(ax1, s * sx - 30, ty1, s * sx + 30, c["motor_end_y"], "#777", lw=0.6)
rect(ax1, -wi, ty0, wi, ty1, "#ddd6c8", lw=0.5)
rect(ax1, -tab_x / 2, -tab_y / 2, tab_x / 2, tab_y / 2, TB)
rect(ax1, -work_x / 2, -work_y / 2, work_x / 2, work_y / 2, "none", ec="g", lw=1, ls="--")
ax1.text(0, 70, "table 460 x 330\nwork 400 x 250 (dashed)", ha="center", va="center", fontsize=9)
gy = c["car_y"][0] - S["car_y_from_spindle"]                       # gantry drawn at the front end, spindle at the ATC
by0 = gy + stack
rect(ax1, -S["beam_len"] / 2, by0, S["beam_len"] / 2, by0 + beam_d, ALc, alpha=0.75)
for s in (-1, 1):
    rect(ax1, s * wi, c["car_y"][0] - foot_l / 2, s * wo, c["car_y"][0] + foot_l / 2, ALc, alpha=0.6)
rect(ax1, A["pickup"][0] - saddle_w / 2, by0 - 60, A["pickup"][0] + saddle_w / 2, by0 - 30, ALc, alpha=0.6)
ax1.add_patch(Circle(A["pickup"], 40, fc="w", ec="k"))
ax1.add_patch(Circle(A["centre"], A["outer_d"] / 2, fc="none", ec="purple", lw=1.2))
ax1.add_patch(Circle(A["centre"], w_pcd / 2, fc="none", ec="purple", lw=0.6, ls=":"))
ax1.text(A["centre"][0], A["centre"][1] - A["outer_d"] / 2 - 25, "Phase 2 umbrella wheel (D-138)\npost on a bracket off the right wall front",
         ha="center", va="top", fontsize=8, color="purple")
ax1.text(-150, by0 + beam_d / 2, "gantry beam\n(front end of travel,\nspindle over the ATC pickup)", ha="center", va="center", fontsize=8)
ax1.text(-sx, ty1 + 95, "Y1\nmotor", ha="center", fontsize=7, color="w"); ax1.text(sx, ty1 + 95, "Y2\nmotor", ha="center", fontsize=7, color="w")
dim(ax1, (-wo, ty1 + 230), (wo, ty1 + 230), f"tub outside {2*wo:.0f}")
dim(ax1, (-wi, ty0 - 30), (wi, ty0 - 30), f"inside {2*wi:.0f}")
dim(ax1, (-wo - 40, ty0), (-wo - 40, ty1), f"tub {c['tub_len']:.0f}", off=(-35, 0))
dim(ax1, (-rx, ty1 - 40), (rx, ty1 - 40), f"Y rails {2*rx:.0f} apart = beam span")
dim(ax1, (rx + 75, c["rail_y"][0]), (rx + 75, c["rail_y"][1]), f"rail {c['rail_buy']}", off=(0, 0), fs=7)
ax1.text(sx, ty0 - 60, f"Y screw {c['screw_buy']}\n(outboard on\nthe wall top)", ha="center", va="top", fontsize=7, color=SC)
ax1.set_title("Top view (X right, Y back). Rails black, screws red, aluminium blue, EG grey", fontsize=10)
ax1.set_aspect("equal"); ax1.set_xlim(-wo - 130, wo + 60); ax1.set_ylim(A["centre"][1] - 230, ty1 + 270); ax1.axis("off")

# --- front section X-Z (through the gantry)
ft = S["floor_t"]
rect(ax2, -wo, -ft, wo, 0, EGc);
for s in (-1, 1):
    rect(ax2, s * wi, 0, s * wo, S["wall_top"], EGc)
    rect(ax2, s * rx - 10, S["wall_top"], s * rx + 10, S["wall_top"] + 17.5, RL)
    rect(ax2, s * rx - 22, S["wall_top"] + 4.6, s * rx + 22, S["car_top"], "#5a7fa8")
    ax2.add_patch(Circle((s * sx, S["wall_top"] + 25), 8, fc=SC, ec="k", lw=0.5))
    rect(ax2, s * wi, S["car_top"], s * wo, S["beam_z"][0], ALc)
rect(ax2, -tab_x / 2, 0, tab_x / 2, tab_t, TB)
rect(ax2, -S["beam_len"] / 2, S["beam_z"][0], S["beam_len"] / 2, S["beam_z"][1], ALc)
rect(ax2, -S["beam_len"] / 2 + beam_t, S["beam_z"][0] + beam_t, S["beam_len"] / 2 - beam_t, S["beam_z"][1] - beam_t, "w", lw=0.4, ls=":")
rect(ax2, -saddle_w / 2, S["saddle_z0"], saddle_w / 2, S["saddle_z0"] + 400, "none", ec="b", lw=0.8, ls="--")
rect(ax2, -40, S["nose_top"], 40, S["nose_top"] + 230, "#eee", lw=0.6)
rect(ax2, -17, S["nose_top"] - 52, 17, S["nose_top"], "#eee", lw=0.6)
for s in (-1, 1):
    ax2.plot([s * S["saddle_x_sweep"]] * 2, [S["saddle_z0"], S["saddle_z0"] + 60], "b:", lw=1)
dim(ax2, (-rx, S["beam_z"][1] + 140), (rx, S["beam_z"][1] + 140), f"span {S['span']:.0f}")
dim(ax2, (wo + 30, 0), (wo + 30, S["wall_top"]), f"{S['wall_top']:.0f}", off=(22, 0))
dim(ax2, (wo + 30, -ft), (wo + 30, 0), f"floor {ft:.0f}", off=(35, 0), fs=7)
dim(ax2, (-260, S["table_top"]), (-260, S["nose_top"] - 52), f"{P['nose_clear']} under\nthe nose", off=(-40, 0), fs=7)
dim(ax2, (-wi, -ft - 30), (wi, -ft - 30), f"{2*wi:.0f}: saddle sweep ±{S['saddle_x_sweep']:.0f} + 15", fs=7)
ax2.text(wo - 70, S["beam_z"][0] - 12, f"foot block {S['foot_t']:.0f} thick", fontsize=7, ha="center", va="top")
ax2.text(0, S["beam_zc"], f"beam box {beam_h:.0f} x {beam_d:.0f} x {beam_t:.0f} wall, {S['beam_len']:.0f} long", ha="center", fontsize=8)
ax2.text(0, S["saddle_z0"] + 8, f"saddle bottom {S['saddle_z0']-S['table_top']:.0f} above the table", ha="center", fontsize=7, color="b")
ax2.set_title("Front section through the gantry (X-Z). Z 0 = floor top", fontsize=10)
ax2.set_aspect("equal"); ax2.set_xlim(-wo - 120, wo + 110); ax2.set_ylim(-ft - 60, S["beam_z"][1] + 170); ax2.axis("off")

# --- side section Y-Z (through the right wall), gantry at both ends of travel
rect(ax3, ty0, -ft, ty1, 0, EGc); rect(ax3, ty0, 0, ty1, S["wall_top"], EGc)
rect(ax3, -tab_y / 2, 0, tab_y / 2, tab_t, TB, alpha=0.6)
ax3.plot(c["rail_y"], [S["wall_top"] + 9] * 2, color=RL, lw=3)
ax3.plot([c["bf_y0"], c["bk_y1"] + 40], [S["wall_top"] + 25] * 2, color=SC, lw=1.5)
rect(ax3, ty1, S["wall_top"], c["motor_end_y"], S["wall_top"] + 55, "#777", lw=0.6)
for k, sy in enumerate(c["spindle_y"]):
    a = 0.85 if k == 0 else 0.35
    cy = sy + S["car_y_from_spindle"]
    rect(ax3, cy - foot_l / 2, S["car_top"], cy + foot_l / 2, S["beam_z"][0], ALc, alpha=a)
    for d in (-y_pitch / 2, y_pitch / 2):
        rect(ax3, cy + d - blk_l / 2, S["wall_top"] + 4.6, cy + d + blk_l / 2, S["car_top"], "#5a7fa8", alpha=a)
    rect(ax3, sy + stack, S["beam_z"][0], sy + stack + beam_d, S["beam_z"][1], ALc, alpha=a)
    rect(ax3, sy + 115, S["saddle_z0"], sy + 145, S["saddle_z0"] + 400, ALc, alpha=a * 0.8)
    rect(ax3, sy - 40, S["nose_top"], sy + 40, S["nose_top"] + 230, "#eee", alpha=a)
    rect(ax3, sy - 17, S["nose_top"] - 52, sy + 17, S["nose_top"], "#eee", alpha=a)
ax3.text(c["spindle_y"][0], S["nose_top"] + 250, "front end:\nspindle at the ATC", ha="center", fontsize=7)
ax3.text(c["spindle_y"][1], S["nose_top"] + 250, "back end", ha="center", fontsize=7)
dim(ax3, (c["spindle_y"][0], -ft - 30), (c["spindle_y"][1], -ft - 30), f"spindle Y travel {c['travel']:.0f} (250 work + 100 to the ATC)", fs=7)
dim(ax3, (ty0, -ft - 75), (ty1, -ft - 75), f"tub {c['tub_len']:.0f}", fs=7)
dim(ax3, (c["spindle_y"][0], S["beam_z"][1] + 20), (c["spindle_y"][0] + stack, S["beam_z"][1] + 20), "175 (D-106)", fs=7)
ax3.set_title("Side section through the right wall (Y-Z): gantry at the front (dark) and back (light) of travel", fontsize=10)
ax3.set_aspect("equal"); ax3.set_xlim(A["centre"][1] - 60, c["motor_end_y"] + 30); ax3.set_ylim(-ft - 110, S["nose_top"] + 300); ax3.axis("off")

fig.suptitle("Type 0, task 22 sketch: moving gantry over a fixed table in one EG tub (D-137, D-138). PROPOSAL, not decided", fontsize=13)
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig(OUT / "gantry_sketch.png", dpi=110)

# ---------------------------------------------------------------- console summary
print(json.dumps(dict(S=S, beam=B, variants=variants), indent=1, default=float))
for k, v in Y.items():
    print(k, {kk: (round(vv, 1) if isinstance(vv, float) else vv) for kk, vv in v.items()})
print("x_rail", x_rail, "x_screw", x_screw, "moving kg", round(S["moving_kg"], 1), "COM from spindle", round(com, 1))
for n, k, y in parts:
    print(f"  {k:6.2f} kg  {n}")

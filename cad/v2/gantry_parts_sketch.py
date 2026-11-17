"""Task 22 step 4, before the STEP: gantry parts G01-G03 as a PROPOSAL for the owner (docs/task22-step4.md).

Run: PYTHONUTF8=1 python cad/v2/gantry_parts_sketch.py
  -> cad/v2/out/gantry_parts_sketch.png   front view, end view at the foot, beam section at mid-span
  -> cad/v2/out/gantry_parts_sketch.json  masses and key numbers

Local coordinates: X along the beam (0 = centre), Y back (0 = beam front face = rail seat), Z up (0 = beam bottom).
Bought-part sizes from cad/vendor/README.md and assembly.py (HIWIN HGR20/HGH20CA, Engder BK12/BF12, DFU1605, DSG16H).
"""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

OUT = pathlib.Path(__file__).parent / "out"; OUT.mkdir(exist_ok=True)
AL = 2700e-9

# ---- beam G01 + back plate G02 (D-147), proposal details
LEN, H, D = 890.0, 150.0, 130.0          # envelope incl. back plate (D-147)
PLATE = 10.0                             # G02
T_TB = 10.0                              # top and bottom walls
T_FRONT = 30.0                           # front wall (was 10): room for the X screw channel
CH_W, CH_D = 80.0, 20.0                  # X screw channel between the rails (rail inner edges at +-40)
PAD = 5.0                                # BK12/BF12 seat pads on the channel floor
END = 40.0                               # solid end blocks: beam-to-foot bolts go down through them
SHOULDER = 3.0                           # rail datum shoulder: under the block's 4.3 clearance (HGH20CA H1)
RAIL_Z = (H / 2 - 50, H / 2 + 50)        # 100 apart (D-104)
SPAN = 690.0; RAIL_X = SPAN / 2          # Y rails
FOOT_L, FOOT_W, FOOT_T = 268.0, 140.0, 40.0
WALL_IN = 305.0                          # foot X range 305..445 (over the wall top)
Y_SCREW_X = 410.0
CAR_Y = -35.0                            # carriage centre: 140 behind the spindle, spindle 175 in front of the face
Y_PITCH, BLK_L, BLK_W, BLK_H = 150.0, 77.5, 44.0, 30.0

# X screw stack (no D-108 spacer): saddle back at Y -30, DSG16H axis 20 from its face
X_AXIS_Y = -BLK_H + 20.0                 # -10
BK_BASE_Y = X_AXIS_Y + 25.0              # 15 = channel floor (20) - pad (5)
HOUSING_BACK_Y = -BLK_H + 40.0           # 10: 10 mm clear of the channel floor
FLANGE_BACK_Y = X_AXIS_Y + 24.0          # 14: 6 mm clear
SADDLE_X = 200.0; BLK_PITCH_X = 100.0
blk_reach = SADDLE_X + BLK_PITCH_X / 2 + BLK_L / 2      # 288.75: X blocks never pass this
BK_X0 = blk_reach + 1.25                 # 290: BK and BF sit beyond the block travel
BK = (BK_X0, BK_X0 + 25 + 12); BF = (-BK_X0 - 20, -BK_X0)
STUB_R = 54.0                            # pulley + KFL000 stub past the BK lock nut (assembly.py)
x_screw_need = (BK[1] + STUB_R) - (BF[0] - 5)

# ---- masses
sec_full = H * (D - PLATE)
cavity = (H - 2 * T_TB) * (D - PLATE - T_FRONT)
channel = CH_W * CH_D
m_chan = (sec_full - cavity - channel) * (LEN - 2 * END) * AL + 2 * sec_full * END * AL
m_plate = H * LEN * PLATE * AL
foot_solid = FOOT_L * FOOT_W * FOOT_T * AL
pockets = 2 * 60 * 100 * 25 * AL         # 2 pockets from the top, in front of the beam
m_foot = foot_solid - pockets
sketch_beam, sketch_feet = 12.5, 5.66
R = dict(beam_channel_kg=m_chan, back_plate_kg=m_plate, beam_total_kg=m_chan + m_plate, foot_kg_each=m_foot,
         moving_mass_change_kg=(m_chan + m_plate - sketch_beam) + (2 * m_foot - sketch_feet),
         x_axis_y=X_AXIS_Y, bk_base_y=BK_BASE_Y, housing_clear=CH_D - HOUSING_BACK_Y, flange_clear=CH_D - FLANGE_BACK_Y,
         block_reach=blk_reach, bk=BK, bf=BF, x_screw_need=x_screw_need, x_screw_buy=700)
(OUT / "gantry_parts_sketch.json").write_text(json.dumps(R, indent=1, default=float))

# ---- drawing
ALc, ALd, RL, SC, ST = "#9fb7cf", "#6f8fb0", "#333", "#b04a2f", "#888"
fig = plt.figure(figsize=(17, 11))
gs = fig.add_gridspec(2, 2, width_ratios=[1.6, 1], height_ratios=[1, 1.1])
a1, a2, a3 = fig.add_subplot(gs[0, :]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])

def rect(ax, x0, y0, x1, y1, fc, ec="k", lw=0.8, **k):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, ec=ec, lw=lw, **k))

def dim(ax, p0, p1, t, off=(0, 0), fs=8):
    ax.annotate("", p0, p1, arrowprops=dict(arrowstyle="<->", lw=0.7))
    ax.text((p0[0] + p1[0]) / 2 + off[0], (p0[1] + p1[1]) / 2 + off[1], t, ha="center", va="center", fontsize=fs,
            bbox=dict(fc="white", ec="none", pad=0.5))

def note(ax, x, y, t, fs=8, **k):
    ax.text(x, y, t, fontsize=fs, **k)

# 1. Front view (X-Z), looking at the rail face
L2 = LEN / 2
rect(a1, -L2, 0, L2, H, ALc)
rect(a1, -L2 + END, H / 2 - CH_W / 2, L2 - END, H / 2 + CH_W / 2, "#cbd8e6", lw=0.5)       # channel
for z in RAIL_Z:
    rect(a1, -300, z - 10, 300, z + 10, RL)
    for x in range(-280, 281, 60):
        a1.add_patch(Circle((x, z), 3, fc="w", ec="w", lw=0))
for xa, xb, n in ((BK[0], BK[0] + 25, "BK12"), (BF[0], BF[1], "BF12")):
    rect(a1, xa - 5, H / 2 - 32, xb + 5, H / 2 + 32, ALd, lw=0.5)
    rect(a1, xa, H / 2 - 30, xb, H / 2 + 30, ST)
    note(a1, (xa + xb) / 2, H / 2 + 36, n, fs=7, ha="center")
a1.plot([BF[0] - 5, BK[1] + STUB_R], [H / 2] * 2, color=SC, lw=2)
for s in (-1, 1):
    rect(a1, s * L2 - (END if s > 0 else 0), 0, s * L2 + (0 if s > 0 else END), H, ALd, alpha=0.6)
    rect(a1, s * WALL_IN, -FOOT_T, s * L2, 0, ALc)
    for k in range(4):
        a1.plot([s * 425] * 2, [-FOOT_T + 5, H], color="k", lw=0.6, ls="--")
    rect(a1, s * RAIL_X - BLK_W / 2, -FOOT_T - BLK_H, s * RAIL_X + BLK_W / 2, -FOOT_T, "#5a7fa8")
    rect(a1, s * Y_SCREW_X - 26, -FOOT_T - 25, s * Y_SCREW_X + 26, -FOOT_T + 15, "#ddd", lw=0.5)
rect(a1, -SADDLE_X - BLK_PITCH_X / 2 - BLK_L / 2, RAIL_Z[0] - 22, -SADDLE_X + BLK_PITCH_X / 2 + BLK_L / 2, RAIL_Z[1] + 22, "none", ec="b", ls="--")
rect(a1, SADDLE_X - BLK_PITCH_X / 2 - BLK_L / 2, RAIL_Z[0] - 22, SADDLE_X + BLK_PITCH_X / 2 + BLK_L / 2, RAIL_Z[1] + 22, "none", ec="b", ls="--")
note(a1, 0, H + 8, "X blocks at both ends of travel (blue dashed): they stop at ±289, so BK12 and BF12 sit just outside them", fs=8, ha="center", color="b")
note(a1, 0, H / 2 + 12, "X screw channel 80 wide x 20 deep, between the rails", fs=8, ha="center")
note(a1, L2 + 8, H - 40, "4 x M8 down\nthrough the\nsolid end block\ninto the foot\n(dashed)", fs=7, ha="left")
note(a1, Y_SCREW_X, -FOOT_T - 40, "Y nut housing\nin a 15 step", fs=7, ha="center", va="top")
dim(a1, (-L2, -95), (L2, -95), "890 (JLC limit 1100)")
dim(a1, (-300, RAIL_Z[1] + 45), (300, RAIL_Z[1] + 45), "X rails 2 x 600, M5 tapped at 60 (E 20)", fs=7)
dim(a1, (BF[0] - 5, H / 2 - 50), (BK[1] + STUB_R, H / 2 - 50), f"X screw needs {x_screw_need:.0f} (buying 700)", fs=7)
dim(a1, (L2 - END, H + 45), (L2, H + 45), "40", fs=7)
dim(a1, (-L2 - 25, 0), (-L2 - 25, H), "150", fs=7)
a1.set_title("Front view (rail face): beam G01 on foot blocks G03. Rails black, screw red", fontsize=10)
a1.set_aspect("equal"); a1.set_xlim(-L2 - 50, L2 + 110); a1.set_ylim(-125, H + 75); a1.axis("off")

# 2. Section at mid-span (Y-Z): the X screw stack
def beam_section(ax, x_end=False):
    if x_end:
        rect(ax, 0, 0, D - PLATE, H, ALd)
    else:
        rect(ax, 0, 0, D - PLATE, H, ALc)
        rect(ax, T_FRONT, T_TB, D - PLATE, H - T_TB, "w", lw=0.5)
        rect(ax, -0.01, H / 2 - CH_W / 2, CH_D, H / 2 + CH_W / 2, "w", lw=0.5)
    rect(ax, D - PLATE, 0, D, H, "#c5d4e3")
beam_section(a2)
for z in RAIL_Z:
    rect(a2, -17.5, z - 10, 0, z + 10, RL)
    rect(a2, -BLK_H, z - 22, -4.3, z + 22, "#5a7fa8")
    sh = z + 10 if z > H / 2 else z - 10 - 8
    rect(a2, 0, sh, SHOULDER, sh + 8, "none", ec="r", lw=0.8)
rect(a2, -BLK_H - 20, -60, -BLK_H, H + 60, ALc, alpha=0.5)
rect(a2, -BLK_H, H / 2 - 26, HOUSING_BACK_Y, H / 2 + 26, "#ddd")
a2.add_patch(Circle((X_AXIS_Y, H / 2), 24, fc="none", ec="k", ls=":", lw=0.8))
a2.add_patch(Circle((X_AXIS_Y, H / 2), 8, fc=SC, ec="k", lw=0.5))
rect(a2, BK_BASE_Y, H / 2 - 30, CH_D, H / 2 + 30, "none", ec=ST, ls="--")
note(a2, 34, H - 18, "cavity: empty now,\nfill later via ports (D-147)", fs=7)
note(a2, 105, -14, "G02 back plate 10:\nbonded (D-155) + M4", fs=7, ha="center", va="top")
note(a2, -45, H + 66, "saddle", fs=7, ha="center")
note(a2, -12, H / 2 + 40, "X nut housing\n(no spacer)", fs=7, ha="right")
note(a2, 3, RAIL_Z[1] + 22, "3 mm datum\nshoulder (red)", fs=7, color="r")
dim(a2, (0, -25), (T_FRONT, -25), "front wall 30", fs=7)
dim(a2, (-BLK_H, H + 25), (0, H + 25), "30", fs=7)
dim(a2, (0, H + 45), (D, H + 45), "130", fs=7)
note(a2, CH_D + 3, H / 2 - 4, f"channel floor:\nhousing clear {CH_D - HOUSING_BACK_Y:.0f},\nnut flange clear {CH_D - FLANGE_BACK_Y:.0f}", fs=7)
a2.set_title("Section at mid-span (Y-Z). Rails, X blocks, saddle on the left;\nBK12/BF12 (grey dashed) seat on 5 mm pads at the beam ends", fontsize=9)
a2.set_aspect("equal"); a2.set_xlim(-70, D + 20); a2.set_ylim(-60, H + 75); a2.axis("off")

# 3. End view at the foot (Y-Z through X = 425)
beam_section(a3, x_end=True)
y0, y1 = CAR_Y - FOOT_L / 2, CAR_Y + FOOT_L / 2
rect(a3, y0, -FOOT_T, y1, 0, ALc)
for yy in (-130, -60):
    rect(a3, yy, -25, yy + 50, 0, "w", lw=0.4, ls=":")
for yb in (CAR_Y - Y_PITCH / 2, CAR_Y + Y_PITCH / 2):
    rect(a3, yb - BLK_L / 2, -FOOT_T - BLK_H, yb + BLK_L / 2, -FOOT_T, "#5a7fa8")
    for d in (-18, 18):
        a3.plot([yb + d] * 2, [-FOOT_T, 0], color="k", lw=0.6)
rect(a3, y0 - 10, -FOOT_T - BLK_H - 17.5 + 4.3, y1 + 10, -FOOT_T - BLK_H + 4.3, RL)
rect(a3, CAR_Y - 20, -FOOT_T - 25, CAR_Y + 20, -FOOT_T + 15, "#ddd", lw=0.5)
for yy in (15, 40, 65, 90):
    a3.plot([yy] * 2, [-FOOT_T + 5, H], color="k", lw=0.6, ls="--")
a3.add_patch(Circle((-175, -FOOT_T - 40), 4, fc="k"))
note(a3, -175, -FOOT_T - 55, "spindle axis\n(Y position)", fs=7, ha="center", va="top")
note(a3, CAR_Y + Y_PITCH / 2, -FOOT_T - BLK_H - 30, "rear Y block: its 4 M5 bolts\nare under the beam, so the\nfeet go on before the beam", fs=7, ha="center", va="top")
note(a3, 60, H / 2, "solid\nend block", fs=7, ha="center")
note(a3, -120, 5, "pockets", fs=7)
dim(a3, (y0, -FOOT_T - 95), (y1, -FOOT_T - 95), "foot 268 (G03), 140 wide, 40 thick", fs=7)
a3.set_title("End view at the foot (Y-Z). Beam bolts dashed (4 x M8)", fontsize=9)
a3.set_aspect("equal"); a3.set_xlim(y0 - 30, D + 20); a3.set_ylim(-FOOT_T - 130, H + 20); a3.axis("off")

fig.suptitle(f"Type 0 gantry, task 22 step 4: PROPOSAL before the JLC STEP. Beam {m_chan + m_plate:.1f} kg (plate {m_plate:.1f}), feet {m_foot:.1f} kg each", fontsize=13)
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig(OUT / "gantry_parts_sketch.png", dpi=110)
print(json.dumps(R, indent=1, default=float))

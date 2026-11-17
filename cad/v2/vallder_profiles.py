"""Vallder X-axis extrusions vs the JLC step-4 beam (task 22, docs/beam-extrusion-check.md).

Reads the owner's Vallder DXF sections in cad/vendor/ and computes area, mass per metre,
second moments and a Bredt twist estimate, with the same load model as beam_options.py
(span 690, 200 N at mid-span, tool 245 below the beam centre).
The JLC step-4 beam (gantry_parts_sketch.py: 150 x 130, front wall 30 with an 80 x 20
channel, 10 walls, 10 back plate taken as fully bonded) goes through the same polygon routine.

Run: PYTHONUTF8=1 python cad/v2/vallder_profiles.py
  -> cad/v2/out/vallder_profiles.json, cad/v2/out/vallder_profiles.png
Axes: DXF x = depth (the rail face is at min x), DXF y = height. Force in Y (cutting, normal
to the rail face) bends about the DXF y axis.
"""
import json
import pathlib

import ezdxf
from ezdxf import path as ep
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = pathlib.Path(__file__).parent
VENDOR = HERE.parent / "vendor"
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)

E_AL, G_AL, RHO = 69e3, 26e3, 2.70e-6
E_EG, RHO_EG = 25e3, 2.30e-6
SPAN, LEN, F, ARM = 690.0, 890.0, 200.0, 245.0


def props(pts):
    """Signed area, first and second moments of a closed polygon about the origin."""
    a = sx = sy = ixx = iyy = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]; x1, y1 = pts[(i + 1) % len(pts)]
        c = x0 * y1 - x1 * y0
        a += c; sx += (x0 + x1) * c; sy += (y0 + y1) * c
        ixx += (y0 * y0 + y0 * y1 + y1 * y1) * c; iyy += (x0 * x0 + x0 * x1 + x1 * x1) * c
    return [a / 2, sx / 6, sy / 6, ixx / 12, iyy / 12]


def section(loops):
    """loops[0] = outer, the rest holes. Returns area, centroid, I_y (force in Y), I_z, hole area."""
    tot = [0.0] * 5; holes = 0.0
    for k, pts in enumerate(loops):
        p = props(pts); s = 1 if p[0] > 0 else -1
        p = [s * v for v in p]
        if k == 0:
            tot = [t + v for t, v in zip(tot, p)]
        else:
            tot = [t - v for t, v in zip(tot, p)]; holes += p[0]
    a, sx, sy, ixx, iyy = tot
    cx, cy = sx / a, sy / a
    return dict(area=a, cx=cx, cy=cy, I_forceY=iyy - a * cx * cx, I_forceZ=ixx - a * cy * cy, holes=holes)


def dxf_loops(p):
    loops = []
    for e in ezdxf.readfile(p).modelspace():
        pts = [(v.x, v.y) for v in ep.make_path(e).flattening(0.005)]
        if pts[0] == pts[-1]:
            pts = pts[:-1]
        loops.append(pts)
    loops.sort(key=lambda q: -abs(props(q)[0]))
    return loops


def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def defl(ei):
    return F * SPAN**3 / (48 * ei) * 1e3                       # um, simply supported


def twist(gj):                                                 # same as beam_options.py
    return (F * ARM / 2) * (SPAN / 2) / gj * ARM * 1e3


def bredt(am, s_over_t):
    return 4 * am**2 / s_over_t


# ---- Bredt inputs: mid-line of the closed cell block behind the open screw channel.
# Wall thicknesses read off the DXF loops (outer vs nearest inner loop); internal webs ignored.
# Rough estimates: the cell block has chamfered rear corners and thin webs.
BREDT = {
    # heavy 235 x 125: cell block about 230 x 78 mid-line, minus the two rear chamfers; walls 4.0 front, 3.5-4.5 rear, ~4.8 top/bottom
    "heavy": dict(am=15000.0, s_over_t=590 / 4.0),
    # 200 x 96: cell block about 196 x 50 mid-line; walls 2.0 front, 2.5 rear
    "200x96": dict(am=7900.0, s_over_t=492 / 2.3),
    # JLC step 4: mid-line 105 deep x 140 tall; top/bottom 10, back 10, front 10 at the channel (80) and 30 beside it (60)
    "jlc": dict(am=105 * 140.0, s_over_t=2 * 105 / 10 + 140 / 10 + 80 / 10 + 60 / 30),
}

profiles = {
    "Vallder 200 x 96": dict(file="vallder_200x96.dxf", key="200x96", stated_kg_m=8.20, eur_m=94.00),
    "Vallder heavy 235 x 125": dict(file="vallder_heavy_235x125.dxf", key="heavy", stated_kg_m=14.80, eur_m=137.00),
}

res = {}
loops_by = {}
for name, d in profiles.items():
    lp = dxf_loops(VENDOR / d["file"])
    loops_by[name] = lp
    s = section(lp)
    xs = [q[0] for q in lp[0]]; ys = [q[1] for q in lp[0]]
    b = BREDT[d["key"]]
    gj = G_AL * bredt(b["am"], b["s_over_t"])
    res[name] = dict(outer_mm=[round(max(ys) - min(ys), 1), round(max(xs) - min(xs), 1)],
                     area_mm2=round(s["area"]), kg_per_m=round(s["area"] * RHO * 1e3, 2),
                     stated_kg_per_m=d["stated_kg_m"], beam_890_kg=round(s["area"] * RHO * LEN, 1),
                     EI_Y=round(E_AL * s["I_forceY"] / 1e12, 3), EI_Z=round(E_AL * s["I_forceZ"] / 1e12, 3),
                     defl_Y_um=round(defl(E_AL * s["I_forceY"]), 1), defl_Z_um=round(defl(E_AL * s["I_forceZ"]), 1),
                     twist_um_est=round(twist(gj), 1),
                     centroid_from_rail_face_mm=round(s["cx"] - min(xs), 1),
                     cells_mm2=round(s["holes"]), eg_fill_kg=round(s["holes"] * LEN * RHO_EG, 1))

# JLC step-4 beam, same routine
H, D, TF, TW, CW, CD = 150.0, 130.0, 30.0, 10.0, 80.0, 20.0
# outer drawn as a polygon with the channel notched into the front face (x = 0 is the rail face)
outer = [(CD, -CW / 2), (0, -CW / 2), (0, -H / 2), (D, -H / 2), (D, H / 2), (0, H / 2), (0, CW / 2), (CD, CW / 2)]
cavity = rect(TF, -H / 2 + TW, D - TW, H / 2 - TW)
s = section([outer, cavity])
b = BREDT["jlc"]
res["JLC step 4 (150 x 130, 30 front wall, 80 x 20 channel)"] = dict(
    outer_mm=[H, D], area_mm2=round(s["area"]), kg_per_m=round(s["area"] * RHO * 1e3, 2),
    beam_890_kg=round(s["area"] * RHO * LEN, 1), note_mass="mid-section only; with the 40 mm solid ends 17.8 kg",
    EI_Y=round(E_AL * s["I_forceY"] / 1e12, 3), EI_Z=round(E_AL * s["I_forceZ"] / 1e12, 3),
    defl_Y_um=round(defl(E_AL * s["I_forceY"]), 1), defl_Z_um=round(defl(E_AL * s["I_forceZ"]), 1),
    twist_um_est=round(twist(G_AL * bredt(b["am"], b["s_over_t"])), 1),
    centroid_from_rail_face_mm=round(s["cx"], 1))
loops_by["JLC step 4"] = [outer, cavity]

# ---- heavy profile: rail grooves, saddle face, X screw position (from the DXF outer loop)
# Rail groove floors 26.0 behind the outer lips (23.0 behind the channel fingers), grooves about 21 wide, rail centres +-77.5
# from the profile centre (155 apart). HGR20 rail 17.5 + HGH20CA to the block top = 30 above the seat.
LIP_TO_SEAT = 26.0; BLOCK_H = 30.0; CH_FLOOR = 43.6; FLOOR_T = 4.0
saddle_back = BLOCK_H - LIP_TO_SEAT                     # block top this far in front of the lips
axis = -saddle_back + 20.0                              # DSG16H axis 20 behind the saddle back (from the lips)
res["heavy_layout"] = dict(
    rails_apart_mm=155, block_outer_edges_mm=155 + 44, saddle_height_mm=400,
    block_top_proud_of_lips_mm=saddle_back,
    screw_axis_behind_lips_mm=axis, channel_floor_behind_lips_mm=CH_FLOOR,
    housing_back_clear_of_floor_mm=round(CH_FLOOR - (-saddle_back + 40.0), 1),
    bk12_base_vs_floor_mm=round(CH_FLOOR - (axis + 25.0), 1),
    channel_floor_thickness_mm=FLOOR_T, channel_opening_mm=76,
    saddle_back_to_centroid_mm=round(saddle_back + res["Vallder heavy 235 x 125"]["centroid_from_rail_face_mm"], 1),
    jlc_saddle_back_to_centroid_mm=round(BLOCK_H + res["JLC step 4 (150 x 130, 30 front wall, 80 x 20 channel)"]["centroid_from_rail_face_mm"], 1))

(OUT / "vallder_profiles.json").write_text(json.dumps(res, indent=1))
for k, v in res.items():
    print(k, v)

# ---- picture: the three sections at the same scale, rail face on the left
fig, axs = plt.subplots(1, 3, figsize=(13, 6.5))
for ax, (name, lp) in zip(axs, loops_by.items()):
    x0 = min(q[0] for q in lp[0]); yc = (min(q[1] for q in lp[0]) + max(q[1] for q in lp[0])) / 2
    for k, pts in enumerate(lp):
        xs = [q[0] - x0 for q in pts] + [pts[0][0] - x0]; ys = [q[1] - yc for q in pts] + [pts[0][1] - yc]
        ax.fill(xs, ys, fc="#bcd" if k == 0 else "white", ec="k", lw=0.6)
    r = [v for k, v in res.items() if k.startswith(name.split(" (")[0])][0]
    ax.set_title(f"{name}\nEI Y {r['EI_Y']} / Z {r['EI_Z']} MNm², twist ≈ {r['twist_um_est']} µm\n{r['beam_890_kg']} kg per 890",
                 fontsize=9)
    ax.set_aspect("equal"); ax.set_xlim(-10, 140); ax.set_ylim(-125, 125); ax.grid(lw=0.3)
    ax.set_xlabel("depth from the rail face (mm)")
fig.suptitle("Beam sections at the same scale (rail face on the left; force in Y pushes left-right)", fontsize=10)
fig.tight_layout()
fig.savefig(OUT / "vallder_profiles.png", dpi=110)

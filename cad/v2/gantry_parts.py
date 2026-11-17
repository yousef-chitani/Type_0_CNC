"""Task 22 step 4: basic STEP models of the JLC gantry parts, for a price quote only.

G01 beam (U channel, open at the back), G02 back plate, G03 foot block (x 2), all 6061.
Geometry is the step-4 proposal (docs/task22-step4.md, gantry_parts_sketch.py) with the
owner's 7 questions NOT yet answered: it is a "very basic" model for pricing (owner, 17 Nov 2026).
Holes are plain at tap-drill size (no threads in STEP). No datum shoulder, no BK/BF pads,
no Y nut step under the feet: those come with the final model.

Run: PYTHONUTF8=1 python cad/v2/gantry_parts.py -> cad/v2/out/jlc/G01_beam.step, G02_back_plate.step,
G03_foot_block.step, gantry_parts.json (re-import check: one solid, size, mass).
Axes: X along the beam, Y depth (front face Y 0), Z up.
"""
import json
import pathlib

import cadquery as cq

OUT = pathlib.Path(__file__).parent / "out" / "jlc"; OUT.mkdir(parents=True, exist_ok=True)
RHO = 2.70e-6                                   # 6061, kg/mm3

LEN, H, D, PLATE = 890.0, 150.0, 130.0, 10.0
DC = D - PLATE                                  # channel part depth, 120
T_TB, T_FRONT, END = 10.0, 30.0, 40.0
CH_W, CH_D = 80.0, 20.0
RAIL_Z = (H / 2 - 50, H / 2 + 50)               # D-104: 100 apart
TAP_M5, TAP_M8, CLR_M8, CLR_M5, TAP_M4 = 4.2, 6.8, 9.0, 5.5, 3.3


def box(x0, x1, y0, y1, z0, z1):
    return cq.Workplane("XY").box(x1 - x0, y1 - y0, z1 - z0, centered=False).translate((x0, y0, z0))


def holes_y(wp_solid, pts, dia, depth, y_face, direction=1):
    """Holes drilled from a face normal to Y (direction +1 = into +Y)."""
    for x, z in pts:
        c = cq.Workplane("XZ").circle(dia / 2).extrude(-depth * direction).translate((x, y_face, z))
        wp_solid = wp_solid.cut(c)
    return wp_solid


def holes_z(wp_solid, pts, dia, z0, z1):
    for x, y in pts:
        wp_solid = wp_solid.cut(cq.Workplane("XY").circle(dia / 2).extrude(z1 - z0).translate((x, y, z0)))
    return wp_solid


# ---- G01 beam
g01 = box(0, LEN, 0, DC, 0, H)
g01 = g01.cut(box(END, LEN - END, T_FRONT, DC + 1, T_TB, H - T_TB))            # cavity, open at the back
g01 = g01.cut(box(-1, LEN + 1, -1, CH_D, H / 2 - CH_W / 2, H / 2 + CH_W / 2))    # X screw channel
rail_x = [LEN / 2 - 270 + 60 * i for i in range(10)]                           # 600 rail, E 20, P 60
g01 = holes_y(g01, [(x, z) for x in rail_x for z in RAIL_Z], TAP_M5, 14, 0)     # M5 x 14 deep
g01 = holes_z(g01, [(x, y) for x in (11.0, 29.0, LEN - 29.0, LEN - 11.0) for y in (30.0, 90.0)], CLR_M8, -1, H + 1)
plate_x = [20 + 75 * i for i in range(12)]                                     # M4 for G02, top and bottom walls
g01 = holes_y(g01, [(x, z) for x in plate_x for z in (T_TB / 2, H - T_TB / 2)], TAP_M4, 12, DC, -1)

# ---- G02 back plate (Y DC..D)
g02 = box(0, LEN, DC, D, 0, H)
for x in (LEN / 4, LEN / 2, 3 * LEN / 4):                                      # 3 fill ports
    g02 = g02.cut(cq.Workplane("XZ").circle(12.5).extrude(-PLATE - 2).translate((x, DC - 1, H / 2)))
g02 = holes_y(g02, [(x, z) for x in plate_x for z in (T_TB / 2, H - T_TB / 2)], 4.5, PLATE + 2, DC - 1, 1)

# ---- G03 foot block: 268 along Y, 140 along X, 40 thick
FL, FW, FT = 268.0, 140.0, 40.0
g03 = box(0, FW, 0, FL, 0, FT)
# 2 pockets 40 x 100 x 25 from the top, in front of the beam, clear of the Y block holes
for (x0, x1) in ((5.0, 45.0), (95.0, 135.0)):
    g03 = g03.cut(box(x0, x1, 10.0, 110.0, FT - 25, FT + 1))
by = FL - D - 4                                                                # beam footprint starts here
# beam end flush with the foot's outer edge (X 100..140 here): 4 x M8 tapped 20 deep
g03 = holes_z(g03, [(FW - END + x, by + y) for x in (11.0, 29.0) for y in (30.0, 90.0)], TAP_M8, FT - 20, FT + 1)
blk = [(FW / 2 + dx, FL / 2 + yc + dy) for yc in (-75.0, 75.0) for dx in (-16, 16) for dy in (-18, 18)]
g03 = holes_z(g03, blk, CLR_M5, -1, FT + 1)                                    # 2 x HGH20CA, 32 x 36

res = {}
for name, wp, qty in (("G01_beam", g01, 1), ("G02_back_plate", g02, 1), ("G03_foot_block", g03, 2)):
    p = OUT / f"{name}.step"
    cq.exporters.export(wp, str(p))
    back = cq.importers.importStep(str(p))
    solids = back.solids().vals()
    bb = back.val().BoundingBox()
    res[name] = dict(qty=qty, solids=len(solids), size_mm=[round(bb.xlen, 1), round(bb.ylen, 1), round(bb.zlen, 1)],
                     mass_kg=round(back.val().Volume() * RHO, 2), file=f"cad/v2/out/jlc/{name}.step")
(OUT / "gantry_parts.json").write_text(json.dumps(res, indent=1))
for k, v in res.items():
    print(k, v)

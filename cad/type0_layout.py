"""Type 0 CNC: parametric layout (CadQuery).

Run:  python cad/type0_layout.py
Writes cad/out/type0.step, cad/out/view_*.svg and cad/out/dimensions.md.

Coordinates: X left(-)/right(+), Y front(-)/back(+), Z up.
Origin: base top surface, on the spindle axis (Y = 0 is the spindle line).
Component sizes marked VERIFY are typical catalogue values: check them
against the parts you buy.
"""
import json, math, pathlib
import cadquery as cq

OUT = pathlib.Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

P = dict(
    # requirements (requirements.md, D-09, D-51)
    travel_x=250, travel_y_work=250, travel_z=150,
    vise_height=100, clearance_nose_to_table=200,
    table_top_above_floor=950,                      # D-49
    # table (D-23)
    table_x=330, table_y=330, table_t=30,
    # HGR20 / HGH20CA (VERIFY)
    rail_w=20, rail_h=17.5, block_assy_h=30, block_w=44, block_l=77.5,
    y_rail_spacing=220, y_block_pitch=150,           # D-20
    x_rail_spacing=150, x_block_pitch=120,           # D-21
    z_rail_spacing=100, z_block_pitch=100,
    # ballscrew SFU/DFU1605 + BK12/BF12 (VERIFY)
    nut_len=90, end_supports_len=45, screw_margin=20,
    # spindle JGL-80 (S01, VERIFY: body 80 mm, length about 300 incl. cylinder)
    spindle_d=80, spindle_len=300,
    # tool rack (D-17): 2 rows x 4 pockets
    pocket_pitch_x=60, row_pitch_y=60, fork_half_depth=35, rack_clear=10,
    tool_below_fork=90, holder_above_fork=40,
    # structure (draft, eg-moulds.md)
    base_x=660, base_h=180, wall=60,
    upright_w=120, gantry_depth=160, beam_h=200,
    beam_front_offset=160,     # spindle axis to beam front face (spindle r + Z/X stack)
    stand_tube=60, stand_tube_t=3, stand_low_ring=150, feet_h=30,   # D-54: 60x60x3 + bracing
    eg_density=2300,
)

def derive(p):
    d = {}
    # Table: Y-position of table centre t. Work: t in [-w/2, +w/2].
    t_work_max = p["travel_y_work"] / 2
    # Tool change: back row centre at Y=0, so front row front edge at
    # -(row_pitch + fork_half_depth). Table back edge must be in front of it.
    front_row_front_edge = -(p["row_pitch_y"] + p["fork_half_depth"])
    t_tc = front_row_front_edge - p["rack_clear"] - p["table_y"] / 2
    d["t_min"], d["t_max"] = t_tc, t_work_max
    d["travel_y_total"] = t_work_max - t_tc
    d["y_overtravel_for_tc"] = d["travel_y_total"] - p["travel_y_work"]
    # Heights above base top
    d["table_top_z"] = p["block_assy_h"] + p["table_t"]
    d["nose_z_top"] = d["table_top_z"] + p["clearance_nose_to_table"]
    d["nose_z_bottom"] = d["nose_z_top"] - p["travel_z"]
    d["fork_z"] = p["block_assy_h"] + p["tool_below_fork"] + 20
    d["beam_bottom_z"] = d["table_top_z"] + p["vise_height"] + 100
    d["beam_top_z"] = d["beam_bottom_z"] + p["beam_h"]
    # Rails and screws
    d["rail_y_len"] = d["travel_y_total"] + p["y_block_pitch"] + p["block_l"]
    d["rail_x_len"] = p["travel_x"] + p["x_block_pitch"] + p["block_l"]
    d["rail_z_len"] = p["travel_z"] + p["z_block_pitch"] + p["block_l"]
    extra = p["nut_len"] + p["end_supports_len"] + p["screw_margin"]
    d["screw_y_len"] = d["travel_y_total"] + extra
    d["screw_x_len"] = p["travel_x"] + extra
    d["screw_z_len"] = p["travel_z"] + extra
    # Gantry
    d["opening_w"] = p["table_x"] + 2 * 35
    d["gantry_w"] = d["opening_w"] + 2 * p["upright_w"]
    d["gantry_y0"] = p["beam_front_offset"]
    d["gantry_y1"] = d["gantry_y0"] + p["gantry_depth"]
    # Rack: parked behind the table's rearmost back edge
    table_back_max = t_work_max + p["table_y"] / 2
    d["rack_front_parked"] = table_back_max + p["rack_clear"]
    rack_depth = p["row_pitch_y"] + 2 * p["fork_half_depth"]
    d["rack_back_parked"] = d["rack_front_parked"] + rack_depth
    d["rack_stroke"] = (d["rack_front_parked"] + p["fork_half_depth"] + p["row_pitch_y"])
    d["rack_rail_len"] = d["rack_stroke"] + 150
    d["rack_screw_len"] = d["rack_stroke"] + 100
    d["rack_rail_x"] = (p["table_x"] / 2 + d["opening_w"] / 2) / 2
    # Base extents in Y
    table_front_min = t_tc - p["table_y"] / 2
    d["base_y0"] = round(table_front_min - 40, -1)          # BK12 + motor bracket land
    d["base_y1"] = round(max(d["rack_back_parked"] + 60, d["gantry_y1"] + 40), -1)
    d["base_len"] = d["base_y1"] - d["base_y0"]
    # Masses (solid EG, D-30)
    base_vol = p["base_x"] * d["base_len"] * p["base_h"] * 1e-9
    opening_vol = d["opening_w"] * p["gantry_depth"] * d["beam_bottom_z"] * 1e-9
    gantry_vol = d["gantry_w"] * p["gantry_depth"] * d["beam_top_z"] * 1e-9 - opening_vol
    d["base_kg"] = base_vol * p["eg_density"]
    d["gantry_kg"] = gantry_vol * p["eg_density"]
    d["epoxy_kg_11pct"] = 0.11 * (d["base_kg"] + d["gantry_kg"])
    d["aggregate_kg"] = 0.89 * (d["base_kg"] + d["gantry_kg"])
    # Stand (D-49): top of stand = underside of base
    d["base_top_above_floor"] = p["table_top_above_floor"] - d["table_top_z"]
    d["stand_top_above_floor"] = d["base_top_above_floor"] - p["base_h"]
    sx, sy = p["base_x"] + 40, d["base_len"] + 40
    leg = d["stand_top_above_floor"] - p["feet_h"] - p["stand_tube"]
    ring = 2 * sx + 2 * (sy - 2 * p["stand_tube"])
    d["stand_xy"] = (sx, sy)
    d["stand_cut"] = {"top ring": ring, "lower ring": ring, "legs (4)": 4 * leg,
                      "diagonal braces: 2 sides + rear (est.)": 2 * math.hypot(sy - 2 * p["stand_tube"], leg) + math.hypot(sx - 2 * p["stand_tube"], leg)}
    d["cabinet_clear_h"] = d["stand_top_above_floor"] - p["stand_tube"] - (p["stand_low_ring"] + p["stand_tube"])
    d["stand_steel_m"] = sum(d["stand_cut"].values()) / 1000
    return d

D = derive(P)

def box(x0, x1, y0, y1, z0, z1):
    return cq.Workplane("XY").box(x1 - x0, y1 - y0, z1 - z0, centered=False).translate((x0, y0, z0))

def build(t=None, x=0.0, znose=None, rack_pos=0.0):
    p, d = P, D
    t = D["t_max"] if t is None else t
    znose = d["nose_z_top"] if znose is None else znose
    parts = {}
    parts["base"] = box(-p["base_x"]/2, p["base_x"]/2, d["base_y0"], d["base_y1"], -p["base_h"], 0)
    g = box(-d["gantry_w"]/2, d["gantry_w"]/2, d["gantry_y0"], d["gantry_y1"], 0, d["beam_top_z"])
    g = g.cut(box(-d["opening_w"]/2, d["opening_w"]/2, d["gantry_y0"]-1, d["gantry_y1"]+1, -1, d["beam_bottom_z"]))
    parts["gantry"] = g
    ry0 = t - p["y_block_pitch"]/2 - p["block_l"]/2  # rails centred on table travel
    ymid = (d["t_min"] + d["t_max"]) / 2
    for s in (-1, 1):
        cx = s * p["y_rail_spacing"]/2
        parts[f"y_rail_{s}"] = box(cx-p["rail_w"]/2, cx+p["rail_w"]/2, ymid-d["rail_y_len"]/2, ymid+d["rail_y_len"]/2, 0, p["rail_h"])
    parts["table"] = box(-p["table_x"]/2, p["table_x"]/2, t-p["table_y"]/2, t+p["table_y"]/2, p["block_assy_h"], d["table_top_z"])
    # X rails on beam front face
    fy = d["gantry_y0"]
    zc = (d["beam_bottom_z"] + d["beam_top_z"]) / 2
    for s in (-1, 1):
        z = zc + s * p["x_rail_spacing"]/2
        parts[f"x_rail_{s}"] = box(-d["rail_x_len"]/2, d["rail_x_len"]/2, fy-p["rail_h"], fy, z-p["rail_w"]/2, z+p["rail_w"]/2)
    saddle_y1 = fy - p["block_assy_h"]
    parts["saddle"] = box(x-100, x+100, saddle_y1-20, saddle_y1, zc-115, zc+115)
    zp_y1 = saddle_y1 - 20 - p["block_assy_h"]
    zp_y0 = zp_y1 - 20
    parts["z_plate"] = box(x-80, x+80, zp_y0, zp_y1, znose+40, znose+40+d["rail_z_len"])
    parts["spindle"] = (cq.Workplane("XY").circle(p["spindle_d"]/2).extrude(p["spindle_len"])
                        .translate((x, 0, znose)))
    # Tool rack (parked) + carrier rails
    rf = d["rack_front_parked"] - rack_pos
    rack = box(-130, 130, rf, rf + p["row_pitch_y"] + 2*p["fork_half_depth"], d["fork_z"]-10, d["fork_z"])
    for row in (0, 1):
        for i in range(4):
            px = -1.5*p["pocket_pitch_x"] + i*p["pocket_pitch_x"]
            py = rf + p["fork_half_depth"] + row*p["row_pitch_y"]
            rack = rack.union(cq.Workplane("XY").circle(16).extrude(p["holder_above_fork"]+p["tool_below_fork"])
                              .translate((px, py, d["fork_z"]-p["tool_below_fork"])))
    parts["rack"] = rack
    for s in (-1, 1):
        cx = s * d["rack_rail_x"]
        parts[f"rack_rail_{s}"] = box(cx-7.5, cx+7.5, d["base_y1"]-d["rack_rail_len"]-20, d["base_y1"]-20, 0, 12.5)
    # Stand
    sx, sy = d["stand_xy"]; st = p["stand_tube"]
    z_top = -p["base_h"]; z_floor = z_top - d["stand_top_above_floor"]
    yc = (d["base_y0"] + d["base_y1"]) / 2
    stand = None
    for zz in (z_top - st, z_floor + p["stand_low_ring"]):
        ring = box(-sx/2, sx/2, yc-sy/2, yc+sy/2, zz, zz+st).cut(box(-sx/2+st, sx/2-st, yc-sy/2+st, yc+sy/2-st, zz-1, zz+st+1))
        stand = ring if stand is None else stand.union(ring)
    for ix in (-1, 1):
        for iy in (-1, 1):
            lx, ly = ix*(sx/2-st/2), yc+iy*(sy/2-st/2)
            stand = stand.union(box(lx-st/2, lx+st/2, ly-st/2, ly+st/2, z_floor+p["feet_h"], z_top-st))
    parts["stand"] = stand
    return parts

def export():
    parts = build()
    asm = cq.Assembly()
    for k, v in parts.items():
        asm.add(v, name=k)
    asm.save(str(OUT / "type0.step"))
    comp = None
    for k, v in parts.items():
        comp = v if comp is None else comp.union(v)
    opts = dict(width=900, height=650, marginLeft=40, marginTop=40, showAxes=False,
                strokeWidth=0.6, showHidden=False)
    views = {"front": (0, -1, 0), "side": (1, 0, 0), "top": (0, 0, 1), "iso": (1, -1.2, 0.8)}
    for name, dirv in views.items():
        cq.exporters.export(comp, str(OUT / f"view_{name}.svg"), opt=dict(opts, projectionDir=dirv))
    # tool-change pose
    tc = build(t=D["t_min"], x=-90, znose=D["fork_z"]+10, rack_pos=D["rack_stroke"])
    comp2 = None
    for v in tc.values():
        comp2 = v if comp2 is None else comp2.union(v)
    cq.exporters.export(comp2, str(OUT / "view_side_toolchange.svg"), opt=dict(opts, projectionDir=(1, 0, 0)))

def report():
    p, d = P, D
    r = lambda v: f"{v:,.0f}"
    lines = ["# Type 0 layout: key dimensions (generated)", "",
             "Generated by `cad/type0_layout.py`. Edit the parameters there and rerun. Sizes marked VERIFY in the script are catalogue assumptions.", "",
             "## Travel", "| | mm |", "|---|---|",
             f"| X travel | {r(p['travel_x'])} |",
             f"| Y travel, work | {r(p['travel_y_work'])} |",
             f"| Y overtravel for tool change | {r(d['y_overtravel_for_tc'])} |",
             f"| **Y travel, total** | **{r(d['travel_y_total'])}** |",
             f"| Z travel | {r(p['travel_z'])} |", "",
             "## Heights above base top", "| | mm |", "|---|---|",
             f"| Table top | {r(d['table_top_z'])} |",
             f"| Spindle nose, top / bottom | {r(d['nose_z_top'])} / {r(d['nose_z_bottom'])} |",
             f"| Rack fork plane | {r(d['fork_z'])} |",
             f"| Gantry opening (beam underside) | {r(d['beam_bottom_z'])} |",
             f"| Beam top | {r(d['beam_top_z'])} |", "",
             "## Castings (solid EG)", "| | Size (mm) | Mass |", "|---|---|---|",
             f"| Base | {r(p['base_x'])} W x {r(d['base_len'])} L x {r(p['base_h'])} H | {r(d['base_kg'])} kg |",
             f"| Gantry | {r(d['gantry_w'])} W x {r(p['gantry_depth'])} D x {r(d['beam_top_z'])} H, opening {r(d['opening_w'])} x {r(d['beam_bottom_z'])} | {r(d['gantry_kg'])} kg |",
             f"| Epoxy at 11% | | {r(d['epoxy_kg_11pct'])} kg |",
             f"| Aggregate at 89% | | {r(d['aggregate_kg'])} kg |", "",
             "## Rails and screws (minimum lengths)", "| Axis | Rail | Ballscrew |", "|---|---|---|",
             f"| X | 2 x {r(d['rail_x_len'])} | {r(d['screw_x_len'])} |",
             f"| Y | 2 x {r(d['rail_y_len'])} | {r(d['screw_y_len'])} |",
             f"| Z | 2 x {r(d['rail_z_len'])} | {r(d['screw_z_len'])} |",
             f"| Rack slide | 2 x {r(d['rack_rail_len'])} (MGN15) | {r(d['rack_screw_len'])} (SFU1204), stroke {r(d['rack_stroke'])} |", "",
             "## Stand", "| | |", "|---|---|",
             f"| Base top above floor | {r(d['base_top_above_floor'])} mm |",
             f"| Stand top above floor | {r(d['stand_top_above_floor'])} mm |",
             f"| Footprint | {r(d['stand_xy'][0])} x {r(d['stand_xy'][1])} mm |"]
    for k, v in d["stand_cut"].items():
        lines.append(f"| {k} | {r(v)} mm |")
    lines.append(f"| **60x60x3 total** | **{d['stand_steel_m']:.1f} m** |")
    lines.append(f"| Clear height between rings (cabinet) | {r(d['cabinet_clear_h'])} mm |")
    (OUT / "dimensions.md").write_text("\n".join(lines) + "\n")
    (OUT / "dimensions.json").write_text(json.dumps({k: v for k, v in d.items()}, indent=1, default=str))

if __name__ == "__main__":
    report()
    export()
    print((OUT / "dimensions.md").read_text())

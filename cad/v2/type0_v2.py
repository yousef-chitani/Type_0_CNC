"""Type 0 v2 (flat-sized, D-71/D-73): parametric layout.

Run: python cad/v2/type0_v2.py  -> cad/v2/out/type0_v2.step, dimensions_v2.md, dimensions_v2.json
X right, Y back (Y=0 spindle line), Z up from the TOP of the spine/foot castings.
Sizes marked VERIFY are catalogue assumptions.
"""
import json, math, pathlib
import cadquery as cq
OUT = pathlib.Path(__file__).parent / "out"; OUT.mkdir(exist_ok=True)

P = dict(
    travel_x_work=400, travel_y=250, travel_z=150, vise=100, nose_clear=180,   # D-79: work area 400 x 250
    table_x=460, table_y=330, table_t=25,
    rail_w=20, rail_h=17.5, block_h=30, block_l=77.5,          # HGR20/HGH20CA VERIFY
    y_rail_spacing=280, y_block_pitch=150, x_rail_spacing=80, x_block_pitch=100,   # D-80
    z_rail_spacing=80, z_block_pitch=90, saddle_w=180,
    nut_len=90, ends_len=45, screw_margin=20,                  # DFU1605 + BK/BF12 VERIFY
    spindle_d=80, spindle_len=213,                             # ER20 80x213 (ATC about 300)
    h=110, spine_w=320, upright_w=70, portal_d=130, beam_h=130, beam_front=110,
    leg_clear=20, foot_back_bar=60, opening_h=225,
    wheel_pockets=8, pocket_pitch=70, wheel_gap=20, wheel_t=60,
    bench_top_to_table=None, table_top_above_floor=950,
    eg_density=2300, pvc_core_d=50, pvc_cores=2,
)

def derive(p):
    d = {}
    d["table_top_z"] = p["block_h"] + p["table_t"]
    d["nose_top"] = d["table_top_z"] + p["nose_clear"]
    d["nose_bottom"] = d["nose_top"] - p["travel_z"]
    d["open_x0"], d["open_x1"] = -p["table_x"]/2 - p["leg_clear"], p["table_x"]/2 + p["leg_clear"]
    d["leg_r_x1"] = d["open_x1"] + p["upright_w"]; d["portal_x0"] = d["open_x0"] - p["upright_w"]
    d["wheel_d"] = p["wheel_pockets"] * p["pocket_pitch"] / math.pi
    d["pickup_x"] = d["leg_r_x1"] + p["wheel_gap"] + p["wheel_t"]/2
    d["portal_x1"] = d["pickup_x"] + p["saddle_w"]/2 + 20
    d["portal_w"] = d["portal_x1"] - d["portal_x0"]
    d["beam_bottom"] = p["opening_h"]; d["beam_top"] = p["opening_h"] + p["beam_h"]
    d["fork_z"] = d["table_top_z"] + 40
    d["x_min"], d["x_max"] = -p["travel_x_work"]/2, d["pickup_x"]
    d["travel_x"] = d["x_max"] - d["x_min"]
    ext = p["nut_len"] + p["ends_len"] + p["screw_margin"]
    d["rail_x"] = d["travel_x"] + p["x_block_pitch"] + p["block_l"]
    d["rail_y"] = p["travel_y"] + p["y_block_pitch"] + p["block_l"]
    d["rail_z"] = p["travel_z"] + p["z_block_pitch"] + p["block_l"]
    d["screw_x"], d["screw_y"], d["screw_z"] = d["travel_x"] + ext, p["travel_y"] + ext, p["travel_z"] + ext
    d["spine_y0"] = -p["travel_y"]/2 - p["table_y"]/2 - 50
    d["portal_y0"], d["portal_y1"] = p["beam_front"], p["beam_front"] + p["portal_d"]
    d["spine_y1"] = d["portal_y1"] + 20
    d["foot_y0"], d["foot_y1"] = d["portal_y0"] - 20, d["spine_y1"] + p["foot_back_bar"]
    d["foot_w"] = d["leg_r_x1"] - d["portal_x0"]
    h = p["h"]
    vol = {}
    vol["spine"] = p["spine_w"] * (d["spine_y1"] - d["spine_y0"]) * h
    vol["foot"] = d["foot_w"] * (d["foot_y1"] - d["foot_y0"]) * h - p["spine_w"] * (d["spine_y1"] - d["foot_y0"]) * h
    legs = 2 * p["upright_w"] * p["portal_d"] * p["opening_h"]
    beam = d["portal_w"] * p["portal_d"] * p["beam_h"]
    cores = p["pvc_cores"] * math.pi * (p["pvc_core_d"]/2)**2 * (d["portal_w"] - 120)
    vol["portal"] = legs + beam - cores
    vol["base"] = vol.pop("spine") + vol.pop("foot")            # D-76: one T-shaped base casting
    vol = {"base": vol["base"], "portal": vol["portal"]}
    d["kg"] = {k: v * 1e-9 * p["eg_density"] for k, v in vol.items()}
    d["kg_total"] = sum(d["kg"].values())
    d["epoxy_kg_11pct"] = 0.11 * d["kg_total"]; d["aggregate_kg"] = 0.89 * d["kg_total"]
    d["bench_top_above_floor"] = p["table_top_above_floor"] - d["table_top_z"] - h
    d["footprint"] = (d["portal_x1"] - d["portal_x0"] + 40, d["foot_y1"] - d["spine_y0"] + 120)
    return d

D = derive(P)

def box(x0, x1, y0, y1, z0, z1):
    return cq.Workplane("XY").box(x1-x0, y1-y0, z1-z0, centered=False).translate((x0, y0, z0))

def build(t=0.0, x=0.0, znose=None):
    p, d = P, D; znose = d["nose_top"] if znose is None else znose
    parts = {}
    base = box(-p["spine_w"]/2, p["spine_w"]/2, d["spine_y0"], d["foot_y1"], -p["h"], 0)
    parts["base"] = base.union(box(d["portal_x0"], d["leg_r_x1"], d["foot_y0"], d["foot_y1"], -p["h"], 0))
    portal = box(d["portal_x0"], d["portal_x1"], d["portal_y0"], d["portal_y1"], 0, d["beam_top"])
    portal = portal.cut(box(d["open_x0"], d["open_x1"], d["portal_y0"]-1, d["portal_y1"]+1, -1, d["beam_bottom"]))
    portal = portal.cut(box(d["leg_r_x1"], d["portal_x1"]+1, d["portal_y0"]-1, d["portal_y1"]+1, -1, d["beam_bottom"]))
    parts["portal"] = portal
    for s in (-1, 1):
        cx = s * p["y_rail_spacing"]/2
        parts[f"y_rail{s}"] = box(cx-10, cx+10, -d["rail_y"]/2, d["rail_y"]/2, 0, p["rail_h"])
    parts["table"] = box(-p["table_x"]/2, p["table_x"]/2, t-p["table_y"]/2, t+p["table_y"]/2, p["block_h"], d["table_top_z"])
    zc = (d["beam_bottom"] + d["beam_top"]) / 2; fy = d["portal_y0"]
    for s in (-1, 1):
        z = zc + s * p["x_rail_spacing"]/2
        xm = (d["x_min"] + d["x_max"]) / 2
        parts[f"x_rail{s}"] = box(xm-d["rail_x"]/2, xm+d["rail_x"]/2, fy-p["rail_h"], fy, z-10, z+10)
    sy1 = fy - p["block_h"]
    parts["saddle"] = box(x-p["saddle_w"]/2, x+p["saddle_w"]/2, sy1-20, sy1, zc-80, zc+80)
    zp1 = sy1 - 20 - p["block_h"]
    parts["z_plate"] = box(x-70, x+70, zp1-20, zp1, znose+30, znose+30+d["rail_z"])
    parts["spindle"] = cq.Workplane("XY").circle(p["spindle_d"]/2).extrude(p["spindle_len"]).translate((x, 0, znose))
    wheel = cq.Workplane("YZ").circle(d["wheel_d"]/2).extrude(p["wheel_t"]).translate((d["pickup_x"]-p["wheel_t"]/2, 0, d["fork_z"]-d["wheel_d"]/2))
    parts["atc_wheel"] = wheel
    return parts

def report():
    p, d = P, D; r = lambda v: f"{v:,.0f}"
    L = ["# Type 0 v2: key dimensions (generated)", "", "From `cad/v2/type0_v2.py`. Z = 0 is the top of the spine/foot castings.", "",
         "| | |", "|---|---|",
         f"| Travel X / Y / Z | {r(d['travel_x'])} (400 work + reach to the ATC wheel) / {r(p['travel_y'])} / {r(p['travel_z'])} |",
         f"| Table | {p['table_x']} x {p['table_y']} x {p['table_t']}, top at Z {r(d['table_top_z'])} |",
         f"| Spindle nose top / bottom | Z {r(d['nose_top'])} / {r(d['nose_bottom'])} |",
         f"| Gantry opening | {r(d['open_x1']-d['open_x0'])} wide x {r(d['beam_bottom'])} high. Beam top Z {r(d['beam_top'])} |",
         f"| ATC wheel | dia {r(d['wheel_d'])}, {p['wheel_pockets']} pockets, pickup at X {r(d['pickup_x'])}, fork plane Z {r(d['fork_z'])} |", "",
         "## Castings", "| Casting | Size (mm) | Mass |", "|---|---|---|",
         f"| Base (T-shape: spine {p['spine_w']} wide x {r(d['foot_y1']-d['spine_y0'])} long, rear cross-piece {r(d['foot_w'])} x {r(d['foot_y1']-d['foot_y0'])}), {p['h']} high | one piece, 2-person lift | {d['kg']['base']:.1f} kg |",
         f"| Gantry portal ({p['pvc_cores']} x {p['pvc_core_d']} mm PVC cores) | {r(d['portal_w'])} W x {r(d['beam_top'])} H x {p['portal_d']} D | {d['kg']['portal']:.1f} kg |",
         f"| **Total** | | **{d['kg_total']:.1f} kg** |",
         f"| Epoxy at 11% / aggregate at 89% | | {d['epoxy_kg_11pct']:.1f} / {d['aggregate_kg']:.1f} kg |", "",
         "## Rails and screws (minimum)", "| Axis | Rail | Screw |", "|---|---|---|",
         f"| X | 2 x {r(d['rail_x'])} | {r(d['screw_x'])} |",
         f"| Y | 2 x {r(d['rail_y'])} | {r(d['screw_y'])} |",
         f"| Z | 2 x {r(d['rail_z'])} | {r(d['screw_z'])} |", "",
         "## Bench", f"Bench top {r(d['bench_top_above_floor'])} mm above the floor (table top at {p['table_top_above_floor']}). Machine footprint about {r(d['footprint'][0])} x {r(d['footprint'][1])} mm."]
    (OUT/"dimensions_v2.md").write_text("\n".join(L)+"\n")
    (OUT/"dimensions_v2.json").write_text(json.dumps(d, indent=1, default=str))

if __name__ == "__main__":
    report()
    asm = cq.Assembly()
    for k, v in build().items(): asm.add(v, name=k)
    asm.export(str(OUT/"type0_v2.step"))
    print((OUT/"dimensions_v2.md").read_text())

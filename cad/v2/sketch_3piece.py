"""Type 0 v2 (scaled down, D-71): 3-piece epoxy-granite frame concept sketch.

Run: python cad/v2/sketch_3piece.py  -> cad/v2/out/sketch_*.svg + masses
Coordinates: X right, Y back (Y=0 = spindle line), Z up from bench top.
All sizes are concept values for review, not final.
"""
import pathlib
OUT = pathlib.Path(__file__).parent / "out"; OUT.mkdir(exist_ok=True)
EG = 2300  # kg/m3

P = dict(travel_x_work=200, travel_y=200, travel_z=150,
         table_x=280, table_y=280, table_t=25, block_h=30,
         y_rail_spacing=180,
         rack_cols=2, rack_pitch=60, rack_gap=20,           # rack on table +X side
         h=110,                                              # spine/foot height
         spine_w=260, upright_w=90, portal_d=130, beam_h=130,
         beam_front=110, foot_d=220, foot_back_bar=60)

def derive(p):
    d = {}
    d["rack_w"] = p["rack_cols"] * p["rack_pitch"] + p["rack_gap"]
    d["table_x0"], d["table_x1"] = -p["table_x"]/2, p["table_x"]/2
    d["rack_x0"], d["rack_x1"] = d["table_x1"], d["table_x1"] + d["rack_w"]
    d["open_x0"], d["open_x1"] = d["table_x0"] - 30, d["rack_x1"] + 30
    d["portal_x0"], d["portal_x1"] = d["open_x0"] - p["upright_w"], d["open_x1"] + p["upright_w"]
    d["portal_w"] = d["portal_x1"] - d["portal_x0"]
    d["open_h"] = p["block_h"] + p["table_t"] + 100 + 70      # vise 100 + margin
    d["portal_h"] = d["open_h"] + p["beam_h"]
    d["spindle_x_max"] = d["rack_x1"] - p["rack_pitch"]/2 - p["rack_gap"]/2
    d["travel_x_total"] = p["travel_x_work"]/2 + d["spindle_x_max"]
    t_min, t_max = -p["travel_y"]/2, p["travel_y"]/2
    d["spine_y0"] = t_min - p["table_y"]/2 - 50
    d["portal_y0"] = p["beam_front"]; d["portal_y1"] = p["beam_front"] + p["portal_d"]
    d["spine_y1"] = d["portal_y1"] + 20
    d["foot_y0"] = d["portal_y0"] - 20; d["foot_y1"] = d["spine_y1"] + p["foot_back_bar"]
    # masses
    h = p["h"]/1000
    spine = p["spine_w"]/1000 * (d["spine_y1"]-d["spine_y0"])/1000 * h
    foot = d["portal_w"]/1000*(d["foot_y1"]-d["foot_y0"])/1000*h - p["spine_w"]/1000*(d["spine_y1"]-d["foot_y0"])/1000*h
    portal = d["portal_w"]/1000*p["portal_d"]/1000*d["portal_h"]/1000 - (d["open_x1"]-d["open_x0"])/1000*p["portal_d"]/1000*d["open_h"]/1000
    d["kg"] = {"spine": spine*EG, "foot": foot*EG, "portal": portal*EG}
    d["kg"]["total"] = sum(d["kg"].values())
    return d

D = derive(P)
COL = dict(spine="#c9c9c4", foot="#b9c7b4", portal="#d7c9b0", table="#9fb6cc", rack="#f3d27a", rail="#3d4f66")

def svg(name, w, h, title, body):
    (OUT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Helvetica, Arial, sans-serif"><rect width="{w}" height="{h}" fill="#fff"/><text x="{w/2}" y="26" text-anchor="middle" font-size="17" font-weight="bold">{title}</text>{body}</svg>')

def R(x0, y0, x1, y1, fill, op=1, dash=""):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{min(x0,x1):.1f}" y="{min(y0,y1):.1f}" width="{abs(x1-x0):.1f}" height="{abs(y1-y0):.1f}" fill="{fill}" fill-opacity="{op}" stroke="#333" stroke-width="0.8"{ds}/>'
def T(x, y, s, a="middle", sz=11, c="#222", b=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{a}" font-size="{sz}" fill="{c}"{" font-weight=\"bold\"" if b else ""}>{s}</text>'

S = 0.6
def top():
    p, d = P, D
    W, H = 900, 640; ox, oy = 420, 330
    X = lambda x: ox + x*S; Y = lambda y: oy - y*S
    b = ""
    b += R(X(d["portal_x0"]), Y(d["foot_y1"]), X(d["portal_x1"]), Y(d["foot_y0"]), COL["foot"])
    b += R(X(-p["spine_w"]/2), Y(d["spine_y1"]), X(p["spine_w"]/2), Y(d["spine_y0"]), COL["spine"])
    for s in (-1, 1):
        b += R(X(s*p["y_rail_spacing"]/2-10), Y(200), X(s*p["y_rail_spacing"]/2+10), Y(-200), COL["rail"])
    b += R(X(d["table_x0"]), Y(p["table_y"]/2), X(d["table_x1"]), Y(-p["table_y"]/2), COL["table"], 0.85)
    b += R(X(d["rack_x0"]), Y(p["table_y"]/2), X(d["rack_x1"]), Y(-p["table_y"]/2), COL["rack"], 0.9)
    for c in range(p["rack_cols"]):
        for r in range(4):
            cx = d["rack_x0"] + p["rack_gap"] + p["rack_pitch"]/2 + c*p["rack_pitch"] - 10
            cy = -90 + r*p["rack_pitch"]
            b += f'<circle cx="{X(cx):.1f}" cy="{Y(cy):.1f}" r="{14*S*1.4:.1f}" fill="none" stroke="#9a7514"/>'
    b += R(X(d["portal_x0"]), Y(d["portal_y1"]), X(d["portal_x1"]), Y(d["portal_y0"]), COL["portal"], 0.75)
    b += f'<line x1="{X(d["portal_x0"]-30)}" y1="{Y(0)}" x2="{X(d["portal_x1"]+30)}" y2="{Y(0)}" stroke="#2c5d8f" stroke-dasharray="8 4"/>'
    b += T(X(d["portal_x1"]+34), Y(0)+4, "spindle line", "start", 10, "#2c5d8f")
    b += T(X(0), Y(d["spine_y0"])+16, f'Y SPINE {p["spine_w"]}×{d["spine_y1"]-d["spine_y0"]:.0f}×{p["h"]}  ≈{d["kg"]["spine"]:.0f} kg', "middle", 11, "#222", True)
    b += T(X(d["portal_x0"]), Y(d["foot_y1"])-6, f'REAR FOOT {d["portal_w"]:.0f}×{d["foot_y1"]-d["foot_y0"]:.0f}×{p["h"]} (U-shape round spine end) ≈{d["kg"]["foot"]:.0f} kg', "start", 11, "#222", True)
    b += T(X(d["portal_x1"])+6, Y(d["portal_y1"])+12, f'GANTRY PORTAL ≈{d["kg"]["portal"]:.0f} kg', "start", 11, "#222", True)
    b += T(X(d["rack_x1"])+6, Y(-60), "tool rack on table side", "start", 10, "#9a7514")
    b += T(X(d["rack_x1"])+6, Y(-60)+13, "(2 × 4, moves with table)", "start", 10, "#9a7514")
    b += T(X(0), Y(d["spine_y0"])+34, "FRONT (Y motor)", "middle", 10)
    b += T(W/2, H-40, f'Top view. Frame total ≈{d["kg"]["total"]:.0f} kg EG in 3 castings. Only joint: spine end into the rear-foot U (dowels + bolts).', "middle", 11, "#555")
    b += T(W/2, H-24, f'X travel {d["travel_x_total"]:.0f} (200 work + rack), Y {p["travel_y"]}, Z {p["travel_z"]}. Portal opening {d["open_x1"]-d["open_x0"]:.0f} wide, offset towards the rack side.', "middle", 11, "#555")
    svg("sketch_top.svg", W, H, "Type 0 v2: 3-piece cast frame (concept)", b)

def front():
    p, d = P, D
    W, H = 900, 470; ox, oy = 420, 360
    X = lambda x: ox + x*S; Z = lambda z: oy - z*S
    b = R(X(d["portal_x0"]), Z(0), X(d["portal_x1"]), Z(-p["h"]), COL["foot"])
    b += R(X(-p["spine_w"]/2), Z(0), X(p["spine_w"]/2), Z(-p["h"]), COL["spine"], 0.9, "4 3")
    for s in (-1, 1):
        x0, x1 = (d["portal_x0"], d["open_x0"]) if s < 0 else (d["open_x1"], d["portal_x1"])
        b += R(X(x0), Z(d["open_h"]), X(x1), Z(0), COL["portal"])
        b += R(X(s*p["y_rail_spacing"]/2-10), Z(17.5), X(s*p["y_rail_spacing"]/2+10), Z(0), COL["rail"])
    b += R(X(d["portal_x0"]), Z(d["portal_h"]), X(d["portal_x1"]), Z(d["open_h"]), COL["portal"])
    b += R(X(d["table_x0"]), Z(p["block_h"]+p["table_t"]), X(d["table_x1"]), Z(p["block_h"]), COL["table"])
    b += R(X(d["rack_x0"]), Z(p["block_h"]+p["table_t"]+60), X(d["rack_x1"]), Z(p["block_h"]+p["table_t"]+50), COL["rack"])
    b += T(X(0), Z(-p["h"])+16, "spine (dashed) inside the rear foot U", "middle", 10)
    b += T(X((d["open_x0"]+d["open_x1"])/2), Z(d["open_h"])+14, f'opening {d["open_x1"]-d["open_x0"]:.0f} × {d["open_h"]:.0f}', "middle", 11, "#c0392b")
    b += T(X(0), Z(d["portal_h"])-8, f'portal {d["portal_w"]:.0f} W × {d["portal_h"]:.0f} H × {p["portal_d"]} D', "middle", 11, "#c0392b")
    svg("sketch_front.svg", W, H, "Type 0 v2: front view (concept)", b)

if __name__ == "__main__":
    top(); front()
    for k, v in D["kg"].items(): print(f"{k}: {v:.1f} kg")
    print("portal_w", D["portal_w"], "open", D["open_x1"]-D["open_x0"], "x travel", D["travel_x_total"], "spine len", D["spine_y1"]-D["spine_y0"])

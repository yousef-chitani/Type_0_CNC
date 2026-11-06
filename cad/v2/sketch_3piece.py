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
         wheel_pockets=8, pocket_pitch=70, wheel_gap=20, wheel_t=60,   # ferris wheel beside +X leg, turns in the Y-Z plane (D-73)
         leg_clear=20, saddle_w=180,
         h=110,                                              # spine/foot height
         spine_w=260, upright_w=70, portal_d=130, beam_h=130,
         beam_front=110, foot_d=220, foot_back_bar=60)

def derive(p):
    d = {}
    import math
    d["table_x0"], d["table_x1"] = -p["table_x"]/2, p["table_x"]/2
    d["open_x0"], d["open_x1"] = d["table_x0"] - p["leg_clear"], d["table_x1"] + p["leg_clear"]
    d["leg_r_x1"] = d["open_x1"] + p["upright_w"]
    d["wheel_d"] = p["wheel_pockets"] * p["pocket_pitch"] / math.pi
    d["pickup_x"] = d["leg_r_x1"] + p["wheel_gap"] + p["wheel_t"]/2
    d["spindle_x_max"] = d["pickup_x"]
    d["portal_x0"] = d["open_x0"] - p["upright_w"]
    d["portal_x1"] = d["pickup_x"] + p["saddle_w"]/2 + 20          # beam overhang past the right leg
    d["portal_w"] = d["portal_x1"] - d["portal_x0"]
    d["open_h"] = p["block_h"] + p["table_t"] + 100 + 70      # vise 100 + margin
    d["portal_h"] = d["open_h"] + p["beam_h"]
    d["travel_x_total"] = p["travel_x_work"]/2 + d["spindle_x_max"]
    d["x_rail_len"] = d["travel_x_total"] + p["saddle_w"]
    t_min, t_max = -p["travel_y"]/2, p["travel_y"]/2
    d["spine_y0"] = t_min - p["table_y"]/2 - 50
    d["portal_y0"] = p["beam_front"]; d["portal_y1"] = p["beam_front"] + p["portal_d"]
    d["spine_y1"] = d["portal_y1"] + 20
    d["foot_y0"] = d["portal_y0"] - 20; d["foot_y1"] = d["spine_y1"] + p["foot_back_bar"]
    # masses
    h = p["h"]/1000
    spine = p["spine_w"]/1000 * (d["spine_y1"]-d["spine_y0"])/1000 * h
    foot_w = d["leg_r_x1"] - d["portal_x0"]
    d["foot_w"] = foot_w
    foot = foot_w/1000*(d["foot_y1"]-d["foot_y0"])/1000*h - p["spine_w"]/1000*(d["spine_y1"]-d["foot_y0"])/1000*h
    legs = 2 * p["upright_w"]/1000 * p["portal_d"]/1000 * d["open_h"]/1000
    beam = d["portal_w"]/1000 * p["portal_d"]/1000 * p["beam_h"]/1000
    cores = 2 * math.pi * 0.025**2 * (d["portal_w"]/1000 - 0.12)      # 2 x 50 mm capped PVC cores (D-74)
    portal = legs + beam
    d["portal_cored"] = (portal - cores) * EG
    d["kg"] = {"spine": spine*EG, "foot": foot*EG, "portal": portal*EG}
    import math as _m
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
    W, H = 900, 640; ox, oy = 380, 330
    X = lambda x: ox + x*S; Y = lambda y: oy - y*S
    b = ""
    b += R(X(d["portal_x0"]), Y(d["foot_y1"]), X(d["leg_r_x1"]), Y(d["foot_y0"]), COL["spine"])
    b += R(X(-p["spine_w"]/2), Y(d["foot_y0"]), X(p["spine_w"]/2), Y(d["spine_y0"]), COL["spine"])
    for s_ in (-1, 1):
        b += R(X(s_*p["y_rail_spacing"]/2-10), Y(200), X(s_*p["y_rail_spacing"]/2+10), Y(-200), COL["rail"])
    b += R(X(d["table_x0"]), Y(p["table_y"]/2), X(d["table_x1"]), Y(-p["table_y"]/2), COL["table"], 0.85)
    b += R(X(d["portal_x0"]), Y(d["portal_y1"]), X(d["portal_x1"]), Y(d["portal_y0"]), COL["portal"], 0.75)
    b += R(X(d["pickup_x"]-p["wheel_t"]/2), Y(d["wheel_d"]/2), X(d["pickup_x"]+p["wheel_t"]/2), Y(-d["wheel_d"]/2), COL["rack"], 0.9)
    b += f'<line x1="{X(d["portal_x0"]-30)}" y1="{Y(0)}" x2="{X(d["portal_x1"]+30)}" y2="{Y(0)}" stroke="#2c5d8f" stroke-dasharray="8 4"/>'
    b += T(X(d["portal_x1"]+34), Y(0)+4, "spindle line", "start", 10, "#2c5d8f")
    b += T(X(0), Y(d["spine_y0"])+16, f'BASE: one T-shaped casting ≈{d["kg"]["spine"]+d["kg"]["foot"]:.0f} kg (2-person lift)', "middle", 11, "#222", True)
    b += T(X(d["portal_x1"])+6, Y(d["portal_y1"])+12, f'PORTAL ≈{d["kg"]["portal"]:.0f} kg ({d["portal_cored"]:.0f} kg cored)', "start", 11, "#222", True)
    b += T(X(d["pickup_x"]+p["wheel_t"]/2+6), Y(-d["wheel_d"]/2)+12, "ferris-wheel ATC, turns in Y-Z", "start", 10, "#9a7514")
    b += T(X(0), Y(d["spine_y0"])+34, "FRONT (Y motor)", "middle", 10)
    b += T(W/2, H-40, f'Top view. Frame ≈{d["kg"]["total"]:.0f} kg EG in 2 castings (base + portal). Only joint: portal legs to base (dowels + bolts).', "middle", 11, "#555")
    b += T(W/2, H-24, f'X travel {d["travel_x_total"]:.0f} (200 work + reach to wheel), X rails {d["x_rail_len"]:.0f}, Y {p["travel_y"]}, Z {p["travel_z"]}. Legs span the table only (opening {d["open_x1"]-d["open_x0"]:.0f}).', "middle", 11, "#555")
    svg("sketch_top.svg", W, H, "Type 0 v2: 2-piece cast frame (concept, rev C)", b)

def front():
    p, d = P, D
    W, H = 900, 470; ox, oy = 380, 360
    X = lambda x: ox + x*S; Z = lambda z: oy - z*S
    b = R(X(d["portal_x0"]), Z(0), X(d["leg_r_x1"]), Z(-p["h"]), COL["spine"])
    b += R(X(d["portal_x0"]), Z(d["open_h"]), X(d["open_x0"]), Z(0), COL["portal"])
    b += R(X(d["open_x1"]), Z(d["open_h"]), X(d["leg_r_x1"]), Z(0), COL["portal"])
    b += R(X(d["portal_x0"]), Z(d["portal_h"]), X(d["portal_x1"]), Z(d["open_h"]), COL["portal"])
    for xc in (d["portal_x0"]+60, d["portal_x1"]-60):
        pass
    b += f'<line x1="{X(d["portal_x0"]+60)}" y1="{Z(d["open_h"]+p["beam_h"]/2)}" x2="{X(d["portal_x1"]-60)}" y2="{Z(d["open_h"]+p["beam_h"]/2)}" stroke="#8a6d3b" stroke-dasharray="6 3"/>'
    for s_ in (-1, 1):
        b += R(X(s_*p["y_rail_spacing"]/2-10), Z(17.5), X(s_*p["y_rail_spacing"]/2+10), Z(0), COL["rail"])
    b += R(X(d["table_x0"]), Z(p["block_h"]+p["table_t"]), X(d["table_x1"]), Z(p["block_h"]), COL["table"])
    fork_z = p["block_h"] + p["table_t"] + 40
    cz = fork_z - d["wheel_d"]/2
    b += R(X(d["pickup_x"]-p["wheel_t"]/2), Z(fork_z+20), X(d["pickup_x"]+p["wheel_t"]/2), Z(fork_z-d["wheel_d"]), COL["rack"], 0.8)
    b += T(X(d["pickup_x"]+p["wheel_t"]/2+6), Z(fork_z-d["wheel_d"]/2), f'wheel Ø{d["wheel_d"]:.0f} edge-on', "start", 10, "#9a7514")
    b += T(X(d["pickup_x"]+p["wheel_t"]/2+6), Z(fork_z-d["wheel_d"]/2)-13, '8 pockets, top pocket = pickup', "start", 10, "#9a7514")
    b += T(X((d["open_x0"]+d["open_x1"])/2), Z(d["open_h"])+14, f'opening {d["open_x1"]-d["open_x0"]:.0f} × {d["open_h"]:.0f}', "middle", 11, "#c0392b")
    b += T(X((d["portal_x0"]+d["portal_x1"])/2), Z(d["portal_h"])-8, f'portal {d["portal_w"]:.0f} W × {d["portal_h"]:.0f} H × {p["portal_d"]} D, beam overhang {d["portal_x1"]-d["leg_r_x1"]:.0f}', "middle", 11, "#c0392b")
    b += T(X(0), Z(-p["h"])+16, "base: one casting (spine + rear cross-piece). Dashed line in beam: capped PVC cores", "middle", 10)
    svg("sketch_front.svg", W, H, "Type 0 v2: front view (concept, rev C)", b)

if __name__ == "__main__":
    top(); front()
    for k, v in D["kg"].items(): print(f"{k}: {v:.1f} kg")
    print("portal_cored", round(D["portal_cored"],1), "portal_w", D["portal_w"], "open", D["open_x1"]-D["open_x0"], "x travel", round(D["travel_x_total"]), "x rails", round(D["x_rail_len"]), "wheel d", round(D["wheel_d"]), "overhang", round(D["portal_x1"]-D["leg_r_x1"]))

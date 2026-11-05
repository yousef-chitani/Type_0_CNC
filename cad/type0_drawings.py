"""Dimensioned 2D views generated from the same parameters as type0_layout.py.

Run:  python cad/type0_drawings.py   -> cad/out/drawing_side.svg, drawing_front.svg
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from type0_layout import P, D, OUT

S = 0.5  # drawing scale px per mm
COL = dict(eg="#c9c9c4", steel="#3d4f66", alu="#9fb6cc", rack="#f3d27a", spindle="#8e8e8e", stand="#6b6b6b", tool="#e0a96d")

class Svg:
    def __init__(s, w, h, title, sub):
        s.w, s.h, s.items = w, h, []
        s.items.append(f'<rect width="{w}" height="{h}" fill="#fff"/>')
        s.items.append(f'<text x="{w/2}" y="28" text-anchor="middle" font-size="18" font-weight="bold">{title}</text>')
        s.items.append(f'<text x="{w/2}" y="48" text-anchor="middle" font-size="12" fill="#555">{sub}</text>')
    def rect(s, x0, y0, x1, y1, fill, stroke="#333", op=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.items.append(f'<rect x="{min(x0,x1):.1f}" y="{min(y0,y1):.1f}" width="{abs(x1-x0):.1f}" height="{abs(y1-y0):.1f}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="0.8"{d}/>')
    def text(s, x, y, t, anchor="start", size=11, fill="#222", bold=False):
        b = ' font-weight="bold"' if bold else ""
        s.items.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" fill="{fill}"{b}>{t}</text>')
    def dim_h(s, x0, x1, y, label):
        s.items.append(f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1:.1f}" y2="{y:.1f}" stroke="#c0392b" marker-start="url(#a)" marker-end="url(#a)"/>')
        s.text((x0+x1)/2, y-4, label, "middle", 11, "#c0392b")
    def dim_v(s, x, y0, y1, label):
        s.items.append(f'<line x1="{x:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y1:.1f}" stroke="#c0392b" marker-start="url(#a)" marker-end="url(#a)"/>')
        s.text(x+5, (y0+y1)/2+4, label, "start", 11, "#c0392b")
    def save(s, name):
        defs = '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#c0392b"/></marker></defs>'
        (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" font-family="Helvetica, Arial, sans-serif">{defs}' + "".join(s.items) + "</svg>")

def side(t, rack_off, znose, name, title):
    p, d = P, D
    floor = -d["base_top_above_floor"]
    zmax = d["nose_z_top"] + 40 + d["rail_z_len"] + 30
    W, H = 1000, int(80 + (zmax - floor + 40) * S)
    ox, oy = 470, 80 + zmax * S                          # screen origin = (Y=0, Z=0)
    X = lambda y: ox + y * S
    Y = lambda z: oy - z * S
    v = Svg(W, H, title, "Side view from the right (front of machine on the left). Scale 1:2 on screen, mm")
    # stand
    st = p["stand_tube"]; y0s, y1s = d["base_y0"]-20, d["base_y1"]+20
    v.rect(X(y0s), Y(-p["base_h"]), X(y1s), Y(-p["base_h"]-st), COL["stand"])
    v.rect(X(y0s), Y(floor+p["stand_low_ring"]+st), X(y1s), Y(floor+p["stand_low_ring"]), COL["stand"])
    for yy in (y0s, y1s-st):
        v.rect(X(yy), Y(-p["base_h"]-st), X(yy+st), Y(floor+p["feet_h"]), COL["stand"])
    v.rect(X(y0s+st+30), Y(-p["base_h"]-st-20), X(y0s+st+230), Y(-p["base_h"]-st-420), "#ddd", dash="4 3")
    v.text(X(y0s+st+130), Y(-p["base_h"]-st-220), "cabinet 600x400x200", "middle", 10, "#666")
    v.items.append(f'<line x1="{X(y0s)-40}" y1="{Y(floor)}" x2="{X(y1s)+40}" y2="{Y(floor)}" stroke="#333" stroke-width="2"/>')
    # base, gantry
    v.rect(X(d["base_y0"]), Y(0), X(d["base_y1"]), Y(-p["base_h"]), COL["eg"])
    v.rect(X(d["gantry_y0"]), Y(d["beam_top_z"]), X(d["gantry_y1"]), Y(d["beam_bottom_z"]), COL["eg"])
    v.rect(X(d["gantry_y0"]), Y(d["beam_bottom_z"]), X(d["gantry_y1"]), Y(0), COL["eg"], op=0.35, dash="5 3")
    # Y rail, table
    ymid = (d["t_min"] + d["t_max"]) / 2
    v.rect(X(ymid-d["rail_y_len"]/2), Y(p["rail_h"]), X(ymid+d["rail_y_len"]/2), Y(0), COL["steel"])
    v.rect(X(t-p["table_y"]/2), Y(d["table_top_z"]), X(t+p["table_y"]/2), Y(p["block_assy_h"]), COL["alu"])
    v.rect(X(t-p["table_y"]/2+40), Y(d["table_top_z"]+p["vise_height"]), X(t-p["table_y"]/2+190), Y(d["table_top_z"]), "#e8e8e8", dash="3 2")
    # X rails, saddle, Z plate, spindle
    fy = d["gantry_y0"]; zc = (d["beam_bottom_z"] + d["beam_top_z"]) / 2
    for sgn in (-1, 1):
        z = zc + sgn * p["x_rail_spacing"]/2
        v.rect(X(fy-p["rail_h"]), Y(z+10), X(fy), Y(z-10), COL["steel"])
    sy1 = fy - p["block_assy_h"]
    v.rect(X(sy1-20), Y(zc+115), X(sy1), Y(zc-115), COL["alu"])
    zp1 = sy1 - 20 - p["block_assy_h"]
    v.rect(X(zp1-20), Y(znose+40+d["rail_z_len"]), X(zp1), Y(znose+40), COL["alu"])
    v.rect(X(-p["spindle_d"]/2), Y(znose+p["spindle_len"]), X(p["spindle_d"]/2), Y(znose), COL["spindle"])
    v.rect(X(-16), Y(znose), X(16), Y(znose-60), COL["tool"])
    # rack
    rf = d["rack_front_parked"] - rack_off
    v.rect(X(rf), Y(d["fork_z"]), X(rf+p["row_pitch_y"]+2*p["fork_half_depth"]), Y(d["fork_z"]-10), COL["rack"])
    for row in (0, 1):
        py = rf + p["fork_half_depth"] + row*p["row_pitch_y"]
        v.rect(X(py-16), Y(d["fork_z"]+p["holder_above_fork"]), X(py+16), Y(d["fork_z"]-p["tool_below_fork"]), COL["tool"], op=0.8)
    v.rect(X(d["base_y1"]-d["rack_rail_len"]-20), Y(12.5), X(d["base_y1"]-20), Y(0), COL["steel"], op=0.6)
    # spindle axis line
    v.items.append(f'<line x1="{X(0)}" y1="{Y(d["beam_top_z"]+30)}" x2="{X(0)}" y2="{Y(-p["base_h"])}" stroke="#2c5d8f" stroke-dasharray="8 4"/>')
    v.text(X(0), Y(d["beam_top_z"]+34), "spindle axis", "middle", 10, "#2c5d8f")
    # dimensions
    v.dim_h(X(d["base_y0"]), X(d["base_y1"]), Y(-p["base_h"])+18, f'base {d["base_len"]:.0f}')
    v.dim_v(X(d["base_y1"])+20, Y(0), Y(-p["base_h"]), f'{p["base_h"]:.0f}')
    v.dim_v(X(d["base_y1"])+70, Y(d["beam_top_z"]), Y(0), f'gantry {d["beam_top_z"]:.0f}')
    v.dim_v(X(d["gantry_y1"])+125, Y(d["beam_bottom_z"]), Y(0), f'opening {d["beam_bottom_z"]:.0f}')
    v.items.append(f'<line x1="{X(d["gantry_y1"])}" y1="{Y(d["beam_bottom_z"])}" x2="{X(d["gantry_y1"])+130}" y2="{Y(d["beam_bottom_z"])}" stroke="#c0392b" stroke-dasharray="2 2"/>')
    v.dim_v(X(d["base_y0"])-30, Y(0), Y(floor), f'{d["base_top_above_floor"]:.0f}')
    v.dim_v(X(d["base_y0"])-80, Y(d["table_top_z"]), Y(floor), f'table {p["table_top_above_floor"]:.0f}')
    v.text(X(d["base_y0"]), Y(-p["base_h"])-6, "FRONT (Y motor)", "start", 10)
    v.text(X(d["base_y1"]), Y(-p["base_h"])-6, "REAR (rack)", "end", 10)
    v.save(name)

def front():
    p, d = P, D
    zmax = d["nose_z_top"] + 40 + d["rail_z_len"] + 70
    W, H = 900, int(90 + (zmax + p["base_h"] + p["stand_tube"] + 60) * S)
    ox, oy = W/2, 70 + zmax * S
    X = lambda x: ox + x * S
    Y = lambda z: oy - z * S
    v = Svg(W, H, "Type 0: front view", "Looking from the front. Gantry, base and stand top. Scale 1:2 on screen, mm")
    v.rect(X(-p["base_x"]/2), Y(0), X(p["base_x"]/2), Y(-p["base_h"]), COL["eg"])
    g0, g1 = d["gantry_w"]/2, d["opening_w"]/2
    for s in (-1, 1):
        v.rect(X(s*g1), Y(d["beam_bottom_z"]), X(s*g0), Y(0), COL["eg"])
    v.rect(X(-g0), Y(d["beam_top_z"]), X(g0), Y(d["beam_bottom_z"]), COL["eg"])
    zc = (d["beam_bottom_z"] + d["beam_top_z"]) / 2
    for s in (-1, 1):
        z = zc + s*p["x_rail_spacing"]/2
        v.rect(X(-d["rail_x_len"]/2), Y(z+10), X(d["rail_x_len"]/2), Y(z-10), COL["steel"])
        v.rect(X(s*p["y_rail_spacing"]/2-10), Y(p["rail_h"]), X(s*p["y_rail_spacing"]/2+10), Y(0), COL["steel"])
        v.rect(X(s*d["rack_rail_x"]-7.5), Y(12.5), X(s*d["rack_rail_x"]+7.5), Y(0), COL["steel"], op=0.6)
    v.rect(X(-p["table_x"]/2), Y(d["table_top_z"]), X(p["table_x"]/2), Y(p["block_assy_h"]), COL["alu"])
    v.rect(X(-100), Y(zc+115), X(100), Y(zc-115), COL["alu"], op=0.7)
    zn = d["nose_z_top"]
    v.rect(X(-80), Y(zn+40+d["rail_z_len"]), X(80), Y(zn+40), COL["alu"], op=0.8)
    v.rect(X(-40), Y(zn+p["spindle_len"]), X(40), Y(zn), COL["spindle"])
    v.rect(X(-16), Y(zn), X(16), Y(zn-60), COL["tool"])
    v.rect(X(-p["base_x"]/2-20), Y(-p["base_h"]), X(p["base_x"]/2+20), Y(-p["base_h"]-p["stand_tube"]), COL["stand"])
    v.dim_h(X(-g0), X(g0), Y(d["beam_top_z"])-12, f'gantry {d["gantry_w"]:.0f}')
    v.dim_h(X(-g1), X(g1), Y(d["beam_bottom_z"])+16, f'opening {d["opening_w"]:.0f}')
    v.dim_h(X(-p["base_x"]/2), X(p["base_x"]/2), Y(-p["base_h"]-p["stand_tube"])+22, f'base {p["base_x"]:.0f}')
    v.dim_h(X(-p["y_rail_spacing"]/2), X(p["y_rail_spacing"]/2), Y(0)+14, f'Y rails {p["y_rail_spacing"]:.0f}')
    v.dim_h(X(-d["rail_x_len"]/2), X(d["rail_x_len"]/2), Y(d["beam_top_z"])-34, f'X rails {d["rail_x_len"]:.0f}')
    v.text(X(g0)+10, Y(zc), "X motor (right)", "start", 10)
    v.save("drawing_front.svg")

if __name__ == "__main__":
    side(D["t_max"], 0, D["nose_z_top"], "drawing_side.svg", "Type 0: side view (working position)")
    side(D["t_min"], D["rack_stroke"], D["fork_z"] + 10, "drawing_side_toolchange.svg",
         "Type 0: side view (tool change: table forward, rack in, back row under spindle)")
    front()
    print("ok")

"""Type 0 v2 timber bench (task 3, D-97): bolted CLS frame, 2 x 18 mm ply top, cabinet front-left,
cooling loop low-right, lower shelf for the PC, reservoir and tools. Stands against a wall.

Run: python cad/v2/bench.py -> cad/v2/out/bench.step, type0_v2_on_bench.step,
     bench_front.svg, bench_side.svg, bench_top.svg, bench_cutlist.md

Bench coordinates (this file): x right, y back, z up, origin = floor under the front-left corner
of the top. The machine model (type0_v2.py) sits on the top with its enclosure centred on it.
Sizes marked CHECK depend on parts not yet in hand.
"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))

OUT = pathlib.Path(__file__).parent / "out"; OUT.mkdir(exist_ok=True)

B = dict(
    top=1000, top_t=36, top_z=785,      # 2 x 18 mm ply, top surface 785 above the floor (D-75)
    foot_h=30,                           # floor to leg bottom with the T02 feet: CHECK when they arrive
    inset=20,                            # frame set in from the top edge
    leg=(76, 89),                        # 2 x 38 x 89 CLS glued: 76 (x) x 89 (y)
    apron=(38, 89), rail=(38, 63),       # CLS 38 x 89 aprons, 38 x 63 lower rails
    shelf_top=120, sheet_t=18, panel_t=12,
    joist_x=(260, 580),                  # under the edges of the base spine (D-80, spine 320 wide)
    cab=(600, 200, 400),                 # RS PRO 600 W x 200 D x 400 H (E12)
    cab_x0=116, cab_y0=30, cab_stand=89, # cabinet on two 38 x 89 stands on the shelf
    slot=(850, 930, 700, 860),           # cable grommet 80 x 160 (T15) through the top, right of the base,
                                         # behind the ATC wheel, inside the enclosure; cut-out size CHECK
    timber_len=2400, kerf=4,
    sheet=(2440, 1220),
)
t = B["top"]; i0 = B["inset"]; i1 = t - i0
lw, ld = B["leg"]; aw, ah = B["apron"]; rw, rh = B["rail"]
frame_top = B["top_z"] - B["top_t"]                  # 749: top of legs and aprons
leg_len = frame_top - B["foot_h"]
apron_z0 = frame_top - ah
rail_z1 = B["shelf_top"] - B["sheet_t"]; rail_z0 = rail_z1 - rh
cw, cd, chh = B["cab"]
cab_z0 = B["shelf_top"] + B["cab_stand"]

def boxes():
    """All bench parts as (name, group, x0, x1, y0, y1, z0, z1)."""
    P = []
    def add(n, g, x0, x1, y0, y1, z0, z1): P.append((n, g, x0, x1, y0, y1, z0, z1))
    for side, (x0, x1) in (("L", (i0, i0 + lw)), ("R", (i1 - lw, i1))):
        for fb, (y0, y1) in (("front", (i0, i0 + ld)), ("back", (i1 - ld, i1))):
            add(f"Leg {side} {fb}", "leg", x0, x1, y0, y1, B["foot_h"], frame_top)
        xa = (i0, i0 + aw) if side == "L" else (i1 - aw, i1)
        add(f"Side apron {side}", "apron", *xa, i0 + ld, i1 - ld, apron_z0, frame_top)
        add(f"Side rail {side}", "rail", *xa, i0 + ld, i1 - ld, rail_z0, rail_z1)
    xin0, xin1 = i0 + lw, i1 - lw
    for fb, (y0, y1) in (("Front", (i0, i0 + aw)), ("Back", (i1 - aw, i1))):
        add(f"{fb} apron", "apron", xin0, xin1, y0, y1, apron_z0, frame_top)
        add(f"{fb} rail", "rail", xin0, xin1, y0, y1, rail_z0, rail_z1)
    for k, xc in enumerate(B["joist_x"]):
        for j, (xa, xb) in enumerate(((xc - aw, xc), (xc, xc + aw))):
            add(f"Joist {k+1}{'ab'[j]}", "joist", xa, xb, i0 + aw, i1 - aw, apron_z0, frame_top)
    add("Shelf", "sheet18", xin0, xin1, i0, i1, rail_z1, B["shelf_top"])
    add("Top layer 1", "sheet18", 0, t, 0, t, frame_top, frame_top + 18)
    add("Top layer 2", "sheet18", 0, t, 0, t, frame_top + 18, B["top_z"])
    add("Back panel", "sheet18", i0, i1, i1, i1 + B["panel_t"] + 6, B["foot_h"], frame_top)
    add("Side panel L", "sheet12", i0 - B["panel_t"], i0, i0, i1, B["foot_h"], frame_top)
    add("Side panel R (fan holes)", "sheet12", i1, i1 + B["panel_t"], i0, i1, B["foot_h"], frame_top)
    cx0, cy0 = B["cab_x0"], B["cab_y0"]
    for s, (xa, xb) in enumerate(((cx0, cx0 + aw), (cx0 + cw - aw, cx0 + cw))):
        add(f"Cabinet stand {s+1}", "stand", xa, xb, cy0, cy0 + cd, B["shelf_top"], cab_z0)
    return P

def equipment():
    """Things that sit in the bench (not cut from timber): drawn in the views and the STEP."""
    cx0, cy0 = B["cab_x0"], B["cab_y0"]
    return [
        ("Electrical cabinet 600x400x200 (E12)", "#8a96a3", cx0, cx0 + cw, cy0, cy0 + cd, cab_z0, cab_z0 + chh),
        ("Radiator + 2 fans (S05), fans blow out", "#6f8fa8", i1 - 52, i1, 300, 540, 380, 500),
        ("Reservoir + pump (S05/S08), size CHECK", "#7fb3d5", 740, 900, 600, 900, B["shelf_top"], B["shelf_top"] + 200),
        ("Mini-PC (E02)", "#555555", 420, 620, 680, 880, B["shelf_top"], B["shelf_top"] + 50),
        ("Tool tray", "#b9a37a", 116, 380, 330, 900, B["shelf_top"], B["shelf_top"] + 80),
    ]

# ---------------------------------------------------------------------------
# Cut list, timber nesting, sheet nesting
# ---------------------------------------------------------------------------
def cut_items():
    """(stock, part, length, qty) for the timber; sheets separately."""
    P = boxes()
    items = [("CLS 38 x 89", f"Leg laminations (2 glued per leg), cut long: trim to {leg_len:.0f} after gluing", leg_len + 6, 8)]
    def L(n):
        p = [q for q in P if q[0] == n][0]; return max(p[3] - p[2], p[5] - p[4])
    items += [("CLS 38 x 89", "Side aprons", L("Side apron L"), 2),
              ("CLS 38 x 89", "Front + back aprons", L("Front apron"), 2),
              ("CLS 38 x 89", "Joist laminations (2 glued per joist)", L("Joist 1a"), 4),
              ("CLS 38 x 89", "Cabinet stands (on edge)", cd, 2),
              ("CLS 38 x 63", "Side rails", L("Side rail L"), 2),
              ("CLS 38 x 63", "Front + back rails", L("Front rail"), 2),
              ("CLS 38 x 63", "Radiator mounting battens", 300, 2)]
    return items

def nest_timber(items):
    out = {}
    for stock in sorted({i[0] for i in items}):
        pcs = sorted([(ln, part) for s, part, ln, q in items if s == stock for _ in range(q)], reverse=True)
        bars = []
        for ln, part in pcs:
            for b in bars:
                if b["used"] + ln + B["kerf"] <= B["timber_len"]:
                    b["cuts"].append((ln, part)); b["used"] += ln + B["kerf"]; break
            else:
                bars.append({"cuts": [(ln, part)], "used": ln + B["kerf"]})
        out[stock] = bars
    return out

def sheet_parts():
    P = {q[0]: q for q in boxes()}
    def wh(n):
        q = P[n]; d = sorted([q[3] - q[2], q[5] - q[4], q[7] - q[6]], reverse=True); return d[0], d[1]
    return [("18 mm plywood", "Top layer 1", *wh("Top layer 1")),
            ("18 mm plywood", "Top layer 2", *wh("Top layer 2")),
            ("18 mm plywood", "Shelf", *wh("Shelf")),
            ("18 mm plywood", "Back panel", B["top"] - 2 * i0, leg_len),
            ("12 mm plywood", "Side panel L", B["top"] - 2 * i0, leg_len),
            ("12 mm plywood", "Side panel R (2 fan holes)", B["top"] - 2 * i0, leg_len)]

def nest_sheets(parts):
    """Simple shelf (strip) packing on 2440 x 1220 sheets, parts may rotate."""
    SW, SH = B["sheet"]; out = {}
    for stock in sorted({p[0] for p in parts}):
        pcs = sorted([p for p in parts if p[0] == stock], key=lambda p: -p[2] * p[3])
        sheets = []
        for _, name, a, b in pcs:
            placed = False
            for sh in sheets:
                for w, h in ((a, b), (b, a)):
                    for strip in sh["strips"]:                     # same strip, beside the others
                        if h <= strip["h"] and strip["x"] + w <= SW:
                            strip["parts"].append((name, w, h, strip["x"], strip["y"])); strip["x"] += w + B["kerf"]; placed = True; break
                    if placed: break
                    if sh["y"] + h <= SH and w <= SW:                # new strip
                        sh["strips"].append({"y": sh["y"], "h": h, "x": w + B["kerf"], "parts": [(name, w, h, 0, sh["y"])]})
                        sh["y"] += h + B["kerf"]; placed = True; break
                if placed: break
            if not placed:
                w, h = (a, b) if a <= SW and b <= SH else (b, a)
                sheets.append({"y": h + B["kerf"], "strips": [{"y": 0, "h": h, "x": w + B["kerf"], "parts": [(name, w, h, 0, 0)]}]})
        out[stock] = sheets
    return out

# ---------------------------------------------------------------------------
# Load check (hand calculation)
# ---------------------------------------------------------------------------
def load_check():
    E_c16, f_m = 8000.0, 16.0                    # C16: mean E (N/mm2), bending strength (N/mm2)
    span = (i1 - aw) - (i0 + aw)                 # joist span between the front and back aprons
    b, h = 2 * aw, ah                            # doubled 38 x 89
    I = b * h**3 / 12; Z = b * h**2 / 6
    # Loads: castings 106 kg + motion and spindle about 25 kg + enclosure about 35 kg + 50 kg
    # leaning/tools = about 216 kg. Assume 70% goes through the two joists (the base spine sits
    # on them), as one point load at mid-span per joist (worst case; really spread along the spine).
    total_kg = 106 + 25 + 35 + 50
    P = total_kg * 9.81 * 0.7 / 2
    defl = P * span**3 / (48 * E_c16 * I)
    stress = P * span / 4 / Z
    leg_stress = total_kg * 9.81 / 4 / (lw * ld)
    return dict(total_kg=total_kg, P=P, span=span, defl=defl, stress=stress, f_m=f_m, leg_stress=leg_stress)

# ---------------------------------------------------------------------------
# Drawings
# ---------------------------------------------------------------------------
COL = {"leg": "#c8a26b", "apron": "#d8b47c", "rail": "#d8b47c", "joist": "#b88d55", "stand": "#b88d55",
       "sheet18": "#e8d3a8", "sheet12": "#efdfbd"}

def svg(name, title, body, w, h):
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
                            f'font-family="Helvetica, Arial, sans-serif"><rect width="{w}" height="{h}" fill="#fff"/>'
                            f'<text x="{w/2}" y="26" text-anchor="middle" font-size="17" font-weight="bold">{title}</text>{body}</svg>')

def rect(x0, y0, x1, y1, fill, op=1.0, sw=0.8, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{min(x0,x1):.1f}" y="{min(y0,y1):.1f}" width="{abs(x1-x0):.1f}" height="{abs(y1-y0):.1f}" '
            f'fill="{fill}" fill-opacity="{op}" stroke="#333" stroke-width="{sw}"{d}/>')

def text(x, y, s, a="middle", c="#222", sz=11):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{a}" font-size="{sz}" fill="{c}">{s}</text>'

def dim_h(x0, x1, y, label):
    return (f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x1:.1f}" y2="{y:.1f}" stroke="#c0392b" stroke-width="0.8"/>'
            f'<line x1="{x0:.1f}" y1="{y-4:.1f}" x2="{x0:.1f}" y2="{y+4:.1f}" stroke="#c0392b"/>'
            f'<line x1="{x1:.1f}" y1="{y-4:.1f}" x2="{x1:.1f}" y2="{y+4:.1f}" stroke="#c0392b"/>' + text((x0+x1)/2, y-4, label, c="#c0392b"))

def dim_v(x, y0, y1, label):
    return (f'<line x1="{x:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y1:.1f}" stroke="#c0392b" stroke-width="0.8"/>'
            f'<line x1="{x-4:.1f}" y1="{y0:.1f}" x2="{x+4:.1f}" y2="{y0:.1f}" stroke="#c0392b"/>'
            f'<line x1="{x-4:.1f}" y1="{y1:.1f}" x2="{x+4:.1f}" y2="{y1:.1f}" stroke="#c0392b"/>' + text(x+6, (y0+y1)/2, label, "start", "#c0392b"))

def views(machine=None):
    S = 0.42; P = boxes(); EQ = equipment()
    ztop = max([q[4] for q in machine["front"]]) if machine else B["top_z"]
    # front view: x across, z up; sections drawn back to front
    ox, oy = 150, 60 + ztop * S + 10
    X = lambda x: ox + x * S; Z = lambda z: oy - z * S
    b = ""
    order = sorted(P, key=lambda p: -p[5])                      # far parts first
    for n, g, x0, x1, y0, y1, z0, z1 in order:
        if n.startswith("Back panel"): continue
        if n.startswith("Side panel"): continue
        b += rect(X(x0), Z(z1), X(x1), Z(z0), COL[g], 0.9)
    for n, c, x0, x1, y0, y1, z0, z1 in EQ:
        b += rect(X(x0), Z(z1), X(x1), Z(z0), c, 0.75)
    if machine:
        for n, x0, x1, z0, z1, c, op in machine["front"]:
            b += rect(X(x0), Z(z1), X(x1), Z(z0), c, op, dash="5 3" if "enclosure" in n else "")
    b += text(X(B["cab_x0"] + cw/2), Z(cab_z0 + chh/2), "CABINET 600 x 400 x 200", c="#fff", sz=12)
    b += text(X(B["cab_x0"] + cw/2), Z(cab_z0 + chh/2) + 15, "door to the front", c="#fff", sz=10)
    b += text(X(i1 - 26), Z(560), "radiator", c="#1b4f72", sz=10)
    b += text(X(i1 - 26), Z(548) + 14, "fans out", c="#1b4f72", sz=10)
    b += text(X(820), Z(B["shelf_top"] + 120), "reservoir", c="#1b4f72", sz=10)
    b += text(X(520), Z(B["shelf_top"] + 70), "PC", sz=10)
    b += text(X(248), Z(B["shelf_top"]) - 4, "tools (behind)", sz=9)
    b += text(X(850), Z(apron_z0 + 45), "e-stop", c="#c0392b", sz=10)
    b += rect(X(835), Z(apron_z0 + 75), X(865), Z(apron_z0 + 55), "#c0392b", 0.9)
    b += dim_h(X(0), X(t), Z(0) + 28, f"top {t}")
    b += dim_v(X(t) + 20, Z(B["top_z"]), Z(0), f"{B['top_z']} top")
    b += dim_v(X(t) + 90, Z(B["shelf_top"]), Z(0), f"{B['shelf_top']} shelf")
    b += dim_v(X(-40) + 0, Z(cab_z0 + chh), Z(cab_z0), f"")
    b += text(X(-46), Z(cab_z0 + chh/2), f"cabinet {cab_z0:.0f}–{cab_z0+chh:.0f}", "end", "#c0392b", 10)
    b += f'<line x1="{X(-10)}" y1="{Z(0)}" x2="{X(t+130)}" y2="{Z(0)}" stroke="#333" stroke-width="1.5"/>'
    for xf in (i0 + lw/2, i1 - lw/2):
        b += rect(X(xf - 25), Z(B["foot_h"]), X(xf + 25), Z(0), "#666")
    b += text(X(t/2), Z(0) + 48, "Front view (front panel-less: cabinet door and shelf open to the front). Feet T02 under the legs.", sz=11)
    h_front = Z(0) + 60
    top_z_draw = Z(machine["top_z"]) if machine else 0
    b += text(X(t/2), Z(B["top_z"] + 300), "machine + enclosure (dashed)", sz=11, c="#555")
    svg("bench_front.svg", "Type 0 timber bench: front view", b, int(X(t) + 230), int(h_front))

    # side view (y across, front on the left), from the left
    ox2 = 150; Y = lambda y: ox2 + y * S
    b = ""
    for n, g, x0, x1, y0, y1, z0, z1 in sorted(P, key=lambda p: -p[2]):
        if n.startswith("Side panel"): continue
        b += rect(Y(y0), Z(z1), Y(y1), Z(z0), COL[g], 0.9)
    for n, c, x0, x1, y0, y1, z0, z1 in EQ:
        b += rect(Y(y0), Z(z1), Y(y1), Z(z0), c, 0.6)
        if not n.startswith("Electrical"):
            b += text(Y((y0+y1)/2), Z(z1) - 3, n.split(" (")[0].split(",")[0], sz=9, c="#1b4f72")
    if machine:
        for n, y0, y1, z0, z1, c, op in machine["side"]:
            b += rect(Y(y0), Z(z1), Y(y1), Z(z0), c, op, dash="5 3" if "enclosure" in n else "")
    b += dim_h(Y(0), Y(t), Z(0) + 28, f"depth {t} (back to the wall)")
    b += text(Y(B["cab_y0"] + cd/2), Z(cab_z0 + chh/2), "cabinet", c="#fff")
    b += f'<line x1="{Y(-10)}" y1="{Z(0)}" x2="{Y(t+60)}" y2="{Z(0)}" stroke="#333" stroke-width="1.5"/>'
    b += text(Y(t) + 30, Z(400), "wall", "start", "#555")
    b += f'<line x1="{Y(t+18)}" y1="{Z(0)}" x2="{Y(t+18)}" y2="{Z(B["top_z"]+40)}" stroke="#555" stroke-width="3"/>'
    sx0, sx1, sy0, sy1 = B["slot"]
    b += rect(Y(sy0), Z(B["top_z"]) - 3, Y(sy1), Z(frame_top) + 3, "#c0392b", 0.8)
    b += text(Y(sy0) - 4, Z(B["top_z"]) - 8, "cable + hose slot", "end", "#c0392b", 10)
    b += text(Y(t/2), Z(0) + 48, "Side view from the left (front on the left). Joists run front to back under the base spine.", sz=11)
    svg("bench_side.svg", "Type 0 timber bench: side view", b, int(Y(t) + 140), int(h_front))

    # top view (plan of the frame under the top, with the machine footprint dashed)
    S2 = 0.5; ox3, oy3 = 60, 60 + t * S2
    X3 = lambda x: ox3 + x * S2; Y3 = lambda y: oy3 - y * S2
    b = rect(X3(0), Y3(t), X3(t), Y3(0), "#f6ecd8", 0.5, dash="4 3")
    for n, g, x0, x1, y0, y1, z0, z1 in P:
        if g in ("leg", "apron", "joist"):
            b += rect(X3(x0), Y3(y1), X3(x1), Y3(y0), COL[g], 0.95)
    if machine:
        for n, x0, x1, y0, y1, c, op in machine["plan"]:
            b += rect(X3(x0), Y3(y1), X3(x1), Y3(y0), c, op, dash="5 3" if "enclosure" in n else "")
            b += text(X3((x0+x1)/2), Y3(y1) + 12, n, sz=9, c="#555")
    sx0, sx1, sy0, sy1 = B["slot"]
    b += rect(X3(sx0), Y3(sy1), X3(sx1), Y3(sy0), "#c0392b", 0.8)
    b += text(X3((sx0+sx1)/2), Y3(sy1) - 4, "slot", c="#c0392b", sz=10)
    b += text(X3(t/2), Y3(0) + 22, "front", sz=12)
    b += text(X3(t/2), Y3(t) - 6, "back (wall)", sz=12)
    for xc in B["joist_x"]:
        b += text(X3(xc), Y3(t/2), "joist", sz=9)
    svg("bench_top.svg", "Type 0 timber bench: plan (frame under the top, machine dashed)", b, int(X3(t) + 60), int(Y3(0) + 40))

# ---------------------------------------------------------------------------
# Machine placement (from type0_v2.py and enclosure.py, without needing CadQuery for the numbers)
# ---------------------------------------------------------------------------
def machine_on_bench():
    import type0_v2 as m
    P, D = m.P, m.D
    gs, gb, gf = 40, 80, 40; y_motor = 150; tE = 12
    ex0 = D["portal_x0"] - gs - tE; ex1 = max(D["portal_x1"], D["pickup_x"] + P["wheel_t"]/2) + gs + tE
    ey0 = D["spine_y0"] - y_motor - gf - tE; ey1 = D["foot_y1"] + gb + tE
    dx = B["top"]/2 - (ex0 + ex1)/2; dy = B["top"]/2 - (ey0 + ey1)/2       # centre the enclosure
    dz = B["top_z"] + P["h"]                                                # machine Z 0 = casting top
    bx = lambda x: x + dx; by = lambda y: y + dy; bz = lambda z: z + dz
    zp_top = D["nose_top"] + 30 + D["rail_z"]; ez1 = max(zp_top, D["nose_top"] + 282, D["beam_top"]) + 50 + tE
    plan = [("base spine", bx(-P["spine_w"]/2), bx(P["spine_w"]/2), by(D["spine_y0"]), by(D["spine_y1"]), "#c9c9c4", 0.6),
            ("base rear foot", bx(D["portal_x0"]), bx(D["leg_r_x1"]), by(D["foot_y0"]), by(D["foot_y1"]), "#c9c9c4", 0.6),
            ("enclosure", bx(ex0), bx(ex1), by(ey0), by(ey1), "none", 1.0)]
    front = [("base", bx(D["portal_x0"]), bx(D["leg_r_x1"]), bz(-P["h"]), bz(0), "#c9c9c4", 0.9),
             ("portal", bx(D["portal_x0"]), bx(D["portal_x1"]), bz(D["beam_bottom"]), bz(D["beam_top"]), "#c9c9c4", 0.9),
             ("leg L", bx(D["portal_x0"]), bx(D["open_x0"]), bz(0), bz(D["beam_bottom"]), "#c9c9c4", 0.9),
             ("leg R", bx(D["open_x1"]), bx(D["leg_r_x1"]), bz(0), bz(D["beam_bottom"]), "#c9c9c4", 0.9),
             ("table", bx(-P["table_x"]/2), bx(P["table_x"]/2), bz(P["block_h"]), bz(D["table_top_z"]), "#9fb6cc", 0.9),
             ("enclosure", bx(ex0), bx(ex1), bz(-P["h"]), bz(ez1), "none", 1.0)]
    side = [("base", by(D["spine_y0"]), by(D["foot_y1"]), bz(-P["h"]), bz(0), "#c9c9c4", 0.9),
            ("portal", by(D["portal_y0"]), by(D["portal_y1"]), bz(0), bz(D["beam_top"]), "#c9c9c4", 0.9),
            ("enclosure", by(ey0), by(ey1), bz(-P["h"]), bz(ez1), "none", 1.0)]
    return dict(dx=dx, dy=dy, dz=dz, plan=plan, front=front, side=side, top_z=B["top_z"],
                enc=(bx(ex0), bx(ex1), by(ey0), by(ey1)), table_top=bz(D["table_top_z"]),
                base=(bx(D["portal_x0"]), bx(D["leg_r_x1"]), by(D["spine_y0"]), by(D["foot_y1"])))

# ---------------------------------------------------------------------------
def write_cutlist(mach):
    items = cut_items(); bars = nest_timber(items); sp = sheet_parts(); sheets = nest_sheets(sp); lc = load_check()
    L = ["# Timber bench (task 3, D-97): cut list, materials and assembly", "",
         "Generated by `cad/v2/bench.py`. Drawings: `bench_front.svg`, `bench_side.svg`, `bench_top.svg`. "
         "3D: `bench.step`, and `type0_v2_on_bench.step` (machine + enclosure on the bench).", "",
         "## Overall", "",
         f"- Top **{t} × {t} mm**, 2 × 18 mm plywood glued and screwed (36 mm). Top surface **{B['top_z']} mm** above the floor, so the machine table is at **{mach['table_top']:.0f} mm** (D-49).",
         f"- Frame **{t - 2*i0} × {t - 2*i0} mm**, set in {i0} mm from the top edge. Legs 76 × 89 (2 × CLS 38 × 89 glued), **{leg_len:.0f} mm** long.",
         f"- Feet: the 4 T02 levelling feet (M10) under the legs, in M10 threaded inserts. Leg length assumes **{B['foot_h']} mm** from the floor to the leg bottom with the feet screwed in part way: **CHECK when the feet arrive** and cut the legs to {B['top_z']} − 36 − (foot height).",
         f"- Lower shelf: 18 mm plywood, top at **{B['shelf_top']} mm**, on the front and back rails. Full depth, {B['top'] - 2*i0 - 2*lw} mm wide between the legs.",
         f"- Cabinet (E12, 600 × 400 × 200) front-left, standing on two 38 × 89 stands on the shelf: bottom at **{cab_z0:.0f} mm**, top at {cab_z0+chh:.0f} mm, door flush with the front. Held at the top by 2 steel angle brackets to the front apron.",
         "- Right-hand bay: radiator with its 2 fans on the inside of the right side panel, blowing out through 2 holes. Reservoir and pump on the shelf below it, at the back.",
         "- PC on the shelf at the back, centre. Tool tray on the shelf behind the cabinet.",
         "- Back panel (18 mm) and both side panels (12 mm) screwed on: they stop the frame racking. The front stays open.",
         f"- Cable and hose grommet through the top (T15, {B['slot'][1]-B['slot'][0]} × {B['slot'][3]-B['slot'][2]} mm outside, with lid and brush), {B['slot'][0]}–{B['slot'][1]} mm from the left edge and {B['slot'][2]}–{B['slot'][3]} mm from the front: inside the enclosure, right of the base and behind the tool-wheel position. It drops into the right-hand bay above the reservoir, so any coolant drip lands there, not on the cabinet. Cut the hole to the grommet's own cut-out size (CHECK).",
         "- Front e-stop (D-91) on the front apron, right-hand end.",
         f"- Machine position: base casting {mach['base'][0]:.0f}–{mach['base'][1]:.0f} mm from the left edge, {mach['base'][2]:.0f}–{mach['base'][3]:.0f} mm from the front. Enclosure {mach['enc'][0]:.0f}–{mach['enc'][1]:.0f} × {mach['enc'][2]:.0f}–{mach['enc'][3]:.0f} (centred on the top). The two joists sit under the edges of the base spine.",
         "", "## Knock-down for the move (all pieces under 40 kg)", "",
         "| Piece | About kg |", "|---|---|"]
    rho_ply, rho_c16 = 560, 470
    def kg(names):
        return sum((p[3]-p[2])*(p[5]-p[4])*(p[7]-p[6]) for p in boxes() if any(p[0].startswith(n) for n in names)) * 1e-9
    L += [f"| Top (2 layers glued, one piece) | {kg(['Top layer']) * rho_ply:.0f} |",
          f"| Left side frame (2 legs + apron + rail, glued) + side panel | {kg(['Leg L', 'Side apron L', 'Side rail L']) * rho_c16 + kg(['Side panel L']) * rho_ply:.0f} |",
          f"| Right side frame + side panel | {kg(['Leg R', 'Side apron R', 'Side rail R']) * rho_c16 + kg(['Side panel R']) * rho_ply:.0f} |",
          f"| Front and back aprons, front and back rails (4 loose pieces, bolted) | {kg(['Front apron', 'Back apron', 'Front rail', 'Back rail']) * rho_c16:.0f} total |",
          f"| Joists (2 doubled, bolted to the aprons) | {kg(['Joist']) * rho_c16:.0f} total |",
          f"| Shelf | {kg(['Shelf']) * rho_ply:.0f} |",
          f"| Back panel | {kg(['Back panel']) * rho_ply:.0f} |",
          "", "The side frames are glued; everything else is bolted or screwed so it comes apart with a spanner and a screwdriver.",
          "", "## Timber cut list", "",
          "| Stock | Part | Length (mm) | Qty |", "|---|---|---|---|"]
    for s, part, ln, q in items:
        L.append(f"| {s} | {part} | {ln:.0f} | {q} |")
    L += ["", "### Cutting plan (2.4 m lengths, 4 mm saw cut allowed)", ""]
    for stock, bs in bars.items():
        L.append(f"**{stock} × 2.4 m: {len(bs)} lengths**")
        L.append("")
        for k, bb in enumerate(bs):
            cuts = " + ".join(f"{ln:.0f}" for ln, _ in bb["cuts"])
            L.append(f"- Length {k+1}: {cuts} (offcut {B['timber_len'] - bb['used']:.0f})")
        L.append("")
    L += ["## Sheet cut list", "", "| Stock | Part | Size (mm) |", "|---|---|---|"]
    for s, n, a, b in sp:
        L.append(f"| {s} | {n} | {a:.0f} × {b:.0f} |")
    L += ["", "### Sheet layout (2440 × 1220)", ""]
    for stock, shs in sheets.items():
        L.append(f"**{stock}: {len(shs)} sheet{'s' if len(shs) > 1 else ''}**")
        L.append("")
        for k, sh in enumerate(shs):
            parts = "; ".join(f"{n} {w:.0f} × {h:.0f} at ({x:.0f}, {y:.0f})" for st in sh["strips"] for n, w, h, x, y in st["parts"])
            L.append(f"- Sheet {k+1}: {parts}")
        L.append("")
    L += ["Offcuts: about 1220 × 440 from the top sheet (spares).", "",
          "### B&Q in-store cutting (first 5 cuts free, then 50p each; pieces at least 500 × 230 mm)", "",
          "- 18 mm sheet 1 (top): rip the full length at 1000 (1 cut), then cross-cut at 1000 and 2000 (2 cuts) → 2 × 1000 × 1000. **3 cuts.** The rip leaves a 220 mm strip, under B&Q's 230 mm minimum: if they won't cut it, ask for a 1000 + 220 split anyway or rip it at home.",
          "- 18 mm sheet 2: cross-cut at 960 and 1920 (2 cuts), rip one 960 piece to 808 (shelf) and the other to 719 (back panel) (2 cuts). **4 cuts.**",
          "- 12 mm sheet: cross-cut at 960 and 1920 (2 cuts), rip both to 719 (2 cuts). **4 cuts.**",
          "- **11 cuts: 5 free + 6 × 50p = £3.00.** Everything then fits in the car. The CLS is cut at home (B&Q's saw doesn't do strip timber).", "",
          "## Materials and hardware (to price: price-check-task-11.md)", "",
          "| BOM | Item | Qty | Where (preference) |", "|---|---|---|---|"]
    for row in HARDWARE:
        L.append("| " + " | ".join(row) + " |")
    L += ["", "## Load check (hand calculation)", "",
          f"- Design load {lc['total_kg']} kg: castings 106 + motion and spindle about 25 + enclosure about 35 + 50 for tools and leaning.",
          f"- Worst case: 70% through the two doubled-38 × 89 joists, as one point load of {lc['P']:.0f} N at the middle of each {lc['span']:.0f} mm span (really the spine spreads it along the joist).",
          f"- Joist deflection **{lc['defl']:.2f} mm**, bending stress **{lc['stress']:.1f} N/mm²** against {lc['f_m']:.0f} for C16 (about {lc['f_m']/lc['stress']:.0f}× margin). The 36 mm top shares the load too, so the real figures are lower.",
          f"- Leg compression {lc['leg_stress']:.2f} N/mm² (C16 allows about 17): trivial.",
          "- Deflection of the bench doesn't affect accuracy: the base casting is far stiffer and is levelled once on the feet. What matters is that the bench doesn't rock or rack: hence the glued side frames, the back and side panels, and the feet.",
          "", "## Assembly", "",
          "1. **Legs:** glue 2 × 38 × 89 face to face (PVA + 5 × 70 screws every 150 mm, staggered, from the inside face). Clamp until dry. Cut to length **after** the glue sets, square both ends.",
          "2. **Feet:** drill the leg bottoms centrally and fit the M10 threaded inserts. Screw the T02 feet in part way.",
          "3. **Side frames:** glue and screw the side apron (top flush with the leg tops) and the side rail between each pair of legs, outer faces flush. Check square by measuring the diagonals.",
          "4. **Bolt holes:** for each front/back apron and rail: drill an 8.5 mm hole through the leg, into the end of the apron or rail (2 per apron end, 1 per rail end), and a 10 mm hole from the inside face of the apron/rail for the cross-dowel nut, about 30 mm from its end (the M8 × 120 bolt passes 76 mm of leg, so about 40 mm reaches into the apron: mark the nut position from the actual bolt). Washer under each bolt head. Check the barrel nuts are 10 mm diameter before drilling.",
          "5. **Stand the frame:** bolt the front and back aprons and rails between the two side frames. Check the diagonals on the top (equal within 2 mm) before tightening.",
          "6. **Joists:** glue and screw each joist pair. Fit them between the front and back aprons, tops flush with the apron tops, and bolt each end through the apron with 2 M8 × 120 bolts (one into each lamination) and cross-dowel nuts about 65 mm from the joist end (bolt through 38 mm of apron, about 80 mm into the joist). 8 bolts in all. Each joist end carries about 0.75 kN; two M8 bolts in C16 hold several times that.",
          "7. **Panels:** screw the back panel (18 mm) to the back legs, apron and rail. Cut the 2 fan holes (Ø 110, centres in `bench_front.svg` / radiator position) in the right side panel, fit the finger guards, screw both side panels on. Screws every 150 mm: the panels are what stops racking.",
          "8. **Shelf:** drop it in on the front and back rails, screw down with 4 screws (removable).",
          "9. **Top:** glue and screw the 2 ply layers together (4 × 30 screws from below on a 150 mm grid, glue spread all over). Cut the grommet hole. Seal all faces and edges with 3 coats of yacht varnish (coolant and shed damp). Lay the top on the frame and fix it from below with 8 corner braces into the aprons.",
          "10. **Level:** put the bench in place, level the top both ways with the feet (the 200 mm level, X02), lock the foot nuts.",
          "11. **Fit-out:** cabinet stands + cabinet + top brackets, radiator battens + radiator, reservoir, PC, cable grommet in the top, e-stop on the front apron.",
          "", "## CHECK items", "",
          "- T02 foot height (sets the leg length).",
          "- RS PRO cabinet mounting: it stands on the 2 stands; confirm its lugs/brackets for the 2 angle brackets at the top.",
          "- Reservoir size (not yet chosen) fits the right-hand bay at the back: about 160 wide × 300 deep × 200 high drawn.",
          "- Radiator and fan sizes from the S05 parts when they arrive: fan hole positions.",
          "- Bolt length: CLS is 38 × 89 planed; check the legs are 76 thick after gluing; adjust the cross-dowel position to the bolt length.",
          "- Barrel nuts (AliExpress, M8 × 15): confirm 10 mm diameter before drilling.",
          "- Grommet cut-out size (T15) before cutting the hole in the top.",
          ]
    (OUT / "bench_cutlist.md").write_text("\n".join(L) + "\n")
    return bars, sheets, lc

HARDWARE = [   # price check 11 (2026-11-08), D-99
    ("T03", "CLS 38 × 89 × 2.4 m, planed C16", "6 lengths", "B&Q Swansea, £6.65 each = £39.90"),
    ("T04", "CLS 38 × 63 × 2.4 m, planed C16", "2 lengths", "B&Q Swansea, £3.97 each = £7.94"),
    ("T05", "Hardwood plywood 18 mm 2440 × 1220 (BB/CC, structural use)", "2 sheets", "B&Q Swansea, £35.80 each = £71.60, cut in store"),
    ("T06", "Hardwood plywood 12 mm 2440 × 1220", "1 sheet", "B&Q Swansea, £27.65, cut in store"),
    ("T07", "M8 × 120 hex bolts + nuts (2 × 10), M8 washers (20), M8 × 15 barrel nuts (2 × 10)", "20 sets: 12 frame joints + 8 joist ends", "B&Q bolts + washers, AliExpress barrel nuts = £28.59"),
    ("T09", "M10 × 24 hex-drive threaded inserts, stainless", "4", "AliExpress, £10.56"),
    ("T10", "Corner braces 52 × 52 (top to aprons, 10-pack) + Expamet HD 90 × 59 × 90 (cabinet top)", "8 + 2", "Screwfix £2.48 + B&Q £5.00 = £7.48"),
    ("T11", "Goldscrew 5 × 70 (100), 4 × 30 (200); Silverscrew 4 × 40 (200)", "3 boxes", "Screwfix, £10.47"),
    ("T12", "D4 PVA wood glue 1 L", "1", "B&Q marketplace (delivered), £11.99"),
    ("T13", "Yacht varnish 750 ml", "1", "Screwfix, £11.99"),
    ("T14", "120 mm fan grills", "2", "AliExpress (wave 1), £6.81"),
    ("T15", "Metal desk cable grommet 80 × 160 with lid and brush", "1", "B&Q marketplace (delivered), £11.04"),
]

def build_step(mach):
    import cadquery as cq
    asm = cq.Assembly(); bench = cq.Assembly()
    def box(x0, x1, y0, y1, z0, z1):
        return cq.Workplane("XY").box(x1-x0, y1-y0, z1-z0, centered=False).translate((x0, y0, z0))
    wood = cq.Color(0.85, 0.7, 0.45); ply = cq.Color(0.92, 0.82, 0.62)
    for n, g, *c in boxes():
        shp = box(*c)
        if n.startswith("Top layer 2"):
            sx0, sx1, sy0, sy1 = B["slot"]
            shp = shp.cut(box(sx0, sx1, sy0, sy1, frame_top - 1, B["top_z"] + 1))
        if n.startswith("Top layer 1"):
            sx0, sx1, sy0, sy1 = B["slot"]
            shp = shp.cut(box(sx0, sx1, sy0, sy1, frame_top - 1, B["top_z"] + 1))
        bench.add(shp, name=n.replace(" ", "_").replace("(", "").replace(")", ""), color=ply if g.startswith("sheet") else wood)
    for n, c, *cc in equipment():
        bench.add(box(*cc), name="equip_" + n.split(" ")[0], color=cq.Color(0.5, 0.55, 0.6, 0.6))
    bench.save(str(OUT / "bench.step"))
    # machine + enclosure on the bench (machine coordinates moved into bench coordinates)
    import type0_v2 as m, enclosure as e
    loc = cq.Location(cq.Vector(mach["dx"], mach["dy"], mach["dz"]))
    full = cq.Assembly()
    full.add(bench, name="bench")
    mach_asm = cq.Assembly()
    for k, v in m.build().items(): mach_asm.add(v, name=k)
    parts, _ = e.model()
    for k, v in parts.items(): mach_asm.add(v, name="encl_" + k, color=cq.Color(0.85, 0.72, 0.54, 0.35))
    full.add(mach_asm, name="machine", loc=loc)
    full.save(str(OUT / "type0_v2_on_bench.step"))

if __name__ == "__main__":
    mach = machine_on_bench()
    views(mach)
    bars, sheets, lc = write_cutlist(mach)
    if "--no-step" not in sys.argv:
        build_step(mach)
    print({k: len(v) for k, v in bars.items()}, {k: len(v) for k, v in sheets.items()},
          f"joist defl {lc['defl']:.2f} mm, stress {lc['stress']:.1f}", f"table top {mach['table_top']:.0f}",
          f"base x {mach['base'][0]:.0f}-{mach['base'][1]:.0f} y {mach['base'][2]:.0f}-{mach['base'][3]:.0f}",
          f"enc {[round(v) for v in mach['enc']]}")

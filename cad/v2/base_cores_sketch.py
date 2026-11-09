"""Sketch: PVC cores for the base casting (proposal, not yet in assembly.py).

Run: python cad/v2/base_cores_sketch.py -> cad/v2/out/base_cores_plan.svg/.png, base_cores_sections.svg/.png
Numbers come from assembly.py so the cores are drawn against the real cast-in features.
"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import assembly as a

P, D, L = a.P, a.D, a.L
OUT = pathlib.Path(__file__).parent / "out"
h, sw = P["h"], P["spine_w"]

# ---- proposed cores (Ø, axis Z, and the runs) -------------------------------------------------
CORE_D, CORE_Z = 50.0, -65.0
SPINE_CORES_X = (-85.0, 0.0, 85.0)                     # 3 runs along Y in the spine
SPINE_Y = (-330.0, 60.0)                               # solid ends: BK + Y motor inserts at the front, tapers at the back
FOOT_CORES_Y = (150.0, 250.0)                          # 2 runs along X in the rear foot
FOOT_X = (-240.0, 240.0)                               # solid under the portal legs and their joint bars
RHO = 2300e-9

def mass_saved():
    area = math.pi * CORE_D ** 2 / 4
    ln = len(SPINE_CORES_X) * (SPINE_Y[1] - SPINE_Y[0]) + len(FOOT_CORES_Y) * (FOOT_X[1] - FOOT_X[0])
    return area * ln * RHO, ln

# ---- drawing helpers -------------------------------------------------------------------------
def rect(x0, y0, x1, y1, fill, op=1.0, sw_=0.8, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{min(x0,x1):.1f}" y="{min(y0,y1):.1f}" width="{abs(x1-x0):.1f}" height="{abs(y1-y0):.1f}" '
            f'fill="{fill}" fill-opacity="{op}" stroke="#333" stroke-width="{sw_}"{d}/>')
def circ(x, y, r, fill, op=1.0):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" fill-opacity="{op}" stroke="#333" stroke-width="0.8"/>'
def poly(pts, fill, op=1.0):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" fill-opacity="{op}" stroke="#333" stroke-width="0.8"/>'
def text(x, y, s, anchor="middle", c="#222", sz=11, w="normal"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{sz}" fill="{c}" font-weight="{w}">{s}</text>'
def page(name, title, body, w, hgt):
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {hgt}" font-family="Helvetica, Arial, sans-serif">'
                            f'<rect width="{w}" height="{hgt}" fill="#fff"/>{text(w/2, 26, title, sz=17, w="bold")}{body}</svg>')

EG, STEEL, CORE, CHAN, NOTE = "#d6d3cc", "#7d8794", "#f2b134", "#ffffff", "#c0392b"

def plan():
    S = 0.95; ox, oy = 70 - D["portal_x0"] * S, 70 + D["foot_y1"] * S
    X = lambda x: ox + x * S; Y = lambda y: oy - y * S
    b = ""
    # outline: spine + rear foot + tapers
    b += rect(X(-sw/2), Y(D["foot_y1"]), X(sw/2), Y(D["spine_y0"]), EG)
    b += rect(X(D["portal_x0"]), Y(D["foot_y1"]), X(D["leg_r_x1"]), Y(D["foot_y0"]), EG)
    tp, fy = L["base_taper"], D["foot_y0"]
    for sx in (-1, 1):
        b += poly([(X(sx*sw/2), Y(fy)), (X(sx*(sw/2+tp)), Y(fy)), (X(sx*sw/2), Y(fy-tp))], EG)
    # portal leg footprints (dashed) on the foot
    for lx0, lx1 in ((D["portal_x0"], D["open_x0"]), (D["open_x1"], D["leg_r_x1"])):
        b += rect(X(lx0), Y(D["portal_y1"]), X(lx1), Y(D["portal_y0"]), "none", 1, 1.2, "6 3")
    b += text(X(D["leg_r_x1"] - 35), Y(D["portal_y1"]) - 5, "portal leg", sz=9, c="#555")
    # Y rail bars, channel, BK/BF plates
    y0, y1 = L["y_rail_y0"], L["y_rail_y0"] + L["y_rail_len"]
    for x in (-L["y_rail_x"], L["y_rail_x"]):
        b += rect(X(x - 20), Y(y1), X(x + 20), Y(y0), STEEL, 0.45)
    b += rect(X(-L["y_chan_w"]/2), Y(L["y_bf_y0"] + BF_L + 15), X(L["y_chan_w"]/2), Y(D["spine_y0"]), CHAN, 0.9, dash="4 2")
    for yy in (L["y_bk_y0"] + 12.5, L["y_bf_y0"] + 10):
        b += rect(X(-30), Y(yy + 15), X(30), Y(yy - 15), STEEL, 0.9)
    # portal joint bars + holes
    for xc in (D["portal_x0"] + 35, D["leg_r_x1"] - 35):
        b += rect(X(xc - 20), Y(D["portal_y1"] - 5), X(xc + 20), Y(D["portal_y0"] + 5), STEEL, 0.9)
        for yy in (D["portal_y0"] + 30, D["portal_y1"] - 30):
            b += circ(X(xc), Y(yy), 6.5 * S, "#fff")
        b += circ(X(xc), Y((D["portal_y0"] + D["portal_y1"]) / 2), 6 * S, "#fff")
    # lifting points and Y motor inserts (side faces)
    for sx in (-1, 1):
        for yy in (D["spine_y0"] + 120, D["foot_y0"] - L["base_taper"] - 40):
            b += rect(X(sx * sw/2 - (40 if sx > 0 else 0)), Y(yy + 6), X(sx * sw/2 + (0 if sx > 0 else 40)), Y(yy - 6), "#9b59b6", 0.8)
    for yy in (L["y_bk_y0"] + 15, L["y_bk_y0"] + 55):
        b += rect(X(sw/2 - 30), Y(yy + 10), X(sw/2), Y(yy - 10), "#9b59b6", 0.8)
    # cores
    for xc in SPINE_CORES_X:
        b += rect(X(xc - CORE_D/2), Y(SPINE_Y[1]), X(xc + CORE_D/2), Y(SPINE_Y[0]), CORE, 0.85)
    for yc in FOOT_CORES_Y:
        b += rect(X(FOOT_X[0]), Y(yc + CORE_D/2), X(FOOT_X[1]), Y(yc - CORE_D/2), CORE, 0.85)
    # labels and dims
    b += text(X(0), Y(SPINE_Y[0]) + 16, f"3 x Ø{CORE_D:.0f} cores, Y {SPINE_Y[0]:.0f} to {SPINE_Y[1]:.0f}", sz=11, c="#9a6400", w="bold")
    b += text(X(0), Y(FOOT_CORES_Y[1]) - 30, f"2 x Ø{CORE_D:.0f} cores, X {FOOT_X[0]:.0f} to {FOOT_X[1]:.0f}", sz=11, c="#9a6400", w="bold")
    b += text(X(-L["y_rail_x"]), Y(y0) + 14, "Y rail bar", sz=9, c="#444")
    b += text(X(0), Y(D["spine_y0"]) + 30, "screw channel", sz=9, c="#444")
    b += text(X(0), Y(L["y_bk_y0"] + 12.5) + 4, "BK12", sz=9, c="#fff")
    b += text(X(0), Y(L["y_bf_y0"] + 10) + 4, "BF12", sz=9, c="#fff")
    b += text(X(sw/2) + 6, Y(L["y_bk_y0"] + 35), "Y motor inserts", "start", "#6c3483", 9)
    b += text(X(-sw/2) - 6, Y(D["spine_y0"] + 120) + 4, "lifting point", "end", "#6c3483", 9)
    b += text(X(-sw/2) - 6, Y(D["foot_y0"] - L["base_taper"] - 40) + 4, "lifting point", "end", "#6c3483", 9)
    b += text(X(D["portal_x0"] + 35), Y(D["portal_y0"]) + 16, "joint bar + M12 + dowel", sz=9, c="#444")
    b += text(X(-sw/2 - 50), Y(fy - 20), "45° taper", "end", sz=9, c="#555")
    for xc in SPINE_CORES_X:
        b += f'<line x1="{X(xc)}" y1="{Y(SPINE_Y[0]) + 34}" x2="{X(xc)}" y2="{Y(SPINE_Y[0]) + 24}" stroke="{NOTE}"/>' + text(X(xc), Y(SPINE_Y[0]) + 46, f"X {xc:+.0f}", sz=9, c=NOTE)
    b += text(X(0), Y(D["spine_y0"]) + 70, "front", sz=12)
    b += f'<line x1="{X(D["portal_x0"])-10}" y1="{Y(-150)}" x2="{X(D["leg_r_x1"])+10}" y2="{Y(-150)}" stroke="{NOTE}" stroke-dasharray="10 4"/>'
    b += text(X(D["leg_r_x1"]) + 18, Y(-150) + 4, "A", "start", NOTE, 13, "bold")
    b += f'<line x1="{X(D["portal_x0"])-10}" y1="{Y(150)}" x2="{X(D["leg_r_x1"])+10}" y2="{Y(150)}" stroke="{NOTE}" stroke-dasharray="10 4"/>' + text(X(D["leg_r_x1"]) + 18, Y(150) + 4, "B", "start", NOTE, 13, "bold")
    b += f'<line x1="{X(85)}" y1="{Y(D["foot_y1"])-10}" x2="{X(85)}" y2="{Y(D["spine_y0"])+10}" stroke="{NOTE}" stroke-dasharray="10 4"/>' + text(X(85), Y(D["spine_y0"]) + 24, "C", sz=13, c=NOTE, w="bold")
    kg, ln = mass_saved()
    b += text(X(0), Y(D["spine_y0"]) + 100, f"Saves about {kg:.1f} kg ({ln/1000:.2f} m of Ø{CORE_D:.0f} pipe). Base {a_kg():.1f} → about {a_kg()-kg:.1f} kg.", sz=12, w="bold")
    page("base_cores_plan.svg", "Base: proposed PVC cores (plan, top face up)", b, int(X(D["leg_r_x1"]) + 140), int(Y(D["spine_y0"]) + 120))

BF_L = a.BF["l"]

def a_kg():
    import json
    return json.loads((a.OUT / "assembly_data.json").read_text())["kg"]["base_casting"]

def sections():
    S = 1.0; b = ""
    # A-A: across the spine at Y -150 (X horizontal, Z up)
    ox, oy = 90 + sw/2 * S + 40, 120
    X = lambda x: ox + x * S; Z = lambda z: oy - z * S
    b += text(X(0), oy - 40, "Section A-A (across the spine, Y -150)", sz=13, w="bold")
    b += rect(X(-sw/2), Z(0), X(sw/2), Z(-h), EG)
    b += rect(X(-L["y_chan_w"]/2), Z(0), X(L["y_chan_w"]/2), Z(-L["chan_depth"]), CHAN)
    for x in (-L["y_rail_x"], L["y_rail_x"]):
        b += rect(X(x - 15), Z(0), X(x + 15), Z(-L["seat_recess"]), "#cfe3f7")
        b += rect(X(x - 20), Z(-L["seat_recess"]), X(x + 20), Z(-L["seat_recess"] - 10), STEEL)
        b += rect(X(x - 10), Z(17.5), X(x + 10), Z(0), "#aab3bd")
    for xc in SPINE_CORES_X:
        b += circ(X(xc), Z(CORE_Z), CORE_D/2 * S, CORE)
        b += circ(X(xc), Z(CORE_Z), CORE_D/2 * S - 3, "#fff")
    b += f'<line x1="{X(sw/2)+12}" y1="{Z(-25)}" x2="{X(sw/2)+12}" y2="{Z(CORE_Z+CORE_D/2)}" stroke="{NOTE}"/>' + text(X(sw/2) + 16, Z(-32), "15 to BK/BF plates", "start", NOTE, 9)
    b += f'<line x1="{X(sw/2)+12}" y1="{Z(CORE_Z-CORE_D/2)}" x2="{X(sw/2)+12}" y2="{Z(-h)}" stroke="{NOTE}"/>' + text(X(sw/2) + 16, Z(-100), "20 bottom skin", "start", NOTE, 9)
    b += text(X(sw/2) + 16, Z(-65) + 4, f"Ø{CORE_D:.0f} at Z {CORE_Z:.0f}", "start", "#9a6400", 10, "bold")
    b += text(X(-sw/2) - 6, Z(-8), "rail bar", "end", "#444", 9)
    b += text(X(0), Z(-8) + 3, "channel", sz=9, c="#444")
    # B-B: across the rear foot at Y 200
    oyb = oy + h + 130; ox2 = 90 - D["portal_x0"] * S
    Xb = lambda x: ox2 + x * S; Zb = lambda z: oyb - z * S
    b += text(Xb(0), oyb - 40, "Section B-B (across the rear foot, Y 150, through the front foot core)", sz=13, w="bold")
    b += rect(Xb(D["portal_x0"]), Zb(0), Xb(D["leg_r_x1"]), Zb(-h), EG)
    for xc in (D["portal_x0"] + 35, D["leg_r_x1"] - 35):
        b += rect(Xb(xc - 20), Zb(-30), Xb(xc + 20), Zb(-40), STEEL)
        b += rect(Xb(xc - 6.5), Zb(0), Xb(xc + 6.5), Zb(-30), "#fff")
        b += rect(Xb(xc - 35), Zb(L["chan_depth"] * 0 + 375 * 0 + 60), Xb(xc + 35), Zb(0), "none", 1, 1, "6 3")
    b += text(Xb(D["portal_x0"] + 35), Zb(70), "portal leg", sz=9, c="#555")
    b += rect(Xb(FOOT_X[0]), Zb(CORE_Z + CORE_D/2), Xb(FOOT_X[1]), Zb(CORE_Z - CORE_D/2), CORE, 0.85)
    b += text(Xb(0), Zb(CORE_Z) + 4, f"core along X (Ø{CORE_D:.0f}), ends 25 from the joint bars", sz=10, c="#5a3d00")
    b += rect(Xb(-30), Zb(-15), Xb(30), Zb(-25), STEEL)
    b += text(Xb(0), Zb(-15) - 4, "BF12 plate (Y 120, just behind this cut)", sz=9, c="#444")
    # C-C: along the spine at X +85 (Y horizontal)
    oyc = oyb + h + 140; S3 = 0.9; ox3 = 90 - D["spine_y0"] * S3
    Yc = lambda y: ox3 + y * S3; Zc = lambda z: oyc - z * S3
    b += text(Yc((D["spine_y0"] + D["foot_y1"]) / 2), oyc - 40, "Section C-C (along the spine, X +85; front on the left)", sz=13, w="bold")
    b += rect(Yc(D["spine_y0"]), Zc(0), Yc(D["foot_y1"]), Zc(-h), EG)
    b += rect(Yc(SPINE_Y[0]), Zc(CORE_Z + CORE_D/2), Yc(SPINE_Y[1]), Zc(CORE_Z - CORE_D/2), CORE, 0.85)
    for yc in FOOT_CORES_Y:
        b += circ(Yc(yc), Zc(CORE_Z), CORE_D/2 * S3, CORE)
    b += text(Yc((SPINE_Y[0] + SPINE_Y[1]) / 2), Zc(CORE_Z) + 4, "spine core (capped both ends)", sz=10, c="#5a3d00")
    b += text(Yc(sum(FOOT_CORES_Y) / 2), Zc(-100) + 3, "foot cores", sz=9, c="#5a3d00")
    for yy in (SPINE_Y[0] - 40, -150, 0, SPINE_Y[1] - 20):
        b += f'<line x1="{Yc(yy)}" y1="{Zc(-h)}" x2="{Yc(yy)}" y2="{Zc(CORE_Z - CORE_D/2)}" stroke="#555" stroke-width="2"/>' if SPINE_Y[0] < yy < SPINE_Y[1] else ""
    b += text(Yc(-150), Zc(-h) + 16, "hold-down straps from the open (bottom) face, every 250 mm", sz=9, c="#555")
    b += text(Yc(D["spine_y0"]) + 4, Zc(-h) + 30, "base is cast upside down: Z 0 on the mould floor, Z -110 is the open face", "start", "#555", 9)
    page("base_cores_sections.svg", "Base cores: sections", b, int(max(Yc(D["foot_y1"]), Xb(D["leg_r_x1"])) + 170), int(Zc(-h) + 60))

if __name__ == "__main__":
    plan(); sections()
    kg, ln = mass_saved()
    print(f"cores {ln:.0f} mm of Ø{CORE_D:.0f}, saves {kg:.1f} kg")

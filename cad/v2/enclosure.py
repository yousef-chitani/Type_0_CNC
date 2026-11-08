"""Type 0 v2 enclosure (D-87): 12 mm MDF box on the bench around the machine, top-hinged front door with window.

Run: python cad/v2/enclosure.py -> cad/v2/out/enclosure.step, enclosure_front.svg, enclosure_side.svg, enclosure_cutlist.md
Coordinates as type0_v2.py (Z = 0 = top of the castings, bench top at Z = -h).
"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
import type0_v2 as m

P, D, OUT = m.P, m.D, m.OUT
E = dict(t=12, gap_side=40, gap_back=80, gap_front=40, gap_top=50,
         y_motor_len=150,            # Y motor + coupling + BK12 in front of the spine
         spindle_total=282,          # G-Penny 230 body + 52 nose
         fixed_front_strip=120,      # fixed panel below the door
         window_w=560, window_h=380, # from the 610 x 610 twinwall sheet
         sheet=(2440, 1220))

def extents():
    zp_top = D["nose_top"] + 30 + D["rail_z"]                 # Z plate top at Z-top
    sp_top = D["nose_top"] + E["spindle_total"]
    x0 = D["portal_x0"] - E["gap_side"]
    x1 = max(D["portal_x1"], D["pickup_x"] + P["wheel_t"]/2) + E["gap_side"]
    y0 = D["spine_y0"] - E["y_motor_len"] - E["gap_front"]
    y1 = D["foot_y1"] + E["gap_back"]
    z0 = -P["h"]
    z1 = max(zp_top, sp_top, D["beam_top"]) + E["gap_top"]
    return dict(x0=x0, x1=x1, y0=y0, y1=y1, z0=z0, z1=z1,
                W=x1-x0, Dp=y1-y0, H=z1-z0)

X = extents(); t = E["t"]
iw, idp, ih = X["W"], X["Dp"], X["H"]                         # internal sizes
door_h = ih - E["fixed_front_strip"]
panels = {
    "Top": (iw + 2*t, idp + 2*t),
    "Back": (iw + 2*t, ih),
    "Side (×2)": (idp, ih),
    "Front fixed strip": (iw + 2*t, E["fixed_front_strip"]),
    "Door (top-hinged)": (iw + 2*t, door_h),
}

def model():
    def box(x0, x1, y0, y1, z0, z1):
        return cq.Workplane("XY").box(x1-x0, y1-y0, z1-z0, centered=False).translate((x0, y0, z0))
    x0, x1, y0, y1, z0, z1 = X["x0"], X["x1"], X["y0"], X["y1"], X["z0"], X["z1"]
    parts = {
        "top": box(x0-t, x1+t, y0-t, y1+t, z1, z1+t),
        "back": box(x0-t, x1+t, y1, y1+t, z0, z1),
        "side_l": box(x0-t, x0, y0, y1, z0, z1),
        "side_r": box(x1, x1+t, y0, y1, z0, z1),
        "front_strip": box(x0-t, x1+t, y0-t, y0, z0, z0+E["fixed_front_strip"]),
    }
    door = box(x0-t, x1+t, y0-t, y0, z0+E["fixed_front_strip"], z1)
    wx = (x0 + x1)/2; wz = z0 + E["fixed_front_strip"] + 30 + E["window_h"]/2   # low: table + spindle tip in view
    door = door.cut(box(wx-E["window_w"]/2, wx+E["window_w"]/2, y0-t-1, y0+1, wz-E["window_h"]/2, wz+E["window_h"]/2))
    parts["door"] = door
    return parts, (wx, wz)

def svg_views(win):
    S = 0.45
    def rect(x0, y0, x1, y1, fill, op=1.0, dash=""):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<rect x="{min(x0,x1):.1f}" y="{min(y0,y1):.1f}" width="{abs(x1-x0):.1f}" height="{abs(y1-y0):.1f}" fill="{fill}" fill-opacity="{op}" stroke="#333" stroke-width="0.8"{d}/>'
    def text(x, y, s, a="middle", c="#222", sz=11):
        return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{a}" font-size="{sz}" fill="{c}">{s}</text>'
    def page(name, title, body, w=900, h=640):
        (OUT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Helvetica, Arial, sans-serif"><rect width="{w}" height="{h}" fill="#fff"/><text x="{w/2}" y="26" text-anchor="middle" font-size="17" font-weight="bold">{title}</text>{body}</svg>')
    mdf, eg, alu, win_c = "#d9b98a", "#c9c9c4", "#9fb6cc", "#cfe6f5"
    # front view (X-Z)
    ox, oy = 450 - (X["x0"]+X["x1"])/2*S, 80 + X["z1"]*S + 10
    Xs = lambda x: ox + x*S; Zs = lambda z: oy - z*S
    b = rect(Xs(X["x0"]-t), Zs(X["z1"]+t), Xs(X["x1"]+t), Zs(X["z0"]), mdf, 0.25)
    b += rect(Xs(D["portal_x0"]), Zs(0), Xs(D["leg_r_x1"]), Zs(-P["h"]), eg)
    b += rect(Xs(D["portal_x0"]), Zs(D["beam_top"]), Xs(D["portal_x1"]), Zs(D["beam_bottom"]), eg)
    for xa, xb in ((D["portal_x0"], D["open_x0"]), (D["open_x1"], D["leg_r_x1"])):
        b += rect(Xs(xa), Zs(D["beam_bottom"]), Xs(xb), Zs(0), eg)
    b += rect(Xs(-P["table_x"]/2), Zs(D["table_top_z"]), Xs(P["table_x"]/2), Zs(P["block_h"]), alu)
    b += rect(Xs(-40), Zs(D["nose_top"]+E["spindle_total"]), Xs(40), Zs(D["nose_top"]), "#8e8e8e")
    b += rect(Xs(-70), Zs(D["nose_top"]+30+D["rail_z"]), Xs(70), Zs(D["nose_top"]+30), alu, 0.6)
    b += rect(Xs(win[0]-E["window_w"]/2), Zs(win[1]+E["window_h"]/2), Xs(win[0]+E["window_w"]/2), Zs(win[1]-E["window_h"]/2), win_c, 0.55)
    b += f'<line x1="{Xs(X["x0"]-t)}" y1="{Zs(X["z0"]+E["fixed_front_strip"])}" x2="{Xs(X["x1"]+t)}" y2="{Zs(X["z0"]+E["fixed_front_strip"])}" stroke="#7a4f1d" stroke-width="2"/>'
    b += text(Xs((X["x0"]+X["x1"])/2), Zs(X["z1"]+t)-8, f'outside {iw+2*t:.0f} W × {ih+t:.0f} H (on the bench)  ·  internal {iw:.0f} × {idp:.0f} × {ih:.0f}', c="#c0392b")
    b += text(Xs((X["x0"]+X["x1"])/2), Zs(win[1]+E["window_h"]/2)-6, f'window {E["window_w"]} × {E["window_h"]} (4 mm polycarbonate) in the top-hinged door', c="#2c5d8f")
    b += text(Xs((X["x0"]+X["x1"])/2), Zs(X["z0"])+18, f'fixed strip {E["fixed_front_strip"]} high · door {door_h:.0f} high, hinged along the top edge', c="#7a4f1d")
    page("enclosure_front.svg", "Type 0 v2 enclosure: front view", b, h=int(Zs(X["z0"]) + 60))
    # side view (Y-Z), front on the left
    ox2, oy2 = 420 - X["y0"]*S, oy
    Ys = lambda y: ox2 + y*S
    b = rect(Ys(X["y0"]-t), Zs(X["z1"]+t), Ys(X["y1"]+t), Zs(X["z0"]), mdf, 0.25)
    b += rect(Ys(D["spine_y0"]), Zs(0), Ys(D["foot_y1"]), Zs(-P["h"]), eg)
    b += rect(Ys(D["portal_y0"]), Zs(D["beam_top"]), Ys(D["portal_y1"]), Zs(0), eg)
    b += rect(Ys(D["spine_y0"]-E["y_motor_len"]), Zs(-20), Ys(D["spine_y0"]), Zs(-80), "#555")
    b += rect(Ys(-40), Zs(D["nose_top"]+E["spindle_total"]), Ys(40), Zs(D["nose_top"]), "#8e8e8e")
    hz = X["z1"]
    ey, ez = X["y0"]-t-door_h*0.87, hz-door_h*0.5
    b += f'<line x1="{Ys(X["y0"]-t):.1f}" y1="{Zs(hz):.1f}" x2="{Ys(ey):.1f}" y2="{Zs(ez):.1f}" stroke="#7a4f1d" stroke-width="3" stroke-dasharray="8 4"/>'
    b += f'<line x1="{Ys(X["y0"]-t):.1f}" y1="{Zs(hz):.1f}" x2="{Ys(X["y0"]-t):.1f}" y2="{Zs(X["z0"]+E["fixed_front_strip"]):.1f}" stroke="#7a4f1d" stroke-width="3"/>'
    b += text(Ys(ey)-4, Zs(ez)+16, "door open (about 60°)", "start", "#7a4f1d")
    b += text(Ys((X["y0"]+X["y1"])/2), Zs(X["z1"]+t)-8, f'depth {idp+2*t:.0f} outside', c="#c0392b")
    b += text(Ys(X["y1"]+t)+6, Zs(X["z0"]+60), "cable + hose slot", "start", "#555")
    b += text(Ys(X["y1"]+t)+6, Zs(X["z0"]+30), "(brush strip) to cabinet", "start", "#555")
    page("enclosure_side.svg", "Type 0 v2 enclosure: side view (front on the left)", b, w=1100, h=int(Zs(X["z0"]) + 60))

def cutlist():
    sw, sh = E["sheet"]
    area = sum(a*b*(2 if "×2" in k else 1) for k, (a, b) in panels.items()) / 1e6
    L = ["# Enclosure (D-87): cut list and notes", "", "Generated by `cad/v2/enclosure.py`.", "",
         f"**Internal:** {iw:.0f} W × {idp:.0f} D × {ih:.0f} H mm. **Outside:** {iw+2*t:.0f} × {idp+2*t:.0f} × {ih+t:.0f} mm (sits on the bench, no bottom panel).", "",
         "| Panel (12 mm MDF) | Size (mm) | Qty |", "|---|---|---|"]
    for k, (a, b) in panels.items():
        L.append(f"| {k.replace(' (×2)','')} | {a:.0f} × {b:.0f} | {2 if '×2' in k else 1} |")
    L += ["", f"Panel area about {area:.2f} m². One 2440 × 1220 sheet is {sw*sh/1e6:.2f} m², so **{math.ceil(area/(sw*sh/1e6)*1.15)} sheets** allowing about 15% for cutting.", "",
          f"**Window:** {E['window_w']} × {E['window_h']} cut-out in the door, covered by a 600 × 420 × 4 mm solid clear polycarbonate panel (D-88) screwed over it from inside with a foam or rubber seal strip.", "",
          "## Fittings (not yet priced)",
          "- Piano hinge, about the door width, along the top edge (door to top panel).",
          "- 2 gas struts (about 100–150 N each, sized for the door weight) or a fold-down stay to hold the door open.",
          "- Door handle and a magnetic catch.",
          "- Door interlock: the E15 switch (already in Phase 2), wired to stop the spindle when the door opens.",
          "- Cables and hoses leave through an 80 × 160 grommet in the bench top, right of the base, inside the enclosure (D-97, D-99): no slot in the back panel needed.",
          "- Seal the inside with 2–3 coats of varnish or paint (MDF swells with coolant mist). Silicone the inside corners.",
          "- Foam tape along the bottom edges to seal against the bench top.", "",
          "## Notes",
          "- The box does not touch the castings, so it carries no vibration and lifts off in one piece for moving (about 20–25 kg of MDF).",
          "- The spindle top at full Z sets the height. The tool wheel side sets the width.",
          "- Mist coolant (Phase 2): consider a small extraction outlet in the back panel later."]
    (OUT/"enclosure_cutlist.md").write_text("\n".join(L) + "\n")
    return area

if __name__ == "__main__":
    parts, win = model()
    asm = cq.Assembly()
    for k, v in m.build().items(): asm.add(v, name=k)
    for k, v in parts.items(): asm.add(v, name="encl_"+k, color=cq.Color(0.85, 0.72, 0.54, 0.35))
    asm.export(str(OUT/"type0_v2_with_enclosure.step"))
    svg_views(win)
    a = cutlist()
    print(f"internal {iw:.0f} x {idp:.0f} x {ih:.0f}, outside {iw+2*t:.0f} x {idp+2*t:.0f} x {ih+t:.0f}, door {door_h:.0f}, area {a:.2f} m2")

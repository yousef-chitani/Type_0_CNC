"""Type 0 v2: mould drawings for the base and portal castings (task 4, D-96).

Run: python cad/v2/moulds.py -> cad/v2/out/mould_base.svg, mould_portal.svg, mould_sheet.svg, moulds.md
All sizes come from type0_v2.py (P, D) plus the mould values in M below. Sizes marked VERIFY depend on
parts that arrive in wave 2 (rails, ballscrew kits): measure them and re-run before marking out the floors.

Base: cast UPSIDE DOWN, top face on the mould floor (it is symmetric left-right, so the floor drawing is
      the same as the machine top view).
Portal: cast lying on its FRONT face (X-rail face) on the floor. Standing over the mould you see the front
      face from behind, so the floor drawing is MIRRORED: machine +X (right, beam overhang) is on the LEFT.
"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import type0_v2 as m

P, D, OUT = m.P, m.D, m.OUT
M = dict(
    t=18,                  # MDF thickness (floors, walls)
    freeboard=20,          # wall height above the casting
    floor_margin=50,       # floor beyond the outside of the walls
    strip_t=4,             # raised strips on the floor = rail-seat recess depth (levelling pour)
    y_strip_w=44,          # Y rail strip (bar 40 + 2 each side)
    y_bar_out=10,          # rail hole to the bar's OUTER edge: bars offset inward so the spine edge keeps an 8 mm EG lip
    link_w=30,             # cross-link strip joining the two Y strips (same level for both rails)
    bar_w=40, bar_t=10,    # insert bars (F07, 40 x 10 flat bar)
    rail_pitch=60,         # HGR20 hole pitch, M5 (VERIFY on the rails)
    y_rail_len=500, x_rail_len=800,   # bought lengths (M01, M02)
    screw_ch_w=70, screw_ch_d=25, draft_deg=2,      # Y-screw channel (D-56)
    screw_ch_y1=150,       # rear end of the Y-screw channel (front end open). VERIFY with the M05 kit
    y_pad_front=(-340, -190), y_pad_rear=(50, 150),  # plain bars in the channel: motor mount + BK12 / BF12
    leg_bolt_x=285, leg_bolt_y=(145, 205),          # portal-to-base M12 studs (2 per leg)
    feet=((-120, -300), (120, -300), (-280, 280), (280, 280)),   # M10 levelling feet (T02) on the underside
    x_pocket=(233, 367),   # X rail-seat pocket (z), one recess for both rails and the screw end blocks
    x_bar_lo=(240, 280), x_bar_hi=(320, 360),       # X rail bars (z): rails at z 250 / 350, holes 10 from the bar edge
    x_bar_x=(-280, 440),   # X rail bars along x; crosswise end pads take the rail end holes + BK12 / BF12
    core_z=295, core_depth=72, core_x=(-260, 420),  # 68 mm downpipe in the beam (D-95)
    lift_x=(-285, 285), lift_depth=65,              # M12 lifting couplers in the beam top
    sleeve_d=20,           # 20 mm uPVC conduit (F09)
)

# ------------------------------------------------------------------------------------------- geometry
t, fb = M["t"], M["freeboard"]
h_base = P["h"]
rail_y_x = P["y_rail_spacing"] / 2
yr0, yr1 = -M["y_rail_len"] / 2, M["y_rail_len"] / 2
y_holes = [yr0 + 10 + M["rail_pitch"] * k for k in range(int((M["y_rail_len"] - 20) // M["rail_pitch"]) + 1)]
y_strip = (yr0 - 5, D["spine_y1"] + 25)                  # strips run past the rail ends to the cross-link
link_y = (y_strip[1] - M["link_w"], y_strip[1])
xr0 = D["portal_x0"]
x_holes = [xr0 + 10 + M["rail_pitch"] * k for k in range(int((M["x_rail_len"] - 20) // M["rail_pitch"]) + 1)]
spine = (-P["spine_w"] / 2, P["spine_w"] / 2, D["spine_y0"], D["foot_y1"])
cross = (D["portal_x0"], D["leg_r_x1"], D["foot_y0"], D["foot_y1"])
base_poly = [(spine[0], spine[2]), (spine[1], spine[2]), (spine[1], cross[2]), (cross[1], cross[2]),
             (cross[1], cross[3]), (cross[0], cross[3]), (cross[0], cross[2]), (spine[0], cross[2])]
portal_poly = [(D["portal_x0"], 0), (D["open_x0"], 0), (D["open_x0"], D["beam_bottom"]), (D["open_x1"], D["beam_bottom"]),
               (D["open_x1"], 0), (D["leg_r_x1"], 0), (D["leg_r_x1"], D["beam_bottom"]), (D["portal_x1"], D["beam_bottom"]),
               (D["portal_x1"], D["beam_top"]), (D["portal_x0"], D["beam_top"])]


def ybar(sx):
    """x extent of the Y rail bar on side sx (+1 right, -1 left): outer edge y_bar_out past the rail centre."""
    outer = sx * (rail_y_x + M["y_bar_out"])
    inner = outer - sx * M["bar_w"]
    return tuple(sorted((inner, outer)))


def perim(poly):
    return sum(math.dist(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))


def mid_anchors(holes, every=2):
    mids = [(a + b) / 2 for a, b in zip(holes, holes[1:])]
    return mids[::every]


# ------------------------------------------------------------------------------------------- tiny SVG writer
class Svg:
    def __init__(s, w, h, title):
        s.w, s.h, s.el = w, h, []
        s.text(10, 22, title, 15, bold=True)

    def add(s, e): s.el.append(e)

    def line(s, x0, y0, x1, y1, c="#000", w=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{c}" stroke-width="{w}"{d}/>')

    def rect(s, x0, y0, x1, y1, fill="none", c="#000", w=1, dash=None, op=1):
        x, y = min(x0, x1), min(y0, y1)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{abs(x1-x0):.1f}" height="{abs(y1-y0):.1f}" fill="{fill}" '
              f'fill-opacity="{op}" stroke="{c}" stroke-width="{w}"{d}/>')

    def poly(s, pts, fill="none", c="#000", w=1.5, op=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.add('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) +
              f'" fill="{fill}" fill-opacity="{op}" stroke="{c}" stroke-width="{w}"{d}/>')

    def circle(s, x, y, r, fill="none", c="#000", w=1):
        s.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{c}" stroke-width="{w}"/>')

    def text(s, x, y, txt, size=10, anchor="start", bold=False, c="#000", rot=0):
        b = ' font-weight="bold"' if bold else ""
        r = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot else ""
        txt = txt.replace("&", "&amp;").replace("<", "&lt;")
        s.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="sans-serif" font-size="{size}" text-anchor="{anchor}" fill="{c}"{b}{r}>{txt}</text>')

    def dim(s, x0, y0, x1, y1, label, off=14, size=9):
        """Aligned dimension between two points, offset to the left of the direction x0,y0 -> x1,y1."""
        L = math.dist((x0, y0), (x1, y1)) or 1
        nx, ny = -(y1 - y0) / L * off, (x1 - x0) / L * off
        a, b = (x0 + nx, y0 + ny), (x1 + nx, y1 + ny)
        s.line(x0, y0, a[0], a[1], "#777", 0.5); s.line(x1, y1, b[0], b[1], "#777", 0.5)
        s.line(*a, *b, "#c00", 0.7)
        for p, q in ((a, b), (b, a)):
            ux, uy = (q[0] - p[0]) / L * 5, (q[1] - p[1]) / L * 5
            s.line(p[0], p[1], p[0] + ux - uy * 0.4, p[1] + uy + ux * 0.4, "#c00", 0.7)
            s.line(p[0], p[1], p[0] + ux + uy * 0.4, p[1] + uy - ux * 0.4, "#c00", 0.7)
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        if ang > 90 or ang <= -90: ang += 180
        cx, cy = (a[0] + b[0]) / 2 + nx * 0.25, (a[1] + b[1]) / 2 + ny * 0.25
        s.text(cx, cy, label, size, "middle", c="#c00", rot=ang)

    def save(s, path):
        body = "\n".join(s.el)
        path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.w}" height="{s.h}" viewBox="0 0 {s.w} {s.h}">'
                        f'<rect width="100%" height="100%" fill="white"/>\n{body}\n</svg>\n')


C = dict(strip="#9ecae1", bar="#636363", pad="#bdbdbd", block="#fdd0a2", anchor="#d94801", sleeve="#31a354",
         reserve="#fcbba1", core="#c6dbef", plug="#e5f5e0", hole="#000")


def legend(s, x, y, items):
    for i, (col, txt) in enumerate(items):
        s.rect(x, y + i * 15, x + 12, y + i * 15 + 10, fill=col)
        s.text(x + 18, y + i * 15 + 9, txt, 9)


# ------------------------------------------------------------------------------------------- BASE
def draw_base():
    sc, ox, oy = 0.8, 430, 360            # plan: machine x -> right, machine y (back) -> down the page
    X = lambda x: ox + x * sc
    Y = lambda y: oy + y * sc
    s = Svg(1150, 1000, "BASE mould: floor plan (= base TOP face; cast upside down). Symmetric left-right. Scale 1:1.25")
    s.text(10, 40, "Front of machine at the TOP of the page. Walls 18 mm MDF outside the outline, "
                   f"{h_base + fb} mm tall (fill line {h_base} mm). Floor 18 mm MDF on CLS battens.", 10)
    # walls (outside the outline) + outline
    outer = [(x + (t if x > 0 else -t), y + (t if y > 0 else -t)) for x, y in base_poly]
    s.poly([(X(x), Y(y)) for x, y in outer], fill="#eee", c="#999", w=1)
    s.poly([(X(x), Y(y)) for x, y in base_poly], fill="white", w=2)
    # reserved relocation zones under the portal legs
    for sx in (-1, 1):
        x0, x1 = sorted((sx * D["open_x1"], sx * D["leg_r_x1"]))
        s.rect(X(x0), Y(D["portal_y0"]), X(x1), Y(D["portal_y1"]), fill=C["reserve"], c="#e34a33", dash="4,2", op=0.6)
    # strips + link
    for sx in (-1, 1):
        s.rect(X(ybar(sx)[0] - 2), Y(y_strip[0]), X(ybar(sx)[1] + 2), Y(y_strip[1]), fill=C["strip"])
    s.rect(X(ybar(-1)[0] - 2), Y(link_y[0]), X(ybar(1)[1] + 2), Y(link_y[1]), fill=C["strip"])
    # Y-screw channel block + pads
    s.rect(X(-M["screw_ch_w"] / 2), Y(spine[2]), X(M["screw_ch_w"] / 2), Y(M["screw_ch_y1"]), fill=C["block"])
    for a, b in (M["y_pad_front"], M["y_pad_rear"]):
        s.rect(X(-M["bar_w"] / 2), Y(a), X(M["bar_w"] / 2), Y(b), fill=C["pad"])
    # rail bars, holes, anchors
    for sx in (-1, 1):
        cx = sx * rail_y_x
        s.rect(X(ybar(sx)[0]), Y(yr0), X(ybar(sx)[1]), Y(yr1), fill=C["bar"], op=0.5)
        for hy in y_holes: s.circle(X(cx), Y(hy), 2.2, fill=C["hole"])
        for ay in mid_anchors(y_holes): s.line(X(cx - 6), Y(ay), X(cx + 6), Y(ay), C["anchor"], 2)
    # sleeves for the portal studs, feet anchors
    for sx in (-1, 1):
        for by in M["leg_bolt_y"]: s.circle(X(sx * M["leg_bolt_x"]), Y(by), M["sleeve_d"] / 2 * sc, fill=C["sleeve"])
    for fx, fy in M["feet"]:
        s.circle(X(fx), Y(fy), 8 * sc, c=C["anchor"], w=1.5); s.line(X(fx) - 6, Y(fy), X(fx) + 6, Y(fy), C["anchor"])
    # dimensions
    s.dim(X(spine[0]), Y(spine[2]), X(spine[1]), Y(spine[2]), f"spine {P['spine_w']:.0f}", 22)
    s.dim(X(cross[0]), Y(cross[3]), X(cross[1]), Y(cross[3]), f"{cross[1]-cross[0]:.0f}", -22)
    s.dim(X(spine[1]), Y(spine[2]), X(spine[1]), Y(cross[3]), f"{cross[3]-spine[2]:.0f}", -60)
    s.dim(X(cross[1]), Y(cross[2]), X(cross[1]), Y(cross[3]), f"{cross[3]-cross[2]:.0f}", -22)
    s.dim(X(-rail_y_x), Y(-200), X(rail_y_x), Y(-200), f"Y rails {P['y_rail_spacing']} c/c", 12)
    s.dim(X(-rail_y_x - 50), Y(yr0), X(-rail_y_x - 50), Y(yr1), f"bar {M['y_rail_len']} (holes {y_holes[0]:.0f}..{y_holes[-1]:+.0f} @ {M['rail_pitch']})", 18)
    s.dim(X(-M["screw_ch_w"] / 2), Y(-20), X(M["screw_ch_w"] / 2), Y(-20), f"{M['screw_ch_w']}", 10)
    s.dim(X(60), Y(spine[2]), X(60), Y(M["screw_ch_y1"]), f"screw channel to y {M['screw_ch_y1']:+.0f}", -10)
    s.dim(X(M["leg_bolt_x"]), Y(M["leg_bolt_y"][0]), X(M["leg_bolt_x"]), Y(M["leg_bolt_y"][1]), f"{M['leg_bolt_y'][1]-M['leg_bolt_y'][0]}", -16)
    s.dim(X(-M["leg_bolt_x"]), Y(M["leg_bolt_y"][1] + 25), X(M["leg_bolt_x"]), Y(M["leg_bolt_y"][1] + 25), f"studs {2*M['leg_bolt_x']} c/c", -8)
    s.text(X(0), Y(spine[2]) - 30, "FRONT (machine -Y)", 11, "middle", True)
    s.text(X(0), Y(0) + 4, "+ origin (spindle line)", 8, "middle")
    s.text(X(D["leg_r_x1"]) - 2, Y(D["portal_y0"]) - 4, "portal leg: RESERVED for relocation feature (TBD)", 8, "end", c="#b30000")
    legend(s, 860, 70, [(C["strip"], f"raised strip {M['strip_t']} mm (rail-seat recess)"),
                        (C["bar"], "insert bar 40x10, M5 tapped (VERIFY)"),
                        (C["pad"], "plain bar 40x10 (drill+tap later)"),
                        (C["block"], f"Y-screw channel block {M['screw_ch_w']}x{M['screw_ch_d']}, {M['draft_deg']} deg draft"),
                        (C["sleeve"], "20 mm conduit sleeve (portal stud)"),
                        (C["anchor"], "M6 anchor on bar back / M10 foot anchor (top)"),
                        (C["reserve"], "reserved: relocation (open question)")])
    # notes
    notes = ["Y bars sit off-centre: rail holes 10 mm from the bar's OUTER edge, leaving an 8 mm lip to the spine edge.",
             f"Holes: M5 rail holes, jig bolt M5 x 30 waxed through the floor + strip into each. {len(y_holes)} per bar.",
             "Strips: 4 mm hardboard, glued + pinned, edges taped. Link strip at the rear joins both recesses.",
             f"Sleeves: 20 mm conduit, {h_base} long, on a waxed M12 rod through the floor and a top batten.",
             "Feet: 4 x M10 coupling nut + 50 mm rod + washer, hung from a batten on the OPEN face (underside).",
             "Probes: DS18B20 at mid-depth in the spine centre and 10 mm below the open face."]
    for i, n in enumerate(notes): s.text(20, 890 + i * 14, n, 9)
    # section A-A at y = 0 (across the spine)
    sx0, sy0, k = 860, 520, 0.8
    s.text(sx0, sy0 - 30, "Section A-A at y = 0 (as in the mould)", 11, bold=True)
    SX = lambda x: sx0 + 140 + x * k * 0.55
    SY = lambda z: sy0 + 160 - z * k
    s.rect(SX(-200), SY(0), SX(200), SY(-t), fill="#ddd")                                    # floor
    for bx in (-180, 0, 180): s.rect(SX(bx - 19), SY(-t), SX(bx + 19), SY(-t - 40), fill="#f2e1c6")   # battens
    for sx in (-1, 1):
        x0 = sx * P["spine_w"] / 2
        s.rect(SX(x0), SY(0), SX(x0 + sx * t), SY(h_base + fb), fill="#eee")                  # walls
        b0, b1 = ybar(sx)
        s.rect(SX(b0 - 2), SY(0), SX(b1 + 2), SY(M["strip_t"]), fill=C["strip"])
        s.rect(SX(b0), SY(M["strip_t"]), SX(b1), SY(M["strip_t"] + 10), fill=C["bar"])
    s.poly([(SX(-36), SY(0)), (SX(36), SY(0)), (SX(35), SY(25)), (SX(-35), SY(25))], fill=C["block"], w=1)
    s.line(SX(-160), SY(h_base), SX(160), SY(h_base), "#00f", 1, "5,3")
    s.text(SX(165), SY(h_base) + 3, f"fill {h_base}", 8, c="#00f")
    s.text(SX(0), SY(-t - 55), "floor 18 MDF on CLS battens", 8, "middle")
    s.text(sx0, sy0 + 230, "Turned over after demould: the strips become 4 mm recesses for", 9)
    s.text(sx0, sy0 + 243, "the levelling pour, the block becomes the 70 x 25 screw channel.", 9)
    s.save(OUT / "mould_base.svg")


# ------------------------------------------------------------------------------------------- PORTAL
def draw_portal():
    sc, ox, oy = 0.9, 520, 520
    X = lambda x: ox - x * sc          # mirrored: machine +X to the left
    Z = lambda z: oy - z * sc          # machine z up the page
    s = Svg(1150, 1000, "PORTAL mould: floor plan (= portal FRONT face; cast face down). MIRRORED. Scale 1:1.1")
    s.text(10, 40, "Seen standing over the mould: machine RIGHT (+X, beam overhang) is on the LEFT. "
                   f"Walls {P['portal_d'] + fb} mm tall (fill line {P['portal_d']}).", 10)
    outer = []
    for x, z in portal_poly:
        outer.append((x, z))
    s.poly([(X(x), Z(z)) for x, z in portal_poly], fill="white", w=2)
    # wedge plug and L-wall region
    s.rect(X(D["open_x0"]), Z(0), X(D["open_x1"]), Z(D["beam_bottom"]), fill=C["plug"], c="#31a354", dash="5,3")
    s.text(X(0), Z(110), "3-piece wedge plug 500 x 225, 2 deg draft", 10, "middle")
    s.text(X(0), Z(95), "(two halves + tapered centre wedge)", 9, "middle")
    s.rect(X(D["leg_r_x1"]), Z(0), X(D["portal_x1"]), Z(D["beam_bottom"]), fill="#f0f0f0", c="#999", dash="5,3")
    s.text(X((D["leg_r_x1"] + D["portal_x1"]) / 2), Z(110), "L-wall (2 boards)", 9, "middle")
    # pocket strip, bars, pads
    s.rect(X(D["portal_x0"]), Z(M["x_pocket"][0]), X(D["portal_x1"]), Z(M["x_pocket"][1]), fill=C["strip"])
    for z0, z1 in (M["x_bar_lo"], M["x_bar_hi"]):
        s.rect(X(M["x_bar_x"][0]), Z(z0), X(M["x_bar_x"][1]), Z(z1), fill=C["bar"], op=0.5)
    for x0, x1 in ((D["portal_x0"], M["x_bar_x"][0]), (M["x_bar_x"][1], D["portal_x1"])):
        s.rect(X(x0), Z(M["x_bar_lo"][0]), X(x1), Z(M["x_bar_hi"][1]), fill=C["pad"])
    for zr in (250, 350):
        for hx in x_holes: s.circle(X(hx), Z(zr), 2.2, fill=C["hole"])
        bar_holes = [hx for hx in x_holes if M["x_bar_x"][0] < hx < M["x_bar_x"][1]]
        for ax in mid_anchors(bar_holes): s.line(X(ax), Z(zr + 15) , X(ax), Z(zr + 3), C["anchor"], 2)
    # core (dashed: it is above the floor, mid-depth)
    s.rect(X(M["core_x"][0]), Z(M["core_z"] - 34), X(M["core_x"][1]), Z(M["core_z"] + 34), c="#2171b5", dash="6,3", w=1.2)
    s.text(X(M["core_x"][1]) + 6, Z(M["core_z"] + 40), f"68 mm downpipe core, {M['core_x'][1]-M['core_x'][0]} long, at {M['core_depth']} mm above the floor (dashed)", 8, c="#2171b5")
    # leg-foot couplers (in the z = 0 wall) and lifting couplers (in the beam-top wall)
    for sx in (-1, 1):
        s.rect(X(sx * M["leg_bolt_x"] - 10), Z(0), X(sx * M["leg_bolt_x"] + 10), Z(-t), fill=C["anchor"])
        s.rect(X(M["lift_x"][0 if sx < 0 else 1] - 10), Z(D["beam_top"]), X(M["lift_x"][0 if sx < 0 else 1] + 10), Z(D["beam_top"] + t), fill=C["anchor"])
    s.text(X(0), Z(-t) + 14, "LEG-FOOT WALL (z = 0): 2 x M12 couplers per leg, jig studs through the wall", 9, "middle", c=C["anchor"])
    s.text(X(0), Z(D["beam_top"] + t) - 4, "BEAM-TOP WALL: 2 x M12 lifting couplers (36 deep, no rod: core below)", 9, "middle", c=C["anchor"])
    # dims
    s.dim(X(D["portal_x1"]), Z(D["beam_top"] + 40), X(D["portal_x0"]), Z(D["beam_top"] + 40), f"{D['portal_w']:.0f}", 0)
    s.dim(X(D["portal_x0"]) + 30, Z(0), X(D["portal_x0"]) + 30, Z(D["beam_top"]), f"{D['beam_top']:.0f}", -10)
    s.dim(X(D["portal_x0"]) + 70, Z(D["beam_bottom"]), X(D["portal_x0"]) + 70, Z(D["beam_top"]), f"beam {P['beam_h']}", -10)
    s.dim(X(D["open_x1"]), Z(-45), X(D["open_x0"]), Z(-45), f"opening {D['open_x1']-D['open_x0']:.0f}", 0)
    s.dim(X(D["portal_x1"]), Z(-45), X(D["leg_r_x1"]), Z(-45), f"{D['portal_x1']-D['leg_r_x1']:.0f}", 0)
    s.dim(X(D["leg_r_x1"]), Z(-45), X(D["open_x1"]), Z(-45), f"{P['upright_w']}", 0)
    s.dim(X(D["portal_x1"]) - 30, Z(M["x_pocket"][0]), X(D["portal_x1"]) - 30, Z(M["x_pocket"][1]), f"pocket {M['x_pocket'][1]-M['x_pocket'][0]}", 12)
    s.dim(X(D["portal_x1"]) - 60, Z(250), X(D["portal_x1"]) - 60, Z(350), f"rails {P['x_rail_spacing']}", 12)
    s.text(X(D["portal_x1"]) - 4, Z(D["beam_top"]) - 20, "+X end", 10, "start", True)
    s.text(X(D["portal_x0"]) + 4, Z(D["beam_top"]) - 20, "-X end", 10, "end", True)
    legend(s, 20, 640, [(C["strip"], f"raised strip {M['strip_t']} mm = rail-seat pocket (both rails + screw end blocks)"),
                        (C["bar"], f"rail bars 40x10, {M['x_bar_x'][1]-M['x_bar_x'][0]} long, M5 at 60 (VERIFY), holes 10 from the outer edge"),
                        (C["pad"], "crosswise end pads 40x120x10: rail end holes + BK12 (+X) / BF12 (-X), drill+tap later"),
                        (C["anchor"], "M12 couplers (leg feet, lifting) / M6 anchors on bar backs")])
    # section B-B through the beam
    sx0, sy0, k = 700, 690, 1.3
    s.text(sx0, sy0 - 14, "Section B-B through the beam (in the mould)", 11, bold=True)
    BX = lambda depth: sx0 + 40 + depth * k
    BZ = lambda z: sy0 + 20 + (D["beam_top"] - z) * k
    s.rect(BX(-t), BZ(D["beam_top"] + t), BX(0), BZ(D["beam_bottom"] - t), fill="#ddd")
    s.text(BX(-t) - 3, BZ(300), "floor", 8, "end")
    s.rect(BX(0), BZ(M["x_pocket"][1]), BX(M["strip_t"]), BZ(M["x_pocket"][0]), fill=C["strip"])
    for z0, z1 in (M["x_bar_lo"], M["x_bar_hi"]):
        s.rect(BX(M["strip_t"]), BZ(z1), BX(M["strip_t"] + 10), BZ(z0), fill=C["bar"])
    s.circle(BX(M["core_depth"]), BZ(M["core_z"]), 34 * k, fill=C["core"], c="#2171b5")
    s.rect(BX(0), BZ(D["beam_top"] + t), BX(P["portal_d"] + fb), BZ(D["beam_top"]), fill="#eee")
    s.rect(BX(0), BZ(D["beam_bottom"]), BX(P["portal_d"] + fb), BZ(D["beam_bottom"] - t), fill="#eee")
    s.rect(BX(M["lift_depth"] - 10), BZ(D["beam_top"]), BX(M["lift_depth"] + 10), BZ(D["beam_top"] - 36), fill=C["anchor"])
    s.line(BX(P["portal_d"]), BZ(D["beam_top"]), BX(P["portal_d"]), BZ(D["beam_bottom"]), "#00f", 1, "5,3")
    s.text(BX(P["portal_d"]) + 3, BZ(D["beam_bottom"]) + 12, f"fill {P['portal_d']}", 8, c="#00f")
    s.line(BX(M["core_depth"]), BZ(M["core_z"]) - 34 * k, BX(P["portal_d"] + fb + 15), BZ(M["core_z"]) - 34 * k, "#555", 1)
    s.text(BX(P["portal_d"] + fb + 18), BZ(M["core_z"]) - 34 * k + 3, "hold-down rod from the top batten", 8)
    s.text(sx0, BZ(D["beam_bottom"] - t) + 18, "Floor at left. The open face (right) becomes the portal back.", 8)
    notes = ["Rail holes: M5, jig bolt M5 x 30 waxed through the floor + strip into each. Plug the bar backs with plasticine.",
             "End pads: crosswise pieces of the same 40x10 bar, butted to the rail bars. Ends of the pocket stay open: dam them at the levelling pour.",
             "Core: 68 mm round downpipe, ends sealed with an MDF disc + silicone + tape. Sits on 3 EG spacers (test-brick offcuts),",
             "      held down at 3 points by M6 rod from a batten across the walls (buoyancy about 6 kg).",
             "Leg-foot couplers: M12 coupling nut (36) + 100 mm M12 rod + nut + washer. Jig stud through the wall. Torque the studs to 25-30 Nm only (VERIFY on a test brick).",
             "Probes: DS18B20 in the beam above the core and in one leg."]
    for i, n in enumerate(notes): s.text(20, 735 + i * 14, n, 9)
    s.save(OUT / "mould_portal.svg")


# ------------------------------------------------------------------------------------------- MDF cut list + sheet layout
def cut_list():
    """Panels for both moulds from one 18 mm MDF sheet (F10)."""
    bh, ph = h_base + fb, P["portal_d"] + fb
    bx = cross[1] - cross[0] + 2 * t + 2 * M["floor_margin"]
    by = spine[3] - spine[2] + 2 * t + 2 * M["floor_margin"]
    px = D["portal_w"] + 2 * t + 2 * M["floor_margin"]
    pz = D["beam_top"] + 2 * t + 2 * M["floor_margin"]
    parts = [("Base floor", bx, by, 1), ("Portal floor", px, pz, 1)]
    # base walls: each inner edge + one wall thickness (pinwheel at outside corners)
    for i in range(len(base_poly)):
        L = math.dist(base_poly[i], base_poly[(i + 1) % len(base_poly)])
        parts.append((f"Base wall {i+1}", L + t, bh, 1))
    for i in range(len(portal_poly)):
        L = math.dist(portal_poly[i], portal_poly[(i + 1) % len(portal_poly)])
        parts.append((f"Portal wall {i+1}", L + t, ph, 1))
    ow, oh = D["open_x1"] - D["open_x0"], D["beam_bottom"]
    parts += [("Plug half (x2: sides + top)", oh, ph, 2), ("Plug top halves", ow / 2 - 30, ph, 2),
              ("Plug centre wedge", 60, ph, 1),
              ("Screw block (laminate to 25)", M["screw_ch_y1"] - spine[2], M["screw_ch_w"] + 2, 2)]
    return parts


def pack(parts, W=2440, H=1220, kerf=4):
    """Simple shelf packing, largest first. Returns placements and whether everything fitted."""
    items = []
    for name, a, b, n in parts:
        for i in range(n): items.append((name, max(a, b), min(a, b)))
    items.sort(key=lambda r: (-r[2], -r[1]))
    shelves, place = [], []
    for name, w, h in items:
        for sh in shelves:
            if sh["h"] >= h and sh["x"] + w <= W:
                place.append((name, sh["x"], sh["y"], w, h)); sh["x"] += w + kerf; break
        else:
            y = sum(s["h"] + kerf for s in shelves)
            if y + h > H or w > W:
                place.append((name, None, None, w, h)); continue
            shelves.append(dict(y=y, h=h, x=w + kerf)); place.append((name, 0, y, w, h))
    return place


def draw_sheet(place):
    k = 0.4
    s = Svg(int(2440 * k) + 40, int(1220 * k) + 90, "18 mm MDF sheet 2440 x 1220 (F10): mould panels (shelf layout, check before cutting)")
    s.rect(20, 40, 20 + 2440 * k, 40 + 1220 * k, fill="#fafafa", w=1.5)
    for name, x, y, w, h in place:
        if x is None: continue
        s.rect(20 + x * k, 40 + y * k, 20 + (x + w) * k, 40 + (y + h) * k, fill="#fee6ce")
        if w * k > 40: s.text(20 + (x + w / 2) * k, 40 + (y + h / 2) * k + 3, f"{name} {w:.0f}x{h:.0f}", 7, "middle")
    s.save(OUT / "mould_sheet.svg")


def report(place, parts):
    misfit = [p for p in place if p[1] is None]
    y_bar_n, x_bar_n = len(y_holes), len([h for h in x_holes if M["x_bar_x"][0] < h < M["x_bar_x"][1]])
    bars = [("Y rail bar", M["y_rail_len"], 2), ("X rail bar", M["x_bar_x"][1] - M["x_bar_x"][0], 2),
            ("X end pad (crosswise)", M["x_bar_hi"][1] - M["x_bar_lo"][0], 2),
            ("Y front pad (motor mount + BK12)", M["y_pad_front"][1] - M["y_pad_front"][0], 1),
            ("Y rear pad (BF12)", M["y_pad_rear"][1] - M["y_pad_rear"][0], 1)]
    bar_total = sum(L * n for _, L, n in bars) + 4 * sum(n for *_, n in bars)
    jig_m5 = 2 * y_bar_n + 2 * len(x_holes)
    anchors = 2 * len(mid_anchors(y_holes)) + 2 * len(mid_anchors([h for h in x_holes if M["x_bar_x"][0] < h < M["x_bar_x"][1]])) + 2 * 2 + 2 * 2
    L = ["# Mould parts (generated by cad/v2/moulds.py)", "",
         "Drawings: `mould_base.svg`, `mould_portal.svg`, `mould_sheet.svg`. Notes and procedure: [docs/moulds.md](../../../docs/moulds.md).", "",
         "## MDF panels (18 mm, one sheet F10)", "| Panel | Size (mm) | Qty |", "|---|---|---|"]
    L += [f"| {n} | {a:.0f} × {b:.0f} | {q} |" for n, a, b, q in parts]
    L += ["", f"Sheet layout: {'all panels fit on one 2440 × 1220 sheet' if not misfit else 'DOES NOT FIT: ' + ', '.join(p[0] for p in misfit)}. "
          "Wall lengths are inner edge + 18 mm (pinwheel corners); trim the inside-corner pieces to fit.", "",
          "## Steel insert bars (40 × 10 flat bar, F07 3 m)", "| Piece | Length (mm) | Qty |", "|---|---|---|"]
    L += [f"| {n} | {Lb:.0f} | {q} |" for n, Lb, q in bars]
    L += [f"| **Total with saw cuts** | **{bar_total:.0f}** of 3,000 | |", "",
          "## Fixings for the moulds", "| Item | Qty | Notes |", "|---|---|---|",
          f"| M5 × 30 jig bolts (waxed) | {jig_m5} + spares | One per rail hole: Y {y_bar_n} per bar, X {len(x_holes)} per rail incl. the end pads |",
          f"| M6 × 20 screw + nut (bar anchors) | {anchors} | Blind M6 holes 6 mm deep on the bar backs, midway between rail holes (X03 has 50 × M6 × 20) |",
          "| M12 coupling nut, 36 long | 8 | Portal leg feet 4, lifting 2, 2 spare |",
          "| M10 coupling nut | 4 | Base feet (T02) |",
          "| M12 rod (F08, 5 × 1 m) | about 2 m | Jig studs (6 × 40), leg-foot anchors (4 × 100), base sleeve rods (4 × 160), portal studs (4 × 160: coupler 18 + grout 3 + base 110 + nut and washer) |",
          "| 20 mm uPVC conduit (F09) | 4 × 110 | Base sleeves for the portal studs |",
          "| 68 mm round downpipe | 1 × 680 | Portal core (D-95) |",
          "| 4 mm hardboard | about 0.25 m² | Raised strips (Y strips, link, X pocket) |"]
    (OUT / "moulds_parts.md").write_text("\n".join(L) + "\n")
    return misfit


if __name__ == "__main__":
    draw_base(); draw_portal()
    parts = cut_list(); place = pack(parts); draw_sheet(place)
    misfit = report(place, parts)
    print((OUT / "moulds_parts.md").read_text())
    print("Y holes:", [round(v) for v in y_holes]); print("X holes:", [round(v) for v in x_holes])
    if misfit: sys.exit("panels do not fit the sheet")

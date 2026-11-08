"""Type 0 v2 full assembly (task 4, D-102 ... D-107).

Run: python cad/v2/assembly.py   -> cad/v2/out/assembly/
       type0_assembly.step   whole machine, named components (open in Fusion 360: File > Open)
       base_casting.step, portal_casting.step   the two castings with every cast-in feature
       assembly_report.md     part list, cast-in features, masses, clash check, VERIFY list
       assembly_front/side/top/iso.svg  views

Coordinates as type0_v2.py: X right, Y back, Z up; Z 0 = top (rail-seat datum) of the base.
Bought parts are accurate envelopes with the real bolt patterns, from datasheets. Values marked
VERIFY are not yet confirmed from a drawing; replace those parts with vendor STEP files in Fusion.
"""
import json, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
import type0_v2 as m

P, D = m.P, m.D
OUT = pathlib.Path(__file__).parent / "out" / "assembly"; OUT.mkdir(parents=True, exist_ok=True)
EG_RHO = 2300e-9                                   # kg/mm3 (type0_v2 eg_density)

# ---------------------------------------------------------------------------
# Bought-part data (mm). Source in the comment; VERIFY = not yet from a drawing.
# ---------------------------------------------------------------------------
RAIL = dict(w=20, h=17.5, pitch=60, e=20, cb_d=9.5, cb_h=8.5, hole_d=6)          # HIWIN HGR20 datasheet
BLOCK = dict(w=44, l=77.5, H=30, H1=4.6, C=32, B=36, bolt="M5")                    # HGH20CA (vendor STEP: H1 4.6)
SCREW = dict(d=16, lead=5)                                                         # DFU1605
NUT = dict(body_d=28, len=100, fl_d=48, fl_t=10, fl_flat=40, pcd=38)               # DFU1605 (vendor STEP: 100 long; flats 40 VERIFY, model has none)
HOUSING = dict(w=52, h=40, l=40, ctr=20)                                           # DSG16H: face 52 x 40, 40 high, centre 20 below the face, 4 x M5 at 40 x 24 (seller drawing)
BK = dict(w=60, h=43, l=25, ctr=25, lock=12, bolt_p=46)                            # BK12 (vendor STEP): 37 long incl. lock nut, centre 25, holes at 46
BF = dict(w=60, h=43, l=20, ctr=25, bolt_p=46)                                     # BF12 (vendor STEP)
COUPLING = dict(d=26, l=35)                                                        # M08 D26 L35
MOTOR_XY = dict(sq=60, body=100, enc=25, pilot_d=38.1, pilot_h=1.6, shaft_d=10, shaft_l=21, hole_p=50, hole_d=5.1)  # 24HS40-5004D-E1000 drawing
MOTOR_Z = dict(sq=60, body=86, brake=20, enc=40, pilot_d=36, pilot_h=1.6, shaft_d=10, shaft_l=21, hole_p=50, hole_d=5.1)     # 24HS34-..-B280 drawing (A4717)
PULLEY = dict(od=36.0, w=20.7, hub_d=23, hub_l=5.5)                                # HTD-5M 20T 15 mm (vendor STEP Maedler 17232000; flanges Ø36)
SPINDLE = dict(d=80, body=230, nose=52, nose_d=34)                                 # G-Penny BST2.2C-80-24K
CLAMP = dict(w=116, h=60, offset=60)                                               # 80 mm clamp: spindle axis 60 from its mounting face (VERIFY: kit part)
FLATBAR_Y = (40, 10)                                                               # F07 40 x 10 under the Y rails (D-105)
FLATBAR_X = (25, 10)                                                               # 25 x 10 under the X rails (D-104)

def box(x0, x1, y0, y1, z0, z1):
    return cq.Workplane("XY").box(x1 - x0, y1 - y0, z1 - z0, centered=False).translate((x0, y0, z0))

def cyl(axis, d, l, c):
    """Cylinder of diameter d, length l along axis 'x','y','z', starting at point c."""
    wp = {"x": "YZ", "y": "XZ", "z": "XY"}[axis]
    s = cq.Workplane(wp).circle(d / 2).extrude(l if axis != "y" else -l)
    return s.translate(c)

# ---------------------------------------------------------------------------
# Layout numbers (derived; see assembly_report.md for the reasoning)
# ---------------------------------------------------------------------------
L = {}
h, sw = P["h"], P["spine_w"]
L["seat_recess"] = 3.0                       # levelling-pour recess over each insert bar (eg-moulds.md)
L["chan_depth"] = 15.0                       # Y screw channel: nut housing clearance, floor = BK/BF seat
L["x_spacer"] = 25.0                         # spacer behind the X nut housing so BK/BF pass under the X blocks (D-108)
L["x_chan_depth"], L["x_pad"] = 45.0, 5.0     # X channel depth; BK/BF seat pads 5 proud of its floor
L["y_chan_w"], L["x_chan_w"] = 70.0, 64.0
# Y axis (rails on the spine top, table on 4 blocks)
L["y_rail_x"] = P["y_rail_spacing"] / 2
L["ty_min"], L["ty_max"] = D["spindle_y"] - P["travel_y"] / 2, D["spindle_y"] + P["travel_y"] / 2   # table centre range
L["y_rail_y0"] = L["ty_min"] - P["y_block_pitch"] / 2 - BLOCK["l"] / 2 - 8
L["y_rail_len"] = 500.0                                                    # M01: 2 x 500
L["y_screw_z"] = BLOCK["H"] - HOUSING["ctr"]                               # 10: nut housing hangs under the table
L["y_bk_y0"] = D["spine_y0"] + BK["lock"] + 2                              # BK at the very front of the spine (belt crosses in front of it, D-107)
L["y_bk_y1"] = L["y_bk_y0"] + BK["l"]
L["y_bf_y0"] = L["ty_max"] + NUT["len"] / 2 + 5
# X axis (rails on the beam front face)
L["beam_zc"] = (D["beam_bottom"] + D["beam_top"]) / 2
L["x_rail_z"] = (L["beam_zc"] - P["x_rail_spacing"] / 2, L["beam_zc"] + P["x_rail_spacing"] / 2)
L["x_bar_shift"] = 3.0                                                     # bars shifted outward (cover to the channel)
L["x_screw_y"] = P["beam_front"] - BLOCK["H"] + L["x_spacer"] + HOUSING["ctr"]   # 125: 15 mm behind the beam face
L["xs_min"], L["xs_max"] = D["x_min"], D["x_max"]                          # saddle centre range
L["x_bk_x0"] = L["xs_max"] + NUT["len"] / 2 + 5                            # BK at the right (drive end)
L["x_bf_x1"] = L["xs_min"] - NUT["len"] / 2 - 5
L["x_rail_len"] = 800.0                                                    # M02: 2 x 800 (beam is 800)
# Saddle and Z (rails on a tall saddle, short moving Z plate, D-104 answer)
L["saddle_t"], L["saddle_h"] = 20.0, 400.0
L["saddle_y1"] = P["beam_front"] - BLOCK["H"]                              # 80
L["saddle_y0"] = L["saddle_y1"] - L["saddle_t"]                            # 60
L["z_riser"] = 15.0                                                        # risers under the Z rails: nut housing clears the saddle
L["zp_t"], L["zp_h"] = 20.0, 200.0
L["zp_y1"] = L["saddle_y0"] - L["z_riser"] - BLOCK["H"]                    # Z plate back face
L["zp_y0"] = L["zp_y1"] - L["zp_t"]
L["z_screw_y"] = L["zp_y1"] + HOUSING["ctr"]
L["spindle_y"] = L["zp_y0"] - CLAMP["offset"]                                 # must equal D["spindle_y"]
L["nose_top"], L["nose_bot"] = D["nose_top"], D["nose_bottom"]

def check_stack():
    calc = L["spindle_y"]
    return calc, D["spindle_y"]

# ---------------------------------------------------------------------------
# Bought parts
# ---------------------------------------------------------------------------
def rail(length, axis_dir, origin, up):
    """HGR20 rail. Built along +X with its base at z=0, then placed. up: 'z' (on a top face) or '-y' (on a front face)."""
    r = box(0, length, -RAIL["w"] / 2, RAIL["w"] / 2, 0, RAIL["h"])
    n = int((length - 2 * RAIL["e"]) // RAIL["pitch"]) + 1
    e = (length - (n - 1) * RAIL["pitch"]) / 2
    for i in range(n):
        x = e + i * RAIL["pitch"]
        r = r.cut(cyl("z", RAIL["hole_d"], RAIL["h"], (x, 0, 0))).cut(cyl("z", RAIL["cb_d"], RAIL["cb_h"], (x, 0, RAIL["h"] - RAIL["cb_h"])))
    holes = [e + i * RAIL["pitch"] for i in range(n)]
    return place(r, axis_dir, origin, up), holes

def block():
    v = v_block()
    if v is not None:
        return v
    b = box(-BLOCK["l"] / 2, BLOCK["l"] / 2, -BLOCK["w"] / 2, BLOCK["w"] / 2, BLOCK["H1"], BLOCK["H"])
    b = b.cut(box(-BLOCK["l"] / 2 - 1, BLOCK["l"] / 2 + 1, -RAIL["w"] / 2 - 0.5, RAIL["w"] / 2 + 0.5, BLOCK["H1"] - 1, RAIL["h"] + 0.5))
    for sx in (-1, 1):
        for sy in (-1, 1):
            b = b.cut(cyl("z", 4.2, 8, (sx * BLOCK["B"] / 2, sy * BLOCK["C"] / 2, BLOCK["H"] - 8)))
    return b

def place(shape, axis_dir, origin, up):
    """Shapes are built along +X with 'up' = +Z. Rotate to the wanted direction and move to origin."""
    s = shape
    if up == "-y":                       # face mounted on a front (−Y facing) surface
        s = s.rotate((0, 0, 0), (1, 0, 0), 90)       # +Z -> -Y
    if axis_dir == "y":
        s = s.rotate((0, 0, 0), (0, 0, 1), 90)
    if axis_dir == "z":
        s = s.rotate((0, 0, 0), (0, 1, 0), -90)
    return s.translate(origin)

def ballscrew(length, stub=15, bkj=BK["l"] + BK["lock"], bf_journal=10):
    """DFU1605 along +X from x=0: drive stub Ø10, BK journal Ø12 (through BK + lock nut), thread, BF journal Ø10."""
    s = cyl("x", 10, stub, (0, 0, 0)).union(cyl("x", 12, bkj, (stub, 0, 0)))
    s = s.union(cyl("x", SCREW["d"], length - stub - bkj - bf_journal, (stub + bkj, 0, 0)))
    return s.union(cyl("x", 10, bf_journal, (length - bf_journal, 0, 0)))

def dfu_nut(flats="y"):
    """DFU nut along X; the flange flats limit 'y' or 'z' (the side facing the housing face)."""
    lim = box(-NUT["len"], NUT["len"], -NUT["fl_flat"] / 2, NUT["fl_flat"] / 2, -30, 30) if flats == "y" else box(-NUT["len"], NUT["len"], -30, 30, -NUT["fl_flat"] / 2, NUT["fl_flat"] / 2)
    v = v_nut()
    if v is not None:
        return v.intersect(lim)
    n = cyl("x", NUT["body_d"], NUT["len"], (-NUT["len"] / 2, 0, 0))
    lim = box(-NUT["len"], NUT["len"], -NUT["fl_flat"] / 2, NUT["fl_flat"] / 2, -30, 30) if flats == "y" else box(-NUT["len"], NUT["len"], -30, 30, -NUT["fl_flat"] / 2, NUT["fl_flat"] / 2)
    f = cyl("x", NUT["fl_d"], NUT["fl_t"], (-NUT["len"] / 2, 0, 0)).intersect(lim)
    return n.union(f).cut(cyl("x", SCREW["d"], NUT["len"] + 2, (-NUT["len"] / 2 - 1, 0, 0)))

def housing():
    """Nut housing built with its mounting face at z=0 facing +Z, screw axis along X at z=-ctr."""
    hb = box(-HOUSING["l"] / 2, HOUSING["l"] / 2, -HOUSING["w"] / 2, HOUSING["w"] / 2, -HOUSING["h"], 0)
    return hb.cut(cyl("x", NUT["body_d"] + 0.5, HOUSING["l"] + 2, (-HOUSING["l"] / 2 - 1, 0, -HOUSING["ctr"])))

def support(kind):
    """BK12 / BF12 built with its base at z=0 (base on +Z up), screw axis along X at z=ctr, body from x=0 to l."""
    v = v_support(kind)
    if v is not None:
        return v
    d = BK if kind == "BK" else BF
    s = box(0, d["l"], -d["w"] / 2, d["w"] / 2, 0, d["h"])
    s = s.cut(cyl("x", 12 if kind == "BK" else 10, d["l"] + 2, (-1, 0, d["ctr"])))
    for sy in (-1, 1):
        s = s.cut(cyl("z", 5.5, d["h"], (d["l"] / 2, sy * d["bolt_p"] / 2, 0)))
    if kind == "BK":
        s = s.union(cyl("x", 26, BK["lock"], (-BK["lock"], 0, d["ctr"])))
    return s

def motor(md):
    """NEMA 24 along -X from the flange face at x=0 (shaft along +X)."""
    v = v_motor_z() if md is MOTOR_Z else v_motor_xy()
    if v is not None:
        return v
    total = md["body"] + md.get("brake", 0) + md["enc"]
    mtr = box(-total, 0, -md["sq"] / 2, md["sq"] / 2, -md["sq"] / 2, md["sq"] / 2).edges("|X").fillet(4)
    for sy in (-1, 1):
        for sz in (-1, 1):
            mtr = mtr.cut(cyl("x", md["hole_d"], 10, (-10, sy * md["hole_p"] / 2, sz * md["hole_p"] / 2)))
    mtr = mtr.union(cyl("x", md["pilot_d"], md["pilot_h"], (0, 0, 0)))
    return mtr.union(cyl("x", md["shaft_d"], md["shaft_l"], (md["pilot_h"], 0, 0)))

def pulley():
    v = v_pulley()
    if v is not None:
        return v
    p = cyl("x", PULLEY["od"], PULLEY["w"], (0, 0, 0)).union(cyl("x", PULLEY["hub_d"], PULLEY["hub_l"], (PULLEY["w"], 0, 0)))
    return p.cut(cyl("x", 10, PULLEY["w"] + PULLEY["hub_l"] + 2, (-1, 0, 0)))

def belt(c1, c2, plane_x, od):
    """Flat belt envelope (15 wide) between two pulley centres (y,z) in the plane x=plane_x."""
    (y1, z1), (y2, z2) = c1, c2
    ang = math.degrees(math.atan2(z2 - z1, y2 - y1)); dist = math.hypot(y2 - y1, z2 - z1)
    loop = (cq.Workplane("YZ").workplane(offset=plane_x).center(y1, z1).circle(od / 2 + 2).extrude(15)
            .union(cq.Workplane("YZ").workplane(offset=plane_x).center(y2, z2).circle(od / 2 + 2).extrude(15))
            .union(cq.Workplane("YZ").workplane(offset=plane_x).center((y1 + y2) / 2, (z1 + z2) / 2)
                   .rect(dist, od + 4).extrude(15).rotate(((y1 + y2) / 2 * 0 + plane_x, (y1 + y2) / 2, (z1 + z2) / 2), (plane_x + 1, (y1 + y2) / 2, (z1 + z2) / 2), ang)))
    return loop

# ---------------------------------------------------------------------------
# Vendor STEP models (cad/vendor/, D-111). Each is mapped into the same local frame as the
# envelope function it replaces, so the placement code is unchanged. Missing file -> envelope.
# ---------------------------------------------------------------------------
VENDOR_DIR = pathlib.Path(__file__).resolve().parent.parent / "vendor"
_VCACHE = {}
USE_VENDOR = "--envelopes" not in sys.argv

class _mat:
    """Rigid transform from where the vendor x, y, z axes go (cols) and a translation."""
    def __init__(self, cols, t):
        from OCP.gp import gp_Trsf
        (a, b, c) = cols
        self.trsf = gp_Trsf()
        self.trsf.SetValues(a[0], b[0], c[0], t[0], a[1], b[1], c[1], t[1], a[2], b[2], c[2], t[2])

def _apply(shape, m):
    return shape.moved(cq.Location(m.trsf))

def vendor(name, cols, t, keep=None, trim=None, cut_bore=None):
    """Load cad/vendor/<name>.step once; keep solids passing keep(bbox); intersect with trim box (vendor coords);
    optionally cut a bore (axis 'x'/'y'/'z', diameter) in vendor coords; then map with cols/t. Returns a Workplane or None."""
    f = VENDOR_DIR / f"{name}.step"
    if not (USE_VENDOR and f.exists()):
        return None
    key = (name, repr(trim), repr(cut_bore), repr(keep is None))
    if key not in _VCACHE:
        w = cq.importers.importStep(str(f))
        sol = [s_ for s_ in w.solids().vals() if keep is None or keep(s_.BoundingBox())]
        shp = cq.Workplane().add(cq.Compound.makeCompound(sol))
        if trim:
            shp = shp.intersect(box(*trim))
        if cut_bore:
            ax, dia, c = cut_bore
            shp = shp.cut(cyl(ax, dia, 400, c))
        _VCACHE[key] = shp.val()
    return cq.Workplane().add(_apply(_VCACHE[key], _mat(cols, t)))

ROT_A = ((0, 1, 0), (0, 0, 1), (1, 0, 0))      # vendor x->y, y->z, z->x
ROT_B = ((0, -1, 0), (0, 0, 1), (-1, 0, 0))    # vendor x->-y, y->z, z->-x

def v_block():          # HGH20CA: vendor length z, width x, up +y, rail top y=0 (rail base -17.5) -> my x/y/z, rail base z=0
    return vendor("hgh20ca_block", ROT_A, (0, 0, 17.5), keep=lambda b: b.xlen > 30)

def v_support(kind):    # BK12/BF12: vendor axis z, base y=-21.5, axis y=3.5; BK lock on +z -> my axis x, base z=0, lock on -x
    if kind == "BK":
        return vendor("bk12", ROT_B, (12, 0, 21.5))
    return vendor("bf12", ROT_B, (10, 0, 21.5))

def v_nut():            # DFU1605: vendor axis x, nut x -115..-15, flange near +x; screw piece removed -> centred, flange at -x
    return vendor("dfu1605_nut", ((-1, 0, 0), (0, -1, 0), (0, 0, 1)), (-65, 0, 0), keep=lambda b: not (b.xlen > 120))

def v_pulley():         # HTD-5M 20T: vendor axis x 0..26.2, pilot bore -> Ø10
    return vendor("htd5m_20t_15", ((1, 0, 0), (0, 1, 0), (0, 0, 1)), (0, 0, 0), cut_bore=("x", 10, (-50, 0, 0)))

def v_motor_xy():       # 24HS40: vendor shaft +z at the origin, flange face z=0; cables trimmed off
    return vendor("24hs40_motor", ROT_A, (0, 0, 0), trim=(-30.5, 30.5, -30.5, 30.5, -125.5, 25))

def v_motor_z():        # 24HS34-B280: vendor shaft +z at (-73.8, 56), shaft tip z 100.1 -> flange face z 77.5
    return vendor("24hs34_brake_motor", ROT_A, (-77.5, 73.8, -56.0), trim=(-104, -43.6, 26, 86.1, -66, 101))

def v_bearing():        # KFL000: vendor axis z, flange holes along y -> my axis x, holes along z
    return vendor("kfl000_bearing", ROT_A, (7.5, 0, 0))

def v_sensor():         # M12 sensor: vendor axis z, sensing face z=0, body to -57.1 (returned as-is: face up)
    return vendor("lj12a3_sensor", ((1, 0, 0), (0, 1, 0), (0, 0, 1)), (0, 0, 0))

# ---------------------------------------------------------------------------
# Castings with cast-in features
# ---------------------------------------------------------------------------
FEATURES = []          # (casting, feature, size, position/notes) for the report and the mould drawings
INSERTS = {}           # name -> shape (steel, cast in)

def base_casting():
    s0, s1 = D["spine_y0"], D["foot_y1"]
    b = box(-sw / 2, sw / 2, s0, s1, -h, 0).union(box(D["portal_x0"], D["leg_r_x1"], D["foot_y0"], D["foot_y1"], -h, 0))
    bw, bt = FLATBAR_Y
    y0, y1 = L["y_rail_y0"], L["y_rail_y0"] + L["y_rail_len"]
    for k, x in enumerate((-L["y_rail_x"], L["y_rail_x"])):
        # levelling recess over the bar (rail seat poured later), insert bar under it
        b = b.cut(box(x - 15, x + 15, y0 - 5, y1 + 5, -L["seat_recess"], 0.1))
        bar = box(x - bw / 2, x + bw / 2, y0, y1, -L["seat_recess"] - bt, -L["seat_recess"])
        INSERTS[f"base_insert_Y_rail_{'LR'[k]}"] = bar
        FEATURES.append(("base", f"Y rail insert bar {'LR'[k]}", f"{bw} x {bt} x {y1-y0:.0f} flat bar, tapped M5 at {RAIL['pitch']} (rail holes)", f"centre X {x:+.0f}, Y {y0:.0f} to {y1:.0f}, top {L['seat_recess']:.0f} below datum"))
    b = b.cut(box(-L["y_rail_x"], L["y_rail_x"], y0 + 20, y0 + 40, -L["seat_recess"], 0.1))   # cross-link so both seats level together
    FEATURES.append(("base", "Rail-seat recesses", f"2 x 30 wide x {L['seat_recess']:.0f} deep + 20 wide cross-link", "filled by the levelling pour"))
    # Y screw channel and BK/BF seats (channel floor = seat)
    cy0, cy1 = D["spine_y0"] - 1, L["y_bf_y0"] + BF["l"] + 15
    b = b.cut(box(-L["y_chan_w"] / 2, L["y_chan_w"] / 2, cy0, cy1, -L["chan_depth"], 0.1))
    FEATURES.append(("base", "Y screw channel", f"{L['y_chan_w']:.0f} wide x {L['chan_depth']:.0f} deep", f"Y {cy0:.0f} to {cy1:.0f}; floor = BK12/BF12 seat (screw axis Z {L['y_screw_z']:.0f})"))
    for nm, yy in (("BK12", L["y_bk_y0"] + BK["l"] / 2), ("BF12", L["y_bf_y0"] + BF["l"] / 2)):
        bar = box(-30, 30, yy - 15, yy + 15, -L["chan_depth"] - 10, -L["chan_depth"])
        INSERTS[f"base_insert_Y_{nm}"] = bar
        FEATURES.append(("base", f"Y {nm} insert plate", "60 x 30 x 10 steel, 2 x M5 tapped (VERIFY BK bolt pattern)", f"under the channel floor at Y {yy:.0f}"))
    # Y motor bracket inserts on the right side face of the spine (motor folded alongside, D-107)
    for yy in (L["y_bk_y0"] + 15, L["y_bk_y0"] + 55):
        ins = cyl("x", 20, 30, (sw / 2 - 30, yy, -45))
        INSERTS[f"base_insert_Ymotor_{yy:.0f}"] = ins
    FEATURES.append(("base", "Y motor bracket inserts", "2 x M8 nut-on-rod", f"right spine face X {sw/2:.0f}, Z -45, Y {L['y_bk_y0']+15:.0f} and {L['y_bk_y0']+55:.0f}"))
    # portal joint: per leg 2 x M12 into a tapped insert bar + 1 dowel sleeve
    for side, xc in (("L", D["portal_x0"] + P["upright_w"] / 2), ("R", D["leg_r_x1"] - P["upright_w"] / 2)):
        ys = (D["portal_y0"] + 30, D["portal_y1"] - 30)
        bar = box(xc - 20, xc + 20, ys[0] - 25, ys[1] + 25, -40, -30)
        INSERTS[f"base_insert_portal_{side}"] = bar
        for yy in ys:
            b = b.cut(cyl("z", 13, 30, (xc, yy, -30)))
        b = b.cut(cyl("z", 12, 30, (xc, (ys[0] + ys[1]) / 2, -30)))
        FEATURES.append(("base", f"Portal joint, {side} leg", "40 x 10 bar tapped 2 x M12 (30 below the top) + Ø12 dowel sleeve (ream Ø10 after grouting)", f"X {xc:+.0f}, Y {ys[0]:.0f} / {ys[1]:.0f}, dowel Y {(ys[0]+ys[1])/2:.0f}"))
    # lifting points: 4 x M12 into the spine side faces (base is cast upside down; sides are free)
    for sx in (-1, 1):
        for yy in (s0 + 120, D["foot_y0"] - 40):
            b = b.cut(cyl("x", 12, 40, (sx * sw / 2 - (40 if sx > 0 else 0), yy, -55)))
    FEATURES.append(("base", "Lifting points", "4 x M12 nut-on-rod, horizontal", f"spine sides at Z -55, Y {s0+120:.0f} and {D['foot_y0']-40:.0f}"))
    return b

def portal_casting():
    x0, x1, y0, y1 = D["portal_x0"], D["portal_x1"], D["portal_y0"], D["portal_y1"]
    pz = D["beam_top"]
    p = box(x0, x1, y0, y1, 0, pz)
    p = p.cut(box(D["open_x0"], D["open_x1"], y0 - 1, y1 + 1, -1, D["beam_bottom"]))
    p = p.cut(box(D["leg_r_x1"], x1 + 1, y0 - 1, y1 + 1, -1, D["beam_bottom"]))
    bw, bt = FLATBAR_X
    rx0 = x0 + (D["portal_w"] - L["x_rail_len"]) / 2
    for k, zr in enumerate(L["x_rail_z"]):
        zb = zr + (L["x_bar_shift"] if zr > L["beam_zc"] else -L["x_bar_shift"])
        p = p.cut(box(rx0 - 1, rx0 + L["x_rail_len"] + 1, y0 - 0.1, y0 + L["seat_recess"], zr - 15, zr + 15))
        bar = box(rx0 + 10, rx0 + L["x_rail_len"] - 10, y0 + L["seat_recess"], y0 + L["seat_recess"] + bt, zb - bw / 2, zb + bw / 2)
        INSERTS[f"portal_insert_X_rail_{'BT'[k]}"] = bar
        FEATURES.append(("portal", f"X rail insert bar {'bottom top'.split()[k]}", f"{bw} x {bt} x {L['x_rail_len']-20:.0f} flat bar, tapped M5 at 60 (rail holes); bar centre {L['x_bar_shift']:.0f} mm outboard of the rail line", f"rail Z {zr:.0f}, bar Z {zb:.0f}, {L['seat_recess']:.0f} behind the front face"))
    p = p.cut(box(rx0 + 20, rx0 + 40, y0 - 0.1, y0 + L["seat_recess"], L["x_rail_z"][0], L["x_rail_z"][1]))
    FEATURES.append(("portal", "Rail-seat recesses (front face)", f"2 x 30 wide x {L['seat_recess']:.0f} deep + cross-link", "levelling pour; cast with the front face down"))
    # X screw channel
    cx0, cx1 = L["x_bf_x1"] - BF["l"] - 10, x1 + 1              # open at the right end for the drive stub
    p = p.cut(box(cx0, cx1, y0 - 0.1, y0 + L["x_chan_depth"], L["beam_zc"] - L["x_chan_w"] / 2, L["beam_zc"] + L["x_chan_w"] / 2))
    FEATURES.append(("portal", "X screw channel", f"{L['x_chan_w']:.0f} high x {L['x_chan_depth']:.0f} deep, with 5 mm seat pads for BK12/BF12", f"X {cx0:.0f} to {cx1:.0f}, centred Z {L['beam_zc']:.0f}; screw axis {L['x_screw_y']-y0:.0f} behind the face (D-108)"))
    seat = y0 + L["x_chan_depth"] - L["x_pad"]
    for nm, xa, xb in (("BK12", L["x_bk_x0"], L["x_bk_x0"] + BK["l"]), ("BF12", L["x_bf_x1"] - BF["l"], L["x_bf_x1"])):
        p = p.union(box(xa - 5, xb + 5, seat, y0 + L["x_chan_depth"] + 0.1, L["beam_zc"] - 32, L["beam_zc"] + 32))
        xx = (xa + xb) / 2
        INSERTS[f"portal_insert_X_{nm}"] = box(xx - 15, xx + 15, seat + 1, seat + 11, L["beam_zc"] - 30, L["beam_zc"] + 30)
        FEATURES.append(("portal", f"X {nm} insert plate", "30 x 60 x 10 steel, 2 x M5 tapped (VERIFY)", f"behind the channel floor at X {xx:.0f}"))
    # PVC cores between the legs only (sleeves pass through the legs)
    for zc in (L["beam_zc"] - 30, L["beam_zc"] + 30):
        p = p.cut(cyl("x", P["pvc_core_d"], (D["open_x1"] - 5) - (D["open_x0"] + 5), (D["open_x0"] + 5, 190, zc)))
    FEATURES.append(("portal", "PVC cores", f"2 x Ø{P['pvc_core_d']} capped pipe", f"Y 190, Z {L['beam_zc']-30:.0f} / {L['beam_zc']+30:.0f}, X {D['open_x0']+5:.0f} to {D['open_x1']-5:.0f} (between the legs)"))
    # joint sleeves: per leg 2 x Ø16 through the full height (M12 rod), dowel at the leg foot
    for side, xc in (("L", x0 + P["upright_w"] / 2), ("R", D["leg_r_x1"] - P["upright_w"] / 2)):
        for yy in (y0 + 30, y1 - 30):
            p = p.cut(cyl("z", 16, pz + 2, (xc, yy, -1)))
        p = p.cut(cyl("z", 12, 30, (xc, (y0 + y1) / 2, -1)))
        FEATURES.append(("portal", f"Joint sleeves, {side} leg", "2 x Ø16 tube through the full height (M12 rod to the base bar) + Ø12 dowel sleeve 30 deep at the foot", f"X {xc:+.0f}, Y {y0+30:.0f} / {y1-30:.0f}"))
    # ATC bracket insert on the right leg outer face (Phase 2), X motor bracket inserts on the beam top
    INSERTS["portal_insert_ATC"] = box(D["leg_r_x1"] - 10, D["leg_r_x1"], (y0 + y1) / 2 - 12.5, (y0 + y1) / 2 + 12.5, 60, 200)
    FEATURES.append(("portal", "ATC wheel bracket insert (Phase 2)", "25 x 10 x 140 bar, 2 x M8 tapped", f"right leg outer face X {D['leg_r_x1']:.0f}, Z 60 to 200"))
    for xx in (330, 430):
        INSERTS[f"portal_insert_Xmotor_{xx}"] = cyl("z", 20, 30, (xx, (y0 + y1) / 2 + 20, pz - 30))
    FEATURES.append(("portal", "X motor bracket inserts", "2 x M8 nut-on-rod", f"beam top Z {pz:.0f}, X 330 / 430, Y {(y0+y1)/2+20:.0f}"))
    for xx in (x0 + 120, x1 - 160):
        p = p.cut(cyl("z", 12, 40, (xx, (y0 + y1) / 2 - 25, pz - 40)))
    FEATURES.append(("portal", "Lifting points", "2 x M12 nut-on-rod, vertical", f"beam top, X {x0+120:.0f} / {x1-160:.0f}"))
    return p

# ---------------------------------------------------------------------------
# Machine assembly (table at Y centre, saddle at X 0, spindle nose at Z-top unless given)
# ---------------------------------------------------------------------------
def build(ty=None, xs=0.0, zn=None):
    ty = D["spindle_y"] if ty is None else ty
    zn = L["nose_top"] if zn is None else zn
    C = {}       # name -> (shape, colour)
    eg, steel, alu, black, blue, dark = (0.62, 0.62, 0.6), (0.75, 0.75, 0.78), (0.82, 0.84, 0.88), (0.15, 0.15, 0.15), (0.35, 0.5, 0.75), (0.3, 0.3, 0.3)
    C["base_casting"] = (base_casting(), eg)
    C["portal_casting"] = (portal_casting(), eg)
    for k, v in INSERTS.items():
        C[k] = (v, (0.45, 0.45, 0.45))
    # --- Y axis
    for k, x in enumerate((-L["y_rail_x"], L["y_rail_x"])):
        r, _ = rail(L["y_rail_len"], "y", (x, L["y_rail_y0"], 0), "z")
        C[f"Y_rail_{'LR'[k]}"] = (r, steel)
        for j, dy in enumerate((-P["y_block_pitch"] / 2, P["y_block_pitch"] / 2)):
            C[f"Y_block_{'LR'[k]}{j}"] = (place(block(), "y", (x, ty + dy, 0), "z"), blue)
    C["table"] = (box(-P["table_x"] / 2, P["table_x"] / 2, ty - P["table_y"] / 2, ty + P["table_y"] / 2, BLOCK["H"], BLOCK["H"] + P["table_t"]), alu)
    yb0 = L["y_bk_y0"]
    C["Y_BK12"] = (support("BK").rotate((0, 0, 0), (0, 0, 1), 90).translate((0, yb0, -L["chan_depth"])), steel)
    C["Y_BF12"] = (support("BF").rotate((0, 0, 0), (0, 0, 1), 90).translate((0, L["y_bf_y0"], -L["chan_depth"])), steel)
    stub = 34.0
    ys0 = yb0 - BK["lock"] - stub
    ylen = (L["y_bf_y0"] + BF["l"] + 10) - ys0
    L["y_screw_len"] = ylen
    C["Y_ballscrew"] = (ballscrew(ylen, stub).rotate((0, 0, 0), (0, 0, 1), 90).translate((0, ys0, L["y_screw_z"])), steel)
    C["Y_nut"] = (dfu_nut("z").rotate((0, 0, 0), (0, 0, 1), 90).translate((0, ty, L["y_screw_z"])), black)
    C["Y_nut_housing"] = (housing().rotate((0, 0, 0), (0, 0, 1), 90).translate((0, ty, BLOCK["H"])), alu)
    # Y drive folded (D-107): pulleys just in front of the spine face, motor alongside the right spine face under the table
    pb1 = yb0 - BK["lock"] - 3                                         # pulley body back face
    rot_m = lambda shp: shp.rotate((0, 0, 0), (0, 0, 1), -90)          # +X -> -Y
    C["Y_pulley_screw"] = (rot_m(pulley()).translate((0, pb1, L["y_screw_z"])), dark)
    mx, mz = sw / 2 + 10 + MOTOR_XY["sq"] / 2, -10.0
    C["Y_pulley_motor"] = (rot_m(pulley()).translate((mx, pb1, mz)), dark)
    C["Y_motor_plate"] = (box(sw / 2, mx + MOTOR_XY["sq"] / 2 + 4, pb1 + 1, pb1 + 9, mz - 40, mz + 30), alu)
    C["Y_motor"] = (rot_m(motor(MOTOR_XY)).translate((mx, pb1 + 9, mz)), black)
    C["Y_motor_bracket"] = (box(sw / 2, sw / 2 + 8, pb1 + 1, pb1 + 70, mz - 40, mz + 20), alu)
    cy, cz = (0 + mx) / 2, (L["y_screw_z"] + mz) / 2
    C["Y_belt"] = (box(-PULLEY["od"] / 2 - 2, mx + PULLEY["od"] / 2 + 2, pb1 - PULLEY["w"] + 3, pb1 - 3, min(L["y_screw_z"], mz) - PULLEY["od"] / 2 - 2, max(L["y_screw_z"], mz) + PULLEY["od"] / 2 + 2), dark)
    # --- X axis
    rx0 = D["portal_x0"] + (D["portal_w"] - L["x_rail_len"]) / 2
    for k, zr in enumerate(L["x_rail_z"]):
        r, _ = rail(L["x_rail_len"], "x", (rx0, P["beam_front"], zr), "-y")
        C[f"X_rail_{'BT'[k]}"] = (r, steel)
        for j, dx in enumerate((-P["x_block_pitch"] / 2, P["x_block_pitch"] / 2)):
            C[f"X_block_{'BT'[k]}{j}"] = (place(block(), "x", (xs + dx, P["beam_front"], zr), "-y"), blue)
    sz0 = L["beam_zc"] - 200 + 0                                          # saddle 400 tall
    sz0 = max(sz0, 100.0)
    C["saddle"] = (box(xs - P["saddle_w"] / 2, xs + P["saddle_w"] / 2, L["saddle_y0"], L["saddle_y1"], sz0, sz0 + L["saddle_h"]), alu)
    C["X_housing_spacer"] = (box(xs - HOUSING["l"] / 2, xs + HOUSING["l"] / 2, L["saddle_y1"], L["saddle_y1"] + L["x_spacer"], L["beam_zc"] - HOUSING["w"] / 2, L["beam_zc"] + HOUSING["w"] / 2), alu)
    C["X_nut_housing"] = (housing().rotate((0, 0, 0), (1, 0, 0), 90).translate((xs, L["saddle_y1"] + L["x_spacer"], L["beam_zc"])), alu)
    C["X_nut"] = (dfu_nut().translate((xs, L["x_screw_y"], L["beam_zc"])), black)
    ybk = P["beam_front"] + L["x_chan_depth"] - L["x_pad"]                  # seat pads (BK/BF base)
    C["X_BK12"] = (support("BK").mirror("YZ", (BK["l"] / 2, 0, 0)).rotate((0, 0, 0), (1, 0, 0), 90).translate((L["x_bk_x0"], ybk, L["beam_zc"])), steel)
    C["X_BF12"] = (support("BF").rotate((0, 0, 0), (1, 0, 0), 90).translate((L["x_bf_x1"] - BF["l"], ybk, L["beam_zc"])), steel)
    xs_left = L["x_bf_x1"] - BF["l"] - 10
    bk_out = L["x_bk_x0"] + BK["l"] + BK["lock"]                       # outer face of the BK lock nut
    pb0 = max(D["portal_x1"] + 4, bk_out + 3)                          # pulley body starts past the beam end
    stub = (pb0 + PULLEY["w"] + PULLEY["hub_l"] + 28) - bk_out        # through the pulley and the KFL000 inner ring
    xlen = bk_out + stub - xs_left
    L["x_screw_len"] = xlen
    C["X_ballscrew"] = (ballscrew(xlen, stub).mirror("YZ").translate((xs_left + xlen, L["x_screw_y"], L["beam_zc"])), steel)
    C["X_pulley_screw"] = (pulley().translate((pb0, L["x_screw_y"], L["beam_zc"])), dark)
    ob0 = pb0 + PULLEY["w"] + PULLEY["hub_l"] + 2
    vb = v_bearing()
    C["X_outboard_bearing"] = (vb.translate((ob0, L["x_screw_y"], L["beam_zc"])), steel) if vb is not None else None
    if C["X_outboard_bearing"] is None:
      C["X_outboard_bearing"] = (box(ob0, ob0 + 10, L["x_screw_y"] - 25, L["x_screw_y"] + 25, L["beam_zc"] - 25, L["beam_zc"] + 25)
                               .cut(cyl("x", 10, 12, (ob0 - 1, L["x_screw_y"], L["beam_zc"]))), steel)
    my, mzz = (D["portal_y0"] + D["portal_y1"]) / 2 + 20, D["beam_top"] + 12 + MOTOR_XY["sq"] / 2
    C["X_pulley_motor"] = (pulley().translate((pb0, my, mzz)), dark)
    C["X_motor_plate"] = (box(pb0 - 10, pb0 - 2, my - 40, my + 34, D["beam_top"], mzz + 34), alu)
    C["X_motor"] = (motor(MOTOR_XY).translate((pb0 - 10, my, mzz)), black)
    C["X_bracket"] = (box(D["portal_x1"] + 0.5, ob0 + 26, L["x_screw_y"] - 30, D["portal_y1"], L["beam_zc"] - 30, L["beam_zc"] - 26), alu)
    C["X_belt"] = (box(pb0 + 3, pb0 + PULLEY["w"] - 3, min(L["x_screw_y"], my) - PULLEY["od"] / 2 - 2, max(L["x_screw_y"], my) + PULLEY["od"] / 2 + 2, L["beam_zc"] - PULLEY["od"] / 2 - 2, mzz + PULLEY["od"] / 2 + 2), dark)
    # --- Z axis (rails on risers on the saddle front, short Z plate moves)
    zr0 = sz0 + 20
    for k, xr in enumerate((xs - P["z_rail_spacing"] / 2, xs + P["z_rail_spacing"] / 2)):
        C[f"Z_riser_{'LR'[k]}"] = (box(xr - 12.5, xr + 12.5, L["saddle_y0"] - L["z_riser"], L["saddle_y0"], zr0, zr0 + 350), alu)
        r, _ = rail(350, "z", (xr, L["saddle_y0"] - L["z_riser"], zr0), "-y")
        C[f"Z_rail_{'LR'[k]}"] = (r, steel)
    zp0 = zn + 40
    zb = zp0 + 120
    for k, xr in enumerate((xs - P["z_rail_spacing"] / 2, xs + P["z_rail_spacing"] / 2)):
        for j, dz in enumerate((-P["z_block_pitch"] / 2, P["z_block_pitch"] / 2)):
            C[f"Z_block_{'LR'[k]}{j}"] = (place(block(), "z", (xr, L["saddle_y0"] - L["z_riser"], zb + dz), "-y"), blue)
    C["Z_plate"] = (box(xs - 70, xs + 70, L["zp_y0"], L["zp_y1"], zp0, zp0 + L["zp_h"]), alu)
    C["Z_nut_housing"] = (housing().rotate((0, 0, 0), (0, 1, 0), -90).rotate((0, 0, 0), (0, 0, 1), 90).rotate((0, 0, 0), (0, 0, 1), 180)
                          .translate((xs, L["zp_y1"], zb)) if False else box(xs - HOUSING["w"] / 2, xs + HOUSING["w"] / 2, L["zp_y1"], L["zp_y1"] + HOUSING["h"], zb - HOUSING["l"] / 2, zb + HOUSING["l"] / 2), alu)
    C["Z_nut"] = (cyl("z", NUT["body_d"], NUT["len"], (xs, L["z_screw_y"], zb - NUT["len"] / 2)), black)
    zsup = sz0 + L["saddle_h"]
    C["Z_BK12_bracket"] = (box(xs - 45, xs + 45, L["z_screw_y"] - 15, L["saddle_y1"], zsup, zsup + 15), alu)
    C["Z_BK12"] = (box(xs - BK["w"] / 2, xs + BK["w"] / 2, L["z_screw_y"] - BK["h"] + BK["ctr"], L["z_screw_y"] + BK["ctr"] - 0, zsup + 15, zsup + 15 + BK["l"]).cut(cyl("z", 12, BK["l"] + 2, (xs, L["z_screw_y"], zsup + 14))), steel)
    zs_bot = zr0 + 10
    C["Z_ballscrew"] = (cyl("z", SCREW["d"], (zsup + 15) - zs_bot, (xs, L["z_screw_y"], zs_bot)).union(cyl("z", 12, BK["l"] + BK["lock"], (xs, L["z_screw_y"], zsup + 15))).union(cyl("z", 10, 15, (xs, L["z_screw_y"], zsup + 15 + BK["l"] + BK["lock"]))), steel)
    zc0 = zsup + 15 + BK["l"] + BK["lock"]
    C["Z_coupling"] = (cyl("z", COUPLING["d"], COUPLING["l"], (xs, L["z_screw_y"], zc0 + 2)), dark)
    zm = zc0 + 2 + COUPLING["l"] + 4
    C["Z_motor_mount"] = (box(xs - 35, xs + 35, L["z_screw_y"] - 35, L["z_screw_y"] + 35, zc0 - 3, zm).cut(cyl("z", 40, zm - zc0 + 5, (xs, L["z_screw_y"], zc0 - 4))), alu)
    C["Z_motor"] = (motor(MOTOR_Z).rotate((0, 0, 0), (0, 1, 0), 90).translate((xs, L["z_screw_y"], zm)), black)
    # spindle + clamp
    sy = L["zp_y0"] - CLAMP["offset"]
    C["spindle_clamp"] = (box(xs - CLAMP["w"] / 2, xs + CLAMP["w"] / 2, sy - SPINDLE["d"] / 2 - 10, L["zp_y0"], zn + 70, zn + 70 + CLAMP["h"]).cut(cyl("z", SPINDLE["d"], CLAMP["h"] + 2, (xs, sy, zn + 69))), alu)
    C["spindle"] = (cyl("z", SPINDLE["d"], SPINDLE["body"], (xs, sy, zn + SPINDLE["nose"])).union(cyl("z", SPINDLE["nose_d"], SPINDLE["nose"], (xs, sy, zn))), (0.9, 0.9, 0.92))
    # home sensors (E10) as envelopes: M12 x 60
    # Y: on the left spine face near the front, pointing up at a flag under the table's left overhang
    vs = v_sensor()
    C["home_sensor_Y"] = ((vs.translate((-sw / 2 - 20, D["spine_y0"] + 60, 15)) if vs is not None else cyl("z", 12, 50, (-sw / 2 - 20, D["spine_y0"] + 60, -35))), (0.9, 0.6, 0.1))
    # X: beyond the beam's right end above the top, facing -X at the saddle's right edge
    hx = (L["xs_max"] + P["saddle_w"] / 2 + 5, (L["saddle_y0"] + L["saddle_y1"]) / 2, D["beam_top"] + 45)
    C["home_sensor_X"] = ((_apply(vs.val(), _mat(ROT_B, hx)) if vs is not None else cyl("x", 12, 55, hx)), (0.9, 0.6, 0.1))
    if vs is not None:
        C["home_sensor_X"] = (cq.Workplane().add(C["home_sensor_X"][0]), C["home_sensor_X"][1])
    # Z: on the saddle front beside the right rail, facing a flag on the Z plate
    hz = (xs + 85, L["saddle_y0"] - 58, zsup - 25)
    C["home_sensor_Z"] = ((cq.Workplane().add(_apply(vs.val(), _mat(((1, 0, 0), (0, 0, 1), (0, -1, 0)), hz))) if vs is not None
                           else box(xs + 79, xs + 91, L["saddle_y0"] - 45, L["saddle_y0"], zsup - 31, zsup - 19)), (0.9, 0.6, 0.1))
    # ATC wheel envelope (Phase 2)
    C["ATC_wheel_envelope"] = (cq.Workplane("YZ").circle(D["wheel_d"] / 2).extrude(P["wheel_t"]).translate((D["pickup_x"] - P["wheel_t"] / 2, sy, D["fork_z"] - D["wheel_d"] / 2)), (0.7, 0.85, 0.7))
    return C

def clashes(C, ignore):
    names = list(C)
    bad = []
    bbs = {n: C[n][0].val().BoundingBox() for n in names}
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            if (a, b) in ignore or (b, a) in ignore or any(p in a and q in b or p in b and q in a for p, q in ignore):
                continue
            A, B = bbs[a], bbs[b]
            if A.xmax <= B.xmin or B.xmax <= A.xmin or A.ymax <= B.ymin or B.ymax <= A.ymin or A.zmax <= B.zmin or B.zmax <= A.zmin:
                continue
            try:
                v = C[a][0].intersect(C[b][0]).val().Volume()
            except Exception:
                v = 0
            if v > 1.0:
                bad.append((a, b, v))
    return bad

# pairs that touch by design (bolted faces, shafts in bores, inserts in castings)
TOUCH = [("rail", "block"), ("insert", "casting"), ("ballscrew", "nut"), ("ballscrew", "BK12"), ("ballscrew", "BF12"), ("ballscrew", "pulley"), ("ballscrew", "outboard"), ("belt", "pulley"), ("belt", "ballscrew"), ("belt", "motor"), ("motor", "plate"), ("pulley", "plate"), ("bracket", "plate"), ("bracket", "outboard"), ("housing", "spacer"), ("bracket", "casting"), ("insert", "bracket"),
         ("nut", "housing"), ("motor", "pulley"), ("motor", "bracket"), ("motor", "mount"), ("ballscrew", "coupling"), ("coupling", "motor"),
         ("spindle", "clamp"), ("Z_BK12", "bracket"), ("ballscrew", "Z_motor_mount"), ("coupling", "mount")]

if __name__ == "__main__":
    poses = {"centre": dict(), "front-left-down": dict(ty=L["ty_min"], xs=L["xs_min"], zn=L["nose_bot"]),
             "back-right-up": dict(ty=L["ty_max"], xs=L["xs_max"], zn=L["nose_top"])}
    results = {}
    ext = {}
    for nm, kw in poses.items():
        INSERTS.clear(); FEATURES.clear()
        C = build(**kw)
        results[nm] = clashes(C, TOUCH)
        for n, (shp, _) in C.items():
            if n.startswith("ATC"):
                continue
            bb = shp.val().BoundingBox()
            for k, v, lo in (("x0", bb.xmin, 1), ("x1", bb.xmax, 0), ("y0", bb.ymin, 1), ("y1", bb.ymax, 0), ("z0", bb.zmin, 1), ("z1", bb.zmax, 0)):
                if k not in ext or (v < ext[k] if lo else v > ext[k]):
                    ext[k] = round(v, 1)
        print(nm, "clashes:", [(a, b, round(v)) for a, b, v in results[nm]])
    INSERTS.clear(); FEATURES.clear()
    C = build()
    asm = cq.Assembly(name="Type0")
    for n, (shp, col) in C.items():
        asm.add(shp, name=n, color=cq.Color(*col))
    asm.save(str(OUT / "type0_assembly.step"))
    base, portal = C["base_casting"][0], C["portal_casting"][0]
    cq.exporters.export(base, str(OUT / "base_casting.step"))
    cq.exporters.export(portal, str(OUT / "portal_casting.step"))
    kg = {k: C[k][0].val().Volume() * EG_RHO for k in ("base_casting", "portal_casting")}
    json.dump(dict(L=L, kg=kg, extents=ext, features=FEATURES, clashes={k: [(a, b, v) for a, b, v in r] for k, r in results.items()}),
              open(OUT / "assembly_data.json", "w"), indent=1, default=str)
    print("masses", {k: round(v, 1) for k, v in kg.items()}, "stack check", check_stack())

#!/usr/bin/env python3
"""V4 frame options (Task 2): mass and hand stiffness of the base tray and upright choices.

Beam formulas only (Timoshenko beam elements assembled into one small 3D frame; no FEA,
no plates). Stdlib only. Lengths in mm, forces in N, results in um per 100 N.
Lengths come from tools/v4_sizes.py sizes(); every other input is named below with its source
or marked "estimate". Run: PYTHONUTF8=1 python tools/v4_frame_stiffness.py

What is modelled: the tray as a grillage (one beam along X at the gantry line, one along Y on
each rail line out to the work), the table across the rails, two steel uprights, the steel beam,
rigid links for the joints. The load is a pair: +100 N at the spindle nose and
-100 N at the table under it (the cutting force acts on both), so the figure is nose against
table. At the wheel pickup the pair is nose against the base's right side (wheel mount there).

Rigid (not modelled, all make the real machine softer): the upright-to-tray and beam-to-upright
bolted joints, T-slot connections inside the tray, the Z axis and its plates, X and Y carriages
and rails, the table, the stand. So these figures RANK the options; they do not predict the
machine's stiffness.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v4_sizes  # noqa: E402
from v4_sizes import sizes, UPRIGHT_W, TABLE_X  # noqa: E402

S = sizes()
F = 100.0                      # N, the load of every figure

# ---- Materials -----------------------------------------------------------------------
E_ST, G_ST, RHO_ST = 205e3, 79e3, 7.85e-6     # steel, N/mm^2, kg/mm^3
E_AL, G_AL = 69e3, 26e3                       # 6063/6082 extrusion (KJN does not state the alloy: estimate)
E_EG, G_EG = 25e3, 10e3                       # EG: the project's pass mark (beam-assessment.md); G = E/2.5
RHO_EG = 2.3e-6                               # kg/mm^3 (beam-assessment.md: 12.7 L -> 29.3 kg)
EPOXY_FRACTION = 0.11                         # by weight (design doc: Ampreg 30, about 11 %)
RHO_SAND = 1.6e-6                             # dry sand, loose (estimate)

# ---- Heights and offsets (not in sizes(); estimates) ---------------------------------
TABLE_STACK = 75.0       # tray top to table top: rail plate 15 + HGH20 rail and block 30 + table 30 (estimate)
BEAM_ABOVE_TABLE = 220.0  # table top to beam centre: v3 Z plate X-block rows (D-179 holes Z 181.5 to 396,
                          # table top Z 70) put the beam centre about 219 above the table (estimate)
NOSE_LOW = 25.0          # table to nose, lowest (D-267): worst case, longest lever below the beam
SPINDLE_AHEAD = 235.0    # spindle axis in front of the beam centre: D-106 (175 from the beam face) + 60 (estimate)
CARRIAGE_KG = 18.0       # X carriage + Z + spindle (tools/portal_overhang.py list, Phase 2 worst case)
PICKUP_X = TABLE_X / 2 + v4_sizes.UPRIGHT_GAP + UPRIGHT_W + v4_sizes.WHEEL_PICKUP_OFFSET  # 415, as v4_sizes

# ---- Geometry from sizes() -----------------------------------------------------------
TRAY_W = S["base_width"] - 2 * UPRIGHT_W      # 500: sizes() base_width includes the two uprights
TRAY_L = S["base_len"]                        # 670 along Y
UP_X = TRAY_W / 2 + UPRIGHT_W / 2             # upright centre, 290
BEAM_X0 = -S["base_width"] / 2                # beam flush with the left upright's outer face
BEAM_X1 = BEAM_X0 + S["beam_len"]


# ---- Sections ------------------------------------------------------------------------
def hollow_rect(b, d, t, ro=None, ri=None, step=0.25):
    """Rectangular hollow section, b along local y, d along local z, rounded corners.
    Corner radii: outer 2t, inner t (EN 10219 typical; assumption). Numerical strip sum."""
    ro = 2 * t if ro is None else ro
    ri = t if ri is None else ri

    def inside(y, z, bb, dd, r):
        ay, az = abs(y) - (bb / 2 - r), abs(z) - (dd / 2 - r)
        if abs(y) > bb / 2 or abs(z) > dd / 2:
            return False
        return not (ay > 0 and az > 0 and ay * ay + az * az > r * r)

    A = Iy = Iz = 0.0
    da = step * step
    ny, nz = int(b / step), int(d / step)
    for i in range(ny):
        y = -b / 2 + (i + 0.5) * step
        for j in range(nz):
            z = -d / 2 + (j + 0.5) * step
            if inside(y, z, b, d, ro) and not inside(y, z, b - 2 * t, d - 2 * t, ri):
                A += da
                Iy += da * z * z      # resists deflection along z
                Iz += da * y * y      # resists deflection along y
    rm = (ro + ri) / 2
    bm, dm = b - t, d - t
    Am = bm * dm - (4 - math.pi) * rm * rm
    pm = 2 * (bm + dm) - (8 - 2 * math.pi) * rm
    J = 4 * Am * Am * t / pm                          # Bredt
    void = (b - 2 * t) * (d - 2 * t) - (4 - math.pi) * ri * ri
    return dict(A=A, Iy=Iy, Iz=Iz, J=J, Asy=A * b / (b + d), Asz=A * d / (b + d), void=void)


def rect(b, d):
    """Solid rectangle, b along local y, d along local z."""
    a, c = max(b, d), min(b, d)
    J = a * c ** 3 * (1 / 3 - 0.21 * c / a * (1 - c ** 4 / (12 * a ** 4)))
    return dict(A=b * d, Iy=b * d ** 3 / 12, Iz=d * b ** 3 / 12, J=J, Asy=5 / 6 * b * d, Asz=5 / 6 * b * d)


def steel(sec):
    return dict(EA=E_ST * sec["A"], EIy=E_ST * sec["Iy"], EIz=E_ST * sec["Iz"], GJ=G_ST * sec["J"],
                GAy=G_ST * sec["Asy"], GAz=G_ST * sec["Asz"])


# KJN Aluminium Profiles datasheet values, read by curl from the KJN product pages on 2026-11-24
# (www.aluminium-profile.co.uk). KJN gives Ix and Iy only; the torsion constant is not published.
KJN_90x90H = dict(I=299.80e4, kg_m=10.50, w=90.0)     # KJN990500: Ix = Iy = 299.80 cm^4, 10.50 kg/m
KJN_80x160H_IR = dict(I_strong=1228.33e4, I_weak=360.89e4, kg_m=13.52)  # IR26526 (price on application)
RHO_AL = 2.70e-6
J_SLOT_FACTOR = 0.06     # J of a slotted profile as a share of Ix + Iy (estimate: open T-slots; not KJN data)

BEAM = hollow_rect(120, 120, 8)                       # v3 beam, SHS 120 x 120 x 8 (D-177, design doc)
UPRIGHTS = {
    # local y = global X (the 80 width of sizes()), local z = global Y
    "U1 RHS 160x80x8": dict(sec=hollow_rect(80, 160, 8), x_width=80, y_depth=160),
    "U2 plate 50x150": dict(sec=rect(50, 150), x_width=50, y_depth=150),
}
UPRIGHT_ALT = {"plate 30x300": rect(30, 300)}         # checked, printed for comparison


RAIL_X = TABLE_X / 2 - 25.0    # Y rails at X +/-205, under the table edges (estimate)
RAIL_PLATE = (50.0, 20.0)      # bright flat bar under each Y rail, width x thickness (the priced bar)
RAIL_I = 0.75 * 20 * 17.5 ** 3 / 12   # HGR20 rail, 25 % off a solid bar (estimate, as z_plate_stiffness.py)
END_PLATE_T = 20.0             # B and C: steel end plate on each tray end, 670 x tray height (estimate)
TABLE_SEC = (330.0, 30.0)      # table plate along the X span between the rails, Y width x thickness,
                               # 6082 (estimate; the table is not designed yet)


def kjn_pieces(layout):
    """Profile pieces of one tray: list of (count, length, axis)."""
    L, W, w = TRAY_L, TRAY_W, KJN_90x90H["w"]
    if layout == "A":
        return [(2, L, "Y"), (3, W - 2 * w, "X")]
    if layout == "B":
        return [(4, W, "X")]
    if layout == "C":
        return [(8, W, "X")]
    raise ValueError(layout)


def part(E, G, b, d, y, z, I_own=None, J=None, A=None, As=None, eg=False):
    """One piece of a composite section; b across (horizontal), d up."""
    A = b * d if A is None else A
    Iv = b * d ** 3 / 12 if I_own is None else I_own
    Ih = d * b ** 3 / 12 if I_own is None else I_own
    return dict(E=E, G=G, A=A, Iv=Iv, Ih=Ih, J=rect(b, d)["J"] if J is None else J,
                As=5 / 6 * A if As is None else As, y=y, z=z, eg=eg)


def composite(parts, bonded, block=None):
    """Bonded: one section (parallel axis about the E-weighted centroid), EG counted.
    Not bonded: each piece on its own axes, EG left out (lower bound)."""
    ps = [p for p in parts if bonded or not p["eg"]]
    EA = sum(p["E"] * p["A"] for p in ps)
    if bonded:
        yc = sum(p["E"] * p["A"] * p["y"] for p in ps) / EA
        zc = sum(p["E"] * p["A"] * p["z"] for p in ps) / EA
        EIy = sum(p["E"] * (p["Iv"] + p["A"] * (p["z"] - zc) ** 2) for p in ps)
        EIz = sum(p["E"] * (p["Ih"] + p["A"] * (p["y"] - yc) ** 2) for p in ps)
    else:
        EIy = sum(p["E"] * p["Iv"] for p in ps)
        EIz = sum(p["E"] * p["Ih"] for p in ps)
    GJ = sum(p["G"] * p["J"] for p in ps)
    if bonded and block:
        GJ = max(GJ, G_EG * rect(*block)["J"])          # the filled tray strip as one solid block
    GA = sum(p["G"] * p["As"] for p in ps)
    return dict(EA=EA, EIy=EIy, EIz=EIz, GJ=GJ, GAy=GA, GAz=GA)


def tray(layout, bonded):
    """Tray as a grillage: one beam along X at the gantry line (full 670 deep section) and one beam
    along Y on each rail line (its share of the 500 wide section), from the work to the gantry line.
    Not bonded: metal pieces only, each on its own (lower bound: EG cracked or not bonded, joints slip).
    Bonded: metal + EG pockets as one section (upper bound, EG bonded at 25 GPa: assumed)."""
    w, A_al, I_al = KJN_90x90H["w"], KJN_90x90H["kg_m"] / RHO_AL / 1000.0, KJN_90x90H["I"]
    J_al, As_al = J_SLOT_FACTOR * 2 * I_al, 0.4 * A_al       # webs only (estimate)
    prof = lambda y, z: part(E_AL, G_AL, w, w, y, z, I_own=I_al, J=J_al, A=A_al, As=As_al)
    if layout == "A":
        # X: 3 cross members (front, under the gantry, back), 320 long between the side members,
        # modelled as running the full width (side members rigid). Pockets 320 x 200 x 90.
        h = 90.0
        xs = [prof(y, 45.0) for y in (-290.0, 0.0, 290.0)]
        xs += [part(E_EG, G_EG, 200.0, h, y, h / 2, eg=True) for y in (-145.0, 145.0)]
        ys = [prof(0.0, 45.0), part(E_EG, G_EG, (TRAY_W - 2 * w) / 2, h, 0.0, h / 2, eg=True)]
        eg_vol = 2 * 200.0 * h * (TRAY_W - 2 * w)
        end_plates = 0.0
    else:
        # X: 4 profiles per layer at Y -290, -45, 45, 290 (two pockets 155 wide), 1 or 2 layers.
        h = 90.0 if layout == "B" else 180.0
        zs = [45.0] if layout == "B" else [45.0, 135.0]
        xs = [prof(y, z) for y in (-290.0, -45.0, 45.0, 290.0) for z in zs]
        xs += [part(E_EG, G_EG, 155.0, h, y, h / 2, eg=True) for y in (-167.5, 167.5)]
        # Y: nothing aluminium runs along Y; the EG (profiles counted as EG, conservative) and the
        # steel end plate (at the tray end, 45 outboard of the rail line: lumped into it)
        ys = [part(E_EG, G_EG, TRAY_W / 2, h, 0.0, h / 2, eg=True),
              part(E_ST, G_ST, END_PLATE_T, h, 0.0, h / 2)]
        eg_vol = 2 * 155.0 * h * TRAY_W
        end_plates = 2 * TRAY_L * h * END_PLATE_T * RHO_ST
    pb, pt = RAIL_PLATE
    ys += [part(E_ST, G_ST, pb, pt, 0.0, h + pt / 2),
           part(E_ST, G_ST, 20.0, 17.5, 0.0, h + pt + 8.75, I_own=RAIL_I)]
    al_len = sum(c * l for c, l, _ in kjn_pieces(layout))
    return dict(px=composite(xs, bonded, (TRAY_L, h)), py=composite(ys, bonded, (TRAY_W / 2, h)), h=h,
                m_al=al_len / 1000 * KJN_90x90H["kg_m"], m_eg=eg_vol * RHO_EG, eg_vol=eg_vol,
                al_len=al_len, m_end=end_plates)


LINK = dict(EA=1e14, EIy=1e17, EIz=1e17, GJ=1e17, GAy=1e14, GAz=1e14)   # rigid joint


# ---- 3D frame solver -----------------------------------------------------------------
def element_k(L, p):
    """Local 12x12 Timoshenko beam stiffness. Dofs per node: ux uy uz rx ry rz."""
    k = [[0.0] * 12 for _ in range(12)]

    def put(i, j, v):
        k[i][j] += v

    a = p["EA"] / L
    t = p["GJ"] / L
    for (i, j, v) in ((0, 0, a), (6, 6, a), (0, 6, -a), (6, 0, -a), (3, 3, t), (9, 9, t), (3, 9, -t), (9, 3, -t)):
        put(i, j, v)
    # bending with deflection along y (rotation rz): EIz, shear GAy
    for (EI, GA, dv, dr, s) in ((p["EIz"], p["GAy"], 1, 5, 1.0), (p["EIy"], p["GAz"], 2, 4, -1.0)):
        phi = 12 * EI / (GA * L * L)
        c = EI / (L ** 3 * (1 + phi))
        m = [[12, 6 * L * s, -12, 6 * L * s],
             [6 * L * s, (4 + phi) * L * L, -6 * L * s, (2 - phi) * L * L],
             [-12, -6 * L * s, 12, -6 * L * s],
             [6 * L * s, (2 - phi) * L * L, -6 * L * s, (4 + phi) * L * L]]
        idx = [dv, dr, 6 + dv, 6 + dr]
        for r in range(4):
            for q in range(4):
                put(idx[r], idx[q], c * m[r][q])
    return k


def axes(p1, p2, ref):
    ex = [b - a for a, b in zip(p1, p2)]
    L = math.sqrt(sum(v * v for v in ex))
    ex = [v / L for v in ex]
    d = sum(a * b for a, b in zip(ref, ex))
    ey = [r - d * e for r, e in zip(ref, ex)]
    n = math.sqrt(sum(v * v for v in ey))
    if n < 1e-9:
        raise ValueError("reference axis along member")
    ey = [v / n for v in ey]
    ez = [ex[1] * ey[2] - ex[2] * ey[1], ex[2] * ey[0] - ex[0] * ey[2], ex[0] * ey[1] - ex[1] * ey[0]]
    return L, [ex, ey, ez]


class Frame:
    def __init__(self):
        self.nodes, self.elems = [], []

    def node(self, x, y, z, new=False):
        for i, n in enumerate([] if new else self.nodes):
            if abs(n[0] - x) < 1e-6 and abs(n[1] - y) < 1e-6 and abs(n[2] - z) < 1e-6:
                return i
        self.nodes.append((x, y, z))
        return len(self.nodes) - 1

    def elem(self, a, b, props, ref):
        self.elems.append((a, b, props, ref))

    def solve(self, loads, fixed):
        """loads: {(node, dof): value}; fixed: list of (node, dof). Returns displacements."""
        n = 6 * len(self.nodes)
        K = [[0.0] * n for _ in range(n)]
        for a, b, p, ref in self.elems:
            L, R = axes(self.nodes[a], self.nodes[b], ref)
            kl = element_k(L, p)
            T = [[0.0] * 12 for _ in range(12)]
            for blk in range(4):
                for r in range(3):
                    for c in range(3):
                        T[3 * blk + r][3 * blk + c] = R[r][c]
            kt = [[sum(kl[i][m] * T[m][j] for m in range(12)) for j in range(12)] for i in range(12)]
            kg = [[sum(T[m][i] * kt[m][j] for m in range(12)) for j in range(12)] for i in range(12)]
            dofs = [6 * a + d for d in range(6)] + [6 * b + d for d in range(6)]
            for i in range(12):
                for j in range(12):
                    K[dofs[i]][dofs[j]] += kg[i][j]
        f = [0.0] * n
        for (nd, d), v in loads.items():
            f[6 * nd + d] += v
        fix = {6 * nd + d for nd, d in fixed}
        free = [i for i in range(n) if i not in fix]
        A = [[K[i][j] for j in free] + [f[i]] for i in free]
        m = len(free)
        for c in range(m):                                   # Gauss, partial pivoting
            p = max(range(c, m), key=lambda r: abs(A[r][c]))
            A[c], A[p] = A[p], A[c]
            for r in range(c + 1, m):
                fac = A[r][c] / A[c][c]
                if fac:
                    for j in range(c, m + 1):
                        A[r][j] -= fac * A[c][j]
        x = [0.0] * m
        for r in range(m - 1, -1, -1):
            x[r] = (A[r][m] - sum(A[r][j] * x[j] for j in range(r + 1, m))) / A[r][r]
        u = [0.0] * n
        for i, v in zip(free, x):
            u[i] = v
        self.u = u
        return u

    def elem_force(self, k_idx):
        a, b, p, ref = self.elems[k_idx]
        L, R = axes(self.nodes[a], self.nodes[b], ref)
        ue = self.u[6 * a:6 * a + 6] + self.u[6 * b:6 * b + 6]
        ul = [sum(R[r][c] * ue[3 * blk + c] for c in range(3)) for blk in range(4) for r in range(3)]
        kl = element_k(L, p)
        return [sum(kl[i][j] * ul[j] for j in range(12)) for i in range(12)]


X_, Y_, Z_ = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)


def build(layout, upright, bonded, beam_props=None, x_load=0.0, second="table"):
    """Frame for one option. Returns frame, nose node, partner node, upright element indices."""
    fr = Frame()
    t = tray(layout, bonded)
    h = t["h"]
    zt = h + TABLE_STACK
    zb = zt + BEAM_ABOVE_TABLE
    up_top = zb - 60.0
    # Horizontal members use ref Y_ so that local z is global Z (EIy = vertical bending).
    # Tray: beam along X at the gantry line, at the tray's mid-height
    xt = sorted({-TRAY_W / 2, -RAIL_X, 0.0, RAIL_X, TRAY_W / 2})
    tn = [fr.node(x, 0, h / 2) for x in xt]
    for a, b in zip(tn, tn[1:]):
        fr.elem(a, b, t["px"], Y_)
    b_l, b_0, b_r = tn[0], tn[2], tn[-1]
    # Rail lines along Y, from the gantry line out to the work; table across them (6082, estimate)
    tb = dict(EA=E_AL * TABLE_SEC[0] * TABLE_SEC[1], EIy=E_AL * rect(*TABLE_SEC)["Iy"],
              EIz=E_AL * rect(*TABLE_SEC)["Iz"], GJ=G_AL * rect(*TABLE_SEC)["J"],
              GAy=G_AL * 5 / 6 * TABLE_SEC[0] * TABLE_SEC[1], GAz=G_AL * 5 / 6 * TABLE_SEC[0] * TABLE_SEC[1])
    zt_mid = zt - TABLE_SEC[1] / 2
    tx = sorted({-RAIL_X, max(-RAIL_X, min(RAIL_X, x_load)), RAIL_X})
    tbl = [fr.node(x, -SPINDLE_AHEAD, zt_mid) for x in tx]
    for a, b in zip(tbl, tbl[1:]):
        fr.elem(a, b, tb, Y_)
    for side in (-1, 1):
        g = fr.node(side * RAIL_X, 0, h / 2)
        r = fr.node(side * RAIL_X, -SPINDLE_AHEAD, h / 2)
        fr.elem(g, r, t["py"], X_)                         # along -Y; ref X_ gives local z = global Z
        fr.elem(r, fr.node(side * RAIL_X, -SPINDLE_AHEAD, zt_mid), LINK, X_)   # rail and blocks rigid
    table_mid = fr.node(max(-RAIL_X, min(RAIL_X, x_load)), -SPINDLE_AHEAD, zt_mid)
    up = steel(UPRIGHTS[upright]["sec"])
    ups = []
    beam_nodes = {}
    for side, bn in ((-1, b_l), (1, b_r)):
        foot = fr.node(side * UP_X, 0, h)
        top = fr.node(side * UP_X, 0, up_top)
        fr.elem(bn, foot, LINK, Z_)                        # bolted face on the tray side: rigid
        ups.append(len(fr.elems))
        fr.elem(foot, top, up, X_)                         # local y = global X
        bc = fr.node(side * UP_X, 0, zb)
        fr.elem(top, bc, LINK, X_)                         # beam on top of the upright: rigid
        beam_nodes[side * UP_X] = bc
    xs = sorted({BEAM_X0, -UP_X, UP_X, PICKUP_X, BEAM_X1, x_load})
    bp = beam_props or steel(BEAM)
    prev = None
    for x in xs:
        nd = beam_nodes.get(x, None)
        if nd is None:
            nd = fr.node(x, 0, zb)
        if prev is not None:
            fr.elem(prev, nd, bp, Y_)
        prev = nd
    carriage = fr.node(x_load, 0, zb)
    nose = fr.node(x_load, -SPINDLE_AHEAD, zt + NOSE_LOW)
    fr.elem(carriage, nose, LINK, X_)                      # Z axis, carriages: rigid
    # The partner point sits where the nose is (a separate node), so the load pair is balanced
    # (no couple). The tool length is left out: it is rigid here and the same for every option.
    part = fr.node(x_load, -SPINDLE_AHEAD, zt + NOSE_LOW, new=True)
    if second == "table":
        fr.elem(table_mid, part, LINK, X_)                 # the work, fixed to the table
    else:
        fr.elem(b_r, part, LINK, X_)                       # wheel fork, mounted on the tray's right side
    return fr, nose, part, ups, (b_l, b_0, b_r), carriage


def compliance(layout, upright, bonded, d, x_load=0.0, second="table", beam_props=None, fix_node=1):
    """um per 100 N, nose against partner, along global dof d (0 X, 1 Y, 2 Z)."""
    fr, nose, part, ups, bnodes, _ = build(layout, upright, bonded, beam_props, x_load, second)
    fr.solve({(nose, d): F, (part, d): -F}, [(bnodes[fix_node], k) for k in range(6)])
    return (fr.u[6 * nose + d] - fr.u[6 * part + d]) * 1000.0, fr, nose, part, ups


def sag_offset(layout, upright):
    """Nose Z sag under the carriage weight at the pickup, less that at the centre (um).
    Tray held at its 3 nodes (stand taken as rigid)."""
    out = []
    for x in (0.0, PICKUP_X):
        fr, nose, part, ups, bn, car = build(layout, upright, True, x_load=x)
        # weight at the nose (235 forward), so the beam's twist is in: an upper bound
        fr.solve({(nose, 2): -CARRIAGE_KG * 9.81}, [(n, k) for n in bn for k in range(6)])
        out.append(fr.u[6 * nose + 2] * 1000.0)
    return out[1] - out[0]


def frame_mass(layout, upright):
    t = tray(layout, True)
    h = t["h"]
    up_len = h + TABLE_STACK + BEAM_ABOVE_TABLE - 60.0       # from the tray bottom to the beam's underside
    m_up = 2 * UPRIGHTS[upright]["sec"]["A"] * up_len * RHO_ST
    m_beam = BEAM["A"] * S["beam_len"] * RHO_ST
    return dict(tray_al=t["m_al"], eg=t["m_eg"], end=t["m_end"], uprights=m_up, beam=m_beam, up_len=up_len,
                total=t["m_al"] + t["m_eg"] + t["m_end"] + m_up + m_beam)


def checks():
    """Asserts that test the model, not its inputs."""
    # 1. One element against the cantilever formula (bending + shear)
    fr = Frame()
    a, b = fr.node(0, 0, 0), fr.node(500, 0, 0)
    p = steel(BEAM)
    fr.elem(a, b, p, Y_)
    fr.solve({(b, 2): -1000.0}, [(a, k) for k in range(6)])
    exact = 1000 * 500 ** 3 / (3 * p["EIy"]) + 1000 * 500 / p["GAz"]
    assert abs(-fr.u[6 * b + 2] / exact - 1) < 1e-6, "cantilever"
    # 2. Overhanging beam on two pins: tip = P a^2 (L + a) / 3EI; a = 0 gives zero at the support
    for ov in (0.0, 100.0, PICKUP_X - UP_X):
        fr = Frame()
        n0, n1 = fr.node(0, 0, 0), fr.node(2 * UP_X, 0, 0)
        stiff = dict(p, GAz=1e18, GAy=1e18)
        if ov > 0:
            n2 = fr.node(2 * UP_X + ov, 0, 0)
            fr.elem(n0, n1, stiff, Y_)
            fr.elem(n1, n2, stiff, Y_)
        else:
            n2 = n1
            fr.elem(n0, n1, stiff, Y_)
        fr.solve({(n2, 2): -F}, [(n0, 0), (n0, 1), (n0, 2), (n0, 3), (n1, 1), (n1, 2), (n0, 5)])
        exact = F * ov ** 2 * (2 * UP_X + ov) / (3 * p["EIy"])
        assert abs(-fr.u[6 * n2 + 2] - exact) <= 1e-9 + 1e-6 * exact, "overhang"
    up = next(iter(UPRIGHTS))
    # 3. Reciprocity (Maxwell): X response to a Z pair equals Z response to an X pair
    _, frz, nz, pz, _ = compliance("B", up, True, 2, x_load=120.0)
    _, frx, nx, px, _ = compliance("B", up, True, 0, x_load=120.0)
    xz = frz.u[6 * nz + 0] - frz.u[6 * pz + 0]
    zx = frx.u[6 * nx + 2] - frx.u[6 * px + 2]
    assert abs(xz - zx) <= 1e-6 * max(abs(xz), 1e-12) + 1e-12, "reciprocity"
    # 4. Mid-span Z load: equal upright axial forces; mirror positions give equal Z figures
    _, fr, _, _, ups = compliance("B", up, True, 2, x_load=0.0)
    n_l, n_r = fr.elem_force(ups[0])[0], fr.elem_force(ups[1])[0]
    assert abs(n_l - n_r) <= 1e-6 * abs(n_l) and abs(n_l + n_r) > 0.5 * F, "mid-span reactions"
    zl = compliance("C", up, False, 2, x_load=-150.0)[0]
    zr = compliance("C", up, False, 2, x_load=150.0)[0]
    assert abs(zl - zr) <= 1e-6 * zl, "mirror"
    # 5. The answer does not depend on which tray node holds the frame (the load pair is balanced)
    for d in range(3):
        c1 = compliance("A", up, True, d, x_load=80.0, fix_node=1)[0]
        c2 = compliance("A", up, True, d, x_load=80.0, fix_node=0)[0]
        assert abs(c1 - c2) <= 1e-6 * abs(c1), "support independence"
    # 6. Section mass against the sellers: K I Metals page 27.27 kg/m, Dyfed list 27.89 kg/m
    kg_m = BEAM["A"] * RHO_ST * 1000
    for seller in (27.27, 27.89):
        assert abs(kg_m / seller - 1) < 0.05, f"SHS kg/m {kg_m:.2f} vs {seller}"
    rhs = UPRIGHTS["U1 RHS 160x80x8"]["sec"]["A"] * RHO_ST * 1000
    assert abs(rhs / 26.4 - 1) < 0.05, f"RHS kg/m {rhs:.2f} vs K I Metals 26.4"
    # 7. Shear area of the RHS is larger along its 160 side (walls along the shear carry it)
    r = UPRIGHTS["U1 RHS 160x80x8"]["sec"]
    assert r["Asz"] > r["Asy"], "RHS shear areas"
    # 8. Each upright fits the 80 width that sizes() is built on (else base_width, X reach, rails change)
    for name, u in UPRIGHTS.items():
        assert u["x_width"] <= UPRIGHT_W, f"{name} wider than UPRIGHT_W"
    return kg_m, rhs


def main():
    kg_m, rhs = checks()
    print(f"Lengths from sizes(): tray {TRAY_W:.0f} (X) x {TRAY_L:.0f} (Y), uprights at X +/-{UP_X:.0f}, "
          f"beam {S['beam_len']} (X {BEAM_X0:.0f} to {BEAM_X1:.0f}), pickup X {PICKUP_X:.0f}")
    print(f"Beam SHS 120x120x8: {kg_m:.2f} kg/m computed (corner radii assumed), I {BEAM['Iy']/1e4:.0f} cm^4, "
          f"J {BEAM['J']/1e4:.0f} cm^4.  RHS 160x80x8: {rhs:.2f} kg/m")
    print(f"Nose {NOSE_LOW:.0f} above the table (lowest), {SPINDLE_AHEAD:.0f} in front of the beam centre, "
          f"beam centre {BEAM_ABOVE_TABLE:.0f} above the table")
    print()
    print("um per 100 N, nose against the table (spindle at X 0) and nose against the tray's right side "
          "(spindle at the pickup).")
    print("Each figure: EG bonded (upper bound on stiffness) / profiles alone, EG ignored (lower bound).")
    hdr = f"{'option':30s}{'mass kg':>8s}  {'X':>11s}{'Y':>11s}{'Z':>11s}  | pickup {'X':>11s}{'Y':>11s}{'Z':>11s}  {'sag':>5s}"
    print(hdr)
    results = {}
    for lay in ("A", "B", "C"):
        for up in UPRIGHTS:
            m = frame_mass(lay, up)
            row = []
            for second, x in (("table", 0.0), ("wheel", PICKUP_X)):
                for d in range(3):
                    hi = compliance(lay, up, True, d, x_load=x, second=second)[0]
                    lo = compliance(lay, up, False, d, x_load=x, second=second)[0]
                    assert 0 < hi <= lo * (1 + 1e-9), "bonded fill must not soften the frame"
                    assert lo < 1000, "units: over 1 mm per 100 N"
                    row.append((hi, lo))
            sag = sag_offset(lay, up)
            results[(lay, up)] = (m, row, sag)
            cells = "".join(f"{h:5.1f}/{l:<5.1f}" for h, l in row[:3])
            cells2 = "".join(f"{h:5.1f}/{l:<5.1f}" for h, l in row[3:])
            print(f"{lay + ' + ' + up:30s}{m['total']:8.0f}  {cells}  |        {cells2} {sag:5.1f}")
    print("sag: extra nose drop (um) under the carriage's own weight at the pickup against X 0: "
          "a fixed offset, taught once")
    print()
    print("Masses (kg): tray aluminium / EG / steel end plates / two uprights / beam; upright length")
    for lay in ("A", "B", "C"):
        t = tray(lay, True)
        for up in UPRIGHTS:
            m = frame_mass(lay, up)
            print(f"  {lay} + {up:18s} {m['tray_al']:5.1f} / {m['eg']:5.1f} / {m['end']:5.1f} / {m['uprights']:5.1f}"
                  f" / {m['beam']:5.1f};"
                  f" {m['up_len']:.0f}")
        print(f"  {lay}: KJN 90x90 H {t['al_len']:.0f} mm in total; EG {t['eg_vol']/1e6:.1f} L, "
              f"epoxy {t['m_eg']*EPOXY_FRACTION:.1f} kg at 11 % (F01 kit 22.68 kg)")
    print()
    # Plate alternative
    alt = UPRIGHT_ALT["plate 30x300"]
    UPRIGHTS["alt plate 30x300"] = dict(sec=alt, x_width=30, y_depth=300)
    r = [compliance("C", "alt plate 30x300", True, d)[0] for d in range(3)]
    print(f"For comparison, C + plate 30 x 300 (bonded): X {r[0]:.1f}  Y {r[1]:.1f}  Z {r[2]:.1f}")
    del UPRIGHTS["alt plate 30x300"]
    print()
    # Beam damping fill (beam_len, fixed beam: no moving-mass penalty)
    L = S["beam_len"]
    void = BEAM["void"] * L
    full = void * RHO_EG
    strip = (120 - 16) * 30.0 * L * RHO_EG
    sand = void * RHO_SAND
    print(f"Beam {L} long: steel {BEAM['A'] * L * RHO_ST:.1f} kg, inside {void/1e6:.1f} L")
    print(f"  D1 full EG fill  +{full:.1f} kg, epoxy {full*EPOXY_FRACTION:.1f} kg")
    print(f"  D2 30 mm EG strip on the inside bottom  +{strip:.1f} kg, epoxy {strip*EPOXY_FRACTION:.1f} kg")
    print(f"  D3 dry sand, loose  +{sand:.1f} kg, no epoxy")
    inner = rect(120 - 16, 120 - 16)
    bp = steel(BEAM)
    bp_fill = dict(bp, EA=bp["EA"] + E_EG * inner["A"], EIy=bp["EIy"] + E_EG * inner["Iy"],
                   EIz=bp["EIz"] + E_EG * inner["Iz"], GJ=bp["GJ"] + G_EG * inner["J"])
    for lab, b in (("empty", bp), ("D1 filled, bonded", bp_fill)):
        c = [compliance("C", "U1 RHS 160x80x8", True, d, beam_props=b)[0] for d in range(3)]
        cp = [compliance("C", "U1 RHS 160x80x8", True, d, x_load=PICKUP_X, second="wheel", beam_props=b)[0]
              for d in range(3)]
        print(f"  C + U1, beam {lab:18s}: X {c[0]:.1f} Y {c[1]:.1f} Z {c[2]:.1f} | pickup X {cp[0]:.1f} "
              f"Y {cp[1]:.1f} Z {cp[2]:.1f}")
    rigid = dict(EA=1e14, EIy=1e17, EIz=1e17, GJ=1e17, GAy=1e14, GAz=1e14)
    c = [compliance("C", "U1 RHS 160x80x8", True, d, beam_props=rigid)[0] for d in range(3)]
    print(f"  C + U1, beam made rigid (share of the beam): X {c[0]:.1f} Y {c[1]:.1f} Z {c[2]:.1f}")
    print("PASS")
    return results


if __name__ == "__main__":
    main()

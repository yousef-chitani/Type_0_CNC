"""Task 22 beam assessment (D-143, D-145): stiffness and mass of the beam options,
and a simple bow estimate for cast-in reference bars in the tub walls.

Run: PYTHONUTF8=1 python cad/v2/beam_options.py  -> cad/v2/out/beam_options.json
Units: mm, N, MPa. Estimates only (plane sections, perfect bond where stated).
"""
import json
import pathlib

E_AL, G_AL, RHO_AL = 69e3, 26e3, 2.70e-6      # 6082/6061, MPa, kg/mm3
E_ST, RHO_ST = 210e3, 7.85e-6
E_EG, RHO_EG = 25e3, 2.30e-6                   # project pass mark (25 GPa), tub mix
SPAN, LEN = 690.0, 890.0                       # rail to rail; beam length
F = 200.0                                      # cut load, N
ARM = 245.0                                    # tool below beam centre (sketch)


def rect_I(b, h):                               # b along the bending direction
    return h * b**3 / 12.0


def tube(z, y, t):
    """Box: z = height (face carrying the X rails), y = depth, wall t.
    Returns I for force in Y (about Z), I for force in Z, area, J (Bredt)."""
    iy = rect_I(y, z) - rect_I(y - 2 * t, z - 2 * t)
    iz = rect_I(z, y) - rect_I(z - 2 * t, y - 2 * t)
    a = z * y - (z - 2 * t) * (y - 2 * t)
    am = (z - t) * (y - t)
    j = 4 * am**2 * t / (2 * ((z - t) + (y - t)))
    return iy, iz, a, j


def defl(ei):                                   # mid-span, um: simply supported, ends fixed
    return F * SPAN**3 / (48 * ei) * 1e3, F * SPAN**3 / (192 * ei) * 1e3


def twist(gj):                                  # tool displacement, um
    phi = (F * ARM / 2) * (SPAN / 2) / gj
    return phi * ARM * 1e3


def row(name, eiy, eiz, mass, gj=None, note=""):
    sy, fy = defl(eiy)
    return dict(option=name, EI_Y_MNm2=round(eiy / 1e12, 3), EI_Z_MNm2=round(eiz / 1e12, 3),
                defl_Y_um_ss=round(sy, 2), defl_Y_um_fixed=round(fy, 2),
                defl_Z_um_ss=round(defl(eiz)[0], 2),
                twist_um=None if gj is None else round(twist(gj), 1),
                mass_kg=round(mass, 1), note=note)


out = []

# 1. Sketch box 150 x 130 x 10 (reference, should give 0.90 MNm2 and 1.5 um)
iy, iz, a, j = tube(150, 130, 10)
box_mass = a * LEN * RHO_AL
out.append(row("Box 150x130x10, one piece or bonded plates", E_AL * iy, E_AL * iz, box_mass, G_AL * j,
               "sketch beam; also the bolted box if the joints do not slip"))

# 2. Bolted 4-plate box, joints slipping (lower bound): each plate bends on its own
#    front/back plates 150 x 10 (full height), top/bottom plates 110 x 10 between them
iy_slip = 2 * rect_I(10, 150) + 2 * rect_I(110, 10)
iz_slip = 2 * rect_I(150, 10) + 2 * rect_I(10, 110)
out.append(row("Bolted 4-plate box, joints slipping (lower bound)", E_AL * iy_slip, E_AL * iz_slip,
               box_mass, None, "torsion also lost; real value between this and row 1"))

# 3. Stock tubes (Aluminium Warehouse, 6000 series e.g. 6082 T6), face = first number
for name, z, y, t, note in [
    ("Tube 152.4x76.2x9.5 (6x3x3/8), 152 face", 152.4, 76.2, 9.5, "face takes 2 rails at 100"),
    ("Tube 120x120x5", 120, 120, 5, "face 120: 2 rails at 100 fit edge to edge, no margin"),
    ("Tube 101.6 sq x 6.3 (4x4x1/4)", 101.6, 101.6, 6.3, "face too small for 2 rails at 100"),
]:
    iy, iz, a, j = tube(z, y, t)
    out.append(row(name, E_AL * iy, E_AL * iz, a * LEN * RHO_AL, G_AL * j, note))

# 4. Two 6x3x3/8 tubes bonded side by side: 152.4 face, 152.4 deep, double centre web
iy1, iz1, a1, j1 = tube(152.4, 76.2, 9.5)
iy2 = 2 * (iy1 + a1 * (76.2 / 2) ** 2)
iz2 = 2 * iz1
_, _, _, jo = tube(152.4, 152.4, 9.5)
out.append(row("2 x tube 6x3x3/8 bonded side by side", E_AL * iy2, E_AL * iz2, 2 * a1 * LEN * RHO_AL,
               G_AL * jo, "both cut from one 2000 mm length; only if bonded and bolted"))

# 5. EG-filled box (sketch box, inside 130 high x 110 deep, full length), bonded
fill_iy, fill_iz = rect_I(110, 130), rect_I(130, 110)
fill_mass = 110 * 130 * LEN * RHO_EG
iy, iz, a, j = tube(150, 130, 10)
out.append(row("Box 150x130x10 filled with EG (bonded)", E_AL * iy + E_EG * fill_iy,
               E_AL * iz + E_EG * fill_iz, box_mass + fill_mass, None,
               "fill adds stiffness only if it stays bonded; damping is the point"))
out.append(row("Box 150x130x10 + EG strip 30 thick on the inside bottom", E_AL * iy, E_AL * iz,
               box_mass + 30 * 110 * LEN * RHO_EG, None, "damping only; stiffness gain ignored"))

# Epoxy for the fill, at the tub mix (11-12 %) and the video's 80/20 sand mix (2.0 kg/L ASSUMED)
fill_L = 110 * 130 * LEN / 1e6
epoxy = dict(fill_litres=round(fill_L, 2), fill_kg_tub_mix=round(fill_mass, 1),
             epoxy_kg_tub_mix=[round(fill_mass * 0.11, 1), round(fill_mass * 0.12, 1)],
             fill_kg_sand_mix=round(fill_L * 2.0, 1), epoxy_kg_sand_mix=round(fill_L * 2.0 * 0.20, 1),
             strip_epoxy_kg=round(30 * 110 * LEN * RHO_EG * 0.115, 2))

# Bow of a cast-in reference bar on a tub wall top (eigenstrain, plane sections)
# wall section EG 140 wide x 185 high; bar 110 wide x 20 thick on top (rail + screw seats)
def bow(e_bar, strain, length):
    a_w, a_b = 140 * 185, 110 * 20
    y_w, y_b = 185 / 2, 185 + 10
    ea = E_EG * a_w + e_bar * a_b
    yc = (E_EG * a_w * y_w + e_bar * a_b * y_b) / ea
    ei = E_EG * (rect_I(185, 140) + a_w * (y_w - yc) ** 2) + e_bar * (rect_I(20, 110) + a_b * (y_b - yc) ** 2)
    p = e_bar * a_b * strain
    kappa = p * (y_b - yc) / ei
    return kappa * length**2 / 8 * 1e3          # um

CTE = dict(aluminium=23e-6, steel=12e-6, eg_industrial=[12e-6, 16e-6])
eg = 14e-6
cases = {
    "room swing 10 K": dict(al=(23e-6 - eg) * 10, st=(12e-6 - eg) * 10),
    "post-cure lock-in 30 K (50 -> 20 C)": dict(al=(23e-6 - eg) * 30, st=(12e-6 - eg) * 30),
    "EG shrinkage 0.3 mm/m (industrial sheet)": dict(al=3e-4, st=3e-4),
}
bows = {}
for k, c in cases.items():
    bows[k] = {f"{m} bar, {L} long": round(bow(E_AL if m == 'Al' else E_ST, c['al' if m == 'Al' else 'st'], L), 1)
               for m in ("Al", "steel") for L in (600, 890)}

res = dict(beams=out, epoxy=epoxy, bar_bow_um=bows, cte_per_K=CTE,
           notes="Bow sign ignored; shrinkage case: EG shrinks round the bar, so the stiffer bar bows more.")
p = pathlib.Path(__file__).parent / "out" / "beam_options.json"
p.parent.mkdir(exist_ok=True)
p.write_text(json.dumps(res, indent=1))
for r in out:
    print(r)
print(epoxy)
for k, v in bows.items():
    print(k, v)

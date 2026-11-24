"""ATC front carrier: hand estimate of fork displacement at the pickup (D-303, D-304).

Load cases at the 12 o'clock fork (groove r 142, Y -85, wheel axis X 200 Z -40 along Y):
  Fy : the clip push along Y (engage: holder pushed -Y into the fork; disengage: pulled +Y).
  Fr : the radial push down the tool axis (drawbar release, nose landing on the holder).
Result: mm at the groove per 100 N. Beam formulas only; every number is an estimate.
Run: python tools/atc_carrier_stiffness.py
"""
E_AL, E_ST = 70e3, 200e3  # N/mm2
R_FORK = 142.0            # groove radius
F = 100.0                 # N

def cant(EI, L):          # tip stiffness of a cantilever, N/mm
    return 3 * EI / L**3

def fk12_tilt(k_theta):   # Y at the rim from bearing tilt, mm per F
    return F * R_FORK / k_theta * R_FORK

def report(name, parts):
    tot = sum(parts.values())
    s = ", ".join(f"{k} {v:.2f}" for k, v in parts.items())
    print(f"{name:<46} {tot:5.2f} mm   ({s})")

# FK12 (7001 DF pair, about 3 mm between pressure centres): tilt stiffness not published.
# Ball-set estimate about 1e6 Nmm/rad; range 0.5e6 to 3e6. Bench-measure it.
KT_LO, KT_MID, KT_HI = 0.5e6, 1e6, 3e6

# Stub shaft dia 12, about 35 from the FK12 face to the hub, moment F*R at its end.
I12 = 3.1416 * 12**4 / 64
shaft = lambda: (F * R_FORK) * 35 / (E_ST * I12) * R_FORK   # rotation * R

# --- Y push (clip) -------------------------------------------------------------
print("Fy (clip push), mm at the groove per 100 N")
# D-303: 3 mm 5754 spoke 20 x 3, r 42 to 142 (L 100); tabs only couple via the thin
# ring, so about 1.5 spokes carry it.
spoke3 = cant(E_AL * 20 * 3**3 / 12, 100) * 1.5
# standoffs axial: 8 x M4 hex 7 AF steel, 70 long; about 3 take the tilt
stand = 3 * E_ST * 30 / 70
base = {"FK12 tilt": fk12_tilt(KT_MID), "stub shaft": shaft()}
report("D-303 3 mm sheet + standoffs", {"disc": F / spoke3, "standoffs": F / stand, **base})
# 6 mm 5083 flat disc, windows, spoke 30 wide, rim ring helps: about 3 spokes
spoke6 = cant(E_AL * 30 * 6**3 / 12, 90) * 3
report("6 mm flat disc on a long hub", {"disc": F / spoke6, **base})
# 8 mm flat disc, no windows: annular plate, take about 6 spoke-equivalents
spoke8 = cant(E_AL * 40 * 8**3 / 12, 90) * 6
report("8 mm flat disc, no windows, long hub", {"disc": F / spoke8, **base})
print(f"  FK12 tilt alone for k_theta {KT_LO:.0e} / {KT_MID:.0e} / {KT_HI:.0e} Nmm/rad: "
      f"{fk12_tilt(KT_LO):.2f} / {fk12_tilt(KT_MID):.2f} / {fk12_tilt(KT_HI):.2f} mm")
print("  With a fixed back-stop under the pickup fork: disc + rim only, FK12 and shaft drop out.")

# --- radial push ---------------------------------------------------------------
print("\nFr (radial push), mm at the groove per 100 N")
# D-303 tab 70 x 3, 27.8 long, groove 38 past the tab end (see D-303 note)
EI_tab = E_AL * 70 * 3**3 / 12
L, a = 27.8, 38.0
tip = F * L**3 / (3 * EI_tab) + F * a * L**2 / (2 * EI_tab)
rot = F * L**2 / (2 * EI_tab) + F * a * L / EI_tab
print(f"D-303 bent tab alone                           {tip + rot * a:5.2f} mm")
print("Flat disc: the push is in the disc plane (stiff); left: the fork foot and the FK12.")
# FK12 as a radial support: F at about 43 from the bearing -> tilt, radial at the groove
for kt in (KT_LO, KT_MID, KT_HI):
    th = F * 43 / kt
    print(f"  FK12 k_theta {kt:.0e}: radial {th * 43:.2f} mm, rim swings {th * R_FORK:.2f} mm in Y")

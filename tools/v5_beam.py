#!/usr/bin/env python3
"""V5 beam pick (plan Task 2): tall steel tube standing up, both X rails on its front face (D-349).

Hand calculation, no FEA (method as tools/portal_overhang.py). For each bought tube:
flat front face for the corner radius, the largest HGR20 rail spacing on it, Ix, Iy, J, mass,
and the beam's share of the nose deflection per 100 N in X, Y and Z.

Beam model: simply supported on the two Y rollers (span = Y rail spacing from v5_sizes), load at
mid-span; twist held at both rollers. The bolted beam-to-roller joints are stiffer than pins,
so bending is overstated; the rollers, rails, carriages, Z axis and spindle are rigid here. So the
figures RANK the tubes; they do not predict the machine.
Run: PYTHONUTF8=1 python tools/v5_beam.py
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v5_sizes import sizes  # noqa: E402

S = sizes()
F = 100.0                         # N
E, G, RHO = 205e3, 79e3, 7.85e-6  # steel, N/mm^2, kg/mm^3
SPAN = S["y_rail_spacing"]        # beam supports: the two Y rollers on the Y rails (v5_sizes)
BEAM_LEN = S["beam_len"]

# ---- Rail fit on the front face --------------------------------------------------------
RAIL_W = 20.0           # HGR20 rail width (vendor README: WR 20)
BLOCK_W = 44.0          # HGH20CA block width (STEP cad/vendor/hgh20ca_block.step, W 44)
SUPPORT_W = 60.0        # BK12 / BF12 / HM12-60-V width across the screw (STEP bk12.step, 60 x 43)
SIDE_CLEAR = 3.0        # block edge to the BK12 / housing (estimate)
SEAT_MARGIN = 5.0       # flat face past each rail edge for the epoxy seat dam (estimate)
MIN_SPACING = BLOCK_W + SUPPORT_W + 2 * SIDE_CLEAR   # rail centres: blocks clear a 60-wide part

# Outside corner radius of cold-formed tube (K I Metals: "BS EN 10219"). EN 10219-2 limits:
# T <= 6: 1.6T to 2.4T; 6 < T <= 10: 2.0T to 3.0T; T > 10: 2.4T to 3.6T (standard, not re-read
# live). The largest is used for the flat face: measure the delivered tube.
def r_out_max(t):
    return (2.4 if t <= 6 else 3.0 if t <= 10 else 3.6) * t


def r_out_calc(t):          # EN 10219-2 nominal radius for section properties
    return (2.0 if t <= 6 else 2.5 if t <= 10 else 3.0) * t


# ---- Lever arms (estimates until Task 5 models the X and Z stack) ------------------------
FRONT_TO_AXIS = 173.0   # beam front face to spindle axis: V4 stack plate back to axis 140 +
                        # block 30 (docs/v4-model.md) + 3 epoxy seat (V4 had a 20 bar)
CENTRE_ABOVE_NOSE_MAX = 45.0   # beam centre above the nose at its top: V4 beam centre 220 above
                               # the table, nose max 175 (docs/v4-model.md); Z rails 50 longer
                               # in V5 put the extra travel below, so the gap stays (ESTIMATE)
NOSES = (S["nose_max"], S["nose_min"])

# ---- Candidates: K I Metals stock, mild steel, curl 26 Nov 2026 (docs/price-check-v5.md) ----
# (height standing up, depth along Y, wall, GBP per metre ex VAT)
TUBES = [
    ("SHS 120x120x8 (reference)", 120, 120, 8, 67.05),
    ("RHS 200x100x8", 200, 100, 8, 90.30),
    ("RHS 200x150x8", 200, 150, 8, 107.08),
    ("RHS 250x150x8", 250, 150, 8, 123.86),
]


# Frame tubes (PrintNC XFrame, YFrame): Y rails epoxy-seated on the Y tubes' top faces.
# PrintNC's Y roller is 80 wide over an 80 tube (STEP, docs/v5-sizes.md), so 80 wide keeps it.
FRAME_TUBES = [
    ("SHS 80x80x5", 80, 80, 5, 28.13),
    ("SHS 80x80x6", 80, 80, 6, 32.46),
    ("SHS 80x80x8", 80, 80, 8, 40.32),
    ("SHS 100x100x6", 100, 100, 6, 45.28),
]
FRAME_LEN = 2 * S["frame_y"] + 2 * S["frame_inner_x"]   # 2 Y tubes + 2 X tubes between them


def section(h, b, t, step=0.1):
    """Area, I about the horizontal axis (vertical bending), I about the vertical axis, J."""
    ro = r_out_calc(t)
    ri = ro - t

    def inside(y, z, hh, bb, r):
        ay, az = np.abs(y) - (bb / 2 - r), np.abs(z) - (hh / 2 - r)
        box = (np.abs(y) <= bb / 2) & (np.abs(z) <= hh / 2)
        corner = (ay > 0) & (az > 0)
        return box & ~(corner & (ay ** 2 + az ** 2 > r ** 2))

    y = np.arange(-b / 2 + step / 2, b / 2, step)
    z = np.arange(-h / 2 + step / 2, h / 2, step)
    Y, Z = np.meshgrid(y, z)
    m = inside(Y, Z, h, b, ro) & ~inside(Y, Z, h - 2 * t, b - 2 * t, ri)
    dA = step * step
    A = m.sum() * dA
    I_h = (Z[m] ** 2).sum() * dA          # vertical loads
    I_v = (Y[m] ** 2).sum() * dA          # horizontal (Y) loads
    rm = ro - t / 2                       # mid-wall line: Bredt
    Am = (h - t) * (b - t) - (4 - math.pi) * rm ** 2
    p = 2 * (h - t) + 2 * (b - t) - (8 - 2 * math.pi) * rm
    J = 4 * Am ** 2 * t / p
    return A, I_h, I_v, J


def nose_deflection(h, b, t, nose):
    """Beam share of the nose movement (um) for 100 N at the nose in X, Y and Z."""
    A, I_h, I_v, J = section(h, b, t)
    L = SPAN
    dy = FRONT_TO_AXIS + b / 2                       # beam centre to spindle axis, along Y
    dz = CENTRE_ABOVE_NOSE_MAX + (S["nose_max"] - nose)   # beam centre to nose, down
    k_twist = 4 * G * J / L                          # two halves, each L/2, ends held
    shear_v = F * L / (4 * G * 2 * t * h)            # webs carry vertical shear
    shear_h = F * L / (4 * G * 2 * t * b)            # flanges carry Y shear
    # Z: vertical bending + shear + twist (force at dy in front of the centre)
    z = F * L ** 3 / (48 * E * I_h) + shear_v + F * dy * dy / k_twist
    # Y: horizontal bending + shear + twist (force at dz below the centre)
    yd = F * L ** 3 / (48 * E * I_v) + shear_h + F * dz * dz / k_twist
    # X: along the beam; couples F*dy (horizontal plane) and F*dz (vertical plane) at mid-span,
    # rotation at mid-span M L / (12 E I) each
    x = (F * dy) * L / (12 * E * I_v) * dy + (F * dz) * L / (12 * E * I_h) * dz
    return 1000 * x, 1000 * yd, 1000 * z


def rail_fit(h, t):
    flat = h - 2 * r_out_max(t)
    largest = flat - RAIL_W - 2 * SEAT_MARGIN
    return flat, largest


if __name__ == "__main__":
    print(f"Span {SPAN:g} (Y rail spacing), beam {BEAM_LEN:g} long, 100 N at mid-span. "
          f"Rail spacing needed >= {MIN_SPACING:g} (block {BLOCK_W:g} + {SUPPORT_W:g} + 2 x {SIDE_CLEAR:g})")
    head = (f"{'tube':28s}{'flat':>6s}{'rails':>7s}{'Ix cm4':>8s}{'Iy cm4':>8s}{'J cm4':>8s}"
            f"{'kg':>6s}{'GBP':>8s}")
    for nose in NOSES:
        head += f"   nose {nose:3g}: X/Y/Z um"
    print(head)
    results = {}
    for name, h, b, t, gbp_m in TUBES:
        A, I_h, I_v, J = section(h, b, t)
        flat, largest = rail_fit(h, t)
        kg = A * BEAM_LEN * RHO
        line = (f"{name:28s}{flat:6.0f}{largest:7.0f}{I_h / 1e4:8.0f}{I_v / 1e4:8.0f}{J / 1e4:8.0f}"
                f"{kg:6.1f}{gbp_m * BEAM_LEN / 1000:8.2f}")
        for nose in NOSES:
            x, y, z = nose_deflection(h, b, t, nose)
            line += f"   {x:5.1f} {y:5.1f} {z:5.1f}      "
        print(line)
        results[name] = (flat, largest)
        if "reference" not in name:
            assert largest >= MIN_SPACING, f"{name}: rails {largest:.0f} apart < {MIN_SPACING:g}"
    ref = results["SHS 120x120x8 (reference)"][1]
    print(f"Reference SHS 120x120x8: rails at most {ref:.0f} apart: does not fit (D-349).")
    print("Ix: vertical loads (height standing up); Iy: loads along Y. Flat face uses the "
          "largest EN 10219 corner radius (3T for 8 wall); properties the nominal 2.5T.")
    flat, largest = rail_fit(S["beam_h"], 8)
    assert MIN_SPACING <= S["x_rail_spacing"] <= largest, "chosen X rail spacing does not fit"
    print(f"Chosen (D-353, D-355): RHS {S['beam_h']}x{S['beam_d']}x8, X rails {S['x_rail_spacing']} apart")
    print(f"\nFrame tubes: 2 Y x {S['frame_y']:g} + 2 X x {S['frame_inner_x']:g} = {FRAME_LEN:g}"
          f" (X tubes between the Y tubes; legs and rack mounts not counted)")
    print(f"{'tube':16s}{'flat top':>9s}{'I cm4':>7s}{'J cm4':>7s}{'kg/m':>6s}{'kg':>6s}{'GBP':>8s}")
    for name, h, b, t, gbp_m in FRAME_TUBES:
        A, I_h, I_v, J = section(h, b, t)
        flat = h - 2 * r_out_max(t)
        assert flat >= RAIL_W + 2 * SEAT_MARGIN, f"{name}: no flat for the Y rail seat"
        print(f"{name:16s}{flat:9.0f}{I_h / 1e4:7.0f}{J / 1e4:7.0f}{A * RHO * 1000:6.1f}"
              f"{A * FRAME_LEN * RHO:6.1f}{gbp_m * FRAME_LEN / 1000:8.2f}")
    print("PASS")

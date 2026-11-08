#!/usr/bin/env python3
"""Portal beam overhang check (open question 11). Hand calculation, no FEA.

Beam: 130 (Y) x 130 (Z) solid epoxy granite with 2 x 50 mm PVC cores (cad/v2/type0_v2.py).
Supports: the two portal legs, centres 570 apart (X -285 and +285). The saddle centre at the
ATC pickup is X 370, so 85 mm past the right leg centre. The beam is treated as simply
supported on the legs with an overhanging point load: this ignores the stiffening from the
legs being cast into the beam, so the real deflection is smaller.
Run: python tools/portal_overhang.py
"""
import math

b = h = 130.0            # beam section, mm
d_core = 50.0
L = 570.0                # leg centre to leg centre, mm
a = 370.0 - 285.0        # overhang from right leg centre to saddle centre, mm
y_offset = 175.0         # spindle axis (Y 0) to beam centre (Y 110 + 65), mm

# Moving mass at the pickup (Phase 2, worst case): saddle 1.6, Z plate 2.4, X blocks 1.6,
# Z rails + blocks + screw 2.5, Z motor with brake 1.9, ATC spindle about 8 kg (G-Penny ER20 is 5.5)
mass_kg = 1.6 + 2.4 + 1.6 + 2.5 + 1.9 + 8.0
P = mass_kg * 9.81       # N

A_core = math.pi * d_core**2 / 4
I_core = math.pi * d_core**4 / 64
I_solid = b * h**3 / 12
cases = {
    "cores side by side (on the neutral axis)": I_solid - 2 * I_core,
    "cores one above the other (32.5 mm off axis)": I_solid - 2 * (I_core + A_core * 32.5**2),
}
A = b * h - 2 * A_core

print(f"Load at the pickup: {mass_kg:.1f} kg = {P:.0f} N, {a:.0f} mm past the right leg centre")
for E in (25000.0, 35000.0):                      # epoxy granite, N/mm^2 (25-35 GPa typical)
    G = E / 2.5
    for name, I in cases.items():
        bend = P * a**2 * (L + a) / (3 * E * I)   # tip deflection, overhanging simply supported beam
        shear = P * a * (L + a) / (L * (5 / 6) * G * A)
        print(f"E {E/1000:.0f} GPa, {name}: bending {bend*1000:.2f} um + shear {shear*1000:.2f} um"
              f" = {(bend+shear)*1000:.2f} um")

# Twist: the spindle hangs 175 mm in front of the beam centre. The torque is the same at every
# X position, so only the extra twist of the 50 mm stub past the leg face changes at the pickup.
T = P * y_offset
J = 0.141 * h**4 - 2 * (math.pi * d_core**4 / 32)  # square section, minus cores (approx.)
theta = T * 50.0 / ((25000.0 / 2.5) * J)
print(f"Extra twist over the 50 mm past the leg face: {theta*1e6:.1f} urad"
      f" = {theta*300*1000:.2f} um at a tool tip 300 mm below the beam")

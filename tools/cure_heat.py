#!/usr/bin/env python3
"""Curing heat estimate for the epoxy-granite castings (open question 9).

Compares each casting with a pure GlassCast 50 PLUS pour that the datasheet calls safe
(50 mm into an insulating mould at 20 C). For a slow-curing slab losing heat by conduction,
the centre temperature rise scales with (heat per volume) x thickness^2 / conductivity.
Material values are typical handbook figures, marked ASSUMED: the test bricks must confirm.
Run: python tools/cure_heat.py
"""
epoxy_mass_frac = 0.11              # D-26 / dimensions_v2.md
rho_epoxy, rho_stone = 1.1, 2.65    # g/cm3 (stone = quartz) ASSUMED
H_epoxy = 450.0                     # J per g of mixed resin + hardener, ASSUMED (typical amine epoxy)
c_epoxy, c_stone = 1.5, 0.78        # J/gK ASSUMED
k_epoxy, k_eg = 0.2, 1.5            # W/mK ASSUMED (epoxy granite 1.2-2 typical)

v_epoxy = (epoxy_mass_frac / rho_epoxy) / (epoxy_mass_frac / rho_epoxy + (1 - epoxy_mass_frac) / rho_stone)
c_mix = epoxy_mass_frac * c_epoxy + (1 - epoxy_mass_frac) * c_stone
dT_adiabatic_eg = epoxy_mass_frac * H_epoxy / c_mix
dT_adiabatic_resin = H_epoxy / c_epoxy
print(f"Epoxy volume fraction in the mix: {v_epoxy:.0%}")
print(f"Upper limit with no heat loss at all: pure resin {dT_adiabatic_resin:.0f} K, EG mix {dT_adiabatic_eg:.0f} K")

ref_t = 50.0   # mm, datasheet maximum into an insulating mould at 20 C
for name, t in [("Portal beam, 130 mm section", 130.0), ("Base, 110 mm high", 110.0),
                ("Rail-seat levelling pour (pure resin, a few mm)", None)]:
    if t is None:
        print(f"{name}: pure resin well under the 50 mm limit")
        continue
    ratio = v_epoxy * (t / ref_t) ** 2 * (k_epoxy / k_eg)
    print(f"{name}: about {ratio:.2f} x the temperature rise of the safe 50 mm pure-resin pour")

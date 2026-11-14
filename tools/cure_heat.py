#!/usr/bin/env python3
"""Curing heat estimate for the epoxy-granite castings with Ampreg 30 + 3X Slow (D-122).

Model: the casting is one lump at a single temperature (heat spreads through 110-130 mm of EG
in well under an hour), releasing its curing heat evenly over a period and losing heat through
the mould faces. Peak rise = (power / loss) x (1 - exp(-period / time constant)).
Material and surface values are typical handbook figures, marked ASSUMED: the heat brick must confirm.
Run: python tools/cure_heat.py
"""
import math
epoxy_mass_frac = 0.11
H_epoxy = 450.0                     # J per g of mixed resin + hardener, ASSUMED (typical amine epoxy)
c_epoxy, c_stone = 1.5, 0.78        # J/gK ASSUMED
U_open, U_mdf = 8.0, 4.0            # W/m2K: open face in still air; face behind 18 mm MDF. ASSUMED
U_ins = 0.6                         # W/m2K: face behind 50 mm insulation. ASSUMED

c_mix = epoxy_mass_frac * c_epoxy + (1 - epoxy_mass_frac) * c_stone          # J/gK
dT_max = epoxy_mass_frac * H_epoxy / c_mix
print(f"Upper limit with no heat loss at all: {dT_max:.0f} K")

# name, mass kg, open-face area m2, MDF-face area m2, insulated-face area m2
cases = [("Base, 80 kg, 110 thick, in its MDF mould", 80.2, 0.317, 0.317 + 0.39, 0.0),
         ("Portal, 38 kg, 130 thick, in its MDF mould", 37.6, 0.126, 0.126 + 0.45, 0.0),
         ("Heat brick 130 x 130 x 200, bare MDF mould", 7.8, 0.026, 0.026 + 0.104, 0.0),
         ("Heat brick, sides wrapped in 50 mm insulation", 7.8, 0.026, 0.026, 0.104)]
print(f"{'':48s}  loss W/K  time const h   rise if the heat comes out over 6 h / 12 h / 24 h")
for name, kg, a_open, a_mdf, a_ins in cases:
    UA = a_open * U_open + a_mdf * U_mdf + a_ins * U_ins
    C = kg * 1000 * c_mix
    tau = C / UA
    Q = kg * 1000 * epoxy_mass_frac * H_epoxy
    rises = [min(dT_max, Q / (h * 3600) / UA * (1 - math.exp(-h * 3600 / tau))) for h in (6, 12, 24)]
    print(f"{name:48s}  {UA:7.1f}  {tau/3600:10.1f}     " + " / ".join(f"{r:.0f} K" for r in rises))

# post-cure heater: tent 1.5 x 1.0 x 0.8 m, 50 mm foil-faced PIR (U about 0.45 W/m2K), plus 30 % for leaks
area, U_tent = 2 * (1.5 * 1.0 + 1.5 * 0.8 + 1.0 * 0.8), 0.45
for shed in (5, 10, 15):
    hold = area * U_tent * 1.3 * (50 - shed)
    ramp = (80.2 + 30) * 1000 * 1.0 * 10 / 3600      # casting + mould, about 1 J/gK, 10 K per hour
    print(f"Post-cure at 50 C, shed at {shed} C: hold {hold:.0f} W, plus {ramp:.0f} W while ramping 10 K/h")

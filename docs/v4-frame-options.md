# V4 frame options (Task 2, 24 Nov 2026)

**For the owner to choose. Nothing here is decided.** Numbers: `PYTHONUTF8=1 python tools/v4_frame_stiffness.py`. Prices: `docs/price-check-v4.md` (curl, 24 Nov 2026, ex VAT).

## How the figures are made
- Lengths from `tools/v4_sizes.py` `sizes()`. Its `base_width` 660 includes the two 80 uprights, so **the tray is 500 (X) x 670 (Y)**, with the uprights bolted to its two X ends (centres X ±290). Beam SHS 120 x 120 x 8, 890 long, X -330 to +560; wheel pickup X 415.
- Beam formulas (Timoshenko beam elements joined into one small 3D frame), stdlib only. The load is a pair: 100 N at the spindle nose and 100 N back on the work under it, so the figure is **nose against table**, in µm per 100 N. At the pickup the pair is nose against the tray's right side, where a base-mounted wheel would sit.
- Worst case: nose 25 above the table (D-267), spindle 235 in front of the beam centre (D-106 plus half the beam, estimate), beam centre 220 above the table (from v3's Z plate, estimate).
- **Taken as rigid:** every bolted joint (upright to tray, beam to upright, tray T-slot joints), the Z axis, carriages, rails and blocks, the stand. The real machine is softer. **These figures rank the options. They do not predict the machine's stiffness.**
- Each figure is given as two numbers:
  - first: EG bonded to the metal at 25 GPa (assumed; the upper bound);
  - second: metal only, every piece on its own (EG cracked or not bonded, joints slip; the lower bound).
- **Profile data:** KJN Aluminium Profiles' own pages: 90 x 90 H, Ix = Iy = 299.80 cm⁴, 10.50 kg/m. KJN gives no torsion constant, so J is an **estimate** (6 % of Ix + Iy, for open T-slots).

## Base tray layouts (all KJN 90 x 90 H, 10 mm slot)

| | Layout | Pockets and how they are closed | Mass (tray) | Stiffness, upright U1 (µm per 100 N: X, Y, Z) | Price (ex VAT) |
|---|---|---|---|---|---|
| **A. Ring, 90 tall** | 2 side members along Y (670) under the Y rails at X ±205; 3 cross members along X (320) at Y -290, 0, +290, joined by corner brackets | 2 pockets 320 x 200 x 90 (11.5 L). Bottom: a sheet screwed into the bottom slots, seams sealed. Top open, EG screeded just below the profile tops. Slot ends taped | 24.1 kg aluminium + 26.5 kg EG (2.9 kg epoxy) | 1.7/3.4, 1.6/4.2, 2.7/8.2 | Profiles £277.80; 12 brackets £144.60; **£422.40** |
| **B. Cross deck, 90 tall** | 4 profiles along X (500) at Y -290, -45, +45, +290, ends tapped M16; a 20 mm steel end plate (670 x 90) on each end, bolted into the profile ends | 2 pockets 155 x 90 x 500 (13.9 L). Ends closed by the end plates, bottom by a sheet, top open | 21.0 kg + 32.1 kg EG (3.5 kg epoxy) + 18.9 kg end plates | 1.6/3.9, 1.5/3.6, 2.6/7.1 | Profiles £250.96; end plates (90 x 20) £46.55; **£297.51** |
| **C. Two-layer cross deck, 180 tall** | B stacked twice (8 profiles), layers bolted together with M8 T-bolts; end plates 670 x 180 x 20 | 2 pockets 155 x 180 x 500 (27.9 L), closed as B | 42.0 kg + 64.2 kg EG (7.1 kg epoxy) + 37.9 kg end plates | 1.2/4.1, 1.4/2.6, 2.3/4.4 | Profiles £501.92; end plates (180 x 20) £93.12; **£595.04** |

Not in the table:
- Bottom sheet: not priced.
- M8 T-nuts: £0.36 each.
- KJN delivery: from £15.50 + VAT.
- A one-layer option in KJN 80 x 160 H (IR range, 160 tall) is listed but **price on application**: not priced.

What the table shows:
- **Bonded, the three trays are close** (Z 2.2 to 2.7). The beam gives the largest share: with the beam made rigid, C + U1 goes from Z 2.3 to 1.2.
- **Not bonded, the depth decides in Y and Z.** Z is 8.2 (A), 7.1 (B) and 4.4 (C); Y is 4.2, 3.6 and 2.6. C holds up best if the EG cracks or comes loose (Ampreg's neat shrinkage is 1.64 %, D-122).
- **But C's unbonded X (4.1) is the worst of the three** (A 3.4). This is partly the model: the rail lines sit at the tray's mid-height, so the lever up to the table grows with the tray's height, and only one X member (at the gantry line) is modelled. Treat the unbonded X figures as rough.
- **The joints decide more than these figures.** They are taken as rigid here, but they are not:
  - A's uprights can only bolt to the side members through M8 T-nuts in a 10 mm slot.
  - B and C bolt to steel end plates (tapped M12), over a face 90 or 180 tall. The 180 face of C doubles the bolts' lever against a 90 face: about 4 times the joint's stiffness in rotation for the same bolts.
- **B and C have no aluminium running along Y.** Under the rails the stiffness along Y comes from the EG, the rail plates and the end plates. With the EG not bonded, B and C rely on those.
- The epoxy is well inside the F01 kit (22.68 kg), even for C.

## Upright sections (steel, no welding)

| | Section | How it takes the tray and the beam | Mass (2 off) | Stiffness with C (X, Y, Z) | Price (ex VAT) |
|---|---|---|---|---|---|
| **U1. RHS 160 x 80 x 8** (S235/S355, EN 10219), 80 in X | Its 160 face bolts to the tray end through both walls (access holes in the outer wall), with 2 dowels. **The open top needs a bolted cap:** a 20 plate cross-bolted through the RHS walls, then the beam bolted to the cap. Mill-finish faces: shim or epoxy the joint | 17.5 kg (A, B; 325 long), 22.3 kg (C; 415 long) | 1.2/4.1, 1.4/2.6, 2.3/4.4 | £70.32/m: £45.71 (A, B; one 650 length), £58.37 (C; 830) |
| **U2. Flat bar 50 x 150** (hot-rolled mild steel), 50 in X | Bolted flat to the tray end, counterbored M12, 2 dowels. **The beam sits on its 50 wide top edge**, bolted down into tapped M12 in solid steel: no cap, one joint fewer. Mill-scale faces: grind (shop) or epoxy-shim the joint | 38.3 kg (A, B), 48.9 kg (C) | 1.2/4.3, 1.3/2.6, 2.2/4.3 | £144.77/m: £94.10 (A, B), £120.16 (C) |

- **The two sections are equally stiff here,** within 0.2 µm in every direction. They differ in the joints, the mass and the price.
- Both stay inside the 80 upright width of `sizes()`, so no length changes.
  - A wider section (for example SHS 120 x 120) would grow `base_width` and the X reach to the wheel, and with them the X rail and screw.
- Checked for comparison: flat bar 30 x 300 (C, bonded): 1.4, 1.3, 2.1. Its Y depth gives no real gain.
- K I Metals sells no steel plate, so a "thick plate" upright is wide flat bar from them.

## At the wheel pickup (spindle at X 415)
- Nose against the tray's right side: **1.9 to 2.1 (X), 1.0 to 1.1 (Y), 1.5 to 1.7 (Z) µm per 100 N** (bonded), for every tray. Only the right upright and the 125 of beam past it are in the path.
- **Sag** under the carriage's own weight (18 kg) at the pickup, against X 0: 0.2 µm or less (weight put at the nose, so the beam's twist is in). It is a fixed offset, taught once.

## Beam damping fill (890 beam, inside 9.6 L)
**The beam no longer moves (fixed gantry), so the moving-mass penalty in `beam-assessment.md` is gone.** Mass is no limit (design doc).

| | Option | Added mass | Epoxy | Effect (C + U1) |
|---|---|---|---|---|
| D0 | Empty | 0 (beam 23.9 kg) | 0 | X 1.2, Y 1.4, Z 2.3; can ring |
| **D1** | Full EG fill, poured through ports | +22.0 kg | 2.4 kg | Bonded: X 1.2, Y 1.3, Z 2.1. **Damping is the real gain**; the stiffness gain is lost if it debonds |
| D2 | 30 mm EG strip on the inside bottom | +6.4 kg | 0.7 kg | Damping only, less than D1 |
| D3 | Dry sand, loose | +15.3 kg (density 1.6, estimate) | 0 | Damps by friction; no stiffness; no shrinkage; can be emptied |
| D4 | Damping sheet bonded inside | small | — | Not priced |

- Any fill closes the inside of the tube. **The bolts through the beam's walls (beam to upright, rails) must go in first:** studs or captive nuts, or a dam that keeps the bolt ends clear.
- Pour before the rail seats are levelled.

## Notes
- **The wheel pickup is still provisional** (`docs/v4-sizes.md`, open item). The pickup offset (85 past the upright) cannot hold a wheel about 392 across unless the wheel sits below the base's side. A larger offset makes the beam's overhang longer. The pickup figures above are at X 415 and will grow a little.
- The Y rails at X ±205 (under the table edges) and the table plate (330 x 30, 6082) are estimates in the model.

## Claude's recommendation
- **Tray: C** (two-layer cross deck, 180 tall).
  - Its lower bound is the best by far (Z 4.4 against 8.2 for A), so it depends least on the EG staying bonded.
  - Its end plates close the pockets for the pour and give the uprights a steel face 180 tall.
  - It is the dearest tray (£595.04 against £297.51 for B).
- **Upright: U2, flat bar 50 x 150.**
  - The beam bolts straight onto solid steel (no cap on an open tube end).
  - Its stiffness is the same as U1. It costs £61.79 more than U1 for C.
- **Beam: D1, full EG fill,** after the through-bolts are fitted and before the rail seats.
- **Against the budget rule** (design doc: the cheapest option that holds ±0.02 mm): C + U2 costs £715.20 ex VAT, against £343.22 for B + U1, so **£371.98 more**. No figure here shows B + U1 failing. My pick buys margin against the EG debonding and a better joint, not a proven need. The call is yours.

## Questions for the owner
1. **Base tray:** A (ring, 90 tall, £422.40), B (cross deck, 90, £297.51) or C (two-layer cross deck, 180, £595.04)? Profiles from KJN Aluminium Profile, a new vendor (ex VAT, delivery from £15.50 + VAT, 7 to 10 working days).
2. **Uprights:** U1, RHS 160 x 80 x 8 with a bolted cap (£58.37 for C), or U2, flat bar 50 x 150 with the beam bolted onto its top edge (£120.16 for C)?
3. **Beam fill:** D1 full EG (+22 kg, 2.4 kg epoxy), D2 30 mm strip, D3 dry sand, or none?
4. **Rail seats:** bright 50 x 20 plates ground flat by a shop (I need your shop's grinding price), or epoxy-levelled seats as in v3?

# Layout (draft 1)

Generated from [`cad/type0_layout.py`](../cad/type0_layout.py) (3D STEP: `cad/out/type0.step`) and [`cad/type0_drawings.py`](../cad/type0_drawings.py). Full numbers: [cad/out/dimensions.md](../cad/out/dimensions.md).

![Side view, working](../cad/out/drawing_side.svg)

![Side view, tool change](../cad/out/drawing_side_toolchange.svg)

![Front view](../cad/out/drawing_front.svg)

## What the layout changed

| Item | Before | Now | Why |
|---|---|---|---|
| Y travel | 250 + about 100 | **250 + 145 = 395** | To reach the back rack row, the front row sticks 95 mm in front of the spindle. The table must clear it |
| Base | 900 × 660 × 180 | **970 × 660 × 180, about 265 kg** | Longer Y travel plus the rack park area |
| Gantry | 640 × 460, opening 400 × 260 | unchanged, about 70 kg | |
| Epoxy / aggregate | 41 / 300 kg | **37 / 298 kg** (at 11%), + about 4 kg for leveling and samples | |
| X rails | 450 | **448 minimum: buy 500** | 450 leaves only 2 mm |
| Z rails | 300 | **330 minimum: buy 350** | Block pitch + travel |
| Y ballscrew | 500 | **550** | Longer Y travel |
| X / Z ballscrews | 420 / 280 | 405 / 305 minimum: buy **420 / 310** | |
| Rack slide rails (MGN15) | 2 × 400 | **2 × 550** | Rack stroke 395 mm |
| Rack screw (SFU1204) | 400 | **500** | |
| Stand steel | 3 m (placeholder) | **10.7 m of 80 × 80 × 5** | 950 mm table height, 700 × 1,010 footprint |
| Rack fork plane | — | 140 above base | Tools hang clear of the Y rails |
| Z assembly | — | Rises about 170 mm above the beam at Z top | Normal for 150 mm Z: the enclosure must be tall enough |

## Problems found
1. **Cabinet does not fit inside the stand.** The clear height between the top and lower rings is about 400 mm, and the cabinet is 500 mm tall.
2. **Stand steel cost.** 10.7 m at the £35/m confirmed for 80 × 80 × 5 is about £375, against the £111 placeholder.

## Assumptions to verify (marked VERIFY in the script)
- HGR20/HGH20CA: block height 30 mm, block length 77.5 mm.
- DFU1605 nut length 90 mm, BK12/BF12 45 mm total. **Ballscrew nut clearance under the table**: the screw centre must sit low enough for the nut housing to clear the table underside (30 mm above the base). A shallow channel cast into the base is likely needed: check against the DSG16H housing drawing.
- Spindle length about 300 mm including the release cylinder.
- Stack from spindle axis to beam face: 160 mm.

# Steel gantry layout sketch (18 Nov 2026)

**Status: proposal, not agreed. No D-numbers yet.** Drawing: `cad/v2/out/steel_gantry_sketch.png`. Numbers: `cad/v2/out/steel_gantry_sketch.json`. Script: `cad/v2/steel_gantry_sketch.py`. The drawing uses the table in the 18 Nov handover entry unchanged, so the problems below are still in it.

## Result

As drawn, the layout has 3 clashes, all from problem 1. **With fixes 1 to 4 applied the check finds no clashes and every access hole is clear** (`python cad/v2/steel_gantry_sketch.py --fixes`). The check covers the whole X, Y and Z travel, and every part is a bounding box.

| # | Problem | Size | Proposed fix |
|---|---|---|---|
| 1 | **Ball nut flange hits the top arm** (X) and **the foot step** (both Y nuts) | 4 mm overlap. The DFU1605 model has a round Ø48 flange, the housing face is only 20 from the axis | Relief slot **12 × 30 × 5 deep** in the arm and in each foot step, over the flange only. Flange of each Y nut faces the front, so its slot stays clear of the M10 bolts |
| 2 | **Right foot, rear inner M10 cannot be reached**: the X belt runs over its access hole (X 345, Y 262) | Hole fully under the belt | Move the rear row of both feet to **X 395 and X 430**. Use **M10 × 25 for every bolt in the 25 thick step** (X 395, 420 and 430): an M10 × 30 leaves only 3 mm of foot |
| 3 | **Y BK12 and BF12 touch the foot** at the inner edge of the step | 0 gap (BK edge and step edge both at X 380) | Start the step at **X 378** |
| 4 | **X block nearly reaches BK12 and BF12** at the end of travel | 1.25 mm | X block pitch **90** instead of 100, gap becomes 6.25 |
| 5 | **Flange 1 mm above the seat and the wall top** | 1 mm | Accept once the flange is measured. Keep chips out of this gap |

## Checked and fine

| Check | Result |
|---|---|
| Rail on the flat | Rail edge 2 inside the flat, BK12 edge 10 inside |
| Top arm over BK12 | 2 clear (BK12 top 392, arm 394) |
| Y BK12 and BF12 under the foot step | 2 clear (top 168, step 170) |
| Bottom arm over the wall | Arm stops at X 290, wall starts at 305 |
| Foot behind, Y motor mount | 6.25 clear at the back of travel |
| Blocks stay on the rails | X 11.25, Y 5 at the front and 17.5 at the back |
| M5 × 20 rail bolts | 7 mm of thread in the 8 mm wall |
| M10 to nearest Y block bolt | 17.5 between centres |

## Moving mass

**73.4 kg**, of which the beam is 31.7 kg. The centre of mass is **170.5 behind the spindle, 30.5 behind the carriages** (carriages at 140). The two rear Y blocks carry about 70 % of the weight when standing still. That is a small load for these blocks, and it keeps the tub unchanged, so I would leave the carriages at 140.

## Not verified

- **Flat width.** 102 assumes an outer corner radius of up to 24. Check it on the real tube or the supplier's data sheet before drilling.
- **Ball nut flange.** Measure the real nut: round or with flats. Flats of 40 would only reduce the overlap to 0, so the slots are still needed.
- **Assumed:** Z motor position, spindle mass, X motor plate and outboard bearing position.
- **Not modelled:** cables, Z screw supports, bolt heads, the bracket that holds the X outboard bearing. That bracket must leave the holes at X 395 and X 430 open.

## Build notes

- Keep the **weld seam off the rail faces**: put it on the front or rear face of the beam.
- Pour order: top seat first with the beam level. After cure, turn the beam over, rest the cured seat on 3 equal pads on the levelled tub rail seats, pour the bottom seat, then check parallelism with an indicator.
- Fit the feet on the Y blocks first, then the beam.

## Owner's answers (18 Nov 2026)

1. **Saddle: steel (D-165).** Sizes open. At the sizes above it adds about 13.4 kg, so about 86.8 kg moving.
2. **X motor: "no fold over".** Read as no belt fold, motor in line with the X screw. **Not confirmed yet.** If so, the motor ends about X 512, about 67 past the beam end, and it covers the rear access holes at X 345 and X 420. Not yet run through the check.
3. **Beam to foot: M10 through access holes (D-166).** Positions depend on answer 2.
4. **Fixes 1 to 4: the owner wants to discuss them first.** None is applied.

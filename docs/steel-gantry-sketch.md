# Steel gantry layout sketch (18 Nov 2026)

**Status: proposal, not agreed. No D-numbers yet.** Drawing: `cad/v2/out/steel_gantry_sketch.png`. Numbers: `cad/v2/out/steel_gantry_sketch.json`. Script: `cad/v2/steel_gantry_sketch.py`. It uses the table in the 18 Nov handover entry unchanged, so the problems below are still in the drawing.

## Result

The layout works apart from the 5 problems below. The check covers the whole X, Y and Z travel. Every part is a bounding box.

| # | Problem | Size | Proposed fix |
|---|---|---|---|
| 1 | **Ball nut flange hits the top arm** (X) and **the foot step** (both Y nuts) | 4 mm overlap. The DFU1605 model has a round Ø48 flange, the housing face is only 20 from the axis | Pocket Ø50 × 5 deep in the arm and in each foot step. Flange of each Y nut faces the front, so the pocket stays clear of the M10 at Y 190 |
| 2 | **Right foot, rear inner M10 cannot be reached**: the X belt runs over its access hole (X 345, Y 262) | Hole fully under the belt | Move the rear row of both feet to **X 395 and X 430**, M10 × 25 (3 mm of foot would be left under an M10 × 30) |
| 3 | **Y BK12 and BF12 touch the foot** at the inner edge of the step | 0 gap (BK edge and step edge both at X 380) | Start the step at **X 378** |
| 4 | **X block nearly reaches BK12 and BF12** at the end of travel | 1.25 mm | X block pitch **90** instead of 100, gap becomes 6.25 |
| 5 | **Flange 1 mm above the seat and the wall top** | 1 mm | Accept once the flange is measured. Keep chips out of this gap |

## Checked and fine

| Check | Result |
|---|---|
| Rail on the flat | Rail edge 2 inside the flat, BK12 edge 10 inside |
| Top arm over BK12 | 2 clear (BK12 top 392, arm 394) |
| Bottom arm over the wall | Arm stops at X 290, wall starts at 305 |
| Foot behind, Y motor mount | 6.25 clear at the back of travel |
| Blocks stay on the rails | X 11.25, Y 5 at the front and 17.5 at the back |
| M5 × 20 rail bolts | 7 mm of thread in the 8 mm wall |
| M10 to nearest Y block bolt | 17.5 between centres |

## Moving mass

**73.4 kg**, of which the beam is 31.7 kg. The centre of mass is **170.5 behind the spindle, 30.5 behind the carriages** (carriages at 140). The two rear Y blocks carry about 70 % of the weight when standing still. That is a small load for these blocks, and it keeps the tub unchanged, so I would leave the carriages at 140.

## Not verified

- **Flat width.** 102 assumes an outer corner radius of up to 24. Check it on the real tube or the supplier's data sheet before drilling.
- **Ball nut flange.** Measure the real nut: round or with flats. Flats of 40 would only reduce the overlap to 0, so the pockets are still needed.
- **Assumed:** Z motor position, spindle mass, X motor plate and outboard bearing position.
- **Not modelled:** cables, Z screw supports, bolt heads.

## Build notes

- Keep the **weld seam off the rail faces**: put it on the front or rear face of the beam.
- Pour order: top seat first with the beam level. After cure, turn the beam over, rest the cured seat on 3 equal pads on the levelled tub rail seats, pour the bottom seat, then check parallelism with an indicator.
- Fit the feet on the Y blocks first, then the beam.

## Questions for the owner

1. **Saddle:** aluminium 3-piece (pick) or steel?
2. **X motor:** behind the beam (pick) or above it?
3. **Beam to foot:** M10 through access holes (pick) or welded end plates?
4. **The 4 fixes above (1 to 4):** accept them all (pick)?

# Steel gantry layout sketch (18 Nov 2026)

**Status: layout not agreed.** Decided so far: steel saddle (D-165), M10 beam joint (D-166), X motor in line with the screw (D-167). Drawing: `cad/v2/out/steel_gantry_sketch.png`. Numbers: `cad/v2/out/steel_gantry_sketch.json`. Script: `cad/v2/steel_gantry_sketch.py`.

## Result

As drawn, the layout has **4 clashes**, from problems 1 and 2. **With fixes 1 to 4 applied the check finds no clashes** (`python cad/v2/steel_gantry_sketch.py --fixes`). None of the fixes is agreed, so the drawing still shows the problems. The check covers the whole X, Y and Z travel, and every part is a bounding box.

| # | Problem | Size | Proposed fix |
|---|---|---|---|
| 1 | **Ball nut flange hits the top arm** (X) and **the foot step** (both Y nuts) | 4 mm overlap. The DFU1605 model has a round Ø48 flange, the housing face is only 20 from the axis | Relief slot **12 × 30 × 5 deep** in the arm and in each foot step, over the flange only. Flange of each Y nut faces the front, so its slot stays clear of the M10 bolts |
| 2 | **X motor hits the beam top** | 1 mm overlap (motor bottom 344, beam top 345) | **5 mm pads under BK12 and BF12.** The X screw, nut housing, spacers and top arm all rise 5. Motor then clears the beam by 4 |
| 3 | **Y BK12 and BF12 touch the foot** at the inner edge of the step | 0 gap (both at X 380) | Start the step at **X 378** |
| 4 | **X block nearly reaches BK12 and BF12** at the end of travel | 1.25 mm | X block pitch **90** instead of 100, gap becomes 6.25 |

## What the in-line X motor changes

- **Length:** the mount runs X 327 to 387 and the motor ends at about **X 512**, 67 past the beam end and the tub side. The enclosure must allow for this on the right.
- **Rear M10 bolts on the right foot:** the holes at X 345 and X 420, Y 262 are under the mount and motor. Tighten these bolts **before** fitting the mount and motor. To re-tighten them later, take the motor and mount off.
- **X screw:** it now ends at about X 362, so it is about **681 long, not 700**. The X drive stub drawing for LiMo must change before the 4 Jan order.
- **Mount seat:** it sits on the bare beam top, beyond the levelled seat. Shim it to line up with the screw.
- **Parts list, not changed yet:** the X pulleys (M15), belt (M16) and outboard bearing (M17) are no longer needed. One more coupling (M08, 3 to 4) and one more NEMA 24 mount (M13, 1 to 2) are needed. The 60 mm mount length is assumed: check it against the LiMo mount.

## Checked and fine

| Check | Result |
|---|---|
| Rail on the flat | Rail edge 2 inside the flat, BK12 edge 10 inside |
| Top arm over BK12 | 2 clear |
| Y BK12 and BF12 under the foot step | 2 clear (top 168, step 170) |
| Bottom arm over the wall | Arm stops at X 290, wall starts at 305 |
| Foot behind, Y motor mount | 6.25 clear at the back of travel |
| Blocks stay on the rails | X 11.25, Y 5 at the front and 17.5 at the back |
| M5 × 20 rail bolts | 7 mm of thread in the 8 mm wall |
| M10 to nearest Y block bolt | 17.5 between centres |
| M10 in the 25 thick foot step (X 420) | Use **M10 × 25**: an M10 × 30 leaves only 3 mm of foot |

## Moving mass

**86.8 kg** with the steel saddle at the sizes first proposed for aluminium (plate 180 × 400 × 20, 2 arms 180 × 130 × 25). The beam is 31.7 kg and the saddle 20.5 kg. The centre of mass is **27.1 behind the carriages**, and the rear Y blocks carry about 68 % of the weight when standing still. Thinner steel would cut this: the saddle sizes are still open.

## Not verified

- **Flat width.** 102 assumes an outer corner radius of up to 24. Check it on the real tube or the supplier's data sheet before drilling.
- **Ball nut flange.** Measure the real nut: round or with flats. Flats of 40 would only reduce the overlap to 0, so the slots are still needed.
- **Assumed:** Z motor position, spindle mass, X motor mount length.
- **Not modelled:** cables, Z screw supports, bolt heads.

## Build notes

- Keep the **weld seam off the rail faces**: put it on the front or rear face of the beam.
- Pour order: top seat first with the beam level. After cure, turn the beam over, rest the cured seat on 3 equal pads on the levelled tub rail seats, pour the bottom seat, then check parallelism with an indicator.
- Fit the feet on the Y blocks first, then the beam, then the X motor mount and motor.

## Open for the owner

1. Fixes 1 to 4: accept or change each.
2. Steel saddle plate and arm thicknesses.
3. Parts list changes for the in-line X motor.

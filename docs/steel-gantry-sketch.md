# Steel gantry layout sketch (18 Nov 2026)

**Status: no clashes. Waiting for the owner to agree the layout.** Decisions: D-164 to D-166, D-168 to D-171. Drawing: `cad/v2/out/steel_gantry_sketch.png`. Numbers: `cad/v2/out/steel_gantry_sketch.json`. Script: `cad/v2/steel_gantry_sketch.py`.

## Result

The check covers the whole X, Y and Z travel and finds **no clashes**. Every part is a bounding box. Every wrench access hole is clear.

| Item | Layout |
|---|---|
| Beam | SHS 150 × 150 × 8, 890 long, rails on the top and bottom faces |
| Saddle | Steel (D-165): front plate 180 × 400 × 20 and 2 arms 180 × 130 × 25. Sizes still open |
| X motor | **Folded over the top of the screw** (D-168): axis 137.5 above the screw, body inboard, 375 belt. Ends inside the beam length |
| Drag chain | On the back of the gantry. No gantry part stands behind the beam's rear face |
| X screw | 700, as ordered. Pulleys, belt and outboard bearing stay in the parts list |
| Ball nut flanges | 40 across the flats, flats top and bottom (D-170). No relief slots |
| Foot step | Starts at X 378 (D-169) |
| X block pitch | 90 (D-169): 6.25 clear of BK12 and BF12 at the end of travel |

## For the owner to agree

1. **Do the M10 bolts need holes in the top wall?** Owner asked why, 18 Nov. Proposal: **no top holes.** All 4 bolts per foot are within 100 of the open tube end, and the inside of the tube is 134 square, so they can be fitted and tightened from the end. The bolts then go through the bottom wall only, and the rear row can go back to X 345 and X 420. Use **M10 × 25** in the 25 thick foot step.
2. **1 mm relief over each nut flange**, in the top arm and both foot steps. The flats are nominally level with the housing face. If a flange stands proud, the housing cannot seat flat and the nut is forced out of line. Owner asked why, 18 Nov: not decided.

**Agreed:** nut housings 20 off centre, towards the flange (D-171).

## Checked and fine

| Check | Result |
|---|---|
| Rail on the flat | Rail edge 2 inside the flat, BK12 edge 10 inside |
| Top arm over BK12 | 2 clear |
| Y BK12 and BF12 under the foot step | 2 clear (top 168, step 170), 2 clear of the step edge |
| X motor over the top arm | 62.5 clear |
| Foot behind, Y motor mount | 6.25 clear at the back of travel |
| Blocks stay on the rails | X 16.25, Y 5 at the front and 17.5 at the back |
| M5 × 20 rail bolts | 7 mm of thread in the 8 mm wall |
| M10 to nearest Y block bolt | 17.5 between centres |

## Moving mass

**86.8 kg** with the steel saddle at the sizes above. The beam is 31.7 kg and the saddle 20.5 kg. The centre of mass is **27.1 behind the carriages**, and the rear Y blocks carry about 68 % of the weight when standing still. Thinner steel would cut this.

## Not verified

- **Flat width.** 102 assumes an outer corner radius of up to 24. Check it on the real tube or the supplier's data sheet before drilling.
- **Ball nut flange.** Sizes are from the owner's DFU01605-4 catalogue sheet. Measure the nut when it arrives.
- **Assumed:** Z motor position, spindle mass, X motor bracket shape.
- **Not modelled:** the drag chain itself (size and route not chosen), cables, Z screw supports, bolt heads.

## Build notes

- Keep the **weld seam off the rail faces**: put it on the front or rear face of the beam, and allow for it if the drag chain mounts there.
- Pour order: top seat first with the beam level. After cure, turn the beam over, rest the cured seat on 3 equal pads on the levelled tub rail seats, pour the bottom seat, then check parallelism with an indicator.
- Fit the feet on the Y blocks first, then the beam, then the X motor bracket.
- Fit each ball nut with its flats top and bottom.

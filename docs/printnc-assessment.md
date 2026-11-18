# PrintNC V4 gantry on Type 0 (18 Nov 2026)

**Status: the model is `Type_0_v3`. Version 1 is saved. The support swap below is in the open document and is NOT saved. 6 features still fail (1 error, 5 warnings), the same as version 1.** Decisions: D-172 to D-184.

## Sources

| Source | What it is |
|---|---|
| `PrintNC V4 Metalcutter V4.0.33 Elements to take.step` (31 MB, untracked, not committed) | 117 named parts: gantry, rollers, Z axis, axis hardware, printed and milled parts. No base frame. X rails 875, Y rails 1375. A different size from the open document |
| Fusion document `PrintNC V4 Metalcutter V4.0.38` (open, unsaved) | Parametric model, 94 user parameters. **This is the model being scaled** |

## Parameters changed in the open document

Parameters only. No direct modelling.

| Parameter | Was | Now | Why |
|---|---|---|---|
| `XCuttingArea` | 625 | **435** | Gives the 600 X rail |
| `YCuttingArea` | 625 | **385** | Gives the 550 Y rail (D-175) |
| `XGantryWidth` | 75 | **120** | 120 wide (D-177) |
| `XGantryHeight` | 75 | **120** | 120 tall (D-177) |
| `XGantryThick` | 4 | **8** | 8 wall |
| `XGantryRadius` | 10 | **16** | Trial value. The real tube corner is not verified |
| `XGantryOffset` | 25 | **−35** | Negative moves the beam towards the rear. Gives the L bracket its 50 seat (D-177) |
| `AdjXGanYRolHoles` | 1 | **13** | Beam bolt rows 25 either side of the centre bolt (D-178) |
| `d4192` (joint Rigid 305, L bracket position) | `… + XGantryOffset` | **`( YRollerLength / 2 ) - ( XGantryWidth / 2 ) - XGantryOffset`** | The original sign moved the bracket the opposite way to the beam |

## Result after the rebuild

| Item | Value |
|---|---|
| X rails, Y rails | 600, **550** |
| Gantry length | 775 |
| Y rail spacing | **700**, tub widened to suit (D-173) |
| X rails | Top and bottom of the beam, seats 150 apart |
| Top roller, bottom roller | 120 wide, 125 wide by formula |
| X screw, Y screw | 700, **650** |
| Y screw position | **Directly above the Y rail**, X ± 350 (D-174) |
| Length of the Y rail and its supports in line | **684** in the 690 tub, 3 clear at each end |
| Y block travel on the 550 rail | About 379 with the model's blocks. Type 0 needs 350 |

## Beam section (D-177)

Sharp-corner figures, 8 wall.

| Property | 150 tall × 75 wide × 8 (D-176) | 120 × 120 × 8 (D-177) | Change |
|---|---|---|---|
| Bending, vertical load (mm⁴) | 9.26 × 10⁶ | 7.53 × 10⁶ | 1.2 times less stiff |
| Bending, horizontal load (mm⁴) | 2.98 × 10⁶ | 7.53 × 10⁶ | **2.5 times stiffer** |
| Twist constant (mm⁴) | 6.93 × 10⁶ | 11.2 × 10⁶ | **1.6 times stiffer** |
| Mass at 775 long, in the model | 19.3 kg | 20.7 kg | 1.4 kg heavier |

Flat on the 120 wide faces: 88 with a 16 corner radius, 72 with a 24 radius. The 20 wide X rail and the 60 wide X BK12 and BF12 risers fit both.

## Still failing (6 features)

| Timeline | Feature | Part | Note |
|---|---|---|---|
| 543 | Rigid 164 | M6 × 12 bolt to XRollerShim | Missing joint origin |
| 1015 | Rigid 110 | XGantry Trigger Mount to XGantry | Joint failed |
| 613, 616, 617, 618 | Extrude2, Chamfer2, Fillet1, Extrude4 | YRoller-Gantry Drill Guide | **Caused by the first 150 beam trial.** They stayed when the beam went back to 75, and a full recompute did not clear them |

## Y roller brace seat (D-177, rebuilt in Fusion 18 Nov 2026)

The L bracket `YRollerBrace` joins the Y roller to the front face of the beam. Its foot is 50 deep. `XGantryOffset` is negative towards the rear, so the roller top in front of the beam = 75 − (beam width ÷ 2) − `XGantryOffset`.

| Item | Result with 120 × 120 × 8 at offset −35 |
|---|---|
| Beam on the roller | Y 506.5 to 626.5. The roller runs Y 456.5 to 606.5 |
| Roller top in front of the beam | **50**: the bracket foot sits flush with the roller end |
| Bracket bolts into the roller | 4, at 12 and 32 from the roller end. Holes line up |
| Bracket bolts into the beam | 4, at Z 223 and 268. Holes line up |
| Beam past the roller's rear end | 20 (12.5 past the fill plate) |
| Clear above the BF12 screw support | 7 |
| Clashes on the structure | None between the beam, bracket and roller |

**Rear beam bolts (D-178):** the rows are at Y 541.5 and 591.5, 25 either side of the centre bolt at Y 566.5. The rear row is 15 from the roller end, and the front row leaves about 6.8 of steel to the access hole at Y 554. The holes in the beam and roller line up after the rebuild. All 5 bolts per side thread into the 3 wall, about 3 threads each.

**Lower bracket bolts:** Z 223 is 18 above the beam's underside. The flat starts 16 up with a 16 corner radius, and the bolts land on the corner with a 24 radius. Check the real tube radius before drilling.

**Other clashes reported:** PrintNC's dual-carriage Z tram bar overlaps the top roller, and that Z axis is not used on Type 0 (D-172). The Y roller sensor mount overlaps the roller side by 0.5.

Checked at one gantry position. The full travel has not been run.

## Hidden in the Fusion model (18 Nov 2026)

Visibility only, nothing is deleted. Turn the eye icon back on to restore a part.

| Hidden | Why |
|---|---|
| Base frame: XFrame, YFrame tubes, wasteboard, cutting area, their end caps and bolts | The epoxy granite tub replaces them |
| PrintNC Z axis: single and dual carriage, spindle, Z hardware, mounts and bolts | Type 0 keeps its own Z axis (D-172) |
| Printed drill guides | Build aids for the steel frame, not machine parts |

Still shown: beam, X and Y rollers, L brackets, rails, blocks, screws, supports, motors, sensors, cable chain brackets and their bolts. The rail blocks, nuts and motors are still PrintNC's models, not the Type 0 parts.

## Screw supports changed to BK12 (D-180, 18 Nov 2026)

Visibility only, on X, Y and Y2. The timeline stayed at 1182 items with 1 error and 5 warnings.

| Hidden | Shown |
|---|---|
| `HM12-57` (3) | `BK12` (3) |
| `HM12 M6x50` bolts (3 sets) | `Nema24 Plate` (3) |

The NEMA 23 motors and D30L40 couplings are still shown until the imported parts go in. No BK12 bolts are modelled yet.

## Moving the Y motors to the back (D-181): not done, Y travel falls short

Measured on 18 Nov 2026 with temporary copies of the parts. The model was not changed. Rear is +Y.

| Y travel, stop to stop | Motors at the front (model now) | Motors at the back |
|---|---|---|
| Front limit | Blocks reach the rail end | Blocks reach the rail end |
| Rear limit | Blocks reach the rail end | Fill plate hits the BK12 |
| **Travel** | **386** | **338** (Type 0 needs 350) |

The BK12 is longer in line than the BF12, so it stops the roller earlier at the rear.

| Part hitting at the rear, motors at the back | Travel if this is the limit |
|---|---|
| `Y 1610 Fill Plate` against BK12 | 338 |
| `YRoller` against BK12 | 352 |
| `Y HGW20CC` block against the BK12 riser | 358 |

- These use the model's PrintNC blocks and fill plate, not the Type 0 HGH20CA blocks.
- The figures are hard contact, with no allowance for limit switches or overtravel.
- The 3 gap at each tub end stays, because the drive line turns about its own centre.
- The rear end of the drive would be at Y 762, 109 behind the tub with the NEMA 23. D-142 allows about 185. The NEMA 24 length is still to be taken from its datasheet.

**How the model is tied together:** `Rigid 311` and `Rigid 312` locate the two risers. The BK12, motor plate, screw, coupling, BF12 and motor follow them through joints. The nut stays with the roller. Y2 is made by mirror features from the Y groups, so it should follow, but this has not been tested.

## Not checked

- Whether 120 × 120 × 8 tube can be bought. It is not in `docs/steel-rhs-suppliers.md`.
- Clashes over the full travel. The model has not been run through its travel.
- The real corner radius of the tube.

## Differences parameters will not fix

| Part | PrintNC model | Type 0 parts list |
|---|---|---|
| Rail blocks | HGW20CC | HGH20CA (parameters change the drill guides only) |
| X and Y screw nuts | SFU1610 | DFU1605 |
| Motors | NEMA 23 in line | NEMA 24, X folded over the screw (D-168) |
| Z axis | HGH15, 1204 screw | Stays Type 0 (D-172): HGH20CA 350, 1605 screw, brake motor |

## Open for the owner

1. **LiMo prices:** confirm the HGH20CA 550 set, the DFU1605 650 set and the shipping in the LiMo basket. `docs/bom.csv` still shows the old 600 prices.
2. **Drill guide:** repair the 5 failed features by undo or by hand in Fusion, or replace the guide.
3. **Steel gantry sketch:** D-172 replaces its gantry layout, so its 2 open items need closing.
4. **Y cable chain brackets:** they are still shown but were mounted on the hidden frame. Keep or hide them once the chain route on the tub is chosen.

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
| 543 | Rigid 164 | M6 × 12 bolt to XRollerShim (shim hidden, D-209) | Missing joint origin |
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

The NEMA 23 motors and D30L40 couplings have since been replaced and hidden (see the DFU1605 section below). No BK12 bolts are modelled yet.

## Moving the Y motors to the back (D-181): risers and rails moved

**Correction:** the earlier figure of 338 Y travel was wrong. It left the rail where it was. The rail must shift 61.5 towards the front, to sit between the turned risers, and then the motors at the back cost no travel.

| Y rail | Y screw | Tub length | Y travel, blocks to rail ends |
|---|---|---|---|
| **550 (D-175, kept by D-185)** | 650 | 690 | **386.2** (550 less the measured 163.8 block span; the model's 385 slider range was run, 18 Nov) |
| 570 (tried, dropped) | 670 | 710 | 406 (measured over 41 positions, no clashes) |

Type 0 needs 350. In the 570 trial the tightest gaps at the ends of travel were 1.0 from block to riser and 4.1 from the SFU1610 nut to the BF12. These use PrintNC's blocks. The 550 figures below replace this trial.

**Open document, not saved (timeline 1183, 1 error, 5 warnings, the same failures as version 1):**
- `YCuttingArea` is back to 385 and `calcYRailLength` has its original formula.
- New sketch `D-181 Y riser targets`, with plain-number points at (-350, -23, 125) and (-335, 561, 125).
- `Rigid 311` and `Rigid 312` point at that sketch, angle 0, flipped. Risers, BK12, BF12, plate, screw, coupling, motor and bolts followed, and Y2 followed through its mirror features.
- The rear of the NEMA 23 motor was at Y 762, 109 behind the tub. D-142 allows about 185. The NEMA 24 figure is in the DFU1605 section below.

- **Y rails moved 61.5 forward (18 Nov):** `d80` is now `calcYRailStartingHole + 36.5 mm + 61.5 mm` and `d196` is `-61.5 mm`. Both rails run Y 2.5 to 552.5, and all 9 holes on each rail line up with the frame holes (Y 37 to 517). The risers did not move. Timeline 1183, 1 error, 5 warnings, the same failures as version 1.

**Travel check at 550 (18 Nov), measured at both ends of the 385 slider range:**

| Gap | Measured |
|---|---|
| Block to rail end | 0.61 |
| Block to riser | 1.61 |
| Grease fitting to riser | 2.0 |
| SFU1610 nut to BF12 | 4.7 |
| Gantry tube to rear BK12 | 14.7 |

These are minimum distances between bodies, except the rail end and nut gaps, which are read along Y. Fusion's interference check is not used as evidence: it also reported nothing for the nut on its screw, so it was not shown to detect a hit. The DFU1605 nut has since been fitted at the same seat, and its extra length runs into the roller, so the 4.7 is unchanged.

**Parts that moved 61.5 forward with the rails:** the rollers, the gantry and X rails (now Y 495 to 515), the Y trigger mount, the roller sensor mount and the cable chain supports. The last three follow the frame holes, and their positions have not been reviewed.

**Two earlier ways of moving the rail failed, and both were undone:**
1. `Rigid 2` offset of -61.5 moves the rail in Z, not Y, and raises the warnings to 10.
2. Pointing `Rigid 2` at a new sketch point moved the rail occurrence and its bolts by -61.5, but the rail body stayed at Y 64 to 614. The Y2 rail and its whole drive then moved +61.5. Y2 is held by `Rigid 202` and `Rigid Group 247`, which holds the Y2 rail and drive together.

**Why the body stays put (found 18 Nov):** only the first rail hole (`Base Feature1`) follows the occurrence, and `Rigid 2` pins that hole to the frame hole at Y 578.5. The rest of the body hangs off the frame: `Extrude1` runs to the `YFrame` end face at Y 650 (offset `d196`), `MoveFace2` pulls that end back to 614, and `Extrude2` adds the rail length. `Rigid 202` pins Y2 the same way, to the mirrored frame hole.

**So the frame hole and the rail end must move together.** The frame hole is `d80` in sketch `YFrameTopHoles` (`calcYRailStartingHole + 36.5 mm`, measured from Y 650). The rail end is `d196`. Changing `d196` alone would leave the first hole outside the rail.

## DFU1605 nuts, 24HS40 motors and D25L35 couplings (D-180, D-182), 18 Nov

Fitted on X, Y and Y2 in `Type_0_v3`. Timeline 1205, 1 error, 5 warnings, the same failures as version 1. **Modified after version 2, not saved.**

- **Nuts:** `dfu1605_nut.step`, flange on the old SFU1610 seat, bolt holes in line, held to the hidden SFU1610 nut by an as-built joint. The nut body runs 100 into the roller. The vendor's 130 screw stub is hidden.
- **Motors:** `24hs40_motor.step`, flange on the back face of the `Nema24 Plate`, held by an as-built joint. Measured from the STEP: body 125 behind the flange, shaft Ø10 × 20, pilot Ø38.1, holes on a 50 square. The plate has the same 50 square.
- **Motor length confirmed from the datasheet (`cad/vendor/24hs40_motor.pdf`, 18 Nov):** the 24HS40-5004D-E1000 body is 122 ± 1 behind the flange and the shaft is Ø10 × 21 ± 1. The STEP (product name `24HE40-5004D-E1000`) shows 125 and 20. The STEP stays in the model, so the real motor rear is about 3 closer than modelled and the real shaft goes about 1 further into the coupling.
- **Couplings:** `D25L35 Coupling (stand-in)` is a plain Ø25 × 35 sleeve with a Ø10 bore, because no vendor CAD exists.
- **Hidden, not deleted:** SFU1610 nuts, their M6 90° grease fittings, NEMA 23 motors, D30L40 8-10 couplings, and the M4 × 16 motor bolts.

| Check | Result |
|---|---|
| Y motor rear | Y 787, 134 behind the tub (D-142 allows about 185) |
| X motor rear | X 527, 139.5 past the 387.5 beam end |
| DFU1605 nut to X BK12 at full X travel | 6.9 |
| Clashes for nuts, motors and couplings at Y 0, Y -385 and X -430 | None by body-to-body overlap once the M4 bolts were hidden |

**Open problem: the coupling grips too little.** The screw end and the motor shaft are 21.2 apart on all three axes, so a 35 long coupling grips only **6.9 of each shaft**. Moving the motor plate 12 towards the screw would give 12.9 of grip and leave 1.6 between coupling and BK12. That means shortening the `BKHM12 Riser` on Y and the matching X part. **The owner chose this (D-186). It is now in the model: see the D-186 and D-187 section below.** Y motor rear at Y 775, 122 behind the tub. The coupling's real bore depth has not been checked.

The motor STEP is one solid that includes its cable tails, so those stick out 133 from the shaft, outboard on Y and upward on X. Ignore them for clearance. The vendor nut has no lube port or flange flats, so the real grease fitting position is not modelled. The M5 motor bolts are not modelled.

## Motor plates moved and risers shortened (D-186, D-187), 18 Nov

In `Type_0_v3` on X, Y and Y2. Timeline 1230, 1 error, 5 warnings, the same failures as version 1. **Modified after version 3, not saved.**

- **Plates:** `Rigid 4` offset is -12 on Y (`d4556`) and X (`d4568`). Y2 follows through its mirror.
- **Motors and couplings:** their as-built joints did not follow the plate, so they were rebuilt (`Rigid 370` to `Rigid 375`). Motors moved 12, couplings 6, which keeps each coupling centred between screw and shaft.
- **Risers:** end face at Y 638 (X 378 on X), R4 corners restored, old rear holes filled, new rear holes at Y 629 (X 369), M6 plate holes 12 deep.
- **Bolts:** rear M6 x 30 bolts moved to the new holes. The second rear bolt on Y and Y2 was at X -305 and 305, outside the riser, and now sits in the correct hole at X -365 and 365.
- **X gantry tube:** old tapped holes at X 381 filled, new 5 mm holes at X 369.

| Check | Result |
|---|---|
| Coupling grip, screw and shaft, X, Y and Y2 | 12.9 each |
| Coupling to BK12 | 1.6 |
| Y motor rear | Y 775 |
| X motor rear | X 515 |
| Clashes at the motor end, Y and Y2 | None |
| Clashes at the motor end, X | Only the M6 bolt threads in the gantry tube, as intended |

**Still to settle:**

1. **Tub holes.** The tub has no modelled holes for the Y riser bolts, so the new Y 629 position must go into the tub drilling.
2. **Front Y riser bolts.** The bolts at X -305 and 305 (Y 561 and Y -6) are also outside the risers. They were already wrong and were not moved.
3. **Assembly order.** Fit the rear riser bolts before the coupling, because the coupling sits close above them.

The 0.5 edge chamfers were not re-cut on the new end faces, and the new holes carry no modelled thread.

## X riser side holes moved (D-189), 18 Nov

In `Type_0_v3`. Timeline 1235, 1 error, 5 warnings, the same failures as version 1. **Modified after version 4, not saved.**

- **Holes:** the two M4 holes at X 375.5 are filled and re-cut at X 369.5, Z 348.5, on the Y 475 and Y 535 faces. The new holes copy the shape of the pair at X 325.5.
- **Screw:** the `M4x8 Pan Head` at X 375.5 moved to X 369.5.
- **Spacing:** 44 to the holes at X 325.5, was 50. Nothing in the model bolts to these holes and the pan head screws clamp no part, so check this if a part is added there later.

| Check | Result |
|---|---|
| Old holes | Fully filled, no void left |
| New hole volume against the X 325.5 holes | 87.18 mm³ each, the same |
| Wall around each new hole, measured with a Ø6 test cylinder | At least 1 all round |

## Not checked

- Whether 120 × 120 × 8 tube can be bought. It is not in `docs/steel-rhs-suppliers.md`.
- Clashes over the full Z travel, and a full X check. Y and X were checked at their ends only for the parts listed above, with the PrintNC blocks still in the model.
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

# PrintNC V4 gantry on Type 0 (18 Nov 2026)

**Status: the parametric model is set to the Type 0 sizes, with 8 features still failing. The Fusion document is NOT saved.** Decisions: D-172 to D-177.

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

## Still failing (8 features)

| Timeline | Feature | Part | Note |
|---|---|---|---|
| 60 | Thread1 | YRoller | **New with D-177.** The rear beam bolt holes are 3 from the roller end, so the M6 thread breaks out. See the seat section |
| 543 | Rigid 164 | M6 × 12 bolt to XRollerShim | Missing joint origin |
| 1015 | Rigid 110 | XGantry Trigger Mount to XGantry | Joint failed |
| 613, 614, 616, 617, 618 | Extrude2, Chamfer1, Chamfer2, Fillet1, Extrude4 | YRoller-Gantry Drill Guide | **Caused by the first 150 beam trial.** They stayed when the beam went back to 75, and a full recompute did not clear them |

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

**Rear beam bolts, not solved:** the rear row into the roller is at Y 603.5, 3 from the roller end, so a hole breaks out of the 3 wall (Thread1 fails). The carriage access holes at Y 554 and 594 leave no clean symmetrical position for the row. Options: tap the row into the 15 thick fill plate under it, or set `AdjXGanYRolHoles` to 17, which leaves about 1.7 of steel between holes.

**Lower bracket bolts:** Z 223 is 18 above the beam's underside. The flat starts 16 up with a 16 corner radius, and the bolts land on the corner with a 24 radius. Check the real tube radius before drilling.

**Other clashes reported:** PrintNC's dual-carriage Z tram bar overlaps the top roller, and that Z axis is not used on Type 0 (D-172). The Y roller sensor mount overlaps the roller side by 0.5.

Checked at one gantry position. The full travel has not been run.

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
4. **Rear beam bolts:** choose how the rear row fixes to the Y roller (see the seat section).

# PrintNC V4 gantry on Type 0 (18 Nov 2026)

**Status: the parametric model is set to the Type 0 sizes, with 8 features still failing. The Fusion document is NOT saved.** Decisions: D-172 to D-176.

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
| `XGantryWidth` | 75 | **75** | 75 wide (D-176) |
| `XGantryHeight` | 75 | **150** | 150 tall (D-176) |
| `XGantryThick` | 4 | **8** | 8 wall (D-176) |
| `XGantryRadius` | 10 | **16** | Trial value. The real tube corner is not verified |
| `XGantryOffset` | 25 | **0** | With the 150 × 75 beam, 25 gives 10 problems and 0 gives 8 |

## Result after the rebuild

| Item | Value |
|---|---|
| X rails, Y rails | 600, **550** |
| Gantry length | 775 |
| Y rail spacing | **700**, tub widened to suit (D-173) |
| X rails | Top and bottom of the beam, seats 150 apart |
| Top roller, bottom roller | 75 wide, 100 wide by formula |
| X screw, Y screw | 700, **650** |
| Y screw position | **Directly above the Y rail**, X ± 350 (D-174) |
| Length of the Y rail and its supports in line | **684** in the 690 tub, 3 clear at each end |
| Y block travel on the 550 rail | About 379 with the model's blocks. Type 0 needs 350 |

## Beam section (D-176)

Sharp-corner figures, 8 wall.

| Property | 150 × 150 × 8 | 150 tall × 75 wide × 8 | Change |
|---|---|---|---|
| Bending, vertical load (mm⁴) | 15.3 × 10⁶ | 9.26 × 10⁶ | 1.65 times less stiff |
| Bending, horizontal load (mm⁴) | 15.3 × 10⁶ | 2.98 × 10⁶ | **5.1 times less stiff** |
| Twist constant (mm⁴) | 22.9 × 10⁶ | 6.93 × 10⁶ | **3.3 times less stiff** |
| Mass at 775 long | 27.6 kg | 20.3 kg (19.3 kg in the model) | About 8 kg lighter |

Flat on the 75 wide faces: 43 with a 16 corner radius, 27 with a 24 radius. The 20 wide X rail fits both. **The 60 wide X BK12 and BF12 risers do not fit either flat.** The gantry brace touches the beam's front face and does not clash.

## Still failing (8 features)

| Timeline | Feature | Part | Note |
|---|---|---|---|
| 494 | Extrude8 | XRollers | No target body |
| 543 | Rigid 164 | M6 × 12 bolt to XRollerShim | Missing joint origin |
| 1015 | Rigid 110 | XGantry Trigger Mount to XGantry | Joint failed |
| 613, 614, 616, 617, 618 | Extrude2, Chamfer1, Chamfer2, Fillet1, Extrude4 | YRoller-Gantry Drill Guide | **Caused by the first 150 beam trial.** They stayed when the beam went back to 75, and a full recompute did not clear them |

## Y roller brace seat (measured 18 Nov 2026, not decided)

The L bracket `YRollerBrace` joins the Y roller to the front face of the beam. Its foot is 50 deep, with M6 bolt rows 18 and 38 in front of the beam face. The roller is 150 long.

Roller top in front of the beam = 75 − (beam width ÷ 2) + `XGantryOffset`. It needs to be at least 50, which puts the front bolt row 12 from the roller end.

| Beam width | `XGantryOffset` | Roller top in front of beam | Front bolt row | Beam past roller rear | State |
|---|---|---|---|---|---|
| 75 | 25 (PrintNC's value) | 62.5 | 24.5 inside the roller end | None | Fits. Earlier trial gave 10 failing features, against 8 at offset 0 |
| 75 | **0 (model now)** | 37.5 | **0.5 past the roller end** | None | **Front 2 bolts on each side have no thread** |
| 150 | 0 | 0 | Off the roller | None | **No seat at all** |
| 150 | 50 | 50 | 12 inside the roller end | 50 | Fits on paper. Reverses D-176. Beam rear about 3.5 past the tub end at the back of travel. Top roller 150 and bottom angle 175 by formula |

The nut plate at the roller end has no holes for the front row, so it does not rescue the current position.

The lower brace bolts into the beam are at Z 223, 18 above the beam's underside. The flat of the face starts 16 up with a 16 corner radius, so they clear it by 2 to the hole centre. With a 24 radius they land on the corner. Check the real tube radius before drilling.

Checked read-only, at one gantry position, with bounding boxes. No parameter was changed for this table and no rebuild was run.

## Not checked

- Whether 150 × 75 × 8 tube can be bought. It is not in `docs/steel-rhs-suppliers.md`.
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
4. **X screw supports:** the 60 wide risers overhang the 43 flat on the beam's top face by 8.5 each side. They need narrowing, or a seat that bridges the corners.
5. **Y roller brace seat:** choose the beam width and `XGantryOffset` from the table above.

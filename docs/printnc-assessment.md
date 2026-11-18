# PrintNC V4 gantry on Type 0 (18 Nov 2026)

**Status: the parametric model is set to the Type 0 sizes, with 8 features still failing. The Fusion document is NOT saved.** Decisions: D-172 to D-175.

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
| `XGantryWidth` | 75 | **150** | D-164 beam |
| `XGantryHeight` | 75 | **150** | D-164 beam |
| `XGantryThick` | 4 | **8** | D-164 beam |
| `XGantryRadius` | 10 | **16** | Trial value. The real tube corner is not verified |
| `XGantryOffset` | 25 | **0** | With 25 the 150 beam gave 141 problems. With 0 it gives 8 |

## Result after the rebuild

| Item | Value |
|---|---|
| X rails, Y rails | 600, **550** |
| Gantry length | 775 |
| Y rail spacing | **700**, tub widened to suit (D-173) |
| X rails | Top and bottom of the beam, seats 150 apart |
| Top roller, bottom roller | 150 wide, 175 wide by formula |
| X screw, Y screw | 700, **650** |
| Y screw position | **Directly above the Y rail**, X ± 350 (D-174) |
| Length of the Y rail and its supports in line | **684** in the 690 tub, 3 clear at each end |
| Y block travel on the 550 rail | About 379 with the model's blocks. Type 0 needs 350 |

## Still failing (8 features)

| Timeline | Feature | Part | Note |
|---|---|---|---|
| 494 | Extrude8 | XRollers | No target body |
| 543 | Rigid 164 | M6 × 12 bolt to XRollerShim | Missing joint origin |
| 1015 | Rigid 110 | XGantry Trigger Mount to XGantry | Joint failed |
| 613, 614, 616, 617, 618 | Extrude2, Chamfer1, Chamfer2, Fillet1, Extrude4 | YRoller-Gantry Drill Guide | **Caused by the first 150 beam trial.** They stayed when the beam went back to 75, and a full recompute did not clear them |

## Not checked

- Whether `XGantryOffset` 0 leaves room for the gantry brace and its bolts.
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

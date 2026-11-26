# V5 Fusion model `Type_0_v5` (plan Tasks 4 to 6)

`Type_0_v5` is a saved, unmodified copy of the parametric PrintNC V4 Metalcutter model (1182 timeline items, 94 user parameters). Changes are made through the Fusion MCP. **Claude does not save the document: the owner saves.**

## Origin
PrintNC's model origin is at the front X frame tube: bottom face, X centre, front face (X frame tubes Z 0 to 80 after Task 4). Moving the origin would touch 1182 features, so the model keeps PrintNC's origin and **V5's world origin (bed top centre) is recorded here as an offset** once the bed is in (D-364). Until then all positions below are in PrintNC model coordinates (mm): X across the machine, Y front to back, Z up.

## Baseline (26 Nov 2026, before any change)
Timeline 1182 items, **no errors and no warnings**. 17 items are not "healthy" only because they are suppressed (6: Z plate and Y brace oval holes and fillets, milled-part threads), rolled back inside their component (5: `Cutting Area` Extrude2, `YFrame` Fillet1 and R-Pattern5, `YRoller` Extrude5, `Printed Drill Guides` Extrude1) or timeline groups (6, no health state). The Task 4 check counts only warnings and errors.

## Parameters changed (Task 4, 26 Nov 2026)
| Parameter | PrintNC | V5 | Why |
|---|---|---|---|
| `FrameLong`, `FrameShort` | 75, 50 | 80, 80 | SHS 80 x 80 x 6 frame (D-354) |
| `FrameThick` | 3 | 6 | D-354 |
| `FrameRadius` | 6 | 12 | EN 10219-2 nominal 2.0T for 6 wall (`tools/v5_beam.py`); measure the delivered tube |
| `XFrameCount` | `max(3; ...)` = 3 | 2 | D-354, D-361 (X tubes full width under the Y tubes) |
| `YRollerWidth` | `max(FrameLong; XFrameWidth)` | 80 | RHS 80 x 40 (D-362); pinned so a frame change does not resize it |
| `YRollerHeight` | `FrameShort` | 40 | D-362 |
| `YRollerRadius` | `FrameRadius` | 6 | Pinned (was tied to the frame radius) |
| `YRollerThick` | 3 | 3 | Unchanged; 4 wall also allowed (D-362) |
| `XTopRollerHeight`, `XTopRollerWidth`, `XTopRollerRadius` | `FrameShort`, `max(FrameLong; XGantryWidth)`, `FrameRadius` | 50, `max(75; XGantryWidth)`, 6 | Pinned at PrintNC's values; the X rollers are dropped in V5 (D-358) and hidden in Task 5 |
| `XCuttingArea`, `YCuttingArea` | 625, 625 | 485, 485 | Gives the 650 rails of `tools/v5_sizes.py` (PrintNC: rail = 25 x ceil((area + 165) / 25)). PrintNC's "cutting area" is not V5's travel (X 433, Y 450) |
| `YCarriageB`, `YCarriageC`, `XCarriageB`, `XCarriageC` | 53, 40 | 32, 36 | HGH20CA hole pattern for the drill guides (PrintNC's own note) |

**Lengths the model now gives:** X and Y rails 650, X and Y screws 750 (all as `v5_sizes`). **X frame tubes and beam 835** (`v5_sizes` beam_len 830.7, D-353 priced 830.7). **Y frame tubes 800** (`v5_sizes` frame_y 781.7, D-354 priced 781.7). PrintNC's formulas are kept; the BOM takes the model's lengths (Task 8).

**After the change:** 4 new warnings, all in the hidden SFU2010 option plates (`Y 2010 Nut Plate` Fillet1, Chamfer1, Chamfer2; `Y 2010 Fill Plate` Chamfer1: lost edge references, cached geometry). These parts are dropped in V5 (`docs/v5-parts.md`).

## Task 4 check, first run (26 Nov 2026, `tools/fusion/v5_check_task4.py`, read-only)
Run after the parameters above, before any part swap. The script text is in the repo; paste it into `fusion_mcp_execute` with `readOnly: true`.

- **Timeline:** 4 warnings, the hidden SFU2010 plates above. No errors.
- **Overlaps:** 138 visible solid bodies (fasteners, drill guides, printed chain/sensor/trigger parts and endcaps left out); 54 pairs over 1 mm³. None is a V5 frame fault:
  - **Dropped PrintNC Z** (`Zaxis Dual Carriage HGH15CA`, `ZAxis Hardware`): the plywood Z plate now cuts the front X tube (57,967 mm³; the tubes are 80 tall, not 50), plus clamp and HGR15 self-overlaps. To be hidden in Task 5 when the Type 0 Z goes in.
  - **Screws in holes:** each 1610 screw in its SFU nut, nut plate and fill plate; Z 1204 screw in its HM10.
  - **Self-overlaps inside PrintNC's vendor models** (`HM12-57`, couplers, `HGR20` against `HGW20CC`; 7 rail/block pairs fail the boolean with bad vendor geometry, ASM_INCONS_VERT_ATT). All go when the HGH20CA, HM12-60-V, DFU1605 and coupler models replace them.
  - **New with the RHS 80 x 40 roller (D-362):** the Y and Y2 fill plates (80 x 40 x 15, PrintNC parameters do not size them) cut the roller wall (747 mm³ each) and the SFU nut cuts the roller (487 mm³ each). The plates are re-made as aluminium flat bar (D-356) and the nut becomes the DFU1605: size both inside the 74 x 34 roller bore when they are swapped.
- **Y limits:** carriage 175 long (SFU nut front Y 539 to fill plate back Y 714, as `v5_sizes`), free between the BKHM12 riser face (Y 62.5) and the BF12 riser face (Y 714.5): **Y travel 477** (450 needed). (The first run's script printed a wrong carriage line, -68.5: the nut plate component holds two small bodies at Y -6.5. Fixed 26 Nov 2026: only bodies over the roller in X count; it now prints 539 to 714, 175 long, travel 477.)
- **Grease fittings at Y max:** the PrintNC block's fitting reaches Y 716.8, 2.8 past the fill plate and 2.3 past the BF12 riser face: **it hits the riser at the hard end of travel.** Travel to a soft limit 3 short still leaves 474. Re-check with the HGH20CA block's fitting.
- **Gantry at Y min:** the beam (Y 611 to 777, Z 194 up, at the stock section) moves 476.5 forward to Y 134.5: 85 clear of the HM12 (Y max 49.3) and 114 above the front X tube (Z 80). **Not checked yet:** the spindle reaching the bed's front and rear edges. There is no spindle (Task 5) and no bed (D-364); the beam section and the front-face carriage are Task 5.

## Y1 hardware swap, part 1 (26 Nov 2026, 47th session; Fusion **not saved**, owner saved version 2 before it)
Script `tools/fusion/v5_y1_place.py` (not read-only; re-runnable; `SEAT` = 0 until item 3). Owner's answers: D-365 to D-368.
- **Imported** into new component `Y1 screw and motor` (identity, then moved): `DFU1605 Nut`, `BF12`, `HM12-60`, `24HS40 Motor`; `HGH20CA Block` moved into new component `Y rails and seats` and copied (2 blocks). Vendor frames:
  - DFU1605: axis local X, flange outer face x -15, nut to x -115 (100 long), flange Ø48 x 10 at x -25 to -15, 6 x Ø5.5 on PCD 38; Body3 = 130 screw piece (hidden). **Flats 40 cut** (`DFU flats 40`, local |y| > 20, Body6 only).
  - BF12: bore axis local Z at local y 3.5, base local y -21.5 (centre height 25).
  - HM12-60: axis local Z, body Z 0 to 90, base local y -30 (axis 30 above the base). **Which end takes the motor is not checked yet** (bearings in sub-occurrence frames).
  - 24HS40: shaft Ø10 axis local -Z, at local (0, 0), shaft tip near Z 21 (from the Ø10 face list): **confirm the flange face Z** before placing.
  - HGH20CA: rail stub along local Z (Body2, hidden), up = local Y, rail bottom local y -17.5, block top 12.5 (H 30).
- **Placed (PrintNC mm):** 2 x HGH20CA at X -377.5, Y centres 589 and 674 (PrintNC's HGW20CC centres), Z 164.6 to 190 (on the kept HGR20 rail, bottom Z 160): **OK.** BF12 at Y 738.25, base Z 185, axis Z 210: **OK.**
- **DFU1605 placed (48th session, after the owner saved version 3):** the occurrence transform never holds for this part (set + snapshot reads back at the origin, also with the timeline rolled back before the flats cut; BF12 and the blocks hold). So the occurrence stays at identity and a Move feature **`DFU place`** in the DFU component (after `DFU flats 40`) moves all its bodies: axis X -377.5, Z 210, flange outer face Y 539, nut back Y 639, flats top and bottom (flange Z 190 to 230, Ø48 across X). Body Ø28 at Z 196 to 224: 3 clear inside the 34 roller bore. **Overlap check:** roller tubing, brace, gantry, HGH20CA blocks and drill guides 0; it hits PrintNC's old 1610 screw (6,582 mm³, goes with the screw swap), the `Y 1610 Nut Plate` (2,843 mm³, re-made as flat bar, item 4) and its M5 tie rods, M5 nuts and two M6 x 12 (`1610 Ballscrew Fasteners`, `YRollerFasteners`: go or change with the nut plate).
- **HM12-60 and 24HS40 placed (48th session):** HM12-60 screw end (bearings local z 0 to 25, lock nut 25 to 33) is local z 0, **motor end local z 90** (Ø50 pilot recess 5 deep, Ø36 coupling bore z 25 to 85, 4 x M5 tapped on a 49.4 square). Placed with the screw-end face at PrintNC's HM12-57 screw-end face, **Y 43**, motor face Y -47, axis Z 210, base Z 180 (riser 20, D-367). 24HS40: flange face local z 0, Ø38.1 pilot 1.1 proud, shaft Ø10 to z +20, **holes Ø5 on a 50 square**; placed flange on the HM12 motor face (Y -47), body to Y -172, cable lead outboard (-X, to X -511). **Check with LiMo: the HM12-60 STEP's holes are on 49.4, the motor's on 50** (0.3 mm off per side: one of the two vendor models is wrong, or the motor needs a different mount). Both transforms hold. **Overlap check:** all hits are PrintNC parts being replaced: HM12-57 and NEMA23 (now hidden), the D30L40 coupler, the old 1610 screw, the 30-tall `Y BKHM12 Riser` (10,494 mm³: riser is 20 now, D-367) and its M6 x 30, M6 x 50 and M4 x 16 screws.
- **Hidden (not deleted):** PrintNC `Y HGW20CC` (with its grease fittings), `Y SFU1610 Nut`, its `M6-1.0 90 Grease Fitting`, `Y BF12`, `Y HM12-57`, `Y NEMA23 Stepper`. Still visible: PrintNC `Y D30L40 8-10mm Coupler`, `Y 1610 Ballscrew` (Z 215), the 30-tall risers and their screws.
- **Overlap check of the new parts (read-only):** BF12 housing cuts the 30-tall `Y BF12 Riser` (5,098 mm³: the riser is 25 tall now, D-367) and an M6 x 30; BF12 bearing against the old screw at Z 215 (goes with the screw swap); HGH20CA against PrintNC's `Y HGR20 Rail` (709 and 725 mm³: rail model profile against the vendor block's groove, check by section) and PrintNC's M6 x 12 block screws (hide with the HGW20CC fasteners); block 2 against the printed drill guide (skipped as printed).
- **Grease nipple:** the HGH20CA STEP has none. PrintNC's HGW20CC fitting reached 2.3 past the BF12 riser face at Y max (first run): keep the 3 mm soft limit until the bought block's nipple is measured.

## Left for Task 4
1. ~~Owner saves `Type_0_v5`~~ (version 2, 26 Nov 2026). The Y1 swap part 1 above is not saved.
2. Swap the Y hardware for the real models in `cad/vendor/`: `hgh20ca_block.step` (Y, Y2), `dfu1605_nut.step`, `bf12.step`, `24hs40_motor.step`; HM12-60-V (only a drawing, `cad/vendor/drawings/hm12_60_v_motor_mount.png`: model it from the drawing, or the owner fetches a STEP); D25L35 coupling (no STEP in the repo: ask).
3. Y rail seats 3 mm (D-363): the Y rails, blocks, rollers and risers go up 3; the risers' nominal heights (D-357) follow.
4. Nut and fill plates as flat bar inside the 80 x 40 roller (D-356, D-362).
5. The bed, once the owner has chosen it and put its STEP in `cad/vendor/` (D-364); then the origin offset and the spindle reach at Y min and Y max.
6. ~~Fix the carriage line in the check script~~ (done 26 Nov 2026); re-run the full check after the swap.

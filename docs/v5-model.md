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
- **Y limits:** carriage 175 long (SFU nut front Y 539 to fill plate back Y 714, as `v5_sizes`), free between the BKHM12 riser face (Y 62.5) and the BF12 riser face (Y 714.5): **Y travel 477** (450 needed). (The script's own "carriage" line takes the nut plate component's box, which holds bodies down to Y -6.5, and so prints -68.5: read the 175 carriage, not that line. Fix the script before the next run.)
- **Grease fittings at Y max:** the PrintNC block's fitting reaches Y 716.8, 2.8 past the fill plate and 2.3 past the BF12 riser face: **it hits the riser at the hard end of travel.** Travel to a soft limit 3 short still leaves 474. Re-check with the HGH20CA block's fitting.
- **Gantry at Y min:** the beam (Y 611 to 777, Z 194 up, at the stock section) moves 476.5 forward to Y 134.5: 85 clear of the HM12 (Y max 49.3) and 114 above the front X tube (Z 80). **Not checked yet:** the spindle reaching the bed's front and rear edges. There is no spindle (Task 5) and no bed (D-364); the beam section and the front-face carriage are Task 5.

## Left for Task 4
1. Owner saves `Type_0_v5` (parameters above).
2. Swap the Y hardware for the real models in `cad/vendor/`: `hgh20ca_block.step` (Y, Y2), `dfu1605_nut.step`, `bf12.step`, `24hs40_motor.step`; HM12-60-V (only a drawing, `cad/vendor/drawings/hm12_60_v_motor_mount.png`: model it from the drawing, or the owner fetches a STEP); D25L35 coupling (no STEP in the repo: ask).
3. Y rail seats 3 mm (D-363): the Y rails, blocks, rollers and risers go up 3; the risers' nominal heights (D-357) follow.
4. Nut and fill plates as flat bar inside the 80 x 40 roller (D-356, D-362).
5. The bed, once the owner has chosen it and put its STEP in `cad/vendor/` (D-364); then the origin offset and the spindle reach at Y min and Y max.
6. Fix the carriage line in the check script; re-run it.

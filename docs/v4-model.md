# V4 Fusion model: base, Y axis, table (Task 4, 24 Nov 2026)

Claude built this model with the Fusion MCP, in a **new, unsaved Fusion design** (Fusion named it `Untitled`). **The owner saves it as `Type_0_v4`.** `Type_0_v3` was not changed.

Uprights, beam and the X and Z axes were added in Task 5 (section at the end). The end plates' outer faces (X ±270) are the upright bolting faces.

## Origin and axes
- **World origin: the top face of the table plate M11 (the work surface), at its centre, with the table at Y mid travel (`y_pos` = 0).** M11 bolts straight to the 4 blocks; there is no carrier plate (owner, 24 Nov 2026: "Drop the carrier").
- X is across the machine (wheel side +X). Y is the table's travel (motor at the rear, +Y). Z is up.
- Everything below the table is placed down from Z 0 by parameters:

| Item | Z (mm) |
|---|---|
| Table plate M11 top | 0 |
| Table plate bottom = block tops | -25 |
| Y screw axis | -50 |
| Rail bottoms = ground bar tops | -55 |
| Tray top (profile tops) | -75 |
| Tray bottom | -165 |
| Bottom sheet bottom | -168 |

- **Moving the table:** set the user parameter `y_pos` between `-y_travel / 2` and `+y_travel / 2` (±150). These all follow it:
  - the table plate and its two drip skirts;
  - the 4 blocks;
  - the nut, its housing and spacer;
  - the lengths of both bellows.

## Components and bodies
| Component | Bodies |
|---|---|
| `Base (extrusion + EG)` | `Profile 90x90 Y-290`, `Y-45`, `Y+45`, `Y+290` (500 along X); `End plate X- 670x90x20`, `End plate X+ 670x90x20`; `EG pocket Y- 155x90x500`, `EG pocket Y+ 155x90x500`; `Bottom sheet` |
| `Y rails and plates` | `Rail seat bar X- 50x20 (ground)` (670 long, full tray Y), `Rail seat bar X+ 50x20 (ground)`; `HGR20 rail X- (vendor section)`, `HGR20 rail X+ (vendor section)`; `HGH20CA block X-/X+ Y-/Y+ (vendor)` (4) |
| `Y screw and motor` | `Y screw DFU1605 600 (envelope, stepped ends)`; `BF12 floating support (vendor)`; `BK12 fixed support (vendor)`; `DFU1605 nut (vendor, flange flats 40 AF added)`; `Nut housing DSG16H (envelope)`; `Nut housing spacer 5`; `Screw bellows front (envelope)`, `Screw bellows rear (envelope)`; `Coupling D25L35 (envelope)`; `Coupling guard (printed envelope)`; `Y motor plate 10 (envelope)`; `Y motor 24HS40 NEMA 24 (vendor, cables cut off)` |
| `Table` | `Table plate 460x330x25 (M11)`; `Drip skirt X- (bent 2 mm sheet, envelope)`, `Drip skirt X+ (bent 2 mm sheet, envelope)` |

Fasteners, T-nuts, dowels, rail holes and tapped holes are not modelled.

## User parameters (mm)
- **Driving values:**
  - `y_travel` 300, `y_pos` 0, `y_rail` 500, `y_screw` 600, `base_len` 670 (all from `tools/v4_sizes.py`);
  - `tray_x` 500, `prof` 90, `prof_y_out` 290, `prof_y_in` 45, `endplate_t` 20 (D-308);
  - `sheet_t` 3;
  - `table_x` 460, `table_y` 330, `table_t` 25 (M11; the carrier plate and `fixture_t` are gone);
  - `rail_x` 205, `bar_w` 50, `bar_t` 20, `bar_len` = `base_len` (670);
  - `block_h` 30, `block_pitch` 100, `nut_spacer_t` 5.
- **Derived:**
  - `z_tbl_bot` = -table_t;
  - `z_rail_bot` = z_tbl_bot - block_h;
  - `z_tray_top` = z_rail_bot - bar_t;
  - `z_tray_bot` = z_tray_top - prof;
  - `screw_z` = z_tbl_bot - nut_spacer_t - 20;
  - `bk_y` = base_len / 2 - 52 (BK12 centre 283);
  - `screw_end` = bk_y + 39 (322);
  - `screw_start` = screw_end - y_screw (-278);
  - `bf_y` = screw_start + 10 (BF12 centre -268);
  - `pocket_w` = prof_y_out - prof_y_in - prof (155).
- The box and cylinder sketches are fully constrained and dimensioned by these expressions. A test changed `tray_x` and the profile grew symmetrically.
- The vendor bodies are placed by Move features whose X, Y, Z are expressions.
- The Y-end layout (BK12, coupling, motor) is fixed relative to `base_len`. The BK12 and BF12 bases sit on the tray top only while `screw_z` - 25 = `z_tray_top`, which holds for the values above. If the stack changes, add a riser.

## Vendor models and envelopes
| Part | Source |
|---|---|
| HGH20CA blocks | **Vendor** `cad/vendor/hgh20ca_block.step` (HIWIN, TraceParts), block body only |
| HGR20 rails | **Vendor section**: a hole-free 10 mm slice of the vendor rail stub, extruded to `y_rail`. No bolt holes |
| BK12, BF12 | **Vendor** `bk12.step`, `bf12.step` (Engder), each part unioned into one body |
| DFU1605 nut | **Vendor** `dfu1605_nut.step`, without its screw piece. The vendor flange is round Ø48; flats 40 AF (top and bottom) are cut in the model, as v3 (D-217) |
| Y motor 24HS40-5004D-E1000 | **Vendor** `24hs40_motor.step`, trimmed to a 62 x 62 box, so the cable stubs are cut off |
| Y screw | Envelope: Ø16 thread; Ø10 BF12 journal; Ø12 BK12 bearing seat; Ø10 through the lock nut and drive stub |
| Nut housing | Envelope: DSG16H, 52 x 40 x 40, centre 20 below the face, Ø28 bore |
| Coupling D25L35 | Envelope: Ø25 x 35, Ø10 bore |
| Profiles | **Rectangular envelope 90 x 90** of the KJN 90 x 90 H section (the T-slots are not modelled) |
| End plates, ground bars, table plate, bottom sheet, EG pockets | Plain boxes at their real sizes |
| Bellows, coupling guard, motor plate, drip skirts | Envelopes (Claude's design, not bought parts yet) |

## Claude's calls (owner to correct)
1. **Y motor at the rear (+Y), in line, outside the table's travel.**
   - The motor plate (10 thick, envelope) bolts to the rear profile's outer face at Y 335. The motor face is at Y 345 and the motor ends at Y 470, so it overhangs the tray by 135.
   - The table's rear edge reaches Y 315 at the +150 limit (nearest motor point 22.9 away, motor plate 20).
2. **The screw is covered by two bellows** (envelopes 60 x 40, Ø20 bore, between the rails, BOM F31). They run from the BF12 to the nut and from the nut to the BK12, and their lengths follow `y_pos`.
   - At the limits the rear bellows closes to 50 (350 open) and the front to 78 (378 open), about 14 % and 21 %.
   - **Required: closed length at most 1/7 of open length (rear).** The supplier must confirm this before ordering. If it cannot be met: a telescopic cover, or a 650 screw (recheck `base_len`, the BK12 position and the motor overhang).
3. **A printed coupling guard** covers the BK12 lock nut and the coupling, from the BK12 housing (Y 295.5) to the motor plate (Y 335). Its top is at the BK12 top + 4 (Z -28), 3 below the table bottom.
4. **Table: M11 (460 x 330 x 25) bolts straight to the 4 blocks** (owner, 24 Nov 2026: "Drop the carrier"). The nut housing hangs from M11's underside.
5. **Nut housing:** a DSG16H on a 5 mm spacer under M11, so the screw axis is 25 below the table bottom (Z -50).
   - The nut flange is modelled with flats 40 AF top and bottom, as v3 (D-217). It clears the table by 5 and the tray top by 5, so the screw is not raised and needs no spacer blocks under the BK12 and BF12.
   - **Check that the LiMo flange has the flats.** With a round Ø48 flange the clearances would be 1 each.
6. Blocks at 100 pitch (D-150), centred under the table. At the ±150 limits the block ends are at ±238.75, inside the rail ends (±250).
7. **Rail seat bars 670 long (full tray Y), rails 500.** Each Y bar is bolted into all 4 profiles (proposed: 2 M8 T-nut screws per profile, 16 in all, X23); the rail sits on the middle 500.
8. **The Y rails are guarded from drips** (BOM F32):
   - **Drip skirts on the table's X edges:** a bent 2 mm sheet L (or printed), envelope. The 6 x 330 flange sits under the table at X ±228 to 234 and the leg hangs down at X ±232 to 234. The leg ends 3 above the tray top and 2 outside the bar's outer face. Drips off the table's long edges land outside the rail bars.
   - **The front and rear ends stay open** (the table overhangs the rail ends). Rail wipers there: the HGH20CA blocks' own end seals, plus a printed wiper on each block end (8). **Not modelled.**
   - The owner may prefer telescopic rail covers or a chip tray instead.

## Findings for later tasks (not changed here)
- **The tray is 540 wide, not 500.**
  - With the 20 end plates, the upright faces are at X ±270.
  - `v4_sizes.py` takes `base_width` 660 = 460 + 2 x (20 + 80), with the uprights starting at ±250.
  - U2 flat bars (50) on the end plates would span X ±270 to ±320 (640 overall).
  - **Task 5 should reconcile this** with `base_width` and the beam overhang. **Done in Task 5:** `base_width` 640.
- **X20's rail-hole note does not fit.** "Holes at 60 pitch, 20 from the ends" does not work on a 500 rail: 8 holes leave 40 at each end, or the end distance must change. Check the LiMo drawing.
- **No bolt holes in the rail model.** The vendor stub's holes are at 60 pitch, but the rail is a hole-free extrusion.

## Check results (read-only script; fix round 1, 24 Nov 2026)
The check script:
- asserts the design is this one (an attribute `type0/model` on the design);
- lists the open documents and the timeline health;
- tests every pair of bodies whose boxes overlap (shrunk 0.01 mm), with a temporary-BRep intersection, and reports volumes over 0.01 mm³;
- casts vertical rays every 2 mm along the screw axis, to check that a body covers the screw from above;
- measures minimum distances.

It was run at `y_pos` 0, -150 and +150. A separate, modifying script set `y_pos` between the runs and set it back to 0 afterwards.

| y_pos | Timeline (141 items) | Bodies | Overlaps | Screw cover (301 rays) | Bellows front / rear | Table Y |
|---|---|---|---|---|---|---|
| 0 | all healthy | 32, all solid | 1 (below) | **all covered** | 228 / 200 | -165 to 165 |
| -150 | all healthy | 32, all solid | 1 (below) | **all covered** | 78 / 350 | -315 to 15 |
| +150 | all healthy | 32, all solid | 1 (below) | **all covered** | 378 / 50 | -15 to 315 |

Minimum distances (mm):

| y_pos | Motor to table | Motor plate to table | Nut to table | Nut to tray | Guard to table | Skirt to bar | Skirt to tray |
|---|---|---|---|---|---|---|---|
| 0 | 160.4 | 170 | 5 | 5 | 130.5 | 2 | 3 |
| -150 | 309.7 | 320 | 5 | 5 | 280.5 | 2 | 3 |
| +150 | 22.9 | 20 | 5 | 5 | 3 | 2 | 3 |

- **The only overlap is screw vs BF12 (vendor), 5.4 mm³.** It is the BF12's retaining ring (bore Ø9.4) sitting on the Ø10 journal: a screw in its hole, because the groove is not modelled. Nothing else overlaps at any position.
- **The screw is covered at every position.** Over the screw, the first body above is the BF12, the front bellows, the nut, the rear bellows, the BK12, the coupling guard or the coupling. No part of it is open to drips from above.
- Open documents during the checks: `Type_0_v3` (not modified) and `Untitled` (this model). No other documents were left open: the STEP imports were done in scratch documents, which were closed without saving.
- **Screenshot (fix round 1, iso, `y_pos` 0):** the tray carries the single 25 mm table plate on the two rails, which now sit on full-length bars. The drip skirts hang at the table's long edges, the rear motor stands past the tray's +Y end, and the BF12 and front bellows show under the table's front edge.

# Task 5: uprights, beam, X axis, Z axis and spindle (24 Nov 2026)

Same unsaved design (`Untitled`; the owner saves it as `Type_0_v4`). `Type_0_v3` was only read.

## Components and bodies
| Component | Bodies |
|---|---|
| `Uprights` | `Upright X-` and `Upright X+ U2 flat bar 50x150x325 (steel)` (X ±270 to ±320, Y 185 to 335, Z -165 to 160), each with 4 counterbores Ø20 x 18; 8 `Upright bolt M12x50`; 4 `Dowel 10x30` |
| `Beam` | `Beam SHS 120x120x8 (steel, R16 outside / R8 inside)` (X -350 to 540, Y 190 to 310, Z 160 to 280); `Beam EG core (fill, D-310)` (9.57 L, cut round the bolt heads); 4 `Beam bolt M12x35` |
| `X axis` | `X rail seat bar upper` and `lower 50x20 (ground, D-311)` (full beam length, on the front face); `HGR20 rail X upper` and `lower (vendor section)` (850, X -330 to 520); 4 `HGH20CA block X ... (vendor)`; `X DFU1605 nut (vendor, flange flats 40 AF, D-217)`; `X nut housing DSG16H (envelope)`; `X nut housing spacer 5`; `X nut bracket 150x145x20 6082 (envelope)`; `X screw DFU1605 900 (envelope, stepped ends)`; `X BK12 fixed support (vendor)`; `X BF12 floating support (vendor)`; `X coupling D25L35 (envelope)`; `X coupling guard (printed envelope)`; `X motor 24HS40 NEMA 24 (vendor, cables cut off)`; `X motor bracket 10 (envelope)`; 2 hidden rail section faces (construction) |
| `Z axis and spindle` | Copied from `Type_0_v3`. Fixed (9): `Z fixed plate 150x442x20 6082`, 2 Z risers, 2 `Z rail HGR20 350`, `Z screw DFU1605 350`, `Z HM12-60-V mount with 2 x 7901C and nut`, `Z coupling D25L35`, `Z motor 24HS34 ... brake`. Moving (34): `Z Moving Plate 150x200x20`, `Z Nut Housing DSG16H`, 4 `Z block HGH20CA`, `Z DFU1605 nut`, the PrintNC 80 clamp with its tram blocks and 22 screws, washers and grubs, `Spindle Jianken JGL-80-2.2R24 (vendor STEP)` and `Spindle nose ISO20 stub` |

## User parameters added (mm)
- `x_travel` 620, `x_min` -215, `x_max` = x_min + x_travel (405), **`x_pos` 0** (spindle axis X, x_min to x_max), `z_travel` 150, **`z_pos` 0** (-75 to +75; nose = 100 + z_pos above the table).
- `x_rail` 850, `x_screw` 900, `beam_len` 890, `beam_x0` -350, `x_rail_x0` = beam_x0 + 20 (from `tools/v4_sizes.py`).
- `beam_sq` 120, `beam_wall` 8, `upr_t` 50, `upr_w` 150, `upr_h` 325, `z_beam_bot` = z_tray_bot + upr_h (160), `z_beam_top` = z_beam_bot + beam_sq, `xbar_t` 20.
- Driven by parameters: the upright height and base (`upr_h`, `z_tray_bot`); the beam, core and bar lengths and start (`beam_len`, `beam_x0`); the rail length (`x_rail`). Three Move features: `X carriage at x_pos` (blocks, nut, housing, spacer, bracket), `Z axis at x_pos` (all Z bodies), `Z moving at z_pos`. The cross-sections, the rail start, the screw and its supports are fixed geometry.

## How the v3 Z axis was copied
- A script read the visible bodies of `Type_0_v3`'s `Z Fixed Plate:1` and `Z Axis Assembly:1` (`Z Fixed Parts`, `Z Moving Parts`), copied them with `TemporaryBRepManager`, translated them by (+222.5, -297, -70) and added them in two base features. Hidden v3 stand-ins (old rails, motor, clamp) were skipped.
- v3's `Z Travel Slider` was at 0 (limits ±75), so the copy is at mid travel: spindle axis X 0, Y 0, nose Z 100 (v3: nose Z 170, table Z 70).
- Each vendor sub-assembly became one body: Z motor, HM12 mount with its bearings and nut, each Z block, the Z nut, the spindle (nose stub kept separate). v3's separate Z fasteners (`ZAxis Fasteners`, `Joint screws added`) were not copied; the clamp screws inside `Z Moving Parts` were.
- Copied from the V4 Y axis by the same method: the X blocks, BK12, BF12, nut, housing, spacer, coupling, guard and 24HS40 motor. The X rails are a slice of the V4 Y rail, extruded to `x_rail`. The X screw is two copies of the Y screw envelope joined in the thread at X 100.

## Claude's calls (owner to correct)
1. **Both X rails on the beam's front face.**
   - The bars sit flush with the beam's top and bottom edges. The rail centres are at Z 185 and 255, **only 70 apart (v3: 137)**.
   - The bottom face cannot take a rail: at the +X limit the carriage straddles the right upright. The top face carries the X screw.
   - **The SHS corner radius:** EN 10219 gives 2t to 3t outside (16 to 24) at t 8, so the flat is 72 to 88. Modelled at R16: each 50 bar has 34 of its width on the flat and 16 over the radius. Fix options: a relief or shim under the bar, or narrower bars.
   - BOM M02 and G01 still say "top and bottom faces" (Task 7).
2. **The v3 Z fixed plate bolts straight onto the 4 X blocks** (block tops at Y 140 = the plate's back face). The blocks (±88.75 at 100 pitch) stand 13.75 past the 150 plate at each side; their bolt holes (±68) are on the plate.
3. **X screw on the beam top, on the centreline** (Y 250, Z 305 = beam top + 25), the same stack as the Y axis:
   - BK12 at X -321 and BF12 at X 530 (outer face flush with the beam end, 540), both on the beam's top face (hot-rolled: shim or pad).
   - The nut hangs from a 150 x 145 x 20 6082 bracket bolted to the Z fixed plate's back face, on a DSG16H and a 5 spacer. The nut flange (flats 40 AF) clears the beam top by 5 and the bracket by 5.
   - **The motor is in line at -X, beyond the beam end** (X -508 to -362), on a 10 mm bracket envelope. Its end plate bolts to the beam end and is also the EG dam. *(Superseded by D-320: the bracket goes; a second HM12-60 on the X- pad carries the motor; plain caps close the beam ends.)* The coupling guard is copied from Y.
   - The screw is not covered (no bellows); chips can land on it.
4. **The uprights stand at Y 185 to 335**, flush with the tray's rear end and 5 behind the beam's front face, so the lower bar overhangs them.
   - The beam sits on their top edges at Z 160. The upright is 325 from the tray bottom (-165), so G07's 2 x 325 is unchanged.
   - The beam's Y place follows from the spindle at Y 0 and the v3 stack: plate back at Y 140, plus the block (30) and the bar (20), puts the beam's front face at Y 190.
   - Under the beam there is 160 to the table top.
5. **The upright-to-end-plate joint is only 150 x 90** (the end plate's height), not 150 x 325 as G08 assumes.
   - 4 M12 at Y 210 and 310, Z -140 and -100, counterbored Ø20 x 18.
   - **M12 x 50, not x 60.** With the 18 counterbore, x 60 would put the tip 8 past the end plate, into the profile end or the EG. x 50 stops 2 short, with 18 of thread in the 20 plate.
   - Dowels Ø10 x 30 at Y 260, Z -145 and -95 (on the vertical centreline, 50 apart, 15 in each part).
6. **Beam bolts: 2 per upright, M12 x 35, heads inside the tube** on the bottom wall (X ±295, Y 220 and 280), fitted before the EG fill and cast in (D-310). They screw into tapped M12 in the upright's top edge. Nothing stands on the beam top at the uprights.

## Check results (24 Nov 2026)
Read-only check script at x_pos, z_pos, y_pos = 0: **168 timeline items, all healthy**; 114 solid visible bodies; 62 overlaps, all of these kinds:
- **Screws and pins in holes that are not modelled (32):** 8 upright bolts in the upright and end plate; 4 dowels in the upright and end plate; 4 beam bolts in the tube wall and upright.
- **BF12 ring on the journal (2):** X and Y, 5.4 mm³ each (known, Task 4).
- **Inside the copied v3 Z, as in v3 (28):** clamp screws, washers and grubs in the clamp (15); tram block screws (2); clamp and tram screws in the moving plate (9); Z screw in the HM12 mount bearings and nut (131 mm³); Z motor against coupling (0.04 mm³).

A second script set x_pos, z_pos and y_pos to the limits, checked every pair that includes a moving body (X carriage, Z, table, Y blocks), measured gaps, and then set all three back to 0.

| Pose (x_pos, z_pos, y_pos) | Nose above table | Moving overlaps | Carriage to upright | To upright bolt heads | To beam bolts | Bracket to BK12 / BF12 | Nut to BK12 / BF12 |
|---|---|---|---|---|---|---|---|
| -215, -75, -150 | 25.0 | 0 | 20.1 (left) | 202.3 | 45.6 | 20.0 / - | 63.0 / 665 |
| -215, +75, +150 | 175.0 | 0 | 20.1 (left) | 202.3 | 45.6 | 20.0 / - | 63.0 / 665 |
| 405, -75, +150 | 25.0 | 0 | **20.1 (right)** | 202.6 | 49.6 | - / 40.7 | 683 / 45.0 |
| 405, +75, -150 | 175.0 | 0 | **20.1 (right)** | 202.6 | 49.6 | - / 40.7 | 683 / 45.0 |

- **Nose 25 and 175 above the table top at the Z limits** (D-267).
- **Upright clearance:** the nearest part is the lower X block. It passes 3 above the upright's top edge and 19.6 in front of it, a gap of 20.1. The upright bolt heads are recessed on the outer face, about 200 from anything on the carriage. The beam bolt heads are inside the tube.
- **Table corners:** the spindle axis runs X -215 to 405 and the table travels Y ±150 under the fixed spindle (Y 0). The corners (±230, ±165) are within the 15 tool margin at -X, -Y and +Y. At +X the axis passes the edge.
- **Longest tool:** a Ø20 cylinder 124 below the nose (10 from the nose to the fork plane, plus 114 of tool, D-289). At Z top, at x_pos 405 (beyond the table) and at -215 (over the table), it hits nothing. The tip is at Z 51: 51 above the table top, 126 above the tray top.
- At z_pos -75, the nose is the lowest moving part, 25 above the table.
- **Screenshot (iso, all at 0):** the two uprights stand on the tray's end plates and carry the beam, with the two rails on its front face. The Z axis and spindle hang in front at the middle, over the table, the X motor sticks out past the left end, and the BF12 sits at the right end.

## Findings for later tasks (not changed here)
- **BOM (Task 7):**
  - M02 and G01: X rails on the front face, not top and bottom.
  - G08: the joint face is 150 x 90.
  - G09: M12 x 50 upright bolts, and the beam bolts with their heads inside the tube.
  - New envelopes: X nut bracket (6082), X motor bracket and beam end plate.
  - M12: the X nut-housing spacer is 5 (as Y), not 52 x 52 x 25.
- **x_travel is 620, not 630** (UPRIGHT_W 50, UPRIGHT_GAP 40). x_rail 850, x_screw 900 and beam_len 890 are unchanged; the beam now starts 30 past the left upright (beam_x0 -350).
- **Rail spacing and bar support** (call 1) are the weak points of this layout. The other option is one rail on the top face with an L carriage, which needs the screw moved elsewhere.
- The X screw has no cover, and the X rail and block wipers are not modelled.
- The upright joint face is small (150 x 90) for a 325 upright carrying the beam 285 above it. The stiffness model (Task 2) took the joint as rigid.

## Task 5 fix round 1 (24 Nov 2026)
This section supersedes calls 1, 3 and 4 above where they differ. The review is at `.superpowers/sdd/2026-11-24-v4-fixed-gantry/task-5-review.md`.

### I1. One ground front plate; X rails 120 apart (D-312)
- **The 2 X bars are replaced by one plate**, `X rail front plate 160x20x890 (steel flat bar, shop-ground, D-312)`.
  - It sits at Y 170 to 190, Z 140 to 300, X -350 to 540, and overhangs the tube by 20 at the top and the bottom.
  - Its length follows `beam_len` and `beam_x0`.
- **The X rails are now 120 apart** (centres Z 160 and 280, was 185 and 255), off the tube's corner radii. Two Move features shift the rows: `X upper rail row to Z 280` and `X lower rail row to Z 160`. The blocks moved with the rails.
- **The Z fixed plate has 16 Ø5.5 holes for the new blocks.** They are at X ±32 and ±68, Z 144, 176, 264 and 296, inserted in the timeline before `Z axis at x_pos`, so they follow x_pos.
  - The socket heads clear the Z risers: the inner heads end at X ±36.25 and the risers start at ±37.5.
- **The uprights have a 5 x 20 relief** at their top front edge (Y 185 to 190, Z 140 to 160), so the plate does not bear on them.
- **Roll stiffness estimate** (reviewer's method: k about 200 N/µm per block, plus about 3e5 N·m/rad for the blocks' own roll):
  - At s 120: K = 4 · 2e8 · 0.06² + 3e5 ≈ **3.2e6 N·m/rad**. That is 2.4 times the 70 layout (1.3e6) and 78 % of v3's 137 (4.1e6).
  - Tool tip per 100 N: about 1.5 µm in Z (Fz, 215 lever) and 0.7 to 2.0 µm in Y (Fy, 150 to 250 lever). In all, **about 2 to 3.5 µm per 100 N**, against 5 to 8 at 70 and 1.5 to 2.5 for v3.

### I2. M16 end-plate bolts and the upright pocket
- The 8 M16 bolts (F26/F27) are modelled in `Base (extrusion + EG)` as `End plate bolt M16`: head Ø24 x 16 on the end plate's outer face, shank 50, at Y ±290 and ±45, Z -120.
- **Each upright has a Ø26 x 17 pocket** at Y 290, Z -120 for the head under it. The pocket has a 5 wall to the M12 counterbore at Y 310, Z -100, and 21 to the dowel. No overlap.

### I3. X screw seats and cover
- **The BK12 and BF12 stand on ground pads**, `X BK12 pad` and `X BF12 pad 50x80x20`, at X -350 to -300 and 490 to 540, Y 210 to 290, Z 280 to 300.
  - The pads are cut from the front plate's stock (one 950 length, G11) and ground with it (F30).
- **The whole X screw stack is 20 higher** (Move `X screw stack on ground pads (+20)`): screw axis Z 325, nut bracket Z 350 to 370. The X motor bracket was redrawn for the new axis (motor plate Z 285 to 365); its end plate (Z 160 to 295) is the beam's -X EG dam. *(Superseded by D-320, not yet modelled.)*
- **X screw cover:** 2 bellows envelopes, `X screw bellows X-` and `X+`, 60 x 40 with a Ø20 bore. Their lengths follow x_pos: X- runs from the BK12 face to the nut flange, X+ from the nut end to the BF12 face.
  - X- is 63 to 683 long and X+ 45 to 665.
  - **Closed length must be 1/11 (X-) and 1/15 (X+) of open.** That is beyond ordinary bellows; the supplier must confirm, or use a telescopic or strip cover (BOM F33).

### Minor
- `Beam end dam X+ 10 (EG dam, envelope)` at X 540 to 550 is added.
- BOM G01 now says the beam-to-upright bolt heads are cast into the EG, so the beam cannot be unbolted after the fill.

### BOM changes
- **G11, new:** one length of flat bar 160 x 20 x 950 for the plate and pads. K I Metals £61.77/m ex VAT (Store API, curl, 24 Nov 2026, https://kimetals.co.uk/materials/mild-steel/mild-steel-flat-bar/kim151153): £58.68 ex, **£70.42 inc VAT**.
- **F29:** the X bars are dropped; Y only, 1340 mm, £68.96 inc VAT (was £156.47).
- **F30:** the grinding scope is now 2 Y bars, the front plate and 2 pads (price pending).
- **F33, new:** X screw bellows (price pending).
- **M02 and G01:** the rail-face text is corrected (front plate, D-312).
- **Phase 1 priced total: £4,416.08** (was £4,433.17).

### Check results (fix round 1)
- **At 0:** 182 timeline items, all healthy; 126 solid bodies; 76 overlaps, all expected:
  - 48 bolts and pins in holes that are not modelled (now including the 8 M16 shanks in the end plates and profiles);
  - the 2 BF12 rings;
  - 26 inside v3's Z;
  - v3's Z screw in the HM12 mount (131 mm³) and its motor touching the coupling (0.04 mm³).
- **At the 4 limit poses**, every pair with a moving body (X carriage, Z, table, Y blocks, bellows) was checked, then x_pos, z_pos and y_pos were set back to 0:

| Pose (x, z, y) | Nose | Moving overlaps | Carriage to upright | To upright and M16 bolt heads | To beam bolts | To supports and pads | Bellows X- / X+ |
|---|---|---|---|---|---|---|---|
| -215, -75, -150 | 25.0 | 0 | 19.6 (left) | 141.4 | 45.6 | 20.0 (bracket to BK12) | 63 / 665 |
| -215, +75, +150 | 175.0 | 0 | 19.6 (left) | 202.3 | 45.6 | 20.0 | 63 / 665 |
| 405, -75, +150 | 25.0 | 0 | **19.6 (right)** | 177.1 | 49.6 | 19.2 (nut to BF12 pad) | 683 / 45 |
| 405, +75, -150 | 175.0 | 0 | **19.6 (right)** | 202.6 | 49.6 | 19.2 | 683 / 45 |

- **Longest tool** (Ø20, 124 below the nose) at Z top: tip at Z 51, no hits at X -215 or 405.
- **Nut to BK12:** 63 at the -X limit. **Nut to BF12:** 45 at the +X limit.

# Task 6: ATC wheel on the right side (24 Nov 2026, D-314 to D-316)
> **Superseded in part (25 Nov, D-317):** the mount bracket, column block, coupling and outboard motor below were replaced by an inboard hub block. See "Task 6 rework" at the end.

The owner saved the design as `Type_0_v4` (CNC mill project) before this task. The wheel was added afterwards and **is not saved**. `Type_0_v3` was only read.

## Placement (D-316)
- **Pickup:** spindle axis X 402 (x_max 405 leaves 3 to spare, as in v3), Y 0. The nose is at Z 70 at the pickup and lifts 50 to Z 120 to clear the holder.
- **Wheel:** axis along X at Y 0, Z -82; holder plane X 402 (holders X 379.5 to 424.5); fork mouths open -X (the spindle enters by moving +X and slides out to X 372).
- **Why this low:** the Z rails' and risers' bottom ends (Z 99, Y 87.5 to 140) travel with X and pass over the wheel. The sweep radius is 197.3, so with a 3 margin the centre can be no higher than Z -81.2 (`tools/v4_wheel_fit.py`). The Z moving plate (lowest Z 145 at nose 100, Y 55) needs the centre at least 147.6 below the nose; at the pickup it is 152 below.
- **The wheel reaches Z -278, 110 below the base bottom (Z -168).** It hangs past the bench's right edge (bench edge at X 330 or less), or the machine stands on risers of 115 or more (owner: OK).
- **Longest tool: 100 below the nose** (D-316). A Ø20 tool 100 long passes 1.2 above the hub top when it enters the pocket. The Task 5 check with 124 still holds for the table side.

## Component `ATC Wheel (Phase 2)` (one base feature, 59 bodies)
Copied from `Type_0_v3`'s `ATC Wheel (Phase 2)` with temporary BRep copies:
- **Turning part** (v3 placed by a +90° turn about Z, so v3 +Y is V4 -X): 12 forks (owner model), 12 ISO20 holders and 12 Ø6 tool stand-ins, the hub.
  - Forks trimmed at the disc's rear face (v3 Y -112), so each ends in a foot on the disc (D-304). The owner's clip shape is unchanged; the fork screws into the disc (2 x M4 each) are not modelled.
  - Hub: the v3 hub plus an 8-flat extension 31 long (101.6 AF), 43 long in all, X 386 to 429 (D-304).
  - **New `Fork disc 5083 6 mm`:** 12-gon, apothem 150, X 429 to 435, centre hole Ø44 (stub flange Ø40). No windows drawn: about 1.13 kg in 5083 as drawn; D-304 allows windows with spokes 30 or wider (about 0.6 kg).
- **Drive, turned round to the outboard side** (D-316): column block, FK12, stub shaft, coupling, 17HS24 motor and their screws, turned 180° about the wheel's vertical line and moved 11 out, so the stub flange bolts to the hub's front face through the disc's hole. FK12 X 444 to 467, motor X 490 to 594.
  - Column block: the ear (above v3 Z -6) and the floor (D-304) cut off; it now sits on the mount bracket.
- **New `ATC mount bracket 6082` (envelope, Claude's call):** a flange 20 thick on the right upright's outer face (X 320 to 340, Y 190 to 330, Z -137 to -45); an arm at Y 205 to 235, Z -137 to -117 (outside the wheel's sweep: 208 from the axis); a plate X 445 to 520, Y -40 to 235 under the column (top Z -117). The flange covers the upright's M12 counterbores: fit the bracket after the upright bolts. Bolts (flange to upright, column to plate) are not modelled.
- **Left out:** the D-303 sheet carrier, 8 standoffs and their button heads, 12 fork-to-tab screws, the 2 ear M6 screws, the old locknut and the sensor grub. **The index flag and sensor (A09) are not placed yet:** the flag was on the hub's machine-side face and the sensor on the old column ear.

## Checks (24 Nov 2026)
- Timeline: 184 items, all healthy.
- **Wheel against the frame** at wheel turns 0°, 10° and 20°: no overlaps.
- **Wheel against the X carriage and Z axis** (a script set x_pos and z_pos, then set both back to 0):

| Pose | Wheel turns checked | Result |
|---|---|---|
| Engaged: x 402, nose 70 | 0° | clean (the pickup holder in the spindle is excluded) |
| Lifted for indexing: x 402, nose 120 | 0° to 30° in 5° steps | clean |
| Withdrawn with a tool: x 372, nose 70, Ø20 x 100 tool | 0° | clean, except the pickup holder, which is the one in the spindle |
| Withdrawn, lifted: x 372, nose 120 | 0°, 10°, 20°, 30° | clean |

- **Inside the wheel (19 overlaps, all expected):** 4 hub-to-stub screws and the stub's Ø12 pilot in the hub (the holes are not cut in the new hub), 4 FK12 screws in the column, 4 motor screws and 2 inner bodies in the vendor motor (as v3).
- **Machine envelope** at y_pos 0: X -508 (X motor) to 594 (ATC motor), Y -335 to 470 (base front to Y motor; the table reaches Y ±315), Z -278 (wheel) to 700 (Z motor). **About 1,102 x 805 x 978 overall**; the Phase 2 enclosure's inside must be at least this, plus room for cables and the table's travel.

## Open (Task 6)
- Index flag and sensor: place them (flag on the disc front at r 44, sensor in the bracket or column).
- Bracket: bolt sizes and stiffness. Hand estimate: torsion of the 75 x 20 plate under the column adds about 0.2 mm per 100 N at the fork, on top of D-304's 2.6.
- BOM A-lines (Phase 2): the disc, longer hub and bracket are not in `bom.csv` yet.
- Bench: the right edge at X 330 or less, or risers.

# Task 6 rework: inboard hub block (25 Nov 2026, D-317)
The owner found the D-316 bracket "a ridiculous shape". It is replaced by one block on the base end plate, with the drive inboard. Modelled in `Type_0_v4`, **not saved**. Spec: `docs/superpowers/specs/2026-11-25-atc-inboard-hub-block-design.md`.

## What changed in `ATC Wheel (Phase 2)` (still one base feature, now 52 bodies)
- **Removed (21):** `ATC mount bracket 6082`, the column block, the D20L25 coupling, the 17HS24-E1K and its 2 inner bodies, the old stub shaft, 4 motor M3, 4 FK12-to-column M4, 4 hub-to-stub M4 x 12, and the FK12 and its locknut (re-added turned round).
- **Added (14, names end in "D-317"):**
  - `ATC hub block 6082`: a flange 20 thick on the end plate X+ face (X 270 to 290, Y -65 to 105, Z -165 to -55) with Ø28 x 17 pockets over the M16 heads at Y ±45; a floor (X 290 to 359, Z -125 to -110); a motor web (X 308 to 316, Y 25 to 105) with a Ø23 pilot hole; and a wall (X 359 to 374) with a Ø37 FK12 bore and a Ø12 sensor hole. The 4 M8 to the end plate are not modelled.
  - The FK12 (turned 180° about the vertical line X 409.05): flange X 374 to 380 on the wall's outboard face, body through the wall, locknut inboard.
  - Stub shaft: a pilot Ø12 in the hub (X 386 to 392), a flange Ø40 on the hub's inboard face (X 381 to 386), and Ø12 from X 291 to 381.
  - GT2 60T (on the stub) and 20T (on the motor), X 293 to 307, centres 60 along Y; belt envelope X 297 to 303.
  - NEMA 17 stand-in 42 x 42 x 40, no encoder, X 316 to 356, Y 39 to 81, Z -103 to -61, with its face on the web and its shaft pointing -X.
  - LJ12A3 stand-in through the wall at Y -44, Z -82 (X 330 to 380), and an M5 head flag on the hub's inboard face (X 382.5 to 386).
  - 4 x M4 x 40 from the hub's outboard face (heads X 421 to 425 in 8 deep counterbores, not cut) into the stub flange.

## Checks (25 Nov 2026)
- Timeline: 184 items, all healthy.
- New parts against each other: only the 4 M4 x 40 in the stub flange (tapped holes not cut).
- New stationary parts against the turning wheel (hub, forks, holders, tools, disc) at 0°, 10°, 20° and 30°: clean.
- Against the frame, carriage and Z: rest, engaged (x 402, nose 70), lifted (x 402, nose 120), withdrawn with a Ø20 x 100 tool (x 372, nose 70, tip Z -30), withdrawn and lifted, and the table at y ±150: clean.
- **Past the table:** x 300 with the nose at 25 and a 100 tool hits the 60T and the belt. LinuxCNC needs a keep-out past X 265: nose 50 or higher (the block top is Z -55).
- **Envelope:** ATC X max 435 (the disc), machine X max 550 (the beam end dam), so about 1,058 x 805 x 978 (was 1,102).
- Stiffness, hand estimate: a 100 N push along X at the pickup fork (r 152) bends the wall and floor by about 0.1 mm at the fork, against 0.2 for the D-316 bracket. Through 1:3, the motor's holding torque at the wheel is 3 x the direct drive's.

## Faults found after modelling (assembly walk-through, 25 Nov 2026): fix in the next model session
The clash check only finds overlaps between modelled bodies. Walking the assembly order turned up 4 faults. Proposed fixes (Claude; owner to confirm with D-317):
1. **FK12 screw heads against the stub flange.** The FK12's 4 M4 (at ±15.5, ±15.5, r 21.9, not modelled) have their heads on the hub side of the flange (X 380 to 384, reaching in to r 18.4). The stub flange (r 20, X 381 to 386) turns 1 away from the FK12 flange. **Fix:** sink the stub flange into a Ø41 x 5 counterbore in the hub's inboard face (flange X 386 to 391, pilot X 391 to 397). That leaves a 6 gap between the FK12 flange and the hub face (heads 4 tall, 2 clear). Add a Ø14 shoulder X 380 to 386 against the bearing. The hub-to-stub screws become M4 x 35 (seat X 421, tip X 386). Model the 4 FK12 M4 x 12 and rerun the turn check.
2. **The motor cannot be fitted.** The gap between the web and the wall is 43, but the motor is 40 long plus 24 of shaft through a closed hole in the web. **Fix:** make the web a separate 8 mm **motor plate** (6082) bolted to the floor with 2 x M5 in slots along Y, which also tensions the belt. The plate, motor and 20T (X 292 to 356, 64 long) drop into the bay (X 290 to 359) from above. Trim the plate to Y 25 to 85, so the rear M8 can be reached.
3. **The locknut cannot pass the pulley seat.** The M12 x 1 locknut goes on from the inboard end, so the seat has to be smaller than M12. **Fix:** the stub steps down to Ø8 from X 291 to 349 (the 60T bore is 8, as the old stub's drive end). Thread M12 x 1 X 349 to 357, journal Ø12 X 357 to 380. The stub goes in from the hub side through the FK12. The 60T and the locknut go on in the bay.
4. **M8 positions (end plate X+, F26, wave 1):** 4 x M8 tapped 15 deep at **(Y -50, Z -95), (Y 95, Z -95), (Y -20, Z -150), (Y 80, Z -150)**. All are below the end plate top (Z -75), 25 or more from the Ø28 M16 pockets at (±45, -120), and 55 apart in Z. The 2 upper heads are reached from the open front of the bay and the rear corner behind the trimmed motor plate; the 2 lower heads from below the floor (Z -125).
- **Envelope correction:** overall the machine is 44 narrower (X max 594 to 550, the beam end dam). The ATC itself ends 159 further in (X 435).

# Hub and disc simplified (25 Nov 2026, D-318)
Owner: the hub "need not be so substantial nor octagonal", the disc can be a laser-cut spoked wheel. Modelled in `Type_0_v4`, **not saved**. `ATC Wheel (Phase 2)` is still one base feature, now 49 bodies.

- **Removed (9):** the 8-flat hub, the solid 12-gon disc, the D-317 stub shaft, the 4 hub-to-stub M4 x 40, the hub-face index flag and the old LJ12A3 stand-in.
- **Added (6, names end in "D-318"):**
  - `Fork disc 5083 6 mm, laser-cut spoked wheel`: X 429 to 435, 12-gon rim apothem 150 outside and 125 inside, 6 spokes 30 wide at 0, 60 ... 300 deg (behind forks 1, 3, 5, 7, 9, 11), inner ring r 56, centre hole Ø14. Window corners are sharp in the model; R 6 in the DXF. 266 cm3, about 0.71 kg.
  - `SHF12 shaft support as hub` (envelope): flange 47 square x 7 on the disc rear face (X 422 to 429), body Ø25 X 401 to 422, bore 12. Check it against the bought part (A10).
  - Stub shaft (fault fix 3 included): Ø8 X 291 to 349, Ø12 (M12 x 1) to 357, journal Ø12 to 380, shoulder Ø16 X 380 to 384, Ø12 to 428. The 60T stand-in still shows a 12 bore (buy bore 8, A08).
  - Index flag: M5 cap head Ø8.5 x 5 on the disc inner ring rear face at Y -40, Z -82 (r 40), X 424 to 429.
  - LJ12A3 stand-in at r 40, X 374 to 422 (face 2 from the flag), in a printed PETG sleeve (tube Ø18, X 374 to 411, with a tab to Y -64 for 2 x M3 into the wall). The cable goes back through the wall's old Ø12 hole at r 44.
- **Bellows hidden:** the 4 bellows envelopes (Y front and rear, X- and X+) are hidden (light bulb off), not deleted.
- **D-317 faults now:** fault 1 is gone (the stub has no flange). Fault 3 is modelled. Faults 2 (separate motor plate) and 4 (M8 positions, drawing note) are still open.

## Checks (25 Nov 2026, D-318)
- Timeline: 184 items, all healthy.
- The 6 new bodies against every solid body in the design, with the turning set (forks, holders, tools, disc, SHF12, flag, stub) turned 0, 10, 20 and 30 deg: no overlaps.
- Clearances: the sensor body (r 34 to 46) and sleeve (r 31 to 49) against the tool tips (r 56): 7; the SHF12 flange flat (23.5) against the sensor (r 34): 10.
- Not rerun: the carriage poses. The new parts are inside the old hub and disc envelopes or below Z -58 (the withdrawn tool tip is at Z -30).

# Task 28: rear shear plates (25 Nov 2026, D-323)

- New component `Rear shear plates (D-323)`, one base feature, 40 bodies. Per side: `Rear shear plate X± 10x200x445` (X ±120 to ±320, Y 335 to 345, Z -165 to 280; 8 x Ø11, 6 x Ø9), `Beam rear spacer X± 80x25x200` (Y 310 to 335, Z 180 to 260; 4 x Ø8.5 x 22 tapped, 4 x Ø11 countersunk Ø20), 4 `Rear plate screw M10x30 ... upright`, 4 `... spacer`, 4 `Spacer screw M10x35 countersunk`, 6 `Rear plate screw M8x20 ... T-nut`. Steel, material copied from the upright.
- Cuts into other components (base feature of tool bodies + Combine cut each): `Upright X+/X- rear M10 tapped holes D-323` (Ø8.5, Y 310 to 335, X ±295, Z -40, 20, 80, 140; clear of the M12 joint bolts at Z -140/-100 and the beam bolt holes at Y 220/280); `Beam rear wall M10 tapped holes D-323` (Ø8.5 through the 8 wall at X ±175, ±265, Z 200, 240); `Beam EG core screw-tip holes D-323` (Y 300 to 302).
- Checks: timeline all healthy. New bodies against every visible body: only screw threads in their tapped holes (M10 in Ø8.5: 436 mm³ in the upright, 174 in the beam wall, 44 in the core, 436 in the spacer) and the M8 T-nut screws in the profile envelope (503 mm³ each; the T-slots are not modelled). Table at full +Y travel reaches Y 315, the plate is at 335 (20 clear); the Y motor plate is at X ±40 only; the X carriage stays in front of Y 285.
- **Saved** (owner asked, 25 Nov 2026).

# Task 29 Step 2: model completed for RFQ (26 Nov 2026, D-320, D-325–D-327, D-331–D-335)

Modelled in `Type_0_v4` (timeline **320 items, 0 unhealthy**; **464 visible solid bodies**, **not saved** — owner saves). Every envelope is replaced with a real part, every body has its material set, and every joint hole has a modelled fastener.

## 1. X HM12-60-V, ground pads, 865 mm screw, and beam end caps (`D-320`, `D-332`, `D-335`)
- **Removed (7):** `Beam end dam X+ 10`, `X motor bracket 10`, `X BK12 fixed support`, `X coupling guard`, `X BK12 pad 50x80x20`, `X screw DFU1605 900`, old `X coupling D25L35`.
- **`X HM12-60-V mount` (`D-320`):** transformed copy of `Z HM12-60-V` at `X -356 to -266, Y 220 to 280, Z 295 to 355` (foot on `Z = 300`, axis `Y = 250, Z = 325`).
- **`X HM12 pad 90 x 60 x 20` (`G11`, `D-332`):** `X -350 to -260, Y 220 to 280, Z 280 to 300`, with a `6.5 x 5.5` step relief at `X -350 to -343.5, Z 294.5 to 300` so the HM12's 12 mm motor flange (`X -356 to -344, Z 295 to 355`) clears the pad by `0.5 mm`. Held to the beam top wall by `4 x M6 x 20` counterbored (`Ø10.5 x 8`) screws (`X -338, -301; Y 235, 265`); carries `2 x M6 x 35` + `4 x M6 x 45` HM12 bolts (`X -316, -286, -273; Y 227, 273`). `X BF12 pad 50 x 80 x 20` gets `4 x M6 x 20` counterbored hold-downs + `2 x M6 x 40` BF12 bolts. Both pads cut from one `90 mm` slice of the `160 x 20` `G11` flat bar (`890 + 90 = 980 mm`).
- **`X screw DFU1605 865` (`D-332`):** user parameter `x_screw = 865 mm`; `Ø10` drive end `X -325 to -303` (`22 mm`), `Ø12` bearing journal `X -303 to -266` (`37 mm`), `Ø16` thread `X -266 to +520` (`786 mm`), `Ø10` BF12 journal `X +520 to +540` (`20 mm`). `X coupling D25L35` sits inside the HM12 at `X -348 to -313`.
- **`Beam end caps 120 x 120 x 5` (`G12`, `D-320`, `D-335`):** two rounded (`R16`) 5 mm mild steel plates at `X -355 to -350` and `X 540 to 545`, each held by `4 x M5 x 16` into blind tapped holes in the 8 mm SHS walls (`(Y 250, Z 276), (Y 250, Z 164), (Y 194, Z 220), (Y 306, Z 220)`) + `F18` silicone.

## 2. Z and X 75 mm belt folds (`D-325`–`D-327`, `D-331`)
Both axes share **identical** fold components (`75 mm` centres, `HTD 250-5M-15` 50T belt, `2 x 6000-2RS` `10 x 26 x 8` bearings, vendor pulley `cad/vendor/htd5m_20t_15.step` bored `Ø10` hub-inboard):
- **Fold plate (`70 x 142 x 20` 6082, qty 2):** full `20 mm` bearing boss over the HM12 (`Ø26` bearing bores `8` deep each side of a `Ø22 x 4` shoulder; `4 x Ø4.5` plain through-holes on `±24.75` square for surface-mounted `4 x M4 x 30` SHCS — `Ø8 x 6` counterbores removed per `D-337` to increase front edge wall from `1.25 mm` to `3.00 mm`), stepped to an `8 mm` motor wing (`±4 mm` slotted `Ø38.5` pilot opening + `4 x Ø5.5` tension slots on `50 x 50` for `4 x M5 x 16` + M5 nuts).
- **Stub shaft (`Ø10 x 68` steel, qty 2):** `Ø10 h6 x 42` lower coupling/bearing shaft, `Ø14 x 1.5` shoulder above the upper bearing inner race, `Ø10 h6 x 24.5` upper pulley seat (retained below the lower bearing by a DIN 471 `10 mm` circlip inside the HM12 `Ø50` pilot bore).
- **Z fold (`Z axis and spindle`, moves with `x_pos`):** `Z fold plate` at `Z 554 to 574`; pulleys at `Z 575.5 to 601.7` (**machine Z max `601.7 mm`**, down `98.3 mm` from `700.0`); `24HS34` brake motor flipped behind `Z fixed plate` (`X ±30, Y 140 to 211, Z 420 to 566`, shaft up to `587`, `50 mm` clear above `X nut bracket` top `Z 370`).
- **X fold (`X axis`):** `X fold plate` at `X -376 to -356, Y 220 to 362, Z 290 to 360`; pulleys at `X -403.7 to -377.5` (**machine X min `-403.7 mm`**, down `104.3 mm` from `-508.0` and `132 mm` shorter than inline HM12); `24HS40` motor behind the beam (`X -368 to -243, Y 294.5 to 355.5, Z 294 to 355.5`, shaft to `-389`, `14 mm` above beam and rear shear plate tops `Z 280`).

## 3. Envelopes replaced, table grid, and joint fasteners (`D-333`–`D-335`)
- **Table (`M11`, `D-334`, `D-335`, `D-337`):** `rail_x` moved inward `5 mm` from `205` to **`200 mm`** (`D-337`): Y bars `X ±175..±225` (M8 T-nut holes `X ±183`), Y rails `X ±190..±210`, Y blocks `X ±178..±222`. `54 x M6` blind (`20 mm` deep) grid on `50 mm` pitch (`X -200..+200, Y -125..+125`) + `4 x Ø8 H7 x 18` blind dowels at `(±175, ±100)` + `Ø10 x 15` top counterbores for `16 x M5 x 16` Y-block screws at **`X ±184, ±216`** (centring the `X = ±200` fixture holes between the block mounting holes; outer edge wall increased from `4.0` to **`9.0 mm`**) and `4 x M5 x 25` Y-nut screws. Drip skirts replaced by `4 x` printed **PETG** side skirts (`164.5 x 67 x 3`, 2 halves per side to fit the P1S bed) screwed horizontally (`8 x M4 x 10`) into M4 tapped holes in the table side edges (`X = ±230, Z = -12.5`), clearing the `HGH20CA` blocks (`X ±222`) by **`8 mm`**.
- **Laser mild-steel parts (`D-335`):** `Y motor plate 80 x 155 x 10` (`Ø38.5` bore, `4 x M5 x 16` motor screws, `4 x M8 x 20` rear-profile T-nut screws), `Y` and `X` `nut housing spacers 52 x 40 x 5`, and `Bottom sheet 500 x 670 x 3` (`F28`, `12 x M6 x 12` button screws into profile bottom T-nuts).
- **`X nut bracket` & `Z fixed plate` (`D-333`):** tapered `150 -> 80 x 145 x 20` 6082 bracket bolted through `Z fixed plate` at `Z = 360` with `4 x M6 x 35` (`X = ±68.5, ±26.0`, clear of Z risers) + `2 x Ø6 x 24` dowels (`X = ±12.0`), plus `4 x M5 x 25` into `X DSG16H`. The 9 obsolete v3 PrintNC X-roller holes in `Z fixed plate` are plugged.
- **Remaining rail, plate and frame holes & screws:** `16 x M5 x 16` Y rail screws + `16 x M8 x 25` counterbored Y bar T-nut screws (`X = ±188`); `28 x M5 x 16` X rail screws + `12 x M8 x 20` counterbored X front-plate-to-beam screws (`Z = 195, 245`); `12 x M5 x 35` Z rail+riser screws + `4 x Ø6 x 18` riser dowels; `16 x M5 x 16` X-block screws; `6 x` Z HM12 screws (`2 x M6 x 35`, `4 x M6 x 45`); `16 x M5 x 16` Z-block screws + `4 x M5 x 20` Z-nut screws; `4 x M6 x 40` Y BK12 + `2 x M6 x 35` Y BF12 screws; end-plate & upright clearance/tapped/dowel holes + `4 x M8 x 30` ATC block flange bolts (`D-317`).

## 4. Materials assigned (`470` total bodies: `464` visible, `6` hidden)
- `Steel`: 393 (bars, plates, beam, uprights, rear shear plates/spacers, rails, carriages, ballscrews, nuts, housings, motors, bearings, stub shafts, steel bolts/screws)
- `Aluminum 6061` (stands in for 6082/6063 in Fusion's library; drawings state 6082-T6): 33 (4 base profiles, table M11, Z fixed/moving plates, 2 Z risers, X nut bracket, Z & X fold plates, Z & X HM12s, 4 pulleys, 2 couplings, spindle clamp + 2 tram blocks, ATC hub block, SHF12, etc.)
- `Aluminum 5083 87 Cold Formed`: 1 (`Fork disc 5083 6 mm`)
- `Stainless Steel`: 6 (4 upright dowels `G08`, ATC `Stub shaft 303`, Jianken spindle + nose)
- `ABS Plastic` (stands in for printed PETG): 27 (4 drip skirts, coupling guard, 12 ATC forks, sensor sleeve, etc.)
- `Rubber`: 7 (Z, X and ATC belts + 4 hidden bellows)
- `Granite, Cut, Polished` (stands in for EG fill): 3 (2 base pockets + beam core)

## 5. Clash and clearance check across 9 poses (26 Nov 2026)
Overall machine envelope at rest (incl. ATC wheel): **`X -403.7 to +550.0` (`953.7`) × `Y -335.0 to +470.0` (`805.0`) × `Z -278.0 to +601.7` (`879.7`)**.

| Pose `(x_pos, z_pos, y_pos)` | Unhealthy timeline | Unexpected overlaps | Nose Z | Z motor to X motor | X nut brkt to X motor | Z motor to X nut brkt | X nut to HM12 / BF12 | Table to Y motor |
|---|---|---|---|---|---|---|---|---|
| `0, 0, 0` (rest, all 464 pairs) | 0 | **0** | 100.0 | 237.7 | 168.3 | 50.0 | 236.0 / 450.0 | 159.0 |
| `-215, -75, -150` | 0 | **0** | 25.0 | 105.5 | **9.5** | 50.0 | **21.0** / 665.0 | 309.0 |
| `-215, +75, +150` | 0 | **0** | 175.0 | 105.5 | **9.5** | 50.0 | **21.0** / 665.0 | **9.0** |
| `+215, -75, +150` (table +X) | 0 | **0** | 25.0 | 440.8 | 383.1 | 50.0 | 451.0 / 235.0 | **9.0** |
| `+215, +75, -150` (table +X) | 0 | **0** | 175.0 | 440.8 | 383.1 | 50.0 | 451.0 / 235.0 | 309.0 |
| `+405, +75, +150` (hard +X) | 0 | **0** | 175.0 | 626.9 | 573.1 | 50.0 | 641.0 / 45.0 | **9.0** |
| `+405, +75, -150` (hard +X) | 0 | **0** | 175.0 | 626.9 | 573.1 | 50.0 | 641.0 / 45.0 | 309.0 |
| `+402, +20, 0` (ATC lifted) | 0 | **0** | 120.0 | 624.0 | 570.1 | 50.0 | 638.0 / 48.0 | 159.0 |
| `+402, -30, 0` (ATC engaged) | 0 | **0** (excl. held holder 1) | 70.0 | 624.0 | 570.1 | 50.0 | 638.0 / 48.0 | 159.0 |


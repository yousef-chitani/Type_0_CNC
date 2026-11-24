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
   - **The motor is in line at -X, beyond the beam end** (X -508 to -362), on a 10 mm bracket envelope. Its end plate bolts to the beam end and is also the EG dam. The coupling guard is copied from Y.
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

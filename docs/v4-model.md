# V4 Fusion model: base, Y axis, table (Task 4, 24 Nov 2026)

Claude built this model with the Fusion MCP, in a **new, unsaved Fusion design** (Fusion named it `Untitled`). **The owner saves it as `Type_0_v4`.** `Type_0_v3` was not changed.

Uprights, beam and the X and Z axes are Task 5. The end plates' outer faces (X ±270) are left as the upright bolting faces.

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
  - **Task 5 should reconcile this** with `base_width` and the beam overhang.
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

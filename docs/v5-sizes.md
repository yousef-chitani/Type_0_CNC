# V5 sizes (PrintNC moving gantry, 16-tool rack behind the bed)

Made by `tools/v5_sizes.py` (`PYTHONUTF8=1 python tools/v5_sizes.py`). All lengths in mm. The one source of V5 lengths for plan Tasks 2 to 8. Asserts at the bottom fail if a rule breaks.

**State (26 Nov 2026): PASS, all inputs filled.** The holder stack comes from the real ISO20-ER16 holder STEP (`cad/vendor/iso20_er16_holder.step`), with the nose taken as the spindle front face where the holder flange seats (D-352). Rack holder tops can sit from **70.85 to 120** above the table.

## Result

| Size | mm | Rule |
|---|---|---|
| x_travel | 433 | max(work 400, rack row 420) + 2 x 6.5 tool radius |
| y_travel | 450 | 300 (250 of work) + rack 150 |
| z_travel | 200 | nose 25 to 225 (D-348) |
| rack_row_span | 420 | 7 x 60, first to last holder centre |
| rack_y_depth | 150 | 40 gap + 30 entry slide + 80 row pitch (D-351) |
| holder_top_min | 70.85 | 25 + 45.85 holder stack (real ISO20 holder, D-352) |
| holder_top_max | 120 | 225 - 5 - 100 tool (D-350) |
| x_rail | 650 | 433 + 177.5 carriage (100 pitch + 77.5 block) + 20 = 630.5, next LiMo size |
| y_rail | 650 | 450 + 175 Y roller + 2 x 0.5 = 626, next LiMo size |
| z_rail | 400 | 200 + 100 + 77.5 + 20 = 397.5, next LiMo size |
| x_screw, y_screw | 750 | rail + 0.7 + 59 (inside HM12-60-V) + 32 (past the rail at BF12) = 741.7, next 50. A standard C5 length, but the HM12 drive end is LiMo's custom end machining (D-211) |
| z_screw | 400 | v3 350 + 50 (D-348) |
| beam_len = frame_x | 830.7 | 49 + 35.5 BF riser + 0.5 + rail 650 + 0.7 + 95 HM12 (beam spans the Y rollers' outer faces, PrintNC) |
| frame_y | 781.7 | HM12 95 + 0.7 + rail 650 + 0.5 + BF riser 35.5, on the Y tube (motor overhangs the tube end, as PrintNC) |
| y_rail_spacing | 750.7 | frame_x - 2 x 40 |
| frame_inner_x | 670.7 | between the Y tubes (SHS 80 x 80 x 6, D-354) |
| beam_h, beam_d | 200, 150 | RHS 200 x 150 x 8 standing up (D-353) |
| x_rail_spacing | 122 | X rail centres on the beam front (D-355) |

**Whip:** longest screw 750 (X and Y), root Ø12.8, fixed-supported, whole length (conservative): **3,433 rpm at 80 %** of critical, 17.2 m/min at lead 5.

## Inputs and sources

Tags: **STEP** measured, **DRAWING**, **D-** decision, **LIMO** live page, **ESTIMATE**.

| Input | Value | Source |
|---|---|---|
| Work area | 400 x 250 | D-344 |
| Y travel for the work | 300 | requirements (250 of work), as V4 |
| Nose | 25 to 225 | D-348 |
| Tool radius | 6.5 | ER20 max collet 13 (D-78 spindle ER20) |
| Rack | 2 x 8, pitch 60 | D-344. Real holder flange Ø33 (STEP), so 27 between flanges (the Ø45 stand-in left 15) |
| Entry slide | 30 | `docs/atc-wheel.md` (Y -55 to -85) |
| Row pitch Y, bed gap | 80, 40 | D-351 |
| Clear over the front row | 5 | plan Review Focus |
| Longest tool | 100 | D-350 |
| Nose to holder top at pickup | 45.85 | STEP `cad/vendor/iso20_er16_holder.step`: flange top 7.483 to pull-stud top 53.329. Nose = spindle front face, where the flange top seats (D-352; the Jianken STEP shows the flange top at its front face X 319). From the taper's gauge diameter (Ø22.22, at 8.233) it is 45.10; the larger figure is used |
| Holder flange | Ø33 | STEP `cad/vendor/iso20_er16_holder.step` (row-spacing check: 80 >= 30 entry + 33 + 5) |
| HGH20CA length | 77.5 | STEP `cad/vendor/hgh20ca_block.step` |
| Block pitch, rail spare (X, Z) | 100, 20 | D-150 |
| X carriage | 150 | Type 0 Z fixed plate width (D-179, D-191) |
| DFU1605 nut | 100 long | STEP `cad/vendor/dfu1605_nut.step`; DRAWING DIN table L 100 |
| Screw root diameter | 12.8 | DRAWING DIN table: d 16 - ball 3.175, rounded down |
| BK12, BF12 | 25 (37 with nut), 20 | STEP `cad/vendor/bk12.step`, `bf12.step` |
| HM12-60-V length | 95 | DRAWING `cad/vendor/drawings/hm12_60_v_motor_mount.png` (the 3rd-party model is 90) |
| Screw end inside HM12 | 59 from its inner face | D-320 (V4 model, 90 mount). **Check with the 95 drawing** |
| Y roller (carriage) | 175 | STEP PrintNC: nut plate to fill plate 1274 to 1439, + 10 of nut past the nut plate (SFU nut from 1264). The DFU flange sits where the SFU flange does |
| Carriage to riser at the end | 0.5 | STEP PrintNC: fill plate 1439, BF riser 1439.5 |
| Rail end to drive riser | 0.7 | STEP PrintNC: rail 64, BK riser 63.3 |
| BF12 riser | 35.5 | STEP PrintNC: 1439.5 to 1475 |
| Screw past the rail, BF end | 32 | STEP PrintNC: rail 1439, screw 1471 |
| Beam end to BF riser | 49 | STEP PrintNC: beam -530, riser -481 |
| Y roller half width | 40 | STEP PrintNC: roller 80, rail at its centre (±490) |
| Y frame tube width | 80 | SHS 80 x 80 x 6 (D-354); PrintNC's roller is 80 (STEP) |
| Beam | RHS 200 x 150 x 8, rails 122 apart | D-353, D-355 (`tools/v5_beam.py`) |
| Z v3 | rail 350, screw 350, travel 150 | D-136 |

PrintNC STEP: `PrintNC V4 Metalcutter V4.0.33 Elements to take.step` (repo root, not in git). It holds the rollers, beam, rails, screws and supports, but **not the frame tubes**, so the frame tube lengths beyond the Y axis parts (`frame_y`) come from the axis parts, not from PrintNC's tubes.

**Seen in the STEP:** the Y block grease fittings reach 1442.1, past the rail end (1439) and the BF riser face (1439.5). At V5's Y max the fittings must clear the riser: check in Task 4.

## LiMo lengths (curl, 26 Nov 2026)

- `linear-guide-set-hgh15-20-25-30` (2 rails + 4 blocks): 200 to 900 in 50s, 1000 to 1800 in 100s, 2000. Custom 10 to 4,000.
- `dfu1605-2005-2505-2510-double-nut-ball-screw-set-c5-gound`: 300 to 1000 in 50s, 1100 to 2000 in 100s. Custom 10 to 4,000.
- All V5 rails (650, 650, 400) and screws (750, 750, 750, 400) are standard lengths.

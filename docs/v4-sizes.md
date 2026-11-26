# V4 sizes (fixed gantry, moving table)

Made by `tools/v4_sizes.py` (`PYTHONUTF8=1 python tools/v4_sizes.py`). All lengths in mm. This is the one source of V4 lengths for the BOM and the Fusion model. Asserts at the bottom of the script fail if a rule breaks.

## Result (updated 26 Nov 2026: D-332 865 mm X screw)

| Size | mm | Rule |
|---|---|---|
| x_travel | 620 | 430 work + 190 wheel reach (Task 5, 24 Nov 2026) |
| y_travel | 300 | table 330 minus 15 tool margin at each end |
| z_travel | 150 | v3 (nose 25 to 175 above table, D-267) |
| x_rail | 850 | travel + 100 + 77.5 + 20 = 817.5, next LiMo size |
| x_screw | **865** | **D-320, D-332 (26 Nov 2026):** `X HM12-60-V` at `X -356..-266` on the `90 x 60 x 20` pad (`X -350..-260`), `BF12` at `X 520..540` → screw spans `X -325..+540` = **865 mm** (custom length at LiMo; saves 35 mm width vs overhanging a 900 mm screw) |
| y_rail | 500 | 497.5, next LiMo size |
| y_screw | 600 | 553, next 50 mm |
| z_rail | 350 | v3 (need 347.5) |
| z_screw | 350 | v3 (`Z HM12-60-V` mount; custom length at LiMo, D-136) |
| beam_len | 890 | X rail 850 + 20 each end |
| base_len | 670 | table 330 + y_travel 300 + 20 each end |
| base_width | 640 | table 460 + 2 x (40 gap + 50 upright): uprights' outer faces at X ±320 (tray 500 + 2 x 20 end plates = 540, U2 flat bar 50) |
| x_rail_x0, x_rail_x1 | -330, 520 | rail centred on the span the blocks sweep over the travel (-303.75 to 493.75; spindle axis X -215 to 405, blocks at ±50) |
| beam_x0, beam_x1 | -350, 540 | rail + 20 each end |
| beam_overhang_left | 30 | past the left upright's outer face (-320) |
| beam_overhang_right | 220 | past the right upright's outer face (+320) |

## Inputs and sources

| Input | Value | Source |
|---|---|---|
| Work X travel | 430 | D-233 (X slider 430) |
| Work area Y | 250 | design doc, 24 Nov 2026 (D-79) |
| Z travel | 150 | design doc; D-267 (nose 25 to 175) |
| Table | 460 x 330 | design doc; D-233 (M11 460 x 330 x 25) |
| Tool margin | 15 | estimate (tool radius past each end of travel) |
| Block length (HGH20CA) | 77.5 | D-150 |
| Block pitch | 100 | D-150 |
| Rail spare | 20 | D-150 |
| Screw length minus travel (Y) | 253 | D-150 (BK12 + BF12 ends) |
| X screw length (`X_SCREW_HM12`) | 865 | D-320, D-332 (`HM12-60-V` at `X -356..-266`, `BF12` at `X 520..540`) |
| BK12 / BF12 length | 25 / 20 | LiMo / vendor STEP |
| Screw root diameter | 13.2 | typical DFU1605 |
| Z rail, Z screw | 350, 350 | D-136 |
| Upright width | 50 | D-309 (U2 flat bar 50 x 150) |
| Table edge to upright | 40 | V4 model (Task 4): table edge 230, tray end plate outer face 270 |
| Wheel pickup offset | 85 (pickup at X 402, x_max 405) | D-316 |
| Wheel reach (`WHEEL_REACH`) | 190 | derived: 230 + 40 + 50 + 85 - 215 |
| Base and beam end margins | 20 | Task 4 / Task 5 |

## LiMo lengths (read 24 Nov 2026, updated 26 Nov 2026)

- **HGH20CA sets:** `850` (X), `500` (Y), and `350` (Z) are all standard LiMo sizes (1 set each; no Y2).
- **DFU1605 C5 double-nut sets:** `600` (Y, standard BK12/BF12 end) is a standard size; **`865` (X) and `350` (Z)** are custom lengths (`10 to 4,000 mm` supported on the LiMo C5 listing), both ordered with the **Z-style `Ø10 x 21.5–22 mm` drive end + `Ø12 x 37 mm` bearing seat** for the `HM12-60-V` mounts (`D-211`, `D-320`, `D-332`), and with `BF12` only if LiMo allows omitting the unused X and Z `BK12`s.

## Whip speed

`x_screw` 865, DFU1605 root diameter 13.2, fixed-supported ends (`HM12-60-V` fixed, `BF12` supported): **2,662 rpm at 80 % of critical speed** (`13.3 m/min` at 5 mm lead), well above stepper speeds.

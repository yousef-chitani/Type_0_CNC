# V4 sizes (fixed gantry, moving table)

Made by `tools/v4_sizes.py` (`PYTHONUTF8=1 python tools/v4_sizes.py`). All lengths in mm. This is the one source of V4 lengths for the BOM and the Fusion model. Asserts at the bottom of the script fail if a rule breaks.

## Result

| Size | mm | Rule |
|---|---|---|
| x_travel | 620 | 430 work + 190 wheel reach (was 630 with the 80 upright and 20 gap; Task 5, 24 Nov 2026) |
| y_travel | 300 | table 330 minus 15 tool margin at each end |
| z_travel | 150 | v3 |
| x_rail | 850 | travel + 100 + 77.5 + 20 = 817.5, next LiMo size |
| x_screw | 900 | travel + 253 = 873, next 50 mm |
| y_rail | 500 | 497.5, next LiMo size |
| y_screw | 600 | 553, next 50 mm |
| z_rail | 350 | v3 (need 347.5) |
| z_screw | 350 | v3 (HM12-60 mount; the +253 rule does not apply). D-136 orders Z 350; whether 350 clears the 150 travel with the HM12 mount is to check in Task 5 |
| beam_len | 890 | X rail 850 + 20 each end |
| base_len | 670 | table 330 + y_travel 300 + 20 each end |
| base_width | 640 | table 460 + 2 x (40 gap + 50 upright): uprights' outer faces at X ±320, as modelled (tray 500 + 2 x 20 end plates = 540, U2 flat bar 50) |
| x_rail_x0, x_rail_x1 | -330, 520 | rail centred on the span the blocks sweep over the travel (-303.75 to 493.75; spindle axis X -215 to 405, blocks at ±50) |
| beam_x0, beam_x1 | -350, 540 | rail + 20 each end |
| beam_overhang_left | 30 | past the left upright's outer face (-320) |
| beam_overhang_right | 220 | past the right upright's outer face (+320). Was 230 with the beam flush left: that left the blocks 3.75 past the rail end at the -X limit |

## Inputs and sources

| Input | Value | Source |
|---|---|---|
| Work X travel | 430 | D-233 (X slider 430) |
| Work area Y | 250 | design doc, 24 Nov 2026 (D-79) |
| Z travel | 150 | design doc; D-267 (nose 25 to 175) |
| Table | 460 x 330 | design doc; D-233 (fixture plate 330 long) |
| Tool margin | 15 | estimate (tool radius past each end of travel) |
| Block length (HGH20CA) | 77.5 | D-150 |
| Block pitch | 100 | D-150 |
| Rail spare | 20 | D-150 |
| Screw length minus travel | 253 | D-150 (screw 653 for 400 travel) |
| BK12 / BF12 length | 25 / 20 | estimate, check LiMo drawing |
| Screw root diameter | 13.2 | estimate (typical 1605) |
| Z rail, Z screw | 350, 350 | D-136 |
| Upright width | 50 | D-309 (U2 flat bar 50 x 150) |
| Table edge to upright | 40 | V4 model (Task 4): table edge 230, tray end plate outer face 270 |
| Wheel pickup offset from right upright outer face | 85 | estimate, fixed in Task 6 |
| Wheel reach (named constant `WHEEL_REACH`) | 190 | derived: table half 230 + 40 + 50 + 85, less 215 (end of work travel); pickup at X 405 |
| Base and beam end margins | 20 | estimate |

## LiMo lengths (read 24 Nov 2026)

`curl -sL --compressed` on https://limobearing.com/. The site is not Shopify or WooCommerce (`/products.json` and `/wp-json/wc/store/products` return 404), so I read the product pages.
- HGH20CA sets (page `linear-guide-set-hgh15-20-25-30`): 200 to 900 in 50 steps, then 1000 and up. 850, 500 and 350 are all sold.
- DFU1605 (page `dfu1605-2005-2505-double-nut-ball-screw`): listed 300 to 1000 in 100 steps, plus "custom lengths 10 to 4,000 mm". So 900 and 600 are standard sizes; 350 is not (next size up 400, cut to length, or custom length). The 50 mm steps follow D-136's order. Confirm the exact screw length with LiMo before the order.

The base_len check assumes the Y screw lies along the base with the BK12 and BF12 supports outside its ends.

## Whip speed

x_screw 900, DFU1605 root diameter 13.2, fixed-supported ends (BK12 fixed, BF12 supported), whole 900 as the span (a bit pessimistic): critical speed about 3,070 rpm, **2,460 rpm with the usual 80 % margin**. At 5 mm lead (1605) that is a feed of about 12 m/min, above what the steppers give, so whip is not the limit.

## Open

- The wheel pickup offset (85) puts the wheel's centre only 85 past the upright, but the wheel is about 392 across (D-302). It fits only if the wheel sits below the base's side or the pickup is placed further out. Task 6 decides; a larger offset adds to x_travel, x_rail and x_screw. With x_travel 620: x_rail stays 850 up to 32 more offset, x_screw stays 900 up to 27 more and within 1000 up to about 127 more. A larger travel also moves the rail and the beam (x_rail_x0, beam_x0), which the V4 model takes as parameters.

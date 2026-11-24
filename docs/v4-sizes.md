# V4 sizes (fixed gantry, moving table)

Made by `tools/v4_sizes.py` (`PYTHONUTF8=1 python tools/v4_sizes.py`). All lengths in mm. This is the one source of V4 lengths for the BOM and the Fusion model. Asserts at the bottom of the script fail if a rule breaks.

## Result

| Size | mm | Rule |
|---|---|---|
| x_travel | 630 | 430 work + 200 wheel reach |
| y_travel | 300 | table 330 minus 15 tool margin at each end |
| z_travel | 150 | v3 |
| x_rail | 850 | travel + 100 + 77.5 + 20 = 827.5, next LiMo size |
| x_screw | 900 | travel + 253 = 883, next 50 mm |
| y_rail | 500 | 497.5, next LiMo size |
| y_screw | 600 | 553, next 50 mm |
| z_rail | 350 | v3 (need 347.5) |
| z_screw | 350 | v3 (HM12-60 mount; the +253 rule does not apply) |
| beam_len | 890 | X rail 850 + 20 each end |
| base_len | 670 | table 330 + y_travel 300 + 20 each end |
| base_width | 660 | table 460 + 2 x (20 gap + 80 upright) |
| beam_overhang_right | 230 | beam 890 less base width 660, beam flush with the left upright's outer face |

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
| Upright width | 80 | estimate, Task 3 sets it |
| Table edge to upright | 20 | estimate |
| Wheel pickup offset from right upright outer face | 85 | estimate, fixed in Task 6 |
| Wheel reach (named constant `WHEEL_REACH`) | 200 | derived: table half 230 + 20 + 80 + 85, less 215 (end of work travel); matches the design doc's "about 200" |
| Base and beam end margins | 20 | estimate |

## LiMo lengths (read 24 Nov 2026)

`curl -sL --compressed` on https://limobearing.com/. The site is not Shopify or WooCommerce (`/products.json` and `/wp-json/wc/store/products` return 404), so I read the product pages.
- HGH20CA sets (page `linear-guide-set-hgh15-20-25-30`): 200 to 900 in 50 steps, then 1000 and up. 850, 500 and 350 are all sold.
- DFU1605 (page `dfu1605-2005-2505-double-nut-ball-screw`): listed 300 to 1000 in 100 steps, plus "custom lengths 10 to 4,000 mm". So 900, 600 and 350 are buyable, 900 as a standard size and 600 and 350 by custom length or the next size down to cut. The 50 mm steps follow D-136's order. Confirm the exact screw length with LiMo before the order.

## Whip speed

x_screw 900, DFU1605 root diameter 13.2, fixed-supported ends (BK12 fixed, BF12 supported), whole 900 as the span (a bit pessimistic): critical speed about 3,070 rpm, **2,460 rpm with the usual 80 % margin**. At 5 mm lead (1605) that is a feed of about 15 m/min, above what the steppers give, so whip is not the limit.

## Open

- The wheel pickup offset (85) puts the wheel's centre only 85 past the upright, but the wheel is about 392 across (D-302). It fits only if the wheel sits below the base's side or the pickup is placed further out. Task 6 decides; a larger offset adds to x_travel, x_rail and x_screw (x_screw stays within 1000 up to about 100 more).

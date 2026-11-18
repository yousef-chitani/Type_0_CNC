# Epoxy-granite tub in `Type_0_v3`: short design (18 Nov 2026)

**Status: approved by the owner and modelled, 18 Nov 2026 (D-196). The Fusion document is not saved yet.**

## Why
The tub is the one casting of the moving-gantry machine (D-137). Modelling it confirms the table height (D-191, D-192), fixes the rail-seat and bolt positions, and gives the mould drawing its sizes.

## Approaches for the tub height
| | Floor / wall above floor | High | Mass | Result |
|---|---|---|---|---|
| **A** | 60 / 80 | 140 | 121.2 kg | **Chosen by the owner, 18 Nov 2026** |
| B | 60 / 125, table on 45 spacers | 185 | 141.2 kg | Rejected: an extra joint and unpriced spacers |
| C | 105 / 80 | 185 | 185.5 kg | Rejected: needs more epoxy than the kit has spare |

## What gets modelled
All sizes in the model's coordinates. Masses are for solid EG at 2,300 kg/m³ before the seats are cut.

| Part | Size and position | Source |
|---|---|---|
| Tub outside | X ±450, Y -37 to 653, Z -15 to 125 | D-173, D-175, this design |
| Channel between the walls | X ±310, floor top Z 45, open at both ends | D-139, D-173, this design |
| Seat recess, each wall | 5 deep (floor Z 120), from X 315 to the outer face (X 450), full length, open at the ends. Moved from X 325 so the risers (X 320 to 380) sit fully on the levelling layer | D-115, D-196 |
| Levelling layer, each wall | Separate body filling the recess, Z 120 to 125 | D-12, D-115 |
| Steel bar, each wall | 40 × 10 × 684, X 330 to 370, Y -34 to 650, Z 110 to 120, separate body | D-28, D-148, F07 |
| Rail holes, each wall | 9 × M5 at X ±350, Y 37 to 517 at 60 pitch | Measured in the model |
| Riser holes, each wall | 7 × M6: (±350, -23), (±335, -6), (±365, -6), (±335, 561), (±365, 561), (±335, 629), (±365, 629) | Measured, with one correction below |

Holes are drawn at tap drill size (M5 4.2, M6 5.0) through the levelling layer and bar. No holes go into the EG below the bar.

The tub goes in a new top-level component, `EG Tub`. Existing parts are not moved or changed. The document is not saved unless the owner says so. Errors and warnings are re-counted after each write (baseline: timeline 1243, 1 error, 5 warnings).

## Calls made in this design, approved by the owner (D-196)
1. **Front riser bolts:** the model has them at X ±305, outside the 320 to 380 riser. The holes go at X ±365, mirroring the ±335 bolts, as was done for the rear bolts (D-187).
2. **The bar stays 40 wide (F07).** The M6 holes at X ±335 and ±365 then have 2.5 of steel to the bar edge.
3. **Bar length 684** covers the risers and the motor plate. 2 × 684 fits the 2 × 1000 of 40 × 10 already priced in F07, one bar from each piece.

## Found while measuring, not changed by this design
1. **Riser bolt lengths do not suit the seat.** With the bar top at Z 120, the M6 x 30 bolts at Y -23 and Y 629 end at Z 119, so they get 1 of thread. Those at Y -6 and Y 561 end at Z 107, 3 past the bottom of the bar. New lengths need the owner's decision and a live price.
2. **Parts that overlap the walls:** both Y frame trigger mounts, the Y cable chain support, the Y cable chain fixed end support and its zip tie plate, and their M5 and M6 screws. They were mounted on the old frame and need new positions.

## Not in this design
Table fixing holes, machine feet and pads, mould details, draft and corner fillets, new positions for the parts listed above.

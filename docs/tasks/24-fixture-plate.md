# Task 24: Fixture plate and front slot for vertical workholding

**Who:** main session (Fusion MCP, design judgement). **Read only:** this file, D-23, D-79, D-191, D-196, D-197, D-200, D-204, D-229 to D-232 in `docs/decisions.md`.

## Decided (19 Nov 2026)
- The plate Y roller is dropped; `Type_0_v3` keeps the PrintNC tube Y rollers (D-229).
- Front slot through the front of the cast tub floor, and the plate over it, for long parts clamped upright (D-230).
- Plate: 6082 460 x 330 x 25 (M11, as now), M6 on a 50 grid plus dowel holes (D-231).
- Plate held to the floor by cast-in fixings (D-232).
- Order: **plate first**, then the slot. The bench question (a matching hole under the slot) waits.

## Known geometry (`Type_0_v3`)
- Tub 780 x 690, channel between the walls X ±310, open at both ends, floor top Z 45, floor bottom Z -15. Cast upside down (D-204): the floor top is moulded against the channel core, so cast-in fixings there are held on that core.
- Plate on the floor: top Z 70 (D-191, D-196). Spindle nose travel Z 95 to 245 (D-214). Y travel about 386.

## Open (ask the owner, one at a time)
1. Plate position in X and Y in the tub, from the spindle's reach at both ends of X and Y travel (measure in `Type_0_v3`).
2. Grid origin and edge margins (50 grid on 460 x 330: e.g. 9 x 6 holes at 25 from the edges).
3. Dowel holes: size (Ø6 or Ø8 reamed, or bushed), count, places.
4. Cast-in fixings: threaded inserts or tapped steel strips; size, count, places; how they are held in the mould (the floor top is moulded against the core when cast upside down: check).
5. Hold-down screws: counterbored through the plate, between grid holes.
6. Then the slot: width (X), depth (Y), plate cut-out, floor strength; then the bench.

## Done when
The plate is modelled in `Type_0_v3` with its grid, dowels and fixing holes, the cast-in fixings are modelled in the tub, and the slot is sized and modelled, all decided by the owner.

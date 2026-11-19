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
1. ~~Plate position~~ **done (D-233): X ±230, Y -37 to 293, top Z 70.** Measured 19 Nov: spindle axis X -222.5, Y 292 at joint zero; Y slider (`Slider 273`, +Y) 0 to -385, X slider (`Slider 275`, -X) 0 to -430; reach X -222.5 to 207.5, Y -93 to 292. Front = -Y (Y motors at Y 638 to 650).
2. ~~Grid~~ **done (D-234): 9 x 6 M6, X -200 to 200, Y 3 to 253.**
3. Dowels: **4 x Ø8 H7 (D-234).** Proposed places, on half-grid points clear of a centre slot: (X ±175, Y 28) front, (X ±175, Y 228) back, 350 x 200 apart. **Confirmed (D-235).**
4. Cast-in fixings: **8 x M8 threaded steel inserts (D-235).** Still open: the insert part (price by curl), its length in the 60 floor, places (half-grid points near the plate edges, missing grid holes, dowels and the slot), how each is held on the channel core.
5. Hold-down: **8 x M8 socket caps, counterbored (D-235)**; length and part follow the insert.
6. Then the slot: width (X), depth (Y), plate cut-out, floor strength; then the bench.

## Notes
- `Type_0_v3` still shows PrintNC's `Wasteboard M6x20` screws (X ±305, Y 32.5 to 567.5, Z 40 to 66) inside the tub floor; the `Wasteboard` (650 x 600) is hidden. Hide or delete the screws when the plate is modelled.
- Fusion script `print` output does not come back through the MCP here: write to a file in the scratchpad and read it.

## Done when
The plate is modelled in `Type_0_v3` with its grid, dowels and fixing holes, the cast-in fixings are modelled in the tub, and the slot is sized and modelled, all decided by the owner.

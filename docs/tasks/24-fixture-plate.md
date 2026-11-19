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
4. ~~Cast-in fixings~~ **done (D-236, D-237): 8 x M8 x 24 DIN 6334 A2 hex connector nuts (B&Q, SIMFIX, £7.52 for 10), cast flush (Z 45 to 21), bolted to the channel core, D-200 prep with a short M8 screw in the back end. Places (X ±125, Y 28), (X ±175, Y 128), (X ±125, Y 228), (X ±25, Y 228).** Slot limit from these: X ±107.5, ending at Y 210 or nearer the front.
5. ~~Hold-down~~ **done (D-238, D-239): 8 x M8 x 30 socket caps 12.9 zinc (Unifix, £20.24 for 200), counterbores Ø14 x 9, 14 into the insert; back plugs M8 x 8 hex A2 (£10.45 for 10), epoxied in, head as anchor.**
6. Then the slot: width (X), depth (Y), plate cut-out, floor strength; then the bench.

## Modelled in `Type_0_v3` (19 Nov 2026, not saved)
- New component `Fixture Plate`: body `Fixture plate 6082` (X ±230, Y -37 to 293, Z 45 to 70; 54 x Ø5.0 M6 tap holes, 4 x Ø8 dowel holes, 8 x Ø9 with Ø14 x 9 counterbores; aluminium as the Z plate) and 8 bodies `M8 x 30 socket cap 12.9` (head Z 61 to 69, tip Z 31).
- In `EG Tub`: hex 13 AF pockets cut in the casting (Z 15.7 to 45), 8 bodies `Insert M8 x 24 DIN 6334 A2` (Z 21 to 45, bore 8) and 8 bodies `Back plug M8 x 8 ISO 4017 A2` (head Z 15.7 to 21, shank to Z 29). Casting volume 40,147,760 to 40,113,454 mm³ (34,306 removed).
- `Wasteboard M6x20` hidden. Clash check of the 26 bodies near the plate: none.

## Notes
- `Type_0_v3` still shows PrintNC's `Wasteboard M6x20` screws (X ±305, Y 32.5 to 567.5, Z 40 to 66) inside the tub floor; the `Wasteboard` (650 x 600) is hidden. Hide or delete the screws when the plate is modelled.
- Fusion script `print` output does not come back through the MCP here: write to a file in the scratchpad and read it.

## Done when
The plate is modelled in `Type_0_v3` with its grid, dowels and fixing holes, the cast-in fixings are modelled in the tub, and the slot is sized and modelled, all decided by the owner.

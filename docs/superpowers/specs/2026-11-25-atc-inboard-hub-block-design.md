# V4 ATC: inboard hub block (replaces the D-316 bracket and outboard drive)

**Status: approach chosen by the owner (25 Nov 2026, Q&A: "Inboard hub"). The owner approved the design ("Approve, model it"). Modelled 25 Nov (D-317), not saved. As built: `docs/v4-model.md` (Task 6 rework). Changed while modelling: the pulleys moved next to the flange (X 293 to 307) with a motor web at X 308 to 316, so the motor is 40 long, not 48.**

## Why
The owner called the D-316 bracket "a ridiculous shape". It bolts to the right upright, which stands behind the wheel (Y 185 to 335). From there it has to reach the drive column on the far side of the wheel, at Y 0. The holders sweep a disc of radius 197 in the plane X 379 to 435, so the bracket has to go round it: a flange, an arm behind the sweep, and a flat plate 275 long reaching forward. No clean shape follows that route.

## Approaches considered
1. **Inboard hub block (chosen).** One block on the base end plate's outer face, on the wheel axis. It holds the bearing and the motor on the machine side of the wheel, and nothing sits past the disc.
2. **Hang from the beam end.** One flat plate past the carriage, from the beam underside down to the outboard column. Rejected: it hangs the wheel and its indexing torque off the end of the precision X beam (220 past the upright), and the envelope stays at X 594.
3. **Tidy the current route.** One tapered plate on edge, from the upright. Rejected: it is still a dog-leg round the sweep, and the envelope stays at X 594.

## Goals
- One part from the frame to the bearing, with a short and direct load path.
- Nothing outboard of the disc, so the machine is narrower and the wheel lifts off outboard.
- Same wheel, pickup and sweep as D-316: pickup X 402, Y 0, nose Z 70; wheel centre Y 0, Z -82; holders X 379.5 to 424.5; disc X 429 to 435.

## What changes from D-316
| | D-316 (now) | Inboard hub block |
|---|---|---|
| Frame anchor | right upright outer face, Y 190 to 330 | base end plate X+ outer face (X 270), round the axis at Y 0 |
| Drive side | outboard (+X), motor out to X 594 | inboard, between the end plate and the wheel (X 270 to 379) |
| Drive | direct: FK12, coupling, 17HS24-E1K (about 150 long in line) | GT2 belt 20T/60T (1:3); A08 comes back |
| Motor (A03) | 17HS24-2004D-E1K, 80 long with encoder | short NEMA 17 without encoder, 48 long or less (for example 17HS19, about 0.59 Nm, about 1.8 Nm at the wheel through 1:3) |
| Machine envelope X max | 594 | about 435 (the disc), 159 narrower |
| Path from frame to bearing | about 400 (flange, arm, plate) | about 70 |

The in-line stack does not fit inboard: FK12 23, coupling 25 and motor 92 need about 140, and the gap is 109. That is why the drive becomes a belt.

## Layout (Claude's proposal, X along the wheel axis)
- **Hub block, one machined 6082 part**, cut on the Type 0 itself (as D-289):
  - **Flange** X 270 to 290 on the end plate face, about Y -40 to 105, Z -165 to -55. It has 2 pockets about Ø28 x 17 over the M16 end-plate bolt heads at Y 45 and Y -45 (Z -120), and 4 x M8 into tapped holes in the end plate (20 plate, blind 15). The flange stands above the end plate top (Z -75); the bolts are all below it.
  - **Floor** joining the flange to the wall, below the motor and FK12 (top about Z -110).
  - **Front wall** X 340 to 355, about Y -40 to 95, Z -125 to -55. The FK12 bolts to its inboard face on the axis, and the motor bolts to its inboard face at Y about +60, Z -82 (behind the axis, away from the operator), with slotted holes to tension the belt. Both shafts come out through the wall.
- **Belt plane** between the wall and the hub (X about 360 to 376): 60T on the stub shaft, 20T on the motor, centres about 60, closed GT2 6 mm belt about 200. A printed belt cover keeps chips off it.
- **Stub shaft** from the FK12 (locknut on the inboard side) through the 60T into the hub's inboard face (X 386). The 4 hub-to-stub screws go in from the outboard side through the hub (about M4 x 50), with their heads inside the disc's Ø44 hole, so the wheel still comes off from outboard.
- **Index sensor (A09)** in the wall at r 44 on the front side (Y about -44), facing a screw-head flag on the hub's inboard face. This closes the "flag and sensor not placed" item.
- **Removed:** the D-316 mount bracket, the column block, the coupling, the 17HS24-E1K, and their screws.

## Constraints and checks
- **Tool clearance:** the block's top (about Z -55) and the 60T (top about Z -63) sit below the withdrawn tool tip (Ø20 x 100 at nose 70, tip Z -30, X 362 to 382).
- **Spindle past the table** (X 245 and over): the block is on the spindle line (Y 0). A 100 tool at the lowest nose (25) reaches Z -75, so past X 265 the nose needs a soft limit (Z 50 or higher), as for the wheel itself. Note this for the LinuxCNC config.
- **Bench:** nothing below Z -168 inboard of X 330. The block's bottom is at Z -165.
- **Wave 1 consequence:** the end plate X+ gets 4 tapped M8 holes now (Phase 1 part). It is a plain plate, so this is a drawing note.
- The re-check uses the four poses in the `docs/v4-model.md` Task 6 checks table, with bounding-box-filtered scripts only.

## Left to the builder
Exact wall, floor and flange sizes within the envelopes above; the belt length from the real pulley sizes; screw lengths; a stiffness hand estimate, compared with D-304's 2.6 + 0.2 mm per 100 N at the fork. Expected: the block itself adds well under 0.05, so the total is about 2.6.

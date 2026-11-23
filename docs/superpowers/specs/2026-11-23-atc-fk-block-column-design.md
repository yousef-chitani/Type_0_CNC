# ATC: support block, column and stub shaft (replaces the one-piece mount): design

23 Nov 2026, 15th session. Status: **for owner approval**. Replaces `2026-11-23-atc-one-piece-mount-design.md` (D-289 to D-294) for the mount; wheel, forks, hub top, holders and the pickup layout stay.

## Why
The owner sent a picture of another machine's ATC: a column beside the frame, the wheel on a small block on top, the motor hanging out underneath. Its designer: *"the principle is just a ball screw support block and motor mount, and one little custom stub shaft."* Owner: the mount should look more like that, and the tub flange is much oversized.

## Goals
- Bought bearing block (preloaded pair, locknut) in place of the machined Ø116 web, 2 x 6804, spacer and hub spigot.
- Motor below on a motor plate, flexible coupling to the stub shaft, as in the picture.
- Parts that are flat plate or bar, made on the owner's mill (no 68-deep pocket).
- Smaller tub plate: 50 x 40 x 10.

Non-goals: moving the wheel (stays X 200, Y -174, forks Z 126 to 136, pickup unchanged); changing the forks or holders; the bench redesign (only noted).
Anti-goals: anything in the tools' sweep (tools at r 89 hang to Z 45, the longest allowed to Z 17); a joint the owner cannot reach to assemble; claiming stiffness that was not worked out.

## Approaches (owner picked A)
- **A. Flange block (FK12) on top of a column of screwed plates.** Closest to the picture, all parts flat bar. More joints than one piece. **Picked.**
- B. Same block on a cut length of 60 x 60 x 5 tube. Fewer joints; buy tube; the tub joint still needs a bracket.
- C. Base block (BK12) on an upright plate face. Works; not like the picture; block loaded sideways on its screws.

## Decided by the owner (23 Nov)
- Approach A.
- Motor hangs below as in the picture: lowest point about **Z -46** (was -10; tub bottom Z -15). **The ATC overhangs the bench front edge** (the machine moves forward on the bench; bench drawings to follow, not in this job).
- Tub plate **50 wide x 40 tall x 10**; the cast-in strip shrinks to **50 x 10 x 40** (not cast yet, drawing change).

## Design (numbers marked *call* are Claude's, for the owner to check)

**Block:** FK12 (THK sheet A15-314: shaft 12, L 27, flange H 10, nose Ø36 g6 x 17, flange Ø54 / 44 across flats, 4 x Ø4.5 on PCD 44, 7001 pair DF P5, locknut M12 x 1, 0.22 kg). Fitted by THK **mounting method B**: flange on top of the column top plate, nose down into a Ø36 H7 bore; 4 x M4 from the top into the plate. The shaft shoulder bears down on the upper collar; the locknut is under the nose, inside the column. Brand and price: curl, at build time (owner's vendor rules).

**Z stack (about, from the fixed hub underside Z 119):**
| Part | Z |
|---|---|
| Hub (unchanged above Z 119) | 119 to 131 |
| Stub shaft flange Ø40 x 5 *call* | 114 to 119 |
| Shoulder Ø14 (bears on the collar, OD 14.9) | to the block top |
| FK12 flange | 98 to 108 |
| Column top plate, 12 thick *call* | 86 to 98 |
| FK12 nose (5 below the plate) | 81 to 98 |
| Locknut | about 72.5 to 81 |
| Coupling Ø20 x 25, 8 to 5 *call* | about 47 to 72 |
| Motor plate 6 thick *call* | about 28 to 34 |
| Motor (17HS24-2004D-E1K, face up, shaft 24) | about -46 to 34 |
The builder fixes exact Z from the vendor's FK12 CAD (shoulder position T2 = 6 per THK) and the bought coupling.

**Stub shaft (steel, *call* 303 stainless or EN1A, turned; the one custom turned part):** top to bottom: Ø12 pilot x 6 into the hub; flange Ø40 x 5 with 4 x M4 tapped at r 14; Ø14 shoulder; Ø12 journal (fit per the block maker) through the block; M12 x 1 thread for the locknut; Ø8 drive end for the coupling. The hub bolts onto the flange: 4 x M4 x 10 from the hub top, counterbored in the hub (check they clear the forks).

**Hub:** cut off the Ø20 spigot and the old grub; underside flat at Z 119 (the 0.5 relief is no longer needed); Ø12 H7 pilot bore 6 deep; 4 counterbored holes for the stub shaft. The index flag stays (r 44, 202.5°, Z 116 to 119).

**Column (6082 plate, screwed and dowelled, *call* sizes):**
- Top plate 70 x 70 x 12, Z 86 to 98: Ø36 H7 bore, 4 x M4 for the block, an ear at -X carrying the index sensor (LJ12A3 M12, r 44 at 202.5°, tapped M12 x 1 plus the M4 lock grub; sensor face 2 below the flag, as now). The ear stays inside r 58 so the holders (inner edge r 66.5) clear it.
- 2 walls at ±Y, 70 (X) x 8, Z -8 to 86, 48.4 apart inside (motor 42 plus clearance), open at ±X: room for the cable boss and cables at +X, and a window to reach the coupling screws and the locknut.
- Motor plate 6 thick between the walls at about Z 28 to 34: Ø22 pilot, 4 x M3 on 31 square.

**Base L (one piece, 6082, milled from 50-wide bar, *call*):** tub plate 50 x 40 x 10 (X 175 to 225, Y -47 to -37, Z -10 to 30) with 2 x M6 counterbored at X 185 and 215, Z 21; arm 50 wide x 20 (Z -8 to 12) from the plate to the tub-side wall (about Y -141.8); a sloped gusset between arm top and plate, as in the picture (stays at Y > -78, clear of the tools, which reach Y -85 at most). The arm end screws to the tub-side wall: 4 x M5 plus 2 dowels *call*.

**Cast-in strip:** 50 x 10 x 40 at X 175 to 225, Y -37 to -27, Z -10 to 30, 2 x M6 at X 185 and 215, Z 21; Ø6.6 cores behind each hole as now. Old 80-wide strip and its holes removed and filled in the model.

**Assembly order:** stub shaft into the FK12, locknut tightened, setscrew locked; FK12 onto the top plate; walls and motor plate to the top plate; motor up onto the motor plate (M3); coupling onto the motor shaft and the stub shaft through the side window, clamp; hub onto the stub shaft flange (4 x M4); forks on; base L to the tub-side wall; the whole ATC to the tub (2 x M6 from the front).

## What it fixes and what it costs
- Fixes: the motor's own runout no longer fights the bearings (coupling); the locknut holds the wheel down (the retention we had no room for).
- Costs: about 36 lower (bench overhang); more parts (block, coupling, 5 plates against one machined part); **tilt**: the FK12's DF (face-to-face) pair lets the shaft tilt a little by design, so a downward push at a fork (r 89) rocks the wheel more than on the 2 x 6804 (23 apart). Not calculated: there is no reliable moment stiffness for a budget FK12. Check on the bench (push down at a fork, dial at the rim). Fallback if it rocks too much: a floating block (FF12, single bearing) at the bottom of the column, about 50 below the FK12, the shaft passing through it to the coupling.

## Left to the builder
Exact Z from the vendor CAD; fits; screw lengths; dowel sizes; the window size; clash and sweep checks as in `atc-wheel.md` (hub, forks, holders, flag swept; spindle against wheel); the arm and wall joint stiffness by hand calc; prices for FK12, coupling, plate (curl); BOM A06, A07 and new lines; `atc-wheel.md`, `decisions.md` (D-295 on), `cast_in_features.md`; note the bench overhang in `design-issues.md`. Do not save `Type_0_v3`: the owner saves.

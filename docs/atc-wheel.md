# ATC wheel (Phase 2): as modelled (22 Nov 2026, D-250, D-253 to D-255)

![ATC wheel at the front right of the tub](atc-wheel.png)

The ATC wheel is the top-level component `ATC Wheel (Phase 2)` in `Type_0_v3`. It is a horizontal umbrella wheel (D-138) in front of the tub. The bracket comes straight out of the tub front face along X 200, the spindle's pickup line (D-253). The wheel is direct driven (D-254). It carries the owner's fork (D-255). **The model is not saved.**

## Layout (world mm, Y = 0 at the rail front ends, tub front face Y -37)

| Item | Where |
|---|---|
| Pickup (spindle axis) | X 200, Y -85. Y stop -88, so 3 to spare |
| Wheel centre | X 200, Y -174, vertical Ø20 shaft Z 80 to 171 |
| Pockets | 8 at 45°, pitch radius 89; the pickup pocket opens towards +Y |
| Forks (owner's model) | Z 166 to 176, V rib mid-plane Z 171; each trimmed to its 45° sector less 0.5 a side; 1 x M3 x 12 countersunk into the hub at r 41.7 |
| Hub | Ø101.5 x 12 6082, Z 159 to 171; the fork tabs sit on top, the fork steps against its edge |
| Holders (stand-in ISO20-ER16) | Ø45 flanges above and below the fork, groove shaped to the fork's 60° V (root Ø29.1), pull stud top Z 225, body to Z 130, tool to Z 85 |
| Wall block | 50 x 50 x 50 6082, X 175 to 225, Y -87 to -37, Z -10 to 40; 2 x M6 x 40 (counterbored) into the strip |
| Arms | 2 plates 10 x 78 x 182 on edge, X 165 to 175 and 225 to 235, Y -224 to -42, Z -10 to 68; 4 x M6 x 25 each into the block's sides |
| Motor plate | Ø120 x 10, Z 68 to 78, on the arms (4 x M5 x 20 into their top edges) |
| Top plate | Ø120 x 10, Z 115 to 125, on 2 Ø12 x 37 posts at X 157 and 243 (M6 x 16 each end) |
| Bearing | 1 x KFL004 on the top plate (Z 125 to 151), collar Z 151 to 159 |
| Drive | NEMA 17 closed loop (A03) face up under the motor plate, Z 0 to 68, between the arms; 4 x M3 x 10 in Ø4 holes (tighten last). Shaft bored Ø5 x 14, M4 grub onto the motor shaft |
| Index | LJ12A3 M12 (A09) through the top plate at 225°, r 44; flag under the hub |
| Cast in (Phase 1) | steel strip 25 x 10 x 50 in the floor's front face, X 187.5 to 212.5, Z -10 to 40, M6 at Z 0 and 30, Ø6.6 core 2 deep behind each hole (D-251, moved by D-253) |

Envelope: X 88 to 312, Y -286 to -37, Z -10 to 225. The lowest part is Z -10, 5 above the tub bottom. Aluminium and shaft: about 645 cm³ (about 1.8 kg).

## Tool change sequence
1. Drop-off: Z up, go to X 200, Y -55, nose down to Z 181 (in front of the tub; the tool tip is at Z 85, 45 above the wall block).
2. Slide -Y to Y -85: the holder's groove enters the empty pickup fork.
3. Release, lift the nose to Z 232 (holder top is Z 225). Index the wheel to the wanted pocket.
4. Pick-up: nose down to Z 181 over the holder, clamp, slide +Y to Y -55, Z up.

## Clash check (22 Nov 2026, after D-253 to D-255)
Copies of the Z axis bodies were moved by dX 421.8, dY -352 or -382, dZ 11 or 62 (approach, pickup, lifted at both Y) and intersected with every ATC body. At the approach a copy of holder 1 was also moved to Y -55.
- **Spindle against the wheel: no clash** with any fork, the hub or holders 2 to 8. The only hits are 2 Z-side bodies (both named `Body1`, not traced) with holder 1, the pocket that is empty at the drop-off and gripped at the pick-up.
- **ATC against the machine at rest: no clash.** The M6 x 40 screws sit in the strip.
- Inside the ATC: only screws in their tapped holes (not modelled as holes).
- Neighbouring forks: no overlap (1 mm apart). Forks against the hub and the holders: no overlap.

| Gap | mm | How found |
|---|---|---|
| Y pickup to the Y stop | 3 | model limits |
| Nose lifted (232) to the top of Z travel (245) | 13 | model limits |
| Nose lifted to the holder tops (225) | 7 | sizes |
| Nose (181) to the fork tops (176) | 5 | sizes |
| Tool tip (85) to the wall block top (40), pocket 1 and drop-off | 45 | sizes |
| Motor body to the arms | 4 each side | sizes |
| Neighbouring forks | 1 | model |

## Direct drive: what is and is not checked
- Torque is not the limit: the wheel only has to turn 45° and the holder slides in radially, so nothing turns it.
- **Tilt loads (not checked):** the KFL004 is self-aligning, so a vertical force at a fork (drawbar eject, clamp pull-up, a height mismatch) bends the Ø5 motor shaft at about 1.3 times that force.
- **Index error at the fork:** the closed-loop encoder is said to give 4000 counts per turn (not confirmed: the maker's page blocked curl). That is 0.09°, about 0.14 mm at r 89. The fork's snap mouth should take that up. Check on the bench.
- **Inertia:** the wheel with 8 holders is far heavier than the motor's rotor. Use a low acceleration in the ATC macro.
- **Rigid joint:** the motor's own bearings carry the lower end of the shaft. Line the motor up with the shaft before tightening its screws.
- **Motor length:** the model uses 68 body + 25 shaft. Measure the real motor. If it is longer than 78, it goes below the tub bottom.

## Not done or not known
- Holders, bearing, collar and motor are still stand-ins (D-252). The real ISO20 holder and the Jianken nose decide the 5 and 7 mm gaps.
- Fork screw: the fork hole is Ø3.8 with a Ø7.1 countersink. M3 or M4? The hub holes are tapped M3 for now.
- Tool length limit: under pocket 1 and the drop-off point is the wall block (top Z 40), 90 below the holder body; under the other pockets, only the bench. The arms and plates sit inside the ring of tools.
- The bench under the wheel is not modelled. The lowest ATC part is Z -10, so a flat bench top level with the tub bottom (Z -15) clears it.
- Fork seat: the hub is round, so each fork's flat step touches it at one point and only the M3 stops the fork turning. A hub with 8 flats (101.6 across) would seat the steps.
- The index flag (225°, r 44) is 2.3 from fork 4's M3 hole: move the flag or the sensor before making the hub.
- Strip cores now run Y -27 to -25 only (behind the strip); the old ones ran from -37. Draw them so on the mould drawing.
- A05 (tool setter) has no place yet.
- Bracket stiffness is not calculated. The motor plate now sits on two arms, not one.

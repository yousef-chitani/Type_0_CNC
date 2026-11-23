# Rear ATC: can the spindle reach it? (task 26, step 1; 23 Nov 2026)

**Answer: no.** The rear ATC is dropped and the front wheel is kept (D-288).

Figures come from `Type_0_v3` as it stands (not saved): body bounding boxes at one pose (Y slider at its rear limit, Z mid), plus hand sums. No moved-copy clash check was run. Every margin that decides the answer is 20 mm or more, so that is enough here.

## What is in the way (measured)
| Item | Value |
|---|---|
| Spindle axis Y reach | -88 to 297 (the spindle body at the rear limit is Y 257 to 337). D-233's -93 to 292 dates from before D-247 |
| Nose Z | 95 to 245 |
| Fixture plate | Y -37 to 293, top Z 70 |
| Tub | Y -37 to 653. Floor top **Z 45** all the way to Y 653. There is no rear wall: only the side walls, X ±310 to 390 |
| Z fixed plate | 120 to 140 behind the spindle axis, X ±75, underside **Z 169** |
| Z rails | 87 to 105 behind, X ±42 to 62, underside Z 169 |
| X roller bottom angle | 140 to 240 behind, X ±75, underside Z 169 |
| Z moving plate | 55 to 75 behind, X ±75, underside = nose + 45 |
| Gantry beam | 148 to 268 behind, full width X ±388, underside **Z 205**. It sweeps Y 60 to 565 |
| Y roller tubes | X ±312 to 388, 98 to 248 behind, Z 155 to 205 |
| X chain supports | up to 368 behind (Y 665 at the rear limit), Z 245 and up |
| Y motors | X ±319 to 484, Y 579 to 775, Z 149 to 211 |
| Y BK12 and risers | X ±320 to 380, Y 554 to 638; NEMA plate to Y 650 |
| The wheel as modelled at the front | 8 pockets at r 89, holders Ø45, holder tops Z 225, holders down to Z 130, tools to Z 85. Drive stack 171 from motor bottom to the fork plane (D-254) |

## 1. The rearmost wheel at the current Y travel
The pickup can be at Y 294 at most (3 inside the stop, as at the front). That is 1 behind the plate's back edge.

- **Wheel behind the pickup (spindle slides +Y into the fork):** the wheel centre is at Y 383. Measured from the pickup, the pockets sit 26, 89, 152 and 178 further back. The pockets 152 and 178 back sit under the Z fixed plate and X roller angle (Z 169) and under the beam (Z 205), and the holder tops are at Z 225. **They clash at the pickup itself**, so more Y travel cannot fix this.
- **Wheel beside the pickup (spindle slides along X):** at the pickup the carriage clears it. The Z rails clear by 1.5 and the moving plate by 1 above the holder tops. But the ring then covers Y 183 to 406, inside the beam's sweep (Y 60 to 565). The beam (Z 205) passes over the holder tops (Z 225) for almost every Y position. To keep clear of the right wall and the Y2 roller tube, the ring must stay at X 305 or less. That puts the pickup at about X 105, so the ring lies over the plate's back-right corner. There the tools (to Z 85, or to Z 60 if the wheel is lowered to clear the beam) and the plate (Z 70) are in each other's way, and that corner is lost for cutting.
- **Wheel in front of the pickup:** this is the front ATC.
- **The fixture plate:** in every rear layout at the current travel, the wheel sits over the back of the plate.
- **Y motors and BK12 risers:** they are not the problem. A ring centred on X 200 ends at X 311.5, and they start at X 319.

**The real limit is height, not reach.** Inside the tub, the carriage underside within ±75 of the spindle X is Z 169, and the beam underside is Z 205 everywhere. The floor is at Z 45. That leaves 124 for holder and tool together. The holder is 95 (pull stud to body bottom), so at most **about 25 of tool**, with no margin, and nothing at all over the plate (Z 70). A wheel lowered that far also loses the 171 drive stack: the motor would end below the floor, so the drive would have to be redesigned.

## 2. More Y travel: a wheel fully behind the plate
- **Inside the tub, behind the plate (Y 293 to 653):** a mirror of the front layout would put the pickup about 48 behind the plate edge (Y 341, +44 travel). It does not help: the height limit above holds for any Y inside the tub, because the gantry passes over all of it.
- **Past the tub end (Y 653), tools hanging past the floor edge:** the wheel still has to sit under the carriage (holder tops Z 165 or lower). The pickup tool must clear the floor edge, so the pickup is at Y 661 or more and the stop at about 664: **+367 of Y travel**. A wheel at full height would also need to be clear of the beam's sweep, which is impossible behind the pickup.
- **Room in the tub:** none. At the rear limit the Y blocks are about 1.2 from the rail ends, the BK12 risers start 2 behind the rails, and the NEMA plates end at Y 650, 3 from the tub end. Any extra travel means a longer tub. D-185 already turned down a 570 rail.
- **Lines that would change (not priced; the answer is no):** both Y rails (550 to about 920), both Y screws (650 to about 1020, and a whip check), the tub (690 to about 1060, plus mould, resin and aggregate), the Y cable chain, and the bench. The X chain supports and the Y motors also move back.

## 3. Result
A rear ATC is not feasible without either about 25 of tool stick-out, or a tub and Y axis about 370 longer. **Owner, 23 Nov 2026 (D-288): keep the front ATC, but it must be very elegant and integrated, not a kludge.**

What follows for the front (not done here):
- The D-251 and D-253 strip and the front keep-out (X 88 to 312) apply again. The strip goes on the mould drawing.
- The front slot (D-236, D-273) may be up to X ±107.5 wide, and the ATC keep-out starts at X 88. The two overlap by 19.5. This is the next thing to settle.
- D-250, D-253 and D-255 (the parts proposed by Claude) are still unconfirmed. They now need checking against the owner's "elegant, integrated" requirement.

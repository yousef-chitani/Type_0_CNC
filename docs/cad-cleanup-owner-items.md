# CAD clean-up: what needs the owner (22 Nov 2026, D-261)

`Type_0_v3` was searched by script for visible screws that clamp nothing and for holes with no screw. 26 screws were removed and 15 holes filled (D-261). The model is saved.

## 1. Missing screws: holes that line up in two parts, but no screw is modelled
These are real joints, so the holes stay. Should Claude model the screws (and add any missing ones to `bom.csv`)?

| Joint | Holes | Note |
|---|---|---|
| Motor to NEMA 24 plate (X, Y, Y2) | 4 each | vendor motor holes |
| NEMA 24 plate to BKHM12 riser (X, Y, Y2) | 3 each, counterbored | |
| BK12 to riser (Y, Y2) | 2 each, at Y 579 and 592 | |
| Y roller brace to Y roller tube (both sides) | 4 each, Z 407/427 | the PrintNC M6 x 12 set for these is hidden |
| Y roller brace to X gantry tube (both sides) | 4 each, Z 223/268 | |
| Y roller tube to X gantry tube (both sides) | 5 each, Y 480/505/530 | |
| X roller bottom angle to Z fixed plate | 5, Z 182/206 | |
| X roller top angle to Z fixed plate | 4, Z 374/398 | |
| HM12 to Z fixed plate | 6 | |
| Z moving plate to the Z HGH20 blocks | 16, counterbored M5 | the blocks sit about 7 behind the plate's back face: check the stack |
| Steel plate hold-downs to the wall bar (D-257, X19) | 10 per wall | M6 x 20 countersunk |
| Cable zip-tie plates to chain supports | 2 each, 4 plates | |
| KFL004 bearing to ATC top plate | 2 (M10) | |

## 2. Holes Claude could not place
- X gantry tube: a Ø16 hole along X at Y 549, Z 309. Clearance for something, or a leftover?
- Y cable chain support: a Ø10 hole along X at Y 220, Z 39. Cable hole or leftover?
- X roller tube: 2 M5 holes (X -254 and -190, Z 372) sit 2 below the top angle's holes (Z 374). A leftover from before D-216, or is the angle 2 out?

## 3. Other things seen
- 373 hidden PrintNC fastener bodies stay in the model (owner: visible only). They can go later.
- The X 1610 fill plate and nut plate (PrintNC parts) are still visible. Are they used with the DFU1605 nuts?
- X gantry trigger mount: its M6 x 20 is 2.5 short of the tube face.
- ATC bracket print (D-260): 80 x 187 x 93 overall. Check that it fits your printer bed.

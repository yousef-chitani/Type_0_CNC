# CAD clean-up: what needs the owner (22 Nov 2026, D-261)

`Type_0_v3` was searched by script for visible screws that clamp nothing and for holes with no screw. 26 screws were removed and 15 holes filled (D-261). The model is saved.

## 1. Missing screws: done (D-262)
112 screws and 2 nuts are modelled in `Joint screws added (D-262)` (sizes in D-262; new ones in BOM line X21). Three things follow from them:
- Done (D-263): the BK12 riser holes (all 4 per riser) are now tapped M6 x 22, and the NEMA 24 plate motor holes tapped M5 through.
- Thread lengths are short in the 3 mm Y roller tube walls (M6 x 12 gets 3 of thread, as PrintNC does).

## 2. Holes Claude could not place
**Closed (D-266, 23 Nov 2026):** the 2 M5 tube holes are filled. The Ø16 is the tube's R8 inside corner and the Ø10 is the zip-tie channel under the chain support (now at Z 33): neither is a hole, both left.
- X gantry tube: a Ø16 hole along X at Y 549, Z 309. Clearance for something, or a leftover?
- Y cable chain support: a Ø10 hole along X at Y 220, Z 39. Cable hole or leftover?
- X roller tube: 2 M5 holes (X -254 and -190, Z 372) sit 2 below the top angle's holes (Z 374). A leftover from before D-216, or is the angle 2 out?

## 3. Other things seen
- 373 hidden PrintNC fastener bodies stay in the model (owner: visible only). They can go later.
- The X 1610 fill plate and nut plate (PrintNC parts) are still visible. Are they used with the DFU1605 nuts?
- X gantry trigger mount: its M6 x 20 is 2.5 short of the tube face. **Done (D-280): the mount was 46 below the X sensor; now 45 taller, screw up 45.**
- ATC bracket print (D-260): 80 x 187 x 93 overall. Check that it fits your printer bed.

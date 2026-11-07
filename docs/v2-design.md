# Type 0 v2: flat-sized design notes

Model: [`cad/v2/type0_v2.py`](../cad/v2/type0_v2.py) → `cad/v2/out/type0_v2.step`. Numbers: [dimensions_v2.md](../cad/v2/out/dimensions_v2.md). Concept sketches: `cad/v2/out/sketch_top.png`, `sketch_front.png`.

## Brief (D-71, D-73)
- Upstairs flat. Every piece ≤ 40 kg. Machine about 120–130 kg plus enclosure, on 4 anti-vibration feet on the owner's timber bench (top 785 mm above the floor).
- **Work area 400 × 250 (D-79).** Travel X 570 (400 work + reach to the ATC wheel), Y 250, Z 150. Table 460 × 330 × 25. Y rails 280 apart on a 320 spine (D-80).
- 2 solid epoxy-granite castings (D-76), with capped PVC cores in the portal beam (D-74): base about 72 kg (2-person lift, FEA to trim later: D-81), portal about 34 kg.

## Joints
**Base: one casting (D-76).** The spine and rear cross-piece are cast as one T-shaped base, about 52 kg (a 2-person lift). There is no frame joint, so the gantry's squareness to Y is set by the casting and the grout layer under the portal legs.

**Portal → base (the only frame joint).** Each leg sits on the base's rear cross-piece. First assembly: shim the portal square to the Y rails, grout, cure, then ream for the dowels. 2 × M12 bolts per leg through cast sleeves into tapped insert bars in the base, plus 1 × Ø10 dowel per leg.

## ATC wheel (Phase 3, D-73)
- Ferris wheel, about Ø178, 8 ISO20 pockets (3D-printed forks, D-58), turning about an X axis in the Y–Z plane beside the right leg, under the beam overhang.
- Mount: a steel/aluminium bracket bolted to the leg's outer face (cast-in insert bar, 2 × M8) carrying a Ø20 shaft on 2 bearings.
- Drive: small closed-loop NEMA 17 (A03) through a belt reduction (about 3:1) or worm. Index: inductive sensor on the wheel hub plus a home flag. LinuxCNC drives it as a rotary joint.
- Pickup = top pocket, at X 280, Y 0, fork plane Z 95. The spindle approaches from above along Z.
- **Holder orientation:** with a true ferris wheel the holders must stay upright (pivoting gondolas) or the pockets must face radially with the top one vertical. Use radial pockets: only the top pocket needs to be vertical, and gravity holds each holder in its fork up to ±90° from the top. **Check this on a printed mock-up**, since holders at the bottom would fall out without a retaining clip.

## Things to check next
- Y screw nut housing under the table (DSG16H: centre 20 mm below its face, 40 mm tall). The table underside is at Z 30 → cast a 70 × 25 mm channel along the spine (as D-56).
- Z assembly height: Z plate top at about Z 585 at Z-top. The enclosure needs about 650 mm internal height above the castings.
- The portal beam overhang (160 mm) with the saddle at the pickup: check deflection when the gantry is detailed.

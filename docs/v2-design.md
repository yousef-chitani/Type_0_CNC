# Type 0 v2: flat-sized design notes

Model: [`cad/v2/type0_v2.py`](../cad/v2/type0_v2.py) → `cad/v2/out/type0_v2.step`. Numbers: [dimensions_v2.md](../cad/v2/out/dimensions_v2.md). Concept sketches: `cad/v2/out/sketch_top.png`, `sketch_front.png`.

## Brief (D-71, D-73)
- Upstairs flat. Every piece ≤ 40 kg. Machine about 120–130 kg plus enclosure, on 4 anti-vibration feet on the owner's timber bench (top 785 mm above the floor).
- **Work area 400 × 250 (D-79).** Travel X 570 (400 work + reach to the ATC wheel), Y 250, Z 150. Table 460 × 330 × 25. Y rails 280 apart on a 320 spine (D-80).
- 2 solid epoxy-granite castings (D-76), with one 68 mm downpipe core in the portal beam (D-95): base about 72 kg (2-person lift, FEA to trim later: D-81), portal about 39.6 kg (beam 150 tall, X rails 100 apart: D-94).

## Joints
**Base: one casting (D-76).** The spine and rear cross-piece are cast as one T-shaped base, about 52 kg (a 2-person lift). There is no frame joint, so the gantry's squareness to Y is set by the casting and the grout layer under the portal legs.

**Portal → base (the only frame joint).** Each leg sits on the base's rear cross-piece. First assembly: shim the portal square to the Y rails, grout, cure. 2 × M12 studs per leg, screwed into couplers cast in the leg feet, drop through sleeves in the base and are nutted underneath (D-96; replaces the full-height sleeves, which crossed the beam core). **Relocation feature (dowels or other) still open:** see moulds.md.

## ATC wheel (Phase 2, D-73/D-86)
- Ferris wheel, about Ø178, 8 ISO20 pockets (3D-printed forks, D-58), turning about an X axis in the Y–Z plane beside the right leg, under the beam overhang.
- Mount: a steel/aluminium bracket bolted to the leg's outer face (cast-in insert bar, 2 × M8) carrying a Ø20 shaft on 2 bearings.
- Drive: small closed-loop NEMA 17 (A03) through a belt reduction (about 3:1) or worm. Index: inductive sensor on the wheel hub plus a home flag. LinuxCNC drives it as a rotary joint.
- Pickup = top pocket, at X 280, Y 0, fork plane Z 95. The spindle approaches from above along Z.
- **Holder orientation:** with a true ferris wheel the holders must stay upright (pivoting gondolas) or the pockets must face radially with the top one vertical. Use radial pockets: only the top pocket needs to be vertical, and gravity holds each holder in its fork up to ±90° from the top. **Check this on a printed mock-up**, since holders at the bottom would fall out without a retaining clip.

## Moulds, bench, mix (tasks 3–5)
Mould drawings: [moulds.md](moulds.md). Bench: [bench.md](bench.md). EG mix and test bricks: [eg-mix.md](eg-mix.md).

## Things to check next
- Y screw nut housing under the table (DSG16H: centre 20 mm below its face, 40 mm tall). The table underside is at Z 30 → cast a 70 × 25 mm channel along the spine (as D-56).
- Z assembly height: Z plate top at about Z 585 at Z-top. The enclosure needs about 650 mm internal height above the castings.
- The portal beam overhang (160 mm) with the saddle at the pickup: check deflection when the gantry is detailed.
- **X motor overhang:** the X motor sticks out about 170 mm past the beam's right end. The enclosure below must grow to about 1,030 inside (open question). The bench is already 1,100 wide (D-97).

## Enclosure (D-87)
**Too narrow for the X motor (open question 15):** widen to about 1,030 internal. See `cad/v2/out/enclosure_cutlist.md` and `enclosure_front.png` / `enclosure_side.png`. 12 mm MDF box, internal 880 × 930 × 742, sits on the bench (not on the castings), top-hinged front door with a low twinwall window, cable/hose slot in the back. Model: `cad/v2/enclosure.py` → `type0_v2_with_enclosure.step`.

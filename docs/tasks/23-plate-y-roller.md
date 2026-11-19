# Task 23: Plate Y roller (`mod-y-roller`) fitted to Type 0

**Who:** main session (Fusion MCP). **Read only:** this file, D-218 … D-221 in `docs/decisions.md`.

The owner's open plate Y roller is the Fusion document `mod-y-roller` (project "CNC mill"). It replaces the PrintNC tube Y roller later; it is not in `Type_0_v3` yet.

## Done (19 Nov 2026, not saved: the owner saves)
- Parameters: `gantry_width` 120, `gantry_height` 120, `steel_radius` 16, `gantry_rail_distance` 62.5 (d38 = it − 12.5), `ballscrew_rail_distance` 37.5, `ballscrew_bolthole` 4.2 (M5 tap). Rail extrude d13 17.5.
- Blocks: HGH20CA, d1 44, d5 32/2, d8 36, d6 5.5; bottom plate counterbore d25 10; plate edge offsets d23, d24 11.5 (75 wide). Components renamed `HGH20CA`, `HGR20 rail`.
- Front plate sketch: tab corners moved in to the plate width; beam bolt rows d78 22 (Z 102 and 155).
- Side holes: 7 holes that drifted after the change pinned with new dimensions d189 … d192.
- Nut: component `DFU1605 double nut`, 100 long (d68 −90).
- Sensor: link broken (timeline group "limit-sensor-y M12 (link broken)"), `sensorHoleSize` 12.5, `sensorPlateSize` 24. Its cosmetic Chamfer14 failed and is suppressed.

## Checked
- No clash between any two bodies (coincident faces excluded).
- Heights in the model's frame (rail base Z 0): block top 30, beam bottom 80, screw centre 55; same as `Type_0_v3` (155, 205, 180).
- Sensor holes line up with the front plate's 2 tapped holes.
- Timeline: same states as before plus `sideholes` warning (2 projections use cache) and the sensor group (suppressed chamfer). Before: Extrude7 rolled back, CutPasteBodies1 suppressed.

## Bottom plate audit (19 Nov 2026, measured in `mod-y-roller`, component frame: X across, block centre X 22; Y along; Z up, rail base 0)
Plate X −5.5 … 49.5, Y −38.82 … 126.18, Z 30 … 45. Screw axis X 22, Z 55. Nut flange Y −36.32 … −26.32 (in front of the front plate), flats at Z 35 and 75.
1. **End slots** (10 deep, Y −26.32 … −16.32 and 103.68 … 113.68) leave small tabs and 46° faces at the corners and trap the outer block screws (D-221).
2. **Ø48 trough** along the full length, flat floor Z 35 (5 mm floor). The Ø10 block counterbores (X 6 and 38) and the Ø6.5 side holes (Z 37.5) break into it as half-moons.
3. **Front ledge** under the nut flange: Ø54 pocket, floor Z 32 (2 mm floor), 2.4 mm side walls.
4. **Block counterbores** 2.8 deep (Z 40 … 42.83), not the 7.5 of D-221; the seat at X 6 is partly gone into the trough.
5. **Side holes** Ø6.5 clearance in both the side plate and the bottom plate (no thread); 15 deep on the left, 10 on the right.
6. **Nut model** body Ø31; the supplier table (`cad/vendor/drawings/dfu_din69051_form_b_table.webp`, DFU01605-4) gives D 28, A 48, H 40, W 38, X 5.5.
7. **Flange bolts vs D-221:** with the front plate on Z 45, the 2 lower flange holes (Z 41.56) fall below the plate, onto the front block-screw counterbores (X 6/38, Y −18.07).
8. **Back plate** carries a copy of the nut hole and 6 tapped holes it does not need.

Geometry limit: block screws 32 apart with Ø10 counterbores leave 22 between them; the nut is Ø28. A round trough on the screw axis misses the counterbores only below Ø29.7.

## Fixed (19 Nov 2026, D-221 … D-225, not saved: the owner saves)
- Old bottom-plate cuts suppressed: Combine1, Extrude3, Extrude4, Extrude8, Extrude9 (nut and front-plate cuts) and Combine2–4 (end slots). Extrude2 counterbores now 7.5 deep (D-221).
- New features at the end of the timeline, named `BP …`: front cut to Y −26.32, Ø32 nut trough, old Ø6.5 side holes filled, M6 tapped (Ø5.0, 12 deep) both sides with threads.
- Front and back plates cut to start at Z 45 (`… bottom to Z45`); nut hole is now an open notch at the bottom; side-screw rows at Z 82, 118, 140, 167 (`sideholes` d191 52, d185 27, d186 22); old Ø5.5 holes filled and tapped M5 (Ø4.2, 12 deep) with threads.
- Side plates: unused front hole (Y −28.82) filled (`SP fill unused front hole`).
- Nut: body cut to Ø28 (`nut body to d28`).
- Checked: no interference between any bodies; no face under 3 mm² on any plate; timeline as before (sensor group, Extrude7) and the `sideholes` warning gone.

## Left, in order
1. **Side plate front strip:** the Ø9 counterbores for the front/back plate screws (Y −21.32 and 108.68) leave 0.5 mm to the beam opening (it starts at Y −16.32 and 103.68). Was the same before. Owner to choose: no counterbore (heads proud 5) or low heads, or a wider strip.
2. The back plate still has the 4 upper nut-flange tapped holes it does not need (harmless). The nut model keeps a 0.004 mm Ø31 step at the flange (from the original nut sketch).
3. The sensor mount stands 20 off the front plate and sticks 70 out past the roller end. Check it against the Y BF12 and the travel end when fitting into `Type_0_v3`.
4. Unpriced: the 6082 plates (bottom 15, sides, front, back 10), M5 x 12 (block), M6 (bottom plate) and M5 (front/back) side screws. Not in `docs/bom.csv`.
5. Fit the roller into `Type_0_v3` (next task): block centres there are Y 427.5 and 512.5 (pitch 85, here 87.5); beam moves 35 forward (D-220).

**Exact next step:** the owner checks and saves `mod-y-roller`, and answers item 1.

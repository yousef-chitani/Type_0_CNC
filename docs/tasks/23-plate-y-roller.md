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

## Left, in order
1. **Drop the 10-deep slots under the front and back plates (D-221).** Plates sit on the bottom plate's top face (Z 45). Block counterbores 7.5 deep. Then re-run the clash check with M5 x 12 screws modelled.
2. Fix the `sideholes` projection warning (re-project the 2 lost edges).
3. The sensor mount stands 20 off the front plate (joint offset, as the original) and sticks 70 out past the roller end. Check it against the Y BF12 and the travel end when fitting into `Type_0_v3`.
4. Unpriced: the 6082 plates (bottom 15, sides, front, back 10) and M5 x 12. Not in `docs/bom.csv`.
5. Fit the roller into `Type_0_v3` (next task): block centres there are Y 427.5 and 512.5 (pitch 85, here 87.5); beam moves 35 forward (D-220).

**Exact next step:** the owner checks and saves `mod-y-roller`. Then a new session does step 1.

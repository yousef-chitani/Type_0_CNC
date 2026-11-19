# Task 23: Plate Y roller (`mod-y-roller`) fitted to Type 0

**Who:** main session (Fusion MCP). **Read only:** this file, D-218 … D-221 in `docs/decisions.md`.

The owner's open plate Y roller is the Fusion document `mod-y-roller` (project "CNC mill"). It replaces the PrintNC tube Y roller later; it is not in `Type_0_v3` yet.

## Front plate into the side plates (D-228, 19 Nov 2026, `mod-y-roller`, not saved)
The open `mod-y-roller` was its saved state: none of D-221 … D-225 (front plate down to Z 36 in a slot, HGW20CC blocks, nut axis Z 56, beam bottom Z 82). The owner chose to work from it. Frame here: front plate Y −26.324 … −16.324, back plate Y 103.676 … 113.676 (all Y values carry −0.004).

**Conflicts found:** the bottom plate's cross bolts (Ø6.5 along X, Y −28.824 / 116.176, Z 37.5) cut 0.75 into the front/back plates; the side-screw row Z 46 cut slivers off the bottom plate (3 loose bodies); row Z 169 ran into the beam-bolt counterbores; the outer block screws sat under the plates.

**Done (features `FX …` at the end of the timeline, root sketches and planes named `FX …`):**
- Front and back plates: old side holes (Z 46, 87, 128, 169) and the 2 lower flange holes filled; plates cut to start at Z 45; M5 tapped Ø4.2, 13 deep from each edge, at Z 70, 87, 128, 150; beam-bolt holes at Z 164 recut (Ø6.5 + Ø10.5 cbore 5 deep).
- Side plates (both): rows Z 46 and 169 filled; new Ø5.5 + Ø9 cbore 5 deep at Z 70 and 150 (Z 87 and 128 kept).
- Bottom plate: end slots filled outside the Ø48 trough (the 3 loose bodies merged); outer block-screw holes recut, counterbores Ø10.6 x 6.5 deep (Z 38.5); cross-bolt holes recut Ø6.6.

**Not finished (stopped at the context limit):**
1. `FX cross bolt holes X5.5` fails ("No target body"; it hit ASM_EDGECOIN when the Y values were corrected by −0.004). Fix: roll back to it, set its participant body to the bottom plate, or delete it and recut Ø6.6 from X −2.5 to 13.5. Its sketch circles are already Ø6.6; its symmetric distance is 16.
2. After the full recompute, the bottom plate volume rose from 99,745 to 106,252 mm³ and its faces fell from 110 to 98. Find which cut is missing (compare with the holes listed above); the outer block-screw sketch may still be Ø6.5 / Ø10.5 (a radius change failed).
3. Then: interference check with stand-in screws (block M6 heads under the plates, M5 x 16 side screws, cross bolts), no face under 0.01 mm² on any plate, screenshot.
4. Leftover seam faces of 0.0001 mm² at the plates' bottom edge (old flange holes) and 0.0096 mm² at the back plate's Z 164 cbores: harmless, clean if wanted.

## Remake: `y-roller-10` (D-226, D-227, 19 Nov 2026)
New Fusion document `y-roller-10` (project "CNC mill"). `mod-y-roller` below is history.

**Frame:** X across (rail centre 0, +X toward the machine), Y along the rail (roller centre 0, front = −Y, nut end), Z up (rail base 0). Fixed heights (D-218): block top 30, screw axis 55, beam bottom 80.

| Part (qty) | Size | Place |
|---|---|---|
| Base plate (1) | 75 x 140 x 10 | X ±37.5, Y ±70, Z 30 … 40 |
| Side plate (2, identical) | 120 x 40 x 10 | X ±27.5 … ±37.5, Y ±60, Z 40 … 80; beam sits on top |
| End plate (2, identical) | 75 x 137 x 10 | X ±37.5, Y ±60 … ±70, Z 40 … 177; Ø29 notch on the screw axis, open at the bottom |

**Holes** (all M5 tapped Ø4.2, clearance Ø5.5, head counterbore Ø10):
- Base, block screws: 8 x M5 x 10 at X ±16, Y ±24.5 and ±60.5, counterbore 5.5 deep from the top (5.5 in the 6-deep block thread). Fit before the end plates.
- Base, from below: M5 x 16 into the side plates (X ±32.5, Y 0 and ±40) and the end plates (X ±32.5, Y ±65), plain Ø5.5 holes, heads under the plate beside the block (Z 25 … 30), tapped 10 in the plates (6 engaged). No counterbore: a Ø10 counterbore at X ±32.5 breaks out at the plate edge.
- End plate into the side-plate ends: M5 x 20 at X ±32.5, Z 60 and 72, tapped 12 in the side plate.
- Nut flange (front plate; back plate has the same holes, unused): M5 tapped through at (X ±19, Z 55) and (X ±13.4, Z 68.4), 4 x M5 x 20 (D-222).
- Beam: M6 clearance Ø6.5 at X ±25, Z 102 and 155, tapped M6 in the beam wall.
- Sensor mount: M6 tapped Ø5.0 at X 0, Z 102 and 127.5.

**Built (19 Nov 2026, document `Untitled`, not saved: the owner saves it as `y-roller-10` in "CNC mill").** Components: Base plate, Side plate (2 occurrences of one component), End plate (2 occurrences of one component), Hardware (HGR20 rail, 2 x HGH20CA with 6-deep M5 threads, beam SHS 120 x 120 x 8 R16 with M6 taps, DFU1605 double nut Ø28 x 100 with flange Ø48 / 40 flats, ball screw Ø16), Screws (38 bodies: head, shank, real length). STEP: `cad/v2/out/y_roller_10.step`. The sensor bracket is not modelled.

**Checked:**
- Interference across all 49 bodies, screws included: none. All features healthy.
- Every screw reaches its thread: block screws 5.5 into the 6-deep block thread; base screws 6 into side/end plates; end-to-side screws 10; flange screws 10 (tapped through); beam M6 6 into the 8 wall.
- Walls: hole to hole at least 7.8 in the side plates and 9.3 in the base; edge holes 2.9 from the plate faces (M5 tapped in 10). End plate: flange tapped holes 2.35 from the Ø29 nut bore (fixed by the DIN flange, PCD 38); side-screw clearance holes 2.25 from the plate's side edge.
- Key access: the 8 block screws are covered by the nut, beam and end plates. Fitting order (built in place on the rail): side plates to the base on the bench (6 screws from below), base onto the blocks (8 block screws from the top), end plates (4 screws from below, then 4 into the side-plate ends), nut through the front notch, flange screws, beam on top, beam bolts. **Not verified:** the 4 end-plate screws are driven from below with 25 mm between the head and the rail seat (Z 0), and nothing below the plate is modelled; check in `Type_0_v3`. All other heads are clear along their axis.

**Calls made in the build (owner to confirm):** base screws without counterbores (above); beam bolts at X ±25 with plain Ø6.5 holes (heads proud 6, no thin counterbore floor); the Ø29 nut bore is an open notch to the plate bottom (a closed bore leaves 0.5 mm); end-to-side screw rows at Z 60 and 72, clear of the base screws; beam bolts tapped M6 straight into the 8 mm tube wall (6 engaged); block screws M5 x 10 leave 0.5 mm before they bottom in the 6-deep thread (D-221 had 1.5).

**Left (new roller):** owner saves; check the heads under the base plate and the end-plate heads against the tub and the Y BF12 in `Type_0_v3`; model the sensor bracket; price the plates and M5 x 10 (8), M5 x 16 (10), M5 x 20 (12), M6 x 16 (8); then fit into `Type_0_v3`.


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

# Type 0 CNC: handover archive

Older entries moved unchanged from `docs/HANDOVER.md` on 18 Nov 2026, newest first. Much of this describes superseded designs: `docs/decisions.md` and the current `docs/HANDOVER.md` take priority.

## 0000000000000000000000000000000000000000. 18 Nov 2026: Z fixed plate modelled (D-191)

**Done:** the owner saved `Type_0_v3` as version 5. The new component `Z Fixed Plate` is 150 wide, 350 high and 20 thick, at X -297.5 to -147.5, Y 417 to 437, Z 169 to 519, held to the bottom X roller by a rigid as-built joint. It has 9 holes, 6.6 clearance with counterbores 10.5 × 6.5 deep (D-191). Measured: all 9 hole axes match the roller and shim holes, the back face touches the bottom roller and the shim, and the next nearest parts are 8 away. The plate is flush with the roller sides, so it does not shorten X travel. Timeline 1243, 1 error and 5 warnings, the same failures as version 1. No material is assigned to the body. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Z risers and rails.** 15 risers and HGR20 rails on the plate, then the blocks, moving plate, screw and motor.
2. **Roller screws.** M6 × 20 for the 5 bottom holes and M6 × 25 for the 4 top holes. Not in `docs/bom.csv`, no live price yet. The top screws thread into only 3 of tube wall: check this.
3. **Table top height.** D-191 assumes Z 70, from the hidden wasteboard. Confirm it when the table is modelled.
4. **Plate stiffness** is not checked (D-184).
5. **Front Y riser bolts** at X -305 and 305 sit outside the risers (already wrong, not moved). The tub needs drilling for the new Y 629 bolts.
6. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, add the 15 risers and HGR20 rails to `Z Fixed Plate`. Re-count errors and warnings after every write.

## 000000000000000000000000000000000000000. 18 Nov 2026: X riser side holes moved, motor length and plate screws settled (D-189, D-190)

**Done:** owner saved `Type_0_v3` as version 4 with D-186 and D-187. After that, the two M4 side holes in the X riser moved from X 375.5 to X 369.5 (D-189), with the pan head screw. Timeline 1235, 1 error and 5 warnings, the same failures as version 1. The datasheet confirms the motor: body 122, shaft 21, against 125 and 20 in the STEP, which stays in the model. Motor plate screws are in `docs/bom.csv` as X11: Drenky A2 M6 x 16 socket cap, pack of 20, £5.99 from Amazon (D-190). Phase 1 is now £3,963.41, £236.59 left. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Front Y riser bolts** at X -305 and 305 sit outside the risers (already wrong, not moved). The tub needs drilling for the new Y 629 bolts.
2. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.
3. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, start the Z plate (D-179, D-184). Re-count errors and warnings after every write.

## 00000000000000000000000000000000000000. 18 Nov 2026: motor plates moved, risers shortened (D-186, D-187)

**Done:** in `Type_0_v3` the motor plates on X, Y and Y2 moved 12 towards the screws, the motors moved with them and the couplings moved 6. The BK12 risers are 12 shorter, their rear bolts moved 12 forward, and the X gantry tube holes moved to match. Measured: 12.9 of grip per shaft, 1.6 from coupling to BK12, Y motor rear at Y 775, X motor rear at X 515. Timeline 1230, 1 error and 5 warnings, the same failures as version 1. Details are in `docs/printnc-assessment.md`. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Motor plate bolts: M6 x 16 chosen (D-188), 9 needed.** Not yet in `docs/bom.csv`. Screwfix and RS blocked curl on 18 Nov, so the owner needs to give a live price.
2. **X riser side holes.** The two 4 mm holes at X 375.5 leave 0.5 of wall to the new end face. Decide whether to move them.
3. **Front Y riser bolts** at X -305 and 305 sit outside the risers (already wrong, not moved). The tub needs drilling for the new Y 629 bolts.
4. **Motor length, owner to confirm.** The STEP is named `24HE40-5004D-E1000` and gives a 125 body. No datasheet for it is in `cad/vendor/`.
5. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.
6. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, start the Z plate (D-179, D-184). Re-count errors and warnings after every write.

## 0000000000000000000000000000000000000. 18 Nov 2026: DFU1605 nuts, 24HS40 motors and couplings fitted

**Done:** the owner saved `Type_0_v3` as version 2 with the rails shifted. After that, DFU1605 nuts, 24HS40 motors and stand-in D25L35 couplings went in on X, Y and Y2, and the parts they replace are hidden. Timeline 1205, 1 error and 5 warnings, the same failures as version 1. Y motor rear is 134 behind the tub (D-142 allows about 185). The nut-to-BF12 gap stays 4.7. Details are in `docs/printnc-assessment.md`. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Coupling grip: decided (D-186), not yet modelled.** Move the motor plates on X, Y and Y2 12 towards the screws, with the motors and couplings. Shorten the Y risers and the matching X part by 12. Expected result: 12.9 of grip per shaft, 1.6 from coupling to BK12, Y motor rear at Y 775.
2. **Motor length, owner to confirm.** The STEP is named `24HE40-5004D-E1000` and gives a 125 body. No datasheet for it is in `cad/vendor/`.
3. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.
4. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, find what locates the `Nema24 Plate` on each axis and apply D-186. Re-count errors and warnings and re-measure the grip and gaps, then start the Z plate.

## 000000000000000000000000000000000000. 18 Nov 2026: Y rails shifted, Y travel measured

**Done:** both Y rails in the open `Type_0_v3` now run Y 2.5 to 552.5, clear of the risers, and all 9 holes on each rail line up with the frame holes. The rail body was tied to the `YFrame` end face, so the frame hole (`d80`) and the rail end (`d196`) had to move together (`docs/printnc-assessment.md`). Y travel is 386.2 on the rails (Type 0 needs 350). At both ends of the 385 slider range the tightest measured gaps are 0.61 from block to rail end and 1.61 from block to riser. The gantry, trigger mount, sensor mount and cable chain supports moved with the rails; the last three still need reviewing. Timeline 1183, 1 error and 5 warnings, the same failures as version 1. **The document is modified and not saved. The owner saves it.**

**Left:** the imported parts, then the Z axis. Rules for model edits: re-count errors and warnings after every write and undo any edit that raises them; hide parts, never delete them; list each change in `docs/printnc-assessment.md`; do not save through the tool.
1. **Imported parts (D-180, D-182).** DFU1605 nut and 24HS40 motor from `cad/vendor/`, and a D25L35 coupling. Take the motor length from the datasheet, because the STEP includes other geometry. This gives the X motor overhang and the Y motor overhang against the 185 in D-142. Re-check the nut against the BF12: the SFU1610 nut stops 4.7 away and the DFU1605 is longer.
2. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, after the owner has saved `Type_0_v3`, import the DFU1605 nut from `cad/vendor/` on the Y axis and re-run the Y travel check.

## 00000000000000000000000000000000000. 18 Nov 2026: Y motors at the back, Y rails still to shift

**Done:** D-184 (Z plate: 6082 in Phase 1 then steel, 15 risers stay, 350 high) and D-185 (Y stays 550 rail, 650 screw, 690 tub). In the open `Type_0_v3`: BK12 supports and NEMA 24 plates shown on X, Y and Y2, and the Y risers, screws and motors turned end for end, with the motors at the back on both sides. Timeline 1183, 1 error and 5 warnings, the same failures as version 1. **The document is modified and not saved. The owner saves it.**

**Left:** the Y rails still run Y 64 to 614 and overlap the BK12 risers by 60.5. They should run Y 2.5 to 552.5. The 386 travel is worked out, and must be measured once the rails are in place. Then item 3 and item 4 in the next entry (D-184 unblocks item 4).

**Do not repeat:** a `Rigid 2` offset moves the rail in Z. Re-pointing `Rigid 2` at a sketch point leaves the rail body behind and throws the Y2 drive 61.5 out. Both are in `docs/printnc-assessment.md`.

**Exact next step:** in a new session, find out why the `Y HGR20` body stays at Y 64 to 614 when its occurrence moves (start with `MoveFace2`, `Base Feature1` and `Rigid Group 247`). Then shift both Y rails 61.5 forward, keeping the 1 error and 5 warnings, and re-measure the travel.

## 0000000000000000000000000000000000. 18 Nov 2026: model update planned, not started

**Done:** the owner saved the model as `Type_0_v3` version 1 (CNC mill project, 1 error and 5 warnings, 1182 timeline items) and allowed changes beyond parameters for D-179 to D-182 (D-183). No change has been made to the model. The session stopped at the context limit.

**Left, in this order.** Re-count errors and warnings after every write and undo any edit that raises them. Hide parts, never delete them, and list each change in `docs/printnc-assessment.md`. Do not save through the tool: tell the owner the document is modified.
1. **Supports (D-180), visibility only.** For X, Y and Y2: hide `HM12-57` and the `HM12 M6x50` fasteners, show the hidden `BK12` and `Nema24 Plate`. The timeline should stay at 1182.
2. **Y motors to the back (D-181).** Root joints `Rigid 311` (BF12 riser to YFrame) and `Rigid 312` (BKHM12 riser to YFrame) locate the risers, and the BK12, motor plates, screw and motor chain off them. Y2 has a `Derived Base Feature1`, so check whether it follows or needs its own edit. Confirm which Y direction is the rear first. Then check the riser fasteners, the 3 gap at each tub end (D-175) and the motor overhang against the 185 in D-142.
3. **Imported parts (D-180, D-182).** DFU1605 nut and 24HS40 motor from `cad/vendor/`, and a D25L35 coupling. Take the motor length from the datasheet, because the STEP includes other geometry. This gives the X motor overhang.
4. **Z axis (D-179): blocked.** The owner must first choose the plate material (steel or 6082), whether the 15 risers stay, and the plate height.

**Exact next step:** in a new session, ask the owner the three Z plate questions, then start at item 1.

## 000000000000000000000000000000000. 18 Nov 2026: Z axis and drive chosen

**Done:** owner chose the Type 0 Z on a new 150 wide plate (D-179), DFU1605 and NEMA 24 on X and Y (D-180), Y motors at the back (D-181) and the X motor in line past the beam end, no belt (D-182). `docs/bom.csv`: M15, M16 and M17 dropped, M08 now 4 couplings. Phase 1 priced total **£3,957.42, £242.58 left**. X now uses the standard BK12 end, so no stub drawing is needed.

**Left:** the Fusion model was not changed and still shows the PrintNC Z, SFU1610, NEMA 23 and the Y motors at the front. D-179 to D-182 cannot be modelled by parameters alone: there is no parameter for the Y motor end, and the new Z plate, nuts, motors and supports are different parts. D-172 says parameters only, so the owner must say whether the model may go beyond that. The document is **unsaved** with **6 failing features** (1 error, 5 warnings). The owner must add a fourth D25L35 to the LiMo basket. Not checked: X motor length past the beam end, the X motor mount, the X screw length, clashes over the full travel. Availability and price of 120 × 120 × 8 and the LiMo prices for the 550 rail and 650 screws are not confirmed.

**Exact next step:** the owner saves the Fusion document under a new name and says whether the model may be changed beyond parameters for D-179 to D-182. Then update the model, or record the mismatch if it stays as it is.

## 00000000000000000000000000000000. 18 Nov 2026: Z axis and drive options

**Done:** assessed the Z axis and the screw and motor mismatch in `docs/z-axis-assessment.md`. Recommended: keep the Type 0 Z with a new 150 wide fixed plate bolted to the PrintNC X rollers, and keep DFU1605 and NEMA 24, changing the model to match. The DFU1605 flange fits the PrintNC rollers. No decision was made and the Fusion model was not changed.

**Left:** the owner has not chosen. The model has the Y motors at the front, but D-142 puts them at the back. The Fusion document is **unsaved** with **6 failing features**. The full travel has not been run. Availability and price of 120 × 120 × 8 and the LiMo prices for the 550 rail and 650 screws are not confirmed.

**Exact next step:** the owner chooses the Z axis option, the drive option and the Y motor end. Then record them as D-179 onwards and update the Fusion model.

## 0000000000000000000000000000000. 18 Nov 2026: beam bolts moved, unused parts hidden

**Done:** owner chose to move the beam bolt rows (D-178): `AdjXGanYRolHoles` is 13, and the holes line up after the rebuild. Failing features went from 8 to 6. The base frame, PrintNC Z axis, spindle and drill guides are hidden in Fusion, listed in `docs/printnc-assessment.md`. Nothing was deleted.

**Left:** the Fusion document is **unsaved** with **6 failing features**. The full travel has not been run. The Y cable chain brackets are still shown with nothing to mount on. Availability and price of 120 × 120 × 8, the real corner radius and the LiMo prices for the 550 rail and 650 screws are not confirmed.

**Exact next step:** the owner saves the Fusion document under a new name. Then run the gantry through its full travel and check for clashes. Use parameters only in Fusion, never direct modelling.

## 000000000000000000000000000000. 18 Nov 2026: beam 120 × 120 × 8, L bracket seated

**Done:** owner chose SHS 120 × 120 × 8 (D-177, amends D-176). In the open Fusion model `XGantryWidth` and `XGantryHeight` are 120, `XGantryOffset` is −35, and the bracket joint `d4192` now subtracts the offset. The L bracket has its full 50 seat and its 8 bolt holes line up. `docs/bom.csv` G01 and `docs/printnc-assessment.md` are updated. The earlier entry's offsets of +25 and +50 had the wrong sign: negative moves the beam to the rear.

**Left:** the rear beam bolts into the Y roller are 3 from the roller end and break out (Thread1 fails). The Fusion document is **unsaved** with **8 failing features**. The full travel has not been run. Availability and price of 120 × 120 × 8 and the real corner radius are not confirmed. LiMo prices for the 550 rail and 650 screws are still not confirmed.

**Exact next step:** the owner chooses how the rear beam bolts fix to the Y roller (`docs/printnc-assessment.md`, seat section), then saves the Fusion document under a new name.

## 00000000000000000000000000000. 18 Nov 2026: Y roller brace has no seat

**Done:** measured the L bracket `YRollerBrace` in the open Fusion model, read-only. It needs at least 50 of roller top in front of the beam. A centred 150 wide beam leaves 0. The current 75 wide beam at `XGantryOffset` 0 leaves 37.5, so the front brace bolts sit 0.5 past the roller end. The table is in `docs/printnc-assessment.md`. No parameter was changed and no decision was made.

**Left:** the owner has not chosen the beam width and offset. Options: 75 wide at offset 25 (recommended, keeps D-176), or 150 wide at offset 50 (reverses D-176). Neither has been rebuilt in Fusion. Offset 25 gave 10 failing features in an earlier trial, against 8 now. The Fusion document is still **unsaved**.

**Exact next step:** the owner chooses the option and saves the Fusion document under a new name. Then set the parameters, rebuild, check the brace bolts and the full travel, and record it as D-177.

## 0000000000000000000000000000. 18 Nov 2026: gantry beam 150 tall × 75 wide × 8

**Done:** owner changed the beam to RHS 150 tall × 75 wide × 8, 775 long (D-176, amends D-164). Fusion `XGantryWidth` is 75, and `XGantryOffset` stays 0 (25 gives 2 more failures). `docs/bom.csv` G01 and `docs/printnc-assessment.md` are updated.

**Left:** the 60 wide X BK12 and BF12 risers overhang the 43 flat on the beam's top face by 8.5 each side. Availability and price of 150 × 75 × 8 are not confirmed. The beam is 5.1 times less stiff horizontally and 3.3 times less in twist than the 150 × 150. LiMo prices for the 550 rail and 650 screws are still not confirmed. The Fusion document is still **unsaved** with **8 failing features**.

**Exact next step:** the owner saves the Fusion document under a new name, then chooses how the X screw supports sit on the 75 wide beam (`docs/printnc-assessment.md`, open item 4). Use parameters only in Fusion, never direct modelling.

## 000000000000000000000000000. 18 Nov 2026: Y rails 550, Y screws 650, tub 900 × 690

**Done:** owner chose the 550 Y rail and a 690 tub (D-175). Fusion `YCuttingArea` is 385, which gives the 550 rail and 650 screw. The rail and its risers need 684, leaving 3 at each tub end. `cad/v2/gantry_sketch.py`, its outputs and `docs/bom.csv` are updated. Baseline tub 141.2 kg, epoxy 15.5 to 16.9 kg.

**Left:** LiMo prices for the 550 rail set, the 650 screws and the shipping are **not confirmed**: curl found no product feed, and `docs/bom.csv` still carries the 600 prices, so the Phase 1 total is not current. Epoxy is tighter: tub 15.5 to 16.9 kg plus about 5 kg for the rail seats, from one 22.68 kg kit. The Fusion document is still **unsaved** with **8 failing features**. `cad/v2/assembly.py` and `docs/moving-gantry-sketch.md` are not updated to the new tub. The sketch still draws the old aluminium beam.

**Exact next step:** the owner saves the Fusion document under a new name and checks the LiMo basket for the 550 rail set and 650 screws. Then put the prices in `docs/bom.csv`. Use parameters only in Fusion, never direct modelling.

## 00000000000000000000000000. 18 Nov 2026: Y screws above the rails, tub length now open

**Done:** owner chose the Y screws directly above the rails (D-174, amends D-140). `cad/v2/gantry_sketch.py` and its outputs are updated. Measured in the Fusion model: the Y rail and its BK12 and BF12 risers need **734** in line with a 600 rail.

**Left:** the tub is still drawn **630** long, so the supports do not fit yet. Options are in `docs/printnc-assessment.md`, open item 1: 600 rail and 734 tub (150.3 kg), or 550 rail and 684 tub (140.1 kg). Either changes the 600 Y screws in `docs/bom.csv`, which is not edited yet. The Fusion document is still **unsaved** with **8 failing features**. `cad/v2/assembly.py` and `docs/moving-gantry-sketch.md` are not updated to the new tub.

**Exact next step:** the owner chooses the Y rail and tub length. Then set `YCuttingArea` if the rail changes, update `cad/v2/gantry_sketch.py` and `docs/bom.csv`, and record it as D-175. Use parameters only in Fusion, never direct modelling.

## 0000000000000000000000000. 18 Nov 2026: tub widened to 900 for the PrintNC gantry

**Done:** owner chose to widen the tub by 10 (D-173). Tub is now 900 × 630, Y rails ± 350, inner walls ± 310, outer walls ± 450. `cad/v2/gantry_sketch.py` and its outputs are updated. Baseline tub 129.0 kg (was 128.1). The Fusion model already has the rails 700 apart and was not changed in this step.

**Left:** the Fusion document is still **unsaved** with **8 failing features**. New open item: the PrintNC model has each Y screw directly above its rail, D-140 has it 65 outboard. `cad/v2/assembly.py` and `docs/moving-gantry-sketch.md` have not been updated to 900. `cad/v2/steel_gantry_sketch.py` was not re-run because D-172 replaces it.

**Exact next step:** the owner saves the Fusion document under a new name and chooses the Y screw position (`docs/printnc-assessment.md`, open item 1). Use parameters only, never direct modelling.

## 000000000000000000000000. 18 Nov 2026: PrintNC V4 gantry scaled in Fusion (document NOT saved)

**Done:** owner chose the PrintNC V4 gantry and rollers on the epoxy granite tub, with the 150 × 150 × 8 beam and the Type 0 Z axis (D-172). The open Fusion document `PrintNC V4 Metalcutter V4.0.38` is set by parameters only: cutting area 435 × 435 (600 rails), beam 150 × 150 × 8, radius 16, `XGantryOffset` 0. Details: `docs/printnc-assessment.md`.

**Left:** the document is **unsaved** and **8 features fail**. 5 are in the YRoller-Gantry Drill Guide and were caused by the first 150 beam trial; the others are Extrude8 in XRollers, Rigid 164 and Rigid 110. Y rail spacing is 700 against the tub's 690. Not checked: room for the gantry brace at offset 0, clashes over the travel, the real tube corner radius. The STEP file and `cad/v2/Facebutton v2 frame.step` are untracked and not committed.

**Exact next step:** the owner saves the Fusion document under a new name, then answers the 3 open items in `docs/printnc-assessment.md` (Y rail spacing first). Use parameters only, never direct modelling.

## 00000000000000000000000. 18 Nov 2026: steel gantry sketch drawn, no clashes

**Done:** `cad/v2/steel_gantry_sketch.py` draws the layout from one list of boxes and checks it over the full X, Y and Z travel: **no clashes**, all access holes clear. Outputs: `cad/v2/out/steel_gantry_sketch.png` and `.json`. Summary: `docs/steel-gantry-sketch.md`. Decisions: D-165 steel saddle, D-166 M10 joint, D-168 X motor folded over the screw with the drag chain on the back (supersedes D-167), D-169 foot step X 378 and X block pitch 90, D-170 ball nut flange flats 40, D-171 nut housings 20 off centre. Moving mass **86.8 kg**. Parts list unchanged.

**Left:** 2 items are open. (1) Proposal to drop the Ø20 top-wall holes and fit the M10 bolts from the open tube ends, rear row back at X 345 and X 420 (would amend D-166; the script still has the holes and the rear row at X 395 and X 430). (2) 1 mm relief over each nut flange. Steel saddle sizes, drag chain size and route are open. Not verified: SHS corner radius (flat width). `cad/v2/Facebutton v2 frame.step` is still untracked: ask the owner what it is.

**Exact next step:** get the owner's answer on the 2 items in `docs/steel-gantry-sketch.md`, apply them to the script and re-run, size the steel saddle, record them (next: D-172). Then the owner starts the gantry in Fusion and prices the tube (Dyfed Steels first).

## 0000000000000000000000. 18 Nov 2026: steel gantry layout brief (sketch NOT drawn)

**Done:** the layout below was worked out by hand. **Not done:** no script, PNG or note exists; no clash check has been run; the owner has not seen or agreed these numbers. All of it is a proposal: no D-numbers.

**Hold fixed:** tub 890 × 630, walls and Y rails (D-139 … D-141); X rails 600 (need 597.5), X screw 700, Y screws 600, Z 350. Coordinates as `cad/v2/gantry_sketch.py`: Z 0 = floor top, Y measured back from the spindle axis for the gantry parts.

| Item | Proposal |
|---|---|
| Usable flat on the SHS faces | Design for **102 wide** (outer corner up to 24, from memory of EN 10219 for 8 mm wall: **verify**). Flat = beam front + 24 to + 126 |
| Beam | Y 150–300 from the spindle (spindle offset **150**, was 175), Z 195–345 |
| Rail seats | Epoxy **4** thick on top and bottom faces. Top pour X ±325; bottom pour stops at ±305, clear of the feet |
| X rails | Top and bottom, same Y: centre **beam front + 36**. Seat to seat 158 apart (was 100) |
| X screw | On top, axis **beam front + 86**, Z 374. BK12 X 290–315 (lock nut to 327), BF12 X −310 to −290, both outside the saddle sweep. Ends −319 to +381 = 700 |
| Top stack | Seat 349, block top 379, **15 spacer** on each block to 394 (DSG16H top = axis + 20 = 394), arm 394–419 |
| Bottom stack | Seat 191, block bottom 161, arm 136–161 |
| Saddle | 3 pieces of 6082: existing front plate 180 × 400 × 20 (Y 125–145, Z 70–470, 5 clear of the beam) + **2 arms 180 × 130 × 25**. 5 × M8 in a row per arm, heads counterbored flush, fitted before the Z risers. Shim at the arm joints for Z squareness. Arms are not priced |
| Z stack | Unchanged in front of the plate (risers 15, rail + block 30, Z plate 20, clamp 60) |
| Feet (G03) | X **310–445** (135 wide, so the 600 rail ends 10 clear), Y 6–280 from the spindle, Z 155–195. 15 step along the whole foot, X 380–445, clears the Y housing and BK12 (168 against 170). Rear limit 280: further back hits the Y motor mount at the far end of travel |
| Beam to foot | **4 × M10 × 30 per foot**, up through the bottom wall into the foot, wrench through **Ø20 access holes in the top wall**. X 345 and 420; Y 190 and 262 from the spindle. Feet onto the Y blocks first, then the beam |
| X motor | Keep the belt fold (D-107): motor **behind the beam**, axis 137.5 behind the screw (375 belt), Z 374, body pointing inboard. Bracket on the beam end and rear face |
| Y carriages | Stay **140** behind the spindle so the tub does not change. Centre of mass will be further back: compute it and report the offset |
| Rail holes | Drill and tap M5 through the 8 mm wall, using the rail as the template, before the pour. Waxed bolts in the holes during the pour. M5 × 20 gives about 7 mm of thread: check |

**Levelling order (proposal):** top face first, free-surface pour with the beam level. After cure, turn the beam over and rest the cured seat on 3 equal pads on the levelled tub rail seats, then pour the bottom face so the two seats come out parallel. The aluminium front plate needs no pour. Check parallelism with an indicator.

**To check when scripted:** clashes at the X, Y and Z travel ends; moving mass with the 31.7 kg beam; flat width from a real source; bolt and hole spacing in the feet.

**Questions for the owner (with picks):** aluminium 3-piece saddle (pick) or steel; X motor behind the beam (pick) or above it; M10 access-hole joint (pick) or welded end plates.

**Note:** `cad/v2/Facebutton v2 frame.step` is untracked, single part named "facebutton", about 491 × 418 × 1000. Not used here and not committed: ask the owner what it is.

**Exact next step:** write `cad/v2/steel_gantry_sketch.py` from the table above (read `cad/v2/out/gantry_sketch.json` for the tub; do not import `gantry_sketch.py`, it rewrites its outputs). Output a PNG with a section through the saddle, a front view and a beam top view, box clash checks, and a one-page `docs/steel-gantry-sketch.md` with the questions. Then the owner agrees it and starts the gantry in Fusion. The owner can model the tub and Y axis now, and prices the tube (Dyfed Steels first).

## 000000000000000000000. 18 Nov 2026: D-164, steel SHS beam chosen

- Owner chose **SHS 150 × 150 × 8, 890 long**: rails on the top and bottom faces, X screw on top. Supersedes D-162/D-163. `bom.csv`: G01 replaced (not priced), generators re-run.
- **Phase 1 £3,972.51 excluding G01 and G03: £227.49 left** for the tube, levelling epoxy, end plates and feet.
- K I Metals live page (curl, 18 Nov): £90.30 ex VAT, £108.36 inc, with 33.9 kg shown, so about 1 m. The 890 mm price and delivery to SA2 were not seen.
- **`cad/v2/out/assembly/type0_assembly.step` and `assembly.py` are the old fixed-gantry design.** Do not start the Fusion assembly from them.
- Open: saddle (RHS or plate), spindle offset (D-106), X motor position, beam-to-foot joint, levelling-pour plan.

**Exact next step:** lay out the beam, rails, X screw, saddle and feet in a new sketch with the levelling-pour plan, and ask the owner the open choices. The owner prices the tube (Dyfed Steels first).

## 00000000000000000000. 17 Nov 2026: steel box-section beam proposed (superseded by D-164)

- Owner proposes a **PrintNC-style steel beam**: rails on the top and bottom faces, X screw on top. The saddle may be RHS too. **D-162/D-163 (Vallder) still stand until the owner decides**; the Vallder beam is not ordered.
- Stiffness (MNm², 890 long, S355). Vallder heavy: 13.1 kg, EI Y 0.51, Z 2.15. **SHS 150 × 150 × 8: 31.7 kg, EI Y 3.22, Z 3.22, GJ 1.83.** RHS 150 × 100 × 8: 26.2 kg, EI Y 1.24, Z 2.37, GJ 0.93. Mid-span deflection under 200 N: 0.4 µm (150 × 150).
- Why steel: the BK12/BF12 bolt flat on the top face (keeps the 700 screw), torsion is much better, and steel expands like EG. Against: moving mass about 70–80 kg (was 56); accuracy now comes from the epoxy levelling of 3 rail faces (beam top and bottom, saddle front); top-to-bottom rail parallelism and Z squareness are set by indicator and shims; weld and cut before levelling; hot-finished (EN 10210) warps less.
- 150 × 150 preferred: its 150 top face takes the top rail plus the BK12 (60 wide), and the taller rail spacing resists tilt.
- Suppliers (other session): `docs/steel-rhs-suppliers.md`. Phone Dyfed Steels, Llanelli, first. K I Metals online: 150 × 150 × 8 £90.30 ex VAT (probably per metre; check).
- Budget: dropping the Vallder frees £148.08, which leaves about £227 for the tube, levelling epoxy, end plates and feet.

**Exact next step:** the owner prices the tube (Dyfed first) and decides steel vs Vallder. If steel: record D-164 (supersedes D-162/D-163); replace G01 in `bom.csv` and re-run the 5 generators; then lay out the beam, rails top and bottom, X screw on top and an RHS saddle (size it) in a new sketch, with the levelling-pour plan.

## 0000000000000000000. 17 Nov 2026: D-163, Vallder price corrected

- The £229.56 was JLC's shipping, not Vallder's. Owner's Vallder checkout (UK): €121.93 + DHL €25.94 = €147.87, no EU VAT. With 20% UK import VAT (paid to DHL): **G01 £148.08** (was £331.31).
- **Phase 1 £4,120.59: £79.41 left** for G03 (feet, unpriced). Not counted: DHL clearance fee; duty assumed 0% (EU origin).
- Note: `bom.csv` has LF line endings, not CRLF as `tasks/README.md` says.

**Exact next step:** unchanged from D-162 below, except the budget question: G03 feet (and end plates) must fit in £79.41. The owner answers rail seats, X screw supports and end plates; then redraw G03 for 235 × 125 in `cad/v2/gantry_parts.py` and get the JLC price.

## 000000000000000000. 17 Nov 2026: D-162, Vallder heavy beam

- Owner chose Vallder (shipping estimate £229.56). Heavy 235 × 125 assumed (200 × 96 ruled out). `bom.csv`: G01 = Vallder £331.31, G02 and G04 dropped, G03 feet stay unpriced. Generators run.
- **Phase 1 £4,303.82: £103.82 over the £4,200 budget**, before the feet. The owner must decide what to cut or accept.
- The JLC STEP files (`cad/v2/out/jlc/`) are now only for G03 (feet) and reference; G01/G02 no longer needed.
- Open before the feet model: rail seats (q4 in `beam-extrusion-check.md`), X screw supports (BK12/BF12 don't fit the channel), beam-to-foot end plates, import VAT/duty on the Vallder order.

**Exact next step:** owner answers the budget overrun and the 3 open points above; then redraw G03 feet and end plates for the 235 × 125 profile in `cad/v2/gantry_parts.py` and get the JLC price for the feet.

## 00000000000000000. 17 Nov 2026: basic JLC STEP for pricing

- Owner asked for a very basic model to get the JLC price now. `cad/v2/gantry_parts.py` → `cad/v2/out/jlc/G01_beam.step` (13.6 kg), `G02_back_plate.step` (3.55 kg), `G03_foot_block.step` (3.48 kg, qty 2). Each re-imports as one solid at the right size.
- Built on my step-4 picks; the 7 questions in `task22-step4.md` and the beam choice (`beam-extrusion-check.md` q1) are still open. Left out: datum shoulder, BK/BF pads, Y nut step, counterbores.

**Exact next step:** the owner uploads the 3 STEPs to JLCCNC (6061, standard finish, G03 × 2) and reports the price; then record it on G01–G03 in `bom.csv` (run the 5 generator scripts) and finish the model after the 7 answers.

## 0000000000000000. 17 Nov 2026: Vallder beam check measured

- Owner sent Vallder's DXF and STEP files. Sections in `cad/vendor/vallder_*.dxf`; `cad/v2/vallder_profiles.py` computes them with the `beam_options.py` load model.
- **Heavy 235 × 125: EI Y 0.51, Z 2.15, twist about 13 µm, 13.1 kg.** JLC step-4 beam on the same routine: **EI Y 0.92, Z 1.33, twist about 4 µm**. 200 × 96: EI Y 0.17, out.
- Heavy layout: rails 154 apart, DSG16H fits (7.6 clear). **BK12/BF12 do not fit** the tapered channel (52.9 wide at their base, they are 60): cut them down, or end plates and a 952 screw (re-buy).
- `docs/beam-extrusion-check.md` rewritten. My pick: keep the JLC channel (D-147); heavy as fallback if the JLC quote is high.

**Exact next step:** the owner picks the beam (`beam-extrusion-check.md` question 1) and answers the 7 questions in `task22-step4.md`; then write `cad/v2/gantry_parts.py`.

## 000000000000000. 17 Nov 2026: task 22 step 4 proposal

- `docs/task22-step4.md` + `cad/v2/out/gantry_parts_sketch.png`: X screw channel in a 30 mm front wall (D-108 spacer out), BK/BF outside the X block travel (X screw needs 696 of 700), solid beam end blocks bolted down into the feet (feet fitted first). Beam 17.8 kg, moving mass about 56 kg.
- Machine sketch relabelled as it stands (`gantry_sketch.png`).

**Exact next step:** the owner answers the 7 questions in `task22-step4.md`; then write `cad/v2/gantry_parts.py` (STEP for the JLC upload).

## 00000000000000. 17 Nov 2026: D-160, tests cut to the mix bricks

- **D-160:** every EG test dropped except mix bricks A1–A4 (10–13 % epoxy, blend P1), judged on surface and voids. Gone: packing test, heat brick and pull test (so the D-159 M5 torque question is gone too), beam section, rail-seat strip, prisms, expansion test (D-149 superseded). `eg-mix-test-plan.md` rewritten (93 lines). Release still compared on the 4 brick moulds (D-120), no cost.
- Now relied on without a test: blend P1, the `curing-heat.md` estimate, rail-bar bow and the rail-seat pour first seen on the real casting.
- **D-161:** X07 torque wrench + socket dropped (−£43.71). Phase 1 priced **£3,972.51** (budget £4,200, **£227.49 left** for G01–G04); wave 3 £910.84.

**Exact next step:** task 22 step 4 (STEP for the JLC quote).

## 0000000000000. 17 Nov 2026: D-159, F08 and F20 dropped

- Owner set the LiMo coupling to 3 (no new checkout saved: DDP sea at $129 not re-seen).
- **D-159:** F08 (M12 rod + nuts) and F20 (40 × 20 bar) dropped, −£42.58. No cast-in lifting points: the castings are lifted with a hydraulic hoist and straps. Test brick C keeps its heat probes; its bar is now a 40 × 10 × 120 F07 offcut tapped M5, pull test with an M5 rail bolt. **Open:** M5 torque steps (the owner's wrench starts at 21 N·m).
- Phase 1 priced **£4,016.22** (budget £4,200, **£183.78 left**), excluding G01–G04. Wave 2 £525.71.
- Not changed yet: `cad/v2/assembly.py` and `base_cores_sketch.py` still draw the lifting points (old fixed-gantry CAD; remove them when the tub CAD is redone).

**Exact next step:** task 22 step 4 (STEP for the JLC quote; the gantry G01–G04 has to fit in £183.78 or the budget moves).

## 000000000000. 17 Nov 2026: LiMo Checkout7

- Rails fixed: HGH20CA 600 × 2, **$43.33 a set** (M01, M02 £29.50 each). Total as saved **$752.72 = £569.35**.
- **DDP sea rose to $129** (was $89; DDP air $269). Only change from Checkout6 was HGH15 → HGH20 rails: looks like a weight band, not confirmed. M05 £470.82.
- Still wrong: D25L35 × 1 (needs 3, +$6.42). Corrected order about $758.50 = about £573.7.
- Phase 1 priced **£4,058.80** (budget £4,200, £141.20 left), excluding G01–G04 (JLC gantry). Wave 1 £2,097.33. Details: `price-check-task-16.md`, last section.

**Exact next step:** owner sets the coupling to 3 (at order time is fine; check DDP sea stays $129); owner decides F08/F20; then task 22 step 4 (STEP for the JLC quote; the gantry has to fit in £141.20 or the budget moves).

## 00000000000. 17 Nov 2026: LiMo Checkout6

- 600 screw × 2 and the 500 rail removed: fixed. DDP sea stays **$89** with 2 × 600 sets, so M05 £440.56 stands.
- Still wrong: rails are HGH15CA 600 × 2 (need HGH20CA, D-11); coupling × 1 (need 3). HGH20CA 600 price still not known.

**Exact next step:** owner swaps HGH15CA for HGH20CA 600 × 2 and sets D25L35 to 3, saves Checkout7; owner decides F08/F20; then task 22 step 4.

## 0000000000. 17 Nov 2026: LiMo Checkout5

- `Checkout5.htm`: C5 set 700 **$153.57** (M05 now £440.56 with the $89 DDP sea seen; £470.82 if it becomes $129). Phase 1 priced **£3,969.54**, wave 1 £2,008.07, excluding 6 lines not priced: M01, M02 (LiMo HGH20CA 600) and G01–G04 (JLC gantry, not in a wave yet).
- Basket wrong in 4 places: 600 screw × 1 (needs 2), HGH20CA 500 (needs 600), HGH15CA 600 (wrong size, needs HGH20CA 600 × 2), D25L35 × 1 (needs 3). Corrected list: `limo-basket.txt` basket C. Details: `price-check-task-16.md`, last section.

**Exact next step:** owner fixes the basket (basket C) and saves a new checkout (HGH20CA 600 price, DDP sea shipping); owner decides F08/F20; then task 22 step 4.

## 000000000. 17 Nov 2026: task 22 step 3 done

- Owner took all picks: **D-150 … D-158** (X rails 2 × 600, X screw 700; Y motor brackets from the 6082 plate; 3 × M09; X rail bars out; F09 out; back plate bonded with Ampreg 30 thickened with whiting; 6th home switch for Y2; Y drive standard BK12 end; 48 V supply kept for Phase 1).
- `bom.csv` edited (M01, M02, M05–M09, M12, M15, M16, F07–F10, F20, E04, E10, E14, X10; new G01–G04) and the 5 generators re-run (`PYTHONUTF8=1` needed on Windows). `gen_wave1_sheet.py` now shows blank prices as "to price".
- **Phase 1 priced £3,528.98**, excluding M01, M02, M05 (LiMo, not priced) and G01–G04 (JLC). Wave 1 £1,567.51, wave 2 £568.29.
- **Held, not dropped:** F08 (M12 rod) and F20 (40 × 20 bar): test brick C in `eg-mix-test-plan.md` uses them, and F08 was listed for lifting points. Owner to decide.
- Flagged prices: M09, M15, E10 are unit price × quantity, shipping for the new quantity not re-checked.
- Open: F07 (does 2 m of 40 × 10 cover 2 × 600 + plates + pads; is the 25 × 10 still needed), M12 cut list (2 Y brackets).

**Exact next step:** the owner saves the LiMo pages (C5 set 700, HGH20CA set 600) and does a new checkout to SA2 (DDP sea), and decides F08/F20; then task 22 step 4 (STEP of G01–G03 for a JLC quote).

## 00000000. 17 Nov 2026: task 22 step 3 draft (waiting on the owner)

- Draft: `docs/task22-step3.md` (lengths, revised LiMo basket in `limo-basket.txt`, `bom.csv` change list, 12 questions). Nothing decided; `bom.csv` unchanged.
- LiMo and StepperOnline still block curl: C5 set 700 and HGH20CA set 600 unpriced (owner to save the pages, question 2).

**Exact next step:** the owner answers the 12 questions in `docs/task22-step3.md` section 4; then record the D-numbers (next D-150) and, if question 10 is yes, edit `bom.csv` and re-run the 5 generators.

## 0000000. 17 Nov 2026: beam assessment, beam chosen

**Done**
- `docs/beam-assessment.md` (numbers: `cad/v2/beam_options.py` → `cad/v2/out/beam_options.json`). JLC max part size **1100 × 600 × 500** (curl, jlccnc.com/cnc-machining); JLC uses its own stock only (6061, 7075, steel 45, SUS304).
- **D-147 beam:** JLC one-piece 6061 U channel 150 × 130 × 10, 890 long, back plate bonded and bolted (EI about 0.90 MNm², 12.5 kg, moving mass about 50 kg). No EG fill now; fill ports in the back plate for later.
- **D-148:** no internal skeleton in the tub; D-115 stays.
- **D-149:** expansion test on prism B2 (test 9 in `eg-mix-test-plan.md`). Industrial EG 12–16 × 10⁻⁶/°C (Schneeberger sheets).

**Left**
- Task 22 step 3: lengths (sketch: Y rails 2 × 600, Y screws 2 × 600, X rails 2 × 600, X screw 700, Z 350; the beam choice does not change them), revised LiMo basket (DDP sea, 950 mm max), `bom.csv` change list (2nd Y screw, M09 motor + driver, couplings, Y mounts, portal casting lines out, gantry parts in incl. the D-147 channel and back plate), electrical (Mesa ch 3 = Y2). **Ask the owner before editing `bom.csv`.**
- Step 4: STEP of the gantry parts for a JLC quote. Unpriced: JLC beam, a 2nd epoxy kit (only if filled later; D-122 price is from 9 Nov), Aluminium Warehouse cut plate (calculator not readable by curl).

**Exact next step:** task 22 step 3 (`docs/tasks/22-moving-gantry-redesign.md`, State section).

## 000000. 17 Nov 2026: EG video notes (side note, no decision)

- Owner's transcript of a YouTube EG-base video, compared with the tub plan: `docs/video-notes-eg-base.md`. Its 80 % sand / 20 % epoxy pourable mix does not suit the tub (EG is the structure here; 20 % needs about 25.6 kg epoxy, more than the kit). Useful for the beam task (EG-filled box: about 25–30 kg more moving mass).
- 4 owner questions at the end of that file (mixing order, mix time, EG-filled beam, pigment). Open question 15a.
- Owner answered (D-144 premix, Ampreg mixed density 1.10 and the test-plan table fixed; D-145 filled beam and internal skeleton go into the beam assessment; D-146 black pigment, price open: question 15a).
- Exact next step unchanged: task 22, the beam assessment (D-143, D-145).

## 00000. 17 Nov 2026: task 22 sketch agreed in part

- Sketch: `docs/moving-gantry-sketch.md`, PNG `cad/v2/out/gantry_sketch.png`, script `cad/v2/gantry_sketch.py`. Tub 890 × 630 × 185, 128 kg solid, inside 610, walls 140 wide and 100 above the table, floor 60. Al box beam 150 × 130 × 10, 890 long, EI 0.90 MNm²; about 50 kg moving in Y.
- Owner answers: D-139 (tub: no back wall, solid, walls 100 up, linked seat pour by a temporary MDF trough), D-140 (Y screws outboard on the wall tops), D-141 (Y travel 350 for the ATC: Y rails and screws 600), D-142 (Y motors direct at the back).
- **Open (D-143): how the beam is made.** Owner: "next task will assess this" (bolted 4-plate box, stock tube, or EG-filled; JLC's maximum part size by curl).
- Not done: step 3 (LiMo basket: Y rails 2 × 600, Y screws 2 × 600, X rails 2 × 600, X screw 700, Z 350; `bom.csv` change list; electrical). `bom.csv` and the LiMo order are unchanged.

**Exact next step:** task 22, the beam assessment (D-143), then step 3.

## 0000. 17 Nov 2026 (late): layout change

- **D-137: moving gantry, fixed table in one cast EG tub** (like Moxer), replacing D-01. Portal casting and joint go. Two Y screws and motors. Tub in one piece, owner accepts about 115–160 kg. Gantry in aluminium, maybe JLC: **sketch first**.
- **D-138: Phase 2 ATC is a Timbre-style umbrella wheel** at a table corner (replaces D-73).
- Checkout 4 recorded ($604.24, basket correct), **but the LiMo order is on hold**: the screw and rail lengths change.
- The Fusion pass (task 09) should pause on the castings and gantry until the sketch is agreed.

**Exact next step:** task 22 (`docs/tasks/22-moving-gantry-redesign.md`) in a fresh session: the sketch.

## 000. Session of 17 Nov 2026 (LiMo prices and checkout)

**Done** (all in `price-check-task-16.md`, last three sections)
- **C5 screw page:** screw + nut only, no supports (superseded).
- **C5 set page:** DFU1605 + steel housing + **C5 BK12/BF12**, lengths in 50 mm steps: 850 $171.57, 600 $141.57, 350 $111.57 = **$424.71** (C7 kits 900/600/400: $152.19). Light preload P2 by default.
- `docs/limo-basket.txt`: basket list for the owner (A = C5, B = C7).
- **Checkout to SA2:** DDP sea $129 (30–45 workdays, max 950 mm), DAP air $239 (tax extra), DDP air $269 (duty included). The owner's saved basket had **2 × 600 mm** and an **HM10-60** (should be 1 × 600 and HM12-60) and no code; corrected in the figures.
- **Whole LiMo order, DDP sea, corrected:**
  - **C5 £487.30** ($644.25: goods after `10OFF` + $129);
  - **C7 £313.13** ($413.98: after `5OFF` + $129);
  - **against £464.41 now** (several sellers).
  - C5 is £22.89 more than now; C7 is £151.28 less.

- **Updated checkout** (owner fixed 1 × 600): **DDP sea $89**, DDP air $209, DAP air $239. Still HM10-60 and no code in it. Corrected: $515.25 + $89 = **£457.05** (without the code: £500.35).
- **D-136 (owner): C5, LiMo, ordered in wave 1 (4 Jan 2027).** `bom.csv` M01–M08 and M13 moved to LiMo, one line per item (all the shipping is on M05). The 5 scripts were re-run. Wave 1 is now £1,927.74 and wave 2 £587.30. **Phase 1: £3,908.22** (was £3,915.58). The wave 1 order sheet has a LiMo section.

- **Checkout 3 (17 Nov, later):** HM12-60 in and **`10OFF` accepted** (10 % of goods, not shipping). But the 600 mm set is × 2 again and DDP sea is $129: as saved $771.65 = £583.67. With 1 × 600 it stays $604.25 = £457.05 (`bom.csv` unchanged).

**Left**
1. ~~Fix the basket~~: **checkout 4 is correct** (1 × 600, HM12-60, `10OFF`, DDP sea $89, total **$604.24**). On 4 Jan: order it with DDP sea. X and Y stub drawings to email with the order number (needs the owner's new CAD, task 09).
2. ~~Is the 10 % code accepted?~~ Yes (checkout 3).
3. The steel nut housing in the C5 set: size and bolt pattern not known (the CAD uses DSG16H). Ask LiMo or check their CAD drawing.
4. LiMo's answer to 6a (rail class, HM12-60 at 50 mm, coupling fit, VAT in DDP): record it under 6a and in `open-questions.md`.
5. After that and the owner's new CAD: X and Y screw end drawings.

**Exact next step:** wait for LiMo's 6a answer and the owner's new CAD; then draw the X and Y screw ends (ask the owner: exact lengths or 850 / 600) so they are ready for the 4 Jan order.

## 00. Session of 16 Nov 2026 (LiMo reply)

**Done**
- LiMo answered message 6 (Amy Jiang): custom end machining from our drawings; light preload, but they advise **C5 ground**; prices from the online store, shipping and dates at checkout. Recorded in `supplier-messages.md` section 6 and `open-questions.md` item 9.
- Reply **6a sent 16 Nov** (rail accuracy class, HM12-60 drilled to 50 mm and cost, D25L35 coupling inside the HM12-60, VAT in the DDP price). Waiting.
- End machining agreed in principle (task 13 notes): LiMo's standard drawing (BK12: Ø10 × 15, M12×1 × 14, Ø12 × 25; BF12: Ø10 × 11 with circlip groove), changing only the **X and Y drive stubs**: longer, Ø10 0/−0.015, one flat 1 mm deep for the pulley and KFL000 grub screws. Z fully standard.
- Owner: lengths stay **X 850 / Y 600** for now; C5 or C7 decided after the C5 price; **no drawings until LiMo answers**.
- **The owner is redoing the CAD** (task 09): the stub and overall lengths come from the new CAD, not the old numbers (X stub about 74, Y about 32 from the thread end; spare 27 / 18 mm goes on the drive stub with 850 / 600).

**Left**
1. **C5 price recorded (17 Nov, `price-check-task-16.md`):** C5 sets (screw, steel housing, C5 BK12/BF12) 850 / 600 / 350 mm = $424.71 vs $152.19 for the C7 kits. Whole LiMo order with C5 by sea: £557.54 (£464.61 if DDP includes VAT) vs £464.41 now and £348.53 LiMo C7. Owner: note the checkout shipping to SA2 (sea and air), then decide C5 or C7 (next D-number: D-136).
2. LiMo's answer to 6a: record it under 6a and in `open-questions.md`.
3. After that and the new CAD: make the X and Y screw drawings (still ask the owner: exact lengths or 850 / 600).

**Exact next step:** superseded by section 000.

## 0. Where the session of 15 Nov (late evening) stopped

**The owner's answers (D-133)**
- `assembly-steps.md` is clear to the owner as written. No simplification of the assembly for now.
- Measuring square (step 8): "choose the one that makes sense". Chosen: an **engineer's square** (300 mm, DIN 875 grade 1 or 2) with the DTI. It's quick and needs no cutting, which matters because it's done after every move.
- Earlier the same day (still current): D-128 re-square after each move; D-129 post-cure and tent stay; D-130 nothing from the Opus branch; D-131 castings keep their features; D-132 portal bolted dry on shims, no grout, no dowels.

**Done and pushed**
- **Task 04 done.** Dowel sleeves removed from `assembly.py` (base 80.3 kg, portal 37.6 kg, no clashes). Re-run: `assembly.py`, `enclosure.py`, `bench.py`, `base_cores_sketch.py`; `cast_in_features.md` regenerated. `render_views.py` and `render_steps.py` were **not** re-run (the holes were under the leg feet, so the pictures don't show them).
- `portal-relocation.md` rewritten to the bolted-dry method, one page. The old grout sketch (`relocation_sketch.py`, `portal_relocation.png`) is deleted.
- Grout piece F dropped from `eg-mix-test-plan.md`.
- `assembly-steps.md`, `open-questions.md`, `phase1-schedule.md` and `assembly.md` updated to match.
- **`docs/price-check-task-15.md`** (engineer's square X10, shim stock X11), partly done with curl. Square found: Mitutoyo 916-227, grade 1, £62.00 ex VAT (£74.40 inc) at MQS, delivery unknown. Shims: only dear ones so far (Cromwell pack £224 ex VAT, RS roll £97.80 ex VAT).

**Later the same evening (D-134)**
- Price check 15 finished by curl: square Mitutoyo 916-227 grade 1 £74.40 inc (MQS); shims Cromwell T&A steel pack 12 × 6 × 12 in, 0.025–0.38 mm, £58.19 inc. The owner finds the UK precision tools too dear and checks **AliExpress** first: the list is at the end of `price-check-task-15.md` (square, shims, **M5 × 20 grade 12.9** rail bolts, optional graded straightedge).
- Task 05: owner chose 12.9 bolts (D-134). Fallback Screwfix A2 1941T, 50 pack £5.89 inc. Not in `bom.csv` yet.

**16 Nov session (D-135)**
- Cooling loop: no radiator or fans, a 20 L bucket reservoir instead (S05 £51.77). Bench re-run (bucket at the back right, PC moved), OUT3 spare in `electrical.md` and the HAL. LinuxCNC simulator not re-run.
- AliExpress reply in `price-check-task-15.md`: square £18.19, shims under £25 (waiting), bolts Screwfix, straightedge KS Tools (price/grade missing). Not in `bom.csv` yet.
- Owner wants rails, ballscrews and accessories from one seller: `docs/motion-parts-one-seller.txt`.

**Task 21 done (15 Nov 2026):** owner gets a LiMo quote (draft: `supplier-messages.md` section 6), including whether the HM12-60 (49.5 mm holes) fits the NEMA 24. limobearing.com blocks curl (403); from the owner's saved page, LiMo DFU1605 C7 kits (BKBF12 + housing) 900/600/400 = $152.19, £200.77–237.07 all-in vs £229.01 (shipping band unknown). Whole LiMo order (screws, rails, HM12-60, coupling) $284.98 after 5 %: £348.53 by sea, £412–467 by air, vs £464.41 now. HL Motion has no DFU1605 (SFU sold out), no pulleys, belts or KFL000; rails £108.83 inc VAT + unknown shipping vs £207.37. Results and draft message in `docs/price-check-task-16.md`. Owner decides; `bom.csv` unchanged.

**Open, in order**
1. **Owner's AliExpress reply** → add X10, X11 and the new X03 (and X05 if swapped) to `bom.csv`, re-run the 4 BOM scripts, update the wave total in `phase1-schedule.md`. That finishes task 05.
2. Task 13: drafts ready, now 5 (section 5 is new: EC Fibreglass, Ampreg delivery to SA2 and shelf life); the owner sends them and the answers go under each message and in `open-questions.md`. Task 15 done: `docs/wave1-order-sheet.md`, generated by `tools/gen_wave1_sheet.py` (one table per vendor, open checks per line, total £1,470.69 = schedule).
3. Task 09 (owner's Fusion pass), then 10, 11 (mould drawings).
4. **Every open task now waits for the owner** (AliExpress reply, the 5 messages, the Fusion pass). Task 14 waits for the Z mount seller's drawing (message 4). Task 17 (tidy the old casting notes) no longer waits: 03 and 06 are on hold (D-131), so a session can do it.

**Warnings for the next session**
- **Ask before deciding** (Q&A tool). Keep answers, documents and procedures short. No grout, glue or other half-measures in joints: either bolted or bonded.
- **Price checks: curl first** (the owner asked: the browser uses many tokens). The notes in `price-check-task-15.md` say which sites curl can read. Do not spoof browser headers to get past a bot block (RS, Amazon): use the browser with one small `get_page_text` instead.
- **Python on Windows:** set `PYTHONUTF8=1` before running the CAD scripts, or `enclosure.py` stops with a `UnicodeEncodeError`.
- **Do not merge `claude/awesome-ramanujan-by9kds`** (old design, clashing D-numbers).
- The CAD still has the 2 × Ø40 portal cores and the ATC insert (both agreed to stay for now, D-131).
- **Git on the owner's PC has no identity set.** Commit with `git -c user.name=Claude -c user.email=noreply@anthropic.com commit ...`; do not change their git config.
- Sections 1–9 are background and partly older; where they disagree, section 0, `decisions.md` and the task files win. Ignore the grout and dowel text in sections 2 and 6.

## 1. What the project is
A DIY 3-axis **fixed-gantry, moving-table** CNC mill with a **cast epoxy-granite (EG) frame**, **LinuxCNC + Mesa 7I76EU**, closed-loop NEMA 24 steppers, and (Phase 2) a **Jianken ISO20 ATC spindle** with an 8-pocket ferris-wheel tool changer. Inspiration: Bootstrap Bill. The owner is in **Swansea, UK**, builds in a **shed**, and must later move it into an **upstairs flat**: pieces ≤ about 40 kg (the base is a 2-person lift).

## 2. Current design (full assembly, D-102 … D-127)
The detailed design now lives in **`cad/v2/assembly.py`** (parametric CadQuery, vendor STEP models swapped in) → `cad/v2/out/assembly/`. Read **`docs/assembly.md`** first; `cad/v2/out/assembly/cast_in_features.md` lists every cast-in feature.

- **Work area 400 × 250, Z 150.** Travel X 570 (incl. reach to the ATC wheel) / Y 250 / Z 150. Table 460 × 330 × 25 (6082). Spindle axis at Y −65 (175 mm in front of the beam face).
- **Castings (2):**
  - **Base:** T-shape, spine **340** × 725, rear cross-piece 640 × 230, 110 high, 45° tapers 100 × 100 at the T-junction. **80.2 kg**. Sits on 3 steel pads on the bench (D-119). Cast upside down (top face on the mould floor = jig).
  - **Portal:** 800 wide, beam **150** × 130, legs 70 × 130, 375 tall, 45° haunches 60 × 60 at the leg/beam corners, 2 × Ø40 PVC cores in the beam with every wall ≥ 20 mm (D-114). **37.6 kg**. Cast lying on its front (rail) face; the back is the open pour face (so no leg flare, D-113).
  - Joint: 2 × M12 rod per leg through cast tubes into **40 × 20** tapped bars in the base (D-116), grouted; no dowels, re-squared after each move (D-128).
  - Inserts: steel flat bar under the rails (40 × 10 for Y, 25 × 10 for X), tapped M5, 5 mm under a levelling-pour recess that is open to the casting edges (D-115).
  - **Resin (D-117, D-122):** Gurit Ampreg 30 + 3X Slow, one 22.68 kg kit, for castings, rail seats and grout; cure at 18 °C or more, post-cure 16 h at 50 °C (Tg 74 °C).
  - **Compaction (D-123):** hand tamping in layers; a vibration motor only if the test bricks show voids.
- **Motion:**
  - HGR20 rails: X 2 × 800, **100 apart** on the beam face; Y 2 × 500, 280 apart; Z 2 × 350, 100 apart on 15 mm risers on a tall saddle.
  - Ballscrews DFU1605: needed overall X 823 / Y 582, so buy **X 850 / Y 600 / Z 350**.
  - BK12/BF12 supports; DSG16H nut housings; X housing on a 25 mm spacer in a 45 mm deep X channel.
- **Drives:** X and Y **folded with 1:1 HTD-5M belts** (Y motor alongside the spine under the table; X motor on the beam top with an outboard KFL000 bearing). **Z direct** on top (motor with brake). Motor hole spacing is **50 mm**, not 47.1.
- **Plates:** saddle 180 × 400 × 20, Z plate 140 × 200 × 20, plus spacer, risers and motor plates.
- **Spindle (Phase 1):** G-Penny 2.2 kW ER20 water-cooled kit (Huanyang VFD on **USB-RS485 + hy_vfd**). DIY cooling loop.
- **Enclosure (Phase 2):** 12 mm MDF, sized from the assembly: **932 × 836 × 898** outside. `cad/v2/enclosure.py`.
- **Bench:** owner-built knock-down timber bench, top 1000 × 1000 at 785 mm, joists under the spine edges, cabinet + cooling loop inside. `cad/v2/bench.py` → `cad/v2/out/bench_cutlist.md`.
- **Electrics / control:** `docs/electrical.md` (Z brake hardwired through the safety relay, D-93), `linuxcnc/type0/` + `docs/linuxcnc.md` (simulator-tested 23/23).
- **3D printing:** owner has 3 × Bambu P1S; printed parts in **PETG** (`docs/printed-parts.md`, `cad/v2/printed_parts.py`).

## 3. Money and phases
| Phase | Scope | Priced | Budget |
|---|---|---|---|
| 1 | Working mill, manual ER20 tool changes | **£3,908.22**, every line priced (price checks 12–15 applied, D-126; LiMo C5, D-136). £282 under the budget; not yet in it: delivery for the Ampreg kit and the GCL quartz. M13 (Z motor mount) is provisional | £4,200 (D-127) |
| 2 | ATC spindle + holders, air, mist, enclosure, tool wheel | about £1,400 (not re-checked) | not set |

- Source of truth: **`docs/bom.csv`**. After editing it, regenerate everything: `python tools/gen_bom_md.py`, `python tools/gen_phase1_xlsx.py`, `python tools/gen_phase1_cost.py`, `python tools/build_open_links.py`, `python tools/gen_wave1_sheet.py`.
- Order waves (`docs/phase1-schedule.md`): **1** (4 Jan) electrics, motors, spindle kit, cooling loop; **2** (15 Feb) bench, moulds, local items and the **motion parts** (D-103); **3** (1 Mar) casting materials; **4** (29 Mar) aluminium plates, collets.

## 4. Schedule
4 Jan → 22 Jul 2027, about 5 h/week. Done = the machine moves under LinuxCNC.
- **Before Jan:** CAD assembly refined by the owner in Fusion.
- **Jan–Feb:** electrics bench-tested indoors.
- **Early March:** spindle kit bench-tested.
- **March:** moulds, then test bricks.
- **April–May:** castings at 17–23 °C, 7-day cure, in an insulated tent with a thermostat heater.
- **June:** assembly.
- **July:** wiring and LinuxCNC on the machine.

## 6. Tasks
1. ~~Electrical design~~: done (`docs/electrical.md`, D-91, D-93).
2. ~~LinuxCNC config~~: done (`linuxcnc/type0/`, `docs/linuxcnc.md`, D-92).
3. ~~Timber bench~~: done and priced (`cad/v2/out/bench_cutlist.md`, D-97, D-99).
4. **Full CAD assembly: first version done** (D-102 … D-116, vendor models in, no clashes at 3 positions; review changes D-114 … D-116 applied). **Waiting for:**
   - the owner's Fusion pass (brackets, plates, sensor mounts, VERIFY list in `docs/assembly.md`) and the returned STEP. Put it in the repo, e.g. `cad/v2/in/`, and feed changes back into `assembly.py`;
   - the M13 seller's drawing (or make the mount from plate).
5. **Mould drawings** (blocked by 4): from the final assembly and `cast_in_features.md`. Cover:
   - panels and the jig-bolt pattern for the insert bars;
   - channels, sleeves, cores and their suspension;
   - the 3-piece wedge plug for the portal opening;
   - haunch and taper blocks, lifting points;
   - the vibration-table deck;
   - printed mould helpers (F19).
6. **EG mix design + test-brick plan: first draft done** (`docs/eg-mix-test-plan.md`, `docs/curing-heat.md` rewritten for Ampreg 30, D-124). Owner to review the pass marks, quantities and kit list. Covers:
   - Ampreg 30 + 3X Slow (D-122), hand-tamped in layers (D-123), GCL quartz 2–5, H&B sand 0–1, whiting; epoxy at 10 / 11 / 12 / 13%;
   - the review's tests (`review-eg-design-report.md` section 4): cut test beam section with the real cores, 3 release methods, packing test with and without GCL 1–3 mm, joint-bar pull test, 500 mm rail-seat test strip, creep and stiffness prisms;
   - a full-thickness heat brick with a centre probe;
   - curing-heat.md rewritten for Ampreg 30 (18 °C minimum, post-cure 16 h at 50 °C);
   - add a heater and thermostat to the BOM.

**In progress / proposals:**
- **Phase 1 simplification (owner request, 15 Nov):** castings and layout as simple and low-risk as possible. Two options in `docs/simplification-options.md`; waiting for the owner. Do not add features to the castings.
- **Portal relocation** (`docs/portal-relocation.md`): decided, bolted dry on shims (D-132, D-133).
- **Opus branch `claude/awesome-ramanujan-by9kds`: do not merge.** It forked from the 8 Nov state and redid tasks 2–5 on the old design with clashing D-numbers. This branch is the truth (owner, 15 Nov). Useful there: `cad/v2/moulds.py` as a starting point for the mould drawings.
- **Rail bolts must be M5 × 20**, not M5 × 16, because of the 5 mm resin seat (open question 4a).
- **Base PVC cores (not adopted yet):** 5 × Ø50 at Z −65, saving about 9.6 kg; sketch in `cad/v2/out/base_cores_plan.png`, `base_cores_sections.png` (`cad/v2/base_cores_sketch.py`). Suspension: an M8 rod through each capped core, fixed in the mould walls at core height, plus mid-span wire hold-downs from a batten; the rods are cut flush and sealed afterwards (they don't reinforce, D-120). The review found the layout sound (15 mm under the BK/BF plates). Owner to decide (maybe after the FEA, D-81).
- **EG design review: done** (`docs/review-eg-design-report.md`). The owner's decisions on it are D-114 … D-123 (smaller cores, open 5 mm rail-seat recesses, 20 mm joint bars, Ampreg 30 with post-cure, insert preparation, 3-point base support, hand tamping first, doc fixes). Not acted on yet: the review's tests (they go in task 6) and its lower-severity notes (gap grading fallback GCL 1–3 mm, mould deck).

Then: rail-seat levelling and assembly procedures, Phase 2 detailing (ATC wheel, enclosure fittings).

## 7. Open questions
`docs/open-questions.md`, in priority order with who answers each. The most urgent:
1. The Ampreg and GCL delivery costs (budget now £4,200, D-127).
2. Ballscrew "Guide Length" and end machining (message drafted in `docs/supplier-messages.md`).
3. Owner's Fusion pass.
4. Safety relay terminal names.
5. AliExpress basket clean-up before wave 1.


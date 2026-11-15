# Open questions (updated 2026-11-15, in priority order)

Resolved items are in decisions.md (D-01 … D-134). **Phase 1 is £3,915.58, every line priced (D-126); the Ampreg and GCL delivery costs, the square and shims (X10, X11) and the M5 × 20 bolts are not in it yet.** Ordered by when the answer is needed (order waves in phase1-schedule.md) and by how costly a wrong answer would be. **Who** says who can answer it: *owner* (you), *session* (Claude, from here), or *bench* (only the hardware can tell). The owner's short list is `owner-todo.txt`.

## Before wave 1 (4 Jan 2027)

1. **USB-RS485 adapter (E24):** check the Waveshare photos show A+/B-/GND screw terminals before ordering.
   Who: owner, on the AliExpress page.
2. **AliExpress basket clean-up**: remove the 6 mm ID tube; check the 12 ferrule packs, the HSC8 16-6 crimper, the 20/14 AWG wire. Add S08 + S05 to the wave 1 basket (D-94) and re-check the S08 price.
   Who: owner, logged in to AliExpress.
3. **Safety relay terminal names** (S11/S12, S21/S22, S33/S34, 13-14, 23-24, 33-34). The product datasheet confirms 3 NO safety outputs but doesn't show the terminals.
   Who: owner, from the label or the wiring sheet in the box (or a photo of it for the session to check). Needed before wiring the cabinet in weeks 3–6.

## Before wave 2 (15 Feb 2027)

4. **Fusion review of the assembly (task 09):** open `cad/v2/out/assembly/type0_assembly.step` (vendor models already in, D-111), detail the brackets, plates and sensor mounts, check the VERIFY list in `docs/assembly.md`, and save the STEP to `cad/v2/in/`. The mould drawings (tasks 10–12) start from it.
   Who: owner (Fusion 360).
4a. **Rail bolts M5 × 20, square and shims (task 05, D-133, D-134):** M5 × 16 is too short with the 5 mm resin seat; X03 becomes 100 × M5 × 20 grade 12.9. Add the engineer's square (X10) and shim stock (X11) to the parts list. UK prices are in `price-check-task-15.md`; the owner checks AliExpress first. VERIFY the bolt length against the rail's counterbore when the rails arrive.
   Who: owner (AliExpress reply), then session updates `bom.csv`.
4b. **Opus branch** (`claude/awesome-ramanujan-by9kds`): started from the 8 Nov state, so its LinuxCNC config, bench, moulds and mix plan are for the old design and its D-92 … D-98 clash with this branch. Not merged. Its mould-drawing script (`cad/v2/moulds.py` there) is a starting point for task 10, to be re-driven from `assembly.py`.
   Who: session, with the mould drawings.

5. **Z motor mount (M13):** ask the AliExpress seller for the HM12-60 drawing (`supplier-messages.md` section 4). It must have 4 holes on a 50 mm square and a Ø36 pilot. If not, the session designs a mount from the 10 mm plate.
   Who: owner sends the message.
5b. **Glove size** for the nitrile gloves (X09), and check the torque wrench stock (none in the Swansea stores on 15 Nov; collect next day).
   Who: owner, at order time.

6. **Screwfix Swansea stock is thin** for T13 varnish (1 each at Parc Tawe and Cwmdu Parc) and the 4 × 40 screws (2–3 per store) on 8 Nov. Re-check before 15 Feb, or order for delivery.
    Who: owner, at order time.
7. **T02 foot height** sets the leg length (bench_cutlist.md assumes 30 mm from the floor to the leg bottom). T02 is in wave 2, so cut the legs after the feet arrive.
    Who: owner, measure the feet.
8. **Reservoir:** 20 L bucket, no radiator (D-135). Measure it when it arrives (bench drawing assumes 300 × 300 × 370 high) and check the kit pump sits in it.
    Who: owner.
9. **Ballscrew "Guide Length"** (before wave 2, D-103): overall or thread length? The assembly needs **overall X 823, Y 582, Z ≈ 350** (D-111): buy X 850 / Y 600 / Z 350; still confirm the end machining. A wrong answer means unusable screws.
   Who: owner, message to the seller. Draft in `supplier-messages.md` (section 1).

## Before wave 3 and the moulds (1 Mar 2027)

10. **Owner FEA on the base (80.2 kg)** to remove material (D-81), and **adopt the proposed base PVC cores or not** (5 × Ø50, about −9.6 kg: `cad/v2/out/base_cores_plan.png`). Either changes the base mould.
   Who: owner. The base STEP is `cad/v2/out/assembly/base_casting.step`.
11. **Ampreg 30 delivery cost to SA2 and shelf life** (EC Fibreglass), and the Easy Composites delivery charge now that only the release agents (F12) come from there.
   Who: owner. Draft in `supplier-messages.md` (section 5).
11c. **Review the test plan** (`docs/eg-mix-test-plan.md`): pass marks, number of pieces, and:
   - Kit and tent parts are priced (price check 14, D-126).
   - Epoxy margin: one kit covers up to 12 %; at 13 % a small top-up pack is needed.
   Who: owner.
12. **GCL delivery cost to SA2** for 3 × 25 kg quartz, and **Hancock & Brown** collection of 3 × 20 kg sand.
   Who: owner. Drafts in `supplier-messages.md` (sections 2 and 3).
13. **Curing heat: confirm with the heat brick** (`eg-mix-test-plan.md`, piece C). Estimate: centre 30–50 °C (D-124).
   Who: owner casts and logs the brick in weeks 12–13.

## Before wave 4 (29 Mar 2027)

14. **Aluminium Warehouse: free delivery to SA2** (order ≥ £150 ex VAT)?
   Who: owner. Put M11, M12 and A06 in the basket and read the delivery line at checkout.
15. **Epoxy confirmed by test bricks** (Ampreg 30 + 3X Slow, D-122), weeks 12–13.
   Who: owner, with the bricks; the session writes the mix and test plan first (task 6).

## Electrical bench tests (weeks 3–6, and when the spindle kit arrives)

16. **Drive and Mesa CHECKs** (docs/linuxcnc.md section 6). Manuals answered most of them (electrical.md section 5); left for the bench:
    - CL57T **ENA logic** with sourcing wiring (manual suggests 24 V = disabled → `output-00-invert 1`).
    - CL57T **ALM polarity** (`input-0N` or `-not`).
    - **V4.1 manual** in the box: same timing, DIP table and signal levels as the V3.0 manual used here?
    - 7I76EU **`source`/`sink` parameters** exist under `hm2_7i76e.0.7i76.0.0` on first start.
    Who: bench, following the procedure.
17. **VFD parameters** (PD001/002/141–144/163–165) against the kit's VFD manual.
    Who: owner, from the manual in the box. Then bench test part E.

## During the build

18. **Flow switch (S05) contact rating** for a 24 V DC Mesa input. Needed before wiring (week 25).
    Who: owner, ask the AliExpress seller; else bench. A reed switch carrying the Mesa input's few mA at 24 V is normally fine (7I76EU input: 10 kΩ, about 2.4 mA).
19. **Spindle minimum rpm** (config uses 6,000).
    Who: owner, from the spindle's sheet or label.
20. **Y home switch position**: at the table's front-most position (+Y in machine terms)?
    Who: owner. Needed before making the sensor brackets.

## Phase 2 (no deadline yet)

21. **Jianken ATC spindle**: torque 0.7 vs 0.87 Nm, pull-stud spec, PNP sensors, import VAT.
    Who: owner, email to Jianken.
22. **B&Q Swansea stock: 12 mm MDF** (enclosure).
    Who: owner, B&Q website stock checker.

## Closed since the last list
- Phase 1 simplification: no stripping, no granite plate; castings keep their features (D-131). Assembly in pictures: `assembly-steps.md`, clear to the owner (D-133).
- Portal joint: bolted dry on shims, no grout, no dowels; re-squared with an engineer's square after each move (D-128, D-132, D-133). Dowel sleeves removed from the CAD (task 04).
- Post-cure and tent stay (D-129). Nothing taken from the Opus branch (D-130).
- Wave 1 order sheet: `wave1-order-sheet.md` (task 15).
- Budget raised to £4,200 (D-127).
- Price checks 12 and 14 applied (D-126).
- Price check 13: Ampreg 30 + 3X Slow chosen (D-122); F20 priced; hand tamping first, no vibration motor or speed controller (D-123).
- Base pads lift the machine 10 mm: accepted, enclosure unchanged, top gap 30 mm (D-121).
- EG design review: done, decisions D-114 … D-120 (portal cores, rail-seat recesses, joint bars, resin, inserts, base pads).
- Portal beam overhang deflection: negligible (D-95).
- Z brake hardwiring: done (D-93).
- VFD driver: USB-RS485 + hy_vfd (D-92).
- Spindle kit timing vs the VFD bench test: kit moved to wave 1 (D-94).
- E23/E24/E25 and the bench materials priced (D-98, D-99).
- X screw packaging, spine cover, spindle line, folded X/Y drives, Z drive (full assembly, D-104 … D-109).
- Vendor STEP models swapped into the assembly (D-111).
- Curing heat: estimate done, not the main risk (D-96); test-brick confirmation is still open below.
- CL57T step/dir/ENA signal levels, step timing, DIP setting for 1,600 pulses/rev; XPSAC5121 output rating; 7I76EU output mode: from the manuals (electrical.md).

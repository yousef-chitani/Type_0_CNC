# Open questions (updated 2026-11-09, in priority order)

Resolved items are in decisions.md (D-01 … D-124). **Phase 1 £3,327.57 is provisional until price check 12 (D-110) and the Ampreg 30 delivery cost.** Ordered by when the answer is needed (order waves in phase1-schedule.md) and by how costly a wrong answer would be. **Who** says who can answer it: *owner* (you), *session* (Claude, from here), or *bench* (only the hardware can tell).

## Before wave 1 (4 Jan 2027)

1. **USB-RS485 adapter (E24):** check the Waveshare photos show A+/B-/GND screw terminals before ordering.
   Who: owner, on the AliExpress page.
2. **AliExpress basket clean-up**: remove the 6 mm ID tube; check the 12 ferrule packs, the HSC8 16-6 crimper, the 20/14 AWG wire. Add S08 + S05 to the wave 1 basket (D-94) and re-check the S08 price.
   Who: owner, logged in to AliExpress.
3. **Safety relay terminal names** (S11/S12, S21/S22, S33/S34, 13-14, 23-24, 33-34). The product datasheet confirms 3 NO safety outputs but doesn't show the terminals.
   Who: owner, from the label or the wiring sheet in the box (or a photo of it for the session to check). Needed before wiring the cabinet in weeks 3–6.

## Before wave 2 (15 Feb 2027)

4. **Fusion review of the assembly (task 4):** open `cad/v2/out/assembly/type0_assembly.step` (vendor models already in, D-111), detail the brackets, plates and sensor mounts, check the VERIFY list in `docs/assembly.md`, and send back the STEP. The moulds (task 5) start from it.
   Who: owner (Fusion 360).
5. **Price check 12** (`docs/price-check-task-12.md`): new screw lengths, flat bars, plates, Z motor mount (50 mm hole spacing), HTD pulleys and belts, outboard bearing.
   Who: owner, local price check.

6. **Screwfix Swansea stock is thin** for T13 varnish (1 each at Parc Tawe and Cwmdu Parc) and the 4 × 40 screws (2–3 per store) on 8 Nov. Re-check before 15 Feb, or order for delivery.
    Who: owner, at order time.
7. **T02 foot height** sets the leg length (bench_cutlist.md assumes 30 mm from the floor to the leg bottom). T02 is in wave 2, so cut the legs after the feet arrive.
    Who: owner, measure the feet.
8. **Reservoir size** for the cooling loop (not chosen yet): the bench leaves about 160 wide × 300 deep × 200 high at the back right of the shelf.
    Who: owner, when the S08 kit arrives (its pump size).
9. **Ballscrew "Guide Length"** (before wave 2, D-103): overall or thread length? The assembly needs **overall X 823, Y 582, Z ≈ 350** (D-111): buy X 850 / Y 600 / Z 350; still confirm the end machining. A wrong answer means unusable screws.
   Who: owner, message to the seller. Draft in `supplier-messages.md` (section 1).

## Before wave 3 and the moulds (1 Mar 2027)

10. **Owner FEA on the base (80.2 kg)** to remove material (D-81), and **adopt the proposed base PVC cores or not** (5 × Ø50, about −9.6 kg: `cad/v2/out/base_cores_plan.png`). Either changes the base mould.
   Who: owner. The base STEP is `cad/v2/out/assembly/base_casting.step`.
11. **Ampreg 30 delivery cost to SA2** (EC Fibreglass shows it only at checkout), and the Easy Composites delivery charge now that only the release agents (F12) come from there.
   Who: owner, in the basket (stop before payment).
11c. **Review the test plan** (`docs/eg-mix-test-plan.md`): pass marks, number of pieces, and:
   - **A third bag of quartz 2–5 mm** (F03 2 → 3): two bags don't cover the castings at 50 % coarse, let alone the tests.
   - Test blend P4 with a bag of GCL 1–3 mm, or only P1–P3?
   - Which kit you already own (scales, 500 mm straightedge + feeler gauges, torque wrench 20–50 N·m, angle grinder + diamond disc, PPE). The rest, plus the PIR board, heater and thermostat (D-124), go into a small price check.
   - Epoxy margin: one kit covers up to 12 %; at 13 % a small top-up pack is needed.
   Who: owner.
12. **GCL delivery cost to SA2** for 2 × 25 kg quartz, and **Hancock & Brown** collection of 3 × 20 kg sand.
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

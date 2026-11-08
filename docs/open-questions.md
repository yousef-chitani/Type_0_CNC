# Open questions (updated 2026-11-08, in priority order)

Resolved items are in decisions.md (D-01 … D-99). **Every Phase 1 BOM line is now priced: £3,331.37.** Ordered by when the answer is needed (order waves in phase1-schedule.md) and by how costly a wrong answer would be. **Who** says who can answer it: *owner* (you), *session* (Claude, from here), or *bench* (only the hardware can tell).

## Before wave 1 (4 Jan 2027)

1. **USB-RS485 adapter (E24):** check the Waveshare photos show A+/B-/GND screw terminals before ordering.
   Who: owner, on the AliExpress page.
2. **AliExpress basket clean-up**: remove the 6 mm ID tube; check the 12 ferrule packs, the HSC8 16-6 crimper, the 20/14 AWG wire. Add S08 + S05 to the wave 1 basket (D-94) and re-check the S08 price.
   Who: owner, logged in to AliExpress.
3. **Safety relay terminal names** (S11/S12, S21/S22, S33/S34, 13-14, 23-24, 33-34). The product datasheet confirms 3 NO safety outputs but doesn't show the terminals.
   Who: owner, from the label or the wiring sheet in the box (or a photo of it for the session to check). Needed before wiring the cabinet in weeks 3–6.

## Before wave 2 (15 Feb 2027)

4. **Screwfix Swansea stock is thin** for T13 varnish (1 each at Parc Tawe and Cwmdu Parc) and the 4 × 40 screws (2–3 per store) on 8 Nov. Re-check before 15 Feb, or order for delivery.
    Who: owner, at order time.
5. **T02 foot height** sets the leg length (bench_cutlist.md assumes 30 mm from the floor to the leg bottom). T02 is in wave 2, so cut the legs after the feet arrive.
    Who: owner, measure the feet.
6. **Reservoir size** for the cooling loop (not chosen yet): the bench leaves about 160 wide × 300 deep × 200 high at the back right of the shelf.
    Who: owner, when the S08 kit arrives (its pump size).

## Before wave 3 and the moulds (1 Mar 2027)

7. **Owner FEA on the base (72 kg)** to remove material (D-81). It changes the base mould.
   Who: owner. The session can export the base as STEP with the load cases and fixed points written down.
8. **GCL delivery cost to SA2** for 2 × 25 kg quartz, and **Hancock & Brown** collection of 3 × 20 kg sand.
   Who: owner. Drafts in `supplier-messages.md` (sections 2 and 3).
9. **Curing heat: confirm with a full-thickness test brick**, and decide on a **post-cure** (16 h at 50 °C raises the softening point from 39 to 47 °C). Heater + thermostat to add to the BOM.
   Who: session writes the plan (handover task 5); owner casts and logs the brick. See `curing-heat.md` (D-96).

## Before wave 4 (29 Mar 2027)

10. **Ballscrew "Guide Length"**: overall or thread length? (needs overall ≥ X 725 / Y 405 / Z 305). A wrong answer means unusable screws.
   Who: owner, message to the seller. Draft in `supplier-messages.md` (section 1).
11. **Aluminium Warehouse: free delivery to SA2** (order ≥ £150 ex VAT)?
   Who: owner. Put M11, M12 and A06 in the basket and read the delivery line at checkout.
12. **Epoxy confirmed by test bricks** (GlassCast 50 PLUS, D-84), weeks 12–13.
   Who: owner, with the bricks; the session writes the mix and test plan first (task 5).

## Electrical bench tests (weeks 3–6, and when the spindle kit arrives)

13. **Drive and Mesa CHECKs** (docs/linuxcnc.md section 6). Manuals answered most of them (electrical.md section 5); left for the bench:
    - CL57T **ENA logic** with sourcing wiring (manual suggests 24 V = disabled → `output-00-invert 1`).
    - CL57T **ALM polarity** (`input-0N` or `-not`).
    - **V4.1 manual** in the box: same timing, DIP table and signal levels as the V3.0 manual used here?
    - 7I76EU **`source`/`sink` parameters** exist under `hm2_7i76e.0.7i76.0.0` on first start.
    Who: bench, following the procedure.
14. **VFD parameters** (PD001/002/141–144/163–165) against the kit's VFD manual.
    Who: owner, from the manual in the box. Then bench test part E.

## During the build

15. **Flow switch (S05) contact rating** for a 24 V DC Mesa input. Needed before wiring (week 25).
    Who: owner, ask the AliExpress seller; else bench. A reed switch carrying the Mesa input's few mA at 24 V is normally fine (7I76EU input: 10 kΩ, about 2.4 mA).
16. **Spindle minimum rpm** (config uses 6,000).
    Who: owner, from the spindle's sheet or label.
17. **Y home switch position**: at the table's front-most position (+Y in machine terms)?
    Who: owner. Needed before making the sensor brackets.

## Phase 2 (no deadline yet)

18. **Jianken ATC spindle**: torque 0.7 vs 0.87 Nm, pull-stud spec, PNP sensors, import VAT.
    Who: owner, email to Jianken.
19. **B&Q Swansea stock: 12 mm MDF** (enclosure).
    Who: owner, B&Q website stock checker.

## Closed since the last list
- Portal beam overhang deflection: negligible (D-95).
- Z brake hardwiring: done (D-93).
- VFD driver: USB-RS485 + hy_vfd (D-92).
- Spindle kit timing vs the VFD bench test: kit moved to wave 1 (D-94).
- E23/E24/E25 and the bench materials priced (D-98, D-99).
- Curing heat: estimate done, not the main risk (D-96); test-brick confirmation is item 6.
- CL57T step/dir/ENA signal levels, step timing, DIP setting for 1,600 pulses/rev; XPSAC5121 output rating; 7I76EU output mode: from the manuals (electrical.md).

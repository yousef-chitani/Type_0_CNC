# Open questions (updated 2026-11-15)

Resolved items are in decisions.md (D-01 … D-98).

## Before ordering (Phase 1, wave 1 on 4 Jan 2027)
1. AliExpress METALWORK ballscrews: is "Guide Length" overall or thread length? (needs overall ≥ X 725 / Y 405 / Z 305)
2. Aluminium Warehouse: free delivery for SA2 at checkout (order ≥ £150 ex VAT)?
3. Flow switch (S05): contact rating suitable for a 24 V DC Mesa input?
4. B&Q Swansea stock: 12 mm MDF (enclosure, Phase 2). GCL pallet delivery cost to Swansea. Hancock & Brown collection.
5. Price check 10 (docs/price-check-task-10.md): E23 pump relay, E24 USB-RS485 adapter, bench timber and fixings (T03–T07), mould sundries (F19–F22).
6. AliExpress basket clean-up (6 mm ID tube, 12 ferrule packs, HSC8 16-6 crimper, 20/14 AWG wire).
7. Jianken (Phase 2 ATC spindle): torque 0.7 vs 0.87 Nm, pull-stud spec, PNP sensors, import VAT.

## Design
8. Epoxy: GlassCast 50 PLUS chosen (D-84). Confirm with test bricks (slow clear casting resin).
9. Curing heat in solid castings and the cold shed (heater + insulated cover; probes).
10. Owner FEA on the base (72 kg) to remove material (D-81).
11. Portal beam overhang (160 mm) deflection with the saddle at the ATC pickup.
12. Wiring CHECKs in electrical.md (XPSAC5121 terminals, CL57T ENA/ALM, VFD parameters) and the CHECK items in docs/linuxcnc.md (7I76EU support in LinuxCNC 2.9, pin names, output mode).
13. ~~LinuxCNC Modbus driver~~: resolved, USB-RS485 + hy_vfd (D-92).
14. **Portal relocation feature** (grout keys, dowels, bolts only, or studs as locators): owner asked for an independent assessment. Options in moulds.md. Must be decided before the base mould is built (week 9).
15. **Enclosure width:** the X motor sticks out about 170 mm past the beam end. The enclosure (D-87) must grow to about 1,030 inside / 1,054 outside, or the motor must fold back. The bench is already 1,100 wide for this (D-97). VERIFY the overhang when the motor and mount arrive.
16. **Release agent:** wax then PVA (eg-moulds.md) or not (Easy Composites, F12 note)? The test bricks try wax only, PVA only and both (eg-mix.md).
17. VERIFY on the wave 2 parts before marking out the moulds: rail hole pitch and end distance, X nut housing width (≤ 56 mm), BK12/BF12 heights (the Y BK12 needs about 10 mm of spacer), Y-screw channel end, rail counterbore depth (M5 × 20 rail bolts).

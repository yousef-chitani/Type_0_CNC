# Open questions (updated at handover, 2026-11-08)

Resolved items are in decisions.md (D-01 … D-91).

## Before ordering (Phase 1, wave 1 on 4 Jan 2027)
1. AliExpress METALWORK ballscrews: is "Guide Length" overall or thread length? (needs overall ≥ X 725 / Y 405 / Z 305)
2. Aluminium Warehouse: free delivery for SA2 at checkout (order ≥ £150 ex VAT)?
3. Flow switch (S05): contact rating suitable for a 24 V DC Mesa input?
4. B&Q Swansea stock: 12 mm MDF (enclosure, Phase 2). GCL pallet delivery cost to Swansea. Hancock & Brown collection.
5. E23 pump relay: price at RS.
6. AliExpress basket clean-up (6 mm ID tube, 12 ferrule packs, HSC8 16-6 crimper, 20/14 AWG wire).
7. Jianken (Phase 2 ATC spindle): torque 0.7 vs 0.87 Nm, pull-stud spec, PNP sensors, import VAT.

## Design
8. Epoxy: GlassCast 50 PLUS chosen (D-84). Confirm with test bricks (slow clear casting resin).
9. Curing heat in solid castings and the cold shed (heater + insulated cover; probes).
10. Owner FEA on the base (72 kg) to remove material (D-81).
11. Portal beam overhang (160 mm) deflection with the saddle at the ATC pickup.
12. Wiring CHECKs in electrical.md (XPSAC5121 terminals, CL57T ENA/ALM, VFD parameters).
13. LinuxCNC driver for Modbus over the 7I76EU RS-485 port (task 2). Fallback: USB-RS485 + hy_vfd.

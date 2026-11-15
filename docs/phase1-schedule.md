# Phase 1 schedule (D-90)

**4 January 2027 → 22 July 2027** (28 weeks, about 5 h/week ≈ 140 h). **Done = the machine moves under LinuxCNC.** Built and run in the shed for now (the flat limits apply when moving out).

Castings are planned for April–May: epoxy needs **≥ 18 °C** for its 7-day cure. Use a heater and an insulated cover in the shed if it is colder. Test bricks can cure indoors.

## Plan

| Weeks | Dates | Work | About h |
|---|---|---|---|
| 1–2 | 04 Jan – 17 Jan | Order wave 1. Install LinuxCNC on the mini-PC, latency test, connect the Mesa 7i76EU | 10 |
| 3–6 | 18 Jan – 14 Feb | Electrical cabinet: DIN layout, PSUs, isolator/MCBs, e-stop safety chain, contactor, drivers. Bench-test all 3 motors + VFD (Modbus) from LinuxCNC on the bench | 20 |
| 7–8 | 15 Feb – 28 Feb | Order wave 2. Build the timber bench (docs/bench.md). When the rails and screws arrive, check them against the mould drawings and re-run `cad/v2/moulds.py` | 10 |
| 9–11 | 01 Mar – 21 Mar | Order wave 3. Build the base and portal moulds (MDF, CLS, insert bars on jig bolts, Y-screw channel, PVC cores, sleeves). Build the tyre vibration table | 15 |
| 12–13 | 22 Mar – 04 Apr | Void test, then 3 test bricks (docs/eg-mix.md), cure indoors 7 days, cut and inspect. Fix the mix. Order wave 4 | 10 |
| 14 | 05 Apr – 11 Apr | Order wave 5 (spindle kit). Final mould prep, release wax + PVA | 5 |
| 15–16 | 12 Apr – 25 Apr | Cast the BASE (heater if < 18 °C), 7-day cure, demould | 8 |
| 17–18 | 26 Apr – 09 May | Cast the PORTAL, 7-day cure, demould. Inspect both castings | 8 |
| 19–20 | 10 May – 23 May | Rail-seat levelling pours (base Y seats, portal X seats), 7-day cure | 8 |
| 21–22 | 24 May – 06 Jun | Y axis: rails, screw, motor, table. Portal onto the base: shim square to Y, grout, cure, ream dowels | 10 |
| 23–24 | 07 Jun – 20 Jun | X and Z axes: rails, screws, saddle, Z plate, brake motor, spindle clamp + spindle (wave 5 arrives) | 10 |
| 25–26 | 21 Jun – 04 Jul | Machine wiring to the cabinet: motor cables, homing sensors, e-stops, spindle + cooling loop, flow switch | 10 |
| 27–28 | 05 Jul – 18 Jul | LinuxCNC config: axes, steps, homing, soft limits, spindle via Modbus. Jog all axes. **Done 22 July** | 10 |
| | | **Total** | **134** |

## Order waves (spread across Phase 1)

| Wave | Order in week | Date | What | £ |
|---|---|---|---|---|
| 1 | 1 | 04 Jan 2027 | Electrical and motors (bench-test indoors): E01, E04, E05, E06, E07, E08, E09, E10, E12, E13, E14, E17, E18, E21, E23, E24, S04, M09, M10, M14 | £1,069.17 + E23, E24 to price |
| 2 | 7 | 15 Feb 2027 | Bench, moulds and local items (B&Q, Screwfix): F10, F11, F17, F18, F08, F09, F19–F22, X03, T02–T07. **Plus the X and Y rails and the ballscrew kits (M01, M02, M05, D-93)**, so their hole positions and the nut housing are in hand before the moulds are built | £615.12 + F19–F22, T03–T07 to price |
| 3 | 9 | 01 Mar 2027 | Casting materials and measuring tools: F01, F02, F12, F03 (3 bags, D-98), F04, F06, F07, X01, X02 | £530.94 |
| 4 | 13 | 29 Mar 2027 | Remaining motion parts and plates: M03, M08, M13, M11, M12 | £437.03 |
| 5 | 14 | 05 Apr 2027 | Spindle kit, collets and cooling (about 8 weeks shipping): S08, S09, S05 | £413.02 |
| | | | **Total priced** | **£3,065.28** (11 lines to price: price-check-task-10.md) |

The 5 V PSU (E22) is shelved (D-91) and no longer in wave 1. Earlier totals (£3,066.41) still counted it.

Owner-built or DIY (no cost): timber bench, vibration table, temperature logging, PC, monitor.

## Watch points
- **Mesa 7i76EU:** £257.74 including import VAT, ordered in wave 1 (week 1). Needed first for the LinuxCNC bench tests.
- **Spindle kit:** order by week 14. Shipping was quoted at about 8 weeks, and it's needed in week 23.
- **AliExpress motion parts:** rails and screws in week 7 (D-93), the rest by week 13 to arrive by week 21 (2–6 weeks).
- **Test bricks need about 10 days** (mix, 7-day cure, cut). Start them as soon as wave 3 arrives, before the moulds are finished.
- **Cold:** if the shed is below 18 °C, cure under an insulated cover with a small heater, and check with the temperature probes.
- **Slack:** about 1 week of buffer, inside weeks 27–28.

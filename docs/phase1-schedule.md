# Phase 1 schedule (D-90)

**4 January 2027 → 22 July 2027** (28 weeks, about 5 h/week ≈ 140 h). **Done = the machine moves under LinuxCNC.** Built and run in the shed for now (the flat limits apply when moving out).

Castings are planned for April–May: GlassCast 50 PLUS needs **17–23 °C, ideally 20 °C**, for its 7-day cure (9 days at 17 °C). See curing-heat.md. Use a heater and an insulated cover in the shed if it is colder. Test bricks can cure indoors.

## Plan

| Weeks | Dates | Work | About h |
|---|---|---|---|
| 1–2 | 04 Jan – 17 Jan | Order wave 1. Install LinuxCNC on the mini-PC, latency test, connect the Mesa 7i76EU | 10 |
| 3–6 | 18 Jan – 14 Feb | Electrical cabinet: DIN layout, PSUs, isolator/MCBs, e-stop safety chain, contactor, drivers. Bench-test all 3 motors from LinuxCNC on the bench (docs/linuxcnc.md section 6, parts A–D) | 20 |
| 7–8 | 15 Feb – 28 Feb | Order wave 2. Build the timber bench (top 785 mm, D-97: cad/v2/out/bench_cutlist.md, about 6–8 h). Mould design check against the model | 10 |
| (on arrival, about week 9–10) | early March | Spindle kit (ordered in wave 1, about 8–9 weeks shipping): bench-test the VFD, spindle and cooling loop from LinuxCNC (docs/linuxcnc.md section 6, part E). About 2 h, fits beside the mould work | (2) |
| 9–11 | 01 Mar – 21 Mar | Order wave 3. Build the base and portal moulds (MDF, CLS, insert bars on jig bolts, Y-screw channel, PVC cores, sleeves). Build the tyre vibration table | 15 |
| 12–13 | 22 Mar – 04 Apr | Test bricks: 2–3 mixes (GlassCast + quartz/sand/whiting), cure indoors, break and inspect. Fix the mix. Order wave 4 | 10 |
| 14 | 05 Apr – 11 Apr | Final mould prep, release wax + PVA | 5 |
| 15–16 | 12 Apr – 25 Apr | Cast the BASE (insulated tent + thermostat heater at 20 °C), 7-day cure, demould | 8 |
| 17–18 | 26 Apr – 09 May | Cast the PORTAL, 7-day cure, demould. Inspect both castings | 8 |
| 19–20 | 10 May – 23 May | Rail-seat levelling pours (base Y seats, portal X seats), 7-day cure | 8 |
| 21–22 | 24 May – 06 Jun | Y axis: rails, screw, motor, table. Portal onto the base: shim square to Y, grout, cure, ream dowels | 10 |
| 23–24 | 07 Jun – 20 Jun | X and Z axes: rails, screws, saddle, Z plate, brake motor, spindle clamp + spindle | 10 |
| 25–26 | 21 Jun – 04 Jul | Machine wiring to the cabinet: motor cables, homing sensors, e-stops, spindle + cooling loop, flow switch | 10 |
| 27–28 | 05 Jul – 18 Jul | LinuxCNC on the machine (config already written, D-92): directions, steps, homing, soft limits, spindle. Jog all axes. **Done 22 July** | 10 |
| | | **Total** | **134** |

## Order waves (spread across Phase 1, D-94)

| Wave | Order in week | Date | What | £ |
|---|---|---|---|---|
| 1 | 1 | 04 Jan 2027 | Electrical, motors, **spindle kit and cooling loop** (bench-test indoors): E01, E04, E05, E06, E07, E08, E09, E10, E12, E13, E14, E17, E18, E21, **E23, E24, E25**, **T14** (fan grills), S04, **S08, S05**, M09, M10, M14 | £1,489.55 |
| 2 | 7 | 15 Feb 2027 | Bench, moulds and local items (B&Q, Screwfix): F10, F11, F17, F18, F08, F09, X03, T02, **T03–T07, T09–T13, T15** (bench, D-99: B&Q Swansea with in-store ply cutting, Screwfix, B&Q marketplace, AliExpress) | £500.06 |
| 3 | 9 | 01 Mar 2027 | Casting materials and measuring tools: F01, F02, F12, F03, F04, F06, F07, X01, X02 | £516.42 |
| 4 | 13 | 29 Mar 2027 | Motion parts, plates, ER20 collets: M01, M02, M03, M05, M08, M13, M11, M12, S09 | £829.66 |
| | | | **Total** | **£3,335.69** |

Wave 5 is gone (D-94): the spindle kit and cooling loop moved to wave 1 so the VFD can be bench-tested early, and the collets (S09) joined wave 4. E22 (5 V PSU) is shelved (D-91) and no longer ordered.

Owner-built or DIY (no cost apart from materials): timber bench (materials T03–T15), vibration table, temperature logging, PC, monitor.

## Watch points
- **Mesa 7i76EU:** £257.74 including import VAT, ordered in wave 1 (week 1). Needed first for the LinuxCNC bench tests.
- **Spindle kit:** ordered in wave 1 (D-94). Shipping was quoted at about 8–9 weeks, so it should arrive in early March, well before it is mounted in week 23. Check the price is still £217.39 + shipping when ordering.
- **AliExpress motion parts:** order by week 13 to arrive by week 21 (2–6 weeks).
- **Cold:** cure inside an insulated tent with a 150–300 W thermostat heater set to 20 °C, and log with the temperature probes (curing-heat.md).
- **Slack:** about 1 week of buffer, inside weeks 27–28.

# Phase 1 schedule (D-90)

**4 January 2027 → 22 July 2027** (28 weeks, about 5 h/week ≈ 140 h). **Done = the machine moves under LinuxCNC.** Built and run in the shed for now (the flat limits apply when moving out).

Castings are planned for April–May: the epoxy needs about **20 °C** to cure, then a post-cure in the tent (D-117; times from the chosen resin's datasheet, see curing-heat.md). Use a heater and an insulated cover in the shed if it is colder. Test bricks can cure indoors.

## Plan

| Weeks | Dates | Work | About h |
|---|---|---|---|
| 1–2 | 04 Jan – 17 Jan | Order wave 1. Install LinuxCNC on the mini-PC, latency test, connect the Mesa 7i76EU | 10 |
| 3–6 | 18 Jan – 14 Feb | Electrical cabinet: DIN layout, PSUs, isolator/MCBs, e-stop safety chain, contactor, drivers. Bench-test all 3 motors from LinuxCNC on the bench (docs/linuxcnc.md section 6, parts A–D) | 20 |
| before 1 | Nov – Dec 2026 | **Full CAD assembly (task 4, D-102)**: first version done (`docs/assembly.md`); refine in Fusion and send back, then mould drawings (task 5) | (owner review) |
| 7–8 | 15 Feb – 28 Feb | Order wave 2 (now includes the motion parts, D-103). Build the timber bench (top 785 mm, D-97: cad/v2/out/bench_cutlist.md, about 6–8 h) | 10 |
| (on arrival, about week 9–10) | early March | Spindle kit (ordered in wave 1, about 8–9 weeks shipping): bench-test the VFD, spindle and cooling loop from LinuxCNC (docs/linuxcnc.md section 6, part E). About 2 h, fits beside the mould work | (2) |
| 9–11 | 01 Mar – 21 Mar | Order wave 3. **Measure the received rails, screws, BK/BF supports and nut housings against the assembly; correct the mould drawings if needed.** Build the base and portal moulds (MDF, CLS, insert bars on jig bolts, Y-screw channel, PVC cores, sleeves). Build the tyre vibration table | 15 |
| 12–13 | 22 Mar – 04 Apr | Mix bricks only (D-160, `eg-mix-test-plan.md`): A1–A4 at 10–13 % epoxy (Ampreg 30, blend P1, hand-tamped), judged on surface and voids. Fix the mix. Order wave 4 | 10 |
| 14 | 05 Apr – 11 Apr | Final mould prep, release as tested (D-120) | 5 |
| 15–16 | 12 Apr – 25 Apr | Cast the BASE (tent + thermostat at 20 °C), 48 h or more at ≥ 18 °C, post-cure 16 h at 50 °C, cool, demould (curing-heat.md) | 8 |
| 17–18 | 26 Apr – 09 May | Cast the PORTAL, same cure and post-cure, demould. Inspect both castings | 8 |
| 19–20 | 10 May – 23 May | Rail-seat levelling pours (base Y seats, portal X seats), cure, post-cure, measure, shim or scrape | 8 |
| 21–22 | 24 May – 06 Jun | Y axis: rails, screw, motor, table. Portal onto the base: bolt on dry, shim the feet, square X to Y (D-132, D-133) | 10 |
| 23–24 | 07 Jun – 20 Jun | X and Z axes: rails, screws, saddle, Z plate, brake motor, spindle clamp + spindle | 10 |
| 25–26 | 21 Jun – 04 Jul | Machine wiring to the cabinet: motor cables, homing sensors, e-stops, spindle + cooling loop, flow switch | 10 |
| 27–28 | 05 Jul – 18 Jul | LinuxCNC on the machine (config already written, D-92): directions, steps, homing, soft limits, spindle. Jog all axes. **Done 22 July** | 10 |
| | | **Total** | **134** |

## Order waves (spread across Phase 1, D-94)

| Wave | Order in week | Date | What | £ |
|---|---|---|---|---|
| 1 | 1 | 04 Jan 2027 | Electrical, motors, **spindle kit and cooling loop** (bench-test indoors): E01, E04, E05, E06, E07, E08, E09, E10, E12, E13, E14, E17, E18, E21, **E23, E24, E25**, S04, **S08, S05**, M09, M10, M14, **M01, M02, M03, M05, M08, M13** (LiMo motion parts, C5, DDP sea, D-136) | £2,099.52 (Checkout7: HGH20CA 600 $43.33, DDP sea $129; fourth coupling, D-182) |
| 2 | 7 | 15 Feb 2027 | Bench, moulds, local items (motion parts moved to wave 1, D-136): F10, F11, F17, F18, F09, X03, T02, **T03–T07, T09–T13** (bench, D-99: B&Q Swansea with in-store ply cutting, Screwfix, B&Q marketplace, AliExpress), **F07** (flat bars, Metal Store; F20 dropped, D-159) | £508.43 (F08, F20 dropped, D-159; M15–M17 dropped, D-182) |
| 3 | 9 | 01 Mar 2027 | Casting materials, test kit, curing tent and measuring tools: F01, F02, F12, F03, F04, F06, X01, X02, **X05–X10** (straightedge, feeler gauges, grinder; X07 dropped D-161; PPE, engineer's square), **F22–F24** (PIR board, heater, thermostat) | £910.84 (X07 dropped, D-161) |
| 4 | 13 | 29 Mar 2027 | Aluminium plates and ER20 collets: M11, M12, S09 | £438.63 |
| | | | **Total** | **£3,957.42** (excluding 4 lines not priced: G01–G04, JLC gantry, not in a wave yet) |

3D-printed parts (D-100, docs/printed-parts.md): fan grills, cable grommet and e-stop box can be printed any time before the bench is fitted out (week 8).

Wave 5 is gone (D-94): the spindle kit and cooling loop moved to wave 1 so the VFD can be bench-tested early, and the collets (S09) joined wave 4. E22 (5 V PSU) is shelved (D-91) and no longer ordered.

Owner-built or DIY (no cost apart from materials): timber bench (materials T03–T15), vibration table, temperature logging, PC, monitor.

## Watch points
- **Mesa 7i76EU:** £257.74 including import VAT, ordered in wave 1 (week 1). Needed first for the LinuxCNC bench tests.
- **Spindle kit:** ordered in wave 1 (D-94). Shipping was quoted at about 8–9 weeks, so it should arrive in early March, well before it is mounted in week 23. Check the price is still £217.39 + shipping when ordering.
- **LiMo motion parts (D-136):** ordered in wave 1 (4 Jan), DDP sea 30–45 workdays, so they arrive mid-February to early March, in time to be measured before the moulds are finished in week 11. All three screw types use the standard BK12 end, so no stub drawings are needed (D-157, D-182). If they're late, finish the moulds from the datasheet sizes and check the parts against the moulds before casting (week 14).
- **Cold and post-cure:** cure inside a 50 mm PIR-board tent with a 500 W–1 kW thermostat heater: 20 °C for the first 48 h, then 50 °C for 16 h. Log with the temperature probes (curing-heat.md).
- **Slack:** about 1 week of buffer, inside weeks 27–28.

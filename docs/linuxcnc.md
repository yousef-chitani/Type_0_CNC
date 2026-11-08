# LinuxCNC starter config (task 2)

Config folder: [`linuxcnc/type0/`](../linuxcnc/type0/). LinuxCNC **2.9** (tested on 2.9.10), AXIS screen, mm.
Decisions: D-92. Items marked **CHECK** must be confirmed on the hardware.

## 1. What is in the folder

| File | What |
|---|---|
| `type0.ini` | Machine settings: axes, speeds, homing, soft limits, Mesa address, VFD port, interlock timings (`[TYPE0]`) |
| `hm2.hal` | Mesa 7I76EU only: step generators and the TB6 inputs/outputs, turned into named signals |
| `machine.hal` | E-stop chain, drive enable, Z brake, coolant pump/fans and flow interlock, homing, manual tool change |
| `spindle.hal` | Huanyang VFD through a USB-RS485 adapter (`hy_vfd`) |
| `postgui.hal`, `panel.xml` | Side panel in AXIS: spindle rpm/amps, VFD link, power OK, flow, brake, drive alarms |
| `shutdown.hal`, `tool.tbl` | Exit actions, tool table |
| `type0_sim.ini` + `sim/` | Simulator (no Mesa, no VFD): same `machine.hal`, fake board and VFD. `sim/test_sim.py` checks the logic |

Only `hm2.hal` knows about the Mesa board and only `spindle.hal` knows about the VFD. Everything else uses signal names, so the simulator runs the real interlock logic.

## 2. Settings chosen (D-92)

| Item | Value |
|---|---|
| Steps | CL57T at **1,600 pulses/rev**, 5 mm lead → **320 steps/mm** (0.003 mm per step) |
| Speed (bring-up) | **2 m/min** (33.3 mm/s), accel **200 mm/s²** on every axis. Step rate 10.7 kHz. Raise later in `type0.ini` |
| Homing | Z first (up), then X (to +X, the ATC side) and Y (to +Y) together. Search 10 mm/s (Z 5), latch back-off 1 mm/s (Z 0.5) |
| Machine coordinates | X 0 … 570, Y 0 … 250, Z −150 … 0 (0 = top). Home switch = the upper limit of each axis |
| After homing | X 565, Y 245, Z −2 |
| Spindle | 6,000 … 24,000 rpm (CHECK the minimum on the spindle sheet), M3/M4/M5, waits for "at speed" |
| VFD link | USB-RS485, 9,600 baud, 8N1, address 1 (`[TYPE0]` in `type0.ini`) |
| Tool change | Manual (M6 shows a dialog). Phase 1 ER20 |
| Servo thread | 1 ms (normal for Mesa Ethernet) |

**Y direction CHECK:** +Y means the *tool* moves toward the back of the work, so on this moving-table machine the **table moves toward the front** when Y goes positive. The Y home switch therefore sits where the table is at its front-most position. If you meant the other end, change the Y homing signs (section 7).

## 3. How the safety logic works

The hardwired chain (2 e-stops → XPSAC5121 → contactor) does the actual stopping (D-35). LinuxCNC only reads it and adds software interlocks on top:

- **Can't enable** unless IN3 "machine power OK" (contactor aux) is on.
- **E-stop (latched until you press e-stop reset in AXIS)** on any of: X/Y/Z drive alarm, Mesa watchdog, coolant fault, VFD link fault.
- **Drive enable (OUT0)** follows the machine-on state. **Z brake (OUT1)** releases 0.3 s after the drives enable (so the drive is holding first). On disable, the brake engages at once and the drives stay on 0.15 s more so Z can't drop.
- **Pump (OUT2) and radiator fans (OUT3)** run while the machine is on (or the spindle is on).
- **Coolant interlock:** the flow switch must be on for 2 s before the VFD is allowed to run. If the spindle is on and flow is lost: the VFD is told to stop and the feed is held at once; if it lasts 5 s → e-stop. If you start the spindle within 2 s of machine-on, it simply waits for flow.
- **VFD link:** if the spindle is on and the VFD stops answering for 2 s → e-stop. With the spindle off, a lost link is only shown on the panel.
- **Mesa watchdog:** if the PC stops talking to the board for 5 ms, all outputs switch off (drives disabled, brake engaged, pump relay off).

All timings are in the `[TYPE0]` section of `type0.ini`.

**Z brake is hardwired (D-93):** the brake coil is fed from Mesa OUT1 through safety relay output 23-24. Pressing an e-stop drops the brake at the same moment as the drives, in hardware, whatever the PC is doing. LinuxCNC's own sequencing (above) still handles normal machine on/off.

## 4. Simulator test (done 2026-11-08)

`sim/test_sim.py` was run against LinuxCNC 2.9.10 (Debian 12 packages): **23 of 23 checks pass**: e-stop refusal without power OK, machine on, drive enable and brake timing, pump on, homing sequence and final positions, G0 moves, soft-limit refusal, spindle start with flow and at-speed wait, flow loss (spindle stop, feed hold, e-stop after 5 s), brake engage then drives off, drive alarm e-stop and reset, VFD link loss with the spindle on (e-stop) and off (no e-stop).

The real `spindle.hal` was also loaded with `hy_vfd` against a dummy serial port: all pins link. `hm2.hal` can only be tested with the board; its pin and parameter names were checked against the LinuxCNC hostmot2 source.

To run it yourself on the mini-PC:
```
cd ~/linuxcnc/configs/type0
linuxcnc type0_sim.ini &
python3 sim/test_sim.py
```
If you edit `type0.ini`, run `python3 sim/make_sim_ini.py` to rebuild `type0_sim.ini`.

## 5. PC set-up and latency test (schedule weeks 1–2)

1. Install the **LinuxCNC 2.9 Debian 12 (Bookworm) PREEMPT-RT ISO** from linuxcnc.org on the mini-PC. Then `sudo apt update && sudo apt upgrade` (gets the latest 2.9.x).
2. BIOS: turn off power saving / C-states, turbo and hyper-threading if the latency test is poor.
3. **Network to the Mesa:** give the onboard Intel port a fixed address on the Mesa's subnet: IP `192.168.1.1`, mask `255.255.255.0`, no gateway (Settings → Network, or `/etc/network/interfaces`). The board is at `192.168.1.121` (W13/W14 down/down).
4. Check the link: `ping 192.168.1.121`. Then `sudo apt install mesaflash` and run `mesaflash --device ether --addr 192.168.1.121 --readhmid`. It should list the StepGens and the smart-serial port for the on-board 7I76. Save the output in the repo.
5. Turn off interrupt coalescing on that port (helps hm2_eth timing): `sudo ethtool -C <port name> rx-usecs 0` (put it in `/etc/network/interfaces` as a `post-up` line so it stays).
6. **Latency test:** `latency-histogram --nobase --sbinsize 1000` for 10 minutes while you load the PC (open a browser, move windows, copy a large file). With an Ethernet Mesa the servo-thread jitter should stay well under 100 µs; under about 50 µs is good.
7. With LinuxCNC running on the real config, watch `hm2_7i76e.0.read.tmax` and `hm2_7i76e.0.write.tmax` in Halshow and check `hm2_7i76e.0.packet-error-level` stays 0. Read time should be well under the 1 ms servo period (a few hundred µs at most).
8. Copy `linuxcnc/type0/` to `~/linuxcnc/configs/type0/` and add yourself to the serial group: `sudo adduser $USER dialout` (log out and in).
9. USB-RS485 adapter: plug it in, find its stable name with `ls -l /dev/serial/by-id/` and put that path in `[TYPE0] VFD_PORT` (more reliable than `/dev/ttyUSB0`).

## 6. Bench-test procedure (schedule weeks 3–6, before mounting on the frame)

Do every step with the motors **unloaded** (couplings off), Z motor lying on the bench (so the brake test doesn't drop anything). Keep one hand near an e-stop.

**A. Power and e-stop (no LinuxCNC yet)**
1. Mains off. Check PE continuity from the plug to the cabinet, plate, PSUs, VFD and spindle body.
2. Power up. 24 V present at TB1 and TB3; Mesa LEDs on. Contactor stays out.
3. Press the green reset: contactor pulls in, 48 V at the drives, VFD display on. Press each e-stop: contactor drops every time. Test both channels (CHECK XPSAC5121 wiring).

**B. Inputs (LinuxCNC running, Machine → Halshow, watch the 7I76 input pins)**
4. IN3 is on with the contactor in, off when an e-stop is pressed.
5. Hold a steel object to each LJ12A3 sensor: IN0/1/2 turn on (and the sensor LED).
6. Drive alarms IN4–6: with all drives healthy they must read **off**. If they read on, use the `-not` pins in `hm2.hal` (CHECK). Then unplug one motor's encoder cable: that drive should alarm, its input change, and LinuxCNC go to e-stop.
7. Flow switch IN7: blow through it or run the pump: on with flow, off without (CHECK contact rating first, open question 3).

**C. Outputs and enable**
8. First start only: run `halcmd show param hm2_7i76e.0.7i76.0.0` and confirm the `source` and `sink` parameters exist (they set the outputs to sourcing; without them the outputs stay off). Reset e-stop and turn the machine on in AXIS. OUT0 on: check the CL57T enable logic: the motors should hold (stiff shaft). If they go *free* when the machine is on, set `output-00-invert 1` in `hm2.hal`. The V3.0 manual suggests this will be needed (24 V on ENA with sourcing wiring = disabled).
9. OUT1: the Z brake clicks free about 0.3 s after machine on, and grips at once at machine off. With the brake released, press an e-stop: it must grip at once (safety output 23-24, D-93).
10. OUT2/OUT3: the pump relay and radiator fans run while the machine is on.

**D. Motion (couplings off)**
11. Check every CL57T is at 1,600 pulses/rev: the V3.0 manual's factory DIP setting SW1–SW4 = on, off, on, on is 1,600. SW7 off = step/dir mode. CHECK the table in the V4.1 manual that comes with the drives.
12. Jog each axis slowly. Mark the shaft: a 5 mm jog must be exactly 1 turn. Note the direction; fix with a negative `SCALE` in `type0.ini` if wrong.
13. Run each axis at 2 m/min (G1 F2000 back and forth) for a few minutes: no drive alarms, no lost position (the closed-loop drives alarm if the error grows).
14. Homing: trigger each home sensor by hand while the axis searches. The search direction must be toward +X, +Y, Z up.

**E. Spindle (VFD and spindle on the bench, coolant loop running)**
15. First run the spindle from the VFD panel only (PD001 = 0) to prove the VFD and wiring. Then set the PD values in `spindle.hal` (PD001 = 2, PD002 = 2, PD164 = 1 …).
16. Start LinuxCNC: the panel's **VFD link** LED goes green. If not, swap the A/B wires and check the baud rate.
17. M3 S8000: spindle runs, rpm matches, "at speed" lights. M5 stops. M4 runs in reverse.
18. Stop the pump (or pinch the hose) with the spindle on: the spindle stops at once, then e-stop after 5 s.
19. Pull the USB plug with the spindle on: e-stop after 2 s. (The VFD itself also loses mains on any e-stop through the contactor.)

Record the results (and any changes to the CHECK items) in `docs/decisions.md`.

## 7. Changing things later

- **Speeds:** raise `MAX_VELOCITY`/`MAX_ACCELERATION` in each `[AXIS_*]` and `[JOINT_*]`, `STEPGEN_MAX_VEL` about 25% above, and `[TRAJ]`/`[DISPLAY] MAX_LINEAR_VELOCITY`. Test on the finished machine.
- **Home at the other end:** swap the sign of `HOME_SEARCH_VEL` and `HOME_LATCH_VEL`, and set `HOME_OFFSET`/`HOME` near the lower limit.
- **Screw compensation (D-10):** add `COMP_FILE` per joint after the mapping run.
- **Phase 2:** stepgen 3 for the ATC wheel (`num_stepgens=4`), inputs IN8–IN14, outputs OUT4–OUT7, a tool-change routine, door interlock. The Mesa RS-485 port (TB3) stays free for any standard-Modbus device (LinuxCNC's `hm2_modbus`, 2.9.5+).

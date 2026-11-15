# LinuxCNC starter config, latency test and bench test (task 2, D-92)

Config files: [`config/linuxcnc/type0/`](../config/linuxcnc/type0/)

| File | What |
|---|---|
| `type0.ini` | Machine settings: axes, scales, speeds, homing, soft limits, VFD port, brake timing |
| `type0.hal` | Mesa 7I76EU: step/dir, PID, home switches, drive alarms, drive enable, Z brake, pump/fans, flow interlock, e-stop chain |
| `spindle_hy.hal` | Huanyang VFD on a USB-RS485 adapter (`hy_vfd`), gated by coolant flow |
| `tool.tbl` | Tool table (manual ER20 changes in Phase 1) |

Pin map, power and safety chain: [electrical.md](electrical.md). The config could not be run here (no LinuxCNC in the cloud session). It was checked by hand and with a script (no pin in two signals, no function added twice). **Expect small fixes on the first start**, mostly pin names (see step 4).

## Main choices (D-92)
- **Spindle control: USB-RS485 adapter + LinuxCNC's `hy_vfd` driver** (owner choice, 2026-11-15). Huanyang HY VFDs use Huanyang's own Modbus-like protocol, which `hy_vfd` speaks. The 7I76EU RS-485 port (TB3) is not used. This replaces the "no USB-RS485 adapter" part of D-58.
- **Scale:** CL57T at 1,600 pulses/rev, 5 mm lead → **320 steps/mm** (3.1 µm per step). Bench-test speeds 50 mm/s (X, Y) and 30 mm/s (Z), 300 mm/s². Raise towards 100 mm/s (6 m/min, D-13) once the machine is built and tuned. At 100 mm/s the step rate is 32 kHz, well inside the step timing used.
- **Step timing:** 5 µs step, 5 µs space, 10 µs direction setup and hold (about double the CL57T figures: CHECK its manual).
- **Homing:** Z first (up), then X (towards +X, the right) and Y (towards +Y, back) together. Inductive sensors, no index. Soft limits only (D-91).
- **Coordinates:** as the CAD model. X 0 = table centre, work X −200…+200, reach to +370 for the Phase 2 tool wheel. Y −125…+125. Z 0 at the top, down to −150.
- **Drive enable:** one output for all three drives (OUT0). **Z brake** (OUT1) releases 0.25 s after the drives come on and drops at once on machine off. The drives stay on 0.15 s longer so Z doesn't sag while the brake bites.
- **Coolant:** pump (OUT2, via relay E23) and radiator fans (OUT3) run whenever the machine is on. The spindle can only run while the flow switch (IN7) is closed. If flow is lost for 3 s with the spindle on, LinuxCNC goes to e-stop.
- **E-stop:** the hardwired chain does the real stopping (D-35). LinuxCNC leaves e-stop only when IN3 (contactor aux = power OK) is on and there's no coolant fault. Drive alarms (IN4–6) are joint amp faults, which also stop the machine.
- **Mesa watchdog:** 5 ms. If the PC or LinuxCNC stops, the 7I76EU turns its outputs off: drives disabled, brake on, pump off.

## 1. Install
1. Download the current **LinuxCNC 2.9.x Debian 12 (Bookworm) ISO** from linuxcnc.org and install it on the mini-PC. It comes with the PREEMPT-RT kernel.
2. **CHECK Mesa support for the 7I76EU:** Mesa's 7I76EU page says which LinuxCNC version is needed. After install, run `mesaflash --device 7i76eu --addr 192.168.1.121 --readhmid` (step 3). If LinuxCNC doesn't recognise the board, update to the latest 2.9.x packages.
3. BIOS: turn off C-states / power saving, turbo / speed-step, and anything called "SMT power management" if the latency test is poor. Keep hyper-threading on unless the test says otherwise.
4. Copy `config/linuxcnc/type0/` to `~/linuxcnc/configs/type0/` on the PC.

## 2. Network to the Mesa card (the onboard Intel port, D-58)
- Card jumpers: W13/W14 down/down → fixed IP **192.168.1.121** (electrical.md section 3).
- PC port: static IP **192.168.1.1**, netmask 255.255.255.0, no gateway, no DNS. In Debian: Settings → Network → the wired port → IPv4 → Manual.
- Turn off interrupt coalescing on that port (`sudo ethtool -C <port> rx-usecs 0`). To keep it after a reboot, add the line to `/etc/network/interfaces` as a `post-up` command or use a small systemd unit.
- Test: `ping 192.168.1.121`. Then `sudo chrt 99 ping -i .001 -q -c 10000 192.168.1.121`: the maximum round-trip time should be well under 0.5 ms (Mesa's usual guide).

## 3. Latency test (week 1–2)
With Ethernet Mesa cards, the PC only has to answer on time once per servo period (1 ms), so the base-thread numbers don't matter.
1. Run `latency-histogram --nobase --sbinsize 1000` for **at least 1 hour**. While it runs, load the PC: open a browser with a video, copy big files, run `glxgears`, plug and unplug a USB stick.
2. **Pass:** servo-thread max jitter under about **100 µs** (10% of the servo period). Up to about 200 µs is still workable with Mesa Ethernet cards. Worse than that: change BIOS settings (step 1.3) and retest.
3. With the card connected and the config running (step 4), check in Halshow: `hm2_7i76eu.0.read.tmax` and `.write.tmax` stay well under the servo period, and `hm2_7i76eu.0.packet-error-level` stays at 0 over an hour of jogging.
4. Write the results in this file (max jitter, read/write tmax, date).

## 4. First start (card only, no drives powered)
1. `mesaflash --device 7i76eu --addr 192.168.1.121 --readhmid`: note the board name and what the firmware has (stepgens, sserial). If the board name isn't `7i76eu`, change `BOARD` in `[HMOT]`. If the stepgen count in the firmware is lower than 5, change `num_stepgens` in `type0.hal`.
2. Start: `linuxcnc ~/linuxcnc/configs/type0/type0.ini`. If it stops with "pin not found", run `halrun`, then `loadrt hostmot2`, `loadrt hm2_eth board_ip=192.168.1.121`, and `show pin` to see the real names. The field I/O name is set by `FIELD` in `[HMOT]` (expected `7i76.0.0`).
3. **CHECK** whether the 7I76EU needs a setting for its outputs to source current (electrical.md section 4, TB6). If an output doesn't switch its load, look for an output mode pin with `halcmd show pin | grep output-00`.
4. Without the USB-RS485 adapter plugged in, LinuxCNC stops at `spindle_hy.hal`. Keep the adapter plugged in: it doesn't need a VFD connected for LinuxCNC to start (CHECK: `vfd.hycomm-ok` just stays false). Without an adapter, comment out the `HALFILE = spindle_hy.hal` line in the INI for card-only tests.

## 5. Bench test (weeks 3–6, everything on the bench indoors)
Do the steps in order. Tick each one and write down anything that needed changing.

**A. 24 V, Mesa and inputs (48 V PSU and VFD mains off)**
1. Halshow → watch `input-00` … `input-07`.
2. Hold a steel flag to each LJ12A3 sensor: the matching input (IN0–2) goes on, and the sensor's LED lights.
3. Close the flow switch by blowing through it (or bridge it): IN7 goes on.

**B. Safety chain (mains on, drives and VFD not yet connected)**
1. Press reset with both e-stops released: the contactor pulls in, IN3 goes on.
2. Press e-stop 1: contactor drops at once, IN3 off, LinuxCNC goes to e-stop. Release it: the contactor must **stay off** until reset is pressed (manual reset). Same for e-stop 2.
3. Disconnect one channel wire at the relay (simulated fault): the relay must refuse to reset. Reconnect.

**C. Drives and motors (motors clamped to the bench, tape flag on each shaft)**
1. Set each CL57T: 1,600 pulses/rev and the motor current (DIP switches: CHECK the CL57T manual). The Z motor driver uses the same settings.
2. Power on, reset, F2 (machine on). OUT0 goes on, all three drives enable (green LED). **If the drives are enabled before machine on, or the opposite**, invert OUT0 (comment in `type0.hal`).
3. Jog each axis +5 mm: the shaft turns exactly 1 turn. Check the direction against the axis (flip the sign of `SCALE` when the machine is built).
4. Drive alarm test: unplug one motor's encoder cable with the machine on. The drive alarms, the matching input (IN4–6) changes, LinuxCNC stops with an amp fault. **If LinuxCNC shows a fault with healthy drives**, use `input-0N-not` for the alarms.
5. Run each motor at 50 mm/s back and forth for 10 minutes: no following errors, motors warm but not hot.

**D. Z brake**
1. Machine off: the Z motor shaft can't be turned by hand.
2. Machine on: after about 0.25 s the brake clicks open and the shaft is held by the motor only.
3. Press an e-stop: the brake clicks shut.

**E. VFD and spindle (spindle clamped in its holder, cooling loop filled and running)**
1. **Never run the water-cooled spindle without water.** Fill and bleed the loop before the first start.
2. Set the VFD parameters (electrical.md section 6, CHECK each one in the VFD manual). Power the VFD off and on after changing PD163–PD165.
3. Wire the adapter: adapter A → VFD RS− (often "A−"), adapter B → VFD RS+ ("B+"). If there's no answer, swap A and B: makers label them differently.
4. Find the adapter's fixed name: `ls /dev/serial/by-id/` and put it in `[VFD]DEVICE`.
5. Start LinuxCNC, machine on. Pump and fans start (OUT2, OUT3), IN7 comes on within a few seconds.
6. MDI `M3 S6000`: spindle starts, `vfd.spindle-speed-fb` reads about 6,000, `spindle.0.at-speed` goes true. Then S12000, S24000, M5. Check `vfd.hycomm-ok` stays true.
7. Flow interlock: with the spindle at S6000, pinch the hose (or unplug the flow switch). Within 3 s LinuxCNC goes to e-stop and the spindle stops.
8. Interlock at start: with the pump unplugged, `M3 S6000` must not start the spindle.

**F. Watchdog**
1. Machine on, Z brake released. Unplug the Ethernet cable from the Mesa card: within a few ms the drives disable and the brake clicks shut. LinuxCNC reports a communication error. Plug in, restart LinuxCNC.

**G. Record**
Write the results and any changed settings here and in decisions.md.

## 6. Later (when the machine is built, weeks 27–28)
- Set the direction (sign of `SCALE`), measure each home switch position and set `HOME_OFFSET`.
- Check the soft limits against the real travel, with about 2 mm to spare at each end.
- Raise the speeds and accelerations step by step until following errors or stalls appear, then back off by 30%.
- Screw mapping for ±0.02 mm (D-10): LinuxCNC screw compensation files, made with a dial indicator against a reference.
- Phase 2: stepgen 03 for the tool wheel, IN8–IN14 and OUT4–OUT7 (electrical.md).

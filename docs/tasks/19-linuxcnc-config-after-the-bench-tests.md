# Task 19: LinuxCNC config after the bench tests

**Start:** branch `claude/hopeful-sagan-28twty`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** Opus 5.5 is fine
**Depends on:** owner's bench results (build weeks 3–6)

## Read
- docs/linuxcnc.md section 6
- linuxcnc/type0/
- docs/electrical.md section 5

## Do
1. Apply the measured ENA and ALM polarity, VFD parameters and minimum spindle rpm. Re-run `linuxcnc/type0/sim/test_sim.py` (23 checks). Do not change the e-stop chain or brake logic: report instead.
2. **Second Y motor (D-137, D-284, D-285).** The config is still the old 3-joint machine. Change it to 4 joints, keeping Z as joint 2 so the brake and homing nets barely move:
   - `type0.ini`: `[KINS] KINEMATICS = trivkins coordinates=XYZY kinstype=BOTH`, `JOINTS = 4`; `[TRAJ] COORDINATES = XYZY`; add `[JOINT_3]` (Y2) as a copy of `[JOINT_1]`. Joint 0 X, 1 Y1, 2 Z, 3 Y2.
   - Homing: `HOME_SEQUENCE = -1` on `[JOINT_1]` and `[JOINT_3]` (negative = the two Y joints home together and square the gantry), X stays 1, Z stays 0. Each Y joint gets its own `HOME_OFFSET`, measured when the gantry is squared on the machine.
   - Travel: replace the old X 570, Y 250 with the `Type_0_v3` travel (D-233: spindle X -222.5 to 207.5, Y -93 to 292, i.e. 430 and 385). Ask the owner where machine zero goes.
   - `hm2.hal`: stepgen.03 (TB2 channel 3) to joint.3; `home-y2` from `input-15`; `alarm-y2` from the TB5 input 16 pin (check the name with `halcmd show pin`).
   - `machine.hal`: `net home-y2 => joint.3.home-sw-in`; `fault-or` gets a 7th input (`personality=0x207`), `alarm-y2 => fault-or.in-06`.
   - `panel.xml`: a Y2 drive alarm LED.
   - Simulator: `sim/sim_hw.hal` gets `sim-home-y2`, joint 3 position loopback and `alarm-y2`; run `sim/make_sim_ini.py`; `sim/test_sim.py` checks `s.homed[:4]`, adds a Y2 alarm e-stop check and a check that joint 3 follows joint 1.
   - The ATC wheel (Phase 2) later goes on step/dir channel 4 on TB3 (D-137).

## Done when
The simulator test passes (with the new Y2 checks); every changed value cites the owner's measurement.

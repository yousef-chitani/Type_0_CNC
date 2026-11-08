#!/usr/bin/env python3
"""Checks the Type 0 config in the simulator. Start LinuxCNC first:
    linuxcnc type0_sim.ini &
then run:  python3 sim/test_sim.py
Each check prints PASS or FAIL. Exit code 0 = all passed."""
import subprocess, sys, time
import linuxcnc

s = linuxcnc.stat()
c = linuxcnc.command()
fails = 0


def hal(cmd):
    return subprocess.run(["halcmd"] + cmd.split(), capture_output=True, text=True).stdout.strip()


def sig(name):
    v = hal(f"gets {name}")
    return {"TRUE": True, "FALSE": False}.get(v, v)


def check(label, ok):
    global fails
    print(("PASS " if ok else "FAIL ") + label)
    fails += 0 if ok else 1


def wait(cond, timeout=10.0):
    end = time.time() + timeout
    while time.time() < end:
        s.poll()
        if cond():
            return True
        time.sleep(0.05)
    return False


def machine_on():
    c.state(linuxcnc.STATE_ESTOP_RESET)
    wait(lambda: s.task_state == linuxcnc.STATE_ESTOP_RESET, 3)
    c.state(linuxcnc.STATE_ON)
    return wait(lambda: s.task_state == linuxcnc.STATE_ON, 3)


def mdi(cmd, timeout=60):
    c.mode(linuxcnc.MODE_MDI)
    c.wait_complete()
    c.mdi(cmd)
    return c.wait_complete(timeout)


wait(lambda: True)

# 1. E-stop chain: no power from the contactor -> cannot enable
hal("sets machine-power-ok 0")
c.state(linuxcnc.STATE_ESTOP_RESET)
time.sleep(0.5); s.poll()
check("cannot leave e-stop while machine-power-ok is false", s.task_state == linuxcnc.STATE_ESTOP)
hal("sets machine-power-ok 1")
check("machine turns on when power is OK", machine_on())

# 2. Drive enable and brake timing
check("drive-enable-out on", sig("drive-enable-out") is True)
time.sleep(0.5)
check("Z brake released after the delay", sig("z-brake-release") is True)
check("pump and fans on with the machine", sig("pump-on") is True)

# 3. Homing: Z first, then X and Y
c.mode(linuxcnc.MODE_MANUAL); c.wait_complete()
c.teleop_enable(0); c.wait_complete()
c.home(-1)
ok = wait(lambda: all(s.homed[:3]), 120)
check("all axes homed", ok)
s.poll()
pos = s.actual_position
check(f"after homing at X565 Y245 Z-2 (got {pos[0]:.2f} {pos[1]:.2f} {pos[2]:.2f})",
      abs(pos[0] - 565) < 0.01 and abs(pos[1] - 245) < 0.01 and abs(pos[2] + 2) < 0.01)

# 4. Moves and soft limits
mdi("G21 G90 G53 G0 X100 Y100 Z-50")
s.poll()
check("G0 to X100 Y100 Z-50", abs(s.actual_position[0] - 100) < 0.01 and abs(s.actual_position[2] + 50) < 0.01)
c.mode(linuxcnc.MODE_MDI); c.wait_complete()
c.mdi("G53 G0 X600")
time.sleep(1); s.poll()
check("move past soft limit X570 is refused", abs(s.actual_position[0] - 100) < 0.01)
c.abort(); c.wait_complete()

# 5. Spindle with coolant interlock
mdi("M3 S12000")
time.sleep(1.5)
check("spindle allowed to run with flow", sig("spindle-run") is True)
check("spindle at speed", sig("spindle-at-speed") is True)
t0 = time.time()
mdi("G1 X120 F600")
s.poll()
check("feed move runs with flow", abs(s.actual_position[0] - 120) < 0.01)

hal("sets coolant-flow-ok 0")
time.sleep(0.6)
check("flow lost: spindle stopped", sig("spindle-run") is False)
check("flow lost: feed held", sig("flow-blocked") is True)
ok = wait(lambda: s.task_state == linuxcnc.STATE_ESTOP, 8)
check("flow lost for 5 s: e-stop", ok)
hal("sets coolant-flow-ok 1")
time.sleep(0.5)
check("Z brake engaged in e-stop", sig("z-brake-release") is False)
time.sleep(0.3)
check("drives disabled after the off delay", sig("drive-enable-out") is False)

# 6. Drive alarm -> e-stop, latched until reset
check("machine back on", machine_on())
hal("sets alarm-y 1")
ok = wait(lambda: s.task_state == linuxcnc.STATE_ESTOP, 3)
check("Y drive alarm: e-stop", ok)
hal("sets alarm-y 0")
check("reset after alarm clears", machine_on())

# 7. VFD link lost while spindle on -> e-stop
mdi("M3 S10000")
time.sleep(1.2)
hal("sets vfd-comm-ok 0")
ok = wait(lambda: s.task_state == linuxcnc.STATE_ESTOP, 5)
check("VFD link lost with spindle on: e-stop", ok)
hal("sets vfd-comm-ok 1")

# 8. VFD link lost with spindle off -> no e-stop
check("machine back on", machine_on())
mdi("M5")
hal("sets vfd-comm-ok 0")
time.sleep(3); s.poll()
check("VFD link lost with spindle off: no e-stop", s.task_state == linuxcnc.STATE_ON)
hal("sets vfd-comm-ok 1")

print(f"\n{fails} failure(s)")
sys.exit(1 if fails else 0)

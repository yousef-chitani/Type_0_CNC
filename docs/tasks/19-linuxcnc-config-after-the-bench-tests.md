# Task 19: LinuxCNC config after the bench tests

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** Opus 5.5 is fine
**Depends on:** owner's bench results (build weeks 3–6)

## Read
- docs/linuxcnc.md section 6
- linuxcnc/type0/
- docs/electrical.md section 5

## Do
1. Apply the measured ENA and ALM polarity, VFD parameters and minimum spindle rpm. Re-run `linuxcnc/type0/sim/test_sim.py` (23 checks). Do not change the e-stop chain or brake logic: report instead.

## Done when
The simulator test passes; every changed value cites the owner's measurement.

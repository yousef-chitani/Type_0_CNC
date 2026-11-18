# Task 09: Owner's Fusion pass and feeding it back

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** owner, then main session
**Depends on:** none (03 is on hold, D-131)

**Warning (18 Nov 2026):** `type0_assembly.step` is the old fixed-gantry design (before D-137). Build the moving-gantry assembly from `docs/moving-gantry-sketch.md`, D-164 and the vendor models in `cad/vendor/`.

## Read
- docs/assembly.md (VERIFY list)
- cad/v2/out/assembly/type0_assembly.step

## Do
1. Owner: open the STEP in Fusion, detail brackets, plates and sensor mounts, work through the VERIFY list, save the STEP to `cad/v2/in/`.
2. Session: put the changes into `assembly.py`, re-run `assembly.py`, `enclosure.py`, `bench.py`, `base_cores_sketch.py`, `render_views.py`, and regenerate `cast_in_features.md`.

## Done when
The assembly matches the owner's file with no clashes.

# Task 03: Strip the castings in the CAD (option A)

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** main session (design judgement)
**Depends on:** 01 = A

## Read
- docs/simplification-options.md (option A table)
- cad/v2/assembly.py (functions `base_casting`, `portal_casting` only)
- cad/v2/out/assembly/cast_in_features.md
- docs/HANDOVER.md section 9 (how to run the CAD)

## Do
1. In `assembly.py`: remove the portal PVC cores, the ATC bracket insert and the dowel sleeves in both castings. Keep everything else.
2. Run `assembly.py` (no clashes at 3 positions), then `render_views.py`, `enclosure.py`, `bench.py`; regenerate `cast_in_features.md` from `assembly_data.json`.
3. Update the masses in `docs/assembly.md` and `docs/HANDOVER.md`. Record the decision. If the portal is over 40 kg, tell the owner the figure and ask before trimming anything.
4. Mark the base-core proposal (`cad/v2/base_cores_sketch.py`) as dropped.

## Done when
STEP files, feature list, views and masses agree; one new decision recorded.

# Task 12: Printed mould helpers

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** Opus 5.5 is fine
**Depends on:** 10

## Read
- docs/printed-parts.md
- cad/v2/printed_parts.py
- cad/v2/out/assembly/cast_in_features.md

## Do
1. Model in PETG: sleeve locators for Ø16 tube on an 18 mm floor, jig spacers that hold an insert bar 5 mm above the floor, dam strips for the rail-seat pour, TPU rings for the M12 rods.
2. Export STL to `cad/v2/out/print/`, add to `docs/printed-parts.md`. Mark any size that depends on a bought part VERIFY.

## Done when
Each part exports and has a print orientation; nothing is sized from a guess.

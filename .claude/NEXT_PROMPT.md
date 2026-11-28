# Next session
## Context (≤5 lines)
57th session finished the `Type_0_v6` Y1/Y2 belt drives (`6 mm` steel plates with `48×38` cable archway, `1:1` `20T` `HTD 5M-300`, top M5 push-down tensioning lug), swapped front `BF12` for real `BK12` blocks (`bk12.step`), added 3D-printed PETG front belt covers, and mounted real `HM12-60` + inline `24HS40` motor at the `+X` drive end (D-389, D-390). Timeline: **1325 items, 0 errors** (**not saved** — owner saves). `docs/bom.csv` updated with v6 lines (`PRICE PENDING` until Dyfed Steels & `price-check-task-19.md` quotes arrive). Last D-number: **D-390**.

## Do this bundle: Type_0_v6 ATC cylinder, homing/chains & v6 BOM pricing
- [ ] Ask owner: did they save `Type_0_v6`? Any live prices from `docs/price-check-task-19.md` or Dyfed Steels (`docs/supplier-messages.md` §8)?
- [ ] If `cad/vendor/` has a real `CD85N20-175` STEP, mount it horizontally inside the rear ATC well (`Y 330..680`) onto the rear cylinder mount block (`Y 682..704`) and add reed-switch brackets & splash curtain details.
- [ ] Check/detail remaining `Type_0_v6` mechanical items: rear Y floating `BF12` blocks, X/Y/Z inductive homing sensor brackets (`LJ12A3`), cable chain routing (using the open `48×38` front Y-plate archways), and Z-axis motor/clamp check.
- [ ] Apply confirmed Dyfed Steels + `price-check-task-19.md` live prices to `docs/bom.csv`, drop superseded V4 frame/ATC lines once v6 prices are in, and verify Phase 1 total vs £4,200 budget.

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md`
- `docs/HANDOVER.md:9-20` — 57th session summary
- `docs/decisions.md:384-392` — D-383 to D-390 (`Type_0_v6` specs)
- `docs/price-check-task-19.md` — ATC pneumatics & coolant loop items
- `docs/supplier-messages.md:143-168` — Dyfed Steels `Type_0_v6` cut list

## Already known (don't re-investigate)
- `Type_0_v6` spindle reach: X `-235..+220` (455 mm), Y `-19.75..+440.25` (460 mm), Z nose `161.8..381.8` (220 mm stroke on 350 mm `2Z HGR15` rails, spindle dropped 20 mm in clamp).
- Y belt drives (`V6 Y Motor Belt Drives:1`): `6 mm` steel plates (`Y -6..0`, `48×38` bottom cable tunnel), `1:1` `20T` `HTD 5M-300` (`C = 99.62 mm`), real `BK12` blocks (`X = ±365`, `Z = 230..273`), PETG stadium belt covers (`Y -39..-6`).
- X drive (`V6 X Motor & HM12-60`): real `hm12_60.step` (`X 319.2..431.2, Y 615.25, Z 455..515`) + coaxial `24HS40` at `+X` (`X = 431.2`).
- 14-tool (`2×7` @ 56 mm X pitch) sliding ATC: parked `Y 525/605` (pull-stud tops `Z 235`), extends `168 mm` on `Y 326..676` HGR15 rails to `Y 357/437` (hard stops `X ±168..±182, Y 326..336`).
- Never save Fusion documents; the owner saves them. `git commit` needs `-c user.name=Claude -c user.email=noreply@anthropic.com`.

## Done when
- `CD85N20-175` & remaining v6 details modelled, `docs/bom.csv` updated with live prices, `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (`CLAUDE.md`), tick `TASKS.md`, write the next `.claude/NEXT_PROMPT.md` with the template at the bottom of `.claude/TASKS.md`.

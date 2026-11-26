# Task bundles (26 Nov 2026)

Groups the open work so each session loads its context once. Task state and decisions stay in
`docs/tasks/README.md` and `docs/decisions.md`; this file only groups and orders. Size: S (part of a
session), M (one session), L (may need two: say where you stopped). Owner-only items
(saving Fusion, browser prices, sending messages) are in `docs/owner-todo.txt`, not here.

## Order
1. **A** when Fusion is connected and the owner has saved `Type_0_v5`; otherwise **B**, then **E1**.
2. Then C (needs the owner's bed STEP), D, E2, F.

---

## A. V5 Y axis finish in Fusion (task 32, V5 plan Task 4 items 2–4, 6) — L
**Needs:** Fusion MCP connected; owner has saved `Type_0_v5` (48th + 49th sessions' work).
- [ ] Y2: mirror `Y1 screw and motor` (DFU1605, BF12, HM12-60, 24HS40, 1605 screw, D25L35, risers) and the two HGH20CA blocks to X +377.5; cable lead outboard (+X); hide PrintNC's Y2 parts as for Y1 (`docs/v5-model.md` "Hidden" list)
- [ ] 3 mm rail seats (D-363): delete `Y 1605 Screw` and riser components first, set `SEAT = 3.0`, re-run; rails, blocks, rollers, risers up 3
- [ ] Nut and fill plates as flat bar inside the 80 x 40 roller (D-356, D-362); hide PrintNC's 1610 nut/fill plates and their M5 rods
- [ ] Full check with `v5_check_task4.py`: re-point the carriage, riser and grease-fitting lines for Y1 and Y2; Y travel at both sides
- [ ] Update `docs/v5-model.md`, task 32 row, CODEMAP if a script is added (e.g. `tools/fusion/v5_y2_place.py`)

Files: `tools/fusion/v5_y1_place.py` (218 lines: datums 11–25, `run` 32–), `tools/fusion/v5_check_task4.py` (96),
`docs/v5-model.md:43-70`, `docs/v5-parts.md` (rows for nut plates, risers), decisions D-356, D-362, D-363, D-366 to D-369.
Stop point if split: after Y2 + check (seats and plates next).

## B. Docs consistency (no Fusion) — S
- [ ] `docs/HANDOVER.md` key-files table: "Decision log D-01 … D-336" → D-369; `Type_0_v3` row says superseded by Fusion: name `Type_0_v5`
- [ ] Root `README.md`: lines 3 and 26 say the CAD is `Type_0_v3`, 8-tool changer: update for V5 (PrintNC moving gantry, 16-tool rack Phase 2)
- [ ] `docs/tasks/20-housekeeping-after-each-task.md:3`: branch `claude/charming-cori-349jm7` → current branch; add "run `python tools/codemap.py --check`"
- [ ] `cad/__pycache__/type0_layout.cpython-313.pyc` is tracked despite `.gitignore`: `git rm --cached`
- [ ] `docs/open-questions.md` header (15 Nov, £3,969.54, D-134) is stale: refresh the header line only, or mark the file V3 history (ask the owner which)
- [ ] `docs/supplier-messages.md`: add the LiMo question "HM12-60 motor holes: 49.4 or 50 square?" (a few lines) if not there
- [ ] Note in `docs/v5-model.md`: PrintNC drill guide 3B holes 0.75 off its riser screws (Y -24.25/55.75 vs -25/55)

Files: `docs/HANDOVER.md:30-45`, `README.md:1-30`, `docs/tasks/20-*.md` (17 lines), `docs/open-questions.md:1-5`, `docs/supplier-messages.md` (grep `LiMo`).

## C. V5 bed and Task 5: beam, X, Z, spindle (V5 plan Task 4 item 5, Task 5) — L
**Needs:** A done; owner's bed STEP in `cad/vendor/` (D-364) for the bed part.
- [ ] Bed from the owner's STEP; world origin at the bed top centre (`docs/v5-model.md` "Origin"); spindle reach at Y min/max
- [ ] Beam RHS 200 x 150 x 8 with both X rails (122 apart) and 3 mm seats on the front face; X screw between the rails
- [ ] Front carriage plate (= Z fixed plate, D-357 to D-360); Type 0 Z from `Type_0_v4` (derive), 50 longer (D-348), brake motor
- [ ] Spindle `cad/vendor/jianken_jgl80_2.2r24.step` in the bought clamp
- [ ] Check: nose 25 and 225 at the Z limits; bed corners reachable; overlaps clean at 3 gantry positions

Files: plan `docs/superpowers/plans/2026-11-26-v5-printnc.md:69-89`, `tools/v5_beam.py`, `tools/v5_sizes.py:98-`, `docs/v5-parts.md`, `docs/v5-sizes.md`.

## D. V5 Task 6: tool rack (Phase 2 space) — M
**Needs:** C. Q&A first (fork entry direction, fork shape, chip guard).
- [ ] Q&A, D-numbers; model 16 forks + ISO20 holders (`cad/vendor/iso20_er16_holder.step`) inside `holder_top_min/max`
- [ ] Checks per plan; write `docs/v5-rack.md`

Files: plan `:90-100`, `tools/v5_sizes.py` (`rack_row_span`, `rack_y_depth`).

## E. V5 Task 7: rail-seat pour plan — M (E1 now, E2 after A)
- [ ] E1 (no Fusion): HIWIN HG20 mounting tolerances by curl; pass mark with the owner (D-number)
- [ ] E2 (needs A's seat bodies): pour plan in `docs/v5-rail-seats.md` (dams, resin and quantity from the model's seat volumes, levelling across both Y tubes and the beam front, cure, measuring, fail → grinding)

Files: plan `:101-106`; resin notes `docs/epoxy-options.md`, `docs/curing-heat.md` (headings only).

## F. V5 Task 8: BOM, prices, wave 1 lengths — L
**Needs:** C, D, E. Before 4 Jan 2027 (wave 1).
- [ ] Mark V4-only `bom.csv` lines dead; add V5 lines from `docs/v5-parts.md` (lengths from `sizes()`), dry sand, printed drill guides
- [ ] Price by curl; owner task file for the rest; total against £4,200
- [ ] LiMo lengths for wave 1; `requirements.md`, task list, handover

Files: plan `:107-113`, `docs/bom.csv` (hook runs the generators), `tools/gen_wave1_sheet.py`.

## Parked (need the owner to say they still apply under V5)
- Tasks 10, 11, 12, 18 (EG tub moulds, rail-seat procedure), 24 (fixture-plate slot, V3), 14 (Z motor mount): V3/V4 tub era.
- Task 29 (V4 RFQ pack): on hold until the owner says (task 31 row).
- Task 19 (LinuxCNC after bench tests, Y2 joint D-284/D-285): needs bench results and a LinuxCNC PC.
- Task 16 (wave 1 price re-check): late December; overlaps F.

---

## NEXT_PROMPT template (copy into `.claude/NEXT_PROMPT.md` at the end of every bundle)
```
# Next session
## Context (≤5 lines)
## Do this bundle: <name>
- [ ] task
## Files to load (exact paths + line ranges)
- path:lines — why
## Already known (don't re-investigate)
## Done when
## Then
Hand over (CLAUDE.md), tick TASKS.md, write the next NEXT_PROMPT.md with this template.
```

# Next session
## Context (≤5 lines)
V5 (PrintNC re-sized, Fusion `Type_0_v5`, not in git). V5 plan Task 4: Y1 is fully swapped to real parts
(HGH20CA x2, DFU1605, BF12, HM12-60, 24HS40, 1605 screw, D25L35, tapped-bar risers; D-365 to D-369),
**not saved** at the 49th session's end. Last D-number D-369. The 50th session only built the code map
(`.claude/CODEMAP.md`, `tools/codemap.py`) and bundles (`.claude/TASKS.md`); no design change.

## Do this bundle: A. V5 Y axis finish in Fusion
**Precondition:** the Fusion MCP answers and the owner says `Type_0_v5` is saved. If either is missing,
do **bundle B** (docs consistency, `.claude/TASKS.md`) and then **E1** (HIWIN HG20 tolerances by curl) instead.
- [ ] Y2: mirror Y1's parts (`Y1 screw and motor` component + 2 HGH20CA blocks) to X +377.5, cable lead +X; hide PrintNC's Y2 parts as listed for Y1
- [ ] 3 mm seats (D-363): delete `Y 1605 Screw` and the riser components, `SEAT = 3.0`, re-run placement
- [ ] Nut and fill plates as flat bar inside the 80 x 40 roller (D-356, D-362)
- [ ] Full read-only check (`v5_check_task4.py`) for Y1 and Y2; Y travel both sides

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md` — map; go to files from it
- `tools/fusion/v5_y1_place.py:1-60` — datums, screw profile, how parts are placed (read the rest only when copying for Y2)
- `tools/fusion/v5_check_task4.py` (96 lines) — the check to extend
- `docs/v5-model.md:43-70` — Y1 swap, what is hidden, what is left
- `docs/decisions.md` — only D-356, D-362, D-363, D-366 to D-369 (grep the D-number)

## Already known (don't re-investigate)
- DFU1605 occurrence transform does not hold: place it with a Move feature (`DFU place`), as Y1.
- Y1 screw axis X -377.5, Z 210 (roller centre); BF12 centre Y 733.15, turned so its circlip fits the groove; HM12 screw-end face Y 43.
- Y travel 489.4 after the risers (blocks against riser end faces). Timeline has 4 known warnings, no errors.
- HM12-60 STEP motor holes on 49.4 square vs 24HS40 on 50: question for LiMo (owner), do not change the model.
- PrintNC drill guide 3B is 0.75 off its own riser screws: note only.
- HGH20CA STEP has no grease nipple: keep the 3 mm soft limit at Y max.
- Never save Fusion documents; the owner does.

## Done when
- Overlap check shows only hidden/replaced PrintNC parts; Y travel recorded for both sides; no new timeline errors.
- `docs/v5-model.md`, task 32 row in `docs/tasks/README.md`, `.claude/TASKS.md` ticked; `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (CLAUDE.md: HANDOVER entry, archive the older one, commit, push), and write the next
`.claude/NEXT_PROMPT.md` with the template at the bottom of `.claude/TASKS.md` (likely bundle C, or E2 if the bed STEP is not in).

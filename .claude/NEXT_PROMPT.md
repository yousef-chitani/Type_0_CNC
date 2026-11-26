# Next session
## Context (≤5 lines)
V5 (PrintNC re-sized, Fusion `Type_0_v5`, not in git). V5 plan Task 4: the Y axis is finished on both sides
(51st session: Y2 = Y1 moved +755, 3 mm seats via user parameter `YRailSeat`, end-cap nut/fill plates D-370,
Y travel 489.4 both sides). **Not saved** at the 51st session's end (started from the owner's version 4).
Last D-number D-370. Left in Task 4: the bed (needs the owner's STEP, not in `cad/vendor/`) and the seat bodies.

## Do this bundle: B. Docs consistency (no Fusion), then E1
**If the owner says a bed STEP is now in `cad/vendor/` and `Type_0_v5` is saved, do bundle C instead** (`.claude/TASKS.md`).
- [ ] Bundle B items in `.claude/TASKS.md` (key-files D-range → D-370, root README for V5, task 20 branch, tracked `.pyc`, open-questions header (ask), LiMo hole-square question, trim "State in five lines", drill guide 3B note)
- [ ] E1: HIWIN HG20 mounting tolerances by curl (CLAUDE.md: curl, never the browser); propose the pass mark and the seat footprint (rail width or wider) to the owner, record a D-number

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md` — map; go to files from it
- `.claude/TASKS.md:26-35` — bundle B list; `:55-57` — E1/E2
- `docs/HANDOVER.md:33-60` — key-files table to fix
- `docs/tasks/README.md:5-11` — rules; the "State in five lines" block

## Already known (don't re-investigate)
- Fusion scripts can run the repo file: `exec(compile(open('D:/Repos/Type_0_CNC/tools/fusion/<f>', encoding='utf-8').read(), '<f>', 'exec'), g)` then `g['run']('')`. Run `v5_y1_place.py` and `v5_y2_place.py` in separate calls.
- A new occurrence's `transform2` set in the call that creates it does not hold: pass the matrix at creation. Rebuilt components get ` (n)` suffixes.
- Y overlaps left are known: HGR20 rail vs HGH20CA groove (709/725 mm³), HM12 lock nut and BF12 circlip on the screw threads. PrintNC X/Z self-overlaps are old.
- HM12-60 STEP holes 49.4 square vs 24HS40 50: ask LiMo (owner). M5 rods for the plates about 200 long (BOM).
- Never save Fusion documents; the owner does.

## Done when
- Bundle B boxes ticked in `.claude/TASKS.md`; E1 tolerances and the proposed pass mark in a doc, owner's answer recorded as a D-number.
- `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (CLAUDE.md), tick TASKS.md, write the next NEXT_PROMPT.md with the template at the bottom of `.claude/TASKS.md`
(likely bundle C once the bed STEP is in, or E2: model the seat bodies, then the pour plan).

# Next session
## Context (≤5 lines)
V5 (PrintNC re-sized, Fusion `Type_0_v5`, not in git). Bundles A, B, E1 and E2 for Y done. 54th session: Y seat
bodies (`tools/fusion/v5_y_seats.py`, 58,500 mm³ each) and the Y pour plan (D-374 to D-377) in `docs/v5-rail-seats.md`.
**Not saved** at the 54th session's end (started from the owner's save with the 53rd session's work).
Last D-number D-377. Y travel 480.1 (450 needed). X seats on the beam front (thickness, bodies, pour) fold into C.

## Do this bundle: C (bed, beam, X, Z, spindle) if the bed STEP is in `cad/vendor/`; else D (tool rack)
- [ ] Ask the owner first: has `Type_0_v5` been saved since the 54th session? If not, run the 5 scripts below in order.
- [ ] Ask: is the bed STEP in `cad/vendor/`? If not, do bundle D (`.claude/TASKS.md` D).
- [ ] C: follow `.claude/TASKS.md` C; include the X rail seats (30 wide per rail, D-372; thickness to ask; pass mark 0.02 across, D-371)
- [ ] Also ask when convenient: the Ampreg 30 mixed density (1.1 g/cm³ assumed in the dose) and the X02 level's sensitivity

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md` — map; go to files from it
- `.claude/TASKS.md` — bundle C (or D)
- `docs/v5-model.md` — the last two dated sections (plate rods, seat bodies) and "Left for Task 4"
- `docs/v5-rail-seats.md` — only if doing the X seats

## Already known (don't re-investigate)
- Run order (each its own `fusion_mcp_execute` call): `v5_y1_place.py`, `v5_y2_place.py`, `v5_roller_screws.py`, `v5_y_seats.py`, then `v5_check_task4.py`. Fusion runs a repo file with `exec(compile(open('D:/Repos/Type_0_CNC/tools/fusion/<f>', encoding='utf-8').read(), '<f>', 'exec'), g)` then `g['run']('')`.
- A new occurrence's `transform2` set in the creating call does not hold: pass the matrix at creation. Rebuilt components get ` (n)` suffixes.
- Check (54th session): timeline 1257, 4 warnings (235, 236, 237, 243), no errors. Known overlaps: HGR20 rail vs HGH20CA groove (709/725 mm³); HM12 lock nut and BF12 circlip on the screw; rods in the nut plate's tapped holes (86.7 mm³ each); rear nuts and rods on the BF12 housing (the model sits 3.4 past the back stop); rods vs printed drill guides 4 and 5. PrintNC X/Z self-overlaps are old. Seats: none.
- The check skips components whose name holds 'M5', 'M6', 'M4', 'M8x', 'Threaded Rod', 'Drill Guide' and others (`v5_check_task4.py:7`): name new parts clear of them.
- Rails: Y HGR20 at X ±377.5, Y 64 to 714, underside Z 163; tube top 160, wall 6; X HGR20 rails at Z 215 and 308 (PrintNC, before the V5 beam).
- `git commit` needs `-c user.name=Claude -c user.email=noreply@anthropic.com` (no identity set on this PC).
- Untracked owner files (repo root PrintNC STEP, `cad/v2/Facebutton v2 frame.step`): leave them unless the owner says.
- Never save Fusion documents; the owner does.

## Done when
- The bundle's TASKS.md items ticked, the check clean apart from the known list, decisions recorded as D-numbers.
- `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (CLAUDE.md), tick TASKS.md, write the next NEXT_PROMPT.md with the template at the bottom of `.claude/TASKS.md`.

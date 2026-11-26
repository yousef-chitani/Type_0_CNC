# Next session
## Context (≤5 lines)
V5 (PrintNC re-sized, Fusion `Type_0_v5`, not in git). Bundles A, B and E1 done. 53rd session: Y plate rods
and nuts modelled both sides, 2 roller screws per side cut to M6 x 9 (D-373), Y travel 480.1 (450 needed).
**Not saved** at the 53rd session's end (started from the owner's save with the 51st session's work).
Last D-number D-373. Seats: pass mark D-371, 30 wide centred, 3 thick (D-372, D-363), in `docs/v5-rail-seats.md`.

## Do this bundle: E2 (or C if the owner says the bed STEP is in `cad/vendor/` and `Type_0_v5` is saved)
- [ ] Ask the owner first: has `Type_0_v5` been saved since the 53rd session? (If not, the rods and screw cuts must be rebuilt: run the 4 scripts below in order.)
- [ ] Model the Y seat bodies (30 wide centred on each HGR20, 3 thick, over the rail length) under both Y rails, in a component named without 'M5' / 'Threaded Rod'; overlap check with `v5_check_task4.py`
- [ ] Seat volumes from the model; pour plan in `docs/v5-rail-seats.md` (dams, resin from `docs/epoxy-options.md`, quantity, levelling across both Y tubes, cure, measuring against D-371, fail → grinding); ask the owner each open choice, record D-numbers
- [ ] X seats on the beam front wait for bundle C (beam not modelled)

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md` — map; go to files from it
- `.claude/TASKS.md` — bundle E (E2) and C
- `docs/v5-rail-seats.md` (47 lines) — tolerances, D-371, D-372
- `docs/v5-model.md:64-85` — Y axis finish, plate rods, run order
- `tools/fusion/v5_y1_place.py:1-35` — datums (axis, `SEAT`), `new_comp` at about line 174

## Already known (don't re-investigate)
- Run order (each its own `fusion_mcp_execute` call): `v5_y1_place.py`, `v5_y2_place.py`, `v5_roller_screws.py`, then `v5_check_task4.py`. Fusion runs a repo file with `exec(compile(open('D:/Repos/Type_0_CNC/tools/fusion/<f>', encoding='utf-8').read(), '<f>', 'exec'), g)` then `g['run']('')`.
- A new occurrence's `transform2` set in the creating call does not hold: pass the matrix at creation. Rebuilt components get ` (n)` suffixes.
- Known overlaps: HGR20 rail vs HGH20CA groove (709/725 mm³); HM12 lock nut and BF12 circlip on the screw; rods in the nut plate's tapped holes (86.7 mm³ each); rear nuts on the BF12 housing (the model sits 3.4 past the back stop); rods vs PrintNC printed drill guides 4 and 5 (jigs). PrintNC X/Z self-overlaps are old.
- Lower rods clear the HGH20CA block screw heads by 0.44 (about 0.2 with ISO 7380 Ø10.5 heads): check on the real parts.
- `git commit` needs `-c user.name=Claude -c user.email=noreply@anthropic.com` (no identity set on this PC).
- Untracked owner files (repo root PrintNC STEP, `cad/v2/Facebutton v2 frame.step`): leave them unless the owner says.
- Never save Fusion documents; the owner does.

## Done when
- Seat bodies in the model, overlap check clean apart from the known list; pour plan section in `docs/v5-rail-seats.md` with the owner's choices as D-numbers.
- `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (CLAUDE.md), tick TASKS.md, write the next NEXT_PROMPT.md with the template at the bottom of `.claude/TASKS.md`
(likely bundle C once the bed STEP is in).

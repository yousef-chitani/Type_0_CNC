# Next session
## Context (≤5 lines)
V5 (PrintNC re-sized, Fusion `Type_0_v5`, not in git). 55th session: bundle C part 1, the beam and X axis
(`tools/fusion/v5_x_place.py`, D-378 to D-382); **not saved** at its end (started from the owner's save with the
54th session's work). The bed waits for a flood-coolant redesign (D-378): no bed, give it inputs. Last D-number D-382.

## Do this bundle: C part 2 (Type 0 Z, clamp, spindle, checks)
- [ ] Ask the owner first: has `Type_0_v5` been saved since the 55th session? If not, run only `v5_x_place.py`, then the check (the owner's save already holds the Y work; re-running the Y scripts can add ` (n)` suffixes, and `v5_x_place.py` finds the Y seat component, BF12 riser and `HGH20CA Block:1` by exact name).
- [ ] Type 0 Z from `Type_0_v4` (component `Z axis and spindle`, copied bodies; doc id `urn:adsk.wipprod:dm.lineage:4QnxX7RCQFGKVl1ms7svww`): copy the bodies as V4 did from v3 (`docs/v4-model.md:151-155`), fixed plate on the X carriage (plate back Y 506.5, carriage X 0), plate, rails and screw 50 longer (D-348; z_rail and z_screw 400), Z block shims 2 mm (D-359), 24HS34 brake motor. Ask before any layout choice.
- [ ] Bought 80 mm clamp from `cad/vendor/drawings/spindle_clamp_80.png` (values in `cad/vendor/drawings/README.md:10`) and the spindle `cad/vendor/jianken_jgl80_2.2r24.step`. If the drawing does not give enough, stop and ask.
- [ ] Check at 3 gantry positions (X min, 0, max; a new or extended read-only check); report the bed-top Z for nose 25 and 225 and the spindle's X/Y reach (D-378). Tick `.claude/TASKS.md` C.
- [ ] Ask the owner: the beam-to-roller bolt pattern (not modelled; the D-373 M6 x 9 copies sit in the old brace footprint and run into the beam's bottom wall); `FRONT_TO_AXIS` (`tools/v5_beam.py`) 173 -> about 190 with the spacers: re-run the D-353 figures once the Z is in.
- [ ] Ask when convenient: X rail-end stops (blocks leave the rail at carriage ±236.25); Ampreg 30 mixed density; X02 level sensitivity.

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md`, `.claude/TASKS.md` bundle C
- `docs/v5-model.md` — section "Beam and X axis" (the layout numbers)
- `tools/fusion/v5_x_place.py` — pattern for copying bodies with a matrix and naming them
- `docs/v4-model.md:137-175` — the V4 Z bodies and how they were copied

## Already known (don't re-investigate)
- Run order (each its own `fusion_mcp_execute` call): `v5_y1_place.py`, `v5_y2_place.py`, `v5_roller_screws.py`, `v5_y_seats.py`, `v5_x_place.py`, then `v5_check_task4.py` (readOnly). Run a repo file: `g = {}; exec(compile(open('D:/Repos/Type_0_CNC/tools/fusion/<f>', encoding='utf-8').read(), '<f>', 'exec'), g)` then `g['run']('')` inside `def run(_context)`.
- Do NOT set PrintNC's `XGantry*` parameters: it breaks 154 features (tried 55th session).
- Body names set inside a base-feature edit do not hold on copied bodies: rename after `finishEdit` (as `v5_x_place.py`).
- X layout: beam Y 556.5 to 706.5, Z 233 to 433, X ±417.5; rails Z 272/394; screw axis Y 526.5, Z 333; X carriage plate back Y 506.5 (17 spacers on the blocks); DSG16H X -20 to 20; gantry at the Y rear stop. Spindle axis estimate Y 366.5 (plate back - 140, V4).
- Check (55th session): timeline 1261, 4 warnings (235, 236, 237, 243), no errors. Known overlaps: HGR20 rail vs HGH20CA groove (Y 709/725, X 725 x 4); HM12 lock nut and BF12 circlip on the screw (Y and X); rods in the nut plate's tapped holes; rear nuts and rods on the BF12 housing; rods vs drill guides 4 and 5.
- The check skips components named with 'M5', 'M6', 'M4', 'M8x', 'Threaded Rod', 'Drill Guide' and others (`v5_check_task4.py:7`).
- Hidden PrintNC parts: XGantry, YRollerBrace x 2, XAxis Hardware, ZAxis Hardware, Zaxis Dual Carriage HGH15CA. PrintNC X/Z fasteners in `Fasteners` are still visible.
- `git commit` needs `-c user.name=Claude -c user.email=noreply@anthropic.com`.
- Untracked owner files (repo root PrintNC STEP, `cad/v2/Facebutton v2 frame.step`): leave them.
- Never save Fusion documents; the owner does.

## Done when
- TASKS.md C items ticked (the bed one stays waiting, D-378), the check clean apart from the known list, decisions as D-numbers.
- `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (CLAUDE.md), tick TASKS.md, write the next NEXT_PROMPT.md with the template at the bottom of `.claude/TASKS.md`.

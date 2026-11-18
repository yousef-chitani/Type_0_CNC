# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000. 18 Nov 2026: HM12-60-V replaces the Z BK12 (D-207), not modelled yet

**Done:** the owner chose the HM12-60-V as Z motor mount and fixed bearing (D-207). `docs/bom.csv` M13 is updated. **No CAD changed: `Type_0_v3` still shows the BK12, the D-206 bracket and the motor mount stand-in, and it has unsaved changes. The owner saves it.**

**Decide first, owner:** the HM12-60-V base is 25 from the screw axis, which is the plane of the fixed plate face (Y 417), but the plate stops at Z 519. With the motor flange kept at Z 612, the 95 long mount spans about Z 517 to 612, so it has nothing to bolt to. Options: make the fixed plate about 95 taller (350 to about 445, recommended, changes M12), or add a separate bracket.

**Check with the mount:**
1. **Screw end.** Confirm with LiMo that the Z screw's standard BK12 end fits the 7001 bearing, and whether the Z set can be supplied without its BK12.
2. **Motor height.** Keep the flange at Z 612 or move it once J 89, L 95 and the coupling are placed.
3. **Coupling.** The drawing lists a 30-42 coupling; the BOM buys D25L35. Check the fit inside the mount. The hub is 11.75 long against the 12.9 grip in D-186.
4. **Motor screws.** PCD 70 gives a 49.5 square against the motor's 50. M4 screws should pass the Ø5.1 motor holes.
5. **D-206 items fall away:** the bracket, its 2 tapped plate holes, the 15 mm piece and the bracket screws.

**Other work left:**
- **Couplings and M12 sensors:** ready to model from `cad/vendor/drawings/README.md`. The sensor drawing says NPN and the BOM buys PNP.
- **X, Y and Y2 HGH20CA blocks:** approved, not done. Changing `YCarriageB/C` and `XCarriageB/C` broke `Rigid 3`, `Rigid 4`, `Rigid 361` and the D-199 riser bolt features, so it was undone. Re-anchor the sketches `YRoller Lower`, `XTopRollerLower` and `Xroller Carriage Holes` on the block centres. Block screws become M5 x 8 (M5 x 10 in the bottom X roller), because the block thread is 6 deep.
- **Still missing:** JGL-80 dimension drawing; clamp length, base holes and bore centre height; LiMo nut housing drawing; LiMo confirmation of the nut flats.

**Exact next step:** the owner saves `Type_0_v3` and chooses how the HM12-60-V is carried. Then, in a new session, model the mount and remove the Z BK12 and bracket.

## 000000000000000000000000000000000000000000000000000. 18 Nov 2026: supplier drawings saved, modelling not started

**Done:** the owner's 7 drawings are saved in `cad/vendor/drawings/`, with their values and flags in `cad/vendor/drawings/README.md`. No CAD was changed in this step.

**Left, by part:**
1. **Couplings (4).** The D25L35 sizes are now known (hub 11.75, M3). Ready to model. The hub is shorter than the 12.9 grip set in D-186, so check the shaft ends against the spider.
2. **Homing sensors.** M12 sizes are known. Ready to model, with the printed mounts changed to M12. The drawing says NPN and the BOM buys PNP.
3. **Z motor mount.** The HM12-60-V drawing is saved. **Owner to decide:** it includes a 7001 bearing, so it may replace the Z BK12 and the D-206 bracket.
4. **Spindle clamp.** The profile is known. Still missing: clamp length along the spindle, base bolt holes and bore centre height.
5. **Spindle JGL-80.** The new page has specifications only. The Jianken dimension drawing is still missing.
6. **Nut housings.** The LiMo drawing (M07) is still missing.
7. **X, Y and Y2 nut flanges.** The catalogue gives 40 across flats. LiMo has not confirmed the flats.
8. **X, Y and Y2 HGH20CA blocks.** Approved, not done: see the entry below.

**`Type_0_v3` still has unsaved changes. The owner saves it.**

**Exact next step:** the owner saves `Type_0_v3` and decides item 3. Then, in a new session, read `cad/vendor/drawings/README.md`, model the couplings and sensors, and do the block swap.

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-136**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 8. Key files
| File | What |
|---|---|
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Full CAD assembly**: STEP for Fusion, castings, cast-in features, views, data |
| `cad/vendor/` | Manufacturer STEP files (and the Z motor PDF) used by the assembly |
| `docs/decisions.md` | Decision log D-01 … D-113 |
| `docs/open-questions.md` | What's still open, in priority order |
| `docs/portal-relocation.md` | Assessment: how the portal goes back in the same place after a move |
| `docs/handoff-opus-tasks.md` | Routine tasks with ready-to-paste briefs for a session on Opus 5.5 |
| `docs/pre-wave1-plan.md` | Week-by-week list of what to settle between 14 Nov 2026 and wave 1 (4 Jan 2027) |
| `docs/electrical.md` | Power, safety chain, 7I76EU pin map, VFD settings |
| `docs/linuxcnc.md`, `linuxcnc/type0/` | LinuxCNC config, simulator, PC set-up, bench tests |
| `cad/v2/bench.py`, `cad/v2/out/bench_*` | Timber bench: drawings, cut list, assembly |
| `cad/v2/enclosure.py`, `cad/v2/out/enclosure_*` | Enclosure (sized from the assembly) |
| `docs/printed-parts.md`, `cad/v2/printed_parts.py`, `cad/v2/out/print/` | Printed parts (PETG) |
| `docs/curing-heat.md`, `tools/cure_heat.py` | Cure process, self-heating estimate, post-cure, tent and heater (Ampreg 30, D-124), heat estimate, heater tent |
| `tools/portal_overhang.py` | Beam overhang check (D-95; beam is now 150 high, still fine) |
| `docs/eg-mix-test-plan.md` | **Mix design and test pieces** (task 6 draft): recipes, tests, pass marks, quantities, kit |
| `docs/eg-moulds.md`, `aggregates.md`, `epoxy-options.md` | Casting notes (partly v1 sizes: use the assembly for sizes) |
| `docs/bom.csv` + generated `bom.md`, `phase1-bom.xlsx`, `phase1-cost.md` | Parts and costs |
| `docs/phase1-schedule.md` | Timeline and order waves |
| `docs/price-check-task-*.md`, `docs/cad-download-task.md`, `docs/supplier-messages.md` | Task files for the owner's local session, message drafts |
| `docs/review-task-eg-design.md`, `docs/review-eg-design-report.md` | EG design review: brief and report |

## 9. Working notes for the next session
- **CadQuery** isn't preinstalled in the cloud container: `pip install cadquery` (about 1 minute). `python cad/v2/assembly.py` takes about 2–3 minutes (vendor STEP import + clash check at 3 positions); `--envelopes` skips the vendor models.
- After changing the assembly, also run `cad/v2/enclosure.py`, `cad/v2/bench.py` and `cad/v2/base_cores_sketch.py` (they read `cad/v2/out/assembly/assembly_data.json` or the assembly numbers), and regenerate `cast_in_features.md` from the `features` list in `assembly_data.json` (one table per casting; no script in the repo).
- **Views:** `python cad/v2/render_views.py` re-renders the PNG views in `cad/v2/out/assembly/` (about 3 minutes; run it after `assembly.py`).
- **Rendering:** the CadQuery SVG exporter gives rotated views; use the matplotlib tessellation render instead. To view SVG drawings, screenshot them with Playwright (preinstalled).
- `docs/bom.csv` uses **CRLF** line endings and CSV-escaped quotes (`""`): keep both when editing.
- LinuxCNC can be tested in a Debian 12 Docker container (2.9.10 from linuxcnc.org); see `docs/linuxcnc.md` section 4.

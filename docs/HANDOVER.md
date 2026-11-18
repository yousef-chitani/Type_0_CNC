# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000. 18 Nov 2026: bottom roller screws settled, next tasks set (D-192)

**Done:** the owner gave the Screwfix page for the 5 bottom roller screws: Easyfix A2 M6 x 20 socket cap, 5209T, pack of 50, £7.59 inc VAT, in stock. This is the pack already in `docs/bom.csv` under X03, so Phase 1 stays £3,963.41, £236.59 left. The owner also set the order: the Z plate stiffness next session, and modelling the cast element as the next major task, which is when the table top height gets confirmed (D-192). The Fusion model was not touched this session. **`Type_0_v3` still needs the owner to save it if D-191 is not saved yet.**

**Left:**
1. **Z plate stiffness** (D-184). Next session.
2. **Model the cast element.** Next major task. Confirm the table top height of Z 70 from D-191 while doing it.
3. **Z risers and rails.** 15 risers and HGR20 rails on the plate, then the blocks, moving plate, screw and motor. The owner has not said whether this comes before or after the cast element.
4. **Top roller screws.** M6 x 25 for the 4 top holes: no live price yet. They thread into only 3 of tube wall: check this.
5. **Front Y riser bolts** at X -305 and 305 sit outside the risers (already wrong, not moved). The tub needs drilling for the new Y 629 bolts.
6. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.

**Exact next step:** in a new session, check the stiffness of `Z Fixed Plate` (6082, 150 wide, 350 high, 20 thick, D-184, D-191). Start from `docs/z-axis-assessment.md`, and report the result to the owner before changing the plate.

## 0000000000000000000000000000000000000000. 18 Nov 2026: Z fixed plate modelled (D-191)

**Done:** the owner saved `Type_0_v3` as version 5. The new component `Z Fixed Plate` is 150 wide, 350 high and 20 thick, at X -297.5 to -147.5, Y 417 to 437, Z 169 to 519, held to the bottom X roller by a rigid as-built joint. It has 9 holes, 6.6 clearance with counterbores 10.5 × 6.5 deep (D-191). Measured: all 9 hole axes match the roller and shim holes, the back face touches the bottom roller and the shim, and the next nearest parts are 8 away. The plate is flush with the roller sides, so it does not shorten X travel. Timeline 1243, 1 error and 5 warnings, the same failures as version 1. No material is assigned to the body. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Z risers and rails.** 15 risers and HGR20 rails on the plate, then the blocks, moving plate, screw and motor.
2. **Roller screws.** M6 × 20 for the 5 bottom holes and M6 × 25 for the 4 top holes. Not in `docs/bom.csv`, no live price yet. The top screws thread into only 3 of tube wall: check this.
3. **Table top height.** D-191 assumes Z 70, from the hidden wasteboard. Confirm it when the table is modelled.
4. **Plate stiffness** is not checked (D-184).
5. **Front Y riser bolts** at X -305 and 305 sit outside the risers (already wrong, not moved). The tub needs drilling for the new Y 629 bolts.
6. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, add the 15 risers and HGR20 rails to `Z Fixed Plate`. Re-count errors and warnings after every write.

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

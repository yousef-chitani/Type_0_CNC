# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000. 18 Nov 2026: supports swapped, Y motors at the back, rail length to re-decide

**Done:** owner settled the Z plate (D-184: 6082 in Phase 1 then steel, 15 risers stay, 350 high). In the open `Type_0_v3`: BK12 supports and NEMA 24 plates shown on X, Y and Y2, Y lengthened by 20 at the owner's request, Y risers and motors moved to the back, Y2 followed. Timeline 1183, 1 error and 5 warnings, the same failures as version 1. **The document is modified and not saved. Do not save it while the rail overlaps the riser unless the owner wants to.**

**Correction:** the 338 Y travel given to the owner was wrong, because it left the rail in place. With the rail shifted 61.5 forward, 550 rails give 386 and 570 rails give 406, against 350 needed. The owner chose +20 on the wrong figure, so **D-175 is unchanged and no D-185 is recorded yet**. Details are in `docs/printnc-assessment.md`.

**Left:** the rail shift (`Rigid 2`, 61.5 towards the front), item 3 and item 4 in the next entry.

**Exact next step:** the owner chooses 550 (back to `YCuttingArea` 385, `Rigid 312` sketch point to Y 561) or 570 (record D-185: rail 570, screw 670, tub 710, new LiMo prices). Then shift the rail and re-measure.

## 0000000000000000000000000000000000. 18 Nov 2026: model update planned, not started

**Done:** the owner saved the model as `Type_0_v3` version 1 (CNC mill project, 1 error and 5 warnings, 1182 timeline items) and allowed changes beyond parameters for D-179 to D-182 (D-183). No change has been made to the model. The session stopped at the context limit.

**Left, in this order.** Re-count errors and warnings after every write and undo any edit that raises them. Hide parts, never delete them, and list each change in `docs/printnc-assessment.md`. Do not save through the tool: tell the owner the document is modified.
1. **Supports (D-180), visibility only.** For X, Y and Y2: hide `HM12-57` and the `HM12 M6x50` fasteners, show the hidden `BK12` and `Nema24 Plate`. The timeline should stay at 1182.
2. **Y motors to the back (D-181).** Root joints `Rigid 311` (BF12 riser to YFrame) and `Rigid 312` (BKHM12 riser to YFrame) locate the risers, and the BK12, motor plates, screw and motor chain off them. Y2 has a `Derived Base Feature1`, so check whether it follows or needs its own edit. Confirm which Y direction is the rear first. Then check the riser fasteners, the 3 gap at each tub end (D-175) and the motor overhang against the 185 in D-142.
3. **Imported parts (D-180, D-182).** DFU1605 nut and 24HS40 motor from `cad/vendor/`, and a D25L35 coupling. Take the motor length from the datasheet, because the STEP includes other geometry. This gives the X motor overhang.
4. **Z axis (D-179): blocked.** The owner must first choose the plate material (steel or 6082), whether the 15 risers stay, and the plate height.

**Exact next step:** in a new session, ask the owner the three Z plate questions, then start at item 1.

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

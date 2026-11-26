# Type 0 CNC: handover (2026-11-26)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (49th session): V5 plan Task 4, Y1 coupling and risers
- **State at start:** `Type_0_v5` version 3 open with the 48th session's work in it, **not saved** (the owner had not saved it). This session's work is on top; still not saved.
- **Decided (owner, Q&A):** **D-369** risers fastened as PrintNC's: HM12-60 and BF12 bolt into M6 tapped in the steel bar; separate M6 cap screws in counterbores hold each riser to the Y tube (tube wall tapped).
- **Done (Fusion, not saved):** D25L35 coupling modelled from the MH table (hubs Ø25 x 11.75, Ø10 bores, clamp slit and M3 hole; spider zone as a Ø25 envelope), Y -36.5 to -1.5; screw journal and motor shaft each 9.5 into a hub; 0 overlap with the screw, the motor and the HM12-60. Risers: HM12 60 x 20 bar Y -47 to 62.5, BF12 60 x 25 bar Y 714.5 to 750; tapped holes on the housing patterns; tube screws at PrintNC's positions. PrintNC Y1 risers, their screws and the NEMA23 screws hidden. Y travel now 489.4 (blocks against the riser end faces). Timeline: the same 4 warnings. `tools/fusion/v5_y1_place.py`, `docs/v5-model.md` updated.
- **Found:** PrintNC drill guide 3B's holes are 0.75 off its own riser screws (Y -24.25/55.75 vs -25/55): transfer-drill the riser or check the guide.
- **Left:** Y2 (mirror of Y1: blocks, DFU, BF12, HM12-60, motor, screw, coupling, risers), 3 mm seats (SEAT, D-363: delete the screw and riser components first), flat-bar nut and fill plates, full check (re-point the carriage, riser and grease-fitting lines). Still open: HM12-60 vs 24HS40 hole square (49.4 vs 50), ask LiMo.
- **Exact next step:** owner saves `Type_0_v5` (48th and 49th sessions' work). Next session does Y2: mirror the `Y1 screw and motor` parts and the two HGH20CA blocks to X +377.5 (check the cable lead goes outboard, +X) and hides PrintNC's Y2 parts as for Y1.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (48th session): V5 plan Task 4, Y1 swap part 2 (DFU, HM12-60, motor, 1605 screw)
- **Done (Fusion, not saved; owner saved version 3 before it):** DFU1605 placed (axis X -377.5, Z 210, flange face Y 539, nut to Y 639, flats top and bottom). Its occurrence transform never holds, so a Move feature `DFU place` moves its bodies. HM12-60 placed (screw-end face Y 43, as PrintNC's HM12-57; motor end faces front; base Z 180) and 24HS40 on it (body to Y -172, cable lead outboard). PrintNC HM12-57 and NEMA23 hidden. **Then, from LiMo's end drawing (owner, now `cad/vendor/drawings/limo_1605_bk12_bf12_ends.png`):** the 1605 screw modelled (`Y 1605 Screw`, L 750, Y -11 to 739, Ø12 shoulder on the HM12 bearing at Y 43); the BF12 moved 5.1 forward (centre Y 733.15) and turned round so its circlip sits in the screw's groove. PrintNC's 1610 screw and coupler hidden. Screw clear of all bearings and the DFU bore. Overlap checks: only PrintNC parts being replaced are hit (old screw, coupler, 1610 nut plate and its M5 tie rods, 30-tall risers and their screws). Timeline: the same 4 known warnings, no errors. `tools/fusion/v5_y1_place.py` and `docs/v5-model.md` updated.
- **Found:** the HM12-60 STEP has its motor holes on a 49.4 square (its drawing: M4 on PCD 70 = 49.5), the 24HS40 STEP on 50. Ask LiMo which is right (owner).
- **Left:** D25L35 coupling (model it from the MH table, D-366; 16 gap between the Ø10 x 15 screw journal and the Ø10 x 20 motor shaft), risers 25 and 20 (hide the PrintNC risers and their screws), then Y2, 3 mm seats, flat-bar plates, full check (re-point the grease-fitting line).
- **Exact next step:** owner saves `Type_0_v5`; next session models the D25L35 10 x 10 in `Y1 screw and motor` from `cad/vendor/drawings/mh_jaw_coupling.webp`, centred on the gap between the screw journal end (Y -11) and the motor shaft tip (Y -27).

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-369**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 8. Key files
| File | What |
|---|---|
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Old** CadQuery assembly of the fixed-gantry design: **superseded by the Fusion 360 model `Type_0_v3`** (D-137, D-183). `cad/v2/out/assembly/cast_in_features.md` has a current section for the EG tub |
| `cad/vendor/` | Manufacturer STEP files (and the Z motor PDF) used by the assembly |
| `docs/decisions.md` | Decision log D-01 … D-336 |
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
| `docs/v4-pour.md` | V4 lean EG fill quantities (`23.5 L`) and pour/tamping order (`D-315`, `D-336`) |
| `docs/eg-moulds.md`, `aggregates.md`, `epoxy-options.md` | Casting notes (partly v1 sizes: use the assembly for sizes) |
| `docs/bom.csv` + generated `bom.md`, `phase1-bom.xlsx`, `phase1-cost.md` | Parts and costs |
| `docs/phase1-schedule.md` | Timeline and order waves |
| `docs/price-check-task-*.md`, `docs/cad-download-task.md`, `docs/supplier-messages.md` | Task files for the owner's local session, message drafts |
| `docs/review-task-eg-design.md`, `docs/review-eg-design-report.md` | EG design review: brief and report |

## 9. Working notes for the next session
- **Fusion 360 MCP:** configured in Antigravity via plugin `fusion-mcp` (`http://127.0.0.1:27182/mcp`). `Type_0_v4` is the active V4 design; do not save Fusion documents unless asked by the owner.
- **CadQuery** isn't preinstalled in the cloud container: `pip install cadquery` (about 1 minute). `python cad/v2/assembly.py` takes about 2–3 minutes (vendor STEP import + clash check at 3 positions); `--envelopes` skips the vendor models.
- After changing the assembly, also run `cad/v2/enclosure.py`, `cad/v2/bench.py` and `cad/v2/base_cores_sketch.py` (they read `cad/v2/out/assembly/assembly_data.json` or the assembly numbers), and regenerate `cast_in_features.md` from the `features` list in `assembly_data.json` (one table per casting; no script in the repo).
- **Views:** `python cad/v2/render_views.py` re-renders the PNG views in `cad/v2/out/assembly/` (about 3 minutes; run it after `assembly.py`).
- **Rendering:** the CadQuery SVG exporter gives rotated views; use the matplotlib tessellation render instead. To view SVG drawings, screenshot them with Playwright (preinstalled).
- `docs/bom.csv` uses **CRLF** line endings and CSV-escaped quotes (`""`): keep both when editing.
- LinuxCNC can be tested in a Debian 12 Docker container (2.9.10 from linuxcnc.org); see `docs/linuxcnc.md` section 4.

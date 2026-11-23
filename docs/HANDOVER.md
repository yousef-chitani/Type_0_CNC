# Type 0 CNC: handover (2026-11-23)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (16th session): ATC FK12 plan tasks 1 to 4 done in the model (not saved); checks not run
- **Task 1 (committed):** LiMo sells the FK12 only as an FK12 + FF12 set: C5 with angular contact bearings **$14.29**, coupling D20L25 **$2.86** (custom bores 3 to 10, so 8 x 5 is fine; hub depth not on the page; D20L30 same price). BOM A07 now "FK12 + coupling", £12.97 at list, ex shipping (curl, 23 Nov). The FF12 in the set is the tilt fallback block. LiMo's FK12 STEP is in `cad/vendor/fk12_limo.step`, measured sizes in `cad/vendor/README.md`: flange Z 0 to 10 (44 across flats, Ø54), nose Ø36 x 17, 4 x Ø4.5 on PCD 44 at 45° to the flats; collars stick out 0.2 at the top and 0.8 below the nose. **The STEP names the bearing pair DB (back-to-back); the spec assumed DF.** Not confirmed: ask LiMo; the bench tilt test stays.
- **Task 2:** 12 Remove features (timeline 1892 to 1903): mount body, 2 x 6804, spacer, 2 x M6 x 20 into the strip, 4 x M3 x 12, sensor M4 grub, hub M4 grub. The old components (`ATC Mount ...`, `Bearings 2 x 6804 ...`, `ATC Posts`) are still there, empty.
- **Task 3:** hub (component renamed `ATC Hub`): spigot cut, relief filled (flat Z 119), Ø12 pilot 6 deep, 4 x Ø4.5 + Ø8 x 4.5 counterbores at r 14 (0/90/180/270°). New `ATC Stub shaft (FK12)`: pilot Ø12 Z 119 to 125, flange Ø40 Z 114 to 119 (4 x M4 tapped), shoulder Ø14 Z 108.2 to 114 (on the FK12 top collar), journal Ø12 Z 82 to 108.2, thread Ø11.98 with cosmetic M12 x 1 Z 71 to 82, drive Ø8 Z 60 to 71. 4 x **M4 x 12** hub to flange (not x 10: x 10 gives only 2.5 of thread). M4 heads 13.3 from the forks.
- **Task 4:** `ATC Block FK12 (A07)`: vendor STEP, placed by moving that occurrence (flange top Z 108, nose to Z 81); Chinese part names renamed. 4 x M4 x 12 FK12 to top plate. `ATC Column plates (6082)`: top plate 70 x 70 x 12 Z 86 to 98 with an ear at -X (r 10 round the sensor), Ø36 bore, 4 x M4 tapped, M12 x 1 tapped for the sensor; walls 70 x 8 Z -8 to 86 at Y -149.8/-141.8 and -206.2/-198.2; motor plate 50 x 48.4 x 6 at **Z 34 to 40** (not 28 to 34: the plan's Z put the motor shaft only 5 into the coupling and the motor down to -52). Motor moved down 47 (Move feature): face Z 34, shaft tip Z 58, **lowest Z -46**. 4 x M3 x 10. `ATC Coupling 8-5 (LiMo D20L25, A07)` Z 46 to 71 (motor shaft 12 in, drive end 11 in, ends 2 apart). Locknut stand-in Ø22 x 8.5 Z 71.7 to 80.2 (in `ATC Fasteners`), 0.7 above the coupling. Sensor not moved (it already sits in the ear's hole, face Z 114).
- Timeline 2072 items, none of the new ones broken (Group27, the import group, reports "unknown"; its items are healthy). **Not saved.**
- **Not done in task 4:** the M4 lock grub hole for the sensor from the ear edge; screws and dowels joining walls, top plate and motor plate; the 2.5 key reach (by eye: the column is open at ±X from Z 40 to 86 and the coupling is 25 in from the wall ends, so it should be fine; measure).
- **The clash check timed out twice** (the MCP call, even with a region filter): run it in smaller pieces (one new body at a time against the region bodies).

**Left:** the rest of task 4 above; task 5 (base L and new strip); task 6 (checks: static, sweep, spindle, mass); task 7 docs (**D-295 to D-297 not written yet**; `atc-wheel.md`, `cast_in_features.md`, `design-issues.md` bench overhang, BOM A06 and the plate line). Ask LiMo: DB or DF pair; D20L25 hub depth.

**Exact next step:** a new session reads this entry and the plan `docs/superpowers/plans/2026-11-23-atc-fk-block-column.md`, finishes task 4 (sensor grub, plate joint screws and dowels, key reach), runs a clash check of each new ATC body on its own, then does task 5. The owner may save `Type_0_v3` first (the model is healthy).

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (15th session): ATC redesign approved: FK12 block, plate column, stub shaft (spec and plan; not modelled)
- Owner sent a picture of another machine's ATC (column beside the frame, wheel on a small block, motor hanging under) and its designer's note: "just a ball screw support block and motor mount, and one little custom stub shaft". Owner: the tub flange is much oversized.
- Q&A: approach A (FK12 flange block on a column of screwed 6082 plates; B tube column and C BK12 on a plate dropped); motor hangs below like the picture, lowest point about Z -46 (was -10), so **the ATC overhangs the bench front edge**; tub plate **50 x 40 x 10**, cast-in strip **50 x 10 x 40**, 2 x M6 at X 185/215, Z 21.
- FK12 sizes from THK sheet A15-314 (shaft 12, L 27, flange H 10, nose Ø36 g6 x 17, flange Ø54, 4 x Ø4.5 on PCD 44, 7001 DF pair, M12 x 1 locknut), fitted by THK mounting method B (flange on top of the plate, locknut inside the column).
- Spec approved: `docs/superpowers/specs/2026-11-23-atc-fk-block-column-design.md`. Plan: `docs/superpowers/plans/2026-11-23-atc-fk-block-column.md` (7 tasks). No D-numbers yet (plan task 7 adds D-295 to D-297). Nothing changed in `Type_0_v3` (it was saved at the start).
- Known risk in the spec: the FK12's DF pair is weak in tilt; bench test, fallback FF12 floating block lower in the column.

**Left:** everything in the plan: prices and FK12 CAD (curl), remove the old mount, hub and stub shaft, FK12 and column, base L and strip, checks, docs.

**Exact next step:** a new session runs the plan `docs/superpowers/plans/2026-11-23-atc-fk-block-column.md` from task 1 (the owner picks subagent-driven or native; native recommended).

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
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Old** CadQuery assembly of the fixed-gantry design: **superseded by the Fusion 360 model `Type_0_v3`** (D-137, D-183). `cad/v2/out/assembly/cast_in_features.md` has a current section for the EG tub |
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

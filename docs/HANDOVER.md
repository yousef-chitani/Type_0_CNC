# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026 (3rd session): flat tub wall tops under a bolted steel plate (D-256 to D-258); one-piece printed ATC bracket decided (D-259), not modelled
- Owner (Q&A): the 5 lip at X ±310 to ±315 goes; the wall top is cast flat at Z 113 and covered by an 80 x 10 x 690 steel plate per wall (Z 115 to 125) on 2 of grout; rails stay at the same height and rely on the plate's flatness; the 40 x 10 bar is cast flush in the wall top (Z 103 to 113) and only takes 10 x M6 x 20 countersunk hold-downs per plate on the rail line. Rail and riser screws tap the plate: M5 x 16, M6 x 20, M6 x 30. Outer strips and everything on them 5 lower (D-258); trigger mounts grow 5 at the bottom so the sensor gap stays 1. Also asked: keep 2 Y blocks per rail (D-20 stands).
- `Type_0_v3`, `EG Tub`: base feature `Wall top plates and strips (D-256 to D-258)` (plates, grout beds, bars, 3 strips, all holes), old bars, levelling layers and strips removed, combine `Wall tops flat Z113, bar and strip pockets`; casting 40,100,817 -> 39,293,267 mm³ (checked by hand). Screws trimmed by combine cuts in their own components; trigger flanges refilled and re-holed; chain supports and screws moved by Move features (world vector); the zip-tie plate by its joint offset (-5). Interference over the tub region: only screws in tapped holes and the overlaps that were there before (roller screws, sensor in its mount, rail 0.03 into the seat). Timeline: 35 unhealthy before and after. **Not saved.**
- BOM: G06 plates, X19 hold-downs, X20 rail screws (all unpriced); X13, X14, F02, F07 notes.

**Left:** D-259 ATC bracket remodel (one PETG print: block + arms 15 + motor plate 15 up to Z 83; posts to X 150/250, 32 long; drop 8 M6 x 25 and 4 M5 x 20; bottom post screws M6 x 25; update A06, `atc-wheel.md`, rerun the ATC clash check). Plate flatness spec and keeping both plates co-planar while the grout cures; mould drawing (flat wall top, bar at Z 103); `docs/machine-assessment.md` mass (tub about 1.9 kg lighter, plus 2 plates about 8.7 kg).

**Exact next step:** owner saves `Type_0_v3`. New session: read this entry and D-259, then rebuild the base feature `ATC Bracket (6082) (geometry)` in `ATC Bracket (6082)` (edit it in place; note: MoveFeature takes a world vector).

## 0000000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026 (2nd session): ATC direct drive, bracket along X 200, owner's fork (D-253 to D-255)
- Owner chose by Q&A: bracket in line with the spindle centre = arm along X 200; wheel stays at X 200, Y -174; direct drive under the plate, rigid with 1 bearing; twin arm plates; fork tabs tapered; the hidden extra forks in the owner's file are leftovers.
- `Type_0_v3`, `ATC Wheel (Phase 2)`: wall block on the floor's front face at X 200, 2 arm plates either side of the motor, Ø120 motor plate, posts at X 157/243, lower KFL004 and GT2 dropped, NEMA 17 face up Z 0 to 68, shaft Z 80 to 171 bored onto the motor shaft, hub Ø101.5 x 12, 8 owner forks (from the unsaved `ISO20_Toolholders` file, one fork) trimmed to 45° sectors, holder grooves shaped to the fork V, sensor and flag at r 44. `EG Tub`: the D-251 strip and its cores edited in place to X 187.5 to 212.5, Z -10 to 40. Timeline: 35 unhealthy before and after. **Not saved.**
- Clash check (same method as before): no clash except the spindle with holder 1 (the carried one) and screws in tapped holes. Forks 1 mm apart.
- BOM: A01, A03, A06, A07 re-described; A08 dropped (0). Phase 1 total unchanged, £3,963.35.
- Docs: `docs/atc-wheel.md` and `.png` rewritten, `docs/machine-assessment.md` sections 5 to 7.

**Left:** real motor length and encoder counts (StepperOnline page blocks curl: owner reads it or measures); fork screw M3 or M4; A06 re-pricing and ATC screws; strip on the tub mould drawing.

**Exact next step:** owner saves `Type_0_v3` (and `ISO20_Toolholders` if wanted). Then the LiMo basket and Dyfed call (`docs/price-check-task-17.md`), and apply the prices to `bom.csv`.

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

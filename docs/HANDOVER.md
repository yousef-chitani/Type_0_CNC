# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (4th session): Y fixed-end chain support moved 6 lower; hole cores cut; clash check run; saved
- `Type_0_v3`: `YAxis Cable Chain Fixed End Support:1` (with its zip-tie plate and 4 M5x20 (9)) moved 6 lower (origin Z 55 to 49); its 2 holes now line up with the strip screws M6x12 (6) at Z 56.5 and 71.5. Joints `Rigid 91` (support to `YFrame(Mirror)`, which held it) and `Rigid 230` (strip screw to support, which dragged the screws) are **suppressed**; screws put back at their D-271 place.
- Casting: the D-271 pocket cuts had left the tapped holes of the parts as casting. Cut out: 3 slivers in the lower strip holes (+X Y520, +X Y220 at Z 54 to 55, -X Y520 at Z 84 to 85; features `Strip pocket hole slivers` / `Remove strip hole slivers (D-271)`) and 20 cores Ø5 x 6 in the 40 x 10 bar holes, Z 97 to 103, which the M6 x 25 hold-down tips hit (`Bar pocket hole cores` / `Remove bar hole cores (D-271)`, 2,356 mm3). Casting 38,630.9 cm3.
- Clash check, visible bodies below Z 140: no clash left with the casting, the levelling pours or the chain support. The 114 left are screw threads in tap-drill holes, 0.03 mm float of the rails and countersunk heads on the plate top, and older stand-ins (risers, ATC, posts). Health 35 before and after.

**Saved** (owner: "Yes, save it").

**Left (model):** D-264 (ISO 7380 Y screws), D-266 (fill 3 holes; first check the top angle screws at Z 374 have their own holes), X 1610 plates fit check, D-275 hub, the X BKHM12 riser BK12 holes. **Docs:** BOM G06 text (8 mm pour, jack screws), X19 hold-down length M6 x 25, new jack screw line (unpriced), pour quantity; `cast_in_features`, `spec-gaps.md`.

**Exact next step:** a new session does D-264 and D-266.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (3rd session): owner Q&A on the design issues (D-264 to D-276); wall-top levelling pour modelled, saved
- Q&A answers recorded as D-264 to D-276 (`docs/design-issues.md` has a status per item). `requirements.md` updated (D-269). Task 26 added (rear ATC study, D-274). Z mount length question added to `supplier-messages.md` section 4 (D-276).
- `Type_0_v3` (D-271), **saved** (owner: "Yes, save it"): cast wall tops Z 113 to 107 (casting 39,293 to 38,633 cm3, about 88.9 kg); 40 x 10 bars Z 97 to 107; 2 mm grout replaced by 8 mm `Levelling pour 8 ±X (D-271)` bodies; 3 outer strips 6 lower, pockets re-cut, old +X Y220 pocket top filled; strip screws (M6x12 (5), (5)(Mirror), (6)), Y220 chain support, both trigger mounts and zip-tie screws #7 and #8 6 lower; trigger tops grown back to Z 133.5; 20 hold-downs extended to M6 x 25; 12 jack screws (bodies in `Joint screws added (D-262)`) and their M6 tap holes in the plates. Health 35 before and after.

**Left (model):** (1) the Y fixed-end chain support (`YAxis Cable Chain Fixed End Support:1`), its zip-tie plate and its 4 M5x20 (9) did NOT move: they are held by joints (`Rigid 1` in the support, `Rigid 271` in root, and the support occurrence itself). Its strip screws did move, so it is 6 out. Fix: edit those joints, or move the occurrence with the joints suppressed (one try moved the plate 12, undone). (2) Strip hole cores in the casting (if any) were not moved. (3) Clash check of the changed parts not run. (4) Then D-264 (ISO 7380 Y screws), D-266 (fill 3 holes; first check the top angle screws at Z 374 have their own holes), X 1610 plates fit check, D-275 hub, the X BKHM12 riser BK12 holes. **Docs:** BOM G06 text (8 mm pour, jack screws), X19 hold-down length M6 x 25, new jack screw line (unpriced), pour quantity; `cast_in_features`, `spec-gaps.md`.

**Exact next step:** a new session fixes the fixed-end chain support (item 1 above) and runs the clash check.

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

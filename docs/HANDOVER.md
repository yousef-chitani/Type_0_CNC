# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026: PrintNC spindle clamp on our Z (D-247)
- `Type_0_v3`, `Z Moving Parts`: the PrintNC 80 mm 3-hole clamp, 2 tram blocks, 4 M6 x 30 + washers, pivot M6 x 12, 4 M6 x 12, 2 M6 x 30 and 4 M8 grub screws added (same components as the PrintNC Z, so they move with our Z slider). Stand-in clamp body hidden.
- Spindle (Jianken) re-added 5 towards the plate: axis Y 297, nose height unchanged; clamp covers 43 to 122 from the front face.
- 9 tapped M6 holes cut in the moving plate (feature names `PNC clamp M6 holes 18/14/10`, threads cosmetic). Clash check: only screw-in-thread overlaps, plus washer and grub overlaps that the PrintNC model already has.
- X18 lists the new screws (unpriced). **Not saved.**

**Left:** HGH20 block screw heads under the clamp (rows Z 274 and 306) are not modelled: counterbores or flush heads needed. Tram-block M6 x 12 engage only about 5 (M6 x 16 would give 9). Then the 22 Nov list below.

**Exact next step:** ask the owner how to seat the block screws under the clamp (counterbore the moving plate, or low-head screws); then the owner saves `Type_0_v3`.

## 0000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026: PrintNC dual-carriage Z tried, Type 0 Z kept (D-246)
- Owner asked for the PrintNC dual-carriage Z with the Jianken spindle, without Y braces and with shorter saddles. Then dropped the saddle and brace changes ("Both stay").
- Tried in `Type_0_v3`: Jianken in the PrintNC clamp fits (spindle 38 closer to the beam, no clashes at the top or bottom of travel). Owner wanted our drive (DFU1605, HM12-60-V, brake motor), but the DFU1605 flange does not fit the 28 gap between the tram plate and the Z plate (9 and 5 deep cuts, only 2 of 6 flange screws fully held).
- **Owner: go back to our Z plate (D-246).** Model put back: `Z Axis Assembly` and `Z Fixed Plate` shown, `Zaxis Dual Carriage HGH15CA` hidden and unchanged, the trial spindle copy deleted. The 33 unhealthy timeline items were there before (2 joint warnings, the rest suppressed or rolled back). **Not saved** (owner: go on unsaved).
- No BOM change.

**Left:** as in the 20 Nov entry: the LiMo basket and the Dyfed call (`docs/price-check-task-17.md`); task 24 slot; the owner saves the model.

**Exact next step:** owner saves `Type_0_v3`, does the LiMo basket and Dyfed call and reports the prices; then apply them to `bom.csv`.

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

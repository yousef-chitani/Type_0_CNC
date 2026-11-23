# Type 0 CNC: handover (2026-11-23)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (18th session): owner changes the ATC column to one angle and the base L to bent 4 mm steel (D-299); docs only, not modelled
- **Owner (D-299):** the column is one continuous L in plan (aluminium angle): the tub-side wall plus a leg closing -X; the far wall goes; +X and -Y open. The base L is one laser-cut and bent 4 mm steel part from a bending service, the arm a U channel (long edges bent up 20, top Z 12), no gusset. Arm bending stiffness about as before (EI about 2.2e9 against 2.3e9, hand calc); end bends and twist not worked out: bench check.
- Spec has a revision section at the top; plan has a new **task 5b** (remodel, with the checks: -X leg squeezed between motor X 179 and sensor edge about X 165.3, leg ends inside r 58, angle root radius at the motor corner, sheet details: no counterbores in 4 mm, M5 row near the bend, upright Z layout, dowels); task 6 static check unticked (rerun).
- This session had no Fusion tools: **the model `Type_0_v3` still has the 2-wall column and the machined base L** (and is still not saved).

**Left:** task 5b, task 6, task 7 (D-295 to D-297, now pointing at D-299 for the base L). Ask LiMo: DB or DF pair; D20L25 hub depth. Prices for the angle and the bent part only from a live page.

**Exact next step:** the owner saves `Type_0_v3` (tasks 1 to 5 are healthy). Then a session with the Fusion MCP reads this entry and does plan task 5b (`docs/superpowers/plans/2026-11-23-atc-fk-block-column.md`), asking the owner the angle size first, then task 6, then task 7.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (17th session): ATC FK12 plan task 4 finished and task 5 done in the model (not saved); clash check clean
- **Owner Q&A (D-298):** motor plate 8 thick (Z 34 to 42) with M4s into its edges, motor screws M3 x 12; dowels only at the top plate; the base L arm ends in an upright flange screwed to the tub-side wall from the tub side (only 3.2 between the motor and the wall's inside face, and the motor goes in before the base L).
- **Task 4 finished:** top plate to each wall 2 x M4 x 16 (X 172/228, counterbored Ø8 x 4.5) + 2 x Ø4 x 16 dowels (X 186/214); each wall to the motor plate 2 x M4 x 12 along Y at X 193/207, Z 38 (counterbored in the walls' outer faces); sensor lock: M4 x 4 brass-tip grub from the ear edge along 202.5°, Z 92. Cosmetic threads on all tapped holes. Locknut stand-in given an Ø11 bore (it was solid).
- **Key reach measured** (6 x 6 path at Z 49.5, 67.5, 76 from ±X): only the stand-in tool on the wheel at X 286 (or 114) is in the way, 76 from the coupling; turn the wheel. Walls, plates and motor clear.
- **Task 5:** tub: old 80-wide strip removed, its pocket and 2 cores filled; new pocket 50 x 10 x 40 (X 175 to 225, Z -10 to 30) and 2 x Ø6.6 cores Y -27 to -25 at X 185/215, Z 21; strip `Steel strip 50 x 10 x 40 front (ATC, 2 x M6 ..., D-297)`. New component `ATC Base L (6082)`, one body: tub plate 50 x 40 x 10, arm 50 x 20 (Z -8 to 12) to Y -133.8, flange 70 x 38 x 8 (X 165 to 235, Z -8 to 30, Y -141.8 to -133.8), gusset 10 wide X 195 to 205 (Y -47 to -78, Z 12 to 30). 2 x M6 x **12** (not x 20: x 20 would go 4.5 past the strip's 2 deep core) in Ø11 x 6.5 counterbores; counterbore edge to gusset 4.5 (≥ 3). Flange: 4 x M5 x 16 at X 170/230, Z 0/24, heads on the tub side, tapped through the wall; 2 x Ø5 x 12 dowels at X 186/214, Z 24.
- **Clash check, one part at a time (now fast: about 1 min):** every new ATC body touches only its own threads (screws in tapped holes, sensor in M12, locknut on the shaft thread). Old, not ours: hub against each fork 2.6 mm³ (hub top unchanged since D-275); the motor STEP's own 2 inner bodies overlap it.
- Mass of the machined parts 1.2 kg (base L 346 g, hub 270 g, walls 278 g, top plate 125 g, stub shaft 98 g, coupling 55 g, motor plate 42 g). Lowest point Z -46. Note: these 6082 bodies carry Fusion's default material "Steel"; the masses above use 2.70 for 6082.
- Timeline 2111 items, none of the new ones broken. **Not saved.** Model scripts: a script that raises an error is rolled back, so results go to a file in the scratchpad.

**Left:** task 6 (sweep of hub, forks, screws, holders and flag; spindle against the wheel at drop-off, pickup and lifted); task 7 docs (D-295 to D-297 not written yet; `atc-wheel.md`, `cast_in_features.md` strip row, `design-issues.md` bench overhang, BOM A06/A07 and new lines, now with the base L flange and the 8 thick motor plate). Ask LiMo: DB or DF pair; D20L25 hub depth. Owner: the M5 heads at Z 0 sit 0.75 beside the arm (key goes in along Y; a ball-end key helps).

**Exact next step:** the owner saves `Type_0_v3`. Then a new session reads this entry and runs plan task 6 (`docs/superpowers/plans/2026-11-23-atc-fk-block-column.md`, sweep method in `docs/atc-wheel.md`), then task 7.

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

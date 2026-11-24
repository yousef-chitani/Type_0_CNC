# Type 0 CNC: handover (2026-11-24)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 24 Nov 2026 (20th session): ATC base L becomes one milled 6082 part (D-301); modelled, not saved
- **Owner Q&A (D-301):** replace the bent 4 mm steel base L with a single milled part: 6082-T6, solid 50 x 20 arm + gusset, made by a CNC service, old-spec fixings; then (counterbores on the tub plate face the wall upright 85 away, so a 3-axis spindle cannot cut them) **M6 heads proud**.
- **Model:** bent body removed; component renamed `ATC Base L (6082, milled)`, one body (features: plate+arm extrude, upright, gusset, R 3 fillets, 2 hole cuts): tub plate 50 x 40 x 10 (Y -47 to -37, Z -10 to 30, 2 x Ø6.6 at X 185/215, Z 21); arm 50 x 20 Z -8 to 12 to Y -133.8; gusset X 195 to 205, Z 30 at Y -47 to Z 12 at Y -78; upright 70 x 52 x 8 (X 165 to 235, Y -141.8 to -133.8, Z -8 to 44) with 4 x Ø5.5 (X 172/229, Z 21/38), 2 x Ø9 key holes (X 193/207, Z 38), 2 x Ø5 dowel holes (X 186/214, Z 24); R 3 inside corners. 368 g (volume x 2.70; body material still says Steel, like the other 6082 parts).
- **Angle:** 2 x Ø5 through the tub-side leg at X 186/214, Z 24 (dowels).
- **Fasteners** (`ATC Fasteners`, base feature `Base L milled fasteners (D-301)`): the 6 old base L screws deleted; new 2 x M6 x 16 (head Y -53 to -47, tip Y -31), 2 x M5 x 20 at X 172 and 2 x M5 x 16 at X 229 (heads Y -133.8 to -128.8, tips unchanged), 2 x dowel Ø5 x 16.
- **Checks:** interference of the 22 bodies around the base L: only screws in tapped holes (M6 in the strip, M5 in the angle). Proud M5 heads reach r 56.1 of the wheel axis (holders start r 66.5); gusset at Y > -78. Key swing worked out by hand, not with key bodies: M6 key blocked only toward +X (gusset) and down (arm), more than 180 deg free; M5 and the M4 through the Ø9 holes from +Y, free. Timeline 2181, 37 unhealthy (all old). Lowest Z -46.

**Left:** task 6 (sweep, spindle against the wheel, rerun static overlap and masses), task 7 docs (D-295 to D-297, BOM: angle 80 x 80 x 8 and the milled base L, prices only from a live page or a service quote). Owner job 6: save, angle root R 12 or less.

**Exact next step:** the owner saves `Type_0_v3`. Then a new session reads this entry and runs plan task 6 (`docs/superpowers/plans/2026-11-23-atc-fk-block-column.md`, sweep method in `docs/atc-wheel.md`), then task 7.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (19th session): ATC plan task 5b modelled (D-300): angle column and bent 4 mm steel base L; not saved
- **Owner Q&A (D-300):** angle 80 x 80 x 8, legs cut; base L without dowels (M5 only); root radius unknown, so R 6 modelled; the base L upright widened so the M5s spread again.
- **Column:** the tub-side wall body became the angle (`Column angle 80 x 80 x 8 cut ...`): trimmed to X 168, -X leg X 168 to 176 down to Y -208, root R 6; old base L holes filled. Wall -Y and its 5 joint parts removed; its unused top plate holes and motor plate taps filled; the screw at X 172, Y -202.2 kept for the -X leg. New: 1 x M4 x 16 + 2 x dowel 4 x 16 (top plate to -X leg), 2 x M4 x 12 (-X leg into the motor plate edge, Z 38). Motor plate trimmed to X 176 with an R 13 corner relief. Clearances: -X leg 2.65 to the sensor, 2.85 to the motor; root up to about R 12 fits (motor plate relief), the motor alone about R 18.
- **Base L:** component renamed `ATC Base L (steel 4, bent)`, the 6082 body removed; new one body (material Steel, 375 g): tub upright 50 x 38 (Y -41 to -37, Z -8 to 30, 2 x Ø6.6), web Z -8 to -4, side flanges up to Z 12 (Y -132.8 to -46, 1 mm relief), wall upright 70 wide (X 165 to 235, Z -8 to 44) with 4 x Ø5.5 at X 172/229, Z 21/38 and 2 x Ø9 access holes over the motor plate M4 heads. Bends R 4 inside, R 8 outside: **not confirmed with a bending service** (SendCutSend guide by curl: U channel base ≥ 2 x flange, met; their min-flange table did not load by curl).
- **Screws:** 2 x M6 x 12, heads proud (tip in the strip hole, 2 short of its back face); 2 x M5 x 16 at X 172 tapped 16 deep along the -X leg (1.9 wall each side), 2 x M5 x 12 at X 229. Cosmetic threads on all new taps. One fault found and fixed: the -X leg join half filled the M4 tap at X 172, Y -145.8 (re-cut).
- **Checks:** clash of every changed body: only screws in their tapped holes (and old: sensor in M12, FK12 screws, grub). Key reach (hex keys as bodies): **the motor M3 in the closed corner (X 184.5, Y -158.5) gets only 2 x 35 deg of 2.5 key swing in place (needs 60): owner chose to screw the motor to the motor plate on the bench, then slide the pair in from -Y (path checked clear)**; the other 3 M3s 120 deg or more; -X leg M4s, base L M5s (long arm in the channel), M6s, motor plate M4s through the Ø9 holes: all clear; coupling and locknut from -Y and +X: only a stand-in tool on the wheel (turn the wheel). Timeline 2173, no new item unhealthy (37 old ones). Lowest Z -46.
- Masses: angle 250 g, top plate 125 g, motor plate 40 g (2.70); base L 375 g (7.85).

**Left:** task 6 (sweep, spindle against the wheel, rerun static overlap and masses), task 7 docs (D-295 to D-297, BOM lines incl. angle 80 x 80 x 8 and the bent base L; prices only from a live page). Owner list: `docs/owner-todo.txt` job 6 (save, angle root R 12 or less, bending service: inside radius, minimum flange, corner relief); ask LiMo DB or DF pair and D20L25 hub depth.

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

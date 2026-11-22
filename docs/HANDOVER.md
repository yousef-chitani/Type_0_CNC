# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026 (2nd session): ATC direct drive, bracket along X 200, owner's fork (D-253 to D-255)
- Owner chose by Q&A: bracket in line with the spindle centre = arm along X 200; wheel stays at X 200, Y -174; direct drive under the plate, rigid with 1 bearing; twin arm plates; fork tabs tapered; the hidden extra forks in the owner's file are leftovers.
- `Type_0_v3`, `ATC Wheel (Phase 2)`: wall block on the floor's front face at X 200, 2 arm plates either side of the motor, Ø120 motor plate, posts at X 157/243, lower KFL004 and GT2 dropped, NEMA 17 face up Z 0 to 68, shaft Z 80 to 171 bored onto the motor shaft, hub Ø101.5 x 12, 8 owner forks (from the unsaved `ISO20_Toolholders` file, one fork) trimmed to 45° sectors, holder grooves shaped to the fork V, sensor and flag at r 44. `EG Tub`: the D-251 strip and its cores edited in place to X 187.5 to 212.5, Z -10 to 40. Timeline: 35 unhealthy before and after. **Not saved.**
- Clash check (same method as before): no clash except the spindle with holder 1 (the carried one) and screws in tapped holes. Forks 1 mm apart.
- BOM: A01, A03, A06, A07 re-described; A08 dropped (0). Phase 1 total unchanged, £3,963.35.
- Docs: `docs/atc-wheel.md` and `.png` rewritten, `docs/machine-assessment.md` sections 5 to 7.

**Left:** real motor length and encoder counts (StepperOnline page blocks curl: owner reads it or measures); fork screw M3 or M4; A06 re-pricing and ATC screws; strip on the tub mould drawing.

**Exact next step:** owner saves `Type_0_v3` (and `ISO20_Toolholders` if wanted). Then the LiMo basket and Dyfed call (`docs/price-check-task-17.md`), and apply the prices to `bom.csv`.

## 000000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026: ATC wheel modelled (D-250 to D-252); whole-machine assessment
- Owner chose by Q&A: pickup X 200, Y -85, slide in along -Y (D-250); a cast-in tapped strip on the right wall's front face (D-251); stand-ins (D-252). **Proposed by Claude, owner to confirm:** the bracket parts, the lift to Z 232, the drive at X 342 (envelope to X 380), the strip's size, threads and the Ø6.6 void behind each hole.
- `Type_0_v3`: new top-level component `ATC Wheel (Phase 2)` (bracket, posts, 2 KFL004, shaft and Ø128 hub, 8 forks, 8 holders and tools, NEMA 17 and GT2 drive, index sensor, screws). In `EG Tub`: body `Steel strip +X front (ATC)`, combines `ATC front strip pocket` and `ATC strip hole clearance`. No clash at rest or at 4 tool-change positions (copies of the Z bodies moved; the joints do not move from scripts). Timeline: 35 unhealthy items before and after. **Not saved.**
- BOM: A01, A03, A05 to A08 re-described for the wheel; F07 covers the strip. A06 price is for the old stock list and must be re-priced; A08 belt now about 366. Phase 1 total unchanged, £3,963.35.
- Docs: `docs/atc-wheel.md` (layout, sequence, gaps), `docs/atc-wheel.png`, `docs/machine-assessment.md` (travel, clashes, stiffness, mass, cost, open items).

**Left:** the open items list in `docs/machine-assessment.md` section 7; the strip must go on the tub mould drawing.

**Owner's new request (22 Nov 2026, not started: session at its context limit):** "direct drive the tool changer and have the bracket inline with centre of the spindle". The owner has a toolholder model open in Fusion (use it in place of the stand-in holders, D-252).
- Direct drive: drop the A08 GT2 3:1 belt and pulleys. The NEMA 17 (A03) goes on the wheel shaft axis (coupling or hollow hub), probably under the bearing plate. Check: room under it (lowest ATC part is Z 0, tub bottom Z -15), 0.8 Nm without the 3:1 reduction, and the index accuracy at the fork (r 89).
- "Bracket inline with centre of the spindle": ask the owner what it means before modelling. Likely: the arm runs along X 200 (the pickup line, the wheel centre line), not along X 315. Then the strip on the right wall's front face (D-251) may need to move or change. Also ask: does the wheel stay at X 200, Y -174?
- Then rerun the clash check (script approach in `docs/atc-wheel.md`: move copies of the Z bodies by dX 421.8, dY -352/-382, dZ 11/62) and update D-250 to D-252, A03, A06 to A08 and `docs/atc-wheel.md`.

**Exact next step:** new session: read this entry and `docs/atc-wheel.md`, ask the owner the 2 questions above, then remodel `ATC Wheel (Phase 2)`. Owner: save `Type_0_v3` first.

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

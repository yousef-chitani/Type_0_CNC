# Type 0 CNC: handover (2026-11-26)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (37th session): review of D-320 to D-337; stale D-337 values fixed in the docs
- **Done:** checked D-320 to D-337 against the BOM and `docs/v4-model.md`. The numbers hold (D-331 belt 250 mm / 50T at 75 mm centres, pull margins 2.3x to 3.2x; D-337 edge walls and rail/block positions; D-336 F01 £208.39). Stale values from before D-337 fixed: Y bar M8 screws `X = ±188` -> **`±183`** in `X23` (`docs/bom.md`, `docs/bom.csv`) and `docs/v4-model.md`; `rail_x` 205 -> **200** in the `docs/v4-model.md` parameter list. No decisions changed, model untouched.
- **Open points found (owner to decide, not changed):** (1) the `Ø14` bar-screw counterbore at `X ±183` reaches `X ±190`, exactly the rail edge: no margin (same as before at ±188 / rail 195); move 1 to 2 mm inboard? (2) D-320's "no bracket" and "coupling inside the HM12" are overtaken by D-326/D-331 but not marked; (3) D-333 "plugged/removed" for the 9 old Z-plate holes: the RFQ drawing must say which; (4) Phase 1 £4,386.61 is at least £186.61 over the £4,200 budget (X24, X25, F30, G10 and others unpriced); the X25 note still quotes an old £215.66 overrun.
- **What is left:** as the 36th-session entry: owner saves `Type_0_v4`, LiMo `865 mm` X screw, `M15`/`M16`/bearings prices; Task 29 steps 3 to 6.
- **Exact next step:** owner saves `Type_0_v4`; next session runs **Task 29 step 3** (assembly order and hex-key access check on `Type_0_v4`).

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (36th session): D-337 edge-wall fixes on `Table plate M11` and `X`/`Z` fold plates in `Type_0_v4`
- **Done (`D-337`, `Type_0_v4` NOT saved — owner saves in Fusion):**
  - **X & Z fold plates (`70 x 142 x 20` 6082):** removed the `4 x Ø8 x 6` HM12 counterbores (front edge wall was `1.25 mm`, now **`3.00 mm`** with plain `Ø4.5` through-holes); updated the `8 x` HM12 mounting screws from `M4 x 25` to surface-mounted **`M4 x 30`** A2 SHCS (`WF2362` in `X21`, price to re-check at checkout; heads clear pulleys by `13.5 mm` and belts by `3.75 mm` laterally / `5.8 mm` axially; envelope unchanged).
  - **Table plate `M11` (`460 x 330 x 25`) & Y rails:** moved `rail_x` inward `5 mm` from `205` to **`200 mm`** (Y bars `X ±175..±225`, M8 T-nut holes `X ±183`, Y rails `X ±190..±210`, Y blocks `X ±178..±222`, table block mounting holes + `16 x M5 x 16` screws `X ±184` and `±216`). Outer `X = ±200` M6 fixture hole columns are now centred between the rail block mounting holes; outer counterbore edge wall increased from `4.0 mm` to **`9.0 mm`**; drip-skirt clearance to blocks increased from `3 mm` to **`8 mm`**.
  - **Checks:** timeline **320 items, 0 unhealthy**; **0 unexpected overlaps** at `y_pos = 0, -150, +150`.
- **What is left:** owner saves `Type_0_v4` in Fusion and updates LiMo (`865 mm` X screw) + prices `M15`/`M16`/bearings + re-checks `WF2362` (`M4 x 30`) at checkout; Task 29 steps 3 to 6 (assembly check with key access, make-ability check per part, Fusion drawings + STEP per part, RFQ cover sheets).
- **Exact next step:** owner saves `Type_0_v4`; next session runs **Task 29 step 3** (assembly order check on `Type_0_v4`, verifying hex-key access for every screw and the pre-pour vs post-pour beam fastener sequence).

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-337**).
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

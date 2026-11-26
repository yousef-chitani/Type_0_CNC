# Type 0 CNC: handover (2026-11-26)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (40th session): V5 started; weighted matrix of ideas to keep
- **Decided (owner):** **D-338** V5 starts (V4 kept as history); **D-339** shops do surface grinding only, everything else bought or printed (owner saw/drill/tap allowed: confirmed 26 Nov); **D-340** no wheel: fixed rack, 2 rows, 16 to 18 tools.
- **Done:** `docs/v5-idea-matrix.md` (tables from `tools/v5_matrix.py`; weights accuracy 25, cost 20, build 15, bought/printed 15, proven 10, carry 10, rack 5; out if it needs milling/turning/laser or scores accuracy 2 or less; sensitivity under 2 other weightings). Result, not decided: **close to stock PrintNC** (moving gantry, bolted steel tube frame, steel beam, epoxy-poured rail seats with grinding as fallback, inline drives, Type 0 Z on bought cut plate, T-slot bed, rack behind the bed under the gantry with +50 Z, sand fill). Screws C5/C7 a tie. Rack: 60 pitch, row of 8 spans 420, of 9 spans 480 (X travel must be at least that). Task 30 closed.
- **Biggest risks named in the doc:** ±0.02 on a PrintNC with +50 Z not shown; PrintNC no-welding not confirmed; grinding unpriced.
- **What is left:** owner answers the 4 questions at the end of `docs/v5-idea-matrix.md`, and says whether the V4 JLC prices (Task 29) are still wanted.
- **Exact next step:** owner answers questions 3 (epoxy pour or grinding) and 4 (C5 or C7); questions 1 and 2 answered (owner-made allowed, D-339; start from PrintNC, D-341); then next session writes the V5 design doc (Task 31) from the matrix winners.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (39th session): Discord feedback, "too many custom parts" / use PrintNC
- **Done:** owner's and ihavenofish's Discord points checked against the repo: `docs/feedback-discord-2026-11-26.md`. No design change, no D-number, model untouched.
- **Findings:** V4 wave 1 is 30 custom pieces (about 22 shapes) over 4 shop processes (mill, lathe, laser, grind); Phase 1 already over budget. v3 was PrintNC on our EG tub and was left mostly for tub reasons (D-288, D-305); ihavenofish proposes stock PrintNC (own frame) with 3 changes: X rails on the front face, X overhang off one side for a rack along Y, +50 Z. A side rack fits about 6 tools per row (Ø45 holder flanges, about 60 pitch) in 300 Y travel. *(Corrected in the 40th session: first said 40 pitch, 8 to 9 tools.)*
- **What is left:** owner answers the 4 questions at the end of the feedback doc (above all: why a new machine rather than a PrintNC). JLC prices for `cad/v4/jlc-step/` still wanted either way.
- **Exact next step:** owner uploads the JLC parts and answers question 2; if "now", next session writes the one-page V4 vs PrintNC + 3 changes side-by-side (no modelling).

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-341**).
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

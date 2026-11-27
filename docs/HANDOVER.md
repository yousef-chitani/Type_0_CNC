# Type 0 CNC: handover (2026-11-26)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `.claude/NEXT_PROMPT.md` and `.claude/CODEMAP.md`, then the rules in `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (54th session): bundle E2 for Y: seat bodies and pour plan
- **State at start:** `Type_0_v5` saved by the owner with the 53rd session's work (rods, nuts, roller screws).
- **Decided (owner, Q&A):** **D-374** two separate pours, one per seat, risers off (height across not tied: the plan doses the lower tube about 21 g more per 1 mm, which only gets close, so an across failure is likely); **D-375** tube tapped M5 first, greased grub screws as plugs, Ø6 drilled through the seat with the rail as guide once it passes; **D-376** waxed aluminium bar dams on tape plus plasticine; **D-377** a failed seat gets a skim pour, then scraping, a grinding shop last.
- **Done (Fusion, not saved):** new `tools/fusion/v5_y_seats.py` builds `Y Rail Seats (epoxy, 30 wide)`: Y1 X -392.5 to -362.5, Y2 X 362.5 to 392.5, Y 64 to 714, Z 160 to 163, 11 Ø6 holes each; **58,500 mm³ gross / 57,567 net per seat**. Check: timeline 1257, the same 4 warnings, no errors, no seat overlaps (seats confirmed in the check's list; direct test against rails, tubes, M5x20, centering guide: 0); Y travel 480.1. M5x20 rail screws still reach through the 6 mm wall.
- **Done (docs):** pour plan in `docs/v5-rail-seats.md` (before, pour, cure, drilling, measuring with X05/X01/X02, fail); D-374 to D-377; run order in `docs/v5-model.md`.
- **Left:** owner saves `Type_0_v5`; Ampreg 30 mixed density (1.1 assumed) and the X02 level's sensitivity to confirm; a stiff bar over 800 long for the across check and a flat sled block for the along check (neither on the parts list); whether the frame fits the post-cure tent; X seats on the beam front (thickness, pour) wait for bundle C.
- **Exact next step:** `.claude/NEXT_PROMPT.md` (bundle C once the bed STEP is in `cad/vendor/`, else D).

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (52nd and 53rd sessions): bundle B, E1, Y plate rods and roller screws
- **State at start:** the 52nd session did bundle B (docs consistency) and E1 (`docs/v5-rail-seats.md`: HIWIN HG20 tolerances by curl, **D-371** pass mark, **D-372** seats 30 wide) and wrote the M5 rod code, but ended without committing or running it; the 53rd committed that (f1d1189). `Type_0_v5` saved by the owner with the 51st session's work.
- **Decided (owner, Q&A):** **D-373** through rods with nuts at both ends (Y travel 480.1, 450 needed); the 2 gantry-to-roller M6x12 per side above the upper outboard rod cut to 9 under the head.
- **Done (Fusion, not saved):** 6 rods Ø5 x 200 and 12 nuts per side (`v5_y1_place.py`, Y2 by `v5_y2_place.py`); new `tools/fusion/v5_roller_screws.py` cuts the 4 screws (copies, PrintNC bodies hidden); `v5_check_task4.py` checks rods against every body. Check: same 4 warnings, no errors, **Y travel 480.1 on Y1 and Y2**; lower rods clear the HGH20CA block screw heads by 0.44 (tight with real ISO 7380 heads, about 0.2). Notes in `docs/v5-model.md` "Plate rods and roller screws".
- **Left:** bundle C (bed: needs the owner's STEP in `cad/vendor/`, not there); E2 (seat bodies 30 wide, then the pour plan). Owner: save `Type_0_v5`; the untracked `PrintNC V4 Metalcutter V4.0.33 Elements to take.step` (repo root) and `cad/v2/Facebutton v2 frame.step` are not committed (yours: say if they belong in git).
- **Exact next step:** owner saves `Type_0_v5`. Then follow `.claude/NEXT_PROMPT.md` (E2 seat bodies, or bundle C if the bed STEP is in).

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-373**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 8. Key files
| File | What |
|---|---|
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Old** CadQuery assembly of the fixed-gantry design: superseded by the Fusion 360 models (D-137, D-183); **the live CAD is `Type_0_v5`** (V5, D-338 on; `docs/v5-model.md`). `cad/v2/out/assembly/cast_in_features.md` has a section for the old EG tub |
| `cad/vendor/` | Manufacturer STEP files (and the Z motor PDF) used by the assembly |
| `docs/decisions.md` | Decision log D-01 … D-373 |
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
- **Fusion 360 MCP:** configured in Antigravity via plugin `fusion-mcp` (`http://127.0.0.1:27182/mcp`). `Type_0_v5` is the live V5 design (`Type_0_v4` is frozen); do not save Fusion documents unless asked by the owner.
- **CadQuery** isn't preinstalled in the cloud container: `pip install cadquery` (about 1 minute). `python cad/v2/assembly.py` takes about 2–3 minutes (vendor STEP import + clash check at 3 positions); `--envelopes` skips the vendor models.
- After changing the assembly, also run `cad/v2/enclosure.py`, `cad/v2/bench.py` and `cad/v2/base_cores_sketch.py` (they read `cad/v2/out/assembly/assembly_data.json` or the assembly numbers), and regenerate `cast_in_features.md` from the `features` list in `assembly_data.json` (one table per casting; no script in the repo).
- **Views:** `python cad/v2/render_views.py` re-renders the PNG views in `cad/v2/out/assembly/` (about 3 minutes; run it after `assembly.py`).
- **Rendering:** the CadQuery SVG exporter gives rotated views; use the matplotlib tessellation render instead. To view SVG drawings, screenshot them with Playwright (preinstalled).
- `docs/bom.csv` uses **CRLF** line endings and CSV-escaped quotes (`""`): keep both when editing.
- LinuxCNC can be tested in a Debian 12 Docker container (2.9.10 from linuxcnc.org); see `docs/linuxcnc.md` section 4.

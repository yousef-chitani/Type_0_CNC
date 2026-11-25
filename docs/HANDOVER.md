# Type 0 CNC: handover (2026-11-25)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 25 Nov 2026 (33rd session): goal set: a quote-ready design before wave 1 (task 29)
- **Owner's goal:** before wave 1 (4 Jan 2027) the design is fully defined, makeable and assemblable, so machine shops can quote the made-to-order parts.
- **Gap map written:** `docs/tasks/29-quote-ready-design.md`. Read from `Type_0_v4` (timeline 194, read-only, nothing changed): 19 made-to-order parts; 6 are envelopes or out of date (X BK12/BF12 pads and X motor bracket against D-320, X nut bracket, beam end dam, Y motor plate, drip skirts); every body has the material Steel. Steps: freeze V4 (task 28 questions), finish the model, assembly order with key access, make-ability check per part, drawings and STEP, RFQ.
- Budget: Phase 1 already £359.80 over and most of these parts are unpriced.
- **Exact next step:** owner answers the 3 questions in `docs/task28-folds-and-footprint.md` and the 4 in task 29. Then task 27 Task 7 and the D-320 model change.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 25 Nov 2026 (32nd session): G15 screws priced; Z and X belt folds sketched; footprint drawn (task 28)
- **G15 priced (curl, 25 Nov):** Westfield 16 x M10 x 30 socket cap 12.9 £6.98, 8 x M10 x 35 countersunk A2 £5.51, 12 x M8 x 20 12.9 £3.29; KJN 12 x M8 T-nut £5.16 (Store API). **£20.94; Phase 1 £4,559.80, £359.80 over.** The Westfield order now passes £40 ex, so delivery is free. The model draws the M10 x 30 with hex heads (socket cap fits). Owner to choose A2 or 12.9 (£7.28) for the countersunk screws.
- **Folds and footprint sketched, docs only:** `docs/task28-folds-and-footprint.md`, drawings from `tools/task28_sketches.py` (`docs/sketches/task28_*.svg`). Z: motor behind the Z fixed plate, HTD 310-5M-15, top Z 700 to about 590 (spindle top at Z max is 545, so little more is possible). X: motor behind the beam, HTD 250-5M-15, X min about -536 (D-320 inline, estimate) to about -430. Both: the HM12-60 holds the coupling, so a pulley needs a stub shaft on 2 bearings or a longer screw end (reopens D-207/D-211); X fold needs a motor plate again, against D-320. Belt margin (D-322) not checked; pulleys and belts not priced.
- **Footprint:** floor per work area V4 7.9, V4 X folded 7.3, v3 + wheel 9.3, v3 + 12-tool rack at 60 pitch about 5.5 (but 1.15 m² of floor against 0.85). Max is right on floor per work; it is more floor in total and goes back to the moving gantry.
- Fusion: `Type_0_v3` was opened read-only for its sizes; `Type_0_v4` is active again. Nothing changed or saved.
- **Exact next step:** owner answers the 3 questions at the end of `docs/task28-folds-and-footprint.md`. Task 27 (model D-320, Task 7) is still first in line.

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

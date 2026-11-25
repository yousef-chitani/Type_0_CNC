# Type 0 CNC: handover (2026-11-25)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 25 Nov 2026 (27th session): ATC mount reworked: inboard hub block on the end plate (D-317); model not saved
- **Owner:** "the ATC bracket is a ridiculous shape, come up with something more elegant". Q&A: "Inboard hub (Recommended)" (over a hanger from the beam end and a tidied upright bracket), then "Approve, model it".
- **Why the old one was a dog-leg:** the right upright stands behind the wheel (Y 185+), so the bracket had to go round the 197 sweep to the outboard drive. The end plate X+ is right behind the wheel axis.
- **D-317 modelled in `Type_0_v4` (not saved):** one 6082 block on the end plate's outer face (flange with M16 head pockets, floor, motor web, wall). The FK12 goes through the wall and the stub runs to the hub's inboard face. GT2 20T/60T belt inside the block (X 293 to 307) from a 40-long NEMA 17 without encoder. The LJ12A3 sensor sits in the wall at r 44, with its flag on the hub. Bracket, column, coupling and 17HS24-E1K removed. Nothing is past the disc: ATC X max 435 (159 in), machine X max 594 to 550 (44 narrower; the beam end sets it).
- **Checks clean:** 184 timeline items healthy; wheel turned 0 to 30°; the four poses (engaged, lifted, withdrawn with a Ø20 x 100 tool, withdrawn lifted); table at y ±150. Only expected overlaps (M4 x 40 in the untapped stub flange). Details: `docs/v4-model.md` (Task 6 rework).
- **New constraint:** past X 265 the spindle needs a soft limit (nose 50 or higher); a 100 tool at nose 25 reaches the 60T at X 300.
- **BOM:** A03 (needs re-pricing: 40-long NEMA 17 plus driver), A06, A07 (coupling dropped), A08 back in (£9.32, 7 Nov price), A09; F26/X25: end plate X+ gets 4 x M8 tapped now (wave 1). Phase 1 still £4,416.08.
- Spec `docs/superpowers/specs/2026-11-25-atc-inboard-hub-block-design.md`, plan `docs/superpowers/plans/2026-11-25-atc-inboard-hub-block.md`.
- Fusion note: inside a base feature edit, `component.bRepBodies` is empty and the bodies carry other names; use `baseFeature.bodies` and match them by bounding box. A script that fails mid-edit leaves Fusion in the edit (design reads as direct); `commandDefinitions.itemById('BaseFeatureStop').execute()` gets out.

- **4 faults found after modelling (assembly walk-through), fixes written, not modelled:** FK12 screw heads 1 from the stub flange (sink the flange into the hub); motor cannot be fitted between the web and the wall (separate slotted motor plate); locknut cannot pass the Ø12 pulley seat (Ø8 seat, 60T bore 8); M8 positions set. See `docs/v4-model.md`, end.
- **Changed after the owner approved the spec:** pulleys moved next to the flange, a motor web added, the motor 40 long (about 0.45 Nm, not 48 and 0.59), the FK12 through the wall with its flange outboard.

**Left:** model the 4 fault fixes; owner saves `Type_0_v4`; owner confirms the D-317 sizes and the 40-long motor (A03 price); the 4 M8 and FK12/motor screws are not modelled; LinuxCNC keep-out past X 265; Task 7 (fill quantities per D-315, wave 1 lengths); the 14 unpriced BOM lines.

**Exact next step:** the owner saves `Type_0_v4`. A new session models the 4 D-317 fault fixes (`docs/v4-model.md`, last section), then runs plan Task 7 from `docs/superpowers/plans/2026-11-24-v4-fixed-gantry.md` with D-315, and adds the F26 X+ 4 x M8 to the wave 1 drawing notes.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 24 Nov 2026 (26th session): V4 plan Task 6 done: ATC wheel on the right side (D-315, D-316); wheel not saved
- **Owner saved the design as `Type_0_v4`** before this session's changes.
- **D-315 (owner):** the EG fill is not structural; a lean mix packed into the voids. Task 7's pour plan shrinks to quantities and fill order. The cheaper resin option (saves £145.61) is open again; BOM not changed.
- **D-316 (owner, Q&A):** pickup at spindle X 402, Y 0, nose Z 70 (lift to 120); wheel centre Z -82, so the wheel reaches Z -278, 110 below the base: it hangs past the bench edge (X 330 or less) or the machine goes on risers. Drive turned round to the outboard side (copied as v3 it landed in the end plate and table edge). Longest tool 100 below the nose.
- **Modelled:** component `ATC Wheel (Phase 2)`, 59 bodies copied from v3 (forks trimmed to a foot on the disc, holders, tools, hub 31 longer, FK12, stub, coupling, motor, column without ear and floor) plus the D-304 disc (6 mm 5083, no windows drawn) and a 6082 mount bracket envelope on the right upright's outer face. Checks clean: frame, carriage engaged, lifted (wheel turned 0 to 30°), withdrawn with a Ø20 x 100 tool; 184 timeline items healthy. Details: `docs/v4-model.md` (Task 6). Hand check: `tools/v4_wheel_fit.py`.
- **Machine envelope:** about 1,102 x 805 x 978 (X -508 to 594, Y -335 to 470, Z -278 to 700).
- A heavy read-only clash script locked Fusion for about 10 minutes; keep Fusion checks to bounding-box-filtered, few-pose scripts.

**Left:** owner saves `Type_0_v4` again (the wheel is unsaved); index flag and sensor not placed; bracket bolts; BOM A-lines for the disc, longer hub and bracket; Task 7 (fill quantities per D-315, wave 1 lengths: X travel 620, one Y set, plate and pads); the 14 unpriced BOM lines.

**Exact next step:** the owner saves `Type_0_v4`. A new session models the 4 D-317 fault fixes (`docs/v4-model.md`, last section), then runs plan Task 7 from `docs/superpowers/plans/2026-11-24-v4-fixed-gantry.md` with D-315.

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

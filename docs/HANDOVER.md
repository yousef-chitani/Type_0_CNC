# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (6th session): X 1610 plates checked, 2 X block screws ISO 7380; not saved
- Design-issues item 17 checked in `Type_0_v3`: the X DFU1605 flange sits on the X 1610 nut plate face (X -140), its 6 holes (PCD 38) line up, the Ø28.2 bore clears the Ø28 nut body, the fill plate's Ø18 hole clears the Ø16 screw. Same as Y and Y2. **D-277: both plates stay** (owner).
- The check found 2 X top block screws by the nut plate (Body7, Body8 of `M5x8 X top block screws`, X -162, Y 489 and 521) hit the 2 lower tie-rod nuts by 0.9, as on Y before D-264. **D-278: ISO 7380 M5 x 8** (owner); modelled, head Z 358 to 360.75, 1.35 under the nut (Z 362.1). Clash check of the X nut area: none left (only threads in holes and vendor-internal overlaps). Health 35 before and after.
- BOM X18: 18 x M5 x 8 plus 6 x ISO 7380 M5 x 8.
- **Model not saved.** The owner saves `Type_0_v3`.

**Left (model):** D-275 hub, the X BKHM12 riser BK12 holes (item 19), X trigger mount M6 x 20 short (item 18). **Docs:** BOM G06 text (8 mm pour, jack screws), X19 hold-down length M6 x 25, new jack screw line (unpriced), pour quantity; `cast_in_features`, `spec-gaps.md`.

**Exact next step:** the owner saves `Type_0_v3`; then a session checks the X BKHM12 riser BK12 holes (design-issues item 19).

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (5th session): D-264 and D-266 modelled, saved
- The owner had saved `Type_0_v3` with the D-271 follow-up (document open, not modified, at the start).
- D-264: the 4 Y and Y2 block screws by the nut plate (Body1, Body3 of `M5x8 Y block screws` and `M5x8 Y2 block screws`; X ±334, ±366, Y 409.5) are now ISO 7380 M5 x 8 button heads (Ø9.5, head Z 158 to 160.75, domed). They clear the tie-rod nut (Z 162.1) by 1.35; clash check of all 16 Y block screws: none.
- D-266: the 2 leftover M5 holes in the X roller tube front wall (X -254.5, -190.5, Z 372, Y 445 to 448) are plugged: base feature and combine `Fill 2 leftover M5 holes (D-266)` in `XRollers` (119 mm3, faces 58 to 56). The top angle screws at Z 374.5 have their own tapped holes in the angle and end at Y 443.5, short of the tube.
- **The other two D-266 "holes" are not holes, so they were left:** the Ø16 in the gantry tube is the R8 inside corner of the 120 x 120 x 8 tube (all 4 corners, full length); the Ø10 in the Y220 chain support is the arched zip-tie channel under its base (now Z 33), linking its 4 zip-tie slots. Recorded in D-266.
- BOM X18: 20 x M5 x 8 plus 4 x ISO 7380 M5 x 8. Timeline health 35 before and after.

**Left (model):** X 1610 plates fit check, D-275 hub, the X BKHM12 riser BK12 holes. **Docs:** BOM G06 text (8 mm pour, jack screws), X19 hold-down length M6 x 25, new jack screw line (unpriced), pour quantity; `cast_in_features`, `spec-gaps.md`.

**Exact next step:** a session checks the X 1610 fill plate and nut plate fit with the DFU1605 nuts (design-issues item 17) and asks the owner.

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

# Type 0 CNC: code map

Read this first. Sections marked `AUTO` are rewritten by `python tools/codemap.py`; edit the
rest by hand. Line numbers in `AUTO:where` are exact; docs are indexed by heading or D-number
because they grow every session.

## Overview
- A DIY CNC mill in planning. **The live CAD is the Fusion 360 document `Type_0_v5`** (PrintNC V4
  Metalcutter, re-sized; D-338 on). It is **not in git** and is often unsaved: only the owner saves it.
- The repo holds the decisions, BOM, design notes, price checks, calc scripts (Python 3.13) and the
  LinuxCNC config. `cad/v2`, `cad/type0_*.py`, `cad/v4` are history (fixed gantry, V4).
- No build. Scripts: `python tools/<script>.py` (PowerShell: set `$env:PYTHONUTF8=1` first; stdlib; some need numpy/scipy/
  matplotlib/openpyxl; `cad/` needs `pip install cadquery`). Checks: `python tools/v5_sizes.py`
  (prints PASS), `python tools/v5_parts_check.py`, `python tools/codemap.py --check`.
- Fusion scripts (`tools/fusion/*.py`) run inside Fusion through the MCP `fusion_mcp_execute`
  (paste the file; `readOnly` for checks). Never with `python`. Never save Fusion documents.
- LinuxCNC: `linuxcnc linuxcnc/type0/type0_sim.ini`, then `python linuxcnc/type0/sim/test_sim.py`
  (needs a LinuxCNC 2.9 PC or Debian 12 Docker; `docs/linuxcnc.md` §4).

## Directory tree
<!-- AUTO:tree -->
```
.claude/  (4 files)  # settings.json (BOM hook), this map, TASKS.md, NEXT_PROMPT.md
cad/  (183 files)  # type0_layout.py / type0_drawings.py: v1 CadQuery layout (history)
  out/  (14 files)  # v1 outputs (history)
  v2/  (104 files)  # CadQuery fixed-gantry design (history, D-137); bench, enclosure, printed parts still used
    out/  (87 files)  # generated STEP/PNG/SVG/JSON from cad/v2 scripts
  v4/  (31 files)
    jlc-step/  (31 files)  # V4 per-part STEP for JLC quotes (task 29, on hold), README inside
  vendor/  (32 files)  # manufacturer STEP/PDF (real parts: use these, never stand-ins), README inside
    drawings/  (10 files)  # supplier drawings (LiMo ends, HM12-60, MH coupling, spindle clamp)
docs/  (133 files)  # the project: decisions, BOM, design notes, price checks (see Docs map)
  img/  (2 files)
  sketches/  (3 files)  # SVG sketches from tools/task28_sketches.py
  superpowers/  (11 files)  # specs/ and plans/ (design docs and step plans, dated)
  tasks/  (26 files)  # one file per task + README.md (task table, rules, state)
linuxcnc/  (14 files)
  type0/  (14 files)  # LinuxCNC 2.9 config: type0.ini + HAL, Mesa 7I76EU
    sim/  (5 files)  # simulator ini builder + checks
tools/  (29 files)  # calc scripts, BOM generators, hook
  fusion/  (6 files)  # scripts run inside Fusion via fusion_mcp_execute (not python)
```
<!-- /AUTO:tree -->

## Entry points
- **Sessions:** `.claude/NEXT_PROMPT.md` → `.claude/TASKS.md` → `docs/tasks/README.md` (task table,
  rules, last D-number) → the task file. `docs/HANDOVER.md` = last two sessions; older in
  `docs/handover-archive.md`.
- **Owner's list:** `docs/owner-todo.txt`. Open design issues: `docs/design-issues.md`,
  `docs/open-questions.md`, `docs/spec-gaps.md`.
- **BOM edit:** `docs/bom.csv` → hook `tools/bom_hook.py` (PostToolUse on Write|Edit, in
  `.claude/settings.json`) → the 5 generators.
- **V5 work:** spec `docs/superpowers/specs/2026-11-26-v5-printnc-design.md`, plan
  `docs/superpowers/plans/2026-11-26-v5-printnc.md` (Tasks 1–8), model log `docs/v5-model.md`.
- **Fusion:** `tools/fusion/v5_y1_place.py` then `tools/fusion/v5_y2_place.py` then `tools/fusion/v5_roller_screws.py` then `tools/fusion/v5_y_seats.py` then `tools/fusion/v5_x_place.py` (beam, X axis) (write; separate calls), `tools/fusion/v5_check_task4.py` (read-only). Fusion can `exec` the repo file (see `docs/v5-model.md`, Y axis finish).

## Data flow (who reads what)
```
docs/bom.csv ─(tools/bom_hook.py, on edit)─┬→ tools/gen_bom_md.py      → docs/bom.md
                                           ├→ tools/gen_phase1_xlsx.py → docs/phase1-bom.xlsx
                                           ├→ tools/gen_phase1_cost.py → docs/phase1-cost.md
                                           ├→ tools/build_open_links.py + open_links_template.py → tools/open_links.py
                                           └→ tools/gen_wave1_sheet.py (+ docs/phase1-schedule.md) → docs/wave1-order-sheet.md
tools/v5_sizes.py:sizes() → tools/v5_beam.py ; numbers copied by hand into docs/v5-sizes.md, Fusion params
tools/v4_sizes.py:sizes() → tools/v4_frame_stiffness.py → tools/v4_joint_sweep.py
docs/v5-parts.md → tools/v5_parts_check.py (every "How made" cell valid)
cad/v2/type0_v2.py → cad/v2/assembly.py → out/assembly/assembly_data.json → cad/v2/enclosure.py, base_cores_sketch.py
                     assembly.py imported by render_views.py, render_steps.py, base_cores_sketch.py (all history)
cad/vendor/*.step → cad/v2/assembly.py, tools/build_fusion_parts.py; imported by hand into Fusion
linuxcnc/type0/type0.ini → sim/make_sim_ini.py → type0_sim.ini (sim_*.hal) → sim/test_sim.py
```

## Script index
<!-- AUTO:scripts -->
- `cad/type0_drawings.py` (133) Dimensioned 2D views generated from the same parameters as type0_layout.py.  
  class Svg, side(t, rack_off, znose, name, title), front()
- `cad/type0_layout.py` (233) Type 0 CNC: parametric layout (CadQuery).  
  derive(p), box(x0, x1, y0, y1, z0, z1), build(t, x, znose, rack_pos), export(), report()
- `cad/v2/assembly.py` (553) Type 0 v2 full assembly (task 4, D-102 ... D-107).  
  box(x0, x1, y0, y1, z0, z1), cyl(axis, d, l, c), check_stack(), rail(length, axis_dir, origin, up), block(), place(shape, axis_dir, origin, up), ballscrew(length, stub...
- `cad/v2/base_cores_sketch.py` (164) Sketch: PVC cores for the base casting (proposal, not yet in assembly.py).  
  mass_saved(), rect(x0, y0, x1, y1, fill, op, sw_, dash), circ(x, y, r, fill, op), poly(pts, fill, op), text(x, y, s, anchor, c, sz, w), page(name, title, body, w, hgt)...
- `cad/v2/beam_options.py` (145) Task 22 beam assessment (D-143, D-145): stiffness and mass of the beam options,  
  rect_I(b, h), tube(z, y, t), defl(ei), twist(gj), row(name, eiy, eiz, mass, gj, note), bow(e_bar, strain, length)
- `cad/v2/bench.py` (452) Type 0 v2 timber bench (task 3, D-97): bolted CLS frame, 2 x 18 mm ply top, cabinet front-left,  
  boxes(), equipment(), cut_items(), nest_timber(items), sheet_parts(), nest_sheets(parts), load_check(), svg(name, title, body, w, h), rect(x0, y0, x1, y1, fill, op, sw...
- `cad/v2/enclosure.py` (148) Type 0 v2 enclosure (D-87): 12 mm MDF box on the bench around the machine, top-hinged front door with window.  
  extents(), model(), svg_views(win), cutlist()
- `cad/v2/gantry_parts.py` (86) Task 22 step 4: basic STEP models of the JLC gantry parts, for a price quote only.  
  box(x0, x1, y0, y1, z0, z1), holes_y(wp_solid, pts, dia, depth, y_face, direction), holes_z(wp_solid, pts, dia, z0, z1)
- `cad/v2/gantry_parts_sketch.py` (172) Task 22 step 4, before the STEP: gantry parts G01-G03 as a PROPOSAL for the owner (docs/task22-step4.md).  
  rect(ax, x0, y0, x1, y1, fc, ec, lw), dim(ax, p0, p1, t, off, fs), note(ax, x, y, t, fs), beam_section(ax, x_end)
- `cad/v2/gantry_sketch.py` (285) Task 22 step 1: moving-gantry sketch (D-137, D-138). Numbers + one PNG, no STEP.  
  r50(x), y_case(front_extra), tub_kg(L, floor_t, wall_top, back, core_d), rect(ax, x0, y0, x1, y1, fc, ec, lw), dim(ax, p0, p1, text, off, fs)
- `cad/v2/open_items_sketch.py` (186) Sketch of the two open items (19 Nov 2026), numbers measured in Fusion `Type_0_v3`.  
  rect(ax, x0, x1, y0, y1, fc, ec, lw), tube(ax, x0, x1, y0, y1, t), hexnut_side(ax, x0, x1, z0, z1), screw(ax, yc, z_seat, head_h, fc, label)
- `cad/v2/printed_parts.py` (123) Type 0 printed parts (D-100), for the owner's Bambu Lab P1S printers (256 x 256 x 256 build).  
  fan_grill(size, pitch, t, hole_d, open_d, ring_w, ring_pitch, spokes), grommet_frame(), grommet_membrane(), grommet_ring(), estop_body(), estop_lid(), bbox(shape)
- `cad/v2/rail_seat_sketch.py` (63) Sketch: rail-seat recess options (review finding 3). Sections at true proportions.  
  rect(ax, x0, x1, y0, y1), panel(ax, title, body, bar, rec, depth, bad, dams, rail_c, note, air)
- `cad/v2/render_steps.py` (128) Step-by-step assembly pictures from the CadQuery model (for docs/assembly-steps.md).  
  pads(), owner(name), draw(ax, parts, lo, hi, elev, azim, zoom)
- `cad/v2/render_views.py` (62) Render the assembly views (PNG) with matplotlib from the CadQuery model.  
  mesh(shape, tol), shaded(tris, col), draw(ax, parts, elev, azim, title)
- `cad/v2/sketch_3piece.py` (119) Type 0 v2 (scaled down, D-71): 3-piece epoxy-granite frame concept sketch.  
  derive(p), svg(name, w, h, title, body), R(x0, y0, x1, y1, fill, op, dash), T(x, y, s, a, sz, c, b), top(), front()
- `cad/v2/steel_gantry_sketch.py` (343) Steel SHS gantry layout (D-164): boxes, clash check, one PNG. No STEP. All of it is a PROPOSAL.  
  add(name, group, x, y, z, mat), mid(c, w), allowed(a, b), place(b, sy, xs, zn), gap(p, q), status(r), keep(prefix), draw(ax, u, v, sy, xs, zn, pick, order, alpha), lab...
- `cad/v2/type0_v2.py` (131) Type 0 v2 (flat-sized, D-71/D-73): parametric layout.  
  derive(p), box(x0, x1, y0, y1, z0, z1), build(t, x, znose), report()
- `cad/v2/vallder_profiles.py` (191) Vallder X-axis extrusions vs the JLC step-4 beam (task 22, docs/beam-extrusion-check.md).  
  props(pts), section(loops), dxf_loops(p), rect(x0, y0, x1, y1), defl(ei), twist(gj), bredt(am, s_over_t), channel_width(lp, depth, yc)
- `linuxcnc/type0/sim/make_sim_ini.py` (34) Write ../type0_sim.ini from ../type0.ini, swapping the hardware HAL files for the
- `linuxcnc/type0/sim/test_sim.py` (137) Checks the Type 0 config in the simulator. Start LinuxCNC first:  
  hal(cmd), sig(name), check(label, ok), wait(cond, timeout), machine_on(), mdi(cmd, timeout)
- `tools/atc_carrier_stiffness.py` (63) ATC front carrier: hand estimate of fork displacement at the pickup (D-303, D-304).  
  cant(EI, L), fk12_tilt(k_theta), report(name, parts)
- `tools/bom_hook.py` (51) Claude Code hook: re-run the BOM generators after docs/bom.csv is edited.  
  main()
- `tools/build_fusion_parts.py` (46) Build exact parts for Type_0_v3 from the vendor STEP files.  
  rail(length, pitch), main()
- `tools/build_open_links.py` (23) Rebuild tools/open_links.py with the current parts list embedded. Run: python tools/build_open_links.py  
  vendor(u)
- `tools/codemap.py` (145) Regenerate the mechanical sections of .claude/CODEMAP.md (tree, script index, where-index).  
  files(), tree(fs), sig(fn), symbols(fs), where(), main()
- `tools/cure_heat.py` (40) Curing heat estimate for the epoxy-granite castings with Ampreg 30 + 3X Slow (D-122).
- `tools/fusion/v5_check_task4.py` (115) Read-only check of Type_0_v5 for V5 plan Task 4 (run through fusion_mcp_execute, readOnly). 1. timeline warnin  
  bodies(root), run(_context)
- `tools/fusion/v5_roller_screws.py` (75) Cut the gantry-to-roller M6x12 screws that the Y plate rods hit to M6 x 9 (D-373). Run through fusion_mcp_exec  
  run(_context)
- `tools/fusion/v5_x_place.py` (181) V5 beam and X axis (plan Task 5, bundle C part 1). Run through fusion_mcp_execute (not read-only) after v5_y1_  
  mat(dx, ybase, zc), box(x0, x1, y0, y1, z0, z1), xcyl(x0, x1, y, z, r), rrect(x0, x1, y0, y1, z0, z1, r), copy(body, m), run(_context)
- `tools/fusion/v5_y1_place.py` (313) Place the Y1 vendor parts in Type_0_v5 (V5 plan Task 4, item 2). Run through fusion_mcp_execute (not read-only  
  mat(cols, t_mm), run(_context)
- `tools/fusion/v5_y2_place.py` (143) Place the Y2 parts in Type_0_v5 (V5 plan Task 4, item 2). Run through fusion_mcp_execute (not read-only) AFTER  
  move(dx_mm), turn_about_y(x_mm, z_mm), placed(t1, extra), run(_context)
- `tools/fusion/v5_y_seats.py` (66) Y rail seats (V5 plan Task 7, bundle E2): the cured epoxy seat under each Y HGR20, as bodies. Run through fusi  
  run(_context)
- `tools/gen_bom_md.py` (62) Regenerate docs/bom.md from docs/bom.csv. Run from the repo root: python tools/gen_bom_md.py  
  esc(s)
- `tools/gen_phase1_cost.py` (29) Regenerate docs/phase1-cost.md from docs/bom.csv (Phase 1 lines only).
- `tools/gen_phase1_xlsx.py` (60) Regenerate docs/phase1-bom.xlsx from docs/bom.csv. Run from the repo root: python tools/gen_phase1_xlsx.py (th  
  label(u), put(r, c, v, bold, fmt, col)
- `tools/gen_wave1_sheet.py` (109) Write docs/wave1-order-sheet.md from docs/bom.csv (task 15).  
  wave1_ids(), vendor(link), cell(s), main()
- `tools/open_links.py` (87) Shop the Type 0 CNC parts list one vendor at a time (standalone: the links are built in).  
  firefox_cmd(), open_tabs(ff, urls, batch), main()
- `tools/open_links_template.py` (87) Shop the Type 0 CNC parts list one vendor at a time (standalone: the links are built in).  
  firefox_cmd(), open_tabs(ff, urls, batch), main()
- `tools/portal_overhang.py` (48) Portal beam overhang check (open question 11). Hand calculation, no FEA.
- `tools/task28_sketches.py` (147) Task 28 sketches: Z and X motor belt folds, and the footprint comparison.  
  svg(w, h, body, vb), rect(x0, y0, x1, y1, fill, stroke, dash, label, ls, op), text(x, y, t, size, anchor, color), line(x0, y0, x1, y1, color, w, dash), z_fold(), x_fol...
- `tools/v4_frame_stiffness.py` (549) V4 frame options (Task 2): mass and hand stiffness of the base tray and upright choices.  
  hollow_rect(b, d, t, ro, ri, step), rect(b, d), steel(sec), kjn_pieces(layout), part(E, G, b, d, y, z, I_own, J, A, As, eg), composite(parts, bonded, block), tray(layo...
- `tools/v4_joint_sweep.py` (40) V4 upright joints as rotation springs (task 28, D-321): how much the nose loses when the  
  spring(k), build(*a), run(label)
- `tools/v4_sizes.py` (129) V4 sizing script (fixed gantry, moving table). All lengths in mm.  
  up(x, steps), up_step(x, step), rail_len(travel), screw_len(travel), critical_rpm(length, dia, k, safety), sizes()
- `tools/v4_wheel_fit.py` (55) V4 ATC wheel fit (Task 6, D-314): how high the wheel may sit under the X carriage.  
  max_centre(y_near, z_bottom), main()
- `tools/v5_beam.py` (166) V5 beam pick (plan Task 2): tall steel tube standing up, both X rails on its front face (D-349).  
  r_out_max(t), r_out_calc(t), section(h, b, t, step), nose_deflection(h, b, t, nose), rail_fit(h, t)
- `tools/v5_matrix.py` (84) V5 weighted idea matrix (docs/v5-idea-matrix.md). Scores 1-5, weighted total out of 100.  
  out(s), total(s)
- `tools/v5_parts_check.py` (42) Check docs/v5-parts.md (plan Task 3): every 'How made' cell is one of the  
  main()
- `tools/v5_sizes.py` (160) V5 sizing script (PrintNC moving gantry, 16-tool rack behind the bed). All lengths in mm.  
  up(x, steps), up_step(x, step), critical_rpm(length, dia, k, safety), rack_row_span(), rack_y_depth(), screw_for_rail(rail), sizes()
- `tools/z_plate_stiffness.py` (208) Z fixed plate stiffness (D-184): how far the tool moves because the plate bends.  
  grid(lo, hi, keys, step), element(a, b, E, nu, t), class Plate, check(), main()
<!-- /AUTO:scripts -->

## Where do I find…
<!-- AUTO:where -->
- V5 sizes (travel, rails, screws, rack) → `tools/v5_sizes.py:98`
- V5 beam section pick → `tools/v5_beam.py:77`
- V5 idea matrix weights → `tools/v5_matrix.py:60`
- V5 parts-list check (How made) → `tools/v5_parts_check.py:13`
- Y1 datums (axis X/Z, SEAT, BF12 centre) → `tools/fusion/v5_y1_place.py:13`
- Y1 1605 screw profile → `tools/fusion/v5_y1_place.py:27`
- Y1 placement entry → `tools/fusion/v5_y1_place.py:45`
- Task 4 check: skipped body names → `tools/fusion/v5_check_task4.py:7`
- Task 4 check entry → `tools/fusion/v5_check_task4.py:25`
- BOM hook: generator list → `tools/bom_hook.py:14`
- V4 sizes → `tools/v4_sizes.py:66`
- V4 frame stiffness model → `tools/v4_frame_stiffness.py:248`
- Z plate FE model → `tools/z_plate_stiffness.py:62`
- Old assembly build / clash check → `cad/v2/assembly.py:380`
- Printed parts (PETG) → `cad/v2/printed_parts.py:14`
- LinuxCNC joints (X, Y, Z) → `linuxcnc/type0/type0.ini:114`
- LinuxCNC HAL file list → `linuxcnc/type0/type0.ini:61`
- LinuxCNC Mesa board config → `linuxcnc/type0/type0.ini:51`
- Sim checks → `linuxcnc/type0/sim/test_sim.py:23`
<!-- /AUTO:where -->
- A decision → `docs/decisions.md`, search `D-NNN` (one line each; last used: see tasks README)
- Task state, budget line, branch → `docs/tasks/README.md` (rules at top, table under `## Tasks`)
- Current V5 model state, what is hidden, what is left → `docs/v5-model.md` `## Left for Task 4`
- V5 part list (PrintNC name → V5 part, how made) → `docs/v5-parts.md`
- V5 numbers → `docs/v5-sizes.md`; beam/price → `docs/price-check-v5.md`
- A price or vendor → `docs/bom.csv` columns `price_gbp,date_checked,link` (CRLF, `""` quotes)
- Phase 1 total → `docs/phase1-cost.md` (generated)
- Wiring, pins, VFD → `docs/electrical.md`; LinuxCNC set-up → `docs/linuxcnc.md`
- Vendor CAD and drawings → `cad/vendor/README.md`, `cad/vendor/drawings/README.md`
- Supplier message drafts → `docs/supplier-messages.md`
- Printed parts and settings → `docs/printed-parts.md`
- Epoxy granite (V3/V4 history) → `docs/eg-*.md`, `docs/curing-heat.md`, `docs/v4-pour.md`

## Docs map (`docs/`; read only what a task names)
- **Live:** `decisions.md`, `bom.csv` (+ generated `bom.md`, `phase1-*`, `wave1-order-sheet.md`),
  `requirements.md`, `owner-todo.txt`, `open-questions.md`, `design-issues.md`, `spec-gaps.md`,
  `v5-*.md` (idea-matrix, sizes, parts, model), `price-check-v5.md`, `printnc-assessment.md`,
  `feedback-discord-2026-11-2*.md`, `supplier-messages.md`, `electrical.md`, `linuxcnc.md`,
  `printed-parts.md`, `phase1-schedule.md`.
- **V4 (frozen, D-324; RFQ on hold):** `v4-*.md`, `price-check-v4.md`, `task28-folds-and-footprint.md`.
- **Price checks for the owner's browser:** `price-check-task*.md` (one per run), `cad-download-task.md`.
- **History (fixed gantry, V3 tub, ATC wheel):** `v2-design.md`, `assembly*.md`, `layout.md`,
  `eg-*.md`, `aggregates.md`, `epoxy-options.md`, `atc-wheel.md`, `rear-atc-reach.md`,
  `machine-assessment.md`, `beam-*.md`, `steel-*.md`, `moving-gantry-sketch.md`, `task22-*.md`,
  `z-*.md`, `portal-relocation.md`, `simplification-options.md`, `scale-down-options.md`,
  `review-*.md`, `video-notes-eg-base.md`, `cad-cleanup-owner-items.md`, `open-items-sketch.md`.

## Conventions & gotchas
- Units mm. V5 model coordinates are PrintNC's (Y1 screw axis X -377.5, Z 210 roller centre);
  `docs/v5-model.md` `## Origin` says where the world origin goes.
- Every decision gets the next D-number in `docs/decisions.md` and the tasks README rule line.
- Prices only from a live page (curl, never the browser) or the owner, with the date. No eBay.
- `docs/bom.csv`: CRLF, CSV-escaped quotes; edit it, never the generated files.
- Real parts only: vendor STEP from `cad/vendor/`; if missing, stop and ask the owner.
- Fusion: occurrence transforms on some imports do not hold (DFU1605): a Move feature places it.
  Hide replaced PrintNC parts, do not delete them. Re-running `v5_y1_place.py` resets transforms and rebuilds the parts built at the axis height when `SEAT` changes.
- `SEAT = 3` in `v5_y1_place.py` must match user parameter `YRailSeat` (joints Rigid 2/202 lift PrintNC's rails). A new occurrence's `transform2` set in its creating call does not hold: pass the matrix at creation. DFU1605 occurrence transforms never hold (Move feature on Y1, copied bodies on Y2).
- Windows: set `PYTHONUTF8=1` (bash) or `$env:PYTHONUTF8=1` (PowerShell); use `encoding="utf-8"` in new scripts.
- The two untracked `*.step` files in the root and `cad/v2/` are the owner's: do not commit them.
- Do not merge branch `claude/awesome-ramanujan-by9kds` (old design).

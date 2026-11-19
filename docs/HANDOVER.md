# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000. 19 Nov 2026: spindle lowered 5 (D-214); real HGR20 rails and X HGH20CA blocks (D-215)

**Done in `Type_0_v3` and saved. Timeline 1434.**
- **Spindle 5 lower** (`Position96`): the clamp now covers 43 to 103 from the front face (allowed 42 to 162). Nose Z 170 at the shown position, so nose travel is Z 95 to 245.
- **Real HGR20 section on Y, Y2 and both X rails** (`HGR20 real section` base features in `Y HGR20`, `Y2 HGR20` and `X HGR20`). Copied from the Z rail section: 17.5 high, Ø6 through with Ø9.5 counterbore, 60 pitch. Same lengths and hole positions as before (Y 550, holes 34.5 / 35.5 from the ends; X 600, E 30). The 18-high stand-in bodies are hidden, not deleted.
- **X blocks: 4 x `hgh20ca_1` (:6 to :9)** at X -265 and -180, Y 505, faces Z 355 (top, on `XRollers`) and Z 175 (bottom, on `XRoller Bottom:1`), each held by an as-built rigid joint. `X HGW20CC` and `X HGW20CC(Mirror)` are hidden.
- **Screws:** `M5x8 X top block screws` (heads inside the tube on the 3 mm bottom wall) and `M5x10 X bottom block screws` (heads under the 6 mm angle flange), 8 each on 32 x 36, jointed to their parts.
- **Holes:** 8 x Ø5.5 cut through the tube bottom wall and through the angle flange (`HGH20CA block holes 5.5 (X top / X bottom)`).
- Ball screws unchanged: they already match M05 (X 700, Y 650 x 2, Z 350, DFU1605 vendor nuts, vendor BK12/BF12).

**Checked:** no clash between the 28 new or changed bodies and the 96 bodies around them. This closes the 700 mm3 block-to-rail overlap and the X nut clash expected in D-212. All new timeline items are healthy.

**Found / left:**
1. **`XRoller Bottom` is one component used twice**, so the 8 new Ø5.5 holes are also in the top angle's flange (`XRoller Bottom:2`), where nothing uses them. Make the top angle its own component if the owner wants them gone.
2. **Old HGW20CC holes are not filled** in the tube bottom wall or the angle flange (on Y they were, D-212). The HGW and HGH holes do not overlap.
3. **No key-access holes for the X top screws.** The top angle (D-209) covers the tube's top wall, so the M5 x 8 heads inside the tube may need a different way in. Owner to choose.
4. The Y block screw / M5 nut clash from D-212 is still open (owner to choose the screw).
5. Rail fixing bolts (M5 x 20, X03) are not modelled.

**Exact next step:** owner answers items 1 to 3 and the D-212 screw choice. Then couplings, sensors, clean-up and STEP files.

## 000000000000000000000000000000000000000000000000000000000. 19 Nov 2026: Jianken JGL-80 vendor STEP replaces the spindle stand-in (D-213)

**Done in `Type_0_v3` and saved. Timeline 1412.**
- Jianken's STEP (`cad/vendor/jianken_jgl80_2.2r24.step`) imported into `Z Moving Parts` as `Jianken JGL-80-2.2R24 spindle (vendor STEP)`, held by a position snapshot, so it rides the Z slider.
- Same axis as the stand-in (X -222.5, Y 292) and the same nose tip (Z 175 at the shown Z position). Body front face Z 207, rear face Z 526, fittings to Z 545.
- The stand-in body is removed with `RemoveBody-Jianken JGL-80 stand-in, length not confirmed` (end of timeline). Sub-component names decoded from GBK to Chinese.
- Outline drawing saved as `cad/vendor/drawings/jianken_jgl80_2.2r24_drawing.pdf`; both READMEs updated.

**Checked:** no clash between the 19 spindle bodies and the 63 other Z assembly, Z fixed plate and EG tub bodies. Timeline health unchanged (the old Chamfer2 error only).

**Found:**
1. **Clamp sits 4 below the clamping range.** The drawing allows clamping 42 to 162 from the front face. The clamp stand-in covers 38 to 98. Move the clamp up at least 4 (or the spindle down) when the real clamp is modelled.
2. **Nose length.** The STEP nose is 32 past the front face, the drawing says 45. The extra 13 is likely the ER16 nut. The nose tip in the model is the STEP's, not the drawing's.
3. **Rear clearance is fine.** The body reaches about 88 higher than the stand-in, but the whole spindle is at Y 336 or less and every Z fixed part (rails, screw, mount, motor) is at Y 384 or more, so no Z position can clash.

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

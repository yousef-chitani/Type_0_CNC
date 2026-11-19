# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000. 19 Nov 2026: top angle split off (D-216); X and Y nut flats (D-217)

**Done in `Type_0_v3` and saved. Timeline 1439.**
- **`XRoller Top Angle`**: new root component, a copy of `XRoller Bottom:2` with the 8 unused Ø5.5 HGH holes (D-215) filled, joined rigidly (as built) to `XRollers`. `XRoller Bottom:2` is hidden, not deleted. `XRoller Bottom` is now used only by the bottom angle.
- **Flange flats on the X, Y and Y2 DFU1605 nuts** (one shared component, `DFU1605 Nut`): flange cut to **40 across flats** (`Flange flats 40 AF (DIN 69051 form B)`), as on the supplier's table and the Z nut (D-205). The flats are horizontal on all three nuts: flanges now Z 160 to 200 (Y, Y2) and Z 360 to 400 (X). This is the only orientation that misses the 6 flange holes (holes at 0° and 45°).

**Checked:** no clash between the 16 changed bodies and the 99 bodies around them. All new timeline items are healthy.

**Left (still open from D-215):**
1. Old HGW20CC holes not filled in the X tube bottom wall and bottom angle flange.
2. No key access for the M5 x 8 X top block screws: the top angle covers the tube's top wall. Owner to choose.
3. The D-212 Y block screw / M5 nut clash: owner to choose the screw.
4. Rail fixing bolts (M5 x 20, X03) not modelled. LiMo has still not confirmed that its nuts have the flats.

**Exact next step:** owner answers items 2 and 3. Then couplings, sensors, clean-up and STEP files.

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

# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000. 18 Nov 2026: EG tub walls thinned and floor edges filleted (D-197)

**Done:** in `Type_0_v3` the tub walls go from 140 to 80 wide, so the tub is now 780 x 690 x 140 high (outer faces X ±390). Both floor-to-wall edges have an R20 fillet. No draft is needed, because the mould is destroyed at demoulding. The 4 front riser screws moved from X ±305 to X ±365, into the riser holes. The casting is 40.18 L, 92.4 kg at 2,300 kg/m³, down from 51.24 L and 117.8 kg. Measured: casting and levelling layer volumes match the hand figures, only the 3 tub bodies changed and the 4 screws moved out of 939 bodies, and the timeline is 1269 with the same 1 error and 5 warnings. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Riser bolt lengths.** The M6 x 30 bolts do not suit the seat. At Y -23 and Y 629 (6 bolts) they end at Z 119, 1 of thread. At Y -6 and Y 561 (8 bolts) they end at Z 107, 3 past the bar into solid EG. M6 x 35 and M6 x 25 would give 6 and 8 of thread. Needs the owner's decision and a live price.
2. **Parts that clash with the walls need new positions:** both Y frame trigger mounts, the Y cable chain support, the Y cable chain fixed end support, and their M6 x 12 screws. The zip tie plate and its M5 screws no longer clash.
3. **Not modelled:** table fixing holes, machine feet and pads, mould details.
4. **Z plate stiffness** (D-184).
5. **Top roller screw strength.** They thread into only 3 of tube wall: check this.
6. **Amazon delivery.** X11 and X12 are free to deliver only on orders over £35. The two packs come to £12.98, and the charge below £35 is not known.
7. **Z risers and rails.** 15 risers and HGR20 rails on the plate, then the blocks, moving plate, screw and motor.

**Exact next step:** the owner saves `Type_0_v3`. Then, in a new session, settle the riser bolt lengths with the owner and get a live price.

## 0000000000000000000000000000000000000000000. 18 Nov 2026: EG tub modelled (D-196)

**Done:** the new component `EG Tub` is in `Type_0_v3`: casting, 2 steel bars 40 x 10 x 684 and 2 levelling layers, with 9 M5 and 7 M6 tap holes per wall through the bar and layer. The tub is 900 x 690 x 140 high, with the floor top at Z 45 and the walls at Z 125. The cast EG is 51.24 L, about 117.8 kg at 2,300 kg/m³. The recess inner edge moved from X 325 to X 315, because the risers span X 320 to 380 (D-196). Table top Z 70 is confirmed: floor Z 45 plus the 25 table plate (M11). Measured: all body volumes match the hand figures, all 939 existing bodies are unchanged, and the timeline is 1266 with the same 1 error and 5 warnings. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Riser bolt lengths.** The M6 x 30 bolts do not suit the seat. At Y -23 and Y 629 (6 bolts) they end at Z 119, 1 of thread. At Y -6 and Y 561 (8 bolts) they end at Z 107, 3 past the bar into solid EG. M6 x 35 and M6 x 25 would give 6 and 8 of thread. Needs the owner's decision and a live price.
2. **Front riser screws in the model.** The 4 screws at X -305 and 305 (Y -6, Y 561) still need moving to X -365 and 365.
3. **Parts that clash with the walls need new positions:** both Y frame trigger mounts, the Y cable chain support, the Y cable chain fixed end support, its zip tie plate, and their screws.
4. **Not modelled:** table fixing holes, machine feet and pads, draft and corner fillets, mould details.
5. **Z plate stiffness** (D-184).
6. **Top roller screw strength.** They thread into only 3 of tube wall: check this.
7. **Amazon delivery.** X11 and X12 are free to deliver only on orders over £35. The two packs come to £12.98, and the charge below £35 is not known.
8. **Z risers and rails.** 15 risers and HGR20 rails on the plate, then the blocks, moving plate, screw and motor.

**Exact next step:** the owner saves `Type_0_v3`. Then, in a new session, settle the riser bolt lengths with the owner and get a live price.

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

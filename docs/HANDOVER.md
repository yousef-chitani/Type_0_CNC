# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000. 18 Nov 2026: HM12-60 mount modelled, Z plate 442 long (D-211)

**Done in `Type_0_v3`, not saved. The owner saves it.**
- The owner's HM12-60 CAD is fitted as `HM12-60-V Z Mount`: bearing end on the screw shoulder at Z 534, motor face at Z 624.
- `Z Fixed Plate` is 442 long, Z 169 to 611, 1 under the mount flange. It has 6 x M6 tapped holes at X -245.5 and -199.5, Z 541, 554 and 584.
- The Z BK12, the D-206 bracket, its 2 tapped holes and the motor mount stand-in are removed.
- The motor moved up 12, so its top is at Z 770. The coupling is at Z 580.75 to 615.75.
- The screw's 10 mm end is 21.5 long, up from 15, ending at Z 592.5. The D25L35 grips 11.75 of each shaft, and the shaft ends stop at the spider.
- `docs/bom.csv`: M05 and M12 updated. No price changes.

**Checked:** no moving-to-fixed clash at Z travel -75, -37.5, 0, +37.5 and +75. The 6 mount holes line up with the plate holes. The only static overlaps are the lock nut's thread on the screw and 0.04 mm3 between the motor shaft and the coupling stand-in. No feature newly fails.

**Left for the owner:**
1. **Measure the real mount before machining the plate.** The CAD differs from the seller's drawing: length 90 against 95, bolt spacing 46 against 45, lower rows 13 apart against 12, bearing 7901 against 7001.
2. **Confirm D-211.** It is Claude's default, because the owner gave no preference. LiMo must confirm the 21.5 long 10 mm end on the Z screw, and any cost.
3. **Spindle clearance.** The Jianken stand-in clears the mount by only 2 at Z travel +75, and its length is not confirmed.
4. **6 x M6 mount screws.** Not sized, not in `docs/bom.csv`, not priced.
5. **M12 price.** The 20 mm 400 x 180 piece is too short for the 442 plate. The longer piece is not priced.

**Exact next step:** the owner saves `Type_0_v3` and measures the mount. Then model the couplings and sensors, and do the HGH20CA block swap.

## 000000000000000000000000000000000000000000000000000000. 18 Nov 2026: XRollerShim replaced by a second XRoller Angle over the top tube (D-209)

**Done in `Type_0_v3`, not saved. The owner saves it.**
- `XRoller Bottom:2` is the same part as the bottom roller, turned over, on top of the tube: flange Z 405 to 411, leg Z 361 to 411. It is joined to `XRollers` by the as-built joint `Top X roller angle to XRollers`.
- `XRollerShim` is hidden, not deleted, because Rigid Groups 252 and 268 and Rigid 164 refer to it.
- The 4 top holes of `Z Fixed Plate` moved from Z 372 and 396 to Z 374.5 and 398.5, in both plate sketches.
- The tube's 8 top holes are tapped M6, and 8 x M6 x 8 flange screws are modelled in `Top angle flange screws M6x8` (D-210).
- `docs/bom.csv`: the 4 top plate screws move from M6 x 30 (X12) to M6 x 20 (X03). No price changes.

**Checked:** no clashes for the new angle at X slide 0, -215 and -430. The 4 plate holes line up with the leg. The timeline has the same 6 failing features as before, and no new ones.

**Left for the owner:**
1. **M6 x 8 screws, 8 off (D-210).** Not in `docs/bom.csv` and not priced. They thread only into the 3 thick tube wall, about 3 threads each.
2. **Rail block screw access.** The tube's top holes are now tapped, so they no longer give tool access to the block screws. The HGH20CA block swap needs its own access holes in the top wall at X -283, -247, -198, -162 and Y 489, 521, under the flange. The M5 rods and X nut sit in line with those holes, so the block screws go in first.
3. **Rail class.** The owner reads LiMo's reply as a 10 % surcharge for Class H. Class H is not chosen yet, and `docs/bom.csv` is unchanged.

**Unused holes:** the leg's centre hole at X -222.5, Z 398.5 and the 4 old tapped holes in the tube's front wall.

**Exact next step:** the owner saves `Type_0_v3`. Then carry out items 1 to 4 of the D-208 entry below.

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

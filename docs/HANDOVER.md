# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000. 18 Nov 2026: supplier drawings saved, modelling not started

**Done:** the owner's 7 drawings are saved in `cad/vendor/drawings/`, with their values and flags in `cad/vendor/drawings/README.md`. No CAD was changed in this step.

**Left, by part:**
1. **Couplings (4).** The D25L35 sizes are now known (hub 11.75, M3). Ready to model. The hub is shorter than the 12.9 grip set in D-186, so check the shaft ends against the spider.
2. **Homing sensors.** M12 sizes are known. Ready to model, with the printed mounts changed to M12. The drawing says NPN and the BOM buys PNP.
3. **Z motor mount.** The HM12-60-V drawing is saved. **Owner to decide:** it includes a 7001 bearing, so it may replace the Z BK12 and the D-206 bracket.
4. **Spindle clamp.** The profile is known. Still missing: clamp length along the spindle, base bolt holes and bore centre height.
5. **Spindle JGL-80.** The new page has specifications only. The Jianken dimension drawing is still missing.
6. **Nut housings.** The LiMo drawing (M07) is still missing.
7. **X, Y and Y2 nut flanges.** The catalogue gives 40 across flats. LiMo has not confirmed the flats.
8. **X, Y and Y2 HGH20CA blocks.** Approved, not done: see the entry below.

**`Type_0_v3` still has unsaved changes. The owner saves it.**

**Exact next step:** the owner saves `Type_0_v3` and decides item 3. Then, in a new session, read `cad/vendor/drawings/README.md`, model the couplings and sensors, and do the block swap.

## 00000000000000000000000000000000000000000000000000. 18 Nov 2026: Z axis stand-ins replaced, the rest listed (D-206)

**Done in `Type_0_v3`:**
- **Z motor.** The StepperOnline 24HS34-5004D-E1000-B280 vendor model is fitted, flange at Z 612, top at Z 758, cables to the back.
- **Z rails.** Two HGR20 x 350 rails with the HIWIN section, 6 counterbored holes at 60 pitch, first hole 25 from the end (`tools/build_fusion_parts.py`). The block and rail overlap has gone.
- **Z BK12 bracket (D-206).** Finished at 90 x 60 x 15: 4 x M5 tapped holes for the BK12, and 2 x M6 counterbored holes into 2 tapped holes in the top edge of the fixed plate.
- **Z coupling.** Corrected from Ø26 to the D25L35 in the BOM. It is still a stand-in.
- **Checks.** No moving-to-fixed clash at Z travel -75, -37.5, 0, +37.5 and +75. The motor clears the mount. The timeline is 1367. The old bodies are hidden, not deleted. **The document is modified and not saved. The owner saves it.**

**Not done: X, Y and Y2 blocks.** The owner approved the swap to HGH20CA, but the 8 HGW20CC blocks are still fitted. Setting `YCarriageB/C` and `XCarriageB/C` to 32 and 36 was tried and undone: it broke `Rigid 3`, `Rigid 4`, `Rigid 361` and the D-199 riser bolt features, the Y roller holes did not move, and the X holes ended up 2 off the block centre. The sketches `YRoller Lower`, `XTopRollerLower` and `Xroller Carriage Holes` need re-anchoring on the block centres. The thread in the HGH20CA is M5 and only 6 deep, so the M6 x 12 block screws must become M5 x 8 (M5 x 10 in the bottom X roller).

**Still stand-ins, and what each needs:**
1. **Spindle JGL-80/2.2R24-20.** Jianken dimension drawing. The page the owner sent covers the JGM series only, and the manual linked in D-39 could not be reached (connection refused).
2. **Spindle clamp 80.** Drawing or measurements of the clamp in the G-Penny kit (S03).
3. **Z nut housing, and the X, Y and Y2 housings.** LiMo drawing of the steel housing (M07).
4. **Z motor mount.** LiMo HM12-60 drawing and the reply to message 6a (task 14).
5. **4 x D25L35 couplings.** LiMo drawing: bore depth and hub shape.
6. **X, Y and Y2 nut flanges.** Still round. LiMo to confirm the flats.
7. **Homing sensors.** M8 in the model, M12 LJ12A3 in the BOM. Owner chose to leave them until the LJ12A3 drawing is available.

**Check when the parts arrive:**
- **BK12 holes.** The vendor CAD has 4 x Ø5.5 on 46 x 16, but `cad/vendor/README.md` said Ø6.6 at 46. The bracket follows the CAD.
- **Motor pilot.** The Z motor STEP shows Ø38.1, its PDF says Ø36. The mount needs the real size.
- **M12 cut list.** The bracket needs a 15 mm piece at least 90 x 60. The 350 x 100 piece leaves under 50 wide after the risers, so it does not cover it. Not priced.
- **Bracket screws.** 4 x M5 x 35 and 2 x M6 x 25 are not in the BOM yet.

**Exact next step:** the owner saves `Type_0_v3`. Then, in a new session, re-anchor the roller hole sketches and fit the HGH20CA blocks on X, Y and Y2.

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

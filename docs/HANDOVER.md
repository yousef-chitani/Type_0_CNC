# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000. 18 Nov 2026: motor plates moved, risers shortened (D-186, D-187)

**Done:** in `Type_0_v3` the motor plates on X, Y and Y2 moved 12 towards the screws, the motors moved with them and the couplings moved 6. The BK12 risers are 12 shorter, their rear bolts moved 12 forward, and the X gantry tube holes moved to match. Measured: 12.9 of grip per shaft, 1.6 from coupling to BK12, Y motor rear at Y 775, X motor rear at X 515. Timeline 1230, 1 error and 5 warnings, the same failures as version 1. Details are in `docs/printnc-assessment.md`. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Motor plate bolts, owner to confirm.** M6 x 20 would bottom out in the 12 deep holes. M6 x 16 fits but is not in `docs/bom.csv`, and needs a live price.
2. **X riser side holes.** The two 4 mm holes at X 375.5 leave 0.5 of wall to the new end face. Decide whether to move them.
3. **Front Y riser bolts** at X -305 and 305 sit outside the risers (already wrong, not moved). The tub needs drilling for the new Y 629 bolts.
4. **Motor length, owner to confirm.** The STEP is named `24HE40-5004D-E1000` and gives a 125 body. No datasheet for it is in `cad/vendor/`.
5. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.
6. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, start the Z plate (D-179, D-184). Re-count errors and warnings after every write.

## 0000000000000000000000000000000000000. 18 Nov 2026: DFU1605 nuts, 24HS40 motors and couplings fitted

**Done:** the owner saved `Type_0_v3` as version 2 with the rails shifted. After that, DFU1605 nuts, 24HS40 motors and stand-in D25L35 couplings went in on X, Y and Y2, and the parts they replace are hidden. Timeline 1205, 1 error and 5 warnings, the same failures as version 1. Y motor rear is 134 behind the tub (D-142 allows about 185). The nut-to-BF12 gap stays 4.7. Details are in `docs/printnc-assessment.md`. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Coupling grip: decided (D-186), not yet modelled.** Move the motor plates on X, Y and Y2 12 towards the screws, with the motors and couplings. Shorten the Y risers and the matching X part by 12. Expected result: 12.9 of grip per shaft, 1.6 from coupling to BK12, Y motor rear at Y 775.
2. **Motor length, owner to confirm.** The STEP is named `24HE40-5004D-E1000` and gives a 125 body. No datasheet for it is in `cad/vendor/`.
3. **Review the parts that moved with the rails:** Y trigger mount, roller sensor mount and cable chain supports.
4. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, once the owner has saved `Type_0_v3`, find what locates the `Nema24 Plate` on each axis and apply D-186. Re-count errors and warnings and re-measure the grip and gaps, then start the Z plate.

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

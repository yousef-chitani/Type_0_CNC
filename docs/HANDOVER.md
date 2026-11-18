# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000. 18 Nov 2026: Y rails shifted, Y travel measured

**Done:** both Y rails in the open `Type_0_v3` now run Y 2.5 to 552.5, clear of the risers, and all 9 holes on each rail line up with the frame holes. The rail body was tied to the `YFrame` end face, so the frame hole (`d80`) and the rail end (`d196`) had to move together (`docs/printnc-assessment.md`). Y travel is 386.2 on the rails (Type 0 needs 350). The 385 slider range was run at 5 positions with no clashes. Timeline 1183, 1 error and 5 warnings, the same failures as version 1. **The document is modified and not saved. The owner saves it.**

**Left:** the imported parts, then the Z axis. Rules for model edits: re-count errors and warnings after every write and undo any edit that raises them; hide parts, never delete them; list each change in `docs/printnc-assessment.md`; do not save through the tool.
1. **Imported parts (D-180, D-182).** DFU1605 nut and 24HS40 motor from `cad/vendor/`, and a D25L35 coupling. Take the motor length from the datasheet, because the STEP includes other geometry. This gives the X motor overhang and the Y motor overhang against the 185 in D-142. Re-check the nut against the BF12: the SFU1610 nut stops 4.7 away and the DFU1605 is longer.
2. **Z axis (D-179, D-184).** New 150 wide plate, 6082 in Phase 1 then steel, 15 risers stay, 350 high.

**Exact next step:** in a new session, after the owner has saved `Type_0_v3`, import the DFU1605 nut from `cad/vendor/` on the Y axis and re-run the Y travel check.

## 00000000000000000000000000000000000. 18 Nov 2026: Y motors at the back, Y rails still to shift

**Done:** D-184 (Z plate: 6082 in Phase 1 then steel, 15 risers stay, 350 high) and D-185 (Y stays 550 rail, 650 screw, 690 tub). In the open `Type_0_v3`: BK12 supports and NEMA 24 plates shown on X, Y and Y2, and the Y risers, screws and motors turned end for end, with the motors at the back on both sides. Timeline 1183, 1 error and 5 warnings, the same failures as version 1. **The document is modified and not saved. The owner saves it.**

**Left:** the Y rails still run Y 64 to 614 and overlap the BK12 risers by 60.5. They should run Y 2.5 to 552.5. The 386 travel is worked out, and must be measured once the rails are in place. Then item 3 and item 4 in the next entry (D-184 unblocks item 4).

**Do not repeat:** a `Rigid 2` offset moves the rail in Z. Re-pointing `Rigid 2` at a sketch point leaves the rail body behind and throws the Y2 drive 61.5 out. Both are in `docs/printnc-assessment.md`.

**Exact next step:** in a new session, find out why the `Y HGR20` body stays at Y 64 to 614 when its occurrence moves (start with `MoveFace2`, `Base Feature1` and `Rigid Group 247`). Then shift both Y rails 61.5 forward, keeping the 1 error and 5 warnings, and re-measure the travel.

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

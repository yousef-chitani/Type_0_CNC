# Type 0 CNC: handover (2026-11-23)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (13th session): ATC one-piece mount, 40 lower (D-289), design written
- Owner: "the mount should be 1 continuous part; the ATC assembly can be made much more compact and shorter". Q&A: machined 6082 (made on the mill before Phase 2), wheel about 40 lower (fork plane Z 131), rigid motor joint kept (D-254).
- Design: `docs/superpowers/specs/2026-11-23-atc-one-piece-mount-design.md`. Mount, bearing, hub replace 9 parts: hub and shaft one part, 1204 self-aligning bearing and motor pilot bored in one set-up in the mount web, cup round the motor, slotted yoke so tools hang through, 80 x 10 x 50 strip with 4 x M6 (Phase 1 mould). Nose at pickup Z 141, lift Z 192 (53 to the top of Z).
- All figures are Claude's proposal, owner to confirm. Nothing modelled.

**Left:** owner approves the design doc; then model it in `Type_0_v3` and run the checks listed in the doc (plate edge at the approach below Z 70, moving-Z clash, grub screw access, real motor length, yoke stiffness). Front slot against the keep-out still open.

**Exact next step:** owner reads and approves the design doc (or corrects it); then a session models the mount and runs its 6 checks.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (12th session): task 26, rear ATC not feasible; front kept (D-288)
- Measured in `Type_0_v3` (bounding boxes, Y at the rear limit, not saved, nothing changed): spindle axis Y -88 to 297; tub floor top Z 45 to Y 653, no rear wall; carriage underside Z 169 (Z plate, Z rails, X roller angle, within X ±75 of the spindle), beam underside Z 205 over the full width, sweeping Y 60 to 565.
- Result in `docs/rear-atc-reach.md`: a rear wheel inside the tub must have its holder tops at Z 165 or lower, which leaves about 25 of tool. With the wheel behind the pickup it also clashes at the pickup itself. With the wheel beside the pickup it sits under the beam's sweep and over the plate's back-right corner. A wheel past the tub end needs +367 of Y travel (rails, screws and tub about 370 longer). The Y motors and BK12 risers are not the limit.
- **D-288 (owner):** rear dropped, front ATC kept, "very very elegant, integrate and not a kludge". Design-issues 11, 12 and 20 updated; task 26 done.

**Left:** front slot against the ATC keep-out (the slot may be X ±107.5, the keep-out starts at X 88, so they overlap by 19.5); review the unconfirmed front ATC parts (D-250, D-253, D-255) against the owner's "elegant, integrated" requirement; the front strip goes on the mould drawing. Still open from the review: task 18 plate pull-down and pour, ATC 6804 bearing idea, the unpriced lines.

**Exact next step:** the owner saves `Type_0_v3`; then a session settles the front slot (task 24 item 6) together with the ATC keep-out, aiming for an integrated front ATC.

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

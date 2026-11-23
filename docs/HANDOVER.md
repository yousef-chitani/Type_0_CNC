# Type 0 CNC: handover (2026-11-23)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (9th session): docs for D-271, D-275 ATC hub modelled; not saved
- `Type_0_v3` was found **saved** with D-280.
- **Docs (D-271), committed:** `bom.csv` G06 (8 mm levelling pour, jack screws, no ground stock), X19 now M6 x 25, new **X22** jack screws 12 x M6 x 20 DIN 913 (unpriced), F02 pour quantity (2 x 437.5 cm³, about 1 kg neat resin). `cad/v2/out/assembly/cast_in_features.md` has a new section for the EG tub, with numbers from the model (tub 38.63 L, about 88.8 kg); the old base and portal tables are kept below it as history. `spec-gaps.md` updated. Phase 1 total unchanged, £3,963.35. `bom.csv` is LF in git now (the CRLF note in section 9 is out of date).
- **D-275 modelled** (owner, Q&A: "Down, hub tapped M4", "202.5°, r 44"): hub with 8 flats 101.6 across (corners Ø110), holes Ø3.3 x 10 tapped M4 (cosmetic threads), fork holes opened to Ø4.5 with a Ø8.5 countersink, 8 x M4 x 12 countersunk screws (replacing the M3s), index flag and LJ12A3 sensor rotated to 202.5°, and the top plate sensor hole moved with them. Features `D-275 ...` in `ATC Shaft and Hub`, `ATC Forks`, `ATC Fasteners` (base feature edited), `ATC Drive`, `ATC Bracket`. Clash check of the wheel: only screw threads and a 0.01 contact band at each fork step (the step measures 50.79 from the centre). Health 35 before and after. Docs: `decisions.md` D-275, `atc-wheel.md`, BOM A01 and A06, design-issues item 23.
- **Model not saved.** The owner saves `Type_0_v3`.

**Left (model):** none from the list. **Docs:** design-issues sections E and F (owner confirmations, stand-ins); X22 and G06 to price; the jack screw length and positions (D-271) for the owner to confirm.

**Exact next step:** the owner saves `Type_0_v3`; then a session works through design-issues section E (owner confirmations) with the owner in the Q&A tool.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (8th session): X trigger mount 45 taller (D-280); not saved
- `Type_0_v3` was found **saved** with D-278 and D-279.
- Design-issues item 18 checked: the X gantry trigger mount (X 250 to 265, Y 565 to 577.5) and its M6 x 20 target ended at Z 288.5, 46 below the X home sensor tip (Z 334.5, pointing down from the X roller). X could not home. (The "2.5 short" note was not the real fault.)
- **D-280** (owner: "Taller trigger mount"): mount grown 45 to Z 333.5, screw up 45 (axis Z 328.5), 1 gap to the sensor as on Y. The band under the sensor is clear over the X travel; the X cable chain lies at Y 584 and beyond, clear of the mount. Features `D-280 ...` in `XGantry Trigger Mount` and `M6x20 (5)`. Clash check: only the 2 old screw overlaps. Health 35 before and after.
- **Model not saved.** The owner saves `Type_0_v3`.

**Left (model):** D-275 hub. **Docs:** BOM G06 text (8 mm pour, jack screws), X19 hold-down length M6 x 25, new jack screw line (unpriced), pour quantity; `cast_in_features`, `spec-gaps.md`. Design-issues sections E and F (owner confirmations, stand-ins).

**Exact next step:** the owner saves `Type_0_v3`; then a session models the D-275 ATC hub (fork screw M4, 8-flat hub), or does the docs list above.

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

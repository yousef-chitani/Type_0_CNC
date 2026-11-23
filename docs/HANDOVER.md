# Type 0 CNC: handover (2026-11-23)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (11th session): Gemini review checked; docs fixed (D-284 to D-287)
- The owner pasted a review of the repo by Gemini (8 points, at commit `db206e3`). Checked each against the repo. Point 2 (roller steel) was already done in D-281 to D-283; point 4 (ATC shaft on one bearing) is the risk the owner accepted in D-254; the rest hold.
- **D-284:** Y2 on the 7I76EU with no pin moved: step/dir 3 = Y2, ATC to channel 4 on TB3 (pins to check), Y2 home IN15, Y2 alarm IN16 (TB5). `electrical.md` updated (4 CL57T drives); `io-list.md` marked out of date.
- **D-285:** LinuxCNC config left at 3 joints (no LinuxCNC on this PC to run the 23 simulator checks). Task 19 step 2 lists the exact changes (trivkins `XYZY`, `HOME_SEQUENCE = -1` on both Y joints, nets, fault input, `Type_0_v3` travel, simulator checks). `linuxcnc.md` says the config is out of date.
- **D-286:** S04 stays 4 x 5 m; its note says 5 runs now, decide when the motor cables are measured. Total unchanged, **£4,041.97, £158.03 left**.
- **D-287:** PETG commissioning parts (risers, motor plates, nut and fill plates): 6 walls, 50% gyroid, in `printed-parts.md`.
- Stale lines fixed: `README.md` (moving gantry, `Type_0_v3`), `tasks/README.md` state lines, key-files row for `cad/v2/assembly.py` (superseded).

**Left from the review:** (1) task 26: the spindle reaches only Y 292 to 297 and the tub runs to Y 653, so a rear wheel needs longer Y travel or sits behind the plate under the gantry; check this first. (3) Task 18: say how each wall-top plate is pulled down onto its jack screws and checked with the straightedge, and how the 8 mm gap is dammed, vented and poured without air. (4) Phase 2: a 6804 bearing in the ATC motor plate (then the motor joint needs some give). (6) Budget: G01, G06, X18 to X22 unpriced against £158.03; one steel order, one screw order. Also from the 10th session: owner saves `Type_0_v3`; drill guides 8A, 8B, 9A, 9B; design-issues item 27.

**Exact next step:** the owner saves `Type_0_v3`; then a session does the Y reach check for task 26 (can the spindle reach a rear wheel at all), before any other rear ATC work.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (10th session): section F with the owner; D-281 to D-283 roller steel, modelled; not saved
- `Type_0_v3` was found **saved** with D-275.
- Section E had nothing the owner could confirm yet (item 20 waits on the rear ATC study D-274, item 21 on the seller), so the owner chose section F.
- **Item 26 done:** the 80 x 187 x 93 ATC bracket fits the P1S bed (256 cube). **Item 22:** the spindle drawing came in D-213; the ISO20 holder stays a stand-in until Phase 2 (owner).
- **D-281:** X roller tube 120 x 60 x 3 (stock); the extra 10 goes up (tube Z 355 to 415, X screw axis still Z 380). Moved up 10: top angle, its 8 M6 x 8, D-262 screws #6 to #9, 4 Z plate holes (now Z 384.5 and 408.5). Nut plate and fill plate are now 120 x 60.
- **D-282:** X roller angles 100 x 50 x 6 (stock); flat legs end at Y 537. 4 rear holes in the top angle and tube top wall moved to Y 521 with their screws; 4 unused rear holes in the bottom angle filled.
- **D-283:** the Y braces are 75 x 50 x 6 (earlier notes said 75 x 75, wrongly), already stock, unchanged.
- Clash check: only screws in tapped holes, rails in blocks and vendor internals. Health 35 before and after. Features `D-281 ...`, `D-282 ...` in `XRollers`, `X 1610 Nut Plate`, `X 1610 Fill Plate`, `XRoller Top Angle`, `XRoller Bottom`, `Top angle flange screws M6x8`, `Joint screws added (D-262)`, `Z Fixed Plate`.
- **BOM:** G05 priced (owner): K I Metals, curl 23 Nov, £65.52 ex VAT, **£78.62** inc VAT, delivery not shown. Total **£4,041.97, £158.03 left**.
- **Model not saved.** The owner saves `Type_0_v3`.

**Left:** hidden drill guides 8A, 8B, 9A, 9B no longer fit the X roller (redo before printing them). Design-issues item 23 (ATC motor length) and 24 (stand-ins) wait on Phase 2 parts; section G (item 27 ATC clash with moving Z, item 28 Chamfer2).

**Exact next step:** the owner saves `Type_0_v3`; then a session does design-issues item 27 (ATC clash check with the moving Z), or the drill guides if they are needed soon.

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

# Type 0 CNC: handover (2026-11-26)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (45th session): V5 plan Task 3 done
- **Decided (owner, Q&A):** **D-356** nut and fill plates are drilled aluminium flat bar; **D-357** HM12 and BF12 risers are steel flat bar with shims; **D-358** one X carriage plate: the Z fixed plate bolts straight onto the 4 X blocks; **D-359** 2 mm shims under the Z blocks and nut housing replace the D-205 pocket; **D-360** a bought 80 mm spindle clamp replaces PrintNC's (D-247).
- **Done:** `docs/v5-parts.md` lists every PrintNC part (Fusion names in `Type_0_v5`, STEP names where they differ) as kept, changed or dropped, with how made, stock, load and notes, plus the new V5 parts. `tools/v5_parts_check.py` **PASS** (52 rows; how-made only bought / printed / owner / shop grind / none; no mill, turn or laser). Joint check in Fusion (read-only, bounding boxes): every PrintNC structural joint is bolted, no welding.
- **Found:** `Type_0_v5` already exists in Fusion as a saved, unmodified copy of PrintNC at stock sizes (1182 timeline items, 94 parameters). Not changed this session. PrintNC has 3 X frame tubes; V5 buys 2 (D-354): what carries the bed and rack is for Task 4.
- **Left:** riser heights, M5/M6 thread length in the 6 mm tube wall, and the spindle clamp choice and price (Task 8). The two untracked STEPs in the repo (`PrintNC ... Elements to take.step`, `cad/v2/Facebutton v2 frame.step`) are not committed.
- **Exact next step:** plan Task 4: in `Type_0_v5`, set PrintNC's parameters for the V5 frame, Y axis and bed (sizes from `tools/v5_sizes.py`, D-353 to D-360), then the check script.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (44th session): V5 plan Tasks 1 and 2 done
- **Decided (owner, Q&A):** **D-352** the "nose" is the spindle front face, where the holder flange seats; **D-353** beam RHS 200 x 150 x 8 standing up; **D-354** frame tubes SHS 80 x 80 x 6; **D-355** X rails 122 apart on the beam front.
- **Done, Task 1:** the owner's ISO20-ER16 holder STEP is now `cad/vendor/iso20_er16_holder.step` (README row). Flange top to pull-stud top is 45.85 and the flange is Ø33 (the stand-in had Ø45). `tools/v5_sizes.py` **PASS**: holder tops 70.85 to 120 above the table.
- **Done, Task 2:** `tools/v5_beam.py` covers the flat face, the rail fit, Ix/Iy/J, mass and the beam's share of nose movement per 100 N (all under 1 µm for 200 x 150) for 4 beams and 4 frame tubes. `docs/price-check-v5.md` has K I Metals Store API prices by curl, 26 Nov: beam £88.95 and frame £94.29, both ex VAT, delivery not known.
- **Left:** the lever arms in `v5_beam.py` (173 front face to axis, beam centre 45 above nose max) are estimates until Task 5. Measure the delivered tube's corner radius before drilling. The holder STEP is converted from a drawing (taper modelled at 8.000°). Still open from the 43rd session: the 59 mm screw end inside the HM12 against the 95 drawing.
- **Exact next step:** plan Task 3. Write `docs/v5-parts.md`: list every PrintNC part (STEP `PrintNC V4 Metalcutter V4.0.33 Elements to take.step`, repo root) as kept, changed or dropped, with how each is made, then Q&A on flagged parts.

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-360**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 8. Key files
| File | What |
|---|---|
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Old** CadQuery assembly of the fixed-gantry design: **superseded by the Fusion 360 model `Type_0_v3`** (D-137, D-183). `cad/v2/out/assembly/cast_in_features.md` has a current section for the EG tub |
| `cad/vendor/` | Manufacturer STEP files (and the Z motor PDF) used by the assembly |
| `docs/decisions.md` | Decision log D-01 … D-336 |
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
| `docs/v4-pour.md` | V4 lean EG fill quantities (`23.5 L`) and pour/tamping order (`D-315`, `D-336`) |
| `docs/eg-moulds.md`, `aggregates.md`, `epoxy-options.md` | Casting notes (partly v1 sizes: use the assembly for sizes) |
| `docs/bom.csv` + generated `bom.md`, `phase1-bom.xlsx`, `phase1-cost.md` | Parts and costs |
| `docs/phase1-schedule.md` | Timeline and order waves |
| `docs/price-check-task-*.md`, `docs/cad-download-task.md`, `docs/supplier-messages.md` | Task files for the owner's local session, message drafts |
| `docs/review-task-eg-design.md`, `docs/review-eg-design-report.md` | EG design review: brief and report |

## 9. Working notes for the next session
- **Fusion 360 MCP:** configured in Antigravity via plugin `fusion-mcp` (`http://127.0.0.1:27182/mcp`). `Type_0_v4` is the active V4 design; do not save Fusion documents unless asked by the owner.
- **CadQuery** isn't preinstalled in the cloud container: `pip install cadquery` (about 1 minute). `python cad/v2/assembly.py` takes about 2–3 minutes (vendor STEP import + clash check at 3 positions); `--envelopes` skips the vendor models.
- After changing the assembly, also run `cad/v2/enclosure.py`, `cad/v2/bench.py` and `cad/v2/base_cores_sketch.py` (they read `cad/v2/out/assembly/assembly_data.json` or the assembly numbers), and regenerate `cast_in_features.md` from the `features` list in `assembly_data.json` (one table per casting; no script in the repo).
- **Views:** `python cad/v2/render_views.py` re-renders the PNG views in `cad/v2/out/assembly/` (about 3 minutes; run it after `assembly.py`).
- **Rendering:** the CadQuery SVG exporter gives rotated views; use the matplotlib tessellation render instead. To view SVG drawings, screenshot them with Playwright (preinstalled).
- `docs/bom.csv` uses **CRLF** line endings and CSV-escaped quotes (`""`): keep both when editing.
- LinuxCNC can be tested in a Debian 12 Docker container (2.9.10 from linuxcnc.org); see `docs/linuxcnc.md` section 4.

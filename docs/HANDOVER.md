# Type 0 CNC: handover (2026-11-26)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 26 Nov 2026 (35th session): Task 29 step 2 and Task 27 Task 7 done — `Type_0_v4` finished (timeline 320, 0 unhealthy, 9 poses clean), BOM updated (£4,386.61)
- **Owner decisions (D-331 to D-336, Q&A):**
  - **D-331:** Z and X belt folds both use **75 mm centres** (`HTD 250-5M-15` 50T, fixing the 310 mm slip in `task28-folds-and-footprint.md`; Optibelt 5M-15 working pull 570 N vs 189 N Z / 251 N X stall, 2.3–3.0x margin, D-322), `2 x 6000-2RS` (`10 x 26 x 8`) in identical `70 x 142 x 20` 6082 fold plates and identical `Ø10 x 68` steel stub shafts (`Ø14 x 1.5` shoulder).
  - **D-332:** X- pad stays on the beam (`90 x 60 x 20` at `X -350..-260`, stepped `6.5 x 5.5` for the HM12's 12 mm flange); X DFU1605 C5 screw shortened from 900 to custom **865 mm** at LiMo (`tools/v4_sizes.py` PASS, whip 2,662 rpm). `G11` flat bar `160 x 20` now `980 mm` (£72.64 inc).
  - **D-333:** Tapered `150->80 x 145 x 20` 6082 `X nut bracket` bolts through `Z fixed plate` (`4 x M6 x 35` + `2 x Ø6 x 24` dowels); 9 obsolete v3 PrintNC roller holes in `Z fixed plate` plugged.
  - **D-334:** `Table plate M11` gets `9 x 6` blind (`20 mm`) M6 grid (`50 mm` pitch) + `4 x Ø8 H7 x 18` blind dowels + `Ø10 x 15` counterbores for `16 x M5 x 16` block and `4 x M5 x 25` nut screws.
  - **D-335:** Mild steel laser sub-pack (`Y motor plate 80 x 155 x 10`, `2 x nut spacers 52 x 40 x 5`, `Bottom sheet 500 x 670 x 3` `F28`); `2 x 120 x 120 x 5` beam end caps (`G12`, `8 x M5 x 16` + silicone); `4 x` side-mounted **PETG printed** drip skirts (`F32`, `164.5 x 67 x 3`, `8 x M4 x 10` into table side edges `X = ±230`, clearing `HGH20CA` blocks by 3 mm).
  - **D-336:** `F01` switched to `2 x 4.66 kg` Ampreg 30 SLOW packs (£208.39 inc, saves £145.61).
- **Model `Type_0_v4` (`docs/v4-model.md`, NOT saved — owner saves in Fusion):** timeline **320 items, 0 unhealthy**; **464 visible solid bodies**, all materials assigned (`Steel` 393, `Aluminum 6061` 33, `Aluminum 5083` 1, `Stainless Steel` 6, `ABS Plastic`/PETG 27, `Rubber` 7, `Granite`/EG 3); every joint hole has a modelled fastener; **0 unexpected overlaps across all 9 rest/limit/ATC poses**; overall envelope **`953.7 x 805.0 x 879.7 mm`**.
- **Task 27 Task 7 & BOM (`docs/v4-pour.md`, `docs/requirements.md`, `docs/v4-sizes.md`, `docs/bom.csv`):** `X18` (£30.82), `X21` (£18.75), `F28` fixings (£9.14), `F32` (£3.08), `G09` (£10.43), `X23` (£10.77), `M17` stub bar (£6.22) priced live by curl (Westfield + KJN + K I Metals, 26 Nov); dead v3 lines (`F07`, `X11`, `X13`, `X14`, `X16`) dropped; **Phase 1 priced total £4,386.61** (down £173.19 from £4,559.80; unpriced: `M15`, `M16`, `F30`, `F31`, `F33`, `G10`, `X24`, `X25`, plus laser/mill/lathe shop quotes).
- **What is left:** owner saves `Type_0_v4` in Fusion and updates LiMo (`865 mm` X screw) + prices `M15`/`M16`/bearings (`docs/owner-todo.txt`); Task 29 steps 3 to 6 (assembly check with key access, make-ability check per part, Fusion drawings + STEP per part, RFQ cover sheets). Note: ATC D-317 fault 2 (separate slotted motor plate) remains open for Phase 2 (`D-328`).
- **Exact next step:** owner saves `Type_0_v4`; next session runs **Task 29 step 3** (assembly order check on `Type_0_v4`, verifying hex-key access for every screw and the pre-pour vs post-pour beam fastener sequence).

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 25 Nov 2026 (34th session): task 29 owner answers (D-329, D-330); V4 EG fill priced against two grouts
- **D-329:** the owner makes the simple parts (saw, drill, tap): base end plates, uprights, beam, beam rear spacers. Shops make the rest. If the upright joint faces need milling, the uprights move to the mill pack (step 4).
- **D-330:** the RFQ is split by process: laser (and bend), CNC mill, surface grind, lathe; one cover sheet per sub-pack. Parts sorted in `docs/tasks/29-quote-ready-design.md`.
- **EG fill against grouts** (owner asked): `docs/eg-fill-vs-grouts.md`. V4 fill 23.5 L (pockets 2 x 6.98, beam 9.57), about 54 kg. EG (P1, 11 %, provisional) **£4.95/L used**; bought for V4 £416.22 (kit) or £270.61 (2 x 4.66 kg) = £17.70 or £11.51 per litre. **Sikadur-42+ HE Cold Climate** £326.95 per 8.85 L = **£36.94/L**, £980.85 for V4. **Parex 100 Newton Grout** (cement) £46.96 per 12.5 L = **£3.76/L**, £93.92 to £140.88; not checked: aluminium contact, damping, water cure. Rawlins, curl 25 Nov; delivery unknown. `bom.csv` not changed.
- Task 29 is not finished: steps 2 to 6 (model, assembly check, make-ability, drawings and STEP, RFQ) remain and need several Fusion sessions.
- **Exact next step:** task 29 step 2: finish `Type_0_v4` (task 27 Task 7; D-320 X HM12 and pad; D-325 to D-327 folds with `cad/vendor/htd5m_20t_15.step`; replace the envelopes; set the material of every body; a fastener for every hole; clash check at the axis ends). Owner: pick the EG fill.

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-336**).
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

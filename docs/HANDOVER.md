# Type 0 CNC: handover (2026-11-28)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `.claude/NEXT_PROMPT.md` and `.claude/CODEMAP.md`, then the rules in `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 28 Nov 2026 (57th session): `Type_0_v6` Y belt drives, front BK12s, X HM12-60 + motor, PETG belt covers & BOM update
- **State at start:** Live Fusion design `Type_0_v6` with 56th session base/ATC/splash shields (`1283` timeline items, `0` errors).
- **Decided (owner, Q&A / live Fusion):** **D-389** Y1/Y2 `6 mm` steel belt plates (`80×195`, `Y -6..0`, `48×38` open bottom cable archway, `±4 mm` vertical motor slots, top push-down M5 tensioning lug `Z 189..197`), `1:1` `20T / 20T` `HTD 5M-300` (15 mm wide, `C = 99.62 mm`), front floating `Y BF12:3` / `Y2 BF12:3` swapped to real fixed `BK12` blocks (`cad/vendor/bk12.step` at `X = ±365`, `Z = 230..273`), and 3D-printed PETG front belt covers (`Y = -39..-6`, 3 mm wall + 3 mm cap); **D-390** PrintNC `X HM12-57` hidden and replaced with real `HM12-60` (`cad/vendor/hm12_60.step` at `X = 319.2..431.2, Y = 615.25, Z = 455..515`) + inline coaxial `24HS40` motor at `+X` (`X = 431.2`).
- **Done (Fusion, NOT saved — owner saves):** Built `V6 Y Motor Belt Drives:1` (6 mm steel plates, 4× real `htd5m_20t_15.step` pulleys, 2× `HTD 5M-300` belts, 2× real `bk12.step`, 2× PETG stadium belt covers), `V6 X Motor & HM12-60` (real `hm12_60.step` + `24hs40_motor`), and **D-391** `ATC Rodless Cylinder CY3B15-200 (Zero Overhang)` (`ZZ = 303 mm`, `Ø16.6` sealed stainless tube, `Ø35×57` magnetic slider, `Y = 360..663, Z = 62` completely inside the ATC well, **0 mm rear overhang**, `Rear Splash Wall 6mm` kept 100% solid). Visually verified via `iso-top-right`, `front`, and `back` screenshots. Timeline: **1327 items, 0 errors**.
- **Done (docs & BOM):** Logged D-389..D-390 in `docs/decisions.md`; updated `docs/bom.csv` (`F01`/`F02` for `32.81 L` EG, `M15`/`M16` for Y `20T`/`HTD 5M-300`, `M11` for `450×280×25`, added `F34` PETG belt covers, `G16` Dyfed Steels v6 pack `PRICE PENDING`, `A12` v6 14-tool ATC `PRICE PENDING`, `S10` flood-coolant loop `PRICE PENDING`) and re-ran all 5 BOM generators + `codemap.py`.
- **Left:** Owner saves `Type_0_v6`, runs `docs/price-check-task-19.md` in browser, phones Dyfed Steels (`01554 772 255`, `docs/supplier-messages.md` §8), and drops real `CD85N20-175` STEP into `cad/vendor/`. Next CAD work: mount `CD85N20-175` + reed switches + splash curtain in rear ATC well, model rear `Y BF12` floating blocks / cable chains / homing sensors, and finalize v6 BOM prices (replacing V4 steel/ATC lines once Dyfed & AliExpress prices arrive).
- **Exact next step:** Owner saves `Type_0_v6`; then `.claude/NEXT_PROMPT.md`.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 27 Nov 2026 (56th session): `Type_0_v6` monolithic EG cast base, flood-coolant moat & 14-tool sliding ATC
- **State at start:** Owner opened new Fusion design `Type_0_v6` (PrintNC 450×450 cutting area, `120×80×6.3` Y-tubes, `80×80` Y-rollers, `120×120×8` beam, `350 mm` `2Z HGR15` rails, `jianken_jgl80_2.2r24` dropped 20 mm → nose `Z 161.8..381.8`).
- **Decided (owner, Q&A / live Fusion):** **D-383** monolithic upside-down EG base cast in plain waxed 18 mm melamine (`810×708.8×80`, **`32.81 L`** net / ~74 kg EG, capped with 6 mm steel bottom plate + M8 upward anchors, embedded `80×8` Y-pads with 12×M8 holes and `20×6` ATC rail strips with 16×M5 holes); **D-384** integral U-shaped flood-coolant moat (front channel `Y 15..45`, sloped side troughs `25→55 mm`, recessed rear ATC well `350×350×55 mm`, 3×Ø36 rear drains → 3-stage sump recirculation loop); **D-385** `450×280×25` fixture plate (`Y 45..325`, 54×M8 @ 50 mm, 32×Ø8 H7 dowels, 8×M8 hold-downs at `Y 85/285`; zero-point deferred); **D-386** 14-tool (`2×7` @ 56 mm X pitch, 80 mm Y pitch) retractable rear ATC on `2×350 mm` HGR15 rails (`Y 324..674`), parked under gantry at `Y 525/605` (`Z 235` pull-studs, +39 mm under `XRoller Bottom`), extending `170 mm` via **`CD85N20-175`** cylinder onto front hard stops (`Y 310..324`); **D-387** 3-sided 6 mm splash shields (`Z 80..270`, 0 overlaps); **D-388** Dyfed Steels live RHS/SHS stock matched (`120×80×6.3`, `80×80×3`, `120×120×8`).
- **Done (Fusion, not saved):** Built `v6_Base` (saved by owner) and integrated into `Type_0_v6` under `V6 Cast Base & ATC` (old `Component665`, `Flood Catch`, `80x20`, `Body6` hidden). Exact ISO20 fork bars (`3.0 mm` at `Z 183.65..186.65`, `Ø30.6` U-slots): **0 interference hits** against all 14 `iso20_er16_holder.step` holders. ATC rails at `Y 326..676` + hard stops `X ±168..±182, Y 326..336` (1 mm clear of fixture plate `Y 325`). `Type_0_v6` timeline: **1283 items, 0 errors**, 5 pre-existing PrintNC warnings.
- **Done (docs):** `docs/price-check-task-19.md` (AliExpress `CD85N20-175` pneumatics, ATC HGR15 slide, flood-coolant loop); `docs/supplier-messages.md` §8 (Dyfed Steels `Type_0_v6` cut-to-length quote); `docs/decisions.md` D-383..D-388; `docs/tasks/README.md` last D-number updated.
- **Left:** **Next session first task: sort out the Y motor belt plates in `Type_0_v6`** (`24hs40_motor:1` & `:2` inside the front of the Y-tubes). Owner saves `Type_0_v6` (and `v6_Base`), runs `docs/price-check-task-19.md` in browser, phones Dyfed Steels (`01554 772 255`), drops real `CD85N20-175` STEP into `cad/vendor/`; update `docs/bom.csv` for v6.
- **Exact next step:** Owner saves `Type_0_v6`; then `.claude/NEXT_PROMPT.md` (start with Y motor belt plates).

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-373**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 8. Key files
| File | What |
|---|---|
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Old** CadQuery assembly of the fixed-gantry design: superseded by the Fusion 360 models (D-137, D-183); **the live CAD is `Type_0_v5`** (V5, D-338 on; `docs/v5-model.md`). `cad/v2/out/assembly/cast_in_features.md` has a section for the old EG tub |
| `cad/vendor/` | Manufacturer STEP files (and the Z motor PDF) used by the assembly |
| `docs/decisions.md` | Decision log D-01 … D-373 |
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
- **Fusion 360 MCP:** configured in Antigravity via plugin `fusion-mcp` (`http://127.0.0.1:27182/mcp`). `Type_0_v5` is the live V5 design (`Type_0_v4` is frozen); do not save Fusion documents unless asked by the owner.
- **CadQuery** isn't preinstalled in the cloud container: `pip install cadquery` (about 1 minute). `python cad/v2/assembly.py` takes about 2–3 minutes (vendor STEP import + clash check at 3 positions); `--envelopes` skips the vendor models.
- After changing the assembly, also run `cad/v2/enclosure.py`, `cad/v2/bench.py` and `cad/v2/base_cores_sketch.py` (they read `cad/v2/out/assembly/assembly_data.json` or the assembly numbers), and regenerate `cast_in_features.md` from the `features` list in `assembly_data.json` (one table per casting; no script in the repo).
- **Views:** `python cad/v2/render_views.py` re-renders the PNG views in `cad/v2/out/assembly/` (about 3 minutes; run it after `assembly.py`).
- **Rendering:** the CadQuery SVG exporter gives rotated views; use the matplotlib tessellation render instead. To view SVG drawings, screenshot them with Playwright (preinstalled).
- `docs/bom.csv` uses **CRLF** line endings and CSV-escaped quotes (`""`): keep both when editing.
- LinuxCNC can be tested in a Debian 12 Docker container (2.9.10 from linuxcnc.org); see `docs/linuxcnc.md` section 4.

# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000. 18 Nov 2026: steel gantry sketch drawn and clash-checked

**Done:** `cad/v2/steel_gantry_sketch.py` draws the layout below from one list of boxes and checks it over the full X, Y and Z travel. Outputs: `cad/v2/out/steel_gantry_sketch.png` and `.json`. Summary and owner questions: `docs/steel-gantry-sketch.md`. Moving mass **73.4 kg**, centre of mass 30.5 behind the Y carriages.

**Found (still in the drawing, fixes proposed, nothing decided):** (1) round Ø48 ball nut flange overlaps the top arm and both foot steps by 4; (2) the X belt covers the right foot access hole at X 345, Y 262; (3) Y BK12/BF12 touch the foot at X 380; (4) X block to BK12/BF12 gap only 1.25 at the end of travel.

**Left:** the owner has not agreed the layout or the 4 fixes. Not verified: SHS corner radius (flat width), the real ball nut flange. No D-numbers, no STEP. `cad/v2/Facebutton v2 frame.step` is still untracked: ask the owner what it is.

**Exact next step:** get the owner's answers to the 4 questions at the end of `docs/steel-gantry-sketch.md`, apply them to the script, re-run until no clashes are left, and record the decisions (next: D-165). Then the owner starts the gantry in Fusion and prices the tube (Dyfed Steels first).

## 0000000000000000000000. 18 Nov 2026: steel gantry layout brief (sketch NOT drawn)

**Done:** the layout below was worked out by hand. **Not done:** no script, PNG or note exists; no clash check has been run; the owner has not seen or agreed these numbers. All of it is a proposal: no D-numbers.

**Hold fixed:** tub 890 × 630, walls and Y rails (D-139 … D-141); X rails 600 (need 597.5), X screw 700, Y screws 600, Z 350. Coordinates as `cad/v2/gantry_sketch.py`: Z 0 = floor top, Y measured back from the spindle axis for the gantry parts.

| Item | Proposal |
|---|---|
| Usable flat on the SHS faces | Design for **102 wide** (outer corner up to 24, from memory of EN 10219 for 8 mm wall: **verify**). Flat = beam front + 24 to + 126 |
| Beam | Y 150–300 from the spindle (spindle offset **150**, was 175), Z 195–345 |
| Rail seats | Epoxy **4** thick on top and bottom faces. Top pour X ±325; bottom pour stops at ±305, clear of the feet |
| X rails | Top and bottom, same Y: centre **beam front + 36**. Seat to seat 158 apart (was 100) |
| X screw | On top, axis **beam front + 86**, Z 374. BK12 X 290–315 (lock nut to 327), BF12 X −310 to −290, both outside the saddle sweep. Ends −319 to +381 = 700 |
| Top stack | Seat 349, block top 379, **15 spacer** on each block to 394 (DSG16H top = axis + 20 = 394), arm 394–419 |
| Bottom stack | Seat 191, block bottom 161, arm 136–161 |
| Saddle | 3 pieces of 6082: existing front plate 180 × 400 × 20 (Y 125–145, Z 70–470, 5 clear of the beam) + **2 arms 180 × 130 × 25**. 5 × M8 in a row per arm, heads counterbored flush, fitted before the Z risers. Shim at the arm joints for Z squareness. Arms are not priced |
| Z stack | Unchanged in front of the plate (risers 15, rail + block 30, Z plate 20, clamp 60) |
| Feet (G03) | X **310–445** (135 wide, so the 600 rail ends 10 clear), Y 6–280 from the spindle, Z 155–195. 15 step along the whole foot, X 380–445, clears the Y housing and BK12 (168 against 170). Rear limit 280: further back hits the Y motor mount at the far end of travel |
| Beam to foot | **4 × M10 × 30 per foot**, up through the bottom wall into the foot, wrench through **Ø20 access holes in the top wall**. X 345 and 420; Y 190 and 262 from the spindle. Feet onto the Y blocks first, then the beam |
| X motor | Keep the belt fold (D-107): motor **behind the beam**, axis 137.5 behind the screw (375 belt), Z 374, body pointing inboard. Bracket on the beam end and rear face |
| Y carriages | Stay **140** behind the spindle so the tub does not change. Centre of mass will be further back: compute it and report the offset |
| Rail holes | Drill and tap M5 through the 8 mm wall, using the rail as the template, before the pour. Waxed bolts in the holes during the pour. M5 × 20 gives about 7 mm of thread: check |

**Levelling order (proposal):** top face first, free-surface pour with the beam level. After cure, turn the beam over and rest the cured seat on 3 equal pads on the levelled tub rail seats, then pour the bottom face so the two seats come out parallel. The aluminium front plate needs no pour. Check parallelism with an indicator.

**To check when scripted:** clashes at the X, Y and Z travel ends; moving mass with the 31.7 kg beam; flat width from a real source; bolt and hole spacing in the feet.

**Questions for the owner (with picks):** aluminium 3-piece saddle (pick) or steel; X motor behind the beam (pick) or above it; M10 access-hole joint (pick) or welded end plates.

**Note:** `cad/v2/Facebutton v2 frame.step` is untracked, single part named "facebutton", about 491 × 418 × 1000. Not used here and not committed: ask the owner what it is.

**Exact next step:** write `cad/v2/steel_gantry_sketch.py` from the table above (read `cad/v2/out/gantry_sketch.json` for the tub; do not import `gantry_sketch.py`, it rewrites its outputs). Output a PNG with a section through the saddle, a front view and a beam top view, box clash checks, and a one-page `docs/steel-gantry-sketch.md` with the questions. Then the owner agrees it and starts the gantry in Fusion. The owner can model the tub and Y axis now, and prices the tube (Dyfed Steels first).

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

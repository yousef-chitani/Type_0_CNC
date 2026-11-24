# Type 0 CNC: handover (2026-11-24)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 24 Nov 2026 (22nd session): ATC front carrier becomes laser-cut and bent 5754 sheet on 8 standoffs (D-303); modelled, not saved
- **Owner:** the solid 6082 carrier (2.8 kg) is "too large and substantial, make it from a laser cut and bended sheet material". Q&A: aluminium 5754 3 mm; tabs tapped M4 ("I'll just tap them"); bought standoffs to the hub.
- **Model:** `Front carrier 5754 3 mm sheet (D-303)` (base feature in `ATC Hub`): 12-gon disc Y -154 to -151 with 12 tabs bent +Y (inside R 3), tab outer face at apothem 142 (same fork seat), tab end Y -123.2 (fork step contact kept), tab 70 wide, tapped M4 (Ø3.3) at Y -132.25; Ø40 centre hole (key access to the hub-to-stub screws); 8 x Ø4.5 at r 41.75; 12 spokes 20 wide, 12 windows r 56 to 122, R 4 corners. **512 g** (was 2.8 kg). Old carrier removed (Remove feature). Fasteners (`Sheet carrier standoffs and screws (D-303)`): 12 x M4 x 8 countersunk fork to tab, 8 x M4 x 70 hex 7 AF male-female steel standoffs (stud into the hub's old M4 holes, 10 deep), 8 x M4 x 8 button head ISO 7380 at the front. The 20 old screws removed (Remove features).
- **Checks:** clash of carrier, forks, holders, tools, hub, new fasteners: only screws/studs in their holes and the fork step face (0.01 mm). Front envelope now Y -156.2 (button heads; was -153). Timeline 2195, 37 unhealthy (unchanged).
- **Stiffness (hand estimate, not simulated):** holder weight alone moves a groove about 0.05 mm. A radial push at the pickup fork (tool release or pull-off) goes out along a 3 mm tab and disc: roughly **1 to 3 mm at the groove per 100 N** (the 10 mm 6082 disc was about 30 x stiffer). Bend tolerance ±1 deg tilts a fork about ±1.1 mm radially at the groove (63 mm from the bend). The release force of the Jianken spindle is not known.
- **Not done:** standoff not confirmed in stock (accu.co.uk 403, RS no answer to curl); no flat pattern/DXF (body is solid-modelled, not a Fusion sheet-metal body).

**Left:** owner decides the pickup stiffness fix (options in D-303: a fixed stop under the pickup fork, solid disc without windows, or thicker 5083), and whether ±1 deg bends are acceptable or the tabs get a shim/adjustment; flat pattern DXF for the laser service; standoff stock and price (owner's browser); then task 6 (sweep) as in the entry below.

**Exact next step:** the owner saves `Type_0_v3` and answers the stiffness question (D-303). Then a new session applies the answer, makes the flat pattern, and runs plan task 6.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 24 Nov 2026 (21st session): ATC wheel vertical, 12 radial pockets, column one block (D-302); modelled, not saved
- **Owner moved the ATC** (90 deg about X: axis along Y, wheel in front of the tub, drive under the tub front). Q&A: top pickup with radial holders; lower 6; column top plate + motor plate one part joined by a -X cheek and a floor; angle gone; 12 pockets; bench pocket under the tub; drive torque "will sort later".
- **Model:** ATC 6 lower (centre X 200, Z -40). `Column block 6082 (D-302)`: front plate Y -48 to -37, ear to the strip (2 x M6 x 20 at X 185/215, Z 21), -X cheek, floor Z -75 to -67, motor plate Y 8 to 16, nothing above Z -17 under the tub; FK12, coupling, motor, sensor unchanged. Old angle, top and motor plates removed (Remove features); base L and its fixings deleted. 12 forks (owner model turned: plate perpendicular to the radius, mouth +Y), groove r 142 at Y -85, fork top Z 107 at the pickup; 12 holders and tools pointing in (tips r 56). `Front carrier 6082 (D-302)` in `ATC Hub`: disc, 12-flat drum (apothem 142) the fork tabs screw onto (M4 x 12 csk, radial), Ø40 boss, Ø96 flange on the old hub with 8 x M4 x 12 in the old fork holes. Hub, flag, stub shaft unchanged.
- **Checks:** clash of all ATC bodies and the tub: only screws in tapped holes, the sensor in its M12, the fork step contact. Timeline 2171, 37 unhealthy (old). Envelope X -22 to 396, Z -236 to 156.
- **Lesson:** deleting a body made by a base feature deletes the whole base feature (the sensor grub went with the base L fixings; remade). Use Remove features.

**Left:** drive torque (A03 0.8 Nm holding against about 0.65 Nm per holder, 2.5 Nm worst, and power-off swing; owner to decide: worm box, planetary, bigger motor); carrier 2.8 kg solid, lighten; bench pocket and wheel space (bench docs); spindle sweep at nose Z 112 vs holders at ±30 deg (task 6); docs `docs/atc-wheel.md` and BOM (task 7, D-295 to D-297).

**Exact next step:** the owner saves `Type_0_v3`. Then a new session reads this entry and D-302 and runs plan task 6 (sweep method in `docs/atc-wheel.md`) at the new pickup: X 200, Y -85, nose Z 112, slide to Y -55.

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

# Type 0 CNC: handover (2026-11-24)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 24 Nov 2026 (24th session): V4 started: fixed gantry, moving table (D-305 to D-307); design doc written, not approved
- **Why:** outside feedback on v3: the front ATC wheel is in the way; rails want machinable faces; a hollow beam rings; tools better outside the frame on an extended gantry.
- **Owner (Q&A):** fixed gantry, table moves in Y on rails on top of the base; base bolted aluminium extrusion with voids filled with EG; steel SHS 120 x 120 x 8 beam; steel uprights bolted to the base sides; v3's indexing wheel outside the frame on the right (+X), one pickup (about +200 mm X); enclosure goes round the wheel.
- **Carried over (Claude's proposal, not objected to):** 400 x 250 x 150, Jianken ATC spindle, LiMo C5 1605 + HGR20, LinuxCNC/Mesa, £4,200, wave 1 on 4 Jan 2027 with lengths redone. Dropped: cast tub, moulds, Y2, front ATC.
- **Doc:** `docs/superpowers/specs/2026-11-24-v4-fixed-gantry-design.md` (builder check done; its 4 questions answered or marked as Claude's calls).

- **Owner approved the doc** ("ignore mass keep budget write plan"): no mass limit; £4,200 kept. **Plan written:** `docs/superpowers/plans/2026-11-24-v4-fixed-gantry.md`, 7 tasks: sizing script, owner picks profiles and prices, BOM and budget, then the new Fusion model `Type_0_v4` (base and Y, uprights and X/Z, wheel), pour plan and wave 1 lengths.

- **Plan run, subagent-driven (owner's choice).** Task 1 done and reviewed: `tools/v4_sizes.py`, `docs/v4-sizes.md` (X travel 630, X rail 850, X screw 900 (whips about 2,460 rpm, 12 m/min), Y rail 500, Y screw 600, Z 350, beam 890, base 670 x 660). Wheel pickup offset 85 is provisional: the wheel is about 392 across, so its plane (Task 6) may push X out. Task 2: `tools/v4_frame_stiffness.py`, `docs/v4-frame-options.md`, `docs/price-check-v4.md` (KJN Aluminium Profile, new vendor); owner chose tray B, uprights flat bar 50 x 150, beam full EG fill, ground rail bars (D-308 to D-311). Task 2's figures were not given a separate review; the owner read the options. SDD ledger: `.superpowers/sdd/2026-11-24-v4-fixed-gantry/progress.md` (gitignored, local only).

**Left:** owner's shop grinding price for the 50 x 20 bars; plan Tasks 3 to 7. The wave 1 order lengths must be redone before 4 Jan 2027.

**Exact next step:** a new session runs plan Task 3 (V4 BOM and budget) from `docs/superpowers/plans/2026-11-24-v4-fixed-gantry.md`, using D-308 to D-311 and `docs/v4-frame-options.md`.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 24 Nov 2026 (23rd session): ATC carrier becomes a flat 6 mm disc on a longer hub, clips kept, column floor removed (D-304); docs only, not modelled
- **Owner:** "ATC needs a better solution than standoffs" and the displacement must leave enough room to engage and disengage the clips. The column block floor "need not really exist". Q&A: "Flat disc on a longer hub", "Keep outlines, cheek full height", "clips, the force is not going to be an issue". A fixed fence behind the holders (no clips) was drawn for the owner and declined.
- **No Fusion connection this session**, so nothing was modelled. `Type_0_v3` still has the D-303 carrier and the column floor.
- **Check** (`tools/atc_carrier_stiffness.py`, hand estimate): a push along Y at the pickup fork, per 100 N: D-303 about 9.4 mm (3 mm disc 7.0, FK12 tilt 2.0, stub 0.35, standoffs under 0.01). Flat 6 mm disc on the hub: about 2.6 mm, now mostly the FK12 tilt (range 0.7 to 4.0; its stiffness is not published). Engage: the Y stop leaves 3 past the pickup, so the give at the snap force must be less than the clip's throat-to-seat distance and under 3. With 1 mm allowed, the clip limit is about 40 N (23 to 85 N). Disengage: 30 stroke, ample.
- **D-304 (to model):** disc 5083 6 mm flat at Y -118 to -112, apothem about 150, Ø40 centre hole, 8 x M4 at r 41.75 into the hub; hub 31 longer forward (inside r 51), deeper counterbores for the hub-to-stub screws; forks get a foot on the disc's rear face (2 x M4 axial), clip mouth at Y -85 as now; standoffs, 16 standoff screws, 12 fork-to-tab screws and the bent carrier removed. Column block: floor Z -75 to -67 removed, outlines kept, cheek full height.

**Left:** model D-304 (Remove features, not body deletes; lesson in the 21st entry, now in `docs/handover-archive.md`); check the disc rear face against the real ISO20 holder flange; the owner's clip shape (arm spread against the neighbours at 30 deg); clash check; flat pattern no longer needed (flat disc: a DXF of the outline). Bench: FK12 tilt (50 N along Y at a fork, dial at the rim). Then task 6 (sweep).

**Exact next step:** the owner saves `Type_0_v3`. Then a session with the Fusion MCP reads this entry and D-304, models it, runs the clash check, and runs plan task 6.


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

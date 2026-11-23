# Type 0 CNC: handover (2026-11-23)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (14th session): ATC mount faults fixed (D-292, D-293); real motor in, 2-wall mount (D-294); sweep clean
- Owner Q&A: sensor held in a tapped web (D-292); flag fix as proposed (D-293). D-291 carried out.
- Modelled in `Type_0_v3`, **not saved** (17 features, all healthy; the 35 broken timeline items are older): motor pocket Ø62 cut through the arm (Z -10 to 81), motor goes in from below; Z 0 flange holes, strip holes and tub cores filled, 2 M6 x 20 removed; web top recessed Z 115 to 119 (r 30 to edge), boss Z 118.5, hub underside relieved 0.5 (r 11.5 to 17); sensor hole Ø11 + cosmetic M12 x 1, M4 hole + cosmetic thread from the web edge, M4 x 8 grub body. Mount now 675 cm³.
- **Sweep check found 4 leftover old parts:** 2 x M10 x 30 and 2 x M10 nuts of the old KFL004 (component `Joint screws added (D-262)`), through the hub and forks: removed. After that the sweep (hub, forks, screws, holders 0 to 45°; flag and hub grub 0 to 360°) against all static bodies nearby: no hits. Static overlaps only screws in tapped holes.
- **Real motor (owner sent the 17HS24-2004D-E1K PDF and STEP, kit 1-CL42T-S08-V41, £39.43):** files in `cad/vendor/`, STEP imported into `ATC Drive`, placed by a Move feature (body Z 1 to 81, shaft to Z 105, boss at +X), stand-in removed. It showed a cable boss that could not pass the Ø62 pocket, cables leaving upwards, and a shaft flat only at Z 90 to 105. **D-294 (owner):** round cup replaced by 2 flat walls at ±Y (open at ±X, cables out at +X), arm end squared, rectangular arm pocket with a boss notch; hub grub moved to Z 100 at 22.5° onto the shaft flat, reached through a Ø5 hole in the web and the spacer. Mount 661 cm³, one body. Sweep re-run: no hits.
- Docs: `atc-wheel.md` (faults marked fixed, table, sweep section, assembly order, new view `atc-wheel-under.png`, re-rendered `atc-wheel.png`), `decisions.md` D-291 note, D-292, D-293; BOM A06, A09; `cast_in_features.md` strip row. For D-294: `atc-wheel.md`, D-294, BOM A03, A06, A07, `cad/vendor/README.md`, both renders.

**Left:** owner saves `Type_0_v3` (the ATC can now be confirmed by the owner). Still open: retaining ring under the lower bearing (only the M4 grub holds the wheel down); motor runout (measure when it arrives); cable route along the arm to the tub not drawn; arm stiffness hand calc; price A06 and A07 (curl); spindle-against-wheel check not re-run (wheel did not move); front slot against the ATC keep-out (task 24 item 6); the strip on the mould drawing.

**Exact next step:** the owner saves `Type_0_v3`; then a session settles the front slot against the ATC keep-out (task 24 item 6), or solves the lower-bearing retention (a shoulder on the spigot under the lower bearing, or a circlip groove with a larger pilot).

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026 (13th session): ATC one-piece mount, 40 lower (D-289, D-290), modelled
- Owner: "the mount should be 1 continuous part; the ATC assembly can be made much more compact and shorter". Q&A: machined 6082, wheel about 40 lower, rigid motor joint kept, 2 bearings in the mount, mill first with JLC as fallback. Design approved: `docs/superpowers/specs/2026-11-23-atc-one-piece-mount-design.md`; plan in `docs/superpowers/plans/`.
- **D-290:** bearings 2 x 6804 (the 6004 bore cut the motor screw holes).
- Modelled in `Type_0_v3`, **not saved**: old bracket, posts, top plate, KFL004, collar, shaft and their screws removed (Remove features); wheel parts and sensor down 40, motor up 13 (Move features); one-piece mount (base feature, 766 cm³); hub spigot joined to the hub; 2 x 6804 and spacer; 4 x M6 x 20, 4 x M3 x 12, M4 grub. Tub: strip 80 x 10 x 50 with 4 x M6, new cores, old cores filled, old strip removed.
- Overlap check in one pose clean, **but 4 faults found after** (listed at the top of `docs/atc-wheel.md`, with fixes): motor cannot be fitted (pocket closed), lower flange screws buried (owner, D-291: "2 is plenty", keep the Z 30 pair), flag hits the web as the hub turns, sensor nut does not fit by the cup. No retaining ring room under the lower bearing. `atc-wheel.md` rewritten, new render. BOM A03, A06, A07 text updated (A06, A07 need re-pricing); `cast_in_features.md` strip row updated.

**Left:** do NOT confirm or save the ATC as final yet (saving the rest is fine). Fix the 4 faults in the model and re-check (hub, flag and forks swept against static bodies; assembly order). Then: measure the real motor (length, runout); arm stiffness hand calc; price A06 and A07 (curl); front slot against the ATC keep-out (task 24 item 6); the strip on the mould drawing.

**Exact next step:** a session fixes the 4 ATC mount faults in `Type_0_v3` as listed at the top of `docs/atc-wheel.md` (pocket through the arm, drop the Z 0 screws per D-291, web recess and hub relief for the flag, sensor fixing), re-runs the checks including the turning hub, then the owner saves.

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

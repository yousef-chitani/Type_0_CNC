# Type 0 CNC: handover (2026-11-18)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000. 18 Nov 2026: Z plate stiffness checked, Z assembly modelled (D-202 to D-204)

**Done:**
- **Z plate stiffness (D-202).** 6082 x 20 stays. At 200 N, plate bending moves the tool 0.4 to 2.2 µm with the nose at Z 100 and up to 3.5 to 10.9 µm at Z 250. Roller flex is not included. See `docs/z-plate-stiffness.md` and `tools/z_plate_stiffness.py`.
- **Z assembly in `Type_0_v3`.** New component `Z Axis Assembly`, with `Z Fixed Parts` joined rigidly to `Z Fixed Plate` and `Z Moving Parts` on the slider `Z Travel Slider` (±75, nose Z 100 to 250, shown at Z 175). Vendor blocks, nut and BK12. Rails, screw and motor are simple solids. The BK12 bracket, motor mount, nut housing, clamp and spindle are stand-ins. The spindle body is the Jianken stand-in (D-203), and its length is not confirmed. The fixed plate body is now aluminium, 2.81 kg. The timeline is 1348, with the same 1 error and 5 warnings. **The document is modified and not saved. The owner saves it.**
- **Jianken quote recorded.** $1,200 + $260 DDP = $1,460, 0.87 Nm, PNP 24 V, about 8 kg. `price_gbp` for S01 is unchanged until VAT is confirmed. Reply draft: `docs/supplier-messages.md` section 7, not sent.
- **Casting way up decided (D-204).** Upside down, rail face on the mould floor.

**Left:**
1. **Nut flange clash, owner to decide.** The Ø48 flange overlaps the moving plate by 4 (centre 20 from the plate, radius 24), over the whole travel. Options: a relief pocket in the moving plate, or flats on the flange if the seller confirms them (40 across flats is unverified). On the other side the flange clears the fixed plate by only 1.
2. **Moving plate width, owner to confirm.** Modelled 150 wide. The 140 in `docs/bom.csv` (M12) would break the outer M5 block holes through the plate edge (hole centre at 68, edge at 70). M12 is not changed yet.
3. **Mould assembly (D-204).** Not started. Task files 10 and 11 describe the old portal and base, not the tub.
4. **Jianken reply.** Owner sends it: import VAT and the pull stud and dimension drawings. S06 holders depend on the pull stud.
5. **Machine height.** The Z motor top is at Z 758. Check it against the enclosure.
6. **Clash check notes.** Over the full travel the only real clash is item 1. The block and rail overlap comes from the simplified rail, which has no grooves. The small screw and BK12 overlap is at the lock nut thread.
7. **Z motor mount (task 14).** Still a stand-in, waiting for the seller's drawing.
8. **Top roller screw strength.** They thread into only 3 of tube wall: check this. Roller flex adds to the stiffness figures.
9. **Strip casting details.** Anchor screws, thread plugs and the mould fixing are not modelled. The 10 of EG between a strip and the bar pocket needs the fine mix (D-118), and it has not been proved by a cut test piece.
10. **Machine width.** The brackets reach X -417 to 502.5; the chain side was 487.5. Check this against the enclosure and bench.
11. **Spacer print files.** The 3 spacers are modelled but have no print file yet.
12. **Not modelled:** the tapped riser bolt holes in the steel bars and levelling layer, table fixing holes, machine feet and pads.
13. **Amazon delivery.** X11, X12 and X14 are free to deliver only on orders over £35. The three packs come to £20.47, and the charge below £35 is not known. X14 showed only 7 left.

**Exact next step:** the owner saves `Type_0_v3` and answers items 1 and 2. Then, in a new session, model the EG tub mould upside down in Fusion (D-204).

## 00000000000000000000000000000000000000000000000. 18 Nov 2026: riser bolts set in the model (D-199, D-201)

**Done:** in `Type_0_v3` the 14 riser bolts now have their chosen lengths. 8 are M6 x 25 (Y -6 and Y 561), with tips at Z 112. 6 are M6 x 35 (Y -23 and Y 629), with tips at Z 114. The heads did not move and the tips keep their 0.4 chamfer. The bolt components are renamed `M6x25 and M6x35 Riser Bolts` and its mirror, and each body is named by length and position. `M6x12 (7)` is now `M6x30 Y2 Roller` and `M6x12 (8)` is now `M6x30 Y Roller`. The 3 spacers are in `docs/printed-parts.md`. Measured: the bolts overlap only the steel bar and the levelling layer, with 8 and 6 of thread in the bar, and no longer reach the EG. The timeline is 1324, up from 1304, with the same 1 error and 5 warnings. **The document is modified and not saved. The owner saves it.**

**Left:**
1. **Strip casting details.** Anchor screws, thread plugs and the mould fixing are not modelled. The 10 of EG between a strip and the bar pocket needs the fine mix (D-118), and it has not been proved by a cut test piece.
2. **Machine width.** The brackets reach X -417 to 502.5; the chain side was 487.5. Check this against the enclosure and bench.
3. **Spacer print files.** The 3 spacers are modelled but have no print file yet.
4. **Not modelled:** the tapped riser bolt holes in the steel bars and levelling layer, table fixing holes, machine feet and pads, mould details.
5. **Z plate stiffness** (D-184).
6. **Top roller screw strength.** They thread into only 3 of tube wall: check this.
7. **Amazon delivery.** X11, X12 and X14 are free to deliver only on orders over £35. The three packs come to £20.47, and the charge below £35 is not known. X14 showed only 7 left.
8. **Z risers and rails.** 15 risers and HGR20 rails on the plate, then the blocks, moving plate, screw and motor.

**Exact next step:** the owner saves `Type_0_v3`. Then, in a new session, check the Z plate stiffness (D-184).

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

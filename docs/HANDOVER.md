# Type 0 CNC: handover (2026-11-19)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000. 23 Nov 2026: BK12 riser holes and NEMA 24 plate motor holes redrawn as tapped (D-263); model saved
- Owner (Q&A): all 4 BK12 holes per riser tapped, not only the X ±373 pair (the X ±327 pair hold PrintNC's M6 x 50, ending at Z 136); 22 deep; plate holes M5 through.
- `Type_0_v3`, Y and Y2 BKHM12 risers: 4 holes each tapped M6, drill 5.0 x 22 (Z 155 to 133), cosmetic thread. 3 NEMA 24 plates: 4 motor holes each tapped M5, drill 4.2 through, cosmetic thread. Each old hole had a square void inside (PrintNC STEP artefact); plugged by base feature + combine-join, re-cut by base feature + combine-cut (the hole and extrude commands found no target body in these parts). Outlines and volumes checked.
- Clash check (visible bodies, these 5 parts): only screw threads in the new holes; no screw reaches a hole bottom. Timeline 35 unhealthy before and after. **Saved.**

**Left:** the 3 holes Claude could not place and the X 1610 fill and nut plates (`docs/cad-cleanup-owner-items.md` sections 2 and 3). X21 and X18 pricing. The X BKHM12 riser was not in this task (its BK12 holes not checked). From before: ATC clash check with the moving Z, A06 re-pricing, motor length, fork screw M3 or M4, plate flatness spec, mould drawing, mass.

**Exact next step:** owner answers sections 2 and 3 of `docs/cad-cleanup-owner-items.md`. Then the LiMo basket and Dyfed call (`docs/price-check-task-17.md`).

## 0000000000000000000000000000000000000000000000000000000000000000000000000000000. 22 Nov 2026 (5th session): missing joint screws modelled (D-262); model saved
- Owner: "Yes, model them" (the joints listed in `docs/cad-cleanup-owner-items.md` section 1).
- `Type_0_v3`: new top-level component `Joint screws added (D-262)` (one base feature): 112 screws + 2 M10 nuts. Axes snapped to the exact hole centres; heads on the counterbore floors found by ray. Sizes and counts in D-262. Clash check: only threads in tapped holes and the known 0.03 rail seat. Timeline 35 unhealthy before and after. **Saved.**
- BOM: new line X21 (M6 x 40, M5 x 16, M5 x 6, M6 x 45, not priced); the rest fall under X03, X11, X14, X18, X19, A06.

**Left:** riser holes for the BK12 screws drawn Ø6.1 (tap M6) and the NEMA 24 plate motor holes drawn Ø5.0 (tap M5): change the hole drawings or the screws. The 3 holes Claude could not place and the X 1610 fill and nut plates (`docs/cad-cleanup-owner-items.md` sections 2 and 3). X21 and X18 pricing. From before: ATC clash check with the moving Z, A06 re-pricing, motor length, fork screw M3 or M4, plate flatness spec, mould drawing, mass.

**Exact next step (owner said "Yes, redraw them", 22 Nov):** new session redraws as tapped holes in `Type_0_v3`: the 2 BK12 screw holes in each of the Y and Y2 BKHM12 risers (X ±373, Y 579 and 592, now Ø6.1 through: tap M6, about 15 deep from the top, Z 155 down; the M6 x 40 ends at Z 146) and the 4 motor holes in each of the 3 NEMA 24 plates (now Ø5.0: tap M5, drill 4.2). Edit the hole features in the riser and plate components (or delete-face and re-cut), check health stays 35, re-run the clash check of `Joint screws added (D-262)`, record D-263, save. Then owner answers sections 2 and 3 of `docs/cad-cleanup-owner-items.md`. Then the LiMo basket and Dyfed call (`docs/price-check-task-17.md`).

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

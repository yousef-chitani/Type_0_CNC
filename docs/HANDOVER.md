# Type 0 CNC: handover (2026-11-25)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

> **Older entries and sections 1-4, 6 and 7 are in `docs/handover-archive.md`.** Read it only if a task needs the history. Keep the two newest entries here.

## 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 25 Nov 2026 (30th session): X motor bracket dropped, X motor on a second HM12-60 (D-320); price check 18 retried; Phase 1 £4,479.10
- **Owner:** "X motor bracket 10 (envelope: beam end plate and EG dam X-, foot, motor plate): this part is silly, just use an integrated mount dont do this bracket nonsense on X. do the rest of the price check". Q&A: "Bought BK12 motor seat", "Yes, HM12-60 as Z", "Plain steel cap plate".
- **D-320 (BOM and docs only; the model is not changed):** a second LiMo HM12-60-V (as Z) is the X motor mount and fixed bearing, replacing the X BK12 and the bracket. Foot 60 x 95, centre height 25 (as the BK12): the screw axis stays at Z 325. X screw ordered with the Z-style 10 x 21.5 end (M05); the X BK12 is unused (M06). Both beam ends get a 120 x 120 x 5 steel cap as the EG dam: **new G12**, K I Metals 120 x 5 flat bar, £3.34 inc. **M13 x 2: £26.06.** Wave 1 £1,982.05 (schedule updated).
- **Price check 18 retried by curl:** Aluminium Warehouse still 429 (A06, M12); StepperOnline captcha (A03, M09), not passed; Simply Bearings answers but has **no SHF12** (A10); Ooznest 403. Nothing else in the list is curl-priceable. Results: `docs/price-check-task-18.md`, "second pass".
- **Phase 1 £4,479.10 (+£16.37), £279.10 over budget.**
- **Open for the model (Type_0_v4, still not saved):** replace `X motor bracket 10` and the BK12 with the HM12-60 (owner CAD as on Z); the X- pad is 50 x 80, the foot 60 x 95 (pad size and the G11 length); the mount position along X (bearing end on the screw shoulder, motor overhang past X -350); 2 cap plates at the beam ends. The NEMA 24 (60 square) on the 25 centre height hangs about 5 below the foot plane, so the motor flange must sit past the pad and the beam end (X -350): that fixes the mount's X position and the bearing shoulder on the 900 screw. HM12 holes 49.5 vs motor 50, and its 7001 bearing is C7 not C5 (both as Z; the owner turned the HM12 down for Y for these reasons, D-151).
- **Exact next step:** the owner saves `Type_0_v4`, adds the second HM12-60 and the X screw end to the LiMo basket, and prices the browser-only lines (owner-todo). Then a session models D-320 in `Type_0_v4` and D-317 fault 2, then plan Task 7.

## 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000. 25 Nov 2026 (29th session): price check 18 by curl: screws at Westfield Fasteners, K I Metals confirmed; Phase 1 £4,462.73
- **Done:** `docs/price-check-task-18.md` has a Results section. Screws priced at **Westfield Fasteners** (new vendor; its own price calculator answers curl; free UK delivery over £40 ex VAT, else £3.50): X20 £5.06, F27 £12.83 (with washers), G09 £11.41, X23 £11.39 (with 16 KJN T-nuts), G08 £5.96 (A1 stainless dowels, accepted by the owner, D-319). A Phase 1-only Westfield order is under £40 ex: £3.50 delivery, not in the total. ATC screws priced in the notes of A06, A09, A10 (Phase 2). K I Metals pages confirm F26 and G11 (and show drilling at £4 to £9 a hole). `bom.csv` updated, generators run. **Phase 1 £4,462.73 (+£46.65), £262.73 over budget.**
- **Flags for the owner:** Westfield is a new vendor. F27, G09, X23 and the ATC M8 lengths are Claude's proposals (M16 x 40, M12 x 60 / 35, M8 x 30): confirm from the model.
- **Blocked:** Aluminium Warehouse and Simply Bearings rate-limited (429) (A06, M12, A10 SHF12); StepperOnline bot check after one page (A03: 17HS16-2004S1 read at $9.13, driver not priced; M09); LiMo 403 (M05); AliExpress lines for the owner's browser. X18, X21 wait for the screw lists from the V4 model; F28 for a material; F30, G10, X25 for shop quotes.
- **Next step:** retry Aluminium Warehouse (`/products/<handle>.js`) and Simply Bearings (`/search/suggest.json?q=SHF12`) slowly by curl; then owner prices the browser-only lines. Model `Type_0_v4` still not saved (task 27, Task 7 next).

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

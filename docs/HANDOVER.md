# Type 0 CNC: handover (2026-11-09)

**Branch:** `claude/charming-cori-349jm7` on `yousef-chitani/Type_0_CNC`. Everything below is committed and pushed. Earlier work: `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

## 1. What the project is
A DIY 3-axis **fixed-gantry, moving-table** CNC mill with a **cast epoxy-granite (EG) frame**, **LinuxCNC + Mesa 7I76EU**, closed-loop NEMA 24 steppers, and (Phase 2) a **Jianken ISO20 ATC spindle** with an 8-pocket ferris-wheel tool changer. Inspiration: Bootstrap Bill. The owner is in **Swansea, UK**, builds in a **shed**, and must later move it into an **upstairs flat**: pieces ≤ about 40 kg (the base is a 2-person lift).

## 2. Current design (full assembly, D-102 … D-120)
The detailed design now lives in **`cad/v2/assembly.py`** (parametric CadQuery, vendor STEP models swapped in) → `cad/v2/out/assembly/`. Read **`docs/assembly.md`** first; `cad/v2/out/assembly/cast_in_features.md` lists every cast-in feature.

- **Work area 400 × 250, Z 150.** Travel X 570 (incl. reach to the ATC wheel) / Y 250 / Z 150. Table 460 × 330 × 25 (6082). Spindle axis at Y −65 (175 mm in front of the beam face).
- **Castings (2):**
  - **Base:** T-shape, spine **340** × 725, rear cross-piece 640 × 230, 110 high, 45° tapers 100 × 100 at the T-junction. **80.2 kg**. Sits on 3 steel pads on the bench (D-119). Cast upside down (top face on the mould floor = jig).
  - **Portal:** 800 wide, beam **150** × 130, legs 70 × 130, 375 tall, 45° haunches 60 × 60 at the leg/beam corners, 2 × Ø40 PVC cores in the beam with every wall ≥ 20 mm (D-114). **37.6 kg**. Cast lying on its front (rail) face; the back is the open pour face (so no leg flare, D-113).
  - Joint: 2 × M12 rod per leg through cast tubes into **40 × 20** tapped bars in the base (D-116), grouted, dowel reamed after.
  - Inserts: steel flat bar under the rails (40 × 10 for Y, 25 × 10 for X), tapped M5, 5 mm under a levelling-pour recess that is open to the casting edges (D-115).
  - **Resin (D-117, D-122):** Gurit Ampreg 30 + 3X Slow, one 22.68 kg kit, for castings, rail seats and grout; cure at 18 °C or more, post-cure 16 h at 50 °C (Tg 74 °C). GlassCast 50 PLUS is dropped.
  - **Compaction (D-123):** hand tamping in layers; a vibration motor only if the test bricks show voids.
- **Motion:**
  - HGR20 rails: X 2 × 800, **100 apart** on the beam face; Y 2 × 500, 280 apart; Z 2 × 350, 100 apart on 15 mm risers on a tall saddle.
  - Ballscrews DFU1605: needed overall X 823 / Y 582, so buy **X 850 / Y 600 / Z 350**.
  - BK12/BF12 supports; DSG16H nut housings; X housing on a 25 mm spacer in a 45 mm deep X channel.
- **Drives:** X and Y **folded with 1:1 HTD-5M belts** (Y motor alongside the spine under the table; X motor on the beam top with an outboard KFL000 bearing). **Z direct** on top (motor with brake). Motor hole spacing is **50 mm**, not 47.1.
- **Plates:** saddle 180 × 400 × 20, Z plate 140 × 200 × 20, plus spacer, risers and motor plates.
- **Spindle (Phase 1):** G-Penny 2.2 kW ER20 water-cooled kit (Huanyang VFD on **USB-RS485 + hy_vfd**). DIY cooling loop.
- **Enclosure (Phase 2):** 12 mm MDF, sized from the assembly: **932 × 836 × 898** outside. `cad/v2/enclosure.py`.
- **Bench:** owner-built knock-down timber bench, top 1000 × 1000 at 785 mm, joists under the spine edges, cabinet + cooling loop inside. `cad/v2/bench.py` → `cad/v2/out/bench_cutlist.md`.
- **Electrics / control:** `docs/electrical.md` (Z brake hardwired through the safety relay, D-93), `linuxcnc/type0/` + `docs/linuxcnc.md` (simulator-tested 23/23).
- **3D printing:** owner has 3 × Bambu P1S; printed parts in **PETG** (`docs/printed-parts.md`, `cad/v2/printed_parts.py`).

## 3. Money and phases
| Phase | Scope | Priced | Budget |
|---|---|---|---|
| 1 | Working mill, manual ER20 tool changes | **£3,327.57, provisional**: M15–M17 are not priced, M05, F07, M12, M13 changed size (**price check 12** pending, `docs/price-check-task-12.md`), and the Ampreg 30 delivery cost is not known | £4,000 |
| 2 | ATC spindle + holders, air, mist, enclosure, tool wheel | about £1,400 (not re-checked) | not set |

- Source of truth: **`docs/bom.csv`**. After editing it, regenerate everything: `python tools/gen_bom_md.py`, `python tools/gen_phase1_xlsx.py`, `python tools/gen_phase1_cost.py`, `python tools/build_open_links.py`.
- Order waves (`docs/phase1-schedule.md`): **1** (4 Jan) electrics, motors, spindle kit, cooling loop; **2** (15 Feb) bench, moulds, local items and the **motion parts** (D-103); **3** (1 Mar) casting materials; **4** (29 Mar) aluminium plates, collets.

## 4. Schedule
4 Jan → 22 Jul 2027, about 5 h/week. Done = the machine moves under LinuxCNC.
- **Before Jan:** CAD assembly refined by the owner in Fusion.
- **Jan–Feb:** electrics bench-tested indoors.
- **Early March:** spindle kit bench-tested.
- **March:** moulds, then test bricks.
- **April–May:** castings at 17–23 °C, 7-day cure, in an insulated tent with a thermostat heater.
- **June:** assembly.
- **July:** wiring and LinuxCNC on the machine.

## 5. Owner's rules
- **Use the Q&A tool heavily** before decisions. Ask, don't assume. The owner pushes back on design details: take it seriously and check mouldability and casting orientation (e.g. D-113).
- **Only prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Few vendors; prefer B&Q / Screwfix (local), then RS. Flag swaps costing > 10% or £5 more.
- Supplier sites block this cloud session. Prices and vendor CAD come from the owner's **local browser session** via task files (`docs/price-check-task-N.md`, `docs/cad-download-task.md`). The owner logs in themselves; the session never handles credentials.
- **Cast, not welded.** Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-123**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 6. Tasks
1. ~~Electrical design~~: done (`docs/electrical.md`, D-91, D-93).
2. ~~LinuxCNC config~~: done (`linuxcnc/type0/`, `docs/linuxcnc.md`, D-92).
3. ~~Timber bench~~: done and priced (`cad/v2/out/bench_cutlist.md`, D-97, D-99).
4. **Full CAD assembly: first version done** (D-102 … D-116, vendor models in, no clashes at 3 positions; review changes D-114 … D-116 applied). **Waiting for:**
   - the owner's Fusion pass (brackets, plates, sensor mounts, VERIFY list in `docs/assembly.md`) and the returned STEP. Put it in the repo, e.g. `cad/v2/in/`, and feed changes back into `assembly.py`;
   - price check 12.
5. **Mould drawings** (blocked by 4): from the final assembly and `cast_in_features.md`. Cover:
   - panels and the jig-bolt pattern for the insert bars;
   - channels, sleeves, cores and their suspension;
   - the 3-piece wedge plug for the portal opening;
   - haunch and taper blocks, lifting points;
   - the vibration-table deck;
   - printed mould helpers (F19).
6. **EG mix design + test-brick plan:**
   - Ampreg 30 + 3X Slow (D-122), hand-tamped in layers (D-123), GCL quartz 2–5, H&B sand 0–1, whiting; epoxy at 10 / 11 / 12 / 13%;
   - the review's tests (`review-eg-design-report.md` section 4): cut test beam section with the real cores, 3 release methods, packing test with and without GCL 1–3 mm, joint-bar pull test, 500 mm rail-seat test strip, creep and stiffness prisms;
   - a full-thickness heat brick with a centre probe;
   - curing-heat.md rewritten for Ampreg 30 (18 °C minimum, post-cure 16 h at 50 °C);
   - add a heater and thermostat to the BOM.

**In progress / proposals:**
- **Base PVC cores (not adopted yet):** 5 × Ø50 at Z −65, saving about 9.6 kg; sketch in `cad/v2/out/base_cores_plan.png`, `base_cores_sections.png` (`cad/v2/base_cores_sketch.py`). Suspension: an M8 rod through each capped core, fixed in the mould walls at core height, plus mid-span wire hold-downs from a batten; the rods are cut flush and sealed afterwards (they don't reinforce, D-120). The review found the layout sound (15 mm under the BK/BF plates). Owner to decide (maybe after the FEA, D-81).
- **EG design review: done** (`docs/review-eg-design-report.md`). The owner's decisions on it are D-114 … D-123 (smaller cores, open 5 mm rail-seat recesses, 20 mm joint bars, Ampreg 30 with post-cure, insert preparation, 3-point base support, hand tamping first, doc fixes). Not acted on yet: the review's tests (they go in task 6) and its lower-severity notes (gap grading fallback GCL 1–3 mm, mould deck).

Then: rail-seat levelling and assembly procedures, Phase 2 detailing (ATC wheel, enclosure fittings).

## 7. Open questions
`docs/open-questions.md`, in priority order with who answers each. The most urgent:
1. Price check 12, and the Ampreg 30 delivery cost.
2. Ballscrew "Guide Length" and end machining (message drafted in `docs/supplier-messages.md`).
3. Owner's Fusion pass.
4. Safety relay terminal names.
5. AliExpress basket clean-up before wave 1.

## 8. Key files
| File | What |
|---|---|
| `docs/assembly.md`, `cad/v2/assembly.py`, `cad/v2/out/assembly/` | **Full CAD assembly**: STEP for Fusion, castings, cast-in features, views, data |
| `cad/vendor/` | Manufacturer STEP files (and the Z motor PDF) used by the assembly |
| `docs/decisions.md` | Decision log D-01 … D-113 |
| `docs/open-questions.md` | What's still open, in priority order |
| `docs/electrical.md` | Power, safety chain, 7I76EU pin map, VFD settings |
| `docs/linuxcnc.md`, `linuxcnc/type0/` | LinuxCNC config, simulator, PC set-up, bench tests |
| `cad/v2/bench.py`, `cad/v2/out/bench_*` | Timber bench: drawings, cut list, assembly |
| `cad/v2/enclosure.py`, `cad/v2/out/enclosure_*` | Enclosure (sized from the assembly) |
| `docs/printed-parts.md`, `cad/v2/printed_parts.py`, `cad/v2/out/print/` | Printed parts (PETG) |
| `docs/curing-heat.md`, `tools/cure_heat.py` | Resin limits (still GlassCast below the top notes: to redo for Ampreg 30, D-122), heat estimate, heater tent |
| `tools/portal_overhang.py` | Beam overhang check (D-95; beam is now 150 high, still fine) |
| `docs/eg-moulds.md`, `aggregates.md`, `epoxy-options.md` | Casting notes (partly v1 sizes: use the assembly for sizes) |
| `docs/bom.csv` + generated `bom.md`, `phase1-bom.xlsx`, `phase1-cost.md` | Parts and costs |
| `docs/phase1-schedule.md` | Timeline and order waves |
| `docs/price-check-task-*.md`, `docs/cad-download-task.md`, `docs/supplier-messages.md` | Task files for the owner's local session, message drafts |
| `docs/review-task-eg-design.md`, `docs/review-eg-design-report.md` | EG design review: brief and report |

## 9. Working notes for the next session
- **CadQuery** isn't preinstalled in the cloud container: `pip install cadquery` (about 1 minute). `python cad/v2/assembly.py` takes about 2–3 minutes (vendor STEP import + clash check at 3 positions); `--envelopes` skips the vendor models.
- After changing the assembly, also run `cad/v2/enclosure.py`, `cad/v2/bench.py` and `cad/v2/base_cores_sketch.py` (they read `cad/v2/out/assembly/assembly_data.json` or the assembly numbers), and regenerate `cast_in_features.md` from the `features` list in `assembly_data.json` (one table per casting; no script in the repo).
- **The PNG views in `cad/v2/out/assembly/` were not re-rendered after D-114 … D-116** (the render script isn't in the repo). The STEP files, `cast_in_features.md` and `assembly_data.json` are current.
- **Rendering:** the CadQuery SVG exporter gives rotated views; use the matplotlib tessellation render instead. To view SVG drawings, screenshot them with Playwright (preinstalled).
- `docs/bom.csv` uses **CRLF** line endings and CSV-escaped quotes (`""`): keep both when editing.
- LinuxCNC can be tested in a Debian 12 Docker container (2.9.10 from linuxcnc.org); see `docs/linuxcnc.md` section 4.

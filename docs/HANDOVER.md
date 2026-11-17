# Type 0 CNC: handover (2026-11-17)

**Branch:** `claude/hopeful-sagan-28twty` on `yousef-chitani/Type_0_CNC` (holds everything from `claude/charming-cori-349jm7` plus the 16 and 17 Nov LiMo sessions). Everything below is committed and pushed. Earlier work: `claude/charming-cori-349jm7`, `claude/trusting-shannon-uwrpm9`, `claude/ecstatic-ramanujan-mhh3xe`.

> **Owner: your list is `docs/owner-todo.txt`.** **Sessions: start with `docs/tasks/README.md`.** The work is split into small tasks, one per session, each listing the only files to read. This handover is background.

## 0000. 17 Nov 2026 (late): layout change

- **D-137: moving gantry, fixed table in one cast EG tub** (like Moxer), replacing D-01. Portal casting and joint go. Two Y screws and motors. Tub in one piece, owner accepts about 115–160 kg. Gantry in aluminium, maybe JLC: **sketch first**.
- **D-138: Phase 2 ATC is a Timbre-style umbrella wheel** at a table corner (replaces D-73).
- Checkout 4 recorded ($604.24, basket correct), **but the LiMo order is on hold**: the screw and rail lengths change.
- The Fusion pass (task 09) should pause on the castings and gantry until the sketch is agreed.

**Exact next step:** task 22 (`docs/tasks/22-moving-gantry-redesign.md`) in a fresh session: the sketch.

## 000. Session of 17 Nov 2026 (LiMo prices and checkout)

**Done** (all in `price-check-task-16.md`, last three sections)
- **C5 screw page:** screw + nut only, no supports (superseded).
- **C5 set page:** DFU1605 + steel housing + **C5 BK12/BF12**, lengths in 50 mm steps: 850 $171.57, 600 $141.57, 350 $111.57 = **$424.71** (C7 kits 900/600/400: $152.19). Light preload P2 by default.
- `docs/limo-basket.txt`: basket list for the owner (A = C5, B = C7).
- **Checkout to SA2:** DDP sea $129 (30–45 workdays, max 950 mm), DAP air $239 (tax extra), DDP air $269 (duty included). The owner's saved basket had **2 × 600 mm** and an **HM10-60** (should be 1 × 600 and HM12-60) and no code; corrected in the figures.
- **Whole LiMo order, DDP sea, corrected:**
  - **C5 £487.30** ($644.25: goods after `10OFF` + $129);
  - **C7 £313.13** ($413.98: after `5OFF` + $129);
  - **against £464.41 now** (several sellers).
  - C5 is £22.89 more than now; C7 is £151.28 less.

- **Updated checkout** (owner fixed 1 × 600): **DDP sea $89**, DDP air $209, DAP air $239. Still HM10-60 and no code in it. Corrected: $515.25 + $89 = **£457.05** (without the code: £500.35).
- **D-136 (owner): C5, LiMo, ordered in wave 1 (4 Jan 2027).** `bom.csv` M01–M08 and M13 moved to LiMo, one line per item (all the shipping is on M05). The 5 scripts were re-run. Wave 1 is now £1,927.74 and wave 2 £587.30. **Phase 1: £3,908.22** (was £3,915.58). The wave 1 order sheet has a LiMo section.

- **Checkout 3 (17 Nov, later):** HM12-60 in and **`10OFF` accepted** (10 % of goods, not shipping). But the 600 mm set is × 2 again and DDP sea is $129: as saved $771.65 = £583.67. With 1 × 600 it stays $604.25 = £457.05 (`bom.csv` unchanged).

**Left**
1. ~~Fix the basket~~: **checkout 4 is correct** (1 × 600, HM12-60, `10OFF`, DDP sea $89, total **$604.24**). On 4 Jan: order it with DDP sea. X and Y stub drawings to email with the order number (needs the owner's new CAD, task 09).
2. ~~Is the 10 % code accepted?~~ Yes (checkout 3).
3. The steel nut housing in the C5 set: size and bolt pattern not known (the CAD uses DSG16H). Ask LiMo or check their CAD drawing.
4. LiMo's answer to 6a (rail class, HM12-60 at 50 mm, coupling fit, VAT in DDP): record it under 6a and in `open-questions.md`.
5. After that and the owner's new CAD: X and Y screw end drawings.

**Exact next step:** wait for LiMo's 6a answer and the owner's new CAD; then draw the X and Y screw ends (ask the owner: exact lengths or 850 / 600) so they are ready for the 4 Jan order.

## 00. Session of 16 Nov 2026 (LiMo reply)

**Done**
- LiMo answered message 6 (Amy Jiang): custom end machining from our drawings; light preload, but they advise **C5 ground**; prices from the online store, shipping and dates at checkout. Recorded in `supplier-messages.md` section 6 and `open-questions.md` item 9.
- Reply **6a sent 16 Nov** (rail accuracy class, HM12-60 drilled to 50 mm and cost, D25L35 coupling inside the HM12-60, VAT in the DDP price). Waiting.
- End machining agreed in principle (task 13 notes): LiMo's standard drawing (BK12: Ø10 × 15, M12×1 × 14, Ø12 × 25; BF12: Ø10 × 11 with circlip groove), changing only the **X and Y drive stubs**: longer, Ø10 0/−0.015, one flat 1 mm deep for the pulley and KFL000 grub screws. Z fully standard.
- Owner: lengths stay **X 850 / Y 600** for now; C5 or C7 decided after the C5 price; **no drawings until LiMo answers**.
- **The owner is redoing the CAD** (task 09): the stub and overall lengths come from the new CAD, not the old numbers (X stub about 74, Y about 32 from the thread end; spare 27 / 18 mm goes on the drive stub with 850 / 600).

**Left**
1. **C5 price recorded (17 Nov, `price-check-task-16.md`):** C5 sets (screw, steel housing, C5 BK12/BF12) 850 / 600 / 350 mm = $424.71 vs $152.19 for the C7 kits. Whole LiMo order with C5 by sea: £557.54 (£464.61 if DDP includes VAT) vs £464.41 now and £348.53 LiMo C7. Owner: note the checkout shipping to SA2 (sea and air), then decide C5 or C7 (next D-number: D-136).
2. LiMo's answer to 6a: record it under 6a and in `open-questions.md`.
3. After that and the new CAD: make the X and Y screw drawings (still ask the owner: exact lengths or 850 / 600).

**Exact next step:** superseded by section 000.

## 0. Where the session of 15 Nov (late evening) stopped

**The owner's answers (D-133)**
- `assembly-steps.md` is clear to the owner as written. No simplification of the assembly for now.
- Measuring square (step 8): "choose the one that makes sense". Chosen: an **engineer's square** (300 mm, DIN 875 grade 1 or 2) with the DTI. It's quick and needs no cutting, which matters because it's done after every move.
- Earlier the same day (still current): D-128 re-square after each move; D-129 post-cure and tent stay; D-130 nothing from the Opus branch; D-131 castings keep their features; D-132 portal bolted dry on shims, no grout, no dowels.

**Done and pushed**
- **Task 04 done.** Dowel sleeves removed from `assembly.py` (base 80.3 kg, portal 37.6 kg, no clashes). Re-run: `assembly.py`, `enclosure.py`, `bench.py`, `base_cores_sketch.py`; `cast_in_features.md` regenerated. `render_views.py` and `render_steps.py` were **not** re-run (the holes were under the leg feet, so the pictures don't show them).
- `portal-relocation.md` rewritten to the bolted-dry method, one page. The old grout sketch (`relocation_sketch.py`, `portal_relocation.png`) is deleted.
- Grout piece F dropped from `eg-mix-test-plan.md`.
- `assembly-steps.md`, `open-questions.md`, `phase1-schedule.md` and `assembly.md` updated to match.
- **`docs/price-check-task-15.md`** (engineer's square X10, shim stock X11), partly done with curl. Square found: Mitutoyo 916-227, grade 1, £62.00 ex VAT (£74.40 inc) at MQS, delivery unknown. Shims: only dear ones so far (Cromwell pack £224 ex VAT, RS roll £97.80 ex VAT).

**Later the same evening (D-134)**
- Price check 15 finished by curl: square Mitutoyo 916-227 grade 1 £74.40 inc (MQS); shims Cromwell T&A steel pack 12 × 6 × 12 in, 0.025–0.38 mm, £58.19 inc. The owner finds the UK precision tools too dear and checks **AliExpress** first: the list is at the end of `price-check-task-15.md` (square, shims, **M5 × 20 grade 12.9** rail bolts, optional graded straightedge).
- Task 05: owner chose 12.9 bolts (D-134). Fallback Screwfix A2 1941T, 50 pack £5.89 inc. Not in `bom.csv` yet.

**16 Nov session (D-135)**
- Cooling loop: no radiator or fans, a 20 L bucket reservoir instead (S05 £51.77). Bench re-run (bucket at the back right, PC moved), OUT3 spare in `electrical.md` and the HAL. LinuxCNC simulator not re-run.
- AliExpress reply in `price-check-task-15.md`: square £18.19, shims under £25 (waiting), bolts Screwfix, straightedge KS Tools (price/grade missing). Not in `bom.csv` yet.
- Owner wants rails, ballscrews and accessories from one seller: `docs/motion-parts-one-seller.txt`.

**Task 21 done (15 Nov 2026):** owner gets a LiMo quote (draft: `supplier-messages.md` section 6), including whether the HM12-60 (49.5 mm holes) fits the NEMA 24. limobearing.com blocks curl (403); from the owner's saved page, LiMo DFU1605 C7 kits (BKBF12 + housing) 900/600/400 = $152.19, £200.77–237.07 all-in vs £229.01 (shipping band unknown). Whole LiMo order (screws, rails, HM12-60, coupling) $284.98 after 5 %: £348.53 by sea, £412–467 by air, vs £464.41 now. HL Motion has no DFU1605 (SFU sold out), no pulleys, belts or KFL000; rails £108.83 inc VAT + unknown shipping vs £207.37. Results and draft message in `docs/price-check-task-16.md`. Owner decides; `bom.csv` unchanged.

**Open, in order**
1. **Owner's AliExpress reply** → add X10, X11 and the new X03 (and X05 if swapped) to `bom.csv`, re-run the 4 BOM scripts, update the wave total in `phase1-schedule.md`. That finishes task 05.
2. Task 13: drafts ready, now 5 (section 5 is new: EC Fibreglass, Ampreg delivery to SA2 and shelf life); the owner sends them and the answers go under each message and in `open-questions.md`. Task 15 done: `docs/wave1-order-sheet.md`, generated by `tools/gen_wave1_sheet.py` (one table per vendor, open checks per line, total £1,470.69 = schedule).
3. Task 09 (owner's Fusion pass), then 10, 11 (mould drawings).
4. **Every open task now waits for the owner** (AliExpress reply, the 5 messages, the Fusion pass). Task 14 waits for the Z mount seller's drawing (message 4). Task 17 (tidy the old casting notes) no longer waits: 03 and 06 are on hold (D-131), so a session can do it.

**Warnings for the next session**
- **Ask before deciding** (Q&A tool). Keep answers, documents and procedures short. No grout, glue or other half-measures in joints: either bolted or bonded.
- **Price checks: curl first** (the owner asked: the browser uses many tokens). The notes in `price-check-task-15.md` say which sites curl can read. Do not spoof browser headers to get past a bot block (RS, Amazon): use the browser with one small `get_page_text` instead.
- **Python on Windows:** set `PYTHONUTF8=1` before running the CAD scripts, or `enclosure.py` stops with a `UnicodeEncodeError`.
- **Do not merge `claude/awesome-ramanujan-by9kds`** (old design, clashing D-numbers).
- The CAD still has the 2 × Ø40 portal cores and the ATC insert (both agreed to stay for now, D-131).
- **Git on the owner's PC has no identity set.** Commit with `git -c user.name=Claude -c user.email=noreply@anthropic.com commit ...`; do not change their git config.
- Sections 1–9 are background and partly older; where they disagree, section 0, `decisions.md` and the task files win. Ignore the grout and dowel text in sections 2 and 6.

## 1. What the project is
A DIY 3-axis **fixed-gantry, moving-table** CNC mill with a **cast epoxy-granite (EG) frame**, **LinuxCNC + Mesa 7I76EU**, closed-loop NEMA 24 steppers, and (Phase 2) a **Jianken ISO20 ATC spindle** with an 8-pocket ferris-wheel tool changer. Inspiration: Bootstrap Bill. The owner is in **Swansea, UK**, builds in a **shed**, and must later move it into an **upstairs flat**: pieces ≤ about 40 kg (the base is a 2-person lift).

## 2. Current design (full assembly, D-102 … D-127)
The detailed design now lives in **`cad/v2/assembly.py`** (parametric CadQuery, vendor STEP models swapped in) → `cad/v2/out/assembly/`. Read **`docs/assembly.md`** first; `cad/v2/out/assembly/cast_in_features.md` lists every cast-in feature.

- **Work area 400 × 250, Z 150.** Travel X 570 (incl. reach to the ATC wheel) / Y 250 / Z 150. Table 460 × 330 × 25 (6082). Spindle axis at Y −65 (175 mm in front of the beam face).
- **Castings (2):**
  - **Base:** T-shape, spine **340** × 725, rear cross-piece 640 × 230, 110 high, 45° tapers 100 × 100 at the T-junction. **80.2 kg**. Sits on 3 steel pads on the bench (D-119). Cast upside down (top face on the mould floor = jig).
  - **Portal:** 800 wide, beam **150** × 130, legs 70 × 130, 375 tall, 45° haunches 60 × 60 at the leg/beam corners, 2 × Ø40 PVC cores in the beam with every wall ≥ 20 mm (D-114). **37.6 kg**. Cast lying on its front (rail) face; the back is the open pour face (so no leg flare, D-113).
  - Joint: 2 × M12 rod per leg through cast tubes into **40 × 20** tapped bars in the base (D-116), grouted; no dowels, re-squared after each move (D-128).
  - Inserts: steel flat bar under the rails (40 × 10 for Y, 25 × 10 for X), tapped M5, 5 mm under a levelling-pour recess that is open to the casting edges (D-115).
  - **Resin (D-117, D-122):** Gurit Ampreg 30 + 3X Slow, one 22.68 kg kit, for castings, rail seats and grout; cure at 18 °C or more, post-cure 16 h at 50 °C (Tg 74 °C).
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
| 1 | Working mill, manual ER20 tool changes | **£3,908.22**, every line priced (price checks 12–15 applied, D-126; LiMo C5, D-136). £282 under the budget; not yet in it: delivery for the Ampreg kit and the GCL quartz. M13 (Z motor mount) is provisional | £4,200 (D-127) |
| 2 | ATC spindle + holders, air, mist, enclosure, tool wheel | about £1,400 (not re-checked) | not set |

- Source of truth: **`docs/bom.csv`**. After editing it, regenerate everything: `python tools/gen_bom_md.py`, `python tools/gen_phase1_xlsx.py`, `python tools/gen_phase1_cost.py`, `python tools/build_open_links.py`, `python tools/gen_wave1_sheet.py`.
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
- Write plainly; record every decision in `docs/decisions.md` with a D-number (last: **D-136**).
- Design small low-load parts for printing (PETG) rather than buying (D-100, D-101).
- The owner uses **Fusion 360**; deliver CAD as STEP with named components.

## 6. Tasks
1. ~~Electrical design~~: done (`docs/electrical.md`, D-91, D-93).
2. ~~LinuxCNC config~~: done (`linuxcnc/type0/`, `docs/linuxcnc.md`, D-92).
3. ~~Timber bench~~: done and priced (`cad/v2/out/bench_cutlist.md`, D-97, D-99).
4. **Full CAD assembly: first version done** (D-102 … D-116, vendor models in, no clashes at 3 positions; review changes D-114 … D-116 applied). **Waiting for:**
   - the owner's Fusion pass (brackets, plates, sensor mounts, VERIFY list in `docs/assembly.md`) and the returned STEP. Put it in the repo, e.g. `cad/v2/in/`, and feed changes back into `assembly.py`;
   - the M13 seller's drawing (or make the mount from plate).
5. **Mould drawings** (blocked by 4): from the final assembly and `cast_in_features.md`. Cover:
   - panels and the jig-bolt pattern for the insert bars;
   - channels, sleeves, cores and their suspension;
   - the 3-piece wedge plug for the portal opening;
   - haunch and taper blocks, lifting points;
   - the vibration-table deck;
   - printed mould helpers (F19).
6. **EG mix design + test-brick plan: first draft done** (`docs/eg-mix-test-plan.md`, `docs/curing-heat.md` rewritten for Ampreg 30, D-124). Owner to review the pass marks, quantities and kit list. Covers:
   - Ampreg 30 + 3X Slow (D-122), hand-tamped in layers (D-123), GCL quartz 2–5, H&B sand 0–1, whiting; epoxy at 10 / 11 / 12 / 13%;
   - the review's tests (`review-eg-design-report.md` section 4): cut test beam section with the real cores, 3 release methods, packing test with and without GCL 1–3 mm, joint-bar pull test, 500 mm rail-seat test strip, creep and stiffness prisms;
   - a full-thickness heat brick with a centre probe;
   - curing-heat.md rewritten for Ampreg 30 (18 °C minimum, post-cure 16 h at 50 °C);
   - add a heater and thermostat to the BOM.

**In progress / proposals:**
- **Phase 1 simplification (owner request, 15 Nov):** castings and layout as simple and low-risk as possible. Two options in `docs/simplification-options.md`; waiting for the owner. Do not add features to the castings.
- **Portal relocation** (`docs/portal-relocation.md`): decided, bolted dry on shims (D-132, D-133).
- **Opus branch `claude/awesome-ramanujan-by9kds`: do not merge.** It forked from the 8 Nov state and redid tasks 2–5 on the old design with clashing D-numbers. This branch is the truth (owner, 15 Nov). Useful there: `cad/v2/moulds.py` as a starting point for the mould drawings.
- **Rail bolts must be M5 × 20**, not M5 × 16, because of the 5 mm resin seat (open question 4a).
- **Base PVC cores (not adopted yet):** 5 × Ø50 at Z −65, saving about 9.6 kg; sketch in `cad/v2/out/base_cores_plan.png`, `base_cores_sections.png` (`cad/v2/base_cores_sketch.py`). Suspension: an M8 rod through each capped core, fixed in the mould walls at core height, plus mid-span wire hold-downs from a batten; the rods are cut flush and sealed afterwards (they don't reinforce, D-120). The review found the layout sound (15 mm under the BK/BF plates). Owner to decide (maybe after the FEA, D-81).
- **EG design review: done** (`docs/review-eg-design-report.md`). The owner's decisions on it are D-114 … D-123 (smaller cores, open 5 mm rail-seat recesses, 20 mm joint bars, Ampreg 30 with post-cure, insert preparation, 3-point base support, hand tamping first, doc fixes). Not acted on yet: the review's tests (they go in task 6) and its lower-severity notes (gap grading fallback GCL 1–3 mm, mould deck).

Then: rail-seat levelling and assembly procedures, Phase 2 detailing (ATC wheel, enclosure fittings).

## 7. Open questions
`docs/open-questions.md`, in priority order with who answers each. The most urgent:
1. The Ampreg and GCL delivery costs (budget now £4,200, D-127).
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

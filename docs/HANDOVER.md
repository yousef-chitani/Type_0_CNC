# Type 0 CNC: handover (updated 2026-11-15)

**Branch:** `claude/awesome-ramanujan-by9kds` on `yousef-chitani/Type_0_CNC` (tasks 2–5 done there; the 2026-11-08 handover was on `claude/ecstatic-ramanujan-mhh3xe`).

## 1. What the project is
A DIY 3-axis **fixed-gantry, moving-table** CNC mill with a **cast epoxy-granite (EG) frame**, **LinuxCNC + Mesa 7I76EU**, closed-loop NEMA 24 steppers, and (Phase 2) a **Jianken ISO20 ATC spindle** with an 8-pocket ferris-wheel tool changer. Inspiration: Bootstrap Bill. The owner is in **Swansea, UK**. It will be built and used in a **shed**, but must later move into an **upstairs flat**: every piece must be carriable (≤ about 40 kg, base about 72 kg is a 2-person lift).

## 2. Current design (v2, D-71 … D-80)
- **Work area 400 × 250, Z 150.** Travel X 570 (incl. reach to the ATC wheel) / Y 250 / Z 150. Table 460 × 330 × 25 (6082).
- **2 solid EG castings:** T-shaped **base** (spine 320 wide, 110 high) about 72 kg; **gantry portal** 800 W × 375 H × 130 D, beam 150 tall (D-94), legs span the table only, beam overhangs 160 mm to the right for the ATC wheel; one 68 mm downpipe core in the beam (D-95); about 39.6 kg. Only frame joint: portal → base (grout once, M12 studs from couplers in the leg feet through sleeves in the base, D-96; relocation feature still open).
- **Motion:** HGR20 rails (X 2 × 800 on 100 spacing, Y 2 × 500 on 280 spacing, Z 2 × 350), DFU1605 screws (X 750, Y 450, Z 350), direct drive, StepperOnline closed-loop NEMA 24 (Z with brake), CL57T drivers.
- **Phase 1 spindle:** G-Penny 2.2 kW ER20 water-cooled kit (Huanyang VFD, Modbus RS-485). DIY cooling loop.
- **Enclosure (Phase 2):** 12 mm MDF box on the bench, top-hinged door, 600 × 420 × 4 mm polycarbonate window.
- **Stand:** owner-built bolted knock-down timber bench, top 1,100 × 1,000 at 785 mm (D-97, docs/bench.md).
- Model and drawings: `cad/v2/type0_v2.py` (parametric CadQuery → STEP + dimensions), `cad/v2/sketch_3piece.py` (concept sketches), `cad/v2/enclosure.py` (enclosure + cut list), `cad/v2/moulds.py` (mould drawings + parts), `cad/v2/bench.py` (bench drawings, STEP, cut list). Outputs in `cad/v2/out/`. `pip install cadquery` to run them. The v1 (large, garage) model is in `cad/` for history only.

## 3. Money and phases (D-66, D-86, D-68)
| Phase | Scope | Priced | Budget |
|---|---|---|---|
| 1 | Working mill, manual ER20 tool changes | **£3,065.28** + 11 lines to price (price check 10) | £4,000 |
| 2 | ATC spindle + holders, air, mist, enclosure, tool wheel | £1,408.22 | not set |
- Source of truth: **`docs/bom.csv`**. Generated from it: `docs/bom.md` (`python tools/gen_bom_md.py`), `docs/phase1-bom.xlsx` (`python tools/gen_phase1_xlsx.py`), `docs/phase1-cost.md` (`python tools/gen_phase1_cost.py`), `tools/open_links.py` (`python tools/build_open_links.py`).
- The old £3,066.41 still counted the shelved 5 V PSU (E22). The new figure drops it and adds the 3rd coarse bag (D-98).
- Phase 1 vendors (12): AliExpress, Screwfix, StepperOnline, RS, Easy Composites, Aluminium Warehouse, GCL, Hancock & Brown, Valentine Clays, The Metal Store, B&Q, Mesa.

## 4. Schedule (D-90, `docs/phase1-schedule.md`)
4 Jan 2027 → 22 Jul 2027, about 5 h/week. Done = machine jogs under LinuxCNC. Electronics first (indoors), moulds Feb–Mar, test bricks late March, castings April–May (≥ 18 °C cure), assembly June, wiring + config July. 5 order waves; X/Y rails and ballscrews now in wave 2 (15 Feb, D-93), the spindle kit by 5 April, the other motion parts by 29 March.

## 5. Owner's rules for working on this project
- **Use the Q&A tool heavily** before decisions. Ask, don't assume.
- **Only list prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Consolidate vendors; prefer B&Q / Screwfix (local), then RS. Flag any swap that costs much more (> 10% or £5) and let the owner decide.
- Most supplier sites block this cloud session. Prices are gathered by the owner's **local browser session** using `docs/price-check-task-N.md` files (task 9 was the last). The owner logs in to AliExpress themselves; the session never handles credentials.
- **Cast, not welded** (weld stress). Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number.

## 6. Tasks
Done:
1. ~~Electrical design~~: `docs/electrical.md` (D-91).
2. ~~LinuxCNC starter config~~: `config/linuxcnc/type0/` + `docs/linuxcnc.md` (D-92). USB-RS485 + `hy_vfd` for the VFD. Not run yet (no LinuxCNC in the cloud): expect pin-name fixes on the first start.
3. ~~Timber bench~~: `docs/bench.md`, `cad/v2/bench.py` (D-97). Items T03–T07 in wave 2, to price.
4. ~~Mould drawings~~: `docs/moulds.md`, `cad/v2/moulds.py` (D-94, D-95, D-96). Re-run with the real rail and screw sizes when wave 2 arrives.
5. ~~EG mix design + test-brick plan~~: `docs/eg-mix.md` (D-98).

Next:
1. **Price check 10** (`docs/price-check-task-10.md`) in the owner's local browser session: E23, E24, T03–T07, F19–F22.
2. **Portal relocation feature: Fable's assessment.** Full brief in section 7 below. Needed by week 9 (1 Mar 2027).
3. **Enclosure widening** for the X motor (open question 15), Phase 2.
4. Rail-seat levelling and assembly procedures (levelling pour, squaring the portal, grouting), then Phase 2 detailing.

## 7. Brief for Fable: portal relocation assessment
The owner asked for an independent assessment of how the portal goes back onto the base in the same place, **explained to them in plain words**. The previous session listed options but deliberately did not choose. Treat the options as a starting point, not a shortlist: a better method is welcome.

**Why it matters.** The machine is built in the shed, then taken apart and carried upstairs to a flat (pieces ≤ about 40 kg). The portal (39.6 kg) is the only frame joint. After each move it must sit square to the Y rails again. The part accuracy target is ±0.02 mm (D-03).

**What is fixed already (D-94, D-96, `cad/v2/moulds.py`):**
- Base cast **upside down**: its top face, where the legs stand, is formed by the MDF mould floor. Anything on that face (pockets, bushes, inserts) is set on or through the floor.
- Portal cast **lying on its front face**: the leg feet (z = 0) are formed by an MDF mould **wall**.
- Leg footprints: 70 (x) × 130 (y), at x ±250…320, y 110…240 (machine coordinates, Y = 0 on the spindle line).
- Joint: 2 × M12 studs per leg at x ±285, y 145 and 205. Studs screw into M12 coupling nuts cast in the leg feet (torque 25–30 Nm until a test brick proves more), drop through 20 mm conduit sleeves in the base, nutted underneath. About 3 mm epoxy grout under each leg, poured once after shimming the portal square.
- The area under each leg is **reserved** (pink on `mould_base.png`) for the relocation feature.
- Studs, sleeves, couplers and the Y rail bars must not be moved without a new decision.

**Options on file** (detail in `docs/moulds.md`, section "Open: portal relocation"): A. grout keys (cones in base pockets, base side released); B. dowels set in epoxy in cast sleeves/bushes; C. bolts and grout only, re-square with the dial indicator each time; D. the studs themselves as locators in close-fitting bushes.

**Questions the assessment should answer:**
1. How repeatable is each option (rough µm or mm), and how much re-alignment work does each leave after a move?
2. Is there real-world evidence (DIY EG machines, machine-tool practice, epoxy replication/grout keys)? Give sources; say plainly where none was found.
3. What has to go into the moulds, and does it fit the reserved area without clashing with the studs and sleeves?
4. What does it cost? Only prices read from a live page or given by the owner, with the date (rule in section 5). No eBay.
5. Can it be tried on a test brick in weeks 12–13 (`docs/eg-mix.md`) before the base is cast in week 15?

**Deliverable.** A plain explanation for the owner with a recommendation. Ask the owner with the Q&A tool before deciding. Then: record the decision as **D-99** in `docs/decisions.md`; update `docs/moulds.md` (replace the open section), `cad/v2/moulds.py` (draw the feature in the reserved area, re-run), `docs/open-questions.md` (item 14), the BOM if parts are added (regenerate with the tools in section 3), and this handover.

**Deadline.** Decided by **week 9 (1 Mar 2027)**, when the base mould floor is marked out and drilled.

## 8. Open questions
See `docs/open-questions.md` (updated at handover).

## 9. Key files
| File | What |
|---|---|
| `docs/requirements.md` | Requirements |
| `docs/decisions.md` | Decision log D-01 … D-98 |
| `docs/v2-design.md` | v2 design notes (joints, ATC wheel, enclosure) |
| `docs/electrical.md` | Power, safety chain, 7I76EU pin map, VFD settings |
| `docs/linuxcnc.md`, `config/linuxcnc/type0/` | LinuxCNC config, latency test, bench test |
| `docs/bench.md` | Timber bench |
| `docs/moulds.md` | v2 mould drawings and parts (relocation options: section 7 brief) |
| `docs/eg-mix.md` | Void test, test bricks, mixing, curing heat |
| `docs/bom.csv` / `bom.md` / `phase1-bom.xlsx` / `phase1-cost.md` | Parts list and costs |
| `docs/phase1-schedule.md` | Timeline and order waves |
| `docs/eg-moulds.md`, `aggregates.md`, `epoxy-options.md` | Casting method notes (v1 sizes; v2 sizes are in moulds.md) |
| `docs/price-check-task-*.md` | Instructions used for the local price checks |
| `tools/open_links.py` | Vendor-by-vendor shopping helper (standalone) |

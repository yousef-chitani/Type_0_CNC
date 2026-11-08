# Type 0 CNC: handover (2026-11-08)

**Branch:** `claude/ecstatic-ramanujan-mhh3xe` on `yousef-chitani/Type_0_CNC`. Everything below is committed and pushed.

## 1. What the project is
A DIY 3-axis **fixed-gantry, moving-table** CNC mill with a **cast epoxy-granite (EG) frame**, **LinuxCNC + Mesa 7I76EU**, closed-loop NEMA 24 steppers, and (Phase 2) a **Jianken ISO20 ATC spindle** with an 8-pocket ferris-wheel tool changer. Inspiration: Bootstrap Bill. The owner is in **Swansea, UK**. It will be built and used in a **shed**, but must later move into an **upstairs flat**: every piece must be carriable (≤ about 40 kg, base about 72 kg is a 2-person lift).

## 2. Current design (v2, D-71 … D-80)
- **Work area 400 × 250, Z 150.** Travel X 570 (incl. reach to the ATC wheel) / Y 250 / Z 150. Table 460 × 330 × 25 (6082).
- **2 solid EG castings:** T-shaped **base** (spine 320 wide, 110 high) about 72 kg; **gantry portal** 800 W × 355 H × 130 D, legs span the table only, beam overhangs 160 mm to the right for the ATC wheel; PVC cores in the beam; about 34 kg. Only frame joint: portal → base (grout once, then dowels + bolts).
- **Motion:** HGR20 rails (X 2 × 800, Y 2 × 500 on 280 spacing, Z 2 × 350), DFU1605 screws (X 750, Y 450, Z 350), direct drive, StepperOnline closed-loop NEMA 24 (Z with brake), CL57T drivers.
- **Phase 1 spindle:** G-Penny 2.2 kW ER20 water-cooled kit (Huanyang VFD, Modbus RS-485). DIY cooling loop.
- **Enclosure (Phase 2):** 12 mm MDF box on the bench, top-hinged door, 600 × 420 × 4 mm polycarbonate window.
- **Stand:** owner-built timber bench, top 785 mm.
- Model and drawings: `cad/v2/type0_v2.py` (parametric CadQuery → STEP + dimensions), `cad/v2/sketch_3piece.py` (concept sketches), `cad/v2/enclosure.py` (enclosure + cut list). Outputs in `cad/v2/out/`. The v1 (large, garage) model is in `cad/` for history only.

## 3. Money and phases (D-66, D-86, D-68)
| Phase | Scope | Priced | Budget |
|---|---|---|---|
| 1 | Working mill, manual ER20 tool changes | **£3,066.41** (+ E23 relay to price) | £4,000 |
| 2 | ATC spindle + holders, air, mist, enclosure, tool wheel | £1,408.22 | not set |
- Source of truth: **`docs/bom.csv`**. Generated from it: `docs/bom.md` (`python tools/gen_bom_md.py`), `docs/phase1-bom.xlsx` (`python tools/gen_phase1_xlsx.py`), `docs/phase1-cost.md`, `tools/open_links.py` (`python tools/build_open_links.py`).
- Phase 1 vendors (12): AliExpress, Screwfix, StepperOnline, RS, Easy Composites, Aluminium Warehouse, GCL, Hancock & Brown, Valentine Clays, The Metal Store, B&Q, Mesa.

## 4. Schedule (D-90, `docs/phase1-schedule.md`)
4 Jan 2027 → 22 Jul 2027, about 5 h/week. Done = machine jogs under LinuxCNC. Electronics first (indoors), moulds Feb–Mar, test bricks late March, castings April–May (≥ 18 °C cure), assembly June, wiring + config July. 5 order waves; the spindle kit must be ordered by 5 April, motion parts by 29 March.

## 5. Owner's rules for working on this project
- **Use the Q&A tool heavily** before decisions. Ask, don't assume.
- **Only list prices confirmed from a live page** (or given by the owner), with the date. Never estimate prices.
- **No eBay.** Consolidate vendors; prefer B&Q / Screwfix (local), then RS. Flag any swap that costs much more (> 10% or £5) and let the owner decide.
- Most supplier sites block this cloud session. Prices are gathered by the owner's **local browser session** using `docs/price-check-task-N.md` files (task 9 was the last). The owner logs in to AliExpress themselves; the session never handles credentials.
- **Cast, not welded** (weld stress). Keep the frame in carriable pieces.
- Write plainly; record every decision in `docs/decisions.md` with a D-number.

## 6. Next tasks (agreed order)
1. ~~Electrical design~~: done, `docs/electrical.md` (D-91). Has CHECK items.
2. **LinuxCNC starter config** for the 7I76EU (3 closed-loop axes, Modbus spindle via the Mesa RS-485 port or USB fallback, e-stop chain on IN3, drive alarms IN4–6, brake on OUT1, flow interlock IN7), plus a latency test and bench-test procedure.
3. **Timber bench design:** cut list, top 785 mm, about 150 kg + enclosure, cabinet space; adds B&Q items to wave 2.
4. **Mould drawings** for the base and portal from the v2 model (panels, jig-bolt hole pattern for insert bars, Y-screw channel 70 × 25, PVC cores, M12 sleeves, dowels, lifting points, vibration-table deck).
5. **EG mix design + test-brick plan:** GlassCast 50 PLUS with GCL quartz 2–5, H&B 0–1 sand, whiting (≤ 8–10%), 2–3 epoxy ratios; mixing order, vibration, curing heat checks.
Then: rail-seat levelling and assembly procedures, Phase 2 detailing.

## 7. Open questions
See `docs/open-questions.md` (updated at handover).

## 8. Key files
| File | What |
|---|---|
| `docs/requirements.md` | Requirements |
| `docs/decisions.md` | Decision log D-01 … D-91 |
| `docs/v2-design.md` | v2 design notes (joints, ATC wheel, enclosure) |
| `docs/electrical.md` | Power, safety chain, 7I76EU pin map, VFD settings |
| `docs/bom.csv` / `bom.md` / `phase1-bom.xlsx` / `phase1-cost.md` | Parts list and costs |
| `docs/phase1-schedule.md` | Timeline and order waves |
| `docs/eg-moulds.md`, `aggregates.md`, `epoxy-options.md` | Casting notes (partly v1 sizes: check against v2) |
| `docs/price-check-task-*.md` | Instructions used for the local price checks |
| `tools/open_links.py` | Vendor-by-vendor shopping helper (standalone) |

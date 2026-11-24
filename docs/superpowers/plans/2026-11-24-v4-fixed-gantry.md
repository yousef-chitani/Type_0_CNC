# Type 0 V4 (fixed gantry, moving table): implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the approved V4 design into checked sizes, a priced BOM inside £4,200, a new Fusion model `Type_0_v4` with no clashes, and corrected lengths for the 4 Jan 2027 wave 1 order.

**Architecture:** First a small Python sizing script fixes every length from the work area and the wheel's pickup, and is the single source for the model and the BOM. Then the owner picks profiles and sections (Q&A), prices are checked by curl, and the model is built in a new Fusion document through the Fusion MCP, axis by axis, each ending with a read-only check script (timeline health, body overlap, reach). The "tests" are script asserts and geometric checks.

**Tech Stack:** Python 3 (`tools/`, plain asserts, run with `PYTHONUTF8=1`); Fusion 360 API via `fusion_mcp_execute`; curl + Python for prices (CLAUDE.md).

**Spec:** `docs/superpowers/specs/2026-11-24-v4-fixed-gantry-design.md` (approved 24 Nov 2026; D-305 to D-307).

## Global Constraints
- Work area **400 x 250**, Z travel 150, table about 460 x 330, table to spindle nose **25 to 175**. Part accuracy ±0.02 mm.
- Fixed gantry; table moves in Y on rails **on top of the base**; uprights **steel**, bolted to the base sides; beam **steel SHS 120 x 120 x 8**.
- Base: bolted aluminium extrusion tray, voids filled with EG (Ampreg 30, about 11 % by weight). No casting, no welding.
- Rail seats: epoxy-levelled or shop-ground plates. **Never as-extruded or hot-rolled faces.**
- Tools: v3's indexing wheel outside the frame on the **right (+X)**, one pickup reached along X. The Phase 2 enclosure goes round the wheel.
- Motion parts: LiMo C5 DFU1605, HGR20 (HGH20CA, ZA), BK12/BF12 (D-136). One Y screw and motor.
- Mass: no limit. Budget: Phase 1 **£4,200**; flag any overrun, do not cut accuracy.
- Prices only from live pages, by curl, with the date; never estimate; no eBay; flag anything more than 10 % or £5 dearer.
- Ask the owner (Q&A tool) before any decision not in the spec; record decisions in `docs/decisions.md` from **D-308**.
- `Type_0_v3` is history: do not edit it. Do not save Fusion documents: the owner saves.
- `docs/bom.csv` is the source of truth (CRLF). Stop at about 130k tokens of context and hand over (CLAUDE.md).

## Review Focus
- The spindle at the wheel's pickup: the Z carriage and X nut housing must not hit the right upright or its bolts as the carriage passes it. Check in Task 5 by moving the X slider to its +X limit.
- The table at both Y limits under the uprights and beam: the uprights' feet and the Y motor must clear the table and the fixture-plate screws. Check in Task 4 at both limits.
- The longest allowed tool in the wheel and in the spindle at Z top: it must clear the table edge and the base top when the spindle crosses to the wheel. Check in Task 5 with the tool length from v3 (D-288 notes).
- Chips and coolant falling off the moving table onto the Y screw and rails. Check in Task 4: the Y screw has a cover or sits outside the drip line.
- The steel-to-aluminium upright joint squareness after bolting: a datum and dowels must exist. Check in Task 3 that the joint has 2 dowels and a ground or shimmed face listed in the BOM.

---

### Task 1: Sizing script
**Files:** Create `tools/v4_sizes.py`; create `docs/v4-sizes.md` (its printed table).

**Interfaces:**
- Produces: `sizes() -> dict` with keys `x_travel, y_travel, z_travel, x_rail, x_screw, y_rail, y_screw, z_rail, z_screw, beam_len, base_len, base_width, beam_overhang_right` (mm), used by Tasks 2 to 7. Inputs at the top of the file as named constants: work area, table size, carriage block length, BK12/BF12 lengths, wheel pickup offset from the right upright's outer face, upright width.

- [ ] Write asserts at the bottom of the file, run under `if __name__ == "__main__":`: `y_travel >= 250`; `x_travel >= 430 + wheel reach`; spindle covers table X ±230 and Y 0 to 330; every rail and screw length is one LiMo sells (check the listing by curl, record the date); `x_screw <= 1000` (1605 whip, state the rpm limit it gives).
- [ ] Run `PYTHONUTF8=1 python tools/v4_sizes.py`: expect FAIL until the constants are filled.
- [ ] Fill the constants from v3 parts (BK12/BF12, HGH20CA, Z axis) and the wheel's geometry after D-304. Run again: expect PASS and the table printed.
- [ ] Write the table into `docs/v4-sizes.md` with a one-line source for each input. Commit.

### Task 2: Owner picks profiles and sections; prices
**Files:** Modify `docs/decisions.md`, `docs/bom.csv` (via the hook), create `docs/price-check-v4.md`.

**Interfaces:**
- Consumes: `sizes()` from Task 1.
- Produces: D-numbers for the base extrusion profile, upright section, beam length, rail plate route (ground plate or epoxy seat), wheel mount side part.

- [ ] Draw 2 to 3 base tray layouts in text (profile size, pocket layout, how pockets are closed for the pour) and 2 upright sections, each with mass and a hand stiffness figure from a short script (`tools/v4_frame_stiffness.py`, like `tools/portal_overhang.py`): deflection at the nose per 100 N in X, Y, Z, and at the wheel pickup. Also ask whether the beam gets a damping fill (`docs/beam-assessment.md` options, figures redone for the 1 m beam). Ask the owner (Q&A). Record decisions.
- [ ] Price by curl (CLAUDE.md methods): the chosen extrusion and fixings, steel SHS or plate for the uprights, the beam at its new length, flat bar for rail plates. Ask the owner for a shop grinding price if ground plates are chosen. Write `docs/price-check-v4.md`.
- [ ] Commit.

### Task 3: BOM for V4 and budget
**Files:** Modify `docs/bom.csv`; generators run by the hook.

- [ ] Drop v3-only lines (tub EG fill share, moulds, roller tubes and angles, Y braces, Y2 motor, driver and screw set, wall-top plates G06, jack screws); add V4 lines (extrusion, fixings, uprights, dowels, rail plates, EG fill for the base pockets); change lengths to `sizes()`. Note each change with D-305 to D-307 or the new D-number.
- [ ] Check: the generated `docs/phase1-cost.md` total is at or under £4,200; if over, list the overrun and the options to the owner (Q&A), do not cut accuracy.
- [ ] Check the steel-to-aluminium joint has 2 dowels per upright and a ground or shimmed face in the BOM (Review Focus). Commit.

### Task 4: New model: base, Y axis, table
**Files:** new Fusion document `Type_0_v4` (owner creates and saves); `docs/v4-model.md` (what is modelled, names, checks).

**Interfaces:**
- Consumes: `sizes()`, Task 2 decisions.
- Produces: components `Base (extrusion + EG)`, `Y rails and plates`, `Y screw and motor`, `Table`; world origin at the table top centre with the table at Y mid travel (write this in `docs/v4-model.md`).

- [ ] Precondition: the Fusion MCP is connected and the owner has created `Type_0_v4`. If not, stop and hand over.
- [ ] Model the base tray (profiles, end plates, EG pocket bodies as separate bodies), rail plates with the epoxy bed, HGR20 rails and blocks, table and fixture plate, one Y screw with BK12/BF12 and motor.
- [ ] Check (read-only script): no unhealthy timeline items; no body overlaps except screws in holes; move the table to both Y limits and repeat; Y screw covered or outside the drip line (Review Focus). Commit `docs/v4-model.md`.

### Task 5: Uprights, beam, X and Z, spindle
**Interfaces:**
- Consumes: Task 4 components.
- Produces: components `Uprights`, `Beam`, `X axis`, `Z axis and spindle` (Z copied from v3 by Insert into Current Design / derive, not edited in v3).

- [ ] Model the steel uprights with 2 dowels each, the beam with epoxy-levelled X rail seats, X rails, X screw, the v3 Z axis and spindle.
- [ ] Check: nose height 25 and 175 above the table at Z limits; spindle reaches the table corners; X slider at +X limit clears the right upright and its bolts (Review Focus); overlap check clean. Commit.

### Task 6: Wheel outside the right side
**Interfaces:**
- Consumes: Task 5 X limit; v3 wheel as of D-304.
- Produces: component `ATC Wheel (Phase 2)` in `Type_0_v4`, its mount, the chip-guard envelope, the enclosure's outside size.

- [ ] Ask the owner (Q&A): the wheel's mount (base side or upright) and its plane; how the spindle enters the fork from X. Record a D-number.
- [ ] Insert the wheel, apply D-304 if `Type_0_v3` still has D-303 (disc 6 mm on the longer hub), mount it so the pickup sits at the X limit from `sizes()`.
- [ ] Check: sweep of the wheel and tools (longest tool) clean; spindle with longest tool crosses from table to wheel without hitting the table edge or base top (Review Focus); print the enclosure's outside size. Commit.

### Task 7: Pour plan, order lengths and docs
**Files:** Create `docs/v4-pour.md`; modify `docs/requirements.md`, `docs/owner-todo.txt`, `docs/wave1-order-sheet.md` (via generators), `docs/tasks/README.md`, `docs/HANDOVER.md`.

- [ ] Pour plan: pocket volumes from the model, EG mass and epoxy at about 11 %, against the F01 kit (22.68 kg), pour order and how pockets are vented and closed; test bricks first.
- [ ] Wave 1: LiMo lengths from `sizes()` replace X 850 / Y 600 / Z 350 where they differ; one Y set, not two; send the owner the changes before 4 Jan 2027.
- [ ] Update `requirements.md` (layout, frame, travel, site, mass), task list and handover. Commit and push.

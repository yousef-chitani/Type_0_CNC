# ATC FK12 block and plate column: implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the one-piece ATC mount in `Type_0_v3` with an FK12 block, a screwed-plate column, a stub shaft, a coupling and a base L, as approved.

**Architecture:** Work in the open Fusion 360 document `Type_0_v3` through the Fusion MCP script tool, inside the top-level component `ATC Wheel (Phase 2)`. Old bodies go by Remove features (as D-289 did); new parts are named components with named bodies. The "tests" are geometric checks run by read-only scripts: timeline health, body overlap (static), and the sweep of turning parts.

**Tech Stack:** Fusion 360 API (Python via `fusion_mcp_execute` script); curl + Python for prices and the vendor CAD.

**Spec:** `docs/superpowers/specs/2026-11-23-atc-fk-block-column-design.md`

## Global Constraints
- Wheel axis X 200, Y -174; forks Z 126 to 136; hub top part Z 119 to 131 unchanged; pickup X 200, Y -85.
- Nothing in the tools' sweep: r 89 around the axis, tools down to Z 17 (longest allowed); nothing at Y < -78 rises above Z 12 except the column (inside r 58).
- Tub plate 50 x 40 x 10, X 175 to 225, Y -47 to -37, Z -10 to 30; strip 50 x 10 x 40, Y -37 to -27; 2 x M6 at X 185 and 215, Z 21.
- Do not save `Type_0_v3`: the owner saves. Prices only from live pages with the date, by curl (CLAUDE.md). No eBay.
- Names in the model and docs in plain words; decisions D-295 onward in `docs/decisions.md`.
- Stop at about 130k tokens of context and hand over (CLAUDE.md).

## Review Focus
- The hub's 4 x M4 heads against the forks' inner edges (forks screw at r 41.7): check in Task 3.
- The sensor ear against the holders as the wheel turns (holder inner edge r 66.5): covered by the sweep in Task 6.
- Coupling and locknut reachable through the open ±X sides with a 2.5 key: check by measurement in Task 4.
- The 2 x M6 counterbores at X 185/215 against the gusset: check gap ≥ 3 in Task 5.
- The motor's cable boss and cables at +X against the walls and the base L: covered by the static check in Task 6.

---

### Task 1: Prices and vendor CAD
**Files:** Modify `docs/bom.csv` (CRLF, `""` quotes), `cad/vendor/README.md`; add `cad/vendor/FK12*.step` if a free download exists.
- [x] Find FK12 (fixed side, 7001 pair) and a Ø20 x 25 coupling, 5 x 8 bores, from the owner's usual vendors (RS first; Shopify `/products.json`, WooCommerce `/wp-json/wc/store/products`); record price, date, URL. If curl is blocked, write `docs/price-check-task-18.md` for the owner and go on with the THK sizes.
- [x] Get FK12 CAD (vendor or THK/HIWIN) to fix the shoulder Z (T2) and locknut Z. Without it, use the THK sheet values from the spec.
- [x] Commit.

### Task 2: Remove the old mount parts
**Interfaces:** Produces an empty mount position; keeps hub, forks, holders, motor, sensor, flag.
- [x] Remove features for: `Mount one piece ...` body, the 2 x 6804 and the spacer, the hub grub M4 x 6, the 2 x M6 x 20 into the strip, the 4 x M3 x 12 motor screws, the sensor M4 grub. List the bodies removed in the commit message.
- [x] Check: read-only script prints every unhealthy timeline item after index 1891, the last item on 23 Nov (the 35 older broken items stay as they are): expect none new.
- [x] Commit (docs note only; the model is not saved).

### Task 3: Hub change and stub shaft
**Files:** model only.
**Interfaces:** Produces component `ATC Stub shaft (FK12)` with body `Stub shaft 303: pilot 12, flange 40 x 5, shoulder 14, journal 12, M12 x 1, drive 8`; hub underside flat at Z 119.
- [x] Hub: cut the Ø20 spigot (Z 84 to 119) and fill the old relief to a flat Z 119; Ø12 pilot bore 6 deep; 4 x Ø4.5 with Ø8 x 4.5 counterbores at r 14 (at 0, 90, 180, 270°, turned to miss the fork screws).
- [x] Stub shaft as in the spec stack, Z from Task 1 (else: flange 114 to 119, shoulder to 108, journal to 81, thread 81 to 71, drive 71 to 59).
- [x] 4 x M4 x 10 cap screws, hub to shaft flange.
- [x] Check: M4 heads to the nearest fork body ≥ 1 mm (minimum distance script). Commit.

### Task 4: FK12, column plates, coupling, motor
**Interfaces:** Produces components `ATC Block FK12 (A06)`, `ATC Column plates (6082)`, `ATC Coupling 8-5`.
- [x] FK12 stand-in (or vendor STEP): flange Ø54/44 across flats x 10 at Z 98 to 108, nose Ø36 x 17 to Z 81, locknut stand-in Ø22 x 8.5 (M12 x 1; check against the vendor CAD) to about Z 72.5; 4 x M4 x 12 into the top plate.
- [x] Top plate 70 x 70 x 12, Z 86 to 98, Ø36 bore, 4 x M4 tapped, ear at -X for the sensor at r 44, 202.5° (tapped M12 x 1, M4 lock grub from the ear edge); ear inside r 58.
- [x] 2 walls 70 x 8, Z -8 to 86, inner faces at Y -149.8 and -198.2; motor plate 6 thick between them at Z 28 to 34 with Ø22 pilot and 4 x Ø3.4 on 31 square; screws and 2 dowels per joint (M4 into the plates' edges, *builder's choice* of count).
- [x] Move the motor so its face is at the motor plate underside (Z 28 if the plate is 28 to 34; keep the boss at +X), 4 x M3 x 10.
- [x] Coupling stand-in Ø20 x 25 joining the Ø8 drive and the Ø5 motor shaft; check the motor shaft enters ≥ 10.
- [x] Move the sensor to the ear, face 2 below the flag.
- [x] Check: a 2.5 key reaches the coupling clamp screws and the locknut setscrew through ±X (measure). Commit.

### Task 5: Base L and cast-in strip
**Interfaces:** Produces component `ATC Base L (6082)`; tub strip body renamed `Steel strip 50 x 10 x 40 (D-295)`.
- [x] Base L: tub plate as in Global Constraints, arm 50 wide Z -8 to 12 from Y -47 to the tub-side wall (Y -149.8 + 8 = -141.8), gusset 10 wide at X 195 to 205, sloped, Y -47 to -78 max; 2 x Ø6.6 + Ø11 x 6.5 counterbores at X 185/215, Z 21; arm end to wall 4 x M5 + 2 dowels.
- [x] Strip: remove the 80-wide strip, fill its holes and cores in the tub; new 50 x 10 x 40 strip with 2 x M6 at X 185/215, Z 21 and Ø6.6 cores Y -27 to -25.
- [x] 2 x M6 x 20 from the front.
- [x] Check: counterbore edge to gusset ≥ 3. Commit.

### Task 6: Checks
- [x] Static overlap of every ATC body against all visible bodies in X 75 to 325, Y -300 to -15, Z -60 to 200: expect only screws in tapped holes.
- [ ] Sweep as in `atc-wheel.md` (hub, forks, fork screws, hub M4s, holders 0 to 45° in 3°; flag 0 to 360° in 5°) against the static bodies: expect no hits above 0.1 mm³.
- [ ] Spindle against the wheel at drop-off, pickup and lifted (the method in `atc-wheel.md`, 13th session): expect only holder 1 at the gripped pocket.
- [ ] Mass of the new metal parts; lowest Z (expect about -46). Record results.

### Task 7: Docs and handover
**Files:** `docs/atc-wheel.md` (rewrite to the new parts, renders `atc-wheel.png`, `atc-wheel-under.png`), `docs/decisions.md` (D-295: FK12 block, plate column, stub shaft, coupling, approach A; D-296: ATC overhangs the bench front, lowest Z about -46; D-297: tub plate 50 x 40 x 10, strip 50 x 10 x 40), `docs/bom.csv` (A06, A07, new lines FK12, coupling, plate), `cad/v2/out/assembly/cast_in_features.md` (strip row), `docs/design-issues.md` (bench overhang), `docs/HANDOVER.md`, `docs/tasks/README.md`.
- [ ] Write, commit, push.

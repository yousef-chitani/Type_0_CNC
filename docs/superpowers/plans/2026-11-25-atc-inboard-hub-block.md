# ATC inboard hub block: implementation plan

> **For agentic workers:** run this with superpowers:executing-plans (native). Steps use checkboxes.

**Goal:** Replace the D-316 ATC mount bracket and outboard drive in `Type_0_v4` with the inboard hub block from the spec.

**Architecture:** Edit the one base feature in the component `ATC Wheel (Phase 2)` from Fusion scripts. Delete the outboard bodies, add new BRep boxes and cylinders for the block, pulleys, belt, motor and sensor stand-ins, and move the FK12 and stub inboard. Do not save: the owner saves.

**Tech stack:** Fusion 360 API (Python, through the MCP script tool), and Markdown/CSV docs.

**Spec:** `docs/superpowers/specs/2026-11-25-atc-inboard-hub-block-design.md`

## Global constraints
- Wheel, pickup and sweep unchanged: pickup X 402, Y 0, nose Z 70; wheel centre Y 0, Z -82; holders X 379.5 to 424.5; disc X 429 to 435.
- Block in the X 270 to 379 gap. Nothing below Z -168 inboard of X 330. Nothing past X 435 except the screw heads in the disc hole.
- Fusion checks: bounding-box-filtered and few-pose only (a heavy script once locked Fusion for 10 minutes). Do not save the document.
- `docs/bom.csv` uses CRLF line endings and `""` escaping.

## Review focus
1. The withdrawn Ø20 x 100 tool (x 372, nose 70, tip Z -30) against the block top and the 60T. Check this pose explicitly.
2. The M16 head pockets: no overlap between the flange and the bolt heads at Y ±45, Z -120.
3. The hub-to-stub screw heads must sit inside the disc's Ø44 hole (r 22 or less).
4. The motor body and the encoder-free length must fit between the flange (X 290) and the wall (X 340).
5. The belt plane (X 360 to 376) against the holders' inboard face (X 379) and the hub (X 386).

---

### Task 1: Model the block and the inboard drive
- [ ] Delete the bodies `ATC mount bracket 6082`, `Column block 6082`, `Coupling D20L25`, the 17HS24 motor and its inner bodies (Body2, Body3), the 4 motor M3 screws, the 4 FK12-to-column screws and the 4 hub-to-stub M4 x 12.
- [ ] Move the FK12 (and Body1) and the stub to the inboard side. The FK12's mounting flange goes on the wall's inboard face at X 340, and the stub's flange on the hub's inboard face at X 386. Rebuild the stub as one cylinder set if moving it is not clean.
- [ ] Add the block body `ATC hub block 6082 (D-317)`: flange X 270 to 290 (Y -40 to 105, Z -165 to -55) with 2 pockets Ø28 over the M16 heads; floor X 290 to 340, Z -125 to -110; wall X 340 to 355 (Y -40 to 95, Z -125 to -55) with Ø26 and Ø24 shaft holes.
- [ ] Add the stand-ins: `NEMA 17 short 42x42x48 (stand-in, A03)` at Y 60, Z -82, X 292 to 340; pulleys `GT2 60T` and `GT2 20T` at X 360 to 376; `GT2 belt 6 mm` (an envelope round both); `LJ12A3 index sensor` through the wall at Y -44, Z -82; flag screw head on the hub's inboard face.
- [ ] Add 4 hub screws `M4 x 50` from the hub's outboard face (r 14) into the stub flange.
- [ ] Verify: timeline healthy, and no overlaps between the new bodies and the frame (base, upright, end plate bolts).

### Task 2: Pose checks
- [ ] Run the 4 poses from the `docs/v4-model.md` Task 6 checks table (engaged, lifted 0 to 30°, withdrawn with the Ø20 x 100 tool, withdrawn and lifted) against the block, motor, pulleys, belt and sensor. Expected: clean.
- [ ] Measure the machine envelope X max. Expected: about 435.

### Task 3: Docs, decisions, BOM, handover
- [ ] D-317 in `docs/decisions.md`: the owner's decisions and the "Proposed by Claude, owner to confirm" part kept separate.
- [ ] `docs/v4-model.md`: a Task 6 rework section, and the envelope updated.
- [ ] BOM: A03 motor (short NEMA 17, not priced, so price pending), A06 block, A07 FK12 only (coupling out), A08 belt drive back (price from the old line, date kept, so it needs a re-check), A09 sensor place, F-line note for the end plate's 4 x M8.
- [ ] `docs/HANDOVER.md` (archive the oldest entry), `docs/tasks/README.md`, commit and push.

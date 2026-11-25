# Task 29: a quote-ready design before wave 1 (owner's goal, 25 Nov 2026)

**Goal (owner):** before wave 1 (4 Jan 2027), the design is fully defined, can be made and can be put together, so machine shops can quote the made-to-order parts.

**Done means:** one RFQ pack a shop can price without asking questions: per part a STEP and a PDF drawing (material, stock, quantity, holes and threads, the few tolerances that matter, finish), plus one cover sheet listing every part. Split into one sub-pack per process, each with its own cover sheet (D-330).

**Read only:** this file, `docs/v4-model.md`, `docs/task28-folds-and-footprint.md` (the 3 open questions).

## Where the model stands (read from `Type_0_v4`, timeline 194, 25 Nov)

### Made-to-order parts in the model (wave 1 candidates)
| # | Part | Qty | Material | Likely process | State in the model |
|---|---|---|---|---|---|
| 1 | Base end plate 670 x 90 x 20 | 2 | steel | saw, drill, tap | real |
| 2 | Base profile 90 x 90 x 500 | 4 | aluminium extrusion | supplier cut and tap | real |
| 3 | Y rail seat bar 50 x 20 x 670 | 2 | steel | surface grind, drill, tap | real |
| 4 | Table plate 460 x 330 x 25 | 1 | 6082 | CNC mill | real; tapped grid / slots not defined |
| 5 | Upright 50 x 150 x 325 | 2 | steel flat bar | mill, drill, tap, dowel holes | real |
| 6 | Beam SHS 120 x 120 x 8 x 890 | 1 | steel | saw, drill, tap | real |
| 7 | X rail front plate 160 x 20 x 890 | 1 | steel | surface grind, drill, tap | real |
| 8 | X BK12 / BF12 pads 50 x 80 x 20 | 2 | steel | grind | **out of date: D-320 replaces the X BK12 with an HM12-60-V on a pad** |
| 9 | X nut bracket 150 x 145 x 20 | 1 | 6082 | CNC mill | **envelope** |
| 10 | X motor bracket 10 | 1 | — | — | **envelope, dropped by D-320, still in the model** |
| 11 | Beam end dam 10 | 1–2 | steel | laser | **envelope** |
| 12 | Y motor plate 10 | 1 | — | laser / mill | **envelope** |
| 13 | Nut housing spacers 5 | 2 | — | laser | real, material not set |
| 14 | Z fixed plate 150 x 442 x 20 | 1 | 6082 | CNC mill | from v3, check holes against V4 |
| 15 | Z moving plate 150 x 200 x 20 | 1 | 6082 | CNC mill | from v3 |
| 16 | Z risers 25 x 15 x 350 | 2 | 6082 | mill | from v3 |
| 17 | Rear shear plate 10 x 200 x 445 | 2 | steel | laser | real (D-323) |
| 18 | Beam rear spacer 80 x 25 x 200 | 2 | bright steel | saw, drill, countersink | real (D-323) |
| 19 | Drip skirts | 2 | 2 mm sheet | laser, bend | envelope |
| 20 | Z fold plate with 2 bearing seats, on the HM12 top (D-325) | 1 | 6082 | CNC mill | **not modelled** |
| 21 | Z stub shaft Ø10 (D-325) | 1 | steel | lathe | **not modelled** |
| 22 | X motor fold plate on the HM12 (D-326) | 1 | 6082 | CNC mill | **not modelled** |
| 23 | X stub shaft Ø10, as Z (D-327) | 1 | steel | lathe | **not modelled** |
| — | ATC hub block, stub shaft, fork disc (Phase 2) | — | — | — | left out of this RFQ (D-328) |

**Whole model:** every body has the material "Steel", aluminium parts included. Drawings need the right material on each part.

## Who makes what (D-329, D-330, 25 Nov)
| Pack | Parts (row numbers above) |
|---|---|
| **Owner (saw, drill, tap)** | 1 base end plates, 5 uprights (if the joint faces need milling they move to the CNC mill pack: step 4), 6 beam, 18 beam rear spacers |
| Supplier cut and tap (KJN) | 2 base profiles |
| **Laser (and bend)** | 11 beam end dam, 12 Y motor plate, 13 nut housing spacers, 17 rear shear plates, 19 drip skirts (10 is dropped, D-320) |
| **CNC mill** | 4 table plate, 9 X nut bracket, 14 Z fixed plate, 15 Z moving plate, 16 Z risers, 20 Z fold plate, 22 X fold plate |
| **Surface grind** | 3 Y rail seat bars, 7 X rail front plate, 8 X HM12 / BF12 pads |
| **Lathe** | 21 Z stub shaft, 23 X stub shaft |
Process per part is the likely one from the table; step 4 confirms it. The owner's parts still get a drawing (for himself), but no RFQ.

## What is left, in order
1. **Freeze the layout. Done 25 Nov:** V4 frozen (D-324), Z fold with a stub shaft (D-325), X fold with a motor plate (D-326). X pulley on a stub shaft as Z (D-327). Open from the folds: belt margin (D-322); pulleys, belts, bearings not priced.
2. **Finish the model** (task 27 Task 7, D-320, D-325, D-326): replace the envelopes (rows 8 to 12, 19) with real parts, model the X HM12-60-V and its pad, both folds (rows 20 to 23, vendor pulley `cad/vendor/htd5m_20t_15.step`), set the material of every body, and give every hole a fastener (or a line in `bom.csv`). Clash check at all axis ends.
3. **Assembly check.** Write the order the parts go together in, with the key for every screw (the D-215 lesson: tie rods and nuts can block keys). Include when the beam is filled with EG (D-310) against when its tapped holes and the D-323 spacer screws go in.
4. **Make-ability check, part by part.** Stock size from a real supplier list, which faces need grinding or milling and which stay as rolled, tolerances only where they matter (rail seats, dowel holes H7, bearing seats), through or tapped, thread depth. Split the parts by process (laser, saw and drill, CNC mill, grind) because that decides which shops to ask.
5. **Drawings and STEP.** One Fusion drawing and one STEP per part, part numbers matching `bom.csv`, quantity and material in the title block. Then the cover sheet.
6. **Send for quotes** (owner). Shops and how many to ask: owner's call.

## Timing
Machined parts typically take a few weeks after an order, so the pack should go out around mid-December for parts to arrive near wave 1. Not confirmed with any shop.

## Budget warning
Phase 1 is already **£359.80 over** (£4,559.80, 25 Nov) and most made-to-order parts above are **not priced**. The quotes will add to that. The owner may want to decide which parts they make themselves before the RFQ goes out.

## Questions for the owner (not decided)
- ~~Is V4 frozen?~~ Yes (D-324).
- ~~X pulley on a stub shaft as Z?~~ Yes (D-327).
- ~~Which parts go to a shop, and which do you make or cut yourself?~~ Simple parts himself (D-329).
- ~~ATC parts in this RFQ?~~ No, wave 1 only (D-328).
- ~~One shop for everything, or split by process?~~ Split by process (D-330).

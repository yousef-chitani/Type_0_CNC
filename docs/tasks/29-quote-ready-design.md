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
| 8 | X HM12 pad 90 x 60 x 20 + X BF12 pad 50 x 80 x 20 | 1 + 1 | steel (G11) | surface grind, drill, tap, counterbore | **done (D-320, D-332): X HM12-60-V on 90x60x20 pad (6.5x5.5 flange relief), X screw 865 mm** |
| 9 | X nut bracket 150->80 x 145 x 20 | 1 | 6082 | CNC mill | **done (D-333): tapered plate, 4 x M6 + 2 x Ø6 dowels through Z plate** |
| 10 | ~~X motor bracket 10~~ | — | — | — | **removed from model (D-320)** |
| 11 | Beam end caps 120 x 120 x 5 (G12) | 2 | steel | owner saw & drill (or laser) | **done (D-320, D-335): R16 corners, 4 x M5 x 16 each + silicone** |
| 12 | Y motor plate 80 x 155 x 10 | 1 | mild steel | laser, tap 4 x M5 | **done (D-335): Ø38.5 pilot, 4 x M5, 4 x Ø9** |
| 13 | Nut housing spacers 52 x 40 x 5 | 2 | mild steel | laser | **done (D-335): 4 x Ø5.5 holes, steel set** |
| 14 | Z fixed plate 150 x 442 x 20 | 1 | 6082 | CNC mill | **done (D-333): 9 old v3 holes plugged; V4 block, nut-bracket & riser holes cut** |
| 15 | Z moving plate 150 x 200 x 20 | 1 | 6082 | CNC mill | **done: block & nut holes + screws modelled** |
| 16 | Z risers 25 x 15 x 350 | 2 | 6082 | mill | **done: 6 x Ø5.5 + 2 x Ø6 dowel holes each** |
| 17 | Rear shear plate 10 x 200 x 445 | 2 | mild steel | laser | real (D-323) |
| 18 | Beam rear spacer 80 x 25 x 200 | 2 | bright steel | saw, drill, countersink | real (D-323) |
| 19 | Drip skirts 164.5 x 67 x 3 | 4 | PETG | **3D printed on P1S (no RFQ, D-335)** | **done (D-335): side-mounted with 8 x M4 x 10, clears Y blocks** |
| 20 | Z fold plate 70 x 142 x 20 (2 x 6000-2RS seats, 8 mm motor wing) | 1 | 6082 | CNC mill | **done (D-325, D-331)** |
| 21 | Z stub shaft Ø10 x 68 (Ø14 x 1.5 shoulder) | 1 | bright steel | lathe | **done (D-325, D-331): identical to row 23** |
| 22 | X fold plate 70 x 142 x 20 (identical to row 20) | 1 | 6082 | CNC mill | **done (D-326, D-331): identical to row 20** |
| 23 | X stub shaft Ø10 x 68 (identical to row 21) | 1 | bright steel | lathe | **done (D-327, D-331)** |
| 24 | Tray bottom sheet 500 x 670 x 3 (F28) | 1 | mild steel | laser | **done (D-335): 12 x Ø6.6 holes for M6 T-nuts** |
| — | ATC hub block, stub shaft, fork disc (Phase 2) | — | — | — | left out of this RFQ (D-328) |

**Whole model:** every body now has its material set in `Type_0_v4` (`Steel`, `Aluminum 6061` for 6082/6063, `Aluminum 5083 87 Cold Formed`, `Stainless Steel`, `ABS Plastic` for printed PETG, `Rubber`, `Granite` for EG fill). Drawings state exact alloy (`6082-T6`, `S275JR`, `EN1A` / bright steel).

## Who makes what (D-329, D-330, D-335, 26 Nov)
| Pack | Parts (row numbers above) |
|---|---|
| **Owner (saw, drill, tap)** | 1 base end plates, 5 uprights (if the joint faces need milling they move to the CNC mill pack: step 4), 6 beam, 11 beam end caps (`G12`), 18 beam rear spacers |
| **Owner 3D print (P1S, PETG)** | 19 drip skirts (4 pieces, side-mounted, D-335) |
| Supplier cut and tap (KJN) | 2 base profiles |
| **Laser (mild steel only, no bending)** | 12 Y motor plate (10 mm; owner taps 4 x M5), 13 nut housing spacers (5 mm, qty 2), 17 rear shear plates (10 mm, qty 2), 24 tray bottom sheet (3 mm, `F28`) |
| **CNC mill (6082-T6)** | 4 table plate, 9 X nut bracket, 14 Z fixed plate, 15 Z moving plate, 16 Z risers (qty 2), 20 & 22 Z/X fold plates (identical, qty 2) |
| **Surface grind (steel)** | 3 Y rail seat bars (qty 2), 7 X rail front plate, 8 X HM12 pad (`90x60x20`) & X BF12 pad (`50x80x20`) |
| **Lathe (steel)** | 21 & 23 Z/X stub shafts `Ø10 x 68` (identical, qty 2) |
Process per part is the likely one from the table; step 4 confirms it. The owner's parts still get a drawing (for himself), but no RFQ.

## What is left, in order
1. **Freeze the layout. Done 25–26 Nov:** V4 frozen (D-324), Z and X belt-folded at 75 mm centres (`HTD 250-5M-15`) with `2 x 6000-2RS` bearings and identical `Ø10 x 68` stub shafts (D-325 to D-327, D-331); belt margin checked (Optibelt 5M-15 working pull 570 N vs 189 N Z / 251 N X stall, 2.3–3.0x margin, D-322).
2. **Finish the model. Done 26 Nov** (`docs/v4-model.md`, timeline 320, 0 unhealthy, 464 visible bodies, **not saved** — owner saves `Type_0_v4`): X HM12-60-V on `90 x 60 x 20` pad + custom 865 mm X screw (D-320, D-332); Z and X 75 mm folds with vendor `htd5m_20t_15.step` pulleys (D-331); all envelopes replaced (D-333 to D-335); table `9 x 6` M6 blind grid + 4 x Ø8 H7 dowels (D-334); all body materials set; every joint hole given a modelled fastener; 9-pose clash check clean across all axis limits and ATC pickup. Task 27 Task 7 docs (`docs/v4-pour.md`, `docs/requirements.md`, `docs/v4-sizes.md`) and D-336 (`2 x 4.66 kg` Ampreg 30) done.
3. **Assembly check (next).** Write the order the parts go together in, with the key for every screw (the D-215 lesson: tie rods and nuts can block keys). Include when the beam is filled with EG (D-310, `docs/v4-pour.md`) against when its tapped holes and the D-323 spacer / front-plate / pad screws go in.
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

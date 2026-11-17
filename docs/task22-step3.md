# Task 22 step 3: lengths, LiMo basket, `bom.csv` change list (17 Nov 2026)

**A draft for the owner. Nothing here is decided and `bom.csv` is unchanged.** Sources: `moving-gantry-sketch.md` (`cad/v2/out/gantry_sketch.json`), D-136 to D-149, `limo-basket.txt`, `price-check-task-16.md`.

## 1. Lengths

| Part | Length | Needed (sketch) | Decided? | Under LiMo's 950 mm (DDP sea)? |
|---|---|---|---|---|
| Y rails | 2 × 600 (one set) | 588 | yes, D-141 | yes |
| Y screws | 2 × 600 | 572 | yes, D-141 | yes |
| X rails | 2 × 600 (one set) | 400 work + 150 block pitch + block + 20 | **no: sketch** | yes |
| X screw | 700 | 653 (400 + the same 253 end allowance as now) | **no: sketch** | yes |
| Z rails, Z screw | 350, 350 | unchanged (D-136) | yes | yes |

- Longest part 700, so all ship DDP sea.
- A LiMo rail set is 2 rails + 4 blocks. Y is one 600 set (one rail per wall), X one 600 set: **2 sets of 600 in all**.
- Y screw margin is small (600 bought, 572 needed).

## 2. Revised LiMo basket (C5)

**Prices are not re-checked.** LiMo still returns 403 to curl (JavaScript bot check, 17 Nov 2026, as on 15 Nov). The prices below come from the owner's saved pages and checkouts of 17 Nov 2026 (`price-check-task-16.md`). Rate: **1 USD = £0.75767** (ECB via frankfurter.app, 16 Nov 2026, curl).

| # | LiMo item | qty | $ each (17 Nov) | $ line | £ after 10OFF, ex shipping |
|---|---|---|---|---|---|
| 1 | DFU1605 Double-nut Ball Screw Set C5, Steel House & C5 BKBF12, **700 mm** (X) | 1 | **not known** | | |
| 2 | same, **600 mm** (Y1, Y2) | **2** | 141.57 | 283.14 | 193.07 |
| 3 | same, 350 mm (Z) | 1 | 111.57 | 111.57 | 76.08 |
| 4 | Linear Guide Set HGH20CA, **600 mm** (X and Y) | **2** | **not known** | | |
| 5 | same, 350 mm (Z) | 1 | 35.76 | 35.76 | 24.38 |
| 6 | HM12-60, C7 (Z) | 1 | 19.14 | 19.14 | 13.05 |
| 7 | D25L35 coupling (Z, Y1, Y2) | **3** | 3.21 | 9.63 | 6.57 |
| 8 | HM12-60, C7 (Y1, Y2): **only if question 3 is "HM12-60"** | 2 | 19.14 | 38.28 | 26.10 |

- **No total and no shipping yet.** Lines 1 and 4 have no price in the repo. Shipping is set at checkout by weight ($89 and $129 were for other baskets).
- Out of the D-136 basket: the 850 set, the 800 and 500 rail sets.

## 3. `bom.csv` change list (proposed)

**Motion**

| Line | Now | Proposed | Price |
|---|---|---|---|
| M01 | Y rail set 500 | **Y rail set 600** | LiMo, not known |
| M02 | X rail set 800 | **X rail set 600** | LiMo, not known |
| M03 | Z 350 | unchanged | |
| M05 | 3 sets X 850 / Y 600 / Z 350 | **4 sets: X 700 / Y 600 × 2 / Z 350** | 600 and 350 known, 700 not |
| M06, M07 | 3 | **4** (in the sets) | |
| M08 | coupling × 1 (Z) | **× 3 (Z, Y1, Y2)** | $3.21 each less 10 % |
| M09 | 2 motor + driver sets (X, Y) | **3 sets (X, Y1, Y2)** | £51.34 + £10.03 UK warehouse, **5 Nov, not re-checked** (StepperOnline also blocks curl: JS cookie check). Not known whether the £10.03 is per set or per order |
| M13 | Z mount HM12-60 | unchanged | |
| new | 2 Y motor mounts (D-142) | question 3 | |
| M15 | 4 HTD pulleys (X, Y) | **2 (X only)** | £3.92 each "free shipping for 4": re-check for 2 |
| M16 | belts 375 (X) + 3 × 525 (Y) | **375 (X) only** | £3.85 + £1.54 shipping (5 Nov) |
| M17 | X outboard bearing | unchanged (X stays belt-folded, D-107) | |
| M12 | 6082 lot incl. X/Y motor plates | Y motor plates out; Y brackets in if question 3 is "plate" | re-cut list needed |

**Frame (portal casting out, tub in)**

| Line | Now | Proposed |
|---|---|---|
| F20 | portal joint bars 40 × 20 | **out** (−£13.50) |
| F08 | M12 rod 5 × 1 m + 100 nuts (the portal's 4 joint rods, D-132, + spares) | question 6 |
| F09 | conduit for M12 bolt sleeves | question 6 |
| F07 | 40 × 10: Y rail bars 2 × 500 + plates + pads. 25 × 10: X rail bars 2 × 780 + ATC bar | **Y rail bars 2 × 600** (cast-in seats, D-115, D-148). **X rail bars out?** (X rails now on the JLC beam face, machined): question 5 |
| F10 | MDF: base floor + gantry floor | one tub mould (floor about 930 × 670): one sheet should still do. No price change |
| F01 | Ampreg kit 22.68 kg | unchanged: tub 14–15 kg, about 7–8 kg left for seats, grout, test prisms (D-139) |
| X10 | square, "for squaring the portal" | keep; note changes to squaring the gantry |

**Gantry (new, unpriced until a JLC STEP quote, step 4)**

| New line | What |
|---|---|
| G01 | Beam: JLC one-piece 6061 U channel 150 × 130 × 10, 890 long, rail faces and holes machined (D-147) |
| G02 | Back plate 6061, bonded and bolted, with fill ports (D-147) |
| G03 | 2 foot blocks 268 × 140 × 40, 6061, pocketed, with the 15 mm step for the Y nut housing (D-140) |
| G04 | Bonding adhesive and bolts for G02 (question 7) |

**Electrical**
- Mesa 7i76EU: channel 3 becomes **Y2** (D-137); the Phase 2 wheel moves to channel 4 on TB3. No part change.
- One more CL57T driver on the 48 V supply (E04, 480 W): in M09.
- Question 8: a home sensor for Y2 (each Y motor homes on its own switch to square the gantry). E10 has 5 LJ12A3 now (4 homing + 1 ATC).
- E14 cable chain: length still TBD; the gantry needs a Y chain along one wall.

**Budget:** Phase 1 limit £4,200; priced total £3,908.22 (D-136). The JLC parts (G01–G03) and LiMo lines 1 and 4 are not priced, so no new total.

## 4. Questions for the owner

1. **X lengths:** X rails 2 × 600 and X screw 700, as in the sketch? Yes or no.
2. **Missing LiMo prices:** please save the LiMo pages (or note the prices) for the **C5 set 700 mm** and the **HGH20CA set 600 mm**, and do a new checkout to SA2 with the basket above (DDP sea price). Curl is blocked.
3. **Y motor mounts (2):**
   - (a) a plate bracket from the 10 mm 6082 plate (M12), motor coaxial behind the set's own C5 BK12 on the levelled seat (D-140); or
   - (b) LiMo HM12-60 × 2 ($38.28): it has its own BK12 (C7), so the set's C5 BK12 is spare and the seat changes, and its holes are 49.5, not the motor's 50 (same problem as Z).
   - My pick: (a).
4. **M09:** 3 sets from StepperOnline, price re-checked by you at order time (curl is blocked)? Yes or no.
5. **F07 X rail bars:** drop them (the X rails bolt straight onto the machined beam face)? Yes or no.
6. **F08, F09:** drop them with the portal joint, or keep for something else (lifting points, hold-downs)?
7. **Back plate bonding:** Ampreg 30 from the kit, or a structural adhesive (unpriced)?
8. **Y2 home sensor:** add a 6th LJ12A3 to E10? Yes or no.
9. **Y drive stub:** the standard BK12 end (Ø10 × 15) goes straight into the coupling, so no Y stub drawing is needed (only X). Agree?
10. **Edit `bom.csv`** with the agreed lines (unknown prices left blank), and re-run the generators? Yes or no.

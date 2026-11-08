# Price check task 12: parts changed by the full CAD assembly (D-104 … D-110)

**Project:** Type 0 CNC. Buyer in **Swansea, SA2**. **Vendor policy (D-82/D-84):** no eBay. Use the vendors already in the order: **AliExpress, Aluminium Warehouse, The Metal Store, RS, Screwfix, B&Q**. These go in **order wave 2 (15 Feb 2027)**, except M12 (wave 4). Background: `docs/assembly.md`.

## Rules
1. Only record prices you can **see on a live product page**, with the size/option selected. Never estimate or convert.
2. Record price as listed, VAT basis, pack size, shipping and delivery estimate.
3. **AliExpress:** ask the person to log in themselves first, and wait. Never type, read or store their password or codes.
4. Do not add to basket, check out, buy or contact sellers. If a page asks for a human check, ask the person.
5. Compare with **Current** and report the delta: **OK** (≤ 10% or £5 above), **PREMIUM** (more), **SAVING** (cheaper).
6. The product must match the spec. Say so if it only partly matches.

## Lines

| ID | Item | Spec | Current |
|---|---|---|---|
| M05 | DFU1605 ballscrew kits, same METALWORK listing (1005010046279521) | Lengths **X 850**, **Y 600**, Z 350 (the assembly needs X 823 and Y 582 overall); kit with BK12/BF12 and nut housing. Note the shipping (per kit or per order) | £214.81 for X 750 / Y 450 / Z 350 |
| F07a | Steel flat bar 40 × 10 | Bright or black mild steel, **2 m** (or 2 × 1 m). The Metal Store first | £36.00 for 3 m |
| F07b | Steel flat bar 25 × 10 | Bright or black mild steel, **2 m**. Same vendor as F07a | none |
| M12 | 6082 aluminium plate, Aluminium Warehouse custom cut | 20 mm: **180 × 400** and **140 × 200**. 25 mm: **52 × 52**. 15 mm: **2 × 25 × 350**. 10 mm: **2 × 150 × 120** (motor plates/brackets). Same order as M11 (check free delivery over £150 ex VAT) | £85.85 for 180 × 160 + 320 × 140 (20 mm) |
| M13 | NEMA 24 motor mount for the Z motor | Mount for a 60 mm closed-loop stepper with **50 mm hole spacing** (StepperOnline 24HS34; NOT the usual 47.1 mm NEMA 24 pattern), 38.1 mm pilot, about 45–50 mm long for a D26 coupling. Say if only 47.1 mm versions exist | £55.16 for 3 brackets |
| M15 | HTD-5M timing pulleys | **20 teeth, 15 mm belt width, 10 mm bore**, with set screws. Quantity **4** | none |
| M16 | HTD-5M closed timing belts | **15 mm wide**, pitch length about **375 mm** and about **525 mm** (give the nearest sizes each side, e.g. 370/375/380 and 520/525/535) | none |
| M17 | Flange bearing 10 mm bore | 2-bolt flange (KFL000 or similar), **10 mm bore**. Quantity 1 | none |

## Reply block

```
ID | vendor | price as listed (currency, VAT basis) | quantity it covers | stock / shipping | product URL | all-in £ | current £ | delta | notes (spec match)
```
Finish with the wave 2 total and the M12 (wave 4) total.

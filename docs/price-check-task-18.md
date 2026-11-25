# Price check task 18: every BOM line still needing a price (25 Nov 2026)

**Project:** Type 0 CNC. Buyer in **Swansea, SA2**. No eBay. Only prices seen on a live page (or given by the owner), with the date, VAT basis, pack size and delivery. Don't buy.

Taken from `docs/bom.csv` after D-318. Dropped lines, printed parts and things the owner already has are left out. "Blank" means no price at all; "partial" means a price is there but part of it is missing or stale.

## A. ATC (Phase 2), changed by D-317 and D-318
| Line | What to price | State |
|---|---|---|
| A10 | SHF12 shaft support, flange type, bore 12 (the new hub). Also get its drawing: flange size, hole pattern, body length | blank (new) |
| A11 | Fork disc, laser-cut 6 mm 5083, 1 off, about 300 across (12-gon), spoked. Needs a DXF first | blank (new) |
| A06 | 6082 stock for the hub block, about 110 x 170 x 110 (plate or bar) | partial: price is for the old stock list |
| A03 | NEMA 17 about 40 long (42 x 42 x 40), no encoder, 5 mm shaft, plus a 48 V driver | partial: price is for the old closed-loop kit |
| A08 | GT2 6 mm: 20T bore 5, **60T bore 8**, closed belt about 200 (100 teeth) | partial: 7 Nov price, bore and belt length not checked |
| A06, A09, A10 | ATC screws: 4 x M8 (block to end plate), 4 x M4 (FK12 to wall), 4 x M3 (motor), 4 x M5 x 12 (SHF12 to disc), 1 x M5 x 10 (flag), 2 x M3 x 10 (sensor sleeve), 24 x M4 (fork feet to disc) | blank |

## B. Phase 1 lines with no price
| Line | What |
|---|---|
| X18 | Gantry and roller screws not in X03 to X17 (redo the list from the V4 model) |
| X20 | Rail screws M5 x 16 socket cap, 44 (50 pack) |
| X21 | Joint screws added in the CAD (redo from the V4 model) |
| F27 | Base end plate bolts M16 socket cap |
| F28 | Pocket bottom sheet and sealing (material not chosen yet) |
| F30 | Shop surface grinding: Y rail bars, X front plate, X screw pads (owner gets the shop price) |
| F31 | Y screw bellows covers (2) |
| F32 | Y rail drip skirts (sheet and bending); wipers are printed |
| F33 | X screw bellows covers (2) |
| G08 | Dowels for the upright joints (4) |
| G09 | Upright and beam bolts M12 socket cap |
| G10 | Upright joint faces: ground or epoxy-shimmed |
| X23 | Rail bar fixing: M8 socket cap screws and T-nuts |
| X24 | Delivery: KJN (F25) and K I Metals (F26, F29, G01, G07, G11) |
| X25 | Machining of the V4 steel: counterbore, tap, ream (end plates, uprights; F26 X+ now gets 4 x M8 too) |

## C. Phase 1 lines with a partial or stale price
| Line | What is missing |
|---|---|
| M05 | LiMo DDP sea shipping (Checkout7 figure, not re-checked) |
| M09 | NEMA 24 kits: re-check at order time (5 Nov price) |
| M12 | 6082 Z plates and risers: Aluminium Warehouse not re-checked (429); the priced pieces are too small for 442 x 150 and 200 x 150 |
| F26, G11 | K I Metals: read from the Store API only; open the page and confirm |
| G01 | Beam SHS 120 x 120 x 8, 890: delivery to SA2 not known (X24) |
| G07 | Uprights: drilling and tapping not priced (X25) |
| F01 | Ampreg 30: V4 needs about 7 of 22.68 kg; a smaller pack is not priced (owner kept the full kit; delivery to SA2 not known) |
| F07 | Flat bar 40 x 10 + 25 x 10: may not be needed in V4 (up to £54.90 saving) |
| X13, X14 | Riser bolts: may drop in V4; if kept, re-price M6 x 20 (8) and M6 x 30 (6) |
| E09 | MCBs and main isolator not priced (EMC filter is) |
| E10 | AliExpress shipping for 6 sensors (priced for 5) |
| E14 | Shielded motor cable not priced; chain length to re-plan for V4 |
| P05 | Push-fit fittings not priced (Phase 2) |

## How
- Shopify and WooCommerce pages: curl (`/products.json`, `/wp-json/wc/store/products`). LiMo, Screwfix and RS block curl: the owner's own browser session.
- Record each price in `docs/bom.csv` with the date and the source page, then run the generators (`docs/tasks/README.md`).

## Results (25 Nov 2026, curl only)

### Screws, washers, dowels: Westfield Fasteners (westfieldfasteners.co.uk)
Read from the site's own quantity price calculator (the page calls it; `cgi-bin/main2.pl?sub=calculate`). Prices are for the quantity shown, **ex VAT / inc VAT**. Small sizes are sold only in set multiples. **Delivery:** free on UK orders over £40 ex VAT, else £3.50 at least. All in stock.

| Line | Item | Qty | Ex VAT | Inc VAT | Note |
|---|---|---|---|---|---|
| X20 | M5 x 16 socket cap, A2-70 (WF2370) | 44 | £4.22 | **£5.06** | |
| F27 | M16 x 40 socket cap, 12.9 bright zinc | 8 | £7.44 | **£8.93** | length is Claude's proposal (KJN tapped depth not known). A2: £9.62 inc |
| F27 | M16 washer form A, A2 | 8 | £3.25 | **£3.90** | |
| G09 | M12 x 60 socket cap, 12.9 BZP | 8 | £6.51 | **£7.81** | lengths are proposals, from the model |
| G09 | M12 x 35 socket cap, 12.9 BZP | 4 | £3.00 | **£3.60** | |
| X23 | M8 x 30 socket cap, 12.9 BZP | 16 | £3.76 | **£4.51** | length not set anywhere: M8 x 30 is Claude's proposal (20 bar + T-nut). A2: £5.76 inc |
| G08 | Dowel Ø10 m6 x 30, DIN 7, **A1 stainless** | 4 | £4.97 | **£5.96** | not hardened: Westfield lists only stainless dowels. Hardened steel not found by curl |
| A06 (ATC) | M8 x 30 socket cap, A2 (block to end plate) | 4 | £2.56 | £3.07 | length is a proposal (20 flange + 15 tapped) |
| A10 (ATC) | M5 x 12 socket cap, A2 | 10 (min) | £2.16 | £2.59 | 4 needed |
| A09 (ATC) | M5 x 10 socket cap, A2 (flag) | 10 (min) | £2.50 | £3.00 | 1 needed |
| A09 (ATC) | M3 x 10 socket cap, A2 (sensor sleeve) | 20 (min) | £2.06 | £2.47 | 2 needed; 4 more for the motor if M3 x 10 fits |

Not priced (no length set): 4 x M4 FK12 to wall, 4 x M3 motor, 24 x M4 fork feet. Phase 1 lines above (X20, F27, G09, X23, G08) together: £39.77 inc, £33.15 ex, so on their own they pay £3.50 delivery; with the ATC screws (£11.13 ex) the order passes £40 ex and delivery is free.

### K I Metals (kimetals.co.uk): product pages read by curl, 25 Nov 2026
The page prices match the Store API figures used in the BOM (per metre).
| Line | Item | Page price per metre | BOM figure | State |
|---|---|---|---|---|
| F26 | Flat bar 90 x 20 (kim151115) | £34.74 ex / £41.69 inc | 2 x 670 = £46.55 ex / **£55.86 inc** | **confirmed** |
| G11 | Flat bar 160 x 20 (kim151153) | £61.77 ex / £74.12 inc | 950 = £58.68 ex / **£70.42 inc** (BOM rounding) | **confirmed** |

Both pages also show: free delivery over £150 + VAT (heavy/oversize exclusions), 2 cuts per length free then £1 a cut, and **drilling from £4 to £9 per hole** (6, 8, 10 ... mm; no tapping or counterboring offered). That is the only machining price seen for X25 / G07.

### StepperOnline (A03, M09): blocked after one page
The first page read gave **17HS16-2004S1** (NEMA 17, 42 x 42 x 40, 0.45 Nm, 2 A, 5 mm shaft, 1 m cable): **$9.13** (US dollars as served to curl; VAT basis and warehouse not shown). Every later page (DM542T driver, the M09 NEMA 24 kit) returned a JavaScript bot check. Not passed. A03 and M09 need the owner's browser.

### KJN T-nut (X23): page confirmed
M8 T-nut KJN530287: £0.36 ex / £0.43 inc each, 3903 in stock (page, 25 Nov 2026). 16 = £6.88 inc.

### Recorded in `docs/bom.csv` (25 Nov 2026)
X20 £5.06, F27 £12.83 (screws + washers), G09 £11.41, G08 £5.96, X23 £11.39 (16 T-nuts + 16 screws, proposed). F26 and G11 confirmed, unchanged. ATC screw prices are in the notes of A06, A09, A10 (Phase 2, not in the total). **Phase 1 priced total: £4,416.08 to £4,462.73 (+£46.65), £262.73 over the £4,200 budget.** None of these were priced before, so nothing is "dearer" than an old price.

### Not priced, and why
| Line | Why |
|---|---|
| A10 SHF12 | Simply Bearings (Shopify) rate-limited (429); LiMo 403. Drawing not got |
| A06, M12 6082 stock | Aluminium Warehouse rate-limited (429, as on 20 Nov) |
| A03, M09 | StepperOnline bot check after the first page |
| A08, A09, E10, E14, P05, E09, F31, F33 | AliExpress: owner's browser |
| A11 | needs the DXF and a laser-cutter quote |
| M05 | LiMo 403: owner's browser |
| X18, X21 | the screw lists must be redone from the V4 model first |
| F28 | sheet material not chosen |
| F30, G10, X25 | shop quotes (owner). K I Metals drilling £4 to £9 a hole is the only figure |
| X24, G01 delivery | shown only at checkout |
| F01, F07, X13, X14 | owner decisions (smaller pack; may drop in V4) |
| F32 | sheet and bending: no supplier chosen |

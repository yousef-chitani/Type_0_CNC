# Price check task 17: lines left after the 20 Nov 2026 repricing

**Project:** Type 0 CNC. Buyer in **Swansea, SA2**. No eBay. Only prices seen on a live page (or given by the owner), with the date, VAT basis, pack size and delivery. Don't buy.

These lines could not be priced by curl on 20 Nov 2026. LiMo returns 403, Aluminium Warehouse rate-limited (429), and Screwfix and RS block curl.

## Owner: LiMo basket (needs your login)
The basket still holds the Checkout7 lines. Change them, then save a checkout and report the line prices and the DDP sea shipping.

| Change | Why |
|---|---|
| One of the 2 × HGH20CA **600** sets → HGH20CA **550** set (keep one 600 set for X) | D-175: Y rails 550 (M01) |
| DFU1605 C5 Y screws 600 × 2 → **650** × 2 | D-175: Y screws 650 (M05) |
| Coupling D25L35: qty **4** | D-182 (M08) |

## Owner: Dyfed Steels (phone 01554 772 255)
- **G01:** SHS 120 × 120 × 8, cut to **775**. They list it (27.89 kg/m). Ask for the price, the cut charge, and collection or delivery to SA2.
- Same call, for G05 later: they list 120 × 60 × 3 RHS but not 75 × 50 × 3.

## Any session (curl, slowly): Aluminium Warehouse, M12
Custom cuts, 6082. Retry `https://www.aluminiumwarehouse.co.uk/products/20-mm-6082-aluminium-plate.js` (Shopify) after a long pause.

| Piece | Thickness |
|---|---|
| 442 × 150 (Z fixed plate) and 200 × 150 (Z moving plate), or one piece both come from | 20 mm |
| 100 × 100 (X nut-housing spacer 52 × 52; check it is still used) | 25 mm |
| 350 × 100 (Z rail risers 2 × 25 × 350) | 15 mm |

## Owner or a session: X18 screws (Screwfix, B&Q, Amazon)
A2 socket cap DIN 912 unless stated: 24 × M5 × 8, 8 × M5 × 10, 8 × M6 × 8, about 34 × M6 × 12, 12 × M6 × 50, 2 × M4 × 8 pan head, 3 × M5 threaded rod (185 each) + nuts, 4 × Ø8 h6 dowel pins (24 to 30 long). Packs are fine; give the pack size.

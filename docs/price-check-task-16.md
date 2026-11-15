# Price check task 16: HL Motion (hlmotion.com) for all motion parts from one seller

**Project:** Type 0 CNC. Buyer in **Swansea, SA2, UK**. The owner wants the rails, ballscrews and their accessories from **one seller** (16 Nov 2026). Site to check: **https://hlmotion.com/** (owner's pick). The full list is `docs/motion-parts-one-seller.txt`: read it first, it is the spec.

## Method: curl first
The owner asked for curl (the browser uses many tokens). Fetch with `curl -sL --compressed` and a plain browser user agent; pull titles, prices and options out with a short Python script. If the site is Shopify, add `.js` to a product URL for the variants as JSON (or `/products.json`). WooCommerce: try `/wp-json/wc/store/products?search=...`. Do not spoof headers past a bot block: if curl is blocked, say so and use the built-in browser with one small `get_page_text`.

## Rules
Only prices seen on a live page, with the option (length, preload, class) selected; note the currency, VAT basis, shipping to the UK and lead time. Don't buy or add to a basket. The item must match the spec. If a price needs a quote, write down what the quote form asks for and draft the message (the owner sends it).

## Lines

| ID | Item | Spec (short; full in `motion-parts-one-seller.txt`) | Qty | Now (Nov 2026, inc VAT) |
|---|---|---|---|---|
| M01–M03 | HGR20 rails + HGH20CA blocks | X 2 × 800, Y 2 × 500, Z 2 × 350 mm; 2 blocks per rail (12) | 6 rails | £207.37 (AliExpress) |
| M05–M07 | DFU1605 ballscrews + BK12/BF12 + DSG16H housing | Overall X 850 / Y 600 / Z 350; ends machined for BK12/BF12; X drive end Ø10 stub about 35 mm | 3 | £229.01 (AliExpress) |
| M15 | HTD-5M pulley 20T, 15 mm belt, 10 mm bore | | 4 | £15.68 |
| M16 | HTD-5M 15 mm closed belts | about 375 and 525 mm pitch length | 2 | £14.27 |
| M17 | KFL000 flange bearing, 10 mm bore | | 1 | £4.05 |
| M08 | Coupling 10–10 mm, about D26 × L35 (Z) | | 1 | £7.40 |
| M13 | NEMA 24 motor mount for BK12 (Z) | 4 holes on a **50 mm** square, Ø36 pilot | 1 | £20.63 |
| | **Total to beat** | | | **£498.41** |

## Also find on the site
- Rail accuracy class and block preload offered (C / H, Z0 / ZA), and whether rails come as matched pairs.
- Ballscrew grade (C7 rolled / C5 ground), nut type (DFU preloaded?), backlash, and whether the length given is **overall or threaded**.
- End-machining drawing for BK12/BF12.
- Shipping to the UK (one shipment?), import VAT / duty handling, lead time.

## Reply block

```
ID | product name | price as listed (currency, VAT basis) | option selected | qty | shipping to UK | lead time | URL | all-in £ | spec match / notes
```

## After
Put the results here, compare the all-in total with £498.41, and ask the owner before changing `bom.csv` (D-number next: D-136).

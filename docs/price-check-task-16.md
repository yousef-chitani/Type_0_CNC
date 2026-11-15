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

---

## Results (15 Nov 2026, by curl)

**How:** HL Motion (trading as HLTNC) is a Shopify store. The whole catalogue (677 products) came from `https://hlmotion.com/products.json` (the store's live data: price, options, in stock). Product pages and `/en-gb/` gave **429 (rate limit)** after a few requests; no headers were spoofed. The store sells in **USD only** (no UK market: `/en-gb` is 404). Converted at **1 USD = £0.756391** (open.er-api.com, 15 Nov 2026).

**Shipping policy** (`/policies/shipping-policy`): ships from China by UPS / FedEx / DHL, "about 10–15 days". EU (Poland), US, Russia and Brazil warehouses for some items. **The buyer pays all customs fees, import fees and duty.** No UK shipping price is shown before the basket, so the UK shipping cost is **not known** (adding to a basket is not allowed). Prices are **ex UK VAT**: add 20 % import VAT (plus courier handling fee if the order is over £135).

| ID | product name | price as listed (USD, ex VAT) | option selected | qty | shipping to UK | lead time | URL (handle) | all-in £ (inc 20 % VAT, ex shipping) | spec match / notes |
|---|---|---|---|---|---|---|---|---|---|
| M01 | 2pc HGR20 rail + 4pc HGH20CA | $57.29 | 800 / 2HGR20+4HGH20CA | 1 set | not shown | 10–15 days (China) | `hltnc-2pc-hgr15-hgr20-square-linear-guide-rail-200mm-to-1000mm-4pc-hgh15ca-hgw15cc-hgh20ca-hgw20cc-for-cnc-router-engraving-副本-1` | 52.00 | match; in stock |
| M02 | same listing | $32.80 | 500 / 2HGR20+4HGH20CA | 1 set | not shown | same | same | 29.77 | match; in stock |
| M03 | same listing | $29.81 | 350 / 2HGR20+4HGH20CA | 1 set | not shown | same | same | 27.06 | match; in stock |
| M05–M07 | SFU1605 ball screw, BK/BF standard processing | $11.64–14.25 (500 / 700 / 900); $10.66 (350) | none fits | 3 | | | `hltnc-sfu1605-ball-screw-with-nut-bk-bf-standard-processing-...` (3 listings) | **not sold** | **sold out** (all lengths); **SFU (single nut), no DFU** anywhere on the site; fixed lengths only (no 600 or 850; 900 would need cutting); no X drive-end stub option |
| (M05–M07 parts) | BK12 / BF12 support, C7 | $4.04 / $1.83 | C7 / BK12, C7 / BF12 | 3 + 3 | | | `hltnc-sales-bk10-bf10-bk12-bf12-...` | 15.98 | in stock; useless without the screws |
| (M05–M07 parts) | DSG16H aluminium nut seat | $1.30 | DSG16H | 3 | | | `hltnc-standard-aluminum-nut-seat-dsg12h-dsg16h-...` | 3.54 | in stock |
| (kit) | Ball screw kit BK12 BF12 DSG16H + D25L30 8×10 coupler | $7.81 | BKBF12-DSG-XB | | | | `hltnc-ball-screw-kit-with-bk12-bf12-support-dsg16h-...` | | sold out |
| M15 | HTD-5M pulley 20T 15 mm | | | 4 | | | | **not sold** | no pulleys or belts on the site |
| M16 | HTD-5M 15 mm closed belts | | | 2 | | | | **not sold** | |
| M17 | KFL000 flange bearing | | | 1 | | | | **not sold** | no KFL / pillow-block bearings |
| M08 | LF two-jaw D25L30 plum coupler | $1.36 | 10*10 | 1 | not shown | | `hltnc-lf-two-jaw-d25l30-coupler-...` | 1.23 | close: D25 × L30, spec says about D26 × L35; check the motor-to-screw gap |
| M13 | HM12-60 integrated motor seat (BK12 built in), aluminium | $10.00 (C7) / $14.33 (C5) | HM12-60-V-C7 | 1 | | | `hltnc-hm12-57-aluminum-stepper-motor-seat-...` | | **sold out**; "60" hole pattern not stated (spec: 50 mm square, Ø36 pilot); it replaces the Z BK12 too. The generic "for 60 or Nema24" flange bracket ($3.24) is not a BK12 mount: no match |

**Also asked for:** rail accuracy class, block preload, matched pairs, ballscrew grade / backlash, overall-or-threaded length, end-machining drawing: **none of these are on the site** (descriptions are images or empty; the only grade shown is C7 / C5 on the supports and motor seats). Two odd things: every rail length has the same weight (2,990 g), and the hidden variants read "price includes Partial shipping cost" and "Contact Customer Service for Discounted". The listed prices look like part-price, with the rest charged as shipping at checkout. **Do not trust the low prices until the shipping is known.**

### Comparison with £498.41

- **One seller is not possible here.** HL Motion has the rails, supports, nut seats and a coupler, but **no DFU1605 (or any in-stock 1605 screw), no pulleys, belts or KFL000, and the Z motor seat is sold out.**
- Rails only: **£90.69 ex VAT, £108.83 inc VAT, plus unknown shipping**, against **£207.37** (AliExpress, inc VAT, delivered). Even with £50 shipping it would save about £48, but the accuracy class and preload are unknown.
- Everything HL Motion has in stock that fits (rails, coupler, 3 BK12, 3 BF12, 3 DSG16H): about **£130.58 inc VAT + shipping**. The screws, pulleys, belts, bearing and Z mount would still come from elsewhere, so it is two or more sellers either way.

### Draft message to HL Motion (owner sends; contact page `https://hlmotion.com/pages/contact`)

> Hello. I want to order for a small CNC mill, shipped to the UK (Swansea, SA2):
> 1. HGR20 rails with HGH20CA blocks: 2 × 800 mm, 2 × 500 mm, 2 × 350 mm, 2 blocks per rail (12 blocks).
> 2. Ball screws 1605 with BK12/BF12 standard end machining, overall length (ends included) 850, 600 and 350 mm. Do you have DFU1605 (double nut, preloaded)? If only SFU1605, what is the backlash? The 850 mm screw needs a 10 mm drive-end stub about 35 mm long.
> 3. 3 × BK12, 3 × BF12, 3 × DSG16H, 1 × coupler D25L30 10×10, 1 × HM12-60 motor seat (when back in stock): is its motor face 4 holes on a 50 mm square with a 36 mm pilot?
>
> Questions: What is the total shipping cost to the UK for all of this in one shipment, and how long? Is your "length" the overall length or the threaded length? Please send the end-machining drawing. Rail accuracy class (C or H) and block preload (Z0 or ZA)? Are rail ends cut square and deburred? Thank you.

**Next:** owner decides. Nothing in `bom.csv` changed. If the owner wants the rails from HL Motion: send the message first, then record a decision (D-136) and update `bom.csv` lines M01–M03.

---

## Limo Bearing (limobearing.com), 15 Nov 2026: blocked

The owner asked for limobearing.com by curl, no browser. **Every URL returns 403** with a JavaScript bot check ("Checking your browser before accessing"): `/`, `/products.json`, `/wp-json/wc/store/products`, `/sitemap.xml`, `/robots.txt`. The site runs on Hostinger Website Builder (`server: hcdn`). Curl cannot pass the check without defeating it, so **no prices**. Options: the owner opens the site and copies the prices for the lines above, or asks the seller by email using the HL Motion draft (same questions).

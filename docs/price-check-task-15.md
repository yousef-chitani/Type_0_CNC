# Price check task 15: engineer's square and shim stock (D-132, D-133)

**Project:** Type 0 CNC. Buyer in **Swansea, SA2**. No eBay. Screwfix and B&Q first, then RS / Cromwell / UK tool shops, then AliExpress. Needed by **order wave 3 (1 Mar 2027)**; both are used at assembly (`assembly-steps.md` steps 6 and 8).

## Method: curl first, browser only if curl can't read the page
The browser costs far more tokens. Fetch pages with `curl -sL --compressed` and a plain browser user agent, then pull out the title and price with a short Python script (Shopify shops: add `.js` to a product URL to get the variants and prices as JSON). For searching, `https://lite.duckduckgo.com/lite/?q=...` works until it rate-limits.

What worked on 15 Nov 2026:
- **curl works:** mqs.co.uk, kaf.ltd (Shopify), cromwell.co.uk product pages, diy.com (title only: the price loads later), hollinbrow.co.uk (no prices: quote only).
- **curl blocked:** RS (403), Amazon (202 page with no content), Bing (bot challenge). Don't try to get round the block. Use the browser for those, and read the page with one `get_page_text` call with a small `max_chars`.

## Rules
Same as price check 14: only prices seen on a live page, with the option selected; give the VAT basis, pack size and delivery; don't buy or add to a basket; the item must match the spec.

## Lines

| ID | Item | Spec | Qty | Found so far (15 Nov 2026) |
|---|---|---|---|---|
| X10 | Engineer's square | **300 mm** long blade, hardened steel, **DIN 875 grade 1 or 2** (or BS 939 grade A/B) stated on the page. Ungraded "precision" squares don't count | 1 | **Mitutoyo 916-227, DIN 875 grade 1, 300 × 200, £62.00 ex VAT (£74.40 inc), MQS** ([page](https://mqs.co.uk/products/try-square-din-875-300x200mm-grade-1-steel-916-227)); delivery at checkout only; MQS minimum order £25 ex VAT. Dearer: Moore & Wright 400/12 grade B, £117.00 ex VAT, Cromwell M&W3421011B |
| X11 | Steel shim stock | Steel or stainless sheet, **0.05, 0.1 and 0.2 mm** (0.02/0.03 and 0.5 mm welcome), about **150 × 150 mm or larger** per thickness: it's cut into 70 × 130 pieces for the portal feet and 40 × 60 for the 3 base pads. An assorted pack is fine | 1 set | **Best UK so far: Cromwell T&A Precision steel pack, 12 sheets 6 × 12 in, 0.001–0.015 in (0.025–0.38 mm), £48.49 ex VAT (£58.19 inc), in stock** ([page](https://www.cromwell.co.uk/shop/materials-maintenance-and-standard-parts/packing-shim/packing-shim-steel-6inw-x-12inl-x-0-001-0-015in-thickness-12-pieces/p/TPN4150001Y)); delivery at checkout only. Dearer: Cromwell stainless pack 0.05–0.50 mm, 150 × 300, 8 pieces, £224.00 ex VAT ([page](https://www.cromwell.co.uk/shop/materials-maintenance-and-standard-parts/packing-shim/stainless-shim-pack-0-05mm-0-50mm-150mmx300mm-8pc/p/PCN4153200L)); RS PRO steel shim 2.5 m roll, £97.80 ex VAT. Arc Euro Trade is closing down; Tracy Tools has no shim; Chronos search needs a browser |

## For the owner: AliExpress check (owner, 15 Nov: the UK prices are too much)

Log in, set delivery to the UK, and for each line note the price with the option selected, the shipping and the delivery date. Search terms in quotes.

| ID | Search | Must say on the page | Beat |
|---|---|---|---|
| X10 | "engineer square 300mm DIN875" or "90 degree square 300x200 grade 1" | 300 mm long blade, hardened steel, **DIN 875 grade 0, 1 or 2** (or "00 / 0 / 1 grade"). A plain "precision square" with no grade doesn't count | £74.40 |
| X11 | "steel shim sheet 0.05mm" (and 0.1, 0.2), or "feeler gauge sheet set" / "shim stock assortment" | Steel or stainless, thicknesses **0.05, 0.1 and 0.2 mm** at least, sheets about **150 × 150 mm or larger** (pieces are cut to 70 × 130). Brass or plastic don't count | £58.19 |
| X03 (task 05) | "M5x20 socket head cap screw 12.9" | **M5 × 20**, socket cap (DIN 912 / ISO 4762), **grade 12.9**, black or zinc, **100 pieces** (or packs that add up to 100). Fallback if nothing good: Screwfix A2 1941T, 2 × 50 at £5.89 | £11.78 |
| X05 (optional) | "steel straight edge 500mm DIN874" or "knife edge straightedge 500mm" | 500 mm, steel, **DIN 874 grade 0, 1 or 2** stated. Already on the list at £115.07 (RS); swap only if graded | £115.07 |

Paste the results in the reply block below.

## Reply block

```
ID | vendor | price as listed (currency, VAT basis) | quantity it covers | stock / shipping | product URL | all-in £ | notes (spec match)
```

## Owner's reply (15 Nov 2026)

| ID | Result |
|---|---|
| X10 | AliExpress, £18.19 ([page](https://www.aliexpress.com/item/1005006022298533.html)). Wins over MQS £74.40 |
| X11 | Owner messaged a seller; expected under £25. Price not final |
| X03 | Screwfix wins: A2 1941T M5 × 20, 2 × 50 at £5.89 = £11.78 (A2, not 12.9: D-134 fallback) |
| X05 | Owner suggests KS Tools 300.0638 precision straight edge 500 mm, Amazon ([page](https://www.amazon.co.uk/gp/product/B007XUELEQ)). Price and DIN 874 grade not given yet |
| — | Owner plans to buy the rails, ballscrews and their accessories from one AliExpress seller: `motion-parts-one-seller.txt` |

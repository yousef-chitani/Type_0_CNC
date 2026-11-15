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
| X10 | Engineer's square | **300 mm** long blade, hardened steel, **DIN 875 grade 1 or 2** (or BS 939 grade A/B) stated on the page. Ungraded "precision" squares don't count | 1 | **Mitutoyo 916-227, DIN 875 grade 1, 300 × 200, £62.00 ex VAT (£74.40 inc), MQS** ([page](https://mqs.co.uk/products/try-square-din-875-300x200mm-grade-1-steel-916-227)); delivery not shown; MQS minimum order £25 ex VAT. Still to check: a grade 2 square for less (Moore & Wright, RS PRO, Verum BS 939 B at B&Q: price not readable by curl) |
| X11 | Steel shim stock | Steel or stainless sheet, **0.05, 0.1 and 0.2 mm** (0.02/0.03 and 0.5 mm welcome), about **150 × 150 mm or larger** per thickness: it's cut into 70 × 130 pieces for the portal feet and 40 × 60 for the 3 base pads. An assorted pack is fine | 1 set | **Too dear so far:** Cromwell Precision Brand stainless pack 0.05–0.50 mm, 150 × 300, 8 pieces, £224.00 ex VAT ([page](https://www.cromwell.co.uk/shop/materials-maintenance-and-standard-parts/packing-shim/stainless-shim-pack-0-05mm-0-50mm-150mmx300mm-8pc/p/PCN4153200L)); RS PRO steel shim 2.5 m roll, £97.80 ex VAT. **Still to check:** AliExpress steel/65Mn shim sheet sets (log in first), Arc Euro Trade, Tracy Tools, Chronos, Amazon UK |

## Reply block

```
ID | vendor | price as listed (currency, VAT basis) | quantity it covers | stock / shipping | product URL | all-in £ | notes (spec match)
```

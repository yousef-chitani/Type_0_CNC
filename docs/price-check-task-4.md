# Price check task 4: parts whose size changed in the layout (for a local Claude session with a browser)

**Project:** Type 0 CNC, a DIY epoxy-granite mill. Buyer in **Swansea, UK**. The layout changed some lengths and sizes. **Goal:** price the new sizes, ideally from the **same listings** as before.

## Rules
1. Only record prices you can **see on a live product page** (select the size/length option and read the price). Never estimate or convert currency.
2. Record price exactly as listed, with currency and VAT basis, shipping to the UK and delivery estimate.
3. Note deal limits (new shopper, "max 1 per shopper") and the normal price.
4. If the same listing does not offer the length, find the cheapest full match elsewhere.
5. **If AliExpress shows a CAPTCHA**, stop and ask the person to solve it in the browser pane, then continue.
6. Do not sign in, add to basket, buy or contact sellers. `NOT FOUND` with the reason if no live price.

## Items

| ID | Item | New spec | Previous listing (price was for old size) |
|---|---|---|---|
| M01 | HGR20 rail kit, Y | 2 × **650 mm** + 4 × HGH20CA (unchanged: re-confirm) | https://www.aliexpress.com/item/1005010242098397.html (£70.85 sale, 1 per shopper) |
| M02 | HGR20 rail kit, X | 2 × **500 mm** + 4 × HGH20CA | same listing (450 mm was £59.05) |
| M03 | HGR20 rail kit, Z | 2 × **350 mm** + 4 × HGH20CA | same listing (300 mm was £55.21) |
| M01-3b | All three in one shop | State whether the 1-per-shopper limit applies across sizes. Also price the Kaiyade listing for 650 / 500 / 350 mm and whether its £79 shipping is per order | https://www.aliexpress.com/item/1005009213173130.html |
| M05 | DFU1605 ballscrew kits | **X 420 mm, Y 550 mm, Z 310 mm** overall length, DFU1605 double nut, machined ends, BK12/BF12, nut housing | https://www.aliexpress.com/item/1005010046279521.html (300/450/500 were £52.99/£58.99/£62.99) |
| M05b | Nut housing drawing | From any DSG16H or DFU1605 housing listing: **height from mounting face to screw centre**, and **total height** | Information only, no price needed |
| A02 | MGN15 rail + MGN15H block | **2 × 550 mm**, 1 block each | https://www.ebay.co.uk/itm/227244866634 (400 mm was £25.99) |
| A04 | SFU1204 kit | **500 mm** + housing + BK10/BF10 + coupling | https://www.aliexpress.com/item/1005006187129418.html (400 mm was £43.39) |
| T01 | Box section steel | **60 × 60 × 3 mild steel, about 12 m** total (e.g. 2 × 6 m, or 4 × 3 m; cut lengths about 1,010 / 700 / 620 mm) | Previous 80 × 80 × 5 £35/m: https://www.ebay.co.uk/itm/128036584011 . Also check local Swansea steel stockholders with online prices |
| E12 | Steel electrical cabinet | **600 W × 400 H × 200 D** mm, IP54 or better, with mounting plate. Fallback **400 × 400 × 200** | Previous 600 × 500 × 200 £92.33: https://www.ebay.co.uk/itm/327345335863 |

## Reply block (output exactly this format)

```
ID | price as listed (currency, VAT basis) | quantity it covers | shipping to UK, delivery estimate | product URL | notes
```

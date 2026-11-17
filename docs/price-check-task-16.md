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

### LiMo DFU1605 ballscrews (owner's saved page, 15 Nov 2026)

The owner saved the product page from a browser ("DFU1605 2005 2505 2510 Double nut ball screw | LiMo", `https://limobearing.com/dfu1605-2005-2505-double-nut-ball-screw`). Prices were taken from the page's own variant data (USD, all `is_available: true`); the price shown on the page, $42.36, matches the 800 mm screw.

**Spec on the page:** 52100 bearing steel, **C7 cold rolled, lead error 50 µm / 300 mm**. Preload: **P1 (no preload, no axial play) by default**; P0 and **P2 (light preload) on request**. Length is **overall length**; custom 10–4,000 mm (pick the nearest standard length, put the exact length in the remark). Standard end machining fits **BK12 + BF12** by default; other machining (the X drive-end stub) by remark plus a drawing emailed with the order number. CAD drawings on the page.

| ID | option | price (USD, ex VAT) | notes |
|---|---|---|---|
| M05 X | DFU1605 & Nut House & Support BKBF12, 900 mm | $54.31 | remark: cut to 850 overall, X drive-end stub Ø10 × about 35 mm (send a drawing; any extra charge not shown) |
| M06 Y | same, 600 mm | $51.74 | standard length |
| M07 Z | same, 400 mm | $46.14 | remark: 350 overall (300 mm is the same price) |
| | **3 kits** | **$152.19 = £115.12 ex VAT, £138.14 inc VAT** | at 1 USD = £0.756391 |

**Shipping (page table, DDP air to the USA; the page says Europe is "similar"):** 2.5–5 kg $39→$69, 5–10 kg $109, 8–14 workdays. The weight of 3 kits is not on the page. For the UK write **"DDP"** in the checkout remark, otherwise it ships DAP and the buyer pays import VAT and the courier fee. Discount codes start at $200 (5 %), so this order does not qualify.

**All-in, inc 20 % VAT on goods + shipping:** **£200.77** if it falls in the 2.5–5 kg band, **£237.07** if 5–10 kg, against **£229.01** now (AliExpress). So it is about the same money, for a stated C7 grade, a stated lead error, zero axial play by default and light preload available. Before ordering: ask the shipping weight and the UK DDP price, whether the X stub costs extra, and ask for P2.

Related products on the same page (not checked against the spec): integrated stepper motor mount $18.86, flexible coupling $2.86, nut housing $3.69, EK/EF supports $9.43. No pulleys, belts or KFL000 seen. **Nothing in `bom.csv` changed.**

### LiMo: rails, Z mount, coupling, housing (owner's saved pages, 15 Nov 2026)

Prices from each page's variant data (USD, ex VAT, all `is_available: true`).

| ID | LiMo product, option | price | notes |
|---|---|---|---|
| M01 | Linear Guide Set HGH15 20 25 30: **HGH20CA, 800 mm** (2 rails + 4 blocks) | $49.38 | preload **ZA (medium) by default**, Z0 / ZB on request; accuracy class **not stated**; holes symmetric to both ends; plugs included; custom length by remark |
| M02 | same, HGH20CA, 500 mm | $40.30 | |
| M03 | same, HGH20CA, 350 mm | $35.76 | |
| M13 | Stepper motor integrated mount bracket **HM12-60, C7** (BK12 built in, C45 steel, deep-groove bearings; C5 = angular contact, $24.86) | $19.14 | the motor hole pattern is **not on the page**: confirm 4 holes on a 50 mm square, Ø36 pilot. Also confirm the coupling fits inside it |
| M08 | Flexible shaft coupling **D25L35**, aluminium, polyurethane spider | $3.21 | bores by remark (D25L35: 4–14 mm), ask 10 × 10 |
| | Aluminium nut housing DSG1605 | $7.38 | already in the DFU kits, not needed |

**Whole LiMo order** (3 DFU1605 kits $152.19 + rails $125.44 + HM12-60 $19.14 + coupling $3.21) = **$299.98**, **$284.98 after the 5 % code `5OFF`** ($200+). Goods alone: **£258.67 inc VAT**.

The rails make it heavy, and no page gives the weight, so the shipping band is not known (page table, DDP to USA, "similar" for Europe):

| shipping | band | all-in £ (inc 20 % VAT on goods + shipping) |
|---|---|---|
| sea, 15–25 workdays | 10–22 kg $99 | **£348.53** |
| air, 8–14 workdays | 10–15 kg $169 | £412.06 |
| air | 15–20 kg $229 | £466.52 |

**Against now:** the same lines (M01–M03, M05–M07, M08, M13) cost **£464.41** from several sellers. LiMo by sea saves about **£116**; by air it is about the same to £2 dearer. Pulleys, belts and the KFL000 (M15–M17, £34.00) still come from elsewhere: LiMo does not sell them.

**Ask LiMo before ordering:** shipping weight and the UK DDP price (sea and air); rail accuracy class (C / H) and whether rails are matched pairs; Z0 instead of ZA is not needed (ZA is fine); HM12-60 motor face (50 mm square, Ø36 pilot?) and coupling fit inside it; X stub extra cost; P2 preload on the screws. `bom.csv` unchanged.

**HM12-60 hole spacing (owner, 15 Nov 2026): 49.5 mm.** The motor (24HS34, drawing A4717) has 50 mm, and the project limit is 50 ± 0.2 mm (`supplier-messages.md` section 4), so **as listed it does not fit**: each hole is about 0.35 mm off on the diagonal. Options: ask LiMo to machine the 4 holes on a 50 mm square (they take custom machining by remark), or open the mount's holes about 1 mm larger and let the pilot do the centring (only if the holes are clearance, not tapped), or make the mount from the 10 mm plate (task 14). Pilot bore still to confirm (must be Ø36 or larger).

### LiMo DFU1605 **C5 ground** (owner's saved page, 17 Nov 2026)

Page: "DFU1605 2005 2505 2510 Double-nut Ball Screw C5 Gound" (`limobearing.com/dfu-double-ball-screw-nut`), prices from its variant data (USD, all available). Spec: 52100 steel, **C5 ground**, **light preload P2 by default** (P1, P3 on request), overall length, custom 10–4,000 mm by remark, standard end machining for BK12 + BF12 unless a note or drawing says otherwise. The page also says LiMo ships **DDP** (duties and taxes paid upfront); below, 20 % VAT is still added as before, so the C5 and C7 figures compare like for like.

**The C5 price is for the screw and nut only.** The C7 price ($152.19) was a kit with the BK12/BF12 supports and the DSG16H nut housing. This page lists no kit. Its related products show "Ball screw bearing support units BK BF" **from $7.71**: that is the cheapest variant on that page, not the BK12/BF12 price, so the supports are still unpriced.

| ID | option | C5 (screw + nut) | C7 kit (screw + supports + housing) |
|---|---|---|---|
| M05 X | 900 mm (cut to 850) | $155.71 | $54.31 |
| M06 Y | 600 mm | $119.71 | $51.74 |
| M07 Z | 400 mm (cut to 350) | $95.71 | $46.14 |
| | 3 nut housings DSG1605 ($7.38 each, separate page) | $22.14 | included |
| | **total** | **$393.27 = £356.96 inc VAT, plus the BK12/BF12 supports (price not known)** | **$152.19 = £138.14 inc VAT** |

So C5 costs about **£219 more than C7** (inc VAT), before the supports.

**Whole LiMo order with C5** (C5 screws + housings $393.27, rails $125.44, HM12-60 C7 $19.14, coupling $3.21 = $541.06). That is over $500, so the 10 % code `10OFF` applies: $486.95. Goods: **£441.99 inc VAT, without the supports.** At 1 USD = £0.756391, with 20 % VAT on goods and shipping:

| shipping (page table) | all-in £ |
|---|---|
| sea 10–22 kg $99 | **£531.85** + supports (£443.21 if the DDP price already includes VAT) |
| air 10–15 kg $169 | £595.39 + supports (£496.15 without added VAT) |
| air 15–20 kg $229 | £649.85 + supports |

With the HM12-60 in C5 ($24.86), add about £4.70. **Against:** £464.41 now (several sellers) and £348.53 for LiMo with C7 by sea. So C5 by sea costs about **£67 more than now** and **£183 more than LiMo C7**, plus the supports. **If LiMo's DDP price already includes UK VAT** (asked in 6a), C5 by sea is £443.21 + supports, about £21 under now before the supports, and LiMo C7 by sea £290.44. Either way C5 costs about £150–185 more than C7, plus the supports. Rate 1 USD = £0.756391 (15 Nov 2026). Phase 1 has £284 headroom (£4,200 − £3,915.58).

**The end drawing on the page** is the same standard machining as task 13's notes: BK12 end Ø10 × 15, M12×1 × 14, Ø12 to 39 from the thread start (so Ø12 × 25); BF12 end Ø10 × 11 with a Ø9.6 circlip groove 1.15 wide at 9.15. Nothing changes there.

**Still missing:** BK12/BF12 support price (C5 or C7 grade) at LiMo, and the checkout shipping to SA2 for sea and air. `bom.csv` unchanged.

### LiMo DFU1605 **C5 set** with C5 BK12/BF12 (owner's second saved page, 17 Nov 2026)

**This replaces the C5 figures above** (they were for the screw alone). Page: "DFU1605 2005 2505 2510 Double-nut Ball Screw Set C5 Gound". The set is **DFU1605 + steel nut housing + C5 BK12/BF12 supports**. Same spec as the C5 screw page: 52100 steel, C5 ground, light preload P2 by default, standard BK12/BF12 end machining unless a note or drawing says otherwise. Lengths go in **50 mm steps**, so 850 and 350 are standard lengths and no cutting remark is needed.

| ID | option | price (USD) |
|---|---|---|
| M05 X | DFU1605 & Steel House & C5 BKBF12, **850 mm** | $171.57 |
| M06 Y | same, **600 mm** | $141.57 |
| M07 Z | same, **350 mm** | $111.57 |
| | **3 sets** | **$424.71 = £385.50 inc 20 % VAT** (C7 kits: $152.19 = £138.14) |

The set's housing is steel, and its size isn't on the page. The CAD uses the aluminium DSG16H, so check the steel housing's size and bolt pattern before ordering. The Z set's BK12 isn't needed if the HM12-60 is used, because the HM12-60 has the BK12 built in.

**Whole LiMo order with C5 sets** (sets $424.71, rails $125.44, HM12-60 C7 $19.14, coupling $3.21 = $572.50; 10 % code `10OFF` → $515.25), at 1 USD = £0.756391 (15 Nov 2026):

| shipping (page table) | 20 % VAT added | if the DDP price already includes VAT |
|---|---|---|
| sea 10–22 kg $99 | **£557.54** | £464.61 |
| air 10–15 kg $169 | £621.07 | £517.56 |
| air 15–20 kg $229 | £675.53 | £562.94 |

With the HM12-60 in C5 ($24.86), add about £4. **Against:** £464.41 now (several sellers, C7 grade from AliExpress) and LiMo C7 by sea £348.53 (£290.44 if VAT is included). So **C5 costs about £209 more than LiMo C7** with VAT added (£174 if VAT is included). With VAT added, it's **£93 more than now**; if VAT is included, it's about the same as now. Phase 1 headroom: £284.42. Still missing: checkout shipping to SA2, and LiMo's answer on VAT (6a). `bom.csv` unchanged.

### LiMo checkout (owner's saved checkout page, 17 Nov 2026, basket A = C5)

**Shipping offered to SA2:**
- **DDP sea, 30–45 workdays, $129.00** (max length 950 mm; our longest is 850);
- DAP air, 7–14 workdays, $239.00, tax not included;
- DDP air, 8–15 workdays, $269.00, duty included.

**The saved basket had two mistakes:**
- **600 mm set × 2** ($283.14); it should be × 1;
- **HM10-60, C7** ($18.86); it should be the **HM12-60, C7** ($19.14), for BK12 / DFU1605.

No discount code was applied either. As saved: $713.79 + $129 = $842.79.

**Corrected** (1 × 600, HM12-60, 10 % code `10OFF` on goods; assumes the code doesn't apply to shipping), at 1 USD = £0.756391 (15 Nov 2026):

| basket | goods after code | + DDP sea $129 | + DDP air $269 |
|---|---|---|---|
| **A, C5 sets** | $515.25 | **$644.25 = £487.30** | $784.25 = £593.20 |
| B, C7 kits (not checked out; code `5OFF`) | $284.98 | **$413.98 = £313.13** | $553.98 = £419.03 |

DDP means the duty is paid by the carrier; the page doesn't say in so many words that UK VAT is included (LiMo's 6a answer will confirm).

**Against £464.41 now:**
- **C5 by DDP sea: £22.89 more**, for C5 ground screws with C5 supports and light preload. Phase 1 would go from £3,915.58 to about £3,938 (headroom left about £262).
- **C7 by DDP sea: £151.28 less.**
- Sea takes 30–45 workdays, so order by mid-December for the wave 2 date (15 Feb).
- Pulleys, belts and the KFL000 (M15–M17) still come from elsewhere.

`bom.csv` unchanged; the owner decides C5 or C7 (D-136).

**Updated checkout (17 Nov 2026):** 1 × 600 now. Shipping: **DDP sea $89**, DDP air $209, DAP air $239 (tax extra). Still HM10-60 ($18.86) and no code: as saved $572.22 + $89 = $661.22. Corrected (HM12-60, `10OFF`): $515.25 + $89 = **$604.25 = £457.05**, £7.36 under the £464.41 it replaces. **D-136: C5 from LiMo, ordered in wave 1.** `bom.csv` updated.

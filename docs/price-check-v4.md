# Price check V4: frame (Task 2, 24 Nov 2026)

All prices were read by `curl -sL --compressed` on **24 Nov 2026**. No browser was used and no price is estimated.
- **"Computed"** means a length worked out with the page's own per-metre price and its own formula. It is not a quote.
- Nothing has been chosen yet. Options and stiffness: `docs/v4-frame-options.md`.

## KJN Aluminium Profile (www.aluminium-profile.co.uk): **a new vendor**, not in the order yet
WooCommerce.
- **Do not use the Store API price for profiles.** `/wp-json/wc/store/products` gives a different number (90 x 90 H: 60.00 in the API, £117.00/m on the page). The per-metre price below is the one on the product page.
- **Price formula on the page:** pieces x (length/1000 x price per metre + cutting charge).
- **VAT:** the per-metre line does not say ex or inc VAT. The page carries a tax factor of 1.2, and its other products show "excl VAT" first. So the prices are read as **ex VAT**.
- **Delivery** (`/delivery/`): UK mainland from **£15.50 + VAT**, by weight and length, exact cost at checkout. A handling charge applies to lengths over 3000 mm. Typical delivery 7 to 10 working days. Click and collect is possible.

| Item | Price | Data | URL |
|---|---|---|---|
| 90 x 90 H profile (KJN990500), 10 mm slot | **£117.00 per metre**, cutting £1.74 per length, 100 to 6000 mm. Drilling option "M16/M16 (+£2.50)" | Ix = Iy = 299.80 cm⁴, 10.50 kg/m | https://www.aluminium-profile.co.uk/90x90-heavy-aluminium-profile-kjn990500/ |
| 80 x 80 H IR profile (IR02627), 8 mm slot (not used in the options) | £65.42 per metre, cutting £1.74 | Ix = Iy = 187.70 cm⁴, 7.19 kg/m | https://www.aluminium-profile.co.uk/80x80-itm-aluminium-profile-ir02627/ |
| 80 x 160 H IR profile (IR26526) | **Price on application** (API price 0.01): not priced | Ix 360.89, Iy 1228.33 cm⁴, 13.52 kg/m | https://www.aluminium-profile.co.uk/80x160-itm-aluminium-profile-ir26526/ |
| 90 x 90 bracket with fixings, BR only (KJN523578) | £12.05 excl VAT, £14.46 inc VAT | | https://www.aluminium-profile.co.uk/90x90-bracket-with-fittings-kjn523578/ |
| M8 T-nut, 10 mm slot (KJN530287) | £0.36 excl VAT, £0.43 inc VAT, per item as listed ("(10)" in the name read as the slot size) | | https://www.aluminium-profile.co.uk/m8-t-nut-10pk-kjn530287/ |

**Computed, 90 x 90 H** (page formula, ex VAT):

| Tray | Pieces | Profiles | Extras | Total |
|---|---|---|---|---|
| A | 2 x 670, 3 x 320 | £277.80 | 12 brackets £144.60 | £422.40 |
| B | 4 x 500 | £240.96 | M16/M16 x 4: £10.00 | £250.96 |
| C | 8 x 500 | £481.92 | M16/M16 x 8: £20.00 | £501.92 |

## K I Metals (kimetals.co.uk)
WooCommerce. Already in the project's supplier list (`steel-rhs-suppliers.md`).
- **Price unit:** the product page's own script prices a cut as length (mm) x price / 1000.
  - It bills 500 mm at least.
  - None of the pages read has a length attribute that would change the divisor.
  - The shown weight is that of 1000 mm.
  - So the price is **per metre, ex VAT**, and the page shows inc VAT beside it.
- The Store API price matched the page on the 5 pages read (marked "page"). Two flat bars were read from the Store API only (marked "API").
- **Cutting:** 2 cuts per length free, then £1 per cut, ±2 to 3 mm.
- **Delivery:** free over £150 + VAT, "heavy/oversize exclusions" apply. The cost to SA2 is not shown.
- **Grade:** box section is "commonly S235JRH to BS EN 10219; selected sections may be S355J2H". Ask in writing if S355 is wanted.
- **No steel plate product.** Wide flat bar (hot-rolled, mill scale) stands in for a thick-plate upright.

| Item | Per metre, ex VAT (inc VAT) | Read from | Computed for V4 (ex VAT) | URL |
|---|---|---|---|---|
| SHS 120 x 120 x 8 (beam), 27.27 kg/m | **£67.05** (£80.46) | page | 890 (`sizes()` beam_len): **£59.67** | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim144709 |
| RHS 160 x 80 x 8 (upright U1), 26.4 kg/m | **£70.32** (£84.38) | page | one length 650 (2 x 325, A/B): £45.71; 830 (2 x 415, C): £58.37 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147811 |
| Flat bar 150 x 50 (upright U2), 58.88 kg/m | **£144.77** (£173.72) | page | 650: £94.10; 830: £120.16 | https://kimetals.co.uk/materials/mild-steel/mild-steel-flat-bar/kim151290 |
| Flat bar 300 x 30 (compared only) | £173.71 (£208.45) | page | | https://kimetals.co.uk/materials/mild-steel/mild-steel-flat-bar/kim151258 |
| Bright flat bar 50 x 20 (rail plates), cold drawn | **£42.89** (£51.47) | page | Y: 2 x 500 (`y_rail`) = 1000: £42.89. X: 2 x 850 (`x_rail`) = 1700: £72.91 | https://kimetals.co.uk/materials/bright-mild-steel/bright-mild-flat-bar/kim42537 |
| Flat bar 90 x 20 (end plates, tray B) | £34.74 | API | 2 x 670 = 1340: £46.55 | https://kimetals.co.uk/materials/mild-steel/mild-steel-flat-bar/kim151115 |
| Flat bar 180 x 20 (end plates, tray C) | £69.49 | API | 2 x 670 = 1340: £93.12 | https://kimetals.co.uk/materials/mild-steel/mild-steel-flat-bar/kim151154 |

## Not priced
- **Shop grinding of the rail plates.** Needs the owner's shop price (only if ground plates are chosen).
- **Bottom sheet** for the pour, M12 bolts and dowels for the upright joints.
- **KJN 80 x 160 H**: price on application.
- **Delivery to SA2** at both vendors: shown only at checkout, which curl cannot reach.

## Sites tried and not usable by curl (24 Nov 2026)
| Site | Result |
|---|---|
| Ooznest (`ooznest.co.uk/products.json`) | 403 |
| Motedis UK (`motedis.co.uk/products.json`) | 404, not Shopify |
| The Metal Store (`themetalstore.co.uk/products.json`) | 404, not Shopify |
| kjnltd.co.uk, systemprofile.co.uk | no response |
| Rapid Metals (WooCommerce Store API) | empty answer |
| Metals4U, Parker Steel (`/products.json`) | 404 |

## Epoxy pack sizes (EC Fibreglass, Ampreg 30 SLOW, 24 Nov 2026)
Read by `curl -sL --compressed` from the page's product data (https://www.ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow):
- 4.66 kg pack: **£86.83** (read as ex VAT, like the £295.00 for the 22.68 kg pack, which is £354.00 inc).
- 2 x 4.66 kg = 9.32 kg binder = £173.66 ex / **£208.39 inc**; V4 needs about 7 kg (`docs/bom.csv` F01). Saves £145.61 against the kit.
- Not chosen: the owner kept the 22.68 kg kit (24 Nov 2026, "go over budget"). Delivery not shown.

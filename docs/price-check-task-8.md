# Price check task 8: consolidate vendors (no eBay)

**Project:** Type 0 CNC, Phase 1. Buyer in **Swansea, UK**. **Goal:** move every item below to **RS Components, Screwfix, B&Q or Easy Composites**, so the order uses as few vendors as possible. **No eBay.**

## Rules
1. Only record prices you can **see on a live product page**. Never estimate or convert.
2. Record the price exactly as listed, ex or inc VAT (RS shows both), pack size, and stock / click & collect at the **Swansea** Screwfix or B&Q stores.
3. The product must match the spec. Say so if it only partly matches. Prefer **RS PRO** or Mean Well / Schneider / Pilz where RS has them.
4. **AliExpress login:** before the first AliExpress page, stop and ask the person to **log in to AliExpress themselves** in the browser pane (UK address, GBP). Wait until they confirm. **Never type, read or store their password or codes.** Read every AliExpress price while logged in. For other sites, do not sign in.
5. **Reading the person's AliExpress basket is allowed** (step A below). Do not add, remove or change basket items, check out, buy or contact sellers. `NOT FOUND` with the reason if no live price.
6. If a page asks for a human check, stop and ask the person.

## RS Components (uk.rs-online.com)

| ID | Item | Spec | Current (all-in, inc VAT) |
|---|---|---|---|
| E04 | 48 V PSU | Mean Well NDR-480-48 (or SDR-480-48), DIN rail, 48 V 10 A | £138.60 |
| E05 | 24 V PSU | Mean Well HDR-150-24, DIN rail | £27.62 |
| E22 | 5 V PSU | Mean Well MDR-10-5 (or HDR-15-5), DIN rail | £15.00 |
| E06 | E-stop safety relay | 24 V AC/DC, dual-channel, 2+ NO safety contacts, manual reset (Pilz PNOZ X2.x, Schneider XPS, or RS PRO) | £30.68 |
| E07 | Contactor | 3-pole, about 9–12 A AC-3, **24 V DC coil**, DIN rail | £26.19 |
| E08 + E21 | E-stop + reset button | 22 mm mushroom e-stop 1 NC, twist release (×2) + 22 mm momentary green NO (×1) | £14.54 (E08 £8.15, E21 £6.39) |
| E09 | EMC filter | Single-phase 230 V, 10–16 A, for a 2.2 kW VFD | £10.39 |
| E17 | Isolator + MCBs | 2-pole 16–20 A DIN isolator, 1 × C16, 2 × C6 MCBs | £24.49 |
| E10 | Inductive sensors × 4 | M12, PNP NO, 24 V, 4 mm range | £9.57 |
| E12 | Steel cabinet | about 600 × 400 × 200 mm, IP55+, mounting plate | £65.95 |
| E18 | Cabinet fan + filters | 120 mm 230 V fan with filter grille, + 1 exhaust filter | £17.46 |
| E13 + E19 | DIN rail, terminals, ferrules, wire | 1 m DIN rail, 30 × 2.5 mm² feed-through terminals + end stops, ferrule kit with crimper, 0.75 mm² and 1.5 mm² wire 10 m each | £61.85 (E13 £33.79, E19 £28.06) |
| S04 + E20 + E14 | Cables | 4-core 1.5 mm² screened (CY) 5 m for the spindle; 4-core 1.0 mm² screened 15 m for motors; cable chain about 25 × 38 mm, 1 m | £69.96 (S04 £18.22, E20 £36.05, E14 £15.69) |
| X03 + X04 | Socket cap screws | M5 × 16 (100), M6 assortment, M8 assortment, M10 × 30 (20), M12 × 120 (10), grade 12.9 or A2 | £68.78 (X03 £40.99, X04 £27.79) |
| F07 | Steel flat bar | 40 × 10 mm bright mild steel, 3 m total (e.g. 3 × 1 m) | £36.00 |
| T02 | Anti-vibration levelling feet × 4 | M10/M12, rubber base, ≥ 50 kg each | £21.95 |
| X01 | Dial test indicator + magnetic base | 0.01 mm lever DTI | £17.20 |
| X02 | Precision level | 200 mm, 0.05 mm/m or better | £68.50 |

## Screwfix (Swansea store)

| ID | Item | Spec | Current (all-in, inc VAT) |
|---|---|---|---|
| F18 | Silicone | Neutral-cure silicone (clear), 310 ml × 2 | £16.98 (F18 tape + silicone together) |
| F17 | Mixer | 1,400–1,600 W paddle mixer (current: Erbauer EPM1600 £69.99) | £69.99 |

## Step A: read the AliExpress basket (after the person has logged in)

Open the AliExpress basket/cart and list **every item** in it: title, seller/store, selected option (size, length, voltage, etc.), quantity, price shown, shipping shown, and the product URL.

Then match each basket item against the **Phase 1 parts** in this file and in the re-check table below (IDs M, S, E, F, X):
- **FULL** — it meets the spec of a parts-list line (give the ID). Use its basket price as that line's new price, and still report the delta against current.
- **PARTIAL** — close but not to spec (say what differs, e.g. rail length, coil voltage, bore).
- **NOT NEEDED** — not useful for Type 0 (just list it, no detail needed).

Do not change the basket. If one basket item could cover several lines, say so. Lines covered by a FULL basket match need no further searching.

## AliExpress: re-check every Phase 1 line while logged in

The current prices came from logged-out pages. Many were new-shopper or "max 1 per shopper" deals. Logged in, record for each line: the **price your account sees**, whether the **deal applies** to this account, **shipping to the account's UK address**, and any **coupon** shown on the page (do not apply it).

| ID | Item | Current (all-in) | Listing |
|---|---|---|---|
| M01 | HGR20 rail kit Y: 2 × 500 mm + 4 blocks | £61.64 | https://www.aliexpress.com/item/1005010242098397.html |
| M02 | HGR20 rail kit X: 2 × 800 mm + 4 blocks | £79.04 | https://www.aliexpress.com/item/1005010242098397.html |
| M03 | HGR20 rail kit Z: 2 × 350 mm + 4 blocks | £57.34 | https://www.aliexpress.com/item/1005010242098397.html |
| M05 | DFU1605 ballscrew kits X 750 / Y 450 / Z 350 | £198.65 | https://www.aliexpress.com/item/1005010046279521.html |
| M08 | Disc or bellows coupling 10 mm to 10 mm | £13.09 | https://www.aliexpress.com/item/1005009879991986.html |
| M13 | Motor and bearing mounts | £40.59 | https://www.aliexpress.com/item/1005006232398099.html |
| S08 | G-Penny 2.2 kW ER20 water-cooled spindle kit | £318.16 | https://www.aliexpress.com/item/32253760001.html |
| S09 | ER20 collet set | £34.49 | https://www.aliexpress.com/item/1005010595086817.html |
| S04 | Shielded 4-core spindle cable | £18.22 | https://www.aliexpress.com/item/32971008305.html |
| S05 | Spindle cooling loop (DIY) | £73.18 | https://www.aliexpress.com/item/1005004896354890.html |
| E07 | Contactor with 24 V coil | £26.19 | https://www.aliexpress.com/item/1005005356561757.html |
| E08 | E-stop mushroom buttons + reset button | £8.15 | https://www.aliexpress.com/item/1005008293871583.html |
| E09 | MCBs / main isolator / EMC filter for VFD | £10.39 | https://www.aliexpress.com/item/1005010519550019.html |
| E10 | Inductive proximity switches 24 V | £9.57 | https://www.aliexpress.com/item/1005010648075147.html |
| E13 | DIN rail / terminals / wiring / ferrules | £33.79 | https://www.aliexpress.com/item/1690060053.html |
| E14 | Cable chain and shielded motor cables | £15.69 | https://www.aliexpress.com/item/1005012723966521.html |
| X01 | Dial test indicator + magnetic base | £17.20 | https://www.aliexpress.com/item/1005013036061506.html |

## AliExpress: new lines (owner choice for these, D-83)

| ID | Item | Spec | Current (all-in, inc VAT) |
|---|---|---|---|
| F08 | M12 threaded rod + nuts | 2 × 1 m zinc M12 rod + about 20–50 M12 nuts | £28.74 |
| F09 | Conduit / tube for bolt sleeves | 20 mm OD PVC or steel tube, 2–3 m (or 14–16 mm ID tube) | £2.29 |
| F18t | Packing tape | Wide clear packing tape, 2–3 rolls | part of F18 £16.98 |

## B&Q (Swansea store)

| ID | Item | Spec | Current (all-in, inc VAT) |
|---|---|---|---|
| F10 | MDF | 18 mm 2440 × 1220 (current £28) | £28.00 |
| F11 | CLS | 38 × 63 × 2400 × 6 (current £3.97 each) | £23.82 |

## Easy Composites (one epoxy supplier)

| ID | Item | Spec | Current (all-in, inc VAT) |
|---|---|---|---|
| F01 | Main EG epoxy, about 14 kg | Low-viscosity, slow epoxy for casting: GlassCast 50 PLUS (15 kg kit) or EL2 + slow hardener. Record viscosity and pot life | £312.59 |
| F02 | Levelling epoxy, 5 kg | GlassCast 50 PLUS 5 kg (current £76.46 ex VAT) | £91.75 |
| F12 | Release agents | PVA release agent + release wax | £31.68 |

## Compare against the current price (required)
For **every** line, compare the new **all-in** price (item + its share of shipping, inc VAT) with the **Current** column, and report the difference.
- Mark **OK** if the new price is no more than **10% or £5** above current (whichever is larger).
- Mark **PREMIUM** if it is more, and give the cheapest current-vendor option too, so the owner can decide.
- Mark **SAVING** if it is cheaper.

## Reply block

```
ID | vendor | price as listed (currency, VAT basis; AliExpress: logged-in price, deal applies Y/N) | quantity it covers | stock / collect / delivery | product URL | all-in £ | current £ | delta £ (OK / PREMIUM / SAVING) | notes
```
Start the reply with the **Step A basket table** (`basket item | option | qty | price | shipping | URL | match: FULL ID / PARTIAL ID / NOT NEEDED | notes`). Finish with: the **vendor list** with a subtotal per vendor, the **total delta** against current, and a list of every **PREMIUM** line.

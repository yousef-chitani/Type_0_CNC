# Price check task 8: consolidate vendors (no eBay)

**Project:** Type 0 CNC, Phase 1. Buyer in **Swansea, UK**. **Goal:** move every item below to **RS Components, Screwfix, B&Q or Easy Composites**, so the order uses as few vendors as possible. **No eBay.**

## Rules
1. Only record prices you can **see on a live product page**. Never estimate or convert.
2. Record the price exactly as listed, ex or inc VAT (RS shows both), pack size, and stock / click & collect at the **Swansea** Screwfix or B&Q stores.
3. The product must match the spec. Say so if it only partly matches. Prefer **RS PRO** or Mean Well / Schneider / Pilz where RS has them.
4. Do not sign in, add to basket, buy or contact sellers. `NOT FOUND` with the reason if no live price.
5. If a page asks for a human check, stop and ask the person.

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

## AliExpress (owner choice for these, D-83)

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
ID | vendor | price as listed (currency, VAT basis) | quantity it covers | stock / collect / delivery | product URL | all-in £ | current £ | delta £ (OK / PREMIUM / SAVING) | notes
```
Finish with: the **vendor list** with a subtotal per vendor, the **total delta** against current, and a list of every **PREMIUM** line.

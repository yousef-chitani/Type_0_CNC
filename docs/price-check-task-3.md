# Price check task 3: AliExpress savings for Stage 1 (for a local Claude session with a browser)

**Project:** Type 0 CNC, a DIY 3-axis epoxy-granite mill. Buyer in **Swansea, UK**. Stage 1 is priced at about £5,200 against a £4,500 budget. **Goal:** find cheaper **AliExpress** options (UK delivery) for the items below.

## Rules
1. Only record prices you can **see on a live product page**. Never estimate or convert currency.
2. Record the price exactly as listed, with currency and VAT basis (AliExpress UK normally shows prices inc VAT: say so if the page states it).
3. Record **shipping to the UK**, the delivery estimate and whether it ships from a **UK/EU warehouse**.
4. Note whether the price is a **new-shopper / limited / "max 1 per shopper"** deal, and give the normal price too.
5. The product must **match the spec**. Say so if it only partly matches.
6. Report the **cheapest full match** plus one better-rated option (more orders / higher store rating) in notes.
7. **If AliExpress shows a CAPTCHA or slider:** stop and ask the person to solve it in the browser pane, then continue. Do not try to bypass it.
8. Do not sign in, add to basket, buy or contact sellers. `NOT FOUND` with the reason if no live price.

## Items

| ID | Item | Spec to match | Current best | Notes |
|---|---|---|---|---|
| S01 | Spindle | **Jianken JGL-80/2.2R24-20**, ISO20, water-cooled, 220 V, 400 Hz, **with clamp/unclamp sensors**, spindle only | £990.57 (Alibaba, VAT?) | Record the torque stated (0.7 or 0.87 Nm) and whether import VAT is included |
| S01b | Spindle + VFD bundle | Same spindle + 2.2 kW VFD with **RS-485 / Modbus** | £1,542.94 (AliExpress) | Only a saving if under about £1,115 |
| S02 | VFD | 2.2 kW, 1-phase 220–240 V in, 0–400 Hz+ out, **RS-485 / Modbus stated on the page** | £124.84 (Huanyang, RS-485 not stated) | RS-485 must be stated |
| S05 | Spindle water cooler | CW-3000 type, 220–240 V, **flow alarm with output contacts / terminal** | £144.00 (eBay UK, output not stated) | UK/EU warehouse preferred (heavy) |
| M01 | HGR20 rail kit | 2 × 650 mm HGR20 + 4 × HGH20CA, **Z1 preload** if offered | £70.85 sale (list £147.49, 1 per shopper) | One kit per axis: also price 2 × 450 mm (M02) and 2 × 300 mm (M03) in the **same** listing |
| M09 | Closed-loop stepper kit × 2 | StepperOnline (or equal) NEMA 24 4 Nm + CL57T-type driver, 10 mm shaft | £112.71 for 2 (StepperOnline) | Check the official StepperOnline AliExpress store |
| M10 | Closed-loop brake motor | NEMA 24 about 3 Nm, 1000-line encoder, 24 V brake, 10 mm shaft | £59.22 (StepperOnline, backorder) | |
| M11 | Table plate | Aluminium 6061/6082 plate **330 × 330 × 30 mm**, cut to size, ideally milled/flat | £190.54 (Aluminium Warehouse) | Custom-cut plate sellers |
| M12 | Saddle and Z plates | Aluminium 6061/6082, 20 mm thick: 1 × 220 × 200 mm and 1 × 300 × 150 mm (placeholder sizes) | £104.98 (reference 300 × 300 × 20) | Price each size |
| F14 | Vibration motors × 2 | 220–240 V single phase, **exciting force stated** (about 0.5–2 kN) | £99.72 (eBay UK, force not stated) | |
| F16 | Thermocouple logger | 4-channel K-type logger **with** 4 probes | £76.99 (eBay UK) | |
| F12 | Mold release | PVA release agent + release wax | £31.68 | |
| F01 | Main epoxy, about 37 kg | Low-viscosity epoxy (≤ 1,000 mPa·s), **slow** hardener (pot life ≥ 60 min), hardener included | £666.59 (Ampreg 30, ECF) | Must ship to UK. Record viscosity and pot life. Heavy: check shipping |
| E12 | Electrical cabinet | Steel 600 × 500 × 200 mm, IP65, mounting plate | £92.33 (eBay UK) | Only if delivered cheaper |
| F15 | Rubber mounts × 4 + table | M10 rubber bobbins, ≥ 150 kg each | not priced | |

## Reply block (output exactly this format)

```
ID | price as listed (currency, VAT basis) | quantity it covers | shipping to UK, warehouse, delivery estimate | product URL | notes (deal limits, spec match, better option)
```

Finish with the **total saving** against the "Current best" column for full matches only.

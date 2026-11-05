# Price check task 2: savings and missing costs (for a local Claude session with a browser)

**Project:** Type 0 CNC, a DIY 3-axis epoxy-granite (EG) mill. Buyer in the **UK**. Budget £4,500; priced parts are currently about £6,000, so **we are looking for savings**.
**Goal:** read live product pages in the browser and report prices in the reply format at the end.

## Rules (same as task 1)
1. Only record prices you can **see on a live product page**. Never estimate or convert currency.
2. Record price exactly as listed, with currency and **ex VAT / inc VAT / VAT?**.
3. Note shipping to the UK (`ship?` if not shown). For in-store items, note **click & collect** availability and stock at any store.
4. The product must **match the spec**. Say so if it only partly matches.
5. Report the **cheapest full match**, plus a better-quality option in notes where relevant.
6. `NOT FOUND` with the reason if no live price.
7. Do not sign in, add to basket, buy or contact sellers.

## Part A: cheaper alternatives (current price in brackets)

| ID | Item | Spec to match | Current | Where to look |
|---|---|---|---|---|
| F03 | Coarse aggregate, about 135 kg | **Dry, clean, washed** quartz or granite gravel, about **2–5 mm**, no clay/dust | £183.60 delivered pallet | **B&Q in-store first** (e.g. kiln-dried or washed grit/gravel 2–5 mm). Then other UK click-and-collect |
| F04 | Medium aggregate, about 90 kg | Dry, clean sand about **0.5–2 mm** | £183.60 delivered pallet | B&Q in-store (e.g. kiln-dried sand, grit sand), other UK |
| F05 | Fine aggregate, about 45 kg | **Kiln-dried** sand about **0.1–0.5 mm** | £188.40 delivered pallet | **B&Q kiln-dried (paving joint) sand**. Note the particle size if stated |
| F06 | Filler, about 30 kg | Silica flour / ground quartz below 0.1 mm, or fly ash | £43.26 per 25 kg | UK pottery suppliers, builders merchants |
| F10 | Melamine-faced MDF or chipboard, **3 sheets** | 18 mm, 2440 × 1220, white melamine faced | £376.20 for 5 delivered | **B&Q in-store single sheets**, Wickes, local timber merchants |
| F11 | Timber battens, 20 m | 44 × 44 mm PSE (or 38 × 63 CLS) | £72.50 (Wickes) | **B&Q in-store**, Wickes |
| F01 | Epoxy for main EG mix, about **37 kg** | Low-viscosity epoxy, **slow hardener**, suitable for filled casting. **Include hardener price** | £590 (Ampreg 30, 2 × 22.68 kg, hardener appears extra) | Easy Composites, East Coast Fibreglass, CFS, Polyestershoppen, AliExpress bulk epoxy (must give viscosity/pot life) |
| E04 | 48 V DC PSU | ≥ 10 A, 48 V, reputable (Mean Well or equal) | £202.27 (Rapid SDR-480-48) | AliExpress Mean Well (e.g. LRS/RSP/SE series), eBay UK, other UK stockists |
| E05 | 24 V DC PSU | 24 V, about 100–150 W | £53.82 (Rapid HDR-150-24) | AliExpress Mean Well, eBay UK |
| E06 | E-stop safety relay | 24 V, **dual-channel** e-stop monitoring, manual reset, 2+ NO safety contacts | £116.20 (CM SAFE 4.3eco) | AliExpress, eBay UK (used Pilz PNOZ X2 / similar) |
| S05 | Spindle water cooler | CW-3000 type, 230 V, **must have a flow-alarm output** | £208.42 (Megacold, flow alarm not stated) | AliExpress, eBay UK. State whether the flow alarm is present |
| F14 | Vibration motors × 2 | 230 V, **exciting force stated** (≈ 0.5–2 kN each), for a table carrying ≈ 330 kg | £99.72 (force not stated) | AliExpress, eBay UK |

## Part B: costs not yet priced

| ID | Item | Spec to match |
|---|---|---|
| E01 | Mesa 7i76EU **total to UK** | From store.mesanet.com: shipping to UK and whether import VAT/duty is collected. Also EuSurplus shipping to UK |
| A01 | ISO20 tool forks × 8 | Budget ISO20 forks (AliExpress/eBay). Current alt: DamenCNC €31.50 each |
| E02b | 2nd Intel NIC for Lenovo M720q Tiny | M720q PCIe riser + low-profile **Intel** NIC (e.g. i210 / i350 / 82574) |
| E09b | MCBs + main isolator | 1 × 2-pole 16 A main isolator (DIN), MCBs: 1 × C16 (VFD), 2 × C6 (PSUs, chiller) |
| E12b | Cabinet filter fan + exhaust filter | 120 mm, 230 V, with filter grille |
| E13b | DIN rail + ferrules + wire | 1 m DIN rail, ferrule kit with crimper, 0.75 mm² and 1.5 mm² wire |
| E14b | Shielded motor/encoder cable | 4-core 1 mm² shielded, about 15 m |
| P05b | Push-fit fittings kit | 6 mm and 8 mm push-in fittings, 1/8 and 1/4 BSP |
| F13b | Packing tape + silicone | Clear packing tape, neutral-cure silicone |
| X03b | M5 and M12 socket cap screws | M5 × 16 (about 100, rail bolts), M12 × 100–150 (8, gantry joint) |
| F01b | Ampreg 30 **slow hardener** | Hardener for 2 × 22.68 kg resin at 100:26 by weight (about 11.8 kg) |
| E08b | Reset push button | 22 mm, green/blue, momentary NO |

## Reply block (output exactly this format)

```
ID | price as listed (currency, ex/inc VAT) | quantity it covers | shipping / collect | product URL | notes
```

Finish with a short list of the **three biggest savings** you found.

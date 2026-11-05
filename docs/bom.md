# Bill of materials (summary)

Full list: [bom.csv](bom.csv). **72 line items, 69 priced.** Prices were read from live pages on 2026-11-04/05 (by this session and a local browser session).

**Pricing rule:** `price_listed` is exactly what the page showed. `price_gbp` is the GBP line total (all units + listed shipping), inc VAT where known. Lines marked *VAT?* may get VAT added, and import VAT may apply to non-UK orders. EUR/USD prices are not converted.

| Subsystem | Line items | Priced | GBP total |
|---|---|---|---|
| Frame | 17 | 16 | £2,129.76 |
| Motion | 14 | 14 | £923.29 |
| Spindle | 7 | 7 | £1,426.23 |
| Tool changer | 6 | 5 | £239.76 |
| Pneumatics | 5 | 5 | £82.88 |
| Electronics | 15 | 14 | £744.50 |
| Enclosure | 3 | 3 | £217.59 |
| Stand | 2 | 2 | £132.98 |
| Metrology | 2 | 2 | £85.70 |
| Fixings | 1 | 1 | £40.99 |
| **All** | **72** | **69** | **£6,023.68** |

**Budget: £4,500.** Priced total: **£6,023.68**. Not priced yet: F15, A01, E01.

## Ten biggest lines
| ID | Item | £ |
|---|---|---|
| S01 | Jianken JGL-80/2.2R24-20 ATC spindle | 990.57 |
| F01 | Epoxy for main frame mix | 590.00 |
| F10 | Melamine-faced board 2440 x 1220 x 18 mm | 376.20 |
| S05 | CW-3000-style radiator unit with flow alarm | 208.42 |
| E04 | 48 V DC power supply about 10 A | 202.27 |
| M11 | Aluminium tooling plate 330 x 330 x 30 mm | 190.54 |
| F05 | Fine sand 0.1-0.5 mm | 188.40 |
| F03 | Kiln-dried quartz gravel 2-5 mm | 183.60 |
| F04 | Kiln-dried sand 0.5-2 mm | 183.60 |
| M05 | SFU1605 ballscrew + DFU1605 preloaded nut | 182.83 |

## Warnings
- **S01 spindle:** the Alibaba key attributes say 0.7 Nm, but other listings say 0.87 Nm. Confirm with Jianken. Import VAT (about 20%) is likely on top of £990.57.
- **S02 VFD:** RS-485/Modbus is not stated on the page. Confirm before buying (D-32).
- **M01–M03 rails:** the sale price is limited to 1 per shopper. At list prices the three kits are £387.63.
- **S06 tool holders:** £6.05 may be a new-shopper price. At list price, 8 holders cost £178.96. The pull stud must match the spindle.
- **E01 Mesa:** US$219 (Mesa) or €250 (EuSurplus), not yet in the GBP total. Shipping and import VAT not shown.
- **F03–F05 aggregates:** pallet quantities are provisional (about 650 kg vs about 300 kg needed). Set them from the grading.
- **F10 melamine:** a 5-pack is £376.20. A local merchant selling 3 sheets would cut this a lot.
- **Reference sizes:** M12, A06, N02 and T01 are priced at placeholder sizes until the layout is drawn.
- **Missing sub-items:** the 2nd Intel NIC and riser (E02), MCBs/isolator (E09), filter fan (E12), DIN rail/ferrules/wire (E13), shielded motor cable (E14), pneumatic fittings (P05), tape/silicone (F13), M5/M12 screws (X03), and the epoxy hardener (F01).

## Full list with links

| ID | Item | Qty | Spec | Link | Listed price | Line £ | Notes |
|---|---|---|---|---|---|---|---|
| F01 | Epoxy for main frame mix | 37 kg | Low-viscosity epoxy with slow hardener | [product](https://ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow) | £295.00 per 22.68 kg pack (EC Fibreglass) — VAT basis not stated | 590.00 | 2 packs. Hardener appears to be SOLD SEPARATELY (100:26 ratio): extra cost not confirmed. Epoxy choice still open |
| F02 | Epoxy for leveling pour / grout / samples | 5 kg | Very low viscosity and slow cure (e.g. GlassCast 50 PLUS) | [product](https://www.easycomposites.co.uk/glasscast-50-plus-clear-epoxy-casting-resin) | £76.46 ex VAT per 5 kg kit (Easy Composites) | 91.75 | Inc VAT calculated at 20% |
| F03 | Kiln-dried quartz gravel 2-5 mm | 1 lot | Graded aggregate: coarse fraction | [product](https://www.specialistaggregates.com/waterford-quartz-gravel-fine-p-2059.html) | Quartz gravel 3-5 mm: £29.60 per 15 kg; 2-3 mm: £183.60 per pallet 10 × 15 kg; all inc VAT and delivery (Specialist Aggregates) | 183.60 | PROVISIONAL: 1 pallet of 2-3 mm. Quantities depend on the grading (open question 5). Medium 3-5 mm: https://www.specialistaggregates.com/waterford-quartz-gravel-medium-p-1316.html |
| F04 | Kiln-dried sand 0.5-2 mm | 1 lot | Graded aggregate: medium fraction | [product](https://www.specialistaggregates.com/filter-media-silica-sand-p-1464.html) | £183.60 per pallet 10 × 25 kg inc VAT and delivery (Specialist Aggregates) | 183.60 | PROVISIONAL quantity. Silica sand 1.0-2.0 mm, washed. Kiln-dried NOT stated: dry before use |
| F05 | Fine sand 0.1-0.5 mm | 1 lot | Graded aggregate: fine fraction | [product](https://www.specialistaggregates.com/sand-water-worn-ultra-fine-p-1303.html) | £188.40 per pallet 10 × 25 kg inc VAT and delivery; £32.40 per 15 kg bag (Specialist Aggregates) | 188.40 | PROVISIONAL quantity. Kiln-dried silica 0.1-0.3 mm. A few bags may be enough once the grading is set |
| F06 | Fine filler (silica flour or fly ash) | 1 lot | Below 0.1 mm | [product](https://potterycrafts.co.uk/products/potterycrafts-quartz-silica-sand?variant=49197100859674) | £36.05 ex VAT per 25 kg (Potterycrafts) | 43.26 | Fine ground quartz. Particle size not stated. Inc VAT calculated. Shipping not shown |
| F07 | Steel flat bar 40 x 10 mm | 2 3 m bars | 40 × 10 mild steel flat bar, 3 m | [product](https://www.themetalstore.co.uk/products/3-metre-lengths-10mm-flat-bar) | £30.00 ex VAT / £36.00 inc VAT per 3 m bar (The Metal Store) | 72.00 | Delivery not shown. Bright (EN3B) bar is an option for flatter inserts |
| F08 | M12 threaded rod + nuts (lifting points and joint) | 1 lot | Zinc or plain steel | [product](https://www.ebay.co.uk/itm/361927188666) | £19.65 for 2 × 1 m rods, free shipping (eBay UK) + nuts £9.09 inc VAT (Screwfix) | 28.74 | Nuts: https://www.screwfix.com/p/easyfix-bzp-steel-hex-nuts-m12-100-pack/15569 |
| F09 | Steel or PVC tube for M12 bolt sleeves | 2 m | About 14-16 mm bore | [product](https://www.screwfix.com/p/deta-tte-round-upvc-white-conduit-20mm-x-3m/256vt) | £2.29 inc VAT per 3 m (Screwfix) | 2.29 | 20 mm uPVC conduit, bore not stated (about 16-17 mm expected, clears M12). Steel alt £10.99: https://www.screwfix.com/p/deta-tte-round-steel-galvanised-class-4-conduit-tube-20mm-x-3m/7734j |
| F10 | Melamine-faced board 2440 x 1220 x 18 mm | 5 sheet | Mould walls and floors | [product](https://www.diy.com/departments/18mm-white-melamine-faced-mdf-board-2440mm-x-1220mm-8-x-4-pack-of-5/1234564004017_BQ.prd) | £376.20 for 5 sheets, free delivery (B&Q / Materials Market) | 376.20 | Need 3: only a 5-pack delivers. A local timber merchant may sell single sheets much cheaper. eBay single MFC sheet £37.10 collection only |
| F11 | Timber battens 44 x 44 mm | 9 m | Floor support and wall bracing | [product](https://www.wickes.co.uk/Wickes-Redwood-PSE-Timber---44-x-44-x-2400mm/p/9000281515) | £7.50 per 2.4 m + delivery from £5 (Wickes) | 72.50 | 9 lengths. Offer ended 4 Nov: page also shows "from £6.20" |
| F12 | Release wax + PVA release film | 1 set |  | [product](https://www.ebay.co.uk/itm/235827548462) | PVA £13.50 free shipping (eBay UK) + wax £9.39 inc VAT + £8.79 express (AliExpress) | 31.68 | Wax: https://www.aliexpress.com/item/1005006037723287.html |
| F13 | Packing tape / silicone / plasticine for fillets | 1 set |  | [product](https://www.ebay.co.uk/itm/357951022386) | Plasticine £16.10 + £2.94 shipping (eBay UK) | 19.04 | Packing tape and silicone NOT priced |
| F14 | Vibration motors | 2 pcs | Unbalanced vibration motors for the vibration table | [product](https://www.ebay.co.uk/itm/900058009643) | £49.86 each, free shipping (eBay UK) | 99.72 | 100 W 230 V 3000 rpm with speed controller. Exciting force not stated: NOT yet sized for about 330 kg. Check before buying |
| F15 | Vibration table springs or rubber mounts + top sheet | 1 set | Takes about 330 kg (mould + casting) | [product](https://www.ebay.co.uk/itm/326960605104) | NOT FOUND (page blocked). Search card: £8.66 + £2.72 per M10 bobbin, 192 kg |  | Unconfirmed. Top sheet not priced |
| F16 | Temperature probes + logger | 1 set | Thermocouples or DS18B20 probes cast in | [product](https://www.ebay.co.uk/itm/800631453870) | £76.99, free shipping (eBay UK) | 76.99 | 4-ch K/J/T logger. Probes included not stated |
| F17 | Mixer | 1 pcs | Paddle mixer or small forced-action mixer | [product](https://www.screwfix.com/p/erbauer-epm1600-1600w-electric-paddle-mixer-220-240v/981kj) | £69.99 inc VAT (Screwfix) | 69.99 | Erbauer EPM1600 |
| M01 | HGR20 rail 650 mm | 2 pcs | Y axis | [product](https://www.aliexpress.com/item/1005010242098397.html) | £70.85 inc VAT, free shipping (AliExpress sale; list £147.49) | 70.85 | 2 × 650 mm + 4 HGH20CA. SALE LIMIT 1 per shopper: may not get all 3 kits at sale price. Preload not stated (Z1 not offered). HIWIN-branded alt: 1 rail + 2 blocks £70.99 + £32.52 https://www.aliexpress.com/item/1005008442623745.html |
| M02 | HGR20 rail 450 mm | 2 pcs | X axis | [product](https://www.aliexpress.com/item/1005010242098397.html) | £59.05 inc VAT, free shipping (AliExpress sale; list £123.91) | 59.05 | 2 × 450 mm + 4 HGH20CA. Same listing and sale limit as M01 |
| M03 | HGR20 rail 300 mm | 2 pcs | Z axis | [product](https://www.aliexpress.com/item/1005010242098397.html) | £55.21 inc VAT, free shipping (AliExpress sale; list £116.23) | 55.21 | 2 × 300 mm + 4 HGH20CA. Same listing and sale limit as M01 |
| M04 | HGH20CA carriage Z1 preload | 12 pcs | 4 per axis | [product](https://www.aliexpress.com/item/1005010242098397.html) | Included in M01-M03 | 0 | 4 HGH20CA per kit. Z1 preload not offered |
| M05 | SFU1605 ballscrew + DFU1605 preloaded nut | 3 pcs | C7 rolled. Ends machined for BK12/BF12. X about 420 mm / Y about 500 mm / Z about 280 mm | [product](https://www.aliexpress.com/item/1005010046279521.html) | £52.99 (300) + £58.99 (450) + £62.99 (500) inc VAT + £7.86 shipping (AliExpress) | 182.83 | DFU1605 double nut, machined ends, housing, BK12/BF12, coupler. C7 and preload value not stated. New listing (0 sold). Shipping shown for 1 kit: may be per kit |
| M06 | BK12 + BF12 end supports | 3 sets |  | [product](https://www.aliexpress.com/item/1005010046279521.html) | Included in M05 | 0 |  |
| M07 | Nut housing DSG16H | 3 pcs |  | [product](https://www.aliexpress.com/item/1005010046279521.html) | Included in M05 | 0 |  |
| M08 | Disc or bellows coupling 10 mm to 10 mm | 3 pcs | Listings give a 10 mm shaft on the 4 Nm NEMA 24 (24HS40-5004D-E1000). Verify. BK12 end is 10 mm | [product](https://www.aliexpress.com/item/1005009879991986.html) | £3.35 inc VAT each + £3.04 shipping (AliExpress) | 13.09 | D26 L35 double diaphragm, 10 × 10 bore. All 3 motors confirmed 10 mm shaft |
| M09 | NEMA 24 closed-loop stepper + driver about 4 Nm | 2 sets | X and Y. Candidate: StepperOnline 1-CL57T-S40-V41 (24HS40-5004D-E1000 + CL57T V4.1 / 24-48 V DC / 1000 PPR encoder) | [product](https://www.omc-stepperonline.com/ts-series-4-0-nm-566-56oz-in-1-axis-closed-loop-stepper-cnc-kit-nema-24-motor-driver-1-cl57t-s40-v41) | £51.34 (VAT?) per set + £10.03 UK warehouse (StepperOnline) | 112.71 | 24HS40-5004D-E1000 + CL57T-V41. Shaft 10 mm D-cut. UK stock 5. VAT basis unclear |
| M10 | NEMA 24 closed-loop stepper with 24 V brake | 1 set | StepperOnline 24HS34-5004D-E1000-B280: 3 Nm / 5 A / 1000 PPR encoder / 2.8 Nm 24 V power-off brake | [product](https://www.omc-stepperonline.com/s-series-nema-24-closed-loop-stepper-motor-3-0nm-424-92oz-in-with-2-8nm-396-51oz-in-electromagnetic-brake-24hs34-5004d-e1000-b280) | £59.22 (VAT?) (StepperOnline) | 59.22 | China warehouse only, backorder, est. 13-19 Nov. Shaft 10 mm D-cut. Shipping not shown |
| M14 | CL57T V4.1 closed-loop driver | 1 pcs | For the Z brake motor. 24-48 V DC / 0-8 A | [product](https://www.omc-stepperonline.com/closed-loop-stepper-driver-v4-1-0-8-0a-24-48vdc-for-nema-17-23-24-stepper-motor-cl57t-v41) | £28.75 (VAT?) + £5.47 DE warehouse (StepperOnline) | 34.22 | No UK stock |
| M11 | Aluminium tooling plate 330 x 330 x 30 mm | 1 pcs | Table. Drill an M6/M8 threaded grid | [product](https://www.aluminiumwarehouse.co.uk/products/30-mm-6082-aluminium-plate) | £158.78 ex VAT (Aluminium Warehouse, 330 × 330 × 30 6082, cut to size) | 190.54 | Inc VAT calculated at 20%. Shipping not shown. Cast tooling plate (flatter) £216.11 ex VAT: https://www.aluminiumwarehouse.co.uk/products/30-mm-aluminium-cast-tooling-plate |
| M12 | Aluminium plate for X saddle and Z spindle plate | 1 lot | About 20 mm thick. Sizes from the layout | [product](https://www.aluminiumwarehouse.co.uk/products/20-mm-6082-aluminium-plate) | £87.48 ex VAT for reference 300 × 300 × 20 (Aluminium Warehouse) | 104.98 | REFERENCE SIZE ONLY: real sizes come from the layout. Inc VAT calculated |
| M13 | Motor and bearing mounts | 1 lot | Machined or bought brackets | [product](https://www.aliexpress.com/item/1005006232398099.html) | £9.99 inc VAT each + £10.62 shipping (AliExpress) | 40.59 | HM12-60 motor bracket with fixed bearing seat (replaces BK12 at motor end). Check fit with M05 |
| S01 | Jianken JGL-80/2.2R24-20 ATC spindle | 1 pcs | 2.2 kW / 24000 rpm / 400 Hz / 220 V / about 0.87 Nm / ISO20 / water-cooled / 80 mm body. Order the clamp/unclamp sensor variant (PNP) | [product](https://www.alibaba.com/product-detail/Jianken-JGL-80-2-2KW-24000RPM_1601249825246.html) | £937.79 (VAT?) + £52.78 shipping (Alibaba, 1-4 pcs) | 990.57 | Drawing confirms JGL-80/2.2R24, 220 V, 400 Hz, ISO20-ER16, water-cooled. Sensors: clamped/released + temperature, PNP 24 V. VFD not included. Pull stud not shown. KEY ATTRIBUTES SAY 0.7 Nm (other listings 0.87 Nm): confirm with Jianken. Import VAT likely on top. Delivery 18 Nov-19 Dec. Alt AliExpress with 2.2 kW VFD £1402.79 inc VAT + £140.15: https://www.aliexpress.com/item/1005010706946690.html |
| S02 | VFD 2.2 kW single-phase input with RS-485 Modbus | 1 pcs | 220 V 3-phase output / up to 400 Hz / single-phase 230 V input | [product](https://www.aliexpress.com/item/1005007299382924.html) | £94.19 inc VAT + £30.65 shipping (AliExpress) | 124.84 | Huanyang HY02D223B, 220 V, 0-400 Hz. RS-485 NOT stated: ask seller before buying (needed for D-32). Alt StepperOnline EV51S20022BX0 £62.74 (VAT?), pre-order, RS-485 not stated: https://www.omc-stepperonline.com/ev51-series-vfd-3hp-2-2kw-12-5a-single-phase-220v-cnc-spindle-motor-variable-frequency-drive-ev51s20022bx0 |
| S03 | Spindle mount clamp to suit spindle body diameter | 1 pcs | 80 mm | [product](https://www.aliexpress.com/item/4001010906801.html) | £17.89 inc VAT, free shipping (AliExpress) | 17.89 | 80 mm clamp |
| S04 | Shielded 4-core spindle cable | 5 m |  | [product](https://www.aliexpress.com/item/32971008305.html) | £18.22 inc VAT for 5 m (AliExpress) | 18.22 | 4-core 16 AWG (about 1.3 mm²) shielded: slightly under 1.5 mm². Shipping not shown |
| S05 | CW-3000-style radiator unit with flow alarm | 1 pcs | CW-3000TG (220 V 1-phase / 9 L tank / 10 L/min max) | [product](https://www.megacold.uk.com/cw-3000ag-water-chiller) | £173.68 ex VAT / £208.42 inc VAT (Megacold) | 208.42 | In stock. Flow alarm output NOT stated: confirm with seller |
| S06 | ISO20 ER16 holders with pull studs | 8 pcs | ISO20-ER16. Pull studs must match the spindle drawbar | [product](https://www.aliexpress.com/item/4000141590118.html) | £6.05 inc VAT each, free shipping (AliExpress; list £22.37) | 48.40 | ISO20-ER16-35L, 0.003 mm. £6.05 may be a new-shopper deal: at list price 8 × £22.37 = £178.96. PULL STUD NOT STATED: must match Jianken. Jianken own holders £37.52-75.03 on the S01 page. DamenCNC Teknomotor €123.50 each |
| S07 | ER16 collet set | 1 set | Precision (AA grade or better) 1-10 mm | [product](https://www.aliexpress.com/item/1005005626185405.html) | £17.89 inc VAT, free shipping (AliExpress) | 17.89 | AA ER16 10-piece set. Sizes not listed. AAA set £68.39 |
| A01 | ISO20 tool forks | 8 pcs | For the 2 x 4 rack | [product](https://damencnc.com/en/teknomotor-toolholder-fork-iso-20/a4038) | €31.50 ex VAT each at 5+ (DamenCNC art. 5400) |  | 8 × €31.50 = €252 ex VAT. RicoCNC forks: price on request |
| A02 | Rack slide linear guide (e.g. MGN15) + carriage | 2 sets | Rack carrier | [product](https://www.ebay.co.uk/itm/227244866634) | £25.99 per set, free shipping (eBay UK) | 51.98 | MGN15 400 mm + MGN15H. 2 sets |
| A03 | Small closed-loop stepper + driver (48 V) | 1 set | Drives the rack slide | [product](https://www.omc-stepperonline.com/1-axis-closed-loop-stepper-cnc-kit-80ncm-113-29oz-in-nema-17-motor-driver-1-cl42t-s08-v41) | £39.43 (VAT?) + £8.34 DE warehouse (StepperOnline) | 47.77 | 1-CL42T-S08-V41: NEMA 17 0.8 Nm + CL42T 24-48 V. 5 mm shaft |
| A04 | Rack drive screw or belt + pulleys | 1 set | Stroke about 300 mm. Sized in the layout | [product](https://www.aliexpress.com/item/1005006187129418.html) | £43.39 inc VAT, free shipping (AliExpress) | 43.39 | SFU1204 400 mm + housing + BK10/BF10 + coupling. Single nut is fine for the rack |
| A05 | Tool length setter (wired switch) | 1 pcs | On the rack carrier | [product](https://www.aliexpress.com/item/1005012101891449.html) | £17.89 inc VAT, free shipping (AliExpress) | 17.89 | N96R, 24 V, NC |
| A06 | Rack plate and fork mount | 1 lot | Aluminium plate | [product](https://www.aluminiumwarehouse.co.uk/products/15-mm-6082-aluminium-plate) | £65.61 ex VAT for reference 300 × 300 × 15 (Aluminium Warehouse) | 78.73 | REFERENCE SIZE ONLY. Inc VAT calculated |
| P01 | Filter / regulator / dryer | 1 pcs |  | [product](https://www.aliexpress.com/item/1005002589702135.html) | £6.50 inc VAT (AliExpress) | 6.50 | AW2000-02 filter-regulator. No dryer |
| P02 | 24 V solenoid valves | 4 pcs | Tool release / taper clean / air blast | [product](https://www.aliexpress.com/item/1005012294513653.html) | £9.49 inc VAT each, free shipping (AliExpress) | 37.96 | 3V1-06 24 V 3/2 NC. Qty 4 (3 + 1 for mist unit) |
| P03 | Air pressure switch | 1 pcs | About 5.5 bar trip point | [product](https://www.aliexpress.com/item/1005013285557375.html) | £5.17 (VAT?) + £3.79 shipping (AliExpress) | 8.96 | QPM11-NO-02. NO contact |
| P04 | Mist coolant system with 24 V solenoid | 1 set |  | [product](https://www.aliexpress.com/item/1005012241646016.html) | £17.59 inc VAT (AliExpress) | 17.59 | BPV-3000 mist unit, no solenoid (uses 4th P02 valve) |
| P05 | Push-fit tubing and fittings 6/8 mm | 1 lot |  | [product](https://www.aliexpress.com/item/1005006780298909.html) | £4.31 + £7.56 inc VAT (AliExpress) | 11.87 | 10 m 6 × 4 + 10 m 8 × 5 PU. Fittings NOT priced |
| E01 | Mesa 7i76EU | 1 pcs |  | [product](https://store.mesanet.com/index.php?route=product/product&product_id=399) | US$219.00 (VAT?) (Mesa). EU: €250.00 (VAT?) EuSurplus |  | Not converted to GBP. Mesa stock 128. EuSurplus in stock: https://eusurplus.com/index.php?route=product/product&product_id=50 . Shipping and import VAT not shown |
| E02 | x86 mini-PC with Intel NIC (2nd port for Mesa) | 1 pcs |  | [product](https://www.ebay.co.uk/itm/168320664800) | £120.00 (VAT?), free shipping (eBay UK) | 120.00 | Lenovo M720q i3-8100T 8 GB 240 GB, refurbished, last one. Riser + 2nd Intel NIC card NOT included or priced |
| E03 | Monitor + keyboard + mouse | 1 set |  | [product](https://www.ebay.co.uk/itm/197551264739) | £31.90 + £5.21 shipping (eBay UK, used) | 37.11 | Dell 22 in monitor + keyboard + mouse |
| E04 | 48 V DC power supply about 10 A | 1 pcs | Mean Well SDR-480-48 (48 V / 10 A / 480 W / DIN rail / universal input) | [product](https://www.rapidonline.com/mean-well-sdr-480-48-rail-psu-48v-10a-480w-din-rail-mount-universal-input-05-1702) | £168.56 ex VAT each (Rapid 05-1702) | 202.27 | Chosen over PSP-600-48 (£182.78 ex VAT at Rapid). In stock |
| E05 | 24 V DC power supply | 1 pcs | Mean Well HDR-150-24 (24 V / 150 W / DIN rail) | [product](https://www.rapidonline.com/mean-well-hdr-150-24-hdr-rail-psu-24v-150w-din-rail-mounted-1-output-reinforced-05-0748) | £44.85 ex VAT each (Rapid 05-0748) | 53.82 | Search link |
| E06 | Safety relay (e-stop) | 1 pcs | CM Manufactory SAFE 4.3eco 45320 (24 V AC/DC / 3 NO + 1 NC) | [product](https://www.rapidonline.com/cm-manufactory-45320-safety-relay-safe-4-3eco-24v-dc-ac-emergency-stop-08-7835) | £116.20 each (Rapid 08-7835) — page labels conflict on VAT | 116.20 | Back order, 10 days. Check single vs dual channel. VAT basis unclear |
| E07 | Contactor with 24 V coil | 1 pcs |  | [product](https://www.aliexpress.com/item/1005005356561757.html) | £26.19 inc VAT, free shipping (AliExpress) | 26.19 | Schneider LC1D09BDC 9 A 24 V DC coil. Genuine not verified. 9 A is enough for the 48 V / VFD control duty but check against the circuit design |
| E08 | E-stop mushroom buttons + reset button | 1 set |  | [product](https://www.aliexpress.com/item/1005008293871583.html) | £8.15 inc VAT for 5, free shipping (AliExpress) | 8.15 | XB2-BS542, 1 NC. Reset button not included |
| E09 | MCBs / main isolator / EMC filter for VFD | 1 set |  | [product](https://www.aliexpress.com/item/1005010519550019.html) | £10.39 inc VAT (AliExpress) | 10.39 | CW4L2-20A-S. MCBs and isolator NOT priced |
| E10 | Inductive proximity switches 24 V | 4 pcs | Homing X / Y / Z / rack | [product](https://www.aliexpress.com/item/1005010648075147.html) | £1.54 inc VAT each + £3.41 shipping (AliExpress) | 9.57 | LJ12A3-4-Z/BY PNP NO |
| E11 | USB to RS-485 adapter | 1 pcs | For VFD Modbus if not using the board's port | [product](https://www.aliexpress.com/item/1005008303150448.html) | £6.90 inc VAT + £4.02 shipping (AliExpress) | 10.92 | FT232, isolated |
| E12 | Steel cabinet + filtered fan | 1 set | Built into the stand | [product](https://www.ebay.co.uk/itm/327345335863) | £78.70 + £13.63 shipping (eBay UK) | 92.33 | MCG M65200 600 × 500 × 200 IP65 with plate. Filter fan NOT priced |
| E13 | DIN rail / terminals / wiring / ferrules | 1 lot |  | [product](https://www.aliexpress.com/item/1690060053.html) | £33.79 inc VAT for 100, free shipping (AliExpress) | 33.79 | Terminals only. DIN rail, ferrules, wire NOT priced |
| E14 | Cable chain and shielded motor cables | 1 lot |  | [product](https://www.aliexpress.com/item/1005012723966521.html) | £15.69 inc VAT per 1 m, free shipping (AliExpress) | 15.69 | 1 m only: length TBD. Shielded motor cable NOT priced |
| E15 | Enclosure door switch | 1 pcs |  | [product](https://www.aliexpress.com/item/1005006072968001.html) | £8.07 inc VAT (AliExpress) | 8.07 | CZ-93B key interlock, 2 NC. No safety standard stated |
| N01 | Enclosure frame (aluminium extrusion) | 1 lot |  | [product](https://www.ebay.co.uk/itm/401900585637) | £72.73 for 8 × 1000 mm, free shipping (eBay UK) | 72.73 | 4040 slot 8. Cut list TBD |
| N02 | Polycarbonate panels + door | 1 lot |  | [product](https://www.cutmy.co.uk/plastic/polycarbonate-sheets/6mm/L1000-W1000/) | £129.17 inc VAT for reference 1000 × 1000 × 6 + shipping from £12.95 (Cut My) | 142.12 | REFERENCE SIZE ONLY: panel sizes TBD |
| N03 | LED light | 1 pcs |  | [product](https://www.aliexpress.com/item/1005013221981188.html) | £2.74 inc VAT (AliExpress) | 2.74 | 24-36 V 5 W |
| T01 | Steel box section for stand | 1 lot | Rated for about 400 kg. Owner fabricates | [product](https://www.ebay.co.uk/itm/128036584011) | £111.00 for 2 × 1.5 m 80 × 80 × 5, free shipping (eBay UK) | 111.00 | REFERENCE ONLY: stand cut list TBD (likely much more than 3 m). 80 × 80 × 5 at £35/m |
| T02 | Levelling feet | 4 pcs |  | [product](https://www.ebay.co.uk/itm/283465312452) | £21.98 for 4, free shipping (eBay UK) | 21.98 | M16, 750 kg each |
| X01 | Dial test indicator + magnetic base | 1 set | For rail alignment and squaring the gantry | [product](https://www.aliexpress.com/item/1005013036061506.html) | £17.20 inc VAT (AliExpress) | 17.20 | Lever DTI 0.01 mm + flexible base |
| X02 | Precision level 0.05 mm/m | 1 pcs | Dasqua 200 mm machine bar level, 0.05 mm/m | [product](https://www.rdgtools.co.uk/product/dasqua-200mm-machine-bar-level-high-sensitivity-0-05mm-graduations-8301-0010/) | £68.50 inc VAT (RDG Tools) | 68.50 | D-42: Dasqua 200 mm 0.05 mm/m. Shipping not shown. 0.02 mm/m alt was £333.72 |
| X03 | Socket cap screw assortment M5-M12 | 1 lot | Includes rail bolts | [product](https://www.ebay.co.uk/itm/336213901049) | £40.99 for 5 kg, free shipping (eBay UK) | 40.99 | M6/M8/M10 only: M5 (rail bolts) and M12 NOT included |

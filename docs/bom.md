# Bill of materials (summary)

Full list: [bom.csv](bom.csv). **81 line items, 77 priced.** Prices were read from live pages on 2026-11-04/05 (by this session and a local browser session).

**Pricing rule:** `price_listed` is exactly what the page showed. `price_gbp` is the GBP line total (all units + listed shipping), inc VAT where known. Lines marked *VAT?* may get VAT added, and import VAT may apply to non-UK orders. EUR/USD prices are not converted.

| Subsystem | Line items | Priced | GBP total |
|---|---|---|---|
| Frame | 19 | 18 | £1,548.40 |
| Motion | 14 | 14 | £890.04 |
| Spindle | 7 | 7 | £1,325.91 |
| Tool changer | 6 | 6 | £256.96 |
| Pneumatics | 6 | 6 | £117.00 |
| Electronics | 20 | 17 | £348.55 |
| Enclosure | 3 | 3 | £217.59 |
| Stand | 2 | 2 | £225.98 |
| Metrology | 2 | 2 | £85.70 |
| Fixings | 2 | 2 | £68.78 |
| **All** | **81** | **77** | **£5,084.91** |

**Budget (D-57): Stage 1 £5,300, Stage 2 £600.** Priced total: **£5,084.91**. Not priced yet: F15, E01, E04, E22.

## Stage totals (D-47)
| Stage | What | GBP priced |
|---|---|---|
| 1 | Frame, motion, spindle, electronics, air, stand, tools | £4,584.70 |
| 2 | Tool rack + drive, enclosure, mist, door switch | £500.21 |

Stage 1 excludes the Mesa board (€309.31, owner-confirmed, not converted), the 48 V and 5 V DIN PSUs (to price) and any import VAT on the spindle. Forks are 3D printed (owner).

## Ten biggest lines
| ID | Item | £ |
|---|---|---|
| S01 | Jianken JGL-80/2.2R24-20 ATC spindle | 990.57 |
| F01 | Epoxy for main frame mix | 666.59 |
| T01 | Stand steel 60 x 60 x 3 | 204.00 |
| M11 | Aluminium tooling plate 330 x 330 x 30 mm | 190.54 |
| M05 | SFU1605 ballscrew + DFU1605 preloaded nut | 186.82 |
| S05 | Spindle water cooler CW-3000 | 144.00 |
| N02 | Polycarbonate panels + door | 142.12 |
| M09 | NEMA 24 closed-loop stepper + driver about 4 Nm | 112.71 |
| M12 | Aluminium plate for X saddle and Z spindle plate | 104.98 |
| M01 | HGR20 rail 650 mm | 104.59 |

## Warnings
- **Not in the total yet:** Mesa 7i76EU (US$219 + shipping; UK import VAT/duty paid on arrival) and 8 forks (US$47.92 + US$13.99 shipping).
- **S01 spindle:** UK import VAT (20%) is likely on top unless Alibaba collects it at checkout. Torque on the page says 0.7 Nm vs 0.87 Nm elsewhere: confirm.
- **M01–M03 rails:** sale price limited to 1 per shopper. At list prices the three kits are £387.63 (+£202.52).
- **S06 holders:** £6.05 may be a new-shopper price. At list price 8 holders are £178.96 (+£130.56). Pull stud must match the spindle.
- **Still to confirm with sellers:** S05 chiller alarm output, S02 VFD RS-485, GCL pallet delivery cost to Swansea (F03/F04).
- **F01 epoxy:** hardener probably included in the ECF packs: confirm by phone.
- **Reference sizes:** M12, A06, N02 and T01 are priced at placeholder sizes until the layout is drawn.

## Full list with links

| ID | Stage | Item | Qty | Spec | Link | Listed price | Line £ | Notes |
|---|---|---|---|---|---|---|---|---|
| F01 | 1 | Epoxy for main frame mix | 1 set | Low-viscosity epoxy with slow hardener | [product](https://ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow) | £295.00 ex VAT (22.68 kg) + 3 × £86.83 ex VAT (4.66 kg) (EC Fibreglass) | 666.59 | 36.66 kg = £555.49 ex VAT, inc VAT calculated. Pack sizes match resin + slow hardener at 100:26, so hardener is PROBABLY INCLUDED: confirm with ECF (0191 4975134). Alt Easy Composites EL2 + AT30 slow £534.00 ex VAT, out of stock. Epoxy choice still open |
| F02 | 1 | Epoxy for leveling pour / grout / samples | 5 kg | Very low viscosity and slow cure (e.g. GlassCast 50 PLUS) | [product](https://www.easycomposites.co.uk/glasscast-50-plus-clear-epoxy-casting-resin) | £76.46 ex VAT per 5 kg kit (Easy Composites) | 91.75 | Inc VAT calculated at 20% |
| F03 | 1 | Coarse aggregate: quartz 2-5 mm | 6 25 kg bags | Washed, kiln-dried angular quartz 2-5 mm (resin-bound grade) | [product](https://www.gclproducts.co.uk/p/resin-bound-gravel/winter-quartz-2-5mm-gravel) | £12.10 ex VAT / £14.52 inc VAT per 25 kg (GCL PermaBound Winter Quartz) | 87.12 | 150 kg. Pallet delivery: cost shown only at checkout, delivery to Swansea not confirmed. Resin-bound aggregates are made for resin, so a good match. Bulk price on request 01246 418144 |
| F04 | 1 | Medium aggregate: quartz 1-3 mm | 4 25 kg bags | Washed, kiln-dried quartz 1-3 mm (resin-bound grade) | [product](https://www.gclproducts.co.uk/p/resin-bound-gravel/autumn-quartz-1-3mm-gravel) | £13.46 ex VAT / £16.15 inc VAT per 25 kg (GCL PermaBound Luxor) | 64.60 | 100 kg. Same pallet as F03 (delivery cost at checkout). Grading overlap with F03 is fine: to be tuned in the packing curve |
| F05 | 1 | Fine sand 0.1-0.5 mm | 2 25 kg bags | Graded aggregate: fine fraction | [product](https://www.diy.com/departments/heidelberg-materials-large-bag-kiln-dried-sand-25kg/5012016180015_BQ.prd) | £17.99 (VAT?) per 25 kg, free next-day delivery (B&Q online) | 35.98 | D-45. 2 bags. Kiln-dried washed silica. PARTIAL: particle size not stated: sieve-check. Previous: £188.40 pallet |
| F06 | 1 | Fine filler (silica flour or fly ash) | 1 lot | Below 0.1 mm | [product](https://potterycrafts.co.uk/products/potterycrafts-quartz-silica-sand?variant=49197100859674) | £36.05 ex VAT per 25 kg (Potterycrafts) | 43.26 | Fine ground quartz. Particle size not stated. Inc VAT calculated. Shipping not shown |
| F07 | 1 | Steel flat bar 40 x 10 mm | 2 3 m bars | 40 × 10 mild steel flat bar, 3 m | [product](https://www.themetalstore.co.uk/products/3-metre-lengths-10mm-flat-bar) | £30.00 ex VAT / £36.00 inc VAT per 3 m bar (The Metal Store) | 72.00 | Delivery not shown. Bright (EN3B) bar is an option for flatter inserts |
| F08 | 1 | M12 threaded rod + nuts (lifting points and joint) | 1 lot | Zinc or plain steel | [product](https://www.ebay.co.uk/itm/361927188666) | £19.65 for 2 × 1 m rods, free shipping (eBay UK) + nuts £9.09 inc VAT (Screwfix) | 28.74 | Nuts: https://www.screwfix.com/p/easyfix-bzp-steel-hex-nuts-m12-100-pack/15569 |
| F09 | 1 | Steel or PVC tube for M12 bolt sleeves | 2 m | About 14-16 mm bore | [product](https://www.screwfix.com/p/deta-tte-round-upvc-white-conduit-20mm-x-3m/256vt) | £2.29 inc VAT per 3 m (Screwfix) | 2.29 | 20 mm uPVC conduit, bore not stated (about 16-17 mm expected, clears M12). Steel alt £10.99: https://www.screwfix.com/p/deta-tte-round-steel-galvanised-class-4-conduit-tube-20mm-x-3m/7734j |
| F10 | 1 | MDF sheet for mould floors | 1 sheet | 18 mm MDF 2440 × 1220: base floor (about 700 × 1,010) + gantry floor (about 700 × 520) in one piece each | [product]() | £28 (B&Q, owner-confirmed), collect | 28.00 | D-61. Seal and coat the floor faces, then wax + PVA |
| F19 | 1 | White gloss furniture panels for mould walls | 2 panels | Semi-edged white gloss panel 2.5 m × 600 × 18: cut to wall strips (about 7.5 m of 200 mm strip per panel) + gantry opening plug | [product]() | £38.97 each (B&Q, owner-confirmed), collect | 77.94 | Gloss face = ready release surface. Wax + PVA anyway. 2 panels allow for the plug and offcuts |
| F11 | 1 | CLS timber 38 x 63 x 2400 (mould bracing) | 9 lengths | Essentials smooth planed C16 whitewood CLS 38 x 63 x 2.4 m | [product](https://www.diy.com/departments/essentials-smooth-planed-c16-whitewood-spruce-cls-timber-l-2-4m-w-63mm-t-38mm/1798294_BQ.prd) | £3.97 each (B&Q, owner-confirmed), collect | 35.73 | 9 lengths, B&Q click and collect (D-43) |
| F12 | 1 | Release agent: PVA + wax | 1 set |  | [product](https://www.ebay.co.uk/itm/235827548462) | PVA £13.50 free shipping (eBay UK) + wax £9.39 inc VAT + £8.79 express (AliExpress) | 31.68 | Wax: https://www.aliexpress.com/item/1005006037723287.html |
| F13 | 1 | Plasticine for corner fillets | 1 set |  | [product](https://www.ebay.co.uk/itm/357951022386) | Plasticine £16.10 + £2.94 shipping (eBay UK) | 19.04 | Packing tape and silicone NOT priced |
| F14 | 1 | Vibration motors | 2 pcs | Unbalanced vibration motors for the vibration table | [product](https://www.ebay.co.uk/itm/900058009643) | £49.86 each, free shipping (eBay UK) | 99.72 | 100 W 230 V with controller. Exciting force not stated. Genuine OLI MVE 200/3E (about 2 kN class) £129.99 + £9.99 each: https://www.ebay.co.uk/itm/277703089794 . Size before buying |
| F15 | 1 | Vibration table springs or rubber mounts + top sheet | 1 set | Takes about 330 kg (mould + casting) | [product](https://www.ebay.co.uk/itm/326960605104) | NOT FOUND (page blocked). Search card: £8.66 + £2.72 per M10 bobbin, 192 kg |  | Unconfirmed. Top sheet not priced |
| F16 | 1 | Temperature probes + logger | 1 set | Thermocouples or DS18B20 probes cast in | [product](https://www.ebay.co.uk/itm/800631453870) | £76.99, free shipping (eBay UK) | 76.99 | 4-ch K/J/T logger. Probes included not stated. AliExpress full match £44.02 is a new-shopper deal (normal £93.84): keep eBay unless the deal is available |
| F17 | 1 | Mixer | 1 pcs | Paddle mixer or small forced-action mixer | [product](https://www.screwfix.com/p/erbauer-epm1600-1600w-electric-paddle-mixer-220-240v/981kj) | £69.99 inc VAT (Screwfix) | 69.99 | Erbauer EPM1600 |
| F18 | 1 | Packing tape + silicone | 1 set | 6 rolls clear tape + neutral-cure silicone | [product](https://www.ebay.co.uk/itm/165130410287) | £8.99 tape + £7.99 silicone, free delivery (eBay UK) | 16.98 | Silicone: https://www.ebay.co.uk/itm/257643689613 |
| M01 | 1 | HGR20 rail 650 mm | 2 pcs | Y: 2 × 650 mm HGR20 + 4 × HGH20CA | [product](https://www.aliexpress.com/item/1005009213173130.html) | £25.59 inc VAT (Kaiyade; normal £26.66) + £79.00 Economy shipping per order | 104.59 | Kaiyade chosen over MHCN (£189.69 at sale prices, but each size is "max 1 per shopper"; £396.77 normal). £79 shipping appears to be per order: CONFIRM IN BASKET that it is charged once for M01-M03. Delivery Nov 21-Dec 18. Store 97.8% |
| M02 | 1 | HGR20 rail 450 mm | 2 pcs | X: 2 × 500 mm HGR20 + 4 × HGH20CA | [product](https://www.aliexpress.com/item/1005009213173130.html) | £22.99 inc VAT (Kaiyade; normal £23.95) | 22.99 | Shipping counted on M01 (one order) |
| M03 | 1 | HGR20 rail 300 mm | 2 pcs | Z: 2 × 350 mm HGR20 + 4 × HGH20CA | [product](https://www.aliexpress.com/item/1005009213173130.html) | £20.29 inc VAT (Kaiyade; normal £21.14) | 20.29 | Shipping counted on M01 (one order) |
| M04 | 1 | HGH20CA carriage Z1 preload | 12 pcs | 4 per axis | [product](https://www.aliexpress.com/item/1005009213173130.html) | Included in M01-M03 | 0 | 4 HGH20CA per Kaiyade kit. Preload not stated |
| M05 | 1 | SFU1605 ballscrew + DFU1605 preloaded nut | 3 pcs | DFU1605 kits (double nut, machined ends, BK12/BF12, housing, coupler): X 450, Y 550, Z 350 mm (listing has no 420/310: next size up, longer than the layout minimums 405/305) | [product](https://www.aliexpress.com/item/1005010046279521.html) | £58.99 (450) + £65.39 (550) + £54.59 (350) inc VAT + £7.85 shipping (AliExpress METALWORK) | 186.82 | Listing does not say overall vs thread length: confirm with the seller (needs overall ≥ X 405 / Y 550 / Z 305). Shipping shown for 1 kit: may be per kit. Normal Y price £74.31 |
| M06 | 1 | BK12 + BF12 end supports | 3 sets |  | [product](https://www.aliexpress.com/item/1005010046279521.html) | Included in M05 | 0 |  |
| M07 | 1 | Nut housing DSG16H | 3 pcs |  | [product](https://www.aliexpress.com/item/1005010046279521.html) | Included in M05 | 0 |  |
| M08 | 1 | Disc or bellows coupling 10 mm to 10 mm | 3 pcs | Listings give a 10 mm shaft on the 4 Nm NEMA 24 (24HS40-5004D-E1000). Verify. BK12 end is 10 mm | [product](https://www.aliexpress.com/item/1005009879991986.html) | £3.35 inc VAT each + £3.04 shipping (AliExpress) | 13.09 | D26 L35 double diaphragm, 10 × 10 bore. All 3 motors confirmed 10 mm shaft |
| M09 | 1 | NEMA 24 closed-loop stepper + driver about 4 Nm | 2 sets | X and Y. Candidate: StepperOnline 1-CL57T-S40-V41 (24HS40-5004D-E1000 + CL57T V4.1 / 24-48 V DC / 1000 PPR encoder) | [product](https://www.omc-stepperonline.com/ts-series-4-0-nm-566-56oz-in-1-axis-closed-loop-stepper-cnc-kit-nema-24-motor-driver-1-cl57t-s40-v41) | £51.34 (VAT?) per set + £10.03 UK warehouse (StepperOnline) | 112.71 | 24HS40-5004D-E1000 + CL57T-V41. Shaft 10 mm D-cut. UK stock 5. VAT basis unclear |
| M10 | 1 | NEMA 24 closed-loop stepper with 24 V brake | 1 set | StepperOnline 24HS34-5004D-E1000-B280: 3 Nm / 5 A / 1000 PPR encoder / 2.8 Nm 24 V power-off brake | [product](https://www.omc-stepperonline.com/s-series-nema-24-closed-loop-stepper-motor-3-0nm-424-92oz-in-with-2-8nm-396-51oz-in-electromagnetic-brake-24hs34-5004d-e1000-b280) | £59.22 (VAT?) (StepperOnline) | 59.22 | China warehouse only, backorder, est. 13-19 Nov. Shaft 10 mm D-cut. Shipping not shown |
| M14 | 1 | CL57T V4.1 closed-loop driver | 1 pcs | For the Z brake motor. 24-48 V DC / 0-8 A | [product](https://www.omc-stepperonline.com/closed-loop-stepper-driver-v4-1-0-8-0a-24-48vdc-for-nema-17-23-24-stepper-motor-cl57t-v41) | £28.75 (VAT?) + £5.47 DE warehouse (StepperOnline) | 34.22 | No UK stock |
| M11 | 1 | Aluminium tooling plate 330 x 330 x 30 mm | 1 pcs | Table. Drill an M6/M8 threaded grid | [product](https://www.aluminiumwarehouse.co.uk/products/30-mm-6082-aluminium-plate) | £158.78 ex VAT (Aluminium Warehouse, 330 × 330 × 30 6082, cut to size) | 190.54 | Inc VAT calculated at 20%. Shipping not shown. Cast tooling plate (flatter) £216.11 ex VAT: https://www.aluminiumwarehouse.co.uk/products/30-mm-aluminium-cast-tooling-plate |
| M12 | 1 | Aluminium plate for X saddle and Z spindle plate | 1 lot | 20 mm 6082: X saddle about 200 × 230, Z plate about 160 × 330 (layout) | [product](https://www.aluminiumwarehouse.co.uk/products/20-mm-6082-aluminium-plate) | £87.48 ex VAT for reference 300 × 300 × 20 (Aluminium Warehouse) | 104.98 | REFERENCE SIZE ONLY: real sizes come from the layout. Inc VAT calculated |
| M13 | 1 | Motor and bearing mounts | 1 lot | Machined or bought brackets | [product](https://www.aliexpress.com/item/1005006232398099.html) | £9.99 inc VAT each + £10.62 shipping (AliExpress) | 40.59 | HM12-60 motor bracket with fixed bearing seat (replaces BK12 at motor end). Check fit with M05 |
| S01 | 1 | Jianken JGL-80/2.2R24-20 ATC spindle | 1 pcs | 2.2 kW / 24000 rpm / 400 Hz / 220 V / about 0.87 Nm / ISO20 / water-cooled / 80 mm body. Order the clamp/unclamp sensor variant (PNP) | [product](https://www.alibaba.com/product-detail/Jianken-JGL-80-2-2KW-24000RPM_1601249825246.html) | £937.79 (VAT?) + £52.78 shipping (Alibaba, 1-4 pcs) | 990.57 | Drawing confirms JGL-80/2.2R24, 220 V, 400 Hz, ISO20-ER16, water-cooled. Sensors: clamped/released + temperature, PNP 24 V. VFD not included. Pull stud not shown. KEY ATTRIBUTES SAY 0.7 Nm (other listings 0.87 Nm): confirm with Jianken. Import VAT likely on top. Delivery 18 Nov-19 Dec. Alt AliExpress with 2.2 kW VFD £1402.79 inc VAT + £140.15: https://www.aliexpress.com/item/1005010706946690.html |
| S02 | 1 | VFD 2.2 kW with RS-485 Modbus | 1 pcs | 2.2 kW, 1-phase 220 V in, 3-phase 220 V out, 0-600 Hz, RS-485 Modbus-RTU stated | [product](https://www.aliexpress.com/item/1005013518595862.html) | £71.99 inc VAT early-bird deal (only 1 left); normal £88.94; free shipping (AliExpress, ZEST Factory Store) | 88.94 | FULL MATCH incl. RS-485 Modbus (D-32). Budgeted at the normal price. Store 96.7%, 216 sold. Previous Huanyang £124.84 had no RS-485 stated |
| S03 | 1 | Spindle mount clamp to suit spindle body diameter | 1 pcs | 80 mm | [product](https://www.aliexpress.com/item/4001010906801.html) | £17.89 inc VAT, free shipping (AliExpress) | 17.89 | 80 mm clamp |
| S04 | 1 | Shielded 4-core spindle cable | 5 m |  | [product](https://www.aliexpress.com/item/32971008305.html) | £18.22 inc VAT for 5 m (AliExpress) | 18.22 | 4-core 16 AWG (about 1.3 mm²) shielded: slightly under 1.5 mm². Shipping not shown |
| S05 | 1 | Spindle water cooler CW-3000 | 1 pcs | CW-3000TG (220 V 1-phase / 9 L tank / 10 L/min max) | [product](https://www.ebay.co.uk/itm/315204411696) | £144.00 (VAT?), free courier (eBay UK) | 144.00 | CW-3000 SDKEHUI, flow + temperature alarms, 3-year warranty. ALARM OUTPUT TERMINAL NOT STATED: ask seller. Previous: £208.42 |
| S06 | 1 | ISO20 ER16 holders with pull studs | 8 pcs | ISO20-ER16. Pull studs must match the spindle drawbar | [product](https://www.aliexpress.com/item/4000141590118.html) | £6.05 inc VAT each, free shipping (AliExpress; list £22.37) | 48.40 | ISO20-ER16-35L, 0.003 mm. £6.05 may be a new-shopper deal: at list price 8 × £22.37 = £178.96. PULL STUD NOT STATED: must match Jianken. Jianken own holders £37.52-75.03 on the S01 page. DamenCNC Teknomotor €123.50 each |
| S07 | 1 | ER16 collet set | 1 set | Precision (AA grade or better) 1-10 mm | [product](https://www.aliexpress.com/item/1005005626185405.html) | £17.89 inc VAT, free shipping (AliExpress) | 17.89 | AA ER16 10-piece set. Sizes not listed. AAA set £68.39 |
| A01 | 2 | ISO20 tool forks (3D printed) | 8 pcs | 3D-printed ISO20 forks from a friend's model | [product]() | Owner sourcing (3D printed) | 0.00 | D-58. Print in PETG/ASA/PA for stiffness and heat. Check grip force and holder fit before Stage 2 |
| A02 | 2 | Rack slide linear guide (e.g. MGN15) + carriage | 2 sets | 2 × MGN15H rail 550 mm + 1 block each | [product](https://www.ebay.co.uk/itm/227244866634) | £32.99 each (VAT?), free courier (eBay UK, VAT-registered seller) | 65.98 | Same listing, full match |
| A03 | 2 | Small closed-loop stepper + driver (48 V) | 1 set | Drives the rack slide | [product](https://www.omc-stepperonline.com/1-axis-closed-loop-stepper-cnc-kit-80ncm-113-29oz-in-nema-17-motor-driver-1-cl42t-s08-v41) | £39.43 (VAT?) + £8.34 DE warehouse (StepperOnline) | 47.77 | 1-CL42T-S08-V41: NEMA 17 0.8 Nm + CL42T 24-48 V. 5 mm shaft |
| A04 | 2 | Rack drive screw or belt + pulleys | 1 set | SFU1204 500 mm + housing + BK10/BF10 + coupling | [product](https://www.aliexpress.com/item/1005006187129418.html) | £46.59 inc VAT, free shipping (AliExpress BST; normal £54.81) | 46.59 | Full match |
| A05 | 2 | Tool length setter (wired switch) | 1 pcs | On the rack carrier | [product](https://www.aliexpress.com/item/1005012101891449.html) | £17.89 inc VAT, free shipping (AliExpress) | 17.89 | N96R, 24 V, NC |
| A06 | 2 | Rack plate and fork mount | 1 lot | Aluminium plate | [product](https://www.aluminiumwarehouse.co.uk/products/15-mm-6082-aluminium-plate) | £65.61 ex VAT for reference 300 × 300 × 15 (Aluminium Warehouse) | 78.73 | REFERENCE SIZE ONLY. Inc VAT calculated |
| P01 | 1 | Filter / regulator / dryer | 1 pcs |  | [product](https://www.aliexpress.com/item/1005002589702135.html) | £6.50 inc VAT (AliExpress) | 6.50 | AW2000-02 filter-regulator. No dryer |
| P02 | 1 | 24 V solenoid valves | 4 pcs | Tool release / taper clean / air blast | [product](https://www.aliexpress.com/item/1005012294513653.html) | £9.49 inc VAT each, free shipping (AliExpress) | 37.96 | 3V1-06 24 V 3/2 NC. Qty 4 (3 + 1 for mist unit) |
| P03 | 1 | Air pressure switch | 1 pcs | About 5.5 bar trip point | [product](https://www.aliexpress.com/item/1005013285557375.html) | £5.17 (VAT?) + £3.79 shipping (AliExpress) | 8.96 | QPM11-NO-02. NO contact |
| P04 | 2 | Mist coolant system with 24 V solenoid | 1 set |  | [product](https://www.aliexpress.com/item/1005012241646016.html) | £17.59 inc VAT (AliExpress) | 17.59 | BPV-3000 mist unit, no solenoid (uses 4th P02 valve) |
| P05 | 1 | Push-fit tubing and fittings 6/8 mm | 1 lot |  | [product](https://www.aliexpress.com/item/1005006780298909.html) | £4.31 + £7.56 inc VAT (AliExpress) | 11.87 | 10 m 6 × 4 + 10 m 8 × 5 PU. Fittings NOT priced |
| P06 | 1 | Push-in fittings | 12 pcs | 8 × 6 mm-1/8 BSP + 4 × 8 mm-1/4 BSP (PROVISIONAL quantities) | [product](https://www.ebay.co.uk/itm/156691426151) | £2.77 each (6 mm) + £2.99 each (8 mm), free delivery (eBay UK) | 34.12 | 8 mm: https://www.ebay.co.uk/itm/110811089560 . Quantities to confirm from the pneumatic layout |
| E01 | 1 | Mesa 7i76EU | 1 pcs |  | [product](https://store.mesanet.com/index.php?route=product/product&product_id=399) | €309.31 (owner-confirmed total) |  | Owner-confirmed price in EUR. Not converted to GBP: add the GBP card charge once paid. Import VAT may apply |
| E02 | 1 | Mini-PC (owner already has) | 1 pcs |  | [product]() | Owner sourced | 0.00 | D-58. Onboard Intel NIC goes to the Mesa board. No 2nd NIC: machine stays offline |
| E03 | 1 | Monitor + keyboard + mouse (owner already has) | 1 set |  | [product]() | Owner sourced | 0.00 | D-58 |
| E04 | 1 | 48 V DC PSU, DIN rail (Mean Well) | 1 pcs | Mean Well DIN rail 48 V ≥ 10 A (e.g. NDR-480-48, SDR-480-48, XDR-480-48) | [product](https://www.rapidonline.com/mean-well-sdr-480-48-rail-psu-48v-10a-480w-din-rail-mount-universal-input-05-1702) | Rapid SDR-480-48 £168.56 ex VAT (confirmed 2026-11-04); others to price |  | D-59: DIN rail for cabinet space. TO PRICE: cheapest DIN 48 V 10 A Mean Well |
| E05 | 1 | 24 V DC PSU, DIN rail (Mean Well HDR-150-24) | 1 pcs | Mean Well HDR-150-24, DIN rail | [product](https://www.omc-stepperonline.com/hdr-150-24-mean-well-24vdc-5-31a-127-4w-115vac-6-25a-150w-230vac-ultra-slim-step-shape-din-rail-power-supply-hdr-150-24) | £27.62 (VAT?), pre-order (StepperOnline, read 2026-11-05) | 27.62 | D-59. Pre-order: check stock. Shipping not shown |
| E22 | 1 | 5 V DC PSU, DIN rail (low wattage) | 1 pcs | Mean Well DIN rail 5 V, about 15 W (e.g. HDR-15-5) | [product]() |  |  | TO PRICE |
| E06 | 1 | E-stop safety relay (used Pilz PNOZ X2.1) | 1 pcs | CM Manufactory SAFE 4.3eco 45320 (24 V AC/DC / 3 NO + 1 NC) | [product](https://www.ebay.co.uk/itm/407310782945) | £27.74 (VAT?) + £2.94 tracked, used (eBay UK) | 30.68 | Used Pilz PNOZ X2.1 774306, 24 V, dual channel, 2 NO, manual reset. Better used PNOZ X2 £39.99 (seller 4.6K): https://www.ebay.co.uk/itm/375423870735 . Previous: £116.20 new |
| E07 | 1 | Contactor with 24 V coil | 1 pcs |  | [product](https://www.aliexpress.com/item/1005005356561757.html) | £26.19 inc VAT, free shipping (AliExpress) | 26.19 | Schneider LC1D09BDC 9 A 24 V DC coil. Genuine not verified. 9 A is enough for the 48 V / VFD control duty but check against the circuit design |
| E08 | 1 | E-stop mushroom buttons + reset button | 1 set |  | [product](https://www.aliexpress.com/item/1005008293871583.html) | £8.15 inc VAT for 5, free shipping (AliExpress) | 8.15 | XB2-BS542, 1 NC. Reset button not included |
| E09 | 1 | MCBs / main isolator / EMC filter for VFD | 1 set |  | [product](https://www.aliexpress.com/item/1005010519550019.html) | £10.39 inc VAT (AliExpress) | 10.39 | CW4L2-20A-S. MCBs and isolator NOT priced |
| E10 | 1 | Inductive proximity switches 24 V | 4 pcs | Homing X / Y / Z / rack | [product](https://www.aliexpress.com/item/1005010648075147.html) | £1.54 inc VAT each + £3.41 shipping (AliExpress) | 9.57 | LJ12A3-4-Z/BY PNP NO |
| E12 | 1 | Electrical cabinet 600 x 400 x 200 | 1 set | Galvanised steel 600 × 400 × 200, IP66, 2 mm mounting plate (mount on its side) | [product](https://www.ebay.co.uk/itm/206672920149) | £65.95 (VAT?), free courier (eBay UK) | 65.95 | D-53. 0.8 mm body steel. Better: MCG M64200 IP65 with gland plate £85.03 delivered https://www.ebay.co.uk/itm/327344915454 . Filter fan on E18 |
| E13 | 1 | DIN rail / terminals / wiring / ferrules | 1 lot |  | [product](https://www.aliexpress.com/item/1690060053.html) | £33.79 inc VAT for 100, free shipping (AliExpress) | 33.79 | Terminals only. DIN rail, ferrules, wire NOT priced |
| E14 | 1 | Cable chain and shielded motor cables | 1 lot |  | [product](https://www.aliexpress.com/item/1005012723966521.html) | £15.69 inc VAT per 1 m, free shipping (AliExpress) | 15.69 | 1 m only: length TBD. Shielded motor cable NOT priced |
| E15 | 2 | Enclosure door switch | 1 pcs |  | [product](https://www.aliexpress.com/item/1005006072968001.html) | £8.07 inc VAT (AliExpress) | 8.07 | CZ-93B key interlock, 2 NC. No safety standard stated |
| E17 | 1 | Main isolator + MCBs | 1 set | 2-pole isolator, 1 × C16, 2 × C6 | [product](https://www.toolstation.com/altrion-dp-incomer-switch/pAH631) | £7.99 inc VAT isolator (Toolstation) + £6.50 C16 + 2 × £5.00 C6 used (eBay UK) | 24.49 | C16: https://www.ebay.co.uk/itm/137268981930 . C6: https://www.ebay.co.uk/itm/387438925848 |
| E18 | 1 | Cabinet fan + filters | 1 set | 120 mm 230 V fan + 2 washable filters | [product](https://www.ebay.co.uk/itm/128137523659) | £9.71 + £3.38 fan, £4.37 filters (eBay UK) | 17.46 | Filters (PC type, not IP rated): https://www.ebay.co.uk/itm/257636727653 |
| E19 | 1 | DIN rail + ferrules + wire | 1 set | 1 m DIN, ferrule kit + crimper, 0.75 and 1.5 mm² wire 10 m each | [product](https://www.ebay.co.uk/itm/174026089905) | £7.94 + £1.99 DIN, £7.99 ferrules, £4.30 + £2.99 + £2.85 wire (eBay UK) | 28.06 | Ferrules: https://www.ebay.co.uk/itm/860051234272 . 0.75: https://www.ebay.co.uk/itm/115469225740 . 1.5: https://www.ebay.co.uk/itm/257223178155 |
| E20 | 1 | Shielded motor/encoder cable | 15 m | CY 4-core 1.0 mm² | [product](https://www.ebay.co.uk/itm/171352110328) | £2.14 per m + £3.95 (eBay UK) | 36.05 |  |
| E21 | 1 | Reset push button | 1 pcs | 22 mm green momentary | [product](https://www.ebay.co.uk/itm/286127619269) | £6.39, free delivery (eBay UK) | 6.39 |  |
| N01 | 2 | Enclosure frame (aluminium extrusion) | 1 lot |  | [product](https://www.ebay.co.uk/itm/401900585637) | £72.73 for 8 × 1000 mm, free shipping (eBay UK) | 72.73 | 4040 slot 8. Cut list TBD |
| N02 | 2 | Polycarbonate panels + door | 1 lot |  | [product](https://www.cutmy.co.uk/plastic/polycarbonate-sheets/6mm/L1000-W1000/) | £129.17 inc VAT for reference 1000 × 1000 × 6 + shipping from £12.95 (Cut My) | 142.12 | REFERENCE SIZE ONLY: panel sizes TBD |
| N03 | 2 | LED light | 1 pcs |  | [product](https://www.aliexpress.com/item/1005013221981188.html) | £2.74 inc VAT (AliExpress) | 2.74 | 24-36 V 5 W |
| T01 | 1 | Stand steel 60 x 60 x 3 | 1 lot | 60 × 60 × 3 mild steel box, 6 × 2000 mm (12 m) | [product](https://www.ebay.co.uk/itm/128036584011) | £34.00 per 2 m (VAT?), free Royal Mail 48 or collect Newport (eBay UK) | 204.00 | D-54. Each 2 m gives 1010 + 700 or 700 + 620 + 620. Alt BM Steel 2 × 7.5 m £158.60 inc VAT + delivery (needs postcode): https://www.bmsteel.co.uk/60-x-60-x-3mm-75m-square-hollow-section-bsen10219-s235jr/p381 |
| T02 | 1 | Levelling feet | 4 pcs |  | [product](https://www.ebay.co.uk/itm/283465312452) | £21.98 for 4, free shipping (eBay UK) | 21.98 | M16, 750 kg each |
| X01 | 1 | Dial test indicator + magnetic base | 1 set | For rail alignment and squaring the gantry | [product](https://www.aliexpress.com/item/1005013036061506.html) | £17.20 inc VAT (AliExpress) | 17.20 | Lever DTI 0.01 mm + flexible base |
| X02 | 1 | Precision level 0.05 mm/m | 1 pcs | Dasqua 200 mm machine bar level, 0.05 mm/m | [product](https://www.rdgtools.co.uk/product/dasqua-200mm-machine-bar-level-high-sensitivity-0-05mm-graduations-8301-0010/) | £68.50 inc VAT (RDG Tools) | 68.50 | D-42: Dasqua 200 mm 0.05 mm/m. Shipping not shown. 0.02 mm/m alt was £333.72 |
| X03 | 1 | Socket cap screw assortment M5-M12 | 1 lot | Includes rail bolts | [product](https://www.ebay.co.uk/itm/336213901049) | £40.99 for 5 kg, free shipping (eBay UK) | 40.99 | M6/M8/M10 only: M5 (rail bolts) and M12 NOT included |
| X04 | 1 | M5 and M12 socket caps | 1 set | 100 × M5 × 16 + 10 × M12 × 120, grade 12.9 | [product](https://www.ebay.co.uk/itm/164030323707) | £9.82 + £17.97, free delivery (eBay UK) | 27.79 | M12: https://www.ebay.co.uk/itm/361974204301 |

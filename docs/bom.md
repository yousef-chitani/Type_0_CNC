# Bill of materials (summary)

Full list: [bom.csv](bom.csv). **72 line items.**

**Pricing rule:** a price is only entered when it has been read from a live supplier page, with the date and link. A blank price means *not confirmed*. Totals only add up confirmed prices.

| Subsystem | Line items | Confirmed total |
|---|---|---|
| Frame | 17 | — |
| Motion | 14 | — |
| Spindle | 7 | — |
| Tool changer | 6 | — |
| Pneumatics | 5 | — |
| Electronics | 15 | — |
| Enclosure | 3 | — |
| Stand | 2 | — |
| Metrology | 2 | — |
| Fixings | 1 | — |
| **All** | **72** | **— (none confirmed yet)** |

Budget: £4,500.

## Status
- Round 8: parts and specs listed, waiting for the owner to review.
- Every row has a link: a product page where a match was found, otherwise a search link. The owner confirms prices.
- Rail and screw lengths are drafts until the layout is drawn.

## Full list with links

Generated from bom.csv. Price is blank until confirmed.

| ID | Item | Qty | Spec | Link | Price (£) | Notes |
|---|---|---|---|---|---|---|
| F01 | Epoxy for main frame mix | 37 kg | Low-viscosity epoxy with slow hardener | [product](https://ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow) |  | Product pending owner's recommendations (open question 13). Candidate only (epoxy still open) |
| F02 | Epoxy for leveling pour / grout / samples | 5 kg | Very low viscosity and slow cure (e.g. GlassCast 50 PLUS) | [product](https://www.easycomposites.co.uk/glasscast-50-plus-clear-epoxy-casting-resin) |  | Price on epoxy-options.md once the product is chosen |
| F03 | Kiln-dried quartz gravel 2-5 mm | 1 lot | Graded aggregate: coarse fraction | [search](https://www.google.com/search?q=kiln+dried+quartz+gravel+2-5mm+25kg+UK) |  | Grading split to be set from the packing curve. Total aggregate is about 280 kg plus test bricks. Search link. Supplier depends on the grading (open question 5) |
| F04 | Kiln-dried sand 0.5-2 mm | 1 lot | Graded aggregate: medium fraction | [search](https://www.google.com/search?q=kiln+dried+silica+sand+0.5-2mm+25kg+UK) |  | Search link |
| F05 | Fine sand 0.1-0.5 mm | 1 lot | Graded aggregate: fine fraction | [search](https://www.google.com/search?q=kiln+dried+silica+sand+0.1-0.5mm+25kg+UK) |  | Search link |
| F06 | Fine filler (silica flour or fly ash) | 1 lot | Below 0.1 mm | [search](https://www.google.com/search?q=silica+flour+25kg+UK) |  | Search link |
| F07 | Steel flat bar 40 x 10 mm | 4 m | Insert bars for rails and pads. Drill and tap M5 for rails and M12 for the gantry joint | [search](https://www.google.com/search?q=40+x+10+mild+steel+flat+bar+cut+to+length+UK) |  | Covers Y and X rails plus gantry pads and bearing-block pads. Search link |
| F08 | M12 threaded rod + nuts (lifting points and joint) | 1 lot | Zinc or plain steel | [search](https://www.google.com/search?q=M12+threaded+rod+zinc+1m+UK) |  | Search link |
| F09 | Steel or PVC tube for M12 bolt sleeves | 2 m | About 14-16 mm bore | [search](https://www.google.com/search?q=16mm+ID+steel+tube+1m+UK) |  | Search link |
| F10 | Melamine-faced board 2440 x 1220 x 18 mm | 3 sheet | Mould walls and floors | [search](https://www.google.com/search?q=melamine+faced+MDF+2440+x+1220+x+18mm) |  | Search link |
| F11 | Timber battens 44 x 44 mm | 20 m | Floor support and wall bracing | [search](https://www.google.com/search?q=PSE+timber+batten+44+x+44mm) |  | Search link |
| F12 | Release wax + PVA release film | 1 set |  | [search](https://www.google.com/search?q=mould+release+wax+PVA+release+agent+UK) |  | Search link |
| F13 | Packing tape / silicone / plasticine for fillets | 1 set |  | [search](https://www.google.com/search?q=packing+tape+silicone+sealant+plasticine) |  | Search link |
| F14 | Vibration motors | 2 pcs | Unbalanced vibration motors for the vibration table | [search](https://www.google.com/search?q=vibration+motor+230V+single+phase+concrete+vibrating+table) |  | Single-phase 230 V. Search link |
| F15 | Vibration table springs or rubber mounts + top sheet | 1 set | Takes about 330 kg (mould + casting) | [search](https://www.google.com/search?q=anti+vibration+rubber+mount+M10+heavy+duty) |  | Search link |
| F16 | Temperature probes + logger | 1 set | Thermocouples or DS18B20 probes cast in | [search](https://www.google.com/search?q=K+type+thermocouple+data+logger+4+channel) |  | For curing-heat monitoring. Search link |
| F17 | Mixer | 1 pcs | Paddle mixer or small forced-action mixer | [search](https://www.google.com/search?q=paddle+mixer+1600W+plaster+mortar) |  | Search link |
| M01 | HGR20 rail 650 mm | 2 pcs | Y axis | [product](https://www.ebay.com/itm/402754263172) |  | Lengths are drafts and will be confirmed in the layout. Per-axis kit: 2 HGR20 rails (choose length) + 4 HGH20CA blocks. Check that Z1 preload is offered |
| M02 | HGR20 rail 450 mm | 2 pcs | X axis | [product](https://www.ebay.com/itm/402754263172) |  | Same listing, 450 mm |
| M03 | HGR20 rail 300 mm | 2 pcs | Z axis | [product](https://www.ebay.com/itm/402754263172) |  | Same listing, 300 mm |
| M04 | HGH20CA carriage Z1 preload | 12 pcs | 4 per axis | [product](https://www.ebay.com/itm/402754263172) |  | Usually bundled with the rails. Included in the kits above (4 blocks per kit) |
| M05 | SFU1605 ballscrew + DFU1605 preloaded nut | 3 pcs | C7 rolled. Ends machined for BK12/BF12. X about 420 mm / Y about 500 mm / Z about 280 mm | [product](https://www.ebay.de/itm/126285976798) |  | Lengths are drafts. Kit includes BK12/BF12 + DSG16H + coupling. Listing shows a single SFU nut: ask the seller for a preloaded DFU1605 nut (D-10) |
| M06 | BK12 + BF12 end supports | 3 sets |  | [product](https://www.ebay.de/itm/126285976798) |  | Often bundled with the screws. Included in the M05 kit |
| M07 | Nut housing DSG16H | 3 pcs |  | [product](https://www.ebay.de/itm/126285976798) |  | Included in the M05 kit |
| M08 | Disc or bellows coupling 10 mm to 10 mm | 3 pcs | Listings give a 10 mm shaft on the 4 Nm NEMA 24 (24HS40-5004D-E1000). Verify. BK12 end is 10 mm | [search](https://www.google.com/search?q=disc+coupling+10mm+10mm+D25+aluminium) |  | Search link. The M05 kit coupling is likely a jaw type: disc coupling preferred |
| M09 | NEMA 24 closed-loop stepper + driver about 4 Nm | 2 sets | X and Y. Candidate: StepperOnline 1-CL57T-S40-V41 (24HS40-5004D-E1000 + CL57T V4.1 / 24-48 V DC / 1000 PPR encoder) | [product](https://www.omc-stepperonline.com/ye-series-1-axis-closed-loop-stepper-cnc-kit-4-0-nm-566-56oz-in-nema-24-motor-and-driver.html) |  | Price not confirmed (site blocks automated reading) |
| M10 | NEMA 24 closed-loop stepper with 24 V brake | 1 set | StepperOnline 24HS34-5004D-E1000-B280: 3 Nm / 5 A / 1000 PPR encoder / 2.8 Nm 24 V power-off brake | [product](https://www.omc-stepperonline.com/s-series-nema-24-closed-loop-stepper-motor-3-0nm-424-92oz-in-with-2-8nm-396-51oz-in-electromagnetic-brake-24hs34-5004d-e1000-b280) |  | Motor only: driver is row M14. Check shaft diameter for the coupling |
| M14 | CL57T V4.1 closed-loop driver | 1 pcs | For the Z brake motor. 24-48 V DC / 0-8 A | [search](https://www.google.com/search?q=StepperOnline+CL57T+V4.1+closed+loop+driver) |  | Search link |
| M11 | Aluminium tooling plate 330 x 330 x 30 mm | 1 pcs | Table. Drill an M6/M8 threaded grid | [search](https://www.google.com/search?q=6082+aluminium+tooling+plate+30mm+cut+to+size+UK) |  | Search link |
| M12 | Aluminium plate for X saddle and Z spindle plate | 1 lot | About 20 mm thick. Sizes from the layout | [search](https://www.google.com/search?q=6082+aluminium+plate+20mm+cut+to+size+UK) |  | Search link |
| M13 | Motor and bearing mounts | 1 lot | Machined or bought brackets | [search](https://www.google.com/search?q=NEMA+24+motor+mount+BK12+bracket) |  | Search link |
| S01 | Jianken JGL-80/2.2R24-20 ATC spindle | 1 pcs | 2.2 kW / 24000 rpm / 400 Hz / 220 V / about 0.87 Nm / ISO20 / water-cooled / 80 mm body. Order the clamp/unclamp sensor variant (PNP) | [product](https://www.alibaba.com/product-detail/Jianken-JGL-80-2-2KW-24000RPM_1601249825246.html) |  | Owner's pick. Confirm specs with the seller. Also on Amazon: https://www.amazon.com/LVSEDTAL-JGL-80-2-2R24-20-24000rpm-Spindle/dp/B0F5HKDVV4 |
| S02 | VFD 2.2 kW single-phase input with RS-485 Modbus | 1 pcs | 220 V 3-phase output / up to 400 Hz / single-phase 230 V input | [search](https://www.google.com/search?q=2.2kW+VFD+220V+single+phase+input+400Hz+RS485+Modbus+spindle) |  | Search link |
| S03 | Spindle mount clamp to suit spindle body diameter | 1 pcs | 80 mm | [search](https://www.google.com/search?q=80mm+spindle+mount+clamp+aluminium) |  | Search link |
| S04 | Shielded 4-core spindle cable | 5 m |  | [search](https://www.google.com/search?q=shielded+4+core+1.5mm+cable+spindle+VFD) |  | Search link |
| S05 | CW-3000-style radiator unit with flow alarm | 1 pcs |  | [search](https://www.google.com/search?q=CW-3000+water+chiller+flow+alarm+230V+UK) |  | Confirm the flow alarm output. Search link |
| S06 | ISO20 ER16 holders with pull studs | 8 pcs | ISO20-ER16. Pull studs must match the spindle drawbar | [product](https://damencnc.com/en/iso20-er16-toolholder-pullstud/a3865) |  | Candidate. Pull stud must match the Jianken drawbar: check the spindle datasheet first |
| S07 | ER16 collet set | 1 set | Precision (AA grade or better) 1-10 mm | [search](https://www.google.com/search?q=ER16+collet+set+AA+precision+1-10mm) |  | Search link |
| A01 | ISO20 tool forks | 8 pcs | For the 2 x 4 rack | [product](https://ricocnc.com/products/82-ISO20-Toolholder-Forks-Plastic-Tool-Clips-for-ATC-CNC-Machine.html) |  | Candidate |
| A02 | Rack slide linear guide (e.g. MGN15) + carriage | 2 sets | Rack carrier | [search](https://www.google.com/search?q=MGN15+linear+rail+400mm+MGN15H+block) |  | Search link |
| A03 | Small closed-loop stepper + driver (48 V) | 1 set | Drives the rack slide | [search](https://www.google.com/search?q=NEMA+17+closed+loop+stepper+driver+48V+kit) |  | Search link |
| A04 | Rack drive screw or belt + pulleys | 1 set | Stroke about 300 mm. Sized in the layout | [search](https://www.google.com/search?q=SFU1204+ballscrew+400mm+kit) |  | Search link |
| A05 | Tool length setter (wired switch) | 1 pcs | On the rack carrier | [search](https://www.google.com/search?q=CNC+tool+length+sensor+setter+normally+closed+24V) |  | Search link |
| A06 | Rack plate and fork mount | 1 lot | Aluminium plate | [search](https://www.google.com/search?q=6082+aluminium+plate+15mm+cut+to+size+UK) |  | Search link |
| P01 | Filter / regulator / dryer | 1 pcs |  | [search](https://www.google.com/search?q=air+filter+regulator+dryer+1%2F4+BSP+compressor) |  | Search link |
| P02 | 24 V solenoid valves | 3 pcs | Tool release / taper clean / air blast | [search](https://www.google.com/search?q=24V+DC+3%2F2+solenoid+valve+1%2F8+BSP+pneumatic) |  | Search link |
| P03 | Air pressure switch | 1 pcs | About 5.5 bar trip point | [search](https://www.google.com/search?q=adjustable+air+pressure+switch+24V+1%2F4+BSP) |  | Search link |
| P04 | Mist coolant system with 24 V solenoid | 1 set |  | [search](https://www.google.com/search?q=mist+coolant+system+CNC+solenoid+24V) |  | Search link |
| P05 | Push-fit tubing and fittings 6/8 mm | 1 lot |  | [search](https://www.google.com/search?q=push+fit+pneumatic+tubing+6mm+8mm+fittings+kit) |  | Search link |
| E01 | Mesa 7i76EU | 1 pcs |  | [product](https://store.mesanet.com) |  | No UK reseller found. EU option: EuSurplus (per LinuxCNC forum). Price not confirmed |
| E02 | x86 mini-PC with Intel NIC (2nd port for Mesa) | 1 pcs |  | [search](https://www.google.com/search?q=Lenovo+ThinkCentre+Tiny+used+Intel+NIC) |  | Search link (eBay). Needs a 2nd Intel NIC: check for a model with an expansion slot |
| E03 | Monitor + keyboard + mouse | 1 set |  | [search](https://www.google.com/search?q=used+monitor+keyboard+mouse) |  | Search link |
| E04 | 48 V DC power supply about 10 A | 1 pcs | For the stepper drives | [product](https://uk.rs-online.com/web/p/switching-power-supplies/6448290) |  | Mean Well PSP-600-48 (48 V / 12.5 A / 600 W / 88-264 V AC input). Also at Rapid: https://www.rapidonline.com/mean-well-psp-600-48-series-enclosed-smpsu-48v-12-5a-600w-pfc-protections-05-1370 |
| E05 | 24 V DC power supply | 1 pcs | For I/O / brake / valves / sensors | [search](https://www.google.com/search?q=Mean+Well+24V+150W+DIN+rail+power+supply+UK) |  | Search link |
| E06 | Safety relay (e-stop) | 1 pcs |  | [search](https://www.google.com/search?q=emergency+stop+safety+relay+24V+dual+channel+DIN) |  | Search link |
| E07 | Contactor with 24 V coil | 1 pcs |  | [search](https://www.google.com/search?q=contactor+24V+DC+coil+3+pole+16A+DIN) |  | Search link |
| E08 | E-stop mushroom buttons + reset button | 1 set |  | [search](https://www.google.com/search?q=emergency+stop+mushroom+button+22mm+NC) |  | Search link |
| E09 | MCBs / main isolator / EMC filter for VFD | 1 set |  | [search](https://www.google.com/search?q=EMC+filter+single+phase+20A+VFD) |  | Search link |
| E10 | Inductive proximity switches 24 V | 4 pcs | Homing X / Y / Z / rack | [search](https://www.google.com/search?q=LJ12A3-4-Z%2FBY+PNP+inductive+proximity+switch) |  | Search link |
| E11 | USB to RS-485 adapter | 1 pcs | For VFD Modbus if not using the board's port | [search](https://www.google.com/search?q=USB+to+RS485+adapter+FTDI) |  | Search link |
| E12 | Steel cabinet + filtered fan | 1 set | Built into the stand | [search](https://www.google.com/search?q=steel+electrical+enclosure+600x500x200+IP65) |  | Search link |
| E13 | DIN rail / terminals / wiring / ferrules | 1 lot |  | [search](https://www.google.com/search?q=DIN+rail+terminal+block+kit+ferrules) |  | Search link |
| E14 | Cable chain and shielded motor cables | 1 lot |  | [search](https://www.google.com/search?q=cable+drag+chain+25x38+shielded+motor+cable) |  | Search link |
| E15 | Enclosure door switch | 1 pcs |  | [search](https://www.google.com/search?q=safety+door+interlock+switch+24V) |  | Search link |
| N01 | Enclosure frame (aluminium extrusion) | 1 lot |  | [search](https://www.google.com/search?q=40x40+aluminium+extrusion+cut+to+length+UK) |  | Search link |
| N02 | Polycarbonate panels + door | 1 lot |  | [search](https://www.google.com/search?q=polycarbonate+sheet+6mm+cut+to+size+UK) |  | Search link |
| N03 | LED light | 1 pcs |  | [search](https://www.google.com/search?q=24V+LED+machine+light) |  | Search link |
| T01 | Steel box section for stand | 1 lot | Rated for about 400 kg. Owner fabricates | [search](https://www.google.com/search?q=80x80x4+steel+box+section+UK) |  | Search link |
| T02 | Levelling feet | 4 pcs |  | [search](https://www.google.com/search?q=heavy+duty+machine+levelling+feet+M16) |  | Search link |
| X01 | Dial test indicator + magnetic base | 1 set | For rail alignment and squaring the gantry | [search](https://www.google.com/search?q=dial+test+indicator+0.01mm+magnetic+base) |  | Search link |
| X02 | Precision level 0.02 mm/m | 1 pcs | For the leveling pour and machine setup | [search](https://www.google.com/search?q=precision+machinist+level+0.02mm%2Fm+200mm) |  | Search link |
| X03 | Socket cap screw assortment M5-M12 | 1 lot | Includes rail bolts | [search](https://www.google.com/search?q=socket+cap+screw+assortment+M5+M12+stainless) |  | Search link |

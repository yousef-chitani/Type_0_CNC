#!/usr/bin/env python3
"""Open the Type 0 CNC parts-list links as tabs in Firefox. Standalone: the links are built in.

Usage (from the folder this file is in, e.g. Downloads):
    py open_links.py              # Phase 1 links (all suppliers)
    py open_links.py --main-only  # only the main link per part
    py open_links.py --phase 2    # Phase 2 (or 3, 1,2 or all)
    py open_links.py --list       # just print the links

If docs/bom.csv from the project is next to this file (or in ../docs), it is read instead,
so the links stay current. Works on Windows, macOS and Linux; falls back to the default browser.
"""
import argparse, csv, json, os, re, shutil, subprocess, sys, time, webbrowser
from pathlib import Path

EMBEDDED = json.loads(r"""[
{
"id": "F01",
"phase": "1",
"item": "Epoxy for main frame mix",
"main": "https://ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow",
"links": [
"https://ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow"
]
},
{
"id": "F02",
"phase": "1",
"item": "Epoxy for leveling pour / grout / samples",
"main": "https://www.easycomposites.co.uk/glasscast-50-plus-clear-epoxy-casting-resin",
"links": [
"https://www.easycomposites.co.uk/glasscast-50-plus-clear-epoxy-casting-resin"
]
},
{
"id": "F03",
"phase": "1",
"item": "Coarse aggregate: quartz 2-5 mm",
"main": "https://www.gclproducts.co.uk/p/resin-bound-gravel/winter-quartz-2-5mm-gravel",
"links": [
"https://www.gclproducts.co.uk/p/resin-bound-gravel/winter-quartz-2-5mm-gravel"
]
},
{
"id": "F04",
"phase": "1",
"item": "Medium + fine: kiln-dried sand 0-1 mm",
"main": "https://hancockandbrown.com/kiln-dried-block-paving-sand-20kg-bag",
"links": [
"https://hancockandbrown.com/kiln-dried-block-paving-sand-20kg-bag"
]
},
{
"id": "F06",
"phase": "1",
"item": "Filler: whiting (calcium carbonate powder)",
"main": "https://valentineclays.co.uk/products/whiting",
"links": [
"https://valentineclays.co.uk/products/whiting"
]
},
{
"id": "F07",
"phase": "1",
"item": "Steel flat bar 40 x 10 mm",
"main": "https://www.themetalstore.co.uk/products/3-metre-lengths-10mm-flat-bar",
"links": [
"https://www.themetalstore.co.uk/products/3-metre-lengths-10mm-flat-bar"
]
},
{
"id": "F08",
"phase": "1",
"item": "M12 threaded rod + nuts (lifting points and joint)",
"main": "https://www.ebay.co.uk/itm/361927188666",
"links": [
"https://www.ebay.co.uk/itm/361927188666",
"https://www.screwfix.com/p/easyfix-bzp-steel-hex-nuts-m12-100-pack/15569"
]
},
{
"id": "F09",
"phase": "1",
"item": "Steel or PVC tube for M12 bolt sleeves",
"main": "https://www.screwfix.com/p/deta-tte-round-upvc-white-conduit-20mm-x-3m/256vt",
"links": [
"https://www.screwfix.com/p/deta-tte-round-upvc-white-conduit-20mm-x-3m/256vt",
"https://www.screwfix.com/p/deta-tte-round-steel-galvanised-class-4-conduit-tube-20mm-x-3m/7734j"
]
},
{
"id": "F11",
"phase": "1",
"item": "CLS timber 38 x 63 x 2400 (mould bracing)",
"main": "https://www.diy.com/departments/essentials-smooth-planed-c16-whitewood-spruce-cls-timber-l-2-4m-w-63mm-t-38mm/1798294_BQ.prd",
"links": [
"https://www.diy.com/departments/essentials-smooth-planed-c16-whitewood-spruce-cls-timber-l-2-4m-w-63mm-t-38mm/1798294_BQ.prd"
]
},
{
"id": "F12",
"phase": "1",
"item": "Release agent: PVA + wax",
"main": "https://www.ebay.co.uk/itm/235827548462",
"links": [
"https://www.ebay.co.uk/itm/235827548462",
"https://www.aliexpress.com/item/1005006037723287.html"
]
},
{
"id": "F13",
"phase": "1",
"item": "Plasticine for corner fillets",
"main": "https://www.ebay.co.uk/itm/357951022386",
"links": [
"https://www.ebay.co.uk/itm/357951022386"
]
},
{
"id": "F17",
"phase": "1",
"item": "Mixer",
"main": "https://www.screwfix.com/p/erbauer-epm1600-1600w-electric-paddle-mixer-220-240v/981kj",
"links": [
"https://www.screwfix.com/p/erbauer-epm1600-1600w-electric-paddle-mixer-220-240v/981kj"
]
},
{
"id": "F18",
"phase": "1",
"item": "Packing tape + silicone",
"main": "https://www.ebay.co.uk/itm/165130410287",
"links": [
"https://www.ebay.co.uk/itm/165130410287",
"https://www.ebay.co.uk/itm/257643689613"
]
},
{
"id": "M01",
"phase": "1",
"item": "HGR20 rail 650 mm",
"main": "https://www.aliexpress.com/item/1005010242098397.html",
"links": [
"https://www.aliexpress.com/item/1005010242098397.html"
]
},
{
"id": "M02",
"phase": "1",
"item": "HGR20 rail 450 mm",
"main": "https://www.aliexpress.com/item/1005010242098397.html",
"links": [
"https://www.aliexpress.com/item/1005010242098397.html"
]
},
{
"id": "M03",
"phase": "1",
"item": "HGR20 rail 300 mm",
"main": "https://www.aliexpress.com/item/1005010242098397.html",
"links": [
"https://www.aliexpress.com/item/1005010242098397.html"
]
},
{
"id": "M04",
"phase": "1",
"item": "HGH20CA carriage Z1 preload",
"main": "https://www.aliexpress.com/item/1005009213173130.html",
"links": [
"https://www.aliexpress.com/item/1005009213173130.html"
]
},
{
"id": "M05",
"phase": "1",
"item": "SFU1605 ballscrew + DFU1605 preloaded nut",
"main": "https://www.aliexpress.com/item/1005010046279521.html",
"links": [
"https://www.aliexpress.com/item/1005010046279521.html"
]
},
{
"id": "M06",
"phase": "1",
"item": "BK12 + BF12 end supports",
"main": "https://www.aliexpress.com/item/1005010046279521.html",
"links": [
"https://www.aliexpress.com/item/1005010046279521.html"
]
},
{
"id": "M07",
"phase": "1",
"item": "Nut housing DSG16H",
"main": "https://www.aliexpress.com/item/1005010046279521.html",
"links": [
"https://www.aliexpress.com/item/1005010046279521.html"
]
},
{
"id": "M08",
"phase": "1",
"item": "Disc or bellows coupling 10 mm to 10 mm",
"main": "https://www.aliexpress.com/item/1005009879991986.html",
"links": [
"https://www.aliexpress.com/item/1005009879991986.html"
]
},
{
"id": "M09",
"phase": "1",
"item": "NEMA 24 closed-loop stepper + driver about 4 Nm",
"main": "https://www.omc-stepperonline.com/ts-series-4-0-nm-566-56oz-in-1-axis-closed-loop-stepper-cnc-kit-nema-24-motor-driver-1-cl57t-s40-v41",
"links": [
"https://www.omc-stepperonline.com/ts-series-4-0-nm-566-56oz-in-1-axis-closed-loop-stepper-cnc-kit-nema-24-motor-driver-1-cl57t-s40-v41"
]
},
{
"id": "M10",
"phase": "1",
"item": "NEMA 24 closed-loop stepper with 24 V brake",
"main": "https://www.omc-stepperonline.com/s-series-nema-24-closed-loop-stepper-motor-3-0nm-424-92oz-in-with-2-8nm-396-51oz-in-electromagnetic-brake-24hs34-5004d-e1000-b280",
"links": [
"https://www.omc-stepperonline.com/s-series-nema-24-closed-loop-stepper-motor-3-0nm-424-92oz-in-with-2-8nm-396-51oz-in-electromagnetic-brake-24hs34-5004d-e1000-b280"
]
},
{
"id": "M14",
"phase": "1",
"item": "CL57T V4.1 closed-loop driver",
"main": "https://www.omc-stepperonline.com/closed-loop-stepper-driver-v4-1-0-8-0a-24-48vdc-for-nema-17-23-24-stepper-motor-cl57t-v41",
"links": [
"https://www.omc-stepperonline.com/closed-loop-stepper-driver-v4-1-0-8-0a-24-48vdc-for-nema-17-23-24-stepper-motor-cl57t-v41"
]
},
{
"id": "M11",
"phase": "1",
"item": "Aluminium tooling plate 330 x 330 x 30 mm",
"main": "https://www.aluminiumwarehouse.co.uk/products/25-mm-6082-aluminium-plate",
"links": [
"https://www.aluminiumwarehouse.co.uk/products/25-mm-6082-aluminium-plate"
]
},
{
"id": "M12",
"phase": "1",
"item": "Aluminium plate for X saddle and Z spindle plate",
"main": "https://www.aluminiumwarehouse.co.uk/products/20-mm-6082-aluminium-plate",
"links": [
"https://www.aluminiumwarehouse.co.uk/products/20-mm-6082-aluminium-plate"
]
},
{
"id": "M13",
"phase": "1",
"item": "Motor and bearing mounts",
"main": "https://www.aliexpress.com/item/1005006232398099.html",
"links": [
"https://www.aliexpress.com/item/1005006232398099.html"
]
},
{
"id": "S01",
"phase": "2",
"item": "Jianken JGL-80/2.2R24-20 ATC spindle",
"main": "https://www.alibaba.com/product-detail/Jianken-JGL-80-2-2KW-24000RPM_1601249825246.html",
"links": [
"https://www.alibaba.com/product-detail/Jianken-JGL-80-2-2KW-24000RPM_1601249825246.html",
"https://www.aliexpress.com/item/1005010706946690.html"
]
},
{
"id": "S08",
"phase": "1",
"item": "G-Penny 2.2 kW ER20 water-cooled spindle kit",
"main": "https://www.aliexpress.com/item/32253760001.html",
"links": [
"https://www.aliexpress.com/item/32253760001.html"
]
},
{
"id": "S09",
"phase": "1",
"item": "ER20 collet set",
"main": "https://www.aliexpress.com/item/1005010595086817.html",
"links": [
"https://www.aliexpress.com/item/1005010595086817.html"
]
},
{
"id": "S02",
"phase": "1",
"item": "VFD (included in the G-Penny kit, S08)",
"main": "https://www.aliexpress.com/item/32253760001.html",
"links": [
"https://www.aliexpress.com/item/32253760001.html"
]
},
{
"id": "S03",
"phase": "1",
"item": "80 mm spindle clamp (included in S08)",
"main": "https://www.aliexpress.com/item/32253760001.html",
"links": [
"https://www.aliexpress.com/item/32253760001.html"
]
},
{
"id": "S04",
"phase": "1",
"item": "Shielded 4-core spindle cable",
"main": "https://www.aliexpress.com/item/32971008305.html",
"links": [
"https://www.aliexpress.com/item/32971008305.html"
]
},
{
"id": "S05",
"phase": "1",
"item": "Spindle cooling loop (DIY)",
"main": "https://www.aliexpress.com/item/1005004896354890.html",
"links": [
"https://www.aliexpress.com/item/1005004896354890.html",
"https://www.aliexpress.com/item/1005007038307491.html",
"https://www.aliexpress.com/item/1005007587285872.html",
"https://www.ebay.co.uk/itm/204638752140"
]
},
{
"id": "S06",
"phase": "2",
"item": "ISO20 ER16 holders with pull studs",
"main": "https://www.aliexpress.com/item/4000141590118.html",
"links": [
"https://www.aliexpress.com/item/4000141590118.html"
]
},
{
"id": "S07",
"phase": "2",
"item": "ER16 collet set",
"main": "https://www.aliexpress.com/item/1005005626185405.html",
"links": [
"https://www.aliexpress.com/item/1005005626185405.html"
]
},
{
"id": "A03",
"phase": "3",
"item": "Small closed-loop stepper + driver (48 V)",
"main": "https://www.omc-stepperonline.com/1-axis-closed-loop-stepper-cnc-kit-80ncm-113-29oz-in-nema-17-motor-driver-1-cl42t-s08-v41",
"links": [
"https://www.omc-stepperonline.com/1-axis-closed-loop-stepper-cnc-kit-80ncm-113-29oz-in-nema-17-motor-driver-1-cl42t-s08-v41"
]
},
{
"id": "A05",
"phase": "3",
"item": "Tool length setter (wired switch)",
"main": "https://www.aliexpress.com/item/1005012101891449.html",
"links": [
"https://www.aliexpress.com/item/1005012101891449.html"
]
},
{
"id": "A06",
"phase": "3",
"item": "ATC wheel discs + bracket",
"main": "https://www.aluminiumwarehouse.co.uk/products/8-mm-6082-aluminium-plate",
"links": [
"https://www.aluminiumwarehouse.co.uk/products/8-mm-6082-aluminium-plate"
]
},
{
"id": "A07",
"phase": "3",
"item": "ATC wheel shaft + 2 bearings",
"main": "https://www.ebay.co.uk/itm/284132754238",
"links": [
"https://www.ebay.co.uk/itm/284132754238",
"https://www.ebay.co.uk/itm/383440913919"
]
},
{
"id": "A08",
"phase": "3",
"item": "ATC wheel drive reduction",
"main": "https://www.aliexpress.com/item/32650791423.html",
"links": [
"https://www.aliexpress.com/item/32650791423.html"
]
},
{
"id": "A09",
"phase": "3",
"item": "ATC wheel index sensor",
"main": "https://www.ebay.co.uk/itm/125499684863",
"links": [
"https://www.ebay.co.uk/itm/125499684863"
]
},
{
"id": "P01",
"phase": "2",
"item": "Filter / regulator / dryer",
"main": "https://www.aliexpress.com/item/1005002589702135.html",
"links": [
"https://www.aliexpress.com/item/1005002589702135.html"
]
},
{
"id": "P02",
"phase": "2",
"item": "24 V solenoid valves",
"main": "https://www.aliexpress.com/item/1005012294513653.html",
"links": [
"https://www.aliexpress.com/item/1005012294513653.html"
]
},
{
"id": "P03",
"phase": "2",
"item": "Air pressure switch",
"main": "https://www.aliexpress.com/item/1005013285557375.html",
"links": [
"https://www.aliexpress.com/item/1005013285557375.html"
]
},
{
"id": "P04",
"phase": "2",
"item": "Mist coolant system with 24 V solenoid",
"main": "https://www.aliexpress.com/item/1005012241646016.html",
"links": [
"https://www.aliexpress.com/item/1005012241646016.html"
]
},
{
"id": "P05",
"phase": "2",
"item": "Push-fit tubing and fittings 6/8 mm",
"main": "https://www.aliexpress.com/item/1005006780298909.html",
"links": [
"https://www.aliexpress.com/item/1005006780298909.html"
]
},
{
"id": "P06",
"phase": "2",
"item": "Push-in fittings",
"main": "https://www.ebay.co.uk/itm/156691426151",
"links": [
"https://www.ebay.co.uk/itm/156691426151",
"https://www.ebay.co.uk/itm/110811089560"
]
},
{
"id": "E01",
"phase": "1",
"item": "Mesa 7i76EU",
"main": "https://store.mesanet.com/index.php?route=product/product&product_id=399",
"links": [
"https://store.mesanet.com/index.php?route=product/product&product_id=399"
]
},
{
"id": "E04",
"phase": "1",
"item": "48 V DC PSU, DIN rail (Mean Well NDR-480-48)",
"main": "https://www.rapidonline.com/mean-well-sdr-480-48-rail-psu-48v-10a-480w-din-rail-mount-universal-input-05-1702",
"links": [
"https://www.rapidonline.com/mean-well-sdr-480-48-rail-psu-48v-10a-480w-din-rail-mount-universal-input-05-1702"
]
},
{
"id": "E05",
"phase": "1",
"item": "24 V DC PSU, DIN rail (Mean Well HDR-150-24)",
"main": "https://www.omc-stepperonline.com/hdr-150-24-mean-well-24vdc-5-31a-127-4w-115vac-6-25a-150w-230vac-ultra-slim-step-shape-din-rail-power-supply-hdr-150-24",
"links": [
"https://www.omc-stepperonline.com/hdr-150-24-mean-well-24vdc-5-31a-127-4w-115vac-6-25a-150w-230vac-ultra-slim-step-shape-din-rail-power-supply-hdr-150-24"
]
},
{
"id": "E06",
"phase": "1",
"item": "E-stop safety relay (used Pilz PNOZ X2.1)",
"main": "https://www.ebay.co.uk/itm/407310782945",
"links": [
"https://www.ebay.co.uk/itm/407310782945",
"https://www.ebay.co.uk/itm/375423870735"
]
},
{
"id": "E07",
"phase": "1",
"item": "Contactor with 24 V coil",
"main": "https://www.aliexpress.com/item/1005005356561757.html",
"links": [
"https://www.aliexpress.com/item/1005005356561757.html"
]
},
{
"id": "E08",
"phase": "1",
"item": "E-stop mushroom buttons + reset button",
"main": "https://www.aliexpress.com/item/1005008293871583.html",
"links": [
"https://www.aliexpress.com/item/1005008293871583.html"
]
},
{
"id": "E09",
"phase": "1",
"item": "MCBs / main isolator / EMC filter for VFD",
"main": "https://www.aliexpress.com/item/1005010519550019.html",
"links": [
"https://www.aliexpress.com/item/1005010519550019.html"
]
},
{
"id": "E10",
"phase": "1",
"item": "Inductive proximity switches 24 V",
"main": "https://www.aliexpress.com/item/1005010648075147.html",
"links": [
"https://www.aliexpress.com/item/1005010648075147.html"
]
},
{
"id": "E12",
"phase": "1",
"item": "Electrical cabinet 600 x 400 x 200",
"main": "https://www.ebay.co.uk/itm/206672920149",
"links": [
"https://www.ebay.co.uk/itm/206672920149",
"https://www.ebay.co.uk/itm/327344915454"
]
},
{
"id": "E13",
"phase": "1",
"item": "DIN rail / terminals / wiring / ferrules",
"main": "https://www.aliexpress.com/item/1690060053.html",
"links": [
"https://www.aliexpress.com/item/1690060053.html"
]
},
{
"id": "E14",
"phase": "1",
"item": "Cable chain and shielded motor cables",
"main": "https://www.aliexpress.com/item/1005012723966521.html",
"links": [
"https://www.aliexpress.com/item/1005012723966521.html"
]
},
{
"id": "E15",
"phase": "2",
"item": "Enclosure door switch",
"main": "https://www.aliexpress.com/item/1005006072968001.html",
"links": [
"https://www.aliexpress.com/item/1005006072968001.html"
]
},
{
"id": "E17",
"phase": "1",
"item": "Main isolator + MCBs",
"main": "https://www.toolstation.com/altrion-dp-incomer-switch/pAH631",
"links": [
"https://www.toolstation.com/altrion-dp-incomer-switch/pAH631",
"https://www.ebay.co.uk/itm/137268981930",
"https://www.ebay.co.uk/itm/387438925848"
]
},
{
"id": "E18",
"phase": "1",
"item": "Cabinet fan + filters",
"main": "https://www.ebay.co.uk/itm/128137523659",
"links": [
"https://www.ebay.co.uk/itm/128137523659",
"https://www.ebay.co.uk/itm/257636727653"
]
},
{
"id": "E19",
"phase": "1",
"item": "DIN rail + ferrules + wire",
"main": "https://www.ebay.co.uk/itm/174026089905",
"links": [
"https://www.ebay.co.uk/itm/174026089905",
"https://www.ebay.co.uk/itm/860051234272",
"https://www.ebay.co.uk/itm/115469225740",
"https://www.ebay.co.uk/itm/257223178155"
]
},
{
"id": "E20",
"phase": "1",
"item": "Shielded motor/encoder cable",
"main": "https://www.ebay.co.uk/itm/171352110328",
"links": [
"https://www.ebay.co.uk/itm/171352110328"
]
},
{
"id": "E21",
"phase": "1",
"item": "Reset push button",
"main": "https://www.ebay.co.uk/itm/286127619269",
"links": [
"https://www.ebay.co.uk/itm/286127619269"
]
},
{
"id": "N01",
"phase": "2",
"item": "Enclosure box: 12 mm MDF",
"main": "https://www.wickes.co.uk/General-Purpose-MDF-Sheet---12-x-1220-x-2440mm/p/110034",
"links": [
"https://www.wickes.co.uk/General-Purpose-MDF-Sheet---12-x-1220-x-2440mm/p/110034"
]
},
{
"id": "N02",
"phase": "2",
"item": "Enclosure window: 4 mm polycarbonate",
"main": "https://www.ebay.co.uk/itm/127568551200",
"links": [
"https://www.ebay.co.uk/itm/127568551200"
]
},
{
"id": "N03",
"phase": "2",
"item": "LED light",
"main": "https://www.aliexpress.com/item/1005013221981188.html",
"links": [
"https://www.aliexpress.com/item/1005013221981188.html"
]
},
{
"id": "T02",
"phase": "1",
"item": "Anti-vibration feet",
"main": "https://www.ebay.co.uk/itm/127050839358",
"links": [
"https://www.ebay.co.uk/itm/127050839358",
"https://www.ebay.co.uk/itm/127050976202"
]
},
{
"id": "X01",
"phase": "1",
"item": "Dial test indicator + magnetic base",
"main": "https://www.aliexpress.com/item/1005013036061506.html",
"links": [
"https://www.aliexpress.com/item/1005013036061506.html"
]
},
{
"id": "X02",
"phase": "1",
"item": "Precision level 0.05 mm/m",
"main": "https://www.rdgtools.co.uk/product/dasqua-200mm-machine-bar-level-high-sensitivity-0-05mm-graduations-8301-0010/",
"links": [
"https://www.rdgtools.co.uk/product/dasqua-200mm-machine-bar-level-high-sensitivity-0-05mm-graduations-8301-0010/"
]
},
{
"id": "X03",
"phase": "1",
"item": "Socket cap screw assortment M5-M12",
"main": "https://www.ebay.co.uk/itm/336213901049",
"links": [
"https://www.ebay.co.uk/itm/336213901049"
]
},
{
"id": "X04",
"phase": "1",
"item": "M5 and M12 socket caps",
"main": "https://www.ebay.co.uk/itm/164030323707",
"links": [
"https://www.ebay.co.uk/itm/164030323707",
"https://www.ebay.co.uk/itm/361974204301"
]
}
]""")
URL = re.compile(r"https?://[^\s,;)]+")

def from_csv():
    here = Path(__file__).resolve().parent
    for p in (here / "bom.csv", here / "docs" / "bom.csv", here.parent / "docs" / "bom.csv"):
        if p.exists():
            out = []
            with open(p, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    main = [r["link"]] if r.get("link") else []
                    seen = []
                    for u in main + URL.findall(r.get("notes", "")) + URL.findall(r.get("price_listed", "")):
                        u = u.rstrip(".")
                        if u and "google.com/search" not in u and u not in seen:
                            seen.append(u)
                    if seen:
                        out.append(dict(id=r["id"], phase=r.get("stage"), item=r["item"], main=seen[0] if main else None, links=seen))
            print(f"using {p}")
            return out
    return EMBEDDED

def firefox_cmd():
    found = shutil.which("firefox")
    if found:
        return found
    for c in (r"C:\Program Files\Mozilla Firefox\firefox.exe",
              r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
              os.path.expandvars(r"%LOCALAPPDATA%\Mozilla Firefox\firefox.exe"),
              "/Applications/Firefox.app/Contents/MacOS/firefox"):
        if os.path.exists(c):
            return c
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="1")
    ap.add_argument("--main-only", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--batch", type=int, default=10)
    a = ap.parse_args()
    phases = {"1", "2", "3"} if a.phase == "all" else set(a.phase.split(","))
    links = []
    for p in from_csv():
        if p["phase"] not in phases:
            continue
        for u in ([p["main"]] if a.main_only and p["main"] else ([] if a.main_only else p["links"])):
            if u not in [l for _, l in links]:
                links.append((p["id"], u))
    print(f"{len(links)} links for phase {a.phase}")
    if a.list:
        for pid, u in links:
            print(f"{pid:4s} {u}")
        return 0
    ff = firefox_cmd()
    if not ff:
        print("Firefox not found: using the default browser")
    for i in range(0, len(links), a.batch):
        chunk = [u for _, u in links[i:i + a.batch]]
        if ff:
            args = [ff]
            for u in chunk:
                args += ["--new-tab", u]
            subprocess.Popen(args)
        else:
            for u in chunk:
                webbrowser.open_new_tab(u)
        print(f"opened {i + len(chunk)}/{len(links)}")
        time.sleep(2)
    return 0

if __name__ == "__main__":
    sys.exit(main())

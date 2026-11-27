# Price check task 19: Type_0_v6 sliding ATC pneumatics & slide hardware (27 Nov 2026)

**Project:** Type 0 CNC (`Type_0_v6` + `v6_Base`). Buyer in **Swansea, SA2**. No eBay. Only prices seen on a live page (or given by the owner), with the date, VAT basis, pack size and delivery. Don't buy.

## A. AliExpress (owner's browser — curl blocked)
All items for the 14-tool sliding ATC rack (`170 mm` travel, `CD85N20` ISO 6432 Ø20 mm magnetic cylinder).

| # | Item | Exact spec to select | Qty | Price seen / notes |
|---|---|---|---|---|
| 1 | **Pneumatic cylinder** (ISO 6432, stainless, magnetic piston) | **`CD85N20`**, **Stroke `175 mm`** (NOT `CD85N10` and NOT non-magnetic `C85N`) | 1 | Owner screenshot 27 Nov showed `CD85N10-175` at £15.59 inc VAT (AFR Brand, Black Friday); check `CD85N20-175` price + delivery |
| 2 | **Magnetic reed/Hall sensors + Ø20 mm band clamps** | `D-C73` or `CS1-U` / `D-M9B` (24 V DC, NPN or 2-wire reed for Mesa 7I76EU) + **`BM2-020` / Ø20 band clamp** | 2 | End-position feedback (`rack-extended` & `rack-retracted`) |
| 3 | **G1/8 speed-control exhaust throttle fittings** | **G1/8 (1/8" BSP)** male to **6 mm** or **8 mm** push-in tube, meter-out flow control | 2 | Prevents rack slamming into front hard stops |
| 4 | **5/2-way 24 V DC solenoid valve** | **`4V210-08`** (24 V DC coil, G1/4 or G1/8 ports) + 2 × silencers + push-in fittings | 1 | Fired from Mesa 7I76EU output (`M6` remap) |
| 5 | **ISO 6432 Ø20 mounting hardware** | Rear clevis/pivot bracket (`Ø20` ISO 6432) + **`M8 × 1.25` rod-end clevis or ball joint** | 1 set | Self-aligns rod so it never binds the HGR15 rails |

## B. Linear slide hardware (LiMo or AliExpress, owner's browser)
| # | Item | Exact spec | Qty | Notes |
|---|---|---|---|---|
| 6 | **ATC linear rails + blocks** | **`HGR15` × `350 mm`** (or `400 mm` if keeping parked `Y = 525/605` with full `170 mm` stroke) + **`4 × HGH15CA`** blocks | 1 set (2 rails + 4 blocks) | Check LiMo alongside Wave 1 rail order (or AliExpress) |

## C. Flood coolant loop (optional — check B&Q / Screwfix / AliExpress when convenient)
| # | Item | Exact spec | Qty | Notes |
|---|---|---|---|---|
| 7 | **Stainless sink basket strainers** | 38–40 mm waste fitting with removable perforated basket | 3 | For the 3 × Ø36–40 mm rear cast-in drains |
| 8 | **100–200 µm nylon filter sock** | Washable aquarium / biodiesel filter sock (~Ø100 × 200 mm) | 2 | Clamped on 40 mm return manifold inside sump |
| 9 | **Coolant pump** | 40–60 W submersible (15–25 L/min, 2.5–3 m head) or 1/8 HP CNC coolant pump (240 V) | 1 | Switched by LinuxCNC `M8/M9` relay |
| 10 | **1/4" Loc-Line nozzle kit + G1/8–G1/4 ball valve** | 2 × 1/4" nozzles + bypass throttle ball valve | 1 set | Delivery + sump aeration bypass |

## How to record
Fill in live price (ex/inc VAT), delivery to SA2, date, and URL — then pass back to record in `docs/bom.csv` and run the BOM generators.

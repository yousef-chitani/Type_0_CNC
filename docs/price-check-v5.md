# V5 price check: beam and frame tubes (26 Nov 2026)

Read by `curl -sL --compressed` from the K I Metals WooCommerce Store API (`/wp-json/wc/store/products?search=box`, 4 pages) on **26 Nov 2026**. No browser was used and no price is estimated. On 24 Nov the Store API price matched the product page for K I Metals (`docs/price-check-v4.md`); the pages were not re-read today.

- Prices are **per metre, ex VAT** (VAT 20 % on top). Cut to any length from 50 mm, 2 cuts free, then £1 per cut (K I Metals, `docs/steel-rhs-suppliers.md`).
- Grade: "commonly S235JRH to BS EN 10219; selected sections may be S355J2H" (product description, 26 Nov). Cold-formed, so the corner radius is 2T to 3T for 8 mm wall: **measure the delivered tube before drilling**.
- All sizes below show "in stock" in the API.
- **Delivery to SA2: not known** (checkout only; free over £150 + VAT, heavy items excluded).
- Costs for one machine use the lengths in `tools/v5_sizes.py` (beam 830.7; frame 2 x 781.7 + 2 x 670.7 = 2904.8) and come from `tools/v5_beam.py`.

## Beam (one piece, 830.7)

| Tube (mild steel, EN 10219) | £/m ex VAT | 830.7 ex VAT | Page |
|---|---|---|---|
| SHS 120 x 120 x 8 (reference, does not fit the rails) | 67.05 | 55.70 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim144709 |
| RHS 200 x 100 x 8 | 90.30 | 75.01 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147817 |
| RHS 200 x 150 x 8 | 107.08 | 88.95 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147822 |
| RHS 250 x 150 x 8 | 123.86 | 102.89 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147827 |

Also stocked (not compared): 200 x 100 x 10 £104.77, 200 x 120 x 6 £75.38, 200 x 150 x 10 £130.79, 250 x 150 x 10 £151.83, 300 x 100 x 8 £123.86, 300 x 200 x 8 £157.42.

## Frame tubes (2904.8 in all)

| Tube | £/m ex VAT | 2904.8 ex VAT | Page |
|---|---|---|---|
| SHS 80 x 80 x 5 | 28.13 | 81.71 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim42396 |
| SHS 80 x 80 x 6 | 32.46 | 94.29 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147478 |
| SHS 80 x 80 x 8 | 40.32 | 117.12 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147490 |
| SHS 100 x 100 x 6 | 45.28 | 131.53 | https://kimetals.co.uk/materials/mild-steel/mild-steel-box-section/kim147593 |

Legs, the stand, the rack mounting and the Y roller tubes are not in these figures (plan Tasks 3, 4 and 8).

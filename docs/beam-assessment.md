# Beam assessment and internal skeleton (task 22, D-143, D-145)

**For the owner to choose. Nothing here is decided.** 17 Nov 2026. Numbers: `PYTHONUTF8=1 python cad/v2/beam_options.py` (→ `cad/v2/out/beam_options.json`). It reproduces the sketch beam (0.90 MNm², 1.5 µm), so the other rows use the same model: span 690 rail to rail, 200 N at mid-span, E 69 GPa (aluminium), EG 25 GPa (the project's pass mark).

## JLC (JLCCNC) limits (curl, jlccnc.com/cnc-machining, 17 Nov 2026)

- **Maximum part size 1100 × 600 × 500 mm.** General tolerance ±0.05 mm. Standard lead time 3 business days.
- The 890 beam, the foot blocks and 890-long bars fit. **A one-piece tub frame (890 × 630) does not** (630 is over 600). It would have to be bolted from parts.
- Materials listed: aluminium 6061 and 7075, steel 45, SUS304 (no 6082).
- The page gives no straightness or flatness figure over 890 mm.
- **No JLC price yet.** It needs a STEP upload (task 22 step 4).

## The beam options

| Option | EI, force in Y (MNm²) | Y deflection, 200 N, simply supported / ends fixed (µm) | Z deflection (µm) | Twist at the tool (µm) | Beam mass (kg) | Moving mass in Y (kg) | Material price (17 Nov 2026) |
|---|---|---|---|---|---|---|---|
| **A. Box 150 × 130 × 10** (the sketch): 4 plates, bonded and bolted | 0.90 | 1.5 / 0.4 | 1.2 | 3.7 | 12.5 | 50 | plates: **not priced** (the cut calculator can't be read by curl; page rate-limited) |
| A, bolted only, if the joints slip (lower bound) | 0.16 | 8.8 / 2.2 | 3.5 | much worse | 12.5 | 50 | as above |
| **B1. Stock tube 152.4 × 76.2 × 9.5** (6 × 3 × 3/8), faces machined | 0.24 | 5.6 / 1.4 | 1.8 | 9.7 | 9.6 | 47 | £172.65 per 1000 mm, ex VAT (Aluminium Warehouse) |
| B2. Stock tube 120 × 120 × 5 | 0.35 | 3.9 / 1.0 | 3.9 | 10.5 | 5.5 | 43 | £77.79 per 1000 mm, ex VAT (Aluminium Warehouse) |
| **B3. Two 6 × 3 × 3/8 tubes bonded and bolted side by side** (152 × 152) | 1.29 | 1.1 / 0.3 | 0.9 | 2.9 | 19.1 | 57 | £283.64 for one 2000 mm length (both pieces), ex VAT (Aluminium Warehouse) |
| **C. Box A filled with EG** (bonded) | 1.26 | 1.1 / 0.3 | 0.8 | n/a | 41.8 | **79** | plates as A + epoxy (below) |
| C2. Box A + 30 mm EG strip on the inside bottom (damping only) | 0.90 | 1.5 / 0.4 | 1.2 | 3.7 | 19.3 | 57 | plates as A + 0.8 kg epoxy |

Notes:
- **Aluminium Warehouse prices** come from the shop's catalogue feed (`/products.json`), 17 Nov 2026, mill finish. The shop shows ex-VAT prices (as recorded for M11). The product pages were rate-limited, so the VAT basis was not re-checked today. The tubes are "6000 series, such as 6082 T6" (shop text).
- **No stock tube is 150 × 130 × 10.** The nearest single tubes are 2.5 to 4 times less stiff sideways. B2's 120 face only just takes two rails at 100 pitch (D-104), with no margin. A 4 × 4 tube is too small for them.
- **A bolted box is only as stiff as its joints.** With bolts alone, the plates can slip on each other, and EI can fall towards 0.16. Bonding the joints (epoxy) plus bolts, or close-fitting dowels, keeps it near 0.90.
- **The beam is not the weak point in any option except B1 and B2** (sketch: the Z stack, the carriages and the bolted feet bend more).

## EG-filled beam (C): what it costs

- Fill: 12.7 L. With the tub mix that is **29.3 kg**, so moving mass in Y goes **50 → about 79 kg** (+58 %). Y acceleration falls by about the same ratio for the same motor torque. The Y resonance frequency falls by about 20 %.
- Epoxy: **3.2–3.5 kg** at the tub mix (11–12 %). The video's 80/20 sand mix: 25.5 kg of fill and 5.1 kg of epoxy.
- **Kit margin:** the kit is 22.68 kg. The tub takes 14.1–15.4 kg, and the rail seats, grout and bricks take about 5 kg (`bom.csv` F01). That leaves **about 2.3–3.6 kg**. A full fill uses all of it or more. A second kit was £354.00 inc VAT + delivery (D-122, 9 Nov 2026; **not re-checked**).
- The stiffness gain (0.90 → 1.26) needs the fill to stay bonded to the walls. Ampreg's neat shrinkage is 1.64 % (D-122), so expect some debonding. **Damping is the real gain.**
- **Lighter options:**
  - C2, a 30 mm EG strip: +6.8 kg, 0.8 kg of epoxy, damping only.
  - A damping sheet bonded inside (constrained layer): lightest, but not priced.

## Internal skeleton in the tub (D-145)

The idea: machined reference bars for the rail and screw seats, joined by a frame and cast in, instead of the levelling pour (D-115).

**Rules it changes:** "Castings: keep them simple, no cast-in features" (task rules), and "no welding" (D-118), so the frame would be bolted.

**Thermal expansion** (per °C):

| Material | Expansion |
|---|---|
| Aluminium | 23 × 10⁻⁶ |
| Steel | 12 × 10⁻⁶ |
| Industrial mineral casting | 12–14 × 10⁻⁶ ("as for steel"): Schneeberger techcon flyer, `schneeberger.com/fileadmin/documents/downloadcenter/01_product_catalogues_company_brochures/05_Mineral_casting/2023_Flyer_techcon_A4_en.pdf` |
| Standard grade | 16 × 10⁻⁶: Schneeberger sheet 542 400 056, `schneeberger.com/fileadmin/images/products/mineral-casting/downloads/542_400_056_EN_.pdf` |

- So aluminium expands about **1.4–1.9 times** as much as EG, not twice. Steel matches.
- Our 11–12 % hand mix has more resin than an industrial mix, so it probably expands more. **It is unmeasured.** A test brick measured at two temperatures would tell.

**Bow of a cast-in bar** (estimate):
- Model: a bar 110 × 20 on top of a 140 × 185 EG wall, perfect bond, plane sections. EG at 14 × 10⁻⁶.
- The shrinkage row uses the industrial sheet's 0.3 mm/m (sheet 056). Ours is unknown and probably higher.

| Cause | Al bar 600 | Al bar 890 | Steel bar 600 | Steel bar 890 |
|---|---|---|---|---|
| Room swing 10 °C | 16 µm | 36 µm | 5 µm | 12 µm |
| Post-cure at 50 °C, back to 20 °C (if locked in hot) | 49 µm | 107 µm | 16 µm | 35 µm |
| EG cure shrinkage 0.3 mm/m | 54 µm | 119 µm | 80 µm | 175 µm |

- Shrinkage bows the steel bar more, because it is stiffer and resists the EG more. D-115 already expects cast-in bars to bow 0.1–0.3 mm.
- **So the accuracy does not come from the machining alone.** The cast-in bars come out bowed by tens of µm to 0.1–0.2 mm, and still need shims, scraping or a levelling pour on top. Industry does the same: the Schneeberger flyer says cast-in steel strips are **milled after casting**. We can't do that over 890 mm.
- **Do long aluminium bars bow?** Yes, in two ways:
  - **In the casting:** see the table.
  - **When machined:** a long bar cut from rolled plate can bow when its stresses are released, especially if one side is machined more than the other. Cast tooling plate, or equal cuts on both sides, reduce this. JLC states only ±0.05 mm general tolerance.

**Tamping** (ASSUMED: the tub is cast the right way up, wall tops open; nothing settles this yet):
- A bar 110 wide on a 140-wide wall top leaves 15 mm each side. The EG under the bar can't be tamped from above, and air would be trapped under it.
- Cast upside down (bars face-down on the mould floor), the walls tamp from the floor side as now, and the bars sit on a flat mould face. But the mould changes and the floor's underside comes out rough.
- The frame ties must cross the floor (there is no back wall). Flat ties block tamping under them. Round bar or threaded rod with gaps of 15 mm or more (3 × the 5 mm stone) is better.

**What JLC would machine:** the two 890 reference bars (6061 or steel 45), the ties, and the foot blocks. Not a one-piece frame (630 > 600). No price until a STEP quote.

## Questions for the owner

1. **Beam:**
   - A, plate box bonded and bolted (0.90, 12.5 kg, plates not priced, JLC machining)?
   - B3, two 6 × 3 × 3/8 tubes bonded and bolted (1.29, 19.1 kg, £283.64 ex VAT material, faces machined)?
   - C, fully EG-filled (1.26, 41.8 kg, moving mass 79 kg, needs a second kit)?
   - Or another?
   - Single tubes B1 and B2 are 2.5 to 4 times less stiff. I'd not use them.
2. **Damping:** add the 30 mm EG strip inside the beam (C2: +6.8 kg, 0.8 kg epoxy)? Yes or no.
3. **Skeleton in the tub:** yes or no? It is a cast-in feature (against the "keep castings simple" rule), the bars still bow, and it still needs a levelling step. The other way is to keep D-115 as it is: cast-in steel seats, then the levelling pour.
4. **Only if 3 is yes:** cast the tub upside down (bars on the mould floor)? Steel or aluminium bars?
5. **Test brick:** measure the hand mix's expansion (a brick measured at two temperatures)? Yes or no.

My pick, if asked: **B3 with the C2 strip, and no skeleton in the tub.**
- **B3:** stiffest per kg here, a live material price, and it fits JLC's 1100 limit for machining the faces.
- **C2:** gives some damping at +7 kg.
- **No skeleton:** it moves the levelling problem rather than removing it, and adds a cast-in feature.

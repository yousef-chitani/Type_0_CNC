# V4 EG fill: volume and price per litre, against Sikadur-42+ and Parex 100 (25 Nov 2026)

The owner asked: how much EG does V4 need, what does it cost per litre, and how does it compare with Sikadur-42+ and Parex 100. Comparison only: `bom.csv` is not changed and nothing is decided.

## 1. Volume

From the model (`docs/v4-model.md`; D-308, D-310). No other EG fill is in the model or the BOM.

| Fill | Size | Volume |
|---|---|---|
| Base pocket Y- | 155 x 90 x 500 | 6.98 L |
| Base pocket Y+ | 155 x 90 x 500 | 6.98 L |
| Beam core (SHS 120 x 120 x 8, cut round the bolt heads) | | 9.57 L |
| **Machine total** | | **23.5 L** (about 54 kg of EG at 2.29 kg/L) |
| 4 mix test bricks (EG only, `eg-mix-test-plan.md`) | 9.2 kg | about 4.0 L |
| Machine + 10 % waste | | 25.9 L |

## 2. EG price per litre

Mix: blend P1 at 11 % epoxy by mass, void-free density 2.29 kg/L (`eg-mix-test-plan.md`). Per litre that is 0.252 kg binder, 1.02 kg quartz, 0.82 kg sand and 0.20 kg whiting. **The 11 % is provisional**: D-315 asks for a lean mix with as little epoxy as will bind it, and the bricks set the real figure. Less epoxy makes EG cheaper still.

BOM prices, inc VAT: Ampreg kit F01 £354.00 / 22.68 kg; 4.66 kg pack £104.20 (`price-check-v4.md`); quartz F03 £14.52 / 25 kg; sand F04 £6.38 / 20 kg; whiting F06 £20.42 / 25 kg.

| Basis | Ampreg 22.68 kg kit | 2 x 4.66 kg packs |
|---|---|---|
| **Used:** material in 1 L of EG | **£4.95 / L** (binder £3.93, stone and filler £1.02) | £6.65 / L (binder £5.63) |
| **Bought:** the V4 packs (binder + 2 quartz + 2 sand + 1 whiting) | £416.22 | £270.61 |
| Bought, per litre of machine fill (23.5 L) | £17.70 / L | £11.51 / L |

The packs also cover the test bricks. The 22.68 kg kit is about 3 times what V4 needs (about 7 kg binder), so the "bought" figure is high. Delivery is not known for any of these.

## 3. The two grouts

Both are Sika products sold by Rawlins Paints (pages read by curl, 25 Nov 2026). **Parex 100 Newton Grout is a cement grout mixed with water, not an epoxy.** "Parex 100" is taken to mean this product.

| | EG (Ampreg 30 + quartz) | Sikadur-42+ HE Cold Climate | Parex 100 Newton Grout |
|---|---|---|---|
| Type | Epoxy + stone, hand-tamped | 3-part epoxy grout, pre-batched, flowable | Cement grout, 4.5 L water per 25 kg bag |
| Pack | see section 2 | 20.4 kg kit = about 8.85 L | 25 kg bag = about 12.5 L |
| Pack price (inc VAT) | see section 2 | **£326.95** (£272.46 ex) | **£46.96** (£39.13 ex) |
| **Price per litre of product** | £4.95 used / £11.51 to £17.70 bought | **£36.94** | **£3.76** |
| Packs for 23.5 L | already in the BOM | 3 kits (26.6 L, 13 % spare) | 2 bags (25 L, 6 % spare); 3 bags for 10 % waste |
| **Cost for V4** | £270.61 to £416.22 (in the BOM now) | **£980.85** | **£93.92** (2 bags) / £140.88 (3) |
| Layer thickness | any | 10 to 150 mm | 10 to 250 mm |
| Fits the 90 deep pockets and the 104 beam bore | yes | yes | yes |
| Placing | tamped in layers; hard through beam ports (F04 note) | flows (flow channel 270 mm) | flows; grout head 150 to 200 mm; no poker vibrators |
| Pot life | about 4 h at 25 °C | about 60 min at 23 °C, 100 min at 5 °C | up to 60 min kept moving; set about 80 min at 20 °C |
| Cure temperature | 18 °C minimum | +5 to +30 °C | +5 to +35 °C; water cure 48 h recommended |
| Density | 2.29 kg/L | 2.3 kg/L | 2.25 kg/L |
| Stiffness (E, compression) | not measured | about 21 GPa | about 31.8 GPa |
| Expansion | not measured | 2.0 to 2.4 x 10⁻⁵ /K (steel about 1.2) | not stated |
| Shrinkage | not measured | -0.018 % | "shrinkage-compensated" |
| Damping | the reason for the beam fill (D-310) | not stated | not stated |

## 4. What it means

- **Parex 100 is the cheapest**: £93.92 to £140.88 for V4 against £270.61 to £416.22 for EG, and it flows into the beam through ports. **Open points (not checked):** fresh cement is alkaline and the base pockets sit against aluminium profiles. Sika says it is safe with steel; aluminium is not mentioned. The beam is steel. Its damping is not stated, and damping is why the beam is filled (D-310). Water curing in closed pockets is not covered either.
- **Sikadur-42+ costs about 7 times more per litre than EG as used.** By the task rule it is dearer by far more than 10 % and £5: £980.85 against £270.61 to £416.22. It flows and cures from +5 °C, but its expansion is about twice steel's.
- **EG stays the cheapest epoxy option.** Buying 2 x 4.66 kg Ampreg instead of the kit (D-315, still open) saves £145.61.
- Delivery: Rawlins shows "shipping from £7.95"; the real figure comes at checkout. Not included above.

## 5. Question for the owner

Keep EG (and which Ampreg pack), or switch the fill to Parex 100 (after checking aluminium contact and damping) or Sikadur-42+?

## Sources (curl, 25 Nov 2026)
- Sikadur-42+ HE Cold Climate, Rawlins: https://rawlinspaints.com/products/11136-sika-sikadur-42-he-cold-climate.html
- Sikadur-42+ HE Cold Climate, Sika GB data: https://gbr.sika.com/en/products/sikadur-42-plus-hecoldclimate.html
- Parex 100 Newton Grout, Rawlins: https://www.rawlinspaints.com/products/9542-sika-parex-100-newton-grout.html
- Parex 100 Newton Grout, Sika GB data: https://gbr.sika.com/en/construction/concrete-repair/grouts/cementitious-grouts/parex-100-newtongrout.html
- EG prices: `docs/bom.csv` F01, F03, F04, F06; `docs/price-check-v4.md` (4.66 kg pack).

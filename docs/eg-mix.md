# EG mix design and test-brick plan (task 5, D-98)

Materials (D-63, D-64, D-84): **GlassCast 50 PLUS** epoxy (F01, F02), **GCL quartz 2–5 mm** (F03, 3 bags), **Hancock & Brown kiln-dried sand 0–1 mm** (F04), **Valentine Clays whiting** (F06, d50 9 µm, ≤ 8–10% of the aggregate). The aggregate is gap-graded (nothing between 1 and 2 mm), which is accepted (aggregates.md).

Plan: **1. void test** (no epoxy) picks the aggregate blend → **2. three test bricks** at three epoxy ratios (owner choice: 3 ratios × 1 brick) → **3. cut, inspect, choose** → numbers for the castings. Weeks 12–13 (from 22 March), about 10 days including the 7-day cure.

## 1. Void test: choose the aggregate blend
Less space between the grains means less epoxy, less heat and less shrinkage. Measure it dry, before any resin is bought or wasted.

Blends to try (by weight):

| Blend | Coarse 2–5 | Sand 0–1 | Whiting |
|---|---|---|---|
| A | 45% | 47% | 8% |
| B | 55% | 37% | 8% |
| C | 60% | 32% | 8% |

Method (each blend twice):
1. Find the volume V of a rigid 2 L container: weigh it empty and full of water (1 g = 1 ml).
2. Mix 3.5 kg of the dry blend in a bucket until even.
3. Fill the container in 3 layers. Vibrate each layer on the vibration table for 30 s (or tap the container on the bench 25 times). Top up, strike off level with a straightedge.
4. Weigh the contents: m. Bulk density ρb = m / V.
5. Voids v = 1 − ρb / 2.65 (2.65 g/cm³ is the grain density of quartz and sand; whiting is 2.7, close enough).

Pick the blend with the **lowest voids**. If two are within 0.01, take the one with more coarse (less fine surface to wet). The material can be reused afterwards: it stays dry. Dry packing understates how well the whiting fills gaps once it's wet with resin, so treat the result as a **comparison between blends**, not an exact epoxy demand.

**Estimated epoxy demand** (voids filled + 10% extra to coat the grains; epoxy density about 1.1 g/cm³: CHECK the TDS):

| Voids v | 0.18 | 0.20 | 0.22 | 0.24 | 0.26 | 0.28 |
|---|---|---|---|---|---|---|
| Epoxy % by weight | 9.1 | 10.2 | 11.4 | 12.6 | 13.8 | 15.1 |

## 2. Test bricks
Three bricks, **10%, 12% and 14% epoxy** by weight of the total mix (the default the owner accepted). If the void test points well away from 12%, centre the three ratios on its estimate, 2 points apart.

| | Brick 1 | Brick 2 | Brick 3 |
|---|---|---|---|
| Epoxy | 10% | 12% | 14% |
| Release on its mould | wax only | PVA only | wax + PVA |
| Insert | — | M12 coupling nut + 70 mm rod anchor (from the F21 spares), on a jig stud through the floor | — |
| Probes | DS18B20 at the centre | DS18B20 at the centre | DS18B20 at the centre |

- **Size: 150 × 150 × 110** (110 = the base thickness). About 5.6 kg each.
- **Moulds:** MDF offcuts from the mould sheet, screwed (no glue), walls 130 tall, silicone fillets. A **4 mm hardboard strip** (44 wide) across each floor, so each brick has a rail-seat recess for a levelling-pour test.
- **Release test:** each mould uses a different release (above). This settles the wax/PVA question for the big moulds (moulds.md).
- **Heat:** stand each mould inside an insulated box (an old cool box, or 50 mm of insulation board around it). An insulated brick behaves like the middle of a big casting, so its temperature rise predicts the core of the base. One more probe logs the room. Log every minute for 72 hours (F16, DIY logger).
- **Conditions:** materials and moulds in the room for 24 h first, room ≥ 18 °C, aggregate bone dry (oven test: 200 g of sand at 110 °C for 1 h must lose less than 0.2 g).

Material for the 3 bricks: about **2.3 kg of epoxy** (with 15% waste, from F02) and about 15 kg of aggregate.

## Mixing procedure (bricks and castings)
1. **Weigh** resin and hardener into a separate pot at the TDS ratio (the BOM says 69:31 by weight: CHECK the label). Stir 2 minutes, scraping the sides and bottom.
2. Pour the mixed epoxy into the mixing bucket. **Add the whiting first** and mix to a smooth slurry (1 minute). Then the **sand** (1 minute), then the **coarse** (2 minutes), until every grain is glossy and there are no dry lumps.
3. Paddle mixer (F17) at low speed, so it doesn't whip in air. Bricks can be mixed by hand.
4. **Castings:** batches of about 15 kg in a 30 L bucket (base about 5 batches, portal about 3). One person mixes while another places and vibrates. Keep pouring without long gaps. Pot life is about 2 hours at 20 °C (CHECK), but place each batch within about 30 minutes of mixing.
5. **Place in layers** of 30–50 mm. Vibrate each layer for 20–40 s until the surface turns glossy and bubbles stop rising. Don't over-vibrate: the coarse grains sink and the resin rises.
6. Work around the insert bars, sleeves and couplers with a stick so no air stays trapped under them.

**Safety:** nitrile gloves, goggles, long sleeves (epoxy sensitises skin, and it gets worse with each exposure). **FFP3 mask when tipping or mixing dry sand, quartz and whiting**: the dust contains fine crystalline silica. Ventilate the room.

## Curing heat checks
| Centre temperature rise above the room | What it means |
|---|---|
| Under 15 °C | Fine. Cast the base as planned |
| 15–25 °C | Acceptable. Keep the room steady, leave the insulation and walls on until it cools |
| Over 25 °C, or over 50 °C in total | Too hot for the 110 mm base: lower the epoxy %, cast at the low end of 18–20 °C, or slow the hardener |

Cure **7 days at ≥ 18 °C** before cutting (bricks) or demoulding (castings: 48–72 h minimum for the walls, eg-moulds.md). In the shed in April, use the heater and insulated cover (D-90) and watch the probes.

## 3. Inspect and choose
After 7 days:
1. **Release:** which mould let go cleanly? Note it for the big moulds.
2. **Weigh and measure** each brick → density. Compare with the void-free figure: 2.32 (10%), 2.27 (12%), 2.21 g/cm³ (14%). More than 3% below it means trapped air.
3. **Tap test** all faces: listen for hollow spots.
4. **Cut each brick in half** (angle grinder or tile saw with a diamond blade, wet, FFP3). On the cut face, score:
   - voids: count holes over 1 mm; any over 2 mm is a fail;
   - wetting: no dry, chalky patches of whiting;
   - segregation: coarse grains spread evenly top to bottom;
   - resin-rich layer on the open face: thickness in mm;
   - the mould face: smooth and fully filled, including the recess edges.
5. **Anchor test (brick 2):** screw an M12 stud into the coupling nut, clamp a plate over it and torque in steps of 5 Nm to 40 Nm. Watch for cracks or movement. This sets the safe torque for the portal studs (25–30 Nm planned).
6. **Levelling-pour test:** pour F02 epoxy about 2.5 mm deep into one brick's recess. After cure, check it with a straightedge and feeler gauges (or the DTI): flat, no meniscus problem at the edges, bonded.

**Choose the lowest epoxy % that passes every check**, then add **0.5%** for the castings (bigger batches mix less perfectly). Write the result in decisions.md.

## Quantities for the castings
Castings 111.7 kg (base 72.1 + portal 39.6, D-95).

| Epoxy % | Epoxy for castings | Aggregate for castings |
|---|---|---|
| 10% | 11.2 kg | 100.5 kg |
| 12% | 13.4 kg | 98.3 kg |
| 14% | 15.6 kg | 96.1 kg |

- **Epoxy bought:** 20 kg (F01 15 + F02 5). Less the bricks (2.3), levelling pours (about 0.5) and grout (about 0.3) leaves about **16.9 kg** for the castings: enough up to about 14%, with little margin at 14%. **If the bricks choose 13.5% or more, order another 5 kg kit (F02, £91.75)** before casting.
- **Aggregate bought:** coarse 75 kg (3 bags, D-98), sand 60 kg, whiting 25 kg. Blend C at 12% needs coarse 59 + 9 (bricks) ≈ 68 kg, sand 31.5 + 4.8 ≈ 36 kg, whiting 7.9 + 1.2 ≈ 9 kg: all within stock, with a little to spare for waste.

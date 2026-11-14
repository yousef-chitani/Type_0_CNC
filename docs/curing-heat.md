# Curing, heat and the post-cure (Ampreg 30 + 3X Slow, D-122)

Rewritten 14 Nov 2026 for the new resin. Sources: Ampreg 30 datasheet numbers copied in price check 13 (`epoxy-options.md`), estimate in `tools/cure_heat.py` (its material values are ASSUMED). **The heat brick in `eg-mix-test-plan.md` must confirm the numbers here.** The earlier GlassCast version of this page is in the git history.

## What the datasheet says

| | Ampreg 30 + 3X Slow |
|---|---|
| Mix ratio by weight | 100 : 26 |
| Pot life | about 4 h at 25 °C, for 150 g kept cool in water. A full bucket is far shorter |
| Minimum cure temperature | **18 °C** |
| Before demoulding | at least **48 h at 18 °C** (16 h at 25 °C) |
| Tg after a room cure | 57 °C (28 days at 21 °C) |
| Tg after post-cure | **74 °C after 16 h at 50 °C**; 81 °C after 5 h at 70 °C |
| Post-cure ramp | about 10 °C per hour |

## The process

1. **Before the pour:** resin, hardener and all aggregate indoors for 48 h, at 18–22 °C. Mould and shed at 18 °C or more.
2. **Pour:** mix in 10–12 kg batches and get each one onto the stone and into the mould straight away. Mixed resin left in a bucket heats up and runs away.
3. **First cure, 48 h or more, never below 18 °C.** Thermostat at 20 °C. No extra heat: early heat can warp the casting. Log the centre probe, the tent air and the humidity.
4. **Post-cure in the tent, casting still in its mould:** raise the thermostat 10 °C each hour to 50 °C, hold 16 h, switch off and let it cool in the closed tent overnight.
5. **Demould only when the casting is back at room temperature.**
6. **Rail seats and grout** get the same treatment: 48 h at 18 °C or more, then 16 h at 50 °C. Wash, abrade and clean the cured surface before each of these pours.

## How hot will the castings get on their own?

Hotter than the old GlassCast plan. GlassCast released its heat over days; Ampreg releases it over hours.

| Piece | If the heat comes out over 6 h | over 12 h | over 24 h |
|---|---|---|---|
| Base (80 kg, 110 mm) | about +28 °C | +17 °C | +9 °C |
| Portal (38 kg, 130 mm) | +23 °C | +13 °C | +7 °C |
| Heat brick, sides insulated | +33 °C | +22 °C | +12 °C |
| Limit with no heat loss at all | +58 °C | | |

- **Expect the centre to peak somewhere between 30 and 50 °C** if the pour starts at 20 °C. The reaction speeds up as it warms, so the faster column is the safer guess.
- That is not harmful to the epoxy. The risks are side effects: a shorter working time for the last batches, a mould that moves as it warms, and stress locked in if one face cools much faster than the other.
- **A closed insulated tent keeps the heat in** and pushes the peak towards the +58 °C limit. For the first 24 h, open the tent lid or a side if the centre probe passes about 40 °C, and close it again as it falls back.
- Keep the PVC cores in mind: PVC softens at about 75–80 °C. The estimate stays below that, and the post-cure is held at 50 °C.
- **The heat brick settles it.** Its sides are wrapped in 50 mm insulation so it reads a little hotter than the real base. If its centre passes 60 °C, start the real pours cooler (materials at 18 °C) and leave the tent open for the first day.

## The tent and heater

- **Tent:** about 1.5 × 1.0 × 0.8 m around the mould. Use **50 mm foil-faced PIR board**, taped at the joints, not polystyrene: polystyrene softens near 80 °C and burns easily, and this tent now runs at 50 °C.
- **Heater:** holding 50 °C takes about 150–200 W; ramping the 80 kg base at 10 °C per hour takes about 300 W more. So **a 500 W heater is enough; up to 1 kW is fine.** A low-surface-temperature type (tubular or oil-filled) with its own over-heat cut-out.
- **Thermostat:** a plug-in controller with a remote probe that can be set to 50 °C. Probe at mould height, away from the heater.
- Heater low down, not touching the board, not blowing on the mould. RCD-protected socket. Smoke alarm in the shed for the 16 h hold. Run the tent empty at 50 °C once before trusting it with a casting.
- These are not on the parts list yet: PIR board, heater, thermostat controller. They go in the next small price check.

## Cold shed

April–May nights in the shed will be below 18 °C, so the tent and thermostat are needed from the moment the pour ends. Below 18 °C the cure stalls and the surface can blush (a waxy film). If the shed is below about 10 °C on the day, postpone: the mould and stone will be too cold even if the air in the tent is warm.

## What to log

Centre probe, a probe near a mould wall, tent air, shed air and humidity, every few minutes from the first batch until the casting is back at room temperature after the post-cure. Note the time of each batch.

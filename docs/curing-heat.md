# Curing heat and the cold shed (open question 9)

Sources: [GlassCast 50 PLUS technical datasheet](https://media.easycomposites.co.uk/datasheets/EC-TDS-GlassCast-50-PLUS.pdf) (read 2026-11-08), estimate in `tools/cure_heat.py`. Test bricks must confirm (task 5).

## What the datasheet says (pure resin)

| Ambient | 17 °C (min) | 20 °C (recommended) | 23 °C (max) |
|---|---|---|---|
| Pot life | 4 h | 2 h | 1 h |
| Max pour depth, thin-walled mould | 100 mm | 80 mm | 75 mm |
| Max pour depth, wood or insulating mould (our MDF) | 70 mm | 50 mm | 35 mm |
| Initial cure | 9 days | 7 days | 5 days |

- Work at **17–23 °C, aim for 20 °C**. Never above 23 °C. Avoid local heat sources (heater blowing on the mould, sun).
- Allow **at least 7 days at 20 °C before demoulding**. (`eg-moulds.md` said 48–72 h; that was for a faster resin. Corrected below.)
- Humidity under 70% RH during the cure.
- **Tg (softening point) is only 39 °C after a room-temperature cure, 47 °C after 16 h at 50 °C.** See the new question at the end.

## Is the curing heat a risk for our castings? Probably not.

The castings are about 11% epoxy by mass, so about 23% by volume; the rest is stone, which conducts heat about 7× better than resin and soaks up heat.

| Casting | Smallest thickness | Expected temperature rise vs a safe 50 mm pure-resin pour |
|---|---|---|
| Portal beam | 130 mm | about 0.2× |
| Base | 110 mm | about 0.15× |
| Rail-seat levelling pour | a few mm of pure resin | far below the limit |

- Even with no heat loss at all, the mix could only rise about 58 K (pure resin: about 300 K). With the 7-day cure, most of the heat leaks away, so expect a rise of a few degrees.
- **Conclusion:** curing heat is not the problem; **cold is**. A cold shed slows the cure (9+ days at 17 °C) and below 17 °C the resin may not cure properly.
- **Confirm with the test bricks:** cast one brick at full thickness (about 130 × 130 × 200 mm in an MDF box) with a temperature probe in the middle and one in the air beside it. Log both for the first 3 days. If the centre rises more than about 10 K above the air, use a fan over the open top (the datasheet's advice for pours over 4 kg and 40 mm).

## Keeping the mould warm (April–May in the shed)

- Build a tent of insulation around the mould on its vibration-table board: rigid foam or foil-faced insulation sheets, or old duvets over a timber frame. About 1.5 × 1.0 × 0.8 m.
- Heat loss is about 140 W at 15 K above the outside temperature with 25 mm polystyrene (7 m² × 1.3 W/m²K × 15 K). So a **150–300 W heater on a thermostat** is enough: a tubular greenhouse heater with a separate plug-in thermostat is ideal (low surface temperature, no hot spot).
- Put the heater low and away from the mould (not blowing on it). Thermostat probe at mould height. Set 20 °C.
- Log the air in the tent and the probe in the casting for the whole cure (the DIY logging is already planned, F16).
- Leave the heater on for the full 7 days before demoulding, and keep the casting above 17 °C for a further week if possible.
- Heater and thermostat are not in the BOM yet. They will be added and priced with task 6 (EG mix and test-brick plan).

## New question: low softening point (Tg 39 °C)

A room-temperature-cured GlassCast 50 PLUS casting softens at about 39 °C. A shed in summer sun, or a spindle and motor warming one spot, can get close to that, and epoxy creeps near its Tg. A **post-cure** of 16 h at 50 °C raises it to 47 °C: that could be done inside the same insulated tent with a larger heater, after the 7-day cure and before the rail-seat pour. To be decided in task 6 (it matters more for dimensional stability than for strength).

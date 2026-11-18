# Z fixed plate stiffness (18 Nov 2026)

**Result: 6082 x 20 is kept (D-202).** At 200 N on the tool, plate bending moves the tool at most 3.5 to 10.9 µm, at the very top of Z travel. With the nose low it is 2.2 µm or less. The target is ±20 µm. A steel 20 plate can replace it later with the same holes and the same spindle position.

Script: `tools/z_plate_stiffness.py`. Its plate model agrees with a hand calculation to 0.04 %, and halving the mesh size does not change the result.

## Tool movement from plate bending, µm at 200 N

Each range runs from the plate held flat on the roller faces to the plate held only at the 9 bolts. The real joint lies between the two. Rails and risers are counted as separate beams, not bonded to the plate.

| Plate | Mass kg | Nose Z 100: X | Y | Z | Nose Z 250: X | Y | Z |
|---|---|---|---|---|---|---|---|
| **6082 x 20 (chosen)** | 2.8 | 0.4 to 2.2 | 0.4 to 1.8 | 0.3 to 1.1 | 1.0 to 3.0 | **3.5 to 10.9** | 2.3 to 6.6 |
| 6082 x 25 | 3.5 | 0.3 to 1.5 | 0.3 to 1.2 | 0.2 to 0.7 | 0.7 to 1.9 | 2.4 to 7.2 | 1.7 to 4.5 |
| 6082 x 30 | 4.3 | 0.2 to 1.0 | 0.2 to 0.8 | 0.2 to 0.5 | 0.5 to 1.4 | 1.7 to 5.0 | 1.2 to 3.3 |
| Steel x 12 | 4.9 | 0.4 to 2.3 | 0.5 to 1.9 | 0.3 to 1.1 | 1.2 to 3.4 | 4.2 to 12.1 | 2.6 to 7.0 |
| Steel x 15 | 6.2 | 0.3 to 1.5 | 0.3 to 1.3 | 0.2 to 0.7 | 0.8 to 2.1 | 3.0 to 7.8 | 1.9 to 4.6 |
| Steel x 20 | 8.2 | 0.2 to 0.8 | 0.2 to 0.7 | 0.2 to 0.4 | 0.4 to 1.1 | 1.7 to 4.3 | 1.1 to 2.6 |

The top of travel is worst because the blocks then sit on the 114 of plate that overhangs above the top roller.

## Inputs

- Plate 150 x 350, Z 169 to 519, 9 bolts, from `Type_0_v3`.
- Rails at X ± 50, block pitch 90, lower block centre 115 above the nose.
- Plate front face to spindle axis 125: riser 15, block 30, moving plate 20, clamp 60.
- Tool tip 50 below the nose (assumed). 200 N is the force used in `docs/beam-assessment.md`.

## Not included

These all add to the figures above:

- **Roller flex and the top roller screws.** The rollers are treated as rigid. The top screws thread into only 3 of tube wall, and that is still not checked.
- Rail block, ball screw, moving plate, clamp and spindle flex.
- Gantry beam bending and twist (`docs/beam-assessment.md`).

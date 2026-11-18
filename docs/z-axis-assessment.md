# Z axis and drive parts: assessment (18 Nov 2026)

**Status: decided 18 Nov 2026.** Z axis option B (D-179), drive option 1 (D-180), Y motors at the back (D-181), X motor in line past the beam end (D-182, not the fold shown in the table below). Measured from the open Fusion model (120 × 120 × 8 beam), `cad/v2/assembly.py`, `docs/bom.csv` and the vendor STEP files. Nothing is drawn or rebuilt yet.

## Z axis

| | PrintNC Z in the model | Type 0 Z (`docs/bom.csv`, `assembly.py`) |
|---|---|---|
| Rails, blocks | HGR15 × 300, 4 HGH15CA | HGR20 × 350, 4 HGH20CA |
| Rail spacing, block pitch | 104, 64 | 100, 90 |
| Screw | 1204, 4 lead | DFU1605 C5 350, 5 lead |
| Motor | NEMA 23, no brake | NEMA 24 closed loop with 24 V brake (D-16, D-41, D-93) |
| Fixed plate, moving plate | 12, 12 | 20, 20 |
| Layout | Rails on the fixed plate, blocks on the moving plate | The same |
| X roller face to spindle axis | **107** | **145** (20 plate, 15 risers, 30 block, 20 plate, 60 clamp) |

### Options

| Option | For | Against |
|---|---|---|
| **A. Keep the PrintNC Z** | Already in the model. Spindle 38 closer to the beam | No brake, so the safety chain in D-93 has nothing to act on. Smaller rails and a thinner plate for steel cutting. Adds a screw, motor and rail type to the order |
| **B. Keep the Type 0 Z, with a new fixed plate that bolts to the PrintNC X rollers (recommended)** | Parts already chosen and priced. Only one new part. Keeps the brake | Spindle 38 further forward than PrintNC, or 23 if the risers can go |
| **C. Design a new Z from scratch** | Could shorten the stack | Same parts and same layout as B, so more design work for little gain |

### What option B needs

- **Fixed plate 150 wide**, not the 180 in `assembly.py`. At 180 it touches the L bracket at the end of X travel. The Z blocks need 144.
- **Holes to match the rollers:** X ± 32 from the plate centre at Z 181.5, 205.5, 372 and 396, and one at the centre at Z 181.5 (M6).
- **Settled (D-184):** 6082 in Phase 1 and steel in a later phase, the 15 risers stay, plate height 350.
- **Settled (D-191):** plate at Z 169 to 519, 9 holes 6.6 clearance with counterbores 10.5 × 6.5 deep. Modelled in `Type_0_v3` as component `Z Fixed Plate`: X -297.5 to -147.5, Y 417 to 437, held to the bottom X roller by a rigid as-built joint.
- **Z reach at this position, using the block, moving plate and clamp sizes in `assembly.py`:** the blocks stay on the rails for a spindle nose between Z 92.75 and Z 275.25. With the table top at Z 70, 150 travel and 180 under the nose, the nose runs Z 100 to 250.
- **Roller screw lengths (D-192 to D-194):** M6 × 30 for the 4 top holes (through the 8 shim), X12 in `docs/bom.csv` (D-194). They thread into only 3 of tube wall, and the extra length adds no thread. Whether that is enough is not checked. The 5 bottom holes are M6 × 20 until the owner decides: M6 × 30 is clear at the 3 holes at Z 181.5 but hits the gantry tube corner by about 2 at the 2 holes at Z 205.5, where M6 × 25 is the longest that fits.

## Ball screws and steppers

The model does not match `docs/bom.csv`:

| Item | Model | Type 0 |
|---|---|---|
| X and Y screw | SFU1610, 10 lead, single nut | DFU1605 C5, 5 lead, double nut |
| Nut length | 44 | 100 |
| Screw supports | HM12-57 (BK12 with a NEMA 23 mount) | BK12 and BF12, separate motor plates |
| Motors | NEMA 23 | NEMA 24 closed loop, about 4 Nm |
| Coupling | D30L40, 8 to 10 | D25L35, 10 to 10 |
| X motor | In line, past the beam end | Folded over the screw (D-168) |
| Y motors | **Front of the machine** | **Back of the machine (D-142)** |

**The DFU1605 fits the PrintNC rollers.** Its flange is 48 across with bolts on a 38 circle (`cad/vendor/dfu1605_nut.step`), the same circle as the model's M5 rods. The 28 body and 100 length fit inside the 150 long roller. The model already holds hidden BK12 supports and NEMA 24 plates.

### Options

| | **1. Keep our spec, change the model (recommended)** | 2. Keep NEMA 24, use 10 lead on X and Y | 3. Change to the PrintNC spec |
|---|---|---|---|
| Parts | DFU1605, NEMA 24 | DFU1610 on X and Y, DFU1605 on Z | SFU1610, NEMA 23 |
| Rapids at 1200 rpm | 6 m/min | 12 m/min on X and Y | 12 m/min |
| Thrust per motor at 4 Nm | 4,524 N | 2,262 N | Lower, as the motor is smaller |
| Encoder step (4,000 counts per rev) | 1.25 µm | 2.5 µm | Depends on the motor |
| Backlash | Preloaded | Preloaded | Single nut, not preloaded |
| Order change | None | New LiMo quote. Availability not checked | New screws and motors. Brake motor still needed on Z |

Thrust assumes 90 % screw efficiency. 1200 rpm is an assumption, in line with the 6 to 7 m/min in D-13. Critical speed does not limit either lead: about 3,180 rpm at 80 % on the 700 screw.

**Leaving the model as it is** is also possible, because the screw diameter and flange match. The nuts, motors and motor positions would then be wrong in every clash check, so it only suits a rough layout.

## Not checked

- No prices were looked up for any new part.
- Clashes over the full travel with the Type 0 Z and the longer nuts.
- Stiffness of the fixed plate.
- Length of the X and Y motors. The vendor STEP sizes include other geometry.

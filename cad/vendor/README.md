# Vendor CAD files

Manufacturer STEP files (and PDF drawings) for the bought parts, downloaded by the owner's local session (`docs/cad-download-task.md`). `cad/v2/assembly.py` uses them in place of its envelope shapes where present.

| File | Part | Source (vendor file name) | Key values (from the drawing or measured in the STEP) |
|---|---|---|---|
| `hgh20ca_block.step` | HIWIN HGH20CA carriage, on a short rail stub | TraceParts, HIWIN (`hgh20ca.stp`) | H 30, **H1 4.3**, W 44, L 77.5, B 32, C 36, M5. Rail WR 20, HR 17.5, P 60, E 20, D 9.5, h 8.5, d 6, M5 × 16 |
| `24hs34_brake_motor.pdf` | StepperOnline 24HS34-5004D-E1000-B280 (Z, brake) | StepperOnline (`24HS34-5004D-E1000-B280_Full_Datasheet.pdf`, dwg A4717) | Flange □60.3 max, holes 4 × Ø5.1 through on **50 ± 0.2**, pilot **Ø36** × 1.6 (not 38.1), shaft Ø10 × 21 (flat 15). Body 86 + brake 20 + encoder 40 = **146** behind the flange |
| `bk12.step` | BK12 fixed support | TraceParts, Engder (`BK12.STEP`) | 60 × 43, length 25 (37 with lock nut). **Centre height 25**, mounting holes Ø6.6 at **46** spacing |
| `bf12.step` | BF12 floating support | TraceParts, Engder (`BF12.STEP`) | 60 × 43 × 20. **Centre height 25**, holes Ø6.6 at **46** |
| `dfu1605_nut.step` | DFU1605 double nut, with a 130 mm screw piece | TraceParts, Engder (`dfu01605.stp`) | Nut length **100** (2 nuts + 10 spacer), body Ø28, flange Ø48 × 10, **no flats in this model** |
| `htd5m_20t_15.step` | HTD-5M 20T pulley, 15 mm belt | TraceParts, Mädler 17232000 (`17232000.stp`) | Teeth Ø30.7, flanges Ø36, 20.7 wide + hub Ø23 × 5.5 (26.2 overall). **Pilot bore in the model**, not Ø10 |
| `lj12a3_sensor.step` | M12 inductive sensor (stand-in for LJ12A3-4-Z/BY) | TraceParts, Omron E2E-X8MD12 via RS 2883243 (`2883243.step`) | M12 × 1, 57.1 long |

Not available as CAD: HGR20R rail alone (use the rail stub or the values above), DSG16H housing (52 × 40 face, 40 high, centre 20 below the face, 4 × M5 at 40 × 24, from the AliExpress drawing), D26 L35 coupling, KFL000 (PTI: no CAD; 60 long, 36 wide, bolt spacing 45), NEMA 24 mount with 50 mm holes, 24HS34 and 24HS40 STEP (StepperOnline login needed).

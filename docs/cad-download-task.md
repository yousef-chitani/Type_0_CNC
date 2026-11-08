# CAD download task: manufacturer STEP files for the full assembly (task 4, D-102)

**For:** the owner's local Claude session with a browser. The cloud session can't reach these sites (they block it or need a login). The cloud session will swap these models into `cad/v2/assembly.py` in place of its envelope shapes.

## Rules
1. **The owner logs in themselves** (HIWIN, TraceParts, Misumi, StepperOnline as needed). Ask them to log in, and wait. Never type, read or store passwords, codes or account details.
2. Download **STEP** (`.step` / `.stp`, AP214 or AP203). If only a ZIP is offered, unzip it and keep the STEP. If there's no STEP, take IGES; if no CAD at all, download the **PDF drawing** instead.
3. Take the **exact part number** listed below. If a configurator asks for options, use the ones given; if an option isn't listed, take the default and say which you chose.
4. **Don't buy, add to basket, or contact sellers.** Free CAD downloads only.
5. Save each file into **`cad/vendor/`** in the repo with the file name given below (keep the vendor's original name in the report).
6. Commit and push to the branch **`claude/trusting-shannon-uwrpm9`**: `git add cad/vendor && git commit -m "Vendor CAD files for the assembly" && git push`. Keep each file under 50 MB; if one is bigger, report it instead of committing.

## Files wanted (most important first)

| # | Save as | Part | Where to look | Notes |
|---|---|---|---|---|
| 1 | `hgr20_rail.step` | HIWIN **HGR20R** rail (any length; 500 mm if asked) | hiwin.de → Linear guideways → HG series → CAD download, or TraceParts "HIWIN HGR20" | Rail length gets set in the assembly |
| 2 | `hgh20ca_block.step` | HIWIN **HGH20CA** carriage (flange-less, standard length, Z0 preload, no special seals) | same | Also note the drawing value **H1** (rail base to carriage underside) in the report |
| 3 | `24hs34_brake_motor.step` (+ `24hs34_brake_motor.pdf`) | StepperOnline **24HS34-5004D-E1000-B280** (Z motor with brake) | omc-stepperonline.com product page → "Download" tab | We have no drawing at all for this one: the **PDF drawing matters most** (total length, brake length, hole spacing) |
| 4 | `24hs40_motor.step` | StepperOnline **24HS40-5004D-E1000** (X/Y motor) | same product site, "1-CL57T-S40-V41" kit or the motor page | The PDF drawing we already have; the STEP is the extra |
| 5 | `bk12.step`, `bf12.step` | Ball-screw support units **BK12** (fixed) and **BF12** (floating) | Misumi (search BK12 / BF12) or TraceParts (THK or HIWIN BK12) | Note **centre height h** and **mounting bolt spacing** from the drawing |
| 6 | `dfu1605_nut.step` | Ball-screw nut **DFU1605** (double nut, 16 mm, 5 mm lead) | TraceParts / Misumi / any supplier's CAD (e.g. "DFU1605 STEP") | Note the nut length and flange flat width |
| 7 | `dsg16h_housing.step` | Nut housing **DSG16H** (for 16 mm nuts) | TraceParts / supplier CAD; else a PDF drawing | Note width, length, height and centre height |
| 8 | `htd5m_20t_15.step` | Timing pulley **HTD 5M, 20 teeth, 15 mm belt, 10 mm bore** | Misumi (HTPA20S5M150 or similar) or TraceParts | Any brand with these sizes |
| 9 | `coupling_d26l35.step` | Disc (double diaphragm) coupling **D26 L35, 10 × 10 bore** | Misumi (e.g. MCOG/SCPW-type 26 mm) or TraceParts | Any brand with D26 L35 |
| 10 | `kfl000_bearing.step` | 2-bolt flange bearing **KFL000** (10 mm bore) | TraceParts / Misumi | |
| 11 | `nema24_mount.step` or PDF | A **NEMA 24 motor mount** with **50 mm hole spacing** (60 mm square, 38.1 pilot) for the Z motor | Misumi / StepperOnline accessories | If only 47.1 mm-spacing mounts exist, say so |
| 12 | `lj12a3_sensor.step` | Inductive sensor **LJ12A3-4-Z/BY** (M12 × 1, about 60 mm long) | TraceParts / GrabCAD (GrabCAD needs a login; the owner logs in) | Any M12 × 60 sensor model is fine |

Optional, if easy: the G-Penny 80 mm spindle (BST2.2C-80-24K) and its 80 mm clamp. These are unlikely to exist; skip them if not found.

## Report back (paste in the chat)

```
# | saved as | vendor + their part number / file name | format | source URL | notes (options chosen, key drawing values: H1, BK12 h and bolt spacing, nut length, housing sizes, Z motor lengths)
```
List anything not found, and why (no CAD offered, login wall, wrong part).

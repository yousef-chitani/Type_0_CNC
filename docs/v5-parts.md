# V5 parts: every PrintNC part and how V5 makes it (plan Task 3, 26 Nov 2026)

**Sources.** Part names are the Fusion components of `Type_0_v5` (a saved, unmodified copy of the parametric PrintNC V4 Metalcutter: 1182 timeline items, 94 user parameters, 327 components, read 26 Nov 2026, read-only). The STEP `PrintNC V4 Metalcutter V4.0.33 Elements to take.step` (repo root, 117 products) has the same parts; where its name differs it is given in brackets. Sizes are body bounding boxes read from the model. V5 sizes: `docs/v5-sizes.md`, D-350 to D-355.

**How made** takes only these values (D-339): **bought**, **printed** (PETG, D-100), **owner** (bought stock, owner saws, drills and taps with printed drill guides; counterbores with a counterbore bit in the drill press), **shop grind** (rail-seat fallback only, D-342), or **none** (dropped). `python tools/v5_parts_check.py` checks this column and that no row says mill, turn or laser.

**Load:** *frame* = machine weight and cutting load through the structure; *thrust* = ball screw axial load (cutting plus acceleration); *cut* = cutting load at the tool; *low* = holds itself only.

## Frame and gantry (`PrintNC Structure`)
| PrintNC part | V5 | How made | Stock | Load | Notes |
|---|---|---|---|---|---|
| `XFrame` (3 tubes 950, RHS 75 x 50 x 3) | changed: 2 X tubes 670.7 | owner | SHS 80 x 80 x 6, cut by the stockist (D-354) | frame | PrintNC has 3 X tubes; V5 buys 2 (D-354). What carries the bed and the rack between them is Task 4 (cross tubes or the bed itself) |
| `YFrame`, `YFrame(Mirror)` (RHS 75 x 50 x 3, 950) | changed: 2 Y tubes 781.7 | owner | SHS 80 x 80 x 6 (D-354) | frame | Y rail seats poured on the top face (D-342, Task 7) |
| `XGantry` (RHS 75 x 75 x 4, 975) | changed: beam 830.7 | owner | RHS 200 x 150 x 8 standing up (D-353) | frame, cut | Both X rails on the front face, 122 apart (D-355). A self-levelling pour needs a level face: the beam lies on its back for the X seat pour (Task 7) |
| `YRoller`, `YRoller(Mirror)` (RHS 75 x 50 x 3, 150) | changed: holes | owner | RHS 75 x 50 x 3 x 150 (D-283) | frame | Holes change from HGW20CC (M6 through) to HGH20CA (4 x M5 tapped in the block top, screws from inside the tube through access holes); beam bolt holes for the 150-deep beam |
| `YRollerBrace`, `YRollerBrace(Mirror)` (angle 75 x 50 x 6, 75) | kept, holes moved | owner | aluminium angle 75 x 50 x 6 (D-283) | frame | Bolts the beam's back face to the Y roller |
| `XRollers` (STEP `XRoller Top`; RHS 75 x 50 x 3, 150) | dropped | none | | | Wraps the top of the beam; the X rails move to the front face (spec, D-349) |
| `XRollerShim` (6061, 125 x 50 x 8) | dropped | none | | | Goes with `XRollers` |
| `XRoller Bottom` (6061 angle 100 x 50, 150) | dropped | none | | | Goes with `XRollers` |
| `Wasteboard` (wood 850 x 850 x 20) | dropped | none | | | Replaced by the bought T-slot bed (new parts below) |
| `Cutting Area` (630 x 630 x 90) | dropped | none | | | Model marker only. V5 work area 400 x 250 |
| `ZAxis Single HGW20CC` / `FacePlate Single Carriage` | dropped | none | | | PrintNC Z option, empty in the model |

## Motion hardware (`Hardware`)
| PrintNC part | V5 | How made | Stock | Load | Notes |
|---|---|---|---|---|---|
| `X HGR20` (x 2), `Y HGR20`, `Y2 HGR20` (800) | changed: lengths | bought | LiMo HGR20, X 650, Y 650 (`v5_sizes`) | cut | X rails on the beam front, Y rails on the poured seats |
| `X HGW20CC`, `X HGW20CC(Mirror)`, `Y HGW20CC`, `Y2 HGW20CC` (with `M6 Flush Grease Fitting`) | changed | bought | LiMo HGH20CA, preload ZA (in the rail sets) | cut | HGH20CA, as Type 0 (D-215). Grease fittings come with the blocks |
| `X/Y/Y2 1610 Ballscrew` (SFU1610, 900) | changed | bought | LiMo DFU1605 C5, X 750, Y 750 (`v5_sizes`) | thrust | D-136, D-343 |
| `X/Y/Y2 SFU1610 Nut` (with `M6-1.0 90 Grease Fitting`) | changed | bought | DFU1605 double nut (in the screw set) | thrust | |
| `X/Y/Y2 BF12` | kept | bought | LiMo BF12 (in the screw set) | thrust | |
| `X/Y/Y2 BK12` (hidden in the model) | dropped | none | | | The model already uses `HM12-57` in their place |
| `X/Y/Y2 HM12-57` (STEP: not present) | changed | bought | LiMo HM12-60-V (NEMA 24 flange, own bearing; BOM M13) | thrust | Motor mount and fixed bearing in one, as D-320 |
| `X/Y/Y2 D30L40 8-10mm Coupler` | changed | bought | LiMo D25L35 10 x 10 (BOM M08) | thrust | NEMA 24 shaft Ø10 to the screw end Ø10 |
| `X/Y/Y2 NEMA23 Stepper` | changed | bought | closed-loop NEMA 24 (Type 0 motors) | thrust | |
| `X/Y/Y2 M8 NPN-NC Inductive Sensor` (STEP `M8 Inductive Sensor`) | changed | bought | LJ12A3 M12 PNP (BOM E10) | low | |
| `X/Y/Y2 2010 Ballscrew Set` (SFU2010, BK15/BF15/HM15, hidden) | dropped | none | | | PrintNC option, not used |
| `Z 1204 Ballscrew Set`, `Z HM10-57`, `Z BK10`, `Z D25L30 8-8mm Coupler`, `Z NEMA23 Stepper`, `Z M8 NPN-NC Inductive Sensor` | dropped | none | | | PrintNC Z not used: the Type 0 Z (DFU1605, HM12-60-V, NEMA 24 with brake) |

## Printed-Milled parts (`Printed-Milled Parts`)
PrintNC prints these first and lets builders mill them later. The model's bodies are stepped and pocketed for a mill. Each row says what carries the load in V5.

| PrintNC part | V5 | How made | Stock | Load | Notes |
|---|---|---|---|---|---|
| `X/Y/Y2 1610 Nut Plate` (75 x 50 x 15, stepped, Ø28.2 bore) | **flagged** | owner (proposed) | aluminium flat bar, about 75 x 15, cut 50 | thrust | In the screw thrust path. The DFU1605 flange (6 holes PCD 38) and Ø28 body fit the plate (D-277). Proposed: a plain drilled plate (bore by hole saw or step drill, 6 tapped M5) in place of the printed one. Not the place for PETG at ±0.02 |
| `X/Y/Y2 1610 Fill Plate` (75 x 50 x 15, Ø18 hole) | **flagged** | owner (proposed) | as the nut plate | thrust | Clamped with the nut plate inside the Y roller by M5 threaded rod (`M5 Threaded Rod and Nuts`) |
| `X/Y/Y2 2010 Nut/Fill Plate` (hidden) | dropped | none | | | SFU2010 option |
| `Y BKHM12 Riser`, `X BKHM12 Riser`, `BKHM12 Riser(Mirror)` (96.5 x 60 x 30, stepped) | **flagged** | owner (proposed) | steel flat bar stack, plus shim stock | thrust | Carries the HM12-60-V. Height changes for V5 (HGH20CA, DFU1605 housing, HM12-60): set in Task 4. Proposed: plain bar to the nominal height, final height by shims so the HM12 and BF12 centres match the nut, checked with a dial gauge along the screw |
| `Y BF12 Riser`, `X BF12 Riser`, `BF12 Riser(Mirror)` (60 x 35.5 x 30) | **flagged** | owner (proposed) | as above | thrust | As the BKHM12 riser |
| `X/Y BKHM15`, `BF15` risers (hidden) | dropped | none | | | SFU2010 option |
| `Nema23 Plate`, `Nema24 Plate` and mirrors (85 x 60 x 12, hidden) | dropped | none | | | The HM12-60-V takes the NEMA 24 flange directly |
| `HM10 Toolhead Adapter`, `ZAxis Nema23 Stepper Mount`, `ZAxis Nema24 Stepper Mount` (steel, milled) | dropped | none | | | PrintNC Z |
| `XAxis Chain Travel End Support`, `XAxis Chain Fixed End Support`, `XAxis Chain Support`, `YAxis Cable Chain Travel End Support`, `YAxis Cable Chain Fixed End Support`, `YAxis Cable Chain Support`, `Cable Zip Tie Plate` (x 4) | changed: re-fitted | printed | PETG | low | Re-sized to the 80 tubes and the 200 x 150 beam in Task 4 |
| `XRoller Sensor Mount`, `YRoller Sensor Mount`, `Y2Roller Sensor Mount` | changed | printed | PETG | low | M12 sensor (E10) in place of M8 |
| `XGantry Trigger Mount`, `YFrame Trigger Mount`, `Y2Frame Trigger Mount` | changed: re-fitted | printed | PETG | low | |
| `Z Sensor Mount` (steel 39 x 14 x 8) | changed | printed | PETG | low | Type 0 Z home sensor; PrintNC's steel one goes with its Z |
| `XFrame Endcap` (x 6), `YFrame Endcap` (x 4), `XGantry Endcap` (x 2) | changed: sizes | printed | PETG | low | For SHS 80 x 80 and RHS 200 x 150. Keep the sand fill in (spec: dry sand damping) |

## PrintNC Z axes (`Zaxis Single Carriage HGW20CC`, hidden; `Zaxis Dual Carriage HGH15CA`)
| PrintNC part | V5 | How made | Stock | Load | Notes |
|---|---|---|---|---|---|
| `1Z 300mm ZPlate`, `1Z Tram Plate`, `1Z HGR20 250mm`, `1Z HGW20CC`, `1Z SFU1204 Ballscrew Nut` (+ block), `1Z ZPlate Tram Bar`, `1Z Temp Plywood Plates` (all), `1Z Fasteners` | dropped | none | | | Single-carriage Z option |
| `2Z 300mm Z Plate`, `2Z 350mm ZPlate`, `2Z Tram Plate`, `2Z HGR15`, `2Z HGH15CA`, `2Z SFU1204 Ballscrew Nut` (+ block), `2Z ZPlate Tram Bar`, `2Z Temp Plywood Plates` (all), `2Z Fasteners` | dropped | none | | | Dual-carriage Z tried and dropped (D-246) |
| `1Z/2Z 80mm 3 Hole Spindle Clamp` (steel 148 x 101 x 79) | **flagged** | bought (proposed) | | cut | D-247 put this clamp on the Type 0 Z. It is a machined part. Proposed: a bought 80 mm spindle clamp |
| `1Z/2Z Spindle Clamp Tram Blocks` (printed) | **flagged** | printed | PETG | cut | Go with the clamp of D-247; only if that clamp stays |
| `80mm 2.2kw Spindle` | changed | bought | G-Penny 2.2 kW ER20 (D-78), Jianken ISO20 later (D-39) | cut | |

## Fasteners and build aids
| PrintNC part | V5 | How made | Stock | Load | Notes |
|---|---|---|---|---|---|
| `Fasteners` (`XFrameFasteners`, `YAxisFasteners`, `YRollerFasteners`, `XGantryFasteners`, `XRoller Fasteners`, `ZAxis Fasteners`, mirrors) | changed: lengths | bought | M4, M5, M6 screws, M5 threaded rod | frame, thrust | Counts and lengths from the V5 model for the BOM (Task 8). M5 rail screws into tapped 6 mm wall: about 5 of thread, check in Task 4. M6 x 12 frame joints into the 6 wall the same |
| `Printed Drill Guides` (23 guides, `1 XFrame Drill Guide` to `11 Spindle Clamp Drill Guide`, rail centering and alignment guides, radius tools) | changed: re-made | printed | PETG | low | Re-made from the V5 model for the new tubes (80, 200 x 150) and HGH20CA. The radius tools gauge the real tube corner radius (D-353 note) |

## New in V5 (no PrintNC part)
| Part | How made | Stock | Load | Notes |
|---|---|---|---|---|
| X carriage plate (on the 4 X HGH20CA blocks, front-face rails) | owner | bought cast tooling plate, cut to size | cut | **Flagged:** one plate that is also the Z fixed plate, or a separate plate. Block screws from the front, counterbored |
| Type 0 Z: fixed and moving plates (D-179, D-184, D-202) | owner | bought cast tooling plate 6082/5083, cut to size, 20 thick | cut | **Flagged:** D-205 nut relief pocket (34 x 14 x 2) is milling; D-248 counterbores are drill-press work |
| Type 0 Z: HGR20 rails, HGH20CA, DFU1605 Z, HM12-60-V, NEMA 24 brake motor, coupling | bought | LiMo (Z 400 rail and screw, `v5_sizes`) | cut, thrust | |
| Z rail risers 15 (D-184) | owner | flat bar | cut | Height only |
| Bed | bought | aluminium T-slot bed, fly-cut on the machine (spec) | cut | Task 4 |
| Rail seats (X and Y) | owner; shop grind if the pour fails | epoxy self-levelling pour with printed dams | cut | Task 7; pass mark 0.02 |
| Tool rack (Phase 2): extrusion and forks | bought (extrusion), printed (forks) | aluminium extrusion, PETG forks | low | Task 6; mounting holes in the frame from the start |
| Chip guard over the rack and rear Y screw ends | printed or bought sheet, owner-cut | PETG or polycarbonate | low | Task 6 (review focus) |
| Legs / stand | owner | timber stand (spec) | frame | Task 4 |

## No welding: joint check (26 Nov 2026)
Read-only script on `Type_0_v5`: for every pair of structure and motion bodies whose bounding boxes touch, the fasteners whose boxes overlap both. This is a bounding-box check, not a contact check.

- **Bolted:** XFrame to both YFrames (`M6x12`), Y and X rails to tubes (`M5x20`), BKHM12 and BF12 risers to tubes and beam (`M6x30`), HM12 and BF12 to risers (`M6x50`, `HM12 M6x50`), Y rollers to blocks, braces and beam (`M6x12 (4)`), nuts to roller plates (`M5 Threaded Rod and Nuts`), X roller parts to each other and the X blocks (`M6x12 (1)`, `M6x12 (2)`, `M5x20 (1)`).
- **Touching with no fastener:** the 1610 nut and fill plates against the HGW20CC blocks (4 pairs). They sit side by side; the plates are held by the threaded rod through the roller, not by the block. Not a weld.
- **Not in the pair check:** sensor mounts, chain supports and endcaps (printed, held by `M4x16`, `M5x20`, `M6x12` screws in the fastener groups), the wasteboard (`Wasteboard M6x20`) and the PrintNC Z (dropped; `1Z/2Z Fasteners`).
- Every structural joint has a numbered printed drill guide (guides 1 to 11). **Result: no welded joint in PrintNC.** V5 joints are new in Task 4 and stay bolted.

## Flagged (for the owner)
1. Nut and fill plates (X, Y, Y2): printed PETG or drilled aluminium flat bar.
2. BKHM12 and BF12 risers: printed PETG or steel flat bar with shims.
3. X carriage plate: one plate with the Z fixed plate, or two.
4. Z nut relief pocket (D-205) is milling: what replaces it.
5. PrintNC 80 mm 3-hole spindle clamp (D-247) is machined: bought clamp instead.

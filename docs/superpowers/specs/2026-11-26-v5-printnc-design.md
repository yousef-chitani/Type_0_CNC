# Type 0 V5: PrintNC with Type 0's own parts (design, 26 Nov 2026)

**Status: draft for the owner's approval.** Decisions D-338 to D-348. Source of the choices: `docs/v5-idea-matrix.md`.

## Why
V4 needed about 30 custom pieces over 4 shop processes (mill, lathe, laser, grind), and Phase 1 was already over budget before any shop quote (`docs/feedback-discord-2026-11-26.md`). The owner's brief for V5 (D-338, D-339): **the only shop work is surface grinding; everything else is bought, 3D printed, or sawn, drilled and tapped by the owner.** PrintNC is a proven bolted-steel machine built this way, so V5 starts from it (D-341) and adds Type 0's own parts where the matrix scored them better.

## Goals
- No milled, turned or laser-cut parts. Shop surface grinding only as the fallback for the rail seats (D-342).
- Work area **400 x 250** (D-79, kept: D-344). Part accuracy ±0.02 mm.
- **16 tools in a fixed rack, 2 rows of 8, behind the bed** (D-340, D-344, D-345), for the Phase 2 ATC spindle. The frame is sized for the rack from the start.
- Phase 1 within **£4,200** (D-127), or the overrun flagged to the owner.
- Built from a fresh copy of PrintNC (D-346), so V5 is a PrintNC with known changes, not a new machine.

## Non-goals and anti-goals
- Not a bigger machine: not PrintNC's stock 625 x 625 cutting area.
- No rotary tool changer (D-340). No belt folds. No cast EG.
- No welding (owner's rule). If a PrintNC part needs welding, it is replaced by a bolted one.
- **Anti-goal:** a part that looks bought or printed but in fact needs a shop to mill, turn or laser it. Each such part is listed and replaced, or it goes back to the owner.
- **Anti-goal:** rails on as-bought tube faces (matrix: out, accuracy 1).

## Constraints
- Owner's rules: decisions in `docs/decisions.md`; prices only from live pages or the owner, dated; no eBay; `docs/bom.csv` is the source of truth.
- Fusion 360. Deliver CAD as STEP with named components. Do not save Fusion documents unless the owner asks.
- Owner-made parts: saw, drill and tap, with printed drill guides (D-329, D-339).

## Decided
| Item | Decision | D |
|---|---|---|
| Base design | PrintNC: moving gantry, fixed bed, bolted steel tube frame, steel tube beam | D-341 |
| Starting model | **Fresh from PrintNC** (the parametric PrintNC V4 Metalcutter Fusion model; the STEP `PrintNC V4 Metalcutter V4.0.33 Elements to take.step` for reference). Not `Type_0_v3`, which stays as history | D-346 |
| PrintNC changes taken | ihavenofish's: both X rails on the beam's front face (not yet checked, see the beam below); +50 Z | D-341, D-348 |
| Z height and rack height | **Table to nose 25 to 225** (+50 on D-267; Z travel 200). Rack holder tops **about 70 to 120 above the table**, tools up to about 150 below the nose. D-347 (keep 175, rack at bed level) is replaced: it could not work, see the rack check below | D-348 |
| Work area | 400 x 250 | D-344 |
| Tools | Fixed rack, **2 rows of 8 = 16 tools**, about 60 pitch (holder flanges Ø45, `docs/atc-wheel.md`). Row of 8 spans about 420, inside about 430 of X travel | D-340, D-344 |
| Rack place | **Behind the bed, under the gantry's path.** Rows run along X. Y travel grows by the rack depth | D-345 |
| Rail seats | Epoxy self-levelling pour on the frame tubes first; shop surface grinding only if the pour fails the pass mark below | D-342 |
| Screws, rails | LiMo C5 ground DFU1605, HGR20 rails. Lengths set by the V5 frame | D-136, D-343 |
| Shop work | Surface grinding only. Owner saws, drills and taps | D-339 |

## Carried over without change
Mesa 7i76EU and the LinuxCNC config (D-31, D-92); safety chain and electrics (`docs/electrical.md`); closed-loop NEMA 24 steppers; Z brake, hardwired (D-16, D-93); G-Penny 2.2 kW ER20 for Phase 1 (D-78) and Jianken ISO20 ATC for Phase 2 (D-39); PETG printed low-load parts (D-100, D-101); MQL coolant; MDF and polycarbonate enclosure; timber stand; vendor rules (D-82).

## Claude's calls (from the matrix and the repo; owner to correct)
- **Beam: steel tube, bought cut to length; section not settled.** v3's SHS 120 x 120 x 8 (D-177: 2.5 times stiffer sideways and 1.6 times in twist than 150 x 75 x 8) has only about **88 of flat front face** (72 with an R24 corner), so two HGR20 rails there are at most **about 68 apart** (v3 had 150, top and bottom), with no room between them for the 60-wide BK12 or the DFU1605 nut. Front-face rails need a **taller tube** (for example RHS about 200 tall, standing up) or a bought flat bar bolted to the front, or the rails stay top and bottom as PrintNC. The builder proposes the section, rail spacing and X screw position to the owner. Check the real corner radius before drilling.
- **Drives: inline,** motor on bought BK12 + HM12 mount and coupling, X, Y1 and Y2 (two Y screws, PrintNC's layout). No belt folds.
- **Z axis: the Type 0 Z** (HGR20, DFU1605, NEMA 24 with brake) on **bought cut-to-size cast tooling plate**, drilled and tapped by the owner from printed jigs. It bolts to PrintNC's X rollers, as v3's D-179 plate did; if the X rails move to the front face, PrintNC's `XRoller Top`/`Bottom` (which wrap the top and bottom of the beam) are replaced by one flat carriage plate on the front-face blocks. PrintNC's own Z (HGH15 / 1204 / NEMA 23) is not used.
- **Bed: bought aluminium T-slot bed**, fly-cut on the machine. Bought cut tooling plate as the alternative (matrix: 84 against 80).
- **Damping: dry sand** in the frame tubes and the beam (matrix: 87; no fill 86, so this is close and cheap to change).
- **Rack:** printed PETG forks on a bought aluminium extrusion, bolted to the frame between the Y frame tubes. Not used until Phase 2, but its space and its mounting holes are in the frame from the start.
- **Rail-seat pass mark (D-342 asks for one):** each poured seat flat to **0.02 mm over its length**, and the two Y seats level with each other to 0.02 mm over the rail span, measured with a dial gauge on a straightedge or on the blocks. **To check against HIWIN's HG20 rail mounting tolerances (parallelism and height difference for the chosen preload) before it is fixed.** Fail: the seat goes to a shop for surface grinding.
- **No welding:** PrintNC is built with bolts and printed drill guides. The builder checks every PrintNC joint in the model and lists any welded one.

## PrintNC parts and how each is made in V5
PrintNC marks some parts as "Printed-Milled". Under D-339 each must be bought, printed, or sawn, drilled and tapped by the owner. To be confirmed part by part in the model:

| PrintNC part (STEP names) | V5: how made (proposed) |
|---|---|
| Frame tubes (`XFrame`, `YFrame`), beam (`XGantry`) | Bought steel tube, cut to length by the stockist; owner drills and taps with printed drill guides |
| Y and X rollers (`YRoller`, `XRoller Top`, `XRoller Bottom`), roller braces | Bought tube or flat bar cut to length; owner drills and taps. A part that needs milled pockets or a machined face is flagged. The X rollers change if the X rails move to the front face (see the beam) |
| Nut plates, fill plates, roller plates (`1610 Nut Plate`, `Fill Plate`, `Roller Plates`) | Bought flat bar, owner drills and taps; or printed if the part takes little load. **Nut holes change to DFU1605 flanges** |
| BK12 and BF12 risers (`BKHM12 Riser`, `BF12 Riser`) | Stacked bought flat bar, drilled; height shimmed |
| Sensor and trigger mounts, cable chain supports, end caps | Printed PETG |
| Motors, couplings, BK/BF supports, rails, blocks | Bought (NEMA 24 instead of PrintNC's NEMA 23; DFU1605 instead of SFU1610; HGR20 as PrintNC) |

## Rough sizes (Claude's estimates, to be checked in the model)
- **X:** about 430 of travel (work 400 plus the 420 row). X rail and screw set from that and the block spacing.
- **Y:** Type 0's Y travel is 300 for 250 of work (requirements); plus the rack's 2 rows and clearance behind the bed, **about +150: Y travel about 450**. The Y rails, both Y screws and the Y frame tubes grow to suit.
- **Z:** travel 200, nose 25 to 225 above the table (D-348). Z rails, Z screw and the Z plate about 50 longer than v3/V4.

## Rack height check (stand-in ISO20 holders, `docs/atc-wheel.md`)
- At pickup the nose is **44 below the holder top** (v3: nose 141, holder top 185). The nose cannot go below 25, so **holder tops at least about 69 above the table.**
- To reach the back row the spindle carries a tool over the front row: holder top + 5 clear + tool length must be at most the top nose height.
- With nose 175 (D-267) that leaves holder tops at 69 to 70 and tools of 100 at most: no margin. That is why D-347 was replaced. With nose 225 (D-348): holder tops 69 to about 120 (100 tools), or tools up to about 150 with the rack at its lowest. The real Jianken nose and ISO20 holders change these by a few mm; check them before fixing the rack height.

## Left to the builder (propose to the owner before modelling)
- Set PrintNC's parameters for 400 x 250 plus the rack (Y), the 120 x 120 x 8 beam, both X rails on the front face, the 16-tool rack space, and the Z of D-348. The X rail layout on the beam is not a parameter change: it is direct modelling, proposed to the owner first. Parameters first; direct modelling only where a parameter cannot do it.
- The list of PrintNC parts by how they are made (table above), with any part that needs a shop flagged to the owner.
- The epoxy pour: where the dams go, how the seats are levelled across both Y tubes, and the check (pass mark above).
- The rack: its exact height (holder tops about 70 to 120 above the table, D-348), how the spindle enters a fork (along Y), how chips are kept off it, tool length limits.
- The new Fusion design `Type_0_v5` (fresh copy of PrintNC; Type 0 Z copied in from `Type_0_v3` or `Type_0_v4`).
- BOM: new lines for V5, old V4 lines marked dead. LiMo rail and screw lengths for the wave 1 order. Prices only from live pages.
- Update `docs/requirements.md` for V5 once the model is checked.

## Approaches considered
- **Layout** (matrix A): **stock PrintNC with ihavenofish's changes (chosen, D-341, 77)**; V4 fixed gantry (66: too many shop parts); own moving-gantry design on a bolted frame (63: not proven).
- **Starting model:** start from `Type_0_v3`, where PrintNC was already scaled for Type 0 (less work, but it brings 6 failing features and v3's tub-based sizes); **fresh from PrintNC (chosen by the owner, D-346):** cleaner, and the scaling is redone for V5's own sizes.
- **Rack place** (matrix I): **behind the bed (chosen, D-345, 76)**: the front stays clear, Y grows about 150. In front of the bed: same Y growth, in the way of loading work, more chips. Below the bed edge on a pop-up slide: no extra Y, but a bought actuator and a moving part. A side rack along Y holds only about 12 in 300 of Y.
- **Size:** **400 x 250 with 16 tools (chosen, D-344)**; 400 x 250 with 18 tools (X travel about 480, frame about 50 wider); stock PrintNC size (bigger, dearer, harder to hold ±0.02).

## Biggest risks
- **±0.02 on a PrintNC** is not shown anywhere in the repo (matrix: accuracy 3 against V4's 5). The C5 screws, screw compensation and poured seats help; the moving gantry is the weak point.
- **Poured seats** may not reach the pass mark; then grinding is needed, and it is not priced.
- **Rack pitch 60** is from the Ø45 holder flanges, not from a real printed fork.
- **+50 Z** makes the spindle overhang longer and the Z a little less stiff (the reason for D-267).
- **Both X rails on the front face** do not fit a 120 beam well (see the beam); the beam section may change.

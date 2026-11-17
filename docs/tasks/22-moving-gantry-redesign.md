# Task 22: Moving-gantry redesign (D-137, D-138)

**Start:** branch `claude/hopeful-sagan-28twty`. Read `docs/tasks/README.md`, then only the files below.

**Who:** main session (design judgement). Ask the owner before deciding anything not in D-137/D-138.
**Depends on:** none. **Blocks:** the LiMo order (D-136, on hold), tasks 09, 10, 11, 14, 18.

## What the owner wants (17 Nov 2026)
- Like the Moxer machine: a cast EG tub (floor + two side walls, maybe a back wall), table fixed inside, gantry rides on Y rails on the wall tops. Two Y screws, two Y motors.
- Tub in one piece; the owner accepts the weight (estimate 115–160 kg solid).
- Gantry in machined aluminium, possibly from JLC (JLCCNC). **Sketch first**; STEP for a quote only after the owner agrees.
- Phase 2 ATC: Timbre-style horizontal fork wheel on a post at a front corner (D-138).
- Work area stays 400 × 250, Z 150, unless the owner says otherwise.

## Read
- docs/decisions.md (D-01, D-73, D-102 … D-138)
- docs/assembly.md (current design; what carries over: Z axis, spindle, motors, rails HGR20, DFU1605)
- docs/simplification-options.md (the owner's "simple, low-risk" brief; one-shot pour risk)
- docs/bom.csv lines M01–M17, E01, E14
- docs/electrical.md TB2 table (channels)

## Do
1. **Sketch** (CadQuery or a dimensioned drawing, PNG + short md): tub sizes and mass, rail positions, gantry beam section and legs, Y screw positions (under each wall top or beside), moving mass, Z clearance, the ATC wheel's place. State EI of the beam and the deflection under a 200 N cut load at mid-span.
2. Show the owner; ask about the open choices (Y screw placement, tub back wall, cores yes/no, beam section).
3. After the owner agrees: list the new screw and rail lengths and the revised LiMo basket (2 Y screws; check the 950 mm max for DDP sea); list `bom.csv` changes (2nd Y screw, motor M09, driver, couplings/belts, portal casting lines out, gantry parts in); electrical channel change. Ask before editing `bom.csv`.
4. Then a STEP of the gantry parts for a JLC quote. First check JLC's maximum CNC part size by curl.

## Done when
The owner has agreed the sketch, the new LiMo basket list is ready before 4 Jan 2027, and `bom.csv` is updated (or the open items are listed in the handover).

## State (17 Nov 2026)
- Steps 1–2 done: sketch `docs/moving-gantry-sketch.md` (`cad/v2/gantry_sketch.py`). Owner answers D-139 … D-142: no back wall, solid, walls 100 above the table, Y screws outboard on the wall tops, Y travel 350 for the ATC, Y motors direct at the back.
- **Open: the beam (D-143).** The owner wants the next task to assess how it is made (bolted 4-plate box, stock tube, EG-filled) and JLC's maximum part size, before step 3.
- **D-145 (owner, 17 Nov): the beam assessment includes an EG-filled beam, and the video's internal skeleton is assessed for the beam and the tub** (`docs/video-notes-eg-base.md`). Points to weigh:
  - Filled beam: about 29 kg more moving mass (50 → about 79 kg in Y), about 3–5 kg more epoxy than the kit has to spare. Partial fill or a damping strip are lighter options.
  - Skeleton in the tub: machined reference bars (rail and screw seats) joined by a frame and cast in, instead of the levelling pour (D-115). Accuracy then comes from machining (JLC), not from the pour. Check: aluminium expands about twice as much as EG and steel per °C (CHECK the EG figure), so long Al bars in EG may bow with temperature; steel bars match better. Check the frame doesn't block tamping (walls 140 wide).
- Sketch lengths for step 3: Y rails 2 × 600, Y screws 2 × 600, X rails 2 × 600, X screw 700, Z 350 (all under the 950 limit). Not ordered; `bom.csv` unchanged.

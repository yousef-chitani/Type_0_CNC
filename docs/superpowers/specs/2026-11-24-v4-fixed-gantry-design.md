# Type 0 V4: fixed gantry, moving table (design, 24 Nov 2026)

## Why
Feedback on v3 from experienced builders (24 Nov 2026):
- The ATC wheel at the front ("sailing boat") is in the way of working at the machine. A rear ATC was already checked and fails (`docs/rear-atc-reach.md`, D-288): it clashes with the beam and limits tool length.
- Better: a gantry extended past the side of the frame, with the tools outside the frame.
- Build the frame from a bolted structure with pockets filled with epoxy granite (EG), instead of a cast EG tub.
- Mount the rails on surfaces that can be machined; a hollow steel beam can ring.

The owner chose a new version, V4: fixed gantry, moving table, built on what v3 taught.

## Goals
- The front of the machine is clear: the tools sit outside the frame, beside it.
- No casting: the base is bought extrusion, bolted, then filled with EG.
- No machining of the big frame: only small parts (rail plates, bolting faces) go to a shop.
- Tool length is not limited by anything under the tool changer.
- Same work and accuracy as v3 (below).

## Non-goals and anti-goals
- Not a bigger machine: the work area stays 400 x 250.
- No rails bolted straight on as-extruded aluminium faces or on hot-rolled steel faces (anti-goal: a frame that looks right but cannot hold ±0.02 mm).
- No welding (the owner bolts).
- No cast EG tub, no moulds.

## Decided by the owner (24 Nov 2026)
| Item | Decision |
|---|---|
| Layout | Fixed gantry. The table moves in Y; the spindle moves in X and Z on the gantry |
| Base | Bolted aluminium extrusion tray; its voids filled with EG for mass and damping (like the reference video, where the extrusion is the structure and the EG adds mass and damping) |
| Gantry beam | Steel, v3's SHS 120 x 120 x 8 |
| Uprights | **Steel** (SHS or thick plate), bolted to the sides of the extrusion base, beam bolted on top (option A) |
| Y rails | On top of the base, under the table |
| Tools | Gantry beam extended past one side of the frame. **v3's indexing wheel** stands outside the frame; the spindle goes out along X to one pickup point and the wheel brings the tool to it (option B; a straight rack would add about 480 mm of X, a rack on a table wing holds only 4 to 5 tools) |
| Rail seats | Epoxy-levelled seats or bolted plates ground flat by a shop. Never as-extruded or hot-rolled faces |
| Wheel side | **Right (+X)**, as v3. No tight width limit in the garage. X home and cable runs at that end (builder's call) |
| Enclosure (Phase 2) | **Goes round the wheel too** (about 300 to 400 mm wider than a v3 enclosure). The wheel needs a chip guard |

## Carried over from v3 (proposed by Claude, not objected to)
- Work area **400 x 250**, Z travel 150, table about 460 x 330 (D-79, D-233). Table to spindle nose 25 to 175 (D-267). Part accuracy ±0.02 mm.
- Spindle Jianken 2.2 kW ATC, ISO20. Closed-loop steppers. LinuxCNC on Mesa. C5 ballscrews DFU1605 and HGR20 rails from LiMo (D-136). v3's Z axis (plates, rails, spindle clamp and tram blocks, D-247) where it fits.
- The ATC wheel: v3's vertical 12-fork wheel and its carrier (D-302 to D-304), re-mounted outside the frame.
- Phase 1 budget **£4,200**. Wave 1 order on **4 Jan 2027**, with the rail and screw lengths redone for V4 before it goes.
- EG mix from v3 (Ampreg 30, about 11 % by weight, test bricks first). The reference video's 90/10 was too dry.
- Owner's rules: prices only from live pages, decisions recorded in `docs/decisions.md`, `docs/bom.csv` is the source of truth.

## Dropped from v3
- The cast EG tub, its moulds and the April to May casting window.
- The moving gantry, its roller tubes and Y braces, the second Y motor (Y2): one Y screw drives the table.
- The front ATC position.

## Rough sizes (Claude's estimates, to be checked in CAD)
- Y: table 330 long + 250 travel: base and Y rails about 600 long. Y screw about 600 (as v3's order).
- X: 430 of work travel + about 200 to reach the wheel's pickup: about 630. X rails and screw about 850 to 900, close to v3's X 850 screw. Beam about 1 m, overhanging the base on the wheel's side.
- Base width: the table width plus room for the uprights' bolting faces.

## Claude's calls (from the builder check; owner to correct)
- **Site and mass:** the machine stands in the garage on the owner's heavy stand (`docs/requirements.md`); the old 40 kg per-piece limit of D-71 (upstairs flat) does not apply, as for v3's 88 kg tub (D-137). The EG is poured into the base in the garage, where the machine stands. The base is one filled tray unless the builder finds a reason to split it.
- **Budget:** £4,200 stays the Phase 1 target. Pick the cheapest option that holds ±0.02 mm, and flag any overrun to the owner (the project's existing rule), rather than cutting accuracy.

## Left to the builder (to propose to the owner before modelling)
- Extrusion profiles and the tray layout; where the EG pockets are and how they are closed.
- Upright section (SHS or plate), its height, and the steel-to-aluminium joint (large bolted face, dowels, ground faces).
- Gantry height from the table, so the nose reaches 25 to 175 above it.
- The wheel's mount (base side or upright), its plane, and how the spindle enters the fork from X.
- Y screw and motor position under the table, and where chips go.
- Whether the beam gets a damping fill (`docs/beam-assessment.md` options).
- New Fusion model: V4 is a new design. v3 parts are copied in where they fit; `Type_0_v3` is kept as history.
- Updated BOM lines and lengths for the wave 1 order.

## Approaches considered
- **Base:** all extrusion (no welding, cut to length, weaker), **extrusion base + steel beam (chosen)**, all bolted steel tube (stiffest, faces need levelling everywhere). Chosen because the beam carries the cutting load and the overhang out to the wheel.
- **Tools:** straight rack along X (+480 mm X, long screw whips), **indexing wheel outside the frame (chosen)** (+200 mm X, reuses v3's wheel), rack on a table wing (4 to 5 tools, more moving mass, near chips).
- **Uprights:** **steel SHS or plate (chosen)**, EG-filled extrusion (less stiff), laser-cut steel side plates (weak sideways without gussets).

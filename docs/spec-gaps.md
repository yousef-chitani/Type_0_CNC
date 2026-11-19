# Where the design misses the spec (19 Nov 2026)

Checked against `docs/requirements.md`, the decisions it cites and the task 24 decisions, using `Type_0_v3` as it is now (not saved).

## Misses

| # | Spec | Design now | Gap |
|---|---|---|---|
| 1 | Fixture plate: **10 hold-down bolts** (owner, D-240) | **8 bolts**: the inner rear pair (X ±25, Y 228) was removed (D-241) | 2 bolts short |
| 2 | Front slot through the tub floor and the plate (D-230) | Not sized or modelled (task 24, item 6) | Open |
| 3 | Table to spindle nose clearance **about 180 to 200** (D-09) | Plate top Z 70, nose travel Z 95 to 245 (D-214): **25 to 175** | 5 to 25 short at the top |
| 4 | Travel **X 570** (D-79, includes the old ATC reach) | X slider 430 (reach X -222.5 to 207.5) | 140 short. The 400 work width is met. The 570 was for the old rack; the ATC is now a front-corner wheel (D-138), so 570 may no longer apply |
| 5 | Layout: **fixed gantry, moving table** (requirements) | Moving gantry, fixed table in a cast tub (D-137) | Changed by decision; `requirements.md` not updated |
| 6 | Tool changer: **rack behind the gantry, through the table opening** (D-06) | Phase 2 umbrella wheel at a front corner (D-138) | Changed by decision; `requirements.md` not updated |
| 7 | Frame: **epoxy granite** | Only the tub is EG; the gantry is steel SHS with PrintNC rollers (D-164, D-172) | Partly met |
| 8 | Frame mass **about 200 to 350 kg** | Tub 92.4 kg (D-197); the rest of the frame is not summed | Probably under 200; not checked |

## Met, with notes
- Work area 400 x 250: spindle reach X 430, Y 385 (D-233). The plate is larger than the reach: 7.5 at -X, 22.5 at +X and 1 at the back cannot be reached.
- Z travel 150: nose Z 95 to 245.
- Phase 1 budget £4,200: £4,023.69 priced, £176.31 left; G01 and G03 not priced yet.

## Not checkable from the model
- Part accuracy ±0.02 (D-10): needs the mapping run on the built machine.

## Model housekeeping
- `Type_0_v3` holds the D-240 and D-241 changes but is not saved.
- `Chamfer2` (timeline item 617, far before the plate) has 2 lost edge references and uses cached geometry.

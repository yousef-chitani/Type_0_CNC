# Discord feedback on the V4 render (25 Nov 2026)

The owner posted a V4 render (fixed gantry, moving table, ATC wheel on the right). Replies, and Claude's check of each against the V4 docs. **Nothing here is decided: the owner chooses.**

## 1. Footprint: fixed gantry against moving gantry (MaxCahill)
> "compare the footprint vs moving gantry ... more bed and still fit 12 tools with them laid out in a line ... no rotary to manage. but fixed will often be more rigid, just needs more footprint per bed area"

- V4 now: work 430 x 250 (X travel 620, of which 190 is only to reach the wheel). Envelope about **1,102 x 805 x 978** (`docs/v4-model.md`). That is about 0.88 m² of floor for about 0.11 m² of work.
- A straight rack was checked in the V4 design (`docs/superpowers/specs/2026-11-24-v4-fixed-gantry-design.md`, "Approaches"): about **+480 mm of X** on the fixed gantry, long X screw that whips. A rack on a table wing holds only 4 to 5 tools.
- On a moving gantry the rack would lie along the bed (Y), not add X: that is Max's point. But v3 (moving gantry) was left for other reasons: front wheel in the way, rear ATC failed (D-288), cast tub (D-305 to D-307).
- **Fair point, not new.** It is the main cost of V4. A side-by-side footprint (v3 + rack along Y against V4 + wheel) is not drawn yet.

## 2. Belt-fold the Z motor (MaxCahill)
> "timing-belt-tucking the z motor ... can cut the headroom needed a lot"

- V4 now: Z motor (24HS34 with brake, M10) on top of the HM12 mount and a D25L35 coupling, direct drive. It is the machine's top: **Z 700**, about 400 above the beam top (Z 300).
- A fold puts the motor beside the screw, shaft down, with a 1:1 belt: about **150 to 180 mm lower** (motor body plus coupling). Same idea as the ATC drive (D-317).
- **Catch:** the brake is on the motor. With a belt, a broken belt drops the spindle; the brake no longer holds Z. Needs a belt with margin (e.g. HTD 5M, 15 wide) or a brake on the screw.
- Also costs: 2 pulleys, a belt, a tensioning slot, a new motor plate. Not priced.
- The same fold on the **X motor** (it sticks out about 160 past the beam's left end, X -508) would shorten the machine in X by about 150.
- Headroom matters for the Phase 2 enclosure and the garage, not for cutting.

## 3. Ribs on the uprights (MaxCahill)
> "simple angle or flat bar stiffening ribs along the uprights ... free rigidity in x"

- V4 now: each upright is a **50 x 150 x 325 steel flat bar** (D-309), only **50 deep in X**. Its bending stiffness in X is about 25 times lower than in Y (I = 150·50³/12 against 50·150³/12).
- The upright-to-end-plate joint is also only **150 x 90** (`docs/v4-model.md`, Task 5 item 5); the stiffness model took it as rigid.
- A bolted steel angle (e.g. 50 x 50 x 6) or flat bar on the upright's front and rear faces, standing out in X, deepens the section in X; run it down onto the tray to enlarge the joint too. No welding needed (owner bolts).
- Clearance: the carriage passes 20.1 in front of the upright at the +X limit (Task 5 clearance), so a rib on the **front** face must stay clear of the lower X block. The wheel's holders start at X 379.5, 59.5 past the right upright's outer face: an outward rib up to about 50 fits there, to be checked in the model.

**Check run 25 Nov (owner chose to work it up).** `tools/v4_frame_stiffness.py` (tray B, D-308), with 2 steel ribs bolted on the upright's front and rear faces, standing out in X, taken as fully joined to the bar (upper bound). µm at the nose per 100 N, EG bonded / EG ignored:

| Upright | I for X bending (cm⁴) | Table X | Table Y | Table Z | Wheel X | Wheel Z |
|---|---|---|---|---|---|---|
| U2 50 x 150 (now) | 156 | 1.6 / 4.1 | 1.5 / 4.2 | 2.6 / 8.6 | 2.0 / 2.7 | 1.4 / 1.5 |
| + 2 ribs 50 x 10 | 398 | 1.5 / 4.0 | 1.5 / 4.1 | 2.5 / 8.5 | 1.8 / 2.5 | 1.2 / 1.3 |
| + 2 ribs 100 x 10 | 1,211 | 1.5 / 4.0 | 1.5 / 4.1 | 2.4 / 8.4 | 1.7 / 2.4 | 1.1 / 1.1 |

- **The upright is not the limit in this model.** Ribs make it 2.5 to 8 times stiffer in X, but the nose gains only about 0.1 to 0.3 µm per 100 N (5 to 15 %, most at the wheel). The portal (two uprights tied by the beam) already carries X; the tray and the beam's twist dominate.
- **What the model leaves out is the joint:** it takes the 150 x 90 upright-to-end-plate joint as rigid. That joint is the likely real weak point. Ribs that run down past the end plate and bolt to the tray's side (gussets) would enlarge it; that is where a rib could pay. It needs a joint model or a test, not this frame model.
- To repeat: add the ribbed section (bar plus two rib rectangles, parallel axis) to `UPRIGHTS` in the tool and run `compliance()`.

## 4. Turn the machine sideways: horizontal mill (rcw)
> "turning the whole thing sideways. Chip clearing is one of the big benefits of horizontal mills"

- Chips fall away from the cut instead of sitting in pockets.
- It is a new architecture: work holding, the table, the ATC, the EG base and the whole V4 model change. Out of scope for Phase 1 unless the owner wants a V5.
- **Noted only.** For deep features, the V4 answer is air blast or flood coolant (Phase 2).

## Owner's answers (25 Nov 2026, D-321)
- Work up all four: **upright ribs, belt-fold Z motor, belt-fold X motor, footprint comparison.** Task 28.
- Horizontal layout: **note for later**, no change to V4.
- Upright ribs: checked above (small gain in the frame model; the joint is the open question).

## Still to ask the owner
- Z fold: belt with margin, or a brake on the screw?
- Ribs: drop them, or turn them into gussets down to the tray (needs a joint check)?

# Discord feedback on the V4 render (25 Nov 2026)

The owner posted a V4 render (fixed gantry, moving table, ATC wheel on the right). Replies, and Claude's check of each against the V4 docs. **Nothing here is decided: the owner chooses.**

## 1. Footprint: fixed gantry against moving gantry (MaxCahill)
> "compare the footprint vs moving gantry ... more bed and still fit 12 tools with them laid out in a line ... no rotary to manage. but fixed will often be more rigid, just needs more footprint per bed area"

- V4 now: work 430 x 250 (X travel 620, of which 190 is only to reach the wheel). Envelope about **1,058 x 805 x 978** (`docs/v4-model.md`, after D-317). That is about 0.85 m² of floor for about 0.11 m² of work.
- A straight rack was checked in the V4 design (`docs/superpowers/specs/2026-11-24-v4-fixed-gantry-design.md`, "Approaches"): about **+480 mm of X** on the fixed gantry, long X screw that whips. A rack on a table wing holds only 4 to 5 tools.
- On a moving gantry the rack would lie along the bed (Y), not add X: that is Max's point. But v3 (moving gantry) was left for other reasons: front wheel in the way, rear ATC failed (D-288), cast tub (D-305 to D-307).
- **Fair point, not new.** It is the main cost of V4. Side-by-side footprint drawn 25 Nov: `docs/task28-folds-and-footprint.md`.

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

### Joint check (25 Nov, owner: "Gussets, check joint")
`tools/v4_joint_sweep.py` puts a rotation spring (about global Y, the X-sway direction) at each upright's **foot** (upright to end plate to tray) and **top** (beam on the upright's top edge). Tray B, U2 upright. µm at the nose per 100 N, EG bonded / ignored:

| Joints (N·mm/rad) | Table X | Table Z | Wheel X | Wheel Z |
|---|---|---|---|---|
| both rigid (what the frame tool assumes) | 1.6 / 4.1 | 2.6 / 8.6 | 2.0 / 2.7 | 1.4 / 1.5 |
| top 1e10, foot rigid | 1.7 / 4.2 | 2.6 / 8.6 | 2.1 / 2.8 | 1.5 / 1.5 |
| top 1e9, foot rigid | 1.9 / 4.5 | 2.7 / 8.7 | 2.5 / 3.2 | 1.5 / 1.6 |
| top 1e10, foot 1e10 | 1.8 / 4.3 | 2.6 / 8.7 | 2.2 / 2.9 | 1.5 / 1.5 |
| top 3e9, foot 3e9 | 2.1 / 4.6 | 2.7 / 8.7 | 2.6 / 3.3 | 1.5 / 1.6 |
| **top 1e9, foot 1e9 (likely as drawn)** | **3.0 / 5.5** | 2.7 / 8.7 | **3.7 / 4.4** | 1.5 / 1.6 |

Y and Z hardly change; **X does.** With both joints soft the frame is a portal whose corners bend, and X at the nose gets about **twice as soft** as the frame tool says.

Hand estimate of the joints as drawn (contact face taken as a short block, E·I/grip, then 3 to 10 times softer for real contact; good to a factor of about 3):
- **Top joint:** the beam sits on the upright's 50 x 150 top edge; the 2 M12 beam bolts are on the edge's centreline (X ±295), so they add nothing against rocking in X. Lever in X: only 50. About **1e9 to 3e9**.
- **Foot joint:** upright on the end plate (150 x 90 face, 4 x M12, stiff), but the end plate then bears on the aluminium profile ends, and its 8 x M16 bolts are all on one row at mid-height (Z -120). About **1e9**, set by the aluminium.
- So the "likely" row above is the honest one: about **3 µm per 100 N in X at the table, 3.7 at the wheel**, not 1.6 and 2.0.

**What gussets could do:**
- **Foot: a rear fish plate.** The upright's rear face and the tray's rear profile face are both at Y 335 (the upright is flush with the tray's rear end). One flat steel plate (say 10 x 150 x 300) bolted to both: tapped M8 in the upright's rear face, T-nuts in the rear profile's slots spread along X. No bending in the plate; it takes the moment in its own plane. Rough estimate: doubles to triples the foot joint.
- **Top: harder.** The beam's rear face (Y 300) is 35 short of the upright's rear face; the front is taken by the X rail plate and the carriage. Options: a corner brace under the beam on the inside (only the 40 gap between the table edge X 230 and the upright X 270, beside the moving table), on the outside (fine on the right, where the beam overhangs 220; only 30 of overhang on the left), or a 35 spacer bar on the beam's rear face plus a fish plate as at the foot.
- Getting both joints to about 1e10 brings X back to about 1.8 / 2.2 (table / wheel).
- These need a look in the model (room beside the table, ATC on the right) before choosing. Not modelled; not priced.

### Rear shear plates (D-323, modelled 25 Nov)
Owner chose "One plate, foot + top". The upright's rear face and the tray's rear profile face are both at Y 335; the beam's rear face is at Y 310. So each side gets one 10 mm steel plate (X ±120 to ±320, Z -165 to 280) bolted to the profile (6 x M8 T-nuts), the upright (4 x M10 tapped) and an 80 x 25 spacer on the beam's rear wall (4 x M10). It works as a shear wall across both joints. Modelled in `Type_0_v4`, clash check clean, saved; details in `docs/v4-model.md` (Task 28). Steel £59.76 (G13, G14), screws £20.94 (G15, priced 25 Nov). Phase 1 £4,559.80.

Stiffness, rough: the joints now depend on bolt groups in friction, not on the 50-wide edge. A guess of 3e9 to 1e10 N·mm/rad each gives X at the table about 2.1 to 1.8 µm per 100 N (wheel 2.6 to 2.2), against about 3.0 / 3.7 without the plates. Not modelled as a plate in the frame tool; a tap test on the built frame would settle it.

## Owner's answers (25 Nov 2026, D-321)
- Work up all four: **upright ribs, belt-fold Z motor, belt-fold X motor, footprint comparison.** Task 28.
- Horizontal layout: **note for later**, no change to V4.
- Upright ribs: checked above (small gain in the frame model; the joint is the open question).

- **Gussets: check the joint** (done above). Next: owner picks the gusset options to model.
- **Z fold: belt with margin, the brake stays on the motor (D-322).**
- Z and X folds sketched and the footprint drawn (25 Nov): `docs/task28-folds-and-footprint.md`, with 3 questions for the owner.

## Still to ask the owner
- Ribs: drop them, or turn them into gussets down to the tray (needs a joint check)?

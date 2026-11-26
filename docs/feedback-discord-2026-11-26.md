# Discord feedback on V4: too many custom parts (26 Nov 2026)

The owner (Quin) and ihavenofish, after the V4 render. Claude's check of each point against the repo. **Nothing here is decided: the owner chooses.** Follow-up: the owner started V5 (D-338 to D-340, `docs/v5-idea-matrix.md`). The earlier round (MaxCahill, rcw) is `docs/feedback-discord-2026-11-25.md`.

## What was said
- **Owner:** too many custom parts; it may be very expensive (JLC prices not in yet); the university might buy a good mill for students.
- **ihavenofish:** a bit over-complicated. Use a **moving gantry**: it is more proven. Any new CNC reinvents the wheel; PrintNC has already done it. **Decide why you are making something new.**
- **ihavenofish, on PrintNC's tool changer problem, fixes that keep the machine:** (1) move the X rail to the front; (2) overhang the X axis off one side; (3) add 50 mm of Z height so tools fit under the gantry.

## 1. "Too many custom parts": the count
- V4 wave 1 (no ATC, D-328): **30 custom pieces**, about **22 different shapes** (some are the same part twice, `cad/v4/jlc-step/README.md`). 23 go to shops, 7 the owner makes (D-329).
- They need **4 shop processes**: CNC milling (7 x 6082 parts), turning (2 stub shafts), laser cutting (8 steel parts), surface grinding (5 rail seats: JLC does not grind, so a second shop). Phase 2 adds the ATC parts.
- Phase 1 is already **£4,386.61, over the £4,200 budget**, with grinding (F30) and other lines not priced (37th session). So the owner's worry is fair: the cost risk is the shop parts, and it is not known until the JLC prices come in.
- **The number of processes and shops is the real complication,** more than the part count. Grinding is the one most likely to be slow and dear.

## 2. Moving gantry / PrintNC: has this been tried?
Yes, partly. **v3 (`Type_0_v3`, D-172 to D-304) was the PrintNC V4 gantry, scaled down, on a cast epoxy granite tub.** It was left for V4 (D-305) because:
- **Front ATC wheel in the way** of the operator and the work (D-305).
- **Rear ATC not possible** (D-288, `docs/rear-atc-reach.md`): inside the tub only about 25 mm of tool fitted below the holder, because of the **tub** floor and walls.
- **Rails on machinable faces, hollow beam ringing** (D-305), and the cast tub itself (one-shot pours).

What ihavenofish suggests is different from v3: **stock PrintNC on its own frame, not on our tub**, plus three small changes. Most of the v3 reasons came from the tub, not from PrintNC:

| v3 problem | Stock PrintNC + the 3 changes |
|---|---|
| Rear ATC: no room under the beam inside the tub (D-288) | No tub. Change 3 (+50 Z) and change 1 (beam underside clear) are aimed at exactly this |
| Front wheel in the way | Change 2 puts the tools **beside** the bed, out of the way. MaxCahill said the same on 25 Nov (rack along the bed, no rotary) |
| Tub casting is one-shot | Gone: PrintNC's frame is bolted steel tube (check: Claude has not confirmed PrintNC's frame needs no welding; owner's rule is no welding) |
| Hollow beam rings | Still true for a PrintNC tube beam; V4's answer (fill the beam with EG, D-310) works on PrintNC too |

## 3. The three changes, as Claude reads them (owner to check with ihavenofish)
1. **X rail to the front.** In PrintNC the two X rails are on the **top and bottom** of the beam (`docs/printnc-assessment.md`). The bottom rail and its roller hang below the beam and use up the room under the gantry. With both rails on the **front face** (as V4 does, D-312) the beam's underside is clear. *Claude's reading; ihavenofish may mean something else.*
2. **Overhang X off one side.** The beam runs past one Y rail, so the spindle can go outside the bed. The tool rack sits there, **along Y**, beside the bed: no wheel, no motor, no indexing.
   - **Catch: how many tools.** The holders have Ø45 flanges (`docs/atc-wheel.md`), so the forks need about 60 mm pitch (D-17 used 60). Type 0's Y travel is 300 to 350, so a side rack along Y holds about **6 tools per row**, not 12. *(Corrected 26 Nov: this first said 40 pitch and 8 to 9 tools.)*
   - The overhang puts more load on one Y roller, and the X screw gets longer.
3. **+50 mm Z.** Room for tool holders under the gantry, so a rack can also sit along the back of the bed. **Cost:** taller Y rollers (or raised rails) and a longer lever from the Y rails to the tool: the machine gets softer in Y. Not worked out.

## 4. "Why make something new?" (for the owner)
This is the question that decides it, and only the owner can answer. From `docs/requirements.md`, what Type 0 asks for: small, accurate parts (±0.02) in aluminium, brass and steel; **12-tool ATC**; garage, pieces you can carry; **£4,200**. As far as the repo shows, a PrintNC (with the 3 changes) is a fair fit for most of it. The custom parts in V4 come mostly from three things: the **fixed gantry** frame, the **EG fill** and ground rail seats, and the **ATC wheel**. If none of those is a must, ihavenofish's point stands.

## 5. If the university buys a mill
Then the owner could make the 7 milled 6082 parts (and later the ATC parts) themselves, as planned for the ATC mount in v3 (D-289, "mill first, JLC fallback"). That cuts the shop cost, not the part count or the design work.

## Suggested next step (not decided)
- **Do not drop V4 before the JLC prices are in** (`cad/v4/jlc-step/`, about an hour of uploading). They answer the "very expensive" worry with numbers.
- In parallel, a **one-page side-by-side: V4 against stock PrintNC + the 3 changes**: custom parts and processes, tools in the rack, Z clearance, footprint, what can be priced from live pages. No modelling. The PrintNC STEP is already here (`PrintNC V4 Metalcutter V4.0.33 Elements to take.step`, untracked).

## To ask the owner
1. Why a new machine rather than a PrintNC: which of fixed gantry, EG fill, ground seats, 12-tool wheel is a must?
2. Do the side-by-side (V4 vs PrintNC + 3 changes) now, or wait for the JLC prices?
3. Is about 6 tools per row in a side rack enough? *(Answered by D-340: rack of 16 to 18 in 2 rows; see `docs/v5-idea-matrix.md`.)*
4. Ask ihavenofish what "move the X rail to the front" means exactly.

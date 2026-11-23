# Outstanding design and layout issues (23 Nov 2026; owner answers D-264 to D-276 added)

Collected from `HANDOVER.md`, `tasks/README.md`, `machine-assessment.md`, `spec-gaps.md`, `open-items-sketch.md`, `cad-cleanup-owner-items.md` and `decisions.md` (to D-263). Design and layout only: prices and supplier items are at the end, in brief.

## A. Structure and accuracy (biggest technical risk)
1. **Stiffness budget is nearly used up.** Calculated parts give about 15 of the 20 µm at the top of Z. Not calculated: PrintNC rollers, roller screws, bearing blocks, spindle clamp. (open; mapping run)
2. **Screws threaded into 3 mm tube walls** (top roller screws, Y roller tube M6 x 12 with 3 of thread). Not checked. Options: rivet nuts or through-bolts. **Decided D-270: keep as PrintNC.**
3. **Printed PETG risers and motor plates (D-244)**: BK12/HM12/BF12 risers, NEMA 24 plates, nut plates. Stiffness not checked. They carry screw thrust. **Decided D-272: commissioning parts, aluminium replacements first job.**
4. **Wall-top steel plates (D-256)**: rails rely on the plate's own flatness, no levelling pour. No flatness spec set for buying the plate. **Decided D-271: jack screws + 8 mm levelling pour; to model.**

## B. Spec misses (`spec-gaps.md`)
5. Table to nose **5 to 25 short** of 180 to 200 at the top of Z (D-09). Decide: accept, or raise Z. **Decided D-267: 175 accepted.**
6. Fixture plate has **8 hold-downs**, owner asked for 10 (D-240, then D-241 removed 2). **Decided D-268: 8.**
7. X travel 430 against the old 570 spec: likely no longer needed (ATC moved), but not decided. **Decided D-269: 430.**
8. `requirements.md` still says fixed gantry, rear ATC rack, all-EG frame, 200 to 350 kg. Needs updating to the moving-gantry design. **Done D-269.**
9. Frame mass not summed. Probably under 200 kg. **Done: about 165 kg (requirements.md).**

## C. Layout items not yet in the model
10. **Front slot** through the tub floor and plate (task 24 item 6): not sized or modelled. Limits: X ±107.5, ending by Y 210. Must also leave the ATC zone clear. **On hold, high priority (D-273).**
11. **ATC keep-out**: nothing in front of the tub from X 88 to 312, up to about 250 forward. Bench top, slot bench and enclosure must respect it. **On hold: rear ATC study (D-274, task 26).**
12. **D-251 / D-253 ATC strip** in the tub floor front face (X 200, Z -10 to 40): must go on the mould drawing before the pour. **On hold (D-274).**
13. **Y soft limit**: ATC pickup is only 3 from the Y stop. Set the limit at -86 or beyond and check on the built machine.

## D. Fastener and assembly questions (owner to decide)
14. Y block screw heads hit the tie-rod nuts by 0.9 (D-212). Claude's pick: DIN 7984 low head M5 x 8. **Decided D-264: ISO 7380; modelled 23 Nov (5th session), clears the nut by 1.35.**
15. No key access to the X top block screws (D-215), and Y is the same. Claude's pick: fit the blocks first, through the open tube ends. **Decided D-265: blocks first.**
16. Three holes Claude could not place: Ø16 in the X gantry tube (Y 549, Z 309); Ø10 in the Y chain support (Y 220, Z 39); 2 M5 in the X roller tube 2 below the top angle holes. **Decided D-266: fill. Modelled 23 Nov (5th session): the 2 M5 tube holes are filled. The other two are not holes: the Ø16 is the gantry tube's own R8 inside corner, the Ø10 is the zip-tie channel under the chain support base (links its 4 zip-tie slots). Left as they are.**
17. X 1610 fill plate and nut plate: still visible. Used with the DFU1605 nuts or not? (Claude checks the fit in the model, then asks)
18. X gantry trigger mount: its M6 x 20 is 2.5 short of the tube face.
19. X BKHM12 riser: its BK12 holes were not checked in D-263 (Y and Y2 were).

## E. Proposals waiting for the owner's confirmation
20. D-250, D-251, D-253, D-255: ATC bracket parts, lift height Z 232, the 4th strip's size and place, the fork layout ("Proposed by Claude, owner to confirm"). **Not confirmed: rear study (D-274).**
21. D-211: HM12-60 Z motor mount and the 442 Z plate. **D-276: ask the seller (message 4).**

## F. Stand-ins and unknown dimensions
22. Jianken spindle drawing: mass, nose shape, ISO20 holder sizes. The ATC's 5 and 7 mm gaps depend on them.
23. ATC motor real length and encoder; fork screw M3 or M4. **Fork screw M4, 8-flat hub (D-275).**
24. ATC holders, bearings and collar are still stand-ins (D-252).
25. Roller steel sizes (D-243): X roller tube 120 x 50 x 3, X roller angles 125 x 50 x 6 and Y braces 75 x 75 are not stock sizes. Choosing stock sizes may move the layout.
26. ATC bracket print is 80 x 187 x 93: check that it fits the printer bed.

## G. Model health and checks still to run
27. ATC clash check with the **moving** Z (only the static check and moved copies were done).
28. Timeline has 35 unhealthy items; `Chamfer2` (item 617) has 2 lost edges.
29. 373 hidden PrintNC fastener bodies remain (can go later).

## H. Blocked downstream work
30. Mould drawings (tasks 10, 11, 12) and the rail-seat procedure (18): not started. They wait on items 10, 12 and the Fusion pass (task 09).
31. Z motor mount (task 14): waits on the seller's drawing.

## Not design, but it limits the design
- £236.65 left, with G01 beam, G05 roller steel, X18 and X21 screws unpriced; A06 needs re-pricing. Next: LiMo basket and the Dyfed call (`price-check-task-17.md`). Wave 1 is 4 Jan 2027.

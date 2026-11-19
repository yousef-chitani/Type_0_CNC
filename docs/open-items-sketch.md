# The 2 open items, sketched (19 Nov 2026)

Picture: `cad/v2/out/open_items_sketch.png` (script `cad/v2/open_items_sketch.py`). All numbers were measured in Fusion `Type_0_v3` (timeline 1439, saved). Nothing in the model was changed.

## Item 1: Y block screw heads hit the tie rod nuts (D-212)
- 4 screws (Y and Y2, the 2 nearest the Y nut plate). The head sits on the tube bottom wall at Z 158. A DIN 912 head (5 high) reaches Z 163. The M5 nut starts at Z 162.1. Clash: 0.9.
- **A** keep DIN 912: clash.
- **B** DIN 7984 low head M5 x 8: head 3.5, same 8.5 dia, 3 mm key. Clears by 0.6. **Claude's pick: closest swap.**
- **C** ISO 7380 button head M5 x 8: head 2.75, 9.5 dia, 3 mm key. Clears by 1.35, lower tightening torque.
- Turning the nut flat-down gains only 0.45: not enough. Not priced.

## Item 2: no key access to the M5 x 8 X top block screws (D-215)
- Above the heads are: the top angle flange (6), the tube top wall (3), 6 M5 tie rods (lowest pair 1.1 above the heads) and, over screws 7 and 8 (X -162), the DFU1605 flange. The flange clears the heads, but it blocks the key.
- **A** Assembly order, no new holes: screw the blocks on first with an L-key through the open tube ends (inside 44 high; screws 14.5 and 50 from the ends). Then fit the rods, the nut, the end plates and the top angle. To change a block later, strip the X carriage. **Claude's pick.**
- **B** 8 x Ø6.5 holes through the angle flange and the top wall. They clear the M6 x 8 flange screws by 2.2, but the rods still block all 8 screws and the nut blocks 7 and 8. They help only with those parts out.
- **C** Go back to HGW20CC flanged blocks, screwed from below. This undoes D-215 and changes M02 in the BOM.
- The same holds on Y: the rods block the D-212 key-access holes (handover note 2a), so Y is also screw-first.

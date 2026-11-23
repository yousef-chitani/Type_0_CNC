# ATC one-piece mount: modelling plan

> For agentic workers: run inline (owner said "model it"). Steps use checkboxes.

**Goal:** model D-289 in `Type_0_v3` (Fusion 360) and check it.
**Architecture:** Fusion API scripts through the Fusion MCP. Old parts are removed with Remove features (history kept, reversible). Moved parts get Move features. New parts are built as new bodies in the existing ATC subcomponents.
**Spec:** `docs/superpowers/specs/2026-11-23-atc-one-piece-mount-design.md` (bearing changed to 2 x 6804 by the owner, 23 Nov: the 6004 bore cut the motor screw holes).

## Global constraints
- World mm; wheel axis X 200, Y -174. Fork plane Z 131 (moved down 40).
- Do not save the document; the owner saves.
- Each step is checked by printing body bounding boxes (the "test").

## Review focus
1. Tools sweeping over the arm and flange notch (tool tip Z 45 against the arm top Z 12).
2. Spindle at approach, pickup and lift positions against the moved wheel.
3. Motor screw counterbores against the 6804 bore (wall ≥ 2).
4. Sensor hole against the cup wall and the motor.
5. Motor body inside the Ø62 pocket.

### Task 1: remove the old stack
Remove: PETG bracket, top plate, both posts, KFL004 upper, shaft collar, Ø20 x 91 shaft, 4 post screws, 2 M6 x 40, 4 M3 x 10.
Check: none of these bodies are listed any more.

### Task 2: move the wheel parts down 40, the motor up 13
Down 40: hub, index flag, 8 forks, 8 fork screws, 16 holders and tools, LJ12A3 sensor. Up 13: motor (face Z 68 to 81).
Check: fork Z 126 to 136, holder top 185, tool tip 45, motor Z 13 to 105.

### Task 3: model the mount (one body, 6082)
Web Ø116 Z 81 to 119; cup Ø74 Z 12 to 81; arm X 160 to 240, Y -52 to -174, Z -10 to 12, rounded Ø80 at the axis; flange X 160 to 240, Y -52 to -37, Z -10 to 40. Cuts: notch X 188 to 212 above Z 12; pocket Ø62 Z 12 to 81; bearing bore Ø32 Z 89 to 119; pilot Ø22 Z 81 to 89; motor screws Ø3.4 at r 21.9 (31 square), counterbore Ø6 down to Z 89; grub access Ø6 along X at Z 85; sensor Ø12 at 202.5°, r 44; cable Ø16 through the arm at the axis; 4 M6 counterbored at X 172 and 228, Z 0 and 30.
Check: bounding box X 142 to 258, Y -232 to -37, Z -10 to 119; volume printed.

### Task 4: bearings, spacer, hub spigot, fasteners
2 x 6804 stand-in rings (Ø20/Ø32 x 7) at Z 89 to 96 and 112 to 119; spacer Ø32/Ø26 Z 96 to 112. Spigot Ø20 Z 82 to 119 joined to the hub, bored Ø5 Z 82 to 106, M4 grub hole along X at Z 85. 4 x M6 x 40 flange to strip; 4 x M3 x 12 motor to web.
Check: bodies listed with these boxes.

### Task 5: checks
Interference of all ATC bodies with each other and with the machine at rest; holders swept (copies rotated 22.5° steps) against the mount; spindle copies at approach, pickup and lift. Screenshot.
Then update `docs/atc-wheel.md`, D-289/D-290, the handover; commit and push.

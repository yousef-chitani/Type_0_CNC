# Decision log

| # | Decision | Reason |
|---|---|---|
| D-01 | Fixed gantry, table moves in Y | Stiffest layout for EG. Same as Bootstrap Bill |
| D-02 | Cast the EG at home | Cost |
| D-03 | Target accuracy ±0.02 mm | Realistic for DIY EG with good alignment |
| D-04 | ISO20 taper | Matches the chosen spindle. Light holders, compact rack |
| D-05 | Rack lives behind the gantry | Leaves the work area clear and away from chips |
| D-06 | Rack comes in low, through the table opening | During a tool change the table moves forward out of the way and the rack slides in under the spindle. No window in the beam, so Z stays short. X travel stays at the work size. Any Y overrun is to be checked in the layout (it depends on rack depth) |
| D-07 | Mist / MQL coolant, full enclosure | Works for alu and steel, with less mess than flood |
| D-08 | Z travel can drop below 250 mm | Small parts. A shorter Z overhang is stiffer. Value set in D-09 |
| D-09 | Z travel 150 mm, about 180–200 mm clearance | Fits a vise, a part and a long tool. Short overhang stays stiff. Enough lift to clear the rack forks |
| D-10 | C7 rolled ballscrews with preloaded double nuts (DFU) | Fits the budget. About ±0.05 mm per 300 mm, brought to ±0.02 mm with a mapping run and LinuxCNC screw compensation |
| D-11 | HGR20-pattern rails, Z1 preload | Plenty for this size. Rails will be checked and sorted on arrival |
| D-12 | Rail seats made with a self-leveling epoxy layer over cured EG, rails bolted to cast-in inserts | Cheap and good to about 0.01–0.02 mm if done carefully. No reference surface needed |
| D-13 | SFU1605 ballscrews, preloaded DFU nuts, on all three axes | Fine resolution and high thrust for steel. One screw and nut type for all axes. Rapids about 6–7 m/min, enough for small parts |
| D-14 | Direct drive through disc or bellows couplings | No backlash and nothing to tension |
| D-15 | NEMA 24 closed-loop steppers, about 4 Nm, on all axes | Margin for the heavy table and for steel |
| D-16 | Z motor has a built-in 24 V holding brake | Stops the spindle drifting down with the power off. Simplest and safest option |
| D-17 | Rack holds two rows of 4 ISO20 pockets at about 60 mm pitch | 4 × 60 mm fits within the 250 mm X travel. Keeps all 8 tools without widening the machine |
| D-18 | Rack driven by a small stepper on a screw or belt, run as a 4th joint in LinuxCNC with a home switch | Exact stop for each row and adjustable in software. Doesn't depend on air pressure |
| D-19 | Tool-length sensor on the rack carrier | Protected from chips and takes no table space. Measures each tool right after pickup |
| D-20 | Y: 2 rails about 220 mm apart, 2 carriages per rail, about 150 mm apart along Y | Wide stance resists cutting moments. Room for the screw between the rails |
| D-21 | X: 2 rails on the gantry front face, about 150 mm apart vertically, screw between them | Only one face to level-pour. Simple and proven on DIY gantries |
| D-22 | Z: rails on the moving spindle plate, blocks fixed on the X saddle | Compact, light saddle. Fine for 150 mm of travel |
| D-23 | Table: 25–30 mm aluminium tooling plate with a threaded M6/M8 grid, about 320 × 320 mm | Light, cheap, can be surfaced on the machine. Suits small fixtured parts |
| D-24 | Separate EG castings (base; gantry), bolted and epoxy-bonded | Smaller molds, each about 60–150 kg, so easier to vibrate and handle. The gantry can be squared to the Y rails before bonding |
| D-25 | Molds made of melamine-faced MDF/ply with packing tape, wax and PVA release | Cheap, flat, easy to cut. Good for one-off castings |
| D-26 | Graded aggregate mix with about 10–12% epoxy by weight | Kiln-dried quartz gravel, sand and fine filler following a packing curve, with low-viscosity casting epoxy. Less epoxy means less cost, less heat and less shrinkage |
| D-27 | Compact on a sprung vibration table driven by unbalanced motors | Even compaction, no voids, reusable for every casting |

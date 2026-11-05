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
| D-28 | Rail and pad fixings are steel insert bars (40×10 mm, tapped), bolted to the mould floor during the pour | Holes stay in line at the rail-bolt pitch and can't drift during vibration |
| D-29 | Gantry joins the base with M12 bolts plus a grout layer: shim the gantry square, inject epoxy grout, tighten after cure | Square and stiff, and the joint isn't stressed while it cures |
| D-30 | Solid castings (no cores) | No documented DIY example of large foam cores was found. Solid is the most proven. Cost: about 315 kg and about 41 kg of epoxy. Curing heat must be managed (see eg-moulds.md) |
| D-31 | Mesa 7i76EU (Ethernet) as the only interface board | 5 step/dir (4 used, 1 spare), 32 inputs and 16 outputs cover the about 20 inputs and 10 outputs needed, with room to spare |
| D-32 | Spindle VFD controlled over Modbus RS-485 | Speed command plus readback of actual speed, faults and load. Lets LinuxCNC confirm the spindle has stopped before releasing a tool |
| D-33 | Water-cooled spindle, with a flow switch interlocked into LinuxCNC | Quiet and doesn't stir up dust in the enclosure. The spindle can't run without coolant flow |
| D-34 | x86 mini-PC with an Intel network port dedicated to the Mesa board | Reliable timing, cheap used |
| D-35 | Hardwired e-stop: buttons and the Mesa watchdog run through a safety relay that drops a contactor, cutting drive power and the VFD run signal | Still stops if the PC or software crashes. The Z brake engages when power drops. LinuxCNC only reads status |
| D-36 | One 48 V DC supply (about 10 A) for all 4 stepper drivers | Keeps torque up at speed. The rack driver must accept 48 V |
| D-37 | Electrical cabinet built into the stand, underneath the machine | Owner's choice: compact. Mitigations: sealed steel box with a sloped drip lip above it, filtered fan blowing air in (keeps dust and mist out), raised off the floor, away from the coolant drain, VFD mounted at the top with heat vented clear of the drives, door reachable from the front |
| D-38 | CW-3000-style radiator unit for the spindle water loop, using its flow alarm output for the interlock | Plenty for 2.2 kW, cheap. Confirm the model has a flow alarm output before buying |
| D-39 | Spindle: Jianken JGL-80/2.2R24-20 (24,000 rpm, 400 Hz, 220 V, ISO20, water-cooled), with clamp/unclamp sensors | About 0.87 Nm vs about 0.70 Nm for the R30 version, so about 25% more torque at every working speed. Better for steel and brass. Sources: [Jianken manual (LinuxCNC forum)](https://forum.linuxcnc.org/media/kunena/attachments/27367/OperationManual2019.pdf), [Amazon listing](https://www.amazon.com/LVSEDTAL-JGL-80-2-2R24-20-24000rpm-Spindle/dp/B0F5HKDVV4) |
| D-40 | ISO20-ER16 tool holders (8) | Owner's choice: cutters up to 10 mm |
| D-41 | Z motor: StepperOnline 24HS34-5004D-E1000-B280 (3 Nm closed-loop with 2.8 Nm 24 V brake) on a CL57T driver | Same frame, maker and driver as X and Y. 3 Nm is plenty for Z: holding the spindle needs only about 0.1 Nm through a 5 mm lead |
| D-42 | Precision level 0.05 mm/m (Dasqua 200 mm, £68.50) instead of 0.02 mm/m (£333.72) | The rail seats level themselves in one linked pour. The level only sets the casting and stand roughly level. Saves £265.22 |
| D-43 | Prefer collecting materials in person from B&Q (Nissan Qashqai) | Owner's preference: avoids delivery costs. Aggregates must still be clean and dry |

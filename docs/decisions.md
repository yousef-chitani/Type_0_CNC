# Decision log

| # | Decision | Reason |
|---|---|---|
| D-01 | Fixed gantry, table moves in Y | Stiffest layout for EG. Same as Bootstrap Bill |
| D-02 | Cast the EG at home | Cost |
| D-03 | Target accuracy ±0.02 mm | Realistic for DIY EG with good alignment |
| D-04 | ISO20 taper | Matches the chosen spindle. Light holders, compact rack |
| D-05 | Rack lives behind the gantry | Leaves the work area clear and away from chips |
| D-06 | Rack comes in low, through the table opening | The table drives forward about 100 mm past its normal travel, and the rack slides in under the gantry. No window in the beam, so Z stays short. Cost: longer base, Y screw and Y rails |
| D-07 | Mist / MQL coolant, full enclosure | Works for alu and steel, with less mess than flood |
| D-08 | Z travel can drop below 250 mm | Small parts. A shorter Z overhang is stiffer. Value set in D-09 |
| D-09 | Z travel 150 mm, about 180–200 mm clearance | Fits a vise, a part and a long tool. Short overhang stays stiff. Enough lift to clear the rack forks |
| D-10 | C7 rolled ballscrews with preloaded double nuts (DFU) | Fits the budget. About ±0.05 mm per 300 mm, brought to ±0.02 mm with a mapping run and LinuxCNC screw compensation |
| D-11 | HGR20-pattern rails, Z1 preload | Plenty for this size. Rails will be checked and sorted on arrival |
| D-12 | Rail seats made with a self-leveling epoxy layer over cured EG, rails bolted to cast-in inserts | Cheap and good to about 0.01–0.02 mm if done carefully. No reference surface needed |

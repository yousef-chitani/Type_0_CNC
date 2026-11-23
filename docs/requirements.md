# Requirements (updated 23 Nov 2026, D-269)

| Item | Requirement | Notes |
|---|---|---|
| Work envelope | **400 × 250 mm** in X and Y (D-79; was 250 × 250, then 200 × 200 in v2). Spindle reach X 430, Y 385 (D-233); the old X 570 is dropped (D-269) | Z travel 150 mm; table to spindle nose 25 to 175 mm (D-267; was about 180–200, D-09) |
| Materials | Aluminium, brass, steel | Small, high-precision parts |
| Part accuracy | ±0.02 mm | Reached with C5 screws (D-136) plus LinuxCNC screw compensation (D-10) |
| Layout | **Moving gantry, fixed table** in a cast tub (D-137) | Gantry moves in Y on rails on the tub walls; spindle moves in X and Z on the gantry |
| Frame | Epoxy granite tub, cast DIY at home (D-196, D-197); steel SHS 120 × 120 × 8 gantry on PrintNC-style rollers (D-164, D-172, D-177) | Wall tops: steel plates on jack screws and an 8 mm levelling pour (D-271) |
| Spindle | Jianken 2.2 kW ATC, ISO20 | About 24,000 rpm. Low torque at low rpm, so steel needs light cuts and small tools |
| Tool changer | 8 tools on an umbrella wheel, Phase 2 (D-138, D-250) | Modelled at the front (X 200, Y -85 pickup); a rear position is being studied (D-274). Was a rack behind the gantry (D-06) |
| Drives | Closed-loop steppers | |
| Control | LinuxCNC on Mesa hardware | Board to be chosen |
| Coolant | Mist / MQL | |
| Enclosure | Full enclosure | Also keeps chips out of the rack |
| Air | Existing compressor | ATC tool release needs about 6 bar or more |
| Site | Garage, on a heavy stand built by the owner | Frame mass about 165 kg: tub about 92, wall plates 9, fixture plate 10, gantry, Z and spindle about 45 to 55 (was a budget of 200–350 kg). The tub carries no load that needs more mass |
| Budget | **Phase 1 ≤ £4,200** (D-127) (frame, motion, electronics, ER20 spindle). Phases 2 (ATC spindle, air, enclosure) and 3 (tool rack) budgeted later | D-66, D-68 |

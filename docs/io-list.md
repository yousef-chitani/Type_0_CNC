# I/O list (draft)

Board: **Mesa 7i76EU** (D-31). Pin numbers will be assigned after checking the 7i76EU manual.

## Step/dir channels

| # | Joint | Notes |
|---|---|---|
| 0 | X | NEMA 24 closed-loop, SFU1605 |
| 1 | Y | NEMA 24 closed-loop, SFU1605 |
| 2 | Z | NEMA 24 closed-loop with brake, SFU1605 |
| 3 | Rack slide | Small stepper. Two positions (front row, back row) plus parked |
| 4 | Spare | Future 4th axis |

## Inputs (24 V, isolated)

| Signal | Count | Notes |
|---|---|---|
| Home switches X, Y, Z, rack | 4 | Also act as limits where possible |
| Drive alarm X, Y, Z, rack | 4 | Closed-loop driver fault outputs |
| Tool clamped / unclamped sensors | 2 | On the spindle. Check which ones the Jianken model includes |
| Air pressure OK | 1 | Pressure switch, about 5.5 bar |
| Spindle coolant flow OK | 1 | Flow switch (D-33) |
| Tool setter | 1 | On the rack carrier (D-19) |
| Touch probe | 1 | |
| E-stop status | 1 | The e-stop chain itself is hardwired |
| Enclosure door closed | 1 | |
| Rack cover / rack at park | 1 | Optional |
| **Total** | **about 17–18** | 32 available |

## Outputs

| Signal | Notes |
|---|---|
| Tool release solenoid | Interlocked: spindle confirmed stopped (Modbus) and Z at tool-change height |
| Taper cleaning air blast | |
| Mist coolant | |
| Air blast | |
| Z brake release | Released only while the drives are enabled |
| Drive enable | |
| Coolant pump | Starts before the spindle |
| Enclosure light | |
| Rack cover | Optional |
| **Total** | **about 8–9**, 16 available |

## Serial

- **Spindle VFD over Modbus RS-485** (D-32): set speed, run/stop, read actual speed, faults and load.

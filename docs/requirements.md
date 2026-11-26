# Requirements (updated 26 Nov 2026, V4 frozen: D-305 to D-336)

| Item | Requirement | Notes |
|---|---|---|
| Work envelope | **400 × 250 mm** in X and Y (`D-79`, table `460 × 330`). Axis travels: **X 620** (`-215` to `+405`: `430` over table + `190` right-side ATC reach), **Y 300** (`±150`), **Z 150** | Table top (`Z = 0`) to spindle nose: **25 to 175 mm** (`D-267`); over the ATC wheel (`X > 265`), soft-limited to `nose >= 70` at pickup (`D-316`, `D-317`) |
| Materials | Aluminium, brass, mild/alloy steel | Small, high-precision parts |
| Part accuracy | ±0.02 mm | LiMo C5 ground DFU1605 double-nut ballscrews (`D-136`) + HGR20 ZA rails on shop-ground steel seats (`D-311`, `D-312`) + LinuxCNC screw compensation |
| Layout | **Fixed gantry, moving table (`D-305`, frozen `D-324`)** | Table (`M11`, `460 × 330 × 25` 6082) moves in Y directly on 4 HGH20CA blocks (`D-313`); spindle moves in X and Z on the gantry |
| Frame | Bolted KJN `90 × 90 H` aluminium extrusion base tray (`4 × 500`) + `20 mm` steel end plates (`D-308`); `50 × 150 × 325` steel uprights (`D-309`); `SHS 120 × 120 × 8 × 890` steel beam (`D-306`); `10 mm` steel rear shear plates + spacers (`D-323`); base pockets + beam filled with `23.5 L` lean EG (`~54 kg`, `D-310`, `D-315`, `D-336`) | No structural casting, no welding. Rail seats: `2 × 50 × 20 × 670` bright bars on Y and one `160 × 20 × 890` plate on X, shop surface-ground (`F30`) |
| Drives | Closed-loop NEMA 24 steppers (`CL57T V4.1`): Y inline at rear (`24HS40`), X and Z belt-folded 1:1 (`HTD 250-5M-15` at `75 mm` centres) onto `Ø10` stub shafts in `HM12-60-V` mounts (`D-320`, `D-325`–`D-327`, `D-331`); 24 V brake on Z (`24HS34-B280`, `D-322`) | Overall machine envelope incl. ATC wheel: **`954 × 805 × 880 mm`** (`X -403.7..+550.0, Y -335.0..+470.0, Z -278.0..+601.7`) |
| Spindle | Phase 1: G-Penny 2.2 kW ER20 water-cooled (`S08`, `D-78`); Phase 2: Jianken JGL-80/2.2R24-20 ISO20 ATC (`S01`, `D-39`) | 24,000 rpm, 80 mm split clamp + tram blocks on Z moving plate (`D-247`) |
| Tool changer | **12 tools on a vertical wheel outside the right side (`+X`, Phase 2, `D-307`, `D-314`–`D-318`)** | Axis along X (`Y = 0, Z = -82`), pickup at `X = 402`, inboard 6082 hub block on `End plate X+` with FK12, 1:3 GT2 belt drive, SHF12 hub and laser-cut 6 mm 5083 spoked disc. Hangs `110 mm` below base bottom (overhangs bench right edge) |
| Control | LinuxCNC on **Mesa 7i76EU** (`E01`, `D-31`) | Dual-channel safety relay (`E06`), RS-485 Modbus to VFD (`D-92`) |
| Coolant | Mist / MQL (`P04`) | Side-mounted printed PETG drip skirts (`F32`, `D-335`) shield the Y rails; blind M6 table grid (`D-334`) keeps coolant off the Y screw |
| Enclosure | Full MDF + polycarbonate enclosure (`Phase 2`, `N01`–`N04`) | Must clear `954 × 805 × 880 mm` plus Y table travel and cable loops |
| Site & Mass | Garage, on owner-built timber stand (`T01`–`T17`) | Total machine mass **~205 kg** (extrusion + end plates 40, EG fill 54, uprights + rear plates + spacers 54, beam + front plate + pads 48, table + Z + motors + spindle ~30; stand-in pieces all carriable before assembly) |
| Budget | **Phase 1 target ≤ £4,200 (`D-127`)** | Currently over target before shop quotes (`docs/phase1-cost.md`); owner makes simple saw/drill/tap steel parts (`D-329`), shops quote laser, mill, grind and lathe sub-packs (`D-330`, Task 29) |

# Electrical design: Phase 1 (task 1)

Source for all Mesa details: **7I76EU manual** (owner-supplied PDF). Items marked **CHECK** must be confirmed against the part's own manual before wiring.

## 1. Power distribution

```
13 A plug (fused 13 A) ──► 2-pole main isolator (E17)
   ├─► MCB C16 ──► EMC filter (E09) ──► contactor pole 1 (L) + pole 2 (N) ──► VFD (S02) ──► spindle
   ├─► MCB C6  ──► contactor pole 3 (L) ──► 48 V PSU SDR-480-48 (E04) ──► 3 × CL57T drives
   └─► MCB C6  ──► 24 V PSU HDR-150-24 (E05)  [ALWAYS ON: never through the contactor]
                │   ──► cabinet filter fan 230 V (E18)
                └─► pump relay contact (E23) ──► coolant pump 220 V (S08 kit)
PC + monitor: own plug (or the third C6 MCB).
```

- **24 V rail (always on):** 7I76EU field + logic power, safety relay, contactor coil, sensors, Z brake, pump relay coil, radiator fans, flow switch.
- **The 7I76EU field power (VFIELD) must come straight from the PSU.** A fuse is OK. A switch, relay or contactor is not (manual: VFIELD ramp < 10 V/ms).
- **13 A plug note:** a single-phase VFD draws more input current than the spindle's output power suggests. Normal cuts are fine. If sustained full-power cutting blows the plug fuse, move to a 16 A circuit (D-91).
- 24 V budget (Phase 1): Mesa about 0.1 A, sensors 4 × 15 mA, contactor coil about 0.1 A, Z brake 0.19 A (4.5 W), fans about 0.2 A, relay coil about 20 mA, safety relay about 0.1 A ⇒ **under 1 A** of the 6.25 A available. Phase 2 solenoids add about 0.6 A.

## 2. Safety chain (hardwired, D-35)

```
+24V ─ A1 Schneider XPSAC5121 (E06) A2 ─ 0V
Channel 1: S11 ─ [E-stop 1 NC-a] ─ [E-stop 2 NC-a] ─ S12
Channel 2: S21 ─ [E-stop 1 NC-b] ─ [E-stop 2 NC-b] ─ S22
Reset:     S33 ─ [green reset button NO (E21)] ─ S34
Output 1:  +24V ─ 13 ─ 14 ─ contactor coil A1 (E07, 24 V DC) ─ A2 ─ 0V
Output 2:  Mesa OUT1 (TB6-18) ─ 23 ─ 24 ─ [Z brake coil +] ─ [Z brake coil −] ─ 0V      (D-93)
                                         └── TVS P6KE33CA (E25) across the coil ──┘
Output 3:  33 ─ 34 spare
```
- **XPSAC5121 datasheet (read 2026-11-08):** 3 NO safety outputs plus 1 solid-state signalling output; each relay output 1.5 A at 24 V DC (DC-13), minimum 10 mA at 16 V; response ≤ 100 ms; start type "unmonitored" (don't bridge the reset button). Both loads are well inside the rating (contactor coil about 0.1–0.25 A, brake 0.19 A).
- **CHECK** the terminal names (S11/S12, S21/S22, S33/S34, 13-14, 23-24, 33-34) on the module's label or wiring sheet: the product datasheet doesn't show them. The scheme above is the usual Preventa layout.
- **Z brake hardwired (D-93):** the brake coil is fed from Mesa OUT1 *through* safety output 23-24. It only releases when LinuxCNC asks for it *and* the safety chain is closed. Pressing an e-stop drops the brake directly, at the same moment the contactor drops the drives, whatever the PC is doing. The TVS diode (bidirectional, about 33 V) across the coil absorbs the coil's turn-off spike when the safety contact opens (the Mesa output's own clamps don't help then). A TVS lets the brake grip faster than a plain flyback diode would.
- E-stops (E08, 2 NC each): **one at the front of the bench, one on the cabinet door** (D-91).
- The contactor drops the 48 V PSU (drives lose power) and the VFD supply. At the same moment safety output 23-24 opens and the Z brake engages (it is a power-off brake).
- **Feedback to LinuxCNC:** +24 V ─ contactor aux NO (13-14) ─ Mesa IN3 "machine power OK". LinuxCNC's own e-stop chain needs IN3 true and no drive alarms.

## 3. 7I76EU jumpers

| Jumper | Setting | Why |
|---|---|---|
| W1 | **Left** (default) | VIN taken from VFIELD: one 24 V supply powers the field I/O |
| W5 | Operate (default) | Normal 2.5 Mbaud field I/O |
| W6 | **Right** | RS-485 termination off. TB3 RS-485 is now unused in Phase 1 (VFD moved to USB, D-92) |
| W13 / W14 | Down / down (default) | Fixed IP **192.168.1.121** |
| W7 | Up (default) | Primary flash |

Logic power: +24 V to **TB3-21/22**, 0 V to **TB3-23/24** (on-card regulator; both TB1 and TB3 power are required).

## 4. Pin map

### TB1: field power
| Pin | Signal | Connect to |
|---|---|---|
| 1–4 | VFIELD | +24 V (fused 2 A, direct from the PSU) |
| 6–8 | GND | 24 V 0 V |

### TB2: step/dir (differential to the CL57T PUL/DIR inputs)
| Channel | Axis | STEP− / STEP+ | DIR− / DIR+ |
|---|---|---|---|
| 0 | X | 2 / 3 | 4 / 5 |
| 1 | Y | 8 / 9 | 10 / 11 |
| 2 | Z (brake motor) | 14 / 15 | 16 / 17 |
| 3 | *Phase 2: ATC wheel* | 20 / 21 | 22 / 23 |
Wire STEP+→PUL+, STEP−→PUL−, DIR+→DIR+, DIR−→DIR− at each driver, using screened twisted pairs (GND pins 1, 7, 13, 19 to the screen at the cabinet end only).

### TB3: logic power (RS-485 not used in Phase 1, D-92)
| Pin | Signal | Connect to |
|---|---|---|
| 21, 22 | Unreg logic + | +24 V |
| 23, 24 | GND | 0 V |
| 15–19 | RS-485 | Not used in Phase 1. Free for a later standard-Modbus device (`hm2_modbus`) |

**VFD link (D-92):** USB-RS485 adapter (E24) in the mini-PC. Adapter **A/+** → VFD **RS+**, **B/−** → VFD **RS−** (swap if it doesn't talk), adapter GND → VFD signal ground if it has one. One screened twisted pair, screen to the cabinet end only, kept away from the motor and spindle cables.

### TB4: analogue spindle
Not used (spindle over RS-485 via a USB adapter, D-92).

### TB6: field I/O 0–15 inputs, 0–7 outputs
Inputs are **sinking** (they read a positive voltage). The PNP sensors connect directly. Outputs are set to **sourcing** mode in `hm2.hal` (`source` mask 65535, `sink` 0: 7I76EU manual, Output modes; an output with neither bit set stays off). Each load returns to 0 V. Max 500 mA per output, 2 A per group of 8. No flyback diodes are needed on loads driven straight from an output (built-in clamps). Inputs switch on above 14.4 V and off below 9.6 V at 24 V field power.

| Pin | I/O | Function | Device |
|---|---|---|---|
| 1 | IN0 | X home | LJ12A3-4-Z/BY (brown +24, blue 0 V, black → IN) |
| 2 | IN1 | Y home | LJ12A3 |
| 3 | IN2 | Z home | LJ12A3 |
| 4 | IN3 | Machine power OK (e-stop chain) | contactor aux NO from +24 V |
| 5 | IN4 | X drive alarm | CL57T ALM (CHECK polarity, invert in HAL if needed) |
| 6 | IN5 | Y drive alarm | CL57T ALM |
| 7 | IN6 | Z drive alarm | CL57T ALM |
| 8 | IN7 | Coolant flow OK | flow switch from +24 V (CHECK contact rating) |
| 9 | IN8 | Tool length setter | *Phase 2 (A05)* |
| 10 | IN9 | Enclosure door closed | *Phase 2 (E15)* |
| 11 | IN10 | Air pressure OK | *Phase 2 (P03)* |
| 12 | IN11 | Tool clamped | *Phase 2 (ATC spindle sensor)* |
| 13 | IN12 | Tool released | *Phase 2* |
| 14 | IN13 | ATC wheel index | *Phase 2 (A09)* |
| 15 | IN14 | ATC wheel drive alarm | *Phase 2 (A03)* |
| 16 | IN15 | spare | |
| 17 | OUT0 | Drive enable (X, Y, Z ENA in parallel) | CL57T ENA (CHECK input voltage and logic) |
| 18 | OUT1 | Z brake release | via safety relay 23-24 (D-93) to the brake coil 24 V, 0.19 A |
| 19 | OUT2 | Coolant pump | interface relay coil (E23) |
| 20 | OUT3 | Radiator fans | 2 × 12 V fans in series on 24 V |
| 21 | OUT4 | Tool release solenoid | *Phase 2 (P02)* |
| 22 | OUT5 | Cone-clean air | *Phase 2 (P02)* |
| 23 | OUT6 | Mist | *Phase 2 (P04)* |
| 24 | OUT7 | ATC wheel drive enable | *Phase 2* |

### TB5: inputs 16–31, outputs 8–15
All spare for later (probe, pendant, Phase 2 additions).

## 5. Drives (CL57T V4.1)
- Power: 48 V from the SDR-480-48, each drive with its own pair of wires back to the PSU terminals.
- Motor and encoder: the motor's own extension cables. Keep them separate from the spindle cable.
- **From the CL57T manual (V3.0, read 2026-11-08; the V4.1 manual wasn't reachable, so confirm with the one in the box):**
  - PUL/DIR: 4.5–5 V high, 0–0.5 V low, 7–16 mA: the Mesa's 5 V differential step/dir outputs drive them directly, **no resistors**. Pulse ≥ 2.5 µs, DIR setup ≥ 5 µs, up to 200 kHz.
  - ENA: 4.5–24 V, so the 24 V Mesa output works **without a resistor**. Unconnected = enabled. With sourcing (PNP) wiring the manual says the logic is reversed: 24 V on ENA = disabled. So `output-00-invert` in `hm2.hal` will probably need to be 1 (confirmed in the bench test). With that setting, the drives are enabled whenever the Mesa output is off; that's acceptable because the contactor removes their 48 V on any e-stop.
  - ALM: open-collector output, 20 mA at 5–24 V, sinking or sourcing. Wire **ALM+ to +24 V, ALM− to the Mesa input**. Its polarity (on when healthy or on when faulted) is set in the drive's PC software and isn't stated; the bench test decides whether `hm2.hal` uses `input-0N` or `input-0N-not`.
  - DIP switches: factory setting **on off on on off off off off**. SW1–SW4 = on, off, on, on is **1,600 pulses/rev** (D-92). SW5 sets direction, SW7 off = step/dir mode.
- With 5 mm-lead screws: 1,600 pulses/rev = **320 steps/mm** (D-92).

## 6. VFD (Huanyang, from the G-Penny kit)
- Mains in via the EMC filter and contactor. Spindle out with the screened 4-core cable; the screen and the spindle PE go to the VFD PE terminal.
- **CHECK** these against the kit's VFD manual. These are the usual Huanyang HY settings for this spindle:

| Parameter | Value | Meaning |
|---|---|---|
| PD001 | 2 | Run commands from RS-485 |
| PD002 | 2 | Frequency from RS-485 |
| PD003 / PD004 / PD005 | 400 | Main / base / max frequency (Hz) |
| PD141 | 220 | Rated motor voltage |
| PD142 | spindle nameplate (about 10 A) | Rated motor current |
| PD143 | 2 | Motor poles |
| PD163 | 1 | Modbus address |
| PD164 | **1** (9,600 baud) | Baud rate (0 = 4,800, 1 = 9,600, 2 = 19,200, 3 = 38,400). Was wrongly given as 2 |
| PD165 | 3 (8N1 RTU) | Data format |

- LinuxCNC talks to it with the `hy_vfd` driver through a USB-RS485 adapter (D-92). The classic Huanyang uses its own protocol, not standard Modbus, so the Mesa RS-485 port can't drive it. Also set PD144 = 3000 (rpm at 50 Hz for a 24,000 rpm / 400 Hz spindle). Config: `linuxcnc/type0/spindle.hal`, set-up in `docs/linuxcnc.md`.

## 7. Cabinet layout (600 × 400 × 200, top to bottom)
1. Top: VFD (hot; vents clear above it), filter fan exhaust grille.
2. DIN rail 1: main isolator, 3 MCBs, EMC filter, contactor, pump relay.
3. DIN rail 2: 24 V PSU, 48 V PSU (or 48 V on the back plate), safety relay, terminal blocks (24 V, 0 V, PE).
4. Back plate: 7I76EU on standoffs, 3 CL57T drives.
5. Bottom: cable glands (gland plate), filter fan intake.
- Keep mains and spindle wiring on one side, signal wiring on the other. Cross at right angles.

## 8. Earthing and screens
- PE from the plug to a PE terminal block, then to the cabinet body, mounting plate, VFD, PSUs, spindle (via its cable) and the machine frame (to an insert bar).
- Cable screens: bonded at the cabinet end only (drives, VFD and the Mesa GND).

## 9. Parts this adds or changes
- **E24 USB-RS485 adapter** (D-92): to price.
- **E25 TVS diode P6KE33CA** across the Z brake coil (D-93): to price.
- **E23 DIN interface relay, 24 V DC coil, about 10 A contact** (for the 220 V pump): to price (RS).
- **E22 5 V PSU: shelved** (not needed for Phase 1).
- Cable glands and ferrules: already covered (basket glands, E13 crimper kit).

"""V5 sizing script (PrintNC moving gantry, 16-tool rack behind the bed). All lengths in mm.

One place for the V5 lengths. Plan Tasks 2 to 8 read sizes().
Run: PYTHONUTF8=1 python tools/v5_sizes.py
Sources for every input are in docs/v5-sizes.md. Each input is tagged:
STEP (measured in a STEP file), DRAWING, D-xxx (decision), LIMO (live page), or
ESTIMATE (no part data: to replace when the part is known).

PrintNC layout (STEP "PrintNC V4 Metalcutter V4.0.33 Elements to take.step", repo root):
the Y screw runs above the Y rail, inside the Y roller; the screw supports sit on
risers just past the rail ends; the beam spans the two Y rollers' outer faces.
V5 keeps that layout and puts its own parts in it.
"""
import math

# ---- Inputs: work, Z, rack ----------------------------------------------
WORK_X = 400                # D-344
WORK_Y = 250                # D-344
Y_WORK_TRAVEL = 300         # Y travel for 250 of work (requirements; v4-sizes rule)
NOSE_MIN, NOSE_MAX = 25, 225   # table to nose (D-348)
TOOL_RADIUS = 6.5           # largest ER20 collet, 13 mm (Phase 1 spindle ER20, D-78)
RACK_PITCH_X = 60           # D-344 (real holder flange Ø33, so 27 between flanges)
TOOLS_PER_ROW = 8           # D-344
RACK_ROWS = 2               # D-344
ENTRY_STROKE = 30           # fork entry slide along Y (docs/atc-wheel.md: Y -55 to -85)
CLEAR = 5                   # tool tip over the front-row holder tops (plan, Review Focus)

HOLDER_STACK = 45.85        # nose (spindle front face, D-352) to pull-stud top at pickup: flange top
                            # 7.483 to stud top 53.329 (STEP cad/vendor/iso20_er16_holder.step)
HOLDER_FLANGE_DIA = 33      # STEP cad/vendor/iso20_er16_holder.step (the stand-in was Ø45)
TOOL_MAX = 100              # longest tool below the nose (D-350)
ROW_PITCH_Y = 80            # front row to back row, holder centres (D-351)
RACK_BED_GAP = 40           # Y axis at end of work travel to front-row entry point (D-351)

# ---- Inputs: bought parts -------------------------------------------------
BLOCK_LEN = 77.5            # HGH20CA L (STEP cad/vendor/hgh20ca_block.step)
BLOCK_PITCH = 100           # 2 blocks per rail, centre to centre (D-150), X and Z
RAIL_END = 20               # spare rail past the blocks (D-150), X and Z
NUT_LEN = 100               # DFU1605 double nut (STEP cad/vendor/dfu1605_nut.step; DIN table L 100)
SCREW_ROOT_DIA = 12.8       # d 16 - ball 3.175 (DRAWING dfu_din69051_form_b_table) rounded down
BK12_LEN, BF12_LEN = 25, 20 # STEP cad/vendor/bk12.step, bf12.step (BK12 37 with lock nut)
HM12_LEN = 95               # HM12-60-V L (DRAWING hm12_60_v_motor_mount.png; 3rd-party model 90)
HM12_SCREW_IN = 59          # screw end inside the HM12 from its inner face (D-320 V4 model, 90 mount)

# ---- Inputs: PrintNC layout (STEP, repo root) -----------------------------
Y_CARRIAGE = 175            # Y roller nut plate to fill plate 1274..1439, plus 10 of nut past the
                            # nut plate (SFU nut 1264); the DFU flange sits where the SFU flange does
END_GAP = 0.5               # carriage to riser at the travel end (fill plate 1439 / BF riser 1439.5)
RISER_GAP = 0.7             # rail end to drive-end riser (rail 64 / BK riser 63.3)
BF_RISER_LEN = 35.5         # BF12 riser along the screw (1439.5..1475)
BF_SCREW_PAST = 32          # screw end past the rail end on the BF side (rail 1439, screw 1471)
BEAM_BF_END = 49            # beam end to BF riser (beam -530, riser -481)
ROLLER_HALF = 40            # Y roller half width; Y rail on its centre (roller 80, rail at ±490)
FRAME_TUBE_W = 80           # Y frame tube width: PrintNC 80 until Task 2
X_CARRIAGE = 150            # Type 0 Z fixed plate width along X (D-179, D-191)
Z_RAIL_V3, Z_SCREW_V3, Z_TRAVEL_V3 = 350, 350, 150   # D-136

# LiMo listings read by curl on 26 Nov 2026 (product pages, Zyro site):
# linear-guide-set-hgh15-20-25-30 (2 rails + 4 blocks) and
# dfu1605-2005-2505-2510-double-nut-ball-screw-set-c5-gound. Custom 10 to 4,000 on both.
LIMO_RAIL_SET = list(range(200, 901, 50)) + list(range(1000, 1801, 100)) + [2000]
LIMO_SCREW_C5 = list(range(300, 1001, 50)) + list(range(1100, 2001, 100))
LIMO_CUSTOM = (10, 4000)
SCREW_STEP = 50             # custom screws ordered in 50 steps (D-136)


def up(x, steps):
    return min(s for s in steps if s >= x)


def up_step(x, step=SCREW_STEP):
    return int(math.ceil(x / step) * step)


def critical_rpm(length, dia=SCREW_ROOT_DIA, k=3.927, safety=0.8):
    """Whip speed, fixed-supported ends, steel, root dia; whole screw length (conservative)."""
    E, rho = 206e9, 7850.0
    L, d = length / 1000.0, dia / 1000.0
    w = (k / L) ** 2 * (d / 4.0) * math.sqrt(E / rho)
    return safety * w * 60 / (2 * math.pi)


def rack_row_span():
    return (TOOLS_PER_ROW - 1) * RACK_PITCH_X       # first to last holder centre


def rack_y_depth():
    return RACK_BED_GAP + ENTRY_STROKE + ROW_PITCH_Y


def screw_for_rail(rail):
    """HM12-60-V drive end, BF12 far end, both on risers just past the rail ends (PrintNC)."""
    return up_step(rail + RISER_GAP + HM12_SCREW_IN + BF_SCREW_PAST)


def sizes():
    x_travel = max(WORK_X, rack_row_span()) + 2 * TOOL_RADIUS
    y_travel = Y_WORK_TRAVEL + rack_y_depth()
    z_travel = NOSE_MAX - NOSE_MIN
    # X: Type 0 carriage plate on 2 blocks per rail (D-150), rails on the beam front (D-349)
    x_carriage = max(X_CARRIAGE, BLOCK_PITCH + BLOCK_LEN)
    x_rail = up(x_travel + x_carriage + RAIL_END, LIMO_RAIL_SET)
    # Y: PrintNC roller between risers at the rail ends
    y_rail = up(y_travel + Y_CARRIAGE + 2 * END_GAP, LIMO_RAIL_SET)
    z_rail = up(z_travel + BLOCK_PITCH + BLOCK_LEN + RAIL_END, LIMO_RAIL_SET)
    x_screw, y_screw = screw_for_rail(x_rail), screw_for_rail(y_rail)
    z_screw = Z_SCREW_V3 + (z_travel - Z_TRAVEL_V3)          # v3 Z, 50 longer (D-348)
    beam_len = BEAM_BF_END + BF_RISER_LEN + END_GAP + x_rail + RISER_GAP + HM12_LEN
    frame_x = beam_len                                       # beam spans the Y rollers (PrintNC)
    frame_y = HM12_LEN + RISER_GAP + y_rail + END_GAP + BF_RISER_LEN   # on the Y tube, motor overhangs
    return dict(
        x_travel=x_travel, y_travel=y_travel, z_travel=z_travel,
        nose_min=NOSE_MIN, nose_max=NOSE_MAX,
        rack_row_span=rack_row_span(), rack_y_depth=rack_y_depth(),
        holder_top_min=None if HOLDER_STACK is None else NOSE_MIN + HOLDER_STACK,
        holder_top_max=NOSE_MAX - CLEAR - TOOL_MAX,
        tool_max=TOOL_MAX,
        x_rail=x_rail, x_screw=x_screw, y_rail=y_rail, y_screw=y_screw,
        z_rail=z_rail, z_screw=z_screw,
        beam_len=beam_len, frame_x=frame_x, frame_y=frame_y,
        y_rail_spacing=frame_x - 2 * ROLLER_HALF,
        frame_inner_x=frame_x - 2 * FRAME_TUBE_W,
    )


if __name__ == "__main__":
    s = sizes()
    for k, v in s.items():
        print(f"{k:18s}{v:9g}" if v is not None else f"{k:18s}  waiting (ISO20 holder STEP)")
    longest = max(("x_screw", "y_screw", "z_screw"), key=lambda k: s[k])
    print(f"{'whip_rpm_80%':18s}{critical_rpm(s[longest]):9.0f}  ({longest} {s[longest]}, "
          f"root Ø{SCREW_ROOT_DIA}, {critical_rpm(s[longest]) * 5 / 1000:.1f} m/min at lead 5)")

    assert s["x_travel"] >= max(WORK_X, s["rack_row_span"]) + 2 * TOOL_RADIUS
    assert s["y_travel"] >= Y_WORK_TRAVEL + s["rack_y_depth"]
    assert s["nose_min"] == 25 and s["nose_max"] == 225
    assert s["holder_top_max"] == s["nose_max"] - CLEAR - s["tool_max"]
    if HOLDER_STACK is not None:
        assert s["holder_top_min"] >= s["nose_min"] + HOLDER_STACK
        assert s["holder_top_min"] <= s["holder_top_max"], "no rack height works"
    # back row reached over the front row: carried holder clears the front holders
    assert ROW_PITCH_Y >= ENTRY_STROKE + HOLDER_FLANGE_DIA + CLEAR, "rows too close for the entry slide"
    for k in ("x_rail", "y_rail", "z_rail"):
        assert s[k] in LIMO_RAIL_SET, k
    custom = []
    for k in ("x_screw", "y_screw", "z_screw"):
        assert LIMO_CUSTOM[0] <= s[k] <= LIMO_CUSTOM[1], k
        if s[k] not in LIMO_SCREW_C5:
            custom.append(f"{k} {s[k]}")
    print("screws by custom length:", ", ".join(custom) or "none")
    # nut and blocks fit on the carriages
    assert NUT_LEN <= Y_CARRIAGE, "DFU1605 longer than the Y roller"
    assert s["frame_inner_x"] >= WORK_X + 2 * TOOL_RADIUS, "bed does not fit between Y tubes"
    if HOLDER_STACK is None:
        print("INCOMPLETE: all other checks pass; holder_top_min waits for the ISO20 holder STEP")
        raise SystemExit(2)
    print("PASS")

"""V4 sizing script (fixed gantry, moving table). All lengths in mm.

One place for the V4 lengths. The BOM and the Fusion model tasks read sizes().
Run: PYTHONUTF8=1 python tools/v4_sizes.py
Sources for every input are in docs/v4-sizes.md.
"""
import math

# ---- Inputs ------------------------------------------------------------
WORK_X = 430             # work travel of the spindle axis in X (D-233: X slider 430)
WORK_Y_AREA = 250        # work area Y (design doc; D-79)
Z_TRAVEL = 150           # Z travel (design doc; D-267: nose 25 to 175 above table)
TABLE_X = 460            # table width (design doc, about 460)
TABLE_Y = 330            # table length (D-233: fixture plate Y 330)
TOOL_MARGIN = 15         # tool radius allowed past each end of axis travel (estimate)
CARRIAGE_LEN = 77.5      # HGH20CA block length (D-150)
BLOCK_PITCH = 100        # two blocks on one rail, centre to centre (D-150)
RAIL_END = 20            # spare rail past the blocks (D-150)
SCREW_EXTRA = 253        # screw length minus travel: 653 - 400 (D-150); covers nut,
                         # BK12 and BF12 ends
BK12_LEN = 25            # BK12 support body length (estimate; check LiMo drawing)
BF12_LEN = 20            # BF12 support body length (estimate; check LiMo drawing)
SCREW_ROOT_DIA = 13.2    # DFU1605 root diameter (typical 1605 screw, estimate)
Z_RAIL = 350             # v3 Z rail set, 2 x 350 (D-136)
Z_SCREW = 350            # v3 Z screw, 350 (D-136; HM12-60 mount, D-207)
UPRIGHT_W = 50           # steel upright U2 flat bar 50 x 150, 50 in X (D-309)
UPRIGHT_GAP = 40         # table edge (230) to upright inner face = tray end plate outer face (270):
                         # tray 500 + 2 x 20 end plates (D-308, V4 model Task 4)
WHEEL_PICKUP_OFFSET = 85  # right upright outer face to pickup, X (estimate, fixed in Task 6)
BASE_END_MARGIN = 20     # base past the table's Y travel, each end (estimate)
BEAM_END_MARGIN = 20     # beam past the X rail, each end (estimate)

# Derived: reach from the table's +X edge region to the wheel pickup (named
# constant, as ruled). Spindle axis at end of work travel is at +215 (WORK_X/2).
WHEEL_REACH = (TABLE_X / 2 + UPRIGHT_GAP + UPRIGHT_W + WHEEL_PICKUP_OFFSET) - WORK_X / 2

# LiMo listing, read by curl on 2026-11-24 (https://limobearing.com/, Zyro site:
# no products.json or WooCommerce API, so the product pages were read).
LIMO_RAIL_SET = list(range(200, 901, 50)) + [1000, 1100, 1200, 1300, 1400,
                                              1500, 1600, 1700, 1800, 2000]
LIMO_SCREW_STD = [300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1500, 1800, 2000]
LIMO_SCREW_CUSTOM = (10, 4000)   # "Custom lengths 10-4,000 mm"; we order 50 mm steps (D-136)
SCREW_STEP = 50

# ---- Helpers -----------------------------------------------------------
def up(x, steps):
    return min(s for s in steps if s >= x)

def up_step(x, step=SCREW_STEP):
    return int(math.ceil(x / step) * step)

def rail_len(travel):
    return up(travel + BLOCK_PITCH + CARRIAGE_LEN + RAIL_END, LIMO_RAIL_SET)

def screw_len(travel):
    return up_step(travel + SCREW_EXTRA)

def critical_rpm(length, dia=SCREW_ROOT_DIA, k=3.927, safety=0.8):
    """Whip speed, fixed-supported ends (BK12 fixed, BF12 supported), steel, root dia."""
    E, rho = 206e9, 7850.0
    L, d = length / 1000.0, dia / 1000.0
    w = (k / L) ** 2 * (d / 4.0) * math.sqrt(E / rho)
    return safety * w * 60 / (2 * math.pi)

def sizes():
    x_travel = WORK_X + WHEEL_REACH
    y_travel = TABLE_Y - 2 * TOOL_MARGIN      # 300: axis range plus tool margin covers the table
    x_rail, x_screw = rail_len(x_travel), screw_len(x_travel)
    y_rail, y_screw = rail_len(y_travel), screw_len(y_travel)
    base_width = TABLE_X + 2 * (UPRIGHT_GAP + UPRIGHT_W)
    beam_len = x_rail + 2 * BEAM_END_MARGIN
    # X rail placed centred on the span the 2 blocks sweep over the whole travel
    # (spindle axis from -WORK_X/2 to -WORK_X/2 + x_travel, blocks centred on it);
    # the beam is the rail plus BEAM_END_MARGIN at each end.
    block_half = BLOCK_PITCH / 2 + CARRIAGE_LEN / 2
    sweep_min = -WORK_X / 2 - block_half
    sweep_max = -WORK_X / 2 + x_travel + block_half
    rail_x0 = (sweep_min + sweep_max) / 2 - x_rail / 2
    beam_x0 = rail_x0 - BEAM_END_MARGIN
    return dict(
        x_travel=x_travel, y_travel=y_travel, z_travel=Z_TRAVEL,
        x_rail=x_rail, x_screw=x_screw, y_rail=y_rail, y_screw=y_screw,
        z_rail=Z_RAIL, z_screw=Z_SCREW,
        beam_len=beam_len,
        base_len=TABLE_Y + y_travel + 2 * BASE_END_MARGIN,
        base_width=base_width,
        x_rail_x0=rail_x0, x_rail_x1=rail_x0 + x_rail,
        beam_x0=beam_x0, beam_x1=beam_x0 + beam_len,
        beam_overhang_left=-base_width / 2 - beam_x0,   # past the left upright's outer face
        beam_overhang_right=beam_x0 + beam_len - base_width / 2,
        block_sweep_min=sweep_min, block_sweep_max=sweep_max,
    )

if __name__ == "__main__":
    s = sizes()
    for k, v in s.items():
        print(f"{k:22s}{v:8g}")
    print(f"{'wheel_reach':22s}{WHEEL_REACH:8g}")
    n = critical_rpm(s["x_screw"])
    print(f"{'x_screw_whip_rpm_80%':22s}{n:8.0f}")

    # Geometry in table-centre X. Spindle axis starts at -WORK_X/2 (left end of work travel).
    axis_min = -WORK_X / 2
    axis_max = axis_min + s["x_travel"]
    pickup_x = TABLE_X / 2 + UPRIGHT_GAP + UPRIGHT_W + WHEEL_PICKUP_OFFSET
    assert axis_max >= pickup_x, "spindle does not reach the wheel pickup"
    assert axis_min - TOOL_MARGIN <= -TABLE_X / 2, "X misses table -230"
    assert axis_min + WORK_X + TOOL_MARGIN >= TABLE_X / 2, "X misses table +230"
    # Y: axis range 0 to y_travel in table coordinates, tool margin each end
    assert s["y_travel"] >= WORK_Y_AREA, "Y work area 250 not covered"
    assert s["y_travel"] + 2 * TOOL_MARGIN >= TABLE_Y, "Y misses table 0 to 330"
    for k in ("x_rail", "y_rail", "z_rail"):
        assert s[k] in LIMO_RAIL_SET, k
    custom = []
    for k in ("x_screw", "y_screw", "z_screw"):
        assert LIMO_SCREW_CUSTOM[0] <= s[k] <= LIMO_SCREW_CUSTOM[1], k
        if s[k] not in LIMO_SCREW_STD:
            custom.append(f"{k} {s[k]}")
    print("screws by custom length (not a standard LiMo size):", ", ".join(custom) or "none")
    assert s["x_screw"] <= 1000, "1605 whip"
    # Consistency check (true by construction of rail_len): Z rail holds Z travel plus blocks.
    assert s["z_rail"] >= Z_TRAVEL + BLOCK_PITCH + CARRIAGE_LEN + RAIL_END
    # Assumes the Y screw lies along the base, with BK12 and BF12 outside its ends.
    assert s["base_len"] >= s["y_screw"] + BK12_LEN + BF12_LEN
    assert s["beam_overhang_right"] > 0
    # The blocks stay on the X rail at both ends of the travel.
    assert s["x_rail_x0"] <= s["block_sweep_min"] and s["x_rail_x1"] >= s["block_sweep_max"]
    print("PASS")

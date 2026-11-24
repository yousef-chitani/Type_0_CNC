"""V4 ATC wheel fit (Task 6, D-314): how high the wheel may sit under the X carriage.

The wheel turns in the Y-Z plane (axis along X) at the pickup X, centred at Y 0
under the spindle. Its holders sweep a disc of radius R_SWEEP. Every carriage
part that passes over the wheel's X slab must stay outside that disc (plus a
margin) at every pickup pose. Inputs are from the V4 model (24 Nov 2026) and the
v3 wheel (D-302, D-304). Run: PYTHONUTF8=1 python tools/v4_wheel_fit.py
"""
import math

# v3 wheel, as copied (mm)
R_HOLDER_END = 196.0       # holder pull-stud end radius (v3 holder 0 deg: Z 61 to 156, centre Z -40)
HOLDER_HALF_W = 22.5       # Ø45 flange
R_SWEEP = math.hypot(R_HOLDER_END, HOLDER_HALF_W)  # corner of the flange
NOSE_ABOVE_CENTRE = 152.0  # v3: nose 112 at pickup, centre -40
HOLDER_ABOVE_NOSE = R_HOLDER_END - NOSE_ABOVE_CENTRE  # taper length in the spindle (44)
LIFT = 50.0                # spindle rise to clear the holder (44 + 6)
MARGIN = 3.0

# V4 machine (model, 24 Nov 2026)
NOSE_MAX = 175.0           # nose at z_pos +75
TRAY_BOTTOM = -168.0       # bottom sheet underside
HUB_R = 51.0               # D-304 hub radius in the holder plane

# Fixed carriage parts lowest edge in the wheel's X slab: Z rails and risers
# (Y 87.5 to 140, bottom Z 99, they ride with X, not with Z).
FIXED = [("Z rails / risers / fixed plate", 87.5, 99.0)]


def max_centre(y_near, z_bottom):
    """Highest wheel centre Z that keeps a part edge at (y_near, z_bottom) outside the sweep."""
    r = R_SWEEP + MARGIN
    if y_near >= r:
        return float("inf")
    return z_bottom - math.sqrt(r * r - y_near * y_near)


def main():
    zc = min(max_centre(y, z) for _, y, z in FIXED)
    nose_pick = zc + NOSE_ABOVE_CENTRE
    # Z limits of the spindle
    nose_pick_max_lift = NOSE_MAX - LIFT
    bottom = zc - R_SWEEP
    longest_tool = NOSE_ABOVE_CENTRE - HUB_R  # nose to the hub radius, along the pocket
    print(f"sweep radius            {R_SWEEP:6.1f}")
    print(f"highest wheel centre Z  {zc:6.1f}")
    print(f"nose at pickup <=       {nose_pick:6.1f}  (lift limit {nose_pick_max_lift:.1f})")
    print(f"wheel bottom Z          {bottom:6.1f}  ({TRAY_BOTTOM - bottom:.1f} below the tray bottom)")
    print(f"longest tool below nose {longest_tool:6.1f}  (tip at the hub, r {HUB_R:.0f})")
    assert nose_pick <= nose_pick_max_lift, "lift does not fit in Z travel"
    assert nose_pick >= 25.0, "pickup below the lowest nose position"


if __name__ == "__main__":
    main()

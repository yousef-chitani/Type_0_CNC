"""Step-by-step assembly pictures from the CadQuery model (for docs/assembly-steps.md).

Run: python cad/v2/render_steps.py   (about 3-4 minutes; add --envelopes to skip the vendor models)
Writes cad/v2/out/assembly/steps/step_NN.png: left = whole machine, right = close-up.
Parts fitted in earlier steps are pale grey; the parts fitted in this step are orange.
"""
import pathlib, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import assembly as A
from render_views import mesh, shaded

OUT = pathlib.Path(__file__).parent / "out" / "assembly" / "steps"
OLD = (0.86, 0.86, 0.86, 0.30)
NEW = (0.95, 0.55, 0.15)          # every part fitted in this step

# (title, part-name prefixes, view (elev, azim), labels [(part, text)])
STEPS = [
    ("Base on its 3 pads (seen from below)", ["base_casting", "base_insert", "pad_"], (-30, 20),
     [("pad_front", "3 steel pads: level the base top with shims")]),
    ("Y rails on their poured seats", ["Y_rail_"], (28, -58),
     [("Y_rail_L", "reference rail: straight to the straightedge"), ("Y_rail_R", "second rail: parallel, dial on a block")]),
    ("Y carriages and table", ["Y_block_", "table"], (28, -58),
     [("table", "bolt the table to 4 blocks; check it slides freely")]),
    ("Y ballscrew", ["Y_BK12", "Y_BF12", "Y_ballscrew", "Y_nut", "Y_nut_housing"], (28, 122),
     [("Y_BK12", "BK12 fixed end"), ("Y_BF12", "BF12 free end"), ("Y_nut_housing", "nut housing bolts under the table")]),
    ("Y motor and belt", ["Y_pulley", "Y_motor", "Y_belt"], (15, -40),
     [("Y_motor", "slide the motor plate to tension the belt")]),
    ("Portal on the base", ["portal_casting", "portal_insert_X", "portal_insert_Xmotor"], (22, -58),
     [("portal_casting", "lower over 4 M12 rods, bolt dry; shim any rocking foot")]),
    ("X rails on the beam", ["X_rail_"], (22, -58),
     [("X_rail_T", "reference rail: straight to the straightedge"), ("X_rail_B", "second rail: parallel, dial on a block")]),
    ("X carriages and saddle", ["X_block_", "saddle"], (22, -58),
     [("saddle", "saddle on 4 blocks; now square X to Y")]),
    ("X ballscrew", ["X_BK12", "X_BF12", "X_ballscrew", "X_nut", "X_nut_housing", "X_housing_spacer"], (22, 122),
     [("X_nut_housing", "housing on a 25 mm spacer, behind the saddle")]),
    ("X motor and belt", ["X_pulley", "X_motor", "X_belt", "X_bracket", "X_outboard_bearing"], (22, -30),
     [("X_motor", "motor on the beam top: slide to tension"), ("X_outboard_bearing", "outboard bearing")]),
    ("Z rails on risers", ["Z_riser_", "Z_rail_"], (22, -58),
     [("Z_rail_R", "rails on 15 mm risers: parallel and plumb")]),
    ("Z plate, screw and motor", ["Z_block_", "Z_plate", "Z_nut", "Z_BK12", "Z_ballscrew", "Z_coupling", "Z_motor"], (22, -58),
     [("Z_motor", "brake motor, direct on the screw"), ("Z_plate", "Z plate on 4 blocks")]),
    ("Spindle", ["spindle_clamp", "spindle"], (22, -58),
     [("spindle", "tram: square the spindle to the table")]),
    ("Home sensors", ["home_sensor_"], (22, -58),
     [("home_sensor_X", "X"), ("home_sensor_Y", "Y"), ("home_sensor_Z", "Z")]),
]


def pads():
    """The 3 steel pads under the base (D-119), indicative positions: they are not in assembly.py."""
    h, sw, D = A.h, A.sw, A.D
    yc = (D["foot_y0"] + D["foot_y1"]) / 2
    out = {}
    for nm, (x, y) in {"pad_left": (-sw / 2 + 25, yc), "pad_right": (sw / 2 - 25, yc), "pad_front": (0, D["spine_y0"] + 40)}.items():
        out[nm] = (A.box(x - 30, x + 30, y - 20, y + 20, -h - 10, -h), (0.55, 0.35, 0.25))
    return out


def owner(name):
    for i, (_, prefixes, _, _) in enumerate(STEPS):
        if any(name.startswith(p) for p in prefixes):
            return i
    return None


def draw(ax, parts, lo, hi, elev, azim, zoom=1.2):
    allt = np.concatenate([t for t, _ in parts]); cols = np.concatenate([c for _, c in parts])
    ax.add_collection3d(Poly3DCollection(allt, facecolors=cols, edgecolors=cols, linewidths=0.15))
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1]); ax.set_zlim(lo[2], hi[2])
    ax.set_box_aspect(hi - lo, zoom=zoom)
    ax.set_proj_type("ortho"); ax.view_init(elev=elev, azim=azim); ax.set_axis_off()


if __name__ == "__main__":
    A.INSERTS.clear(); A.FEATURES.clear()
    C = A.build()
    C.update(pads())
    C.pop("ATC_wheel_envelope", None)      # Phase 2
    C.pop("portal_insert_ATC", None)       # Phase 2
    M = {}
    for n, v in C.items():
        if v is None:
            continue
        t = mesh(v[0])
        if len(t):
            M[n] = (t, v[1])
    lost = [n for n in M if owner(n) is None]
    if lost:
        print("not in any step:", lost)
    allp = np.concatenate([t for t, _ in M.values()]).reshape(-1, 3)
    glo, ghi = allp.min(0), allp.max(0)
    OUT.mkdir(parents=True, exist_ok=True)
    for i, (title, _, (el, az), labels) in enumerate(STEPS):
        new = {n: v for n, v in M.items() if owner(n) == i}
        old = {n: v for n, v in M.items() if owner(n) is not None and owner(n) < i}
        parts = [(t, np.tile(OLD, (len(t), 1))) for t, _ in old.values()] + [(t, shaded(t, (0.2, 0.2, 0.2) if n.startswith("pad_") else NEW)) for n, (t, c) in new.items()]
        fig = plt.figure(figsize=(16, 8))
        fig.suptitle(f"Step {i + 1}: {title}", fontsize=16, x=0.02, ha="left")
        ax = fig.add_subplot(1, 2, 1, projection="3d")
        draw(ax, parts, glo, ghi, el, az, zoom=1.3)
        ax.set_title("whole machine (grey = already fitted, orange = this step)", fontsize=10)
        npts = np.concatenate([t for t, _ in new.values()]).reshape(-1, 3)
        c, r = (npts.min(0) + npts.max(0)) / 2, (npts.max(0) - npts.min(0)).max() / 2 * 1.25 + 30
        lo, hi = c - r, c + r
        # close-up: keep only triangles near the new parts so the box clips cleanly
        near = []
        for t, col in parts:
            keep = ((t >= lo - 1) & (t <= hi + 1)).all(axis=2).all(axis=1)
            if keep.any():
                near.append((t[keep], col[keep]))
        ax2 = fig.add_subplot(1, 2, 2, projection="3d")
        draw(ax2, near, lo, hi, el, az)
        ax2.set_title("close-up", fontsize=10)
        for part, text in labels:
            if part in M:
                p = M[part][0].reshape(-1, 3)
                q = (p.min(0) + p.max(0)) / 2; q[2] = p.max(0)[2] + 15
                ax2.text(*q, text, fontsize=10, color="black", zorder=50,
                         bbox=dict(boxstyle="round,pad=0.25", fc="#fff8d0", ec="#c9a227", lw=0.8))
        fig.subplots_adjust(left=0.0, right=1.0, top=0.9, bottom=0.0, wspace=0.0)
        fig.savefig(OUT / f"step_{i + 1:02d}.png", dpi=90); plt.close(fig)
        print("step", i + 1, title, len(new), "parts")
    print("written to", OUT)

"""V4 upright joints as rotation springs (task 28, D-321): how much the nose loses when the
upright foot joint (upright to end plate to tray) and the top joint (beam on the upright top edge)
are not rigid. Springs act about global Y only (X sway); all else as v4_frame_stiffness.py.
Run: PYTHONUTF8=1 python tools/v4_joint_sweep.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
K = {"foot": None, "top": None}
import v4_frame_stiffness as T  # noqa: E402
_build = T.build
def spring(k):
    s = dict(T.LINK); s["EIz"] = k * 1.0; return s
def build(*a, **kw):
    fr, nose, part, ups, bn, car = _build(*a, **kw)
    add = []
    for u in ups:
        p, q, props, ref = fr.elems[u - 1]          # tray node -> foot (LINK)
        if K["foot"]:
            x, y, z = fr.nodes[q]; j = fr.node(x, y, z - 1.0, new=True)
            fr.elems[u - 1] = (p, j, T.LINK, T.Z_); add.append((j, q, spring(K["foot"]), T.X_))
        p, q, props, ref = fr.elems[u + 1]          # upright top -> beam centre (LINK)
        if K["top"]:
            x, y, z = fr.nodes[p]; j = fr.node(x, y, z + 1.0, new=True)
            fr.elems[u + 1] = (j, q, T.LINK, ref); add.append((p, j, spring(K["top"]), T.X_))
    fr.elems.extend(add)
    return fr, nose, part, ups, bn, car
T.build = build
def run(label):
    row = []
    for second, x in (("table", 0.0), ("wheel", T.PICKUP_X)):
        for d in (0, 2):
            h = T.compliance("B", "U2 plate 50x150", True, d, x_load=x, second=second)[0]
            l = T.compliance("B", "U2 plate 50x150", False, d, x_load=x, second=second)[0]
            row.append(f"{h:5.1f}/{l:<5.1f}")
    print(f"{label:32s} | {' '.join(row[:2])} | {' '.join(row[2:])}")
print(f"{'joints (N mm/rad)':32s} | table X, Z         | wheel X, Z")
run("both rigid (tool as is)")
for k in (1e10, 3e9, 1e9, 3e8):
    K.update(foot=None, top=k); run(f"top {k:.0e}, foot rigid")
for k in (3e9, 1e9):
    K.update(foot=k, top=k); run(f"top {k:.0e}, foot {k:.0e}")

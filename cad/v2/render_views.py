"""Render the assembly views (PNG) with matplotlib from the CadQuery model.

Run after assembly.py: python cad/v2/render_views.py  (about 3 minutes)
Writes cad/v2/out/assembly/assembly_{iso,iso_back,front,side,top}.png and castings_tapers.png.
The CadQuery SVG exporter gives rotated views, so the shapes are tessellated and drawn as shaded triangles.
"""
import pathlib, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import assembly as A

OUT = pathlib.Path(__file__).parent / "out" / "assembly"
LIGHT = np.array([-0.45, -0.6, 0.66])

def mesh(shape, tol=1.5):
    """Triangles (n, 3, 3) of a CadQuery workplane, coarse enough for a picture."""
    tris = []
    for s in shape.vals():
        v, t = s.tessellate(tol, 0.5)
        if not t:
            continue
        p = np.array([(q.x, q.y, q.z) for q in v])
        tris.append(p[np.array(t)])
    return np.concatenate(tris) if tris else np.zeros((0, 3, 3))

def shaded(tris, col):
    n = np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0])
    n /= np.maximum(np.linalg.norm(n, axis=1, keepdims=True), 1e-9)
    k = 0.55 + 0.45 * np.abs(n @ LIGHT)
    c = np.ones((len(tris), 4)); c[:, :3] = np.clip(np.array(col[:3])[None, :] * k[:, None], 0, 1)
    return c

def draw(ax, parts, elev, azim, title):
    allt = np.concatenate([t for t, _ in parts]); cols = np.concatenate([c for _, c in parts])
    ax.add_collection3d(Poly3DCollection(allt, facecolors=cols, edgecolors=cols, linewidths=0.2))
    lo, hi = allt.reshape(-1, 3).min(0), allt.reshape(-1, 3).max(0)
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1]); ax.set_zlim(lo[2], hi[2])
    ax.set_box_aspect(hi - lo, zoom=1.15)
    ax.set_proj_type("ortho"); ax.view_init(elev=elev, azim=azim); ax.set_axis_off(); ax.set_title(title)

if __name__ == "__main__":
    A.INSERTS.clear(); A.FEATURES.clear()
    C = A.build()
    parts = {n: (mesh(shp), col) for n, (shp, col) in C.items()}
    parts = {n: (t, shaded(t, col)) for n, (t, col) in parts.items() if len(t)}
    views = {"iso": (22, -58), "iso_back": (22, 122), "front": (0, -90), "side": (0, 180), "top": (90, -90)}
    for nm, (el, az) in views.items():
        fig = plt.figure(figsize=(12.2, 9.5)); ax = fig.add_subplot(projection="3d")
        draw(ax, list(parts.values()), el, az, f"Type 0 assembly: {nm.replace('_', ' ')}")
        fig.savefig(OUT / f"assembly_{nm}.png", dpi=100); plt.close(fig)
    fig = plt.figure(figsize=(16, 7))
    for i, (key, el, az, ttl) in enumerate((("portal_casting", 20, -60, "portal front-left"), ("portal_casting", 20, 125, "portal back-right"),
                                            ("base_casting", 50, -60, "base from above"))):
        ax = fig.add_subplot(1, 3, i + 1, projection="3d")
        t = mesh(C[key][0], 0.5)
        draw(ax, [(t, shaded(t, (0.62, 0.62, 0.58)))], el, az, ttl)
    fig.savefig(OUT / "castings_tapers.png", dpi=100); plt.close(fig)
    print("views written to", OUT)

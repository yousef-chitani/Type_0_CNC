"""Z fixed plate stiffness (D-184): how far the tool moves because the plate bends.

Plate finite element model (Mindlin, 4-node, selective integration). The plate is
150 wide x 350 high, bolted to the X rollers. Sizes are from Type_0_v3 (18 Nov 2026).
Only the plate (and optionally the rails and risers on it) bends. Rollers, screws,
blocks, moving plate, clamp and spindle are treated as rigid.

Run: python tools/z_plate_stiffness.py
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

FORCE = 200.0            # N at the tool, same as docs/beam-assessment.md
W, Z0, Z1 = 150.0, 169.0, 519.0
RAIL_X = 50.0            # rails at X +/- 50
BLOCK_PITCH = 90.0
BLOCK_LEN = 77.5
LOW_BLOCK_ABOVE_NOSE = 115.0   # lower block centre above the spindle nose
STICKOUT = 50.0          # tool tip below the nose (assumed)
STACK = 125.0            # plate front face to spindle axis: 15 riser, 30 block, 20 plate, 60 clamp
BOLTS = [(x, z) for z in (181.5, 205.5, 372.0, 396.0) for x in (-32.0, 32.0)] + [(0.0, 181.5)]
NOSES = (100.0, 250.0)   # nose Z at the bottom and top of the 150 travel

ALU = dict(name="6082", E=70e3, nu=0.33, rho=2.70e-6)
STEEL = dict(name="Steel", E=205e3, nu=0.30, rho=7.85e-6)
# Bending stiffness of one rail and one riser, added without any composite action.
RAIL_I = 0.75 * 20 * 17.5**3 / 12     # HGR20, 25 % off a solid bar for the holes and grooves (estimate)
RISER_I = 25 * 15**3 / 12


def grid(lo, hi, keys, step):
    pts = sorted({round(float(k), 6) for k in keys if lo <= k <= hi} | {lo, hi})
    out = [pts[0]]
    for a, b in zip(pts, pts[1:]):
        n = max(1, int(np.ceil((b - a) / step - 1e-9)))
        out += list(np.linspace(a, b, n + 1)[1:])
    return np.array(out)


def element(a, b, E, nu, t):
    """Stiffness of a rectangular element a x b. Node dofs: w, ax (dw/dx), az (dw/dz)."""
    G, k = E / (2 * (1 + nu)), 5 / 6
    D = E * t**3 / (12 * (1 - nu**2)) * np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1 - nu) / 2]])
    S = k * G * t * np.eye(2)
    sx, sz = np.array([-1, 1, 1, -1.0]), np.array([-1, -1, 1, 1.0])
    K = np.zeros((12, 12))
    jac = a * b / 4
    g = 1 / np.sqrt(3)
    for xi, eta in [(-g, -g), (g, -g), (g, g), (-g, g)]:
        dx = sx * (1 + eta * sz) / 4 * 2 / a
        dz = sz * (1 + xi * sx) / 4 * 2 / b
        B = np.zeros((3, 12))
        B[0, 1::3], B[1, 2::3], B[2, 1::3], B[2, 2::3] = dx, dz, dz, dx
        K += B.T @ D @ B * jac
    dx, dz, N = sx / 2 / a, sz / 2 / b, np.full(4, 0.25)
    B = np.zeros((2, 12))
    B[0, 0::3], B[0, 1::3], B[1, 0::3], B[1, 2::3] = dx, -N, dz, -N
    return K + B.T @ S @ B * (a * b)


class Plate:
    def __init__(self, mat, t, step=5.0, rails=False):
        self.mat, self.t = mat, t
        xk = [-W / 2, W / 2, -62.5, 62.5, 0, -32, 32, -37, -27, 27, 37, -5, 5]
        xk += [s * (RAIL_X + d) for s in (-1, 1) for d in (-12.5, 0, 12.5)]
        zk = [181.5, 205.5, 372, 396, 219, 355, 405]
        zk += [z + d for z, _ in BOLTS for d in (-5, 5)]
        for n in NOSES:
            for c in (n + LOW_BLOCK_ABOVE_NOSE, n + LOW_BLOCK_ABOVE_NOSE + BLOCK_PITCH):
                zk += [c - BLOCK_LEN / 2, c, c + BLOCK_LEN / 2]
        self.x, self.z = grid(-W / 2, W / 2, xk, step), grid(Z0, Z1, zk, step)
        self.nx, self.nz = len(self.x), len(self.z)
        self.n = self.nx * self.nz
        rows, cols, vals = [], [], []
        cache = {}
        for j in range(self.nz - 1):
            for i in range(self.nx - 1):
                a, b = self.x[i + 1] - self.x[i], self.z[j + 1] - self.z[j]
                key = (round(a, 6), round(b, 6))
                ke = cache.setdefault(key, element(a, b, mat["E"], mat["nu"], t))
                nodes = [self.id(i, j), self.id(i + 1, j), self.id(i + 1, j + 1), self.id(i, j + 1)]
                dof = np.array([[3 * m, 3 * m + 1, 3 * m + 2] for m in nodes]).ravel()
                rows.append(np.repeat(dof, 12)), cols.append(np.tile(dof, 12)), vals.append(ke.ravel())
        if rails:
            EI = STEEL["E"] * RAIL_I + ALU["E"] * RISER_I
            for xr in (-RAIL_X, RAIL_X):
                i = int(np.argmin(abs(self.x - xr)))
                for j in range(self.nz - 1):
                    L = self.z[j + 1] - self.z[j]
                    ke = EI / L**3 * np.array([[12, 6 * L, -12, 6 * L], [6 * L, 4 * L * L, -6 * L, 2 * L * L],
                                               [-12, -6 * L, 12, -6 * L], [6 * L, 2 * L * L, -6 * L, 4 * L * L]])
                    a, c = self.id(i, j), self.id(i, j + 1)
                    dof = np.array([3 * a, 3 * a + 2, 3 * c, 3 * c + 2])
                    rows.append(np.repeat(dof, 4)), cols.append(np.tile(dof, 4)), vals.append(ke.ravel())
        self.K = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                               shape=(3 * self.n, 3 * self.n))

    def id(self, i, j):
        return j * self.nx + i

    def nodes_in(self, x0, x1, z0, z1):
        e = 1e-6
        return [self.id(i, j) for j, z in enumerate(self.z) if z0 - e <= z <= z1 + e
                for i, x in enumerate(self.x) if x0 - e <= x <= x1 + e]

    def fixed(self, support):
        if support == "bolts":
            out = []
            for bx, bz in BOLTS:
                out += self.nodes_in(bx - 5, bx + 5, bz - 5, bz + 5)
        else:  # rollers: faces held flat, top roller through the 125 wide shim
            out = self.nodes_in(-W / 2, W / 2, Z0, 219) + self.nodes_in(-62.5, 62.5, 355, 405)
        return sorted(set(out))

    def patch(self, xc, zc):
        """Load shared over the rail width and block length, by tributary area."""
        nodes, weights = [], []
        x0, x1, z0, z1 = xc - 12.5, xc + 12.5, zc - BLOCK_LEN / 2, zc + BLOCK_LEN / 2
        def trib(v, k, lo, hi):
            left = max(lo, (v[k - 1] + v[k]) / 2) if k > 0 else max(lo, v[k])
            right = min(hi, (v[k] + v[k + 1]) / 2) if k < len(v) - 1 else min(hi, v[k])
            return max(0.0, right - left)
        for j in range(self.nz):
            for i in range(self.nx):
                area = trib(self.x, i, x0, x1) * trib(self.z, j, z0, z1)
                if area > 0:
                    nodes.append(self.id(i, j)), weights.append(area)
        weights = np.array(weights)
        return np.array(nodes), weights / weights.sum()

    def solve(self, support):
        fix = self.fixed(support)
        free = np.setdiff1d(np.arange(3 * self.n), [3 * m for m in fix])
        lu = spl.splu(self.K[free][:, free].tocsc())
        results = {}
        arm = STACK + self.t / 2
        for nose in NOSES:
            zl, zu = nose + LOW_BLOCK_ABOVE_NOSE, nose + LOW_BLOCK_ABOVE_NOSE + BLOCK_PITCH
            d = LOW_BLOCK_ABOVE_NOSE + STICKOUT
            # Force on each block (left low, left up, right low, right up) per 1 N at the tool
            cases = {"X": (-arm / RAIL_X / 4, -arm / RAIL_X / 4, arm / RAIL_X / 4, arm / RAIL_X / 4),
                     "Y": ((1 + d / BLOCK_PITCH) / 2, -d / BLOCK_PITCH / 2,
                           (1 + d / BLOCK_PITCH) / 2, -d / BLOCK_PITCH / 2),
                     "Z": (-arm / BLOCK_PITCH / 2, arm / BLOCK_PITCH / 2, -arm / BLOCK_PITCH / 2, arm / BLOCK_PITCH / 2)}
            spots = [(-RAIL_X, zl), (-RAIL_X, zu), (RAIL_X, zl), (RAIL_X, zu)]
            # Balance: block forces must add up to the tool force and its moments
            a, b, c, e = cases["Y"]
            assert abs(a + b + c + e - 1) < 1e-9
            assert abs((a + c) * d + (b + e) * (d + BLOCK_PITCH)) < 1e-9
            a, b, c, e = cases["X"]
            assert abs(a + b + c + e) < 1e-9 and abs((c + e - a - b) * RAIL_X - arm) < 1e-9
            a, b, c, e = cases["Z"]
            assert abs(a + b + c + e) < 1e-9 and abs((b + e) * BLOCK_PITCH - arm) < 1e-9
            patches = [self.patch(*s) for s in spots]
            for name, unit in cases.items():
                f = np.zeros(3 * self.n)
                for fi, (nodes, wt) in zip(unit, patches):
                    f[3 * nodes] += fi * FORCE * wt
                u = np.zeros(3 * self.n)
                u[free] = lu.solve(f[free])
                # Virtual work: tool movement = sum(unit block force x block movement)
                tip = sum(fi * (u[3 * nodes] * wt).sum() for fi, (nodes, wt) in zip(unit, patches))
                results[(nose, name)] = tip * 1000  # um
        return results


def check():
    """Hand check: strip on line supports at both ends, centre line load."""
    t, L, E, nu = 20.0, 350.0, ALU["E"], 0.0
    p = Plate(dict(ALU, nu=nu), t, step=2.5)
    fix = p.nodes_in(-W / 2, W / 2, Z0, Z0) + p.nodes_in(-W / 2, W / 2, Z1, Z1)
    free = np.setdiff1d(np.arange(3 * p.n), [3 * m for m in fix])
    mid = int(np.argmin(abs(p.z - (Z0 + L / 2))))
    f = np.zeros(3 * p.n)
    row = [p.id(i, mid) for i in range(p.nx)]
    wt = np.gradient(p.x)
    f[[3 * m for m in row]] = 100 * wt / wt.sum()
    u = np.zeros(3 * p.n)
    u[free] = spl.spsolve(p.K[free][:, free].tocsc(), f[free])
    fe = u[3 * p.id(p.nx // 2, mid)]
    I = W * t**3 / 12
    hand = 100 * L**3 / (48 * E * I) + 100 * L / (4 * (5 / 6) * (E / 2) * W * t)
    return fe, hand


def main():
    fe, hand = check()
    print(f"Hand check, 100 N on a 350 strip: model {fe*1000:.2f} um, hand {hand*1000:.2f} um, "
          f"difference {100*(fe/hand-1):+.2f} %")
    coarse = Plate(ALU, 20.0, step=5.0).solve("rollers")
    fine = Plate(ALU, 20.0, step=2.5).solve("rollers")
    worst = max(fine, key=fine.get)
    print(f"Mesh check, 6082 x 20, worst case {worst}: 5 mm {coarse[worst]:.2f} um, 2.5 mm {fine[worst]:.2f} um")
    options = [(ALU, 20), (ALU, 25), (ALU, 30), (STEEL, 20), (STEEL, 15), (STEEL, 12)]
    print(f"\nTool movement in um at {FORCE:.0f} N, rails and risers counted. Nose at Z 100, then Z 250")
    print("Plate       kg | supports | X low Y low Z low | X high Y high Z high")
    for mat, t in options:
        kg = mat["rho"] * W * (Z1 - Z0) * t
        for support in ("rollers", "bolts"):
            r = Plate(mat, t, step=2.5, rails=True).solve(support)
            low = " ".join(f"{r[(NOSES[0], a)]:5.1f}" for a in "XYZ")
            high = " ".join(f"{r[(NOSES[1], a)]:5.1f}" for a in "XYZ")
            print(f"{mat['name']:5} x{t:<3} {kg:5.1f} | {support:7} | {low} | {high}")


if __name__ == "__main__":
    main()

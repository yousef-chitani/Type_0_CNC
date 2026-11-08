"""Type 0 printed parts (D-100), for the owner's Bambu Lab P1S printers (256 x 256 x 256 build).

Run: python cad/v2/printed_parts.py -> cad/v2/out/print/*.stl + *.step + preview SVGs
Material and settings: docs/printed-parts.md. Sizes marked CHECK depend on parts not yet in hand.
"""
import pathlib
import cadquery as cq

OUT = pathlib.Path(__file__).parent / "out" / "print"; OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# T14: 120 mm fan grill (x2). Screws through the grill and the 12 mm side panel into the fan.
# ---------------------------------------------------------------------------
def fan_grill(size=120.0, pitch=105.0, t=3.0, hole_d=4.4, open_d=114.0, ring_w=2.4, ring_pitch=11.0, spokes=4):
    g = cq.Workplane("XY").rect(size, size).extrude(t).edges("|Z").fillet(6)
    g = g.cut(cq.Workplane("XY").circle(open_d / 2).extrude(t))            # big opening
    for r in [r for r in [ring_pitch * k for k in range(1, 7)] if r + ring_w / 2 < open_d / 2]:
        ring = cq.Workplane("XY").circle(r + ring_w / 2).circle(r - ring_w / 2).extrude(t)
        g = g.union(ring)
    for k in range(spokes):                                                  # spokes hold the rings
        g = g.union(cq.Workplane("XY").rect(open_d, ring_w).extrude(t).rotate((0, 0, 0), (0, 0, 1), 45 + 180 / spokes * k))
    g = g.union(cq.Workplane("XY").circle(7).extrude(t))                     # hub
    g = g.cut(cq.Workplane("XY").rect(pitch, pitch, forConstruction=True).vertices().circle(hole_d / 2).extrude(t))
    g = g.cut(cq.Workplane("XY").workplane(offset=t - 1.2).rect(pitch, pitch, forConstruction=True).vertices()
              .circle(4.2).extrude(1.2))                                     # shallow counterbore for pan heads
    return g

# ---------------------------------------------------------------------------
# T15: cable + hose grommet for the bench top (36 mm thick). 3 parts:
#   frame (ASA) drops into a 70 x 150 hole; membrane (TPU 95A) with slits; clamp ring (ASA)
#   held by 4 x 4 x 30 wood screws (T11) through the ring and the flange into the bench top.
#   Opening 60 x 140 for the hoses and cables.
# ---------------------------------------------------------------------------
G = dict(flange=(80.0, 160.0), hole=(70.0, 150.0), open=(60.0, 140.0), top_t=36.0, flange_t=4.0,
         sleeve_depth=30.0, recess=1.4, memb_t=1.2, ring_t=3.0, screw_clear=4.5)

def grommet_frame():
    fw, fl = G["flange"]; hw, hl = G["hole"]; ow, ol = G["open"]
    f = cq.Workplane("XY").rect(fw, fl).extrude(G["flange_t"]).edges("|Z").fillet(8)
    sleeve = cq.Workplane("XY").rect(hw - 0.6, hl - 0.6).extrude(-G["sleeve_depth"]).edges("|Z").fillet(5)
    f = f.union(sleeve)
    f = f.cut(cq.Workplane("XY").workplane(offset=-G["sleeve_depth"]).rect(ow, ol).extrude(G["sleeve_depth"] + G["flange_t"]))
    f = f.cut(cq.Workplane("XY").workplane(offset=G["flange_t"] - G["recess"]).rect(ow + 8, ol + 8).extrude(G["recess"]))
    f = f.cut(cq.Workplane("XY").rect(fw - 8, fl - 8, forConstruction=True).vertices().circle(G["screw_clear"] / 2)
              .extrude(G["flange_t"]))
    return f

def grommet_membrane():
    ow, ol = G["open"]
    m = cq.Workplane("XY").rect(ow + 7.6, ol + 7.6).extrude(G["memb_t"])
    m = m.cut(cq.Workplane("XY").rect(1.0, ol - 10).extrude(G["memb_t"]))                       # long slit
    for y in range(-60, 61, 15):                                                                 # cross slits
        m = m.cut(cq.Workplane("XY").center(0, y).rect(ow - 10, 1.0).extrude(G["memb_t"]))
    return m

def grommet_ring():
    fw, fl = G["flange"]; ow, ol = G["open"]
    r = cq.Workplane("XY").rect(fw, fl).extrude(G["ring_t"]).edges("|Z").fillet(8)
    r = r.cut(cq.Workplane("XY").rect(ow, ol).extrude(G["ring_t"]).edges("|Z").fillet(3))
    r = r.cut(cq.Workplane("XY").rect(fw - 8, fl - 8, forConstruction=True).vertices().circle(G["screw_clear"] / 2).extrude(G["ring_t"]))
    return r

# ---------------------------------------------------------------------------
# Bench front e-stop box (D-91): XB2-BS544 (E08) in a yellow ASA box on the front apron.
#   Body: open front, 4 screw bosses, cable entry for an M20 gland in the bottom, 2 wood-screw
#   holes in the back. Lid: 4 mm plate with a 22.5 mm hole (+ anti-turn notch).
#   Inside 70 x 70 x 75 deep: CHECK the depth behind the panel on the button that arrives.
# ---------------------------------------------------------------------------
E = dict(inner=(70.0, 70.0), depth=75.0, wall=3.0, lid_t=4.0, hole_d=22.5, notch=(3.2, 4.2),
         boss_d=9.0, pilot=3.2, clear=4.5, gland_d=20.5, mount_d=4.5)   # 4 x 30 wood screws (T11)

def estop_body():
    iw, ih = E["inner"]; w = E["wall"]; d = E["depth"]
    ow, oh = iw + 2 * w, ih + 2 * w
    b = cq.Workplane("XY").rect(ow, oh).extrude(d + w).edges("|Z").fillet(4)        # back at z=0, open at the top (front)
    b = b.cut(cq.Workplane("XY").workplane(offset=w).rect(iw, ih).extrude(d + 1).edges("|Z").fillet(2))
    off = iw / 2 - E["boss_d"] / 2 + 0.5
    for sx in (-1, 1):
        for sy in (-1, 1):
            boss = cq.Workplane("XY").center(sx * off, sy * off).circle(E["boss_d"] / 2).extrude(d + w)
            b = b.union(boss)
            b = b.cut(cq.Workplane("XY").workplane(offset=w + d - 28).center(sx * off, sy * off).circle(E["pilot"] / 2).extrude(29))
    # cable entry in the bottom wall (y = -oh/2), centred in depth
    b = b.cut(cq.Workplane("XZ").workplane(offset=oh / 2 - 0.01).center(0, w + d / 2).circle(E["gland_d"] / 2).extrude(w + 1))
    # 2 mounting holes in the back, countersunk from inside
    for y in (-18, 18):
        b = b.cut(cq.Workplane("XY").center(0, y).circle(E["mount_d"] / 2).extrude(w))
        b = b.cut(cq.Workplane("XY").workplane(offset=w - 1.5).center(0, y).circle(4.5).extrude(1.5))
    return b

def estop_lid():
    iw, ih = E["inner"]; w = E["wall"]
    ow, oh = iw + 2 * w, ih + 2 * w
    l = cq.Workplane("XY").rect(ow, oh).extrude(E["lid_t"]).edges("|Z").fillet(4)
    l = l.cut(cq.Workplane("XY").circle(E["hole_d"] / 2).extrude(E["lid_t"]))
    nw, nd = E["notch"]
    l = l.cut(cq.Workplane("XY").center(0, E["hole_d"] / 2 + nd / 2 - 1).rect(nw, nd).extrude(E["lid_t"]))
    off = iw / 2 - E["boss_d"] / 2 + 0.5
    l = l.cut(cq.Workplane("XY").rect(2 * off, 2 * off, forConstruction=True).vertices().circle(E["clear"] / 2).extrude(E["lid_t"]))
    # raised legend frame (print "E-STOP" by hand or add text in the slicer)
    return l

PARTS = {
    "T14_fan_grill_120": (fan_grill, "ASA or PETG", 2),
    "T15_grommet_frame": (grommet_frame, "ASA", 1),
    "T15_grommet_membrane": (grommet_membrane, "TPU 95A", 1),
    "T15_grommet_ring": (grommet_ring, "ASA", 1),
    "E26_estop_box_body": (estop_body, "ASA, yellow", 1),
    "E26_estop_box_lid": (estop_lid, "ASA, yellow", 1),
}

def bbox(shape):
    bb = shape.val().BoundingBox(); return bb.xlen, bb.ylen, bb.zlen

if __name__ == "__main__":
    for name, (fn, mat, qty) in PARTS.items():
        s = fn()
        cq.exporters.export(s, str(OUT / f"{name}.stl"), tolerance=0.05, angularTolerance=0.1)
        cq.exporters.export(s, str(OUT / f"{name}.step"))
        cq.exporters.export(s, str(OUT / f"{name}.svg"),
                            opt={"width": 420, "height": 320, "projectionDir": (1, -1.2, 1.4), "showHidden": False})
        x, y, z = bbox(s); vol = s.val().Volume() / 1000
        print(f"{name}: {x:.0f} x {y:.0f} x {z:.0f} mm, {vol:.1f} cm3, {mat}, qty {qty}")

"""Build exact parts for Type_0_v3 from the vendor STEP files.

HGR20 rail: cross-section taken from the HIWIN rail stub in cad/vendor/hgh20ca_block.step.
Native frame: rail top at Y 0, base at Y -17.5, length along +Z from 0.
Output: cad/v2/out/fusion_parts/
"""
import cadquery as cq
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "cad/v2/out/fusion_parts"
OUT.mkdir(parents=True, exist_ok=True)


def rail(length, pitch=60.0):
    stub = cq.importers.importStep(str(ROOT / "cad/vendor/hgh20ca_block.step")).solids().vals()[1]
    # Slice between the bolt holes (holes at Z 0 and +-60, mark at Z -30.25).
    cutter = cq.Solid.makeBox(40, 40, 1.0, cq.Vector(-20, -30, -15.5))
    slice_ = stub.intersect(cutter)
    faces = [f for f in slice_.Faces() if abs(f.Center().z + 15.5) < 1e-6]
    section = faces[0].translate(cq.Vector(0, 0, 15.5))  # start the rail at Z 0
    body = cq.Solid.extrudeLinear(section, cq.Vector(0, 0, length))
    count = int((length - 14) // pitch) + 1
    start = (length - (count - 1) * pitch) / 2
    r = cq.Workplane("XY").add(body)
    for i in range(count):
        z = start + i * pitch
        through = cq.Solid.makeCylinder(3.0, 20, cq.Vector(0, -18.5, z), cq.Vector(0, 1, 0))
        cbore = cq.Solid.makeCylinder(4.75, 9.5, cq.Vector(0, -8.5, z), cq.Vector(0, 1, 0))
        r = r.cut(cq.Workplane("XY").add(through)).cut(cq.Workplane("XY").add(cbore))
    return r, count, start


def main():
    r, count, start = rail(350.0)
    s = r.val()
    b = s.BoundingBox()
    print(f"HGR20 x 350: {b.xlen:.2f} x {b.ylen:.2f} x {b.zlen:.2f}, valid {s.isValid()}, "
          f"{count} holes, first at {start}, {s.Volume()/1000:.1f} cm3")
    cq.exporters.export(r, str(OUT / "hgr20_350.step"))
    c = (cq.Workplane("XY").circle(12.5).circle(5.0).extrude(35.0))
    cq.exporters.export(c, str(OUT / "coupling_d25l35_standin.step"))


if __name__ == "__main__":
    main()

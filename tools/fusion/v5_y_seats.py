# Y rail seats (V5 plan Task 7, bundle E2): the cured epoxy seat under each Y HGR20, as bodies.
# Run through fusion_mcp_execute (not read-only) after v5_y1_place.py / v5_y2_place.py /
# v5_roller_screws.py; then v5_check_task4.py. Re-running drops the component and rebuilds it.
# Footprint D-372: 30 wide centred on the rail, over the rail length; thickness D-363 (3, the
# YRailSeat offset): from the Y tube top up to the rail underside, both read from the model.
# Holes: the rail's Ø6 through holes carried down through the seat (the M5 rail screws pass
# through it into the tapped tube wall). Prints gross / net volume per seat (resin from gross).
# The name avoids the check's SKIP list ('M5', 'M6', ...), so the check sees the seats.
import adsk.core, adsk.fusion

NAME = 'Y Rail Seats (epoxy, 30 wide)'
WIDTH = 30.0
TUBE_TOP = 160.0


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    for o in list(root.occurrences):
        if o.component.name.startswith(NAME):
            o.deleteMe()

    rails = []
    for o in root.allOccurrences:
        if o.isVisible and o.fullPathName.split('+')[-1] in ('Y HGR20:1', 'Y2 HGR20:1'):
            b = [b for b in o.bRepBodies if b.isVisible][0]
            holes = sorted({round(f.geometry.origin.y * 10, 2) for f in b.faces
                            if isinstance(f.geometry, adsk.core.Cylinder)
                            and abs(f.geometry.radius * 20 - 6.0) < 0.01})
            rails.append((o.fullPathName.split('+')[-1], b.boundingBox, holes))
    assert len(rails) == 2, rails

    tb = adsk.fusion.TemporaryBRepManager.get()
    U = adsk.fusion.BooleanTypes
    out = []
    for rname, bb, holes in rails:
        xc = (bb.minPoint.x + bb.maxPoint.x) * 5
        y0, y1, z1 = bb.minPoint.y * 10, bb.maxPoint.y * 10, bb.minPoint.z * 10
        z0 = TUBE_TOP
        c = adsk.core.Point3D.create(xc / 10, (y0 + y1) / 20, (z0 + z1) / 20)
        s = tb.createBox(adsk.core.OrientedBoundingBox3D.create(
            c, adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 1, 0),
            WIDTH / 10, (y1 - y0) / 10, (z1 - z0) / 10))
        gross = s.volume * 1000
        for y in holes:
            h = tb.createCylinderOrCone(adsk.core.Point3D.create(xc / 10, y / 10, z0 / 10), 0.3,
                                        adsk.core.Point3D.create(xc / 10, y / 10, z1 / 10), 0.3)
            tb.booleanOperation(s, h, U.DifferenceBooleanType)
        side = 'Y2' if xc > 0 else 'Y1'
        out.append(('%s seat' % side, s))
        print(side, rname, 'X %.1f to %.1f, Y %.1f to %.1f, Z %.1f to %.1f' % (
            xc - WIDTH / 2, xc + WIDTH / 2, y0, y1, z0, z1),
            'holes', len(holes), holes[:1], holes[-1:],
            'gross %.0f mm3, net %.0f mm3' % (gross, s.volume * 1000))

    oc = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    cc = oc.component
    cc.name = NAME
    bf = cc.features.baseFeatures.add()
    bf.startEdit()
    for n, b in out:
        cc.bRepBodies.add(b, bf).name = n
    bf.finishEdit()
    print('component', cc.name, 'bodies', cc.bRepBodies.count)

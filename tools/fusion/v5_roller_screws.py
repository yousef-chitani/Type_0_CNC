# Cut the gantry-to-roller M6x12 screws that the Y plate rods hit to M6 x 9 (D-373). Run through
# fusion_mcp_execute (not read-only) AFTER v5_y1_place.py and v5_y2_place.py (it needs both sides'
# 'Plate Rods' bodies). Re-runnable: builds the copies once, keeps PrintNC's originals hidden.
# Why: the upper rod on the screw's outboard side (Y1 rod 2, Y2 rod 3, Z 223.9 to 228.9) ran 1.9
# into the tips of two screws per side that stood 3 below the roller's 3 mm top wall (Z 227).
# Cut at the wall's inside face (roller top - 3): the tip is flush, the rod clears by 1.1.
import adsk.core, adsk.fusion

NAME = 'Y roller screws cut to M6 x 9 (D-373)'
WALL = 3.0          # RHS 80 x 40 x 3 roller (D-362, modelled 3 wall)


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    tb = adsk.fusion.TemporaryBRepManager.get()
    U = adsk.fusion.BooleanTypes

    rods = [b for o in root.allOccurrences if o.isVisible and 'Plate Rods' in o.component.name
            for b in o.bRepBodies if b.name.startswith('Rod') and 'nut' not in b.name]
    assert len(rods) == 12, 'run v5_y1_place.py and v5_y2_place.py first (%d rods)' % len(rods)
    roller = [o for o in root.allOccurrences if o.component.name == 'YRoller'][0]
    cut_z = round(roller.boundingBox.maxPoint.z * 10, 1) - WALL   # wall's inside face, mm

    def hits(b):
        for r in rods:
            t = tb.copy(b)
            tb.booleanOperation(t, tb.copy(r), U.IntersectionBooleanType)
            if t.volume > 1e-6:
                return True
        return False

    # Screws the rods hit, both sides (PrintNC's group and its mirror). Once hidden, a screw is
    # found again by name (bodies of the same name in the same occurrence).
    done = [o for o in root.occurrences if o.component.name == NAME]
    names = set(b.name for o in done for b in o.component.bRepBodies)
    found = []
    for o in root.allOccurrences:
        if not o.fullPathName.startswith('Fasteners:1+YRollerFasteners'):
            continue
        for b in o.bRepBodies:
            key = o.fullPathName + ' | ' + b.name
            if key in names or (b.isLightBulbOn and b.isSolid and hits(b)):
                found.append((key, b))
    assert len(found) == 4, 'expected 4 screws (2 per side), found %d' % len(found)

    if not done:
        oc = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        cc = oc.component
        cc.name = NAME
        bf = cc.features.baseFeatures.add()
        bf.startEdit()
        for key, b in found:
            bb = b.boundingBox
            keep = tb.createBox(adsk.core.OrientedBoundingBox3D.create(
                adsk.core.Point3D.create((bb.minPoint.x + bb.maxPoint.x) / 2, (bb.minPoint.y + bb.maxPoint.y) / 2,
                                         (cut_z / 10 + bb.maxPoint.z) / 2 + 0.05),
                adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 1, 0),
                bb.maxPoint.x - bb.minPoint.x + 0.2, bb.maxPoint.y - bb.minPoint.y + 0.2,
                bb.maxPoint.z - cut_z / 10 + 0.1))
            t = tb.copy(b)
            tb.booleanOperation(t, keep, U.IntersectionBooleanType)
            cc.bRepBodies.add(t, bf).name = key
        bf.finishEdit()
    for key, b in found:
        b.isLightBulbOn = False
    for o in root.occurrences:
        if o.component.name == NAME:
            for b in o.bRepBodies:
                bb = b.boundingBox
                print('%s  Z %.1f..%.1f' % (b.name, bb.minPoint.z * 10, bb.maxPoint.z * 10))
    for key, b in found:  # a hidden body hides in every occurrence of its component
        print('%s: %d occurrence(s)' % (b.parentComponent.name, len(root.allOccurrencesByComponent(b.parentComponent))))

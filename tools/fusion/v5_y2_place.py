# Place the Y2 parts in Type_0_v5 (V5 plan Task 4, item 2). Run through fusion_mcp_execute (not
# read-only) AFTER tools/fusion/v5_y1_place.py. Re-runnable: it syncs Y2 to Y1 each time.
# Y2 = Y1 moved +755 in X (screw axis X -377.5 -> +377.5), not mirrored: every Y1 part is
# symmetric about the vertical plane through its screw axis, so a move gives the mirror image.
# Only the 24HS40 differs: turned 180 deg about the screw axis so its cable lead points +X
# (outboard). Each Y2 part is a second occurrence of the Y1 part's component (same part), except
# the DFU1605 (a copy of its placed bodies, see below). Run it in its own fusion_mcp_execute call:
# in the same call as v5_y1_place.py its moves did not hold (26 Nov 2026).
# Also: 2 more HGH20CA blocks in 'Y rails and seats'; PrintNC's Y2 parts that these replace are
# hidden (never deleted).
import adsk.core, adsk.fusion

DX = 755.0  # mm, Y1 axis X -377.5 to Y2 axis X +377.5
DFU2 = 'Y2 DFU1605 Nut (copy of Y1 bodies)'


def move(dx_mm):
    m = adsk.core.Matrix3D.create()
    m.translation = adsk.core.Vector3D.create(dx_mm / 10, 0, 0)
    return m


def turn_about_y(x_mm, z_mm):
    """180 deg about the line X = x_mm, Z = z_mm along Y."""
    m = adsk.core.Matrix3D.create()
    m.setToRotation(3.14159265358979, adsk.core.Vector3D.create(0, 1, 0),
                    adsk.core.Point3D.create(x_mm / 10, 0, z_mm / 10))
    return m


def placed(t1, extra):
    m = t1.copy()
    for e in extra:
        m.transformBy(e)
    return m


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    d = adsk.fusion.Design.cast(app.activeProduct)
    root = d.rootComponent
    y1 = [o for o in root.occurrences if o.component.name == 'Y1 screw and motor'][0]
    y2 = [o for o in root.occurrences if o.component.name == 'Y2 screw and motor']
    y2 = y2[0] if y2 else root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    y2.component.name = 'Y2 screw and motor'

    # Screw axis from the Y1 screw (follows SEAT).
    sb = [o for o in y1.childOccurrences if o.component.name.startswith('Y 1605 Screw')][0].boundingBox
    ax_x = (sb.minPoint.x + sb.maxPoint.x) * 5
    ax_z = (sb.minPoint.z + sb.maxPoint.z) * 5

    # Drop Y2 occurrences whose component Y1 no longer has (e.g. a part rebuilt after SEAT changed).
    y1_comps = [o.component for o in y1.childOccurrences]
    for o in list(y2.childOccurrences):
        if o.component.name == 'DFU1605 Nut' or (
                o.component.name != DFU2 and not any(o.component == c for c in y1_comps)):
            o.deleteMe()
    for k in y1.childOccurrences:
        if k.component.name == 'DFU1605 Nut':
            continue  # copied below
        extra = [move(DX)]
        if k.component.name == '24HS40 Motor':
            extra = [turn_about_y(ax_x, ax_z), move(DX)]
        want = placed(k.transform2, extra)
        twin = [o for o in y2.childOccurrences if o.component == k.component]
        if twin:
            twin = twin[0]
            twin.transform2 = want
        else:  # placed at creation: transform2 set in the call that creates it does not hold
            twin = y2.component.occurrences.addExistingComponent(k.component, want).createForAssemblyContext(y2)
        twin.isLightBulbOn = k.isLightBulbOn

    # DFU1605: its occurrence transform does not hold (Y1 note in v5_y1_place.py; a second
    # occurrence moved +755 also read back at Y1's place, 26 Nov 2026). So Y2 gets its own
    # component holding copies of the placed Y1 bodies (same vendor geometry, flats cut) moved
    # +755. Rebuilt when it no longer matches Y1 (e.g. after SEAT changed).
    dfu1 = [o for o in y1.childOccurrences if o.component.name == 'DFU1605 Nut'][0]
    src = [b for b in dfu1.bRepBodies if b.isLightBulbOn]
    a = dfu1.boundingBox
    old = [o for o in y2.childOccurrences if o.component.name == DFU2]
    if old:
        b = old[0].boundingBox
        if abs(b.minPoint.x - a.minPoint.x - DX / 10) > 0.01 or abs(b.minPoint.z - a.minPoint.z) > 0.01 \
                or abs(b.minPoint.y - a.minPoint.y) > 0.01:
            old[0].deleteMe()
            old = []
    if not old:
        tb = adsk.fusion.TemporaryBRepManager.get()
        oc = y2.component.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        cc = oc.component
        cc.name = DFU2
        bf = cc.features.baseFeatures.add()
        bf.startEdit()
        for s in src:
            t = tb.copy(s)
            tb.transform(t, move(DX))
            nb = cc.bRepBodies.add(t, bf)
            nb.name = s.name
            nb.appearance = s.appearance
        bf.finishEdit()

    # HGH20CA blocks: Y2 pair = Y1 pair moved +755 in X.
    rs = [o for o in root.occurrences if o.component.name == 'Y rails and seats'][0]
    blocks = [o for o in rs.childOccurrences if o.component.name == 'HGH20CA Block']
    b1 = sorted([o for o in blocks if o.boundingBox.maxPoint.x < 0], key=lambda o: o.boundingBox.minPoint.y)
    b2 = [o for o in blocks if o.boundingBox.minPoint.x >= 0]
    for o1, o2 in zip(b1, b2):
        o2.transform2 = placed(o1.transform2, [move(DX)])
    for o1 in b1[len(b2):]:
        b2.append(rs.component.occurrences.addExistingComponent(
            o1.component, placed(o1.transform2, [move(DX)])).createForAssemblyContext(rs))

    # Hide (never delete) the PrintNC Y2 parts these replace.
    for o in root.allOccurrences:
        p, n = o.fullPathName, o.name
        if p.startswith('Hardware:1+Y2Axis Hardware:1+') and n in (
                'Y2 HGW20CC:1', 'Y2 NEMA23 Stepper:1', 'Y2 HM12-57:1', 'Y2 BF12:1', 'Y2 SFU1610 Nut:1',
                'Y2 1610 Ballscrew:1', 'Y2 D30L40 8-10mm Coupler:1', 'M6-1.0 90 Grease Fitting(Mirror):1'):
            o.isLightBulbOn = False
        if p.startswith('Printed-Milled Parts:1+Y2Axis Printed-Milled Parts:1+Y2 1610 BFBKHM12:1+') and n in (
                'BKHM12 Riser(Mirror):1', 'BF12 Riser(Mirror):1'):
            o.isLightBulbOn = False
        if p.startswith('Printed-Milled Parts:1+Y2Axis Printed-Milled Parts:1+Y2 1610 BFBKHM12:1+Y2 1610 Roller Plates:1+') \
                and n in ('Y2 1610 Nut Plate:1', 'Y2 1610 Fill Plate:1'):
            o.isLightBulbOn = False
        if p.startswith('Fasteners:1+YRollerFasteners(Mirror):1+') and n.startswith('M5 Threaded Rod'):
            for b in o.bRepBodies:  # PrintNC's SFU flange rods and nuts, Y2 side
                if b.boundingBox.minPoint.x > 30:
                    b.isLightBulbOn = False
        # Riser screws, housing screws and the NEMA23's M4x16, Y2 side bodies only (X > 300).
        if p.startswith('Fasteners:1+YAxisFasteners(Mirror):1+') and n in (
                'M6x30(Mirror):1', 'M6x50(Mirror) (1):1', 'HM12 M6x50(Mirror):1', 'M4x16(Mirror):1'):
            for b in o.bRepBodies:
                if b.boundingBox.minPoint.x > 30:
                    b.isLightBulbOn = False
    if d.snapshots.hasPendingSnapshot:
        d.snapshots.add()
    for o in list(y2.childOccurrences) + b2:
        bb = o.boundingBox
        print(o.name, 'X %.1f..%.1f Y %.1f..%.1f Z %.1f..%.1f' % (
            bb.minPoint.x * 10, bb.maxPoint.x * 10, bb.minPoint.y * 10, bb.maxPoint.y * 10,
            bb.minPoint.z * 10, bb.maxPoint.z * 10))

# Place the Y1 vendor parts in Type_0_v5 (V5 plan Task 4, item 2). Run through fusion_mcp_execute
# (not read-only) AFTER the vendor STEPs were imported into component 'Y1 screw and motor'
# (26 Nov 2026: DFU1605 Nut, BF12, HM12-60, 24HS40 Motor, HGH20CA Block, identity transforms).
# Re-running only resets the transforms (and skips cuts / copies that already exist).
# Datums (PrintNC model mm): Y1 screw axis X -377.5, **Z 210 = roller centre** (owner 26 Nov:
# was PrintNC's 215; the DFU body Ø28 needs the 34 bore of the 80 x 40 roller centred).
# SEAT = epoxy rail-seat height (D-363, 3 mm): 0 until item 3 lifts rails, blocks and rollers.
import adsk.core, adsk.fusion

SEAT = 0.0
AX_X, AX_Z = -377.5, 210.0 + SEAT
RAIL_BOT = 160.0 + SEAT          # Y frame tube top
BLOCK_YC = (589.0, 674.0)        # PrintNC HGW20CC block centres (same pattern, HGH20CA 77.5 long)
NUT_FACE_Y = 539.0               # front face of PrintNC's SFU nut flange = carriage front
BF_YC = 738.25                   # PrintNC BF12 centre in Y
HM_SCREW_FACE_Y = 43.0           # PrintNC HM12-57 screw-end face


def mat(cols, t_mm):
    m = adsk.core.Matrix3D.create()
    m.setWithCoordinateSystem(adsk.core.Point3D.create(*[v / 10 for v in t_mm]),
                              *[adsk.core.Vector3D.create(*c) for c in cols])
    return m


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    d = adsk.fusion.Design.cast(app.activeProduct)
    root = d.rootComponent
    top = [o for o in root.occurrences if o.component.name == 'Y1 screw and motor'][0]
    kid = {o.component.name: o for o in top.childOccurrences}

    # DFU1605: local X = screw axis, flange face at x -15, nut to x -115. Local y -> Z so the
    # 40 flats (local |y| > 20, clear of the 6 x Ø5.5 holes) are top and bottom.
    # The occurrence transform does NOT hold for this part: set + snapshot reads back at the
    # origin (tried 26 Nov 2026 with transform/transform2, timeline rolled before the cut; the
    # component holds its own Base Feature). So the occurrence stays at identity and a Move
    # feature 'DFU place' (after the flats cut) moves its bodies. Not re-run if it exists.
    dfu = kid['DFU1605 Nut']
    c = dfu.component
    for b in c.bRepBodies:
        if b.name == 'Body3':
            b.isLightBulbOn = False  # 130 screw piece from the vendor file
    if not any(f.name == 'DFU flats 40' for f in c.features.extrudeFeatures):
        sk = c.sketches.add(c.xYConstructionPlane)
        L = sk.sketchCurves.sketchLines
        for y0, y1 in ((2.0, 3.0), (-3.0, -2.0)):
            L.addTwoPointRectangle(adsk.core.Point3D.create(-6.1, y0, 0), adsk.core.Point3D.create(-1.4, y1, 0))
        prof = adsk.core.ObjectCollection.create()
        for p in sk.profiles:
            prof.add(p)
        ei = c.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
        ei.setSymmetricExtent(adsk.core.ValueInput.createByString('30 mm'), True)
        flange = [b for b in c.bRepBodies if b.name == 'Body6']
        ei.participantBodies = flange
        f = c.features.extrudeFeatures.add(ei)
        f.name = 'DFU flats 40'
    if not any(f.name == 'DFU place' for f in c.features.moveFeatures):
        col = adsk.core.ObjectCollection.create()
        for b in c.bRepBodies:
            col.add(b)
        mi = c.features.moveFeatures.createInput2(col)
        mi.defineAsFreeMove(mat([(0, -1, 0), (0, 0, 1), (-1, 0, 0)], (AX_X, NUT_FACE_Y - 15, AX_Z)))
        c.features.moveFeatures.add(mi).name = 'DFU place'

    # BF12: bore axis local Z at local y 3.5, base at local y -21.5 (centre height 25).
    kid['BF12'].transform2 = mat([(1, 0, 0), (0, 0, 1), (0, -1, 0)], (AX_X, BF_YC, AX_Z - 3.5))

    # HGH20CA: rail stub along local Z, up = local Y, rail bottom at local y -17.5. Blocks go in
    # 'Y rails and seats' (plan Task 4 component); PrintNC's HGR20 rail is kept.
    rs = [o for o in root.occurrences if o.component.name == 'Y rails and seats']
    rs = rs[0] if rs else root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    rs.component.name = 'Y rails and seats'
    if 'HGH20CA Block' in kid:
        kid['HGH20CA Block'].moveToComponent(rs)
    blocks = [o for o in rs.childOccurrences if o.component.name == 'HGH20CA Block']
    while len(blocks) < 2:
        rs.component.occurrences.addExistingComponent(blocks[0].component, adsk.core.Matrix3D.create())
        blocks = [o for o in rs.childOccurrences if o.component.name == 'HGH20CA Block']
    for b in blocks[0].component.bRepBodies:
        if b.name == 'Body2':
            b.isLightBulbOn = False  # 150 rail stub from the vendor file
    for o, yc in zip(blocks, BLOCK_YC):
        o.transform2 = mat([(1, 0, 0), (0, 0, 1), (0, -1, 0)], (AX_X, yc, RAIL_BOT + 17.5))

    # HM12-60: axis local Z, screw end (bearings, local z 0 to 25, lock nut 25 to 33) at local
    # z 0, motor end (Ø50 pilot recess, 4 x M5 on 49.4 square) at local z 90, base local y -30.
    # Screw-end face at PrintNC's HM12-57 screw-end face, Y 43; motor face Y -47; base Z 180.
    kid['HM12-60'].transform2 = mat([(1, 0, 0), (0, 0, 1), (0, -1, 0)], (AX_X, HM_SCREW_FACE_Y, AX_Z))
    # 24HS40: flange face local z 0, Ø38.1 pilot, shaft Ø10 to local z +20, holes on 50 square;
    # the cable lead (local -y) points outboard (-X).
    kid['24HS40 Motor'].transform2 = mat([(0, 0, 1), (1, 0, 0), (0, 1, 0)], (AX_X, HM_SCREW_FACE_Y - 90, AX_Z))
    for n in ('HM12-60', '24HS40 Motor'):
        kid[n].isLightBulbOn = True
    # Not placed yet: D25L35 (to model, D-366), the 1605 screw (needs LiMo's end drawing).

    # Hide (never delete) the PrintNC Y1 parts these replace.
    for o in root.allOccurrences:
        p = o.fullPathName
        if p.startswith('Hardware:1+YAxis Hardware:1+') and o.name in (
                'Y HGW20CC:1', 'Y SFU1610 Nut:1', 'Y BF12:1', 'M6-1.0 90 Grease Fitting:1',
                'Y HM12-57:1', 'Y NEMA23 Stepper:1'):
            o.isLightBulbOn = False
    if d.snapshots.hasPendingSnapshot:
        d.snapshots.add()
    for o in [dfu, kid['BF12'], kid['HM12-60'], kid['24HS40 Motor']] + blocks:  # DFU: bodies moved, so its box is the placed one
        bb = o.boundingBox
        print(o.name, 'X %.1f..%.1f Y %.1f..%.1f Z %.1f..%.1f' % (
            bb.minPoint.x * 10, bb.maxPoint.x * 10, bb.minPoint.y * 10, bb.maxPoint.y * 10,
            bb.minPoint.z * 10, bb.maxPoint.z * 10))

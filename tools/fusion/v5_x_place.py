# V5 beam and X axis (plan Task 5, bundle C part 1). Run through fusion_mcp_execute (not
# read-only) after v5_y1_place.py, v5_y2_place.py, v5_roller_screws.py, v5_y_seats.py; then
# v5_check_task4.py. Re-running drops both components and rebuilds them.
# Layout (owner, 27 Nov 2026):
#   D-353/D-380 beam RHS 200 x 150 x 8 on the full top of both Y rollers: Z 233 to 433, Y 556.5
#     (front face, flush with the roller front end, gantry at the rear stop) to 706.5, X +-417.5
#     (the model's XGantryLength 835). Corners EN 10219-2 nominal R 2.5T = 20 out, 12 in
#     (tools/v5_beam.py r_out_calc).
#   D-379/D-372 X seats 3 thick, 30 wide, on the front face under each rail; D-355 rails 122 apart,
#     centred on the face: Z 272 and 394; rails X -325 to 325 (650).
#   D-358/D-381 4 HGH20CA blocks (pitch 100, D-150) with 17 drilled steel spacers: the plate back
#     sits 50 off the face (Y 506.5). Screw axis 30 off the face (Y 526.5), Z 333.
#   D-381/D-382 the Y1 screw train (HM12-60 + 7901C, D25L35, 24HS40, DFU1605 screw 750, BF12)
#     copied from Y1 and turned onto the face: HM12-60 straight on the face at the -X beam end
#     (motor past the end), BF12 on a 5 shim. DFU1605 nut flange at the -X end, DSG16H housing
#     (drawing values, cad/vendor/README.md: 52 x 40 face, 40 high, centre 20 below the face)
#     behind it, centred on the carriage (X -20 to 20). Carriage centre X 0.
# Hidden (not deleted): PrintNC XGantry (and its X rollers), both YRollerBrace, XAxis Hardware,
# ZAxis Hardware, Zaxis Dual Carriage HGH15CA (the Type 0 Z replaces it: bundle C part 2).
# Names avoid the check's SKIP list ('M5', 'M6', ...).
import adsk.core, adsk.fusion

BEAM = 'V5 Beam (RHS 200x150x8)'
XAX = 'V5 X axis (front-face rails)'
FACE_Y = 556.5            # beam front face (= Y roller front end)
BEAM_Y1 = 706.5
BEAM_Z0, BEAM_Z1 = 233.0, 433.0
BEAM_X = 417.5
R_OUT, WALL = 20.0, 8.0
RAIL_Z = (272.0, 394.0)
RAIL_X0 = -325.0
AXIS_Z = 333.0
AXIS_OFF = 30.0           # screw axis off the face
SPACER = 17.0
BLOCK_X = (-50.0, 50.0)
SEAT_W = 30.0
# Y1 frame (source): axis X -377.5, tube top Z 160, axis Z 213
Y_LAT, Y_TOP = -377.5, 160.0
TRAIN_DX = -370.5         # Y1 HM12-60 body Y -47 -> X -417.5 (the beam end)
RAIL_DX = RAIL_X0 - 64.0  # Y rail Y 64 -> X -325
NUT_DX = -20.0 - 541.5    # DFU flange back face Y 541.5 -> X -20 (housing front)
HIDE = ('PrintNC Structure:1+XGantry:1', 'PrintNC Structure:1+YFrame:1+YRollerBrace:1',
        'PrintNC Structure:1+YFrame(Mirror):1+YRollerBrace(Mirror):1',
        'Hardware:1+XAxis Hardware:1', 'Hardware:1+ZAxis Hardware:1',
        'Zaxis Dual Carriage HGH15CA:1')

P = adsk.core.Point3D.create
V = adsk.core.Vector3D.create


def mat(dx, ybase, zc):
    """Y1 frame -> beam face: X' = y + dx, Y' = ybase - z, Z' = zc - (x - Y_LAT). mm in, cm out."""
    m = adsk.core.Matrix3D.create()
    m.setWithArray([0, 1, 0, dx / 10, 0, 0, -1, ybase / 10, -1, 0, 0, (zc + Y_LAT) / 10, 0, 0, 0, 1])
    return m


def box(x0, x1, y0, y1, z0, z1):
    tb = adsk.fusion.TemporaryBRepManager.get()
    return tb.createBox(adsk.core.OrientedBoundingBox3D.create(
        P((x0 + x1) / 20, (y0 + y1) / 20, (z0 + z1) / 20), V(1, 0, 0), V(0, 1, 0),
        abs(x1 - x0) / 10, abs(y1 - y0) / 10, abs(z1 - z0) / 10))


def xcyl(x0, x1, y, z, r):
    tb = adsk.fusion.TemporaryBRepManager.get()
    return tb.createCylinderOrCone(P(x0 / 10, y / 10, z / 10), r / 10, P(x1 / 10, y / 10, z / 10), r / 10)


def rrect(x0, x1, y0, y1, z0, z1, r):
    """Bar along X with a rounded-rectangle section (Y x Z), corner radius r."""
    tb = adsk.fusion.TemporaryBRepManager.get()
    U = adsk.fusion.BooleanTypes.UnionBooleanType
    b = box(x0, x1, y0 + r, y1 - r, z0, z1)
    tb.booleanOperation(b, box(x0, x1, y0, y1, z0 + r, z1 - r), U)
    for y in (y0 + r, y1 - r):
        for z in (z0 + r, z1 - r):
            tb.booleanOperation(b, xcyl(x0, x1, y, z, r), U)
    return b


def copy(body, m):
    tb = adsk.fusion.TemporaryBRepManager.get()
    c = tb.copy(body)
    tb.transform(c, m)
    return c


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    tb = adsk.fusion.TemporaryBRepManager.get()
    D = adsk.fusion.BooleanTypes.DifferenceBooleanType
    for o in list(root.occurrences):
        if o.component.name.startswith(BEAM) or o.component.name.startswith(XAX):
            o.deleteMe()

    occ = {o.fullPathName: o for o in root.allOccurrences}

    def vis_bodies(path):
        return [b for b in occ[path].bRepBodies if b.isVisible]

    def under(prefix):
        return [(p, b) for p, o in occ.items() if p.startswith(prefix) and o.isVisible
                for b in o.bRepBodies if b.isVisible]

    # ---- beam ----
    beam = rrect(-BEAM_X, BEAM_X, FACE_Y, BEAM_Y1, BEAM_Z0, BEAM_Z1, R_OUT)
    tb.booleanOperation(beam, rrect(-BEAM_X - 1, BEAM_X + 1, FACE_Y + WALL, BEAM_Y1 - WALL,
                                    BEAM_Z0 + WALL, BEAM_Z1 - WALL, R_OUT - WALL), D)
    beam_bodies = [('Beam RHS 200x150x8 (steel, R20 out / R12 in)', beam)]

    # ---- X axis ----
    out = []
    rail = vis_bodies('Hardware:1+YAxis Hardware:1+Y HGR20:1')[0]
    seat = [b for b in occ['Y Rail Seats (epoxy, 30 wide):1'].bRepBodies if b.name == 'Y1 seat'][0]
    block = vis_bodies('Y rails and seats:1+HGH20CA Block:1')[0]
    rail_yb = FACE_Y + Y_TOP                       # n = z - 160 -> Y = FACE_Y - n
    bb = block.boundingBox
    blk_c = (bb.minPoint.y + bb.maxPoint.y) * 5    # block centre along Y1 (mm)
    blk_n1 = bb.maxPoint.z * 10 - Y_TOP            # block top off the tube top (33)
    for i, z in enumerate(RAIL_Z):
        side = 'lower' if i == 0 else 'upper'
        out.append(('X seat %s (epoxy 30 x 3)' % side, copy(seat, mat(RAIL_DX, rail_yb, z))))
        out.append(('X rail HGR20 %s 650' % side, copy(rail, mat(RAIL_DX, rail_yb, z))))
        for j, x in enumerate(BLOCK_X):
            out.append(('X block HGH20CA %s %d' % (side, j + 1), copy(block, mat(x - blk_c, rail_yb, z))))
            y0 = FACE_Y - blk_n1
            out.append(('X block spacer %s %d (steel 44x50x17)' % (side, j + 1),
                        box(x - 25, x + 25, y0, y0 - SPACER, z - 22, z + 22)))
    train_yb = FACE_Y + Y_TOP + 23.0                # Y1 HM12-60 base (n 23) -> on the face
    for p, b in under('Y1 screw and motor:1+'):
        part = p.split('+')[1]
        if part.startswith(('Y1 HM12 Riser', 'Y1 BF12 Riser', 'Y1 Nut Plate', 'Y1 Fill Plate',
                            'Y1 Plate Rods')):
            continue
        if part.startswith('DFU1605 Nut'):
            out.append(('X DFU1605 nut ' + b.name, copy(b, mat(NUT_DX, train_yb, AXIS_Z))))
            continue
        name = part.split(':')[0].replace('Y 1605 Screw', '1605 Screw').replace(' (2)', '')
        last = p.split('+')[-1].split(':')[0].strip()
        if last != part.split(':')[0]:
            name += ' ' + last
        out.append(('X ' + name + ' ' + b.name, copy(b, mat(TRAIN_DX, train_yb, AXIS_Z))))
    bfr = occ['Y1 screw and motor:1+Y1 BF12 Riser (60 wide, 28 tall):1'].bRepBodies.item(0).boundingBox
    out.append(('X BF12 shim 5 (steel 60 wide)',
                box(bfr.minPoint.y * 10 + TRAIN_DX, bfr.maxPoint.y * 10 + TRAIN_DX,
                    FACE_Y, FACE_Y - 5, AXIS_Z - 30, AXIS_Z + 30)))
    ay = FACE_Y - AXIS_OFF
    hs = box(-20, 20, ay - 20, ay + 20, AXIS_Z - 26, AXIS_Z + 26)
    tb.booleanOperation(hs, xcyl(-21, 21, ay, AXIS_Z, 14), D)
    out.append(('X nut housing DSG16H (drawing: 52 x 40 face, 40 high)', hs))

    for name, bodies in ((BEAM, beam_bodies), (XAX, out)):
        oc = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        cc = oc.component
        cc.name = name
        bf = cc.features.baseFeatures.add()
        bf.startEdit()
        for n, b in bodies:
            cc.bRepBodies.add(b, bf)
        bf.finishEdit()
        assert cc.bRepBodies.count == len(bodies)
        for i, (n, b) in enumerate(bodies):   # names set inside the edit do not hold on copies
            cc.bRepBodies.item(i).name = n
        print(name, cc.bRepBodies.count, 'bodies')

    for p in HIDE:
        occ[p].isLightBulbOn = False
    for b in root.occurrences.itemByName(XAX + ':1').bRepBodies:
        k = b.boundingBox
        if any(s in b.name for s in ('seat lower', 'rail HGR20 lower', 'block HGH20CA lower 1',
                                      'spacer lower 1', 'housing', 'shim', 'HM12-60 Body1',
                                      '24HS40 Motor Body3', 'Screw', 'BF12 Body1', 'nut Body6')):
            print('  %-58s X %7.1f..%7.1f Y %6.1f..%6.1f Z %6.1f..%6.1f' % (
                b.name[:58], k.minPoint.x * 10, k.maxPoint.x * 10, k.minPoint.y * 10,
                k.maxPoint.y * 10, k.minPoint.z * 10, k.maxPoint.z * 10))
    k = root.occurrences.itemByName(BEAM + ':1').bRepBodies.item(0)
    print('beam volume %.0f cm3 (%.1f kg)' % (k.volume, k.volume * 7.85e-3))

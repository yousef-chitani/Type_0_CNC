"""Regenerate docs/phase1-bom.xlsx from docs/bom.csv. Run from the repo root: python tools/gen_phase1_xlsx.py (then recalc in LibreOffice/Excel)."""
import csv, re
from urllib.parse import urlparse
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
rows=[r for r in csv.DictReader(open('docs/bom.csv')) if r['stage']=='1']
URL=re.compile(r'https?://[^\s,;)]+')
NAMES={'aliexpress.com':'AliExpress','ebay.co.uk':'eBay UK','ebay.de':'eBay DE','ebay.com':'eBay','omc-stepperonline.com':'StepperOnline','store.mesanet.com':'Mesa store','eusurplus.com':'EuSurplus','aluminiumwarehouse.co.uk':'Aluminium Warehouse','rapidonline.com':'Rapid','diy.com':'B&Q','wickes.co.uk':'Wickes','screwfix.com':'Screwfix','toolstation.com':'Toolstation','themetalstore.co.uk':'The Metal Store','easycomposites.co.uk':'Easy Composites','ecfibreglasssupplies.co.uk':'EC Fibreglass','gclproducts.co.uk':'GCL','hancockandbrown.com':'Hancock & Brown','valentineclays.co.uk':'Valentine Clays','rdgtools.co.uk':'RDG Tools','alibaba.com':'Alibaba','google.com':'Search'}
def label(u):
    h=urlparse(u).netloc.replace('www.','').replace('uk.','')
    return NAMES.get(h,h)
F=lambda **k: Font(name="Arial", **k)
wb=Workbook(); ws=wb.active; ws.title="Phase 1"
ws.append(["Type 0 CNC v2: Phase 1 parts list (work area 400 × 250)"]); ws["A1"].font=F(bold=True,size=14)
ws.append(["Blue = price read from a live page or given by the owner. Yellow columns are for you: Bought? (Y/N) and Actual paid £ (e.g. Y and 61.20). Links: click to open."]); ws["A2"].font=F(italic=True,size=9)
ws.append([])
hdr=["ID","Subsystem","Item","Qty","Unit","Specification","Price as listed","Line £","Link","Link 2","Link 3","Notes","Date checked","Bought? (Y/N)","Actual paid £"]
ws.append(hdr); hr=4
for c in range(1,len(hdr)+1):
    cell=ws.cell(row=hr,column=c); cell.font=F(bold=True,color="FFFFFF"); cell.fill=PatternFill("solid",fgColor="2C3E50"); cell.alignment=Alignment(wrap_text=True,vertical="center")
yellow=PatternFill("solid",fgColor="FFF2B3"); thin=Side(style="thin",color="DDDDDD")
start=hr+1
for i,r in enumerate(rows):
    rr=start+i; urls=[]
    for u in ([r['link']] if r['link'] else [])+URL.findall(r['notes'])+URL.findall(r['price_listed']):
        u=u.rstrip('.')
        if u not in urls: urls.append(u)
    notes=URL.sub('',r['notes']).replace(' :',':').replace('  ',' ').strip(' .:')
    vals=[r['id'],r['subsystem'],r['item'],int(r['qty']) if r['qty'].isdigit() else r['qty'],r['unit'],r['specification'],r['price_listed'],float(r['price_gbp']) if r['price_gbp'] else None,None,None,None,notes,r['date_checked'],None,None]
    for c,v in enumerate(vals,1):
        cell=ws.cell(row=rr,column=c,value=v); cell.font=F(size=9); cell.alignment=Alignment(wrap_text=True,vertical="top"); cell.border=Border(bottom=thin)
    for k,u in enumerate(urls[:3]):
        c=ws.cell(row=rr,column=9+k,value=f'=HYPERLINK("{u}","{label(u)}")'); c.hyperlink=u; c.font=F(size=9,color="0563C1",underline="single")
    if not urls: ws.cell(row=rr,column=9,value="owner / DIY / included").font=F(size=9,italic=True,color="888888")
    ws.cell(row=rr,column=8).font=F(size=9,color="0000FF"); ws.cell(row=rr,column=8).number_format='£#,##0.00;(£#,##0.00);"-"'
    for c in (14,15): ws.cell(row=rr,column=c).fill=yellow
    ws.cell(row=rr,column=15).number_format='£#,##0.00;(£#,##0.00);"-"'
end=start+len(rows)-1; tr=end+2
def put(r,c,v,bold=False,fmt='£#,##0.00',col=None):
    cell=ws.cell(row=r,column=c,value=v); cell.font=F(bold=bold,color=col) if col else F(bold=bold); cell.number_format=fmt
put(tr,7,"Phase 1 total",True); put(tr,8,f"=SUM(H{start}:H{end})",True); put(tr,15,f"=SUM(O{start}:O{end})",True)
put(tr+1,7,"Budget (D-68)"); put(tr+1,8,4000,col="0000FF")
put(tr+2,7,"Remaining",True); put(tr+2,8,f"=H{tr+1}-H{tr}",True,'£#,##0.00;(£#,##0.00)')
put(tr+3,7,"Bought so far (lines marked Y)"); put(tr+3,8,f'=SUMIF(N{start}:N{end},"Y",H{start}:H{end})')
for i,w in enumerate([6,12,30,6,10,40,34,11,16,16,16,40,11,10,12],1): ws.column_dimensions[get_column_letter(i)].width=w
ws.freeze_panes="D5"; ws.auto_filter.ref=f"A{hr}:O{end}"
s=wb.create_sheet("Summary"); s.append(["Subsystem","Line £","Actual paid £"])
for c in range(1,4): s.cell(row=1,column=c).font=F(bold=True)
subs=list(dict.fromkeys(r['subsystem'] for r in rows))
for i,g in enumerate(subs,2):
    s.cell(row=i,column=1,value=g).font=F()
    for c,L in ((2,'H'),(3,'O')):
        x=s.cell(row=i,column=c,value=f"=SUMIF('Phase 1'!B{start}:B{end},A{i},'Phase 1'!{L}{start}:{L}{end})"); x.font=F(color="008000"); x.number_format='£#,##0.00;(£#,##0.00);"-"'
n=len(subs)+1
s.cell(row=n+1,column=1,value="Total").font=F(bold=True)
for c,L in ((2,'B'),(3,'C')):
    x=s.cell(row=n+1,column=c,value=f"=SUM({L}2:{L}{n})"); x.font=F(bold=True); x.number_format='£#,##0.00'
for c,w in (('A',18),('B',14),('C',14)): s.column_dimensions[c].width=w
wb.save('docs/phase1-bom.xlsx')

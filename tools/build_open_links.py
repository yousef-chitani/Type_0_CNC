"""Rebuild tools/open_links.py with the current parts list embedded. Run: python tools/build_open_links.py"""
import csv, json, re
from pathlib import Path
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"https?://[^\s,;)]+")
NAMES = {'aliexpress.com':'AliExpress','omc-stepperonline.com':'StepperOnline','store.mesanet.com':'Mesa','eusurplus.com':'EuSurplus','aluminiumwarehouse.co.uk':'Aluminium Warehouse','rapidonline.com':'Rapid','diy.com':'B&Q','wickes.co.uk':'Wickes','screwfix.com':'Screwfix','toolstation.com':'Toolstation','themetalstore.co.uk':'The Metal Store','easycomposites.co.uk':'Easy Composites','ecfibreglasssupplies.co.uk':'EC Fibreglass','gclproducts.co.uk':'GCL','hancockandbrown.com':'Hancock & Brown','valentineclays.co.uk':'Valentine Clays','rdgtools.co.uk':'RDG Tools','alibaba.com':'Alibaba','rs-online.com':'RS Components','uk.rs-online.com':'RS Components'}
def vendor(u):
    h = urlparse(u).netloc.lower().replace('www.', '')
    return NAMES.get(h, NAMES.get(h.replace('uk.', ''), h))
data = []
for r in csv.DictReader(open(ROOT/'docs'/'bom.csv', encoding='utf-8')):
    if not r['link'] or 'ebay.' in r['link'] or 'google.com/search' in r['link']:
        continue
    extra = [u.rstrip('.') for u in URL.findall(r['notes']) + URL.findall(r['price_listed']) if 'ebay.' not in u and 'google.com' not in u]
    data.append(dict(id=r['id'], phase=r['stage'], item=r['item'], qty=f"{r['qty']} {r['unit']}", price=r['price_gbp'],
                     vendor=vendor(r['link']), url=r['link'], extra=[u for u in dict.fromkeys(extra) if u != r['link']]))
missing = [dict(id=r['id'], phase=r['stage'], item=r['item']) for r in csv.DictReader(open(ROOT/'docs'/'bom.csv', encoding='utf-8'))
           if r['link'] and ('ebay.' in r['link'])]
tpl = (ROOT/'tools'/'open_links_template.py').read_text(encoding='utf-8')
out = tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False)).replace('__NOLINK__', json.dumps(missing, ensure_ascii=False))
(ROOT/'tools'/'open_links.py').write_text(out, encoding='utf-8')
print(f"{len(data)} parts embedded, {len(missing)} eBay-only parts listed as 'needs a new vendor'")

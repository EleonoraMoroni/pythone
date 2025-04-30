#no sequenziale, ma provincia, prima la sigla, poi nome provincia,
# poi abitanti più kmq + ricalcolar ekla densità in kmq e confrontare

import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding = "iso-8859-1")

import bs4
doc = bs4.BeautifulSoup(text)
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2] :
    if type(tr) == bs4.element.Tag :
        tds = tr.contents
        sigl = tds[7].get.text()
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".", ""))
        kmq = float(tds[4].get_text().replace(".", ""))
        densitaSito = float(tds[6].get_text().replace(",", ".")) 
        print(f"{sigl} {prov:25s} {resi:9d} {kmq:6.2f} {densitaSito:6.2f}")


""" densita = residenti / kmq
    round(densita, 2)
    if densitaSito - densita < 1e-14
       densitaSito == densita
       print(f"la densità ...........")
    else
    .......
"""
       

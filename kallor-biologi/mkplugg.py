# -*- coding: utf-8 -*-
import sys, os, re, importlib
sys.path.insert(0, "/tmp/bio")
from playwright.sync_api import sync_playwright
OM = [(1,"omrade1","ch01n","biologi-1-vetenskap"),(2,"omrade2","ch02n","biologi-2-cellen"),
      (3,"omrade3","ch03n","biologi-3-mangfald"),(4,"omrade4","ch04n","biologi-4-ekologi")]
CSS = """
@page{size:A4;margin:11mm 12mm 14mm 12mm}
*{box-sizing:border-box}body{font:12pt/1.45 Inter,sans-serif;color:#241712;margin:0}
h1{font:700 18pt Inter;color:#245040;margin:0}.sub{font:10pt Inter;color:#6b625b;margin:0 0 6pt}
.beta{font:700 8pt Carlito;background:#fff5d6;color:#a8651a;padding:1pt 5pt;border-radius:3pt;vertical-align:middle}
h2{font:700 14.5pt Inter;color:#fff;background:#2f6b4f;padding:2pt 7pt;border-radius:4pt;margin:6pt 0 4pt;break-after:avoid}
h3{break-after:avoid;font:700 12.5pt Inter;color:#2f6b4f;margin:6pt 0 2pt}
ul{margin:0 0 4pt;padding-left:12pt}li{margin:0 0 3pt}
.begr{columns:2;column-gap:9mm;font:10pt/1.28 Inter}.begr div{break-inside:avoid;margin:0 0 1.5pt}
.q{break-inside:avoid;margin:0 0 7pt;display:flex;gap:5pt}.q .n{font:700 12pt Inter;color:#2f6b4f;min-width:17pt}
.q .p{font:italic 10pt Inter;color:#6b625b}
.alt{display:grid;grid-template-columns:1fr 1fr;gap:0 8pt;margin-top:2pt;font-size:12pt}
.qcols{columns:1}
table{border-collapse:collapse;margin:3pt 0;font:11pt Inter}td,th{border:.7pt solid #b9b1a6;padding:1.5pt 6pt}th{background:#e5f1e9}
.fakeann{display:none}
.sf{white-space:nowrap;font:10pt Inter;color:#6b625b}.lines{border-bottom:.6pt solid #bdb5aa;height:15pt;margin-top:2pt}
.fac{font:12pt/1.4 Inter;columns:2;column-gap:9mm}.fac div{break-inside:avoid;margin:0 0 4pt}
.note{font:italic 10.5pt Inter;color:#6b625b}
.pb{break-before:page}
"""
def build(nr, folder, mod, slug):
    os.chdir("/tmp/bio/"+folder if folder!="." else "/tmp/bio"); sys.path.insert(0, os.getcwd()); sys.path.insert(0, "/tmp/bio")
    M = importlib.import_module(mod)
    from pluggfragor import PQ
    h = [f"<h1>Plugga inför prov – {M.NAMN} <span class='beta'>beta</span></h1>",
         f"<p class='sub'>Område {nr} · sammanfattning, viktiga begrepp och övningsfrågor med facit. Skriv ut och plugga de sista dagarna.</p>",
         "<h2>Sammanfattning</h2><ul>"+"".join(f"<li>{s}</li>" for s in M.SAMMAN)+"</ul>",
         "<h2>Viktiga begrepp</h2><div class='begr'>"+"".join(f"<div><b>{a}</b> – {b}</div>" for a,b in M.BEGR)+"</div>",
         "<h2 class='pb'>Övningsfrågor</h2><p class='note'>Försök svara själv innan du tittar på facit på sista sidan.</p><div class='qcols'>"]
    fac = []; n = 0; pos = 0; last = None
    RUBRIK = {"mc": "Välj ett alternativ", "sf": "Sant eller falskt", "kort": "Svara kort"}
    for it in PQ[nr]:
        n += 1
        if it[0] != last:
            h.append(f"<h3>{RUBRIK[it[0]]}</h3>"); last = it[0]
        if it[0] == "mc":
            _, q, ratt, fel = it
            k = (pos * 3 + 1) % 4; pos += 1
            alt = list(fel); alt.insert(k, ratt)
            body = q + "<div class='alt'>" + "".join(f"<div>{'ABCD'[i]} {o}</div>" for i, o in enumerate(alt)) + "</div>"
            fac.append(f"<b>{n}.</b> {'ABCD'[k]} – {ratt}")
        elif it[0] == "sf":
            body = it[1] + "<br>" + "<br>".join(f"{chr(97+i)}) {t} &nbsp;<span class='sf'>☐ Sant &nbsp;☐ Falskt</span>" for i, (t, v) in enumerate(it[2]))
            fac.append(f"<b>{n}.</b> " + ", ".join(f"{chr(97+i)}) {'Sant' if v else 'Falskt'}" for i, (t, v) in enumerate(it[2])))
        else:
            body = it[1] + "<div class='lines'></div><div class='lines'></div>"
            fac.append(f"<b>{n}.</b> {it[2]}")
        h.append(f"<div class='q'><span class='n'>{n}</span><div>{body}</div></div>")
    h.append("</div><h2 class='pb'>Facit</h2><div class='fac'>" + "".join(f"<div>{f}</div>" for f in fac) + "</div>")
    h.append("<p class='note'>Frågorna övar grunderna: de viktigaste begreppen och fakta. På provet får du också förklara, tolka resultat och resonera. Facit på de korta svaren är förslag; andra rimliga svar kan också vara rätt.</p>")
    html = f"<!doctype html><meta charset=utf-8><style>{CSS}</style>"+"".join(h)
    p = f"/tmp/bio/out/{slug}-pluggblad.html"; open(p,"w").write(html)
    return p

with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    for o in OM:
        p = build(*o); pg.goto("file://"+p)
        pg.pdf(path=p.replace(".html",".pdf"), format="A4", print_background=True, prefer_css_page_size=True,
               display_header_footer=True, header_template="<span></span>",
               footer_template=f"<div style='font:8pt Inter;width:100%;padding:0 13mm;color:#6b625b;display:flex;justify-content:space-between'><span>Pluggis · Biologi · Plugga inför prov (beta)</span><span><span class='pageNumber'></span>/<span class='totalPages'></span></span></div>")
    b.close()

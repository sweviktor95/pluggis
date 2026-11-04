# -*- coding: utf-8 -*-
import sys, os, re, importlib
sys.path.insert(0, "/tmp/bio")
from playwright.sync_api import sync_playwright
OM = [(1,"omrade1","ch01n","biologi-1-vetenskap"),(2,"omrade2","ch02n","biologi-2-cellen"),
      (3,"omrade3","ch03n","biologi-3-mangfald"),(4,".","ch04","biologi-4-ekologi")]
CSS = """
@page{size:A4;margin:12mm 13mm 14mm 13mm}
*{box-sizing:border-box}body{font:10.6pt/1.5 Inter,sans-serif;color:#241712;margin:0}
h1{font:700 20pt Inter;color:#245040;margin:0}.sub{font:10pt Inter;color:#6b625b;margin:0 0 6pt}
.beta{font:700 8pt Carlito;background:#fff5d6;color:#a8651a;padding:1pt 5pt;border-radius:3pt;vertical-align:middle}
h2{font:700 13.5pt Inter;color:#fff;background:#2f6b4f;padding:2pt 7pt;border-radius:4pt;margin:8pt 0 5pt;break-after:avoid}
h3{break-after:avoid;font:700 11pt Inter;color:#2f6b4f;margin:6pt 0 2pt}
ul{margin:0 0 4pt;padding-left:12pt}li{margin:0 0 4pt}
.begr{columns:2;column-gap:9mm;font:9.8pt/1.4 Inter}.begr div{break-inside:avoid;margin:0 0 2.5pt}
.q{break-inside:avoid;margin:0 0 9pt;display:flex;gap:5pt}.q .n{font:700 11pt Inter;color:#2f6b4f;min-width:17pt}
.q .p{font:8pt Carlito;color:#6b625b}
.alt{display:grid;grid-template-columns:1fr 1fr;gap:0 8pt;margin-top:2pt;font-size:10pt}
.qcols{columns:1}
table{border-collapse:collapse;margin:3pt 0;font:9.6pt Inter}td,th{border:.7pt solid #b9b1a6;padding:1.5pt 6pt}th{background:#e5f1e9}
.fakeann{display:none}
.lines{border-bottom:.6pt solid #bdb5aa;height:17pt;margin-top:2pt}
.fac{font:10pt/1.45 Inter;columns:2;column-gap:9mm}.fac div{break-inside:avoid;margin:0 0 4pt}
.note{font:italic 9.2pt Inter;color:#6b625b}
.pb{break-before:page}
"""
def strip(s): return s
def build(nr, folder, mod, slug):
    os.chdir("/tmp/bio/"+folder if folder!="." else "/tmp/bio"); sys.path.insert(0, os.getcwd())
    M = importlib.import_module(mod)
    h = [f"<h1>Plugga inför prov – {M.NAMN} <span class='beta'>beta</span></h1>",
         f"<p class='sub'>Område {nr} · sammanfattning, viktiga begrepp och övningsfrågor med facit. Skriv ut och plugga de sista dagarna.</p>",
         "<h2>Sammanfattning</h2><ul>"+"".join(f"<li>{s}</li>" for s in M.SAMMAN)+"</ul>",
         "<h2>Viktiga begrepp</h2><div class='begr'>"+"".join(f"<div><b>{a}</b> – {b}</div>" for a,b in M.BEGR)+"</div>",
         "<h2 class='pb'>Övningsfrågor</h2><p class='note'>Försök svara själv innan du tittar på facit på sista sidan.</p><div class='qcols'>"]
    last = None
    for i, t in enumerate(M.TEST):
        d, q, opts = t[0], t[1], t[2]
        if d != last:
            h.append(f"<h3>{M.DEL_NAMN.get(d,d)}</h3>"); last = d
        if q == "TABELL":
            rub, rader = M.TEST_TABELL
            q = M.TEST_D_TEXT + "<table><tr>"+"".join(f"<th>{c}</th>" for c in rub)+"</tr>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rader)+"</table>" + "<br>".join(M.TEST_D_SUB)
        body = q
        if opts: body += "<div class='alt'>"+"".join(f"<div>{o}</div>" for o in opts)+"</div>"
        else: body += "<div class='lines'></div><div class='lines'></div>" if (len(t)>4 and t[4] and t[4]<=4) else "<div class='lines'></div><div class='lines'></div><div class='lines'></div>"
        h.append(f"<div class='q'><span class='n'>{i+1}</span><div>{body}</div></div>")
    h.append("</div><h2 class='pb'>Facit</h2><div class='fac'>")
    for i, t in enumerate(M.TEST):
        f = M.FACIT[i]
        if t[2]: f = f"{f} – {t[2][ord(f)-65][2:]}"
        h.append(f"<div><b>{i+1}.</b> {f}</div>")
    h.append("</div><p class='note'>Facit på öppna frågor är förslag; andra rimliga svar kan också ge poäng. Frågorna är samma typ som på provet men inte samma uppgifter.</p>")
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

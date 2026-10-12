# -*- coding: utf-8 -*-
import sys, os, re
sys.path.insert(0, '/tmp/bio')
from bstyle import *
from bbuild import html_to_pdf, page_texts, doc, OUT, TABCSS
from pypdf import PdfReader, PdfWriter
import importlib, os
CH = os.environ.get('CH', '04')
L = importlib.import_module('ch'+CH+'_latt')

LCSS = """
body{font-size:11.6pt;line-height:1.55}
.lp{display:flex;align-items:center;gap:7pt;margin:0 0 6pt;font:700 8.4pt Carlito}
.lp .p1{background:var(--g2);color:#fff;padding:2pt 7pt;border-radius:4pt;letter-spacing:.8pt}
.lp .p1.ova{background:#e0782f}
.lp .dots{display:flex;gap:3pt}.lp .dots i{display:block;width:14pt;height:5pt;border-radius:3pt;background:#cfe2d3}.lp .dots i.on{background:var(--g2)}
.lp span.t{color:var(--mut);font-weight:400;font-size:8.6pt}
h2.lh{font:700 22pt Carlito;color:var(--g1);margin:0 0 8pt}
.t p{margin:0 0 9pt;font-size:11.6pt}
.fig img{border-radius:10pt}
.kom{display:flex;gap:10pt;align-items:center;background:#fff3cf;border-radius:10pt;padding:10pt 14pt;margin-top:12pt;break-inside:avoid}
.kom .ex{flex:none;width:24pt;height:24pt;border-radius:50%;background:#e3b32c;color:#fff;font:700 14pt/24pt Carlito;text-align:center}
.kom .lb{font:700 7.8pt Carlito;letter-spacing:1pt;color:#a8651a;display:block}
.kom .tx{font:12pt/1.4 Carlito}
.ex1{margin:0 0 14pt;break-inside:avoid}
.ex1 .hd{display:flex;gap:8pt;align-items:flex-start}
.ex1 .hd>div{flex:1;min-width:0}
.sf{margin-left:0!important;width:100%!important}.ln,.fy p,.dr,.sort,.nrbox{margin-left:0!important}.bank{margin-left:0!important}
.ex1 .no{flex:none;width:17pt;height:17pt;border-radius:50%;background:#e0782f;color:#fff;font:700 10pt/17pt Carlito;text-align:center}
.ex1 .ty{font:700 7.6pt Carlito;letter-spacing:1pt;color:#e0782f;display:block}
.ex1 .q{font:700 11.4pt/1.35 Carlito;display:block;margin:0;grid-template-columns:none}
.chips{display:flex;gap:7pt;flex-wrap:wrap;margin:6pt 0 0 25pt}
.chips span{border:1pt solid #cfd6d0;border-radius:14pt;padding:3pt 11pt;font:10.4pt Carlito}
.sort{display:flex;gap:7pt;flex-wrap:wrap;margin:6pt 0 0 25pt}
.sort div{width:48pt;text-align:center;font:10.4pt Carlito}
.sort div b{display:block;border:1pt solid #cfd6d0;border-radius:6pt;padding:3pt 0;font-weight:400}
.sort div i{display:block;width:18pt;height:18pt;border:1.3pt solid #9aa;border-radius:4pt;margin:4pt auto 0}
.bank{display:inline-block;background:#e4edf5;border-radius:6pt;padding:3pt 10pt;font:10.4pt Carlito;margin:5pt 0 6pt 25pt}
.fy p{margin:0 0 7pt 25pt;font:11pt Carlito}
.ln{margin:5pt 0 0 25pt;font:10.6pt Carlito}.ln i{display:block;height:17pt;border-bottom:.8pt solid #aab}
.dr{display:grid;grid-template-columns:1fr 1fr;gap:6pt 40pt;margin:6pt 0 0 25pt;font:10.6pt Carlito}
.dr div{border:1pt solid #cfd6d0;border-radius:5pt;padding:3pt 9pt;position:relative}
.sf{margin:6pt 0 0 25pt;font:10.6pt Carlito;width:calc(100% - 25pt)}.sf table{width:100%;border-collapse:collapse}
.sf td{padding:4pt 2pt;border-bottom:.6pt solid #e2e2e2}.sf th{font:700 9pt Carlito;text-align:center;width:40pt}
.sf b.bx{display:inline-block;width:12pt;height:12pt;border:1.2pt solid #9aa;border-radius:3pt}
.bx2{display:inline-block;width:11pt;height:11pt;border:1.2pt solid #9aa;border-radius:3pt;margin-right:5pt;vertical-align:-1pt}
.sf td.c{text-align:center}
.nrbox{margin:6pt 0 0 25pt;font:10.6pt Carlito}.nrbox div{display:flex;gap:8pt;align-items:center;margin:0 0 5pt}.nrbox i{display:inline-block;width:17pt;height:17pt;border:1.2pt solid #9aa;border-radius:4pt}
.ord2{display:grid;grid-template-columns:1fr 1fr;gap:6pt;margin-top:8pt}
.ord2 div{background:#f4f9f3;border-radius:6pt;padding:6pt 9pt;font:9.6pt/1.3 Carlito}.ord2 b{display:block;color:var(--g2);font-size:10.6pt}
.stp{display:grid;grid-template-columns:repeat(4,1fr);gap:8pt;margin:6pt 0 12pt}
.stp div{background:#fff;border:1pt solid #e4e4e4;border-radius:8pt;padding:7pt 8pt;font:9.4pt/1.3 Carlito}
.stp b{display:inline-block;width:14pt;height:14pt;border-radius:50%;background:var(--g2);color:#fff;font:700 8.5pt/14pt Carlito;text-align:center;margin-bottom:3pt}
.vik{display:grid;grid-template-columns:70pt 1fr;gap:10pt;align-items:center;margin:0 0 9pt;font:11.4pt/1.35 Carlito}
.vik img{width:70pt;border-radius:5pt}
.sub h3{margin-top:6pt}
"""

def esc_ex(n, typ, label, inner):
    return f'<div class="ex1"><div class="hd"><span class="no">{n}</span><div><span class="ty">{label}</span>{inner}</div></div></div>'

def ex_html(n, e):
    k = e[0]
    if k == "sortera":
        return esc_ex(n, k, "SORTERA", f'<span class="q">{e[1]}</span><div class="sort">' + "".join(f"<div><b>{x}</b><i></i></div>" for x in e[2]) + '</div>')
    if k == "ringa":
        return esc_ex(n, k, "RINGA IN", f'<span class="q">{e[1]}</span><div class="chips">' + "".join(f"<span>{x}</span>" for x in e[2]) + '</div>')
    if k == "fyll":
        return esc_ex(n, k, "FYLL I", '<span class="q">Skriv rätt ord på linjen.</span><span class="bank">Ord att välja: ' + " · ".join(e[1]) + '</span><div class="fy">' + "".join(f"<p>{x}</p>" for x in e[2]) + '</div>')
    if k == "skriv":
        return esc_ex(n, k, "SKRIV", f'<span class="q">{e[1]}</span><div class="ln">{e[2]}' + "<i></i>" * e[3] + '</div>')
    if k == "skriv3":
        return esc_ex(n, k, "SKRIV", f'<span class="q">{e[1]}</span><div class="ln"><p>______________ → ______________ → ______________</p></div>')
    if k == "skriv2":
        return esc_ex(n, k, "SKRIV", f'<span class="q">{e[1]}</span><div class="ln">' + "".join(f"<p>{x}<i></i></p>" for x in e[2]) + '</div>')
    if k == "rita":
        return esc_ex(n, k, "RITA OCH SKRIV", f'<span class="q">{e[1]}</span><div class="ln">' + "<i></i>" * 6 + '</div>')
    if k == "streck":
        import random
        return esc_ex(n, k, "DRA STRECK", f'<span class="q">{e[1]}</span><div class="dr">' + "".join(f"<div>{a}</div><div>{b}</div>" for a, b in zip(e[2], e[3])) + '</div>')
    if k == "sf":
        return esc_ex(n, k, "SANT ELLER FALSKT", f'<span class="q">{e[1]}</span><div class="sf"><table><tr><th></th><th>Sant</th><th>Falskt</th></tr>' + "".join(f'<tr><td>{x}</td><td class="c"><b class="bx"></b></td><td class="c"><b class="bx"></b></td></tr>' for x in e[2]) + '</table></div>')
    if k == "kryssa":
        return esc_ex(n, k, "KRYSSA", f'<span class="q">{e[1]}</span><div class="dr">' + "".join(f"<div><b class='bx2'></b> {x}</div>" for x in e[2]) + '</div>')
    if k == "siffror":
        return esc_ex(n, k, "SKRIV SIFFROR", f'<span class="q">{e[1]}</span><div class="nrbox">' + "".join(f"<div><i></i>{x}</div>" for x in e[2]) + '</div>')
    raise ValueError(k)

def prog(i, typ):
    return ('<div class="lp"><span class="p1' + (' ova' if typ == 'ÖVA' else '') + f'">{typ}</span><span class="t">Del {i} av {L.NDEL}</span><span class="dots">'
            + "".join(f'<i class="{"on" if j < i else ""}"></i>' for j in range(L.NDEL)) + '</span></div>')

def lasa_page(i, d):
    h = '<section class="sec">' + prog(i, 'LÄS') + f'<h2 class="lh">{d["titel"]}</h2><div class="t">'
    for p in d['fore']: h += (p if p.startswith('<h3') else f"<p>{p}</p>")
    if 'sub1' in d:
        for key in ('sub1', 'sub2'):
            t, ps, f = d[key]
            h += f'<div class="sub"><h3>{t}</h3>' + "".join(f"<p>{p}</p>" for p in ps) + fig(L.FIG + f, w="82%") + '</div>'
    else:
        if d.get('fig'): h += fig(L.FIG + d['fig'], w=d.get('figw'))
        for p in d['efter'][:2] if d.get('fig2') else d['efter']: h += (p if p.startswith('<h3') else f"<p>{p}</p>")
        if d.get('fig2'):
            h += fig(L.FIG + d['fig2'], w="88%")
    h += '</div>'
    h += f'<div class="kom"><span class="ex">!</span><div><span class="lb">KOM IHÅG</span><span class="tx">{d["kom"]}</span></div></div></section>'
    return h

def ova_page(i, d):
    h = '<section class="sec">' + prog(i, 'ÖVA') + f'<h2 class="lh">Öva: Del {i}</h2>'
    for n, e in enumerate(d['ova'], 1): h += ex_html(n, e)
    return h + '</section>'

def ord_page():
    h = ('<section class="sec"><div class="sh"><h2>Viktiga ord</h2></div><p>Läs orden och titta på bilderna. Du kan komma tillbaka hit när du läser.</p>'
         + fig(L.ORD_FIG) + '<div class="ord2">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in L.ORD_EXTRA) + '</div></section>')
    return h

def viktigast_page():
    h = '<section class="sec"><div class="sh"><h2>Det viktigaste</h2></div><p>Här är allt det viktigaste i kapitlet. Läs det en gång till.</p>'
    for ic, t in L.VIKTIGAST:
        img = f'<img src="file://{L.FIG}{ic}">' if ic else '<div></div>'
        h += f'<div class="vik">{img}<span>{t}</span></div>'
    return h + '</section>'

def test_pages():
    h = '<section class="sec"><div class="sh"><h2>Testa dig själv</h2></div><p>Nu får du visa vad du har lärt dig. Du kan titta i kapitlet om du vill.</p>'
    for n, e in enumerate(L.TEST, 1):
        h += ex_html(n, e)
    return h + '</section>'

def first_page():
    cards = "".join(f'<div><b>{i}</b><br>{t}</div>' for i, t in enumerate(L.SA_GOR, 1))
    lara = "".join(f"<li>{x}</li>" for x in L.LARA)
    return f"""<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(f'Kapitel {L.NR} · {L.NAMN} · Lättläst', 1)}{LCSS}
@page{{margin:0}}
body{{margin:0}}
.cv img{{width:210mm;height:87.6mm;display:block}}
.band{{background:#2f6b4f;color:#fff;height:36mm;padding:7mm 18mm 0}}
.band h1{{font:700 34pt Carlito;margin:0}}.band p{{font:15pt Carlito;margin:3pt 0 0}}
.in{{padding:8mm 18mm 0}}
.in p{{font-size:12pt}}
.lar{{background:#e7eef5;border-radius:8pt;padding:11pt 14pt;margin-top:10pt;font:11pt/1.4 Carlito}}
.lar .rb{{font:700 8.4pt Carlito;letter-spacing:1pt;color:#2b5d7a;margin-bottom:5pt;display:block}}
.lar ul{{margin:0;padding-left:13pt}}
h3.sg{{font:700 14pt Carlito;color:var(--g2);margin:12pt 0 4pt}}
.ft{{position:absolute;left:18mm;right:14.8mm;bottom:11mm;display:flex;justify-content:space-between;font:8.4pt Carlito;color:#6b625b}}
.ft b{{color:#2f6b4f;font-size:8.8pt}}
</style></head><body><div class="cv"><img src="file://{L.FIG}cover_lattlast.png"></div>
<div class="band"><h1>{L.NAMN}</h1><p>{L.UNDER}</p></div>
<div class="in"><p>{L.INTRO_L[0]}</p><p>{L.INTRO_L[1]}</p>
<h3 class="sg">Så här gör du</h3><div class="stp">{cards}</div>
<div class="lar"><span class="rb">DET HÄR SKA DU LÄRA DIG</span><ul>{lara}</ul></div></div>
<div class="ft"><span>Kapitel {L.NR} · {L.NAMN} · Lättläst</span><b>1</b></div></body></html>"""

def teacher_page(start):
    pk = "".join(f"<li>{x}</li>" for x in L.TILL_PUNKTER)
    f = "".join(f"<p>{x}</p>" for x in L.FACIT)
    return ('<section class="sec teacher"><h2>Till läraren</h2><h3>Om den lättlästa versionen</h3><p>' + L.TILL_LARAREN + '</p><ul class="pu">' + pk + '</ul><p>' + L.TILL_TIPS + '</p>'
            '<h3>Facit – övningar</h3><div class="cols2">' + f + '</div></section>')

def build(komplett=True):
    body = ord_page()
    for i, d in enumerate(L.DELAR, 1):
        body += lasa_page(i, d) + ova_page(i, d)
    body += viktigast_page() + test_pages()
    foot = f'Kapitel {L.NR} · {L.NAMN} · Lättläst'
    def full(b, start): return (f'<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(foot, start)}{LCSS}{TABCSS(L.TAB)}</style></head><body>{b}</body></html>')
    tmp = f'{OUT}/_latt_body.pdf'
    html_to_pdf(full(body, 2), tmp)
    n = len(PdfReader(tmp).pages)
    p1 = f'{OUT}/_latt_p1.pdf'
    html_to_pdf(first_page(), p1)
    w = PdfWriter()
    for f in (p1, tmp):
        for pg in PdfReader(f).pages: w.add_page(pg)
    name = f'{OUT}/biologi-{L.NR}-{L.SLUG}-lattlast.pdf'
    w.write(name)
    res = {'lattlast': name}
    if komplett:
        t2 = f'{OUT}/_latt_teacher.pdf'
        html_to_pdf(full(teacher_page(n + 2), n + 2), t2)
        w2 = PdfWriter()
        for f in (name, t2):
            for pg in PdfReader(f).pages: w2.add_page(pg)
        name2 = f'{OUT}/biologi-{L.NR}-{L.SLUG}-lattlast-komplett.pdf'
        w2.write(name2); res['lattlast-komplett'] = name2
    return res

if __name__ == '__main__':
    print(build())

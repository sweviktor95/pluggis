# -*- coding: utf-8 -*-
import sys, os, json, re, importlib, copy
sys.path.insert(0,'/tmp/kemi')
import render as R
from build import cover as _c, intro_page, uppg_html, samman_html, FOOT, wrap as _w, render as prender
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
SC=json.load(open('/tmp/kemi/scenes.json'))
OUT='/tmp/kemi/out'; REPO='/mnt/user-data/outputs/pluggis'
# tema
CSS=R.CSS.replace('--acc:#b4452f','--acc:#1d6b78').replace('--acc2:#e9b44c','--acc2:#4fb6bf').replace('--soft:#fdf1e7','--soft:#e8f4f5').replace('#fde4dc','#d6ebed').replace('#fff8f2','#f1f9f9').replace('#e5d3c4','#c9dfe1').replace('#fff3d6','#dff1f2')
CSS+="""
.tl{display:flex;margin:10pt 0 14pt;break-inside:avoid}
.tl .p{flex:1;border-top:3pt solid var(--acc);padding:6pt 4pt 0;position:relative;font-size:8.6pt;line-height:1.3}
.tl .p b{display:block;font:700 10pt Carlito;color:var(--acc)}
.tl .p:before{content:"";position:absolute;top:-6.5pt;left:4pt;width:9pt;height:9pt;border-radius:50%;background:var(--acc2);border:1.5pt solid var(--acc)}
.kalla{background:#e3f1f2;border-left:4pt solid var(--acc);border-radius:4pt;padding:7pt 12pt;margin:9pt 0;break-inside:avoid}
.kalla .kh{font:700 8pt Carlito;letter-spacing:.8pt;text-transform:uppercase;color:var(--acc)}
.kalla q{display:block;font-style:italic;margin:3pt 0}
.kalla .ku{font-size:8.8pt;color:#6b5d54}
.bildp{margin:8pt 0 10pt;break-inside:avoid}.bildp svg{width:100%;height:auto;border-radius:8pt;display:block}.bildp .bt{font-size:8.6pt;color:#6b5d54;margin-top:3pt}
.lab{border:1.6pt solid var(--acc);border-radius:9pt;padding:9pt 14pt;margin:12pt 0}
.lab h3{margin:0 0 4pt;font-size:15pt;color:var(--acc)}
.lab ol,.lab ul{margin:3pt 0;padding-left:16pt}
.fac h5{font:700 9.4pt Carlito;margin:5pt 0 1pt}
.two{columns:2;column-gap:18pt}
.two li{break-inside:avoid}
"""
def block(b,kn=""):
    k=b[0]
    if k=="tidslinje":
        return '<div class="tl">'+"".join(f'<div class="p"><b>{a}</b>{t}</div>' for a,t in b[1])+'</div>'
    if k=="kalla":
        return f'<div class="kalla"><span class="kh">{b[1]}</span><q>{b[2]}</q><span class="ku">{b[3]}</span></div>'
    if k=="bild":
        return f'<div class="bildp">{SC[b[1]]}<div class="bt">{b[2]}</div></div>'
    return R.block(b,kn)
def sections(secs):
    out=""
    for s in secs:
        out+=f'<div class="sec"><div class="sec-head"><span class="badge">{s["nr"]}</span><h2>{s["titel"]}</h2></div><p class="intro">{s["intro"]}</p>'+"".join(block(b,s["nr"]) for b in s["block"])+"</div>"
    return out
def lab_html(L):
    lt=re.sub(r"^Kemilabbet:?\s*","",L["titel"])
    return f'<div class="lab"><h3>Kemilabbet: {lt}</h3><p><b>Syfte.</b> {L["syfte"]}</p><p><b>Material.</b> {L["material"]}</p><b>Gör så här</b><ol>'+"".join(f"<li>{x}</li>" for x in L["utforande"])+'</ol><b>Frågor</b><ol>'+"".join(f"<li>{q}</li>" for q,_ in L["fragor"])+'</ol></div>'
def cover(T,variant,scene):
    lab={"vanlig":"","lattlast":"Lättläst","fordjupning":"Fördjupning"}[variant]
    svg=SC.get(scene,SC['kemi']).replace('width="640" height="260"','width="100%" height="100%" preserveAspectRatio="xMidYMid slice"')
    return f"""<html><head><meta charset=utf-8><style>{CSS}
@page{{margin:0}}.cv{{height:297mm;position:relative;background:#fff}}.top{{height:140mm;position:relative;overflow:hidden}}.top svg{{position:absolute;inset:0;width:100%;height:100%}}
.kap{{position:absolute;left:18mm;top:14mm;font:700 11pt Carlito;letter-spacing:2pt;color:#fff;background:rgba(0,0,0,.35);padding:3pt 10pt;border-radius:6pt}}
.lab2{{position:absolute;right:18mm;top:14mm;font:700 11pt Carlito;background:#fff;color:var(--acc);padding:3pt 10pt;border-radius:6pt}}
.tit{{background:#0f3f48;color:#fff;padding:14mm 18mm 10mm;min-height:60mm}}.tit h1{{font-size:40pt;margin:0 0 3pt;line-height:1.05}}.tit p{{font:15pt Carlito;margin:0;color:#d3eef0}}
.under{{padding:10mm 18mm;color:#6b5d54;font:italic 12pt Lora}}</style></head><body><div class=cv><div class=top>{svg}<span class=kap>KAPITEL {T['nr']} · KEMI · ÅK {T['arskurs']}</span>{('<span class=lab2>'+lab+'</span>') if lab else ''}</div>
<div class=tit><h1>{T['namn']}</h1><p>{T['under']}</p></div><div class=under>Kemi för högstadiet · Pluggis · beta</div></div></body></html>"""
def lat_secs(secs):
    out=[]
    for s in secs:
        n=copy.deepcopy(s); n['intro']=s['intro'].split('. ')[0].rstrip('.')+'.'
        ps=0; nb=[]
        for b in n['block']:
            if b[0]=="p":
                ps+=1
                if ps>2: continue
            if b[0]=="ruta" and b[1] in("fakta","exempel"): continue
            nb.append(b)
        n['block']=nb; out.append(n)
    return out
def test_html(m,lat=False):
    A=m.TEST_A[:5] if lat else m.TEST_A; B=m.TEST_B[:4] if lat else m.TEST_B
    o='<div class="sec pb"><div class="sec-head"><h2>Testa dig själv</h2></div><h3 class="h">Del A · Välj rätt svar</h3><ol>'
    for q,opts,_ in A: o+=f'<li>{q}<div class="hint">'+"&nbsp;&nbsp;".join(f"<b>{chr(65+j)}</b> {x}" for j,x in enumerate(opts))+"</div></li>"
    o+='</ol><h3 class="h">Del B · Svara kort</h3><ol>'+"".join(f"<li>{q}</li>" for q,_ in B)+'</ol>'
    K=m.KALLA
    o+=f'<h3 class="h">Del C · Källan</h3><div class="kalla"><span class="kh">Källa</span><q>{K["text"]}</q><span class="ku">{K["ursprung"]}</span></div><ol>'+"".join(f"<li>{q}</li>" for q,_ in K["fragor"])+'</ol>'
    o+=f'<h3 class="h">Del D · Skriv</h3><p>{m.SKRIV["uppgift"]}</p></div>'
    return o
def facit(m,secs,U,A,B,lab=True):
    o='<div class="sec pb fac"><div class="sec-head"><h2>Facit</h2></div><h4>Kolla dig själv</h4>'
    for s in secs: o+=f"<p><b>{s['nr']}</b> "+" · ".join(f"{i}) {a}" for i,a in enumerate(s['svar'],1))+"</p>"
    o+="<h4>Uppgifter</h4>"+"".join(f"<p><b>{i}.</b> {u[4]}</p>" for i,u in enumerate(U,1))
    if A: o+="<h4>Del A</h4><p>"+", ".join(f"{i}) {chr(65+a[2])}" for i,a in enumerate(A,1))+"</p>"
    if B: o+="<h4>Del B</h4><p>"+"<br>".join(f"{i}) {a[1]}" for i,a in enumerate(B,1))+"</p>"
    if lab:
        o+="<h4>Del C · Källan</h4><p>"+"<br>".join(f"{i}) {a[1]}" for i,a in enumerate(m.KALLA['fragor'],1))+"</p>"
        o+="<h4>Kemilabbet</h4><p>"+"<br>".join(f"{i}) {a[1]}" for i,a in enumerate(m.LAB['fragor'],1))+"</p>"
    return o+"</div>"
def larar(m,fordj=False):
    o='<div class="sec pb fac"><div class="sec-head"><h2>Lärarhandledning</h2></div>'
    for t,tx in m.LARAR: o+=f"<h4>{t}</h4><p>{tx}</p>"
    o+=f"<h4>Bedömningsstöd, skrivuppgiften</h4><p>"+"<br>".join(m.SKRIV['stod'])+"</p>"
    o+=f"<h4>Bonuslabb / bonusuppgift</h4><p>{m.LAB['bonus']}</p>"
    o+='<h4>Förslag till Blooket</h4><ol class="two">'+"".join(f"<li>{q[0]} <em>({q[1]})</em></li>" for q in m.BLOOKET)+"</ol>"
    o+='<h4>Förslag till Jeopardy</h4><p>'+"<br>".join(f"<b>{c}:</b> "+"; ".join(f"{p} – {l} → {a}" for p,l,a in rows) for c,rows in m.JEOPARDY.items())+"</p>"
    o+='<h4>Källor</h4><ul>'+"".join(f'<li>{t}<br><span class="mini">{u}</span></li>' for t,u in m.KALLOR)+"</ul></div>"
    return o
def build_chapter(name):
    m=importlib.import_module(name); T=m.T
    scene=next((b[1] for s in m.S for b in s['block'] if b[0]=='bild'),'kemi')
    os.makedirs(OUT,exist_ok=True); res={}
    variants={
     "vanlig":lambda: intro_page(T,m.S)+sections(m.S)+lab_html(m.LAB)+uppg_html(m.UPPG)+'<div class="pb"></div>'+samman_html(m.SAMMAN,m.BEGREPP)+test_html(m),
     "lattlast":lambda: intro_page(T,m.S)+sections(lat_secs(m.S))+uppg_html(m.UPPG[:5])+'<div class="pb"></div>'+samman_html(m.SAMMAN[:5],m.BEGREPP[:8])+test_html(m,True),
     "fordjupning":lambda: intro_page(dict(T,mal=[f["titel"] for f in m.F],fundera="Det här häftet bygger vidare på kapitlet. Vilken del tror du blir svårast att förklara för en kompis?"),m.F)+sections(m.F)+uppg_html(m.F_UPPG)+'<div class="pb"></div>'+samman_html(m.F_SAMMAN,m.F_BEGR),
    }
    komp={
     "vanlig":lambda: facit(m,m.S,m.UPPG,m.TEST_A,m.TEST_B)+larar(m),
     "lattlast":lambda: facit(m,lat_secs(m.S),m.UPPG[:5],m.TEST_A[:5],m.TEST_B[:4])+larar(m),
     "fordjupning":lambda: facit(m,m.F,m.F_UPPG,[],[],lab=False)+larar(m),
    }
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page()
        for v,fn in variants.items():
            base=f"{OUT}/{T['fil']}-{v}"
            prender(pg,cover(T,v,scene),base+'-cover.pdf',cover=True)
            cls="lat" if v=="lattlast" else ""
            html=f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body class='{cls}'>{fn()}</body></html>"
            prender(pg,html,base+'-main.pdf',footer=f"Kapitel {T['nr']} · Kemi – {T['namn']}")
            prender(pg,f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body class='{cls}'>{komp[v]()}</body></html>",base+'-komp.pdf',footer=f"Kapitel {T['nr']} · Kemi – {T['namn']} · Lärarversion")
            for kk in (False,True):
                w=PdfWriter()
                for f in (base+'-cover.pdf',base+'-main.pdf')+((base+'-komp.pdf',) if kk else ()):
                    for pgx in PdfReader(f).pages: w.add_page(pgx)
                fn_=f"{OUT}/{T['fil']}-{v}{'-komplett' if kk else ''}.pdf"; w.write(fn_); res[(v,kk)]=fn_
        b.close()
    return res
if __name__=="__main__":
    for n in sys.argv[1:]: print(n,{k:v for k,v in build_chapter(n).items()})

# -*- coding: utf-8 -*-
import sys, os, json, re, importlib, glob, shutil
sys.path.insert(0,'/tmp/hist')
import render as R
REPO='/mnt/user-data/outputs/pluggis'
def RUTA(t,r,x): return f'<div class="ruta ruta-{t}"><span class="ruta-rubrik">{r}</span>{x}</div>'
def mini(head,rows): return '<table class="mini-tabell">'+("<thead><tr>"+"".join(f"<th>{c}</th>" for c in head)+"</tr></thead>" if head else "")+"<tbody>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)+"</tbody></table>"
def tosite(b):
    k=b[0]
    if k=="p": return b[1]
    if k=="ruta": return RUTA(b[1] if b[1] in("fakta","tank","visste","historia") else "fakta",b[2],b[3])
    if k=="tab": return mini(b[1],b[2])
    if k=="list": return "<ul>"+"".join(f"<li>{x}</li>" for x in b[1])+"</ul>"
    if k=="tidslinje": return mini(["År","Händelse"],[[a,t] for a,t in b[1]])
    if k=="kalla": return RUTA("historia",b[1],f"<em>{b[2]}</em><br><span class='sv'>{b[3]}</span>")
    return None
def sek(s):
    texts=[s['intro']]; kf=None; bild=None; bt=""
    for b in s['block']:
        if b[0]=="kolla": kf=b[1]; continue
        if b[0]=="bild":
            if bild is None: bild="bilder/historia-"+b[1]+".png"; bt=b[2]
            continue
        h=tosite(b)
        if h: texts.append(h)
    d=dict(ikon=s['ikon'],titel=s['nr']+" "+s['titel'],text=texts,kontrollfraga=" ".join(f"{i}. {q}" for i,q in enumerate(kf or [],1)),kontrollsvar=" ".join(f"{i}. {a}" for i,a in enumerate(s['svar'],1)))
    if bild: d['bild']=bild; d['bildText']=bt
    return d
def gen(mods):
    struct=[]; manifest=""; scripts=""
    for name in mods:
        m=importlib.import_module(name); T=m.T; nid=T['nodeid']
        sm={s['id']:s for s in m.S}; leaves=[]; js="// Genererad från historiekapitel %d (samma källa som häftet).\nvar innehall = window.innehall || {};\n\n"%T['nr']
        G=m.GRUPPER; nb=len(m.BEGREPP); per=(nb+len(G)-1)//len(G)
        for gi,(suf,tit,intro,ids) in enumerate(G):
            lid=f"{nid}-{suf}"; leaves.append((lid,tit))
            sek_=[sek(sm[i]) for i in ids]
            if gi==len(G)-1:
                K=m.KALLA; L=m.LAB
                sek_.append(dict(ikon="🔎",titel="Källan: öva källkritik",text=["Läs källan och svara på frågorna.",RUTA("historia","Källa",f"<em>{K['text']}</em><br><span class='sv'>{K['ursprung']}</span>")],kontrollfraga=" ".join(f"{i}. {q}" for i,(q,_) in enumerate(K['fragor'],1)),kontrollsvar=" ".join(f"{i}. {a}" for i,(_,a) in enumerate(K['fragor'],1))))
                sek_.append(dict(ikon="🧪",titel="Historikerns verkstad: "+re.sub(r"^Historikerns verkstad:?\s*","",L['titel']),text=[f"<strong>Syfte.</strong> {L['syfte']}",f"<strong>Material.</strong> {L['material']}","<strong>Gör så här</strong><ol>"+"".join(f"<li>{x}</li>" for x in L['utforande'])+"</ol>"],kontrollfraga=" ".join(f"{i}. {q}" for i,(q,_) in enumerate(L['fragor'],1)),kontrollsvar=" ".join(f"{i}. {a}" for i,(_,a) in enumerate(L['fragor'],1))))
            d=dict(intro=intro,sektioner=sek_,begrepp=[dict(term=a,forklaring=b) for a,b in m.BEGREPP[gi*per:(gi+1)*per]],exitTicket=[dict(fraga=q,svar=a) for q,a in m.TEST_B[gi*2:gi*2+2]])
            js+=f'innehall["{lid}"] = '+json.dumps(d,ensure_ascii=False,indent=1)+";\n\n"
        # tidsresa
        if m.SCEN:
            slug=T['fil'].replace('historia-','tr-'); lid=f"{nid}-tidsresa"; leaves.append((lid,"Tidsresa (spel)"))
            js+=f'innehall["{lid}"] = '+json.dumps(dict(text=f"Följ med på en tidsresa: {m.SCEN['titel']}. Läs om varje etapp och svara på frågan för att komma vidare. Din progression sparas i webbläsaren.",bild="",inbaddad=f"simuleringar/{slug}.html",inbaddadTitel=m.SCEN['titel']),ensure_ascii=False,indent=1)+";\n\n"
            sc=dict(m.SCEN); sc['id']=T['fil']
            open(f"{REPO}/simuleringar/{slug}.html","w").write(simhtml(sc))
        if T['nr']==9: leaves.append(("historia-varldskrigen-forsta","Kartsimulering: första världskriget"))
        if T['nr']==11: leaves += [("historia-varldskrigen-andra","Kartsimulering: andra världskriget"),("historia-dagen-d","Dagen D (spel)")]
        js+="window.innehall = innehall;\n"
        open(f"{REPO}/innehall/historia-{T['nr']:02d}.js","w").write(js)
        scripts+=f'<script src="innehall/historia-{T["nr"]:02d}.js"></script>\n'
        manifest+=f'''window.hafte["{nid}"] = {{
  titel: "Kapitel {T['nr']} – {T['namn']}",
  vanlig: "hafte/{T['fil']}-vanlig.pdf",
  lattlast: "hafte/{T['fil']}-lattlast.pdf",
  fordjupning: "hafte/{T['fil']}-fordjupning.pdf",
  komplett: {{
    vanlig: "hafte/{T['fil']}-vanlig-komplett.pdf",
    lattlast: "hafte/{T['fil']}-lattlast-komplett.pdf",
    fordjupning: "hafte/{T['fil']}-fordjupning-komplett.pdf"
  }}
}};
'''
        struct.append((T['arskurs'],T['nr'],f"Kapitel {T['nr']} – {T['namn']}",nid,leaves))
    return struct,manifest,scripts
def simhtml(sc):
    return f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{sc['titel']}</title><link rel="stylesheet" href="tr/stil.css"></head><body>
<div class="app"><div class="scene" id="scene"><svg id="svg" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice" aria-label="{sc['titel']}"><g id="far"></g><g id="world"></g></svg>
<div class="hud"><div class="clock" id="clock"><small>{sc['plats']}</small>{sc['tid']}</div><div class="steps" id="steps" aria-label="Framsteg"></div></div></div>
<div class="dock" id="dock" aria-live="polite"></div></div>
<script>window.SCEN={json.dumps(sc,ensure_ascii=False)};</script>
<script src="tr/assets.js"></script><script src="tr/motor.js"></script></body></html>'''
def write_struct(struct):
    ak={7:[],8:[],9:[]}
    for a,nr,tit,nid,leaves in sorted(struct):
        ak[a].append((tit,nid,leaves))
    def node(tit,nid,leaves,ind):
        sp=" "*ind
        return f'{sp}{{\n{sp}  id: "{nid}",\n{sp}  titel: "{tit}",\n{sp}  barn: [\n'+",\n".join(f'{sp}    {{ id: "{i}", titel: "{t}" }}' for i,t in leaves)+f"\n{sp}  ]\n{sp}}}"
    blocks=[]
    for a in (7,8,9):
        if not ak[a]: continue
        blocks.append(f'      {{\n        id: "historia-ak{a}",\n        titel: "Årskurs {a}",\n        barn: [\n'+",\n".join(node(t,n,l,10) for t,n,l in ak[a])+"\n        ]\n      }")
    return ",\n".join(blocks)
if __name__=="__main__":
    mods=sys.argv[1:]
    struct,manifest,scripts=gen(mods)
    p=f'{REPO}/innehall/struktur.js'; s=open(p).read()
    m=re.search(r'(id: "historia",\s*titel: "Historia \(beta\)",\s*ikon: "🏛️",\s*barn: \[\n)(.*?)(\n    \]\n  \},\n  \{\n    id: "bild")',s,re.S)
    assert m,"historia-nod hittades inte"
    s=s[:m.start(2)]+write_struct(struct)+s[m.end(2):]; open(p,'w').write(s)
    p=f'{REPO}/hafte/manifest.js'; s=open(p).read()
    s=re.sub(r'\n// ==== HISTORIA START ====.*?// ==== HISTORIA END ====\n','',s,flags=re.S)
    s+="\n// ==== HISTORIA START ====\n"+manifest+"// ==== HISTORIA END ====\n"; open(p,'w').write(s)
    p=f'{REPO}/index.html'; s=open(p).read()
    s=re.sub(r'<!-- HISTORIA START -->.*?<!-- HISTORIA END -->\n','',s,flags=re.S)
    s=s.replace('<script src="innehall/spanska-hola.js"></script>','<script src="innehall/spanska-hola.js"></script>\n<!-- HISTORIA START -->\n'+scripts+'<!-- HISTORIA END -->',1); open(p,'w').write(s)
    print("klart",len(mods))

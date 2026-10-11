# -*- coding: utf-8 -*-
import sys, os, json, re, importlib, glob, shutil
sys.path.insert(0,'/tmp/kemi')
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
            if bild is None: bild="bilder/kemi-"+b[1]+".png"; bt=b[2]
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
        sm={s['id']:s for s in m.S}; leaves=[]; js="// Genererad från kemikapitel %d (samma källa som häftet).\nvar innehall = window.innehall || {};\n\n"%T['nr']
        G=m.GRUPPER; nb=len(m.BEGREPP); per=(nb+len(G)-1)//len(G)
        for gi,(suf,tit,intro,ids) in enumerate(G):
            lid=f"{nid}-{suf}"; leaves.append((lid,tit))
            sek_=[sek(sm[i]) for i in ids]
            if gi==len(G)-1:
                K=m.KALLA; L=m.LAB
                sek_.append(dict(ikon="🔎",titel="Källan: öva källkritik",text=["Läs källan och svara på frågorna.",RUTA("historia","Källa",f"<em>{K['text']}</em><br><span class='sv'>{K['ursprung']}</span>")],kontrollfraga=" ".join(f"{i}. {q}" for i,(q,_) in enumerate(K['fragor'],1)),kontrollsvar=" ".join(f"{i}. {a}" for i,(_,a) in enumerate(K['fragor'],1))))
                sek_.append(dict(ikon="🧪",titel="Kemilabbet: "+re.sub(r"^Kemilabbet:?\s*","",L['titel']),text=[f"<strong>Syfte.</strong> {L['syfte']}",f"<strong>Material.</strong> {L['material']}","<strong>Gör så här</strong><ol>"+"".join(f"<li>{x}</li>" for x in L['utforande'])+"</ol>"],kontrollfraga=" ".join(f"{i}. {q}" for i,(q,_) in enumerate(L['fragor'],1)),kontrollsvar=" ".join(f"{i}. {a}" for i,(_,a) in enumerate(L['fragor'],1))))
            d=dict(intro=intro,sektioner=sek_,begrepp=[dict(term=a,forklaring=b) for a,b in m.BEGREPP[gi*per:(gi+1)*per]],exitTicket=[dict(fraga=q,svar=a) for q,a in m.TEST_B[gi*2:gi*2+2]])
            js+=f'innehall["{lid}"] = '+json.dumps(d,ensure_ascii=False,indent=1)+";\n\n"
        js+="window.innehall = innehall;\n"
        open(f"{REPO}/innehall/kemi-{T['nr']:02d}.js","w").write(js)
        scripts+=f'<script src="innehall/kemi-{T["nr"]:02d}.js"></script>\n'
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

if __name__=="__main__":
    mods=sys.argv[1:]
    struct,manifest,scripts=gen(mods)
    p=f'{REPO}/hafte/manifest.js'; t=open(p).read()
    old=re.search(r'\n// ==== KEMI START ====\n(.*?)// ==== KEMI END ====\n',t,re.S)
    prev=old.group(1) if old else ""
    for blk in re.findall(r'window\.hafte\["[^"]+"\] = \{.*?\n\};\n',manifest,re.S):
        k=re.search(r'window\.hafte\["([^"]+)"\]',blk).group(1)
        prev=re.sub(r'window\.hafte\["'+re.escape(k)+r'"\] = \{.*?\n\};\n','',prev,flags=re.S)+blk
    t=re.sub(r'\n// ==== KEMI START ====.*?// ==== KEMI END ====\n','',t,flags=re.S)
    t+="\n// ==== KEMI START ====\n"+prev+"// ==== KEMI END ====\n"; open(p,'w').write(t)
    p=f'{REPO}/index.html'; t=open(p).read()
    m_=re.search(r'<!-- KEMI START -->\n(.*?)<!-- KEMI END -->\n',t,re.S)
    allsc=set((m_.group(1) if m_ else "").splitlines())|set(scripts.splitlines())
    allsc="".join(x+"\n" for x in sorted(allsc) if x.strip())
    t=re.sub(r'<!-- KEMI START -->.*?<!-- KEMI END -->\n','',t,flags=re.S)
    t=t.replace('<!-- HISTORIA END -->\n','<!-- HISTORIA END -->\n<!-- KEMI START -->\n'+allsc+'<!-- KEMI END -->\n',1); open(p,'w').write(t)
    print("klart",len(mods))

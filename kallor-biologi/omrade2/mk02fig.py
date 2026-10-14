# -*- coding: utf-8 -*-
import sys, random, math
sys.path.insert(0,'/tmp/figs')
from svgkit import *
from playwright.sync_api import sync_playwright
OUT='/tmp/bio/fig02n/'
def render(name, svg, w, h, scale=2):
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=scale)
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.screenshot(path=OUT+name+'.png', omit_background=False); b.close()
    print(name)

# ---------- omslag: mikroskopvy av celler
def cover(sky, pill_col, name, variant):
    W,H=1818,759
    random.seed({'v':4,'l':9,'f':2}[variant])
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Carlito">'
    s+=f'<defs><radialGradient id="bg" cx="50%" cy="50%" r="75%"><stop offset="0" stop-color="{sky[0]}"/><stop offset="1" stop-color="{sky[1]}"/></radialGradient></defs>'
    s+=f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
    # växtceller till vänster (celler med vägg), djurceller till höger, bakterier
    def plant(x,y,w,h,rot=0):
        o=f'<g transform="rotate({rot} {x} {y})"><rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="14" fill="#cfe8b5" stroke="#4d8a3e" stroke-width="6"/>'
        o+=f'<rect x="{x-w/2+14}" y="{y-h/2+14}" width="{w-28}" height="{h-28}" rx="8" fill="#e6f4d6" stroke="#8fbf70" stroke-width="2"/>'
        o+=f'<ellipse cx="{x+w*0.12}" cy="{y}" rx="{w*0.26}" ry="{h*0.28}" fill="#f4fbea" opacity=".85"/>'
        o+=f'<circle cx="{x-w*0.28}" cy="{y-h*0.08}" r="{min(w,h)*0.14}" fill="#8a6bb0" stroke="#5d4682" stroke-width="3"/>'
        for dx,dy in [(-.3,.28),(.3,-.3),(.34,.3),(-.05,-.33)]:
            o+=f'<ellipse cx="{x+w*dx}" cy="{y+h*dy}" rx="14" ry="8" fill="#3f9a4f" stroke="#256b34" stroke-width="2"/>'
        return o+'</g>'
    def animal(x,y,r):
        pts=[]
        n=60
        for i in range(n):
            a=2*math.pi*i/n; rr=r*(1+0.07*math.sin(3*a+x))
            pts.append((x+rr*math.cos(a), y+rr*math.sin(a)*0.86))
        d='M'+' L'.join(f'{px:.1f},{py:.1f}' for px,py in pts)+'Z'
        o=f'<path d="{d}" fill="#fadcc8" stroke="#d98a63" stroke-width="6" stroke-linejoin="round"/>'
        o+=f'<circle cx="{x-r*0.1}" cy="{y}" r="{r*0.33}" fill="#b79ad6" stroke="#6f4f9c" stroke-width="4"/><circle cx="{x-r*0.14}" cy="{y-r*0.05}" r="{r*0.1}" fill="#6f4f9c"/>'
        for dx,dy in [(.5,.3),(-.55,-.3),(.3,-.5),(-.35,.45)]:
            o+=f'<ellipse cx="{x+r*dx}" cy="{y+r*dy}" rx="{r*0.15}" ry="{r*0.08}" fill="#e98a4a" stroke="#b5561e" stroke-width="2" transform="rotate(30 {x+r*dx} {y+r*dy})"/>'
        return o
    def bact(x,y,rot):
        return (f'<g transform="rotate({rot} {x} {y})"><rect x="{x-34}" y="{y-12}" width="68" height="24" rx="12" fill="#bfe0f2" stroke="#3b7ba8" stroke-width="4"/>'
                f'<path d="M{x-20},{y} q8,-7 14,0 t14,0" fill="none" stroke="#26506f" stroke-width="2.5"/></g>')
    # rutnät av växtceller
    for r_ in range(6):
        for c_ in range(5):
            x=60+c_*150+(r_%2)*40; y=70+r_*130
            if x<760: s+=plant(x,y,140,120)
    for (x,y,r) in [(1180,200,120),(1400,420,140),(1010,520,110),(1640,160,100),(1600,640,95),(1260,640,80)]:
        s+=animal(x,y,r)
    for (x,y,rt) in [(940,150,20),(1500,300,-30),(900,380,60),(1130,380,10),(1720,430,40),(1330,90,-15),(1050,700,-20)]:
        s+=bact(x,y,rt)
    s+=f'<rect x="156" y="103" width="226" height="72" rx="36" fill="#fff"/><text x="269" y="152" font-size="34" font-weight="700" letter-spacing="3" text-anchor="middle" fill="{pill_col}">KAPITEL 2</text>'
    s+='</svg>'
    render(name, s, W, H, 1)
cover(("#e9f5e6","#b8dcc0"),"#2f6b4f","cover_vanlig","v")
cover(("#fdf3dc","#f0cf9a"),"#a85a22","cover_lattlast","l")
cover(("#e6e9f6","#aab4dc"),"#34407a","cover_fordjupning","f")

# ---------- Bild: specialiserade celler
def panelsvg(W,H,body,bg="#f3f8f1"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Carlito">'
            f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5d6b75"/></marker></defs>'
            f'<rect width="{W}" height="{H}" rx="18" fill="{bg}"/>{body}</svg>')
def T(x,y,s,size=22,fill="#24323c",w="400",a="middle"): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
W,H=1450,470
b=''
cards=[("Muskelcell","Drar ihop sig och ger rörelse"),("Nervcell","Skickar signaler, kan vara lång"),("Röd blodkropp","Transporterar syre"),("Rothårscell","Tar upp vatten ur jorden"),("Palisadcell","Fotosyntes i bladet")]
cw=270; gap=20
for i,(n,d) in enumerate(cards):
    x=20+i*(cw+gap)
    b+=f'<rect x="{x}" y="20" width="{cw}" height="430" rx="16" fill="#fff"/>'
    cx=x+cw/2
    if i==0:
        b+=f'<rect x="{cx-100}" y="120" width="200" height="60" rx="30" fill="#e8908a" stroke="#b5453d" stroke-width="3"/>'
        for k in range(8): b+=f'<line x1="{cx-80+k*22}" y1="128" x2="{cx-80+k*22}" y2="172" stroke="#c8605a" stroke-width="3"/>'
        for xx in (cx-30,cx+30): b+=f'<ellipse cx="{xx}" cy="150" rx="9" ry="6" fill="#8a6bb0"/>'
        b+=f'<rect x="{cx-100}" y="200" width="200" height="50" rx="25" fill="#e8908a" stroke="#b5453d" stroke-width="3"/>'
        for k in range(8): b+=f'<line x1="{cx-80+k*22}" y1="207" x2="{cx-80+k*22}" y2="243" stroke="#c8605a" stroke-width="3"/>'
        b+=f'<ellipse cx="{cx}" cy="225" rx="9" ry="6" fill="#8a6bb0"/>'
    if i==1:
        b+=f'<circle cx="{cx-60}" cy="190" r="34" fill="#f1d68a" stroke="#b8902a" stroke-width="3"/><circle cx="{cx-60}" cy="190" r="12" fill="#8a6bb0"/>'
        for ang in (200,250,300,150):
            a=math.radians(ang); b+=f'<path d="M{cx-60+30*math.cos(a)},{190+30*math.sin(a)} L{cx-60+70*math.cos(a)},{190+70*math.sin(a)}" stroke="#b8902a" stroke-width="4" fill="none" stroke-linecap="round"/>'
        b+=f'<path d="M{cx-26},192 C{cx+10},192 {cx+10},215 {cx+50},215 L{cx+110},215" stroke="#b8902a" stroke-width="6" fill="none" stroke-linecap="round"/>'
        for k in range(3): b+=f'<circle cx="{cx+60+k*22}" cy="215" r="3.5" fill="#fff" stroke="#b8902a" stroke-width="2"/>'
    if i==2:
        b+=f'<ellipse cx="{cx}" cy="200" rx="68" ry="68" fill="#d9483e" stroke="#9a2a22" stroke-width="3"/><ellipse cx="{cx}" cy="200" rx="30" ry="30" fill="#b53028"/>'
    if i==3:
        b+=f'<rect x="{cx-45}" y="100" width="90" height="100" rx="12" fill="#dff0d0" stroke="#4d8a3e" stroke-width="4"/><circle cx="{cx}" cy="140" r="14" fill="#8a6bb0"/>'
        b+=f'<path d="M{cx-14},200 L{cx-10},265 L{cx+10},265 L{cx+14},200Z" fill="#dff0d0" stroke="#4d8a3e" stroke-width="4"/>'
        for xx in (-25,0,25): b+=f'<circle cx="{cx+xx}" cy="285" r="3" fill="#3b7ba8"/>'
    if i==4:
        b+=f'<rect x="{cx-38}" y="95" width="76" height="170" rx="14" fill="#cfe8b5" stroke="#4d8a3e" stroke-width="4"/>'
        for (dx,dy) in [(-18,120),(10,150),(-14,185),(14,215),(-8,245),(16,118)]: b+=f'<ellipse cx="{cx+dx}" cy="{dy}" rx="13" ry="8" fill="#3f9a4f" stroke="#256b34" stroke-width="2"/>'
        b+=f'<circle cx="{cx}" cy="180" r="10" fill="#8a6bb0"/>'
    b+=T(cx,340,n,26,"#24323c","700")+T(cx,375,d.split(' ')[0]+' '+' '.join(d.split(' ')[1:3]),19,"#5d6b75")
    b+=T(cx,400," ".join(d.split(' ')[3:]),19,"#5d6b75")
render('spec-celler', panelsvg(W,H,b), W,H, 1)

# ---------- Bild: kork (Hooke)
W,H=1000,330
b=''
b+=f'<rect x="40" y="40" width="360" height="250" rx="14" fill="#e9d5b0" stroke="#b08f55" stroke-width="3"/>'
for r in range(6):
    for c in range(9):
        b+=f'<rect x="{62+c*38+ (r%2)*0}" y="{58+r*38}" width="30" height="30" rx="4" fill="#f6ead0" stroke="#a3834a" stroke-width="2"/>'
b+=T(220,320,"Korkbit, som Hooke såg den",20,"#5d6b75")
b+=f'<path d="M420,165 L560,165" stroke="#5d6b75" stroke-width="4" marker-end="url(#ah)"/>'+T(490,145,"mikroskop",19,"#5d6b75")
b+='<clipPath id="cp"><circle cx="780" cy="165" r="124"/></clipPath><circle cx="780" cy="165" r="130" fill="#fffdf6" stroke="#8a7a5a" stroke-width="6"/><g clip-path="url(#cp)">'
for r in range(9):
    for c in range(9):
        b+=f'<rect x="{640+c*32}" y="{35+r*32}" width="27" height="27" rx="3" fill="#f6ead0" stroke="#a3834a" stroke-width="2.5"/>'
b+='</g>'
b+=T(780,325,"Små ”rum” – Hooke kallade dem celler (1665)",20,"#5d6b75")
render('kork', panelsvg(W,H,b,"#faf6ec"), W,H, 1)

# ---------- Bild: växtens gasutbyte dag/natt
W,H=1430,420
b=''
def plant(x,sun,tag):
    o=f'<rect x="{x}" y="20" width="680" height="380" rx="16" fill="{"#fff8de" if sun else "#e3e8f4"}"/>'
    o+=T(x+340,58,tag,26,"#24323c","700")
    # blad
    o+=f'<path d="M{x+240},300 C{x+240},170 {x+340},120 {x+450},130 C{x+450},230 {x+360},300 {x+240},300Z" fill="#7fbf6a" stroke="#3f7d4f" stroke-width="4"/><path d="M{x+250},295 L{x+440},140" stroke="#3f7d4f" stroke-width="3"/>'
    return o
b+=plant(20,True,"Dag, i ljus: båda processerna pågår")
b+=plant(730,False,"Natt: bara cellandning")
# dag
b+=f'<circle cx="150" cy="120" r="30" fill="#f2c744"/>'
b+=T(110,200,"koldioxid",20,"#5d6b75")+f'<path d="M60,215 L255,250" stroke="#3b7ba8" stroke-width="5" marker-end="url(#ah)"/>'
b+=f'<path d="M470,200 L640,160" stroke="#c64f3f" stroke-width="5" marker-end="url(#ah)"/>'+T(590,145,"syre ut",19,"#5d6b75")
b+=T(350,350,"Fotosyntes binder koldioxid och bildar glukos + syre",20,"#3f7d4f","700")
b+=T(350,378,"Cellandning pågår samtidigt men sker i mindre skala",19,"#5d6b75")
# natt
b+=f'<path d="M1040,100 a28,28 0 1 0 22,44 a22,22 0 1 1 -22,-44z" fill="#f4e7a0"/>'
b+=f'<path d="M790,230 L965,260" stroke="#c64f3f" stroke-width="5" marker-end="url(#ah)"/>'+T(840,215,"syre",20,"#5d6b75")
b+=f'<path d="M1175,200 L1340,165" stroke="#3b7ba8" stroke-width="5" marker-end="url(#ah)"/>'
b+=T(1300,145,"koldioxid ut",19,"#5d6b75")
b+=T(1060,350,"Ingen fotosyntes utan ljus: växten tar upp syre och",20,"#34407a","700")+T(1060,378,"släpper ut koldioxid, som alla andra levande celler",19,"#5d6b75")
render('dagnatt', panelsvg(W,H,b,"#ffffff"), W,H, 1)

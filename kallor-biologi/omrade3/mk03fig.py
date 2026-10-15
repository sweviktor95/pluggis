# -*- coding: utf-8 -*-
import sys, math, random
sys.path.insert(0,'/tmp/bio')
import cellkit as K
from cellkit import T, svg, render
K.OUT='/tmp/bio/fig03n/'
INK="#24323c"; MUT="#5d6b75"

# ---------- småformer -----------------------------------------------------------
def spruce(x,y,h,col="#2f6b4f",dark="#245a40"):
    w=h*0.42; o=f'<rect x="{x-h*0.03}" y="{y-h*0.12}" width="{h*0.06}" height="{h*0.12}" fill="#6b4a2f"/>'
    for i in range(5):
        top=y-h*0.12-h*0.88*(1-i*0.19)+0; yb=y-h*0.12-h*0.8*i*0.2
        ww=w*(1-i*0.17)/2; hh=h*0.28
        o+=f'<path d="M{x},{yb-hh} L{x+ww},{yb} L{x-ww},{yb} Z" fill="{col if i%2==0 else dark}"/>'
    return o
def birch(x,y,h):
    o=f'<rect x="{x-h*0.025}" y="{y-h*0.6}" width="{h*0.05}" height="{h*0.6}" fill="#efe9dc"/>'
    for k in range(5): o+=f'<rect x="{x-h*0.025}" y="{y-h*0.5+k*h*0.1}" width="{h*0.05}" height="{h*0.012}" fill="#3b3a36"/>'
    for (dx,dy,r) in [(0,-0.68,.2),(-.12,-.55,.14),(.13,-.57,.15),(0,-.82,.14)]:
        o+=f'<circle cx="{x+dx*h}" cy="{y+dy*h}" r="{r*h}" fill="#8fc16a" opacity=".95"/>'
    return o
def fly(x,y,s=1):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="0" width="12" height="34" rx="5" fill="#f3ecd9" stroke="#cfc5a8" stroke-width="2"/>'
            f'<path d="M-34,2 Q-30,-34 0,-36 Q30,-34 34,2 Z" fill="#d6453d" stroke="#a02d27" stroke-width="2.5"/>'
            '<circle cx="-14" cy="-16" r="4.5" fill="#fff"/><circle cx="8" cy="-24" r="4" fill="#fff"/><circle cx="17" cy="-10" r="4.5" fill="#fff"/></g>')
def flower(x,y,col="#f4c542",s=1,stem="#4d8a3e"):
    o=f'<path d="M{x},{y} L{x},{y+60*s}" stroke="{stem}" stroke-width="{4*s}"/>'
    for a in range(0,360,60):
        o+=f'<ellipse cx="{x+12*s*math.cos(math.radians(a))}" cy="{y+12*s*math.sin(math.radians(a))}" rx="{9*s}" ry="{6*s}" transform="rotate({a} {x+12*s*math.cos(math.radians(a))} {y+12*s*math.sin(math.radians(a))})" fill="{col}"/>'
    return o+f'<circle cx="{x}" cy="{y}" r="{6*s}" fill="#e08a2c"/>'
def blabar(x,y,s=1):
    o=f'<path d="M{x},{y} q-30,-30 -50,-10 M{x},{y} q30,-40 55,-15 M{x},{y} q0,-40 -5,-55" stroke="#4d8a3e" stroke-width="{4*s}" fill="none"/>'
    for (dx,dy) in [(-50,-10),(55,-15),(-5,-55),(-30,-26)]:
        o+=f'<ellipse cx="{x+dx}" cy="{y+dy}" rx="{18*s}" ry="{11*s}" fill="#6ab04c"/>'
    for (dx,dy) in [(-20,6),(18,3)]: o+=f'<circle cx="{x+dx}" cy="{y+dy}" r="{7*s}" fill="#3d4a86"/>'
    return o
def fox(x,y,s=1,col="#d9692b"):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M-62,-52 Q-120,-96 -176,-40 Q-168,-18 -120,-20 Q-84,-22 -62,-34Z" fill="{col}"/><path d="M-176,-40 Q-168,-18 -146,-24 Q-150,-44 -176,-40Z" fill="#fff"/>'
            f'<rect x="-52" y="-30" width="11" height="30" fill="#2b2b2b"/><rect x="-26" y="-30" width="11" height="30" fill="#2b2b2b"/><rect x="30" y="-30" width="11" height="30" fill="#2b2b2b"/><rect x="54" y="-30" width="11" height="30" fill="#2b2b2b"/>'
            f'<ellipse cx="0" cy="-50" rx="74" ry="30" fill="{col}"/><ellipse cx="30" cy="-34" rx="38" ry="14" fill="#f6e7d4"/>'
            f'<path d="M50,-66 Q80,-96 112,-62 L146,-44 Q148,-36 138,-34 L100,-30 Q70,-30 50,-44Z" fill="{col}"/>'
            f'<path d="M64,-84 L72,-114 L90,-82Z" fill="{col}"/><path d="M88,-80 L104,-108 L110,-72Z" fill="{col}"/><path d="M68,-86 L73,-104 L82,-85Z" fill="#2b2b2b"/>'
            f'<path d="M110,-44 L146,-44 Q148,-36 138,-34 L112,-34Z" fill="#f6e7d4"/><circle cx="143" cy="-42" r="5" fill="#2b2b2b"/><circle cx="104" cy="-56" r="4.5" fill="#2b2b2b"/></g>')
def bird(x,y,s=1,col="#c0392b"):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="22" ry="15" fill="#6d7a86"/><ellipse cx="6" cy="8" rx="14" ry="9" fill="{col}"/>'
            f'<circle cx="16" cy="-10" r="10" fill="#2b2b2b"/><path d="M24,-10 L34,-7 L24,-4Z" fill="#e0a030"/><path d="M-22,0 L-42,-6 L-40,10Z" fill="#4a5560"/></g>')
def butterfly(x,y,s=1):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="-14" cy="-8" rx="14" ry="20" fill="#e08a2c" transform="rotate(-25 -14 -8)"/><ellipse cx="14" cy="-8" rx="14" ry="20" fill="#e08a2c" transform="rotate(25 14 -8)"/>'
            '<ellipse cx="-11" cy="12" rx="9" ry="13" fill="#f4c542"/><ellipse cx="11" cy="12" rx="9" ry="13" fill="#f4c542"/><rect x="-2" y="-14" width="4" height="34" rx="2" fill="#3a2f28"/></g>')
def bee(x,y,s=1):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="26" ry="17" fill="#f4c542"/><rect x="-6" y="-16" width="9" height="32" fill="#2b2b2b"/><rect x="10" y="-14" width="8" height="28" fill="#2b2b2b"/>'
            '<ellipse cx="-4" cy="-22" rx="14" ry="9" fill="#cfe9f7" opacity=".9" transform="rotate(-20 -4 -22)"/><ellipse cx="10" cy="-22" rx="12" ry="8" fill="#cfe9f7" opacity=".9" transform="rotate(15 10 -22)"/><circle cx="-26" cy="-2" r="8" fill="#2b2b2b"/></g>')

# ---------- omslag --------------------------------------------------------------
def cover(variant):
    W,H=1818,759
    pal={'v':('#cfe6dc','#eaf3e2','#9fc8b0'),'l':('#d9ecf4','#f2f7e6','#a8cfc0'),'f':('#c7ddd2','#e3eed9','#7fb095')}[variant]
    random.seed({'v':3,'l':8,'f':5}[variant])
    s=f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal[0]}"/><stop offset="1" stop-color="{pal[1]}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#sk)"/>'
    s+=f'<circle cx="1480" cy="170" r="70" fill="#fff6d0" opacity=".9"/>'
    s+=f'<path d="M0,420 Q300,300 620,400 T1250,380 T1818,400 L1818,759 L0,759Z" fill="{pal[2]}" opacity=".6"/>'
    for i in range(14): s+=spruce(40+i*58+random.randint(-10,10),470+random.randint(-10,15),170+random.randint(-30,60),"#3b7a58","#2c6247")
    s+=f'<path d="M0,560 Q400,520 900,570 T1818,545 L1818,759 L0,759Z" fill="#7fb36a"/>'
    s+=f'<path d="M0,640 Q500,600 1000,650 T1818,625 L1818,759 L0,759Z" fill="#6aa457"/>'
    for i in range(9): s+=spruce(520+i*70+random.randint(-15,15),640+random.randint(-8,10),210+random.randint(-30,70))
    for x in (880,990,1260): s+=birch(x,640,260)
    for (x,y) in [(160,690),(290,720),(430,700),(1170,720),(1350,700),(1500,725),(1650,700)]: s+=flower(x,y,random.choice(["#f4c542","#f08cb0","#b7a7e8","#fff"]),1.2)
    for (x,y) in [(60,700),(560,730),(760,715),(1090,705),(1720,735)]: s+=blabar(x,y,1)
    s+=fly(700,705,1.1)+fly(1230,740,0.9)
    s+=fox(1480,690,1.25)
    s+=bird(1100,470,1.2)+butterfly(330,560,1.4)+butterfly(1560,480,1.1)+bee(220,640,1.2)
    s+=f'<rect x="38" y="38" width="170" height="46" rx="23" fill="#fff" opacity=".9"/>'+T(123,70,"KAPITEL 3",24,"#2f6b4f","700")
    return svg(W,H,s,pal[0])
for v,n in (('v','vanlig'),('l','lattlast'),('f','fordjupning')):
    render('cover_'+n, cover(v), 1818, 759, 1)

# ---------- ekosystemtjänster (fyra kort) ---------------------------------------
W,H=1500,560
b=''
cards=[("Försörjande","mat, fisk, bär, virke, vatten, läkemedel","#fdf0d5",lambda cx:(blabar(cx,330,1.6)+'<path d="M%d,230 q40,-30 80,0 q-40,30 -80,0z" fill="#6fb3d8"/><path d="M%d,230 l-22,-16 v32z" fill="#6fb3d8"/>'%(cx-30,cx-30))),
       ("Reglerande","pollinering, vattenrening, kolinlagring","#e6f1fa",lambda cx:(bee(cx-40,250,1.8)+flower(cx+70,290,"#f08cb0",1.6)+'<path d="M%d,360 q30,-24 60,0 t60,0 t60,0" stroke="#3b82c4" stroke-width="8" fill="none"/>'%(cx-90))),
       ("Stödjande","bördig jord, fotosyntes, näringskretslopp","#e7f3e1",lambda cx:('<path d="M%d,330 q80,-100 160,0z" fill="#8a6a45"/><path d="M%d,330 h160" stroke="#6b4a2f" stroke-width="8"/>'%(cx-80,cx-80)+'<path d="M%d,250 q-50,-60 20,-90 q60,20 -20,90z" fill="#58a85f"/><path d="M%d,250 v80" stroke="#3f7f46" stroke-width="6"/>'%(cx,cx))),
       ("Kulturella","friluftsliv, jakt, fiske, rekreation, inspiration","#f4e8f5",lambda cx:('<path d="M%d,340 L%d,230 L%d,340z" fill="#e86a4a"/><path d="M%d,340 L%d,280 L%d,340z" fill="#f09b82"/>'%(cx-70,cx,cx+70,cx-20,cx,cx+20)+spruce(cx+110,345,120)+spruce(cx-115,345,100)))]
cw=345; gap=20
for i,(n,d,bg,ic) in enumerate(cards):
    x=20+i*(cw+gap); cx=x+cw/2
    b+=f'<rect x="{x}" y="20" width="{cw}" height="520" rx="18" fill="{bg}" stroke="#e3dccd" stroke-width="2"/>'+ic(cx)
    b+=T(cx,415,n,36,INK,"700")
    words=d.split(', ')
    for k,w_ in enumerate((', '.join(words[:2]), ', '.join(words[2:4]), ', '.join(words[4:]))):
        if w_: b+=T(cx,452+k*26,w_,22,MUT)
render('ekotjanster', svg(W,H,b,"#fbf9f3"), W, H, 1)

# ---------- rikena ------------------------------------------------------------
W,H=1500,560
b=''
rik=[("Djur","tar upp näring genom att äta","#fdeee0",lambda cx:fox(cx+30,350,0.8)),
     ("Växter","gör egen mat med fotosyntes","#e6f3de",lambda cx:(birch(cx,360,220))),
     ("Svampar","bryter ner död material","#f7e8e8",lambda cx:(fly(cx,330,2.2))),
     ("Bakterier","celler utan cellkärna","#e4f0f8",lambda cx:('<g transform="rotate(-25 %d 290)"><rect x="%d" y="262" width="150" height="56" rx="28" fill="#bfe0f2" stroke="#3b7ba8" stroke-width="5"/><path d="M%d,290 q16,-14 28,0 t28,0 t28,0" stroke="#26506f" stroke-width="4" fill="none"/></g>'%(cx,cx-75,cx-60))),
     ("Encelliga med kärna","t.ex. amöbor, alger, jäst","#efe9f7",lambda cx:('<path d="M%d,290 q-70,-70 20,-90 q70,0 80,50 q10,60 -50,70 q-60,10 -50,-30z" fill="#fadcc8" stroke="#d98a63" stroke-width="6"/><circle cx="%d" cy="262" r="22" fill="#b79ad6" stroke="#6f4f9c" stroke-width="4"/>'%(cx-20,cx+8)))]
cw=280; gap=20
for i,(n,d,bg,ic) in enumerate(rik):
    x=20+i*(cw+gap); cx=x+cw/2
    b+=f'<rect x="{x}" y="20" width="{cw}" height="520" rx="18" fill="{bg}" stroke="#e3dccd" stroke-width="2"/>'+ic(cx)
    b+=T(cx,440,n if len(n)<14 else "Encelliga",32,INK,"700")
    if len(n)>=14: b+=T(cx,470,"med cellkärna",24,INK,"700")
    b+=T(cx,500 if len(n)<14 else 500,d,20,MUT)
render('rikena', svg(W,H,b,"#fbf9f3"), W, H, 1)

# ---------- nyckel (flödesschema) ---------------------------------------------
W,H=1600,760
b=''
def nod(x,y,w,h,t1,t2=None,fill="#fff",stroke="#cfc6b2",bold=False,sz=26):
    o=f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
    if t2: return o+T(x,y-6,t1,sz,INK,"700" if bold else "400")+T(x,y+26,t2,sz,INK,"700" if bold else "400")
    return o+T(x,y+9,t1,sz,INK,"700" if bold else "400")
def lin(x1,y1,x2,y2,lab=None,lx=0,ly=0,a="middle"):
    o=f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#5d6b75" stroke-width="3.5" marker-end="url(#ah)"/>'
    if lab: o+=T((x1+x2)/2+lx,(y1+y2)/2+ly,lab,23,"#a84d22","700",a)
    return o
LEAF=dict(fill="#f9f2d6",stroke="#d5c47a",bold=True)
b+=nod(750,70,460,84,"Har trädet barr eller blad?","",fill="#e7f3e1",bold=True)
b+=lin(600,112,380,190,"barr",-45,-5)+lin(900,112,1090,190,"blad",45,-5)
b+=nod(380,235,420,84,"Hur sitter barren?","",fill="#e7f3e1",bold=True)
b+=lin(290,278,190,400,"två och två i knippe",-10,-8,"end")+lin(470,278,570,400,"en och en runt kvisten",10,-8,"start")
b+=nod(190,450,260,90,"TALL","Pinus sylvestris",**LEAF)
b+=nod(570,450,260,90,"GRAN","Picea abies",**LEAF)
b+=nod(1090,235,470,84,"Är bladet delat i småblad?","",fill="#e7f3e1",bold=True)
b+=lin(980,278,860,400,"ja",-18,-8,"end")+lin(1200,278,1250,400,"nej",24,-8,"start")
b+=nod(860,450,260,90,"RÖNN","Sorbus aucuparia",**LEAF)
b+=nod(1250,450,440,84,"Hur ser bladet ut?","",fill="#e7f3e1",bold=True)
b+=lin(1160,493,1060,610,"trekantigt, dubbelsågat",-10,-8,"end")+lin(1340,493,1420,610,"nästan runt, grova tänder",10,-8,"start")
b+=nod(1060,660,260,90,"BJÖRK","Betula pendula",**LEAF)
b+=nod(1420,660,260,90,"ASP","Populus tremula",**LEAF)
render('nyckel', svg(W,H,b,"#fbf9f3"), W, H, 1)

# ---------- naturligt urval: pepparfjäril -------------------------------------
def moth(x,y,dark,rot=0,s=1):
    wing="#4a4036" if dark else "#e6e1d6"; edge="#2b2620" if dark else "#a39d90"
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><path d="M0,-4 L-46,-22 L-40,22 L0,10Z" fill="{wing}" stroke="{edge}" stroke-width="3"/><path d="M0,-4 L46,-22 L40,22 L0,10Z" fill="{wing}" stroke="{edge}" stroke-width="3"/>'
            f'<ellipse cx="0" cy="4" rx="7" ry="22" fill="{edge}"/>'+('' if dark else f'<circle cx="-22" cy="0" r="2.5" fill="{edge}"/><circle cx="22" cy="0" r="2.5" fill="{edge}"/><circle cx="-14" cy="12" r="2.5" fill="{edge}"/><circle cx="14" cy="12" r="2.5" fill="{edge}"/>')+'</g>')
def trunk(x0,w,h):
    o=f'<rect x="{x0}" y="90" width="{w}" height="{h}" rx="14" fill="#d8d3c4" stroke="#a8a28f" stroke-width="3"/>'
    random.seed(4)
    for i in range(18):
        px=x0+random.randint(14,w-14); py=100+random.randint(0,h-30)
        o+=f'<ellipse cx="{px}" cy="{py}" rx="{random.randint(12,26)}" ry="{random.randint(7,14)}" fill="#c4bfae" opacity=".7"/>'
    return o
W,H=1500,560; b=''
titles=[("1 Variation","Fjärilarna är olika. Några är ljusa, några mörka."),("2 Urval","Fåglarna ser de mörka lättast och tar dem först"),("3 Nästa generation","De ljusa överlever och får fler ungar. Det blir fler ljusa.")]
cw=470; gap=25
for i,(t,d) in enumerate(titles):
    x=20+i*(cw+gap); cx=x+cw/2
    b+=f'<rect x="{x}" y="20" width="{cw}" height="520" rx="18" fill="#fff" stroke="#e3dccd" stroke-width="2"/>'+T(cx,62,t,32,INK,"700")
    b+=trunk(x+95,280,370)
    if i==0:
        for (dx,dy,dk,r) in [(60,60,False,-10),(190,50,True,12),(110,150,False,5),(230,160,False,-20),(70,255,True,-5),(190,260,False,15),(120,330,False,0)]:
            b+=moth(x+95+dx,100+dy,dk,r,0.9)
    if i==1:
        for (dx,dy,dk,r) in [(60,60,False,-10),(190,50,True,12),(110,150,False,5),(230,160,False,-20),(70,255,True,-5),(190,260,False,15),(120,330,False,0)]:
            b+=moth(x+95+dx,100+dy,dk,r,0.9)
        for (dx,dy) in [(190,50),(70,255)]:
            b+=f'<circle cx="{x+95+dx}" cy="{100+dy}" r="46" fill="none" stroke="#c0392b" stroke-width="5" stroke-dasharray="10 7"/>'
        b+=bird(x+420,170,1.1)+bird(x+30,330,0.9)
    if i==2:
        for (dx,dy,dk,r) in [(50,55,False,-10),(200,50,False,12),(110,140,False,5),(235,150,False,-20),(70,240,False,-5),(190,255,False,15),(130,320,True,0),(230,330,False,8)]:
            b+=moth(x+95+dx,100+dy,dk,r,0.9)
    b+=T(cx,498,d.split(". ")[0]+("." if not d.split(". ")[0].endswith(".") else ""),21,MUT)
    if '. ' in d: b+=T(cx,524,d.split('. ',1)[1],21,MUT)
render('urval', svg(W,H,b,"#fbf9f3"), W, H, 1)

# -*- coding: utf-8 -*-
import math, sys
sys.path.insert(0,'/tmp/bio')
from cellkit import *
import cellkit
cellkit.OUT='/tmp/bio/fig02n/'
def card_icon(W,H,body,bg): return svg(W,H,body,bg)
def sun(x,y,r=30,rays=True):
    o=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f6cf4a"/>'
    if rays: o+=''.join(f'<line x1="{x+r*1.35*math.cos(a)}" y1="{y+r*1.35*math.sin(a)}" x2="{x+r*1.8*math.cos(a)}" y2="{y+r*1.8*math.sin(a)}" stroke="#f6cf4a" stroke-width="5" stroke-linecap="round"/>' for a in [i*math.pi/4 for i in range(8)])
    return o
def leaf(x,y,s=1,rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><path d="M-80,60 C-100,-40 0,-90 90,-100 C100,0 30,70 -80,60Z" fill="#7fbf6a" stroke="#3f7d4f" stroke-width="5"/>'
            '<path d="M-72,54 L82,-92" stroke="#3f7d4f" stroke-width="3.5"/></g>')
def cellblob(x,y,rx,ry,fill="#fbe4d3",st="#d98a63"): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{st}" stroke-width="7"/>'
def arr(x1,y1,x2,y2,col="#5d6b75",w=6): return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" marker-end="url(#ah2)"/>'
cellkit_svg=svg
def SV(W,H,body,bg="#f4f9ef"):
    return svg(W,H,body,bg).replace('</defs>','<marker id="ah2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.2" markerHeight="3.2" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>')

# ---- l_liv: kännetecken på liv
W,H=1200,380
b=''
tiles=[("Celler",'cell'),("Energi",'bolt'),("Växer",'grow'),("Förökar sig",'two'),("Reagerar",'react')]
tw=216;gap=14;x0=(W-5*tw-4*gap)/2
for i,(n,k) in enumerate(tiles):
    x=x0+i*(tw+gap);cx=x+tw/2
    b+=f'<rect x="{x}" y="15" width="{tw}" height="350" rx="18" fill="#fff" stroke="#dbe7dc" stroke-width="2"/>'
    if k=='cell': b+=cellblob(cx,160,75,62)+nucleus(cx-8,158,28)+mito(cx+38,192,10,0.5)
    if k=='bolt': b+=f'<path d="M{cx+10},85 L{cx-35},170 L{cx-5},170 L{cx-20},240 L{cx+40},145 L{cx+8},145Z" fill="#f2c744" stroke="#c99b12" stroke-width="5" stroke-linejoin="round"/>'
    if k=='grow':
        for (dx,sc) in ((-60,0.5),(0,0.8),(60,1.1)):
            b+=f'<rect x="{cx+dx-4}" y="{230-60*sc}" width="8" height="{60*sc}" fill="#4d8a3e"/><circle cx="{cx+dx}" cy="{230-60*sc}" r="{16*sc+8}" fill="#7fbf6a" stroke="#3f7d4f" stroke-width="4"/>'
    if k=='two':
        b+=cellblob(cx-42,170,40,40)+nucleus(cx-42,170,14)+cellblob(cx+42,170,40,40)+nucleus(cx+42,170,14)+f'<path d="M{cx-4},120 L{cx-4},220" stroke="#d98a63" stroke-width="4" stroke-dasharray="6 6"/>'
    if k=='react':
        b+=sun(cx+55,95,20)+f'<rect x="{cx-30-4}" y="170" width="8" height="70" fill="#4d8a3e" transform="rotate(18 {cx-30} 240)"/><circle cx="{cx-2}" cy="165" r="28" fill="#7fbf6a" stroke="#3f7d4f" stroke-width="4"/>'
    b+=T(cx,305,n,32,INK,"700")
render('l_liv', SV(W,H,b),W,H)

# ---- l_foto: fotosyntes (löv)
W,H=1200,560
b=sun(110,95,36)+arr(165,135,265,215,"#e0872f",7)+T(235,95,"ljus",30,"#b97a1e","700","start")
b+=leaf(580,290,1.7,-8)
b+=chloro(560,300,-35,0.9)
b+=arr(70,360,330,330,"#3b7ba8")+T(170,332,"koldioxid",30,INK,"700")
b+=arr(520,505,520,435,"#3b86c0")+T(520,548,"vatten (från rötterna)",28,INK,"700","middle")
b+=arr(790,230,1010,170,"#2f7d3a")+T(980,140,"glukos",30,INK,"700")
b+=arr(800,330,1030,320,"#c64f3f")+T(980,365,"syre",30,INK,"700")
render('l_foto', SV(W,H,b),W,H)

# ---- l_andning: cellandning
W,H=1200,480
b=cellblob(600,250,230,160)+mito(600,250,-10,2.3)+nucleus(430,200,0)
b=cellblob(600,250,230,160)+mito(600,255,-10,2.3)
b+=arr(90,190,360,215,"#d98a3a")+T(220,170,"glukos",30,INK,"700")
b+=arr(90,330,360,300,"#c64f3f")+T(220,375,"syre",30,INK,"700")
b+=arr(850,215,1110,190,"#3b7ba8")+T(990,170,"koldioxid + vatten",28,INK,"700")
b+=f'<path d="M900,330 L945,285 L922,285 L950,240" stroke="#e8b923" stroke-width="10" fill="none" stroke-linejoin="round"/>'+T(1040,330,"energi",32,"#b8861a","700")
b+=T(600,452,"mitokondrien",28,MUT,"700")
render('l_andning', SV(W,H,b,"#fbf1e8"),W,H)

# ---- ikoner till Det viktigaste (436x320)
def icon(name, body, bg): render(name, SV(436,320,body,bg),436,320)
icon('l_ic1', cellblob(218,160,120,95)+nucleus(200,155,42)+mito(290,205,15,0.65)+chloro(130,115,-30,0.55)*0, "#f4f9ef")
icon('l_ic2', sun(80,70,28)+leaf(230,185,1.0,-8)+chloro(225,190,-35,0.5), "#f4f9ef")
icon('l_ic3', cellblob(218,160,150,105)+mito(218,165,-10,1.6), "#fbf1e8")
icon('l_ic4', f'<path d="M110,170 C110,70 330,70 330,150" stroke="#3f7d4f" stroke-width="12" fill="none" marker-end="url(#ah2)"/><path d="M330,190 C330,260 110,260 110,190" stroke="#7a8a95" stroke-width="12" fill="none" marker-end="url(#ah2)"/>'+T(220,165,"kol",42,INK,"700"), "#f4f9ef")
icon('l_ic5', cellblob(80,160,45,45)+nucleus(80,160,16)+'<rect x="155" y="125" width="70" height="70" rx="10" fill="#f4b6ae" stroke="#c2574d" stroke-width="5"/>'+f'<path d="M290,200 C250,120 330,100 340,160 C360,100 400,130 380,185 L335,240Z" fill="#e5675b" stroke="#a23a30" stroke-width="5"/>'+arr(128,160,150,160)+arr(232,160,255,160), "#f7f1ee")

# ---- l_ord: översikt av ord
W,H=1200,960
b=''
items=[("Cell","cell"),("Cellkärna","nuc"),("Mitokondrie","mito"),("Kloroplast","chl"),("Fotosyntes","foto"),("Cellandning","and")]
cw,ch=380,430
for i,(n,k) in enumerate(items):
    x=30+(i%3)*(cw+15); y=25+(i//3)*(ch+15)
    b+=f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="20" fill="#fff" stroke="#dbe7dc" stroke-width="3"/>'
    cx=x+cw/2; cy=y+170
    if k=='cell': b+=cellblob(cx,cy,130,100)+nucleus(cx-15,cy-5,42)+mito(cx+60,cy+40,12,0.6)
    if k=='nuc': b+=nucleus(cx,cy,95)
    if k=='mito': b+=mito(cx,cy,-10,2.3)
    if k=='chl': b+=chloro(cx,cy,-15,2.3)
    if k=='foto': b+=sun(cx-95,cy-55,22)+leaf(cx+10,cy+15,0.9,-8)
    if k=='and': b+=cellblob(cx,cy,140,100)+mito(cx,cy,-10,1.6)
    desc={'cell':"Den minsta levande enheten.",'nuc':"Innehåller DNA.",'mito':"Gör energi: cellandning.",'chl':"Gör socker: fotosyntes.",'foto':"Ljus, koldioxid och vatten blir glukos och syre.",'and':"Glukos och syre ger energi."}[k]
    b+=T(cx,y+342,n,40,INK,"700")
    words=desc.split(); lines=[];cur=''
    for w in words:
        if len(cur+' '+w)>26: lines.append(cur);cur=w
        else: cur=(cur+' '+w).strip()
    lines.append(cur)
    for j,l in enumerate(lines): b+=T(cx,y+380+j*30,l,24,MUT)
render('l_ord', SV(W,H,b,"#f4f9ef"),W,H)

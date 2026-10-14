# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/bio')
import cellkit as K
from cellkit import T, labels, mito, chloro, nucleus, render
def SV(W,H,body,bg="#faf7f2"): return K.svg(W,H,body,bg)
BL="#3b82c4"; OR="#e08a2c"; GR="#3f8f55"
def arr(x1,y1,x2,y2,col="#5d6b75",w=7): return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" marker-end="url(#ah2)"/>'
def dots(pts,col,r=11): return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>' for x,y in pts)

# ---------- 1. transport ----------
def osmos():
    W,H=1500,640; o=''
    for i,(tit,sub) in enumerate([("Diffusion","Ingen energi behövs"),("Osmos","Ingen energi behövs"),("Aktiv transport","Kräver energi")]):
        x0=30+i*490; cx=x0+225
        o+=f'<rect x="{x0}" y="90" width="450" height="400" rx="16" fill="#fff" stroke="#d8d2c6" stroke-width="3"/>'
        o+=T(cx,60,tit,40,"#24323c","700")
        o+=f'<line x1="{cx}" y1="100" x2="{cx}" y2="480" stroke="#7a56b0" stroke-width="8" stroke-dasharray="26 12"/>'
        o+=T(cx,545,sub,32,"#5d6b75","400")
    # diffusion
    cx=30+225
    L=[(80,150),(130,210),(180,150),(100,290),(170,260),(70,370),(150,350),(200,420),(110,430),(190,330),(60,230),(210,215)]
    R=[(330,200),(400,400),(360,320)]
    o+=dots(L,BL)+dots(R,BL)+arr(cx-60,300,cx+90,300,"#24323c")
    o+=T(135,128,"mycket",30,"#5d6b75")+T(375,128,"lite",30,"#5d6b75")
    # osmos
    cx=30+490+225; x0=520
    o+=dots([(x0+90,200),(x0+110,390),(x0+60,300)],"#8fc3ea",9)
    o+=dots([(cx+70,170),(cx+170,230),(cx+100,300),(cx+190,360),(cx+80,410),(cx+160,150)],OR,17)
    o+=dots([(cx+130,260),(cx+60,350),(cx+170,440),(cx+110,200)],"#8fc3ea",9)
    o+=arr(cx-70,300,cx+45,300,BL,7)
    o+=T(x0+95,128,"rent vatten",30,"#5d6b75")+T(cx+130,128,"mycket löst",30,"#5d6b75")
    # aktiv
    cx=30+980+225; x0=1010
    o+=dots([(x0+80,170),(x0+170,260),(x0+110,360)],BL)
    o+=dots([(cx+60,150),(cx+130,190),(cx+190,150),(cx+80,230),(cx+170,230),(cx+70,330),(cx+150,350),(cx+200,420),(cx+90,430)],BL)
    o+=f'<rect x="{cx-30}" y="270" width="60" height="90" rx="14" fill="#f2d06b" stroke="#b98a12" stroke-width="5"/>'
    o+=arr(cx-95,315,cx-40,315,"#24323c")+arr(cx+40,315,cx+95,315,"#24323c")
    o+=T(cx,400,"⚡ energi",30,"#b98a12","700")
    o+=T(x0+85,128,"lite",30,"#5d6b75")+T(cx+130,128,"mycket",30,"#5d6b75")
    render('f_osmos',SV(W,H,o),W,H)
osmos()

# ---------- 2. endosymbios ----------
def endo():
    W,H=1500,900; o=''
    def blob(x,y): return f'<ellipse cx="{x}" cy="{y}" rx="190" ry="120" fill="#e9f0f7" stroke="#5b86b0" stroke-width="6"/>'
    def bact(x,y,col,st): return f'<rect x="{x-44}" y="{y-22}" width="88" height="44" rx="22" fill="{col}" stroke="{st}" stroke-width="5"/>'
    rows=[("Mitokondrie","#e9a37a","#c4622d"),("Kloroplast","#8fd18a","#2e7d3a")]
    for r,(nm,col,st) in enumerate(rows):
        y0=70+r*440; cy=y0+170
        o+=T(40,y0,nm,42,"#24323c","700","start")
        for k in range(3):
            cx=250+k*500
            o+=blob(cx,cy)
            o+=nucleus(cx+85,cy-30,38)
            if r==1: o+=mito(cx-110,cy+55,10,0.7)
            if k==0: o+=bact(cx-10,cy+165,col,st)
            if k==1:
                o+=f'<ellipse cx="{cx-20}" cy="{cy-25}" rx="72" ry="44" fill="none" stroke="#5b86b0" stroke-width="4" stroke-dasharray="8 6"/>'+bact(cx-20,cy-25,col,st)
            if k==2: o+=(mito if r==0 else chloro)(cx-20,cy-25,0,1)
            o+=f'<circle cx="{cx-170}" cy="{cy-125}" r="26" fill="#24323c"/>'+T(cx-170,cy-114,str(k+1),34,"#fff","700")
            if k<2: o+=arr(cx+200,cy,cx+290,cy,"#5d6b75",7)
    render('f_endo',SV(W,H,o),W,H)
endo()

# ---------- 3. blad ----------
def blad():
    W,H=1500,760; o=''
    X0,X1=330,1170
    o+=f'<rect x="{X0}" y="150" width="{X1-X0}" height="8" fill="#e8d37a" stroke="#c7a92f" stroke-width="2"/>'
    # upper epidermis
    for i in range(0,(X1-X0)//70):
        o+=f'<rect x="{X0+i*70+3}" y="160" width="64" height="44" rx="6" fill="#d7ecd0" stroke="#4f8f58" stroke-width="3"/>'
    # palisade
    for i in range(0,(X1-X0)//52):
        x=X0+i*52+3; o+=f'<rect x="{x}" y="210" width="46" height="130" rx="12" fill="#a9dc9c" stroke="#3f8f55" stroke-width="3"/>'
        for yy in (235,275,315): o+=f'<ellipse cx="{x+23}" cy="{yy}" rx="11" ry="7" fill="#2e7d3a"/>'
    # spongy
    import random; random.seed(4)
    for j in range(2):
        for i in range(0,(X1-X0)//78):
            x=X0+i*78+40+(j*39); y=380+j*70
            if x>X1-30 or abs(x-860)<75 and abs(y-425)<75: continue
            o+=f'<ellipse cx="{x}" cy="{y}" rx="34" ry="30" fill="#c9eabd" stroke="#3f8f55" stroke-width="3"/><ellipse cx="{x-6}" cy="{y}" rx="9" ry="6" fill="#2e7d3a"/>'
    # vein
    vx,vy=860,425
    o+=f'<circle cx="{vx}" cy="{vy}" r="58" fill="#fff" stroke="#24323c" stroke-width="5"/><path d="M{vx-58},{vy} A58,58 0 0 1 {vx+58},{vy}" fill="#8fc3ea" stroke="#24323c" stroke-width="4"/><path d="M{vx-58},{vy} A58,58 0 0 0 {vx+58},{vy}" fill="#f4bf7a" stroke="#24323c" stroke-width="4"/>'
    # lower epidermis with stomata
    for i in range(0,(X1-X0)//70):
        x=X0+i*70+3
        if 3<=i<=4: continue
        o+=f'<rect x="{x}" y="500" width="64" height="44" rx="6" fill="#d7ecd0" stroke="#4f8f58" stroke-width="3"/>'
    sx=X0+3*70+3+64
    o+=f'<path d="M{sx-64},500 q-4,24 4,44 h44 q-8,-20 -4,-44z" fill="#6fbf6a" stroke="#2e7d3a" stroke-width="4"/><path d="M{sx+64},500 q4,24 -4,44 h-44 q8,-20 4,-44z" fill="#6fbf6a" stroke="#2e7d3a" stroke-width="4"/>'
    o+=f'<rect x="{X0}" y="548" width="{X1-X0}" height="2" fill="none"/>'
    # gas arrows
    o+=arr(sx-30,640,sx-30,560,"#5d6b75",7)+arr(sx+40,560,sx+40,640,"#5d6b75",7)
    o+=T(sx-45,690,"CO₂ in",32,"#24323c","700","end")+T(sx+55,690,"O₂ ut",32,"#24323c","700","start")
    left=[("Kutikula",X0+30,154),("Övre epidermis",X0+100,182),("Palisadvävnad",X0+130,275),("Svampvävnad",X0+110,380),("Klyvöppning",sx,522)]
    right=[("Ledningsstrimma",vx+45,vy-20),("Nedre epidermis",X1-90,522)]
    o+=labels(W,left,right,150,560,32,40,W-40)
    render('f_blad',SV(W,H,o),W,H)
blad()

# ---------- 4. begränsande faktor ----------
def begr():
    W,H=1300,720; o=''
    x0,y0,x1,y1=170,610,1230,90
    o+=f'<path d="M{x0},{y1-20} L{x0},{y0} L{x1},{y0}" stroke="#24323c" stroke-width="6" fill="none"/>'
    o+=T((x0+x1)//2,690,"Ljusintensitet",36,"#24323c","700")
    o+=f'<text transform="translate(70,{(y0+y1)//2}) rotate(-90)" font-size="36" font-weight="700" fill="#24323c" text-anchor="middle">Fotosyntesens hastighet</text>'
    # curves: low CO2 plateau ~ y 400; high CO2 plateau ~ y 190
    o+=f'<path d="M{x0},{y0} C 330,520 420,420 560,400 L 1180,400" stroke="#c4622d" stroke-width="9" fill="none"/>'
    o+=f'<path d="M{x0},{y0} C 330,500 500,260 700,200 L 1180,190" stroke="#2e7d3a" stroke-width="9" fill="none"/>'
    o+=T(1170,375,"Lite koldioxid",34,"#c4622d","700","end")
    o+=T(1170,165,"Mycket koldioxid",34,"#2e7d3a","700","end")
    o+=f'<line x1="560" y1="400" x2="560" y2="{y0}" stroke="#5d6b75" stroke-width="3" stroke-dasharray="10 8"/>'
    o+=T(365,655,"Ljus begränsar",30,"#5d6b75","400")+T(870,500,"Något annat begränsar",32,"#5d6b75","400")
    o+=T(870,540,"(här: koldioxid)",30,"#5d6b75","400")
    render('f_begr',SV(W,H,o),W,H)
begr()

# ---------- 5. växtens organ ----------
def vaxt():
    W,H=1500,820; o=''
    o+=f'<rect x="40" y="520" width="640" height="260" fill="#e7d5bd"/>'
    # roots
    for d in ((360,520,360,740),(360,560,250,680),(360,570,470,690),(250,680,200,760),(470,690,520,765),(360,640,330,720)):
        o+=f'<path d="M{d[0]},{d[1]} L{d[2]},{d[3]}" stroke="#a37a4c" stroke-width="10" stroke-linecap="round"/>'
    # stem
    o+=f'<path d="M360,520 L360,200" stroke="#3f8f55" stroke-width="16" stroke-linecap="round"/>'
    for (x,y,rot) in ((290,330,-30),(430,300,30),(280,440,-20),(440,420,20)):
        o+=f'<ellipse cx="{x}" cy="{y}" rx="80" ry="34" transform="rotate({rot} {x} {y})" fill="#6fbf6a" stroke="#2e7d3a" stroke-width="5"/>'
    for a in range(0,360,60):
        import math
        o+=f'<ellipse cx="{360+46*math.cos(math.radians(a)):.0f}" cy="{170+46*math.sin(math.radians(a)):.0f}" rx="26" ry="20" fill="#f08aa8" stroke="#c0446c" stroke-width="4"/>'
    o+=f'<circle cx="360" cy="170" r="22" fill="#f2d06b" stroke="#b98a12" stroke-width="4"/>'
    left=[("Blad",230,330),("Rot",250,680)]
    right=[("Blomma",410,150),("Stam",368,480)]
    o+=labels(W,left,right,150,700,34,40,690)
    # tube
    tx=1010
    o+=f'<rect x="{tx-190}" y="100" width="170" height="560" rx="12" fill="#cfe6f8" stroke="#3b82c4" stroke-width="6"/><rect x="{tx+20}" y="100" width="170" height="560" rx="12" fill="#fbe3c4" stroke="#e08a2c" stroke-width="6"/>'
    o+=arr(tx-105,600,tx-105,180,BL,12)
    o+=arr(tx+70,200,tx+70,560,OR,12)+arr(tx+140,560,tx+140,240,OR,12)
    o+=T(tx-105,60,"Xylem",40,BL,"700")+T(tx+105,60,"Floem",40,OR,"700")
    o+=T(tx-105,705,"Vatten och",30,"#24323c","700")+T(tx-105,740,"mineraler uppåt",30,"#24323c","700")
    o+=T(tx+105,705,"Socker åt",30,"#24323c","700")+T(tx+105,740,"båda håll",30,"#24323c","700")
    o+=T(tx+105,790,"",30)
    render('f_vaxt',SV(W,H,o),W,H)
vaxt()

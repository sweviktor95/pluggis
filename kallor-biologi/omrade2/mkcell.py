# -*- coding: utf-8 -*-
import math, random
from playwright.sync_api import sync_playwright
OUT='/tmp/bio/fig02n/'
INK="#24323c"; MUT="#5d6b75"
def render(name, svg, w, h, scale=3):
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=scale)
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.screenshot(path=OUT+name+'.png'); b.close()
    print(name)
def svg(W,H,body,bg="#faf7f2"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Carlito">'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5d6b75"/></marker><marker id="ah2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.2" markerHeight="3.2" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>'
            f'<rect width="{W}" height="{H}" rx="20" fill="{bg}"/>{body}</svg>')
def T(x,y,s,size=30,fill=INK,w="400",a="middle",it=False):
    st=' font-style="italic"' if it else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}"{st}>{s}</text>'
def labels(W, left, right, ytop, ybot, size=32, lx=40, rx=None):
    """left/right: lista (text, ax, ay). Sorteras på ay så att linjerna inte korsas. Etikettens y sprids jämnt."""
    rx = rx or W-40
    o=''
    for side,items in (('L',left),('R',right)):
        items=sorted(items,key=lambda t:t[2]); n=len(items)
        for i,(t,ax,ay) in enumerate(items):
            ly = ytop+(ybot-ytop)*(i+0.5)/n if n>1 else (ytop+ybot)/2
            if side=='L':
                ex=lx+len(t)*size*0.52+14
                o+=T(lx,ly+size*0.35,t,size,INK,"700","start")
            else:
                ex=rx-len(t)*size*0.52-14
                o+=T(rx,ly+size*0.35,t,size,INK,"700","end")
            o+=f'<path d="M{ex:.0f},{ly:.0f} L{ax},{ay}" stroke="#5d6b75" stroke-width="2.2" fill="none"/><circle cx="{ax}" cy="{ay}" r="6" fill="#2f6b4f" stroke="#fff" stroke-width="2"/>'
    return o
def mito(x,y,rot=0,s=1):
    o=f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><ellipse rx="52" ry="28" fill="#f0a070" stroke="#c4622d" stroke-width="4"/>'
    o+='<path d="M-34,-18 L-34,6 M-18,-24 L-18,12 M-2,-26 L-2,16 M14,-24 L14,12 M30,-18 L30,6" stroke="#c4622d" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    return o+'</g>'
def chloro(x,y,rot=0,s=1):
    o=f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><ellipse rx="48" ry="26" fill="#6fbf6a" stroke="#2e7d3a" stroke-width="4"/>'
    for k in (-26,-9,8,25): o+=f'<rect x="{k-6}" y="-13" width="12" height="26" rx="4" fill="#3a9448"/>'
    return o+'</g>'
def nucleus(x,y,r):
    o=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#d9c8ee" stroke="#7a56b0" stroke-width="6"/><circle cx="{x-r*0.18}" cy="{y+r*0.1}" r="{r*0.3}" fill="#8a63bd"/>'
    o+=f'<path d="M{x-r*0.55},{y-r*0.45} q{r*0.18},-{r*0.2} {r*0.35},0 t{r*0.35},0 M{x+r*0.1},{y+r*0.55} q{r*0.18},-{r*0.2} {r*0.35},0 t{r*0.3},0" stroke="#5d3f8e" stroke-width="3.5" fill="none"/>'
    return o
def ribos(pts):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#26506f"/>' for x,y in pts)

# ---------------- djurcell
W,H=1200,640
b=''
pts=[]
for i in range(72):
    a=2*math.pi*i/72; r=1+0.04*math.sin(3*a+1)+0.03*math.sin(5*a)
    pts.append((600+330*r*math.cos(a),320+235*r*math.sin(a)))
d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
b+=f'<path d="{d}" fill="#fbe4d3" stroke="#d98a63" stroke-width="12" stroke-linejoin="round"/>'
b+=nucleus(570,310,105)
b+=mito(400,230,-25)+mito(760,440,20)+mito(430,440,10)
rib=[(745,260),(800,330),(720,360),(690,200),(660,430),(500,160),(440,340),(850,400)]
b+=ribos(rib)
L=[("Cellmembran",285,330),("Cytoplasma",360,350),("Mitokondrie",378,455)]
R=[("Cellkärna",672,255),("Ribosomer",800,330)]
b+=labels(W,L,R,90,550)
render('cellen-djurcell', svg(W,H,b), W,H)

# ---------------- växtcell
W,H=1200,640
b='<rect x="270" y="50" width="660" height="520" rx="30" fill="#a9cf7f" stroke="#6b9a4a" stroke-width="3"/>'
b+='<rect x="298" y="78" width="604" height="464" rx="14" fill="#eaf5da" stroke="#7aa75a" stroke-width="4"/>'
b+='<ellipse cx="660" cy="320" rx="190" ry="125" fill="#d9ecf5" stroke="#7db0c8" stroke-width="5"/>'
b+=nucleus(405,180,62)
for (x,y,r) in [(560,130,0),(780,128,0),(860,230,70),(850,410,80),(700,495,0),(520,495,0),(360,330,80),(355,470,40)]:
    b+=chloro(x,y,r,0.85)
b+=mito(450,380,-20,0.75)+mito(800,510,10,0.6)
L=[("Cellvägg",285,150),("Cellmembran",300,260),("Cellkärna",343,190),("Cytoplasma",340,420)]
L=[("Cellvägg",284,120),("Cellkärna",350,160),("Cellmembran",299,300),("Cytoplasma",385,430)]
R=[("Kloroplast",828,128),("Vakuol",760,290),("Mitokondrie",848,505)]
b+=labels(W,L,R,90,550)
render('cellen-vaxtcell', svg(W,H,b,"#f4f9ef"), W,H)

# ---------------- bakterie
W,H=1200,420
b=''
b+='<rect x="280" y="120" width="560" height="190" rx="95" fill="#8fb8d8" stroke="#3a6f95" stroke-width="5"/>'
b+='<rect x="296" y="136" width="528" height="158" rx="79" fill="#bfdcee" stroke="#4a87b0" stroke-width="3"/>'
b+='<rect x="308" y="148" width="504" height="134" rx="67" fill="#dff0fa"/>'
b+='<path d="M420,215 C430,170 460,170 470,215 S510,260 520,215 S560,165 575,215 S620,265 635,215 S680,170 700,200" stroke="#7a56b0" stroke-width="7" fill="none" stroke-linecap="round"/>'
b+=ribos([(380,190),(400,250),(470,255),(560,250),(660,255),(740,200),(765,255),(600,175),(350,230)])
b+='<path d="M840,215 C890,150 930,280 985,215 S1060,170 1090,205" stroke="#3a6f95" stroke-width="7" fill="none" stroke-linecap="round"/>'
L=[("Cellvägg",290,175),("Cellmembran",305,260),("Cytoplasma",345,215)]
R=[("DNA (ingen cellkärna)",605,170),("Ribosomer",740,200),("Flagell",1010,236)]
L=[("Cellvägg",287,170),("DNA",422,215),("Cellmembran",312,265)]
R=[("Ribosomer",740,200),("Flagell",911,215),("Cytoplasma",712,226)]
b+=labels(W,L,R,45,375,size=32)
b+=T(600,405,"Bakterien har inget kärnmembran: DNA ligger fritt i cytoplasman.",24,MUT,"400","middle",True)
render('cellen-bakterie', svg(W,H,b,"#f1f7fb"), W,H)

# ---------------- fotosyntes <-> cellandning
W,H=1200,590
b=''
b+='<circle cx="110" cy="85" r="38" fill="#f6cf4a"/>'+''.join(f'<line x1="{110+52*math.cos(a)}" y1="{85+52*math.sin(a)}" x2="{110+68*math.cos(a)}" y2="{85+68*math.sin(a)}" stroke="#f6cf4a" stroke-width="6" stroke-linecap="round"/>' for a in [i*math.pi/4 for i in range(8)])
b+='<path d="M160,130 L225,190" stroke="#e0872f" stroke-width="7" stroke-dasharray="3 12" stroke-linecap="round" marker-end="url(#ah2)"/>'+T(235,110,"ljus",28,"#b97a1e","700","start")
b+='<path d="M120,450 C100,320 200,220 340,205 C350,330 260,440 120,450Z" fill="#7fbf6a" stroke="#3f7d4f" stroke-width="6"/><path d="M130,440 L330,215" stroke="#3f7d4f" stroke-width="4"/>'
b+=chloro(255,350,-40,0.8)
b+=T(230,515,"Fotosyntes",34,"#2e6b3a","700")+T(230,548,"i kloroplasterna",25,MUT)
b+='<ellipse cx="960" cy="350" rx="190" ry="135" fill="#fbe4d3" stroke="#d98a63" stroke-width="9"/>'+mito(960,350,-10,1.5)
b+=T(960,515,"Cellandning",34,"#b4531f","700")+T(960,548,"i mitokondrierna (nästan alla celler)",25,MUT)
b+='<path d="M400,235 C520,140 700,140 800,210" stroke="#3f7d4f" stroke-width="8" fill="none" marker-end="url(#ah2)"/>'
b+='<rect x="440" y="62" width="280" height="76" rx="14" fill="#fff" stroke="#9cc99f" stroke-width="3"/>'+T(580,97,"glukos + syre",32,INK,"700")+T(580,126,"bildas vid fotosyntes",23,MUT)
b+='<path d="M830,490 C700,560 520,560 400,460" stroke="#7a8a95" stroke-width="8" fill="none" marker-end="url(#ah2)"/>'
b+='<rect x="440" y="415" width="300" height="76" rx="14" fill="#fff" stroke="#b9c2c8" stroke-width="3"/>'+T(590,450,"koldioxid + vatten",32,INK,"700")+T(590,479,"bildas vid cellandning",23,MUT)
b+='<path d="M1130,270 L1170,225 L1148,225 L1170,185" stroke="#e8b923" stroke-width="9" fill="none" stroke-linejoin="round"/>'+T(1140,168,"energi",26,"#b8861a","700")
render('cellen-fotosyntes', svg(W,H,b,"#f4f9ef"), W,H)

# ---------------- storlek (logaritmisk skala, stort till vänster)
W,H=1200,540
b=''
lo,hi=math.log10(0.00001),math.log10(2)
def X(mm): return 80+(hi-math.log10(mm))/(hi-lo)*(W-160)
AX=345
b+=f'<line x1="50" y1="{AX}" x2="{W-50}" y2="{AX}" stroke="#8b979f" stroke-width="4"/>'
for mm,lab in [(1,"1 mm"),(0.1,"0,1 mm"),(0.01,"0,01 mm"),(0.001,"0,001 mm"),(0.0001,"0,0001 mm")]:
    b+=f'<line x1="{X(mm)}" y1="{AX-13}" x2="{X(mm)}" y2="{AX+13}" stroke="#8b979f" stroke-width="4"/>'+T(X(mm),AX+45,lab,26,MUT)
BY=AX+75
x1,x2=X(0.1),X(0.0002)
b+=f'<rect x="50" y="{BY}" width="{x1-54}" height="46" rx="10" fill="#6a9b7a"/>'+T((50+x1)/2,BY+32,"Ögat",26,"#fff","700")
b+=f'<rect x="{x1}" y="{BY}" width="{x2-x1-4}" height="46" rx="10" fill="#4a82b0"/>'+T((x1+x2)/2,BY+32,"Ljusmikroskop",26,"#fff","700")
b+=f'<rect x="{x2}" y="{BY}" width="{W-50-x2}" height="46" rx="10" fill="#8e72b8"/>'+T((x2+W-50)/2,BY+32,"Elektronmikroskop",24,"#fff","700")
items=[("amöba",0.3,"ca 0,3 mm"),("människoägg",0.12,"0,1 mm"),("hudcell",0.03,"0,03 mm"),("röd blodkropp",0.0075,"0,0075 mm"),("bakterie",0.002,"0,002 mm"),("virus",0.0001,"0,0001 mm")]
col={'amöba':('#d4e9c4','#6b9a4a'),'människoägg':('#fadccb','#d98a63'),'hudcell':('#fadccb','#d98a63'),'röd blodkropp':('#d9483e','#9a2a22'),'bakterie':('#bfdcee','#3a6f95'),'virus':('#f2b7cc','#c85a85')}
for i,(n,mm,lab) in enumerate(items):
    x=X(mm); hi_t=(i%2==1)
    ty=55 if hi_t else 135   # namn
    iy=ty+85
    lx=x-22 if n=='amöba' else x
    b+=T(lx,ty,n,27,INK,"700")+T(lx,ty+28,lab,24,MUT)
    b+=f'<line x1="{x}" y1="{iy+30}" x2="{x}" y2="{AX}" stroke="#8b979f" stroke-width="2.5" stroke-dasharray="5 6"/><circle cx="{x}" cy="{AX}" r="7" fill="#2f6b4f"/>'
    c,st=col[n]
    if n=='bakterie': b+=f'<rect x="{x-18}" y="{iy-9}" width="36" height="18" rx="9" fill="{c}" stroke="{st}" stroke-width="3"/>'
    elif n=='virus': b+=f'<polygon points="{x},{iy-13} {x+12},{iy-6} {x+12},{iy+6} {x},{iy+13} {x-12},{iy+6} {x-12},{iy-6}" fill="{c}" stroke="{st}" stroke-width="3"/>'
    else:
        r={'amöba':26,'människoägg':27,'hudcell':22,'röd blodkropp':14}[n]
        b+=f'<circle cx="{x}" cy="{iy}" r="{r}" fill="{c}" stroke="{st}" stroke-width="4"/>'
b+=T(W/2,H-18,"Skalan är logaritmisk: varje steg åt höger är 10 gånger mindre. Bildernas storlek är inte skalenlig.",23,MUT,"400","middle",True)
render('cellen-storlek', svg(W,H,b,"#f4f7f5"), W,H)

# ---------------- specialiserade celler
W,H=1200,440
b=''
cards=[("Muskelcell",["Drar ihop sig","och ger rörelse"]),("Nervcell",["Skickar signaler,","kan bli mycket lång"]),("Röd blodkropp",["Transporterar syre"]),("Rothårscell",["Tar upp vatten","ur jorden"]),("Palisadcell",["Fotosyntes","i bladet"])]
cw=222; gap=14; x0=(W-5*cw-4*gap)/2
for i,(n,d) in enumerate(cards):
    x=x0+i*(cw+gap); cx=x+cw/2
    b+=f'<rect x="{x}" y="20" width="{cw}" height="400" rx="18" fill="#fff" stroke="#e1e8e2" stroke-width="2"/>'
    if i==0:
        for yy,hh in ((120,60),(200,50)):
            b+=f'<rect x="{cx-90}" y="{yy}" width="180" height="{hh}" rx="{hh/2}" fill="#e8908a" stroke="#b5453d" stroke-width="4"/>'
            for k in range(7): b+=f'<line x1="{cx-66+k*22}" y1="{yy+8}" x2="{cx-66+k*22}" y2="{yy+hh-8}" stroke="#c8605a" stroke-width="3"/>'
        for xx,yy in ((cx-35,150),(cx+35,150),(cx,225)): b+=f'<ellipse cx="{xx}" cy="{yy}" rx="10" ry="6" fill="#8a6bb0"/>'
    if i==1:
        b+=f'<circle cx="{cx-42}" cy="190" r="28" fill="#f1d68a" stroke="#b8902a" stroke-width="4"/><circle cx="{cx-42}" cy="190" r="10" fill="#8a6bb0"/>'
        for ang in (200,250,150,300):
            a=math.radians(ang); b+=f'<path d="M{cx-42+25*math.cos(a)},{190+25*math.sin(a)} L{cx-42+50*math.cos(a)},{190+50*math.sin(a)}" stroke="#b8902a" stroke-width="5" fill="none" stroke-linecap="round"/>'
        b+=f'<path d="M{cx-15},195 C{cx+10},195 {cx+10},225 {cx+35},225 L{cx+90},225" stroke="#b8902a" stroke-width="7" fill="none" stroke-linecap="round"/>'
    if i==2:
        b+=f'<ellipse cx="{cx}" cy="190" rx="70" ry="70" fill="#d9483e" stroke="#9a2a22" stroke-width="4"/><ellipse cx="{cx}" cy="190" rx="30" ry="30" fill="#b53028"/>'
    if i==3:
        b+=f'<rect x="{cx-45}" y="100" width="90" height="100" rx="12" fill="#dff0d0" stroke="#4d8a3e" stroke-width="5"/><circle cx="{cx}" cy="140" r="15" fill="#8a6bb0"/>'
        b+=f'<path d="M{cx-14},200 L{cx-10},255 L{cx+10},255 L{cx+14},200Z" fill="#dff0d0" stroke="#4d8a3e" stroke-width="5"/>'
        for xx in (-26,0,26): b+=f'<circle cx="{cx+xx}" cy="275" r="4" fill="#3b7ba8"/>'
    if i==4:
        b+=f'<rect x="{cx-40}" y="90" width="80" height="180" rx="14" fill="#cfe8b5" stroke="#4d8a3e" stroke-width="5"/>'
        for dx,dy in [(-8,130),(8,165),(-8,200),(8,235),(-6,262)]: b+=chloro(cx+dx,dy,0,0.4)
        b+=f'<circle cx="{cx+14}" cy="115" r="10" fill="#8a6bb0"/>'
    b+=T(cx,318,n,29,INK,"700")
    for k,l in enumerate(d): b+=T(cx,355+k*30,l,24,MUT)
render('spec-celler', svg(W,H,b,"#f3f8f1"), W,H)

# ---------------- dag / natt
W,H=1200,470
b=''
def blad(ox):
    return f'<path d="M{ox+230},330 C{ox+210},210 {ox+300},150 {ox+390},140 C{ox+400},250 {ox+330},330 {ox+230},330Z" fill="#7fbf6a" stroke="#3f7d4f" stroke-width="5"/><path d="M{ox+238},322 L{ox+385},150" stroke="#3f7d4f" stroke-width="3.5"/>'
b+='<rect x="15" y="15" width="580" height="440" rx="18" fill="#fff6d8"/><rect x="605" y="15" width="580" height="440" rx="18" fill="#e3e8f4"/>'
b+=T(305,62,"Dag (i ljus)",34,INK,"700")+T(895,62,"Natt",34,INK,"700")
b+=blad(0)+blad(590)
b+='<circle cx="90" cy="130" r="30" fill="#f6cf4a"/>'
b+='<path d="M900,95 a30,30 0 1 0 24,48 a24,24 0 1 1 -24,-48z" fill="#f4e7a0"/>'
def arr(x1,y1,x2,y2,col,lab,lx,ly,anch="middle"):
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{col}" stroke-width="7" stroke-linecap="round" marker-end="url(#ah2)"/>'+T(lx,ly,lab,26,INK,"700",anch)
# dag
b+=arr(60,250,225,270,"#3b7ba8","koldioxid in",120,235)
b+=arr(400,215,545,175,"#c64f3f","syre ut",490,160)
b+=T(305,380,"Fotosyntes + cellandning",27,"#3f7d4f","700")+T(305,412,"Mer syre bildas än det som används.",23,MUT)
# natt
b+=arr(650,250,815,270,"#c64f3f","syre in",715,235)
b+=arr(990,270,1135,225,"#3b7ba8","koldioxid ut",1075,300)
b+=T(895,380,"Bara cellandning",27,"#34407a","700")+T(895,412,"Ingen fotosyntes utan ljus.",23,MUT)
render('dagnatt', svg(W,H,b,"#ffffff"), W,H)

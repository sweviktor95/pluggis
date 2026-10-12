# Illustrationer till provet (egenritade, i sajtens gröna palett). Kör: python3 mkprov.py
from playwright.sync_api import sync_playwright
G1,G2,G3,G4,G5="#245040","#38564A","#5F8472","#EAF1EC","#DCE6DF"
F='font-family="Carlito"'
def svg(W,H,inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="{W}" height="{H}" rx="12" fill="#f4f8f5"/>{inner}</svg>'
def label(x,y,t,w=190): return f'<rect x="{x-w/2}" y="{y-20}" width="{w}" height="34" rx="17" fill="#fff" stroke="{G5}" stroke-width="2"/><text x="{x}" y="{y+3}" text-anchor="middle" {F} font-size="17" font-weight="700" fill="{G2}">{t}</text>'

def bonor():
    W,H=760,290; s=''
    # bord
    s+=f'<rect x="0" y="228" width="{W}" height="62" fill="#c9a27a"/><rect x="0" y="228" width="{W}" height="6" fill="#b88c62"/>'
    # fönster
    s+=f'<rect x="60" y="22" width="230" height="170" rx="8" fill="#c9b79a"/><rect x="72" y="34" width="206" height="146" fill="#cfe6f4"/><rect x="172" y="34" width="6" height="146" fill="#c9b79a"/><rect x="72" y="104" width="206" height="6" fill="#c9b79a"/><circle cx="238" cy="66" r="20" fill="#f7dd8e"/>'
    for i in range(3): s+=f'<polygon points="{110+i*45},110 {128+i*45},110 {150+i*45},228 {118+i*45},228" fill="#f7e9b8" opacity=".55"/>'
    def jar(cx,top,sprout):
        j=f'<rect x="{cx-38}" y="{top}" width="76" height="92" rx="12" fill="#e9f1f1" stroke="#9fb4b4" stroke-width="3"/><rect x="{cx-30}" y="{top-9}" width="60" height="12" rx="3" fill="#b9c9c9"/>'
        for k,(dx,dy) in enumerate([(-20,70),(0,74),(20,70),(-10,58),(12,60),(-26,56),(24,56)]): j+=f'<ellipse cx="{cx+dx}" cy="{top+dy}" rx="9" ry="6" fill="#a9754a" transform="rotate({k*25} {cx+dx} {top+dy})"/>'
        if sprout: j+=f'<path d="M{cx} {top+55} q-4 -26 6 -40" stroke="#5F8472" stroke-width="4" fill="none"/><ellipse cx="{cx+10}" cy="{top+12}" rx="9" ry="5" fill="#7fae8c"/>'
        return j
    s+=jar(175,136,True)+label(175,258,"Burk A · soligt fönster",230)
    # kylskåp
    s+=f'<rect x="470" y="14" width="210" height="236" rx="14" fill="#eef2f3" stroke="#aebcc0" stroke-width="3"/><rect x="482" y="26" width="186" height="212" rx="8" fill="#dde8ec"/><rect x="482" y="132" width="186" height="5" fill="#aebcc0"/><rect x="654" y="40" width="7" height="60" rx="3" fill="#8fa2a8"/>'
    s+=f'<text x="500" y="62" {F} font-size="26" fill="#7aa6c4">❄</text><text x="610" y="112" {F} font-size="22" fill="#7aa6c4">❄</text>'
    s+=jar(575,158,False).replace('rect x="%d"'%(575-30),'rect x="%d"'%(575-30))
    s+=label(575,276,"Burk B · kylskåp",190)
    return svg(W,H,s)

def jast():
    W,H=760,300; s=''
    s+=f'<rect x="0" y="246" width="{W}" height="54" fill="#d9c7a8"/>'
    temps=[("10 °C",126,36,"#dce9a7"),("25 °C",380,56,"#c9e0a0"),("40 °C",634,76,"#bcd993")]
    for t,cx,r,col in temps:
        # ballong
        s+=f'<ellipse cx="{cx}" cy="{150-r*0.55}" rx="{r*0.7}" ry="{r}" fill="{col}" stroke="#7fa176" stroke-width="3"/><path d="M{cx-6} {150-r*0.55+r-2} l6 10 l6 -10" fill="{col}" stroke="#7fa176" stroke-width="3"/>'
        # flaska
        s+=f'<rect x="{cx-12}" y="150" width="24" height="40" fill="#e9f1f1" stroke="#9fb4b4" stroke-width="3"/><path d="M{cx-12} 190 L{cx-50} 215 L{cx-50} 244 Q{cx-50} 250 {cx-44} 250 L{cx+44} 250 Q{cx+50} 250 {cx+50} 244 L{cx+50} 215 L{cx+12} 190 Z" fill="#e9f1f1" stroke="#9fb4b4" stroke-width="3"/>'
        s+=f'<path d="M{cx-47} 226 L{cx+47} 226 L{cx+47} 244 Q{cx+47} 247 {cx+44} 247 L{cx-44} 247 Q{cx-47} 247 {cx-47} 244 Z" fill="#e3c98a"/>'
        for dx,dy in [(-24,236),(-6,232),(14,238),(30,230),(4,240)]: s+=f'<circle cx="{cx+dx}" cy="{dy}" r="3.4" fill="#fff" opacity=".85"/>'
        s+=label(cx,282,t,110)
    s+=f'<text x="380" y="24" text-anchor="middle" {F} font-size="16" fill="{G2}">Jäst, socker och vatten i tre flaskor. Ballongen fångar gasen som jästen bildar.</text>'
    return svg(W,H,s)

def plaster():
    W,H=330,200; s=''
    s+=f'<rect x="30" y="20" width="270" height="130" rx="14" fill="#fff" stroke="#c9b79a" stroke-width="3"/>'
    s+=f'<text x="165" y="58" text-anchor="middle" {F} font-size="27" font-weight="700" fill="#6b4a2f">DetoxPlåstret™</text><text x="165" y="82" text-anchor="middle" {F} font-size="15" fill="#6b4a2f">NYHET! Sätts under foten</text>'
    s+=f'<ellipse cx="165" cy="115" rx="56" ry="24" fill="#a9754a"/><ellipse cx="165" cy="115" rx="40" ry="16" fill="#8c5c36"/>'
    s+=f'<rect x="85" y="160" width="160" height="26" rx="13" fill="{G4}"/><text x="165" y="178" text-anchor="middle" {F} font-size="14" font-weight="700" fill="{G2}">Påhittad produkt</text>'
    return svg(W,H,s)

def dryck():
    W,H=620,210; s=''
    s+=f'<rect x="0" y="176" width="{W}" height="34" fill="#d4e3d9"/>'
    s+=f'<rect x="96" y="22" width="28" height="22" rx="5" fill="{G3}"/><path d="M92 44 h36 q14 0 14 14 v96 q0 12 -12 12 h-40 q-12 0 -12 -12 v-96 q0 -14 14 -14z" fill="#ffffff" stroke="{G3}" stroke-width="3"/><rect x="84" y="78" width="52" height="56" fill="{G4}"/>'
    s+=f'<text x="110" y="101" text-anchor="middle" {F} font-size="13" font-weight="700" fill="{G2}">SPORT</text><text x="110" y="120" text-anchor="middle" {F} font-size="13" font-weight="700" fill="{G2}">DRYCK</text>'
    s+=f'<path d="M230 100 C230 60 290 60 300 92 C310 60 370 60 370 100 C370 140 320 160 300 178 C280 160 230 140 230 100z" fill="{G4}" stroke="{G3}" stroke-width="4"/>'
    s+=f'<path d="M250 112 h28 l10 -26 l16 50 l12 -24 h30" fill="none" stroke="{G2}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    s+=f'<text x="470" y="95" text-anchor="middle" {F} font-size="20" font-weight="700" fill="{G2}">Bättre kondition?</text><text x="470" y="120" text-anchor="middle" {F} font-size="15" fill="{G2}">Det är det företaget påstår.</text>'
    return svg(W,H,s)

with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    for name,(fn,W,H) in {"p_bonor":(bonor,760,290),"p_jast":(jast,760,300),"p_plaster":(plaster,330,200),"p_dryck":(dryck,620,210)}.items():
        pg=b.new_page(viewport={'width':W,'height':H},device_scale_factor=3)
        pg.set_content(f'<body style="margin:0">{fn()}</body>'); pg.screenshot(path=f'/tmp/bio/fig01n/{name}.png'); pg.close()
    b.close()

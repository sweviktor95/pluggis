from playwright.sync_api import sync_playwright
import math
steps=[("1","Observera","och undra","#2f6b4f"),("2","Ställ en fråga","och en hypotes","#3a7ca5"),("3","Planera","undersökningen","#3a7ca5"),
       ("4","Genomför","och dokumentera","#2f6b4f"),("5","Analysera","resultaten","#4f8a63"),("6","Dra slutsatser","– ny fråga?","#d9772b")]
W,H=560,470;cx,cy,R=280,235,150
s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" rx="14" fill="#f4f9f3"/>'
s+=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#c9d8d0" stroke-width="11"/>'
s+=f'<circle cx="{cx}" cy="{cy}" r="78" fill="#e6f0f3"/><text x="{cx}" y="{cy-22}" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="17" fill="#241712">Granska och dela</text>'
for i,t in enumerate(["Andra forskare","kontrollerar och","upprepar"]): s+=f'<text x="{cx}" y="{cy+2+i*18}" text-anchor="middle" font-family="Carlito" font-size="14" fill="#555">{t}</text>'
for i,(n,a,b,c) in enumerate(steps):
    ang=math.radians(-90+i*60);x=cx+R*math.cos(ang);y=cy+R*math.sin(ang)
    w,h=150,52
    s+=f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="9" fill="#fff" stroke="{c}" stroke-width="2.5"/>'
    s+=f'<text x="{x}" y="{y-3}" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="17" fill="#241712">{a}</text><text x="{x}" y="{y+15}" text-anchor="middle" font-family="Carlito" font-size="13.5" fill="#666">{b}</text>'
    s+=f'<circle cx="{x-w/2}" cy="{y-h/2}" r="12" fill="{c}"/><text x="{x-w/2}" y="{y-h/2+5}" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="14" fill="#fff">{n}</text>'
    # pil mot nästa
    a2=math.radians(-90+i*60+36);px=cx+R*math.cos(a2);py=cy+R*math.sin(a2);tx=-math.sin(a2);ty=math.cos(a2)
    s+=f'<polygon points="{px+tx*10},{py+ty*10} {px-tx*10+ty*7},{py-ty*10-tx*7} {px-tx*10-ty*7},{py-ty*10+tx*7}" fill="#5f7280"/>'
s+='</svg>'
open('/tmp/bio/fig01/v_cykel.svg','w').write(s)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=b.new_page(viewport={'width':W,'height':H},device_scale_factor=3)
    pg.set_content(f'<body style="margin:0">{s}</body>');pg.screenshot(path='/tmp/bio/fig01/v_cykel.png');b.close()

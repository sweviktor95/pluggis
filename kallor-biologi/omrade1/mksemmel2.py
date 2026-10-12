from playwright.sync_api import sync_playwright
W,H=480,320
bars=[("1846",11.4,"#c0392b","11,4 %"),("1848",1.3,"#4f8a63","1,3 %")]
y0=250;sc=17
s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="{W}" height="{H}" rx="10" fill="#faf7f0"/>'
s+='<text x="14" y="26" font-family="Carlito" font-size="15" fill="#555">Mödrar som dog i barnsängsfeber på läkarkliniken</text>'
for v in (0,5,10):
    y=y0-v*sc;s+=f'<line x1="60" x2="455" y1="{y}" y2="{y}" stroke="#e1ddd2"/><text x="52" y="{y+5}" text-anchor="end" font-family="Carlito" font-size="14" fill="#666">{v} %</text>'
xs=[150,330]
for (lab,v,c,t),x in zip(bars,xs):
    h=v*sc;s+=f'<rect x="{x-45}" y="{y0-h}" width="90" height="{h}" rx="3" fill="{c}"/><text x="{x}" y="{y0-h-8}" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="16" fill="#241712">{t}</text>'
    s+=f'<text x="{x}" y="{y0+22}" text-anchor="middle" font-family="Carlito" font-size="15" fill="#555">{lab}</text>'
s+=f'<line x1="60" x2="455" y1="{y0}" y2="{y0}" stroke="#6b7b72" stroke-width="2"/>'
s+='<text x="345" y="120" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="14.5" fill="#4f8a63">handtvätt i klorkalk</text><text x="345" y="138" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="14.5" fill="#4f8a63">krävs från 1847</text>'
s+=f'<text x="455" y="{H-8}" text-anchor="end" font-family="Carlito" font-style="italic" font-size="12.5" fill="#666">Allmänna sjukhuset i Wien. Källa: MJA 2018</text></svg>'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=b.new_page(viewport={'width':W,'height':H},device_scale_factor=3)
    pg.set_content(f'<body style="margin:0">{s}</body>');pg.screenshot(path='/tmp/bio/fig01n/f_semmelweis2.png');b.close()

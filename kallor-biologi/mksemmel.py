from playwright.sync_api import sync_playwright
W,H=480,320
bars=[("Läkar-<tspan x='{x}' dy='19'>kliniken</tspan>",9.8,"#c0392b","ca 10 %"),("Barnmorske-<tspan x='{x}' dy='19'>kliniken</tspan>",3.6,"#9aa5a9","ca 3,6 %"),("Läkar-<tspan x='{x}' dy='19'>kliniken efter</tspan>",1.27,"#4f8a63","ca 1,3 %")]
y0=240;sc=14.5
s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="{W}" height="{H}" rx="10" fill="#faf7f0"/>'
s+='<text x="14" y="26" font-family="Carlito" font-size="15" fill="#555">Andel mödrar som dog i barnsängsfeber</text>'
for v in (0,5,10):
    y=y0-v*sc;s+=f'<line x1="60" x2="455" y1="{y}" y2="{y}" stroke="#e1ddd2"/><text x="52" y="{y+5}" text-anchor="end" font-family="Carlito" font-size="14" fill="#666">{v} %</text>'
xs=[110,230,360]
for (lab,v,c,t),x in zip(bars,xs):
    h=v*sc;s+=f'<rect x="{x-35}" y="{y0-h}" width="70" height="{h}" rx="3" fill="{c}"/><text x="{x}" y="{y0-h-8}" text-anchor="middle" font-family="Carlito" font-weight="700" font-size="15" fill="#241712">{t}</text>'
    s+=f'<text x="{x}" y="{y0+22}" text-anchor="middle" font-family="Carlito" font-size="14.5" fill="#555">{lab.format(x=x)}</text>'
s+=f'<line x1="60" x2="455" y1="{y0}" y2="{y0}" stroke="#6b7b72" stroke-width="2"/><line x1="296" x2="296" y1="55" y2="{y0}" stroke="#4f8a63" stroke-dasharray="5 4"/>'
s+='<text x="304" y="66" font-family="Carlito" font-weight="700" font-size="14.5" fill="#4f8a63">handtvätt</text><text x="304" y="84" font-family="Carlito" font-weight="700" font-size="14.5" fill="#4f8a63">införs 1847</text>'
s+=f'<text x="455" y="{H-10}" text-anchor="end" font-family="Carlito" font-style="italic" font-size="13.5" fill="#666">Ungefärliga värden, Wien 1840–1848</text></svg>'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=b.new_page(viewport={'width':W,'height':H},device_scale_factor=3)
    pg.set_content(f'<body style="margin:0">{s}</body>');pg.screenshot(path='/tmp/bio/fig01/f_semmelweis.png');b.close()

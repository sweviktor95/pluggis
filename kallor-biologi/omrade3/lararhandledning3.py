# -*- coding: utf-8 -*-
"""Lärarhandledning kapitel 2 Cellen: en gemensam handledning för alla tre nivåerna (handledning, facit, bedömningsstöd)."""
import os, re, sys
sys.path.insert(0, '/tmp/bio')
os.environ['CH'] = '03n'
from bstyle import *
from bbuild_n import html_to_pdf, doc, OUT
import ch03n as G, ch03n_latt as L, ch03n_fordj as F, fordj_common as C
from svar_ov3 import KOLLA2

def strip_dot(t): return t.rstrip(".")
grund_h = [(strip_dot(a), b) for a, b in re.findall(r'<p><b>(.*?)</b>\s*(.*?)</p>', G.HANDLEDNING_HTML.split('</h3>', 1)[1], re.S)]
latt_h = re.findall(r'<h3 class="mm">(.*?)</h3><p class="hl">(.*?)</p>', L.HANDLEDNING_HTML, re.S)
assert len(grund_h) == 9 and len(latt_h) == 9, (len(grund_h), len(latt_h))
TITLES = [t for _, t, _ in G.S]
FORD = {1: ([0, 2], [0]), 2: ([1], [1]), 3: ([3], [2]), 5: ([4], [3, 4]), 7: ([5], [5])}   # moment-index -> (UPG-index, RUTOR-index)

def delomr_of(i):
    return "Start" if i == 0 else ("3.1" if i <= 4 else "3.2")

def kolla_facit(inner):
    qs = re.findall(r'<li>(.*?)</li>', "".join(re.findall(r'<div class="kolla">.*?</div>', inner, re.S)), re.S)
    return "".join(f"<li><i>{q}</i><br>{KOLLA2.get(q, '')}</li>" for q in qs)

body = []
body.append('<section class="sec"><div class="pill">Kapitel 3 · Lärarhandledning</div><h1 style="font:700 28pt Carlito;margin:8pt 0 2pt">Biologisk mångfald</h1>'
            '<p style="font-size:13pt"><i>En gemensam handledning för Lättläst, Grundtext och Fördjupning: handledning, facit och bedömningsstöd per moment.</i></p>'
            f'<h3>Om kapitlet</h3><p>{G.LGR}</p>'
            f'<h3>Så är materialet upplagt</h3><p>{L.TILL_LARAREN}</p>'
            '<ul class="pu"><li><b>Lättläst</b> och <b>Grundtext</b> följer samma moment i samma ordning. <b>Fördjupning</b> finns för fem av nio moment (markerade nedan).</li>'
            '<li>Varje moment har en handledning, facit till övningarna i Lättläst, facit till kontrollfrågorna i Grundtext och, där det finns, svar till Fördjupning.</li>'
            '<li>Provet för området har eget facit och bedömningsstöd i prov-lärarversionen. Alla elevhäften är utan facit.</li></ul>'
            '<h3>Innehåll</h3><ol class="pu">' + "".join(f"<li>{t}</li>" for t in TITLES) + '<li>Testa dig själv, sammanfattning och bedömning</li><li>Bonuslabb och källor</li></ol></section>')

for i, (nr, t, inner) in enumerate(G.S):
    d = delomr_of(i)
    head = (f"Start · {t}" if i == 0 else (f"Delområde {d} {G.DELOMR[d]}" if i in (1, 5) else "") ) 
    pre = f'<div class="note">Delområde {d} · {G.DELOMR[d]}</div>' if d != "Start" else '<div class="note">Start</div>'
    sec = [f'<section class="sec teacher">{pre}<h2>{t}</h2>']
    sec.append(f'<h3>Handledning, Grundtext</h3><p>{grund_h[i][1]}</p>')
    sec.append(f'<h3>Handledning, Lättläst</h3><p>{latt_h[i][1]}</p>')
    kf = kolla_facit(inner)
    if kf: sec.append(f'<h3>Facit: kontrollfrågor i Grundtext</h3><ol class="pu">{kf}</ol>')
    sec.append(f'<h3>Facit: övningar i Lättläst</h3><p>{L.FACIT[i].split(":</b>", 1)[-1].strip() if ":</b>" in L.FACIT[i] else L.FACIT[i]}</p>')
    if i in FORD:
        ui, ri = FORD[i]
        sec.append('<h3>Fördjupning: svarsexempel</h3>' + "".join(f"<p><b>Uppgift {j+1}.</b> {F.SVAR[j]}</p>" for j in ui))
        if ri: sec.append('<h3>Fördjupning: svar på rutorna i texten</h3>' + "".join(f"<p><b>{F.RUTOR[j][0]}</b> {F.RUTOR[j][1]}</p>" for j in ri))
    else:
        sec.append('<p class="note">Fördjupning saknas för det här momentet.</p>')
    sec.append('</section>')
    body.append("".join(sec))

# test, sammanfattning, bedömning
t = ['<section class="sec teacher"><h2>Testa dig själv och bedömning</h2><h3>Facit: Testa dig själv, Grundtext</h3><ol class="pu">']
for n, ((dl, q, alts, pts, nl), f) in enumerate(zip(G.TEST, G.FACIT), 1):
    qq = re.sub(r"<[^>]+>", "", q if q != "TABELL" else G.TEST_D_TEXT + " (tabell med antal arter per ruta)")
    t.append(f"<li>Del {dl}. <i>{qq[:90]}{'…' if len(qq) > 90 else ''}</i><br>{f}</li>")
t.append('</ol>')
t.append('<h3>Facit: Testa dig själv, Lättläst</h3><p>' + L.FACIT[-1].split(":</b>", 1)[-1].strip() + '</p>')
t.append('<h3>Bedömningsstöd för resonemangsuppgifter</h3>' + table(["", "Grundläggande", "Utvecklade", "Välutvecklade"], C.BED))
t.append('<p class="note">Kunskapskraven är kvalitativa. Provets facit och förmågeöversikt finns i prov-lärarversionen. Förmåga 2 (systematiska undersökningar) bedöms främst i labbarna 3.1 och 3.2 och i bonuslabben.</p></section>')
body.append("".join(t))
B = G.BONUS
bl = ['<section class="sec teacher"><h2>Bonuslabb: ' + B["titel"] + '</h2><p><i>' + B["ingress"] + '</i></p><h3>Syfte</h3><p>' + B["syfte"] + '</p><h3>Material</h3><ul class="pu">' + "".join(f"<li>{x}</li>" for x in B["material"]) +
      '</ul><h3>Genomförande</h3><ol class="pu">' + "".join(f"<li>{x}</li>" for x in B["genomf"]) + '</ol><h3>Förväntat resultat</h3><p>' + B["resultat"] + '</p><h3>Säkerhet</h3><ul class="pu">' + "".join(f"<li>{x}</li>" for x in B["sakerhet"]) +
      '</ul><h3>Vanliga problem</h3><ul class="pu">' + "".join(f"<li>{x}</li>" for x in B["problem"]) + '</ul><h3>Bedömning</h3>' + table(["Nivå", "Kännetecken"], [list(x) for x in B["bedom"]]) +
      '<h3>Faktakontroll och källor</h3><p class="note">' + G.FAKTA + ' ' + "Fördjupningens källor och källstatus: se fördjupningens facit och lärarversionens källförteckning (kontrollerade 2026-10-15). Allt är utkast som bör granskas av en lärare." + '</p></section>']
body.append("".join(bl))
html = doc("".join(body), "Kapitel 3 · Biologisk mångfald · Lärarhandledning", 1, tab="3")
out = f'{OUT}/biologi-3-mangfald-lararhandledning.pdf'
html_to_pdf(html, out)
from pypdf import PdfReader
print(out, len(PdfReader(out).pages))

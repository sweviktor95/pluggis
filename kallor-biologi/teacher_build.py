# -*- coding: utf-8 -*-
"""Bygger lärarversion (samma häfte + löpande källhänvisning + källförteckning).
Användning: python3 teacher_build.py <kap: 01n|04n> <nivå: vanlig|lattlast|fordjupning> [--dry]
"""
import sys, os, re, json, html as _html
sys.path.insert(0, '/tmp/bio')
CHP, LEVEL = sys.argv[1], sys.argv[2]
DRY = '--dry' in sys.argv
os.environ['CH'] = CHP
OUTL = '/tmp/bio/out_larare'
os.makedirs(OUTL, exist_ok=True)

import kallor_ref as K
import bbuild, bbuild_n
from pypdf import PdfReader, PdfWriter

MAP = K.MAPS[(CHP, LEVEL)]
STATE = {'markers': [], 'misses': []}

KRCSS = ("sup.kr{font-size:.62em;font-weight:700;color:#14653a;vertical-align:super;line-height:0;"
         "margin-left:.08em;font-family:'Inter','Helvetica',sans-serif;letter-spacing:0}")

def needle_re(needle):
    parts = []
    for i, c in enumerate(needle):
        last = (i == len(needle) - 1)
        if c == ' ':
            parts.append(r'(?:\s|&nbsp;|\u00a0|<[^>]*>)+')
        else:
            parts.append(re.escape(c) + ('' if last else r'(?:<[^>]*>)*'))
    return re.compile(''.join(parts))

def insert_markers(h):
    found = []
    for needle, claim, refs in MAP:
        m = needle_re(needle).search(h)
        if not m:
            STATE['misses'].append(needle); continue
        found.append((m.end(), claim, refs, needle))
    found.sort(key=lambda x: x[0])
    out, last, n = [], 0, 0
    # flera nålar på samma position -> ett gemensamt nummer vore krångligt; ge varje eget
    for pos, claim, refs, needle in found:
        n += 1
        out.append(h[last:pos]); out.append(f'<sup class="kr">[{n}]</sup>'); last = pos
        STATE['markers'].append((n, claim, refs))
    out.append(h[last:])
    h = ''.join(out)
    h = h.replace('</style>', KRCSS + '</style>', 1)
    return h

RIBBON = ('<div style="position:fixed;top:7mm;right:9mm;background:#14653a;color:#fff;font:700 9pt Helvetica,sans-serif;'
          'padding:2mm 4mm;border-radius:2mm;letter-spacing:.04em;z-index:99">LÄRARVERSION · [n] = källhänvisning, se källförteckningen sist</div>')

def wrap(orig):
    def f(html, path, *a, **k):
        base = os.path.basename(path)
        if base.endswith('_body.pdf'):
            html = insert_markers(html)
        elif base.endswith('_p1.pdf'):
            html = html.replace('</body>', RIBBON + '</body>', 1)
        elif base.endswith('_teacher.pdf'):
            pass
        return orig(html, path, *a, **k)
    return f

for mod in (bbuild, bbuild_n):
    mod.OUT = OUTL
    mod.html_to_pdf = wrap(mod.html_to_pdf)

# ---- bygg elevhäftet (utan komplett) i OUTL
if LEVEL == 'vanlig':
    M = bbuild_n.M
    res = bbuild_n.build_vanlig(M, komplett=False)
    student = res['vanlig']; NR, SLUG, NAMN = M.NR, M.SLUG, M.NAMN
    FOOT = f'Kapitel {M.NR} · {M.NAMN}'
elif LEVEL == 'lattlast':
    import bbuild_latt
    bbuild_latt.OUT = OUTL
    res = bbuild_latt.build(komplett=False)
    L = bbuild_latt.L
    student = res['lattlast']; NR, SLUG, NAMN = L.NR, L.SLUG, L.NAMN
    FOOT = f'Kapitel {L.NR} · {L.NAMN} · Lättläst'
else:
    import runpy
    # fordj-skriptet bygger även komplett-pdf; vi använder bara den vanliga
    g = runpy.run_path('/tmp/bio/bbuild_fordj_n.py')
    M = g['M']
    student = f'{OUTL}/biologi-{M.NR}-{M.SLUG}-fordjupning.pdf'
    NR, SLUG, NAMN = M.NR, M.SLUG, M.NAMN
    FOOT = f'Fördjupning {M.NR} · {M.NAMN}'

print('MISSES:', STATE['misses'])
print('MARKERS:', len(STATE['markers']))
if DRY: sys.exit(0)

# ---- källförteckning
def esc(s): return _html.escape(s, quote=False)
parts = [f'<div class="kk"><h1>Källförteckning för lärare</h1>'
 '<p class="lead">Siffrorna [1], [2] … i texten hänvisar hit. Varje post säger vilket påstående i häftet som avses, '
 'vilka källor som stöder det och hur långt vi har kunnat kontrollera det.</p>'
 '<div class="leg"><b>Så läser du statusen</b><ul>'
 '<li><b>Öppnad och kontrollerad</b> – sidan hämtades och uppgifterna jämfördes med texten (datum anges).</li>'
 '<li><b>Delvis kontrollerad</b> – källan stöder en del; resten står i anmärkningen.</li>'
 '<li><b>Uträknat</b> – kontrollräknat, ingen extern källa behövs.</li>'
 '<li><b>Ingen källa öppnad</b> – allmänt läroboksfaktum som ännu inte är kontrollerat mot en källa.</li></ul>'
 '<p>Många av källorna är sekundära (uppslagsverk, undervisningssidor, Wikipedia). Använd dem som utgångspunkt och gå vidare till originalen. '
 'Granskningen är gjord av Claude och är inte en ämnesgranskning av en lärare.</p></div>']
SEEN = {}
for n, claim, refs in STATE['markers']:
    items = []
    for rid in refs:
        r = K.REFS[rid]
        if rid in SEEN:
            items.append(f'<div class="ref s{r["s"]}"><div class="rt">{esc(r["t"])} <span class="st">{esc(K.STATUS[r["s"]])}</span></div><div class="n">Anmärkning och länk: se [{SEEN[rid]}].</div></div>')
            continue
        SEEN[rid] = n
        stat = K.STATUS[r['s']]
        link = f'<a href="{r["u"]}">{esc(r["u"])}</a>' if r['u'] else ''
        more = f'<div class="m"><b>Läs mer:</b> {esc(r["m"])}</div>' if r['m'] else ''
        items.append(f'<div class="ref s{r["s"]}"><div class="rt">{esc(r["t"])} <span class="st">{esc(stat)}</span></div>'
                     f'{("<div class=u>"+link+"</div>") if link else ""}<div class="n">{esc(r["n"])}</div>{more}</div>')
    parts.append(f'<div class="post"><div class="pc"><span class="nr">[{n}]</span> {esc(claim)}</div>{"".join(items)}</div>')
parts.append('</div>')
KKCSS = """
.kk h1{font-size:19pt;color:#14653a;margin:0 0 3mm}
.kk .lead{font-size:10pt;margin:0 0 3mm}
.kk .leg{background:#eef6f0;border-left:3px solid #14653a;padding:2.5mm 4mm;font-size:8.6pt;margin-bottom:4mm}
.kk .leg ul{margin:1mm 0 1mm 4mm;padding:0}.kk .leg p{margin:1mm 0 0}
.kk .post{break-inside:avoid;border-top:1px solid #cfe0d4;padding:2mm 0 1.5mm;font-size:8.4pt;line-height:1.38}
.kk .pc{font-weight:700;margin-bottom:1mm}.kk .nr{color:#14653a}
.kk .ref{margin:0 0 1.4mm 4mm}.kk .rt{font-weight:600}
.kk .st{font-weight:600;font-size:7.4pt;padding:.3mm 1.6mm;border-radius:1mm;background:#e3f1e7;color:#14653a;margin-left:1.5mm}
.kk .sD .st{background:#fdf1d6;color:#7a5600}.kk .sE .st{background:#fbe3e0;color:#8b2a20}.kk .sR .st{background:#e5ecf7;color:#26457a}
.kk .u{font-size:7.4pt;color:#555;word-break:break-all}.kk .u a{color:#555;text-decoration:none}
.kk .n{color:#222}.kk .m{color:#333}
"""
n_pages = len(PdfReader(student).pages)
body = ''.join(parts)
html = bbuild_n.doc(body, FOOT + ' · Källor', n_pages + 1, tab='4', extra=KKCSS)
kk = f'{OUTL}/_kk_{CHP}_{LEVEL}.pdf'
bbuild_n.html_to_pdf.__wrapped__ if False else None
# anropa originalfunktionen utan markörinsättning (namnet slutar inte på _body.pdf)
bbuild_n.html_to_pdf(html, kk)
w = PdfWriter()
for f in (student, kk):
    for pg in PdfReader(f).pages: w.add_page(pg)
final = f'{OUTL}/biologi-{NR}-{SLUG}-{ {"vanlig":"vanlig","lattlast":"lattlast","fordjupning":"fordjupning"}[LEVEL] }-lararversion.pdf'
w.write(final)
print('OK', final, 'sidor:', len(PdfReader(final).pages), 'elevhäfte:', n_pages)

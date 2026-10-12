# -*- coding: utf-8 -*-
import sys, os, re, subprocess, importlib
sys.path.insert(0, '/tmp/bio')
from bstyle import *
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

OUT = '/tmp/bio/out'
os.makedirs(OUT, exist_ok=True)

def html_to_pdf(html, path, landscape=False):
    hp = path + '.html'
    open(hp, 'w', encoding='utf8').write(html)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = b.new_page()
        pg.goto('file://' + hp)
        pg.wait_for_timeout(400)
        pg.pdf(path=path, prefer_css_page_size=True, print_background=True)
        b.close()

def page_texts(pdf):
    r = PdfReader(pdf)
    return [(pg.extract_text() or '') for pg in r.pages]

def doc(body, foot, start, tab="4"):
    bg = ('@page{@right-top{content:"%s";background:linear-gradient(to right,transparent 7.3mm,#2f6b4f 7.3mm);'
          'color:#fff;font:700 11pt Carlito;padding-left:7.3mm;text-align:center;vertical-align:middle;height:16mm;margin-top:8mm}}' % tab)
    return (f'<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(foot, start)}{bg}</style></head>'
            f'<body>{body}</body></html>')

# ---------------------------------------------------------------- delar
def sam_html(samman, begr):
    return ('<section class="sec"><div class="sh"><h2>Sammanfattning</h2></div>'
            '<div class="sam"><ul>' + "".join(f"<li>{x}</li>" for x in samman) + '</ul></div>'
            '<h3>Viktiga begrepp</h3><div class="begr">' + "".join(f"<div><b>{t}</b>{d}</div>" for t, d in begr) + '</div></section>')

def test_html(M, nivaer=True):
    out = ['<section class="sec"><div class="sh"><h2>Testa dig själv</h2></div>'
           '<p class="note">Uppgifterna är byggda som i nationella prov i biologi. ● grundläggande &nbsp;●● utvecklat &nbsp;●●● välutvecklat</p>']
    last = None
    n = 0
    for (d, q, alts, pts, nl) in M.TEST:
        n += 1
        if d != last:
            out.append(f'<div class="pill">Del {d} · {M.DEL_NAMN[d].upper()}</div>')
            last = d
        dots = "●" * pts
        if q == "TABELL":
            out.append(f'<div class="q"><span class="n">{n}</span><div>{M.TEST_D_TEXT}'
                       + table(M.TEST_TABELL[0], M.TEST_TABELL[1], "tbl num")
                       + "".join(f"<div>{s}</div>" for s in M.TEST_D_SUB) + lines(3) + f'</div><span class="pts">{dots}</span></div>')
            continue
        a = ""
        if alts:
            longalts = max(len(x) for x in alts) > 40
            a = f'<div class="alts{" one" if longalts else ""}">' + "".join(f"<div>{x}</div>" for x in alts) + "</div>"
        l = lines(max(nl - 1, 2)) if nl else ""
        out.append(f'<div class="q"><span class="n">{n}</span><div>{q}{a}{l}</div><span class="pts">{dots}</span></div>')
    out.append('</section>')
    return "".join(out)

def teacher_vanlig(M):
    f = M.FACIT
    items = []
    for i, x in enumerate(f, 1):
        items.append(f"<p><b>{i}.</b> {x}</p>")
    facit = '<div class="cols2">' + "".join(items) + '</div>'
    return ('<section class="sec teacher"><h2>Till läraren: facit och kopplingar</h2>'
            '<h3>Koppling till Lgr22 och nationella prov</h3><p>' + M.LGR + '</p>'
            '<h3>Facit – Testa dig själv</h3>' + facit +
            '<h3>Faktakontroll och källor</h3><p class="note">' + M.FAKTA + '</p></section>')

def bonus_html(M):
    B = M.BONUS
    mat = "".join(f"<li>{x}</li>" for x in B['material'])
    gen = "".join(f"<li>{x}</li>" for x in B['genomf'])
    sak = "".join(f"<li>{x}</li>" for x in B['sakerhet'])
    pro = "".join(f"<li>{x}</li>" for x in B['problem'])
    bed = '<table class="tbl">' + "<tr>" + "".join(f"<th>{a}</th>" for a, _ in B['bedom']) + "</tr><tr>" + "".join(f"<td style='font-weight:400'>{b}</td>" for _, b in B['bedom']) + "</tr></table>"
    return ('<section class="sec teacher"><div class="pill">Lärarhandledning · Bonuslabb</div><h2>' + B['titel'] + '</h2><p>' + B['ingress'] + '</p>'
            '<div class="cols2"><h3>Syfte och koppling</h3><p>' + B['syfte'] + '</p><h3>Tid och grupper</h3><p>' + B['tid'] + '</p>'
            '<h3>Material per grupp</h3><ul class="pu">' + mat + '</ul>'
            '<h3>Genomförande – tips</h3><ol class="steps g">' + gen + '</ol>'
            '<h3>Förväntat resultat och förklaring</h3><p>' + B['resultat'] + '</p>'
            '<h3>Säkerhet och etik</h3><ul class="pu">' + sak + '</ul>'
            '<h3>Vanliga problem</h3><ul class="pu">' + pro + '</ul></div>'
            '<h3>Bedömning</h3>' + bed + '</section>')

def elevblad(M):
    return ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
            '<div class="sh small"><h2>Småkryp i förnan</h2></div>') + _elev_tail()

def _elev_tail():
    steps_ = ["Lägg förnan löst på nätet i tratten.", "Ställ burken under tratten och lampan ovanför.", "Låt stå 1–3 dygn.",
              "Töm burken i en petriskål. Sortera djuren med pensel och lupp.", "Räkna hur många du hittar av varje sort."]
    djur = ["Hoppstjärtar", "Kvalster", "Gråsuggor", "Spindlar", "Tusenfotingar", "Skalbaggar", "Övriga"]
    t = table(["Djur", "Antal", "Äter"], [[d, "", ""] for d in djur], "tbl num")
    return ('<p>Plats där förnan samlades: ______________________________</p>'
            '<div class="row"><div class="main"><h3>Gör så här</h3>' + steps(steps_, True) + '</div>'
            '<div class="side"></div></div>' + t +
            '<h3>Frågor</h3><ol class="steps g"><li>Varför går djuren nedåt i tratten?</li>' + '</ol>' + lines(2) +
            '<ol class="steps g"><li>Vilka av djuren hjälper till med nedbrytningen?</li></ol>' + lines(2) +
            '<ol class="steps g"><li>Rita en näringsväv med minst fyra av djuren du hittade.</li></ol>' + lines(6) +
            '<ol class="steps g"><li>Vad tror du händer med nedbrytningen om marken blir mycket torr?</li></ol>' + lines(2) + '</section>')

# ---------------------------------------------------------------- förstasida
def first_page(M, variant, pages):
    cover = {'vanlig': 'cover_vanlig.png', 'lattlast': 'cover_lattlast.png', 'fordjupning': 'cover_fordjupning.png'}[variant]
    band = '#2f6b4f' if variant != 'fordjupning' else '#24503b'
    titel = M.NAMN if variant != 'fordjupning' else 'Fördjupning: ' + M.NAMN
    under = M.UNDER
    toc = ""
    for nr, t, pg in pages:
        toc += f'<div class="toc"><span>{nr}</span><span>{t}</span><span class="pgn">{pg}</span></div>'
    lara = "".join(f"<li>{x}</li>" for x in M.MAL)
    return f"""<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css('Kapitel 4 · Ekologi', 1)}
@page{{margin:0}}
body{{margin:0}}
.cv img{{width:210mm;height:87.6mm;display:block}}
.band{{background:{band};color:#fff;height:36mm;padding:7mm 18mm 0}}
.band h1{{font:700 34pt Carlito;margin:0}}.band p{{font:15pt Carlito;margin:3pt 0 0}}
.in{{padding:7mm 18mm 0}}
.intro{{font:italic 10.4pt/1.5 Lora;margin:0 0 6mm}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.lar{{background:#e7eef5;border-radius:6pt;padding:9pt 11pt;font:9.4pt/1.35 Carlito}}
.lar .rb{{font:700 8pt Carlito;letter-spacing:1pt;color:#2b5d7a;margin-bottom:5pt;display:block}}
.lar ul{{margin:0;padding-left:11pt}}.lar li{{margin:0 0 3pt}}
.toc{{display:grid;grid-template-columns:22pt 1fr 24pt;font:9.6pt Carlito;padding:3pt 0;border-bottom:.5pt dotted #aaa}}
.toc .pgn{{text-align:right}}
.fun{{background:#fdefe3;border-radius:6pt;padding:8pt 11pt;margin-top:8pt;font:9.4pt/1.35 Carlito}}
.fun .rb{{font:700 8pt Carlito;letter-spacing:1pt;color:#a84d22;display:block;margin-bottom:3pt}}
.ft{{position:absolute;left:18mm;right:14.8mm;bottom:11mm;display:flex;justify-content:space-between;font:8.4pt Carlito;color:#6b625b}}
.ft b{{color:#2f6b4f;font-size:8.8pt}}
</style></head><body><div class="cv"><img src="file:///tmp/bio/fig/{cover}"></div>
<div class="band"><h1>{titel}</h1><p>{under}</p></div>
<div class="in"><p class="intro">{M.INTRO}</p>
<div class="two"><div class="lar"><span class="rb">DET HÄR SKA DU LÄRA DIG</span><ul>{lara}</ul></div>
<div>{toc}<div class="fun"><span class="rb">FUNDERA INNAN DU LÄSER</span>{M.FUNDERA}</div></div></div></div>
<div class="ft"><span>Kapitel 4 · Ekologi</span><b>1</b></div></body></html>"""

# ---------------------------------------------------------------- vanlig
def build_vanlig(M, komplett=False):
    secs = list(M.S)
    body = "".join(f'<section class="sec">{h(nr, t)}{inner}</section>' if False else
                   f'<section class="sec">{head(nr, t)}{inner}</section>' for nr, t, inner in secs)
    body += '<section class="sec">' + M.LAB_HTML + '</section>'
    body += sam_html(M.SAMMAN, M.BEGR)
    body += test_html(M)
    tmp = f'{OUT}/_vanlig_body.pdf'
    html_to_pdf(doc(body, 'Kapitel 4 · Ekologi', 2), tmp)
    texts = page_texts(tmp)
    def find(s, start=0):
        for i in range(start, len(texts)):
            if s in re.sub(r"\s+", " ", texts[i][:500].replace("ﬂ","fl").replace("ﬁ","fi")):
                return i + 2
        return '?'
    pages = []
    for nr, t, _ in secs:
        pages.append((nr, t, find(t)))
    pages.append(('', 'Undersök: nedbrytning', find('Undersök: Var bryts')))
    pages.append(('', 'Sammanfattning och begrepp', find('Sammanfattning')))
    a = find('Testa dig själv');
    n = len(texts) + 1
    pages.append(('', 'Testa dig själv', f'{a}–{n}'))
    first = f'{OUT}/_vanlig_p1.pdf'
    html_to_pdf(first_page(M, 'vanlig', pages), first)
    res = {}
    w = PdfWriter()
    for f in (first, tmp):
        for pg in PdfReader(f).pages: w.add_page(pg)
    name = f'{OUT}/biologi-4-ekologi-vanlig.pdf'
    w.write(name); res['vanlig'] = name
    if komplett:
        t2 = f'{OUT}/_vanlig_teacher.pdf'
        body2 = teacher_vanlig(M) + bonus_html(M) + elevblad(M)
        html_to_pdf(doc(body2, 'Kapitel 4 · Ekologi', len(texts) + 2), t2)
        w2 = PdfWriter()
        for f in (name, t2):
            for pg in PdfReader(f).pages: w2.add_page(pg)
        name2 = f'{OUT}/biologi-4-ekologi-vanlig-komplett.pdf'
        w2.write(name2); res['vanlig-komplett'] = name2
    return res

if __name__ == '__main__':
    import ch04 as M
    print(build_vanlig(M, komplett='--k' in sys.argv))

# -*- coding: utf-8 -*-
"""Prov kapitel 3 + 4 (Biologisk mångfald, Ekologi) för anpassade grundskolan (NO). Elevversion och lärarversion.
Kör: python3 kallor-biologi/prov34_anpassad.py   Resultat: planering/biologi-omrade4/biologi-3-4-prov-anpassad-{elev,larare}.pdf"""
import os, base64
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, 'fig34')
OUT = os.path.join(HERE, '..', 'planering', 'biologi-omrade4')

def img(name, h=None, w=None, cls=''):
    b = base64.b64encode(open(os.path.join(FIG, name), 'rb').read()).decode()
    st = (f'height:{h}mm;' if h else '') + (f'width:{w}mm;' if w else '')
    return f'<img class="{cls}" style="{st}" src="data:image/png;base64,{b}" alt="">'

def L(n, cls=''):
    return f'<div class="ln {cls}"></div>' * n

def box(t):  # kryssruta + text
    return f'<span class="opt"><span class="cb"></span>{t}</span>'

# ---------------------------------------------------------------- frågor
# (förmåga, bild/innehåll-funktion, facit, bedömningsstöd)
LEV = [('gran', 'Gran'), ('hare', 'Hare'), ('svamp', 'Svamp'), ('sol', 'Sol'), ('vatten', 'Vatten'), ('sten', 'Sten')]
def q1():
    cells = ''.join(f'<div class="lev"><div class="lh">{img("lev_"+k+".png", h=19)}</div><b>{n}</b>'
                    f'<div class="lv">{box("Levande")}{box("Inte levande")}</div></div>' for k, n in LEV)
    return 'Är det levande eller inte levande? Kryssa ett svar under varje bild.' + f'<div class="levrad">{cells}</div>'

def q4():
    return ('Titta på bilderna. Vilken bild passar till vilket ord? Skriv A, B eller C på strecket.'
            '<div class="tre">'
            f'<div>{img("tre_a.png", h=30)}<b>A</b></div><div>{img("tre_b.png", h=30)}<b>B</b></div><div>{img("tre_c.png", h=30)}<b>C</b></div></div>'
            '<table class="t"><tr><th>Ord</th><th>Det betyder</th><th>Bild</th></tr>'
            '<tr><td><b>Producent</b></td><td>Gör egen mat med solljus</td><td class="sv">___</td></tr>'
            '<tr><td><b>Konsument</b></td><td>Äter växter eller andra djur</td><td class="sv">___</td></tr>'
            '<tr><td><b>Nedbrytare</b></td><td>Bryter ner det som är dött</td><td class="sv">___</td></tr></table>')

def q5():
    return ('Det här är en näringsväv. Pilen pekar mot den som <b>äter</b>.'
            f'<div class="c">{img("vav.png", h=58)}</div>'
            '<div class="sub"><b>a)</b> Vad äter haren? Skriv ett svar. <span class="inl">______________</span></div>'
            '<div class="sub"><b>b)</b> Vem äter haren? Skriv ett svar. <span class="inl">______________</span></div>'
            '<div class="sub"><b>c)</b> Vilken är en producent? Kryssa ett.<br>' + box('Gräs') + box('Hare') + box('Räv') + '</div>')

def q11():
    return ('<span class="fk">Påhittade värden</span> Elever räknade hur många olika växtarter som fanns i en ruta på 1 m × 1 m. '
            'De räknade på två platser.'
            f'<div class="duo">{img("provruta.png", h=40)}'
            '<table class="t"><tr><th>Plats</th><th>Antal arter i rutan</th></tr>'
            '<tr><td>Äng</td><td>14</td></tr><tr><td>Gräsmatta</td><td>3</td></tr></table></div>'
            '<div class="sub"><b>a)</b> Vilken plats har flest arter? ' + box('Äng') + box('Gräsmatta') + '</div>'
            '<div class="sub"><b>b)</b> Vilken plats har störst biologisk mångfald? ' + box('Äng') + box('Gräsmatta') + '</div>'
            '<div class="sub"><b>c)</b> Eleverna använde en ruta lika stor på båda platserna. Varför?<br>' + box('Då blir det rättvist att jämföra') + box('Då blir det roligare') + '</div>')

# nr, titel/förmåga, frågehtml, antal skrivrader, facit, stöd
Q = [
 # ---- Del A
 ('A', 1, 'Levande eller inte', q1(), 0,
  'Gran, hare och svamp är levande. Sol, vatten och sten är inte levande.',
  'Begrepp: skiljer levande från icke-levande. Allt rätt = visar. 4–5 rätt = delvis.'),
 ('A', 2, 'Vad växter behöver',
  'Vad behöver en växt för att växa? Kryssa <b>tre</b>.<br>' + box('Ljus') + box('Vatten') + box('Näring från jorden') + box('Godis') + box('Plast'), 0,
  'Ljus, vatten och näring från jorden.',
  'Miljöfaktorer: känner till vad växter behöver. Tre rätt = visar. Två rätt = delvis.'),
 ('A', 3, 'Miljö påverkar växter',
  'Det regnar inte på hela sommaren. Vad händer med växterna i en äng?<br>' + box('De mår bra') + box('De torkar och mår dåligt') + box('De blir fler'), 0,
  'De torkar och mår dåligt.',
  'Miljöfaktorer: kopplar brist på vatten till att växter mår dåligt.'),
 ('A', 4, 'Producent, konsument, nedbrytare', q4(), 0,
  'Producent: A (gran, solen). Konsument: B (haren). Nedbrytare: C (svamp och mask).',
  'Begrepp: kopplar tre begrepp till bilder. Alla rätt = visar. Två rätt = delvis.'),
 # ---- Del B
 ('B', 5, 'Näringsväv', q5(), 0,
  'a) Gräs eller blåbär. b) Räv eller örn. c) Gräs. Pilen visar vem som äter vem.',
  'Samband: läser en näringsväv. a–c rätt = visar. Två av tre rätt = delvis.'),
 ('B', 6, 'Energin från solen',
  'Var kommer energin i naturen ifrån från början?<br>' + box('Från solen') + box('Från räven') + box('Från vattnet'), 0,
  'Från solen.',
  'Samband: vet att solen är den första energikällan.'),
 ('B', 7, 'Kretslopp',
  'Ett löv faller ner på marken och dör. Vad händer sedan? Skriv 1, 2 och 3 i rätt ordning.'
  '<div class="sub"><span class="nr">___</span> Växter tar upp näringen och växer.</div>'
  '<div class="sub"><span class="nr">___</span> Nedbrytare gör lövet till näring i jorden.</div>'
  '<div class="sub"><span class="nr">___</span> Lövet ligger på marken och är dött.</div>', 0,
  '1 = Lövet ligger på marken och är dött. 2 = Nedbrytare gör lövet till näring. 3 = Växter tar upp näringen och växer.',
  'Samband: ser att ämnen går runt i naturen. Rätt ordning = visar. Två steg rätt = delvis.'),
 ('B', 8, 'Vad händer om?',
  'Alla rävar försvinner från skogen. Vad händer med antalet harar?<br>' + box('Det blir fler harar') + box('Det blir färre harar') + box('Det blir lika många')
  + '<div class="sub"><b>Varför tror du det?</b> Skriv eller berätta.</div>', 2,
  'Det blir fler harar. Harar blir inte uppätna av rävar, och då överlever fler.',
  'Samband: Medverkar = väljer fler. Enkelt = ger en enkel orsak (”rävarna äter harar”). Utvecklat = följer kedjan: färre rävar, färre uppätna harar, fler harar.'),
 ('B', 9, 'Gräset försvinner',
  'En torr sommar försvinner nästan allt gräs. Vad kan hända med haren och med räven? Skriv eller berätta.'
  '<div class="bank"><b>Orden kan hjälpa:</b> mat · färre · äter · hare · räv · gräs</div>', 3,
  'Haren får mindre mat och blir färre. Då får räven mindre mat och blir också färre.',
  'Samband: Medverkar = säger att haren eller räven påverkas. Enkelt = förklarar ett steg. Utvecklat = förklarar båda stegen i rätt ordning.'),
 # ---- Del C
 ('C', 10, 'Biologisk mångfald',
  'Vad betyder <b>biologisk mångfald</b>?<br>' + box('Det finns många olika arter') + box('Det finns många djur av samma art') + box('Det finns bara stora djur'), 0,
  'Det finns många olika arter.',
  'Begrepp: förstår begreppet biologisk mångfald.'),
 ('C', 11, 'Undersökning: räkna arter', q11(), 0,
  'a) Äng. b) Äng. c) Då blir det rättvist att jämföra.',
  'Undersökning: tolkar en enkel tabell (a, b) och förstår varför man gör lika på båda platserna (c). Alla rätt = visar. Två rätt = delvis.'),
 # ---- Del D
 ('D', 12, 'Hot mot arter',
  'Vilka <b>två</b> är hot mot djur och växter? Kryssa två.<br>' + box('Skog hugs ner och blir bostäder') + box('Man skyddar en sjö')
  + box('Plast och gift hamnar i naturen') + box('Man planterar träd'), 0,
  'Skog hugs ner och blir bostäder. Plast och gift hamnar i naturen.',
  'Miljö: känner till hot mot arter. Två rätt = visar. Ett rätt = delvis.'),
 ('D', 13, 'Naturen ger oss',
  'Vad får vi av naturen? Kryssa <b>tre</b>.<br>' + box('Bär och svamp') + box('Trä till hus') + box('Bin som pollinerar blommor') + box('Färdig pizza'), 0,
  'Bär och svamp, trä till hus, bin som pollinerar blommor.',
  'Miljö: vet att människan är beroende av naturen. Tre rätt = visar. Två rätt = delvis.'),
 ('D', 14, 'Ta ställning',
  'En skog ska bli bostäder. I skogen växer en sällsynt blomma. Vad tycker du?<br>' + box('Bygg ändå') + box('Bygg inte') + box('Bygg en bit bort')
  + '<div class="sub"><b>Skriv eller berätta varför du tycker så.</b></div>', 3,
  'Eget val. Eleven ska kunna ge en orsak som hänger ihop med valet, till exempel att blomman kan försvinna för alltid, eller att människor behöver bostäder.',
  'Kommunicera och ta ställning: Medverkar = väljer och nämner en orsak. Enkelt = orsaken hänger ihop med valet. Utvecklat = nämner både för och emot och väger dem.'),
 ('D', 15, 'Vad kan du göra?',
  'Vad kan du göra för att skydda naturen? Skriv, rita eller berätta ett exempel.', 3,
  'Exempel: plocka inte hotade blommor, slänga skräp rätt, åka kollektivt, spara el, inte köpa mer än man behöver.',
  'Miljö och hållbar utveckling: ger ett rimligt eget exempel. Utvecklat = förklarar också hur det hjälper naturen.'),
]
DEL = {'A': ('Del A', 'Vad är naturen?'), 'B': ('Del B', 'Vem äter vem? Hur hänger det ihop?'), 'C': ('Del C', 'Många olika arter'), 'D': ('Del D', 'Människan och naturen')}
FORM = {'A': 'Begrepp och miljöfaktorer', 'B': 'Samband i naturen', 'C': 'Biologisk mångfald och undersökning', 'D': 'Miljö och ställningstagande'}

CSS = '''
@font-face{font-family:Carlito;src:url(file:///usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf);font-weight:400}
@font-face{font-family:Carlito;src:url(file:///usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf);font-weight:700}
@page{size:A4;margin:12mm 14mm 11mm 14mm}
*{box-sizing:border-box}html,body{margin:0}
body{font:13pt/1.38 Carlito,sans-serif;color:#241712}
.top{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5pt solid #2f6b4f;padding-bottom:4pt;margin-bottom:6pt}
h1{font:700 20pt Carlito;margin:0;color:#245040}
.nm{font-size:12pt}
.band{background:#2f6b4f;color:#fff;font:700 13pt Carlito;padding:3pt 9pt;border-radius:4pt;margin:9pt 0 5pt;break-after:avoid}
.q{display:grid;grid-template-columns:24pt minmax(0,1fr);column-gap:4pt;margin:0 0 9pt;break-inside:avoid}
.n{display:inline-block;width:21pt;height:21pt;border-radius:50%;background:#e0782f;color:#fff;font:700 12.5pt/21pt Carlito;text-align:center}
.opt{display:inline-block;margin:3pt 14pt 3pt 0;white-space:nowrap}
.cb{display:inline-block;width:14pt;height:14pt;border:1.8pt solid #333;border-radius:3pt;vertical-align:-3pt;margin-right:5pt}
.ln{border-bottom:1.2pt solid #777;height:23pt}
.sub{margin:5pt 0 0}
.inl{letter-spacing:0}
.c{text-align:center;margin:4pt 0}
.levrad{display:flex;gap:6pt;margin-top:5pt}
.lev{flex:1;text-align:center;border:1.2pt solid #c7d6cc;border-radius:6pt;padding:4pt 2pt;font-size:11pt}
.lh{height:19mm;display:flex;align-items:center;justify-content:center}
.lh img{max-width:100%;object-fit:contain}
.lv{display:flex;flex-direction:column;align-items:flex-start;padding-left:4pt;margin-top:3pt}
.lv .opt{margin:1pt 0;font-size:10.5pt}
.lv .cb{width:11pt;height:11pt;vertical-align:-2pt;margin-right:3pt}
.tre{display:flex;gap:8pt;justify-content:center;margin:5pt 0;text-align:center}
.tre div{flex:1;border:1.2pt solid #c7d6cc;border-radius:6pt;padding:3pt}
.tre img{max-width:100%}
.tre b{display:block;font-size:14pt}
table.t{border-collapse:collapse;margin:5pt 0;width:100%}
table.t th{background:#2f6b4f;color:#fff;text-align:left;padding:3pt 7pt;font-size:12pt}
table.t td{border:1.2pt solid #c7d6cc;padding:4pt 7pt;font-size:12.5pt}
td.sv{width:48pt;text-align:center}
.duo{display:flex;gap:12pt;align-items:center;margin:5pt 0}
.duo table{width:auto;flex:1}
.fk{background:#fff1b8;padding:0 5pt;border-radius:3pt;font-weight:700;font-size:11pt;margin-right:4pt}
.bank{background:#eaf3ec;border-radius:5pt;padding:4pt 8pt;margin:5pt 0;font-size:12pt}
.nr{display:inline-block;border-bottom:1.5pt solid #333;min-width:30pt;text-align:center;margin-right:7pt}
.ans{margin-top:5pt}
.fac{background:#eaf3ec;border-left:4pt solid #2f6b4f;border-radius:3pt;padding:4pt 8pt;margin-top:5pt;font-size:12pt;break-inside:avoid}
.fac .st{color:#4a3a30;font-size:11pt;margin-top:3pt}
.fac .gr{display:flex;gap:16pt;margin-top:4pt;font-size:11pt}
.fm{display:inline-block;background:#245040;color:#fff;border-radius:9pt;padding:0 7pt;font-size:10pt;margin-left:6pt}
.info{font-size:11.5pt;color:#444;margin:0 0 6pt}
h2{font:700 15pt Carlito;color:#245040;margin:12pt 0 4pt}
p{margin:4pt 0}
ul{margin:4pt 0 4pt 16pt;padding:0}li{margin:2pt 0}
.src{font-size:10.5pt;color:#444}
.pb{break-before:page}
'''

def qhtml(q, teacher):
    dl, nr, titel, body, rader, facit, stod = q
    h = f'<div class="q"><div><span class="n">{nr}</span></div><div>{body}'
    h += L(rader) if rader else ''
    if teacher:
        h += (f'<div class="fac"><b>Facit:</b> {facit}<div class="st"><b>Bedömning:</b> {stod}</div>'
              '<div class="gr"><span>☐ Visar</span><span>☐ Visar delvis</span><span>☐ Inte ännu</span></div></div>')
    return h + '</div></div>'

def page(teacher):
    h = f'<style>{CSS}</style>'
    h += ('<div class="top"><h1>Prov: Natur och ekologi</h1><div class="nm">Namn: ____________________ &nbsp; Datum: __________</div></div>')
    if not teacher:
        h += '<p class="info">Biologisk mångfald och ekologi. Läs frågan eller be om hjälp att läsa. Svara med kryss, streck eller ord. Du kan också berätta för din lärare.</p>'
    else:
        h += ('<p class="info"><b>Lärarversion med facit och bedömningsstöd.</b> Prov i naturorienterande ämnen för anpassade grundskolan, årskurs 7–9, '
              'med fokus på biologisk mångfald och ekologi (kapitel 3–4).</p>')
    cur = None
    for q in Q:
        if q[0] != cur:
            cur = q[0]
            t = DEL[cur]
            h += f'<div class="band">{t[0]}: {t[1]}</div>'
        h += qhtml(q, teacher)
    if teacher:
        h += '<div class="pb"></div>' + TEACHER_BACK
    return h

TEACHER_BACK = '''
<h2>Så hänger provet ihop med kursplanen</h2>
<p>Provet utgår från kursplanen i naturorienterande ämnen för anpassade grundskolan, åk 7–9, och dess centrala innehåll
<i>Natur, miljö och samhälle</i> (biologisk mångfald, näringskedjor och kretslopp, hur miljöfaktorer påverkar djur, växter och svampar, människans beroende av naturen och ansvar för hållbar utveckling)
samt <i>Systematiska undersökningar</i> (observationer och fältstudier, att läsa av och värdera resultat). Frågor om kropp och hälsa ingår inte.</p>
<h2>Förmågor, inte poäng</h2>
<p>Provet har inga poäng. Varje fråga bedöms som <b>visar</b>, <b>visar delvis</b> eller <b>inte ännu</b>, och du ser vad eleven visar per förmåga:</p>
<ul>
<li><b>Del A, Begrepp och miljöfaktorer</b> (fråga 1–4): använda begrepp som levande, producent, konsument och nedbrytare, och veta vad växter behöver.</li>
<li><b>Del B, Samband i naturen</b> (fråga 5–9): beskriva samband i näringsvävar, energiflöde, kretslopp och vad som händer om något förändras.</li>
<li><b>Del C, Biologisk mångfald och undersökning</b> (fråga 10–11): förstå begreppet och tolka en enkel undersökning.</li>
<li><b>Del D, Miljö och ställningstagande</b> (fråga 12–15): känna till hot, se hur människan är beroende av naturen, ta ställning och kommunicera om miljö.</li>
</ul>
<p>Kunskapskraven i slutet av årskurs 9 beskriver att eleven <i>medverkar i att beskriva</i> samband (E), beskriver dem <i>enkelt</i> (C) eller <i>utvecklat</i> (A).
I de öppna frågorna (8, 9, 14, 15) finns därför ett svar som visar att eleven <b>medverkar</b>, ett som är <b>enkelt</b> och ett som är <b>utvecklat</b>. Det är elevens helhet över hela provet som visar var eleven befinner sig, och provet är ett av flera underlag.</p>
<h2>Anpassningar</h2>
<ul>
<li>Läs gärna upp frågorna, och låt eleven svara muntligt eller peka. Skriv ner det eleven säger.</li>
<li>Dela provet i två eller tre tillfällen, till exempel en del per tillfälle.</li>
<li>Låt eleven ha begreppen och bilderna från kapitlen framme om det är så ni har arbetat.</li>
<li>Rita eller skriv med dator är lika bra som handskrift. Skriv ner vilka stöd eleven haft, så att du kan jämföra mellan tillfällen.</li>
</ul>
<h2>Underlag och källor</h2>
<p class="src">Alla värden i fråga 11 är påhittade. Bilderna kommer från kapitel 3–4 i Pluggis.<br>
Skolverket, kursplan i naturorienterande ämnen för anpassade grundskolan: <b>syllabuswebb.skolverket.se/subject/GRSANAT01/8</b> (kontrollera gärna aktuell version).</p>
'''

def build():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = b.new_page()
        for teacher, name in [(False, 'biologi-3-4-prov-anpassad-elev.pdf'), (True, 'biologi-3-4-prov-anpassad-larare.pdf')]:
            pg.set_content(f'<html><meta charset="utf-8"><body>{page(teacher)}</body></html>')
            pg.wait_for_timeout(300)
            f = os.path.join(OUT, name)
            pg.pdf(path=f, format='A4', print_background=True, prefer_css_page_size=True)
            print('wrote', os.path.normpath(f))
        b.close()

if __name__ == '__main__':
    build()

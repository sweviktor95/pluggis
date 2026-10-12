# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)
BED = [["Resonemang", "Enkla påståenden, ett led. Orsak eller verkan nämns.", "Orsak och verkan kopplas ihop i två led.", "Flera led i en sammanhängande kedja. Visar hur stegen hänger ihop."],
       ["Begrepp", "Några begrepp används, ibland oprecist.", "Relevanta begrepp används korrekt.", "Begreppen används korrekt och förklaras i sammanhanget."],
       ["Värdering", "Ger ett argument eller en åsikt.", "Ger argument för och emot.", "Väger argument mot varandra, visar osäkerheter och tar motiverat ställning."],
       ["Undersökningar", "Föreslår en enkel undersökning.", "Planerar med variabler och upprepningar.", "Värderar metoden, felkällor och hur säker slutsatsen kan bli."]]
def uppg_html(UPG, split=4):
    out = ['<section class="sec"><div class="sh"><h2>Resonera och ta ställning</h2></div>'
           '<p class="note">Uppgifterna liknar de svåraste uppgifterna på nationella prov. Personer, rubriker och mätvärden är påhittade. Svara utförligt och resonera i flera led. ● grundläggande &nbsp;●● utvecklat &nbsp;●●● välutvecklat</p>']
    for i, (q, p) in enumerate(UPG, 1):
        if i == split:
            out.append('</section><section class="sec"><div class="sh"><h2>Resonera och ta ställning, forts.</h2></div>')
        out.append(f'<div class="q" style="break-inside:avoid;grid-template-columns:16pt minmax(0,1fr) 34pt"><span class="n">{i}</span><div>{q}{lines(7)}</div><span class="pts">{"●"*p}</span></div>')
    out.append('</section>')
    return "".join(out)
def teacher_html(intro, SVAR, rutor, fakta):
    sv = '<div class="cols2">' + "".join(f"<p><b>{i}.</b> {x}</p>" for i, x in enumerate(SVAR, 1)) + '</div>'
    bed = table(["", "Grundläggande", "Utvecklat", "Välutvecklat"], BED)
    return ('<section class="sec teacher"><h2>Till läraren: facit och bedömningsstöd</h2><p>' + intro + '</p><h3>Svarsexempel</h3>' + sv + '</section>'
            '<section class="sec teacher"><h2>Till läraren: bedömning och svar på rutorna</h2><h3>Bedömningsstöd för resonemangsuppgifter</h3>' + bed +
            '<h3>Svar på rutorna i texten</h3>' + "".join(f"<p><b>{a}</b> {b}</p>" for a, b in rutor) +
            '<h3>Faktakontroll och källor</h3><p class="note">' + fakta + '</p></section>')

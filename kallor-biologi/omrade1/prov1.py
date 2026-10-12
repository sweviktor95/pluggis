# -*- coding: utf-8 -*-
"""Prov område 1 Biologi som vetenskap: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os
sys.path.insert(0, '/tmp/bio')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader, PdfWriter

FIG = '/tmp/bio/fig01n/'
ANNONS = ('<div class="fakeann"><span class="fake">Påhittad annons</span></div><div style="border:1pt solid #d9d2c8;border-radius:5pt;padding:5pt 8pt;margin:4pt 0"><b>NYHET! DetoxPlåstret™</b><br>Sätt plåstret under foten när du sover – på morgonen har det blivit brunt av alla gifter som dragits ut ur kroppen! ”Jag har aldrig mått så bra”, säger Anna, 34. Vetenskapligt utvecklat.</div>')
TABELL = table(["Temperatur", "Försök 1", "Försök 2", "Försök 3"], [["10 °C", "13 cm", "12 cm", "14 cm"], ["25 °C", "22 cm", "24 cm", "23 cm"], ["40 °C", "31 cm", "18 cm", "30 cm"]], "tbl num")

def match(left, right):
    return ('<table class="tbl num" style="width:92%"><tr><th>Forskare</th><th>Upptäckt</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')

# nivå, fråga, alternativ, poäng, antal linjer, facit, bedömning
P = [
 ("E", "Vilken fråga går att undersöka?", ["A Är hundar snälla?", "B Hur högt hoppar en groda?", "C Är sommar bäst?", "D Är krasse fin?"], 1, 0, "B", "1 p för B."),
 ("E", "Du gör ett rättvist test. Vad gör du?", ["A Ändrar många saker samtidigt", "B Ändrar bara en sak och håller allt annat lika", "C Ändrar ingenting", "D Mäter bara en gång"], 1, 0, "B", "1 p för B."),
 ("E", "Dra streck mellan forskaren och det de upptäckte. Skriv bokstaven.<br>" + match(["1 Pasteur", "2 Semmelweis", "3 Marshall och Warren"], ["A Handtvätt minskade dödsfall", "B Magsår kommer av en bakterie", "C Små organismer kommer utifrån"]) + "Svar: 1 ___ &nbsp; 2 ___ &nbsp; 3 ___", None, 3, 0,
  "1 C, 2 A, 3 B", "1 p per rätt."),
 ("E", "En tabell visar hur höga plantor är. Vad ska stå efter varje siffra? Ge ett exempel.", None, 1, 1, "En enhet, t.ex. mm eller cm.", "1 p för enhet."),
 ("E", "Vilka två påståenden går att pröva med mätningar? Kryssa i två.<br>☐ Pizza är godast.<br>☐ Vatten kokar vid 100 °C.<br>☐ Rött är den finaste färgen.<br>☐ Kaniner springer fortare än sköldpaddor.", None, 2, 0,
  "Vatten kokar vid 100 °C. Kaniner springer fortare än sköldpaddor.", "1 p per rätt. Avdrag om fler än två kryssas."),
 ("E", "Ge två frågor du kan ställa till en källa för att se om den går att lita på.", None, 2, 3, "Två av: vem har skrivit, varför är det skrivet / vill de sälja något, finns det belägg, är det nytt, säger andra källor samma sak.", "1 p per fråga som går att använda för att granska en källa."),
 ("E", "Du vill testa om bönor gror bäst i varmt eller kallt. Vad ändrar du? Nämn något som ska vara lika.", None, 2, 3, "Ändrar: temperaturen. Lika: t.ex. sorts bönor, antal, vatten, jord, ljus.", "1 p ändrar temperaturen. 1 p minst en variabel som hålls lika."),
 ("C", "Mira vill ta reda på om temperaturen påverkar hur snabbt bönor gror. Hon sätter bönor i en burk i ett soligt fönster och bönor i en annan burk i kylskåpet." + fig(FIG+"p_bonor.png", None, "72%") + "a) Ge ett skäl till att undersökningen inte blir rättvis.<br>b) Föreslå en förbättring.", None, 2, 5,
  "a) Både temperatur och ljus skiljer sig (fönster ljust, kylskåp mörkt). b) Båda i samma ljus eller båda i mörker; samma vatten och antal bönor; flera bönor.", "a) 1 p. b) 1 p."),
 ("C", "a) Räkna ut medelvärdet av 12, 14 och 13 mm.<br>b) Förklara varför man gör flera försök och räknar medelvärde.", None, 2, 4, "a) 13 mm. b) En enskild mätning kan påverkas av slump eller misstag. Flera försök gör resultatet säkrare.", "a) 1 p. b) 1 p för att slumpen/misstag påverkar och att flera försök ger säkrare resultat."),
 ("C", "Förklara skillnaden mellan slump och systematiskt fel. Ge ett exempel på varje.", None, 2, 5, "Slump: tillfälliga variationer (t.ex. man läser av linjalen lite olika varje gång), jämnar ut sig vid upprepning. Systematiskt fel: samma fel varje gång (t.ex. en låda som alltid är varmare), upprepning hjälper inte, planering och kontroll hjälper.", "1 p slump med exempel. 1 p systematiskt fel med exempel."),
 ("C", "Semmelweis krävde att läkarna skulle tvätta händerna på 1840-talet.<br>a) Vilket belägg hade han för att det hjälpte?<br>b) Ge ett skäl till att många läkare ändå inte trodde honom.", None, 3, 5,
  "a) Dödligheten på läkarkliniken sjönk från 11,4 % till 1,3 %. b) Han kunde inte förklara hur det fungerade (man visste inte att bakterier kan orsaka sjukdomar); läkarna ville inte tro att de själva spred sjukdom; han publicerade sig sent.", "a) 1 p för att dödligheten sjönk (2 p om siffror eller jämförelse med barnmorskekliniken ges). b) 1 p."),
 ("C", "Läs annonsen." + ANNONS + fig(FIG+"p_plaster.png", None, "34%") + "a) Ge två skäl till att vara skeptisk. Använd källkritiska frågor.<br>b) Vad är skillnaden mellan en trovärdig och en relevant källa?", None, 3, 6,
  "a) Tendens: företaget säljer plåstret. Beroende: ingen källa till ”vetenskapligt utvecklat”. En persons berättelse är inget belägg. b) Trovärdig = går att lita på. Relevant = passar min fråga.", "a) 1 p per skäl med koppling till kriterium (max 2). b) 1 p för båda begreppen rätt."),
 ("A", "Ett företag påstår att deras sportdryck ger bättre kondition." + fig(FIG+"p_dryck.png", None, "60%") + "Planera en undersökning som kan pröva påståendet. Beskriv hur du använder kontrollgrupp, placebo, randomisering och blindning och förklara varför varje del behövs.", None, 4, 8,
  "Slumpa deltagare till två grupper (randomisering) så att grupperna blir lika från början. Grupp A får sportdrycken, grupp B en likadan dryck utan det verksamma ämnet (placebo) så att förväntningar inte påverkar. Varken deltagare eller testledare vet vem som fått vad (dubbelblind). Mät konditionen före och efter med samma test. Många deltagare minskar slumpens betydelse.", "1 p per del som beskrivs rätt (kontrollgrupp/placebo, randomisering, blindning, mätning/upprepning). Se bedömningsguiden för resonemang."),
 ("A", "<span class='fake'>Påhittade värden</span> En grupp undersökte hur temperaturen påverkar jäst.<br>" + fig(FIG+"p_jast.png", None, "78%") + TABELL + "Siffrorna är hur mycket en ballong växte (omkrets).<br>a) Ett värde avviker. Vilket? Ge en möjlig förklaring.<br>b) Hur skulle du hantera värdet och redovisa resultatet? Vilken slutsats kan du dra om 25 °C och 40 °C?", None, 4, 8,
  "a) 18 cm vid 40 °C. T.ex. ballongen satt löst, fel mängd jäst. b) Undersök först om det finns en rimlig förklaring. Redovisa värdet, förklara det och visa medelvärde med och utan det (26 cm resp. 30,5 cm). Redovisa spridning. Gör fler försök. Skillnaden mellan 10 och 25 °C är tydlig; mellan 25 och 40 °C är den osäker på grund av det avvikande värdet.", "1 p avvikande värde och förklaring. 1 p hanterar värdet motiverat. 1 p redovisar osäkerhet. 1 p slutsats med nyans."),
 ("A", "Två trovärdiga källor säger olika om ett kosttillskott: en myndighet avråder och en studie betald av tillverkaren visar effekt. Resonera om hur du väger källorna och vad du skulle vilja veta mer. Formulera ett argument och bemöt ett motargument.", None, 4, 8,
  "Väg: Vad bygger respektive källa på? Är studien oberoende granskad och upprepad? Hur många deltog, hur var den upplagd? Tendens hos tillverkaren (betald studie), men det gör den inte automatiskt fel. Vill veta mer: fler oberoende studier och sammanställningar. Argument: påstående, belägg, motargument, bemötande och slutsats med angiven säkerhet.", "1 p väger källorna med relevanta kriterier. 1 p anger vad mer som behövs. 1 p argument med belägg. 1 p bemöter motargument och anger säkerhet."),
]
NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
       ["13 Planera", "Föreslår en enkel undersökning med en grupp som får dryck.", "Använder kontrollgrupp och placebo och förklarar varför.", "Använder alla fyra delar, förklarar vilket fel var och en förhindrar och resonerar om antal deltagare."],
       ["14 Jäst", "Pekar ut det avvikande värdet.", "Förklarar möjlig orsak och räknar medelvärde.", "Hanterar värdet motiverat, redovisar osäkerhet och drar nyanserad slutsats."],
       ["15 Källor", "Säger att tillverkaren vill sälja.", "Använder kriterier (tendens, beroende) för båda källorna.", "Väger källorna, anger vad som saknas och bemöter ett motargument."]]

def build(lararversion):
    h = ['<section class="sec"><div style="display:flex;justify-content:space-between;align-items:baseline"><div class="pill">Kapitel 1 · Prov</div><div class="note">Namn: ____________________ &nbsp; Klass: ________ &nbsp; Poäng: ____ / 36</div></div>'
         '<div class="sh"><h2>Biologi som vetenskap</h2></div>'
         '<p class="note">Hjälpmedel: penna. Del E ska alla svara på. Del C och del A visar vad du kan på högre nivåer. Svara kort och tydligt. Personer, annonser och mätvärden i uppgifterna är påhittade. Siffran till höger visar hur många poäng uppgiften ger.</p>']
    last = None; n = 0
    for (niv, q, alts, pts, nl, fac, bed) in P:
        n += 1
        if niv != last:
            if last is not None: h.append('<div style="margin-top:10pt"></div>')
            h.append(f'<div class="pill">{NIVA[niv][0]} · {NIVA[niv][1].upper()}</div>')
            last = niv
        a = ""
        if alts:
            a = '<div class="alts">' + "".join(f"<div>{x}</div>" for x in alts) + '</div>'
        l = lines(nl) if nl and not lararversion else ""
        fa = f'<div style="background:#e9f3e9;border-radius:5pt;padding:4pt 8pt;margin-top:4pt;font:9pt/1.35 Carlito"><b>Facit:</b> {fac}<br><b>Poäng:</b> {bed}</div>' if lararversion else ""
        h.append(f'<div class="q" style="grid-template-columns:16pt minmax(0,1fr) 30pt"><span class="n">{n}</span><div>{q}{a}{l}{fa}</div><span class="pts">{pts} p</span></div>')
    h.append('</section>')
    if lararversion:
        e = sum(x[3] for x in P if x[0] == "E"); c = sum(x[3] for x in P if x[0] == "C"); a = sum(x[3] for x in P if x[0] == "A")
        h.append('<section class="sec teacher"><h2>Till läraren: bedömning</h2>'
                 f'<p>Provet har {e} p på del E, {c} p på del C och {a} p på del A (totalt {e+c+a} p). Del E går att klara med enbart lättläst-versionen av kapitlet, del C med grundtexten och del A med fördjupningen. Elever som är bra på att se mönster kan klara högre nivåer med lägre texter.</p>'
                 '<h3>Riktvärden</h3><ul class="pu"><li><b>E:</b> minst 8 av 12 p på del E, och uppgifterna visar att eleven kan planera enkelt, dokumentera, använda begrepp och granska en källa.</li>'
                 '<li><b>C:</b> E-nivån samt minst 7 av 12 p på del C.</li><li><b>A:</b> C-nivån samt minst 7 av 12 p på del A, med resonemang som är sammanhängande och nyanserade.</li></ul>'
                 '<p class="note">Poängen är en vägledning. Kunskapskraven är kvalitativa: ”enkla”, ”utvecklade” och ”välutvecklade” resonemang. Betyget sätts av en samlad bedömning av provet och elevens övriga underlag, till exempel labbrapporter och muntliga resonemang.</p>'
                 '<h3>Bedömningsguide för resonemangsuppgifterna</h3>' + table(BED[0], BED[1:]) +
                 '<h3>Kopplingar</h3><p>Uppgift 1, 2, 4, 7, 8, 9 och 10: systematiska undersökningar (planera, dokumentera, värdera). Uppgift 3 och 11: förklaringsmodellers framväxt. Uppgift 5: vad vetenskap kan pröva. Uppgift 6, 12, 15: informationssökning, källkritik och argumentation. Uppgift 13 och 14: planering och värdering på hög nivå.</p>'
                 '<p class="note">Fakta kontrollerad mot kallor-omrade1.md. Provet är inte kalibrerat mot nationella prov.</p></section>')
    return "".join(h)

def doc(body, foot):
    return f'<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(foot, 1)}.q .alts{{grid-template-columns:1fr 1fr}}{DYS}</style></head><body>{body}</body></html>'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        p = f'{OUT}/biologi-1-{name}.pdf'
        html_to_pdf(doc(build(lar), 'Kapitel 1 · Biologi som vetenskap · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))

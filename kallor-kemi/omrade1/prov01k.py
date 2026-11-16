# -*- coding: utf-8 -*-
"""Prov område 1 Kemi som vetenskap: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os, re
sys.path.insert(0, '/tmp/kem')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader, PdfWriter

FIG = '/tmp/kem/fig01k/'
ANNONS = ('<div class="fakeann"><span class="fake">Påhittad annons</span></div><div style="border:1pt solid #d9d2c8;border-radius:5pt;padding:5pt 8pt;margin:4pt 0"><b>NYHET! RenaMax™ Kemikaliefri rengöring</b><br>100 % naturlig och därför helt ofarlig för dig och miljön! Testad: 9 av 10 nöjda kunder. Tar bort alla fläckar.</div>')
TABELL = table(["Temperatur", "Försök 1 (s)", "Försök 2 (s)", "Försök 3 (s)"], [["5 °C", "150", "160", "148"], ["20 °C", "70", "118", "72"], ["40 °C", "29", "33", "31"]], "tbl num")

def match(left, right):
    return ('<table class="tbl num" style="width:92%"><tr><th>Forskare</th><th>Upptäckt</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')

# nivå, fråga, alternativ, poäng, antal linjer, facit, bedömning
P = [
 ("E", "Vilken fråga går att undersöka med mätningar?", ["A Är kemi roligt?", "B Hur påverkar temperaturen hur fort socker löser sig i vatten?", "C Är lila den finaste färgen?", "D Är sockerkakor goda?"], 1, 0, "B", "1 p för B."),
 ("E", "Vad ska du alltid ha på dig när du arbetar med kemikalier i labbet?", ["A Solglasögon", "B Skyddsglasögon", "C Hörlurar", "D Mössa"], 1, 0, "B", "1 p för B."),
 ("E", "Vilka två regler gäller i ett kemilabb? Kryssa i två.<br>☐ Smaka på ämnet om det luktar gott.<br>☐ Sätta upp långt hår.<br>☐ Ha skyddsglasögon på.<br>☐ Äta lunch vid labbänken.", None, 2, 0, "Sätta upp långt hår. Ha skyddsglasögon på.", "1 p per rätt. Avdrag om fler än två kryssas."),
 ("E", "Bilden visar vatten i en mätcylinder. Läs av nivån vid den lägsta delen av vattenytan. Skriv värdet och enheten." + fig(FIG+"p_cylinder.png", None, "26%") + "Svar: ____________", None, 2, 0, "62 ml.", "1 p för värdet 62. 1 p för enheten ml."),
 ("E", "Dra streck mellan forskaren och det hen gjorde. Skriv bokstaven.<br>" + match(["1 Boyle", "2 Lavoisier", "3 Dalton"], ["A Allt är uppbyggt av atomer", "B Massan är lika före och efter en reaktion", "C Krävde att påståenden prövas med försök"]) + "Svar: 1 ___ &nbsp; 2 ___ &nbsp; 3 ___", None, 3, 0, "1 C, 2 B, 3 A", "1 p per rätt."),
 ("E", "Du vill testa om en sockerbit löser sig fortare i varmt vatten än i kallt. Vad ändrar du? Nämn något som ska vara lika.", None, 2, 3, "Ändrar: vattnets temperatur. Lika: t.ex. vattenmängd, sorts och storlek på sockerbiten, omrörning.", "1 p ändrar temperaturen. 1 p minst en variabel som hålls lika."),
 ("E", "Ge två frågor du kan ställa för att se om ett påstående i en reklam går att lita på.", None, 2, 3, "Två av: vem säger det, vill de sälja något, vilka belägg finns, hur gammal är informationen, säger andra källor samma sak.", "1 p per fråga som går att använda för att granska ett påstående."),
 ("C", "Mia vill veta om en fläckborttagare fungerar bättre än vatten. Hon lägger ett tyg med stor fläck i fläckborttagaren i tio minuter och ett tyg med liten fläck i vatten i två minuter.<br>a) Ge ett skäl till att testet inte är rättvist.<br>b) Föreslå en förbättring och förklara varför den gör testet rättvisare.", None, 3, 6,
  "a) Fläckens storlek och tiden skiljer sig, så man vet inte om skillnaden beror på vätskan. b) Likadana fläckar och lika lång tid i båda vätskorna, så att bara vätskan skiljer sig.", "a) 1 p. b) Allmänt förslag (”gör det rättvist”) 0 p. Specifikt förslag (”lika stor fläck och lika lång tid”) 1 p. Specifikt förslag med förklaring (”så att bara vätskan skiljer sig”) 2 p."),
 ("C", "Diagrammet visar hur lång tid en brustablett tog att lösa sig vid olika vattentemperatur." + fig(FIG+"p_diagram.png", None, "80%") + "a) Hur lång tid tog det vid 30 °C?<br>b) Beskriv sambandet mellan temperatur och tid.<br>c) Uppskatta tiden vid 35 °C och förklara hur du kom fram till det.", None, 3, 5,
  "a) Cirka 52 s. b) Ju varmare vatten, desto kortare tid. c) Cirka 40–45 s, eftersom värdet ligger mellan det vid 30 °C (52 s) och 40 °C (33 s).", "a) 1 p (50–55 s godtas). b) 1 p. c) 1 p för värde mellan 33 och 52 s med motivering."),
 ("C", "a) Tre försök gav 148 s, 160 s och 148 s. Räkna ut medelvärdet.<br>b) Förklara varför man gör flera försök och räknar medelvärde.", None, 2, 4, "a) (148 + 160 + 148) / 3 = 152 s. b) En enskild mätning kan påverkas av slump eller misstag. Flera försök och medelvärde gör resultatet säkrare.", "a) 1 p. b) 1 p för att en mätning kan påverkas av slump eller misstag och att flera gör resultatet säkrare."),
 ("C", "a) Vad är en modell i kemi?<br>b) Ge ett exempel på något partikelmodellen kan förklara och ett exempel på något den inte säger något om.", None, 3, 6,
  "a) En förenkling som förklarar och förutsäger, och som inte är samma sak som verkligheten. b) Kan förklara: att en gas fyller rummet, eller varför tabletten löser sig fortare i varmt vatten. Säger inget om: ämnets färg eller lukt.", "a) 1 p. b) 1 p för exempel på vad modellen förklarar. 1 p för exempel på begränsning."),
 ("C", "Läran om de fyra elementen levde i över 2 000 år.<br>a) Vad gjorde att forskare till slut började tvivla på den?<br>b) Förklara hur Lavoisiers vägningar passade med Daltons atomteori.", None, 3, 6,
  "a) Boyle och andra krävde att påståenden skulle prövas med försök, och Lavoisier visade med vägningar att massan bevaras, vilket den gamla läran inte förklarade bra. b) Om atomer inte skapas eller försvinner i en reaktion kan massan inte ändras, vilket stämmer med att massan är lika före och efter.", "a) 1 p. b) 1 p för att atomer inte försvinner. 1 p för kopplingen till bevarad massa."),
 ("A", "Klassen vill veta om ett tvättmedel verkligen tar bort fläckar bättre än bara vatten. Planera en undersökning. Beskriv vad du ändrar, mäter och håller lika, vilken jämförelse du har med, hur du gör bedömningen opartisk och hur du upprepar. Förklara varför varje del behövs.", None, 4, 8,
  "Ändrar: vätskan (tvättmedel eller bara vatten). Mäter: hur ljus fläcken blir, t.ex. på en poängskala. Håller lika: tygsort, fläck, mängd vätska, tid och sätt att skölja. Jämförelse: bara vatten, så att man ser effekten av tvättmedlet. Opartiskhet: en kamrat som inte vet vilken som är vilken sätter poäng (blindning). Upprepa flera gånger så slumpen får mindre betydelse.", "1 p ändrar/mäter/lika rätt. 1 p jämförelse med förklaring. 1 p opartisk bedömning med förklaring. 1 p upprepning med förklaring."),
 ("A", "<span class='fake'>Påhittade värden</span> En klass undersökte hur vattnets temperatur påverkar hur lång tid en brustablett tar att lösa sig." + TABELL + "a) Ett värde avviker. Vilket? Ge en möjlig förklaring.<br>b) Räkna ut medelvärdet för 20 °C med och utan det avvikande värdet. Hur skulle du hantera värdet och redovisa resultatet?<br>c) Vilken slutsats kan du dra? Hur säker är du?", None, 4, 8,
  "a) 118 s vid 20 °C. T.ex. klockan stoppades sent eller tabletten fastnade. b) Med: (70 + 118 + 72) / 3 = 87 s. Utan: (70 + 72) / 2 = 71 s. Undersök först om det finns en känd orsak, gör om mätningen om det går, redovisa båda medelvärdena öppet och motivera valet. c) Tiden minskar när temperaturen ökar (153 s, ca 71–87 s, 31 s). Vid 5 och 40 °C är spridningen liten och slutsatsen säker. Vid 20 °C är osäkerheten större på grund av det avvikande värdet.", "1 p avvikande värde och möjlig orsak. 1 p medelvärden rätt och motiverad hantering. 1 p redovisar öppet. 1 p slutsats med nyans om säkerheten."),
 ("A", "Läs annonsen." + ANNONS + "Resonera om vad som är problematiskt i annonsen och vad du skulle vilja veta mer. Formulera ett argument mot att lita på annonsen och bemöt ett möjligt motargument.", None, 4, 8,
  "Problem: ”kemikaliefri” stämmer inte bokstavligt (allt är kemikalier) och säger inget om faran; ”naturlig” betyder inte ofarlig; ”9 av 10 nöjda” saknar jämförelse, antal och vad de var nöjda med; avsändaren vill sälja. Vill veta: vilka ämnen, vilken märkning, oberoende test, jämförelse med annan produkt eller vatten. Argument + motargument (t.ex. ”men många är nöjda”) med bemötande (nöjd är inte samma sak som att den fungerar bättre, och utan jämförelse vet man inte) och slutsats med angiven säkerhet.", "1 p problem med flera orsaker (kemikaliefri, naturlig, 9 av 10). 1 p vad som behövs för att bedöma. 1 p argument med belägg. 1 p bemöter motargument och anger säkerhet."),
]
NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
       ["13 Planera", "Föreslår en enkel jämförelse mellan tvättmedel och vatten.", "Anger vad som ändras, mäts och hålls lika och använder jämförelse.", "Förklarar varför varje del behövs, inklusive opartisk bedömning och upprepning."],
       ["14 Avvikande värde", "Pekar ut det avvikande värdet.", "Förklarar möjlig orsak och räknar medelvärde.", "Hanterar värdet motiverat, redovisar öppet och drar nyanserad slutsats."],
       ["15 Granska", "Säger att tillverkaren vill sälja.", "Granskar flera ord och siffror i annonsen med kriterier.", "Väger problemen, anger vad som saknas och bemöter ett motargument."]]
# Förmåga per uppgift (1 = begrepp/modeller, 2 = systematiska undersökningar, 3 = granska/kommunicera/ta ställning)
FORM = ["F2", "F2", "F2", "F2", "F1", "F2", "F3", "F2", "F2", "F2", "F1", "F1", "F2", "F2", "F3"]
FN = {"F1": "Begrepp, modeller och samband", "F2": "Systematiska undersökningar", "F3": "Granska information, kommunicera och ta ställning"}
FORMKOM = {"F1": "Modeller och förklaringsmodellers framväxt (uppgift 5, 11 och 12).",
           "F2": "Planera, dokumentera och värdera på papper. Själva genomförandet bedöms i labb 1.1 och 1.2 och i bonuslabben.",
           "F3": "Källkritik och argumentation (uppgift 7 och 15)."}
IMPROV = ('<h3>Förbättra en undersökning (uppgift 8)</h3><p>Trappan allmänt förslag, specifikt förslag och specifikt förslag med förklaring motsvarar E-, C- och A-nivå i bedömningen av förbättringar. Därför är ett allmänt förslag (”gör det rättvist”) rött, ett specifikt förslag gult och ett specifikt förslag med förklaring grönt.</p>')
KOPPL = "Uppgift 1, 2, 3, 4, 6, 8, 9, 10, 13 och 14: systematiska undersökningar (säkerhet, mätning, planera, dokumentera, värdera). Uppgift 5, 11 och 12: modeller och kemins framväxt. Uppgift 7 och 15: källkritik och argumentation."
KAP = "Kapitel 1"; NAMN_ = "Kemi som vetenskap"

def teacher_section():
    from collections import Counter
    cn = Counter(x[0] for x in P)
    rows = ""
    for f in ("F1", "F2", "F3"):
        idx = [i for i, t in enumerate(FORM) if f in t]
        rows += f'<tr><td>{f[1]}. {FN[f]}</td><td>{", ".join(str(i+1) for i in idx) or "–"}</td><td>{FORMKOM[f]}</td></tr>'
    ftab = '<table class="tbl"><tr><th>Förmåga</th><th>Uppgifter</th><th>Kommentar</th></tr>' + rows + '</table>'
    return ('<section class="sec teacher"><h2>Till läraren: bedömning</h2>'
        f'<p>Provet har {len(P)} uppgifter: {cn.get("E", 0)} på del E, {cn.get("C", 0)} på del C och {cn.get("A", 0)} på del A. Del E motsvarar lättläst-versionen, del C grundtexten och del A fördjupningen. Uppgiftstyperna varierar (flerval, flersvar, matchning, kortsvar och resonemang), och varje uppgift är kopplad till en förmåga i facit.</p>'
        '<h3>Så använder du trafikljuset</h3><p>Provet har ingen poängräkning. Vid varje uppgift finns tre prickar: <b style="color:#c0392b">röd</b> (kan inte ännu), <b style="color:#b8860b">gul</b> (kan delvis) och <b style="color:#2e8b57">grön</b> (kan nästan helt). Ringa in den nivå som svaret ligger på. Eleven kan göra en egen markering med en färg och du en annan, och ni kan jämföra.</p>'
        '<table class="tbl"><tr><th>Färg</th><th>Så bedömer du uppgiften</th></tr>'
        '<tr><td>Röd</td><td>Svaret saknar det som efterfrågas eller bygger på missförstånd.</td></tr>'
        '<tr><td>Gul</td><td>Svaret har någon del av det facit anger, eller rätt idé men med luckor. Vid uppgifter med flera delar (a, b, c) klarar eleven en del men inte alla.</td></tr>'
        '<tr><td>Grön</td><td>Svaret innehåller det som facit anger, eller likvärdiga formuleringar, och hänger ihop.</td></tr></table>'
        '<h3>Förmågor som provet prövar</h3>' + ftab +
        '<p class="note">Ett skriftligt prov kan inte pröva allt. Planering, genomförande och dokumentation bedöms också i labbarna, och diskussion och argumentation i undervisningen.</p>'
        '<h3>Bedömning av resonemang</h3><p>Resonemang bedöms efter hur många led eleven för och hur väl de hänger ihop, inte efter hur mycket eleven skriver: orsak, följd och konsekvens, samt slutsats och rätt användning av begrepp. Ett längre svar som upprepar samma led är inte bättre. Facit visar förväntade led, och andra rimliga led godtas.</p>'
        + IMPROV +
        '<h3>Från trafikljus till betyg</h3>'
        '<p>Det finns inga prövade gränser för provet. Som utgångspunkt för en samlad bedömning: del E visar grundläggande kunskaper, del C utvecklade och del A välutvecklade. Många gröna och gula på del E tyder på E-nivå, gröna på del C på C-nivå och gröna på del A på A-nivå. Kunskapskraven är kvalitativa (”enkla”, ”utvecklade” och ”välutvecklade” resonemang), så betyget sätts av en samlad bedömning av provet och elevens övriga underlag.</p>'
        '<h3>Bedömningsguide för resonemangsuppgifterna</h3>' + table(BED[0], BED[1:]) +
        '<h3>Kopplingar</h3><p>' + KOPPL + '</p>'
        '<p class="note">Fakta är kontrollerad mot källfilen för området. Upplägget är inspirerat av nationella prov, men provet är inte prövat på elever och bedömningen är ett förslag. Personer, annonser och mätvärden i uppgifterna är påhittade.</p></section>')

TLS = '<span class="tl"><i style="background:#d64541"></i><i style="background:#f2c230"></i><i style="background:#3aa860"></i></span>'

def split_parts(q):
    """Delar upp en uppgift i delfrågor a), b), c) ... Returnerar (inledning, [(bokstav, text)]) eller None."""
    ms = [m for m in re.finditer(r'(?<![\w(])([a-e])\) ', q)]
    seq = []
    want = 'a'
    for m in ms:
        if m.group(1) == want:
            seq.append(m); want = chr(ord(want) + 1)
    if len(seq) < 2:
        return None
    pre = q[:seq[0].start()]
    items = []
    for i, m in enumerate(seq):
        end = seq[i + 1].start() if i + 1 < len(seq) else len(q)
        txt = q[m.end():end]
        txt = re.sub(r'(<br>|\s)+$', '', txt)
        items.append((m.group(1), txt))
    pre = re.sub(r'(<br>|\s)+$', '', pre)
    return pre, items

def build(lararversion):
    h = ['<section class="sec"><div style="display:flex;justify-content:space-between;align-items:baseline"><div class="pill">' + KAP + ' · Prov</div><div class="note">Namn: ____________________ &nbsp; Klass: ________ </div></div>'
         '<div class="sh"><h2>' + NAMN_ + '</h2></div>'
         '<p class="note">Hjälpmedel: penna. Del E ska alla svara på. Del C och del A visar vad du kan på högre nivåer. Svara kort och tydligt. Personer, annonser och mätvärden i uppgifterna är påhittade. Till höger om varje uppgift finns tre prickar: röd (kan inte ännu), gul (kan delvis) och grön (kan nästan helt). Ringa in den nivå som svaret ligger på.</p>']
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
        sp = split_parts(q)
        if sp:
            pre, items = sp
            each = max(2, round(nl / len(items))) if nl else 0
            sub = "".join(f'<div class="sp"><div><b>{lab})</b> {txt}{lines(each) if (each and not lararversion) else ""}</div>{TLS}</div>' for lab, txt in items)
            q = pre; a2 = a; a = ""; l = ""
            sub = a2 + sub
        else:
            sub = ""
        fa = f'<div style="background:#f7e6e4;border-radius:5pt;padding:4pt 8pt;margin-top:4pt;font:9pt/1.35 Carlito"><b>Förmåga:</b> {FORM[n-1]} &nbsp; <b>Facit:</b> {fac}</div>' if lararversion else ""
        h.append(f'<div class="q" style="grid-template-columns:16pt minmax(0,1fr) 44pt"><span class="n">{n}</span><div>{q}{a}{sub}{l}{fa}</div>' + ('<span></span>' if sub else TLS) + '</div>')
    h.append('</section>')
    if lararversion: h.append(teacher_section())
    return "".join(h)

def doc(body, foot):
    return f'<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(foot, 1)}.q .alts{{grid-template-columns:1fr 1fr}}{DYS}.sp{{display:grid;grid-template-columns:minmax(0,1fr) 44pt;gap:7pt;margin:5pt 0 3pt;align-items:start}}.tl{{display:flex;gap:4pt;justify-content:flex-end;padding-top:1pt}}.tl i{{display:block;width:11pt;height:11pt;border-radius:50%;border:.6pt solid #555}}</style></head><body>{body}</body></html>'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        p = f'{OUT}/kemi-1-{name}.pdf'
        html_to_pdf(doc(build(lar), 'Kapitel 1 · Kemi som vetenskap · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))

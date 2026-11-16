# -*- coding: utf-8 -*-
"""Prov område 1 Kemi som vetenskap: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os
sys.path.insert(0, '/tmp/kem')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader, PdfWriter

FIG = '/tmp/kem/fig03k/'
TABELL = table(["Atom", "Protoner", "Neutroner", "Elektroner"], [["D", "8", "8", "8"], ["E", "8", "9", "8"], ["F", "9", "10", "9"]], "tbl num")

def match(left, right, h1="Grupp", h2="Beskrivning"):
    return ('<table class="tbl num" style="width:92%"><tr><th>' + h1 + '</th><th>' + h2 + '</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')

# nivå, fråga, alternativ, poäng, antal linjer, facit, bedömning
P = [
 ("E", "Vilken partikel har laddningen +1?", ["A Neutronen", "B Protonen", "C Elektronen", "D Atomkärnan"], 1, 0, "B", "1 p för B."),
 ("E", "En atom har atomnummer 11 och masstal 23. Hur många neutroner har den?", ["A 11", "B 12", "C 23", "D 34"], 1, 0, "B", "1 p för B (23 − 11 = 12)."),
 ("E", "Vilka två påståenden stämmer? Kryssa i två.<br>☐ En atom är neutral eftersom den har lika många protoner som elektroner.<br>☐ Neutronen har negativ laddning.<br>☐ Alla metaller är fasta vid rumstemperatur.<br>☐ Ädelgaser har fullt yttersta skal.", None, 2, 0, "En atom är neutral eftersom den har lika många protoner som elektroner. Ädelgaser har fullt yttersta skal.", "1 p per rätt påstående. Avdrag 1 p om fler än två kryssas (lägst 0 p). Neutronen har laddning 0 och kvicksilver är flytande."),
 ("E", "Bilden visar en atom (schematisk)." + fig(FIG+"p_atom.png", None, "40%") + "a) Vilket atomnummer har atomen?<br>b) Vilket masstal har atomen?<br>Svar a: ____________ &nbsp; Svar b: ____________", None, 2, 0, "a) 7 (antalet protoner). b) 14 (7 protoner + 7 neutroner).", "a) 1 p. b) 1 p."),
 ("E", "Dra streck mellan gruppen och beskrivningen. Skriv bokstaven.<br>" + match(["1 Alkalimetaller", "2 Halogener", "3 Ädelgaser"], ["A Mycket oreaktiva gaser med fullt yttersta skal", "B Mjuka metaller som reagerar kraftigt med vatten", "C Reaktiva icke-metaller, till exempel klor"]) + "Svar: 1 ___ &nbsp; 2 ___ &nbsp; 3 ___", None, 3, 0, "1 B, 2 C, 3 A", "1 p per rätt."),
 ("E", "Vad är isotoper? Ge ett exempel.", None, 2, 3, "Atomer av samma grundämne (samma antal protoner) med olika antal neutroner. Exempel: kol-12 och kol-14.", "1 p för definitionen. 1 p för ett rätt exempel."),
 ("E", "Beskriv vad som hände i Rutherfords försök med guldfolie och vilken slutsats han drog.", None, 2, 3, "De flesta alfapartiklarna gick rakt igenom folien och några få avlänkades. Slutsatsen var att atomen har en liten, tung kärna med positiv laddning.", "1 p för iakttagelsen. 1 p för slutsatsen om en liten, tung kärna."),
 ("C", "Tre neutrala atomer har undersökts. Värdena är påhittade." + TABELL + "a) Räkna ut masstalet för varje atom.<br>b) Vilka två atomer är isotoper av samma grundämne? Motivera.", None, 3, 6,
  "a) D: 8 + 8 = 16. E: 8 + 9 = 17. F: 9 + 10 = 19. b) D och E, eftersom de har samma antal protoner (8) men olika antal neutroner.", "a) 1 p för alla tre (följdfel godtas). b) 1 p för D och E. 1 p för motivering med samma protoner och olika neutroner."),
 ("C", "Diagrammet visar hur mängden av ett påhittat radioaktivt ämne minskar." + fig(FIG+"p_kurva.png", None, "70%") + "a) Läs av halveringstiden.<br>b) Hur mycket finns kvar efter 15 år?<br>c) Varför blir mängden aldrig exakt noll genom att halveras?", None, 3, 5,
  "a) 5 år (80 g blir 40 g). b) 10 g (15 år är tre halveringstider: 80 → 40 → 20 → 10). c) Efter varje halveringstid finns hälften kvar av det som fanns, så det finns alltid något kvar.", "a) 1 p (5 år). b) 1 p (10 g, avläsning 9–11 godtas). c) 1 p för att det alltid är hälften kvar."),
 ("C", "Bilden visar en del av det periodiska systemet. Tre ämnen är markerade." + fig(FIG+"p_pse.png", None, "58%") + "a) Vilka två av de markerade ämnena liknar varandra mest? Förklara med valenselektroner.<br>b) Vilket markerat ämne har fullt yttersta skal?", None, 3, 5,
  "a) Na och K: de står i samma grupp (grupp 1) och har samma antal valenselektroner, 1, och reagerar därför liknande. b) Ne (neon).", "a) 1 p för Na och K. 1 p för att de har lika många valenselektroner. b) 1 p för neon."),
 ("C", "a) Nämn tre egenskaper som är typiska för metaller.<br>b) Nämn en egenskap som är typisk för icke-metaller.", None, 3, 6,
  "a) T.ex. leder värme och el, glänser, går att böja eller hamra utan att gå sönder. b) T.ex. leder värme och el dåligt, fasta är spröda, många är gaser.", "a) 2 p för tre rätt (1 p för två rätt). b) 1 p."),
 ("C", "a) Thomsons modell säger att positiv laddning är utspridd i atomen. Förklara varför Rutherfords försök inte stämde med den modellen.<br>b) Nämn en begränsning hos Bohrs modell.", None, 3, 6,
  "a) Enligt Thomsons modell borde alfapartiklarna gå rakt igenom eller böjas av lite. I försöket avlänkades några få kraftigt, vilket visar att den positiva laddningen sitter samlad i en liten kärna. b) Bohrs modell fungerar bra för väte men inte för atomer med flera elektroner, och ersattes av kvantmekaniken.", "a) 1 p för vad modellen förutsäger. 1 p för att några avlänkades kraftigt och att det visar en liten kärna. b) 1 p."),
 ("A", "Ett sjukhus använder strålning mot cancer. En tidning skriver: ”Strålning är alltid farligt.”<br>a) Nämn en användning och en risk med radioaktiv strålning.<br>b) Förklara tre sätt att skydda sig mot strålning.<br>c) Värdera tidningens påstående.", None, 4, 8,
  "a) T.ex. användning: strålbehandling, bilddiagnostik eller åldersbestämning med kol-14. Risk: joniserande strålning kan skada celler. b) Korta tiden, öka avståndet och skärma av (papper, aluminium, bly beroende på strålning). c) Påståendet är för kategoriskt. Strålning är nyttig i sjukvården men skadar celler vid hög dos. Vad som avgör är sorten, dosen, tiden och skyddet.", "1 p för användning och risk. 1 p för tre skydd (två rätt ger 0 p). 2 p för värderingen: 1 p för att väga nytta mot risk och 1 p för vad det beror på."),
 ("A", "Rubidium (Rb) står i grupp 1, under kalium. Det finns inte med i kapitlets text.<br>a) Förutsäg hur många valenselektroner det har, om det är en metall eller icke-metall och hur reaktivt det är jämfört med kalium. Motivera med platsen i det periodiska systemet.<br>b) Värdera hur säker din förutsägelse är och hur du skulle kunna kontrollera den.", None, 4, 8,
  "a) 1 valenselektron (grupp 1), en mjuk metall (alkalimetall), och reaktivare än kalium eftersom reaktiviteten ökar nedåt i gruppen. b) Förutsägelsen bygger på trender i gruppen och är rimlig men inte säker, eftersom trender kan ha undantag. Kontrolleras med försök i lärardemo eller jämförelse med data för litium, natrium och kalium.", "1 p för 1 valenselektron/metall. 1 p för reaktivare med motivering (trend nedåt i gruppen). 1 p för att förutsägelsen bygger på trender och inte är säker. 1 p för hur den kan kontrolleras."),
 ("A", "Skolan använder skalmodellen (2, 8, 8) fast Bohrs modell har begränsningar.<br>a) Klor har elektronerna 2, 8, 7 och fluor 2, 7. Förklara med modellen varför ämnena liknar varandra.<br>b) Förklara varför man ändå använder modellen, och beskriv var dess gräns går.", None, 4, 8,
  "a) Båda har 7 elektroner i yttersta skalet (valenselektroner) och står i samma grupp (17). Valenselektronerna avgör hur ämnet reagerar. b) Modellen är enkel och förklarar mycket, till exempel gruppernas släktskap, så den är användbar för de första ämnena. Bohrs modell fungerar bra för väte men inte för atomer med flera elektroner, och skalen med 2, 8, 8 är en förenkling som inte stämmer längre ned i systemet.", "a) 1 p för 7 valenselektroner i båda. 1 p för att de avgör hur ämnet reagerar/samma grupp. b) 1 p för att modellen är användbar trots begränsning. 1 p för att den inte fungerar för atomer med flera elektroner."),
]
NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
       ["13 Strålning", "Nämner en användning eller risk.", "Nämner användning och risk och minst två skydd.", "Värderar påståendet genom att väga nytta mot risk och förklara vad det beror på."],
       ["14 Förutsäga", "Anger valenselektroner eller att det är en metall.", "Förutsäger egenskaper och motiverar med platsen i gruppen.", "Motiverar med trender, värderar hur säker förutsägelsen är och hur den kan kontrolleras."],
       ["15 Modellens gräns", "Säger att klor och fluor står i samma grupp.", "Förklarar likheten med 7 valenselektroner.", "Kopplar valenselektroner till reaktivitet och värderar modellens användbarhet och gräns."]]
# Förmåga per uppgift (1 = begrepp/modeller, 2 = systematiska undersökningar, 3 = resonera, värdera och ta ställning)
FORM = ["F1", "F1", "F1", "F1", "F1", "F1", "F1", "F1", "F2", "F1", "F1", "F1", "F3", "F3", "F3"]
FN = {"F1": "Begrepp, modeller och samband", "F2": "Systematiska undersökningar", "F3": "Värdera, kommunicera och ta ställning"}
FORMKOM = {"F1": "Atomens byggnad, modeller, isotoper, periodiska systemet och grupper (uppgift 1–8 och 10–12).",
           "F2": "Tolka ett sönderfallsdiagram (uppgift 9). Själva genomförandet bedöms i labb 3.1 och 3.2 och i bonuslabben.",
           "F3": "Värdera strålning, förutsäga och värdera förutsägelser och värdera modellers användbarhet och gränser (uppgift 13–15)."}
IMPROV = ''
KOPPL = "Uppgift 1–8 och 10–12: begrepp, modeller och samband. Uppgift 9: tolka diagram (systematiska undersökningar). Uppgift 13–15: värdera, förutsäga och ta ställning."
KAP = "Kapitel 3"; NAMN_ = "Atomer och grundämnen"

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
        fa = f'<div style="background:#f7e6e4;border-radius:5pt;padding:4pt 8pt;margin-top:4pt;font:9pt/1.35 Carlito"><b>Förmåga:</b> {FORM[n-1]} &nbsp; <b>Facit:</b> {fac}</div>' if lararversion else ""
        h.append(f'<div class="q" style="grid-template-columns:16pt minmax(0,1fr) 44pt"><span class="n">{n}</span><div>{q}{a}{l}{fa}</div><span class="tl"><i style="background:#d64541"></i><i style="background:#f2c230"></i><i style="background:#3aa860"></i></span></div>')
    h.append('</section>')
    if lararversion: h.append(teacher_section())
    return "".join(h)

def doc(body, foot):
    return f'<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(foot, 1)}.q .alts{{grid-template-columns:1fr 1fr}}{DYS}.tl{{display:flex;gap:4pt;justify-content:flex-end;padding-top:1pt}}.tl i{{display:block;width:11pt;height:11pt;border-radius:50%;border:.6pt solid #555}}</style></head><body>{body}</body></html>'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        p = f'{OUT}/kemi-3-{name}.pdf'
        html_to_pdf(doc(build(lar), 'Kapitel 3 · Atomer och grundämnen · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))

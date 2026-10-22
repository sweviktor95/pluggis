# -*- coding: utf-8 -*-
"""Prov område 1 Kemiska föreningar och reaktioner: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os
sys.path.insert(0, '/tmp/kem')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader, PdfWriter

FIG = '/tmp/kem/fig04k/'
TABELL = table(["Ämne", "Smältpunkt", "Leder fast ämne ström?", "Leder löst i vatten ström?"], [["X", "790 °C", "Nej", "Ja"], ["Y", "−90 °C", "Nej", "Nej"], ["Z", "1085 °C", "Ja", "Löser sig inte"]], "tbl num")

def match(left, right, h1="Begrepp", h2="Beskrivning"):
    return ('<table class="tbl num" style="width:92%"><tr><th>' + h1 + '</th><th>' + h2 + '</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')

# nivå, fråga, alternativ, poäng, antal linjer, facit, bedömning
P = [
 ("E", "Vilken sorts bindning finns i en molekyl av vatten, H₂O?", ["A Jonbindning", "B Kovalent bindning", "C Metallbindning", "D Ingen bindning"], 1, 0, "B", "1 p för B."),
 ("E", "Vad kallas en negativ jon?", ["A Katjon", "B Anjon", "C Molekyl", "D Neutron"], 1, 0, "B", "1 p för B."),
 ("E", "Vilka två påståenden stämmer? Kryssa i två.<br>☐ Fast salt leder elektrisk ström.<br>☐ Saltlösning leder elektrisk ström.<br>☐ Bordssalt smälter vid mycket högre temperatur än vatten fryser.<br>☐ Sockerlösning leder ström bra.", None, 2, 0, "Saltlösning leder elektrisk ström. Bordssalt smälter vid mycket högre temperatur än vatten fryser.", "1 p för varje rätt kryss. Dra 1 p för varje fel kryss (lägst 0 p)."),
 ("E", "Bilden visar två ämnen (schematiskt)." + fig(FIG+"p_modeller.png", None, "62%") + "a) Vilket ämne är en jonförening, A eller B?<br>b) Vilket ämne består av molekyler?<br>Svar a: ____________ &nbsp; Svar b: ____________", None, 2, 0, "a) A (positiva och negativa joner i ett gitter). b) B (vattenmolekyler).", "a) 1 p. b) 1 p."),
 ("E", "Dra streck mellan begreppet och beskrivningen. Skriv bokstaven.<br>" + match(["1 Utgångsämne", "2 Produkt", "3 Exoterm"], ["A Ämne som bildas i reaktionen", "B Ämne som reagerar", "C Reaktion som avger energi"]) + "Svar: 1 ___ &nbsp; 2 ___ &nbsp; 3 ___", None, 2, 0, "1 B, 2 A, 3 C.", "2 p för tre rätt, 1 p för två rätt."),
 ("E", "Nämn tre tecken på att en kemisk reaktion har skett.", None, 3, 3, "T.ex. gas bildas (bubblor), temperaturen ändras, färgen ändras, ett fast ämne bildas, ljus eller lukt.", "1 p för varje rätt tecken."),
 ("E", "a) Hur många atomer av varje sort finns i en molekyl H₂O?<br>b) Vad betyder molekylformeln CO₂?", None, 2, 3, "a) 2 väteatomer och 1 syreatom. b) En kolatom och två syreatomer (koldioxid).", "a) 1 p. b) 1 p."),
 ("C", "Tre påhittade ämnen har undersökts. Värdena är påhittade men liknar riktiga ämnen." + TABELL + "a) Vilket ämne är troligen en jonförening, vilket en molekylförening och vilket en metall? Motivera.<br>b) Förklara varför X leder ström löst i vatten men inte som fast ämne.", None, 3, 6,
  "a) X är troligen en jonförening (hög smältpunkt, leder löst men inte fast). Y är troligen en molekylförening (låg smältpunkt, leder inte). Z är troligen en metall (leder som fast ämne). b) I fast ämne sitter jonerna fast i gittret. Löst i vatten kan jonerna röra sig fritt och bära strömmen.", "a) 1 p för alla tre rätt. 1 p för motivering. b) 1 p."),
 ("C", "a) Balansera: H₂ + Cl₂ → HCl<br>b) Balansera: Na + Cl₂ → NaCl<br>c) Förklara varför man sätter tal framför formlerna men aldrig ändrar talen inne i formlerna.", None, 3, 5,
  "a) H₂ + Cl₂ → 2 HCl. b) 2 Na + Cl₂ → 2 NaCl. c) Talet framför visar hur många molekyler som reagerar. Ändrar man talet inne i formeln byter man ut ämnet (till exempel är H₂O₂ inte vatten).", "a) 1 p. b) 1 p. c) 1 p."),
 ("C", "En elev vägde en flaska med ättika och en bikarbonat före och efter reaktionen." + fig(FIG+"p_vag.png", None, "62%") + "a) Förklara varför massan minskade i den öppna flaskan.<br>b) Hur mycket massa försvann i den öppna flaskan?<br>c) Varför ändrades inte massan i den slutna flaskan?", None, 3, 6,
  "a) Det bildas koldioxid, en gas, som lämnar den öppna flaskan och tar sin massa med sig. b) 150,0 − 148,6 = 1,4 g. c) Gasen stannar kvar, så ingen massa lämnar systemet (massans bevarande).", "a) 1 p. b) 1 p. c) 1 p."),
 ("C", "Diagrammet visar bildad gas mot tid för samma reaktion vid två temperaturer, A och B (påhittat försök)." + fig(FIG+"p_kurva.png", None, "58%") + "a) Vilket försök gick fortast? Hur ser man det?<br>b) Vilket försök hade högst temperatur? Förklara med partiklar.<br>c) Hur mycket gas bildades ungefär totalt?", None, 3, 6,
  "a) B, kurvan stiger brantare. b) B: vid högre temperatur rör sig partiklarna snabbare och krockar oftare och hårdare, så reaktionen går fortare. c) Ungefär 70 cm³ (65–70 godtas).", "a) 1 p. b) 1 p. c) 1 p."),
 ("C", "a) Förklara hur en natriumatom blir en natriumjon.<br>b) Vad är en jonbindning?<br>c) Varför leder inte fast salt ström?", None, 3, 6,
  "a) Natriumatomen (2, 8, 1) avger sin valenselektron och får 2, 8. Den har fortfarande 11 protoner men bara 10 elektroner, så laddningen blir +1. b) Attraktionen mellan positiva och negativa joner. c) Jonerna sitter fast i gittret och kan inte röra sig.", "a) 1 p. b) 1 p. c) 1 p."),
 ("A", "Bordssalt smälter vid ungefär 800 °C medan vatten fryser vid 0 °C.<br>a) Förklara skillnaden med bindningarna.<br>b) Förklara varför saltlösning leder ström men sockerlösning inte.<br>c) Värdera påståendet: ”Vatten leder elektricitet.”", None, 4, 8,
  "a) Bordssalt är en jonförening där jonerna hålls ihop av starka krafter i gittret, så det krävs mycket energi för att få dem att röra sig. Mellan vattenmolekylerna är krafterna svaga. b) I saltlösning finns rörliga joner som bär strömmen. Socker består av molekyler utan laddning. c) Påståendet är en förenkling. Rent vatten leder dåligt, men vanligt vatten leder eftersom det innehåller lösta salter (joner). Därför är det farligt med el nära vatten.", "a) 2 p (1 p för jonernas starka krafter, 1 p för svaga krafter mellan molekyler). b) 1 p. c) 1 p för att väga: vatten leder dåligt men vanligt vatten leder."),
 ("A", "En brusande tablett löses och det bubblar.<br>a) Förklara med krockar mellan partiklar varför den löses snabbare i varmt än i kallt vatten.<br>b) Förklara varför en krossad tablett reagerar snabbare än en hel.<br>c) Eleven säger: ”Tabletten försvann.” Värdera påståendet utifrån massans bevarande.", None, 4, 8,
  "a) I varmt vatten rör sig partiklarna snabbare, krockar oftare och hårdare och fler krockar leder till reaktion. b) Den krossade tabletten har större ytarea, så fler partiklar kan krocka med vattnet samtidigt. c) Tabletten har reagerat och bildat nya ämnen, bland annat en gas som lämnar bägaren. Atomerna har inte försvunnit. Massan hos allt tillsammans bevaras, men i en öppen bägare minskar den mätta massan när gasen lämnar.", "a) 1 p. b) 1 p. c) 2 p (1 p för att atomerna inte försvinner, 1 p för att gasen lämnar i öppen bägare)."),
 ("A", "En elev säger: ”I en kemisk reaktion skapas nya atomer, så massan kan öka.”<br>a) Bedöm påståendet och använd 2 H₂ + O₂ → 2 H₂O i svaret.<br>b) Förklara vad exoterm och endoterm betyder, och hur man kan avgöra vilken sort en reaktion är.<br>c) Värdera hur säker din slutsats i b) är.", None, 4, 8,
  "a) Påståendet är fel. Atomer skapas inte, de byter partner. I formeln finns 4 H och 2 O på båda sidor, så massan bevaras i ett slutet system. b) Exoterm: energi avges och omgivningen blir varmare. Endoterm: energi tas upp och omgivningen blir kallare. Man kan mäta temperaturen före och efter. c) En enda mätning är osäker: mätfel, värmeförluster och slumpen. Man bör upprepa försöket och jämföra med en kontroll innan man drar en säker slutsats.", "a) 2 p (1 p för att atomer inte skapas, 1 p för att använda formeln). b) 1 p. c) 1 p för att värdera säkerheten."),
]
NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
       ["13 Egenskaper", "Nämner att salt har hög smältpunkt eller att saltlösning leder.", "Förklarar skillnaderna med jonbindning och molekyler.", "Kopplar bindningstyp till smältpunkt och ledning och värderar påståendet om vatten."],
       ["14 Hastighet", "Säger att varmt vatten ger snabbare reaktion.", "Förklarar med krockar och ytarea.", "Förklarar med krockar och värderar påståendet om att tabletten försvinner med massans bevarande."],
       ["15 Massa och energi", "Säger att atomer inte försvinner.", "Använder reaktionsformeln för att visa att massan bevaras och förklarar exoterm och endoterm.", "Värderar hur säker slutsatsen om energin är och föreslår kontroller."]]
# Förmåga per uppgift (1 = begrepp/modeller, 2 = systematiska undersökningar, 3 = resonera, värdera och ta ställning)
FORM = ["F1", "F1", "F1", "F1", "F1", "F1", "F1", "F1", "F1", "F2", "F2", "F1", "F3", "F3", "F3"]
FN = {"F1": "Begrepp, modeller och samband", "F2": "Systematiska undersökningar", "F3": "Värdera, kommunicera och ta ställning"}
FORMKOM = {"F1": "Bindningar, joner, egenskaper, reaktioner och reaktionsformler (uppgift 1–9 och 12).",
           "F2": "Tolka vägningar och ett reaktionshastighetsdiagram (uppgift 10 och 11). Själva genomförandet bedöms i labb 4.1 och 4.2 och i bonuslabben.",
           "F3": "Värdera egenskaper och ledning, hastighet och massans bevarande och energi i reaktioner (uppgift 13–15)."}
IMPROV = ''
KOPPL = "Uppgift 1–9 och 12: begrepp, modeller och samband. Uppgift 10–11: tolka mätdata (systematiska undersökningar). Uppgift 13–15: värdera, förklara och ta ställning."
KAP = "Kapitel 4"; NAMN_ = "Kemiska föreningar och reaktioner"

def teacher_section():
    e = sum(x[3] for x in P if x[0] == "E"); c = sum(x[3] for x in P if x[0] == "C"); a = sum(x[3] for x in P if x[0] == "A")
    import math
    te = math.ceil(e * 2 / 3); tc = math.ceil(c / 2); ta = math.ceil(a / 2)
    rows = ""
    for f in ("F1", "F2", "F3"):
        idx = [i for i, t in enumerate(FORM) if f in t]
        pts = sum(P[i][3] for i in idx)
        rows += f'<tr><td>{f[1]}. {FN[f]}</td><td>{", ".join(str(i+1) for i in idx) or "–"}</td><td>{pts} p</td><td>{FORMKOM[f]}</td></tr>'
    ftab = '<table class="tbl"><tr><th>Förmåga</th><th>Uppgifter</th><th>Poäng</th><th>Kommentar</th></tr>' + rows + '</table>'
    return ('<section class="sec teacher"><h2>Till läraren: bedömning</h2>'
        f'<p>Provet har {e} p på del E, {c} p på del C och {a} p på del A (totalt {e+c+a} p). Fördelningen är medvetet C-tung: de flesta poängen ligger på C, sedan E och minst på A, ungefär som i de nationella proven. Del E motsvarar lättläst-versionen, del C grundtexten och del A fördjupningen. Uppgiftstyperna varierar (flerval, flersvar, matchning, kortsvar och resonemang), och varje uppgift är kopplad till en förmåga i facit.</p>'
        '<h3>Förmågor som provet prövar</h3>' + ftab +
        '<p class="note">Ett skriftligt prov kan inte pröva allt. Förmåga 2 bedöms också i labbrapporter och i bonuslabben, och förmåga 3 i diskussioner och argumentationer.</p>'
        '<h3>Poängsättning av resonemang</h3><p>Resonemang poängsätts efter hur många led eleven för, inte efter hur mycket eleven skriver: 1 p för varje korrekt led (orsak, följd, konsekvens) som hänger ihop med föregående, och 1 p för slutsats eller för att relevanta begrepp används rätt. Ett längre svar som upprepar samma led ger inte fler poäng. Facit visar förväntade led, och andra rimliga led godtas.</p>'
        + IMPROV +
        '<h3>Gränser för provbetyg</h3>'
        f'<p>Det finns inga prövade gränser för det här provet. De nationella proven sätter provbetyg efter poängsumma, med gränser som fastställs efter prövning på många elever, och det går inte att göra här. Som utgångspunkt kan du pröva: <b>E</b> vid minst {te} av {e} p på del E, <b>C</b> om E-nivån är uppnådd och minst {tc} av {c} p på del C, <b>A</b> om C-nivån är uppnådd och minst {ta} av {a} p på del A. Justera efter klassens resultat och efter vad eleverna visar i övrigt.</p>'
        '<p class="note">Kunskapskraven är kvalitativa (”enkla”, ”utvecklade” och ”välutvecklade” resonemang), och betyget sätts av en samlad bedömning av provet och elevens övriga underlag.</p>'
        '<h3>Bedömningsguide för resonemangsuppgifterna</h3>' + table(BED[0], BED[1:]) +
        '<h3>Kopplingar</h3><p>' + KOPPL + '</p>'
        '<p class="note">Fakta är kontrollerad mot källfilen för området. Upplägget är inspirerat av nationella prov, men provet är inte prövat på elever och gränserna är förslag. Personer, annonser och mätvärden i uppgifterna är påhittade.</p></section>')

def build(lararversion):
    h = ['<section class="sec"><div style="display:flex;justify-content:space-between;align-items:baseline"><div class="pill">' + KAP + ' · Prov</div><div class="note">Namn: ____________________ &nbsp; Klass: ________ &nbsp; Poäng: ____ / ' + str(sum(x[3] for x in P)) + '</div></div>'
         '<div class="sh"><h2>' + NAMN_ + '</h2></div>'
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
        fa = f'<div style="background:#f7e6e4;border-radius:5pt;padding:4pt 8pt;margin-top:4pt;font:9pt/1.35 Carlito"><b>Förmåga:</b> {FORM[n-1]} &nbsp; <b>Facit:</b> {fac}<br><b>Poäng:</b> {bed}</div>' if lararversion else ""
        h.append(f'<div class="q" style="grid-template-columns:16pt minmax(0,1fr) 30pt"><span class="n">{n}</span><div>{q}{a}{l}{fa}</div><span class="pts">{pts} p</span></div>')
    h.append('</section>')
    if lararversion: h.append(teacher_section())
    return "".join(h)

def doc(body, foot):
    return f'<!doctype html><html lang="sv"><head><meta charset="utf-8"><style>{css(foot, 1)}.q .alts{{grid-template-columns:1fr 1fr}}{DYS}</style></head><body>{body}</body></html>'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        p = f'{OUT}/kemi-4-{name}.pdf'
        html_to_pdf(doc(build(lar), 'Kapitel 4 · Kemiska föreningar och reaktioner · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))

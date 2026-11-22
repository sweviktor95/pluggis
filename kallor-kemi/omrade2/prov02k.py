# -*- coding: utf-8 -*-
"""Prov område 1 Kemi som vetenskap: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os, re
sys.path.insert(0, '/tmp/kem')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader, PdfWriter

FIG = '/tmp/kem/fig02k/'
TABELL = table(["Föremål", "Massa (g)", "Volym (cm³)"], [["A", "21,6", "8"], ["B", "7,5", "10"], ["C", "31,2", "4"]], "tbl num")
SMALT = table(["Ämne", "Smältpunkt (°C)"], [["Paraffin", "ca 52"], ["Tenn", "232"], ["Bly", "327"]], "tbl num")

def match(left, right, h1="Metod", h2="Används för"):
    return ('<table class="tbl num" style="width:92%"><tr><th>' + h1 + '</th><th>' + h2 + '</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')

# nivå, fråga, alternativ, poäng, antal linjer, facit, bedömning
P = [
 ("E", "Vilket påstående om partiklarna i en gas stämmer?", ["A De ligger tätt i ett mönster.", "B De är långt ifrån varandra och rör sig snabbt åt alla håll.", "C De glider förbi varandra men ligger nära.", "D De står stilla."], 1, 0, "B", "1 p för B."),
 ("E", "Ett föremål har massan 24 g och volymen 8 cm³. Vilken densitet har det?", ["A 3 g/cm³", "B 16 g/cm³", "C 32 g/cm³", "D 0,33 g/cm³"], 1, 0, "A", "1 p för A (24 / 8 = 3 g/cm³)."),
 ("E", "Vilka två påståenden stämmer? Kryssa i två.<br>☐ Is flyter på vatten eftersom is har lägre densitet.<br>☐ Temperaturen stiger medan is smälter.<br>☐ Salt går att filtrera bort från saltvatten.<br>☐ En fällning är ett fast ämne som bildas när lösningar blandas.", None, 2, 0, "Is flyter på vatten eftersom is har lägre densitet. En fällning är ett fast ämne som bildas när lösningar blandas.", "1 p per rätt. Avdrag om fler än två kryssas."),
 ("E", "Ett metallstycke läggs i en mätcylinder med vatten. Innan stycket lades i stod vattnet på 40 ml. Bilden visar nivån efter." + fig(FIG+"p_cylinder.png", None, "26%") + "a) Läs av nivån nu. Skriv värde och enhet.<br>b) Räkna ut metallstyckets volym.<br>Svar a: ____________ &nbsp; Svar b: ____________", None, 2, 0, "a) 58 ml. b) 58 − 40 = 18 ml = 18 cm³.", "a) 1 p för 58 ml (med enhet). b) 1 p för 18 cm³ (följdfel godtas)."),
 ("E", "Dra streck mellan metoden och vad den används till. Skriv bokstaven.<br>" + match(["1 Filtrering", "2 Destillation", "3 Kromatografi"], ["A Skilja färgämnen som vandrar olika långt", "B Skilja sand från vatten", "C Skilja ämnen med olika kokpunkter"]) + "Svar: 1 ___ &nbsp; 2 ___ &nbsp; 3 ___", None, 3, 0, "1 B, 2 C, 3 A", "1 p per rätt."),
 ("E", "Vad är skillnaden mellan en homogen och en heterogen blandning? Ge ett exempel på vardera.", None, 2, 3, "Homogen: ser likadan ut överallt, delarna syns inte, t.ex. saltvatten. Heterogen: delarna syns eller går att skilja åt, t.ex. sand i vatten.", "1 p för rätt skillnad med exempel på homogen. 1 p för heterogen med exempel. Alternativt 1 p för skillnaden och 1 p för två rätta exempel."),
 ("E", "Beskriv vad som händer med partiklarna när is smälter till flytande vatten.", None, 2, 3, "Partiklarna rör sig mer och lämnar sina fasta platser i mönstret. I vätskan ligger de fortfarande nära varandra men glider förbi varandra.", "1 p för att partiklarna lämnar mönstret/rör sig mer. 1 p för att de ligger nära och glider förbi varandra i vätskan."),
 ("C", "Elin har en blandning av sand, salt och vatten.<br>a) Vilken metod använder hon först, och vad blir kvar i filtret?<br>b) Hur får hon tillbaka saltet?<br>c) Varför går det inte att filtrera bort saltet?", None, 3, 6,
  "a) Filtrering. Sanden blir kvar i filtret. b) Indunsta filtratet (saltvattnet): vattnet förångas och saltet blir kvar. c) Saltet är löst i vattnet: partiklarna är så små att de går genom filtret.", "a) 1 p. b) 1 p. c) 1 p för att saltet är löst/för små partiklar."),
 ("C", "Tre föremål A, B och C har mätts. Värdena är påhittade." + TABELL + "a) Räkna ut densiteten för varje föremål.<br>b) Vilket eller vilka föremål flyter på vatten (densitet 1,0 g/cm³)? Förklara.", None, 3, 6,
  "a) A: 21,6 / 8 = 2,7 g/cm³. B: 7,5 / 10 = 0,75 g/cm³. C: 31,2 / 4 = 7,8 g/cm³. b) B flyter, eftersom densiteten 0,75 är lägre än vattnets 1,0. A och C sjunker.", "a) 1 p för alla tre rätt (följdfel godtas). b) 1 p för B. 1 p för förklaring med densitet."),
 ("C", "Diagrammet visar temperaturen när ett fast ämne värms jämnt." + fig(FIG+"p_kurva.png", None, "76%") + "Tabellen visar smältpunkter." + SMALT + "a) Vid vilken temperatur smälter ämnet?<br>b) Förklara varför temperaturen ligger still medan ämnet smälter.<br>c) Vilket ämne i tabellen kan det vara?", None, 3, 5,
  "a) Cirka 52 °C. b) Värmen går åt att bryta loss partiklarna från mönstret, inte att få dem att röra sig snabbare, så temperaturen ändras inte. c) Paraffin.", "a) 1 p (50–54 godtas). b) 1 p för att värmen går åt till att bryta loss partiklarna / inte höja rörelsen. c) 1 p för paraffin (följdfel godtas)."),
 ("C", "a) Förklara med partikelmodellen varför en gas kan tryckas ihop men en vätska knappt kan det.<br>b) Nämn något som partikelmodellen inte visar.", None, 3, 6,
  "a) I en gas finns det stort tomrum mellan partiklarna, så de kan komma närmare varandra. I en vätska ligger partiklarna redan nära varandra. b) T.ex. krafterna mellan partiklarna, hur partiklarna rör sig, ämnets färg eller att partiklarna inte är bollar.", "a) 1 p för gas (tomrum). 1 p för vätska (redan nära). b) 1 p för en giltig begränsning."),
 ("C", "Kromatogrammet visar tre kända färgämnen A, B och C och ett okänt prov X." + fig(FIG+"p_kroma.png", None, "58%") + "a) Vilka av A, B och C ingår i X?<br>b) Förklara varför färgämnena hamnar på olika höjd på papperet.", None, 3, 5,
  "a) A och C. b) Färgämnena löser sig olika bra i lösningsmedlet och fastnar olika mycket på papperet, så de vandrar olika långt.", "a) 1 p för A och C (båda). b) 1 p för löser sig olika bra. 1 p för fastnar olika mycket på papperet/vandrar olika långt."),
 ("A", "Du får ett okänt, vitt, fast ämne. Det kan vara bordssalt, socker eller något annat ämne. Planera en undersökning som kan ta reda på vad det är. Beskriv minst tre egenskaper du mäter eller testar, vad du jämför med, varför du behöver mer än en egenskap och vad du gör för att arbeta säkert.", None, 4, 8,
  "Mät t.ex. löslighet i vatten, smältpunkt och densitet, eller testa om det bildar fällning. Jämför med kända prov av salt och socker, och med tabellvärden. Flera egenskaper behövs eftersom flera ämnen kan ha liknande värde på en egenskap, och slutsatsen blir säkrare ju fler som stämmer. Upprepa mätningarna. Säkerhet: skyddsglasögon, smaka inte på ämnet.", "1 p för minst tre lämpliga egenskaper. 1 p för jämförelse med kända ämnen/tabell. 1 p för varför flera egenskaper behövs. 1 p för säkerhet och upprepning/slutsats som säger hur säker den är."),
 ("A", "Ett lag skulle få tillbaka 5,0 g salt men fick 4,2 g. Ett annat lag fick 5,3 g. Värdena är påhittade.<br>a) Räkna ut utbytet för det första laget.<br>b) Ge två tänkbara orsaker till att laget fick mindre än 5,0 g.<br>c) Vad kan det betyda att det andra laget fick mer än de startade med, och hur kan de kontrollera det?", None, 4, 8,
  "a) 4,2 / 5,0 × 100 = 84 %. b) T.ex. salt som fastnat på filter, bägare eller skål, spill, salt som sprutat vid upphettning. c) Mer än 100 % är orimligt eftersom man inte kan få mer än man hade. Saltet kan vara fuktigt eller ha sand i sig. Kontrollera genom att torka längre och väga om, och göra om försöket.", "a) 1 p. b) 1 p för två orsaker. c) 1 p för att resultatet är orimligt/fel. 1 p för en rimlig orsak och kontroll."),
 ("A", "Partikelmodellen säger att partiklarna i ett fast ämne ligger tätare än i en vätska. Ändå flyter is på vatten.<br>a) Förklara varför is flyter på vatten. Använd begreppet densitet.<br>b) Förklara varför detta är ett exempel på en begränsning hos den enkla partikelmodellen.<br>c) Förklara vad det betyder för livet i en sjö på vintern att is flyter.", None, 4, 8,
  "a) Is har lägre densitet (0,92 g/cm³) än flytande vatten (ca 1,0). b) Den enkla modellen förutsäger att fast ämne är tätare än vätska, men för vatten ordnar sig partiklarna i is i ett glest mönster som tar mer plats. Modellen tar inte hänsyn till hur krafterna ordnar partiklarna, så den behöver kompletteras. c) Isen ligger på ytan och isolerar. Vattnet under kan vara kvar flytande (ca 4 °C), så djur kan överleva vintern. Om isen sjönk kunde sjön frysa underifrån.", "a) 1 p. b) 1 p för att modellen förutsäger fel/inte räcker. 1 p för varför (isens glesa mönster/krafterna). c) 1 p för ett resonemang med minst två led (isen på ytan isolerar → vatten under fryser inte)."),
]
NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
       ["13 Planera", "Föreslår en eller två egenskaper att mäta.", "Anger minst tre egenskaper och vad som jämförs med.", "Förklarar varför flera egenskaper behövs, planerar upprepning och säkerhet och drar slutsats med osäkerhet."],
       ["14 Utbyte", "Räknar ut utbytet eller anger en orsak.", "Räknar ut utbytet och anger flera orsaker.", "Resonerar om att över 100 % är orimligt, anger orsak och hur man kontrollerar."],
       ["15 Modellens gräns", "Säger att is flyter eftersom den är lättare.", "Förklarar med densitet och att modellen räcker till en viss gräns.", "Kopplar isens glesa mönster till modellens begränsning och drar slutsatsen för livet i sjön."]]
# Förmåga per uppgift (1 = begrepp/modeller, 2 = systematiska undersökningar, 3 = resonera, värdera och ta ställning)
FORM = ["F1", "F1", "F1", "F2", "F1", "F1", "F1", "F2", "F2", "F2", "F1", "F2", "F2", "F2", "F3"]
FN = {"F1": "Begrepp, modeller och samband", "F2": "Systematiska undersökningar", "F3": "Värdera, kommunicera och ta ställning"}
FORMKOM = {"F1": "Partikelmodellen, tillstånd, densitet, blandningar och metoder (uppgift 1–3, 5–7 och 11).",
           "F2": "Mäta, tolka och planera på papper. Själva genomförandet bedöms i labb 2.1 och 2.2 och i bonuslabben.",
           "F3": "Resonera och värdera modellens gränser (uppgift 15)."}
IMPROV = ''
KOPPL = "Uppgift 4, 8, 9, 10, 12, 13 och 14: systematiska undersökningar (mäta, tolka, planera, värdera). Uppgift 1, 2, 3, 5, 6, 7 och 11: begrepp och modeller. Uppgift 15: resonera och värdera modellens gränser."
KAP = "Kapitel 2"; NAMN_ = "Materia och partiklar"

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


def front_page(lararversion):
    cn = {k: [i + 1 for i, x in enumerate(P) if x[0] == k] for k in "ECA"}
    def rng(l): return f"{l[0]}–{l[-1]}"
    box_ = '<td style="height:26pt"></td>'
    up = ('<table class="tbl num" style="width:100%"><tr><th>Del</th><th>Uppgifter</th><th style="width:15%">Röd</th><th style="width:15%">Gul</th><th style="width:15%">Grön</th></tr>'
          + "".join(f'<tr><td style="font-weight:700">{NIVA[k][0]} · {NIVA[k][1]}</td><td>{rng(cn[k])}</td>{box_*3}</tr>' for k in "ECA") + '</table>')
    steg = ["F", "E", "D", "C", "B", "A"]
    mat = ('<table class="tbl num" style="width:100%"><tr><th style="width:34%">Förmåga</th>' + "".join(f'<th>{x}</th>' for x in steg) + '</tr>'
           + "".join(f'<tr><td style="font-weight:700">{FN[f]}</td>{box_*6}</tr>' for f in ("F1", "F2", "F3"))
           + f'<tr><td style="font-weight:700;background:#f7e6e4">Samlad nivå på provet</td>{box_*6}</tr></table>')
    return ('<section class="sec" style="break-after:page"><div style="display:flex;justify-content:space-between;align-items:baseline"><div class="pill">' + KAP + ' · Prov</div><div class="note">Namn: ____________________ &nbsp; Klass: ________ &nbsp; Datum: ________</div></div>'
            '<div class="sh"><h2>' + NAMN_ + '</h2></div>'
            '<h3>Så många uppgifter på varje nivå</h3>'
            '<p class="note">Fyll i hur många uppgifter du har på röd, gul och grön, så ser du var du står på varje del.</p>' + up +
            '<h3 style="margin-top:14pt">Nivå per förmåga</h3>'
            '<p class="note">Markera i matrisen vilken nivå du bedömer att du ligger på i varje förmåga. Läraren markerar med en annan färg, så kan ni jämföra. Provet har ingen poängräkning.</p>' + mat +
            '<h3 style="margin-top:14pt">Lärarens övergripande kommentarer</h3>' + lines(7) +
            '<p class="note" style="margin-top:8pt">Nästa steg för eleven:</p>' + lines(3) + '</section>')

def build(lararversion):
    h = [front_page(lararversion), '<section class="sec"><div class="pill">' + KAP + ' · Prov</div>'
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
        p = f'{OUT}/kemi-2-{name}.pdf'
        html_to_pdf(doc(build(lar), 'Kapitel 2 · Materia och partiklar · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))

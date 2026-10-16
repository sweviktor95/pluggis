# -*- coding: utf-8 -*-
"""Kemi område 1 Kemi som vetenskap – lättläst version (byggd per moment)."""
FIG = '/tmp/kem/fig01k/'
NR = 1
SLUG = "kemi-vetenskap"
TAB = "1"
NAMN = "Kemi som vetenskap"
NDEL = 9
UNDER = "Så undersöker och tänker en kemist"
INTRO_L = ["I det här kapitlet lär du dig hur en kemist arbetar.",
           "Du lär dig arbeta säkert i ett kemilabb och göra ett rättvist försök. Du lär dig också vad en modell är, hur kemin har vuxit fram och hur du kollar om ett påstående stämmer.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Start: vad kemi är",
        "Delområde 1.1 Arbeta som kemist: säkerhet, utrustning, fråga och plan, resultat",
        "Delområde 1.2 Modeller, källor och argument: modeller, kemins historia och källkritik"]
ORD_FIG = None
ORD_EXTRA = [("kemi", "läran om ämnen och hur de förändras"), ("ämne", "en sorts material, till exempel vatten eller socker"), ("naturvetenskap", "kunskap som man prövar med undersökningar"),
             ("faropiktogram", "en symbol som visar vilken fara ett ämne har"), ("signalord", "Fara eller Varning på en etikett"), ("mätcylinder", "ett glasrör med skala för att mäta volym"),
             ("menisk", "vattenytans böjning i mätcylindern"), ("hypotes", "en gissning som man kan pröva"), ("variabel", "något som kan ändras eller mätas i ett försök"),
             ("rättvist försök", "du ändrar bara en sak i taget"), ("medelvärde", "lägg ihop alla värden och dela med antalet"), ("felkälla", "något som kan göra mätningen osäker"),
             ("slutsats", "svaret på frågan, byggt på resultatet"), ("modell", "en enkel bild eller idé som förklarar något"), ("partikel", "en mycket liten bit som ämnen är uppbyggda av"),
             ("grundämne", "ett ämne som inte går att dela upp i enklare ämnen"), ("atom", "den minsta delen av ett grundämne"), ("källkritik", "att kolla vem som säger något och varför"),
             ("kemikalie", "ett kemiskt ämne, till exempel vatten eller salt"), ("belägg", "mätningar som visar att något stämmer")]

TB_PERSON = ('<table class="tb"><tr><th>Kemist</th><th>Gör</th></tr>'
             '<tr><td>Analytisk kemist</td><td>Mäter vad ett prov innehåller</td></tr><tr><td>Läkemedelskemist</td><td>Tar fram och testar läkemedel</td></tr>'
             '<tr><td>Materialkemist</td><td>Utvecklar material, till exempel batterier</td></tr><tr><td>Miljökemist</td><td>Undersöker föroreningar</td></tr></table>')
TB_VAR = ('<table class="tb"><tr><th>Variabel</th><th>I försöket</th></tr>'
          '<tr><td>Jag ändrar</td><td>Vattnets temperatur</td></tr><tr><td>Jag mäter</td><td>Tiden tills tabletten är borta</td></tr>'
          '<tr><td>Jag håller lika</td><td>Mängd vatten, sort på tablett</td></tr></table>')
TB_BRUS = ('<table class="tb"><tr><th>Temperatur</th><th>Försök 1 (s)</th><th>Försök 2 (s)</th><th>Försök 3 (s)</th><th>Medelvärde (s)</th></tr>'
           '<tr><td>5 °C</td><td></td><td></td><td></td><td></td></tr><tr><td>20 °C</td><td></td><td></td><td></td><td></td></tr><tr><td>40 °C</td><td></td><td></td><td></td><td></td></tr></table>')
TB_FLACK = ('<table class="tb"><tr><th>Vätska</th><th>Poäng 0–3</th></tr>'
            '<tr><td>A Bara vatten</td><td></td></tr><tr><td>B Diskmedel</td><td></td></tr><tr><td>C Fläckborttagare X</td><td></td></tr><tr><td>D Tvättmedel</td><td></td></tr></table>')

DELOMR = {"1.1": "Arbeta som kemist", "1.2": "Modeller, källor och argument"}
DELAR = [
 dict(titel="Vad är kemi?", prog="Start · Vad är kemi?",
  fore=["<strong>Kemi</strong> handlar om ämnen och hur de förändras. Allt du ser och rör vid är gjort av ämnen: vatten, socker, plast och luft.", "Kemi är en <strong>naturvetenskap</strong>. Kemister gissar inte. De gör undersökningar och mäter."],
  fig="l_kemister.png", figw="95%",
  efter=["Det finns många sorters kemister. De kan till exempel mäta vad ett prov innehåller, ta fram läkemedel, utveckla nya material eller undersöka föroreningar."],
  kom="Kemi är läran om ämnen och hur de förändras. Kemister undersöker och mäter.",
  ova=[("ringa", "Vad handlar kemi om?", ["Ämnen och hur de förändras", "Bara om djur", "Bara om planeter"]),
       ("sf", "Kryssa i rätt ruta.", ["Kemister gör undersökningar och mäter.", "Kemi finns bara i labbet.", "Vatten är ett ämne."]),
       ("fyll", ["mäter", "ämnen", "förändras"], ["Kemi handlar om ______________.", "Ämnen ______________ i kemiska reaktioner.", "En kemist ______________ och undersöker."]),
       ("skriv", "Nämn något i ditt kök som är gjort av kemiska ämnen.", "Ett exempel är", 2)]),

 dict(titel="Säkerhet och utrustning i kemilabbet", prog="Delområde 1.1 · Säkerhet och utrustning",
  fore=["I ett kemilabb är säkerheten viktigast.", "<ol class='st'><li>Ha skyddsglasögon på.</li><li>Sätt upp långt hår.</li><li>Smaka eller drick aldrig något.</li><li>Ät inte i labbet.</li><li>Torka upp spill och säg till läraren.</li><li>Tvätta händerna efteråt.</li></ol>"],
  fig="v_utrustning.png", figw="64%",
  efter=["Farliga produkter har <strong>faropiktogram</strong>. Det är röda rutor med en svart bild.", "På etiketten står också <strong>Fara</strong> eller <strong>Varning</strong>.",
         "Du mäter volym med en <strong>mätcylinder</strong>. Håll ögonen i höjd med vattenytan. Läs av där ytan är lägst."],
  fig2="v_piktogram.png", fig2w="76%", n1=2,
  kom="Använd skyddsglasögon. Smaka aldrig. Läs av mätcylindern med ögonen i höjd med ytan.",
  ova=[("ringa", "Vad ska du alltid ha på dig när du arbetar med kemikalier?", ["Skyddsglasögon", "Mössa", "Handskar av ull"]),
       ("sf", "Kryssa i rätt ruta.", ["Du får smaka på ämnen i labbet.", "Långt hår ska sättas upp.", "Piktogrammen visar vilken fara ämnet har."]),
       ("streck", "Dra streck till rätt mätning.", ["Volym", "Massa", "Temperatur"], ["termometer", "mätcylinder", "våg"]),
       ("fyll", ["skyddsglasögon", "faropiktogram", "ytan"], ["Jag har ______________ på mig i labbet.", "Ett ______________ visar vilken fara ett ämne har.", "Jag läser av vid den lägsta delen av ______________."])]),

 dict(titel="Från fråga till plan", prog="Delområde 1.1 · Från fråga till plan",
  fore=["En undersökning börjar med en fråga som du kan mäta svaret på.", "<strong>Exempel:</strong> Hur påverkar vattnets temperatur tiden det tar för en brustablett att lösa sig?"],
  fig="l_cykel.png", figw="85%",
  efter=["En <strong>hypotes</strong> är en gissning som du kan pröva. Skriv: ”Om … så …, eftersom …”.", "I ett försök finns tre sorters <strong>variabler</strong>.", TB_VAR,
         "Ett försök är <strong>rättvist</strong> om du bara ändrar en sak i taget."],
  fig2="v_brus.png", fig2w="95%", n1=2,
  kom="Ändra en sak i taget. Mät något. Håll allt annat lika.",
  ova=[("ringa", "Vad är en hypotes?", ["En gissning som går att pröva", "Ett säkert svar", "En tabell"]),
       ("streck", "Dra streck till rätt sorts variabel.", ["Jag ändrar", "Jag mäter", "Jag håller lika"], ["tid tills tabletten är borta", "temperatur", "mängd vatten"]),
       ("sf", "Kryssa i rätt ruta.", ["I ett rättvist försök ändrar man bara en sak i taget.", "Man ska ändra både temperatur och vattenmängd.", "En hypotes kan visa sig vara fel."]),
       ("skriv", "Du vill veta om en sockerbit löser sig fortare om du rör om. Vad ändrar du?", "Jag ändrar", 2)]),

 dict(titel="Dokumentera och värdera", prog="Delområde 1.1 · Dokumentera och värdera",
  fore=["Skriv ner dina mätvärden i en tabell. Skriv enheter, till exempel s för sekunder.", "Gör flera mätningar. Räkna sedan ut <strong>medelvärdet</strong>.", "<strong>Exempel:</strong> 70 s, 78 s och 74 s. Medelvärdet är (70 + 78 + 74) / 3 = 74 s."],
  fig="v_brusdiagram.png", figw="80%",
  efter=["Ett diagram visar mönster. Det du ändrar (temperatur) ligger på den vågräta axeln. Det du mäter (tid) ligger på den lodräta.",
         "En <strong>felkälla</strong> är något som kan göra mätningen osäker, till exempel att klockan startas sent.", "En <strong>slutsats</strong> svarar på frågan: Ju varmare vatten, desto kortare tid. Hypotesen stämde."],
  kom="Upprepa mätningarna, räkna medelvärde och skriv en slutsats som svarar på frågan.",
  ova=[("ringa", "Hur räknar du ut ett medelvärde?", ["Lägger ihop värdena och delar med antalet", "Tar det största värdet", "Tar det minsta värdet"]),
       ("fyll", ["medelvärdet", "felkälla", "slutsats"], ["Jag räknade ut ______________.", "Att klockan startade sent är en ______________.", "Jag skrev en ______________ som svarar på frågan."]),
       ("sf", "Kryssa i rätt ruta.", ["Ett tal behöver en enhet.", "Man ska bara göra en mätning.", "Man ska upprepa mätningarna."]),
       ("skriv", "Räkna ut medelvärdet av 29 s, 33 s och 31 s.", "Medelvärdet är", 2)]),

 dict(titel="Labb 1.1 Brustabletten och temperaturen", prog="Delområde 1.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur påverkar vattnets temperatur tiden det tar för en brustablett att lösa sig?", "Du behöver: tre glas, mätcylinder, termometer, ur, brustabletter, vatten, skyddsglasögon."],
  fig=None,
  efter=["<ol class='st'><li>Mät upp 2 dl vatten i varje glas.</li><li>Gör vattnet cirka 5 °C, 20 °C och 40 °C.</li><li>Släpp ner en tablett och starta klockan.</li><li>Stoppa klockan när tabletten är borta.</li><li>Gör tre försök för varje temperatur.</li><li>Räkna medelvärde.</li></ol>", TB_BRUS,
         "<strong>Säkerhet:</strong> Ha skyddsglasögon. Drick inte vattnet. Använd inte varmare vatten än 40 °C. Torka upp spill."],
  kom="Rör inte om. Starta och stoppa klockan på samma sätt varje gång.",
  ova=[("fyll", ["temperaturen", "tiden", "mängd vatten"], ["Jag ändrade ______________.", "Jag mätte ______________.", "Jag höll lika ______________."]),
       ("skriv", "Vad visar ditt resultat? Stämde din hypotes?", "Mitt resultat visar", 3),
       ("skriv", "Vad kan ha gjort mätningen osäker?", "Det kan ha varit", 2)]),

 dict(titel="Vad är en modell i kemi?", prog="Delområde 1.2 · Vad är en modell i kemi?",
  fore=["Kemister arbetar med sådant som är för litet att se. Då använder de <strong>modeller</strong>.", "En modell är en enkel bild eller idé som förklarar något. En modell är inte riktiga verkligheten."],
  fig="l_modell.png", figw="95%",
  efter=["<strong>Exempel:</strong> I partikelmodellen tänker vi oss att ämnen består av små partiklar.", "Modellen förklarar varför en brustablett löser sig fortare i varmt vatten: partiklarna rör sig snabbare.",
         "Men modellen kan inte förklara allt, till exempel ämnets färg. Då behövs en annan modell."],
  kom="En modell är en förenkling. Den kan förklara en del men inte allt.",
  ova=[("ringa", "Vad är en modell?", ["En enkel bild eller idé som förklarar något", "En riktig bit av ett ämne", "En tabell med mätvärden"]),
       ("sf", "Kryssa i rätt ruta.", ["En modell är samma sak som verkligheten.", "En modell kan förklara en del men inte allt.", "En karta är en modell."]),
       ("fyll", ["partiklar", "förenkling", "färg"], ["En modell är en ______________.", "I partikelmodellen består ämnen av ______________.", "Modellen säger inget om ämnets ______________."]),
       ("skriv", "Ge ett exempel på en modell du ser i vardagen.", "Ett exempel är", 2)]),

 dict(titel="Hur kemin vuxit fram", prog="Delområde 1.2 · Hur kemin vuxit fram",
  fore=["För länge sedan trodde man att allt var gjort av fyra element: jord, vatten, luft och eld. Det trodde man i över 2 000 år."],
  fig="v_tidslinje.png", figw="95%",
  efter=["Boyle tvivlade 1661. Han ville ha bevis från försök.", "Lavoisier vägde ämnen 1789. Han visade att massan är lika stor före och efter en reaktion.",
         "Dalton föreslog 1808 att allt är gjort av atomer. Atomer av olika ämnen väger olika."],
  fig2="v_massa.png", fig2w="85%", n1=3,
  kom="Modeller ändras när nya undersökningar visar något nytt: fyra element blev atomer.",
  ova=[("streck", "Dra streck till rätt forskare.", ["Boyle", "Lavoisier", "Dalton"], ["atomteori", "krävde bevis från försök", "massan bevaras"]),
       ("sf", "Kryssa i rätt ruta.", ["Man trodde länge att allt var fyra element.", "Lavoisier vägde ämnen.", "Atomteorin kom före Boyle."]),
       ("fyll", ["atomer", "försök", "massan"], ["Boyle ville ha bevis från ______________.", "Lavoisier visade att ______________ bevaras.", "Dalton sa att allt består av ______________."]),
       ("skriv", "Varför är det bra att en modell kan ändras?", "Det är bra eftersom", 2)]),

 dict(titel="Granska kemipåståenden", prog="Delområde 1.2 · Granska påståenden",
  fore=["Du ser påståenden om kemi i reklam: ”Kemikaliefritt!” eller ”100 % naturligt!”. Stämmer de?", "Ställ frågor. Det kallas <strong>källkritik</strong>."],
  fig=None,
  efter=["<ol class='st'><li>Vem säger det?</li><li>Varför säger de det? Vill de sälja?</li><li>Vilka belägg finns?</li><li>Hur gammal är informationen?</li><li>Vad säger andra källor?</li></ol>",
         "<strong>Kemikalie</strong> betyder kemiskt ämne. Vatten och salt är kemikalier. Därför kan inget vara kemikaliefritt.", "Naturligt betyder inte ofarligt. Flugsvampen är naturlig men giftig."],
  kom="Fråga: vem, varför, vilka belägg? Naturligt är inte alltid ofarligt.",
  ova=[("ringa", "Vilken fråga är bra när du granskar en reklam?", ["Vill de sälja något?", "Vilken färg har förpackningen?", "Hur stor är bilden?"]),
       ("sf", "Kryssa i rätt ruta.", ["Vatten är en kemikalie.", "Allt som är naturligt är ofarligt.", "Reklam vill ofta sälja något."]),
       ("fyll", ["belägg", "källkritik", "kemikalie"], ["Att ställa frågor om en källa kallas ______________.", "Mätningar som visar att något stämmer är ______________.", "Vatten är en ______________."]),
       ("skriv", "Skriv en fråga du skulle ställa om en reklam som säger ”kemikaliefri”.", "Jag skulle fråga", 2)]),

 dict(titel="Labb 1.2 Fungerar fläckborttagaren?", prog="Delområde 1.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Tar fläckborttagare X bort en fläck bättre än vatten, diskmedel och tvättmedel? (Namnet är påhittat.)", "Du behöver: fyra tygbitar med lika fläck, fyra glas, vätskorna, ur, skyddsglasögon och handskar."],
  fig="v_flack.png", figw="95%",
  efter=["<ol class='st'><li>Märk tygbitarna A–D.</li><li>Häll lika mycket av varje vätska i varsitt glas.</li><li>Lägg tygbitarna i vätskorna. Låt dem ligga lika länge.</li><li>Skölj lika länge och låt torka.</li><li>Sätt poäng: 0 = ingen skillnad, 3 = fläcken är borta. Låt en kamrat sätta poäng utan att veta vilken som är vilken.</li></ol>", TB_FLACK,
         "<strong>Säkerhet:</strong> Ha skyddsglasögon och handskar. Läs etiketten. Blanda aldrig produkter. Tvätta händerna."],
  kom="Vatten är med som jämförelse. Ändra bara vätskan.",
  ova=[("fyll", ["vätskan", "poäng", "jämförelse"], ["Jag ändrade ______________.", "Jag satte ______________ på fläcken.", "Bara vatten är en ______________."]),
       ("skriv", "Tog fläckborttagare X bort fläcken bäst? Skriv vad du såg.", "Jag såg att", 3),
       ("skriv", "Vad testade du inte? Till exempel andra sorters fläckar.", "Jag testade inte", 2)]),
]

VIKTIGAST = [("l_ic1.png", "Kemi är läran om ämnen och hur de förändras. Kemister undersöker och mäter."),
             ("l_ic5.png", "Använd skyddsglasögon, smaka aldrig och läs av mätcylindern rätt. Faropiktogram visar faror."),
             ("l_ic2.png", "En undersökning: fråga, hypotes, test och slutsats."),
             ("l_ic3.png", "Ett rättvist försök: ändra en sak, mät en sak och håll resten lika."),
             ("l_ic4.png", "Upprepa mätningarna, räkna medelvärde och skriv en slutsats som svarar på frågan."),
             ("l_ic7.png", "En modell är en förenkling. Den kan förklara en del men inte allt, och den kan ändras."),
             ("l_ic8.png", "Från fyra element till atomer: Boyle, Lavoisier och Dalton."),
             ("l_ic6.png", "Granska påståenden: vem, varför, vilka belägg? Allt är kemikalier.")]
TEST = [("ringa", "Vad ska du ha på dig i ett kemilabb?", ["Skyddsglasögon", "Solglasögon", "Hörlurar"]),
        ("streck", "Dra streck till rätt förklaring.", ["Hypotes", "Medelvärde", "Modell", "Källkritik"], ["en enkel idé som förklarar något", "en gissning som går att pröva", "att granska vem som säger något", "summan delat med antalet"]),
        ("sf", "Kryssa i rätt ruta.", ["Man ska ändra en sak i taget.", "Man behöver bara mäta en gång.", "Allt är kemikalier.", "Naturligt är alltid ofarligt.", "Modeller kan ändras.", "Lavoisier visade att massan bevaras."]),
        ("fyll", ["hypotes", "felkälla", "atomer"], ["En gissning som går att pröva är en ______________.", "Något som gör en mätning osäker är en ______________.", "Dalton sa att allt består av ______________."]),
        ("siffror", "Sätt i ordning. Skriv 1, 2, 3 och 4.", ["Gör ett test", "Ställ en fråga", "Skriv en slutsats", "Skriv en hypotes"]),
        ("skriv", "Varför ska man bara ändra en sak i taget?", "Man ska ändra en sak eftersom", 3),
        ("skriv", "Räkna ut medelvärdet av 148 s, 160 s och 148 s. Avrunda till hela sekunder.", "Medelvärdet är", 2),
        ("skriv", "Varför kan man inte lita på en reklam utan att kolla?", "Det är så eftersom", 2)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 1 (Kemi som vetenskap): säkerhet och utrustning, att planera ett rättvist försök med en variabel i taget, att dokumentera och värdera, att förklara vad en modell är och att modeller förändras samt att granska påståenden om kemi. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå. Partikelmodellen fördjupas i kapitel 2.")
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "9 delar (start, sex moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Samma två delområden som grundtexten.", "Övningar med flera format: ringa in, dra streck, kryssa, fyll i, skriva och sätta i ordning.", "Kom ihåg-ruta i varje moment och en samlad Viktigast-sida."]
HANDLEDNING_HTML = """
<h3>Handledning per moment (lättläst)</h3>
<h3 class="mm">Vad är kemi?</h3><p class="hl"><b>E-mål:</b> eleven vet att kemi handlar om ämnen och förändringar och att kemister undersöker och mäter. <b>Vanligt fel:</b> att kemi bara finns i labbet.</p>
<h3 class="mm">Säkerhet och utrustning i kemilabbet</h3><p class="hl"><b>E-mål:</b> eleven följer säkerhetsreglerna och läser av en mätcylinder. <b>Vanligt fel:</b> att läsa av vid ytans övre kant.</p>
<h3 class="mm">Från fråga till plan</h3><p class="hl"><b>E-mål:</b> eleven skriver en hypotes och pekar ut vad som ändras, mäts och hålls lika. <b>Vanligt fel:</b> att ändra flera saker samtidigt.</p>
<h3 class="mm">Dokumentera och värdera</h3><p class="hl"><b>E-mål:</b> eleven fyller i tabell, räknar medelvärde och skriver en enkel slutsats. <b>Vanligt fel:</b> att glömma enheter.</p>
<h3 class="mm">Labb 1.1 Brustabletten och temperaturen</h3><p class="hl"><b>Material:</b> glas, mätcylinder, termometer, ur, brustabletter. <b>Förväntat:</b> kortare tid i varmare vatten. Använd inte varmare vatten än 40 °C.</p>
<h3 class="mm">Vad är en modell i kemi?</h3><p class="hl"><b>E-mål:</b> eleven förklarar enkelt vad en modell är och ger ett exempel. <b>Vanligt fel:</b> att modellen är en bild av hur det ”egentligen ser ut”.</p>
<h3 class="mm">Hur kemin vuxit fram</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på hur en modell ändrats (fyra element till atomer). <b>Vanligt fel:</b> att äldre forskare var ”dumma”.</p>
<h3 class="mm">Granska kemipåståenden</h3><p class="hl"><b>E-mål:</b> eleven ställer minst två frågor om ett påstående. <b>Vanligt fel:</b> ”naturligt är ofarligt” och ”kemikaliefritt är säkrast”.</p>
<h3 class="mm">Labb 1.2 Fungerar fläckborttagaren?</h3><p class="hl"><b>Material:</b> vit bomull, te eller kaffe, glas, vatten, diskmedel, tvättmedel och en fläckborttagare. <b>Förväntat:</b> resultaten varierar. Förbered fläckarna så att de hinner torka.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Ämnen och hur de förändras. 2) Sant, falskt, sant. 3) ämnen, förändras, mäter. 4) Egna exempel.",
 "<b>Säkerhet och utrustning:</b> 1) Skyddsglasögon. 2) Falskt, sant, sant. 3) Volym – mätcylinder; Massa – våg; Temperatur – termometer. 4) skyddsglasögon, faropiktogram, ytan.",
 "<b>Från fråga till plan:</b> 1) En gissning som går att pröva. 2) Jag ändrar – temperatur; Jag mäter – tid tills tabletten är borta; Jag håller lika – mängd vatten. 3) Sant, falskt, sant. 4) Om du rör om eller inte.",
 "<b>Dokumentera och värdera:</b> 1) Lägger ihop värdena och delar med antalet. 2) medelvärdet, felkälla, slutsats. 3) Sant, falskt, sant. 4) (29 + 33 + 31) / 3 = 31 s.",
 "<b>Labb 1.1:</b> 1) temperaturen, tiden, mängd vatten. 2) Egna resultat, t.ex. kortare tid i varmare vatten. 3) T.ex. att klockan startades sent eller att vattnet svalnade.",
 "<b>Vad är en modell:</b> 1) En enkel bild eller idé som förklarar något. 2) Falskt, sant, sant. 3) förenkling, partiklar, färg. 4) T.ex. en karta eller en molekylmodell.",
 "<b>Hur kemin vuxit fram:</b> 1) Boyle – krävde bevis från försök; Lavoisier – massan bevaras; Dalton – atomteori. 2) Sant, sant, falskt. 3) försök, massan, atomer. 4) Man kan rätta fel och förbättra förklaringarna.",
 "<b>Granska kemipåståenden:</b> 1) Vill de sälja något? 2) Sant, falskt, sant. 3) källkritik, belägg, kemikalie. 4) T.ex. Vilka ämnen innehåller den, och vilka belägg finns?",
 "<b>Labb 1.2:</b> 1) vätskan, poäng, jämförelse. 2) Egna resultat. 3) Egna svar, t.ex. andra sorters fläckar eller tyger.",
 "<b>Testa dig:</b> 1) Skyddsglasögon. 2) Hypotes – en gissning som går att pröva; Medelvärde – summan delat med antalet; Modell – en enkel idé som förklarar något; Källkritik – att granska vem som säger något. 3) Sant, falskt, sant, falskt, sant, sant. 4) hypotes, felkälla, atomer. 5) Ställ en fråga 1; Skriv en hypotes 2; Gör ett test 3; Skriv en slutsats 4. 6) Annars vet man inte vad som gav skillnaden. 7) (148 + 160 + 148) / 3 = 152 s. 8) Reklam vill ofta sälja, så man behöver kolla belägg.",
]

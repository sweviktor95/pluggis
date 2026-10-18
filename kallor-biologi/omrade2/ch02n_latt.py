# -*- coding: utf-8 -*-
"""Område 2 Cellen och livets processer – lättläst version (nya ramverket, byggd per moment)."""
FIG = '/tmp/bio/fig02n/'
NR = 2
SLUG = "cellen"
TAB = "2"
NAMN = "Cellen och livets processer"
NDEL = 11
UNDER = "Små byggstenar – stora processer"
INTRO_L = ["I det här kapitlet lär du dig vad allt levande är byggt av: celler.",
           "Du lär dig hur en cell ser ut, hur växter gör mat av solljus och hur alla celler får energi. Du lär dig också hur celler bildar organ och hela kroppen.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Start: vad som kännetecknar liv, och vad en cell är",
        "Delområde 2.1 Cellen: cellteorin, mikroskopet, djurcell, växtcell och bakterier",
        "Delområde 2.2 Fotosyntes och cellandning: hur växter gör mat och hur alla celler får energi",
        "Delområde 2.3 Organ och organsystem: hur celler blir vävnader, organ och en hel kropp"]
ORD_FIG = FIG + "l_ord.png"
ORD_FIGW = "52%"
ORD_EXTRA = [("organism", "en levande varelse, till exempel en växt eller ett djur"), ("encellig", "består av en enda cell, till exempel en bakterie"), ("flercellig", "består av många celler"),
             ("cellteorin", "alla levande varelser är byggda av celler, och nya celler kommer från andra celler"), ("mikroskop", "ett instrument som förstorar små saker"),
             ("cellmembran", "ett tunt skal runt cellen"), ("cytoplasma", "geléartad massa inuti cellen"), ("cellvägg", "en stadig vägg runt växtceller"),
             ("vakuol", "en blåsa med vatten i växtcellen"), ("ribosom", "en liten del som bygger proteiner"), ("klorofyll", "grönt ämne som fångar ljus"),
             ("glukos", "druvsocker, cellens bränsle"), ("producent", "gör egen mat, till exempel en växt"), ("kretslopp", "ämnen som går runt och används om och om igen"),
             ("vävnad", "många lika celler som arbetar ihop"), ("organ", "en del av kroppen, till exempel hjärtat"), ("organsystem", "flera organ som arbetar ihop"),
             ("bakterie", "en encellig organism utan cellkärna"), ("antibiotika", "läkemedel mot bakterier. Hjälper inte mot virus"), ("jäsning", "när jäst får energi utan syre")]

TB_LIV = ('<table class="tb"><tr><th>Kännetecken</th><th>Exempel</th></tr>'
          '<tr><td>Celler</td><td>Allt levande är byggt av celler</td></tr><tr><td>Energi</td><td>Växter tar ljus. Djur äter mat.</td></tr>'
          '<tr><td>Växer</td><td>Ett frö blir en växt</td></tr><tr><td>Förökar sig</td><td>Djur får ungar</td></tr>'
          '<tr><td>Reagerar</td><td>Växten vänder sig mot ljus</td></tr></table>')
TB_FOREM = ('<table class="tb"><tr><th>Del</th><th>Djurcell</th><th>Växtcell</th></tr>'
            '<tr><td>Cellvägg</td><td class="n">–</td><td class="n">✔</td></tr>'
            '<tr><td>Kloroplast</td><td class="n">–</td><td class="n">✔</td></tr><tr><td>Stor vakuol</td><td class="n">–</td><td class="n">✔</td></tr></table>')
TB_PROC = ('<table class="tb"><tr><th></th><th>Fotosyntes</th><th>Cellandning</th></tr>'
           '<tr><td>In</td><td>koldioxid, vatten, ljus</td><td>glukos, syre</td></tr><tr><td>Ut</td><td>glukos, syre</td><td>koldioxid, vatten, energi</td></tr>'
           '<tr><td>Var</td><td>kloroplast</td><td>mitokondrie</td></tr><tr><td>När</td><td>bara i ljus</td><td>hela tiden</td></tr></table>')
TB_JAST = ('<table class="tb"><tr><th>Temperatur</th><th>5 min</th><th>10 min</th><th>15 min</th></tr>'
           '<tr><td>ca 5 °C</td><td></td><td></td><td></td></tr><tr><td>ca 20 °C</td><td></td><td></td><td></td></tr>'
           '<tr><td>ca 35 °C</td><td></td><td></td><td></td></tr><tr><td>ca 50 °C</td><td></td><td></td><td></td></tr></table>')
TB_SYST = ('<table class="tb"><tr><th>Organsystem</th><th>Uppgift</th></tr>'
           '<tr><td>Matsmältning</td><td>Bryter ner maten</td></tr><tr><td>Andning</td><td>Tar in syre</td></tr>'
           '<tr><td>Cirkulation</td><td>Transporterar med blodet</td></tr><tr><td>Nervsystem</td><td>Skickar signaler</td></tr>'
           '<tr><td>Skelett och muskler</td><td>Stöd och rörelse</td></tr><tr><td>Utsöndring</td><td>Renar blodet</td></tr></table>')

DELOMR = {"2.1": "Cellen", "2.2": "Fotosyntes och cellandning", "2.3": "Organ och organsystem"}
DELAR = [
 dict(titel="Vad är liv?", prog="Start · Vad är liv?",
  fore=["Hur vet vi att något lever? Biologer ser efter några <strong>kännetecken</strong>.", TB_LIV],
  fig="l_liv.png",
  efter=["Allt levande är byggt av <strong>celler</strong>. Cellen är den minsta levande enheten.", "En bakterie är en enda cell. Det kallas <strong>encellig</strong>. En människa är byggd av miljarder celler. Det kallas <strong>flercellig</strong>.",
         "Virus är inte byggda av celler. De kan inte föröka sig själva. Därför räknas de oftast inte som levande."],
  kom="Allt levande är byggt av celler. Cellen är den minsta levande enheten.",
  ova=[("ringa", "Vad är den minsta levande enheten?", ["Cellen", "Hjärtat", "Kroppen"]),
       ("sf", "Kryssa i rätt ruta.", ["Alla levande varelser är byggda av celler.", "Virus räknas oftast som levande.", "En bakterie är en enda cell."]),
       ("fyll", ["celler", "encellig", "flercellig"], ["Allt levande är byggt av ______________.", "En bakterie är ______________.", "En människa är ______________."]),
       ("skriv", "Nämn två kännetecken på liv.", "Två kännetecken är", 2)]),

 dict(titel="Cellteorin och mikroskopet", prog="Delområde 2.1 · Cellteorin och mikroskopet",
  fore=["Celler är för små för att man ska se dem. År 1665 tittade Robert Hooke på kork i ett mikroskop. Han såg små rum som liknade vaxkakor. Han kallade dem <strong>celler</strong>.", "Senare forskare fann att alla växter och djur är byggda av celler. Det kallas <strong>cellteorin</strong>."],
  fig="kork.png", figw="80%",
  efter=["<strong>Cellteorin</strong> säger tre saker:", "<ol class='st'><li>Alla levande varelser består av celler.</li><li>Cellen är den minsta levande enheten.</li><li>Nya celler kommer från andra celler.</li></ol>",
         "Ett <strong>mikroskop</strong> förstorar. Du räknar ut förstoringen så här: <strong>okular × objektiv</strong>. Ett okular 10× och ett objektiv 40× ger 10 · 40 = <strong>400</strong> gånger förstoring."],
  fig2="l_mikroskop.png", fig2w="46%", n1=2,
  kom="Alla levande varelser består av celler. Förstoring = okular × objektiv.",
  ova=[("ringa", "Vem såg celler i kork år 1665?", ["Hooke", "Pasteur", "Darwin"]),
       ("kryssa", "Vad säger cellteorin? Kryssa i tre rutor.", ["Alla levande varelser består av celler.", "Celler kommer från andra celler.", "Bara djur har celler.", "Cellen är den minsta levande enheten."]),
       ("fyll", ["400", "okular", "mikroskop"], ["Ett ______________ förstorar små saker.", "Förstoring = ______________ × objektiv.", "10 × 40 = ______________."]),
       ("skriv", "Vad kallade Hooke de små rummen i korken?", "Han kallade dem", 1)]),

 dict(titel="Djurcell och växtcell", prog="Delområde 2.1 · Djurcell och växtcell",
  fore=["Inuti en cell finns små delar. Varje del har ett jobb. De kallas <strong>organeller</strong>.", "<strong>Cellkärnan</strong> har cellens DNA. <strong>Cellmembranet</strong> bestämmer vad som kommer in och ut. <strong>Mitokondrien</strong> gör energi. <strong>Cytoplasman</strong> fyller cellen."],
  fig="cellen-djurcell.png", figw="64%",
  efter=["Båda har cellmembran, cellkärna och mitokondrier. Växtceller har tre delar som djurceller saknar. <strong>Cellväggen</strong> ger stöd. <strong>Kloroplasterna</strong> gör fotosyntes. <strong>Vakuolen</strong> är en stor blåsa med vatten.", TB_FOREM],
  fig2="cellen-vaxtcell.png", fig2w="64%", n1=1,
  kom="Växtceller har cellvägg, kloroplaster och stor vakuol. Alla celler har cellmembran, cytoplasma och DNA.",
  ova=[("ringa", "Vilken del finns bara i växtceller?", ["Mitokondrie", "Kloroplast", "Cellkärna"]),
       ("streck", "Dra streck till rätt uppgift.", ["Cellkärnan", "Mitokondrien", "Kloroplasten"], ["gör energi", "gör fotosyntes", "har DNA"]),
       ("sf", "Kryssa i rätt ruta.", ["Djurceller har cellvägg.", "Växtceller har också mitokondrier.", "Alla växtceller har kloroplaster."]),
       ("skriv", "Varför har växtceller kloroplaster?", "De har kloroplaster eftersom", 2)]),

 dict(titel="Bakterier och encelliga organismer", prog="Delområde 2.1 · Bakterier och encelliga organismer",
  fore=["En <strong>bakterie</strong> är en cell utan cellkärna. DNA flyter fritt i cellen. Bakterier är mycket små."],
  fig="cellen-bakterie.png", figw="88%",
  efter=["Bakterier finns överallt: i jord, i vatten och i din tarm. De flesta bakterier är ofarliga eller nyttiga. Några orsakar sjukdom.", "Sjukdomar som beror på bakterier kan ibland behandlas med <strong>antibiotika</strong>. Antibiotika hjälper inte mot virus, till exempel en förkylning.",
         "Det finns också encelliga organismer med cellkärna. En amöba är ett exempel. Jäst är en encellig svamp."],
  kom="Bakterier är celler utan cellkärna. Antibiotika hjälper mot bakterier men inte mot virus.",
  ova=[("ringa", "Vad saknar en bakterie?", ["Cellkärna", "DNA", "Cellmembran"]),
       ("sf", "Kryssa i rätt ruta.", ["Alla bakterier är farliga.", "Antibiotika hjälper mot virus.", "Jäst är en encellig svamp."]),
       ("fyll", ["bakterier", "antibiotika", "encelliga"], ["Små celler utan cellkärna kallas ______________.", "Läkemedel mot bakterier heter ______________.", "En amöba och jäst är ______________ organismer."]),
       ("skriv", "Varför hjälper inte antibiotika mot en förkylning?", "Det hjälper inte eftersom", 2)]),

 dict(titel="Labb 2.1 Mikroskopera celler", prog="Delområde 2.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur ser en växtcell ut i ett mikroskop?", "Du behöver: mikroskop, objektglas, täckglas, pincett, pipett, vatten och jodlösning. Läraren har skurit ut en lökbit."],
  fig=None,
  efter=["<ol class='st'><li>Dra loss ett tunt skinn från insidan av ett lökblad med pincetten.</li><li>Lägg skinnet plant på ett objektglas. Droppa på en droppe jodlösning.</li><li>Sänk ett täckglas över preparatet. Gör det långsamt så att inga luftbubblor fastnar.</li><li>Titta först med lägsta förstoring. Sedan med högre.</li><li>Rita en cell. Skriv vad du ser. Skriv förstoringen.</li></ol>",
         "<strong>Säkerhet:</strong> Mikroskop och glas hanteras varsamt. Läraren använder kniven. Tvätta händerna efteråt."],
  kom="Lökceller har cellvägg och cellkärna. De saknar kloroplaster eftersom löken växer under jord.",
  ova=[("fyll", ["cellvägg", "cellkärnan", "förstoringen"], ["Jodet färgar ______________ brun.", "Lökceller har en tydlig ______________.", "Skriv alltid ______________ under teckningen."]),
       ("rita", "Rita en lökcell. Skriv namn på delarna du ser."),
       ("skriv", "Vilka delar kunde du se?", "Jag kunde se", 2),
       ("skriv", "Lökcellerna saknar kloroplaster. Varför tror du det?", "Det beror på att", 2)]),

 dict(titel="Växten som producent", prog="Delområde 2.2 · Växten som producent",
  fore=["Växter gör egen mat. Det kallas <strong>fotosyntes</strong>. Växten är en <strong>producent</strong>.", "Växten behöver tre saker: <strong>koldioxid</strong> från luften, <strong>vatten</strong> från jorden och <strong>ljus</strong> från solen."],
  fig="l_foto.png", figw="80%",
  efter=["Då bildas <strong>glukos</strong> och <strong>syre</strong>. Glukos är druvsocker. Syret släpps ut i luften.", "<strong>koldioxid + vatten + ljus → glukos + syre</strong>",
         "Fotosyntesen sker i <strong>kloroplasterna</strong>. De är gröna av klorofyll. Klorofyll fångar ljuset.", "Växten använder glukosen som energi och till att växa. Det som blir över lagras, till exempel som stärkelse i potatis."],
  kom="Fotosyntes: koldioxid + vatten + ljus blir glukos + syre. Den sker i kloroplasterna.",
  ova=[("ringa", "Vad bildas vid fotosyntes?", ["Glukos och syre", "Koldioxid och vatten", "Energi och värme"]),
       ("fyll", ["kloroplasterna", "koldioxid", "producent"], ["Fotosyntesen sker i ______________.", "Växten tar in ______________ från luften.", "En växt kallas ______________ eftersom den gör egen mat."]),
       ("sf", "Kryssa i rätt ruta.", ["Växter behöver ljus för fotosyntes.", "Växter får sin mat från jorden.", "Syre bildas vid fotosyntes."]),
       ("skriv", "Vad kan växten göra med glukosen?", "Växten kan", 2)]),

 dict(titel="Cellandning", prog="Delområde 2.2 · Cellandning",
  fore=["Alla celler behöver energi. Energin finns i glukos. Cellen tar ut energin i <strong>cellandningen</strong>.", "Cellandningen sker i <strong>mitokondrierna</strong>."],
  fig="l_andning.png", figw="78%",
  efter=["<strong>glukos + syre → koldioxid + vatten + energi</strong>", "Nästan alla levande celler gör cellandning. Det gör både djur och växter. Växter gör den dag och natt.",
         "Cellandning är inte samma sak som att andas med lungorna. Lungorna tar in syre. Syret används i cellerna.",
         "Jäst kan få energi utan syre. Det kallas <strong>jäsning</strong>. Då bildas koldioxid och alkohol. Jästens koldioxid gör att bröd jäser."],
  kom="Cellandning: glukos + syre blir koldioxid + vatten + energi. Den sker i mitokondrierna i nästan alla celler.",
  ova=[("ringa", "Var sker cellandningen?", ["I mitokondrierna", "I cellväggen", "I lungorna"]),
       ("fyll", ["energi", "syre", "mitokondrierna"], ["Glukos och ______________ används i cellandningen.", "Cellen får ______________ från cellandningen.", "Cellandning sker i ______________."]),
       ("sf", "Kryssa i rätt ruta.", ["Växter gör cellandning.", "Cellandning sker bara i lungorna.", "Cellandning ger koldioxid."]),
       ("skriv", "Vad bildas när celler gör cellandning?", "Det bildas", 2)]),

 dict(titel="Processerna tillsammans", prog="Delområde 2.2 · Processerna tillsammans",
  fore=["Fotosyntes och cellandning är varandras motsatser. Det som bildas i den ena används i den andra.", TB_PROC],
  fig="cellen-fotosyntes.png", figw="80%",
  efter=["En växt gör fotosyntes när det är ljust. Den gör <em>också</em> cellandning hela tiden, även på natten.", "Kolet går runt i ett <strong>kretslopp</strong>. Fotosyntesen tar in koldioxid. Cellandningen släpper ut koldioxid.",
         "Energin går inte runt. Den kommer från solen och blir till värme. Därför behöver livet ny energi hela tiden."],
  kom="Fotosyntes och cellandning är motsatser. Kolet går runt. Energin går inte runt.",
  ova=[("streck", "Dra streck till rätt process.", ["Fotosyntes", "Cellandning"], ["glukos + syre blir energi", "ljus och koldioxid blir glukos"]),
       ("sf", "Kryssa i rätt ruta.", ["Växter gör cellandning på natten.", "Växter gör aldrig cellandning.", "Fotosyntesen behöver ljus."]),
       ("ringa", "Vad går inte runt i ett kretslopp?", ["Energi", "Kol", "Syre"]),
       ("skriv", "Hur är fotosyntes och cellandning motsatser?", "De är motsatser eftersom", 3)]),

 dict(titel="Labb 2.2 Jäst och koldioxid", prog="Delområde 2.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur påverkar temperaturen hur mycket koldioxid jäst bildar?", "Du behöver: fyra flaskor med ballonger, jäst, socker, vatten, termometer, måttband och klocka."],
  fig=None,
  efter=["<ol class='st'><li>Ställ fyra vattenbad: kallt (ca 5 °C), rumsvarmt (ca 20 °C), ljummet (ca 35 °C) och varmt (ca 50 °C).</li><li>Häll 1 tsk jäst, 1 tsk socker och 1 dl ljummet vatten i varje flaska.</li><li>Sätt en ballong på varje flaska. Ställ flaskorna i baden.</li><li>Mät ballongens omkrets efter 5, 10 och 15 minuter. Fyll i tabellen.</li></ol>", TB_JAST,
         "<strong>Säkerhet:</strong> Använd inte hett vatten. Högst ca 50 °C. Torka upp spill. Ät inte jästen. Tvätta händerna."],
  kom="Jäst bildar koldioxid. Temperaturen påverkar hur mycket.",
  ova=[("fyll", ["koldioxid", "ballongen", "temperaturen"], ["Jästen bildar gasen ______________.", "Gasen fyller ______________.", "Vi ändrar ______________ i försöket."]),
       ("ringa", "Vilken sak ska vara lika i alla flaskor?", ["Mängden jäst", "Temperaturen", "Ballongens omkrets"]),
       ("skriv", "Vid vilken temperatur blev ballongen störst?", "Den blev störst vid", 1),
       ("skriv", "Varför ska man ha lika mycket jäst i alla flaskor?", "Det ska man eftersom", 2)]),

 dict(titel="Specialiserade celler och vävnader", prog="Delområde 2.3 · Specialiserade celler och vävnader",
  fore=["Hos flercelliga varelser har cellerna olika jobb. De kallas <strong>specialiserade celler</strong>. De har en form som passar jobbet."],
  fig="spec-celler.png", figw="92%",
  efter=["Muskelceller drar ihop sig. Nervceller skickar signaler. Röda blodkroppar transporterar syre. Rothårsceller tar upp vatten.",
         "Många lika celler som arbetar ihop bildar en <strong>vävnad</strong>, till exempel muskelvävnad. Flera vävnader bildar ett <strong>organ</strong>, till exempel hjärtat."],
  fig2="cellen-nivaer.png", fig2w="92%", n1=2,
  kom="Celler blir vävnader. Vävnader blir organ. Organ blir organsystem.",
  ova=[("ringa", "Vilken cell skickar signaler?", ["Nervcell", "Röd blodkropp", "Rothårscell"]),
       ("siffror", "Sätt nivåerna i ordning från minst till störst. Skriv 1, 2, 3 och 4.", ["Organ", "Cell", "Organism", "Vävnad"]),
       ("streck", "Dra streck till rätt jobb.", ["Muskelcell", "Röd blodkropp", "Rothårscell"], ["tar upp vatten", "drar ihop sig", "transporterar syre"]),
       ("skriv", "Varför har celler olika form?", "De har olika form eftersom", 2)]),

 dict(titel="Kroppens organsystem – översikt", prog="Delområde 2.3 · Kroppens organsystem – översikt",
  fore=["Flera organ som arbetar ihop bildar ett <strong>organsystem</strong>. Alla organsystem tillsammans bildar en <strong>organism</strong>, till exempel en människa.", TB_SYST],
  fig="cellen-samarbete.png", figw="84%",
  efter=["Alla celler behöver glukos och syre. De måste också bli av med koldioxid och avfall.", "Organsystemen hjälps åt. Matsmältningen tar upp glukos. Lungorna tar in syre. Blodet transporterar. Njurarna renar blodet.", "Allt som kroppen gör hjälper cellerna."],
  kom="Organsystemen samarbetar. Allt kroppen gör hjälper cellerna.",
  ova=[("ringa", "Vad är ett organsystem?", ["Organ som arbetar ihop", "En enda cell", "Ett enda organ"]),
       ("streck", "Dra streck till rätt uppgift.", ["Matsmältningen", "Andningen", "Cirkulationen"], ["tar in syre", "transporterar med blodet", "bryter ner maten"]),
       ("fyll", ["blodet", "syre", "glukos"], ["Lungorna tar in ______________.", "Tunntarmen tar upp ______________.", "______________ transporterar ämnena till cellerna."]),
       ("skriv", "Varför behöver cellerna blodet?", "Cellerna behöver blodet eftersom", 2)]),
]
VIKTIGAST = [("l_ic1.png", "Allt levande är byggt av celler. Cellen är den minsta levande enheten. Förstoring = okular × objektiv."),
             ("l_ic2.png", "Växter gör fotosyntes i kloroplasterna: koldioxid + vatten + ljus blir glukos + syre."),
             ("l_ic3.png", "Cellandning i mitokondrierna: glukos + syre blir koldioxid + vatten + energi. Alla celler gör den."),
             ("l_ic4.png", "Fotosyntes och cellandning är motsatser. Kolet går runt. Energin går inte runt."),
             ("l_ic5.png", "Celler blir vävnader, organ och organsystem. Organsystemen hjälps åt att ge cellerna det de behöver."),
             (None, "Bakterier är celler utan cellkärna. Antibiotika hjälper mot bakterier men inte mot virus.")]
TEST = [("ringa", "Vilken del finns bara i växtceller?", ["Mitokondrie", "Cellkärna", "Kloroplast"]),
        ("streck", "Dra streck till rätt förklaring.", ["Mitokondrie", "Kloroplast", "Cellkärna", "Cellvägg"], ["har DNA", "ger stöd i växtceller", "gör fotosyntes", "gör energi"]),
        ("sf", "Kryssa i rätt ruta.", ["Fotosyntes sker i mitokondrierna.", "Växter gör cellandning dag och natt.", "Bakterier har cellkärna.", "Cellen är den minsta levande enheten.", "Antibiotika hjälper mot virus.", "Förstoring = okular × objektiv."]),
        ("fyll", ["koldioxid", "glukos", "syre"], ["Fotosyntes: ______________ + vatten + ljus blir glukos + syre.", "Cellandning: ______________ + syre blir koldioxid + vatten + energi."]),
        ("siffror", "Sätt i ordning från minst till störst. Skriv 1, 2, 3 och 4.", ["Organsystem", "Vävnad", "Cell", "Organ"]),
        ("skriv", "Varför behöver en växt både kloroplaster och mitokondrier?", "Växten behöver båda eftersom", 3),
        ("ringa", "Ett mikroskop har okular 10× och objektiv 10×. Hur stor är förstoringen?", ["10 gånger", "100 gånger", "1 000 gånger"]),
        ("skriv", "Varför hjälper organsystemen cellerna?", "De hjälper cellerna eftersom", 2)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 2 (Cellen och livets processer): kännetecken på liv, cellteorin och mikroskop, skillnader mellan djurcell, växtcell och bakterie, "
                "fotosyntes och cellandning i ord, hur de hänger ihop samt hur celler bildar vävnader, organ och organsystem. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå. Kopplingarna framåt görs i kapitel 4 (kolets kretslopp) och kapitel 6–7 (organsystemen).")
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "11 delar (start, sju moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Kom ihåg-ruta i varje del med det viktigaste i en mening.", "Övningar direkt efter varje del: ringa in, dra streck, fyll i med ordbank, sant/falskt, kryssa och skriv med meningsstart.",
                "Labbarna är skrivna så att de går att göra med enkel utrustning."]
HANDLEDNING_HTML = """
<h3>Handledning per moment</h3>
<h3 class="mm">Start. Vad är liv?</h3><p class="hl"><b>Mål:</b> eleven nämner kännetecken på liv och vet att cellen är den minsta levande enheten. <b>Tips:</b> låt eleverna först skriva en egen lista och jämföra efteråt. Virus är ett bra gränsfall att diskutera.</p>
<h3 class="mm">Cellteorin och mikroskopet</h3><p class="hl"><b>E-mål:</b> eleven återger vad cellteorin säger och räknar ut förstoring. <b>Vanligt fel:</b> eleverna glömmer att multiplicera okular och objektiv.</p>
<h3 class="mm">Djurcell och växtcell</h3><p class="hl"><b>E-mål:</b> eleven namnger cellens delar och deras uppgifter och skiljer djur- från växtcell. <b>Vanligt fel:</b> ”växtceller har inga mitokondrier”.</p>
<h3 class="mm">Bakterier och encelliga organismer</h3><p class="hl"><b>E-mål:</b> eleven vet att bakterier saknar cellkärna och att antibiotika inte verkar mot virus. <b>Vanligt fel:</b> ”alla bakterier är farliga” och ”virus är bakterier”.</p>
<h3 class="mm">Labb 2.1 Mikroskopera celler</h3><p class="hl"><b>Material:</b> mikroskop, objektglas, täckglas, pincett, jodlösning, lök. <b>Förväntat:</b> rektangulära celler med cellvägg och brunfärgad cellkärna. <b>Vanliga fel:</b> veckat skinn, luftbubblor, för tjockt preparat. Läraren använder kniven.</p>
<h3 class="mm">Växten som producent</h3><p class="hl"><b>E-mål:</b> eleven anger ämnen in och ut vid fotosyntes. <b>Vanligt fel:</b> ”växter får sin mat från jorden”.</p>
<h3 class="mm">Cellandning</h3><p class="hl"><b>E-mål:</b> eleven anger ämnen in och ut vid cellandning och vet att den sker i mitokondrierna. <b>Vanligt fel:</b> att cellandning är detsamma som lungandning.</p>
<h3 class="mm">Processerna tillsammans</h3><p class="hl"><b>E-mål:</b> eleven jämför processerna och vet att växter gör cellandning hela tiden. <b>Vanligt fel:</b> ”växter andas bara på natten”.</p>
<h3 class="mm">Labb 2.2 Jäst och koldioxid</h3><p class="hl"><b>Material:</b> fyra flaskor med ballonger, jäst, socker, termometer, måttband. <b>Förväntat:</b> mest gas vid ljummet vatten, minst i kyla, ofta mindre vid 50 °C. Resultaten varierar. <b>Vanliga fel:</b> olika mängd jäst, ballongen sätts på för sent.</p>
<h3 class="mm">Specialiserade celler och vävnader</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på specialiserade celler och ordnar nivåerna cell, vävnad, organ. <b>Vanligt fel:</b> att nivåerna blandas ihop.</p>
<h3 class="mm">Kroppens organsystem – översikt</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på organsystem och deras uppgifter. Koppla till cellens behov av glukos och syre.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Cellen. 2) Sant, falskt, sant. 3) celler, encellig, flercellig. 4) T.ex. celler, energi, växer, förökar sig, reagerar.",
 "<b>Cellteorin och mikroskopet:</b> 1) Hooke. 2) Alla levande varelser består av celler. Celler kommer från andra celler. Cellen är den minsta levande enheten. 3) mikroskop, okular, 400. 4) Celler.",
 "<b>Djurcell och växtcell:</b> 1) Kloroplast. 2) Cellkärnan – har DNA; Mitokondrien – gör energi; Kloroplasten – gör fotosyntes. 3) Falskt, sant, falskt. 4) De gör fotosyntes.",
 "<b>Bakterier och encelliga organismer:</b> 1) Cellkärna. 2) Falskt, falskt, sant. 3) bakterier, antibiotika, encelliga. 4) Förkylning beror på virus. Antibiotika verkar bara mot bakterier.",
 "<b>Labb 2.1:</b> 1) cellkärnan, cellvägg, förstoringen. 2) Egen teckning. 3) T.ex. cellvägg och cellkärna. 4) Löken växer under jord och behöver inte fotosyntes.",
 "<b>Växten som producent:</b> 1) Glukos och syre. 2) kloroplasterna, koldioxid, producent. 3) Sant, falskt, sant. 4) Använda den som energi, växa eller lagra den.",
 "<b>Cellandning:</b> 1) I mitokondrierna. 2) syre, energi, mitokondrierna. 3) Sant, falskt, sant. 4) Koldioxid, vatten och energi.",
 "<b>Processerna tillsammans:</b> 1) Fotosyntes – ljus och koldioxid blir glukos; Cellandning – glukos + syre blir energi. 2) Sant, falskt, sant. 3) Energi. 4) Det som bildas i den ena används i den andra.",
 "<b>Labb 2.2:</b> 1) koldioxid, ballongen, temperaturen. 2) Mängden jäst. 3) Egna resultat, oftast ca 35 °C. 4) För att bara temperaturen ska skilja mellan flaskorna.",
 "<b>Specialiserade celler och vävnader:</b> 1) Nervcell. 2) Cell 1, Vävnad 2, Organ 3, Organism 4. 3) Muskelcell – drar ihop sig; Röd blodkropp – transporterar syre; Rothårscell – tar upp vatten. 4) Formen passar jobbet.",
 "<b>Kroppens organsystem:</b> 1) Organ som arbetar ihop. 2) Matsmältningen – bryter ner maten; Andningen – tar in syre; Cirkulationen – transporterar med blodet. 3) syre, glukos, blodet. 4) Blodet transporterar glukos och syre till cellerna och för bort koldioxid.",
 "<b>Testa dig:</b> 1) Kloroplast. 2) Mitokondrie – gör energi; Kloroplast – gör fotosyntes; Cellkärna – har DNA; Cellvägg – ger stöd i växtceller. 3) Falskt, sant, falskt, sant, falskt, sant. 4) koldioxid, glukos. 5) Cell 1, Vävnad 2, Organ 3, Organsystem 4. 6) Kloroplasterna gör glukos. Mitokondrierna använder glukosen för att få energi. 7) 100 gånger. 8) De ger cellerna glukos och syre och för bort avfall.",
]

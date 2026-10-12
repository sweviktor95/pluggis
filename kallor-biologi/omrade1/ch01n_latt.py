# -*- coding: utf-8 -*-
"""Område 1 Biologi som vetenskap – lättläst version (nya ramverket, byggd per moment)."""
FIG = '/tmp/bio/fig01n/'
NR = 1
SLUG = "vetenskap"
TAB = "1"
NAMN = "Biologi som vetenskap"
NDEL = 9
UNDER = "Hur vet vi det vi vet om livet?"
INTRO_L = ["I det här kapitlet lär du dig hur forskare tar reda på saker.",
           "Du lär dig göra egna undersökningar. Du lär dig också att kolla om något är sant.",
           "Namn och siffror i exemplen är påhittade. Forskarna Pasteur, Semmelweis, Marshall och Warren är riktiga."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Delområde 1.1 Undersöka systematiskt: fråga, plan, tabell, diagram och slutsats",
        "Delområde 1.2 Modeller, källor och argument: vad vetenskap kan pröva, hur forskare har ändrat sig och hur du kollar en källa"]
ORD_FIG = None
ORD_EXTRA = [("biologi", "läran om allt som lever"), ("organism", "allt som lever, till exempel djur, växter och bakterier"),
             ("undersökningsbar fråga", "en fråga du kan svara på genom att mäta eller titta"), ("hypotes", "det man tror blir svaret, och varför"),
             ("variabel", "något som kan ändras eller mätas"), ("rättvist test", "man ändrar bara en sak. Allt annat är lika"),
             ("tabell", "ett sätt att skriva ner det man mäter"),
             ("diagram", "en bild av siffror, till exempel staplar"),
             
             ("resultat", "det man mäter eller ser"), ("slutsats", "det man lär sig av resultatet"),
             ("felkälla", "något som kan göra att resultatet blir fel"), ("slump", "något som händer av en tillfällighet"),
             ("påstående", "något man säger är sant"), ("belägg", "mätningar eller observationer som visar något"),
             ("åsikt", "vad någon tycker. Går inte att mäta"), ("pseudovetenskap", "låter som vetenskap men saknar belägg"),
             ("modell", "ett sätt att förklara hur något fungerar"), ("mikroorganism", "en mycket liten organism, till exempel en bakterie"),
             ("källa", "där informationen kommer ifrån"), ("trovärdig", "går att lita på"), ("relevant", "passar min fråga"),
             ("avsändare", "den som har skrivit eller gjort texten")]

TB_ELLA = ('<table class="tb"><tr><th>Ella ändrar</th><th>Ella mäter</th><th>Ella håller lika</th></tr>'
           '<tr><td>ljuset (ljus eller mörker)</td><td>hur hög krassen blir (mm)</td><td>jord, vatten, antal frön</td></tr></table>')
TB_FRAGA = ('<table class="tb"><tr><th>Går inte att undersöka</th><th>Går att undersöka</th></tr>'
            '<tr><td>Är solrosor fina?</td><td>Hur mycket växer en solros på en vecka?</td></tr>'
            '<tr><td>Är musik bra när man pluggar?</td><td>Kommer man ihåg fler ord efter att ha lyssnat på musik?</td></tr></table>')
TB_MAT = ('<table class="tb"><tr><th>Dag</th><th>Ljus (mm)</th><th>Mörker (mm)</th></tr>'
          '<tr><td class="n">1</td><td class="n">5</td><td class="n">5</td></tr><tr><td class="n">3</td><td class="n">15</td><td class="n">25</td></tr>'
          '<tr><td class="n">5</td><td class="n">28</td><td class="n">42</td></tr><tr><td class="n">7</td><td class="n">40</td><td class="n">60</td></tr></table>')
TB_FEL = ('<table class="tb"><tr><th>Felkälla</th><th>Exempel</th></tr>'
          '<tr><td>Slump</td><td>Man läser av linjalen lite olika varje gång.</td></tr>'
          '<tr><td>Misstag</td><td>Man mäter från fel ställe på linjalen.</td></tr>'
          '<tr><td>Olika villkor</td><td>Den ena krassen får mer vatten.</td></tr></table>')
TB_PROVA = ('<table class="tb"><tr><th>Påstående</th><th>Går det att pröva?</th></tr>'
            '<tr><td>Vatten fryser vid 0 °C.</td><td>Ja. Man kan mäta temperaturen.</td></tr>'
            '<tr><td>Hundar har bättre luktsinne än människor.</td><td>Ja. Man kan testa det.</td></tr>'
            '<tr><td>Katter är gulligare än hundar.</td><td>Nej. Det är en åsikt.</td></tr>'
            '<tr><td>Ditt stjärntecken bestämmer hur du är.</td><td>Ja. Det är prövat. Det finns inga belägg.</td></tr></table>')
TB_RAKNA = ('<table class="tb"><tr><th>Fallsträcka (cm)</th><th>Reaktionstid (s)</th></tr>'
            '<tr><td class="n">5</td><td class="n">0,10</td></tr><tr><td class="n">10</td><td class="n">0,14</td></tr>'
            '<tr><td class="n">15</td><td class="n">0,17</td></tr><tr><td class="n">20</td><td class="n">0,20</td></tr>'
            '<tr><td class="n">25</td><td class="n">0,23</td></tr><tr><td class="n">30</td><td class="n">0,25</td></tr></table>')
TB_REP = ('<ol class="st"><li><b>Fråga.</b> Vad ville vi ta reda på?</li><li><b>Så gjorde vi.</b> Vad ändrade vi? Vad mätte vi? Vad höll vi lika?</li>'
          '<li><b>Resultat.</b> Tabell och diagram.</li><li><b>Slutsats.</b> Svara på frågan. Skriv vad som kan ha blivit fel.</li></ol>')
TB_CHECK = ('<table class="tb"><tr><th>Fråga om källan</th><th>Bra tecken</th></tr>'
            '<tr><td>Vem har skrivit?</td><td>Forskare, myndighet eller en känd organisation</td></tr>'
            '<tr><td>Varför är det skrivet?</td><td>Att informera. Inte att sälja</td></tr>'
            '<tr><td>Finns det belägg?</td><td>Mätningar, undersökningar eller länkar till forskning</td></tr>'
            '<tr><td>Är det nytt?</td><td>Skrivet för inte så länge sedan</td></tr>'
            '<tr><td>Säger andra källor samma sak?</td><td>Ja, minst två till</td></tr></table>')
ARG = ('<div class="arg"><b class="h">SÅ ARGUMENTERAR DU</b>1. <b>Påstående:</b> Jag tycker att …<br>2. <b>Belägg:</b> Jag tycker det eftersom …<br>'
       '3. <b>Motargument:</b> Någon kan säga att … Men …<br>4. <b>Slutsats:</b> Alltså …</div>')

DELOMR = {"1.1": "Undersöka systematiskt", "1.2": "Modeller, källor och argument"}
DELAR = [
 dict(titel="Vad är biologi?", prog="Start · Vad är biologi?",
  fore=["Biologi är läran om allt som lever.", "Allt som lever kallas <strong>organismer</strong>. Djur, växter, svampar och bakterier är organismer.", "Biologer forskar om organismer. De forskar också om människans kropp.", "Det finns många sorters biologer. Här är fyra:"],
  fig="l_yrken.png",
  efter=["Biologer arbetar ute i naturen eller inne i ett labb.", "Många biologer hjälper till att skydda naturen eller att göra nya mediciner."],
  kom="Biologi är läran om allt som lever. Allt som lever kallas organismer.",
  ova=[("ringa", "Vad är en organism?", ["Allt som lever", "En sten", "Ett tal"]),
       ("streck", "Vad forskar biologerna om? Dra streck.", ["Zoolog", "Botaniker", "Marinbiolog", "Mikrobiolog"], ["växter", "små organismer, som bakterier", "djur", "livet i havet"]),
       ("fyll", ["labb", "naturen", "kropp"], ["Biologer kan arbeta ute i ______________.", "Biologer kan också arbeta inne i ett ______________.", "Biologer forskar också om människans ______________."])]),

 dict(titel="Från fråga till plan", prog="Delområde 1.1 · Från fråga till plan",
  fore=["Forskare börjar med en fråga. Men alla frågor går inte att undersöka.", "En fråga som går att undersöka kallas en <strong>undersökningsbar fråga</strong>. Man kan svara på den genom att <strong>mäta</strong> eller <strong>titta</strong>."] + [TB_FRAGA]
       + ["Sedan gissar forskaren vad svaret blir. Det kallas en <strong>hypotes</strong>. Man skriver också varför man tror det.", "Forskare arbetar i steg. Stegen går runt i en cirkel."],
  fig="l_cykel.png",
  efter=["<span class='fake'>Påhittat exempel</span> Ella undrar: <em>Växer krasse bättre i ljus eller i mörker?</em>", "Hypotes: <em>Krassen blir högst i ljus, eftersom växter behöver ljus.</em>", "Hon gör ett <strong>rättvist test</strong> med två lådor.",
         "Ella ändrar bara en sak: ljuset. Allt annat är lika. Det man ändrar kallas en <strong>variabel</strong>.", TB_ELLA,
         "<h3>Säkert i labbet</h3>", "Läs hela instruktionen först. Ha skyddsglasögon när läraren säger det. Ät och drick aldrig i labbet. Fråga om du är osäker."],
  fig2="l_krasse.png",
  kom="En fråga som går att undersöka kan man mäta. I ett rättvist test ändrar man bara en sak.",
  ova=[("ringa", "Vilken fråga går att undersöka?", ["Är hundar snälla?", "Hur långt hoppar en groda?", "Är sommar bäst?"]),
       ("streck", "Dra streck till rätt förklaring.", ["Det Ella ändrar", "Det Ella mäter", "Det som är lika"], ["hur hög krassen blir", "jord och vatten", "ljuset"]),
       ("kryssa", "Vad ska vara lika i båda lådorna? Kryssa i rätt rutor.", ["Samma jord", "Lika mycket vatten", "Samma ljus", "Lika många frön"]),
       ("kryssa", "Vad gör du i labbet? Kryssa i rätt rutor.", ["Läser hela instruktionen först", "Äter godis", "Frågar om jag är osäker", "Springer runt"]),
       ("skriv", "Varför ska man bara ändra en sak i ett test?", "Man ska bara ändra en sak eftersom", 2)]),

 dict(titel="Dokumentera", prog="Delområde 1.1 · Dokumentera",
  fore=["När du mäter ska du skriva ner värdena direkt. Använd en <strong>tabell</strong>.", "Tabellen ska ha rubriker. Skriv också enhet, till exempel mm eller s.", "<span class='fake'>Påhittade siffror</span> Så här kan Ellas tabell se ut:", TB_MAT],
  fig="l_stapel.png", figw="55%",
  efter=["Ett <strong>diagram</strong> gör siffrorna lätta att jämföra. Ella ritar ett stapeldiagram.", "Ett bra diagram har <strong>rubrik</strong>. Axlarna har namn och enhet. Staplarna har namn.",
         "<h3>Så skriver du en rapport</h3>", TB_REP],
  kom="Skriv värdena i en tabell med rubriker och enheter. Rita ett diagram med rubrik och axlar.",
  ova=[("ringa", "Vad ska stå i tabellens rubrik?", ["Höjd (mm)", "Bara en siffra", "Inget"]),
       ("rita", "Rita ett stapeldiagram: Grupp A 12 cm, Grupp B 8 cm. Skriv rubrik och namn på axlarna."),
       ("siffror", "Sätt delarna av rapporten i rätt ordning. Skriv 1, 2, 3 och 4.", ["Slutsats", "Fråga", "Resultat", "Så gjorde vi"]),
       ("fyll", ["tabell", "rubrik", "enhet"], ["Man skriver värdena i en ______________.", "Ett diagram ska ha en ______________.", "Efter siffran skriver man en ______________, till exempel mm."])]),

 dict(titel="Värdera", prog="Delområde 1.1 · Värdera",
  fore=["Ett resultat kan bli fel. Det beror på <strong>felkällor</strong>.", TB_FEL, "<strong>Slump</strong> är sådant som bara händer. Därför gör man om testet flera gånger. Då blir resultatet säkrare."],
  fig="l_stapel.png", figw="55%",
  efter=["Slutsatsen ska stämma med resultatet.", "<strong>Ellas slutsats:</strong> Krassen blir högre i mörker. Den växer på höjden för att leta efter ljus. Men den mår bäst i ljus.",
         "Hypotesen var alltså fel. Det gör inget! Man lär sig ändå.", "Ella testade bara krasse. Hon kan inte säga att alla växter gör så. Skriv alltid vad du inte vet."],
  kom="Resultatet kan bli fel. Gör om testet flera gånger. Slutsatsen ska stämma med resultatet.",
  ova=[("ringa", "En fläkt blåser på en av krassarna. Vad är det?", ["En felkälla", "En slutsats", "En hypotes"]),
       ("sf", "Kryssa i rätt ruta.", ["Man kan få fel resultat av slump.", "Det är dåligt om hypotesen var fel.", "Det är bra att göra testet flera gånger."]),
       ("fyll", ["slutsatsen", "felkälla", "flera"], ["Något som kan ge fel resultat kallas en ______________.", "Man gör testet ______________ gånger.", "______________ ska stämma med resultatet."]),
       ("skriv", "Varför är det bra att göra ett test flera gånger?", "Det är bra eftersom", 2)]),

 dict(titel="Labb 1.1 Reaktionstid", prog="Delområde 1.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Hur snabb är din reaktion? Vi mäter med en fallande linjal.", "Ni är två och två. Ni behöver en linjal på 30 cm och en penna.", "Ni gör på samma sätt varje gång: samma linjal, samma hand och fem försök. Då blir testet rättvist."],
  fig="v_linjal.png", figw="48%",
  efter=["<ol class='st'><li>Din kompis håller linjalen lodrätt. Noll ska vara vid din tumme och pekfinger.</li><li>Kompisen släpper linjalen utan att säga till.</li><li>Du fångar den så fort du kan.</li><li>Läs av var du fångade linjalen. Skriv ner centimeter.</li><li>Gör fem försök. Byt sedan plats.</li></ol>",
         "<h3>Räkna om till tid</h3>", TB_RAKNA, "<strong>Säkerhet:</strong> Sitt eller stå stadigt. Skriv bara ner ditt eget värde. Du behöver inte visa det för alla."],
  kom="Fallsträckan visar din reaktionstid. Gör flera försök och skriv i en tabell.",
  ova=[("fyll", ["cm", "fem", "tabell"], ["Jag gör ______________ försök.", "Jag skriver värdena i en ______________.", "Jag mäter fallsträckan i ______________."]),
       ("rita", "Rita ett stapeldiagram över dina fem försök. Skriv rubrik och namn på axlarna."),
       ("skriv", "Vad blev din slutsats? Svara på frågan: Hur snabb är din reaktion?", "Min reaktionstid var ungefär", 2),
       ("skriv", "Nämn en felkälla. Vad kunde ha blivit fel?", "En felkälla är", 2)]),

 dict(titel="Vad kan vetenskap pröva?", prog="Delområde 1.2 · Vad kan vetenskap pröva?",
  fore=["Ett <strong>påstående</strong> är något man säger är sant.", "Vetenskap kan pröva ett påstående om det går att mäta eller titta. Det man mäter eller ser kallas <strong>belägg</strong>.", "En <strong>åsikt</strong> är vad någon tycker. Åsikter går inte att mäta. Därför kan vetenskapen inte pröva dem.", TB_PROVA],
  fig=None,
  efter=["<h3>Pseudovetenskap</h3>", "Ibland låter något som vetenskap, men det finns inga belägg. Det kallas <strong>pseudovetenskap</strong>.", "Horoskopet säger att ditt stjärntecken styr hur du är. Forskare har testat det. De har inte hittat belägg."],
  kom="Vetenskap prövar påståenden med belägg. Åsikter går inte att pröva.",
  ova=[("kryssa", "Vilka påståenden går att pröva? Kryssa i rätt rutor.", ["Kaniner springer fortare än sköldpaddor.", "Rött är den finaste färgen.", "Vatten kokar vid 100 °C.", "Pizza är godast."]),
       ("ringa", "Vad är belägg?", ["Mätningar och observationer", "Vad någon tycker", "En gissning utan test"]),
       ("fyll", ["belägg", "åsikt", "pseudovetenskap"], ["Mätningar som visar något kallas ______________.", "Det man tycker kallas en ______________.", "Det som låter som vetenskap men saknar belägg kallas ______________."]),
       ("skriv", "Hur kan man pröva påståendet: Hundar har bättre luktsinne än människor?", "Man kan", 2)]),

 dict(titel="När forskare ändrat sig", prog="Delområde 1.2 · När forskare ändrat sig",
  fore=["Forskare förklarar hur saker fungerar. En förklaring kallas en <strong>modell</strong>.", "Om nya undersökningar visar något annat, ändrar forskarna modellen. Här är tre exempel."],
  sub1=("Pasteur och kolven (1861)", ["Förr trodde många att <strong>mikroorganismer</strong>, alltså mycket små organismer, kunde uppstå av sig själva i mat.", "Pasteur kokade buljong i en kolv med lång böjd hals. Damm fastnade i böjen. Buljongen förblev klar.", "Slutsats: små organismer kommer utifrån. De uppstår inte av sig själva."], "v_pasteur.png"),
  sub2=("Semmelweis och händerna (1847)", ["I Wien dog många mammor efter förlossningen i barnsängsfeber. Det dog fler på läkarklinikens avdelning än på barnmorskornas.", "Läkarna hade rört vid döda kroppar. Semmelweis trodde att något följde med händerna. Från 1847 skulle alla tvätta händerna i klorkalklösning.", "Dödligheten sjönk från 11,4 % till 1,3 %. Men många läkare trodde inte på honom."], "f_semmelweis2.png"),
  sub3=("Marshall, Warren och magsåren (1982)", ["Förr trodde man att magsår kom av stress och livsstil.", "Marshall och Warren hittade en bakterie i magsäcken, <em>Helicobacter pylori</em>. Många trodde inte på dem.", "År 1984 drack Marshall själv bakterier och fick en inflammation i magsäcken. Gör aldrig så själv! Idag botas magsår med antibiotika och medicin som minskar syran. De fick Nobelpriset 2005."], "f_hpylori.png"),
  subw="50%", efter=[],
  kom="En modell kan ändras när nya undersökningar visar något annat.",
  ova=[("streck", "Vem upptäckte vad? Dra streck.", ["Pasteur", "Semmelweis", "Marshall och Warren"], ["handtvätt minskar dödsfall", "magsår kommer av en bakterie", "små organismer kommer utifrån"]),
       ("ringa", "Vad hände med dödligheten efter handtvätten?", ["Den sjönk", "Den steg", "Den blev lika"]),
       ("fyll", ["modell", "belägg", "bakterie"], ["En förklaring kallas en ______________.", "Marshall och Warren hittade en ______________ i magsäcken.", "Forskare ändrar sig när de får nya ______________."]),
       ("skriv", "Varför ändrade forskarna sig i de tre exemplen?", "De ändrade sig eftersom", 2)]),

 dict(titel="Söka information och bedöma källor", prog="Delområde 1.2 · Söka information och bedöma källor",
  fore=["När du söker på nätet: använd flera sökord. Till exempel <em>sömn tonåringar forskning</em>.", "En <strong>källa</strong> är där informationen kommer ifrån. <strong>Avsändaren</strong> är den som har skrivit eller gjort texten. Fråga dig om källan är trovärdig och relevant.", "<strong>Trovärdig</strong> betyder att man kan lita på den. <strong>Relevant</strong> betyder att den passar din fråga."],
  fig="l_fyra.png",
  efter=["Fråga också: Finns det <strong>belägg</strong>? Reklam har ofta inga belägg. Den vill sälja.", TB_CHECK, ARG],
  kom="Fråga: vem, varför, belägg, när och fler källor. Då ser du om en källa går att lita på.",
  ova=[("streck", "Vilken fråga passar? Dra streck.", ["Vem?", "Varför?", "När?", "Fler källor?"], ["Står det på fler ställen?", "Vem har skrivit texten?", "Vill de sälja något?", "Är texten gammal?"]),
       ("ringa", "Reklamen säger: ”Superbär botar ALLT på en dag!” Vad tror du?", ["Det är sant", "Det är nog inte sant"]),
       ("fyll", ["trovärdig", "relevant", "belägg"], ["En källa som går att lita på är ______________.", "En källa som passar min fråga är ______________.", "Mätningar som visar något kallas ______________."]),
       ("skriv", "Hur kan du se om en webbsida går att lita på?", "Jag kan", 2)]),

 dict(titel="Labb 1.2 Granska ett påstående", prog="Delområde 1.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Är påståendet sant? Du ska granska det med hjälp av två källor.", "Välj ett påstående:"] ,
  fig=None,
  efter=["<ol class='st'><li>Tio procent av hjärnan används.</li><li>Socker gör barn hyperaktiva.</li><li>Blixten slår aldrig ned två gånger på samma plats.</li></ol>",
         "<ol class='st'><li>Sök efter påståendet. Hitta två olika källor.</li><li>Fyll i checklistan för varje källa.</li><li>Bestäm: Är påståendet sant, osant eller osäkert?</li><li>Skriv ett kort argument. Använd mallen.</li></ol>", ARG,
         "<strong>Säkerhet:</strong> Skriv inga personuppgifter. Klicka inte på reklam eller länkar du inte litar på."],
  kom="Granska varje källa. Svara sedan med påstående, belägg, motargument och slutsats.",
  ova=[("skriv2", "Källa 1: Skriv webbadress eller namn. Svara sedan: vem har skrivit? Är den trovärdig?", ["Källa 1:", "Trovärdig? Varför?"]),
       ("skriv2", "Källa 2: Skriv webbadress eller namn. Svara sedan: vem har skrivit? Är den trovärdig?", ["Källa 2:", "Trovärdig? Varför?"]),
       ("skriv2", "Skriv ditt argument.", ["Mitt påstående:", "Belägg:", "Motargument och svar:", "Slutsats:"])]),
]
VIKTIGAST = [("l_ic1.png", "Biologi är läran om allt som lever."), ("l_ic2.png", "Forskare frågar, gissar (hypotes), testar och svarar (slutsats)."),
             ("l_ic3.png", "I ett rättvist test ändrar man bara en sak."), ("l_ic4.png", "Resultatet är det man mäter. Slutsatsen är det man lär sig."),
             (None, "Resultatet kan bli fel. Gör om testet och skriv vad som kan ha blivit fel."),
             (None, "Vetenskap prövar påståenden med belägg. Åsikter går inte att pröva."),
             (None, "En modell kan ändras när nya undersökningar visar något annat."),
             ("l_ic6.png", "Tro inte på allt du läser. Kolla vem, varför, belägg, när och fler källor.")]
TEST = [("ringa", "Vem forskar om växter?", ["Botaniker", "Zoolog", "Marinbiolog"]),
        ("streck", "Dra streck till rätt förklaring.", ["Hypotes", "Resultat", "Slutsats", "Belägg"], ["det man lär sig", "det man mäter eller ser", "det man tror blir svaret, och varför", "mätningar som visar något"]),
        ("sf", "Kryssa i rätt ruta.", ["I ett rättvist test ändrar man många saker.", "Man får äta i labbet.", "Man kan inte pröva en åsikt med mätningar.", "Allt som står på nätet är sant."]),
        ("ringa", "Vilken fråga går att undersöka?", ["Är hundar snälla?", "Hur högt hoppar en groda?", "Är sommar bäst?"]),
        ("skriv2", "Du vill testa om bönor gror bäst i varmt eller kallt. Vad ska du ändra? Vad ska vara lika?", ["Jag ändrar", "Det här ska vara lika:"]),
        ("skriv", "Ali säger: ”Mina bönor i värmen grodde snabbast. Alltså gror alla bönor bäst i värme.” Vad borde Ali göra för att vara säkrare?", "Ali borde", 2),
        ("skriv", "Semmelweis fick läkarna att tvätta händerna. Vad hände med dödligheten?", "Dödligheten", 1),
        ("skriv", "En webbsida säger att ett te botar förkylning på en timme. Hur kan du ta reda på om det stämmer?", "Jag kan", 2)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 1 (Biologi som vetenskap): systematiska undersökningar (fråga, plan, dokumentera, värdera), vad vetenskap kan pröva, "
                "hur förklaringsmodeller ändrats (Pasteur, Semmelweis, Marshall och Warren) samt informationssökning, källkritik och enkel argumentation. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå.")
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "9 delar (start, sex moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Kom ihåg-ruta i varje del med det viktigaste i en mening.", "Övningar direkt efter varje del: ringa in, dra streck, fyll i med ordbank, sant/falskt, kryssa och skriv med meningsstart.",
                "Labbarna är skrivna så att de går att göra med enkel utrustning."]
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
HANDLEDNING_HTML = """
<h3>Handledning per moment</h3>
<h3 class="mm">Start. Vad är biologi?</h3><p class="hl"><b>Mål:</b> eleven vet att biologi är läran om allt som lever. <b>Tips:</b> låt eleverna berätta vilken sorts biolog de själva skulle vilja vara.</p>
<h3 class="mm">Från fråga till plan</h3><p class="hl"><b>E-mål:</b> eleven kan avgöra om en fråga går att undersöka, vet att man ändrar en sak åt gången och nämner några säkerhetsregler. <b>Vanligt fel:</b> eleverna ändrar flera saker samtidigt (till exempel både ljus och placering). Be dem peka ut vad som ska vara lika. <b>Kommentar:</b> hypotesen ska innehålla ett ”eftersom”.</p>
<h3 class="mm">Dokumentera</h3><p class="hl"><b>E-mål:</b> eleven fyller i en tabell med rubriker och enheter och ritar ett diagram med rubrik och benämnda axlar. <b>Vanligt fel:</b> enhet saknas, axlar utan namn, staplar utan namn. <b>Kommentar:</b> låt eleverna rita för hand, så ser du direkt vad som saknas.</p>
<h3 class="mm">Värdera</h3><p class="hl"><b>E-mål:</b> eleven nämner en felkälla och förklarar varför man upprepar ett försök. <b>Vanligt fel:</b> eleverna tror att ett försök där hypotesen var fel är misslyckat. <b>Kommentar:</b> skillnaden mellan slump och systematiskt fel kommer först i grundtexten.</p>
<h3 class="mm">Labb 1.1 Reaktionstid</h3><p class="hl"><b>Material:</b> linjal 30 cm, penna, papper. <b>Förväntat:</b> de flesta hamnar på ca 15–25 cm, alltså ca 0,17–0,23 s (tabellen räknar med t = √(2·s/g), g = 9,81 m/s²). <b>Vanliga fel:</b> eleven ser kompisens hand och förutser släppet; linjalen hålls sned; noll ligger inte vid fingrarna. <b>Redovisning:</b> klassens värden, inte personliga. <b>Bonuslabb:</b> jämför höger och vänster hand, eller före och efter några minuters övning. Tala om vad som kan förklara skillnaden.</p>
<h3 class="mm">Vad kan vetenskap pröva?</h3><p class="hl"><b>E-mål:</b> eleven skiljer påståenden som går att pröva från åsikter och vet vad belägg är. <b>Vanligt fel:</b> eleverna tror att ”pröva” betyder ”bevisa att det är sant”. Ett påstående kan visa sig vara fel. <b>Kommentar:</b> horoskopet är bara ett exempel. Astrologer fick i ett dubbelblint test (Carlson, Nature 1985) para ihop födelsehoroskop med personlighetsprofiler och lyckades inte bättre än slumpen. Välj gärna egna exempel från klassen.</p>
<h3 class="mm">När forskare ändrat sig</h3><p class="hl"><b>E-mål:</b> eleven kan para ihop forskare och upptäckt och förklara att nya belägg kan ändra en modell. <b>Källor:</b> siffrorna för Semmelweis är från MJA 2018; Marshalls självförsök 1984 och Nobelpriset 2005 enligt Nobelstiftelsen och PMC. <b>Kommentar:</b> betona att Marshalls självförsök inte är något man ska göra.</p>
<h3 class="mm">Söka information och bedöma källor</h3><p class="hl"><b>E-mål:</b> eleven ställer frågorna vem, varför, belägg, nytt och fler källor till en källa och förklarar trovärdig och relevant. <b>Argumentation:</b> rutan ”Så argumenterar du” är den enkla mallen som används även i labben. Kunskapskraven kräver argumentation redan på E-nivå. <b>Vanligt fel:</b> eleverna blandar ihop trovärdig (går att lita på) och relevant (passar frågan).</p>
<h3 class="mm">Labb 1.2 Granska ett påstående</h3><p class="hl"><b>Påståenden:</b> (1) Att vi bara använder tio procent av hjärnan är en myt: hjärnavbildning (PET och fMRI) visar att alla delar av hjärnan är aktiva, även under sömn. (2) Socker gör barn hyperaktiva: dubbelblinda studier och en sammanställning av Wolraich m.fl. har inte visat något sådant samband. (3) Blixten kan slå ned flera gånger på samma plats: höga byggnader som Empire State Building träffas flera gånger varje år (NOAA/National Weather Service). <b>Källor:</b> Scientific American (tio-procentsmyten), Wolraich m.fl., JAMA 1995 (sammanställning av 23 studier om socker), NOAA/National Weather Service (blixt). Kontrollera gärna mot aktuella källor före lektionen. <b>Bedömningsstöd E:</b> eleven använder minst en frågeställning om källan, nämner ett belägg och drar en slutsats. <b>Bonuslabb:</b> låt eleverna hitta ett eget påstående från sociala medier och granska det.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Allt som lever. 2) Zoolog – djur; Botaniker – växter; Marinbiolog – livet i havet; Mikrobiolog – små organismer, som bakterier. 3) naturen, labb, kropp.",
 "<b>Från fråga till plan:</b> 1) Hur långt hoppar en groda? 2) Det Ella ändrar – ljuset; mäter – hur hög krassen blir; lika – jord och vatten. 3) Samma jord, lika mycket vatten, lika många frön. 4) Läser hela instruktionen först, frågar om jag är osäker. 5) Då vet man vad som orsakade skillnaden.",
 "<b>Dokumentera:</b> 1) Höjd (mm). 2) Stapeldiagram med rubrik, axlar med namn och enhet (cm), staplarna 12 och 8. 3) Slutsats 4, Fråga 1, Resultat 3, Så gjorde vi 2. 4) tabell, rubrik, enhet.",
 "<b>Värdera:</b> 1) En felkälla. 2) Sant, falskt, sant. 3) felkälla, flera, Slutsatsen. 4) Då är det mindre troligt att resultatet bara var en slump.",
 "<b>Labb 1.1:</b> 1) fem, tabell, cm. 2) Eget diagram. 3) T.ex. ”ungefär 0,2 s”. 4) T.ex. att man såg kompisens hand eller att linjalen hölls sned.",
 "<b>Vad kan vetenskap pröva?:</b> 1) Kaniner springer fortare än sköldpaddor. Vatten kokar vid 100 °C. 2) Mätningar och observationer. 3) belägg, åsikt, pseudovetenskap. 4) T.ex. testa med lukter och se vilka som hittar dem.",
 "<b>När forskare ändrat sig:</b> 1) Pasteur – små organismer kommer utifrån; Semmelweis – handtvätt minskar dödsfall; Marshall och Warren – magsår kommer av en bakterie. 2) Den sjönk. 3) modell, bakterie, belägg. 4) Nya undersökningar gav nya belägg.",
 "<b>Söka information och bedöma källor:</b> 1) Vem? – vem har skrivit texten; Varför? – vill de sälja något; När? – är texten gammal; Fler källor? – står det på fler ställen. 2) Det är nog inte sant. 3) trovärdig, relevant, belägg. 4) Kolla vem som skrivit, om de vill sälja något, om det finns belägg och om fler källor säger samma sak.",
 "<b>Labb 1.2:</b> Egna svar. Se bedömningsstödet i handledningen.",
 "<b>Testa dig:</b> 1) Botaniker. 2) Hypotes – det man tror blir svaret, och varför; Resultat – det man mäter eller ser; Slutsats – det man lär sig; Belägg – mätningar som visar något. 3) Falskt, falskt, sant, falskt. 4) Hur högt hoppar en groda? 5) Ändra temperaturen. Lika: sorts bönor, antal, vatten, jord, ljus. 6) Göra om testet flera gånger, med fler bönor. 7) Den sjönk (från 11,4 % till 1,3 %). 8) T.ex. kolla vem som står bakom, om de vill sälja, och om pålitliga källor säger samma sak.",
]

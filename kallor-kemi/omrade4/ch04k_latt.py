# -*- coding: utf-8 -*-
"""Kemi område 4 Kemiska föreningar och reaktioner – lättläst version (byggd per moment)."""
FIG = '/tmp/kem/fig04k/'
NR = 4
SLUG = "kemi-foreningar"
TAB = "4"
NAMN = "Kemiska föreningar och reaktioner"
NDEL = 9
UNDER = "Från atomer till nya ämnen"
INTRO_L = ["I det här kapitlet lär du dig hur atomer sitter ihop till molekyler och joner.",
           "Du lär dig också vad en kemisk reaktion är och hur man skriver den. Du lär dig varför massan inte ändras.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Start: vad som händer när atomer möts",
        "Delområde 4.1 Molekyler och joner: kovalent bindning, joner och egenskaper hos ämnen",
        "Delområde 4.2 Kemiska reaktioner: tecken på reaktion, reaktionsformler, hastighet och energi"]
ORD_FIG = None
ORD_EXTRA = [("kemisk förening", "ett ämne med atomer av olika grundämnen som sitter ihop"), ("kemisk bindning", "det som håller ihop atomer"), ("molekyl", "atomer som delar elektroner och sitter ihop"),
             ("kovalent bindning", "atomer delar elektronpar"), ("jon", "en laddad atom"), ("katjon", "en positiv jon"), ("anjon", "en negativ jon"),
             ("jonbindning", "positiva och negativa joner drar till varandra"), ("salt", "en jonförening, till exempel bordssalt"), ("smältpunkt", "temperaturen då ett ämne smälter"),
             ("elektrolyt", "ett ämne som leder ström när det är löst"), ("kemisk reaktion", "nya ämnen bildas"), ("utgångsämne", "ämne som reagerar"), ("produkt", "ämne som bildas"),
             ("balansera", "lika många atomer av varje sort på båda sidor"), ("katalysator", "gör att en reaktion går fortare"), ("exoterm", "avger energi, det blir varmare"), ("endoterm", "tar upp energi, det blir kallare")]

TB_BIND = ('<table class="tb"><tr><th></th><th>Kovalent bindning</th><th>Jonbindning</th></tr>'
           '<tr><td>Vad händer?</td><td>atomerna delar elektroner</td><td>elektroner flyttar</td></tr><tr><td>Mellan vad?</td><td>icke-metaller</td><td>metall och icke-metall</td></tr><tr><td>Exempel</td><td>H₂O, CO₂, CH₄</td><td>NaCl</td></tr></table>')
TB_JON = ('<table class="tb"><tr><th></th><th>Protoner</th><th>Elektroner</th><th>Laddning</th></tr>'
          '<tr><td>Na</td><td>11</td><td>11</td><td>0</td></tr><tr><td>Na⁺</td><td>11</td><td>10</td><td>+1</td></tr><tr><td>Cl</td><td>17</td><td>17</td><td>0</td></tr><tr><td>Cl⁻</td><td>17</td><td>18</td><td>−1</td></tr></table>')
TB_EGEN = ('<table class="tb"><tr><th></th><th>Molekylförening</th><th>Jonförening</th></tr>'
           '<tr><td>Smältpunkt</td><td>oftast låg</td><td>hög (salt ca 800 °C)</td></tr><tr><td>Fast ämne leder ström?</td><td>nej</td><td>nej</td></tr><tr><td>Löst eller smält leder ström?</td><td>nej</td><td>ja</td></tr></table>')
TB_SKIL = ('<table class="tb"><tr><th>Förändring</th><th>Kemisk eller fysikalisk?</th></tr>'
           '<tr><td>Isbit smälter</td><td>fysikalisk</td></tr><tr><td>Socker löses i vatten</td><td>fysikalisk</td></tr><tr><td>Papper brinner</td><td>kemisk</td></tr><tr><td>Spik rostar</td><td>kemisk</td></tr></table>')
TB_BAL = ('<table class="tb"><tr><th>Atom</th><th>Före (2 H₂ + O₂)</th><th>Efter (2 H₂O)</th></tr>'
          '<tr><td>H</td><td>4</td><td>4</td></tr><tr><td>O</td><td>2</td><td>2</td></tr></table>')
TB_EXO = ('<table class="tb"><tr><th></th><th>Exoterm</th><th>Endoterm</th></tr>'
          '<tr><td>Energi</td><td>avges</td><td>tas upp</td></tr><tr><td>Omgivningen</td><td>blir varmare</td><td>blir kallare</td></tr><tr><td>Exempel</td><td>förbränning</td><td>ättika + bikarbonat</td></tr></table>')
TB_LABB1 = ('<table class="tb"><tr><th>Vätska</th><th>Lampan lyser?</th></tr>'
            '<tr><td>Destillerat vatten</td><td></td></tr><tr><td>Saltvatten</td><td></td></tr><tr><td>Sockervatten</td><td></td></tr><tr><td>Kranvatten</td><td></td></tr></table>')
TB_LABB2 = ('<table class="tb"><tr><th>Försök</th><th>Massa före</th><th>Massa efter</th></tr>'
            '<tr><td>Sluten flaska</td><td></td><td></td></tr><tr><td>Öppen flaska</td><td></td><td></td></tr></table>')

DELOMR = {"4.1": "Molekyler och joner", "4.2": "Kemiska reaktioner"}
DELAR = [
 dict(titel="Vad händer när atomer möts?", prog="Start · Vad händer när atomer möts?",
  fore=["Atomer sitter ofta ihop med andra atomer. Då bildas en <strong>kemisk förening</strong>. Vatten och bordssalt är exempel.", "Det som håller ihop atomerna kallas <strong>kemisk bindning</strong>."],
  fig="v_oversikt.png", figw="90%",
  efter=["Atomer kan <strong>dela</strong> elektroner. Då bildas molekyler.", "Elektroner kan också <strong>flytta</strong> från en atom till en annan. Då bildas joner.", "I en <strong>kemisk reaktion</strong> byter atomerna partner. Nya ämnen bildas. Inga atomer försvinner."],
  kom="Atomer sitter ihop med bindningar. I en kemisk reaktion bildas nya ämnen.",
  ova=[("ringa", "Vad håller ihop atomer?", ["Kemiska bindningar", "Magneter", "Lim"]),
       ("sf", "Kryssa i rätt ruta.", ["Vatten är en kemisk förening.", "Atomer försvinner i en kemisk reaktion.", "I en kemisk reaktion bildas nya ämnen."]),
       ("fyll", ["delar", "flyttar", "bindning"], ["Atomer kan ______________ elektroner.", "Elektroner kan också ______________ till en annan atom.", "Det som håller ihop atomer kallas kemisk ______________."]),
       ("skriv", "Nämn en kemisk förening du känner till.", "En kemisk förening är", 1)]),

 dict(titel="Molekyler och kovalent bindning", prog="Delområde 4.1 · Molekyler och kovalent bindning",
  fore=["I en <strong>kovalent bindning</strong> delar atomer elektroner. Det sker mellan icke-metaller.", "Atomer som sitter ihop på det sättet bildar en <strong>molekyl</strong>."],
  fig="v_kovalent.png", figw="100%",
  efter=["Exempel: vatten H₂O har 2 väteatomer och 1 syreatom. Koldioxid CO₂ har 1 kolatom och 2 syreatomer. Metan CH₄ har 1 kolatom och 4 väteatomer.", "<strong>Molekylformeln</strong> visar vilka atomer som finns och hur många.", "Väte vill ha 1 bindning, syre 2 och kol 4."],
  kom="Kovalent bindning: atomer delar elektroner. Atomerna bildar en molekyl.",
  ova=[("ringa", "Vad händer i en kovalent bindning?", ["Atomer delar elektroner", "Elektroner flyttar", "Atomer försvinner"]),
       ("sf", "Kryssa i rätt ruta.", ["H₂O har två väteatomer.", "CO₂ har två kolatomer.", "En molekyl har atomer som sitter ihop."]),
       ("fyll", ["syreatom", "kolatom", "väteatomer"], ["CH₄ har en ______________ och fyra väteatomer.", "H₂O har två ______________ och en syreatom.", "CO₂ har en ______________ och två syreatomer."]),
       ("skriv", "Vad betyder molekylformeln H₂O?", "H₂O betyder", 2)]),

 dict(titel="Joner och jonföreningar", prog="Delområde 4.1 · Joner och jonföreningar",
  fore=["En <strong>jon</strong> är en laddad atom. Den har avgett eller tagit upp elektroner.", "En positiv jon kallas <strong>katjon</strong>. En negativ jon kallas <strong>anjon</strong>."],
  fig="v_jon.png", figw="50%",
  efter=["Natrium avger 1 elektron och blir Na⁺. Klor tar upp 1 elektron och blir Cl⁻.", TB_JON, "Na⁺ och Cl⁻ drar till varandra. Det är <strong>jonbindning</strong>. Då bildas ett salt, till exempel bordssalt NaCl. Jonerna sitter i ett <strong>kristallgitter</strong>."],
  kom="Jon = laddad atom. Katjon är positiv, anjon är negativ. Jonbindning: + och − drar till varandra.",
  ova=[("ringa", "Vad är en jon?", ["En laddad atom", "En atom utan kärna", "En molekyl"]),
       ("sf", "Kryssa i rätt ruta.", ["Na⁺ är en katjon.", "Cl⁻ är en positiv jon.", "Bordssalt är en jonförening."]),
       ("streck", "Dra streck till rätt namn.", ["Katjon", "Anjon", "Jonbindning"], ["negativ jon", "positiv jon", "+ och − drar till varandra"]),
       ("skriv", "Hur blir en natriumatom en natriumjon?", "Den", 2)]),

 dict(titel="Egenskaper hos föreningar", prog="Delområde 4.1 · Egenskaper hos föreningar",
  fore=["Hur ett ämne är uppbyggt avgör hur det beter sig.", TB_EGEN],
  fig="v_ledning.png", figw="72%",
  efter=["Salt smälter vid ungefär 800 °C. Vatten fryser vid 0 °C. Jonerna i salt hålls ihop hårt.", "Fast salt leder inte ström. Jonerna sitter fast. I saltvatten kan jonerna röra sig, så saltvatten leder ström. Ett sådant ämne kallas <strong>elektrolyt</strong>.", "Sockervatten leder inte ström. Det finns inga joner."],
  kom="Salt har hög smältpunkt. Saltvatten leder ström, fast salt och sockervatten gör det inte.",
  ova=[("ringa", "Vilken vätska leder ström?", ["Saltvatten", "Sockervatten", "Destillerat vatten"]),
       ("sf", "Kryssa i rätt ruta.", ["Fast salt leder ström.", "Salt har hög smältpunkt.", "Sockervatten innehåller joner."]),
       ("fyll", ["joner", "fast", "elektrolyt"], ["Saltvatten leder ström för att det finns ______________.", "I ______________ salt sitter jonerna fast.", "Ett ämne som leder ström när det är löst är en ______________."]),
       ("skriv", "Varför leder inte sockervatten ström?", "Det beror på att", 2)]),

 dict(titel="Labb 4.1 Leder lösningar elektrisk ström?", prog="Delområde 4.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Vilka vätskor leder elektrisk ström?", "Du behöver: batteri (4,5 V), lampa, sladdar, två elektroder, destillerat vatten, saltvatten, sockervatten, kranvatten och skyddsglasögon."],
  fig="v_labb1.png", figw="56%",
  efter=["<ol class='st'><li>Koppla kretsen. Testa att lampan lyser när elektroderna rör varandra.</li><li>Sänk elektroderna i en vätska. Rör dem inte ihop.</li><li>Skriv om lampan lyser.</li><li>Skölj elektroderna mellan vätskorna.</li></ol>", TB_LABB1,
         "<strong>Säkerhet:</strong> Använd bara batteriet, aldrig vägguttag. Ha skyddsglasögon. Smaka inte. Tvätta händerna."],
  kom="Lösningar med joner leder ström. Lösningar utan joner gör det inte.",
  ova=[("fyll", ["lyste", "saltvatten", "joner"], ["Lampan ______________ i en av vätskorna.", "Det var ______________.", "Det finns ______________ i den vätskan."]),
       ("skriv", "Vilka vätskor ledde inte ström?", "De som inte ledde var", 2),
       ("skriv", "Varför leder saltvatten ström?", "Det beror på att", 2)]),

 dict(titel="Vad är en kemisk reaktion?", prog="Delområde 4.2 · Vad är en kemisk reaktion?",
  fore=["I en <strong>kemisk reaktion</strong> bildas nya ämnen. Ämnena du börjar med är <strong>utgångsämnen</strong>. Ämnena som bildas är <strong>produkter</strong>.", "Exempel: <b>metan + syre → koldioxid + vatten</b>."],
  fig="v_reaktion.png", figw="62%",
  efter=["Tecken på reaktion: gas bildas, temperaturen ändras, färgen ändras, ett fast ämne bildas, ljus eller lukt.", "Men bubblor räcker inte. Kokande vatten bubblar också, och det är fortfarande vatten.", TB_SKIL],
  kom="Kemisk reaktion: nya ämnen bildas. Fysikalisk förändring: samma ämne byter tillstånd eller form.",
  ova=[("ringa", "Vad kallas ämnena som bildas?", ["Produkter", "Utgångsämnen", "Elektroder"]),
       ("sf", "Kryssa i rätt ruta.", ["Ett papper som brinner är en kemisk reaktion.", "När is smälter bildas ett nytt ämne.", "Gasbildning kan vara ett tecken på reaktion."]),
       ("streck", "Dra streck till rätt typ.", ["Isbit smälter", "Spik rostar", "Socker löses"], ["kemisk", "fysikalisk", "fysikalisk"]),
       ("skriv", "Nämn två tecken på en kemisk reaktion.", "Två tecken är", 2)]),

 dict(titel="Reaktionsformler och oförstörbarhet", prog="Delområde 4.2 · Reaktionsformler",
  fore=["En <strong>reaktionsformel</strong> visar reaktionen med formler. Atomerna försvinner inte. Därför måste det vara lika många atomer av varje sort på båda sidor.", "Man <strong>balanserar</strong> genom att sätta tal framför formlerna. Ändra aldrig talen inne i formlerna."],
  fig="v_balans.png", figw="76%",
  efter=["<strong>2 H₂ + O₂ → 2 H₂O</strong>", TB_BAL, "<strong>Massan bevaras</strong>: massan är lika stor före och efter i en sluten behållare. Lavoisier visade det. I en öppen flaska kan massan minska om en gas lämnar."],
  kom="Balansera: lika många atomer av varje sort på båda sidor. Massan bevaras.",
  ova=[("ringa", "Vad får man aldrig ändra när man balanserar?", ["Talen inne i formlerna", "Talen framför formlerna", "Pilen"]),
       ("sf", "Kryssa i rätt ruta.", ["Atomer försvinner i en reaktion.", "2 H₂O har 4 väteatomer.", "Massan bevaras i en sluten behållare."]),
       ("fyll", ["bildas", "balansera", "lika"], ["Man måste ______________ formeln.", "Det ska vara ______________ många atomer på båda sidor.", "När en gas ______________ i en öppen flaska kan vågen visa mindre."]),
       ("skriv", "Räkna: hur många H-atomer finns i 2 H₂O?", "Det finns", 2)]),

 dict(titel="Hastighet och energi", prog="Delområde 4.2 · Hastighet och energi",
  fore=["<strong>Reaktionshastighet</strong> är hur fort en reaktion går. Partiklarna måste krocka för att reagera.", "Reaktionen går fortare vid högre temperatur, högre koncentration, större ytarea och med en <strong>katalysator</strong>."],
  fig="v_hastighet.png", figw="76%",
  efter=["En <strong>exoterm</strong> reaktion avger energi. En <strong>endoterm</strong> reaktion tar upp energi.", TB_EXO],
  fig2="v_energi.png", fig2w="62%", n1=1,
  kom="Fler och hårdare krockar ger snabbare reaktion. Exoterm: varmare. Endoterm: kallare.",
  ova=[("ringa", "Vad gör en katalysator?", ["Reaktionen går fortare", "Reaktionen går långsammare", "Den förbrukas"]),
       ("sf", "Kryssa i rätt ruta.", ["Hög temperatur ger snabbare reaktion.", "Exoterm betyder att energi tas upp.", "Förbränning avger energi."]),
       ("streck", "Dra streck till rätt ord.", ["Exoterm", "Endoterm", "Katalysator"], ["tar upp energi", "ökar hastigheten", "avger energi"]),
       ("skriv", "Hur kan du få en reaktion att gå fortare?", "Man kan", 2)]),

 dict(titel="Labb 4.2 Massan bevaras", prog="Delområde 4.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Ändras massan när ättika och bikarbonat reagerar?", "Du behöver: våg, två flaskor, ballong, ättika, bikarbonat, skyddsglasögon."],
  fig="v_labb2.png", figw="56%",
  efter=["<ol class='st'><li>Häll ättika i flaskan. Lägg bikarbonat i ballongen och trä på den.</li><li>Väg allt. Skriv ned massan.</li><li>Lyft ballongen så bikarbonatet faller ned. Väg igen.</li><li>Gör samma sak i en öppen flaska.</li></ol>", TB_LABB2,
         "<strong>Säkerhet:</strong> Ha skyddsglasögon. Använd bara en tesked bikarbonat. Torka upp spill."],
  kom="Slutet system: massan är lika. Öppen flaska: gasen lämnar och massan minskar.",
  ova=[("fyll", ["gasen", "oförändrad", "minskade"], ["I den slutna flaskan var massan ______________.", "I den öppna flaskan ______________ massan.", "Det beror på att ______________ lämnade flaskan."]),
       ("skriv", "Har några atomer försvunnit? Förklara.", "Nej, för att", 2),
       ("skriv", "Hur kan du göra mätningen bättre?", "Man kan", 2)]),
]

VIKTIGAST = [("l_ic1.png", "Molekyl: atomer delar elektroner (kovalent bindning). Exempel H₂O, CO₂, CH₄."),
             ("l_ic2.png", "Jon: laddad atom. Positiv och negativ jon drar till varandra: jonbindning."),
             ("l_ic3.png", "Salt har hög smältpunkt. Saltvatten leder ström, fast salt och sockervatten gör det inte."),
             ("l_ic4.png", "Kemisk reaktion: nya ämnen bildas. Utgångsämnen blir produkter."),
             ("l_ic5.png", "Balansera: lika många atomer av varje sort på båda sidor. Massan bevaras."),
             ("l_ic6.png", "Högre temperatur, koncentration, ytarea och katalysator ger snabbare reaktion."),
             ("l_ic7.png", "Exoterm: energi avges. Endoterm: energi tas upp.")]
TEST = [("ringa", "Vad kallas en positiv jon?", ["Katjon", "Anjon", "Molekyl"]),
        ("streck", "Dra streck till rätt förklaring.", ["Molekyl", "Jonbindning", "Balansera", "Katalysator"], ["lika många atomer på båda sidor", "atomer delar elektroner", "ökar hastigheten", "+ och − drar till varandra"]),
        ("sf", "Kryssa i rätt ruta.", ["Fast salt leder ström.", "Saltvatten leder ström.", "Is som smälter är en kemisk reaktion.", "Atomer försvinner inte i en reaktion.", "Förbränning avger energi.", "H₂O har två syreatomer."]),
        ("fyll", ["molekyl", "produkter", "exoterm"], ["Atomer som delar elektroner bildar en ______________.", "Ämnena som bildas kallas ______________.", "En reaktion som avger energi är ______________."]),
        ("siffror", "Sätt i ordning. Skriv 1, 2, 3 och 4.", ["Balansera formeln", "Skriv formlerna", "Kontrollera", "Räkna atomerna"]),
        ("skriv", "Balansera: H₂ + Cl₂ → HCl. Skriv med tal framför.", "Svar:", 2),
        ("skriv", "Varför smälter salt vid högre temperatur än vatten fryser?", "Det beror på att", 2),
        ("skriv", "Nämn ett tecken på kemisk reaktion och en sak som påverkar hastigheten.", "Tecken:", 3)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 4 (Kemiska föreningar och reaktioner): kovalent bindning och molekyler, joner och jonföreningar, skillnaden i egenskaper, tecken på kemisk reaktion, enkla reaktionsformler och massans bevarande, reaktionshastighet samt exoterma och endoterma reaktioner. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå.")
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "9 delar (start, sex moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Samma två delområden som grundtexten.", "Övningar med flera format: ringa in, dra streck, kryssa, fyll i, skriva och sätta i ordning.", "Kom ihåg-ruta i varje moment och en samlad Viktigast-sida."]
HANDLEDNING_HTML = """
<h3>Handledning per moment (lättläst)</h3>
<h3 class="mm">Vad händer när atomer möts?</h3><p class="hl"><b>E-mål:</b> eleven vet att atomer binds ihop och att en reaktion ger nya ämnen. <b>Vanligt fel:</b> att atomer försvinner i reaktioner.</p>
<h3 class="mm">Molekyler och kovalent bindning</h3><p class="hl"><b>E-mål:</b> eleven läser molekylformler och vet att kovalent bindning är delade elektroner. <b>Vanligt fel:</b> att H₂O är H₂ + O. Bygg gärna modeller med tandpetare.</p>
<h3 class="mm">Joner och jonföreningar</h3><p class="hl"><b>E-mål:</b> eleven skiljer katjon från anjon och förklarar hur Na⁺ och Cl⁻ bildas. <b>Vanligt fel:</b> att en jon har fått fler protoner.</p>
<h3 class="mm">Egenskaper hos föreningar</h3><p class="hl"><b>E-mål:</b> eleven skiljer jonförening från molekylförening med smältpunkt och ledningsförmåga. <b>Vanligt fel:</b> att vatten alltid leder ström.</p>
<h3 class="mm">Labb 4.1 Leder lösningar elektrisk ström?</h3><p class="hl"><b>Material:</b> batteri 4,5 V, lampa, grafitstavar, destillerat vatten, saltvatten, sockervatten, kranvatten. <b>Förväntat:</b> saltvatten leder, sockervatten och destillerat vatten leder inte märkbart, kranvatten svagt. Aldrig nätspänning.</p>
<h3 class="mm">Vad är en kemisk reaktion?</h3><p class="hl"><b>E-mål:</b> eleven ger tecken på reaktion och skiljer kemisk från fysikalisk förändring. <b>Vanligt fel:</b> att allt som bubblar är en reaktion.</p>
<h3 class="mm">Reaktionsformler och oförstörbarhet</h3><p class="hl"><b>E-mål:</b> eleven räknar atomer och förstår att massan bevaras. <b>Vanligt fel:</b> att ändra talen inne i formeln.</p>
<h3 class="mm">Hastighet och energi</h3><p class="hl"><b>E-mål:</b> eleven nämner faktorer som påverkar hastigheten och skiljer exoterm från endoterm.</p>
<h3 class="mm">Labb 4.2 Massan bevaras</h3><p class="hl"><b>Material:</b> våg, flaskor, ballong, ättika, bikarbonat. <b>Förväntat:</b> massan oförändrad i den slutna flaskan (ballongen kan ge någon tiondels gram uppdrift) och mindre i den öppna. Skyddsglasögon.</p>
"""
FACIT = [
 "<b>Start:</b> 1) Kemiska bindningar. 2) Sant, falskt, sant. 3) delar, flyttar, bindning. 4) T.ex. vatten eller bordssalt.",
 "<b>Molekyler och kovalent bindning:</b> 1) Atomer delar elektroner. 2) Sant, falskt, sant. 3) kolatom, väteatomer, kolatom. 4) Två väteatomer och en syreatom.",
 "<b>Joner och jonföreningar:</b> 1) En laddad atom. 2) Sant, falskt, sant. 3) Katjon – positiv jon; Anjon – negativ jon; Jonbindning – + och − drar till varandra. 4) Den avger en elektron och får laddningen +1.",
 "<b>Egenskaper hos föreningar:</b> 1) Saltvatten. 2) Falskt, sant, falskt. 3) joner, fast, elektrolyt. 4) Sockervatten har inga joner som kan bära strömmen.",
 "<b>Labb 4.1:</b> 1) Egna svar, troligen lyste lampan i saltvatten. 2) Sockervatten, destillerat vatten (kranvatten kan leda svagt). 3) Det finns joner som kan röra sig.",
 "<b>Vad är en kemisk reaktion?:</b> 1) Produkter. 2) Sant, falskt, sant. 3) Isbit smälter – fysikalisk; Spik rostar – kemisk; Socker löses – fysikalisk. 4) T.ex. gasbildning och temperaturförändring.",
 "<b>Reaktionsformler och oförstörbarhet:</b> 1) Talen inne i formlerna. 2) Falskt, sant, sant. 3) balansera, lika, bildas. 4) 4 väteatomer.",
 "<b>Hastighet och energi:</b> 1) Reaktionen går fortare. 2) Sant, falskt, sant. 3) Exoterm – avger energi; Endoterm – tar upp energi; Katalysator – ökar hastigheten. 4) T.ex. höja temperaturen eller smula sönder ett fast ämne.",
 "<b>Labb 4.2:</b> 1) oförändrad, minskade, gasen. 2) Nej, gasen följde med ut och har massa. 3) T.ex. väga noggrannare och upprepa.",
 "<b>Testa dig:</b> 1) Katjon. 2) Molekyl – atomer delar elektroner; Jonbindning – + och − drar till varandra; Balansera – lika många atomer på båda sidor; Katalysator – ökar hastigheten. 3) Falskt, sant, falskt, sant, sant, falskt. 4) molekyl, produkter, exoterm. 5) Skriv formlerna 1; Räkna atomerna 2; Balansera formeln 3; Kontrollera 4. 6) H₂ + Cl₂ → 2 HCl. 7) Jonerna i salt hålls ihop av starka krafter, så det krävs mycket energi. 8) T.ex. gasbildning; temperatur påverkar hastigheten.",
]

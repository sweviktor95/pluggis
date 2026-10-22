# -*- coding: utf-8 -*-
"""Kemi område 4 Kemiska föreningar och reaktioner – grundtext (per moment). Samma format som område 1–3."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
FIG = '/tmp/kem/fig04k/'
NR = 4
SLUG = "kemi-foreningar"
TAB = "4"
NAMN = "Kemiska föreningar och reaktioner"
UNDER = "Från atomer till nya ämnen"
INTRO = ("Vatten, bordssalt och koldioxid är alla kemiska föreningar, men de beter sig helt olika. Varför smälter salt först vid ungefär 800 °C medan vatten fryser vid 0 °C? Och vad är det som händer när ett ljus brinner, järn rostar eller bikarbonat fräser i ättika? "
         "I det här kapitlet ser du hur atomer binds ihop, antingen genom att dela elektroner eller genom att elektroner flyttar från en atom till en annan. Du lär dig också hur kemiska reaktioner förvandlar ämnen utan att några atomer försvinner, hur du skriver och balanserar enkla reaktionsformler och vad som påverkar hur fort en reaktion går. "
         "Namn och mätvärden i uppgifterna är påhittade, om inget annat står.")
MAL = ["hur atomer binds ihop till molekyler genom att dela elektroner", "hur joner bildas när elektroner flyttar, och hur jonföreningar och salter är uppbyggda",
       "hur bindningstypen förklarar egenskaper som smältpunkt, löslighet och ledningsförmåga", "hur du känner igen en kemisk reaktion och skiljer den från en fysikalisk förändring",
       "hur du skriver och balanserar enkla reaktionsformler och varför massan bevaras", "vad som påverkar reaktionshastigheten, och vad exoterma och endoterma reaktioner är",
       "hur du planerar och genomför undersökningar och drar slutsatser av dina resultat"]
FUNDERA = "Vätgas och syrgas är två gaser. När de reagerar bildas vatten, som är en vätska och helt olik gaserna. Vad tror du har hänt med atomerna? Har några försvunnit, eller har de bara bytt plats? Skriv din gissning och spara den. I slutet av kapitlet får du se om du ändrar dig."
DELOMR = {"4.1": "Molekyler och joner", "4.2": "Kemiska reaktioner"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)

KQ = {
 "Start": [("Vad är en kemisk förening?", "Ett ämne där atomer av olika grundämnen är bundna till varandra, till exempel vatten (H₂O) eller bordssalt (NaCl)."),
           ("Vilka två sorters bindningar tittar vi på i kapitlet?", "Kovalent bindning, där atomer delar elektroner, och jonbindning, där elektroner flyttar från en atom till en annan."),
           ("Vad händer med atomerna i en kemisk reaktion?", "Bindningar bryts och nya bildas, så atomerna sitter ihop på ett nytt sätt. Atomerna är desamma före och efter.")],
 "4.1.1": [("Vad är en molekyl?", "En grupp atomer som hålls ihop av kovalenta bindningar."),
           ("Vad sker i en kovalent bindning?", "Två atomer delar ett eller flera par av elektroner."),
           ("Mellan vilka sorters grundämnen bildas oftast kovalenta bindningar?", "Mellan icke-metaller."),
           ("Hur många väteatomer och syreatomer finns i en vattenmolekyl, H₂O?", "Två väteatomer och en syreatom."),
           ("Vad betyder CO₂ och vad kallas ämnet?", "En kolatom och två syreatomer. Ämnet är koldioxid."),
           ("Hur många bindningar vill kol ha i den förenklade modellen, och varför?", "Fyra, eftersom kol har 4 valenselektroner och behöver 4 till för att få fullt yttersta skal.")],
 "4.1.2": [("Vad är en jon?", "En atom (eller grupp av atomer) som har fått en laddning genom att avge eller ta upp elektroner."),
           ("Vad är skillnaden mellan katjon och anjon?", "Katjon är en positiv jon och anjon är en negativ jon."),
           ("Hur bildas en natriumjon, Na⁺, och vilken elektronfördelning får den?", "Natrium (2, 8, 1) avger en elektron och får 2, 8. Det är 11 protoner och 10 elektroner, så laddningen är +1."),
           ("Hur bildas en kloridjon, Cl⁻?", "Klor (2, 8, 7) tar upp en elektron och får 2, 8, 8. Det är 17 protoner och 18 elektroner, så laddningen är −1."),
           ("Vad är jonbindning?", "Attraktionen mellan positiva och negativa joner."),
           ("Hur är en saltkristall uppbyggd?", "Av positiva och negativa joner som sitter i ett regelbundet jonkristallgitter, där varje jon omges av motsatt laddade joner.")],
 "4.1.3": [("Varför har jonföreningar höga smältpunkter?", "Jonerna hålls ihop av starka krafter i gittret, så det krävs mycket energi för att få isär dem. Bordssalt smälter vid ungefär 800 °C."),
           ("Varför har molekylföreningar ofta låga smältpunkter?", "Krafterna mellan molekylerna är svaga, så det går åt lite energi för att få dem att röra sig fritt."),
           ("Leder fast salt elektrisk ström? Motivera.", "Nej. Jonerna sitter fast i gittret och kan inte röra sig."),
           ("När leder en jonförening ström?", "När den är löst i vatten eller smält, eftersom jonerna då kan röra sig fritt."),
           ("Vad är en elektrolyt?", "Ett ämne som leder ström när det är löst eller smält, eftersom det innehåller rörliga joner."),
           ("Varför leder sockerlösning inte ström?", "Socker består av molekyler utan laddning. Det finns inga fria joner som kan bära strömmen.")],
 "4.2.1": [("Vad kallas ämnena före och efter en kemisk reaktion?", "Utgångsämnen (reaktanter) före och produkter efter."),
           ("Nämn tre tecken på att en kemisk reaktion har skett.", "Gasbildning (bubblor), färgförändring, temperaturförändring, att ett fast ämne bildas eller ljus och lukt."),
           ("Varför bevisar inte bubblor ensamma att en kemisk reaktion skett?", "Kokande vatten bildar också bubblor, men det är fortfarande vatten (en fysikalisk förändring)."),
           ("Vad är skillnaden mellan kemisk och fysikalisk förändring?", "I en kemisk förändring bildas nya ämnen. I en fysikalisk förändring är det samma ämne som byter tillstånd eller form."),
           ("Är det kemisk eller fysikalisk förändring när socker löses i vatten? Motivera.", "Fysikalisk. Sockret är kvar och går att få tillbaka genom att låta vattnet dunsta."),
           ("Skriv reaktionen när metan brinner med ord.", "metan + syre → koldioxid + vatten")],
 "4.2.2": [("Varför måste man balansera en reaktionsformel?", "Atomerna varken skapas eller förstörs, så det måste finnas lika många av varje sort på båda sidor."),
           ("Vad är en koefficient och var skriver man den?", "Talet framför en formel. Det anger hur många molekyler (eller formelenheter) som reagerar eller bildas."),
           ("Vad får man aldrig göra när man balanserar?", "Ändra talen inne i formlerna, eftersom det skulle byta ut ämnet."),
           ("Balansera: H₂ + O₂ → H₂O.", "2 H₂ + O₂ → 2 H₂O"),
           ("Vad menas med massans bevarande, och vem visade det med noggranna vägningar?", "Att massan är lika stor före och efter en reaktion i ett slutet system. Lavoisier visade det på 1780-talet."),
           ("Varför kan massan minska på en våg när en gas bildas i en öppen flaska?", "Gasen lämnar flaskan och tar sin massa med sig. Atomerna har inte försvunnit.")],
 "4.2.3": [("Vad är reaktionshastighet?", "Hur snabbt utgångsämnen förbrukas eller produkter bildas."),
           ("Nämn fyra saker som påverkar reaktionshastigheten.", "Temperatur, koncentration, ytarea (hur finfördelat ett fast ämne är) och katalysator."),
           ("Varför går en reaktion fortare vid högre temperatur?", "Partiklarna rör sig snabbare, krockar oftare och hårdare, och fler krockar leder till reaktion."),
           ("Vad är en katalysator?", "Ett ämne som gör att en reaktion går fortare utan att själv förbrukas."),
           ("Vad är skillnaden mellan exoterm och endoterm reaktion?", "Exoterm: energi avges och omgivningen blir varmare. Endoterm: energi tas upp och omgivningen blir kallare."),
           ("Ge ett exempel på en exoterm och en endoterm reaktion.", "Exoterm: förbränning. Endoterm: ättika och bikarbonat, där temperaturen sjunker.")],
}
def kq(key):
    return kolla(key if key != "Start" else "Start", [q for q, a in KQ[key]])

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad händer när atomer möts?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p>I kapitel 3 lärde du dig att allt består av atomer och att det är elektronerna i yttersta skalet, <strong class='green'>valenselektronerna</strong>, som avgör hur ett ämne reagerar. Nu ser vi vad som händer när atomer möts. Atomer finns sällan ensamma. De flesta ämnen du känner till är <strong class='green'>kemiska föreningar</strong>: ämnen där atomer av olika grundämnen är bundna till varandra. Vatten (H₂O), koldioxid (CO₂) och bordssalt (NaCl) är exempel.</p>"
     "<p>Atomerna hålls ihop av <strong class='green'>kemiska bindningar</strong>. I den förenklade modell vi använder finns två huvudsorter. I en <strong class='green'>kovalent bindning</strong> delar atomerna elektroner. I en <strong class='green'>jonbindning</strong> flyttar elektroner från en atom till en annan, så att atomerna blir laddade och dras till varandra.</p>"
     "<p>I en <strong class='green'>kemisk reaktion</strong> bryts bindningar och nya bildas, så att nya ämnen uppstår. Atomerna är desamma före och efter, men de sitter ihop på ett nytt sätt. Därför kan inga atomer försvinna.</p>"
     "<p>I det här kapitlet svarar vi på tre frågor:</p>"
     + bullets(["Hur binds atomer ihop, och hur påverkar det ämnets egenskaper?", "Hur vet man att en kemisk reaktion har skett, och hur skriver man den?", "Vad avgör hur fort en reaktion går och om den avger eller tar upp energi?"]),
   [begrepp([("Kemisk förening", "Ämne där atomer av olika grundämnen är bundna till varandra."), ("Kemisk bindning", "Det som håller ihop atomer."), ("Kemisk reaktion", "Förändring där nya ämnen bildas.")]),
    box("tank", "Tänk efter", "<p>Bordssalt är gjort av natrium, en metall som reagerar kraftigt med vatten, och klor, en grön gas. Ändå är salt ofarligt på maten. Hur kan egenskaperna bli så olika? Skriv ner din idé.</p>")])
 + fig(FIG+"v_oversikt.png", "<b>Bild 4.1</b> Tre sätt som atomer kan ordnas om: i en molekyl delar de elektroner, i en jonförening flyttar elektroner, och i en kemisk reaktion byter atomerna partner. Bilderna är schematiska.", "90%")
 + table(["Delområde", "Du lär dig"],
         [["<b>4.1</b> Molekyler och joner", "Kovalent bindning och molekyler, joner och jonföreningar, och hur bindningstypen förklarar egenskaper som smältpunkt och ledningsförmåga. Labb: leder lösningar elektrisk ström?"],
          ["<b>4.2</b> Kemiska reaktioner", "Tecken på reaktion, reaktionsformler och massans bevarande, reaktionshastighet samt energi i reaktioner. Labb: massan bevaras."]])
 + kq("Start"))

# ------------------------------------------------------------------ 4.1.1
add("4.1.1", "Molekyler och kovalent bindning", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Molekyler och kovalent bindning",
 roww("<p>Många ämnen består av <strong class='green'>molekyler</strong>: grupper av atomer som hålls ihop av <strong class='green'>kovalenta bindningar</strong>. I en kovalent bindning <em>delar</em> två atomer ett eller flera par av elektroner. Sådana bindningar bildas oftast mellan icke-metaller.</p>"
      "<p>Varför delar atomer elektroner? I vår förenklade modell vill atomerna få fullt yttersta skal, som ädelgaserna har. Väte har en elektron och behöver två (som helium). Två väteatomer kan dela varsin elektron, och då har båda två elektroner i sitt skal. Det är en vätgasmolekyl, H₂. Syre har sex valenselektroner och behöver två till. Kol har fyra och behöver fyra till.</p>",
      [begrepp([("Molekyl", "Grupp av atomer som hålls ihop av kovalenta bindningar."), ("Kovalent bindning", "Bindning där atomer delar elektronpar."), ("Molekylformel", "Visar vilka atomer och hur många som finns i molekylen.")])])
 + fig(FIG+"v_kovalent.png", "<b>Bild 4.2</b> Fyra molekyler (schematiskt): vätgas H₂, vatten H₂O, metan CH₄ och koldioxid CO₂. Varje blått elektronpar mellan två atomer är en bindning.", "84%")
 + "<p>I en vattenmolekyl delar syre ett elektronpar med varje väteatom. I metan delar kol ett par med var och en av fyra väteatomer. I koldioxid delar kol <em>två</em> par med varje syreatom, vilket kallas en dubbelbindning. Syrgas, O₂, har också en dubbelbindning.</p>"
 + "<h3>Att läsa en molekylformel</h3>"
 + roww("<p><strong class='green'>Molekylformeln</strong> visar vilka grundämnen som finns och hur många atomer av varje. Den lilla siffran efter en beteckning gäller atomen framför. H₂O betyder alltså två väteatomer och en syreatom. Står det ingen siffra betyder det en atom.</p>"
        "<p>Antalet bindningar en atom vill ha hänger ihop med valenselektronerna: väte vill ha 1 bindning, syre 2, kväve 3 och kol 4. Det kan du använda när du bygger modeller av molekyler med modellkit, eller med tandpetare och gummibjörnar. Varje tandpetare är en bindning.</p>",
        [table(["Atom", "Valens-elektroner", "Bindningar"], [["Väte, H", "1", "1"], ["Syre, O", "6", "2"], ["Kväve, N", "5", "3"], ["Kol, C", "4", "4"]], "tbl num")])
 + kq("4.1.1"))

# ------------------------------------------------------------------ 4.1.2
add("4.1.2", "Joner och jonföreningar", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Joner och jonföreningar",
 roww("<p>Atomer kan också få fullt yttersta skal genom att elektroner <em>flyttar</em>. En atom som avger eller tar upp elektroner blir en <strong class='green'>jon</strong>, alltså en laddad atom. Antalet protoner ändras inte, bara antalet elektroner. Laddningen är antalet protoner minus antalet elektroner.</p>"
      "<p>Natrium har elektronerna 2, 8, 1. Om natriumatomen avger sin enda valenselektron får den 2, 8, precis som ädelgasen neon. Den har 11 protoner men bara 10 elektroner och blir en natriumjon, Na⁺, med laddningen +1. Klor har 2, 8, 7. Tar kloratomen upp en elektron får den 2, 8, 8 och laddningen −1: en kloridjon, Cl⁻.</p>",
      [begrepp([("Jon", "Laddad atom (eller grupp av atomer)."), ("Katjon", "Positiv jon, till exempel Na⁺."), ("Anjon", "Negativ jon, till exempel Cl⁻.")])])
 + fig(FIG+"v_jon.png", "<b>Bild 4.3</b> Natrium avger en elektron och blir Na⁺. Klor tar upp en elektron och blir Cl⁻. Elektronen som flyttar är orange (schematiskt).", "46%")
 + "<h3>Jonbindning och salter</h3>"
 + roww("<p>Metaller avger elektroner lätt och bildar katjoner. Icke-metaller tar upp elektroner och bildar anjoner. Kraften som drar positiva och negativa joner mot varandra kallas <strong class='green'>jonbindning</strong>. Ämnen som bildas av en metall och en icke-metall är <strong class='green'>jonföreningar</strong>, ofta kallade <strong class='green'>salter</strong>.</p>"
        "<p>Jonerna bildar inte enskilda par utan ett stort, regelbundet mönster, ett <strong class='green'>kristallgitter</strong>. I natriumklorid, vanligt bordssalt, omges varje natriumjon av kloridjoner och tvärtom. Formeln NaCl visar förhållandet: en natriumjon för varje kloridjon.</p>",
        [begrepp([("Jonbindning", "Attraktion mellan positiva och negativa joner."), ("Salt", "Jonförening av en metall och en icke-metall."), ("Kristallgitter", "Regelbundet mönster av joner.")])])
 + fig(FIG+"v_kristall.png", "<b>Bild 4.4</b> Natriumklorid (schematiskt): positiva natriumjoner och negativa kloridjoner i ett regelbundet gitter. Bilden visar ett plan.", "58%")
 + box("tank", "Tänk efter", "<p>Varför är bordssalt, NaCl, elektriskt neutralt även om det består av laddade joner? Och varför kan inte två Na⁺ bilda en bindning med varandra?</p>") + kq("4.1.2"))

# ------------------------------------------------------------------ 4.1.3
add("4.1.3", "Egenskaper hos föreningar", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Egenskaper hos föreningar",
 "<p>Hur ett ämne är uppbyggt avgör hur det beter sig. Det gäller smältpunkt, ledningsförmåga och löslighet. Här jämför vi molekylföreningar, jonföreningar och metaller.</p>"
 + table(["", "Molekylföreningar (t.ex. H₂O, CO₂, CH₄)", "Jonföreningar (t.ex. NaCl)", "Metaller"],
         [["<b>Byggs upp av</b>", "Molekyler", "Joner i ett gitter", "Metallatomer"],
          ["<b>Smält- och kokpunkt</b>", "Oftast låga. Svaga krafter mellan molekylerna.", "Höga. Bordssalt smälter vid ungefär 800 °C.", "Oftast höga"],
          ["<b>Leder ström</b>", "Nej", "Fast: nej. Löst eller smält: ja.", "Ja"],
          ["<b>Löser sig i vatten</b>", "Varierar: socker löser sig", "Ofta ja", "Nej"]], "tbl")
 + "<h3>Smältpunkt</h3>"
 + "<p>Vatten fryser vid 0 °C, men bordssalt smälter först vid ungefär 800 °C. Skillnaden beror på bindningarna. I en jonförening hålls jonerna fast av starka krafter i gittret, och det krävs mycket energi för att få dem att röra sig. Mellan molekylerna i en molekylförening är krafterna svaga, så det går åt lite energi. Därför är jonföreningar vid rumstemperatur oftast fasta, medan molekylföreningar ofta är gaser eller vätskor.</p>"
 + "<h3>Ledningsförmåga</h3>"
 + roww("<p>För att leda elektrisk ström behövs <em>rörliga laddade partiklar</em>. I fast salt sitter jonerna fast i gittret, så fast salt leder inte. Löser man saltet i vatten drar vattenmolekylerna loss jonerna från gittret, och då kan de röra sig och bära strömmen. Detsamma gäller om saltet smälts. Ett ämne som leder ström när det är löst eller smält kallas en <strong class='green'>elektrolyt</strong>.</p>"
        "<p>Sockerlösning leder inte ström, eftersom socker består av molekyler utan laddning. Rent vatten leder dåligt, men kranvatten leder lite eftersom det innehåller små mängder lösta salter. Metaller leder ström som fast ämne, vilket du får veta mer om i fördjupningen.</p>",
        [begrepp([("Elektrolyt", "Ämne som leder ström när det är löst eller smält.")])])
 + fig(FIG+"v_ledning.png", "<b>Bild 4.5</b> Lampan lyser bara om det finns rörliga laddade partiklar: fast salt leder inte, saltlösning leder och sockerlösning leder inte (schematiskt).", "58%")
 + kq("4.1.3"))

# ------------------------------------------------------------------ Labb 4.1
add("Labb", "4.1 Leder lösningar elektrisk ström?", f"Kapitel {NR} · Delområde 4.1 {DELOMR['4.1']} · Labb 4.1 Leder lösningar elektrisk ström?",
 "<p>Du har lärt dig att det behövs rörliga joner för att en lösning ska leda ström. I det här försöket testar du det genom att jämföra fyra vätskor med en enkel krets.</p>"
 + fig(FIG+"v_labb1.png", "<b>Bild 4.6</b> Kopplingsschema: batteri, lampa och två elektroder som sänks ned i lösningen.", "36%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Vilka av vätskorna destillerat vatten, saltvatten, sockervatten och kranvatten leder elektrisk ström?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror för varje vätska och förklara med joner.</p>"
        "<p><strong class='green'>Material:</strong> batteri 4,5 V, liten glödlampa, sladdar, två elektroder (grafitstavar eller blyertsstift), fyra bägare med destillerat vatten, saltvatten, sockervatten och kranvatten, destillerat vatten och hushållspapper för sköljning, skyddsglasögon.</p><h3>Gör så här</h3>"
        + steps(["Koppla kretsen enligt bilden. Testa att den fungerar genom att hålla elektroderna mot varandra: lampan ska lysa.",
                 "Sänk ned elektroderna i den första vätskan så att de inte rör varandra. Notera om lampan lyser starkt, svagt eller inte alls.",
                 "Skölj elektroderna i destillerat vatten och torka dem mellan varje vätska.",
                 "Testa alla fyra vätskor och fyll i tabellen.",
                 "Förklara resultaten med joner."]),
        [box("begrepp", "Begrepp", "<b class='t'>Elektrolyt</b><p>Ämne som leder ström när det är löst eller smält.</p><b class='t'>Elektrod</b><p>Ledare som för in strömmen i vätskan.</p>"),
         box("tank", "Bra att veta", "<p>En svag ström syns kanske inte som ljus i lampan. Jämför därför alltid med destillerat vatten.</p>")])
 + table(["Vätska", "Lampan lyser?", "Leder strömmen?"], [["Destillerat vatten", "", ""], ["Saltvatten", "", ""], ["Sockervatten", "", ""], ["Kranvatten", "", ""]], "tbl num")
 + '<p class="note">Säkerhet: Använd bara batteriet (högst 4,5 V). Använd aldrig vägguttag. Ha skyddsglasögon. Håll försöket kort, för vid elektroderna kan små mängder gas bildas. Smaka inte på något. Torka upp spill och tvätta händerna.</p>'
 + "<h3>Frågor</h3>"
 + steps(["Vilka vätskor ledde ström, och vad innehåller de som de andra saknar?", "Varför ledde sockervattnet inte, fast socker löser sig i vatten?", "Hur säker är din slutsats om kranvattnet? Vad kunde du göra för att bli säkrare?"], True))

# ------------------------------------------------------------------ 4.2.1
add("4.2.1", "Vad är en kemisk reaktion?", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Vad är en kemisk reaktion?",
 roww("<p>I en <strong class='green'>kemisk reaktion</strong> omvandlas ett eller flera ämnen till nya ämnen med andra egenskaper. Ämnena du börjar med kallas <strong class='green'>utgångsämnen</strong> (reaktanter), och ämnena som bildas kallas <strong class='green'>produkter</strong>. Man skriver reaktionen med en pil: utgångsämnen → produkter.</p>"
      "<p>Exempel: när metan i naturgas brinner reagerar den med syre och bildar koldioxid och vatten. Reaktionen kan skrivas <b>metan + syre → koldioxid + vatten</b>. När järn rostar reagerar det med syre (och vatten) och bildar järnoxid: <b>järn + syre → järnoxid</b>.</p>",
      [begrepp([("Utgångsämne", "Ämne som reagerar. Kallas också reaktant."), ("Produkt", "Ämne som bildas."), ("Ny substans", "Ämne med egenskaper som skiljer sig från utgångsämnena.")])])
 + fig(FIG+"v_reaktion.png", "<b>Bild 4.7</b> Vätgas och syrgas reagerar och bildar vatten (schematiskt): atomerna byter partner men inga atomer försvinner.", "50%")
 + "<h3>Tecken på kemisk reaktion</h3>"
 + "<p>Det finns några vanliga tecken på att en kemisk reaktion har skett:</p>"
 + bullets(["<b>Gas bildas:</b> det bubblar eller fräser, till exempel när bikarbonat blandas med ättika.", "<b>Temperaturen ändras:</b> det blir varmare eller kallare utan att du värmer eller kyler.", "<b>Färgen ändras</b> eller ett <b>fast ämne bildas</b> i en lösning.", "<b>Ljus eller lukt</b> uppstår, till exempel vid förbränning."])
 + "<p>Tecknen visar att något <em>kan</em> ha hänt, men de bevisar inte alltid en reaktion. Kokande vatten bubblar också, men det är fortfarande vatten.</p>"
 + "<h3>Kemisk eller fysikalisk förändring?</h3>"
 + "<p>I en <strong class='green'>fysikalisk förändring</strong> är det samma ämne som byter tillstånd eller form. Atomerna sitter ihop på samma sätt som förut. I en kemisk förändring bryts bindningar och nya ämnen bildas.</p>"
 + '<div style="break-inside:avoid">' + table(["Förändring", "Typ", "Varför"],
         [["En isbit smälter", "Fysikalisk", "Fortfarande vatten, bara annat tillstånd"], ["Socker löses i vatten", "Fysikalisk", "Sockret finns kvar och kan fås tillbaka när vattnet dunstar"], ["Ett papper brinner", "Kemisk", "Nya ämnen bildas, bland annat koldioxid och vatten"], ["En järnspik rostar", "Kemisk", "Järnoxid bildas, ett nytt ämne"]], "tbl") + '</div>'
 + kq("4.2.1"))

# ------------------------------------------------------------------ 4.2.2
add("4.2.2", "Reaktionsformler och oförstörbarhet", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Reaktionsformler och oförstörbarhet",
 roww("<p>En <strong class='green'>reaktionsformel</strong> visar en reaktion med kemiska formler i stället för ord. Vätgas och syrgas som bildar vatten blir H₂ + O₂ → H₂O. Räknar vi atomerna har vi två väteatomer och två syreatomer till vänster men bara en syreatom till höger. En syreatom har försvunnit, men det kan inte ske. Atomer skapas eller förstörs inte i kemiska reaktioner, de byter bara partner.</p>"
      "<p>Därför måste formeln <strong class='green'>balanseras</strong>, så att det finns lika många atomer av varje sort på båda sidor. Det gör man genom att sätta <strong class='green'>koefficienter</strong>, alltså tal framför formlerna.</p>",
      [begrepp([("Reaktionsformel", "Reaktionen skriven med kemiska formler."), ("Balansera", "Se till att lika många atomer av varje sort finns på båda sidor."), ("Koefficient", "Talet framför en formel i en reaktionsformel.")])])
 + "<h3>Så balanserar du</h3>"
 + steps(["Skriv formeln med rätt formler för alla ämnen: H₂ + O₂ → H₂O.", "Räkna atomerna på båda sidor. Här finns 2 O till vänster men 1 O till höger.",
          "Sätt koefficienter framför formlerna tills det är lika. Skriv 2 H₂O: då finns 2 O till höger, men 4 H. Sätt då 2 H₂ till vänster.", "Kontrollera: 2 H₂ + O₂ → 2 H₂O har 4 H och 2 O på båda sidor."])
 + "<p class='note'>Ändra aldrig talen inne i en formel. H₂O är vatten, men H₂O₂ är ett annat ämne.</p>"
 + fig(FIG+"v_balans.png", "<b>Bild 4.8</b> Metan brinner (schematiskt): CH₄ + 2 O₂ → CO₂ + 2 H₂O. Det finns 1 C, 4 H och 4 O på båda sidor.", "64%")
 + "<h3>Massans bevarande</h3>"
 + "<p>Eftersom inga atomer försvinner är massan lika stor före och efter en reaktion i ett slutet system. Det visade Antoine Lavoisier på 1780-talet med noggranna vägningar. Om 10 g av ett ämne reagerar helt med 8 g av ett annat och bara en produkt bildas, väger produkten 18 g (påhittade siffror). Om en gas bildas i en öppen behållare kan vågen ändå visa mindre massa, för gasen har lämnat behållaren och tagit sin massa med sig.</p>"
 + "<p>Tre vanliga reaktioner är <b>förbränning</b> (bränsle + syre → koldioxid + vatten, energi avges), <b>rostning</b> eller oxidation av järn (järn + syre + vatten → järnoxid) och <b>syra mot metall</b> (metall + syra → salt + vätgas, gas bubblar upp).</p>" + kq("4.2.2"))

# ------------------------------------------------------------------ 4.2.3
add("4.2.3", "Hastighet och energi", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Hastighet och energi",
 roww("<p><strong class='green'>Reaktionshastigheten</strong> säger hur snabbt utgångsämnen förbrukas eller produkter bildas. För att en reaktion ska ske måste partiklarna krocka med varandra med tillräcklig energi och rätt riktning. Allt som ger fler eller hårdare krockar gör reaktionen snabbare:</p>"
      + bullets(["<b>Högre temperatur:</b> partiklarna rör sig snabbare och krockar oftare och hårdare.", "<b>Högre koncentration:</b> partiklarna sitter tätare, så de krockar oftare.", "<b>Större ytarea:</b> finfördelat fast ämne har fler partiklar att krocka med.", "<b>Katalysator:</b> får reaktionen att gå fortare utan att förbrukas (t.ex. enzymer i kroppen)."]),
      [begrepp([("Reaktionshastighet", "Hur fort en reaktion går."), ("Katalysator", "Ämne som ökar hastigheten utan att förbrukas."), ("Koncentration", "Hur mycket ämne som finns i en viss volym.")])])
 + fig(FIG+"v_hastighet.png", "<b>Bild 4.9</b> Fler och hårdare krockar ger snabbare reaktion (schematiskt).", "46%")

 + "<h3>Energi i reaktioner</h3>"
 + roww("<p>För att bryta bindningar behövs energi, och när nya bindningar bildas avges energi. Avges mer energi än som behövs är reaktionen <strong class='green'>exoterm</strong>: energi avges till omgivningen, som blir varmare. Förbränning är exotermt. Behövs mer energi än som avges är reaktionen <strong class='green'>endoterm</strong>: energi tas upp, och omgivningen blir kallare. När ättika och bikarbonat reagerar sjunker temperaturen, så det är en endoterm reaktion.</p>",
        [begrepp([("Exoterm", "Avger energi, omgivningen blir varmare."), ("Endoterm", "Tar upp energi, omgivningen blir kallare.")])])
 + fig(FIG+"v_energi.png", "<b>Bild 4.10</b> Energidiagram (schematiskt): vid en exoterm reaktion har produkterna mindre energi än utgångsämnena, vid en endoterm reaktion mer.", "38%")
 + kq("4.2.3"))

# ------------------------------------------------------------------ Labb 4.2
add("Labb", "4.2 Massan bevaras: väg före och efter", f"Kapitel {NR} · Delområde 4.2 {DELOMR['4.2']} · Labb 4.2 Massan bevaras",
 "<p>Lavoisier vägde ämnen före och efter reaktioner. I det här försöket gör du något liknande: du låter ättika och bikarbonat reagera i en sluten och i en öppen flaska och väger.</p>"
 + fig(FIG+"v_labb2.png", "<b>Bild 4.11</b> Sluten flaska med ballong och öppen flaska på våg (schematiskt, påhittade värden).", "36%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Ändras massan när ättika och bikarbonat reagerar, och spelar det någon roll om flaskan är öppen eller sluten?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror för båda fallen och motivera.</p>"
        "<p><strong class='green'>Material:</strong> våg (0,1 g), två plastflaskor eller koniska kolvar, ballong, ättika, bikarbonat (natriumvätekarbonat), mätcylinder, tesked, liten bägare, skyddsglasögon, hushållspapper.</p><h3>Gör så här</h3>"
        + steps(["Häll 50 ml ättika i flaskan. Lägg 1 tesked bikarbonat i ballongen och trä ballongen över flaskhalsen utan att hälla ned bikarbonatet.",
                 "Väg flaska, ballong och innehåll tillsammans. Skriv ned massan.",
                 "Lyft ballongen så bikarbonatet faller ned. Vänta tills det slutar bubbla och väg igen.",
                 "Upprepa med en öppen flaska. Ställ flaskan med ättikan och en bägare med bikarbonat på vågen, notera massan, häll ned bikarbonatet, ställ tillbaka bägaren och väg igen."]),
        [box("begrepp", "Begrepp", "<b class='t'>Slutet system</b><p>Inget ämne kommer in eller ut.</p><b class='t'>Massans bevarande</b><p>Massan är lika stor före och efter.</p>"),
         box("tank", "Bra att veta", "<p>Använd ballong, inte ett tätt lock: gasen kan annars ge så högt tryck att flaskan spricker.</p>")])
 + table(["Försök", "Massa före (g)", "Massa efter (g)", "Skillnad (g)"], [["Sluten flaska", "", "", ""], ["Öppen flaska", "", "", ""], ["Eget försök", "", "", ""]], "tbl num")
 + '<p class="note">Säkerhet: Ha skyddsglasögon. Använd bara en tesked bikarbonat. Torka upp spill direkt. Ättika kan irritera ögonen, så skölj med vatten om du får stänk i ögat.</p>'
 + "<h3>Frågor</h3>"
 + steps(["Vad hände med massan i den slutna och i den öppna flaskan?", "Förklara skillnaden med vad som hände med gasen. Har några atomer försvunnit?", "Vilka felkällor finns? Hur kan du göra mätningen bättre?"], True))

SAMMAN = ["En <strong>kemisk förening</strong> är ett ämne där atomer av olika grundämnen är bundna till varandra med <strong>kemiska bindningar</strong>.",
          "I en <strong>kovalent bindning</strong> delar atomer elektronpar, oftast mellan icke-metaller. Atomerna bildar <strong>molekyler</strong>, som H₂O, CO₂ och CH₄. Molekylformeln visar vilka atomer och hur många.",
          "En <strong>jon</strong> är en laddad atom. En <strong>katjon</strong> är positiv (avger elektroner), en <strong>anjon</strong> är negativ (tar upp elektroner). Ex: Na⁺ och Cl⁻.",
          "<strong>Jonbindning</strong> är attraktionen mellan positiva och negativa joner. Metall plus icke-metall ger en jonförening (<strong>salt</strong>) med joner i ett <strong>kristallgitter</strong>.",
          "Jonföreningar har höga smältpunkter (NaCl ungefär 800 °C), molekylföreningar ofta låga. En jonförening leder ström när den är löst eller smält (<strong>elektrolyt</strong>) men inte som fast ämne.",
          "I en <strong>kemisk reaktion</strong> bildas nya ämnen. <strong>Utgångsämnen</strong> reagerar och <strong>produkter</strong> bildas. Tecken: gas, temperaturförändring, färgförändring, fast ämne, ljus eller lukt. En fysikalisk förändring ger inga nya ämnen.",
          "En <strong>reaktionsformel</strong> måste <strong>balanseras</strong>: lika många atomer av varje sort på båda sidor. Man sätter koefficienter framför formlerna och ändrar aldrig talen i formlerna.",
          "<strong>Massan bevaras</strong> i ett slutet system (Lavoisier). I en öppen behållare kan massan minska om en gas lämnar.",
          "<strong>Reaktionshastigheten</strong> ökar med temperatur, koncentration, ytarea och katalysator. Reaktioner kan vara <strong>exoterma</strong> (avger energi) eller <strong>endoterma</strong> (tar upp energi)."]

BEGR = [("Anjon", "Negativ jon."), ("Balansera", "Göra så att lika många atomer av varje sort finns på båda sidor."), ("Elektrolyt", "Ämne som leder ström när det är löst eller smält."), ("Endoterm", "Tar upp energi."),
        ("Exoterm", "Avger energi."), ("Fysikalisk förändring", "Samma ämne byter tillstånd eller form."), ("Jon", "Laddad atom."),
        ("Jonbindning", "Attraktion mellan positiva och negativa joner."), ("Jonförening", "Förening av joner, ofta en metall och en icke-metall."), ("Katalysator", "Ämne som ökar reaktionshastigheten utan att förbrukas."),
        ("Katjon", "Positiv jon."), ("Kemisk bindning", "Det som håller ihop atomer."), ("Kemisk förening", "Ämne med atomer av olika grundämnen bundna till varandra."), ("Kemisk reaktion", "Förändring där nya ämnen bildas."),
        ("Koefficient", "Talet framför en formel i en reaktionsformel."), ("Kovalent bindning", "Bindning där atomer delar elektronpar."), ("Kristallgitter", "Regelbundet mönster av joner."),
        ("Massans bevarande", "Massan är lika stor före och efter en reaktion i ett slutet system."), ("Molekyl", "Atomer som hålls ihop av kovalenta bindningar."),
        ("Molekylformel", "Visar vilka atomer och hur många som finns i molekylen."), ("Produkt", "Ämne som bildas i en reaktion."), ("Reaktionsformel", "Reaktion skriven med formler."),
        ("Reaktionshastighet", "Hur fort en reaktion går."), ("Salt", "Jonförening av en metall och en icke-metall."), ("Utgångsämne", "Ämne som reagerar. Kallas även reaktant.")]

TEST = [
 ("A", "Vad kallas en positivt laddad jon?", ["A Anjon", "B Katjon", "C Molekyl", "D Neutron"], 1, 0),
 ("A", "Vilken formel visar koldioxid?", ["A CO", "B C₂O", "C CO₂", "D Co"], 2, 0),
 ("A", "Vilket ämne leder elektrisk ström när det är löst i vatten?", ["A Socker", "B Bordssalt", "C Syre", "D Vätgas"], 1, 0),
 ("A", "Vilket är ett tecken på att en kemisk reaktion har skett?", ["A Is smälter", "B Socker löses i vatten", "C Det bildas bubblor av en ny gas när två ämnen blandas", "D Vatten kokar"], 2, 0),
 ("B", "Förklara skillnaden mellan en kovalent bindning och en jonbindning.", None, 2, 3),
 ("B", "Förklara vad som menas med att en reaktion är exoterm, och ge ett exempel.", None, 2, 3),
 ("C", "TABELL", None, 3, 5),
 ("C", "a) Balansera H₂ + Cl₂ → HCl och 2 Mg + O₂ → MgO (sätt koefficienter). b) Förklara varför man sätter tal framför formlerna men aldrig ändrar talen inne i formlerna.", None, 3, 5),
 ("D", "En elev blandar ättika och bikarbonat i en öppen flaska på en våg och ser att massan minskar. Hon säger: ”Då försvann atomer!” Bedöm påståendet, och förklara hur man kan göra försöket så att massan inte minskar.", None, 3, 6),
 ("D", "Förklara med natrium och klor hur en jonbindning bildas (valenselektroner, joner och laddning). Förklara också varför fast bordssalt inte leder ström men saltlösning gör det.", None, 3, 6),
 ("E", "Ett kylpaket blir kallt när man trycker så att två ämnen blandas. Förutsäg om reaktionen är exoterm eller endoterm, förklara energiomsättningen med bindningar och diskutera hur du kan kontrollera din slutsats.", None, 3, 7),
 ("E", "Bedöm påståendet ”En kemisk reaktion kan ändra massan eftersom nya atomer bildas”. Använd en reaktionsformel och förklara även hur temperatur och katalysator kan påverka hur fort reaktionen går.", None, 3, 7),
]
TEST_TABELL = (["Ämne", "Smältpunkt", "Leder fast ämne ström?", "Leder löst i vatten ström?"], [["X", "805 °C", "Nej", "Ja"], ["Y", "−78 °C", "Nej", "Nej"], ["Z", "660 °C", "Ja", "Löser sig inte"]])
TEST_D_TEXT = "Tre påhittade ämnen har undersökts. Värdena är påhittade men liknar riktiga ämnen."
TEST_D_SUB = ["a) Vilket ämne är troligen en jonförening, vilket en molekylförening och vilket en metall? Motivera med uppgifterna.", "b) Förklara varför ämne X leder ström löst i vatten men inte som fast ämne.", "c) Vad säger smältpunkten hos ämne Y om krafterna mellan dess partiklar?"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Tolka resultat och förklara", "D": "Resonera och ta ställning", "E": "Förutsäg och värdera"}
FACIT = [
 "B", "C", "B", "C",
 "I en kovalent bindning delar två atomer elektronpar, oftast mellan icke-metaller, och det ger molekyler. I en jonbindning flyttar en eller flera elektroner från en atom (oftast en metall) till en annan (oftast en icke-metall), så att positiva och negativa joner bildas som dras till varandra.",
 "Exoterm betyder att energi avges till omgivningen, som blir varmare. Exempel: förbränning, till exempel när metan brinner.",
 "a) X är troligen en jonförening (hög smältpunkt, leder löst men inte fast). Y är troligen en molekylförening (låg smältpunkt, leder inte). Z är troligen en metall (leder som fast ämne). b) I fast ämne sitter jonerna fast i gittret. När X löses i vatten kan jonerna röra sig fritt och bära strömmen. c) Den låga smältpunkten visar att krafterna mellan partiklarna är svaga, så det krävs lite energi för att få dem att röra sig.",
 "a) H₂ + Cl₂ → 2 HCl. 2 Mg + O₂ → 2 MgO. b) Koefficienterna visar hur många molekyler som reagerar och ändrar inte vilket ämne det är. Ändrar man talen inne i formeln byter man ut ämnet, till exempel blir H₂O₂ ett annat ämne än H₂O.",
 "Påståendet är fel. Atomer försvinner inte i kemiska reaktioner. När ättika och bikarbonat reagerar bildas koldioxid, en gas, som lämnar den öppna flaskan och tar sin massa med sig, så vågen visar mindre. Massan hos allt tillsammans, flaska, innehåll och gas, är oförändrad. Genom att låta reaktionen ske i en sluten flaska eller i en flaska med ballong, så att gasen stannar kvar, visar vågen samma massa före och efter. (Obs: ballongen ger en liten uppdrift, så vågen kan visa någon tiondels gram mindre. Det är en mätosäkerhet.)",
 "Natrium har en valenselektron (2, 8, 1) och avger den lätt. Då får atomen 2, 8, men fortfarande 11 protoner, så den blir en positiv natriumjon, Na⁺. Klor har sju valenselektroner (2, 8, 7) och tar upp en elektron, får 2, 8, 8 och laddningen −1: Cl⁻. De motsatta laddningarna drar mot varandra, och det är jonbindningen. I fast salt sitter jonerna fast i gittret och kan inte röra sig, så ingen laddning transporteras. I saltlösning har vattnet dragit loss jonerna, som kan röra sig och bära strömmen.",
 "Öppet svar. Ett välutvecklat svar: kylpaketet blir kallt, så energi tas upp från omgivningen: reaktionen är endoterm. Det beror på att det krävs mer energi för att bryta bindningarna i utgångsämnena än som avges när nya bildas. Slutsatsen kan kontrolleras genom att mäta temperaturen med termometer före och efter, upprepa försöket, jämföra med en kontroll (bara vatten) och se om temperaturen sjunker varje gång. Det kan också vara en lösning av ett salt som tar upp värme när det löses, vilket visar att man behöver mer än en iakttagelse.",
 "Påståendet är fel. Atomer skapas inte i kemiska reaktioner, de byter partner, så massan bevaras i ett slutet system. Exempel: 2 H₂ + O₂ → 2 H₂O har 4 H och 2 O på båda sidor. Högre temperatur gör att partiklarna krockar oftare och hårdare, så reaktionen går fortare. En katalysator ökar hastigheten utan att förbrukas, och ändrar inte massan eller vilka produkter som bildas i huvudsak.",
]
LGR = ("Området täcker det centrala innehållet i årskurs 7–9 om elektronöverföring och delade elektroner (förenklad bindningsmodell), partikelmodellen för kemiska reaktioner samt Lavoisier och massans bevarande. "
       "Delområde 4.1 behandlar kovalent bindning och molekyler, joner och jonföreningar och hur bindningstypen förklarar egenskaper som smältpunkt, löslighet och ledningsförmåga. Delområde 4.2 behandlar tecken på kemiska reaktioner, skillnaden mellan kemisk och fysikalisk förändring, att skriva och balansera enkla reaktionsformler, massans bevarande samt reaktionshastighet och energiomsättning. "
       "Labbarna tränar att undersöka ledningsförmåga hos lösningar och att väga före och efter en reaktion, planera, dokumentera och dra slutsatser. Uppgifterna följer betygskriteriernas progression från att beskriva till att förklara och värdera, och är inspirerade av frisläppta nationella prov i kemi. "
       "Anslutning till andra ämnen: kemiska reaktioner och energi förekommer också i biologi (fotosyntes, förbränning) och fysik (energiomvandling). I kemi ligger fokus på bindningar och reaktioner på partikelnivå.")
FAKTA = ("Kontrollerat mot öppna källor (2026-10-22): kovalent bindning som delade elektronpar mellan icke-metaller, exempel HCl, O₂ (dubbelbindning) och CH₄, molekylföreningars låga smält- och kokpunkter, att de inte leder ström och att vissa polära ämnen som socker löser sig (Cognito); jonbindning som elektronöverföring mellan metall och icke-metall, Na⁺ och Cl⁻, jonkristallgitter, höga smältpunkter, hårda men spröda, och ledning bara när löst eller smält (Cognito, TutorChase); natriumklorids smältpunkt ca 801–802 °C (TutorChase, Engineering ToolBox) och att vattenmolekyler drar loss jonerna vid upplösning (TutorChase); gasbubblor och temperaturfall vid ättika och bikarbonat, att massan blir lägre i öppen behållare och oförändrad i sluten samt säkerhetsråd (AACT); kollisionsteorin och faktorerna temperatur, koncentration, ytarea och katalysator samt exoterm och endoterm (Physics and Maths Tutor); Lavoisier och massans bevarande (Science History Institute). "
         "Ej källkontrollerat: att atomer vill ha fullt yttersta skal som förenklad förklaring, antalet bindningar för H, O, N och C (1, 2, 3, 4), definitionerna av kemisk förening, fysikalisk förändring, katjon och anjon, reaktionsformlerna och deras balansering, kranvattens ledningsförmåga, att enzymer och bilkatalysatorer är katalysatorer, förbränning som exoterm, att ballongen ger en liten uppdrift, att ättika och bikarbonat bildar koldioxid, vatten och natriumacetat, och att gas kan bildas vid elektroderna i labb 4.1. Alla exempelmätvärden är påhittade. "
         "Källor: Skolverket, Lgr22 kursplan i kemi. · Cognito, TutorChase, AACT, Physics and Maths Tutor, LibreTexts, Engineering ToolBox, Science History Institute. · Illustrationer: egenritade för detta kapitel.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven ser att atomer kan sitta ihop på olika sätt och att reaktioner ordnar om atomer. Låt eleverna skriva sin gissning om vätgas och syrgas (Fundera) och spara den. Vanligt fel: att ämnen ”försvinner” i reaktioner. Koppla till kapitel 3: valenselektroner avgör bindningen.</p>
<p><b>Molekyler och kovalent bindning.</b> C-mål: förklara hur bindningar bildas med delade elektroner och läsa molekylformler. Vanliga fel: att en kovalent bindning är en sorts ”klibbig” pinne, att H₂O är H₂ + O, och att elektronerna tillhör bara den ena atomen. Bygg modeller med modellkit eller tandpetare och gummibjörnar och kontrollera antal bindningar.</p>
<p><b>Joner och jonföreningar.</b> C-mål: förklara jonbildning med elektronskal och laddning. Vanliga fel: att en jon har fått fler protoner, att Na och Na⁺ är samma sak, och att jonföreningar är laddade som helhet. Låt eleverna räkna protoner och elektroner för Na, Na⁺, Cl och Cl⁻ i par. Magnesium och flervärda joner tas upp i fördjupningen.</p>
<p><b>Egenskaper hos föreningar.</b> A-mål: förklara egenskaper med bindningstypen. Vanliga fel: att vatten leder ström (rent vatten leder dåligt, men vanligt vatten innehåller salter) och att salt alltid leder. Koppla till kapitel 2 om lösningar. Siffran för saltets smältpunkt skiljer lite mellan källor (801–802 °C), skriv därför ”ungefär 800 °C”.</p>
<p><b>Labb 4.1 Leder lösningar elektrisk ström?</b> Material: batteri 4,5 V, glödlampa, grafitstavar eller blyertsstift som elektroder, destillerat vatten, saltvatten, sockervatten, kranvatten. Förväntat: saltvatten leder tydligt, sockervatten och destillerat vatten leder inte märkbart, kranvatten leder svagt (kan variera med vattnets halt av salter). Vanliga fel: att elektroderna rör varandra, att man inte sköljer mellan vätskorna. Håll försöket kort eftersom gas kan bildas vid elektroderna, och använd aldrig nätspänning.</p>
<p><b>Vad är en kemisk reaktion?</b> C-mål: ange tecken och skilja kemisk från fysikalisk förändring. Vanliga fel: att alla bubblor betyder reaktion, att lösa upp är en kemisk reaktion och att smältning är det. Ge fler fall att sortera.</p>
<p><b>Reaktionsformler och oförstörbarhet.</b> C-mål: balansera enkla formler och förklara massbevarande. Vanliga fel: att ändra talen inne i formlerna, att koefficienten gäller bara första atomen och att massan försvinner när något brinner. Låt eleverna räkna atomer med bilderna som stöd. Gasen från brinnande material väger också något.</p>
<p><b>Hastighet och energi.</b> A-mål: förklara hur temperatur, koncentration och ytarea påverkar hastigheten och resonera om energiomsättning. Vanliga fel: att en katalysator förbrukas och att alla reaktioner avger värme. Betona att modellen med krockar är en förklaring. Visa gärna brustablett i kallt och varmt vatten.</p>
<p><b>Labb 4.2 Massan bevaras.</b> Material: våg, flaskor, ballong, ättika, bikarbonat. Förväntat: i den slutna flaskan är massan i stort sett oförändrad (ballongens uppdrift kan ge någon tiondels gram), i den öppna flaskan minskar den med massan av gasen som lämnat. Vanliga fel: att lösa lock på för tätt (tryck) och att väga flaskan utan bägaren. Använd skyddsglasögon och en tesked bikarbonat.</p>
"""
LAB_HTML = ""

BONUS = dict(
 titel="Bygg molekyler och en saltkristall",
 ingress="Eleverna bygger modeller av molekyler och av ett jonkristallgitter och undersöker vad som skiljer dem. Kräver inga kemikalier.",
 syfte="Eleverna tränar att koppla bindning, formel och uppbyggnad och att använda modeller med insikt om deras begränsningar.",
 tid="Grupper om två till fyra.",
 material=["Modellkit eller gummibjörnar och tandpetare i fyra färger (väte, syre, kol, natrium/klor)", "Papper och penna", "Saltkorn eller förstoringsglas (valfritt)"],
 genomf=["Låt gruppen bygga H₂O, CO₂ och CH₄ och kontrollera att varje väte har 1, syre 2 och kol 4 bindningar.", "Skriv molekylformeln för varje modell och ange antal atomer.", "Bygg ett litet jongitter med två färger så att varje jon omges av motsatt laddade joner.", "Jämför: vad är en enskild enhet i molekylmodellen och i gittermodellen?", "Diskutera vad modellerna visar bra och vad de inte visar, till exempel att elektronerna inte är kulor och att verkligheten inte är platt.", "Förklara med modellerna varför salt smälter vid högre temperatur än vatten."],
 resultat="Eleverna ser att molekyler är avgränsade grupper av atomer, medan ett jongitter fortsätter åt alla håll och att jonföreningens formel anger förhållandet mellan jonerna.",
 sakerhet=["Använd inte godis som ska ätas om det varit i klassrummet; använd separata mängder.", "Tandpetare kan stickas: hantera försiktigt."],
 problem=["Eleverna ger kol fler eller färre än fyra bindningar: påminn om valenselektronerna.", "Gittermodellen blir ostabil: låt eleverna bygga ett plan först."],
 bedom=[("Grundläggande", "Bygger molekyler och skriver formler."), ("Utvecklat", "Förklarar hur bindningarna bildas med elektronerna."), ("Välutvecklat", "Använder modellerna för att förklara egenskaper och diskuterar modellernas begränsningar.")],
 forslag=["Vad är skillnaden mellan en molekylformel och en formel för en jonförening?", "Bygg koldioxid och förklara varför det behövs dubbelbindningar.", "Vad kan inte modellerna visa?"],
)
ELEV_HTML = ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
 '<div class="sh small"><h2>Bygg molekyler och en saltkristall</h2></div>'
 '<p><b>Frågeställning:</b> Vad skiljer en molekyl från ett jonkristallgitter?</p>'
 '<h3>Mina molekyler</h3><p>Molekylformel och antal bindningar för H₂O, CO₂ och CH₄:</p>' + lines(3) +
 '<h3>Mitt jongitter</h3><p>Så här omges varje jon:</p>' + lines(2) +
 '<h3>Frågor</h3><ol class="steps g"><li>Vad är lika och vad skiljer molekyl- och gittermodellen?</li></ol>' + lines(2) +
 '<ol class="steps g"><li>Vad visar modellerna inte? Hur kan det påverka dina slutsatser?</li></ol>' + lines(3) + '</section>')
RUTOR = []

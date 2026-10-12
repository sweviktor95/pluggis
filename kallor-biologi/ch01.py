# -*- coding: utf-8 -*-
"""Biologi kapitel 1 – Biologi som vetenskap. Källa för vanlig (+ komplett)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
FIG = '/tmp/bio/fig01/'
NR = 1
SLUG = "vetenskap"
TAB = "1"
NAMN = "Biologi som vetenskap"
UNDER = "Hur vet vi det vi vet om livet?"
INTRO = ("Hur vet forskare att fjällräven är hotad, att bakterier kan orsaka sjukdomar eller att växter behöver ljus? Ingen har bara bestämt det. "
         "Kunskapen kommer från människor som har varit nyfikna, ställt frågor och sedan noggrant undersökt naturen – i skogen, i havet och i laboratoriet. "
         "I det här kapitlet får du lära dig hur det går till, och hur du själv kan undersöka och granska som en forskare.")
MAL = ["vad biologi är och vad olika biologer arbetar med",
       "hur ny kunskap tas fram och granskas",
       "hur några viktiga upptäckter har ändrat vår bild av livet",
       "att planera en undersökning med frågeställning, hypotes och variabler",
       "att redovisa och värdera resultat",
       "att arbeta säkert i laboratoriet och använda mikroskop",
       "att skilja vetenskap från pseudovetenskap och granska källor"]
FUNDERA = "Tänk på något du ”vet” om naturen, till exempel att myggor gillar vissa personer mer än andra. Hur skulle du kunna ta reda på om det verkligen stämmer?"
LAB_TOC = "Undersök: gråsuggor"
LAB_FIND = "Undersök: Trivs"

S = []
def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)

# ---------------------------------------------------------------- 1.1
S.append(("1.1", "Vad är biologi?",
 row("<p>Biologi betyder ”läran om livet”. Ordet kommer från grekiskans <em>bios</em> (liv) och <em>logos</em> (lära). Biologi handlar om allt som lever: bakterier, svampar, växter, djur och människor. Biologer undersöker hur organismer är uppbyggda, hur de fungerar, hur de samspelar med varandra och med sin miljö, och hur livet har utvecklats.</p>"
     "<p>Biologi är en av <strong class='green'>naturvetenskaperna</strong>, tillsammans med bland annat kemi och fysik. Gemensamt för dem är att de försöker förklara naturen med hjälp av <strong class='green'>systematiska undersökningar</strong>, alltså undersökningar som görs noggrant och planerat, så att andra kan kontrollera och upprepa dem.</p>"
     "<h3>Biologer arbetar på många sätt</h3><p>Livet är så stort att ingen kan vara expert på allt. Därför specialiserar sig biologer på olika områden. Vissa arbetar ute i naturen, andra i laboratorier, på sjukhus eller vid en dator där de analyserar stora mängder data.</p>",
   [begrepp([("Biologi", "Läran om livet och levande organismer."),
             ("Organism", "En levande varelse, till exempel en bakterie, en svamp, en växt eller ett djur."),
             ("Naturvetenskap", "Vetenskaper som undersöker naturen, t.ex. biologi, kemi och fysik.")])])
 + fig(FIG+"v_yrken.png", "<b>Bild 1.1</b> Några av alla yrken inom biologin. Många biologer arbetar på universitet, myndigheter, sjukhus, företag eller naturvårdsorganisationer.")
 + kolla("1.1", ["Vad betyder ordet biologi?", "Vad menas med att en undersökning är systematisk?", "Välj två av yrkena i bild 1.1. Ge ett exempel på en fråga som var och en skulle kunna undersöka."])))

# ---------------------------------------------------------------- 1.2
S.append(("1.2", "Hur skaffar vi kunskap?",
 "<p>All forskning börjar med nyfikenhet. En forskare observerar något, till exempel att det finns färre humlor i ett område än för tio år sedan, och undrar varför. Sedan försöker hon ta reda på svaret med hjälp av en undersökning. Det finns flera sätt att undersöka.</p>"
 + cards([("Fältstudie", "Man undersöker naturen där den finns, utan att ändra på något. Ekologer kan till exempel räkna humlor på olika ängar."),
          ("Experiment", "Man ändrar en sak med flit och ser vad som händer, ofta i ett laboratorium. Man kan t.ex. testa om humlor föredrar blå eller gula blommor."),
          ("Modell och simulering", "Man gör en förenklad bild av verkligheten, ofta i en dator, för att förutsäga vad som kan hända – t.ex. hur humlorna påverkas av ett varmare klimat.")])
 + "<h3>Forskning är en cykel</h3>"
 + roww("<p>Arbetet följer ofta stegen i bild 1.2. Det viktiga är att svaret ska bygga på <strong class='green'>belägg</strong>, alltså observationer och mätningar, och inte på vad någon tycker eller tror.</p>"
        "<p>Ett resultat leder nästan alltid till nya frågor. Därför är forskning aldrig riktigt ”klar”.</p>"
        "<h3>Andra granskar</h3><p>När forskare är klara skriver de en vetenskaplig artikel. Innan den publiceras läser andra experter den och letar efter fel. Det kallas <strong class='green'>expertgranskning</strong> (på engelska <em>peer review</em>). Andra forskare kan också upprepa undersökningen. Om de får samma resultat blir kunskapen säkrare.</p>",
        [fig(FIG+"v_cykel.png", "<b>Bild 1.2</b> Den vetenskapliga arbetsgången. I verkligheten hoppar forskare ofta fram och tillbaka mellan stegen.")])
 + "<h3>Hypotes, teori och fakta</h3>"
 + "<p>En <strong class='green'>hypotes</strong> är ett möjligt svar på en fråga, som går att pröva. En <strong class='green'>teori</strong> är något mycket större: en förklaring som har prövats av många forskare under lång tid och som stämmer med väldigt många observationer. Evolutionsteorin och cellteorin är två exempel. När någon säger ”det är bara en teori” i vardagen menar de något helt annat än en forskare gör.</p>"
 + kolla("1.2", ["Vad är skillnaden mellan en fältstudie och ett experiment?", "Varför är det viktigt att andra forskare kan upprepa en undersökning?", "Förklara skillnaden mellan en hypotes och en teori."])))

# ---------------------------------------------------------------- 1.3
S.append(("1.3", "Upptäckter som ändrade biologin",
 "<p>Biologisk kunskap har vuxit fram under lång tid. Nya verktyg och nya undersökningar har gång på gång ändrat hur vi förstår livet. Ibland har gamla förklaringar fått ge vika för nya, bättre.</p>"
 + fig(FIG+"v_tidslinje.png", "<b>Bild 1.3</b> Några viktiga steg i biologins historia.")
 + '<div class="cols2"><h3 style="margin-top:0">Mikroskopet öppnade en ny värld</h3><p>På 1670-talet slipade holländaren Antonie van Leeuwenhoek egna linser. I en vattendroppe såg han små levande varelser som ingen människa hade sett förut. Mikroskopet gjorde det möjligt att upptäcka celler och mikroorganismer.</p>'
   "<h3>Linné gav arterna namn</h3><p>Svensken Carl von Linné skapade ett system för att ordna och namnge arter. Från 1750-talet fick varje art ett namn i två delar, till exempel <em>Bellis perennis</em> för tusensköna. Systemet används fortfarande.</p>"
   "<h3>Darwin förklarade mångfalden</h3><p>År 1859 gav Charles Darwin ut en bok om hur arter förändras genom <strong class='green'>naturligt urval</strong>. Han byggde sin teori på mängder av observationer från sina resor och från avel av djur.</p>"
   "<h3>DNA – livets kod</h3><p>År 1953 kunde James Watson och Francis Crick beskriva hur DNA-molekylen ser ut. De använde röntgenbilder som Rosalind Franklin och hennes kollegor hade tagit. Det visar att stora upptäckter ofta bygger på många forskares arbete.</p></div>"
 + "<h3>Ett klassiskt experiment: kan liv uppstå ur ingenting?</h3>"
 + roww("<p>Förr trodde många att små organismer kunde uppstå av sig själva i till exempel buljong som stod framme. Omkring år 1860 testade fransmannen Louis Pasteur den idén. Han kokade buljong i två sorters glaskolvar, så att alla mikroorganismer dog.</p>"
        "<p>Kolv A hade ett rakt rör. Damm och mikroorganismer från luften kunde falla ner i buljongen, och efter några dagar blev den grumlig. Kolv B hade en lång, böjd ”svanhals”. Luft kom in, men dammet fastnade i böjen. Buljongen förblev klar. Pasteurs slutsats: mikroorganismerna kommer från luften – de uppstår inte ur ingenting.</p>",
        [fig(FIG+"v_pasteur.png", "<b>Bild 1.4</b> Pasteurs svanhalskolvar.")])
 + kolla("1.3", ["Varför var mikroskopet så viktigt för biologin?", "Varför var det viktigt att luft kunde komma in i båda Pasteurs kolvar?", "Ge ett exempel på hur en gammal förklaring har ersatts av en ny."])))

# ---------------------------------------------------------------- 1.4
S.append(("1.4", "Planera en undersökning",
 "<p>Klass 7B undrar om krasse behöver ljus för att växa. Så här kan de planera ett experiment som ger ett tillförlitligt svar.</p>"
 + fig(FIG+"v_krasse.png", "<b>Bild 1.5</b> Krasse som har vuxit i sju dagar i ljus (A) och i en mörk låda (B). Lådans framsida är bortklippt på bilden.")
 + '<div class="cols2"><h3 style="margin-top:0">1. Frågeställning</h3><p>En bra frågeställning går att undersöka och besvara med mätningar: <em>Påverkar ljus hur högt krasse växer på en vecka?</em></p>'
   "<h3>2. Hypotes</h3><p>Klassen tror: <em>Krassen i ljus växer högre, eftersom växter behöver ljus för fotosyntesen.</em> En hypotes ska ha en motivering – den är inte bara en gissning.</p>"
   "<h3>3. Variabler – ändra bara en sak</h3><p>En <strong class='green'>variabel</strong> är något som kan ändras eller mätas i en undersökning. För att testet ska bli rättvist får bara en variabel ändras åt gången. Allt annat måste vara lika – annars vet man inte vad som orsakade resultatet. Ofta jämför man med en <strong class='green'>kontrollgrupp</strong>, där man inte ändrar något.</p></div>"
 + table(["Typ av variabel", "Vad betyder det?", "I krassförsöket"],
         [["Oberoende variabel", "Det du själv ändrar med flit.", "Ljus eller mörker"], ["Beroende variabel", "Det du mäter – det som kanske påverkas.", "Krassens höjd i mm"],
          ["Kontrollerade variabler", "Allt annat, som måste vara lika i båda försöken.", "Jord, vatten, temperatur, antal frön, tid"]])
 + row(box("fundera", "Upprepa!", "<p>Klassen sår krasse i tre lådor av varje sort och mäter tio plantor i varje låda. Ju fler mätningar, desto mindre påverkar slumpen resultatet.</p>"), None).replace("row one", "row one")
 + kolla("1.4", ["Vad är skillnaden mellan oberoende och beroende variabel?", "Varför ska bara en variabel ändras åt gången?"])))

# ---------------------------------------------------------------- 1.5
S.append(("1.5", "Resultat och slutsatser",
 "<p>Under försöket mäter klassen krassen varje dag och skriver in mätvärdena i en tabell. Sedan räknar de ut <strong class='green'>medelvärdet</strong> för varje grupp: de lägger ihop alla värden och delar med antalet värden.</p>"
 + roww(table(["Dag", "0", "1", "2", "3", "4", "5", "6", "7"], [["A · ljus (mm)", "0", "0", "5", "12", "20", "27", "33", "38"], ["B · mörker (mm)", "0", "0", "7", "17", "28", "40", "50", "58"]], "tbl num")
        + '<p class="cap" style="margin-top:-4pt"><b>Tabell 1.1</b> Medelhöjd för krassen i klassens försök (exempelresultat).</p>'
        "<p>Ett diagram gör det lättare att se mönster. När något förändras över tid passar ett linjediagram bra. Tiden sätts på x-axeln och det man mäter på y-axeln. Glöm inte rubriker och enheter på axlarna!</p>"
        "<h3>En överraskning</h3><p>Resultatet stämde inte med hypotesen. Krassen i mörker blev högre! Men den var också gul, tunn och vek. Växter i mörker lägger all sin energi på att växa på höjden för att nå ljuset. Fröets näring tar snart slut, och utan ljus kan växten inte göra fotosyntes.</p>",
        [fig(FIG+"v_diagram.png", "<b>Bild 1.6</b> Krassens medelhöjd under sju dagar.")])
 + "<h3>Värdera resultatet</h3><p>En forskare frågar sig alltid: Kan jag lita på resultatet? Mätte vi rätt sak?</p>"
 + bullets(["<strong>Felkällor</strong> är saker som kan ha påverkat resultatet utan att vi ville det. Kanske fick lådorna olika mycket vatten, eller så var det varmare inne i den mörka lådan.",
            "<strong>Tillförlitlighet</strong> handlar om hur säkra mätningarna är. Skulle vi få samma resultat om vi gjorde om försöket?",
            "<strong>Giltighet</strong> handlar om huruvida vi har mätt det vi ville veta. Är höjden ett bra mått på om krassen ”växer bra”? Det hade kanske varit bättre att väga krassen eller titta på färgen."])
 + roww("<h3 style='margin-top:2pt'>Slutsats</h3><p>Klassens slutsats: Krasse som växer i mörker blir högre men svagare än krasse i ljus. Höjden är inte ett bra mått på hur bra en växt mår. En ny fråga väcks: <em>Hur mycket väger krassen?</em></p>",
        [begrepp([("Medelvärde", "Summan av alla värden delat med antalet värden."), ("Felkälla", "Något som kan ha påverkat resultatet utan att man ville det."),
                  ("Tillförlitlighet", "Hur säkra och upprepbara mätningarna är."), ("Giltighet", "Om man har mätt det man ville undersöka.")]),
         box("visste", "Bra att veta", "<p>Ett resultat som inte stämmer med hypotesen är inte ett misslyckande. Det är så forskningen går framåt!</p>")])))

# ---------------------------------------------------------------- 1.6
S.append(("1.6", "I laboratoriet",
 "<p>I ett laboratorium kan forskare göra experiment under kontrollerade förhållanden. I skolans NO-sal finns mycket av samma utrustning som i ett riktigt labb. Det är viktigt att känna till vad sakerna heter och hur de används.</p>"
 + fig(FIG+"v_utrustning.png", "<b>Bild 1.7</b> Vanlig utrustning i ett biologilabb. Volym mäts noggrannast med mätcylinder eller pipett – strecken på en bägare visar bara ungefär.")
 + "<h3>Säkerhet först</h3>"
 + roww(steps(["Lyssna på instruktionerna och läs hela labbinstruktionen innan du börjar.", "Använd skyddsglasögon och förkläde när läraren säger det. Sätt upp långt hår.",
               "Ät, drick eller smaka aldrig något i labbet.", "Lukta försiktigt genom att vifta lukten mot dig – aldrig direkt över ett kärl.",
               "Säg till direkt om något går sönder eller om du skadar dig.", "Diska, städa och tvätta händerna när du är klar."]),
        [box("varning", "Faroetiketter", "<p>Kemikalier som kan vara farliga har en varningssymbol på förpackningen: en svart bild i en vit ruta med röd kant. Läs alltid etiketten innan du använder något.</p>"),
         box("tank", "Tänk efter", "<p>Varför är det viktigt att aldrig äta i labbet, även om man bara använder ofarliga saker just den dagen?</p>")])
 + "<h3>Skriva en labbrapport</h3><p>När du har gjort en undersökning redovisar du den i en labbrapport. Den ska vara så tydlig att någon annan kan göra om försöket och kontrollera ditt resultat.</p>"
 + '<div class="cards" style="grid-template-columns:repeat(5,1fr)">' + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in [
      ("Syfte och frågeställning", "Vad vill du ta reda på?"), ("Hypotes", "Vad tror du och varför?"), ("Material och metod", "Vad använde du och hur gjorde du?"),
      ("Resultat", "Vad hände? Tabeller och diagram."), ("Diskussion och slutsats", "Vad betyder resultatet? Felkällor?")]) + '</div>'))

# ---------------------------------------------------------------- 1.7
S.append(("1.7", "Mikroskopet",
 "<p>De flesta organismer och nästan alla celler är för små för att synas med blotta ögat. Ett <strong class='green'>ljusmikroskop</strong> förstorar upp till ungefär 1 000 gånger. Ljuset går nerifrån, genom preparatet, och sedan genom två linser: objektivet och okularet.</p>"
 + roww("<h3 style='margin-top:0'>Räkna ut förstoringen</h3><p>Både okularet och objektivet förstorar. På varje lins står hur många gånger den förstorar, till exempel 10× eller 40×. Den totala förstoringen räknar du ut så här:</p>"
        '<div class="sam" style="text-align:center;font-weight:700"><span class="mut" style="font-weight:400">okularets förstoring × objektivets förstoring</span><br><span class="green">10× · 40× = 400 gångers förstoring</span></div>'
        "<h3>Så använder du mikroskopet</h3>" + steps(["Börja alltid med det minsta objektivet.", "Lägg preparatet på objektbordet och fäst det med klämmorna.",
          "Titta från sidan och vrid med grovinställningen tills objektivet nästan nuddar glaset.", "Titta i okularet och vrid sakta uppåt tills bilden blir skarp.",
          "Finjustera med fininställningen. Byt sedan till större objektiv om du vill."]),
        [fig(FIG+"v_mikroskop.png", "<b>Bild 1.8</b> Ljusmikroskopets delar.")])
 + "<h3>Gör ett preparat av lökhinna</h3>"
 + roww(steps(["Droppa en droppe vatten på ett objektglas med pipetten.", "Dra loss den tunna hinnan på insidan av en lökbit med pincetten.", "Lägg hinnan slätt i vattendroppen. Undvik veck.",
               "Sänk ner täckglaset snett från ena sidan med preparatnålen, så att det inte blir luftbubblor.", "Tillsätt gärna en droppe jodlösning vid kanten. Då syns cellkärnorna tydligare."], g=True),
        [fig(FIG+"v_lok.png", "<b>Bild 1.9</b> Lökceller i mikroskop, ca 100×.", "42mm")])
 + box("tank", "Utmaning", "<p>Rita det du ser. Skriv vilken förstoring du använde. Hur många celler ser du i synfältet vid 100× och vid 400×? Förklara skillnaden.</p>")))

# ---------------------------------------------------------------- 1.8
S.append(("1.8", "Vetenskap eller pseudovetenskap?",
 "<p>Ibland låter något vetenskapligt fast det inte är det. Det kallas <strong class='green'>pseudovetenskap</strong> – ”pseudo” betyder falsk. Pseudovetenskap använder gärna ord som ”forskare”, ”naturligt” eller ”kliniskt bevisat”, men påståendena har inte prövats ordentligt eller har prövats och visat sig vara fel.</p>"
 + table(["Vetenskap", "Pseudovetenskap"], [
     ["Påståenden går att pröva och kan visa sig vara fel.", "Påståenden är vaga eller går inte att pröva."],
     ["Bygger på systematiska undersökningar med många deltagare.", "Bygger på enstaka berättelser: ”Det funkade för mig!”"],
     ["Granskas av andra experter innan det publiceras.", "Granskas inte, eller bara av den som säljer något."],
     ["Ändrar sig när nya belägg kommer fram.", "Håller fast vid idén, vad undersökningarna än visar."],
     ["Redovisar osäkerheter och felkällor.", "Lovar säkra och enkla resultat."]], "tbl num")
 + '<div class="cols2"><h3 style="margin-top:0">Exempel: homeopati</h3><p>Inom homeopati späds ett ämne ut i vatten så många gånger att det ofta inte finns en enda molekyl av ämnet kvar. Stora sammanställningar av forskningen visar att homeopatiska medel inte fungerar bättre än <strong class="green">placebo</strong>, alltså sockerpiller utan verksamt ämne.</p>'
   "<h3>Placeboeffekten</h3><p>Om man tror att en behandling hjälper kan man faktiskt må lite bättre – även om pillret är tomt. Därför jämför forskare ofta en ny medicin med placebo. I de bästa studierna vet varken deltagarna eller forskarna vem som fått vad.</p>"
   "<h3>Även forskare kan ha fel</h3><p>År 1998 publicerade en brittisk läkare en studie med tolv barn, som påstod att ett vaccin kunde orsaka autism. Andra forskare försökte upprepa resultatet men lyckades inte. Det visade sig att studien var fusk. Den drogs tillbaka 2010 och läkaren förlorade sin legitimation. Stora studier med hundratusentals barn har inte hittat något samband.</p>"
   "<p>Exemplet visar både en svaghet och en styrka: enskilda forskare kan göra fel – studien klarade till och med granskningen – men när andra forskare upprepade undersökningen avslöjades felet till slut.</p></div>"
 + "<h3>Samband är inte samma sak som orsak</h3>"
 + roww("<p>När glassförsäljningen ökar, ökar också antalet drunkningsolyckor. Betyder det att glass gör att man drunknar? Nej! Båda beror på en tredje sak: värmen. När det är varmt äter fler glass, och fler badar. Två saker kan alltså ändras samtidigt utan att den ena orsakar den andra. Det kallas att det finns en <strong class='green'>korrelation</strong> men inget orsakssamband.</p>",
        [fig(FIG+"v_glass.png", "<b>Bild 1.10</b> Två kurvor som följer varandra.")])))

# ---------------------------------------------------------------- 1.9
S.append(("1.9", "Granska information",
 "<p>Varje dag möter du påståenden om hälsa, mat, djur och miljö – i sociala medier, reklam, nyheter och samtal. Att granska källor kritiskt betyder att du ställer frågor om informationen innan du tror på den eller sprider den vidare. Fyra frågor brukar kallas de <strong class='green'>källkritiska kriterierna</strong>.</p>"
 + '<div class="cards" style="grid-template-columns:repeat(4,1fr)">' + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in [
      ("Äkthet", "Är källan den den utger sig för att vara? Är bilden eller citatet äkta?"), ("Tid", "När skrevs det? Är informationen fortfarande aktuell?"),
      ("Beroende", "Var kommer uppgifterna ifrån? Har avsändaren själv undersökt, eller bara hört från någon annan?"),
      ("Tendens", "Vill avsändaren något – sälja, övertyga eller påverka? Visas flera sidor av saken?")]) + '</div>'
 + fig(FIG+"v_inlagg.png", "<b>Bild 1.11</b> Ett påhittat inlägg i sociala medier, granskat med de källkritiska kriterierna.")
 + roww("<h3 style='margin-top:0'>Tips för att kontrollera</h3>" + bullets([
        "<strong>Sök efter källan.</strong> Finns studien? Vilka har gjort den, och hur många deltog?",
        "<strong>Jämför flera källor.</strong> Vad säger till exempel Folkhälsomyndigheten, Livsmedelsverket eller ett universitet?",
        "<strong>Var extra misstänksam</strong> mot rubriker med många utropstecken, ord som ”chockade” och löften som låter för bra för att vara sanna.",
        "<strong>Tänk på dina egna känslor.</strong> Vi tror lättare på sådant vi redan tycker eller vill ska vara sant."]),
        [box("tank", "Diskutera", "<p>Ett skogsbolag, en miljöorganisation och en lärobok beskriver skogsbruk. Hur tror du att texterna skiljer sig åt? Vilken har mest tendens?</p>")])
 + kolla("1.8–1.9", ["Ge två kännetecken på pseudovetenskap.", "Vad är placebo, och varför jämför man nya mediciner med placebo?", "Förklara med ett eget exempel skillnaden mellan samband och orsak.", "Vilka är de fyra källkritiska kriterierna?"])))

# ---------------------------------------------------------------- Undersök (elevlabb)
LAB_HTML = (
 '<div class="sh small"><h2>Undersök: Trivs gråsuggor bäst i ljus eller mörker?</h2></div>'
 "<p>Nu är det din tur att genomföra en hel undersökning, steg för steg. Gråsuggor finns under stenar, brädor och löv nästan överallt. De är ofarliga och lätta att samla in. Du ska använda allt du har lärt dig om frågeställning, hypotes, variabler och upprepning.</p>"
 + fig(FIG+"v_valkammare.png", "<b>Bild 1.12</b> En valkammare. Bara ljuset skiljer de två sidorna åt – fuktigheten är densamma.")
 + row("<p><strong class='green'>Frågeställning:</strong> Väljer gråsuggor ljus eller mörker?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror och motivera. Tänk på var du brukar hitta gråsuggor.</p>"
       "<p><strong class='green'>Material:</strong> låda eller stor petriskål, svart papper eller folie, fuktigt hushållspapper, pensel, 10 gråsuggor, klocka.</p>"
       "<h3>Gör så här</h3>" + steps(["Lägg fuktigt papper i hela botten av lådan. Täck över ena halvan med svart papper.", "Flytta gråsuggorna försiktigt med penseln och släpp dem i mitten.",
          "Räkna hur många som är på den mörka respektive ljusa sidan varje minut i 10 minuter.", "Byt plats på den mörka och den ljusa sidan och gör om försöket.",
          "Räkna ut medelvärdet och rita ett diagram.", "Släpp tillbaka djuren där du hittade dem."]),
       [table(["Minut", "1", "2", "3", "4", "5", "…", "10"], [["Mörker", "", "", "", "", "", "", ""], ["Ljus", "", "", "", "", "", "", ""]], "tbl num"),
        box("begrepp", "Variabler", "<b class='t'>Oberoende</b><p>Ljus eller mörker.</p><b class='t'>Beroende</b><p>Antal gråsuggor på varje sida.</p><b class='t'>Kontrollerade</b><p>Samma fuktighet och temperatur, samma djur, samma tid.</p>"),
        box("tank", "Utvärdera", "<p>Stämde hypotesen? Varför byter man plats på sidorna i steg 4? Vad kan gråsuggornas val ha för betydelse för deras överlevnad i naturen?</p>")]))

SAMMAN = ["<strong>Biologi</strong> är läran om livet. Biologer arbetar inom många områden, i fält, i labb och vid datorer.",
          "Kunskap tas fram med fältstudier, experiment och modeller. Resultaten granskas av andra forskare och upprepas.",
          "En <strong>hypotes</strong> är ett prövbart svar på en fråga. En <strong>teori</strong> är en väl prövad förklaring med många belägg.",
          "Upptäckter som mikroskopet, Pasteurs försök och DNA:s struktur har ändrat vår bild av livet.",
          "I en undersökning ändrar man bara en variabel i taget och håller allt annat lika. Man upprepar för att minska slumpens betydelse.",
          "Resultat redovisas i tabeller och diagram och värderas med tanke på felkällor, tillförlitlighet och giltighet.",
          "Pseudovetenskap låter vetenskapligt men bygger inte på prövade belägg. Samband betyder inte alltid orsak.",
          "Granska information med de källkritiska kriterierna: äkthet, tid, beroende och tendens."]
BEGR = [("Belägg", "Observationer och mätningar som stöder en slutsats."), ("Beroende variabel", "Det man mäter i en undersökning."),
        ("Experiment", "Undersökning där man ändrar något med flit och ser vad som händer."), ("Felkälla", "Något som kan ha påverkat resultatet utan att man ville det."),
        ("Fältstudie", "Undersökning av naturen där den finns."), ("Frågeställning", "Den fråga en undersökning ska besvara."),
        ("Giltighet", "Om man har mätt det man ville undersöka."), ("Granskning", "När andra experter kontrollerar forskning innan den publiceras."),
        ("Hypotes", "Ett möjligt, prövbart svar på en fråga."), ("Kontrollerade variabler", "Det som hålls lika för att testet ska bli rättvist."),
        ("Korrelation", "När två saker ändras samtidigt. Samband, men inte alltid orsak."), ("Medelvärde", "Summan av alla värden delat med antalet värden."),
        ("Oberoende variabel", "Det man själv ändrar i en undersökning."), ("Placebo", "Behandling utan verksamt ämne, t.ex. sockerpiller."),
        ("Pseudovetenskap", "Något som låter vetenskapligt men inte bygger på prövade belägg."), ("Teori", "En väl prövad förklaring som stöds av många belägg."),
        ("Tillförlitlighet", "Hur säkra och upprepbara mätningarna är.")]

ANNONS = ('<div style="border:1pt solid #d9d2c8;border-radius:5pt;padding:5pt 8pt;margin:3pt 0"><b>NYHET! DetoxPlåstret™</b><br>Sätt plåstret under foten när du sover – på morgonen har det blivit brunt av alla gifter som dragits ut ur kroppen! ”Jag har aldrig mått så bra”, säger Anna, 34. Vetenskapligt utvecklat. Endast 399 kr för 10 st!</div>')
TEST = [
 ("A", "Elin undersöker om temperaturen påverkar hur mycket gas jäst bildar. Hon mäter mängden gas efter 20 minuter. Vilken är den beroende variabeln?", ["A Temperaturen", "B Mängden gas", "C Mängden jäst", "D Tiden, 20 minuter"], 1, 0),
 ("A", "Vilket påstående går att undersöka med naturvetenskapliga metoder?", ["A Blåbär smakar godare än lingon.", "B Krasse gror snabbare vid 20 °C än vid 10 °C.", "C Det är fel att jaga varg.", "D Naturen vill alltid vara i balans."], 1, 0),
 ("A", "Ett mikroskop har ett okular som förstorar 10× och ett objektiv som förstorar 40×. Hur mycket förstoras bilden totalt?", ["A 4 gånger", "B 50 gånger", "C 400 gånger", "D 4 000 gånger"], 1, 0),
 ("B", "Ge två säkerhetsregler för arbete i laboratoriet och förklara varför de är viktiga.", None, 1, 4),
 ("B", "Förklara varför en forskare bör upprepa ett försök flera gånger.", None, 2, 4),
 ("C", "Noah vill ta reda på om gödning påverkar hur mycket ärtplantor växer. Han har tillgång till ärtfrön, krukor, jord, vatten, flytande gödning och en linjal. Planera undersökningen. Skriv<br>a) en frågeställning och en hypotes,<br>b) vilken som är den oberoende och den beroende variabeln,<br>c) minst tre variabler som ska hållas lika,<br>d) hur Noah ska göra för att resultatet ska bli tillförlitligt.", None, 3, 7),
 ("D", "TABELL", None, 2, 5),
 ("E", "Läs annonsen och svara på frågorna." + ANNONS + "a) Använd de källkritiska kriterierna. Ge två skäl till att vara skeptisk.<br>b) Hur skulle man kunna undersöka om plåstret verkligen drar ut gifter? Beskriv ett försök. ●●●", None, 2, 6),
 ("F", "En undersökning visar att elever som äter frukost får bättre betyg. Ludvig säger: ”Då ska alla äta frukost, så blir betygen bättre!” Har Ludvig rätt? Resonera kring samband och orsak och ge exempel på andra förklaringar.", None, 3, 5),
]
TEST_TABELL = (["Temperatur", "Försök 1", "Försök 2", "Försök 3", "Medelvärde"], [["10 °C", "13 cm", "12 cm", "14 cm", ""], ["25 °C", "22 cm", "24 cm", "23 cm", ""], ["40 °C", "31 cm", "18 cm", "30 cm", ""]])
TEST_D_TEXT = "En grupp undersökte hur temperaturen påverkar jäst. De blandade jäst, socker och vatten i flaskor och satte en ballong över varje flaska. Efter 30 minuter mätte de ballongens omkrets. De gjorde tre försök vid varje temperatur."
TEST_D_SUB = ["a) Räkna ut medelvärdet för 10 °C och 25 °C.", "b) Ett av värdena skiljer sig mycket från de andra. Vilket? Ge en möjlig felkälla.", "c) Vilken slutsats kan gruppen dra? ●●●"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Planera en undersökning", "D": "Tolka resultat", "E": "Granska information", "F": "Resonera"}
FACIT = [
 "B", "B", "C",
 "T.ex. skyddsglasögon (skyddar ögonen mot stänk), ät aldrig i labbet (kemikalier eller bakterier kan komma in i kroppen), säg till om något går sönder (glassplitter och spill kan skada andra).",
 "Ett enskilt försök kan påverkas av slumpen eller av ett misstag. Med flera försök kan man räkna ut ett medelvärde och upptäcka avvikande värden. Resultatet blir mer tillförlitligt.",
 "a) T.ex. Växer ärtplantor högre om de får gödning? Hypotes med motivering, t.ex. att gödning innehåller näringsämnen som växter behöver. b) Oberoende: mängd gödning (med/utan eller olika mängder). Beroende: plantans höjd (eller massa). c) Samma jord, mängd vatten, ljus, temperatur, krukstorlek, antal frön, tid. d) Flera krukor per grupp, mäta flera plantor, räkna ut medelvärde, en kontrollgrupp utan gödning, mäta på samma sätt varje gång.",
 "a) 10 °C: (13 + 12 + 14) / 3 = 13 cm. 25 °C: (22 + 24 + 23) / 3 = 23 cm. b) 18 cm vid 40 °C. Felkällor: ballongen satt löst och gas läckte ut, fel mängd jäst eller socker, mätfel. c) Ju varmare (upp till 40 °C), desto mer gas bildar jästen. Ett välutvecklat svar nämner att 18 cm bör räknas bort eller att försöket bör göras om.",
 "a) Tendens: företaget säljer plåstret. Beroende: ingen källa till ”vetenskapligt utvecklat”. Anekdot: en persons upplevelse är inget belägg. b) T.ex. sätt plåster på en svamp med rent vatten eller under fötterna på flera personer. Om plåstret blir brunt även utan ”gifter” beror färgen på fukt (svett). Jämför med vanliga plåster.",
 "Nej, ett samband behöver inte betyda orsak. Andra förklaringar: elever som äter frukost kanske sover mer, har mer stöd hemma eller mår bättre av andra skäl. För att visa orsak behövs ett experiment där bara frukosten skiljer sig mellan grupperna.",
]
LGR = ("Kapitlet behandlar det centrala innehållet om fältstudier och experiment: planering, utförande och värdering av resultat samt dokumentation med bilder, tabeller och diagram (1.2, 1.4–1.7). "
       "Digitala verktyg (t.ex. dataloggrar, digitalmikroskop och artappar) kan med fördel användas i labbarna. Avsnitt 1.3 tar upp de biologiska förklaringsmodellernas historiska framväxt och föränderlighet. "
       "Avsnitt 1.8–1.9 tränar kritisk granskning av information och argument i frågor som rör miljö och hälsa. Uppgifterna följer uppläggningen i de nationella proven, där ett delprov prövar förmågan att genomföra systematiska undersökningar.")
FAKTA = ("Krassresultaten och jästdata är exempelvärden för undervisning. Att växter i mörker sträcker sig och blir bleka (etiolering) är väl belagt och kan gärna testas i klassrummet. "
         "Källor: Skolverket: Läroplan för grundskolan (Lgr22), kursplan i biologi, samt kommentarmaterial till kursplanen i biologi. · Skolverket: information om nationellt prov i biologi årskurs 9. · "
         "Skolverket, Lärportalen: Att genomföra systematiska undersökningar. · Illustrationer: egenritade för detta kapitel.")
BONUS = dict(
 titel="Hur snabbt reagerar du?",
 ingress="En enkel men fullständig undersökning med bara en linjal. Eleverna mäter sin reaktionstid och undersöker själva vad som påverkar den.",
 syfte="Eleverna planerar och genomför en egen kontrollerad undersökning med upprepningar, medelvärde och värdering. Passar som övning inför delprovet om systematiska undersökningar i det nationella provet.",
 tid="40–60 minuter. Par eller grupper om tre: en släpper, en fångar, en antecknar.",
 material=["30 cm-linjal (en per grupp)", "Elevblad", "Valfritt: telefon för att mäta tid med stoppur som jämförelse"],
 genomf=["Låt grupperna själva välja frågeställning och formulera hypotes.", "Den som fångar sitter med armen vilande på bordskanten.", "Släpp linjalen på olika tidpunkter så att fångaren inte kan gissa.",
         "Minst 5, gärna 10 försök per person och villkor. Räkna medelvärde.", "Omvandla centimeter till tid med tabellen på elevbladet."],
 resultat="Typiska värden ligger runt 15–25 cm, alltså ungefär 0,17–0,23 sekunder. Reaktionen kräver att ögat uppfattar rörelsen, att signalen går via nerver till hjärnan och att hjärnan skickar en signal till handens muskler. Skillnaden mellan händerna är ofta liten. Träningseffekt syns ofta de första försöken. Tabellen bygger på formeln t = √(2s/g).",
 sakerhet=["Inga särskilda risker. Påminn om att linjalen ska släppas rakt ner och inte kastas."],
 problem=["Fångaren gissar och fångar i förväg (ger orimligt korta tider – stryk dem).", "Handen rör sig nedåt med linjalen.", "Olika startläge för fingrarna."],
 forslag=["Reagerar man snabbare med sin starka hand?", "Blir reaktionstiden kortare med träning (10 försök i rad)?", "Reagerar man snabbare på ljud än på syn? (Fångaren blundar och den som släpper säger ”nu”.)", "Påverkar det om man räknar baklänges samtidigt?"],
 bedom=[("Grundläggande", "Genomför försöket enligt plan och redovisar resultat i tabell."), ("Utvecklat", "Väljer och motiverar variabler, gör upprepningar och räknar medelvärde. Drar en slutsats."),
        ("Välutvecklat", "Värderar tillförlitligheten, diskuterar felkällor och föreslår välgrundade förbättringar.")])

ELEV_HTML = ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
  '<div class="sh small"><h2>Hur snabbt reagerar du?</h2></div>'
  + row(fig(FIG+"v_linjal.png"), [table(["Fallsträcka", "Reaktionstid"], [["5 cm", "101 ms"], ["10 cm", "143 ms"], ["15 cm", "175 ms"], ["20 cm", "202 ms"], ["25 cm", "226 ms"], ["30 cm", "247 ms"]], "tbl num")
        + '<p class="note">ms = millisekunder (tusendels sekunder)</p>']).replace('class="row"', 'class="row w"', 1)
  + row("<h3>Gör så här</h3>" + steps(["Fångaren vilar underarmen mot bordskanten. Tummen och pekfingret är öppna vid 0 på linjalen.", "Släpp linjalen utan förvarning. Fångaren nyper så snabbt som möjligt.",
          "Läs av var fingrarna fångade linjalen, i cm.", "Gör minst 5 försök för varje villkor. Räkna ut medelvärdet."], True)
        + "<p>Vår frågeställning:</p>" + lines(2) + "<p>Vår hypotes (med motivering):</p>" + lines(2) + "<p>Oberoende variabel:</p>" + lines(1) + "<p>Beroende variabel:</p>" + lines(1) + "<p>Kontrollerade variabler:</p>" + lines(2),
        [table(["Försök", "1", "2", "3", "4", "5", "Medel"], [["Villkor A (cm)", "", "", "", "", "", ""], ["Villkor B (cm)", "", "", "", "", "", ""]], "tbl num")
         + "<p>Slutsats:</p>" + lines(3) + "<p>Felkällor och förbättringar:</p>" + lines(3) + "<p>Vilka organsystem behövs för att du ska kunna fånga linjalen?</p>" + lines(2)]).replace('class="row"', 'class="row w"', 1)
  + '</section>')

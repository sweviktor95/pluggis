# -*- coding: utf-8 -*-
"""Kemi område 2 Materia och partiklar – grundtext (per moment). Samma format som område 1."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
FIG = '/tmp/kem/fig02k/'
NR = 2
SLUG = "kemi-materia"
TAB = "2"
NAMN = "Materia och partiklar"
UNDER = "Allt består av partiklar"
INTRO = ("Varför flyter is på vatten men en järnbult sjunker? Varför kan du känna doften av nybakat bröd från ett annat rum? Och hur får man tillbaka saltet när det har löst sig i vatten? "
         "Allt omkring dig är gjort av materia, och för att förklara hur materia beter sig använder kemister en modell: allt består av små partiklar som hela tiden rör sig. "
         "I det här kapitlet lär du dig vad som kännetecknar olika ämnen, hur partikelmodellen förklarar fast, flytande och gasformigt tillstånd, vad som skiljer rena ämnen från blandningar och hur man kan skilja ämnen från varandra. "
         "Namn och mätvärden i uppgifterna är påhittade, om inget annat står.")
MAL = ["hur du beskriver ämnen med egenskaper som densitet, smältpunkt, kokpunkt och löslighet", "hur du räknar ut densitet och förutsäger om något flyter eller sjunker",
       "hur partikelmodellen förklarar fast, flytande och gasformigt tillstånd", "hur partikelmodellen förklarar tillståndsförändringar, diffusion och tryck, och vad den inte visar",
       "skillnaden mellan rena ämnen och blandningar, och mellan homogena och heterogena blandningar", "hur du separerar blandningar med filtrering, avdunstning, destillation och kromatografi",
       "hur du kan identifiera ämnen och vad en fällning är"]
FUNDERA = "Tänk dig en kopp varmt te. Du lägger i en sockerbit utan att röra om. Efter en stund smakar det sött hela vägen. Hur tror du att sockret har kommit dit? Skriv din förklaring och spara den. I slutet av kapitlet får du se om du ändrar dig."
DELOMR = {"2.1": "Ämnen, blandningar och partikelmodellen", "2.2": "Separations- och analysmetoder"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)

KQ = {
 "Start": [("Vad menas med materia?", "Allt som har massa och tar plats, till exempel fasta föremål, vätskor och gaser som luft."),
           ("Är luft materia? Hur vet du det?", "Ja. Luft har massa och tar plats. Det syns till exempel på att en uppblåst fotboll tar plats och väger mer än en tom."),
           ("Vad säger partikelmodellen om vad allt är uppbyggt av?", "Att allt består av små partiklar som hela tiden rör sig, med tomrum emellan.")],
 "2.1.1": [("Vad är skillnaden mellan ett ämne och ett material?", "Ett ämne är en sorts materia med bestämda egenskaper, t.ex. vatten. Ett material är det något är gjort av och kan vara ett eller flera ämnen, t.ex. trä eller stål."),
           ("Hur räknar du ut densitet, och vilka enheter används?", "Densitet = massa / volym. Enheten är gram per kubikcentimeter (g/cm³), eller g/ml."),
           ("Ett metallstycke väger 54 g och har volymen 20 cm³. Vilken densitet har det, och vilket ämne kan det vara?", "54 g / 20 cm³ = 2,7 g/cm³. Det stämmer med aluminium."),
           ("Varför flyter is på vatten?", "Is har lägre densitet (0,92 g/cm³) än flytande vatten (ca 1,0 g/cm³)."),
           ("Vad är skillnaden mellan smältpunkt och kokpunkt?", "Smältpunkten är temperaturen då ett fast ämne blir flytande. Kokpunkten är temperaturen då en vätska kokar och blir gas."),
           ("Vad betyder att en lösning är mättad?", "Att det inte går att lösa mer av ämnet i lösningsmedlet vid den temperaturen. Överskottet blir kvar som fast ämne.")],
 "2.1.2": [("Beskriv hur partiklarna rör sig och ligger i ett fast ämne, en vätska och en gas.", "Fast: tätt, ordnat, vibrerar på plats. Vätska: nära varandra men oordnat, glider förbi varandra. Gas: långt ifrån varandra, rör sig snabbt åt alla håll."),
           ("Vad kallas det när en vätska blir gas, och vad kallas det när en gas blir vätska?", "Förångning (avdunstning eller kokning) och kondensation."),
           ("Hur ändras temperaturen medan en isbit smälter?", "Den ligger still vid 0 °C så länge det finns både is och vatten."),
           ("Vad är skillnaden mellan avdunstning och kokning?", "Avdunstning sker bara vid vätskans yta och vid alla temperaturer. Kokning sker i hela vätskan vid kokpunkten."),
           ("Förklara med partiklar varför doften sprids i ett rum.", "Doftens partiklar rör sig hela tiden och blandar sig med luftens partiklar. Det kallas diffusion."),
           ("Nämn två saker som partikelmodellen inte visar.", "T.ex. kraften mellan partiklarna, hur partiklarna rör sig, hur partiklarna egentligen ser ut och ämnets färg eller lukt.")],
 "2.1.3": [("Vad är skillnaden mellan ett rent ämne och en blandning?", "Ett rent ämne består av bara en sorts partikel. En blandning innehåller minst två ämnen."),
           ("Vad är skillnaden mellan en homogen och en heterogen blandning?", "I en homogen blandning ser det likadant ut överallt, du ser inte delarna. I en heterogen blandning kan du se eller skilja delarna."),
           ("Ge ett exempel på en lösning och peka ut lösningsmedel och löst ämne.", "Saltvatten: vatten är lösningsmedlet och salt är det lösta ämnet."),
           ("Vad är en legering?", "En blandning av metaller, till exempel mässing av koppar och zink."),
           ("Du löser 5 g salt i 100 g vatten. Hur mycket väger lösningen?", "105 g. Massan bevaras när ämnen blandas, ingenting försvinner.")],
 "2.2.1": [("Vilken egenskap utnyttjar du när du filtrerar en blandning?", "Att vissa ämnen är olösliga och partiklarna för stora för att passera filtret, medan det lösta går igenom."),
           ("Vad kallas det som är kvar i filtret, och vad kallas det som rinner igenom?", "Det som är kvar kallas residuet, det som rinner igenom kallas filtratet."),
           ("Hur får du tillbaka saltet från saltvatten?", "Genom att avdunsta eller koka bort vattnet. Saltet blir kvar."),
           ("Vad är sedimentering?", "Att tyngre partiklar sjunker till botten och kan hällas ifrån (dekanteras).")],
 "2.2.2": [("Vilken skillnad mellan ämnen utnyttjas vid destillation?", "Olika kokpunkter."),
           ("Vilket ämne kokar först när du destillerar en blandning av etanol (78 °C) och vatten (100 °C)?", "Etanol, eftersom den har lägst kokpunkt."),
           ("Vad är kylarens uppgift vid destillation?", "Att kyla ångan så att den kondenserar till vätska som kan samlas upp."),
           ("Varför vandrar olika färger olika långt på filterpapperet vid kromatografi?", "Ämnena löser sig olika bra i lösningsmedlet och fastnar olika mycket på papperet."),
           ("Varför ska pennstrecket sitta ovanför vattenytan i början?", "Annars löser färgen ut i vattnet i stället för att vandra upp i papperet.")],
 "2.2.3": [("Hur kan du identifiera ett okänt fast ämne?", "Mät flera egenskaper, t.ex. densitet, smältpunkt och löslighet, och jämför med en tabell."),
           ("Varför räcker det ofta inte med en enda egenskap för att identifiera ett ämne?", "Flera ämnen kan ha ungefär samma värde på en egenskap. Flera egenskaper tillsammans ger en säkrare slutsats."),
           ("Vad är en fällning?", "Ett fast ämne som bildas när två lösningar blandas och som sjunker eller svävar i vätskan."),
           ("Hur används fällning vid rening av avloppsvatten?", "Man tillsätter ett ämne så att t.ex. fosfat bildar ett fast ämne som sedan kan filtreras bort."),
           ("Nämn en sak som en analys inte kan säga.", "T.ex. hur mycket det finns av ett ämne (om testet bara visar om det finns), eller om provet är representativt för allt.")],
}
def kq(key):
    return kolla(key if key != "Start" else "Start", [q for q, a in KQ[key]])

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad är materia?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p>Allt som har massa och tar plats kallas <strong class='green'>materia</strong>. Stenar, vatten, träd, mjölk och du själv är materia, men också sådant du inte ser: luften är materia eftersom den har massa och tar plats. En uppblåst fotboll väger mer än en tom.</p>"
     "<p>Materia kan finnas i tre vanliga <strong class='green'>tillstånd</strong>: fast, flytande och gas. Vatten kan vara is, flytande vatten eller vattenånga, och det är fortfarande samma ämne. Ändå beter sig de tre tillstånden mycket olika.</p>"
     "<p>För att förklara varför använder kemister en <strong class='green'>modell</strong>, partikelmodellen. Den säger att allt består av mycket små partiklar som hela tiden är i rörelse, med tomrum emellan. Hur partiklarna ligger och rör sig bestämmer om ett ämne är fast, flytande eller gas. I det här kapitlet svarar vi på tre frågor:</p>"
     + bullets(["Hur beskriver man ämnen och material med hjälp av egenskaper som densitet, smältpunkt, kokpunkt och löslighet?", "Hur förklarar partikelmodellen tillstånd, tillståndsförändringar och blandningar?", "Hur kan man skilja ämnen åt och ta reda på vad ett prov innehåller?"]),
   [begrepp([("Materia", "Allt som har massa och tar plats."), ("Tillstånd", "Om ett ämne är fast, flytande eller gas."), ("Partikel", "En mycket liten byggsten som materia är uppbyggd av.")]),
    box("tank", "Tänk efter", "<p>Du har en sluten plastpåse fylld med luft. Vad kan du göra för att visa att luften i påsen har massa och tar plats?</p>")])
 + fig(FIG+"v_oversikt.png", "<b>Bild 2.1</b> Samma ämne i tre tillstånd: is, flytande vatten och vattenånga. Partikelmodellen visar hur partiklarna ligger.", "96%")
 + table(["Delområde", "Du lär dig"],
         [["<b>2.1</b> Ämnen, blandningar och partikelmodellen", "Egenskaper som densitet, smältpunkt och kokpunkt, partikelmodellen och skillnaden mellan rena ämnen och blandningar. Labb: densitet och flyta eller sjunka."],
          ["<b>2.2</b> Separations- och analysmetoder", "Filtrering, avdunstning, destillation, kromatografi och fällning, och hur man identifierar ämnen. Labb: separera sand, salt och vatten."]])
 + kq("Start"))

# ------------------------------------------------------------------ 2.1.1
add("2.1.1", "Ämnen och material", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Ämnen och material",
 "<p>Ett <strong class='green'>ämne</strong> är en sorts materia med bestämda egenskaper, till exempel vatten, järn eller socker. Ett <strong class='green'>material</strong> är det något är gjort av, till exempel trä, glas eller stål. Ett material kan bestå av ett ämne eller av flera ämnen.</p>"
 + "<p>Ämnen känner vi igen på sina <strong class='green'>egenskaper</strong>. Några kan du bedöma med sinnena, som färg, form och hårdhet. Men det är bättre att mäta, för sinnena kan lura oss. Fyra mätbara egenskaper är särskilt viktiga: densitet, smältpunkt, kokpunkt och löslighet. Ett ämne har samma värden oavsett hur stort provet är. En liten och en stor bit aluminium har samma densitet.</p>"
 + "<h3>Densitet</h3>"
 + roww("<p><strong class='green'>Densitet</strong> säger hur mycket massa ett ämne har per volym. Du räknar ut den så här:</p>"
        "<p style='text-align:center'><b>densitet = massa / volym</b></p>"
        "<p>Massan mäter du i gram (g) med en våg. Volymen mäter du i kubikcentimeter (cm³) eller milliliter (ml), där 1 ml är lika med 1 cm³. Har ett metallstycke massan 54 g och volymen 20 cm³ är densiteten 54 / 20 = 2,7 g/cm³. Det stämmer med aluminium.</p>"
        "<p>En fast kropp med oregelbunden form kan du mäta genom <strong class='green'>vattenförskjutning</strong>: lägg den i en mätcylinder med vatten och läs av hur mycket vattennivån stiger. Skillnaden är kroppens volym.</p>",
        [begrepp([("Densitet", "Massa per volym, t.ex. g/cm³."), ("Egenskap", "Något som kännetecknar ett ämne."), ("Vattenförskjutning", "Sätt att mäta volymen hos ett föremål genom att se hur mycket vattnet stiger.")])])
 + fig(FIG+"v_vattenforskj.png", "<b>Bild 2.2</b> Volymen mäts med vattenförskjutning: nivån stiger från 50 ml till 70 ml, så metallstycket har volymen 20 cm³. Värdena är påhittade.", "58%")
 + table(["Ämne", "Densitet (g/cm³)", "Ämne", "Densitet (g/cm³)"],
         [["Luft (normalt tryck)", "0,0013", "Havsvatten (25 °C)", "1,03"], ["Etanol (20 °C)", "0,79", "Aluminium", "2,7"], ["Olivolja", "0,91", "Järn", "7,8"], ["Is", "0,92", "Bly", "11,3"], ["Vatten (4 °C)", "1,00", "Guld", "19,3"]], "tbl num")
 + "<p class='note'>Värdena är avrundade från tabeller och kan skilja något mellan källor. Vattnets densitet är som störst vid 4 °C, ca 1,00 g/cm³, och något lägre (0,998 g/cm³) vid 20 °C.</p>"
 + roww("<h3 style='margin-top:0'>Flyta eller sjunka</h3><p>Du kan använda densitet för att förutsäga om något flyter. Ett föremål flyter i en vätska om dess densitet är <b>lägre</b> än vätskans, och sjunker om den är <b>högre</b>. Is (0,92 g/cm³) flyter på vatten (ca 1,0 g/cm³), och olivolja flyter på vatten. En järnbult (7,8 g/cm³) sjunker. Havsvatten har något högre densitet än sötvatten, så det är lättare att flyta i havet än i en insjö.</p>",
        [fig(FIG+"v_flyta.png", "<b>Bild 2.3</b> Olja flyter på vatten, en isbit flyter och en järnbult sjunker.", "100%")])
 + "<h3>Smältpunkt och kokpunkt</h3>"
 + "<p><strong class='green'>Smältpunkten</strong> är den temperatur då ett fast ämne blir flytande. <strong class='green'>Kokpunkten</strong> är den temperatur då en vätska kokar och blir gas. Rena ämnen har bestämda värden, så de kan användas för att känna igen ämnet. Vatten smälter vid 0 °C och kokar vid 100 °C vid normalt lufttryck. Etanol, som finns i handsprit, smälter vid −114 °C och kokar vid 78 °C. Det betyder att etanol är gas vid temperaturer där vatten fortfarande är vätska.</p>"
 + table(["Ämne", "Smältpunkt (°C)", "Ämne", "Smältpunkt (°C)"],
         [["Is (vatten)", "0", "Aluminium", "658"], ["Paraffin (ljusvax)", "ca 52", "Bordssalt", "802"], ["Tenn", "232", "Guld", "1063"], ["Bly", "327", "Koppar", "1083"], ["Zink", "419", "", ""]], "tbl num")
 + "<h3>Löslighet</h3>"
 + roww("<p><strong class='green'>Löslighet</strong> säger hur mycket av ett ämne som går att lösa i en viss mängd lösningsmedel, till exempel vatten. Salt (natriumklorid) löser sig upp till ungefär 36 g i 100 ml vatten vid 20 °C. Socker löser sig mycket bättre, ungefär 190 g per 100 ml vid 25 °C. Sand är <b>olöslig</b> i vatten: det löser sig inte alls.</p>"
        "<p>När lösningsmedlet inte kan ta emot mer av ämnet är lösningen <strong class='green'>mättad</strong>. Det som tillsätts därefter blir kvar som fast ämne på botten. Fasta ämnen löser sig oftast bättre i varmt vatten än i kallt, medan gaser löser sig sämre.</p>",
        [box("tank", "Tänk efter", "<p>En kub väger 21,6 g och har sidan 2 cm. Räkna ut volymen (sida × sida × sida) och densiteten. Flyter den på vatten?</p>")])
 + kq("2.1.1"))

# ------------------------------------------------------------------ 2.1.2
add("2.1.2", "Partikelmodellen", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Partikelmodellen",
 row("<p>Hur kan man förklara att is är hård, vatten rinner och ånga fyller hela rummet? <strong class='green'>Partikelmodellen</strong> ger ett svar. Den bygger på tre idéer:</p>"
     + bullets(["Allt består av mycket små <strong class='green'>partiklar</strong>.", "Partiklarna är hela tiden i <strong class='green'>rörelse</strong>. Ju högre temperatur, desto snabbare rör de sig.", "Mellan partiklarna finns <strong class='green'>tomrum</strong>, och partiklarna påverkar varandra med krafter."])
     + "<p>Vad en partikel är beror på ämnet. Det kan vara en atom eller en molekyl. Du lär dig mer om atomer i kapitel 3 och om molekyler och joner i kapitel 4. Här ritar vi alla partiklar som runda kulor.</p>",
   [begrepp([("Partikelmodellen", "Modell där allt består av små partiklar som rör sig."), ("Tillstånd", "Fast, flytande eller gas."), ("Diffusion", "Partiklar sprider sig själva ut bland andra partiklar.")])])
 + fig(FIG+"v_partikel.png", "<b>Bild 2.4</b> Partikelmodellen för fast ämne, vätska och gas.", "100%")
 + "<h3>Fast, flytande och gas</h3>"
 + table(["", "Fast ämne", "Vätska", "Gas"],
         [["<b>Avstånd</b>", "Tätt ihop", "Nära varandra", "Långt ifrån varandra"], ["<b>Ordning</b>", "Ordnade i ett mönster", "Oordnade", "Oordnade"],
          ["<b>Rörelse</b>", "Vibrerar på sin plats", "Glider förbi varandra", "Rör sig snabbt åt alla håll"], ["<b>Form och volym</b>", "Bestämd form och volym", "Bestämd volym, formen anpassas efter kärlet", "Fyller hela kärlet"]], "tbl")
 + "<p>Därför går ett fast ämne inte att hälla, medan en vätska rinner. En gas kan tryckas ihop, eftersom det finns mycket tomrum mellan partiklarna. En vätska kan knappt tryckas ihop alls.</p>"
 + "<h3>Tillståndsförändringar</h3>"
 + roww("<p>När ett ämne värms eller kyls kan det byta tillstånd. Ändringarna har egna namn: <b>smältning</b> (fast till vätska), <b>stelning</b> (vätska till fast), <b>förångning</b> (vätska till gas), <b>kondensation</b> (gas till vätska) och <b>sublimering</b> (fast direkt till gas). Förångning kan ske på två sätt: <b>avdunstning</b> sker bara vid vätskans yta, vid alla temperaturer. <b>Kokning</b> sker i hela vätskan vid kokpunkten.</p>"
        "<p>Med partikelmodellen: när du tillför värme rör sig partiklarna snabbare. När de rör sig tillräckligt snabbt klarar krafterna inte längre att hålla dem på plats i mönstret, och ämnet smälter. Vid ännu högre temperatur flyger partiklarna iväg från varandra, och vätskan blir gas. Att kyla gör tvärtom.</p>"
        "<p>Det finns något som överraskar. Under tiden ett ämne smälter eller kokar ligger temperaturen <b>still</b>, trots att du fortsätter värma. Värmen går åt till att bryta loss partiklarna från varandra och ökar inte rörelsen.</p>",
        [fig(FIG+"v_tillstand.png", "<b>Bild 2.5</b> Tillståndsförändringarna mellan fast, flytande och gas.", "100%")])
 + "<h3>Diffusion och tryck</h3>"
 + roww("<p>Du kan känna doften av mat från ett annat rum. Doftämnets partiklar rör sig hela tiden, krockar med luftens partiklar och sprids ut. När partiklar sprids själva bland andra partiklar kallas det <strong class='green'>diffusion</strong>. Det händer även utan att något rörs om: en droppe färg i stilla vatten färgar efter en stund hela vattnet. Diffusion är snabb i gaser och långsam i vätskor.</p>"
        "<p>Gaspartiklar rör sig snabbt och slår mot kärlets väggar. Alla slag tillsammans ger ett <strong class='green'>tryck</strong>. Om du värmer gasen i en sluten behållare rör sig partiklarna snabbare, slagen blir hårdare och oftare, och trycket ökar. Därför kan en sluten burk spricka om den hettas upp.</p>",
        [fig(FIG+"v_diffusion.png", "<b>Bild 2.6</b> Diffusion: en färgdroppe sprids i vatten, efter hand blir färgen jämn. Partiklarna syns bara i modellen.", "100%")])
 + "<h3>Vad modellen inte visar</h3>"
 + "<p>Partikelmodellen är en förenkling. Bilderna är tvådimensionella, men verkligheten är tredimensionell. Bilderna visar inte rörelsen, krafterna mellan partiklarna eller deras energi. Partiklar är inte färgade kulor: färg, lukt och smak hos ämnet förklaras inte av modellen så här enkelt. Och det är inte hela sanningen att partiklarna är runda bollar. När du behöver förklara mer får du använda en bättre modell, till exempel atommodellen i kapitel 3.</p>"
 + box("tank", "Tänk efter", "<p>Varför är det svårt att rita en bra bild av partiklarnas rörelse på papper? Vilka nya bilder eller hjälpmedel kunde visa det bättre?</p>")
 + kq("2.1.2"))

# ------------------------------------------------------------------ 2.1.3
add("2.1.3", "Rena ämnen och blandningar", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Rena ämnen och blandningar",
 row("<p>Ett <strong class='green'>rent ämne</strong> består av bara en sorts partiklar. Destillerat vatten och bordssalt är nästan rena ämnen. En <strong class='green'>blandning</strong> innehåller minst två ämnen. De flesta saker du möter är blandningar: luft, mjölk, saltvatten, jord, choklad.</p>"
     "<p>Ett rent ämne har en bestämd smältpunkt och kokpunkt. För en blandning varierar de med hur mycket av varje ämne som ingår. Därför kan man använda dem för att se om ett prov är rent.</p>",
   [begrepp([("Rent ämne", "Består av bara en sorts partikel."), ("Blandning", "Innehåller minst två ämnen."), ("Lösning", "Homogen blandning av ett löst ämne i ett lösningsmedel.")])])
 + fig(FIG+"v_blandning.png", "<b>Bild 2.7</b> Partikelbilder: ett rent ämne, en homogen blandning (lösning) och en heterogen blandning.", "64%")
 + "<h3>Homogena och heterogena blandningar</h3>"
 + roww("<p>I en <strong class='green'>homogen blandning</strong> är allt blandat så jämnt att det ser likadant ut överallt. Du kan inte se de olika delarna. Saltvatten är ett exempel. I en <strong class='green'>heterogen blandning</strong> kan du se eller skilja delarna: sand i vatten, sallad, granit.</p>"
        "<p>En homogen blandning av ett ämne som löst sig i ett annat kallas <strong class='green'>lösning</strong>. Det ämne som löses kallas <b>löst ämne</b> och det som löser kallas <b>lösningsmedel</b>. I saltvatten är salt det lösta ämnet och vatten lösningsmedlet. Vatten är det vanligaste lösningsmedlet, men det finns fler.</p>"
        "<p>Luft är en homogen blandning av flera gaser. En blandning av metaller kallas <strong class='green'>legering</strong>. Mässing är en legering av koppar och zink, brons av koppar och tenn. Legeringen kan ha helt andra egenskaper än metallerna var för sig, till exempel vara hårdare.</p>",
        [box("tank", "Tänk efter", "<p>Är en kopp te med socker i homogen eller heterogen? Och en kopp te med tebitar i? Förklara med partikelmodellen.</p>")])
 + "<h3>Vad händer när ämnen blandas?</h3>"
 + "<p>När du blandar ämnen försvinner ingenting. Ämnena finns kvar som de var och går i princip att få tillbaka, så vi kan skilja dem åt (delområde 2.2). Att blanda är inte en kemisk reaktion (se kapitel 4). Därför är <b>massan</b> lika stor före och efter: löser du 5 g salt i 100 g vatten får du 105 g saltvatten.</p>"
 + kq("2.1.3"))

# ------------------------------------------------------------------ Labb 2.1
add("Labb", "2.1 Densitet och flyta eller sjunka", f"Kapitel {NR} · Delområde 2.1 {DELOMR['2.1']} · Labb 2.1 Densitet och flyta eller sjunka",
 "<p>Du ska mäta massa och volym för olika föremål, räkna ut deras densitet och förutsäga om de flyter eller sjunker. Sedan prövar du din förutsägelse.</p>"
 + fig(FIG+"v_labb1.png", "<b>Bild 2.8</b> Först massan på vågen, sedan volymen med vattenförskjutning, därefter räknar du ut densiteten.", "46%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Kan man förutsäga om ett föremål flyter eller sjunker genom att räkna ut dess densitet?</p><p><strong class='green'>Hypotes:</strong> Skriv vilka föremål du tror flyter, och varför.</p>"
        "<p><strong class='green'>Material:</strong> våg, mätcylinder, vatten, saltlösning (20 g salt löst i 100 ml vatten), tre till fem små fasta föremål av olika material som inte löser sig i vatten (till exempel en metallbit, en träbit, en sten, ett stycke plast), skyddsglasögon, trasa.</p><h3>Gör så här</h3>"
        + steps(["Väg varje föremål och skriv massan i tabellen.",
                 "Fyll mätcylindern till ungefär hälften med vatten och läs av volymen. Lägg försiktigt ner föremålet så att det blir helt täckt och läs av igen. Skillnaden är föremålets volym.",
                 "Räkna ut densiteten: massa delat med volym. Jämför med vattnets densitet, 1,0 g/cm³, och skriv din förutsägelse: flyter eller sjunker.",
                 "Prova i en bägare med vatten. Stämde din förutsägelse?",
                 "Prova även ett av föremålen i saltlösningen. Sker det något annorlunda? Förklara med densitet."]),
        [box("begrepp", "Begrepp", "<b class='t'>Densitet</b><p>Massa per volym.</p><b class='t'>Förutsägelse</b><p>En bedömning du gör innan du provar, byggd på din kunskap.</p>"),
         box("tank", "Bra att veta", "<p>Föremål som flyter kan du trycka ner under ytan med en tunn pinne för att mäta volymen. Pinnen ska bara vara med i vattnet en liten bit.</p>")])
 + table(["Föremål", "Massa (g)", "Volym (cm³)", "Densitet (g/cm³)", "Förutsägelse", "Resultat"], [["1", "", "", "", "", ""], ["2", "", "", "", "", ""], ["3", "", "", "", "", ""]], "tbl num")
 + '<p class="note">Säkerhet: Använd skyddsglasögon. Torka upp spill på golvet direkt så att ingen halkar. Använd bara vatten och saltlösning. Smaka inte på lösningen.</p>'
 + "<h3>Frågor</h3>"
 + steps(["Vilka föremål hade högre densitet än vatten? Sjönk de alla?", "Hur kan ett fartyg av stål flyta fast stål har högre densitet än vatten?", "Varför är det lättare att flyta i saltvatten än i vanligt vatten? Förklara med densitet."], True))

# ------------------------------------------------------------------ 2.2.1
add("2.2.1", "Filtrering, avdunstning och sedimentering", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Filtrering, avdunstning och sedimentering",
 row("<p>Eftersom ämnena i en blandning behåller sina egenskaper kan vi <strong class='green'>separera</strong> dem. Hur vi gör beror på vilken egenskap som skiljer dem. Det kan vara att det ena är olösligt, att det ena sjunker, eller att de har olika kokpunkter. I det här momentet möter du tre enkla metoder.</p>",
   [begrepp([("Separera", "Skilja ämnen i en blandning från varandra."), ("Filtrat", "Vätskan som rinner igenom filtret."), ("Residu", "Det fasta som blir kvar i filtret.")])])
 + "<h3>Sedimentering och dekantering</h3>"
 + "<p>Om en fast substans är tyngre än vätskan och inte löser sig sjunker den med tiden till botten. Det kallas <strong class='green'>sedimentering</strong> och det som sjunkit kallas sediment. Sedan kan du försiktigt hälla av vätskan. Det kallas <strong class='green'>dekantering</strong>. Metoden är enkel men inte särskilt noggrann, för små partiklar kan hänga kvar i vätskan länge.</p>"
 + "<h3>Filtrering</h3>"
 + roww("<p>Med <strong class='green'>filtrering</strong> separerar du olösliga fasta ämnen från en vätska. Filterpapper har små hål, <b>porer</b>. Vätskan och det som är löst går igenom, men fasta partiklar som är större än porerna fastnar. Det som blir kvar i filtret är <b>residuet</b>, och vätskan som kommer igenom är <b>filtratet</b>.</p>"
        "<p>Sand i vatten går bra att filtrera. Saltvatten går inte att separera med filtrering: saltet är löst, det vill säga uppdelat i partiklar som är mycket mindre än porerna, så det följer med vattnet genom filtret.</p>",
        [fig(FIG+"v_filtrering.png", "<b>Bild 2.9</b> Filtrering. Sanden fastnar i filtret, saltvattnet rinner igenom.", "100%")])
 + "<h3>Avdunstning och indunstning</h3>"
 + "<p>Vill du få tillbaka ett löst ämne kan du få bort lösningsmedlet. Om du låter vattnet <strong class='green'>avdunsta</strong> blir det lösta ämnet kvar som fast ämne. Det går snabbare om du värmer, så att vätskan kokar. Då kallas det <strong class='green'>indunstning</strong>. Metoden fungerar bra för salt i vatten, eftersom saltet inte följer med ångan. Den fungerar inte om det lösta ämnet själv är lättflyktigt eller bryts ned av värmen.</p>"
 + fig(FIG+"v_flode.png", "<b>Bild 2.10</b> Så separerar du sand, salt och vatten: först filtrering, sedan indunstning.", "56%")
 + kq("2.2.1"))

# ------------------------------------------------------------------ 2.2.2
add("2.2.2", "Destillation och kromatografi", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Destillation och kromatografi",
 row("<p>Ibland räcker det inte med filtrering och indunstning. Om du vill ha tillbaka vattnet från saltvatten, eller skilja två vätskor åt, behöver du andra metoder. Destillation utnyttjar att ämnen har <b>olika kokpunkter</b>. Kromatografi utnyttjar att ämnen <b>löser sig olika bra</b> och fastnar olika mycket.</p>",
   [begrepp([("Destillation", "Separation som utnyttjar olika kokpunkter."), ("Kromatografi", "Separation som utnyttjar att ämnen vandrar olika långt."), ("Kondensera", "Gå från gas till vätska.")])])
 + "<h3>Destillation</h3>"
 + roww("<p>Vid <strong class='green'>destillation</strong> värms blandningen. Det ämne som har lägst kokpunkt blir gas först. Gasen leds in i en <b>kylare</b>, där den kyls och kondenserar till vätska, som samlas upp i ett annat kärl. På så sätt får du det ämnet separat.</p>"
        "<p>Med saltvatten blir det bara vattnet som blir gas. Saltet har en mycket högre kokpunkt och blir kvar i kolven. Det som samlas upp är därför rent vatten, så metoden går att använda för att göra dricksvatten av havsvatten. Blandar du etanol (kokpunkt 78 °C) och vatten (100 °C) får du mest etanol först. Det är inte en helt skarp separation, för även vatten förångas lite grann, så man kan upprepa processen.</p>",
        [fig(FIG+"v_destillation.png", "<b>Bild 2.11</b> Destillation: ångan kyls i kylaren och droppar ner i uppsamlingskärlet.", "100%")])
 + "<h3>Kromatografi</h3>"
 + roww("<p>Många färger är blandningar av flera färgämnen. Med <strong class='green'>papperskromatografi</strong> kan du se dem. Du gör en prick eller ett streck med färgen en bit upp på ett filterpapper och ställer papperets nederkant i lite lösningsmedel, till exempel vatten. Vattnet sugs upp i papperet och tar med sig färgämnena. De som löser sig bra i vatten och fastnar lite på papperet vandrar långt. De som fastnar mer vandrar kortare. Färgerna delar sig i band.</p>"
        "<p>Pennstrecket måste sitta ovanför vattenytan i början. Annars löser färgen ut i vattnet i stället för att vandra upp i papperet. Metoden används av analytiska kemister för att se vilka ämnen ett prov innehåller, till exempel färgämnen i mat eller bläck.</p>",
        [fig(FIG+"v_kromatografi.png", "<b>Bild 2.12</b> Kromatografi: tre färgämnen vandrar olika långt på papperet.", "100%")])
 + box("tank", "Tänk efter", "<p>Vilken metod skulle du välja för att (a) få ut socker ur sockervatten, (b) få rent vatten ur sockervatten, (c) se vilka färger som ingår i grön tuschpenna? Motivera.</p>")
 + kq("2.2.2"))

# ------------------------------------------------------------------ 2.2.3
add("2.2.3", "Identifiera ämnen och fällning", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Identifiera ämnen och fällning",
 row("<p>Hur tar man reda på vad ett okänt ämne är? Kemister <strong class='green'>identifierar</strong> ämnen genom att mäta egenskaper och jämföra med kända värden i tabeller. Ett fast ämne som är vitt, löser sig i vatten och smälter vid 802 °C är sannolikt bordssalt. Ett metallstycke med densiteten 2,7 g/cm³ är sannolikt aluminium.</p>"
     "<p>En enda egenskap räcker sällan. Flera ämnen kan ha nästan samma värde på en egenskap, så man mäter flera och ser om alla stämmer. Ju fler som stämmer, desto säkrare är slutsatsen.</p>",
   [begrepp([("Identifiera", "Ta reda på vad ett ämne är."), ("Fällning", "Fast ämne som bildas när två lösningar blandas."), ("Indikator", "Ämne som byter färg vid ändrade förhållanden.")])])
 + "<h3>Kemiska tester och indikatorer</h3>"
 + "<p>Ibland används kemiska tester. En <strong class='green'>indikator</strong> är ett ämne som byter färg beroende på om en lösning är sur eller basisk. Det används för att pröva lösningar. Hur syror, baser och pH fungerar får du lära dig i kapitel 5. Här räcker det att veta att färgen på en indikator kan bli en ledtråd.</p>"
 + "<h3>Fällning</h3>"
 + roww("<p>Ibland blir en klar lösning grumlig när du blandar den med en annan klar lösning. Då har ett nytt, olösligt ämne bildats. Det fasta ämnet kallas en <strong class='green'>fällning</strong> och sjunker oftast med tiden. Fällning är en kemisk reaktion, och den kan användas för att visa att ett visst löst ämne finns i provet.</p>"
        "<p>Fällning används också för att rena vatten. I ett reningsverk kan man tillsätta ett ämne som får lösta ämnen, till exempel fosfat, att bilda ett fast ämne. Det kan sedan filtreras eller sedimenteras bort. Fosfat vill man få bort från avloppsvatten eftersom för mycket fosfat i sjöar och hav ger algblomning. Vid avhärdning av hårt vatten kan man tillsätta kalk och soda, så att kalcium och magnesium fälls ut som fasta ämnen.</p>",
        [fig(FIG+"v_felling.png", "<b>Bild 2.13</b> Fällning: två klara lösningar blandas och ett fast ämne bildas.", "100%")])
 + "<h3>Vad kan en analys säga?</h3>"
 + "<p>En analys kan svara på vilka ämnen som finns i ett prov, men det är inte alltid den svarar på <i>hur mycket</i>. Ett test kan också ge fel svar om provet är förorenat, om metoden inte är känslig nog, eller om flera ämnen ger samma reaktion. Dessutom säger ett prov bara något om just det provet. Ett vattenprov från en plats behöver inte stämma för hela sjön. Därför gör man upprepade prov och olika metoder, och redovisar hur säker slutsatsen är.</p>"
 + box("tank", "Tänk efter", "<p>Du får ett vitt pulver och ska ta reda på om det är socker eller salt. Vilka egenskaper kan du mäta eller testa utan att smaka på det? Vad behöver du för att kunna jämföra?</p>")
 + kq("2.2.3"))

# ------------------------------------------------------------------ Labb 2.2
add("Labb", "2.2 Separera sand, salt och vatten", f"Kapitel {NR} · Delområde 2.2 {DELOMR['2.2']} · Labb 2.2 Separera sand, salt och vatten",
 "<p>Du får en blandning av sand, salt och vatten. Din uppgift är att planera hur du separerar dem och sedan ta reda på hur mycket du fick tillbaka. Därefter prövar du kromatografi på färgade pennor.</p>"
 + fig(FIG+"v_labb2.png", "<b>Bild 2.14</b> Filtrera blandningen, och indunsta filtratet i en skål. Kromatografin görs separat med filterpapper.", "40%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Hur kan man separera sand, salt och vatten ur en blandning, och hur mycket får man tillbaka?</p><p><strong class='green'>Hypotes:</strong> Hur tror du att du får tillbaka allt? Vilken ordning ska metoderna komma i?</p>"
        "<p><strong class='green'>Material:</strong> blandning av 10 g sand och 5 g salt i 100 ml vatten, våg, tratt, filterpapper, bägare, porslinsskål eller metallskål, värmeplatta, tång eller grytlappar, glasstav och 2–3 olika vattenlösliga färgpennor till kromatografin, lite vatten, skyddsglasögon.</p><h3>Gör så här</h3>"
        + steps(["Väg ett tomt filterpapper och vik det i tratten över en ren bägare.",
                 "Häll blandningen långsamt genom filtret. Skölj ur bägaren med lite vatten.",
                 "Låt sanden torka, väg den och dra av filterpapperets massa.",
                 "Väg den tomma skålen. Indunsta filtratet i skålen på värmeplattan. Stäng av värmen när lite vätska återstår så att saltet inte spritter.",
                 "Låt skålen svalna. Väg den och räkna ut saltets massa.",
                 "Kromatografi: rita ett streck med en penna en bit upp på ett filterpapper, ställ nederkanten i lite vatten (strecket ovanför ytan) och jämför banden när vattnet nått nästan till toppen."]),
        [box("begrepp", "Begrepp", "<b class='t'>Filtrat</b><p>Vätskan som kommer genom filtret.</p><b class='t'>Residu</b><p>Det som blir kvar i filtret.</p><b class='t'>Utbyte</b><p>Hur mycket du fick tillbaka jämfört med hur mycket du hade.</p>"),
         box("tank", "Bra att veta", "<p>Smaka aldrig på något i labbet, inte heller på saltet. Skålen blir mycket varm, så använd tång.</p>")])
 + table(["Ämne", "Massa före (g)", "Massa efter (g)", "Skillnad (g)"], [["Sand", "", "", ""], ["Salt", "", "", ""]], "tbl num")
 + '<p class="note">Säkerhet: Använd skyddsglasögon. Skålen och värmeplattan blir mycket varma: använd tång och rör inte. Smaka inget. Håll håret samlat. Torka upp spill.</p>'
 + "<h3>Frågor</h3>"
 + steps(["Varför fungerade filtreringen på sanden men inte på saltet?", "Hur mycket av sanden och saltet fick du tillbaka? Vilka felkällor kan förklara skillnaden?", "Vilka band fick du i kromatografin? Vad säger det om pennornas färger?"], True))

SAMMAN = ["<strong>Materia</strong> är allt som har massa och tar plats. Materia finns som fast, flytande eller gas (tillstånd).",
          "Ett <strong>ämne</strong> känns igen på sina egenskaper: <strong>densitet</strong>, <strong>smältpunkt</strong>, <strong>kokpunkt</strong> och <strong>löslighet</strong>.",
          "<strong>Densitet</strong> = massa / volym. Ett föremål flyter i en vätska om dess densitet är lägre än vätskans.",
          "<strong>Partikelmodellen</strong>: allt består av partiklar som rör sig, med tomrum emellan. I fasta ämnen ligger de tätt och ordnat, i vätskor nära men oordnat, i gaser långt isär.",
          "Tillståndsförändringar är <strong>smältning, stelning, förångning, kondensation</strong> och <strong>sublimering</strong>. Temperaturen ligger still medan ett ämne smälter eller kokar.",
          "<strong>Diffusion</strong> är att partiklar sprider sig bland varandra. Gaser får <strong>tryck</strong> av att partiklarna slår mot väggarna.",
          "Modellen visar inte krafter, rörelse eller att partiklar är något annat än bollar. Den är en förenkling.",
          "Ett <strong>rent ämne</strong> har en sorts partiklar. En <strong>blandning</strong> har minst två. Blandningar är <strong>homogena</strong> eller <strong>heterogena</strong>. En <strong>lösning</strong> har ett löst ämne i ett lösningsmedel. En <strong>legering</strong> är en blandning av metaller.",
          "Vid blandning bevaras massan. Ämnena finns kvar och kan separeras.",
          "<strong>Filtrering</strong> skiljer fast från vätska, <strong>indunstning</strong> får tillbaka löst ämne, <strong>destillation</strong> utnyttjar olika kokpunkter och <strong>kromatografi</strong> skiljer ämnen som vandrar olika långt.",
          "Ämnen <strong>identifieras</strong> genom att mäta flera egenskaper. En <strong>fällning</strong> är ett fast ämne som bildas när lösningar blandas. En analys har gränser."]

BEGR = [("Avdunstning", "Förångning som sker vid vätskans yta."), ("Blandning", "Innehåller minst två ämnen."), ("Densitet", "Massa per volym."), ("Destillation", "Separation som utnyttjar olika kokpunkter."),
        ("Diffusion", "Partiklar som sprider sig bland andra partiklar."), ("Fällning", "Fast ämne som bildas när lösningar blandas."), ("Filtrering", "Separation av olösligt fast ämne och vätska."),
        ("Gas", "Tillstånd där partiklarna är långt ifrån varandra."), ("Heterogen blandning", "Blandning där delarna syns eller kan skiljas åt."), ("Homogen blandning", "Blandning som ser likadan ut överallt."),
        ("Kokpunkt", "Temperaturen då en vätska kokar."), ("Kondensation", "Gas blir vätska."), ("Kromatografi", "Separation av ämnen som vandrar olika långt."), ("Legering", "Blandning av metaller."),
        ("Löslighet", "Hur mycket som går att lösa i ett lösningsmedel."), ("Lösning", "Homogen blandning av löst ämne och lösningsmedel."), ("Materia", "Allt som har massa och tar plats."),
        ("Mättad lösning", "Lösning som inte kan lösa mer."), ("Partikelmodellen", "Modell där allt består av små partiklar i rörelse."), ("Rent ämne", "Består av en sorts partikel."),
        ("Smältpunkt", "Temperaturen då ett fast ämne smälter."), ("Sublimering", "Fast ämne blir gas direkt."), ("Tillstånd", "Fast, flytande eller gas."), ("Tryck", "Gaspartiklarnas slag mot väggarna."),
        ("Vattenförskjutning", "Metod att mäta volym.")]

TEST = [
 ("A", "Ett föremål har massan 40 g och volymen 5 cm³. Vilken densitet har det?", ["A 0,125 g/cm³", "B 8 g/cm³", "C 35 g/cm³", "D 200 g/cm³"], 1, 0),
 ("A", "Vilket påstående om partiklarna i en gas stämmer?", ["A De ligger tätt i ett mönster.", "B De glider förbi varandra men ligger nära varandra.", "C De är långt ifrån varandra och rör sig snabbt åt alla håll.", "D De står stilla."], 2, 0),
 ("A", "Vilken metod använder du för att separera sand från vatten?", ["A Destillation", "B Filtrering", "C Kromatografi", "D Fällning"], 1, 0),
 ("A", "Vad är en legering?", ["A En lösning av salt i vatten.", "B En blandning av metaller.", "C Ett rent ämne.", "D En gas."], 1, 0),
 ("B", "Förklara varför is flyter på vatten. Använd begreppet densitet.", None, 1, 3),
 ("B", "Förklara vad som menas med en mättad lösning.", None, 1, 3),
 ("C", "TABELL", None, 2, 5),
 ("C", "Förklara med partikelmodellen vad som händer med partiklarna när vatten kokar, och varför temperaturen ligger still under tiden.", None, 2, 5),
 ("D", "Du har en blandning av fint grus, bordssalt och vatten. Beskriv i vilken ordning och med vilka metoder du kan få tillbaka (1) gruset, (2) saltet och (3) rent vatten. Förklara varför varje metod fungerar.", None, 3, 6),
 ("D", "Förklara varför en gas kan tryckas ihop men en vätska knappt kan det. Använd partikelmodellen. Förklara också en begränsning hos modellen, det vill säga något den inte visar.", None, 3, 6),
 ("E", "Du ska ta reda på om ett okänt vitt, fast ämne är salt, socker eller något annat. Planera en undersökning. Beskriv vilka egenskaper du mäter eller testar, vad du jämför med och hur du drar en slutsats. Förklara varför du behöver mer än en egenskap.", None, 3, 7),
 ("E", "Förklara hur man kan avgöra om ett prov är ett rent ämne eller en blandning med hjälp av smältpunkt eller kokpunkt. Diskutera också vad en sådan mätning kan och inte kan säga, och varför flera mätningar behövs.", None, 3, 7),
]
TEST_TABELL = (["Föremål", "Massa (g)", "Volym (cm³)"], [["A", "27", "10"], ["B", "78", "10"], ["C", "9,2", "10"]])
TEST_D_TEXT = "Elin mätte massan och volymen hos tre små föremål av olika material. Mätvärdena är påhittade. Vattnets densitet är 1,0 g/cm³."
TEST_D_SUB = ["a) Räkna ut densiteten för varje föremål.", "b) Vilka föremål flyter på vatten och vilka sjunker? Förklara.", "c) Vilket av föremålen kan vara järn (7,8 g/cm³) och vilket kan vara aluminium (2,7 g/cm³)?"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Tolka resultat och förklara", "D": "Resonera och ta ställning", "E": "Planera och resonera"}
FACIT = [
 "B", "C", "B", "B",
 "Is har lägre densitet (ca 0,92 g/cm³) än flytande vatten (ca 1,0 g/cm³). Ett föremål med lägre densitet än vätskan flyter. Isen tar mer plats än samma massa vatten.",
 "En lösning som inte kan lösa mer av ämnet vid den temperaturen. Det som tillsätts efter det blir kvar som fast ämne på botten.",
 "a) A: 27/10 = 2,7 g/cm³. B: 78/10 = 7,8 g/cm³. C: 9,2/10 = 0,92 g/cm³. b) C flyter (lägre densitet än 1,0), A och B sjunker (högre densitet). c) A kan vara aluminium (2,7), B kan vara järn (7,8).",
 "Partiklarna får värme och rör sig så snabbt att de lämnar vätskan och blir gas, överallt i vätskan. Under kokningen går värmen åt att bryta loss partiklarna från varandra, inte till att öka rörelsen, så temperaturen ligger still vid kokpunkten.",
 "(1) Filtrera: gruset fastnar i filtret (residu) och saltvattnet rinner igenom (filtrat), så gruset är fast och olösligt. (2) Indunsta filtratet: vattnet förångas och saltet blir kvar, eftersom salt har mycket högre kokpunkt. (3) Vill du också ha rent vatten destillerar du filtratet: vattnet kokar först, kyls och kondenserar i kylaren och samlas upp, medan saltet blir kvar i kolven. Destillation ger alltså både vatten och salt, medan indunstning ger saltet men låter vattnet försvinna ut i luften.",
 "I en gas är det stort tomrum mellan partiklarna, så de kan komma närmare varandra när man trycker. I en vätska ligger partiklarna redan nära varandra och det finns nästan inget tomrum. Begränsning: modellen är en 2D-bild som visar partiklar som kulor och inte rörelsen, krafterna eller energin.",
 "Öppet svar. Ett välutvecklat svar: mät densitet (massa/volym), smältpunkt, löslighet i vatten och ev. kokpunkt eller test med indikator, och jämför med tabellvärden (salt: smälter vid 802 °C, löser sig ca 36 g/100 ml; socker: löser sig mycket bättre). Smaka inte. Ett värde räcker inte eftersom flera ämnen kan ha liknande värde på en egenskap. Slutsatsen blir säkrare ju fler egenskaper som stämmer. Diskutera felkällor, att provet kan vara förorenat och att man bör upprepa.",
 "Öppet svar. Ett rent ämne har en bestämd smältpunkt och kokpunkt, och temperaturen ligger still under smältningen. En blandning smälter eller kokar över ett temperaturområde och har ett annat värde än de rena ämnena. Mätningen kan visa att provet inte är rent men inte vilka ämnen det innehåller eller hur mycket. Flera mätningar behövs för att utesluta mätfel och bekräfta mönstret.",
]
LGR = ("Området täcker det centrala innehållet i årskurs 7–9 om materiens uppbyggnad med partikelmodeller, ämnens egenskaper och blandningar samt separations- och analysmetoder. "
       "Delområde 2.1 behandlar ämnen och material, partikelmodellen med tillståndsförändringar, diffusion och tryck och dess begränsningar samt rena ämnen och blandningar. Delområde 2.2 behandlar filtrering, avdunstning, sedimentering, destillation, kromatografi, identifiering av ämnen och fällning samt vad en analys kan och inte kan säga. "
       "Labbarna tränar att mäta och räkna ut densitet, förutsäga och pröva, och att planera och genomföra en separation. Uppgifterna följer betygskriteriernas progression från att beskriva till att förklara och resonera, och är inspirerade av frisläppta nationella prov i kemi. "
       "Anslutning till andra ämnen: densitet och tillstånd behandlas också i fysik, och blandningar och rening återkommer i biologi (vatten) och teknik. I kemi ligger fokus på partiklar och ämnens egenskaper.")
FAKTA = ("Kontrollerat mot öppna källor (2026-10-18): densitetsvärden för vatten (1,00 g/cm³ vid 4 °C, 0,998 vid 20 °C), is (0,92), aluminium, järn, bly, guld, luft, etanol (0,789), olivolja och havsvatten; smältpunkter för is, paraffin, tenn, bly, zink, aluminium, bordssalt, koppar och guld; etanolens kokpunkt (78,4 °C) och smältpunkt (−114 °C); löslighet för salt (ca 36 g/100 ml vid 20 °C) och socker (ca 190 g/100 ml vid 25 °C), att mättade lösningar och att fasta ämnens löslighet i regel ökar med temperaturen; partikelmodellens beskrivning av fast, vätska och gas; tillståndsförändringarnas namn och att temperaturen ligger still under förändringen; att avdunstning sker vid ytan men kokning i hela vätskan; att partiklar rör sig hela tiden och att diffusion i vätskor är långsam; att is flyter därför att vatten har störst densitet vid 4 °C och isens kristallstruktur tar mer plats; hur filtrering, indunstning, destillation och kromatografi fungerar; fällning i vattenrening (fosfat, kalcium, magnesium). "
         "Ej källkontrollerat: att mässing är koppar och zink och brons koppar och tenn (allmän kunskap), att tryck uppstår av att partiklar slår mot väggar (allmän fysik), att gaser löser sig sämre i varmare vatten och förklaringar med partikelmodellen om värme och temperaturen som ligger still, sambandet mellan indikatorer och syra/bas (kapitel 5), att algblomning orsakas av fosfat (allmänt), att ett fartyg flyter p.g.a. sin form. Alla exempelmätvärden är påhittade. "
         "Källor: Skolverket, Lgr22 kursplan i kemi. · HyperPhysics, EngineeringToolbox, Alloprof, Creative Chemistry, RSC Education, LibreTexts. · Illustrationer: egenritade för detta kapitel.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven förstår att materia är allt som har massa och tar plats och att partikelmodellen används för att förklara tillstånd. Låt eleverna skriva sin förklaring till hur sockret hamnar i hela koppen (Fundera) och spara den. Vanligt fel: att luft inte är materia. Väg en tom och en uppblåst fotboll (eller basketboll) på en våg.</p>
<p><b>Ämnen och material.</b> C-mål: beskriva ämnen med egenskaper, räkna ut densitet och använda den för att förutsäga flyta/sjunka. Vanligt fel: att tunga saker alltid sjunker (densitet är massa per volym) och att en stor bit har högre densitet än en liten av samma ämne. Gör gärna en snabb demo med en isbit i vatten och i etanol (lärardemo, brandfara): isen sjunker i etanol eftersom etanol har lägre densitet (0,79).</p>
<p><b>Partikelmodellen.</b> C-mål: förklara fast, vätska, gas och tillståndsförändringar med modellen och nämna vad den inte visar. Vanliga fel: att partiklarna blir större vid uppvärmning, att det finns luft mellan partiklarna, att partiklarna själva smälter, och att temperaturen stiger under smältning. Diffusion kan demonstreras med en färgdroppe i stilla vatten (kallt och varmt) eller med doft. Att diffusion är snabbare i varmt vatten är rimligt med modellen men är inte belagt i vår källa; låt eleverna testa.</p>
<p><b>Rena ämnen och blandningar.</b> C-mål: skilja rent ämne från blandning och homogen från heterogen blandning. Vanliga fel: att ”rent” betyder ”utan skadliga ämnen” och att luft är ett ämne. Gör korten: ge eleverna 10 vardagsprodukter att sortera.</p>
<p><b>Labb 2.1 Densitet och flyta eller sjunka.</b> Material: våg, mätcylinder, vatten, saltlösning (20 g salt i 100 ml vatten), små föremål. Förväntat: metall sjunker, trä och vissa plaster flyter, men resultaten beror på föremålen. Vanliga fel: luftbubblor på föremålet ger för stor volym, vattnet stänker, föremål som flyter hålls inte under ytan. Ett ägg flyter i tillräckligt salt vatten men sjunker i vanligt, och passar som extra demonstration.</p>
<p><b>Filtrering, avdunstning och sedimentering.</b> C-mål: välja metod efter egenskap och förklara varför filtrering inte fungerar på löst salt. Vanligt fel: att saltet kan filtreras bort. Visa gärna ett filter med porer under förstoring om det finns tillgång.</p>
<p><b>Destillation och kromatografi.</b> C-mål: beskriva hur destillation och kromatografi fungerar och välja rätt metod. Destillation görs helst som lärardemo. Kromatografi går bra som elevförsök med filterpapper och vattenlösliga tuschpennor. Vanliga fel: att pennstrecket hamnar under vattenytan, och att alla pennor innehåller flera färger. Prova pennorna i förväg.</p>
<p><b>Identifiera ämnen och fällning.</b> C-mål: använda flera egenskaper för att dra en slutsats och beskriva vad en fällning är och var den används. Vanligt fel: att man kan identifiera ett ämne från en enda egenskap. Kemiska tester med indikatorer kopplas till kapitel 5.</p>
<p><b>Labb 2.2 Separera sand, salt och vatten.</b> Material: blandning av 10 g sand och 5 g salt i 100 ml vatten (lärarförberedd), filtrering och indunstning. Förväntat: ca 9–10 g sand och 4–5 g salt, men sanden blir lätt fuktig och saltet kan spritta eller sitta kvar på bägaren. Säkerhet: skyddsglasögon, tång, ej smaka. Kromatografin är ett tillägg.</p>
"""
LAB_HTML = ""

BONUS = dict(
 titel="Densitetstorn: lager av vätskor",
 ingress="Eleverna bygger ett litet torn av vätskor i ett glas. Vätskorna lägger sig i lager efter densitet. Ett enkelt sätt att koppla ihop densitet och partikelmodell.",
 syfte="Eleverna förstår att vätskor med olika densitet lägger sig i lager och använder tabellvärden för att förutsäga ordningen. Labben tränar att göra en förutsägelse och pröva den.",
 tid="Grupper om två till tre.",
 material=["Ett högt genomskinligt glas eller en mätcylinder", "Matolja", "Vatten med några droppar matfärg", "Saltlösning (salt löst i vatten) med en annan matfärg", "Sked och bägare", "Skyddsglasögon", "Anteckningsblad"],
 genomf=["Låt eleverna förutsäga i vilken ordning matolja, vatten och saltlösning lägger sig. Ge dem densitetsvärden: olivolja ca 0,91 g/cm³, vatten ca 1,0 g/cm³, havsvatten ca 1,03 g/cm³.", "Häll saltlösningen i glaset först.", "Häll försiktigt vattnet längs glasets insida eller över en sked på saltlösningen.", "Häll slutligen oljan försiktigt ovanpå på samma sätt.", "Studera lagren. Stämde förutsägelsen?", "Diskutera: varför blandas inte olja och vatten? Varför lägger sig saltlösningen under vanligt vatten?"],
 resultat="Matoljan flyter överst, sedan vattnet och underst saltlösningen om lösningen är tillräckligt salt. Lagren mellan vatten och saltlösning kan blandas lite med tiden och försiktighet behövs vid hällning. Förklaring med densitet och partikelmodell: i saltlösningen finns mer massa per volym.",
 sakerhet=["Använd skyddsglasögon.", "Smaka inte på något.", "Torka upp spill, olja kan göra golvet halt."],
 problem=["Lagren blandas när man häller för snabbt: häll långsamt längs glaset eller över en sked.", "Saltlösningen är för svag för att skilja sig från vatten: använd mer salt, men inte mer än vad som löser sig.", "Färgen sprider sig: använd bara några droppar."],
 bedom=[("Grundläggande", "Genomför försöket och beskriver ordningen på lagren."), ("Utvecklat", "Förutsäger ordningen med hjälp av densitet och jämför med resultatet."), ("Välutvecklat", "Förklarar lagren med densitet och partikelmodell och värderar vad som kan gå fel.")],
 forslag=["Vad händer om du lägger i en isbit eller en liten bit plast i tornet?", "Kan du bygga ett torn med fyra lager genom att lösa olika mängd salt?", "Hur påverkar temperaturen hur fort lagren blandas?"],
)
ELEV_HTML = ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
 '<div class="sh small"><h2>Densitetstorn</h2></div>'
 '<p><b>Frågeställning:</b> I vilken ordning lägger sig matolja, vatten och saltlösning i ett glas?</p><p><b>Min förutsägelse:</b> Underst ____________, i mitten ____________, överst ____________, eftersom …</p>' + lines(2) +
 '<h3>Densitetsvärden</h3>' + table(["Vätska", "Densitet (g/cm³)"], [["Olivolja", "ca 0,91"], ["Vatten", "ca 1,0"], ["Havsvatten", "ca 1,03"]], "tbl num") +
 '<h3>Resultat</h3><p>Rita eller skriv hur lagren hamnade.</p>' + lines(3) +
 '<h3>Frågor</h3><ol class="steps g"><li>Stämde din förutsägelse?</li></ol>' + lines(2) +
 '<ol class="steps g"><li>Förklara med densitet varför lagren hamnade så.</li></ol>' + lines(3) +
 '<ol class="steps g"><li>Vad hände om du hällde för snabbt? Förklara med partiklar.</li></ol>' + lines(2) + '</section>')
RUTOR = []

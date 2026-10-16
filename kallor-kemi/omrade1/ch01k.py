# -*- coding: utf-8 -*-
"""Kemi område 1 Kemi som vetenskap – grundtext (per moment). Samma format som biologins kapitel."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
FIG = '/tmp/kem/fig01k/'
NR = 1
SLUG = "kemi-vetenskap"
TAB = "1"
NAMN = "Kemi som vetenskap"
UNDER = "Så undersöker och tänker en kemist"
INTRO = ("Hur kan en brustablett försvinna i ett vattenglas, och varför går det fortare i varmt vatten än i kallt? Hur vet en tillverkare att en fläckborttagare verkligen fungerar? Och varför trodde människor i över tvåtusen år att allt var gjort av bara fyra element? "
         "Kemi handlar om ämnen och hur de förändras, men också om hur kemister arbetar: de ställer frågor, mäter, jämför och granskar varandras svar. "
         "I det här kapitlet lär du dig arbeta säkert i ett kemilabb, planera ett rättvist försök och värdera resultatet. Du lär dig också vad en modell är, hur kemin har vuxit fram och hur du granskar påståenden om kemi. Namn och mätvärden i uppgifterna är påhittade, om inget annat står.")
MAL = ["hur du arbetar säkert i ett kemilabb och läser av mätutrustning", "hur du går från en fråga till en plan med hypotes och variabler",
       "hur du dokumenterar, räknar medelvärde och värderar ett resultat", "hur du genomför ett rättvist försök med en brustablett",
       "vad en modell är i kemi och varför modeller kan förändras", "hur kemin vuxit fram från de fyra elementen till atomteorin",
       "hur du granskar påståenden om kemi, till exempel i reklam"]
FUNDERA = "Titta på produkterna i ditt kök eller badrum: diskmedel, tvål, tandkräm, rengöring. Vilka tror du är ”kemikalier” och vilka är det inte? Skriv ner din gissning och spara den. I slutet av kapitlet får du se om du ändrar dig."
DELOMR = {"1.1": "Arbeta som kemist", "1.2": "Modeller, källor och argument"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)

KQ = {
 "Start": [("Vad handlar kemi om?", "Om ämnen och hur de förändras, till exempel när något löses upp, rostar, bränns eller blandas."),
           ("Nämn tre sorters arbete där man behöver kemi.", "T.ex. analytisk kemist (mäter vad prov innehåller), läkemedelskemist, materialkemist, miljökemist."),
           ("Varför räcker det inte att bara läsa om kemi för att förstå den?", "Kemi är en naturvetenskap: svaren prövas genom undersökningar och mätningar, inte bara genom att man tror eller läser.")],
 "1.1.1": [("Nämn tre regler du alltid följer i ett kemilabb.", "T.ex. skyddsglasögon, långt hår uppsatt, aldrig smaka eller dricka, ingen mat i labbet, tvätta händerna, berätta för läraren om något går fel."),
           ("Vad betyder en röd ruta med en brinnande låga som faropiktogram?", "Ämnet är brandfarligt: det kan antändas lätt."),
           ("Vad står på en kemikalieetikett förutom produktnamnet?", "Faropiktogram, signalord (Fara eller Varning), faroangivelser och leverantörens kontaktuppgifter."),
           ("Hur läser du av en mätcylinder rätt?", "Ögonen i nivå med vattenytan, och du läser av vid den lägsta delen av den böjda ytan (menisken)."),
           ("Vad gör du om du misstänker att någon fått i sig något farligt?", "Ring 112 och begär Giftinformationscentralen. Vänta inte på symtom. Vid mindre bråttom: 010-456 67 00.")],
 "1.1.2": [("Vad är en hypotes?", "En välgrundad gissning som går att pröva i en undersökning, ofta på formen ”om … så …, eftersom …”."),
           ("Vad är skillnaden mellan den oberoende och den beroende variabeln?", "Den oberoende variabeln ändrar du. Den beroende mäter du för att se om den påverkas."),
           ("Varför ska bara en variabel ändras i taget?", "Annars vet du inte vad som orsakade skillnaden i resultatet."),
           ("Ge två exempel på kontrollerade variabler i brustablettförsöket.", "T.ex. vattenmängd, tablettens storlek och sort, glasets form, att alla startar och stoppar klockan på samma sätt.")],
 "1.1.3": [("Varför ska man upprepa mätningarna?", "För att se hur mycket värdena varierar och för att minska risken att ett slumpfel avgör resultatet."),
           ("Räkna ut medelvärdet av 70 s, 78 s och 74 s.", "(70 + 78 + 74) / 3 = 74 s."),
           ("Vad är en felkälla? Ge ett exempel.", "Något som kan göra mätningen mindre säker, t.ex. att man startar klockan sent, läser av termometern fel eller att vattnet svalnar."),
           ("Vad ska en slutsats innehålla?", "Ett svar på frågeställningen som bygger på resultatet, och om hypotesen stämde.")],
 "1.2.1": [("Vad är en modell i kemi?", "En förenkling som hjälper oss att förklara och förutsäga något vi inte kan se eller mäta direkt."),
           ("Varför är en modell inte samma sak som verkligheten?", "Den lämnar medvetet bort detaljer. Den kan förklara vissa saker men inte allt."),
           ("Ge ett exempel på något en modell kan förklara och något den inte kan förklara.", "T.ex. partikelmodellen förklarar varför gas fyller hela rummet, men säger inget om ämnets färg."),
           ("Vad händer med en modell när nya undersökningar visar något den inte kan förklara?", "Modellen ändras eller byts ut mot en bättre.")],
 "1.2.2": [("Vad ansåg Empedokles och Aristoteles att allt var uppbyggt av?", "Fyra element (jord, vatten, luft och eld)."),
           ("Vad gjorde Boyle annorlunda?", "Han tvivlade på de fyra elementen och krävde att påståenden skulle prövas med försök."),
           ("Vad visade Lavoisier med sina vägningar?", "Att massan är lika stor före och efter en reaktion: ingenting försvinner."),
           ("Vad säger Daltons atomteori om grundämnen?", "Att ett grundämne består av atomer som är lika varandra och väger lika mycket, och att olika grundämnen har olika atomer."),
           ("Varför är det en styrka att modeller kan ändras?", "Man kan rätta fel och förbättra förklaringarna när nya undersökningar visar mer.")],
 "1.2.3": [("Vilka frågor ställer du för att granska ett påstående?", "Vem säger det, varför, vilka belägg finns, hur gammalt är det och säger andra källor samma sak?"),
           ("Varför är ordet ”kemikaliefri” missvisande?", "Allt är gjort av kemiska ämnen, även vatten och luft. Ordet säger inte något om hur farlig produkten är."),
           ("Är allt som är naturligt ofarligt? Motivera.", "Nej. Naturliga ämnen kan vara giftiga, t.ex. gift i flugsvamp. Om något är farligt beror på ämnet och mängden, inte på om det är naturligt."),
           ("Varför är en reklam inte en tillräcklig källa för att veta om en produkt fungerar?", "Avsändaren vill sälja och väljer vad som visas. Man behöver oberoende belägg eller ett eget rättvist test.")],
}
def kq(key):
    return kolla(key if key != "Start" else "Start", [q for q, a in KQ[key]])

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad är kemi?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p><strong class='green'>Kemi</strong> är läran om ämnen och hur de förändras. Allt du ser, äter och rör vid är gjort av kemiska ämnen: vatten, socker, plast, tvål, luft. När en brustablett löser sig, när järn rostar eller när mat tillagas sker kemiska förändringar. Kemi är därför inte något som bara finns i ett labb.</p>"
     "<p>Kemi är också en <strong class='green'>naturvetenskap</strong>. Det betyder att kemister inte nöjer sig med att tro eller gissa. De ställer frågor, gör undersökningar, mäter och prövar sina förklaringar mot det som verkligen händer. Andra kemister kontrollerar och upprepar försöken. Det är det som gör att vi kan lita på kunskapen.</p>"
     "<p>Det finns många slags kemister. Några exempel är <strong class='green'>analytiska kemister</strong> som mäter vad ett prov innehåller, <strong class='green'>läkemedelskemister</strong> som tar fram och testar läkemedel, <strong class='green'>materialkemister</strong> som utvecklar material som plast och batterier och <strong class='green'>miljökemister</strong> som undersöker föroreningar i luft, vatten och mark.</p>"
     "<p>I det här kapitlet svarar vi på tre frågor:</p>"
     + bullets(["Hur arbetar en kemist säkert, planerar ett rättvist försök och värderar resultatet?", "Vad är en modell, och hur har kemins modeller förändrats?", "Hur granskar du påståenden om kemi, till exempel i reklam?"]),
   [begrepp([("Kemi", "Läran om ämnen och hur de förändras."), ("Naturvetenskap", "Kunskap som prövas med undersökningar och mätningar."), ("Ämne", "En sorts material med bestämda egenskaper, t.ex. vatten eller socker.")]),
    box("tank", "Tänk efter", "<p>Nämn tre kemiska förändringar du har sett den här veckan. Hur vet du att det är en förändring och inte bara en blandning?</p>")])
 + table(["Delområde", "Du lär dig"],
         [["<b>1.1</b> Arbeta som kemist", "Säkerhet och utrustning, att gå från fråga till plan och att dokumentera och värdera. Labb: brustabletten och temperaturen."],
          ["<b>1.2</b> Modeller, källor och argument", "Vad en modell är, hur kemin vuxit fram och hur du granskar påståenden. Labb: fungerar fläckborttagaren?"]])
 + kq("Start"))

# ------------------------------------------------------------------ 1.1.1
add("1.1.1", "Säkerhet och utrustning i kemilabbet", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · Säkerhet och utrustning i kemilabbet",
 "<p>I ett kemilabb arbetar du med ämnen som kan vara farliga om de hanteras fel. Därför har alla samma grundregler. De skyddar både dig och dem du arbetar med.</p>"
 + fig(FIG+"v_utrustning.png", "<b>Bild 1.1</b> Vanlig utrustning i ett kemilabb: mätcylinder, bägare, E-kolv, provrör, våg, termometer, pipett och skyddsglasögon.", "96%")
 + row("<h3 style='margin-top:0'>Grundregler</h3>"
       + bullets(["Använd <strong class='green'>skyddsglasögon</strong> hela tiden när du arbetar med kemikalier eller värme.",
                  "Sätt upp långt hår, ha inga hängande smycken och bär stängda skor.",
                  "Smaka, sniffa och dricka aldrig något i labbet, och ät inte där.",
                  "Läs hela instruktionen innan du börjar och ta bara den mängd du behöver.",
                  "Torka upp spill direkt och berätta för läraren om något går sönder eller spills.",
                  "Tvätta händerna när du är klar.",
                  "Vet du inte vad ett ämne är? Fråga innan du använder det."]),
       [box("tank", "Tänk efter", "<p>Varför är regeln om skyddsglasögon viktig även när ni bara använder vatten och en brustablett?</p>")])
 + "<h3>Faropiktogram och etiketter</h3>"
 + "<p>Farliga produkter är märkta med <strong class='green'>faropiktogram</strong>: röda rutor på spetsen med en svart bild. De visar vilken sorts fara det handlar om. På etiketten finns också ett <strong class='green'>signalord</strong>, antingen <i>Fara</i> (för de allvarligaste farorna) eller <i>Varning</i>, och <strong class='green'>faroangivelser</strong> som beskriver farorna med ord. Där står också produktens namn och leverantörens kontaktuppgifter.</p>"
 + fig(FIG+"v_piktogram.png", "<b>Bild 1.2</b> De nio faropiktogrammen: explosivt, brandfarligt, oxiderande, gas under tryck, frätande, akut giftigt, hälsofarligt, varning (utropstecken) och miljöfarligt.", "96%")
 + row("<h3 style='margin-top:0'>Mäta rätt</h3><p>Kemister mäter volym, massa och temperatur. <strong class='green'>Volym</strong> mäts i milliliter (ml) med en mätcylinder. Vattnets yta är lite böjd, och den böjda ytan kallas <strong class='green'>menisk</strong>. Du håller ögonen i nivå med ytan och läser av vid den lägsta delen. <strong class='green'>Massa</strong> mäts i gram (g) med en våg. <strong class='green'>Temperatur</strong> mäts i grader Celsius (°C) med en termometer. Låt termometern hänga fritt i vätskan och vänta tills värdet slutat ändras innan du läser av.</p>",
       [fig(FIG+"v_menisk.png", "<b>Bild 1.3</b> Avläsning av en mätcylinder. Håll ögonen i nivå med ytan. Fel avläsning ger fel värde.", "100%")])
 + box("visste", "Om något går fel", "<p>Få kemikalier i ögonen: skölj genast med mycket vatten och säg till läraren. Misstänker du att någon fått i sig något farligt: ring <b>112</b> och begär Giftinformationscentralen. Vänta inte på symtom. Vid mindre bråttom kan du ringa Giftinformationscentralen på <b>010-456 67 00</b>, dygnet runt.</p>")
 + kq("1.1.1"))

# ------------------------------------------------------------------ 1.1.2
add("1.1.2", "Från fråga till plan", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · Från fråga till plan",
 row("<p>En undersökning börjar med en fråga. Inte alla frågor går att undersöka i ett kemilabb. ”Är brustabletter goda?” är en fråga om tycke. ”Hur påverkar vattnets temperatur tiden det tar för en brustablett att lösa sig?” är en <strong class='green'>undersökningsbar fråga</strong>: du kan mäta svaret.</p>"
     "<p>Sedan skriver du en <strong class='green'>hypotes</strong>. Det är en gissning som du kan pröva, helst med en förklaring: ”<i>Om vattnet är varmare, så löser tabletten sig fortare, eftersom allt rör sig snabbare i varmt vatten.</i>” En hypotes kan visa sig vara fel. Det är också ett viktigt resultat.</p>",
   [begrepp([("Undersökningsbar fråga", "En fråga som går att svara på med mätningar."), ("Hypotes", "En gissning som går att pröva."), ("Variabel", "Något som kan ändras eller mätas i ett försök.")])])
 + fig(FIG+"v_brus.png", "<b>Bild 1.4</b> Tre glas med brustablett. Samma mängd vatten och samma sorts tablett i alla glas. Det enda som ändras är temperaturen.", "96%")
 + "<h3>Variabler</h3>"
 + "<p>I ett försök finns tre sorters <strong class='green'>variabler</strong>. Den <strong class='green'>oberoende variabeln</strong> är det du ändrar, här vattnets temperatur. Den <strong class='green'>beroende variabeln</strong> är det du mäter för att se om den påverkas, här tiden tills tabletten är upplöst. Alla andra saker som kan påverka resultatet, till exempel vattenmängd, tablettens storlek och sort och hur du startar och stoppar klockan, ska du hålla lika. De kallas <strong class='green'>kontrollerade variabler</strong>.</p>"
 + table(["Sorts variabel", "I brustablettförsöket"],
         [["Oberoende (jag ändrar)", "Vattnets temperatur: 5 °C, 20 °C och 40 °C"], ["Beroende (jag mäter)", "Tid tills tabletten är upplöst, i sekunder"], ["Kontrollerade (jag håller lika)", "Vattenmängd, tablettsort och storlek, glasets form, ingen omrörning, samma sätt att mäta tiden"]])
 + roww("<h3 style='margin-top:0'>Ett rättvist försök</h3><p>Ett försök är <strong class='green'>rättvist</strong> om du bara ändrar en variabel i taget. Ändrar du två saker samtidigt, till exempel både temperatur och vattenmängd, kan du inte veta vilken som gav skillnaden. Ofta behöver du också en <strong class='green'>jämförelse</strong>, ett prov där du inte ändrar något, så att du har något att jämföra med.</p>"
        "<p>Skriv sedan en <strong class='green'>plan</strong> innan du börjar: vilken utrustning du behöver, vad du gör i vilken ordning, hur du mäter och hur många gånger du upprepar. Gör också en tom tabell att fylla i.</p>",
        [box("tank", "Tänk efter", "<p>Du vill veta om en sockerbit löser sig fortare om du rör om. Vilken variabel ändrar du, vilken mäter du och vad håller du lika?</p>")])
 + kq("1.1.2"))

# ------------------------------------------------------------------ 1.1.3
add("1.1.3", "Dokumentera och värdera", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · Dokumentera och värdera",
 row("<p>Skriv ner det du mäter medan du mäter, inte efteråt. Använd en <strong class='green'>tabell</strong> med rubriker och <strong class='green'>enheter</strong> (till exempel s för sekunder och °C för grader Celsius). Ett tal utan enhet säger nästan ingenting.</p>"
     "<p>Gör alltid flera mätningar för samma sak. Då ser du hur mycket värdena varierar, och slumpen får mindre makt över resultatet. För varje temperatur räknar du ut <strong class='green'>medelvärdet</strong>: lägg ihop alla värden och dela med antalet. Av 70 s, 78 s och 74 s blir medelvärdet (70 + 78 + 74) / 3 = 74 s.</p>",
   [begrepp([("Medelvärde", "Summan av värdena delat med antalet värden."), ("Felkälla", "Något som kan göra en mätning mindre säker."), ("Slutsats", "Svaret på frågan, byggt på resultatet.")])])
 + fig(FIG+"v_brusdiagram.png", "<b>Bild 1.5</b> Medelvärden från ett exempelförsök med brustablett. Mätvärdena är påhittade.", "86%")
 + "<p>Ett <strong class='green'>diagram</strong> gör mönster lättare att se. Lägg det du ändrar (temperaturen) på den vågräta axeln och det du mäter (tiden) på den lodräta. Skriv ut namn och enhet på båda axlarna och sätt en rubrik.</p>"
 + roww("<h3 style='margin-top:0'>Värdera resultatet</h3><p>Fråga dig: Svarar resultatet på frågan? Stämde hypotesen? Vilka <strong class='green'>felkällor</strong> kan ha påverkat? Det kan vara att klockan startades sent, att termometern lästes av fel eller att vattnet hann svalna. Skriv hur du skulle göra annorlunda nästa gång.</p>"
        "<p>Slutsatsen ska bygga på dina egna mätningar. Skriv den som ett svar på frågan: ”<i>Ju varmare vatten, desto kortare tid tog det för tabletten att lösa sig. Hypotesen stämde.</i>” Skriv också hur säker du är. Hade du få mätningar eller stora skillnader mellan försöken är du mindre säker. Om ett värde sticker ut kan du undersöka om det beror på ett misstag, men du får inte bara ta bort det för att det inte passar.</p>",
        [box("tank", "Tänk efter", "<p>Tre grupper mäter 148 s, 160 s och 148 s för samma temperatur. Är värdena lika nog för att lita på medelvärdet? Varför?</p>")])
 + kq("1.1.3"))

# ------------------------------------------------------------------ Labb 1.1
add("Labb", "1.1 Brustabletten och temperaturen", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · Labb 1.1 Brustabletten och temperaturen",
 "<p>Du ska undersöka hur vattnets temperatur påverkar hur fort en brustablett löser sig, och följa hela vägen från fråga till slutsats.</p>"
 + roww("<p><strong class='green'>Frågeställning:</strong> Hur påverkar vattnets temperatur tiden det tar för en brustablett att lösa sig?</p><p><strong class='green'>Hypotes:</strong> Skriv din hypotes med ”om … så …, eftersom …”.</p>"
        "<p><strong class='green'>Material:</strong> tre genomskinliga glas (samma sort), mätcylinder, termometer, ur eller stoppur, brustabletter av samma sort (minst nio), kallt vatten med is, kranvatten och varmt vatten, skyddsglasögon.</p><h3>Gör så här</h3>"
        + steps(["Mät upp samma mängd vatten i varje glas, till exempel 2 dl (200 ml).",
                 "Gör vattnet cirka 5 °C, 20 °C och 40 °C. Kontrollera med termometern. Använd inte varmare vatten än 40 °C.",
                 "Släpp ner en hel tablett i det första glaset och starta klockan i samma stund. Rör inte om.",
                 "Stoppa klockan när tabletten har försvunnit helt. Skriv tiden i tabellen.",
                 "Upprepa med nytt vatten, tre försök för varje temperatur.",
                 "Räkna ut medelvärdet för varje temperatur och rita ett stapeldiagram."]),
        [box("begrepp", "Begrepp", "<b class='t'>Oberoende variabel</b><p>Det du ändrar.</p><b class='t'>Beroende variabel</b><p>Det du mäter.</p><b class='t'>Medelvärde</b><p>Summan delat med antalet.</p>"),
         box("tank", "Bra att veta", "<p>Brustabletten innehåller bland annat citronsyra och natriumvätekarbonat. När de kommer i vatten reagerar de med varandra och bildar koldioxidgas. Det är bubblorna du ser.</p>")])
 + table(["Temperatur", "Försök 1 (s)", "Försök 2 (s)", "Försök 3 (s)", "Medelvärde (s)"], [["5 °C", "", "", "", ""], ["20 °C", "", "", "", ""], ["40 °C", "", "", "", ""]], "tbl num")
 + "<h3>Frågor</h3>"
 + steps(["Vilken variabel ändrade du, vilken mätte du och vad höll du lika?", "Vad visar ditt diagram? Stämde din hypotes?", "Förklara resultatet. Hur kan det hänga ihop med att partiklarna rör sig snabbare i varmt vatten?", "Vilka felkällor kan ha påverkat resultatet, och hur skulle du minska dem?", "Hur kan du göra försöket säkrare att lita på?"], True)
 + '<p class="note">Säkerhet: Använd skyddsglasögon. Drick inte av vattnet eller tabletterna. Använd inte varmare vatten än 40 °C. Torka upp spill direkt.</p>')

# ------------------------------------------------------------------ 1.2.1
add("1.2.1", "Vad är en modell i kemi?", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · Vad är en modell i kemi?",
 row("<p>Kemister arbetar med sådant som är för litet att se. Därför använder de <strong class='green'>modeller</strong>. En modell är en förenklad bild eller idé som hjälper oss att förklara och förutsäga hur något fungerar. En modell är inte verkligheten. Den lämnar medvetet bort detaljer, precis som en karta lämnar bort de flesta saker som finns i landskapet.</p>"
     "<p>Ett exempel är <strong class='green'>partikelmodellen</strong>. I den tänker vi oss att ett ämne är uppbyggt av små partiklar. I ett fast ämne sitter de tätt på fasta platser. I en vätska ligger de tätt men kan glida förbi varandra. I en gas är det stora avstånd och partiklarna rör sig fritt. Du lär dig mer om partikelmodellen i kapitel 2.</p>",
   [begrepp([("Modell", "En förenkling som förklarar och förutsäger."), ("Begränsning", "Det en modell inte kan förklara.")])])
 + fig(FIG+"l_modell.png", "<b>Bild 1.6</b> Partikelmodellen för fast ämne, vätska och gas. Partiklarna är i verkligheten otroligt mycket mindre än i bilden.", "96%")
 + roww("<h3 style='margin-top:0'>Vad modellen kan och inte kan</h3><p>Med partikelmodellen kan du förklara varför en gas fyller hela rummet och varför en brustablett löser sig fortare i varmt vatten: partiklarna rör sig snabbare. Men modellen säger ingenting om ämnets färg eller lukt, och i bilden ser partiklarna ut som runda bollar, vilket är en förenkling. När vi frågar något som modellen inte kan svara på behöver vi en annan eller en bättre modell.</p>"
        "<p>Modeller finns överallt i vardagen: en karta, ett kretsschema, en molekylmodell av kulor och pinnar. Alla är förenklingar som är bra för ett visst syfte.</p>",
        [box("tank", "Tänk efter", "<p>En karta över Luleå är en modell. Vad kan du se på kartan, och vad kan du inte se? Vad skulle du behöva en annan modell för?</p>")])
 + kq("1.2.1"))

# ------------------------------------------------------------------ 1.2.2
add("1.2.2", "Hur kemin vuxit fram", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · Hur kemin vuxit fram",
 row("<p>Kemisk kunskap har vuxit fram under tusentals år. De första förklaringarna kom från filosofer som tänkte ut hur världen fungerar. Den grekiske filosofen <strong class='green'>Empedokles</strong> (ca 450 f.Kr.) menade att allt är uppbyggt av fyra ”rötter”: jord, vatten, luft och eld. <strong class='green'>Aristoteles</strong> (ca 350 f.Kr.) byggde ut läran om de fyra elementen, och den levde kvar i över tvåtusen år.</p>"
     "<p>Under medeltiden försökte alkemister bland annat göra guld av andra ämnen. De lyckades inte, men de utvecklade många arbetssätt och redskap som kemin senare använde.</p>",
   [begrepp([("Grundämne", "Ämne som inte går att dela upp i enklare ämnen med kemiska metoder."), ("Atom", "Den minsta delen av ett grundämne som behåller grundämnets egenskaper.")])])
 + fig(FIG+"v_tidslinje.png", "<b>Bild 1.7</b> Fem steg i kemins historia, från Empedokles till Dalton.", "96%")
 + "<h3>Från tro till försök</h3>"
 + "<p>År 1661 gav den engelske forskaren <strong class='green'>Robert Boyle</strong> ut boken <i>The Sceptical Chymist</i>. Han tvivlade på de fyra elementen och krävde att påståenden skulle prövas med försök. Det var ett viktigt steg mot kemi som experimentell vetenskap.</p>"
 + roww("<p>Fransmannen <strong class='green'>Antoine Lavoisier</strong> använde noggranna vågar. År 1789 beskrev han att massan är lika stor före och efter en reaktion i ett slutet kärl: ingenting försvinner, ämnena bara ändrar form. Han gav också syre dess namn. Du ser tanken i bild 1.8: en sluten flaska med en tablett och vatten väger lika mycket före och efter reaktionen, eftersom gasen blir kvar i flaskan.</p>",
        [fig(FIG+"v_massa.png", "<b>Bild 1.8</b> Massan är lika före och efter reaktionen när inget släpper ut ur flaskan.", "100%")])
 + roww("<p>Engelsmannen <strong class='green'>John Dalton</strong> kom 1808 med en <strong class='green'>atomteori</strong>. Han föreslog att varje grundämne består av små atomer som är lika varandra och väger lika mycket, och att atomer av olika ämnen väger olika. Han menade att föreningar bildas när atomer sätts ihop i enkla förhållanden, till exempel en kolatom och en syreatom i kolmonoxid. Atomerna skapas inte och försvinner inte i en reaktion. Det passade med Lavoisiers vägningar.</p>"
        "<p>Daltons teori är en modell. Idag vet vi mer: atomerna består själva av ännu mindre delar. Men grundtanken att allt är uppbyggt av atomer lever kvar.</p>",
        [fig(FIG+"v_dalton.png", "<b>Bild 1.9</b> Två av Daltons idéer: atomer av olika ämnen väger olika, och föreningar bildas i enkla förhållanden.", "100%")])
 + box("tank", "Tänk efter", "<p>Läran om fyra element levde över 2 000 år. Vad fick till slut forskarna att byta modell? Varför är det bra att en modell kan bytas ut?</p>")
 + kq("1.2.2"))

# ------------------------------------------------------------------ 1.2.3
add("1.2.3", "Granska kemipåståenden", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · Granska kemipåståenden",
 row("<p>Du möter påståenden om kemi hela tiden: ”Ny fläckborttagare – tar bort allt!”, ”Kemikaliefritt”, ”100 % naturligt”. Några stämmer, andra är reklam eller halvsanningar. Därför behöver du kunna <strong class='green'>granska</strong> dem, och här är <strong class='green'>källkritik</strong> ett verktyg.</p>"
     + steps(["<b>Vem</b> säger det? Är det en forskare, en myndighet, ett företag eller en privatperson?", "<b>Varför</b> säger de det? Vill de informera, övertyga eller sälja?", "<b>Vilka belägg</b> finns? Hänvisar de till mätningar eller undersökningar du kan se?", "<b>Hur gammal</b> är informationen? Har kunskapen ändrats?", "<b>Vad säger andra källor?</b> Finns det oberoende källor som säger samma sak?"], True),
   [begrepp([("Källkritik", "Att granska vem som säger något, varför och med vilka belägg."), ("Påstående", "Något som sägs vara sant."), ("Belägg", "Mätningar eller undersökningar som stöder ett påstående.")])])
 + "<h3>”Kemikaliefritt” och ”naturligt”</h3>"
 + roww("<p>Ordet <strong class='green'>kemikalie</strong> betyder egentligen kemiskt ämne. Vatten, salt, socker och syre är alla kemikalier. Därför kan ingenting vara bokstavligen ”kemikaliefritt”. Ordet används ofta för att säga ”utan ämnen jag tycker är farliga”, men det säger inget om vilka ämnen det gäller eller hur farliga de är.</p>"
        "<p>”Naturligt” betyder inte heller ofarligt. Flugsvampen är naturlig men giftig. Om något är farligt beror på vilket ämne det är och hur mycket man får i sig, inte på om det kommer från naturen eller en fabrik.</p>",
        [box("tank", "Tänk efter", "<p>Du ser en annons: ”Vår tvål är kemikaliefri och därför helt ofarlig.” Vilka frågor ställer du?</p>")])
 + "<h3>Vad går att pröva?</h3>"
 + "<p>Vissa påståenden går att pröva själv med ett rättvist försök. ”Fläckborttagare X tar bort fläckar bättre än vanligt diskmedel” kan du undersöka: du väljer en fläck, använder samma mängd, samma tid och en jämförelse med bara vatten. Andra påståenden, som ”den är bäst”, går inte att pröva eftersom det inte är tydligt vad ”bäst” betyder. En bra granskare frågar alltid: <i>Går det här att mäta, och vem har mätt?</i></p>"
 + kq("1.2.3"))

# ------------------------------------------------------------------ Labb 1.2
add("Labb", "1.2 Fungerar fläckborttagaren?", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · Labb 1.2 Fungerar fläckborttagaren?",
 "<p>En reklam påstår att ”Fläckborttagare X” tar bort fläckar bättre än andra produkter. Du ska planera och genomföra ett rättvist test av påståendet. Produktnamnet är påhittat.</p>"
 + fig(FIG+"v_flack.png", "<b>Bild 1.10</b> Fyra tygbitar med likadan fläck och fyra vätskor: A bara vatten (jämförelse), B diskmedel, C fläckborttagare X och D tvättmedel.", "96%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Tar fläckborttagare X bort en fläck bättre än bara vatten, diskmedel och tvättmedel?</p><p><strong class='green'>Hypotes:</strong> Skriv vilken du tror är bäst och varför.</p>"
        "<p><strong class='green'>Material:</strong> fyra likadana tygbitar (vit bomull) med samma fläck (till exempel te eller kaffe som fått torka), fyra glas, mätcylinder, de fyra vätskorna, sked eller pinne, ur, skyddsglasögon, handskar och en referensskala (se nedan).</p><h3>Planera och gör så här</h3>"
        + steps(["Bestäm vad du ändrar (vätskan), vad du mäter (hur ljus fläcken blir) och vad du håller lika: fläckens storlek, mängden vätska, tiden och hur du rör.",
                 "Gör fläckarna likadana och låt dem torka. Märk tygbitarna A–D.",
                 "Häll samma mängd av varje vätska i varsitt glas. Lägg tygbitarna i vätskorna och låt dem ligga lika länge. Rör lika mycket.",
                 "Skölj lika länge och låt torka. Jämför mot en referensskala: 0 = ingen skillnad, 1 = lite ljusare, 2 = mycket ljusare, 3 = fläcken är borta.",
                 "Låt en kamrat som inte vet vilken som är vilken sätta poäng. Då påverkar förväntningarna inte resultatet.",
                 "Gör om försöket minst en gång. Skriv resultatet i tabellen."]),
        [box("begrepp", "Begrepp", "<b class='t'>Jämförelse</b><p>Ett prov utan det du testar, här bara vatten.</p><b class='t'>Belägg</b><p>Resultat som stöder eller motsäger ett påstående.</p>"),
         box("tank", "Bra att veta", "<p>Läs etiketten på produkterna innan du börjar. Blanda aldrig olika rengöringsmedel med varandra.</p>")])
 + table(["Vätska", "Poäng försök 1", "Poäng försök 2", "Medelvärde"], [["A Bara vatten", "", "", ""], ["B Diskmedel", "", "", ""], ["C Fläckborttagare X", "", "", ""], ["D Tvättmedel", "", "", ""]], "tbl num")
 + "<h3>Frågor</h3>"
 + steps(["Vilken vätska tog bort fläcken bäst? Stämmer det med reklamens påstående?", "Varför är det bra med en jämförelse med bara vatten och en kamrat som sätter poäng?", "Vilka felkällor kan ha påverkat? Hur kan du minska dem?", "Vad kan du säga och inte säga om fläckborttagare X utifrån just ditt test? Vilka fläckar och tyger testade du inte?"], True)
 + '<p class="note">Säkerhet: Använd skyddsglasögon och handskar. Läs etiketten. Blanda aldrig produkter. Drick inte och undvik att andas in ångor; vädra. Tvätta händerna efteråt.</p>')

SAMMAN = ["<strong>Kemi</strong> är läran om ämnen och hur de förändras. Kemi är en naturvetenskap: svaren prövas med undersökningar och mätningar.",
          "I kemilabbet använder du skyddsglasögon, sätter upp långt hår, smakar aldrig på något och följer instruktionen. <strong>Faropiktogram</strong> och etiketter berättar om farorna.",
          "Du läser av en mätcylinder med ögonen i nivå med ytan, vid den lägsta delen av <strong>menisken</strong>.",
          "En <strong>hypotes</strong> är en gissning som går att pröva. I ett <strong>rättvist försök</strong> ändrar du en <strong>oberoende variabel</strong>, mäter en <strong>beroende variabel</strong> och håller övriga <strong>kontrollerade</strong>.",
          "Du upprepar mätningar, räknar <strong>medelvärde</strong>, redovisar i tabell och diagram med enheter och värderar <strong>felkällor</strong> innan du drar en <strong>slutsats</strong>.",
          "I brustablettförsöket gick det fortare ju varmare vattnet var. Det kan förklaras med att partiklarna rör sig snabbare.",
          "En <strong>modell</strong> är en förenkling som förklarar och förutsäger. Den har <strong>begränsningar</strong> och kan ändras när nya undersökningar visar mer.",
          "Läran om fyra element ersattes steg för steg: Boyle krävde försök, Lavoisier visade att massan bevaras och Dalton föreslog en <strong>atomteori</strong>.",
          "Med <strong>källkritik</strong> frågar du vem som säger något, varför, vilka belägg som finns, hur gammalt det är och vad andra källor säger.",
          "<strong>Kemikalie</strong> betyder kemiskt ämne. ”Kemikaliefritt” och ”naturligt” säger inte om något är farligt eller ofarligt."]

BEGR = [("Atom", "Den minsta delen av ett grundämne som behåller grundämnets egenskaper."), ("Atomteori", "Daltons idé från 1808 att allt består av atomer."), ("Belägg", "Mätningar eller undersökningar som stöder ett påstående."),
        ("Beroende variabel", "Det du mäter i ett försök."), ("Faropiktogram", "Symbol i röd ruta på spetsen som visar vilken fara ett ämne har."), ("Felkälla", "Något som gör en mätning mindre säker."),
        ("Grundämne", "Ämne som inte går att dela upp i enklare ämnen med kemiska metoder."), ("Hypotes", "En gissning som går att pröva."), ("Kemi", "Läran om ämnen och hur de förändras."),
        ("Kemikalie", "Kemiskt ämne, t.ex. vatten eller salt."), ("Kontrollerad variabel", "Något du håller lika i ett försök."), ("Källkritik", "Att granska vem som säger något, varför och med vilka belägg."),
        ("Medelvärde", "Summan av värdena delat med antalet."), ("Menisk", "Vätskeytans böjning i en mätcylinder."), ("Modell", "En förenkling som förklarar och förutsäger."),
        ("Oberoende variabel", "Det du ändrar i ett försök."), ("Partikelmodell", "Modell där ämnen är uppbyggda av små partiklar."), ("Rättvist försök", "Försök där bara en variabel ändras i taget."),
        ("Signalord", "Fara eller Varning på en etikett."), ("Slutsats", "Svaret på frågan, byggt på resultatet."), ("Undersökningsbar fråga", "Fråga som går att svara på med mätningar.")]

TEST = [
 ("A", "Vad betyder faropiktogrammet med en människa som har ett stjärnformat märke på bröstet?", ["A Ämnet är brandfarligt.", "B Ämnet kan vara hälsofarligt, till exempel skada organ eller arvsmassan.", "C Ämnet är bra för kroppen.", "D Ämnet är en gas under tryck."], 1, 0),
 ("A", "Hur läser du av en mätcylinder rätt?", ["A Med ögonen ovanför ytan och vid ytans övre kant.", "B Med ögonen i nivå med ytan och vid den lägsta delen av ytan.", "C Med ögonen under ytan.", "D Det spelar ingen roll."], 1, 0),
 ("A", "I ett försök undersöks hur mängden socker påverkar hur sött te smakar. Vilken är den oberoende variabeln?", ["A Hur sött teet smakar.", "B Mängden socker.", "C Mängden te.", "D Temperaturen på teet."], 1, 0),
 ("A", "Vem krävde 1661 att påståenden om kemi skulle prövas med försök?", ["A Empedokles", "B Aristoteles", "C Boyle", "D Dalton"], 2, 0),
 ("B", "Nämn två regler du alltid följer i ett kemilabb.", None, 1, 3),
 ("B", "Förklara vad en modell är i kemi.", None, 1, 3),
 ("C", "TABELL", None, 2, 5),
 ("C", "Mia testade tre fläckborttagare. Hon tog olika mycket av varje och lät dem verka olika länge. Förklara varför hennes jämförelse inte är rättvis och hur hon kan göra den rättvis.", None, 2, 5),
 ("D", "En annons säger: ”Vår kemikaliefria rengöring är säkrare än allt annat.” Granska påståendet. Förklara vad som är problemet med ordet ”kemikaliefri” och vilka frågor du skulle ställa för att avgöra om annonsen går att lita på.", None, 3, 6),
 ("D", "Läran om de fyra elementen levde i över 2 000 år innan den ersattes. Förklara varför det är en styrka för naturvetenskapen att modeller kan ändras. Använd ett exempel från kapitlet.", None, 3, 6),
 ("E", "Elias tror att en brustablett löser sig fortare om man rör om i vattnet. Planera en undersökning som kan pröva hans idé. Beskriv hypotes, vad du ändrar, vad du mäter, vad du håller lika, hur du upprepar mätningarna och hur du dokumenterar resultatet.", None, 3, 7),
 ("E", "En grupp mätte hur lång tid en brustablett tog att lösa sig (påhittade medelvärden): 10 °C: 132 s, 20 °C: 80 s, 30 °C: 52 s, 40 °C: 33 s, 50 °C: 22 s. Vilken tid skulle du uppskatta vid 35 °C? Förklara hur du kommer fram till det. Förklara också varför du inte kan vara säker på ett värde som ligger utanför det som är uppmätt, till exempel vid 80 °C.", None, 3, 7),
]
TEST_TABELL = (["Temperatur", "Försök 1 (s)", "Försök 2 (s)", "Försök 3 (s)"], [["20 °C", "140", "152", "146"], ["50 °C", "48", "52", "50"]])
TEST_D_TEXT = "Elin undersökte hur snabbt en sockerbit löses i 2 dl vatten av olika temperatur. Hon upprepade varje försök tre gånger. Resultaten är påhittade."
TEST_D_SUB = ["a) Räkna ut medelvärdet av tiden för varje temperatur.", "b) Förklara med partikelmodellen varför tiden skiljer sig mellan temperaturerna."]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Tolka resultat och förklara", "D": "Resonera och ta ställning", "E": "Planera och resonera"}
FACIT = [
 "B", "B", "B", "C",
 "T.ex. använd skyddsglasögon, sätt upp långt hår, smaka aldrig på något, ät inte i labbet, följ instruktionen, torka upp spill, tvätta händerna.",
 "En förenkling som hjälper oss att förklara och förutsäga något, till exempel något vi inte kan se. Den är inte verkligheten och har begränsningar.",
 "a) 20 °C: (140 + 152 + 146) / 3 = 146 s. 50 °C: (48 + 52 + 50) / 3 = 50 s. b) Vid högre temperatur rör sig partiklarna i vattnet snabbare, så de träffar sockerbiten oftare och hårdare och sockret lossnar fortare.",
 "Hon ändrar flera saker samtidigt (mängd och tid), så hon vet inte vad som gav skillnaden. Hon ska ändra bara produkten och hålla mängd, tid, fläck, tyg och sätt att skölja lika. Hon bör också ha en jämförelse med bara vatten.",
 "Öppet svar. Ett välutvecklat svar förklarar att allt är kemiska ämnen, även vatten, så ”kemikaliefri” inte kan stämma bokstavligt och inte säger hur farliga ämnena är. Frågor: vem säger det, varför (sälja?), vilka belägg och mätningar finns, vad menas med ”säkrare”, jämfört med vad, vad säger oberoende källor, och vilken märkning (piktogram, faroangivelser) har produkten.",
 "Öppet svar. Exempel: de fyra elementen byttes ut när Boyle krävde försök och Lavoisier och Dalton lade fram nya förklaringar som stämde bättre med mätningar. Att kunna ändra modellen gör att fel rättas och förklaringarna blir bättre. En vetenskap som aldrig ändrar sig kan inte lära sig något nytt.",
 "Hypotes, t.ex. ”Om man rör om löser tabletten sig fortare, eftersom vattnet nära tabletten byts ut.” Ändra: omrörning (med/utan). Mäta: tid tills tabletten är upplöst. Hålla lika: vattenmängd, temperatur, tablettsort och storlek, glas, sättet att mäta tid. Upprepa minst tre gånger för varje fall och räkna medelvärde. Dokumentera i tabell med enheter och gärna diagram, samt felkällor.",
 "Vid 35 °C ligger tiden mellan värdena vid 30 °C (ca 52 s) och 40 °C (ca 33 s), så ca 40–45 s. Kurvan sjunker mindre brant efter hand, så en rak linje mellan punkterna är en grov uppskattning. Vid 80 °C vet vi inte hur kurvan fortsätter eftersom inget är mätt där, och trenden kan ändras. Man kan inte vara säker utanför det uppmätta området.",
]
LGR = ("Området täcker det centrala innehållet om kemins arbetssätt i årskurs 7–9: säkerhet och hantering av kemikalier, planering, genomförande och värdering av systematiska undersökningar, modeller och hur de förändras över tid samt granskning av påståenden om kemi. "
       "Delområde 1.1 behandlar säkerhet och utrustning, att gå från fråga till plan och att dokumentera och värdera. Delområde 1.2 behandlar modeller, kemins historia och källkritik. "
       "Labbarna tränar att genomföra ett rättvist försök med en variabel i taget och att pröva ett påstående. Uppgifterna följer betygskriteriernas progression: från att namnge och beskriva till att förklara samband och resonera i flera led, och är inspirerade av frisläppta nationella prov i kemi.")
FAKTA = ("Uppgifterna i kapitlet kommer från öppnade källor och läroböcker; se lärarversionens källförteckning. Kontrollerat mot öppna källor: de nio faropiktogrammen och deras betydelse, signalorden Fara och Varning, vad en kemikalieetikett ska innehålla, Giftinformationscentralens telefonnummer, Kemisamfundets uttalanden om ordet kemikaliefri, uppgifter om Empedokles, Aristoteles, Boyle (1661), Lavoisier (1789) och Dalton (1808), brustablettens innehåll och koldioxidbildningen samt avläsning av menisk. "
         "Ej källkontrollerat: allmänna laboratoriesäkerhetsregler, alkemisternas strävan efter guld, att atomer har mindre delar, att flugsvamp är giftig och förklaringar med partikelmodellen. Tider och temperaturer i exempelförsöken är påhittade. "
         "Källor: Skolverket, Lgr22 kursplan i kemi. · Frisläppta nationella prov i kemi åk 9. · Illustrationer: egenritade för detta kapitel.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven förstår att kemi är läran om ämnen och förändringar, och att kemister arbetar genom att undersöka. Låt eleverna skriva sin lista över vad som är ”kemikalier” (Fundera) och spara den. Poängen är att allt är kemikalier, så att eleverna kan återvända till listan i 1.2.3.</p>
<p><b>Säkerhet och utrustning i kemilabbet.</b> C-mål: följa säkerhetsreglerna, tolka piktogram och läsa av mätutrustning rätt. Vanligt fel: att läsa av menisken uppifrån eller vid den övre kanten. Vanligt fel: att piktogram är bara dekoration. Låt eleverna hitta tre piktogram på produkter hemma.</p>
<p><b>Från fråga till plan.</b> C-mål: formulera en undersökningsbar fråga och hypotes och skilja oberoende, beroende och kontrollerade variabler. Vanligt fel: att hypotesen måste vara rätt, eller att fler variabler ändras samtidigt. Låt eleverna skriva egna hypoteser med ”om … så …, eftersom …”.</p>
<p><b>Dokumentera och värdera.</b> C-mål: redovisa i tabell och diagram, räkna medelvärde och värdera felkällor. Vanligt fel: att glömma enheter och axelrubriker; att ta bort ett värde för att det inte passar. Fördjupningen tar upp precision, riktighet och avvikande värden.</p>
<p><b>Labb 1.1 Brustabletten och temperaturen.</b> Material: tre glas, mätcylinder, termometer, ur, brustabletter, isvatten, varmt vatten. Förväntat: tiden minskar när temperaturen ökar, ungefär halverad mellan varje steg i exempeldata (152 s, 74 s, 31 s, påhittade). Vanliga fel: vattnet svalnar eller värms under mätningen, olika sätt att stoppa tiden, olika stora tablettbitar. Använd inte varmare vatten än 40 °C.</p>
<p><b>Vad är en modell i kemi?</b> C-mål: förklara vad en modell är och ge exempel på vad den kan och inte kan förklara. Partikelmodellen behandlas utförligt i kapitel 2; här används den som exempel. Vanligt fel: att modellen är en bild av hur det ”egentligen ser ut”.</p>
<p><b>Hur kemin vuxit fram.</b> C-mål: beskriva hur en modell förändrats med nya undersökningar, från fyra element till atomteori. Vanligt fel: att äldre forskare var ”dumma”. Lavoisiers vägning kan visas med brustablett i en sluten flaska eller plastpåse. Tablett och vatten ska vara åtskilda före (t.ex. i en liten kapsel), annars börjar reaktionen innan flaskan är stängd.</p>
<p><b>Granska kemipåståenden.</b> C-mål: granska ett påstående med flera frågor och motivera bedömningen. Vanligt fel: ”naturligt är ofarligt”, ”kemikaliefritt är säkrast”. Be eleverna ta med annonser från hemma eller tidningar.</p>
<p><b>Labb 1.2 Fungerar fläckborttagaren?</b> Material: vit bomull, te eller kaffe, vatten, diskmedel, tvättmedel och en fläckborttagare (produktnamnet X är påhittat i texten). Förväntat: resultaten varierar; ofta tar vatten bort lite, och de flesta produkterna är bättre. Låt eleverna jämföra med reklamens påstående och diskutera vad testet inte säger. Förbered fläckarna i förväg så att de hinner torka.</p>
"""
LAB_HTML = ""

BONUS = dict(
 titel="Sockerbit eller strösocker: vad löser sig fortast?",
 ingress="Eleverna jämför hur fort en sockerbit och samma mängd strösocker löser sig i vatten, och planerar själva ett rättvist försök. Ett enkelt sätt att träna variabler och upprepning.",
 syfte="Eleverna planerar och genomför ett försök med en variabel i taget, räknar medelvärde och värderar resultatet. Labben tränar systematiska undersökningar och kopplar till partikelmodellen (kapitel 2).",
 tid="Grupper om två till tre.",
 material=["Sockerbitar och strösocker (samma sort socker)", "Våg som mäter i gram", "Tre genomskinliga glas per grupp", "Mätcylinder, vatten av rumstemperatur", "Ur eller stoppur, sked eller pinne", "Skyddsglasögon", "Anteckningsblad"],
 genomf=["Låt eleverna formulera frågeställning och hypotes: vilket löser sig fortast, och varför?", "Väg upp lika mycket socker i form av sockerbit och strösocker, till exempel 4 g vardera.", "Mät upp lika mycket vatten av samma temperatur i glasen.", "Släpp ner sockret, starta klockan och stoppa när allt är upplöst. Rör inte, eller rör lika mycket i båda.", "Upprepa minst tre gånger för varje form och räkna medelvärde.", "Diskutera: vilka variabler hölls lika? Hur kan formen (stor bit eller små korn) kopplas till partikelmodellen?"],
 resultat="Strösockret löser sig fortare än sockerbiten. Förklaring: strösockret har större yta mot vattnet, så fler partiklar kommer i kontakt med vatten på samma gång. Läraren kan hänvisa till partikelmodellen i kapitel 2; den fördjupade förklaringen (ytan) är en förklaringsmodell, inte något eleverna måste kunna i kapitel 1.",
 sakerhet=["Använd skyddsglasögon.", "Ät eller drick inget i labbet, även om det är socker.", "Torka upp spill direkt."],
 problem=["Sockerbiten vägs inte lika mycket som strösockret: väg upp och använd jämna mängder (bryt vid behov).", "Olika vattentemperatur påverkar resultatet: mät upp vatten från samma kran och kontrollera med termometer.", "Omrörning görs olika: bestäm på förhand."],
 bedom=[("Grundläggande", "Genomför försöket och redovisar vilket som löste sig fortast."), ("Utvecklat", "Redovisar med medelvärden, håller variabler lika och drar slutsats."), ("Välutvecklat", "Värderar metoden, diskuterar felkällor och förklarar resultatet med en modell.")],
 forslag=["Löser sig socker fortare i varmt än kallt vatten?", "Påverkar omrörning hur fort sockret löser sig?", "Löser sig salt och socker lika fort?"],
)
ELEV_HTML = ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
 '<div class="sh small"><h2>Sockerbit eller strösocker</h2></div>'
 '<p><b>Frågeställning:</b> Vilket löser sig fortast i vatten: en sockerbit eller samma mängd strösocker?</p><p><b>Min hypotes:</b> Om … så …, eftersom …</p>' + lines(2) +
 '<h3>Variabler</h3>' + table(["Sorts variabel", "I mitt försök"], [["Jag ändrar (oberoende)", ""], ["Jag mäter (beroende)", ""], ["Jag håller lika (kontrollerade)", ""]], "tbl num") +
 '<h3>Resultat</h3>' + table(["Form", "Försök 1 (s)", "Försök 2 (s)", "Försök 3 (s)", "Medelvärde (s)"], [["Sockerbit", "", "", "", ""], ["Strösocker", "", "", "", ""]], "tbl num") +
 '<h3>Frågor</h3><ol class="steps g"><li>Vilket löstes fortast? Stämde din hypotes?</li></ol>' + lines(2) +
 '<ol class="steps g"><li>Vilka felkällor kan ha påverkat resultatet?</li></ol>' + lines(2) +
 '<ol class="steps g"><li>Förklara resultatet med en modell: hur kan formen på sockret påverka?</li></ol>' + lines(3) +
 '<ol class="steps g"><li>Hur skulle du förbättra försöket nästa gång?</li></ol>' + lines(2) + '</section>')
RUTOR = []

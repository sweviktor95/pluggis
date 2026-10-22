# -*- coding: utf-8 -*-
"""Kemi område 4 Kemiska föreningar och reaktioner – fördjupning (per moment)."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/kem/fig04k/'
NR = 4
SLUG = "kemi-foreningar"
TAB = "4+"
NAMN = "Kemiska föreningar och reaktioner"
UNDER = "Varför binder atomer som de gör, och vad styr hur reaktioner går?"
INTRO = ("Hur kan man veta vilken formel en jonförening har, och varför är vatten polärt men koldioxid inte? Varför rostar järn, och hur kan en bit zink skydda det? "
         "I den här fördjupningen går du djupare in i kemiska formler och namn, i metallbindning och skillnaden mellan bindningstyper, i elektronegativitet och polära bindningar, i förbränning och brandsäkerhet, i rost och korrosionsskydd och i energi, aktiveringsenergi och katalysatorer. "
         "Namn och mätvärden i uppgifterna är påhittade exempel.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Förklara egenskaper hos ämnen med bindningstyp och elektronegativitet.", "Skriva och balansera reaktionsformler för vardagliga reaktioner och resonera om energi och hastighet.",
       "Värdera metoder och påståenden, till exempel för brandsäkerhet och rostskydd, och hur säkra slutsatserna är."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 4. Fördjupningen bygger på begreppen kovalent bindning, jon, jonbindning, molekylformel, reaktionsformel, balansera, reaktionshastighet, katalysator, exoterm och endoterm."
D = {"4.1": "Molekyler och joner", "4.2": "Kemiska reaktioner"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F4.1.1", "Kemiska formler och namn", "4.1",
 "<p>Hur vet man att natriumklorid är NaCl men magnesiumklorid är MgCl₂? Svaret är att en jonförening alltid är neutral som helhet.</p>"
 + fig(FIG+"f_formler.png", "<b>Bild F4.1</b> Formeln för en jonförening följer av jonernas laddning: den sammanlagda laddningen ska bli noll (schematiskt).", "86%")
 + row("<p>Ämnen i grupp 1 har en valenselektron och bildar joner med laddningen +1, ämnen i grupp 2 har två och bildar joner med laddningen +2. Syre (grupp 16) tar upp två elektroner och blir O²⁻, och klor (grupp 17) tar upp en och blir Cl⁻. Jonformeln hittar du genom att få laddningarna att ta ut varandra. Natrium (+1) och klor (−1) går ihop 1:1, så NaCl. Magnesium (+2) behöver två kloridjoner, så MgCl₂. Två natriumjoner behövs för en oxidjon, så Na₂O.</p>"
       "<p>Namnet bygger på jonerna: metallens namn först och icke-metallen med ändelsen <i>-id</i>: natriumklorid, magnesiumoxid. För molekylföreningar anger man ofta antalet atomer med förled som di-: koldioxid (CO₂) men kolmonoxid (CO). Många vardagsämnen har dock egna namn, som vatten och metan.</p>",
       [begrepp([("Jonformel", "Formel som visar förhållandet mellan jonerna."), ("Laddningsbalans", "Positiv och negativ laddning tar ut varandra."), ("Ändelsen -id", "Visar att icke-metallen är en anjon, till exempel klorid.")]),
        box("tank", "Tänk efter", "<p>Aluminium (grupp 13) bildar Al³⁺ och syre bildar O²⁻. Hur många av varje jon behövs för att laddningen ska bli noll? Skriv formeln.</p>")])
 + "<h3>Hur användbar är regeln?</h3>"
 + "<p>Regeln med gruppnummer fungerar bra för de lätta grundämnena i grupp 1, 2 och 13 samt 16 och 17. Många ämnen längre ned i periodiska systemet, till exempel järn, kan bilda joner med olika laddning. Då måste laddningen anges. Det är ett exempel på en förenklad modell som är användbar men inte gäller överallt.</p>")

add("F4.1.2", "Bindningar fördjupat", "4.1",
 "<p>I grundtexten mötte du kovalent bindning och jonbindning. Det finns en tredje huvudsort, <strong class='green'>metallbindning</strong>, som förklarar varför metaller leder ström och går att forma.</p>"
 + fig(FIG+"f_metall.png", "<b>Bild F4.2</b> Metallbindning (schematiskt): positiva metalljoner hålls ihop av ett hav av fria elektroner som rör sig mellan dem.", "76%")
 + row("<p>I en metall avger atomerna sina yttre elektroner, som inte sitter fast vid någon särskild atom. De positiva metalljonerna hålls ihop av attraktionen till elektronerna som rör sig fritt mellan dem. Eftersom elektronerna är fria leder metaller el och värme. Och eftersom jonerna kan glida förbi varandra utan att bindningen bryts går metaller att böja och hamra.</p>"
       "<p>Jonföreningar är i stället hårda men spröda. Om ett lager joner förskjuts ett steg hamnar joner med lika laddning intill varandra och stöter bort varandra, så kristallen spricker.</p>",
       [table(["", "Kovalent", "Jon", "Metall"], [["Partiklar", "Atomer som delar", "Joner", "Joner + fria e⁻"], ["Leder fast", "Nej", "Nej", "Ja"], ["Formbar", "–", "Spröd", "Ja"]], "tbl")])
 + "<h3>Gränserna är glidande</h3>"
 + "<p>Bindningstyperna är modeller. Många riktiga bindningar ligger mellan ytterligheterna: elektronerna delas ibland ojämnt (polär bindning), och i vissa jonföreningar är bindningen delvis kovalent. Modellerna är användbara för att förutsäga egenskaper, men man måste känna till deras gränser.</p>")

add("F4.1.3", "Elektronegativitet", "4.1",
 "<p>Delar atomerna elektronerna lika? Svaret beror på hur starkt de drar i elektronerna.</p>"
 + fig(FIG+"f_polar.png", "<b>Bild F4.3</b> Vatten är polärt (bindningarna dras mot syre, de tar inte ut varandra) och koldioxid är opolärt (bindningarna tar ut varandra).", "92%")
 + row("<p><strong class='green'>Elektronegativitet</strong> är en atoms förmåga att dra till sig elektronerna i en bindning. Linus Pauling gjorde den första skalan. Syre har värdet 3,5, klor 3,0, kol 2,5 och väte 2,1. Skillnaden mellan atomernas värden säger vilken sorts bindning det är: under ungefär 0,5 är bindningen opolär, mellan ungefär 0,5 och 2,0 polär kovalent, och över ungefär 2,0 liknar den en jonbindning. Gränserna är något godtyckliga.</p>"
       "<p>I en polär bindning delas elektronerna ojämnt. Den mer elektronegativa atomen får en liten negativ laddning (δ−) och den andra en liten positiv (δ+). O–H-bindningen har skillnaden 1,4 och är polär, C–H-bindningen har 0,4 och är opolär.</p>",
       [begrepp([("Elektronegativitet", "Hur starkt en atom drar i elektronerna i en bindning."), ("Polär bindning", "Elektronerna delas ojämnt."), ("Opolär bindning", "Elektronerna delas ungefär lika.")]),
        box("tank", "Tänk efter", "<p>Beräkna skillnaden i elektronegativitet för H–Cl (H 2,1, Cl 3,0). Är bindningen polär eller opolär? Vilken atom får δ−?</p>")])
 + "<h3>Polära molekyler</h3>"
 + "<p>Om en molekyl har polära bindningar som inte tar ut varandra är hela molekylen polär. Vatten är vinklat, så bindningarna tar inte ut varandra och molekylen får en positiv och en negativ sida. Koldioxid är rak, och de två bindningarna drar åt motsatta håll, så molekylen som helhet är opolär. Polära molekyler har oftast högre smält- och kokpunkter och löser sig bättre i vatten än opolära.</p>")

add("F4.2.1", "Förbränning och brandsäkerhet", "4.2",
 "<p>Förbränning är en av de vanligaste kemiska reaktionerna i vardagen: ljus, brasor, gasspisar och motorer. Här tittar vi på reaktionsformlerna och på hur man släcker bränder.</p>"
 + fig(FIG+"f_brand.png", "<b>Bild F4.4</b> Brandtriangeln: en brand behöver bränsle, syre och värme. Tar man bort en av dem slocknar branden.", "70%")
 + row("<p>Vid fullständig förbränning av ett kolväte bildas koldioxid och vatten och energi avges. Metan: CH₄ + 2 O₂ → CO₂ + 2 H₂O. Etanol: C₂H₅OH + 3 O₂ → 2 CO₂ + 3 H₂O. Kontrollera själv: på båda sidor finns 2 C, 6 H och 7 O i etanolreaktionen. Vid brist på syre blir förbränningen ofullständig och det kan bildas kolmonoxid och sot. Kolmonoxid är giftig och luktfri, därför är det viktigt med god ventilation vid eldning.</p>"
       "<p>Man släcker en brand genom att ta bort något av det som behövs. Vatten kyler, och tar alltså bort värme. En brandfilt eller ett lock täcker över och tar bort syre. Vid en fettbrand ska man aldrig använda vatten, eftersom det kan få det heta fettet att stänka kraftigt. Man kan också ta bort bränsle, till exempel genom att stänga av gasen.</p>",
       [begrepp([("Fullständig förbränning", "Ger koldioxid och vatten."), ("Ofullständig förbränning", "Ger bland annat kolmonoxid och sot."), ("Brandtriangeln", "Bränsle, syre och värme.")]),
        box("tank", "Tänk efter", "<p>Varför slocknar ett stearinljus under ett upp-och-nedvänt glas? Använd brandtriangeln och förklara varför det slocknar efter en stund.</p>")])
 + "<h3>Hur användbar är brandtriangeln?</h3>"
 + "<p>Brandtriangeln är en förenklad modell som ger en bra tumregel för att släcka bränder. Verkligheten är mer komplicerad: olika material och bränder kräver olika släckmedel, och därför ska man följa lokala råd och släckutrustningens märkning.</p>")

add("F4.2.2", "Rost och korrosionsskydd", "4.2",
 "<p>Varje år rostar mycket järn och stål. Hur kan man skydda det?</p>"
 + fig(FIG+"f_rost.png", "<b>Bild F4.5</b> Rost och tre sätt att skydda järn: skikt av färg eller zink och en offeranod (schematiskt).", "92%")
 + row("<p>Rost bildas när järn reagerar med syre i närvaro av vatten: järn + syre + vatten → rost (järnoxid, förenklat 4 Fe + 3 O₂ → 2 Fe₂O₃). Både syre och vatten behövs, så nyckeln till att skydda järn är att hålla syre och vatten borta. Rosten flagnar, vilket gör att järnet under fortsätter rosta.</p>"
       "<p>Skydden bygger på olika principer. <b>Färg och olja</b> är en barriär men måste täcka hela ytan och underhållas. <b>Galvanisering</b> är ett skikt av zink: zinken är mer reaktiv än järn och rostar först, så den skyddar även om skiktet repas. En <b>offeranod</b> av magnesium eller zink som kopplas till järn används på fartyg och rörledningar, och metallen offrar sig. En <b>legering</b> som rostfritt stål innehåller krom, som bildar ett tunt oxidskikt som skyddar.</p>",
       [begrepp([("Korrosion", "Att en metall bryts ned av reaktion med omgivningen."), ("Galvanisering", "Skikt av zink på järn."), ("Offeranod", "Mer reaktiv metall som rostar i stället för järnet.")]),
        box("tank", "Tänk efter", "<p>Varför är det olämpligt att skydda en stålbåt med en bit koppar i stället för zink? Ledtråd: vilken metall är mest reaktiv?</p>")])
 + "<h3>Vilket skydd är bäst?</h3>"
 + "<p>Det beror på situationen. Färg är billigt men kräver underhåll, zink skyddar även vid repor, offeranod passar för föremål som sitter i vatten eller jord, och rostfritt stål är dyrare men håller länge. Ett bra svar väger kostnad, hållbarhet och miljö.</p>")

add("F4.2.3", "Energi i kemiska reaktioner", "4.2",
 "<p>Varför brinner inte en trädbit av sig själv, trots att den kan reagera med syre och avge energi? Svaret har med aktiveringsenergi att göra.</p>"
 + fig(FIG+"f_aktivering.png", "<b>Bild F4.6</b> Energidiagram för en exoterm reaktion (schematiskt): reaktionen behöver en energitopp, aktiveringsenergin, och en katalysator sänker toppen.", "88%")
 + row("<p>För att en reaktion ska starta måste partiklarna krocka med tillräcklig energi. Den minsta energi som behövs kallas <strong class='green'>aktiveringsenergi</strong>. Därför behöver till exempel en tändsticka gnuggas eller ett bål tändas, även om reaktionen sedan avger mer energi än den kostade. En <strong class='green'>katalysator</strong> ger reaktionen en annan väg med lägre aktiveringsenergi, så att fler krockar räcker. Katalysatorn förbrukas inte.</p>"
       "<p>Energin i en reaktion kommer av att bindningar bryts (kräver energi) och nya bildas (avger energi). Är den energi som avges större än den som krävdes är reaktionen exoterm, annars endoterm. Hur mycket energi som totalt avges ändras inte av en katalysator, bara hur snabbt reaktionen går.</p>",
       [begrepp([("Aktiveringsenergi", "Energi som krävs för att en reaktion ska starta."), ("Energidiagram", "Visar energin hos ämnena under en reaktion.")]),
        box("tank", "Tänk efter", "<p>Rita ett energidiagram för en endoterm reaktion med och utan katalysator. Var hamnar utgångsämnena och produkterna, och vad förändras med katalysatorn?</p>")])
 + "<h3>Vad är en modell värd här?</h3>"
 + "<p>Energidiagram och krockmodellen ger en enkel bild av varför reaktioner går och hur katalysatorer verkar. Verkligheten är mer komplicerad, men modellen räcker för att förutsäga hur temperatur och katalysator påverkar hastigheten.</p>")

UPG = [
 ("Magnesium står i grupp 2 och klor i grupp 17. a) Förklara vilka joner de bildar och varför. b) Förklara varför formeln för magnesiumklorid är MgCl₂. c) Värdera regeln att gruppnumret bestämmer jonens laddning: när fungerar den och när inte?", 3),
 ("En elev säger: ”Metaller leder ström eftersom de är jonföreningar.” a) Förklara hur metaller leder ström. b) Bedöm påståendet. c) Förklara varför en jonkristall är spröd medan en metall går att böja.", 3),
 ("Kloratomen drar hårdare i elektronerna än väteatomen (H 2,1, Cl 3,0). a) Beräkna skillnaden och avgör vilken sorts bindning H–Cl är. b) Förklara vad δ+ och δ− betyder i molekylen. c) Förklara varför CO₂ är opolär fast C=O-bindningarna är polära.", 3),
 ("Det börjar brinna i en stekpanna med olja. a) Förklara med brandtriangeln hur du ska släcka och vad du inte ska göra. b) Skriv och balansera förbränning av etanol (C₂H₅OH + O₂ → CO₂ + H₂O). c) Förklara varför det är farligt att elda i ett rum med dålig ventilation.", 3),
 ("En segelbåt har skrov av stål. a) Förklara hur stål rostar. b) Jämför tre sätt att skydda skrovet (färg, zink, offeranod) och värdera dem. c) Förklara varför en offeranod av zink skyddar men en av koppar inte gör det.", 3),
 ("En fabrik ska göra en reaktion snabbare. a) Förklara hur högre temperatur, större ytarea och en katalysator var för sig ökar hastigheten. b) Rita ett energidiagram för en exoterm reaktion och markera aktiveringsenergin med och utan katalysator. c) En kollega säger att katalysatorn gör att reaktionen avger mer energi. Värdera påståendet.", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) Magnesium har 2 valenselektroner och avger dem: Mg²⁺. Klor har 7 och tar upp en: Cl⁻. Båda får fullt yttersta skal. b) Laddningen måste bli noll: Mg²⁺ behöver två Cl⁻, så MgCl₂. c) Regeln fungerar bra för grupp 1, 2, 13 och för 16 och 17. Den fungerar sämre för övergångsmetaller som järn, som kan bilda joner med olika laddning. Det är en förenklad modell.",
 "a) Metaller leder ström eftersom de har fria elektroner som kan röra sig mellan metalljonerna. b) Påståendet är fel: metaller är inte jonföreningar. De består av positiva joner i ett hav av fria elektroner (metallbindning). Jonföreningar leder bara löst eller smält. c) I en jonkristall hamnar likladdade joner intill varandra om ett lager förskjuts, så de stöter bort varandra och kristallen spricker. I en metall kan jonerna glida förbi varandra utan att bindningen bryts.",
 "a) Skillnaden är 3,0 − 2,1 = 0,9, vilket ger en polär kovalent bindning. b) δ− betyder en liten negativ laddning (på Cl, som drar hårdare), δ+ en liten positiv (på H). c) CO₂ är rak. De två polära bindningarna drar åt motsatta håll och tar ut varandra, så molekylen som helhet är opolär.",
 "a) Ta bort syre genom att lägga ett lock eller en brandfilt över, och stäng av värmen. Använd aldrig vatten, eftersom det kan få fettet att stänka kraftigt. b) C₂H₅OH + 3 O₂ → 2 CO₂ + 3 H₂O. På båda sidor: 2 C, 6 H, 7 O. c) Vid brist på syre blir förbränningen ofullständig och kolmonoxid bildas. Det är giftigt och luktfritt.",
 "a) Stål (järn) reagerar med syre och vatten och bildar rost (järnoxid). b) Färg: billigt men måste underhållas och släpper in vatten om det repas. Zink (galvanisering): skyddar även vid repor eftersom zink är mer reaktiv. Offeranod: bra för föremål som sitter i vatten, kräver byte. Ett välutvecklat svar väger kostnad, hållbarhet och miljö. c) Zink är mer reaktiv än järn och rostar i stället. Koppar är mindre reaktiv än järn och skulle få järnet att rosta snabbare.",
 "a) Högre temperatur: partiklarna rör sig snabbare och krockar oftare och hårdare, så fler når aktiveringsenergin. Större ytarea: fler partiklar kan krocka. Katalysator: en väg med lägre aktiveringsenergi. b) Ett diagram med utgångsämnen högt och produkter lågt, en energitopp över utgångsämnena, och en lägre topp med katalysator. c) Påståendet är fel. En katalysator ändrar bara hastigheten, inte hur mycket energi som totalt avges.",
]
RUTOR = [("Tänk efter (Kemiska formler och namn):", "Al³⁺ och O²⁻: två Al ger +6 och tre O ger −6, så Al₂O₃."),
         ("Tänk efter (Bindningar fördjupat):", "Ja, men inte exakt. Det är en modell: skillnaden mellan bindningstyperna är glidande, och de flesta bindningar ligger mellan ytterligheterna."),
         ("Tänk efter (Elektronegativitet):", "3,0 − 2,1 = 0,9. Bindningen är polär kovalent, och Cl får δ−."),
         ("Tänk efter (Förbränning och brandsäkerhet):", "Ljuset behöver syre. Glaset stänger in luften, och när syret förbrukats slocknar lågan: ett av hörnen i brandtriangeln saknas."),
         ("Tänk efter (Rost och korrosionsskydd):", "Koppar är mindre reaktiv än järn, så den skyddar inte. Zink är mer reaktiv och rostar först."),
         ("Tänk efter (Energi i kemiska reaktioner):", "Utgångsämnena ligger lågt och produkterna högt. Katalysatorn sänker bara energitoppen, den ändrar inte nivåerna.")]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar kemiska formler och namn, metallbindning och bindningstyper, elektronegativitet och polära bindningar, förbränning och brandsäkerhet, rost och korrosionsskydd samt aktiveringsenergi, och tränar det resonemang som krävs på högsta nivå.",
      SVAR, RUTOR,
      "Källstatus: metallbindning, jonföreningars sprödhet, ledningsförmåga, elektronegativitetsvärdena för O, Cl, C och H, gränserna för polär och opolär bindning, polaritet hos vatten och koldioxid, rostens villkor och skyddsmetoderna (galvanisering, offeranod, legering), aktiveringsenergi och katalysatorer är kontrollerade mot öppna källor (se källförteckningen). Allmän läroboksfakta, inte källkontrollerad i detta arbete: jonladdningar utifrån gruppnummer, namnregler, förbränning med etanol och dess balansering, ofullständig förbränning, att kolmonoxid är giftigt, släckråd (brandfilt, aldrig vatten på fettbrand) och rostens exakta formel. Alla mätvärden i uppgifterna är påhittade.")

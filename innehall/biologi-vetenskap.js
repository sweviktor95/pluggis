// Biologi som vetenskap – sajtsidor byggda utifrån Kapitel 1 (häftet, vanlig version).
// Begrepp, definitioner och siffror följer häftet, med de rättelser som faktakollen gav.
// Bilderna är utklippta ur häftet.

var innehall = window.innehall || {};

var RUTA = function(typ, rubrik, text) {
  return '<div class="ruta ruta-' + typ + '"><span class="ruta-rubrik">' + rubrik + '</span>' + text + '</div>';
};

// ---------- 1.1 + 1.3: Vad är biologi? ----------
innehall["biologi-vetenskap-vad-ar-biologi"] = {
  intro: "Hur vet forskare att fjällräven är hotad, att bakterier kan orsaka sjukdomar eller att växter behöver ljus? Ingen har bara bestämt det. Kunskapen kommer från människor som har varit nyfikna, ställt frågor och noggrant undersökt naturen.",
  sektioner: [
    {
      ikon: "🌱",
      titel: "Vad är biologi?",
      text: [
        "Biologi betyder ”läran om livet”. Ordet kommer från grekiskans <em>bios</em> (liv) och <em>logos</em> (lära). Biologi handlar om allt som lever: bakterier, svampar, växter, djur och människor. Biologer undersöker hur <strong>organismer</strong> är uppbyggda, hur de fungerar, hur de samspelar med varandra och med sin miljö, och hur livet har utvecklats.",
        "Biologi är en av <strong>naturvetenskaperna</strong>, tillsammans med bland annat kemi och fysik. Gemensamt för dem är att de försöker förklara naturen med hjälp av <strong>systematiska</strong> undersökningar, alltså undersökningar som görs noggrant och planerat, så att andra kan kontrollera och upprepa dem.",
        RUTA("fakta", "Gränsfall: virus", "Virus har arvsmassa, men de kan inte föröka sig utan en värdcell. Därför räknar många forskare dem inte som levande organismer. Mikrobiologer studerar dem ändå.")
      ],
      kontrollfraga: "Vad menas med att en undersökning är systematisk?",
      kontrollsvar: "Att den görs noggrant och planerat, så att andra kan kontrollera och upprepa den."
    },
    {
      ikon: "👩‍🔬",
      titel: "Biologer arbetar på många sätt",
      text: [
        "Livet är så stort att ingen kan vara expert på allt. Därför specialiserar sig biologer på olika områden. Vissa arbetar ute i naturen, andra i laboratorier, på sjukhus eller vid en dator där de analyserar stora mängder data.",
        "<strong>Ekolog:</strong> undersöker hur arter samspelar med varandra och med miljön.<br><strong>Marinbiolog:</strong> studerar livet i havet, från plankton till fiskar och sälar.<br><strong>Mikrobiolog:</strong> forskar om bakterier och andra mikroorganismer (och om virus).<br><strong>Genetiker:</strong> undersöker DNA och hur egenskaper ärvs.<br><strong>Botaniker:</strong> expert på växter.<br><strong>Zoolog:</strong> studerar djur, deras kroppar och levnadssätt.<br><strong>Etolog:</strong> undersöker djurs beteenden, till exempel hur bin visar varandra var maten finns.<br><strong>Medicinsk forskare:</strong> undersöker människokroppen, sjukdomar och nya läkemedel.<br><strong>Naturvårdsbiolog:</strong> arbetar för att skydda hotade arter och värdefull natur."
      ],
      kontrollfraga: "Välj två av yrkena. Ge ett exempel på en fråga som var och en skulle kunna undersöka.",
      kontrollsvar: "Till exempel: en ekolog kan undersöka varför det finns färre humlor på en äng än för tio år sedan. En genetiker kan undersöka vilka gener som gör att en växt tål torka."
    },
    {
      ikon: "🔭",
      titel: "Upptäckter som ändrade biologin",
      text: [
        "Biologisk kunskap har vuxit fram under lång tid. Nya verktyg och nya undersökningar har gång på gång ändrat hur vi förstår livet. Ibland har gamla förklaringar fått ge vika för nya, bättre.",
        "<strong>Mikroskopet öppnade en ny värld.</strong> På 1670-talet slipade holländaren Antonie van Leeuwenhoek egna linser. I en vattendroppe såg han små levande varelser som ingen människa hade sett förut. Mikroskopet gjorde det möjligt att upptäcka celler och mikroorganismer.",
        "<strong>Linné gav arterna namn.</strong> Svensken Carl von Linné skapade ett system för att ordna och namnge arter. Från 1750-talet fick varje art ett namn i två delar, till exempel <em>Bellis perennis</em> för tusensköna. Systemet används fortfarande.",
        "<strong>Darwin förklarade mångfalden.</strong> År 1859 gav Charles Darwin ut en bok om hur arter förändras genom naturligt urval. Han byggde sin teori på mängder av observationer från sina resor och från avel av djur.",
        "<strong>DNA – livets kod.</strong> År 1953 kunde James Watson och Francis Crick beskriva hur DNA-molekylen ser ut. De använde röntgenbilder som Rosalind Franklin och hennes kollegor hade tagit. Det visar att stora upptäckter ofta bygger på många forskares arbete."
      ],
      bild: "bilder/vetenskap-tidslinje.png",
      bildText: "Bild 1.3 Några viktiga steg i biologins historia.",
      kontrollfraga: "Varför var mikroskopet så viktigt för biologin?",
      kontrollsvar: "Med mikroskopet kunde forskare se saker som är för små för ögat, till exempel celler och mikroorganismer. Det öppnade en helt ny värld att undersöka."
    },
    {
      ikon: "🧪",
      titel: "Ett klassiskt experiment: kan liv uppstå ur ingenting?",
      text: [
        "Förr trodde många att små organismer kunde uppstå av sig själva i till exempel buljong som stod framme. Omkring år 1860 testade fransmannen Louis Pasteur den idén. Han kokade buljong i två sorters glaskolvar, så att alla mikroorganismer dog.",
        "Kolv A hade ett rakt rör. Damm och mikroorganismer från luften kunde falla ner i buljongen, och efter några dagar blev den grumlig. Kolv B hade en lång, böjd ”svanhals”. Luft kom in, men dammet fastnade i böjen. Buljongen förblev klar.",
        "Pasteurs slutsats: mikroorganismerna kommer från luften – de uppstår inte ur ingenting."
      ],
      bild: "bilder/vetenskap-svanhals.png",
      bildText: "Bild 1.4 Pasteurs svanhalskolvar.",
      kontrollfraga: "Varför var det viktigt att luft kunde komma in i båda Pasteurs kolvar?",
      kontrollsvar: "Om luften hade stängts ute hade någon kunnat säga att livet behöver luft för att uppstå. När luft kom in i båda kolvarna var det bara dammet som skilde dem åt, så försöket visade att mikroorganismerna kom med dammet."
    }
  ],
  begrepp: [
    { term: "Biologi", forklaring: "Läran om livet och levande organismer." },
    { term: "Organism", forklaring: "En levande varelse, till exempel en bakterie, en svamp, en växt eller ett djur." },
    { term: "Naturvetenskap", forklaring: "Vetenskaper som undersöker naturen, till exempel biologi, kemi och fysik." }
  ],
  exitTicket: [
    { fraga: "Vad betyder ordet biologi?", svar: "”Läran om livet”, från grekiskans bios (liv) och logos (lära)." },
    { fraga: "Ge ett exempel på hur en gammal förklaring har ersatts av en ny.", svar: "Till exempel att man förr trodde att små organismer uppstod av sig själva i buljong. Pasteurs försök visade att de kom från luften." }
  ]
};

// ---------- 1.2, 1.4–1.7 + Undersök: Vetenskaplig metod ----------
innehall["biologi-vetenskap-metod"] = {
  intro: "All forskning börjar med nyfikenhet. Här får du lära dig hur forskare tar fram kunskap, hur du planerar en egen undersökning och hur du redovisar och värderar resultatet.",
  sektioner: [
    {
      ikon: "❓",
      titel: "Hur skaffar vi kunskap?",
      text: [
        "En forskare observerar något, till exempel att det finns färre humlor i ett område än för tio år sedan, och undrar varför. Sedan försöker hon ta reda på svaret med hjälp av en undersökning. Det finns flera sätt att undersöka.",
        "<strong>Fältstudie:</strong> man undersöker naturen där den finns, utan att ändra på något. Ekologer kan till exempel räkna humlor på olika ängar.<br><strong>Experiment:</strong> man ändrar en sak med flit och ser vad som händer, ofta i ett laboratorium. Man kan till exempel testa om humlor föredrar blå eller gula blommor.<br><strong>Modell och simulering:</strong> man gör en förenklad bild av verkligheten, ofta i en dator, för att förutsäga vad som kan hända – till exempel hur humlorna påverkas av ett varmare klimat."
      ],
      kontrollfraga: "Vad är skillnaden mellan en fältstudie och ett experiment?",
      kontrollsvar: "I en fältstudie undersöker man naturen där den finns utan att ändra något. I ett experiment ändrar man något med flit och ser vad som händer."
    },
    {
      ikon: "🔄",
      titel: "Forskning är en cykel",
      text: [
        "Arbetet följer ofta stegen i bilden. Det viktiga är att svaret ska bygga på <strong>belägg</strong>, alltså observationer och mätningar, och inte på vad någon tycker eller tror. Ett resultat leder nästan alltid till nya frågor. Därför är forskning aldrig riktigt ”klar”.",
        "<strong>Andra granskar.</strong> När forskare är klara skriver de en vetenskaplig artikel. Innan den publiceras läser andra experter den och letar efter fel. Det kallas <strong>expertgranskning</strong> (på engelska <em>peer review</em>). Andra forskare kan också upprepa undersökningen. Om de får samma resultat blir kunskapen säkrare.",
        "<strong>Hypotes, teori och fakta.</strong> En <strong>hypotes</strong> är ett möjligt svar på en fråga, som går att pröva. En <strong>teori</strong> är något mycket större: en förklaring som har prövats av många forskare under lång tid och som stämmer med väldigt många observationer. Cellteorin säger till exempel att alla organismer är byggda av celler. Evolutionsteorin är ett annat exempel. När någon säger ”det är bara en teori” i vardagen menar de något helt annat än en forskare gör."
      ],
      bild: "bilder/vetenskap-arbetsgang.png",
      bildText: "Bild 1.2 Den vetenskapliga arbetsgången. I verkligheten hoppar forskare ofta fram och tillbaka mellan stegen.",
      kontrollfraga: "Förklara skillnaden mellan en hypotes och en teori. Varför är det viktigt att andra forskare kan upprepa en undersökning?",
      kontrollsvar: "En hypotes är ett möjligt svar på en fråga som går att pröva. En teori är en väl prövad förklaring som stämmer med många observationer. Om andra forskare kan upprepa en undersökning och få samma resultat blir kunskapen säkrare, och fel kan upptäckas."
    },
    {
      ikon: "📝",
      titel: "Planera en undersökning",
      text: [
        "Klass 7B undrar om krasse behöver ljus för att växa. Så här kan de planera ett experiment som ger ett tillförlitligt svar.",
        "<strong>1. Frågeställning.</strong> En bra frågeställning går att undersöka och besvara med mätningar: Påverkar ljus hur högt krasse växer på en vecka?",
        "<strong>2. Hypotes.</strong> Klassen tror: Krassen i ljus växer högre, eftersom växter behöver ljus för fotosyntesen. En hypotes ska ha en motivering – den är inte bara en gissning.",
        "<strong>3. Variabler – ändra bara en sak.</strong> En <strong>variabel</strong> är något som kan ändras eller mätas i en undersökning. För att testet ska bli rättvist får bara en variabel ändras åt gången. Allt annat måste vara lika – annars vet man inte vad som orsakade resultatet. Ofta jämför man med en kontrollgrupp, där man inte ändrar något.",
        "<strong>Oberoende variabel:</strong> det du själv ändrar med flit. I krassförsöket: ljus eller mörker.<br><strong>Beroende variabel:</strong> det du mäter – det som kanske påverkas. I krassförsöket: krassens höjd i mm.<br><strong>Kontrollerade variabler:</strong> allt annat, som måste vara lika i båda försöken. Här: jord, vatten, temperatur, antal frön och tid.",
        RUTA("tank", "Upprepa!", "Klassen sår krasse i tre lådor av varje sort och mäter tio plantor i varje låda. Ju fler mätningar, desto mindre påverkar slumpen resultatet.")
      ],
      bild: "bilder/vetenskap-krasse.png",
      bildText: "Bild 1.5 Krasse som har vuxit i sju dagar i ljus (A) och i en mörk låda (B). Lådans framsida är bortklippt på bilden.",
      kontrollfraga: "Vad är skillnaden mellan oberoende och beroende variabel? Varför ska bara en variabel ändras åt gången?",
      kontrollsvar: "Den oberoende variabeln är det man själv ändrar, och den beroende är det man mäter. Om flera saker ändras samtidigt vet man inte vilken som orsakade resultatet."
    },
    {
      ikon: "📊",
      titel: "Resultat och slutsatser",
      text: [
        "Under försöket mäter klassen krassen varje dag och skriver in mätvärdena i en tabell. Sedan räknar de ut <strong>medelvärdet</strong> för varje grupp: de lägger ihop alla värden och delar med antalet värden.",
        "Ett diagram gör det lättare att se mönster. När något förändras över tid passar ett linjediagram bra. Tiden sätts på x-axeln och det man mäter på y-axeln. Glöm inte rubriker och enheter på axlarna!",
        "<strong>En överraskning.</strong> Resultatet stämde inte med hypotesen. Krassen i mörker blev högre! Men den var också gul, tunn och vek. Växter i mörker sträcker sig snabbt uppåt, som om de söker ljus. Det kallas etiolering. Fröets näring tar snart slut, och utan ljus kan växten inte göra fotosyntes.",
        "<strong>Värdera resultatet.</strong> En forskare frågar sig alltid: Kan jag lita på resultatet? Mätte vi rätt sak?",
        "<strong>Felkällor</strong> är saker som kan ha påverkat resultatet utan att vi ville det. Kanske fick lådorna olika mycket vatten, eller så var det varmare inne i den mörka lådan.<br><strong>Tillförlitlighet</strong> handlar om hur säkra mätningarna är. Skulle vi få samma resultat om vi gjorde om försöket?<br><strong>Giltighet</strong> handlar om att mäta det du ville veta. Är höjden ett bra mått på om krassen ”växer bra”? Det hade kanske varit bättre att väga krassen eller titta på färgen.",
        "<strong>Slutsats.</strong> Klassens slutsats: Krasse som växer i mörker blir högre men svagare än krasse i ljus. Höjden är inte ett bra mått på hur bra en växt mår. En ny fråga väcks: Hur mycket väger krassen?",
        RUTA("visste", "Bra att veta", "Ett resultat som inte stämmer med hypotesen är inte ett misslyckande. Det är så forskningen går framåt!")
      ],
      bild: "bilder/vetenskap-krasse-diagram.png",
      bildText: "Bild 1.6 Krassens medelhöjd under sju dagar. Dag 7: A (ljus) 38 mm, B (mörker) 58 mm.",
      kontrollfraga: "Skriv ner skillnaden mellan tillförlitlighet och giltighet med egna ord.",
      kontrollsvar: "Tillförlitlighet handlar om hur säkra och upprepbara mätningarna är. Giltighet handlar om att man har mätt det man ville undersöka."
    },
    {
      ikon: "🥽",
      titel: "I laboratoriet",
      text: [
        "I ett laboratorium kan forskare göra experiment under kontrollerade förhållanden. I skolans NO-sal finns mycket av samma utrustning som i ett riktigt labb. Det är viktigt att känna till vad sakerna heter och hur de används. Volym mäts noggrannast med mätcylinder eller pipett – strecken på en bägare visar bara ungefär.",
        "<strong>Säkerhet först</strong><br>1. Lyssna på instruktionerna och läs hela labbinstruktionen innan du börjar.<br>2. Använd skyddsglasögon och förkläde när läraren säger det eller när du ser en varningssymbol. Sätt upp långt hår.<br>3. Ät, drick eller smaka aldrig något i labbet.<br>4. Lukta försiktigt genom att vifta lukten mot dig – aldrig direkt över ett kärl.<br>5. Säg till direkt om något går sönder eller om du skadar dig.<br>6. Diska, städa och tvätta händerna när du är klar.",
        RUTA("fakta", "Faroetiketter", "Kemikalier som kan vara farliga har en varningssymbol på förpackningen: en svart bild i en vit romb med röd kant. Läs alltid etiketten innan du använder något."),
        RUTA("tank", "Tänk efter", "Varför är det viktigt att aldrig äta i labbet, även om man bara använder ofarliga saker just den dagen?"),
        "<strong>Skriva en labbrapport.</strong> När du har gjort en undersökning redovisar du den i en labbrapport. Den ska vara så tydlig att någon annan kan göra om försöket och kontrollera ditt resultat. Den har fem delar:<br><strong>Syfte och frågeställning</strong> – vad vill du ta reda på?<br><strong>Hypotes</strong> – vad tror du och varför?<br><strong>Material och metod</strong> – vad använde du och hur gjorde du?<br><strong>Resultat</strong> – vad hände? Tabeller och diagram.<br><strong>Diskussion och slutsats</strong> – vad betyder resultatet? Felkällor?"
      ],
      bild: "bilder/vetenskap-utrustning.png",
      bildText: "Bild 1.7 Vanlig utrustning i ett biologilabb.",
      kontrollfraga: "Ge två säkerhetsregler för arbete i laboratoriet och förklara varför de är viktiga.",
      kontrollsvar: "Till exempel: ät aldrig i labbet, eftersom kemikalier kan finnas på bord och händer. Säg till direkt om något går sönder, så att ingen skär sig eller blir skadad."
    },
    {
      ikon: "🔬",
      titel: "Mikroskopet",
      text: [
        "De flesta organismer och nästan alla celler är för små för att synas med blotta ögat. Ett ljusmikroskop förstorar upp till ungefär 1 000 gånger. Ljuset går nerifrån, genom preparatet, och sedan genom två linser: objektivet och okularet.",
        "<strong>Räkna ut förstoringen.</strong> Både okularet och objektivet förstorar. På varje lins står hur många gånger den förstorar, till exempel 10× eller 40×. Den totala förstoringen räknar du ut så här: okularets förstoring × objektivets förstoring. Exempel: 10× · 40× = 400 gångers förstoring.",
        "<strong>Så använder du mikroskopet</strong><br>1. Börja alltid med det minsta objektivet.<br>2. Lägg preparatet på objektbordet och fäst det med klämmorna.<br>3. Titta från sidan och vrid med grovinställningen tills objektivet nästan nuddar glaset.<br>4. Titta i okularet och vrid sakta uppåt tills bilden blir skarp.<br>5. Finjustera med fininställningen. Byt sedan till större objektiv om du vill.",
        "<strong>Gör ett preparat av lökhinna</strong><br>1. Droppa en droppe vatten på ett objektglas med pipetten.<br>2. Dra loss den tunna hinnan på insidan av en lökbit med pincetten.<br>3. Lägg hinnan slätt i vattendroppen. Undvik veck.<br>4. Sänk ner täckglaset snett från ena sidan med preparatnålen, så att det inte blir luftbubblor.<br>5. Tillsätt gärna en droppe jodlösning vid kanten. Då syns cellkärnorna tydligare.",
        RUTA("tank", "Utmaning", "Rita det du ser. Skriv vilken förstoring du använde. Hur många celler ser du i synfältet vid 100× och vid 400×? Förklara skillnaden.")
      ],
      bild: "bilder/vetenskap-mikroskop.png",
      bildText: "Bild 1.8 Ljusmikroskopets delar.",
      kontrollfraga: "Ett mikroskop har ett okular som förstorar 10× och ett objektiv som förstorar 40×. Hur mycket förstoras bilden totalt?",
      kontrollsvar: "400 gånger (10 × 40)."
    },
    {
      ikon: "🪲",
      titel: "Undersök: trivs gråsuggor bäst i ljus eller mörker?",
      text: [
        "Nu är det din tur att genomföra en hel undersökning, steg för steg. Gråsuggor finns under stenar, brädor och löv nästan överallt. De är ofarliga och lätta att samla in. Du ska använda allt du har lärt dig om frågeställning, hypotes, variabler och upprepning.",
        RUTA("fakta", "Gråsugga", "Kräftdjur som lever på land. Andas med gälliknande organ och torkar lätt ut."),
        "<strong>Frågeställning:</strong> Väljer gråsuggor ljus eller mörker?<br><strong>Hypotes:</strong> Skriv vad du tror och motivera. Tänk på var du brukar hitta gråsuggor.<br><strong>Material:</strong> låda eller stor petriskål, svart papper eller folie, fuktigt hushållspapper, pensel, 10 gråsuggor, klocka.",
        "<strong>Gör så här</strong><br>1. Lägg fuktigt papper i hela botten av lådan. Täck över ena halvan med svart papper.<br>2. Flytta gråsuggorna försiktigt med penseln och släpp dem i mitten.<br>3. Räkna hur många som är på varje sida varje minut i 10 minuter. Skriv i en tabell (minut 1–10, antal i mörker, antal i ljus).<br>4. Byt plats på den mörka och den ljusa sidan och gör om försöket.<br>5. Räkna ut medelvärdet och rita ett diagram.<br>6. Släpp tillbaka djuren där du hittade dem.",
        "<strong>Variabler.</strong> Oberoende: ljus eller mörker. Beroende: antal gråsuggor på varje sida. Kontrollerade: samma fuktighet och temperatur, samma djur, samma tid.",
        RUTA("tank", "Utvärdera", "Stämde hypotesen? Varför byter man plats på sidorna i steg 4? Vad kan gråsuggornas val ha för betydelse för deras överlevnad i naturen?")
      ]
    }
  ],
  begrepp: [
    { term: "Belägg", forklaring: "Observationer och mätningar som stöder en slutsats." },
    { term: "Hypotes", forklaring: "Ett möjligt, prövbart svar på en fråga." },
    { term: "Teori", forklaring: "En väl prövad förklaring som stöds av många belägg." },
    { term: "Experiment", forklaring: "Undersökning där man ändrar något med flit och ser vad som händer." },
    { term: "Fältstudie", forklaring: "Undersökning av naturen där den finns." },
    { term: "Frågeställning", forklaring: "Den fråga en undersökning ska besvara." },
    { term: "Oberoende variabel", forklaring: "Det man själv ändrar i en undersökning." },
    { term: "Beroende variabel", forklaring: "Det man mäter i en undersökning." },
    { term: "Kontrollerade variabler", forklaring: "Det som hålls lika för att testet ska bli rättvist." },
    { term: "Medelvärde", forklaring: "Summan av alla värden delat med antalet värden." },
    { term: "Felkälla", forklaring: "Något som kan ha påverkat resultatet utan att man ville det." },
    { term: "Tillförlitlighet", forklaring: "Hur säkra och upprepbara mätningarna är." },
    { term: "Giltighet", forklaring: "Om man har mätt det man ville undersöka." },
    { term: "Expertgranskning", forklaring: "När andra experter kontrollerar forskning innan den publiceras (på engelska peer review)." }
  ],
  exitTicket: [
    { fraga: "Elin undersöker om temperaturen påverkar hur mycket gas jäst bildar. Hon mäter mängden gas efter 20 minuter. Vilken är den beroende variabeln?", svar: "Mängden gas." },
    { fraga: "Förklara varför en forskare bör upprepa ett försök flera gånger.", svar: "För att minska slumpens betydelse och göra resultatet säkrare. Ju fler mätningar, desto mindre påverkar enstaka fel resultatet." },
    { fraga: "En grupp mätte ballongens omkrets vid tre försök per temperatur: 25 °C gav 22, 24 och 23 cm. Vad är medelvärdet?", svar: "23 cm ((22 + 24 + 23) ÷ 3)." }
  ]
};

// ---------- 1.8–1.9: Vetenskap och källkritik ----------
innehall["biologi-vetenskap-hur-utvecklas-kunskap"] = {
  intro: "Ibland låter något vetenskapligt fast det inte är det. Varje dag möter du påståenden om hälsa, mat, djur och miljö. Här lär du dig skilja vetenskap från pseudovetenskap och granska information.",
  sektioner: [
    {
      ikon: "⚖️",
      titel: "Vetenskap eller pseudovetenskap?",
      text: [
        "Ibland låter något vetenskapligt fast det inte är det. Det kallas <strong>pseudovetenskap</strong> – ”pseudo” betyder falsk. Pseudovetenskap använder gärna ord som ”forskare”, ”naturligt” eller ”kliniskt bevisat”, men påståendena har inte prövats ordentligt eller har prövats och visat sig vara fel.",
        "<strong>Vetenskap:</strong> påståenden går att pröva och kan visa sig vara fel. Bygger på systematiska undersökningar med många deltagare. Granskas av andra experter innan det publiceras. Ändrar sig när nya belägg kommer fram. Redovisar osäkerheter och felkällor.<br><strong>Pseudovetenskap:</strong> påståenden är vaga eller går inte att pröva. Bygger på enstaka berättelser: ”Det funkade för mig!” Granskas inte, eller bara av den som säljer något. Håller fast vid idén, vad undersökningarna än visar. Lovar säkra och enkla resultat."
      ],
      kontrollfraga: "Ge två kännetecken på pseudovetenskap.",
      kontrollsvar: "Till exempel: påståendena är vaga eller går inte att pröva, de bygger på enstaka berättelser, de granskas inte av oberoende experter, eller de lovar säkra och enkla resultat."
    },
    {
      ikon: "💊",
      titel: "Homeopati och placebo",
      text: [
        "<strong>Exempel: homeopati.</strong> Inom homeopati späds ett ämne ut i vatten så många gånger att det ofta inte finns en enda molekyl av ämnet kvar. Stora sammanställningar av forskningen visar att homeopatiska medel inte fungerar bättre än placebo, alltså sockerpiller utan verksamt ämne.",
        "<strong>Placeboeffekten.</strong> Om man tror att en behandling hjälper kan man faktiskt må lite bättre – även om pillret är tomt. Därför jämför forskare ofta en ny medicin med placebo. I de bästa studierna vet varken deltagarna eller forskarna vem som fått vad."
      ],
      kontrollfraga: "Vad är placebo, och varför jämför man nya mediciner med placebo?",
      kontrollsvar: "Placebo är en behandling utan verksamt ämne, till exempel ett sockerpiller. Man jämför för att se om medicinen verkligen gör skillnad, eftersom man kan må bättre bara av att tro att man får hjälp."
    },
    {
      ikon: "🧾",
      titel: "Även forskare kan ha fel",
      text: [
        "År 1998 publicerade en brittisk läkare en studie med tolv barn, som påstod att ett vaccin kunde orsaka autism. Andra forskare försökte upprepa resultatet men lyckades inte. Det visade sig att studien var fusk. Den drogs tillbaka 2010 och läkaren förlorade sin legitimation. Stora studier med hundratusentals barn har inte hittat något samband.",
        "Exemplet visar både en svaghet och en styrka. Enskilda forskare kan göra fel. Den här studien klarade till och med expertgranskningen. Men när andra forskare upprepade undersökningen avslöjades felet till slut."
      ]
    },
    {
      ikon: "📈",
      titel: "Samband är inte samma sak som orsak",
      text: [
        "När glassförsäljningen ökar, ökar också antalet drunkningsolyckor. Betyder det att glass gör att man drunknar? Nej! Båda beror på en tredje sak: värmen. När det är varmt äter fler glass, och fler badar. Två saker kan alltså ändras samtidigt utan att den ena orsakar den andra. Det kallas att det finns en <strong>korrelation</strong> men inget orsakssamband. En korrelation visar ett samband, men det betyder inte att den ena saken orsakar den andra."
      ],
      kontrollfraga: "Förklara med ett eget exempel skillnaden mellan samband och orsak.",
      kontrollsvar: "Till exempel: elever som äter frukost får bättre betyg. Det kan bero på frukosten, men också på att de sover bra och har en stabil vardag. Det är ett samband, men det är inte säkert att frukosten är orsaken."
    },
    {
      ikon: "🕵️",
      titel: "Källkritik: granska information",
      text: [
        "Varje dag möter du påståenden om hälsa, mat, djur och miljö – i sociala medier, reklam, nyheter och samtal. Att granska källor kritiskt betyder att du ställer frågor om informationen innan du tror på den eller sprider den vidare. Fyra frågor brukar kallas de <strong>källkritiska kriterierna</strong>:",
        "<strong>Äkthet:</strong> Är källan den den utger sig för att vara? Är bilden eller citatet äkta?<br><strong>Tid:</strong> När skrevs det? Är informationen fortfarande aktuell?<br><strong>Beroende:</strong> Var kommer uppgifterna ifrån? Har avsändaren själv undersökt, eller bara hört från någon annan?<br><strong>Tendens:</strong> Vill avsändaren något – sälja, övertyga eller påverka? Visas flera sidor av saken?",
        "<strong>Tips för att kontrollera.</strong> Sök efter källan: finns studien? Vilka har gjort den, och hur många deltog? Jämför flera källor, till exempel Folkhälsomyndigheten, Livsmedelsverket eller ett universitet. Var extra misstänksam mot rubriker med många utropstecken, ord som ”chockade” och löften som låter för bra för att vara sanna. Tänk också på dina egna känslor: vi tror lättare på sådant vi redan tycker eller vill ska vara sant.",
        RUTA("tank", "Diskutera", "Ett skogsbolag, en miljöorganisation och en lärobok beskriver skogsbruk. Hur tror du att texterna skiljer sig åt? Vilken har mest tendens?")
      ],
      bild: "bilder/vetenskap-inlagg.png",
      bildText: "Bild 1.11 Ett påhittat inlägg i sociala medier, granskat med de källkritiska kriterierna.",
      kontrollfraga: "Vilka är de fyra källkritiska kriterierna?",
      kontrollsvar: "Äkthet, tid, beroende och tendens."
    }
  ],
  begrepp: [
    { term: "Pseudovetenskap", forklaring: "Något som låter vetenskapligt men inte bygger på prövade belägg." },
    { term: "Placebo", forklaring: "Behandling utan verksamt ämne, till exempel sockerpiller." },
    { term: "Korrelation", forklaring: "När två saker ändras samtidigt, ett samband. Det betyder inte att den ena orsakar den andra." },
    { term: "Källkritiska kriterier", forklaring: "Fyra frågor att ställa till en källa: äkthet, tid, beroende och tendens." }
  ],
  exitTicket: [
    { fraga: "En annons säger: ”Sätt plåstret under foten – på morgonen har det blivit brunt av alla gifter som dragits ut! Vetenskapligt utvecklat.” Ge två skäl att vara skeptisk.", svar: "Till exempel: tendens (säljaren vill sälja), beroende (ingen studie eller källa anges), och att den bygger på en enstaka berättelse. Ett riktigt försök skulle jämföra med ett plåster utan verksamt ämne." },
    { fraga: "En undersökning visar att elever som äter frukost får bättre betyg. Ludvig säger: ”Då ska alla äta frukost, så blir betygen bättre!” Har han rätt?", svar: "Det är inte säkert. Det finns ett samband, men det betyder inte att frukosten är orsaken. Andra förklaringar kan vara sömn, vanor hemma eller hur mycket stöd eleven får." }
  ]
};

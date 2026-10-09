// Cellen – livets byggsten: sajtsidor byggda utifrån Kapitel 2 (häftet, vanlig version).
// Följer häftet, med rättelserna från faktakollen. Bilderna är utklippta ur häftet.

var innehall = window.innehall || {};

var RUTA = function(typ, rubrik, text) {
  return '<div class="ruta ruta-' + typ + '"><span class="ruta-rubrik">' + rubrik + '</span>' + text + '</div>';
};

// ---------- 2.1–2.4, 2.6, 2.7 + Undersök osmos ----------
innehall["biologi-cellen"] = {
  intro: "Du består av ungefär 30 000 miljarder celler. Just nu delar sig några av dem, några skickar signaler till din hjärna och några bär syre runt i kroppen. Ändå började du som en enda cell. En bakterie är också bara en cell – men den klarar sig helt själv.",
  sektioner: [
    {
      ikon: "❔",
      titel: "Vad är liv?",
      text: [
        "Det låter som en enkel fråga, men den är svår att besvara. En eld kan ”växa” och ”äta” ved, men den lever inte. Ett frö kan ligga stilla i flera år, men det lever. Biologer har därför kommit överens om några kännetecken som allt levande har gemensamt.",
        "<strong>Består av celler:</strong> allt levande är uppbyggt av en eller flera celler.<br><strong>Har ämnesomsättning:</strong> tar upp näring och energi och omvandlar dem.<br><strong>Växer och utvecklas:</strong> blir större och förändras under livet.<br><strong>Förökar sig:</strong> kan bilda nya individer av samma slag.<br><strong>Reagerar på omgivningen:</strong> växter vänder sig mot ljuset, du drar bort handen från något varmt.<br><strong>Har arvsmassa:</strong> DNA styr cellen och förs vidare till avkomman.<br><strong>Gör sig av med avfall:</strong> det som inte behövs lämnar cellen eller kroppen.",
        "<strong>Cellteorin.</strong> År 1665 tittade engelsmannen Robert Hooke på en tunn skiva kork i ett tidigt mikroskop. Han såg små rum och kallade dem <em>cells</em>, ”små kammare”. Under 1800-talet visade forskare att alla växter och djur är byggda av celler. Det ledde fram till <strong>cellteorin</strong>, en av biologins viktigaste teorier:<br>1. Alla levande organismer består av en eller flera celler.<br>2. Cellen är livets minsta enhet – det minsta som kan leva.<br>3. Nya celler bildas bara när andra celler delar sig.",
        RUTA("tank", "Diskutera", "Ett virus har arvsmassa och kan föröka sig – men bara inuti en annan cell. Det har ingen egen ämnesomsättning. Lever ett virus? Använd kännetecknen ovan.")
      ],
      kontrollfraga: "Nämn fyra kännetecken för liv. Varför räknas inte en eld som levande, fast den kan växa?",
      kontrollsvar: "Till exempel: består av celler, har ämnesomsättning, växer och utvecklas, förökar sig, reagerar på omgivningen, har arvsmassa, gör sig av med avfall. En eld består inte av celler, har ingen arvsmassa och förökar sig inte som en organism."
    },
    {
      ikon: "🔭",
      titel: "Celler – stora och små",
      text: [
        "De flesta celler är så små att du behöver mikroskop för att se dem. En tusendels millimeter kallas en <strong>mikrometer</strong> (µm). En vanlig cell i din kropp är ungefär 10–30 mikrometer, alltså några hundradels millimeter. Bakterier är ännu mindre. Människans äggcell är en av de största cellerna i kroppen – den syns nästan med blotta ögat.",
        "<strong>Encelliga och flercelliga.</strong> Vissa organismer består av en enda cell. De kallas encelliga. Bakterier, jästsvampar och amöbor är exempel. Den enda cellen måste klara allt själv: ta upp näring, göra sig av med avfall och föröka sig. Växter, djur och de flesta svampar är flercelliga. Deras celler har delat upp arbetet mellan sig. Vissa celler är specialister på att transportera syre, andra på att skicka signaler eller tillverka socker.",
        "<strong>Två huvudtyper av celler.</strong> Alla celler har ett cellmembran och cytoplasma, och de flesta har DNA. De finns i två huvudtyper:<br><strong>Celler utan cellkärna</strong>, där DNA:t ligger fritt i cytoplasman. Hit hör bakterier. De är små och enkla.<br><strong>Celler med cellkärna</strong>, där DNA:t ligger skyddat inne i kärnan. Hit hör djurceller, växtceller och svampceller. De är större och har många olika delar.",
        RUTA("visste", "Visste du?", "Varför är celler så små? Allt cellen behöver måste ta sig in genom cellmembranet. I en liten cell når ämnena snabbt överallt. Om cellen blev för stor skulle mitten inte hinna få syre och näring.")
      ],
      bild: "bilder/cellen-storlek.png",
      bildText: "Bild 2.1 Ungefärlig storlek på några celler och ett virus. Bilderna är inte skalenliga. Varje steg åt höger på skalan är 10 gånger mindre.",
      kontrollfraga: "Vad är den stora skillnaden mellan en bakteriecell och en djurcell?",
      kontrollsvar: "Bakteriecellen har ingen cellkärna – DNA:t ligger fritt i cytoplasman. Djurcellen har en cellkärna där DNA:t ligger skyddat, och många fler organeller."
    },
    {
      ikon: "🏭",
      titel: "Djurcellen",
      text: [
        "En cell kan liknas vid en liten fabrik. Den har en ledning, kraftverk, tillverkning, transporter och en vägg som bestämmer vad som kommer in och ut. De olika delarna inuti cellen kallas <strong>organeller</strong> – ”små organ”.",
        "<strong>Cellmembran</strong> (grind och staket): tunn hinna runt cellen. Släpper in det cellen behöver och släpper ut avfall.<br><strong>Cytoplasma</strong> (fabriksgolvet): geléartad vätska som fyller cellen. Här sker många kemiska reaktioner.<br><strong>Cellkärna</strong> (ledningen): innehåller DNA med cellens ”ritningar”. Styr vad cellen gör. Inne i kärnan syns ibland en <em>kärnkropp</em>, där delar till ribosomerna tillverkas (den behöver du inte kunna).<br><strong>Mitokondrie</strong> (kraftverket): här sker cellandningen: socker och syre ger energi åt cellen.<br><strong>Ribosomer</strong> (arbetarna vid bandet): tillverkar proteiner efter instruktionerna från DNA.<br><strong>Endoplasmatiskt nätverk</strong> (löpande bandet): system av gångar där proteiner tillverkas och transporteras.<br><strong>Golgiapparat</strong> (packavdelningen): sorterar och paketerar ämnen i små blåsor som skickas iväg. Blåsorna kallas ibland vesiklar."
      ],
      bild: "bilder/cellen-djurcell.png",
      bildText: "Bild 2.2 En djurcell i genomskärning, förenklad. Celler i kroppen ser olika ut beroende på vilken uppgift de har.",
      kontrollfraga: "Varför kallas mitokondrien ibland cellens kraftverk? Vad innehåller cellkärnan?",
      kontrollsvar: "I mitokondrien sker cellandningen, där socker och syre ger energi åt cellen. Cellkärnan innehåller DNA, cellens ritningar."
    },
    {
      ikon: "🌿",
      titel: "Växtcellen",
      text: [
        "En växtcell har samma organeller som en djurcell – även mitokondrier. Men den har också tre delar som djurceller saknar: cellvägg, kloroplaster och en stor vakuol.",
        "<strong>Cellvägg:</strong> en stadig vägg av cellulosa utanför cellmembranet. Den ger cellen form och stöd, ungefär som ett skelett. Därför kan en växt stå upprätt utan ben.<br><strong>Kloroplaster:</strong> gröna organeller som innehåller klorofyll. Här sker fotosyntesen, där växten använder solljusets energi för att bygga socker.<br><strong>Vakuol:</strong> en stor blåsa fylld med cellsaft. När den är full trycker den ut mot cellväggen och gör cellen spänd. Får växten för lite vatten blir den slak.",
        "Växtceller kan alltså göra något som inga djurceller kan: tillverka sin egen näring med hjälp av solljus. Hur det går till, och hur alla celler sedan får energi ur näringen, läser du om i nästa avsnitt (Fotosyntes och cellandning).",
        RUTA("visste", "Visste du?", "Cellulosa från växternas cellväggar är det vanligaste ämnet som levande organismer bygger upp på jorden. Papper, bomull och trä består till stor del av cellulosa.")
      ],
      bild: "bilder/cellen-vaxtcell.png",
      bildText: "Bild 2.3 En växtcell, förenklad. Ribosomer, endoplasmatiskt nätverk och golgiapparat finns också men visas inte här.",
      kontrollfraga: "Vilka tre delar har växtceller som djurceller saknar? Varför blir en växt slak om den inte får vatten?",
      kontrollsvar: "Cellvägg, kloroplaster och en stor vakuol. Vakuolen fylls av vatten och trycker ut mot cellväggen så att cellen blir spänd. Utan vatten minskar trycket och växten blir slak."
    },
    {
      ikon: "🦠",
      titel: "Bakterier, svampar och virus",
      text: [
        "Bakterier är de vanligaste organismerna på jorden. De finns i jorden, i vattnet och i din tarm – där de hjälper dig att bryta ner maten. Bara ett fåtal bakterier orsakar sjukdomar.",
        "<strong>Bakterier.</strong> En bakterie är en egen organism, och bara en cell. Den har cellvägg och cellmembran men ingen cellkärna och inga mitokondrier. Förutom sitt stora DNA har många bakterier små DNA-ringar som kallas plasmider. Vissa bakterier simmar med hjälp av en flagell. Under bra förhållanden kan en bakterie dela sig på 20 minuter.",
        "<strong>Svampar.</strong> Svampceller har cellkärna, precis som djur- och växtceller. De har cellvägg, men den är byggd av kitin och inte av cellulosa. Svampar saknar kloroplaster och kan inte göra fotosyntes. Jäst är en encellig svamp som förökar sig genom att knoppa av nya celler.",
        "<strong>Virus – inte en cell.</strong> Ett virus är mycket mindre än en bakterie. Det består bara av arvsmassa i ett skal av protein. Viruset kan inte föröka sig själv. Det tar sig in i en levande cell och tvingar cellen att tillverka nya virus. Antibiotika fungerar därför inte mot virus: antibiotika angriper delar som bakterier har, till exempel cellväggen – och sådana delar saknar virus. Om antibiotika används i onödan kan bakterierna bli <strong>resistenta</strong>. Då slutar medicinen att fungera.",
        "<strong>Jämförelse:</strong><br>Cellmembran: djurcell ✔, växtcell ✔, svampcell ✔, bakterie ✔.<br>Cellkärna: djurcell ✔, växtcell ✔, svampcell ✔, bakterie –.<br>Mitokondrier: djurcell ✔, växtcell ✔, svampcell ✔, bakterie –.<br>Cellvägg: djurcell –, växtcell ✔ (cellulosa), svampcell ✔ (kitin), bakterie ✔.<br>Kloroplaster: bara växtcell ✔.<br>Stor vakuol: växtcell ✔, svampcell ibland, djurcell och bakterie –."
      ],
      bild: "bilder/cellen-bakterie.png",
      bildText: "Bild 2.5 En bakteriecell, förenklad. Bakterien har ingen cellkärna – dess DNA ligger fritt i cytoplasman.",
      kontrollfraga: "Samir har förkylning och vill ha antibiotika. Förklara varför det inte hjälper.",
      kontrollsvar: "Förkylning orsakas av virus. Antibiotika angriper delar som bara bakterier har, till exempel cellväggen, och virus saknar sådana delar. Antibiotika hjälper därför inte mot virus."
    },
    {
      ikon: "✂️",
      titel: "Celler delar sig och specialiseras",
      text: [
        "Varje sekund dör miljontals celler i din kropp – och nya bildas. Nya celler kan bara bildas genom att en cell delar sig. Kroppen behöver celldelning för att <strong>växa</strong> (från en cell till miljarder), <strong>laga skador</strong> (till exempel ett sår) och <strong>ersätta utslitna celler</strong> i hud och tarm.",
        "I cellkärnan finns DNA:t uppdelat i <strong>kromosomer</strong>. Människans kroppsceller har 46 kromosomer, 23 från mamman och 23 från pappan. Vid en vanlig celldelning, <strong>mitos</strong>, får båda de nya cellerna 46 kromosomer. Före delningen kopieras alla kromosomer, så att båda de nya cellerna får exakt samma DNA.",
        "Könsceller – spermier och ägg – bildas genom en annan sorts delning, <strong>reduktionsdelning</strong> (meios). Då halveras antalet kromosomer till 23. När en spermie befruktar ett ägg blir det åter 46 kromosomer i den nya cellen.",
        RUTA("fakta", "Stamceller", "Stamceller är celler som ännu inte har bestämt sig för vad de ska bli. De kan dela sig och bli många olika celltyper. Forskare undersöker hur stamceller kan användas för att laga skadade organ."),
        "<strong>Specialiserade celler.</strong> Nästan alla celler i din kropp har samma DNA. Ändå ser de väldigt olika ut. Det beror på att olika <strong>gener</strong> är ”påslagna” i olika celler. En gen är en del av DNA:t som innehåller instruktionen för en egenskap eller ett protein. När en cell utvecklas till en särskild celltyp kallas det att den <strong>specialiseras</strong>. Formen passar uppgiften: en nervcell är lång för att nå långt, och en röd blodkropp saknar cellkärna (och därmed DNA) för att få plats med mer syre."
      ],
      bild: "bilder/cellen-mitos.png",
      bildText: "Bild 2.7 Vanlig celldelning (mitos). Förenklad bild: bara 3 av cellens 46 kromosomer visas.",
      kontrollfraga: "Vilken nytta har kroppen av att celler delar sig? Ge två exempel.",
      kontrollsvar: "Kroppen kan växa, laga skador (till exempel ett sår) och ersätta utslitna celler i hud och tarm."
    },
    {
      ikon: "🥔",
      titel: "Undersök: vad händer med potatis i saltvatten?",
      text: [
        "Cellmembranet släpper igenom vatten. Vatten rör sig genom membranet mot den sida där det finns mer löst ämne, till exempel salt. Det kallas <strong>osmos</strong>. Ett löst ämne är något som är upplöst i vätskan, som salt i vatten. Saltvatten drar alltså vatten ur potatisen. I den här undersökningen ser du osmos i potatisceller.",
        "<strong>Frågeställning:</strong> Hur påverkas potatisbitars vikt av hur mycket salt det finns i vattnet?<br><strong>Hypotes:</strong> Skriv vad du tror och motivera med det du vet om cellmembranet.<br><strong>Material:</strong> potatis, kniv, skärbräda, 3 bägare, salt, vatten, våg, linjal, hushållspapper.",
        "<strong>Gör så här</strong><br>1. Skär nio lika stora potatisbitar, ungefär 4 cm långa.<br>2. Torka och väg varje bit. Skriv upp vikten.<br>3. Lägg tre bitar i varje bägare: rent vatten, 5 % och 10 % saltlösning.<br>4. Vänta minst 30 minuter, gärna längre.<br>5. Torka av bitarna och väg dem igen. Räkna ut viktförändringen.",
        "<strong>Variabler.</strong> Oberoende: hur mycket salt det finns i vattnet. Beroende: potatisbitarnas vikt. Kontrollerade: bitarnas storlek, samma potatis, samma tid, samma mängd vätska.",
        RUTA("tank", "Utvärdera", "Stämde hypotesen? Känn på bitarna – vilka är slaka och vilka är fasta? Förklara med hjälp av osmos och vakuolen. Vilka felkällor finns?"),
        RUTA("fakta", "Titta också på: vattenpest i mikroskop", "Lägg ett blad av vattenpest i en vattendroppe på ett objektglas och lägg på ett täckglas. Vid 400× ser du cellväggar och massor av gröna kloroplaster. Om du väntar en stund kan du se kloroplasterna röra sig runt i cellen!")
      ],
      bild: "bilder/cellen-osmos.png",
      bildText: "Bild 2.12 Uppställning av försöket.",
      kontrollfraga: "Vad händer med en potatisbit i 10 % saltlösning, och varför?",
      kontrollsvar: "Den blir lättare och slak. Vatten rör sig med osmos ut ur potatisbitens celler mot saltlösningen, där det finns mer löst ämne."
    }
  ],
  begrepp: [
    { term: "Cell", forklaring: "Livets minsta enhet." },
    { term: "Ämnesomsättning", forklaring: "Alla kemiska processer i en organism, till exempel när näring omvandlas till energi." },
    { term: "Organell", forklaring: "En del i cellen med en särskild uppgift." },
    { term: "Protein", forklaring: "Ämne som bygger upp kroppen och styr många processer i cellen." },
    { term: "Cellmembran", forklaring: "Hinna som styr vad som går in i och ut ur cellen." },
    { term: "Cellkärna", forklaring: "Organell som innehåller DNA och styr cellen." },
    { term: "Cellvägg", forklaring: "Stadig vägg utanför cellmembranet hos växter, svampar och bakterier." },
    { term: "Mitokondrie", forklaring: "Organell där cellandningen sker." },
    { term: "Ribosom", forklaring: "Liten organell som tillverkar proteiner." },
    { term: "Vakuol", forklaring: "Blåsa med cellsaft som gör växtcellen spänd." },
    { term: "Bakterie", forklaring: "Encellig organism utan cellkärna." },
    { term: "Virus", forklaring: "Arvsmassa i ett proteinskal. Ingen cell." },
    { term: "Kromosom", forklaring: "Hoprullad DNA-tråd. Människans kroppsceller har 46." },
    { term: "Mitos", forklaring: "Vanlig celldelning som ger två likadana celler." },
    { term: "Gen", forklaring: "En del av DNA:t som innehåller instruktionen för en egenskap eller ett protein." },
    { term: "Osmos", forklaring: "När vatten rör sig genom ett membran mot den sida där det finns mer löst ämne." }
  ],
  exitTicket: [
    { fraga: "Vilken organell finns i växtceller men inte i djurceller? A mitokondrie, B kloroplast, C cellkärna, D ribosom.", svar: "B – kloroplast." },
    { fraga: "Vilket påstående om bakterier stämmer? A De har cellkärna. B De är encelliga och saknar cellkärna. C De är en sorts virus. D De har kloroplaster.", svar: "B – bakterier är encelliga och saknar cellkärna." },
    { fraga: "Para ihop: cellkärna, mitokondrie, kloroplast, cellmembran med A fotosyntes, B bestämmer vad som kommer in, C innehåller DNA och styr cellen, D cellandning.", svar: "Cellkärna – C, mitokondrie – D, kloroplast – A, cellmembran – B." }
  ]
};

// ---------- 2.5: Fotosyntes och cellandning ----------
innehall["biologi-liv-fotosyntes-cellandning"] = {
  intro: "Alla celler behöver energi – för att växa, röra sig, tillverka ämnen och dela sig. Nästan all energi som finns i levande organismer kommer från början från solen. Två processer gör det möjligt: fotosyntesen, som fångar in solens energi, och cellandningen, som frigör energin i cellerna.",
  sektioner: [
    {
      ikon: "☀️",
      titel: "Fotosyntesen",
      text: [
        "Fotosyntesen sker i kloroplasterna, framför allt i växternas blad. Klorofyllet fångar ljusenergi. Växten tar upp koldioxid från luften genom små öppningar i bladen, klyvöppningar, och vatten från marken genom rötterna. Av detta bygger den <strong>glukos</strong>, ett slags socker. Syre bildas och släpps ut.",
        "Glukosen används på olika sätt: som bränsle i cellandningen, som byggmaterial till cellulosa i cellväggarna, och som lager i form av stärkelse, till exempel i potatis.",
        "<strong>Fotosyntes</strong> (i kloroplasterna): koldioxid + vatten → glukos + syre (med hjälp av solljus)."
      ],
      bild: "bilder/cellen-fotosyntes.png",
      bildText: "Bild 2.4 Fotosyntes och cellandning hänger ihop. Det som bildas i den ena processen används i den andra.",
      kontrollfraga: "Vad behöver en växt för att kunna göra fotosyntes, och vad bildas?",
      kontrollsvar: "Växten behöver koldioxid, vatten och ljus. Det bildas glukos (socker) och syre."
    },
    {
      ikon: "🔥",
      titel: "Cellandningen",
      text: [
        "Cellandningen sker i mitokondrierna i nästan alla celler – hos djur, växter och svampar. Bakterier har inga mitokondrier, men många bakterier gör en liknande process i sin cell. Glukos reagerar med syre, och den energi som finns lagrad i glukosen frigörs. Samtidigt bildas koldioxid och vatten.",
        "Energin används till allt cellen gör. En del blir värme – det är därför du blir varm när du springer. Koldioxiden förs med blodet till lungorna och andas ut.",
        "<strong>Cellandning</strong> (i mitokondrierna): glukos + syre → koldioxid + vatten + energi.",
        RUTA("fakta", "Utan syre", "Vissa celler kan få lite energi även utan syre, till exempel jästsvampar och dina muskler vid mycket hård ansträngning. Då sker det genom en annan process som ger mycket mindre energi. Du får läsa mer om det i fördjupningen.")
      ],
      kontrollfraga: "I vilka celler sker cellandning? Var i cellen?",
      kontrollsvar: "I nästan alla celler – hos djur, växter och svampar. Den sker i mitokondrierna."
    },
    {
      ikon: "🔗",
      titel: "Hur hänger de ihop?",
      text: [
        "Det som bildas i den ena processen används i den andra. Fotosyntesen gör glukos och syre av koldioxid och vatten. Cellandningen använder glukos och syre och bildar koldioxid och vatten igen. Så kretsar ämnena runt, medan energin kommer från solen.",
        RUTA("tank", "Vanligt missförstånd", "”Växter andas inte, de gör bara fotosyntes.” Fel! Växter gör cellandning dygnet runt. Fotosyntes sker bara när det är ljust."),
        RUTA("tank", "Prova själv", "Lägg vattenpest i vatten under en lampa. Små bubblor av syre stiger från bladen. Flytta lampan längre bort – vad händer med antalet bubblor?")
      ],
      kontrollfraga: "Förklara varför man kan säga att energin i din smörgås ursprungligen kommer från solen.",
      kontrollsvar: "Växterna (till exempel säden i brödet) fångar solens energi i fotosyntesen och lagrar den i glukos och andra ämnen. När du äter smörgåsen frigörs energin i dina celler genom cellandning."
    }
  ],
  begrepp: [
    { term: "Fotosyntes", forklaring: "Koldioxid och vatten blir glukos och syre med hjälp av solljus. Sker i kloroplasterna." },
    { term: "Cellandning", forklaring: "Glukos och syre ger energi, koldioxid och vatten. Sker i mitokondrierna." },
    { term: "Kloroplast", forklaring: "Grön organell i växtceller där fotosyntesen sker." },
    { term: "Glukos", forklaring: "Ett slags socker som växter bygger i fotosyntesen." }
  ],
  exitTicket: [
    { fraga: "Vilken process tar upp koldioxid och bildar syre, och var sker den?", svar: "Fotosyntesen, i kloroplasterna." },
    { fraga: "Gör växter cellandning på natten?", svar: "Ja. Växter gör cellandning dygnet runt, men fotosyntes bara när det är ljust." }
  ]
};

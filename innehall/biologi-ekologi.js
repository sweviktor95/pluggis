// Ekologi – sajtsidor byggda utifrån Kapitel 4 (häftet, vanlig version).
// Följer häftet, med rättelserna från faktakollen. Bilderna är utklippta ur häftet.
// "Hållbar utveckling" har ännu inget innehåll (ingen motsvarande del i häftet).

var innehall = window.innehall || {};

var RUTA = function(typ, rubrik, text) {
  return '<div class="ruta ruta-' + typ + '"><span class="ruta-rubrik">' + rubrik + '</span>' + text + '</div>';
};

// ---------- 4.1 + 4.8: Ekosystem ----------
innehall["biologi-ekologi-ekosystem"] = {
  intro: "En havsörn dyker ner mot en vik i Bottenviken och fångar en gädda. Gäddan har ätit abborrar, abborrarna har ätit djurplankton och djurplanktonen har ätit små alger som har fångat solljus. Allt levande hänger ihop i ett nät av beroenden. Läran om hur organismer samspelar med varandra och med sin miljö kallas ekologi.",
  sektioner: [
    {
      ikon: "🏡",
      titel: "Vad är ekologi?",
      text: [
        "Ekologi kommer från grekiskans <em>oikos</em>, som betyder hus eller hem. Ekologer undersöker hur organismer lever i sitt ”hem”: vad de äter, vem som äter dem, vilka de konkurrerar med och hur de påverkas av till exempel temperatur, ljus och vatten. Ekologer studerar naturen på olika nivåer.",
        "<strong>Individ:</strong> en skogshare.<br><strong>Population:</strong> alla individer av samma art som lever inom ett visst område, till exempel alla skogsharar i en skog.<br><strong>Samhälle:</strong> alla populationer av olika arter i samma område.<br><strong>Ekosystem:</strong> samhället tillsammans med den livlösa miljön: ljus, vatten, jord, luft och temperatur.<br><strong>Biosfär:</strong> alla ekosystem på jorden tillsammans – allt liv och alla platser där det finns liv.",
        RUTA("tank", "Tänk efter", "Är ett ekosystem alltid stort? Kan en vattenpöl, en murken stubbe eller din tarm vara ett ekosystem?")
      ],
      bild: "bilder/ekologi-nivaer.png",
      bildText: "Bild 4.1 Ekologins nivåer, från en enda individ till allt liv på jorden.",
      kontrollfraga: "Vad är skillnaden mellan en population och ett samhälle?",
      kontrollsvar: "En population är alla individer av samma art i ett område. Ett samhälle är alla populationer av olika arter i samma område."
    },
    {
      ikon: "🌡️",
      titel: "Levande och icke-levande faktorer",
      text: [
        "Allt som påverkar en organism kallas faktorer. Faktorer från andra organismer, som föda, rovdjur, konkurrenter och sjukdomar, kallas <strong>biotiska</strong> (bios = liv). Faktorer från den livlösa miljön, som temperatur, ljus, vatten, näringsämnen och vind, kallas <strong>abiotiska</strong>.",
        "Varje art har en livsmiljö där den kan leva. En abborre behöver sjö- eller havsvatten med tillräckligt med syre. En fjällräv behöver kalla fjäll med lämlar och gamla lyor."
      ],
      kontrollfraga: "Ge två biotiska och två abiotiska faktorer som påverkar en gädda. Varför räknas vattnet och solljuset till ekosystemet?",
      kontrollsvar: "Biotiska: till exempel föda (abborre, mört) och rovdjur (havsörn). Abiotiska: till exempel temperatur och syre i vattnet. Vattnet och solljuset är livlös miljö som organismerna är beroende av, och ekosystemet är samhället tillsammans med den livlösa miljön."
    },
    {
      ikon: "🌍",
      titel: "Lokala och globala ekosystem",
      text: [
        "Ekosystemen ser olika ut beroende på klimat, ljus, vatten och jord. Men de fungerar efter samma principer: producenter fångar solenergi, konsumenter äter, nedbrytare tar hand om det döda och materien går i kretslopp.",
        "<strong>Barrskog i Norrbotten:</strong> kalla vintrar och kort sommar med ljusa nätter. Producenter: tall, gran, björk, bärris, mossor, lavar. Konsumenter: älg, skogshare, tjäder, lodjur, björn. Nedbrytningen är långsam – kallt och surt. Artrikedomen är måttlig.<br><strong>Bottenviken:</strong> kallt bräckt vatten (en blandning av sött och salt) med is på vintern. Producenter: växtplankton, alger, vass. Konsumenter: djurplankton, sik, abborre, gädda, säl, havsörn. Nedbrytningen är långsam i kallt vatten. Artrikedomen är låg, eftersom få arter klarar bräckt vatten.<br><strong>Tropisk regnskog:</strong> varmt och regnigt hela året. Producenter: höga lövträd, lianer (klätterväxter) och epifyter (växter som växer på andra växter). Konsumenter: insekter, apor, fåglar, ormar, jaguar. Nedbrytningen är mycket snabb. Artrikedomen är mycket hög.<br><strong>Savann:</strong> varmt, med regnperiod och torrperiod. Producenter: gräs och spridda träd som akacior. Konsumenter: zebror, gnuer, giraffer, lejon. Nedbrytningen är snabb under regnperioden. Artrikedomen är hög, särskilt bland stora däggdjur.",
        "I barrskogen bryts löv och barr ner långsamt eftersom det är kallt. Därför bildas tjocka lager av förna (döda löv och barr på marken) och torv. I regnskogen går nedbrytningen så fort att näringen nästan direkt tas upp av växterna igen. Jorden i sig är ofta näringsfattig.",
        "Ekosystemen hänger också ihop globalt. Flyttfåglar som häckar i Norrbotten övervintrar i Afrika, och laxen vandrar mellan älvarna och havet. Koldioxid från ett land påverkar klimatet i hela världen."
      ],
      bild: "bilder/ekologi-ekosystem.png",
      bildText: "Bild 4.9 Två ekosystem i Norrbotten och två i andra delar av världen.",
      kontrollfraga: "Varför bryts löv ner långsammare i Norrbotten än i en regnskog?",
      kontrollsvar: "I Norrbotten är det kallt, och nedbrytarna (svampar och bakterier) arbetar långsammare i kyla. I regnskogen är det varmt och fuktigt, så nedbrytningen går mycket snabbt."
    }
  ],
  begrepp: [
    { term: "Population", forklaring: "Alla individer av en art inom ett område." },
    { term: "Samhälle", forklaring: "Alla populationer av olika arter i samma område." },
    { term: "Ekosystem", forklaring: "Organismerna och den livlösa miljön i ett område." },
    { term: "Biosfär", forklaring: "Alla ekosystem på jorden tillsammans." },
    { term: "Biotisk faktor", forklaring: "Påverkan från andra levande organismer." },
    { term: "Abiotisk faktor", forklaring: "Påverkan från den livlösa miljön." },
    { term: "Förna", forklaring: "Döda löv och barr som ligger på marken." }
  ],
  exitTicket: [
    { fraga: "Vilket av dessa är en abiotisk faktor för en fjällräv: lämlar, temperatur, rödräv eller en sjukdom?", svar: "Temperatur. De andra är biotiska faktorer (andra organismer)." },
    { fraga: "Varför har Bottenviken låg artrikedom?", svar: "Vattnet är bräckt (en blandning av sött och salt) och kallt, och få arter klarar det." }
  ]
};

// ---------- 4.2 + 4.3: Näringskedjor och näringsvävar ----------
innehall["biologi-ekologi-naringskedjor-naringsvavar"] = {
  intro: "I kapitel 2 lärde du dig att växter gör fotosyntes och att alla celler behöver energi från cellandning. Nu ska vi se vad det betyder för ett helt ekosystem. Organismerna kan delas in i tre grupper efter hur de får sin energi och näring.",
  sektioner: [
    {
      ikon: "🌱",
      titel: "Producenter, konsumenter och nedbrytare",
      text: [
        "<strong>Producenter:</strong> gröna växter, alger och växtplankton. De bygger sin egen näring med fotosyntes och är grunden i nästan alla näringskedjor.<br><strong>Konsumenter:</strong> djur som äter andra organismer. Växtätare äter producenter, rovdjur äter andra djur och allätare äter både och.<br><strong>Nedbrytare:</strong> svampar och bakterier som bryter ner döda växter och djur, avföring och nedfallna löv. De frigör näringsämnen som växterna kan använda igen.",
        RUTA("visste", "Visste du?", "Detritusätare som daggmaskar, gråsuggor och hoppstjärtar äter döda växtdelar. De hackar sönder materialet så att svampar och bakterier kan bryta ner det snabbare. De räknas som konsumenter, men de hjälper nedbrytarna.")
      ],
      kontrollfraga: "Vad skulle hända i en skog om alla nedbrytare försvann?",
      kontrollsvar: "Döda växter och djur skulle bli liggande och ingen näring skulle frigöras till växterna. Till slut skulle växterna få brist på näring och hela ekosystemet skulle drabbas."
    },
    {
      ikon: "⛓️",
      titel: "Näringskedjor",
      text: [
        "En <strong>näringskedja</strong> visar vem som äter vem. Varje steg i kedjan kallas ett led. Producenten är första ledet. Pilarna ritas från den som blir uppäten till den som äter, alltså åt samma håll som energin går. Den som står först i en näringskedja ovanför marken eller i vattnet är alltid en producent. (I marken kan en kedja börja med dött material.)",
        "Djurplankton äter växtplankton och är därför första ordningens konsument eller växtätare. Abborren äter djurplankton och är andra ordningens konsument. Havsörnen har inga naturliga fiender och kallas <strong>toppkonsument</strong>.",
        "Många djur kan stå på flera nivåer. En björn äter både blåbär och älgkalvar. En människa som äter en sallad är första ordningens konsument, men när hon äter en köttbit är hon andra eller tredje ordningens konsument."
      ],
      bild: "bilder/ekologi-kedja.png",
      bildText: "Bild 4.2 En näringskedja i Bottenviken. Konsumenterna numreras efter hur många steg de står från producenterna. Pilen pekar från den som blir uppäten till den som äter – åt samma håll som energin går.",
      kontrollfraga: "Varför står alltid en producent först i en näringskedja ovanför marken eller i vattnet?",
      kontrollsvar: "Producenterna är de enda som kan bygga sin egen näring med hjälp av solljus. Alla andra organismer måste få sin energi genom att äta."
    },
    {
      ikon: "🕸️",
      titel: "Näringsvävar",
      text: [
        "I verkligheten äter de flesta djur flera olika saker och blir uppätna av flera olika rovdjur. Näringskedjorna korsar varandra och bildar en <strong>näringsväv</strong>. En näringsväv visar bättre hur ett ekosystem verkligen fungerar.",
        "<strong>När en art försvinner.</strong> Om en art försvinner påverkas alla som hänger ihop med den. Om abborrarna fiskas bort får gäddan mindre mat. Samtidigt blir det fler djurplankton och insektslarver, eftersom färre äter dem. Ju fler kopplingar det finns i väven, desto lättare kan ekosystemet klara en förändring.",
        "<strong>Kaskadeffekt.</strong> När en förändring högst upp i en näringskedja sprider sig nedåt genom flera nivåer kallas det en kaskadeffekt.",
        "<strong>Exempel: vargarna i Yellowstone.</strong> I nationalparken Yellowstone i USA utrotades vargarna under 1920-talet. Hjortarna blev då många och betade hårt på unga träd och buskar längs vattendragen. År 1995 släpptes vargar ut igen. Forskare såg att hjortarna betade mindre på vissa platser och att träd och buskar kunde växa upp. Där blev det fler småfåglar och bävrar. Forskarna diskuterar fortfarande hur stor vargarnas betydelse var. Klimatet och jakten kan också ha spelat roll.",
        RUTA("tank", "Tänk efter", "Använd bilden. Vad händer med insektslarverna om knipan försvinner? Vad händer då med vattenväxterna?")
      ],
      bild: "bilder/ekologi-vav.png",
      bildText: "Bild 4.3 En förenklad näringsväv i en sjö eller vik. Pilarna visar åt vilket håll energin går.",
      kontrollfraga: "Om abborrarna fiskas bort, vad händer med gäddan och med djurplanktonen?",
      kontrollsvar: "Gäddan får mindre mat. Det blir fler djurplankton och insektslarver, eftersom färre äter dem."
    }
  ],
  begrepp: [
    { term: "Producent", forklaring: "Organism som bygger sin egen näring med fotosyntes: gröna växter, alger, växtplankton." },
    { term: "Konsument", forklaring: "Djur som äter andra organismer." },
    { term: "Nedbrytare", forklaring: "Svampar och bakterier som bryter ner döda organismer och frigör näring." },
    { term: "Detritusätare", forklaring: "Djur som äter döda växtdelar och hackar sönder dem så att nedbrytarna kan bryta ner dem snabbare." },
    { term: "Näringskedja", forklaring: "Visar vem som äter vem. Pilarna går åt samma håll som energin." },
    { term: "Näringsväv", forklaring: "Flera näringskedjor som hänger ihop." },
    { term: "Toppkonsument", forklaring: "Ett djur högst upp i näringskedjan, utan naturliga fiender." },
    { term: "Kaskadeffekt", forklaring: "En förändring som sprider sig genom flera nivåer i en näringsväv." }
  ],
  exitTicket: [
    { fraga: "Rita (skriv) en näringskedja med fyra led från en skog och peka ut producent och konsumenter.", svar: "Till exempel: blåbärsris (producent) → skogshare (konsument 1) → lodjur (konsument 2). Fyra led kan vara gräs → hare → räv → örn." },
    { fraga: "Åt vilket håll pekar pilen i en näringskedja?", svar: "Från den som blir uppäten till den som äter, alltså åt samma håll som energin går." }
  ]
};

// ---------- 4.4 + 4.5 + Undersök: Energi och materia ----------
innehall["biologi-ekologi-energi-materia"] = {
  intro: "Nästan all energi i ett ekosystem kommer från solen. Energin flödar igenom ekosystemet och försvinner som värme, men materien – alla atomer som organismer är byggda av – försvinner aldrig. Den går i kretslopp.",
  sektioner: [
    {
      ikon: "⚡",
      titel: "Energin flödar genom ekosystemet",
      text: [
        "Producenterna fångar en liten del av solljuset med fotosyntesen och lagrar energin i glukos och andra ämnen. När en växtätare äter växten förs en del av energin vidare. Men det mesta av energin förs inte vidare.",
        "<strong>Varför försvinner energi i varje led?</strong><br>Organismen använder energi för att leva: röra sig, hålla värmen och laga celler. Det mesta blir till slut värme.<br>Allt äts inte upp: rötter, ben, päls och fjädrar blir kvar.<br>Allt som äts tas inte upp i kroppen, utan lämnar den som avföring.",
        "Som en tumregel förs bara omkring 10 procent av energin vidare till nästa nivå. Resten går förlorad som värme eller hamnar hos nedbrytarna. Man brukar rita det som en <strong>energipyramid</strong>.",
        "Energi går alltså inte i kretslopp, den flödar genom ekosystemet: in som solljus och ut som värme. Därför behövs ett ständigt tillskott av solenergi.",
        "<strong>Därför är näringskedjor korta.</strong> Efter fyra eller fem led finns det för lite energi kvar för ytterligare en nivå. Därför finns det många fler harar än lodjur och många fler växtplankton än havsörnar. Toppkonsumenter behöver stora områden för att hitta tillräckligt med mat.",
        "<strong>Mat och hållbarhet.</strong> Om vi äter växtmat direkt tar vi till vara mer av den energi växterna har fångat. När djur föds upp på foder går en stor del av energin förlorad på vägen. Därför kan samma åkermark föda fler människor om en större del av maten är växtbaserad."
      ],
      bild: "bilder/ekologi-pyramid.png",
      bildText: "Bild 4.4 En energipyramid. Bara ungefär en tiondel av energin förs vidare till nästa nivå.",
      kontrollfraga: "Ge två förklaringar till varför energi försvinner mellan nivåerna. Varför finns det färre rovdjur än växtätare i en skog?",
      kontrollsvar: "Organismerna använder energi för att leva och det mesta blir värme, och allt äts inte upp eller tas inte upp i kroppen. Det finns färre rovdjur eftersom det finns mindre energi kvar för varje nivå uppåt i näringskedjan."
    },
    {
      ikon: "♻️",
      titel: "Materien går i kretslopp",
      text: [
        "Samma kolatomer, kväveatomer och vattenmolekyler används om och om igen. Atomerna i din kropp har en gång funnits i växter, djur, luft och hav.",
        "<strong>Kolets kretslopp</strong><br>1. <strong>Fotosyntes:</strong> växter tar upp koldioxid från luften och bygger in kolet i glukos.<br>2. <strong>Näringskedjan:</strong> kolet förs vidare till djur som äter växterna.<br>3. <strong>Cellandning:</strong> växter och djur släpper ut koldioxid när de använder glukosen.<br>4. <strong>Nedbrytning:</strong> när organismer dör bryter nedbrytarna ner dem. Då frigörs koldioxid och näringsämnen.<br>5. <strong>Förbränning:</strong> kol som har legat lagrat i miljontals år som olja, kol och naturgas släpps ut när människan bränner det.<br>6. <strong>Havet:</strong> koldioxid löser sig också i havsvatten, och växtplankton och alger tar upp den i fotosyntesen. Havet tar upp och släpper ut koldioxid hela tiden.",
        RUTA("fakta", "Klimatet", "När vi bränner fossila bränslen släpper vi ut mer koldioxid än växterna och haven hinner ta upp. Halten i luften ökar och förstärker växthuseffekten. Därför blir jorden varmare."),
        RUTA("fakta", "Även kväve", "Växter behöver kväve för att bygga proteiner. Nedbrytarna frigör kväve ur döda organismer, och vissa bakterier kan ta kväve direkt från luften.")
      ],
      bild: "bilder/ekologi-kol.png",
      bildText: "Bild 4.5 Kolets kretslopp, förenklat. Pilarna visar hur kol rör sig mellan luften, levande organismer och marken.",
      kontrollfraga: "Beskriv två processer som tar kol från luften och två som släpper ut kol till luften.",
      kontrollsvar: "Tar kol från luften: fotosyntes och havets upptag av koldioxid. Släpper ut kol: cellandning och förbränning (och nedbrytning)."
    },
    {
      ikon: "🍵",
      titel: "Undersök: var bryts det ner snabbast?",
      text: [
        "Nedbrytarna arbetar i det tysta, men deras arbete går att mäta. I den här undersökningen gräver du ner tepåsar och väger hur mycket som har brutits ner efter några veckor. Metoden används även av riktiga forskare runt om i världen för att jämföra nedbrytning i olika jordar.",
        "<strong>Frågeställning:</strong> I vilken jord bryts organiskt material ner snabbast?<br><strong>Hypotes:</strong> Skriv vad du tror och motivera med det du vet om nedbrytare.<br><strong>Material:</strong> tepåsar med grönt te eller rooibos (utan snöre av plast), våg, spritpenna, glasspinnar som markörer, spade, tre olika platser eller krukor med olika jord.",
        "<strong>Gör så här</strong><br>1. Märk och väg varje tepåse. Skriv upp vikten.<br>2. Gräv ner tre påsar på varje plats, 8 cm djupt. Märk platsen.<br>3. Vänta 4–8 veckor. (I kruka inomhus: håll jorden fuktig.)<br>4. Gräv upp påsarna, borsta av jorden och låt dem torka ett dygn.<br>5. Väg igen och räkna ut hur många procent som har försvunnit.",
        "<strong>Variabler.</strong> Oberoende: typ av jord. Beroende: hur mycket av teet som har brutits ner. Kontrollerade: samma sorts te, samma djup, samma tid.",
        RUTA("tank", "Utvärdera", "Var gick nedbrytningen snabbast? Vilka abiotiska faktorer kan förklara skillnaden – fukt, temperatur, syre? Varför ska man ha tre påsar på varje plats?")
      ],
      bild: "bilder/ekologi-tepasar.png",
      bildText: "Bild 4.10 Tepåsar nedgrävda i tre olika jordar."
    }
  ],
  begrepp: [
    { term: "Energipyramid", forklaring: "En bild som visar att bara omkring 10 procent av energin förs vidare till nästa nivå." },
    { term: "Kretslopp", forklaring: "Materia, till exempel kol, som används om och om igen mellan luft, organismer och mark." },
    { term: "Fossila bränslen", forklaring: "Olja, kol och naturgas, som har legat lagrade i miljontals år." }
  ],
  exitTicket: [
    { fraga: "Vad är skillnaden mellan hur energi och materia rör sig i ett ekosystem?", svar: "Energin flödar igenom: in som solljus och ut som värme. Materien, till exempel kol, går i kretslopp och används om och om igen." },
    { fraga: "Varför är nedbrytarna så viktiga för växterna?", svar: "De bryter ner döda organismer och frigör näringsämnen som växterna kan ta upp och använda igen." }
  ]
};

// ---------- 4.6: Population och resurser ----------
innehall["biologi-ekologi-population-resurser"] = {
  intro: "Om en population har gott om mat, plats och inga fiender kan den växa snabbt. Men ingen population kan växa hur länge som helst. Förr eller senare tar någon resurs slut – mat, vatten, boplatser eller ljus. Det finns alltid något som begränsar hur stor en population kan bli.",
  sektioner: [
    {
      ikon: "📈",
      titel: "Vad påverkar populationens storlek?",
      text: [
        "<strong>Tillgång på föda och vatten:</strong> mer mat ger fler ungar som överlever.<br><strong>Rovdjur:</strong> många rovdjur håller nere antalet bytesdjur.<br><strong>Konkurrens:</strong> arter som behöver samma resurs tävlar om den.<br><strong>Sjukdomar och parasiter:</strong> sprids lättare när det är trångt.<br><strong>Abiotiska faktorer:</strong> en kall vår eller en torr sommar kan slå ut många individer."
      ],
      kontrollfraga: "Ge tre faktorer som kan begränsa hur stor en population blir.",
      kontrollsvar: "Till exempel tillgång på föda och vatten, rovdjur, konkurrens, sjukdomar och parasiter, eller abiotiska faktorer som en kall vår."
    },
    {
      ikon: "🐭",
      titel: "Lämmelår",
      text: [
        "I fjällen varierar antalet lämlar kraftigt. Vissa år blir de enormt många, ett lämmelår, och sedan kraschar populationen. Fjällräven, som lever mest av lämlar, får många valpar under lämmelår och nästan inga under år med lite mat. Därför ökar antalet fjällrävar efter ett lämmelår. Rovdjurens antal följer alltså bytesdjurens, med en liten fördröjning."
      ],
      bild: "bilder/ekologi-lamlar.png",
      bildText: "Bild 4.6 Antalet lämlar och fjällrävar varierar i cykler. Kurvorna är förenklade (ingen skala på y-axeln).",
      kontrollfraga: "Titta på bilden. Varför kommer topparna för fjällrävarna lite efter topparna för lämlarna?",
      kontrollsvar: "Fjällrävarna behöver först mycket mat för att få många ungar som överlever. När lämlarna har blivit många dröjer det en tid innan rävarna hinner bli fler."
    }
  ],
  begrepp: [
    { term: "Begränsande faktor", forklaring: "Något, till exempel mat, plats eller rovdjur, som begränsar hur stor en population kan bli." }
  ],
  exitTicket: [
    { fraga: "Varför kan en population inte växa hur länge som helst?", svar: "Förr eller senare tar någon resurs slut, till exempel mat, vatten, boplatser eller ljus, eller så begränsar rovdjur och sjukdomar antalet." }
  ]
};

// ---------- 4.6 (delvis): Liv i samspel ----------
innehall["biologi-ekologi-liv-i-samspel"] = {
  intro: "Arter samspelar med varandra på olika sätt. Ibland tjänar en art på bekostnad av en annan, ibland förlorar båda lite, och ibland tjänar båda på samarbetet.",
  sektioner: [
    {
      ikon: "🤝",
      titel: "Samspel mellan arter",
      text: [
        "<strong>Rovdjur och byte:</strong> rovdjuret tjänar, bytet förlorar. Lodjur och skogshare är ett exempel.",
        "<strong>Konkurrens:</strong> båda förlorar lite. Rödräv och fjällräv konkurrerar om både mat och lyor.",
        "<strong>Symbios:</strong> båda tjänar på samarbetet. En lav är en svamp och en alg som lever tillsammans: algen gör fotosyntes, svampen skyddar och håller kvar vatten."
      ],
      kontrollfraga: "Vilken sorts samspel är en lav, och vad får svampen och algen ut av det?",
      kontrollsvar: "Symbios. Algen gör fotosyntes och ger näring, och svampen skyddar algen och håller kvar vatten. Båda tjänar på samarbetet."
    }
  ],
  begrepp: [
    { term: "Konkurrens", forklaring: "När arter som behöver samma resurs tävlar om den." },
    { term: "Symbios", forklaring: "Samarbete där båda arterna tjänar på det." }
  ],
  exitTicket: [
    { fraga: "Rödräv och fjällräv konkurrerar om mat och lyor. Vem tjänar på det?", svar: "Ingen. Båda förlorar lite i en konkurrens." }
  ]
};

// ---------- 4.7: Ekosystems känslighet ----------
innehall["biologi-ekologi-systems-kanslighet"] = {
  intro: "Människan är en del av ekosystemen och påverkar dem mer än någon annan art. Två tydliga exempel från Östersjön visar hur kunskap om näringskedjor och kretslopp hjälper oss att förstå miljöproblem.",
  sektioner: [
    {
      ikon: "☠️",
      titel: "Miljögifter anrikas i näringskedjan",
      text: [
        "Vissa gifter, till exempel DDT och PCB, bryts ner mycket långsamt och lagras i djurens fett. När en mört äter tusentals plankton samlas giftet från alla planktonen i mörtens kropp. När gäddan äter många mörtar blir halten ännu högre. Det kallas <strong>anrikning</strong>. Toppkonsumenterna drabbas därför hårdast.",
        "<strong>Exempel: havsörnen.</strong> På 1960- och 70-talen var havsörnen nära att försvinna från Sverige. Gifterna gjorde att äggskalen blev tunna och att ungarna dog. I början av 1970-talet lyckades bara ungefär var femte häckning längs östkusten. Gifterna förbjöds, och Naturskyddsföreningen lade ut giftfri mat. I dag finns det flera tusen havsörnar i Sverige, och arten är inte längre rödlistad."
      ],
      bild: "bilder/ekologi-anrikning.png",
      bildText: "Bild 4.7 Hur ett miljögift anrikas. Varje mört äter många plankton, och varje gädda äter många mörtar. Ju högre upp i kedjan, desto högre halt i varje individ.",
      kontrollfraga: "Varför drabbas toppkonsumenter hårdast av miljögifter?",
      kontrollsvar: "Giftet bryts ner långsamt och lagras i fettet. Eftersom varje led äter många individer från ledet under blir halten högre och högre uppåt i näringskedjan, och toppkonsumenterna får de högsta halterna."
    },
    {
      ikon: "🌊",
      titel: "Övergödning",
      text: [
        "Kväve och fosfor från jordbruk, avlopp och trafik rinner ut i sjöar och hav. Där fungerar de som gödning. Algerna växer explosionsartat (algblomning), och när de dör sjunker de till botten. Nedbrytarna som bryter ner dem förbrukar syret. I delar av Östersjön har bottnarna blivit så syrefattiga att nästan inget kan leva där."
      ],
      bild: "bilder/ekologi-overgodning.png",
      bildText: "Bild 4.8 Övergödning steg för steg: näring läcker ut, alger växer, algerna dör och sjunker, nedbrytare använder syre, syrebrist.",
      kontrollfraga: "Förklara kort hur övergödning kan leda till syrebrist.",
      kontrollsvar: "Näring från åkrar och avlopp gör att algerna växer kraftigt. När algerna dör sjunker de, och nedbrytarna som bryter ner dem förbrukar syret i bottenvattnet, så det blir syrebrist."
    }
  ],
  begrepp: [
    { term: "Anrikning", forklaring: "När ett gift samlas i allt högre halter högre upp i näringskedjan." },
    { term: "Övergödning", forklaring: "När för mycket näringsämnen hamnar i sjöar och hav." }
  ],
  exitTicket: [
    { fraga: "Vilka två ämnen från jordbruk och avlopp orsakar övergödning?", svar: "Kväve och fosfor." }
  ]
};

// ---------- 4.9: Hållbar utveckling (ny; finns ännu inte i häftet) ----------
// Lgr22 biologi 7–9, Natur och miljö: "Människans påverkan på naturen lokalt och globalt samt hur man
// på individ- och samhällsnivå kan främja hållbar utveckling." och "Betydelsen av biologisk mångfald och ekosystemtjänster."
innehall["biologi-ekologi-hallbar-utveckling"] = {
  intro: "Vi lever av naturen: mat, vatten, virke och luft att andas. Men om vi använder naturen för hårt kan den inte ge oss lika mycket i framtiden. Hållbar utveckling handlar om hur vi kan leva bra nu utan att förstöra möjligheterna för dem som kommer efter oss.",
  sektioner: [
    {
      ikon: "🌍",
      titel: "Vad är hållbar utveckling?",
      text: [
        "<strong>Hållbar utveckling</strong> betyder att vi tillgodoser dagens behov utan att ta ifrån kommande generationer möjligheten att tillgodose sina. Så beskrevs det i en rapport från FN år 1987. År 2015 enades världens länder om 17 globala mål för hållbar utveckling, <strong>Agenda 2030</strong>.",
        "Hållbar utveckling har tre delar som hänger ihop: <strong>miljön</strong> (naturen och klimatet), <strong>samhället</strong> (till exempel hälsa, utbildning och rättvisa) och <strong>ekonomin</strong> (jobb och pengar). I biologin tittar vi mest på den första delen, men de påverkar varandra.",
        "Det du har lärt dig i det här kapitlet visar varför. Energin flödar bara genom ekosystemet, så vi är beroende av solen. Materien går i kretslopp, så när vi släpper ut mer koldioxid än naturen hinner ta upp förändras klimatet. Och när en art försvinner kan det påverka hela näringsväven."
      ],
      kontrollfraga: "Förklara med egna ord vad hållbar utveckling betyder.",
      kontrollsvar: "Att vi använder naturen och resurserna så att vi klarar våra behov nu, men så att framtida generationer också kan klara sina. Naturen ska inte förstöras eller användas upp."
    },
    {
      ikon: "🐝",
      titel: "Ekosystemtjänster – naturens gratis hjälp",
      text: [
        "<strong>Ekosystemtjänster</strong> är det naturen gör för oss. Friska ekosystem med stor biologisk mångfald ger oss många tjänster:<br><strong>Mat och material:</strong> fisk, bär, virke.<br><strong>Pollinering:</strong> humlor och bin gör att många grödor ger skörd.<br><strong>Rent vatten och ren luft:</strong> skogar och våtmarker renar vatten, och växter tar upp koldioxid.<br><strong>Jordens näring:</strong> nedbrytare ger växterna näring.<br><strong>Hälsa och naturupplevelser:</strong> många mår bra av att vara ute i skogen eller vid vattnet.",
        "Om mångfalden minskar kan tjänsterna bli sämre. Därför hänger biologisk mångfald och hållbar utveckling ihop."
      ],
      kontrollfraga: "Ge två exempel på ekosystemtjänster och förklara hur de hjälper oss.",
      kontrollsvar: "Till exempel pollinering (bin och humlor ger skörd av bär och grödor) och rent vatten (skogar och våtmarker renar vattnet). Även mat, virke och naturupplevelser räknas."
    },
    {
      ikon: "🙋",
      titel: "Vad kan jag göra?",
      text: [
        "Hållbar utveckling är inte bara något politiker bestämmer. Det du gör varje dag spelar också roll, särskilt när många gör likadant.",
        "<strong>Mat:</strong> släng mindre mat. Att äta mer växtbaserad mat sparar energi, eftersom en stor del av energin går förlorad i varje led när djur föds upp på foder (som du läste i 4.4).<br><strong>Prylar:</strong> laga, byt och köp begagnat i stället för att alltid köpa nytt.<br><strong>Resor:</strong> gå, cykla eller åk kollektivt när du kan. Det minskar utsläppen av koldioxid.<br><strong>Natur:</strong> släng aldrig skräp i naturen och plantera aldrig ut trädgårdsväxter där. Låt en bit gräsmatta bli äng, så får bin och fjärilar mat.",
        RUTA("tank", "Tänk efter", "Vilken av sakerna ovan skulle du själv kunna göra? Vad skulle göra det svårt för dig, och hur skulle ni kunna hjälpa varandra?")
      ],
      kontrollfraga: "Ge två saker du själv kan göra för en mer hållbar framtid och förklara varför de hjälper.",
      kontrollsvar: "Till exempel slänga mindre mat (så sparas resurserna som krävdes för att odla och transportera den) och åka kollektivt eller cykla (så minskar utsläppen av koldioxid)."
    },
    {
      ikon: "🏛️",
      titel: "Vad kan samhället göra?",
      text: [
        "Vissa saker kan en enskild person inte lösa. Då behövs gemensamma beslut:<br><strong>Lagar och regler:</strong> till exempel förbud mot miljögifter som DDT (som du läste om i 4.7), regler för hur mycket kväve och fosfor som får släppas ut och för hur mycket fisk som får fiskas.<br><strong>Skyddad natur:</strong> nationalparker och naturreservat. År 2022 enades världens länder om att skydda 30 procent av jordens land, sötvatten och hav till år 2030.<br><strong>Energi:</strong> att ersätta olja, kol och naturgas med energi som inte ger lika mycket koldioxid, till exempel vind, sol och vatten.<br><strong>Kretslopp:</strong> återvinning, och att göra produkter som håller längre och går att laga.<br><strong>Forskning och utbildning:</strong> kunskap om hur ekosystemen fungerar hjälper oss att fatta bättre beslut.",
        RUTA("tank", "Avvägningar", "Det är sällan enkelt. Skogsbruk ger jobb och virke, men kalhyggen påverkar många arter. Vindkraft minskar utsläppen, men kan störa fåglar och renar. Hur kan man väga olika intressen mot varandra? Vems röst behöver höras?")
      ],
      kontrollfraga: "Ge ett exempel på något som samhället kan göra men en enskild person inte kan.",
      kontrollsvar: "Till exempel besluta om lagar och förbud (som förbudet mot DDT), skydda natur genom nationalparker och naturreservat, eller bygga ut energi som inte ger lika mycket koldioxid."
    }
  ],
  begrepp: [
    { term: "Hållbar utveckling", forklaring: "Att tillgodose dagens behov utan att ta ifrån framtida generationer möjligheten att tillgodose sina." },
    { term: "Agenda 2030", forklaring: "Världens länders 17 globala mål för hållbar utveckling, antagna 2015." },
    { term: "Ekosystemtjänst", forklaring: "Något naturen gör för oss, till exempel pollinering, rent vatten eller mat." }
  ],
  exitTicket: [
    { fraga: "Vilka tre delar hänger ihop i hållbar utveckling?", svar: "Miljön, samhället och ekonomin." },
    { fraga: "Varför minskar mer växtbaserad mat belastningen på miljön?", svar: "När djur föds upp på foder går en stor del av energin förlorad i varje led. Växtmat direkt tar bättre vara på energin som växterna fångat." }
  ]
};

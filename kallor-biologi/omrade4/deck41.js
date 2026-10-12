const { build } = require("./mkpptx.js");
build({
  out: "/tmp/bio/out/biologi-4-1-ekosystem-och-energi.pptx",
  title: "Ekosystem och energi", kicker: "BIOLOGI · KAPITEL 4 · EKOLOGI", sub: "Delområde 4.1: ekosystem, näringsvävar, energiflöde och biomassa",
  lessons: "Start: Vad är ekologi? · Vad är ett ekosystem? · Producenter, konsumenter och näringsvävar · Energiflöde och biomassa · Labb 4.1",
  foot: "Biologi · Kapitel 4 · Delområde 4.1 Ekosystem och energi",
  titleNotes: "Presentationen följer grundtexten i kapitel 4, delområde 4.1. Några bilder per moment. Anteckningarna innehåller handledning.",
  async slides(h) {
    const A = "Vad är ekologi?";
    h.section(A, "Start: ekologins nivåer", "Fråga: Vad åt du till lunch i dag? Följ maten bakåt ända till solen. Hur många steg blev det?");
    h.cards(A, "Ekologi och dess nivåer", [["Individ", "En enda organism, till exempel en hare."], ["Population", "Alla individer av en art inom ett område."], ["Samhälle", "Alla populationer av olika arter i området."], ["Ekosystem", "Samhället och den livlösa miljön."]], { h: 3.4, note: "Biosfären är alla ekosystem på jorden tillsammans.", notes: "Ekologi kommer från grekiskans oikos, hus. Låt eleverna placera skolgården på nivåerna." });
    h.kolla(A, "Kolla dig själv: Start", ["Vad betyder ordet ekologi?", "Vad är skillnaden mellan en population och ett samhälle?", "Ge ett exempel på ett litet och ett stort ekosystem."]);

    const B = "Vad är ett ekosystem?";
    h.section(B, "Biotiska och abiotiska faktorer", "Vanligt fel: eleverna räknar bara djuren som ekosystemet. Betona den livlösa miljön.");
    h.cards(B, "Två sorters faktorer", [["Biotiska faktorer", "Påverkan från andra levande organismer: föda, rovdjur, konkurrenter, sjukdomar."], ["Abiotiska faktorer", "Påverkan från den livlösa miljön: temperatur, ljus, vatten, näring och vind."]], { h: 3.2, note: "Livsmiljö = platsen där arten lever. Biotop = typ av livsmiljö.", notes: "Ge exempel för en gädda och en fjällräv." });
    h.table(B, "Ekosystem ser olika ut men fungerar likadant", ["", "Barrskog i Norrbotten", "Bottenviken", "Tropisk regnskog"], [["Klimat", "Kalla vintrar", "Kallt bräckt vatten", "Varmt och regnigt"], ["Producenter", "Tall, gran, bärris", "Växtplankton, alger", "Höga lövträd"], ["Konsumenter", "Älg, lodjur, tjäder", "Sik, gädda, säl", "Apor, ormar, jaguar"]], { colW: [2.4, 3.3, 3.2, 3.23], fs: 20, rowH: 0.8, note: "Samma principer: producenter, konsumenter, nedbrytare och kretslopp.", notes: "Jämför två ekosystem: en skillnad och en likhet." });
    h.kolla(B, "Kolla dig själv", ["Ge två biotiska och två abiotiska faktorer som påverkar en gädda.", "Varför räknas vattnet och solljuset till ekosystemet?", "Välj två ekosystem. Beskriv en skillnad och en likhet."]);

    const C = "Producenter, konsumenter och näringsvävar";
    h.section(C, "Vem äter vem?", "Rita en näringskedja på tavlan tillsammans. Pilen pekar mot den som äter.");
    await h.imgText(C, "Tre grupper i ekosystemet", ["Producenter gör egen näring med fotosyntes.", "Konsumenter äter andra organismer.", "Nedbrytare bryter ner döda växter och djur.", "Detritusätare hackar sönder dött material."], "l_tre.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "Svampar och bakterier är nedbrytare. Daggmaskar och gråsuggor är detritusätare." });
    await h.imgText(C, "Näringskedja", ["Varje steg är ett led.", "Pilen pekar mot den som äter, åt samma håll som energin.", "Först i kedjan står alltid en producent.", "Högst upp: toppkonsument."], "ekologi-kedja.png", { iw: 6.6, imgLeft: false, fs: 22, notes: "Vanligt fel: pilen ritas åt fel håll." });
    await h.imgText(C, "Näringsväv och kaskadeffekt", ["Flera kedjor som hänger ihop.", "Tar man bort en art påverkas många.", "En förändring som sprider sig genom flera led kallas kaskadeffekt.", "Fler kopplingar ger ett stabilare ekosystem."], "ekologi-vav.png", { iw: 6.6, imgLeft: false, fs: 22, notes: "Yellowstone och vargarna är ett känt men omdiskuterat exempel på kaskadeffekt." });
    h.kolla(C, "Kolla dig själv", ["Varför står alltid en producent först i en näringskedja?", "Vad skulle hända i en skog om alla nedbrytare försvann?", "Förklara varför en näringsväv visar mer än en näringskedja."]);

    const D = "Energiflöde och biomassa";
    h.section(D, "Vart tar energin vägen?", "Solen är källan. Energin flödar genom ekosystemet och försvinner som värme.");
    await h.imgText(D, "Energin minskar för varje led", ["Nästan all energi kommer från solen.", "Bara cirka 10 procent förs vidare.", "Resten blir värme eller hamnar hos nedbrytare.", "Därför är näringskedjor korta."], "ekologi-pyramid.png", { iw: 6.4, imgLeft: false, fs: 22, notes: "10 procent är ett genomsnitt, ofta 5–20 procent." });
    h.stat(D, "Biomassa", "10 %", "av energin förs vidare till nästa led", ["Biomassa är vikten av levande organismer, ofta torrvikt.", "Den minskar oftast uppåt i kedjan.", "Därför finns det fler harar än lodjur.", "Växtbaserad mat tar vara på mer av energin."], { notes: "Fördjupning: i öppet hav kan biomassan vid ett visst tillfälle vara omvänd, eftersom växtplankton omsätts snabbt." });
    h.kolla(D, "Kolla dig själv", ["Varifrån kommer nästan all energi?", "Ge två förklaringar till varför energi försvinner mellan leden.", "Varför finns det färre rovdjur än växtätare?", "Vad menas med biomassa?"]);

    const E = "Labb 4.1 Energi i en näringskedja";
    h.section(E, "Modellspel med ris och skålar", "Material: 1 000 g ris, våg, fem skålar. Förväntat: 1 000, 100, 10 och 1 g. Vanligt fel: procent och gram blandas ihop.");
    h.table(E, "Resultat vid 10 % och 20 %", ["Led", "Ris (g) vid 10 %", "Ris (g) vid 20 %"], [["Producent", "1 000", "1 000"], ["Växtätare", "100", "200"], ["Rovdjur", "10", "40"], ["Toppkonsument", "1", "8"]], { colW: [4.5, 3.8, 3.83], fs: 22, rowH: 0.8, note: "Hur många procent av producenternas energi når toppkonsumenten? Vad förenklar modellen?", notes: "Svar: 0,1 procent respektive 0,8 procent. Modellen förenklar: djur äter flera sorters föda, procenttalet varierar." });
  }
}).catch(e => { console.error(e); process.exit(1); });

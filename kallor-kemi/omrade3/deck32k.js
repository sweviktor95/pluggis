const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-3-2-periodiska-systemet.pptx",
  title: "Periodiska systemet", kicker: "KEMI · KAPITEL 3 · ATOMER OCH GRUNDÄMNEN", sub: "Delområde 3.2: grundämnen, metaller och icke-metaller, grupper, förekomst, labb: metaller och icke-metaller",
  lessons: "Grundämnen och periodiska systemet · Grupper med släktskap · Grundämnen i naturen och kroppen · Labb 3.2",
  foot: "Kemi · Kapitel 3 · Delområde 3.2 Periodiska systemet",
  titleNotes: "Presentationen följer grundtexten i kapitel 3, delområde 3.2. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Grundämnen och periodiska systemet", B = "Grupper med släktskap", Cc = "Grundämnen i naturen och kroppen", D = "Labb 3.2 Metaller och icke-metaller";
    h.section(A, "Grundämnen och periodiska systemet", "Fråga: varför tror ni att ämnena står just där de gör? Samla gissningar.");
    await h.imgText(A, "Det periodiska systemet", ["118 erkända grundämnen.", "Ordnade efter stigande atomnummer.", "Rader: perioder. Kolumner: grupper.", "Blå metaller, gröna icke-metaller, gula halvmetaller."], "v_pse.png", { iw: 8.4, imgLeft: false, fs: 20, notes: "Låt eleverna hitta sitt favoritämne och säga period och grupp." });
    h.table(A, "Metaller och icke-metaller", ["", "Metaller", "Icke-metaller"], [["Leder värme och el", "Bra", "Dåligt"], ["Utseende", "Glänsande", "Matta"], ["Att forma", "Går att böja och hamra", "Fasta är spröda"], ["Tillstånd", "Fasta (utom kvicksilver)", "Många är gaser"]], { colW: [3.6, 4.3, 4.3], note: "Halvmetaller ligger mellan, t.ex. kisel. Undantag: grafit leder el trots att kol är en icke-metall." });
    h.cards(A, "Hur systemet växte fram", [["1869", "Mendelejev ordnar ämnena efter atommassa och egenskaper."], ["Luckor", "Han lämnar tomma platser och förutsäger egenskaper."], ["Idag", "Systemet ordnas efter atomnummer."]], { h: 3.2 });
    h.kolla(A, "Kolla dig själv", ["Hur är systemet ordnat?", "Vad kallas rader och kolumner?", "Nämn tre egenskaper hos metaller."]);

    h.section(B, "Grupper med släktskap", "Fråga: varför liknar ämnen i samma kolumn varandra? Svaret finns i elektronerna.");
    await h.imgText(B, "Valenselektroner", ["Elektronerna i yttersta skalet avgör hur ämnet reagerar.", "Natrium: 2, 8, 1 (grupp 1).", "Klor: 2, 8, 7 (grupp 17).", "Neon: 2, 8 (grupp 18)."], "v_skal.png", { iw: 8.6, imgLeft: false, fs: 21, notes: "Skalmodellen 2, 8, 8 är en förenkling för de första grundämnena." });
    h.table(B, "Tre grupper", ["Grupp", "Namn", "Egenskaper"], [["1", "Alkalimetaller", "Mjuka, reagerar kraftigt med vatten, reaktiviteten ökar nedåt"], ["17", "Halogener", "Reaktiva icke-metaller, klor grön gas, brom rödbrun vätska, jod fast"], ["18", "Ädelgaser", "Fullt yttersta skal, mycket oreaktiva"]], { colW: [1.8, 3.2, 7.2], note: "Alkalimetallers reaktion med vatten visas bara som lärardemo eller film." });
    h.kolla(B, "Kolla dig själv", ["Vad är valenselektroner?", "Varför liknar ämnen i samma grupp varandra?", "Varför är ädelgaserna oreaktiva?"]);

    h.section(Cc, "Grundämnen i naturen och kroppen", "Fråga: vilka grundämnen tror ni att kroppen mest består av?");
    await h.imgText(Cc, "Vanligaste grundämnena", ["Jordskorpan: syre ca 47 %, kisel ca 28 %.", "Kroppen: syre, kol, väte och kväve.", "Siffrorna för kroppen skiljer mellan källor."], "v_forekomst.png", { iw: 8.6, imgLeft: false, fs: 22, notes: "Betona att kroppens siffror är ungefärliga." });
    h.kolla(Cc, "Kolla dig själv", ["Vilka två grundämnen är vanligast i jordskorpan?", "Vilka är vanligast i kroppen?", "Nämn ett grundämne i vardagen och dess användning."]);

    h.section(D, "Labb 3.2: metaller och icke-metaller", "Material: batteri (högst 4,5 V), lampa, sladdar, prover, skyddsglasögon. Förväntat: koppar, aluminium, järn och zink leder el, svavel inte, grafit leder.");
    await h.imgText(D, "Gör så här", ["Titta: glänser provet?", "Koppla in i kretsen: lyser lampan?", "Pröva om provet är sprött eller böjbart.", "Sortera och jämför med periodiska systemet."], "v_labb2.png", { iw: 5.8, imgLeft: false, fs: 21, notes: "Säkerhet: bara lågspänning, ingen kortslutning, skyddsglasögon." });
    h.table(D, "Frågor att svara på", ["Fråga", "Tips"], [["Vilka prover var metaller?", "Gemensamma egenskaper."], ["Passade något inte?", "Grafit är ett undantag."], ["Räcker en egenskap?", "Jämför flera."]], { colW: [6, 6.2] });
  }
}).catch(e => { console.error(e); process.exit(1); });

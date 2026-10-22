const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-3-0-introduktion-till-atomer.pptx",
  title: "Introduktion till atomer", kicker: "KEMI · KAPITEL 3 · ATOMER OCH GRUNDÄMNEN", sub: "Start: vad är en atom och vad är ett grundämne?",
  lessons: "Vad är en atom? · Hur liten är en atom? · Vad ingår i kapitlet?",
  foot: "Kemi · Kapitel 3 · Start Vad är en atom?",
  titleNotes: "Presentationen följer grundtexten i kapitel 3, Start. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Vad är en atom?";
    h.section(A, "Allt består av atomer", "Fråga: om du delar en guldbit om och om igen, hur slutar det? Låt eleverna skriva en gissning och spara den till slutet av kapitlet.");
    await h.imgText(A, "Från metallbit till atom", ["Allt är gjort av atomer.", "Atomer av samma sort bildar ett grundämne.", "En atom har en kärna med elektroner runt omkring.", "Bilderna är schematiska, inte skalenliga."], "v_oversikt.png", { iw: 8.2, imgLeft: false, fs: 22, notes: "Gå igenom stegen från metallbit till atomkärna. Betona att bilden är en förenkling." });
    h.cards(A, "Hur liten är en atom?", [["Atomen", "Radie ungefär 0,1 nm, alltså 1 · 10⁻¹⁰ m."], ["Kärnan", "Mindre än en tiotusendel av atomens radie."], ["Bild", "Om atomen vore en fotbollsarena vore kärnan ungefär ett knappnålshuvud. Det är en bild, inte en mätning."]], { h: 3.4, note: "Betona att arenajämförelsen är en analogi. Nästan hela atomen är tom." });
    h.table(A, "Vad ingår i kapitlet?", ["Delområde", "Du lär dig"], [["3.1 Atomens byggnad", "Protoner, neutroner och elektroner, atomnummer och masstal, atommodellernas historia, isotoper och radioaktivitet. Labb: svarta lådan."], ["3.2 Periodiska systemet", "Hur grundämnena är ordnade, metaller och icke-metaller, grupper med släktskap, grundämnen i naturen och kroppen. Labb: metaller och icke-metaller."]], { colW: [4.2, 8] });
    h.kolla(A, "Kolla dig själv", ["Vad är en atom?", "Hur många grundämnen finns det ungefär?", "Hur stor är en atom och hur stor är kärnan i förhållande till den?"]);
  }
}).catch(e => { console.error(e); process.exit(1); });

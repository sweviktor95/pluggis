const { build } = require("./mkpptx.js");
build({
  out: "/tmp/kem/out/kemi-1-0-introduktion-till-kemi.pptx",
  title: "Introduktion till kemi", kicker: "KEMI · KAPITEL 1 · KEMI SOM VETENSKAP", sub: "Start: vad är kemi och hur arbetar en kemist?",
  lessons: "Vad är kemi? · Kemister · Hur kemister arbetar",
  foot: "Kemi · Kapitel 1 · Start Vad är kemi?",
  titleNotes: "Presentationen följer grundtexten i kapitel 1, Start. Några bilder. Anteckningarna innehåller handledning. Allt material är utkast (beta).",
  async slides(h) {
    const A = "Vad är kemi?";
    h.section(A, "Kemi är läran om ämnen", "Fråga: vilka produkter i köket eller badrummet tror ni är ”kemikalier”? Spara svaren, de används i slutet av kapitlet (Granska kemipåståenden).");
    h.cards(A, "Tre grundidéer", [["Ämnen", "Allt är gjort av ämnen: vatten, socker, plast, luft."], ["Förändring", "Ämnen kan lösas upp, rosta, brinna eller blandas."], ["Naturvetenskap", "Kemister undersöker och mäter, de gissar inte."]], { h: 3.4, note: "Allt, från vatten och vetemjöl till kroppen, består av kemikalier (Svenska Kemisamfundet).", notes: "Vanligt fel: att kemi bara finns i labbet." });
    await h.imgText(A, "Många sorters kemister", ["Analytisk kemist: mäter vad ett prov innehåller.", "Läkemedelskemist: tar fram och testar läkemedel.", "Materialkemist: utvecklar material, till exempel batterier.", "Miljökemist: undersöker föroreningar."], "l_kemister.png", { iw: 7.7, imgLeft: false, fs: 20, notes: "Exempel på yrkesroller. Inte källkontrollerat. Be eleverna ge fler exempel." });
    await h.imgText(A, "Hur en kemist arbetar", ["Fråga: vad undrar jag?", "Hypotes: ett prövbart svar.", "Testa: gör en undersökning.", "Slutsats: vad lärde jag mig? Andra kontrollerar och upprepar."], "l_cykel.png", { iw: 6.4, imgLeft: false, notes: "Cykeln återkommer i delområde 1.1 (Från fråga till plan)." });
    h.table(A, "Vad ingår i kapitlet?", ["Delområde", "Du lär dig"], [["1.1 Arbeta som kemist", "Säkerhet, utrustning, fråga och plan, dokumentera och värdera. Labb: brustabletten."], ["1.2 Modeller, källor och argument", "Modeller, kemins historia, källkritik. Labb: fläckborttagaren."]], { colW: [4.6, 7.53], fs: 20, rowH: 1.0, notes: "Kapitlet bygger på att eleverna prövar själva." });
    h.kolla(A, "Kolla dig själv", ["Vad handlar kemi om?", "Nämn tre sorters kemister.", "Varför räcker det inte att bara läsa om kemi?"]);
  }
}).catch(e => { console.error(e); process.exit(1); });
